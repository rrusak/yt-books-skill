#!/usr/bin/env python3
"""Create the production folder for one book video.

Usage:
    python init_book_folder.py <book-slug> [base-dir]

Creates <base-dir>/<book-slug>/ with the empty production subfolders
images/, voice/, thumbnails/, music/ and videos/. The four main documents
are written by Claude into the root of <book-slug>/ afterwards.
Existing folders and files are left untouched.
"""
import re
import sys
from pathlib import Path

SUBFOLDERS = ["images", "voice", "thumbnails", "music", "videos"]


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    slug = sys.argv[1].strip()
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        print(f"Slug must be lowercase kebab-case (e.g. 'faust', 'the-great-gatsby'), got: {slug!r}")
        return 1
    base = Path(sys.argv[2]) if len(sys.argv) > 2 else Path.cwd()
    root = base / slug
    root.mkdir(parents=True, exist_ok=True)
    for name in SUBFOLDERS:
        (root / name).mkdir(exist_ok=True)
    print(root.resolve())
    for name in SUBFOLDERS:
        print(f"  {name}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
