#!/usr/bin/env python3
"""Derive the spoiler-free player-facing world doc from the GM master copy.

meine-welt-gm.md is the single source of truth for the campaign world. Any
heading of the form "## GM: ..." (any heading level) marks a GM-only
section - secrets, unresolved mysteries with a decided answer, production
notes - that must never reach the public doc. This script strips every
such section (heading plus its body, up to but not including the next
heading of the same or shallower level) and writes the remainder to
meine-welt.md.

Usage:
    python3 strip_gm_notes.py <meine-welt-gm.md> <meine-welt.md>

Re-run this after every edit to the GM master file instead of hand-editing
the public file - that's the only way the two stay in sync.
"""
import re
import sys
from pathlib import Path

GM_HEADING = re.compile(r"^(#{2,6})\s+GM:.*$")
ANY_HEADING = re.compile(r"^(#{2,6})\s+.*$")


PUBLIC_TITLE = "# Meine Welt"


def strip_gm_sections(text):
    lines = text.splitlines()
    # Everything before the first "## " heading is GM-file front matter
    # (title, spoiler-warning note) - replace it with a plain public title
    # rather than copying it verbatim.
    first_heading = next(
        (i for i, l in enumerate(lines) if re.match(r"^## ", l)), len(lines)
    )
    lines = [PUBLIC_TITLE, ""] + lines[first_heading:]

    out = []
    skip_until_level = None
    for line in lines:
        m = ANY_HEADING.match(line)
        if skip_until_level is not None:
            if m and len(m.group(1)) <= skip_until_level:
                skip_until_level = None
            else:
                continue
        gm = GM_HEADING.match(line)
        if gm:
            skip_until_level = len(gm.group(1))
            continue
        out.append(line)

    # Collapse runs of 3+ blank lines left behind by removed sections.
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])
    dst.write_text(strip_gm_sections(src.read_text()))
    print(f"wrote {dst}")


if __name__ == "__main__":
    main()
