#!/usr/bin/env python3
"""Check a generated book folder for length, timing and numbering problems.

Usage:
    python check_book.py <path-to-book-folder> [--wpm 140]

Reads 02-illustrations.md and 03-script.md from the folder root and reports:
- spoken words per voice and in total, and the estimated runtime;
- the number of scenes in the script and of scene prompts in the plan;
- scene numbers that appear in one file but not the other;
- scenes whose spoken text is far outside the target length;
- whether the five production subfolders and 05-narrator.md exist;
- whether the final scene invites comments and asks viewers to subscribe and click the bell;
- personal lines still marked [CONFIRM: ...] (narrator-bible.md, truth rules);
- the "Once upon a time" handoff ending the introduction, and the introduction's length
  (about 90 seconds: 200-230 words, never over 240, in 2-3 scenes);
- style warnings from references/spoken-style.md: banned phrases, lists of three,
  "not X, but Y", long narrator sentences and written connectors.

Spoken text is the content of the ```text fences in 03-script.md.
Scene headings in both files look like: "## 05 · Title" or "### 05 · Title".
"""
import re
import sys
from pathlib import Path

HEADING = re.compile(r"^#{2,4}\s+(\d{1,3})\s*[·\-—]\s*(.+)$")
VOICE = re.compile(r"\bVoice\**\s*:\s*\**\s*([A-Za-z]+)", re.IGNORECASE)
PAUSE = re.compile(r"\[(?:long )?pause[^\]]*\]", re.IGNORECASE)
TAG = re.compile(r"\[[^\]]*\]")  # pause markers and audio tags are not spoken words
CONFIRM = re.compile(r"\[CONFIRM:\s*([^\]]*)\]", re.IGNORECASE)  # personal line awaiting the creator
SUBFOLDERS = ["images", "voice", "thumbnails", "music", "videos"]
STYLE_GUIDE = Path(__file__).resolve().parent.parent / "references" / "spoken-style.md"
NOT_BUT = re.compile(
    r"\bnot (?:just |only |merely |even )?[^.!?;\n]{1,60}?\bbut\b"
    r"|\bit'?s not about\b[^.!?]*[.!?]\s+it'?s about\b",
    re.IGNORECASE,
)
_ITEM = r"(?:[\w'-]+\s+){0,3}[\w'-]+"  # list items are short: 1-4 words
# "A, B, and C": short items, and the last one ends at punctuation or the end of the sentence.
TRIAD = re.compile(rf"\b{_ITEM},\s+{_ITEM},?\s+(?:and|or)\s+{_ITEM}(?=\s*(?:[,.;:!?]|$))", re.IGNORECASE)
WRITTEN_CONNECTORS = re.compile(r"\b(however|moreover|furthermore|therefore|thus|nevertheless)\b", re.IGNORECASE)
SENTENCE_END = re.compile(r"(?<=[.!?])\s+|\n+")
LONG_SENTENCE = 25  # words; narrator sentences longer than this are flagged


def parse_scenes(text: str):
    """Return {scene_number: {"title", "voice", "spoken"}} in file order."""
    scenes = {}
    current = None
    in_fence = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            if not in_fence and current is not None and stripped[3:].strip().lower() in ("text", ""):
                in_fence = True
            elif in_fence:
                in_fence = False
            continue
        if in_fence and current is not None:
            scenes[current]["spoken"].append(line)
            continue
        m = HEADING.match(stripped)
        if m:
            current = int(m.group(1))
            scenes[current] = {"title": m.group(2).strip(), "voice": "", "spoken": []}
            continue
        if stripped.startswith("#"):
            current = None  # a non-scene heading (e.g. a character) ends the scene
            continue
        if current is not None:
            v = VOICE.search(stripped)
            if v and not scenes[current]["voice"]:
                scenes[current]["voice"] = v.group(1).strip().upper()
    return scenes


def unwrap_confirm(text):
    """Keep the words of a [CONFIRM: ...] line, since they will be spoken once confirmed."""
    return CONFIRM.sub(lambda m: m.group(1), text)


def word_count(lines):
    return len(TAG.sub(" ", unwrap_confirm(" ".join(lines))).split())


def load_banned_phrases():
    """Phrases listed in section 1 of spoken-style.md, as `- `phrase`` items."""
    if not STYLE_GUIDE.exists():
        return []
    phrases, in_section = [], False
    for line in STYLE_GUIDE.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            in_section = line.startswith("## 1.")
            continue
        m = re.match(r"^- `([^`]+)`\s*$", line.strip())
        if in_section and m:
            phrases.append(m.group(1).lower())
    return phrases


