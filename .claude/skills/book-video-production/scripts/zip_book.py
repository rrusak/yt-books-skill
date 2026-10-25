#!/usr/bin/env python3
"""Zip a book folder, keeping its empty production subfolders.

Usage:
    python zip_book.py <path-to-book-folder> [output.zip]

Ordinary zipping drops empty folders; this adds an explicit entry for every
directory so images/, voice/, thumbnails/, music/ and videos/ survive.
"""
import sys
import zipfile
from pathlib import Path


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    root = Path(sys.argv[1]).resolve()
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else root.with_suffix(".zip")
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr(f"{root.name}/", "")
        for path in sorted(root.rglob("*")):
            arc = f"{root.name}/{path.relative_to(root).as_posix()}"
            if path.is_dir():
                zf.writestr(arc + "/", "")
            else:
                zf.write(path, arc)
    print(out.resolve())
    return 0


if __name__ == "__main__":
    sys.exit(main())
