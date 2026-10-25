#!/usr/bin/env python3
"""Check a generated book folder for length, timing and numbering problems.

Usage:
    python check_book.py <path-to-book-folder> [--wpm 140]

Reads 02-illustrations.md and 03-script.md from the folder root and reports:
- spoken words per voice and in total, and the estimated runtime;
- the number of scenes in the script and of scene prompts in the plan;
- scene numbers that appear in one file but not the other;
- scenes whose spoken text is far outside the target length;
- whether the five production subfolders exist.

Spoken text is the content of the ```text fences in 03-script.md.
Scene headings in both files look like: "## 05 · Title" or "### 05 · Title".
"""
import re
import sys
from pathlib import Path

HEADING = re.compile(r"^#{2,4}\s+(\d{1,3})\s*[·\-—]\s*(.+)$")
VOICE = re.compile(r"\bVoice\**\s*:\s*\**\s*([A-Za-z]+)", re.IGNORECASE)
PAUSE = re.compile(r"\[(?:long )?pause[^\]]*\]", re.IGNORECASE)
SUBFOLDERS = ["images", "voice", "thumbnails", "music", "videos"]


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


def word_count(lines):
    return len(PAUSE.sub(" ", " ".join(lines)).split())


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
    return 0


if __name__ == "__main__":
    sys.exit(main())