def style_warnings(script):
    """Warnings from spoken-style.md. They are for review, not hard errors."""
    warnings = []
    banned = [(p, re.compile(r"(?<![\w'])" + re.escape(p) + r"(?![\w'])")) for p in load_banned_phrases()]
    not_but_scenes = []
    for num, s in script.items():
        text = TAG.sub(" ", unwrap_confirm("\n".join(s["spoken"]))).replace("’", "'")
        lower = text.lower()
        for phrase, rx in banned:
            if rx.search(lower):
                warnings.append(f"Scene {num:02d}: banned phrase '{phrase}'")
        not_but_scenes += [num] * len(NOT_BUT.findall(text))
        sentences = [x for x in SENTENCE_END.split(text) if x.strip()]
        triads = sum(1 for x in sentences if TRIAD.search(x))
        if triads > 1:
            warnings.append(f"Scene {num:02d}: {triads} possible lists of three (limit 1 per scene)")
        if s["voice"] == "NARRATOR":
            long = [len(x.split()) for x in sentences if len(x.split()) > LONG_SENTENCE]
            if long:
                warnings.append(f"Scene {num:02d}: {len(long)} narrator sentence(s) over {LONG_SENTENCE} words ({', '.join(map(str, long))})")
            connectors = sorted({c.lower() for c in WRITTEN_CONNECTORS.findall(text)})
            if connectors:
                warnings.append(f"Scene {num:02d}: written connector(s) in narrator text: {', '.join(connectors)}")
    if len(not_but_scenes) > 2:
        where = ", ".join(f"{n:02d}" for n in sorted(set(not_but_scenes)))
        warnings.append(f"{len(not_but_scenes)} possible 'not X, but Y' constructions (limit 2 per video) in scenes {where}")
    return warnings


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    wpm = 140
    if "--wpm" in sys.argv:
        wpm = int(sys.argv[sys.argv.index("--wpm") + 1])
        args = [a for a in args if a != str(wpm)]
    if not args:
        print(__doc__)
        return 1
    root = Path(args[0])
    script_path = root / "03-script.md"
    plan_path = root / "02-illustrations.md"
    problems = []

    for name in SUBFOLDERS:
        if not (root / name).is_dir():
            problems.append(f"Missing folder: {name}/")

    if not script_path.exists():
        print(f"Not found: {script_path}")
        return 1
    script = parse_scenes(script_path.read_text(encoding="utf-8"))

    by_voice = {}
    total = 0
    for num, s in script.items():
        words = word_count(s["spoken"])
        s["words"] = words
        total += words
        by_voice[s["voice"] or "UNSET"] = by_voice.get(s["voice"] or "UNSET", 0) + words
        if not s["voice"]:
            problems.append(f"Scene {num:02d}: no Voice line")
        if words == 0:
            problems.append(f"Scene {num:02d}: no spoken text in a ```text fence")
        elif words < 40 or words > 200:
            problems.append(f"Scene {num:02d}: {words} words (expected roughly 60-150)")

    print(f"Script: {len(script)} scenes, {total} spoken words, ~{total / wpm:.1f} min at {wpm} wpm")
    for voice, words in sorted(by_voice.items()):
        print(f"  {voice}: {words} words (~{words / wpm:.1f} min)")
    if not 2800 <= total <= 3500:
        problems.append(f"Total {total} words is outside the 3,000-3,300 target (20-25 min)")

    if script:
        last = max(script)
        final_text = " ".join(script[last]["spoken"]).lower()
        if "subscribe" not in final_text or "bell" not in final_text:
            problems.append(f"Final scene {last:02d}: no direct 'subscribe to the channel and click the bell button' call to action")
        if "comment" not in final_text:
            problems.append(f"Final scene {last:02d}: no invitation to comment")

    # Ritual: "Once upon a time" ends the introduction, just before the first story scene.
    order = sorted(script)
    handoff = [n for n in order if "once upon a time" in " ".join(script[n]["spoken"]).lower()]
    story = [n for n in order if script[n]["voice"] == "STORYTELLER"]
    if not handoff:
        problems.append("No 'Once upon a time...' handoff (channel ritual)")
    elif story:
        before_story = [n for n in order if n < story[0]]
        if before_story and handoff[0] != before_story[-1]:
            problems.append(f"'Once upon a time...' is in scene {handoff[0]:02d}, not in the last introduction scene ({before_story[-1]:02d})")

    # Introduction: everything before the first story scene, about 90 seconds (scenario guide section 5).
    if story:
        intro = [n for n in order if n < story[0]]
        intro_words = sum(script[n]["words"] for n in intro)
        print(f"Introduction: {len(intro)} scene(s), {intro_words} words, ~{intro_words / wpm * 60:.0f} s")
        if intro_words > 240:
            problems.append(f"Introduction is {intro_words} words (~{intro_words / wpm * 60:.0f} s); keep it to 200-230, never over 240")
        elif intro_words < 150:
            problems.append(f"Introduction is only {intro_words} words; check that hook, framing, welcome and logline are all there")
        if not 2 <= len(intro) <= 3:
            problems.append(f"Introduction has {len(intro)} scenes (expected 2-3)")

    for num, s in script.items():
        for m in CONFIRM.finditer("\n".join(s["spoken"])):
            problems.append(f"Scene {num:02d}: unconfirmed personal line, settle before approval: \"{m.group(1).strip()}\"")

    if not (root / "05-narrator.md").exists():
        problems.append("05-narrator.md not found")

    if plan_path.exists():
        plan = parse_scenes(plan_path.read_text(encoding="utf-8"))
        # Only count numbered scene prompts, not character entries.
        plan_nums = set(plan)
        script_nums = set(script)
        print(f"Illustrations: {len(plan_nums)} numbered scene prompts")
        if not 33 <= len(plan_nums) <= 42:
            problems.append(f"{len(plan_nums)} illustrations (expected 35-40)")
        for n in sorted(script_nums - plan_nums):
            problems.append(f"Scene {n:02d} is in the script but has no illustration prompt")
        for n in sorted(plan_nums - script_nums):
            problems.append(f"Illustration {n:02d} has no matching scene in the script")
    else:
        problems.append("02-illustrations.md not found")

    if problems:
        print("\nTo review:")
        for p in problems:
            print(f"  - {p}")
    else:
        print("\nNo problems found.")

    style = style_warnings(script)
    if style:
        print("\nStyle warnings (spoken-style.md; fix, or keep on purpose):")
        for w in style:
            print(f"  - {w}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
