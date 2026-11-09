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
- whether the final scene invites comments and uses one approved subscribe line (scenario
  guide section 1), different from the previous book's in ../narration-history.md;
- one early soft ask for a like around minutes 3-5, not repeated in the outro;
- personal lines still marked [CONFIRM: ...] (narrator-bible.md, truth rules);
- the "Once upon a time" handoff ending the introduction, and the introduction's length
  (about 90 seconds: 200-230 words, never over 240, in 2-3 scenes);
- the verdict scene just before the outro;
- narrator cut-ins in the story (scenes like 14a): 1-3, 25-45 words each, the first at
  minutes 3-5, 4+ minutes apart, none in the last four story scenes;
- style warnings from references/spoken-style.md: banned phrases, lists of three,
  "not X, but Y", long narrator sentences and written connectors.

Spoken text is the content of the ```text fences in 03-script.md.
Scene headings in both files look like: "## 05 · Title" or "### 05 · Title".
A narrator cut-in after scene 14 is "### 14a · Cut-in: Title" and has no illustration.
"""
import re
import sys
from pathlib import Path

HEADING = re.compile(r"^#{2,4}\s+(\d{1,3})([a-z])?\s*[·\-—]\s*(.+)$")
VOICE = re.compile(r"\bVoice\**\s*:\s*\**\s*([A-Za-z]+)", re.IGNORECASE)
PAUSE = re.compile(r"\[(?:long )?pause[^\]]*\]", re.IGNORECASE)
TAG = re.compile(r"\[[^\]]*\]")  # pause markers and audio tags are not spoken words
CONFIRM = re.compile(r"\[CONFIRM:\s*([^\]]*)\]", re.IGNORECASE)  # personal line awaiting the creator
SUBFOLDERS = ["images", "voice", "thumbnails", "music", "videos"]
STYLE_GUIDE = Path(__file__).resolve().parent.parent / "references" / "spoken-style.md"
SCENARIO_GUIDE = Path(__file__).resolve().parent.parent / "references" / "scenario-guide.md"
LIKE_ASK = re.compile(r"\b(?:a like|leave a like|like button|hit like|tap like|give it a like|giving it a like|hit the like)\b", re.IGNORECASE)
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


class SceneId(tuple):
    """A scene number such as 14, or a narrator cut-in such as 14a (after scene 14).

    Sorts as 14 < 14a < 15 and formats like a number: f"{SceneId(14, 'a'):02d}" == "14a".
    """

    def __new__(cls, number, suffix=""):
        return super().__new__(cls, (int(number), (suffix or "").lower()))

    @property
    def number(self):
        return self[0]

    @property
    def is_cutin(self):
        return bool(self[1])

    def __format__(self, spec):
        return format(self[0], spec or "02d") + self[1]

    def __str__(self):
        return format(self, "02d")

    __repr__ = __str__


def parse_scenes(text: str):
    """Return {SceneId: {"title", "voice", "spoken"}} in file order."""
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
            current = SceneId(m.group(1), m.group(2))
            scenes[current] = {"title": m.group(3).strip(), "voice": "", "spoken": []}
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


def normalise(text):
    """Lower-case spoken text without tags, curly quotes or extra spaces, for comparing lines."""
    text = TAG.sub(" ", unwrap_confirm(text)).replace("’", "'").replace("“", '"').replace("”", '"')
    return " ".join(text.lower().split())


def load_subscribe_lines():
    """Numbered wordings under '#### Approved subscribe lines' in scenario-guide.md."""
    if not SCENARIO_GUIDE.exists():
        return {}
    lines, in_section = {}, False
    for line in SCENARIO_GUIDE.read_text(encoding="utf-8").splitlines():
        if line.startswith("#"):
            in_section = line.strip().lower() == "#### approved subscribe lines"
            continue
        m = re.match(r'^(\d+)\.\s+"(.+)"\s*$', line.strip())
        if in_section and m:
            lines[int(m.group(1))] = normalise(m.group(2))
    return lines


def previous_subscribe_line(history_path, slug):
    """The approved wording number used by the most recent other book in narration-history.md."""
    if not history_path.exists():
        return None, None
    previous = (None, None)
    for entry in re.split(r"^## ", history_path.read_text(encoding="utf-8"), flags=re.MULTILINE)[1:]:
        parts = [p.strip() for p in entry.splitlines()[0].split("·")]
        if len(parts) > 1 and parts[1] == slug:
            continue
        m = re.search(r"^- Subscribe line:\s*(\d+)", entry, re.MULTILINE)
        previous = (parts[0], int(m.group(1)) if m else None)
    return previous


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
        elif num.is_cutin:
            if not 20 <= words <= 50:
                problems.append(f"Cut-in {num:02d}: {words} words (expected 25-45, 10-20 seconds)")
        elif words < 40 or words > 200:
            problems.append(f"Scene {num:02d}: {words} words (expected roughly 60-150)")

    print(f"Script: {len(script)} scenes, {total} spoken words, ~{total / wpm:.1f} min at {wpm} wpm")
    for voice, words in sorted(by_voice.items()):
        print(f"  {voice}: {words} words (~{words / wpm:.1f} min)")
    if not 2800 <= total <= 3500:
        problems.append(f"Total {total} words is outside the 3,000-3,300 target (20-25 min)")

    order = sorted(script)
    start, elapsed = {}, 0
    for n in order:
        start[n] = elapsed
        elapsed += script[n]["words"]

    if script:
        last = max(script)
        final_text = " ".join(script[last]["spoken"]).lower()
        if "subscribe" not in final_text or "bell" not in final_text:
            problems.append(f"Final scene {last:02d}: no direct 'subscribe to the channel and click the bell button' call to action")
        if "comment" not in final_text:
            problems.append(f"Final scene {last:02d}: no invitation to comment")

        # The subscribe line: one approved wording, word for word, not the previous book's.
        approved = load_subscribe_lines()
        final_norm = normalise("\n".join(script[last]["spoken"]))
        used = [k for k, v in approved.items() if v in final_norm]
        if approved and not used:
            problems.append(f"Final scene {last:02d}: the subscribe line is not one of the approved wordings (scenario guide section 1)")
        elif used:
            print(f"Subscribe line: approved wording {used[0]}")
            prev_book, prev_line = previous_subscribe_line(root.resolve().parent / "narration-history.md", root.resolve().name)
            if prev_line == used[0]:
                problems.append(f"Subscribe line {used[0]} is the same as the previous book's ({prev_book}); rotate to another")

        # The early soft ask: one like-ask around minutes 3-5; the outro does not repeat it.
        early = [n for n in order if n != last and LIKE_ASK.search(" ".join(script[n]["spoken"]))]
        if not early:
            problems.append("No early soft ask for a like (around minutes 3-5, usually the first cut-in)")
        else:
            if len(early) > 1:
                problems.append(f"{len(early)} like-asks before the outro ({', '.join(f'{n:02d}' for n in early)}); keep one")
            minute = start[early[0]] / wpm
            if not 2.5 <= minute <= 6:
                problems.append(f"Early soft ask in scene {early[0]:02d} starts at ~{minute:.1f} min (aim for minutes 3-5)")
            if LIKE_ASK.search(final_text):
                problems.append(f"Final scene {last:02d} asks for a like again; it was already asked in scene {early[0]:02d}")

    # Ritual: "Once upon a time" ends the introduction, just before the first story scene.
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

    # Verdict: a narrator scene titled "Verdict…", just before the final scene (scenario guide section 7).
    verdict = [n for n in order if script[n]["title"].lower().startswith("verdict")]
    if not verdict:
        problems.append("No verdict scene (a narrator scene titled 'Verdict: ...' just before the outro)")
    else:
        v = verdict[0]
        if len(order) > 1 and v != order[-2]:
            problems.append(f"Verdict is scene {v:02d}; it should come just before the outro (scene {order[-2]:02d})")
        if script[v]["voice"] != "NARRATOR":
            problems.append(f"Verdict scene {v:02d} should be voiced by the NARRATOR")
        if not 40 <= script[v]["words"] <= 95:
            problems.append(f"Verdict scene {v:02d}: {script[v]['words']} words (expected 50-80)")

    # Narrator cut-ins during the story: scenes like 14a (scenario guide section 6).
    cutins = [n for n in order if n.is_cutin]
    if story:
        story_scenes = [n for n in order if script[n]["voice"] == "STORYTELLER" and not n.is_cutin]
        if not 1 <= len(cutins) <= 3:
            problems.append(f"{len(cutins)} narrator cut-ins in the story (expected 1-3)")
        for i, n in enumerate(cutins):
            if SceneId(n.number) not in script:
                problems.append(f"Cut-in {n:02d} follows no scene {n.number:02d}")
            if script[n]["voice"] != "NARRATOR":
                problems.append(f"Cut-in {n:02d} should be voiced by the NARRATOR")
            if not story_scenes[0] < n < story_scenes[-1]:
                problems.append(f"Cut-in {n:02d} is outside the story")
            elif len(story_scenes) >= 4 and n > story_scenes[-4]:
                problems.append(f"Cut-in {n:02d} is in the last four story scenes (the climax); move it earlier")
            minute = start[n] / wpm
            if i == 0 and not 3 <= minute <= 5.5:
                problems.append(f"First cut-in {n:02d} starts at ~{minute:.1f} min (aim for minutes 3-5)")
            if i > 0:
                gap = (start[n] - start[cutins[i - 1]]) / wpm
                if gap < 4:
                    problems.append(f"Cut-in {n:02d} is only ~{gap:.1f} min after cut-in {cutins[i - 1]:02d} (keep them 4+ min apart)")

    for num, s in script.items():
        for m in CONFIRM.finditer("\n".join(s["spoken"])):
            problems.append(f"Scene {num:02d}: unconfirmed personal line, settle before approval: \"{m.group(1).strip()}\"")

    if not (root / "05-narrator.md").exists():
        problems.append("05-narrator.md not found")

    if plan_path.exists():
        plan = parse_scenes(plan_path.read_text(encoding="utf-8"))
        # Only count numbered scene prompts, not character entries. Cut-ins (14a) hold
        # the previous scene's image, so they have no prompt of their own.
        plan_nums = {n for n in plan if not n.is_cutin}
        script_nums = {n for n in script if not n.is_cutin}
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
