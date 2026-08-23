#!/usr/bin/env python3
"""Render a FoundryVTT "Ironsmith" oracle compendium (json-packs/<pack>/*.json)
into per-category Markdown reference files, mirroring what
build_reference_markdown.py does for Datasworn.

Each file in the source pack is either a Folder document (has "sorting" but
no "results") or a RollTable document (has "results"). This script rebuilds
the folder tree, then writes one Markdown file per root-level folder so each
output file stays small enough to read on demand.

Usage:
    python3 build_ironsmith_oracles.py <json-pack-dir> <output_dir>
"""
import glob
import html
import json
import os
import re
import sys
from pathlib import Path


def html_to_text(s):
    if not s:
        return ""
    s = re.sub(r"</p>\s*<p>", "\n\n", s)
    s = re.sub(r"</?p>", "", s)
    s = html.unescape(s)
    return s.strip()


def html_to_cell(s):
    """Flatten to a single line for use inside a Markdown table cell."""
    text = html_to_text(s)
    return re.sub(r"\s+", " ", text)


def slugify(name):
    s = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return s or "misc"


def load_pack(pack_dir):
    folders = {}
    tables = []
    for path in glob.glob(os.path.join(pack_dir, "*.json")):
        d = json.loads(Path(path).read_text())
        if "results" in d:
            tables.append(d)
        elif "sorting" in d:
            folders[d["_id"]] = d
    return folders, tables


def render_table(table, depth):
    heading = "#" * min(depth + 2, 6)
    out = [f"{heading} {table['name']}\n"]
    desc = html_to_text(table.get("description"))
    if desc:
        out.append(f"{desc}\n")
    if table.get("formula"):
        out.append(f"*Dice: {table['formula']}*\n")

    rows = sorted(table.get("results", []), key=lambda r: r.get("range", [0, 0]))
    lines = ["Roll | Result", "---|---"]
    for r in rows:
        lo, hi = r.get("range", [None, None])
        rng = f"{lo}" if lo == hi else f"{lo}-{hi}"
        text = html_to_cell(r.get("description"))
        lines.append(f"{rng} | {text}")
    out.append("\n".join(lines) + "\n")
    return "\n".join(out)


def render_folder(folder_id, folders, tables_by_folder, depth, out):
    folder = folders.get(folder_id)
    if folder and depth > 0:
        heading = "#" * min(depth + 2, 6)
        out.append(f"{heading} {folder['name']}\n")

    for table in sorted(tables_by_folder.get(folder_id, []), key=lambda t: t.get("sort", 0)):
        out.append(render_table(table, depth))

    children = [f for f in folders.values() if f.get("folder") == folder_id]
    children.sort(key=lambda f: f.get("sort", 0))
    for child in children:
        render_folder(child["_id"], folders, tables_by_folder, depth + 1, out)


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    pack_dir = sys.argv[1]
    out_dir = Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)

    folders, tables = load_pack(pack_dir)

    tables_by_folder = {}
    for t in tables:
        tables_by_folder.setdefault(t.get("folder"), []).append(t)

    root_folders = [f for f in folders.values() if not f.get("folder")]
    # Tables with no folder at all (shouldn't happen in this pack, but be safe).
    root_folders_by_id = {f["_id"]: f for f in root_folders}

    for root in root_folders:
        out = [f"# Ironsmith Expanded Oracles — {root['name']}\n"]
        render_folder(root["_id"], folders, tables_by_folder, 0, out)
        text = "\n".join(out)
        out_path = out_dir / f"{slugify(root['name'])}.md"
        out_path.write_text(text)
        print(f"wrote {out_path} ({len(text)} bytes)")

    if None in tables_by_folder:
        out = ["# Ironsmith Expanded Oracles — Misc\n"]
        for t in tables_by_folder[None]:
            out.append(render_table(t, 0))
        out_path = out_dir / "misc.md"
        out_path.write_text("\n".join(out))
        print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
