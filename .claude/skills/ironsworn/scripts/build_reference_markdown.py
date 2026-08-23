#!/usr/bin/env python3
"""Render a Datasworn ruleset JSON file into per-category Markdown reference files.

Datasworn (https://github.com/rsek/datasworn) ships the Ironsworn rules as
structured JSON. That's great for exact lookups but too large to read
wholesale as context. This script walks the JSON tree once and writes small,
topic-scoped Markdown files (moves.md, oracles.md, assets.md, ...) that are
cheap to read on demand.

Usage:
    python3 build_reference_markdown.py <input.json> <output_dir>

Re-run this whenever the vendored JSON in references/datasworn/ is updated.
"""
import json
import sys
from pathlib import Path

# Top-level Datasworn keys that become their own output file.
TOP_LEVEL_SECTIONS = [
    "rules",
    "moves",
    "oracles",
    "assets",
    "npcs",
    "atlas",
    "truths",
    "rarities",
    "delve_sites",
    "site_domains",
    "site_themes",
]

CONTAINER_KEYS = ("contents", "collections")


def esc(text):
    return "" if text is None else str(text)


def render_range_table(rows, extra_cols=()):
    rows = [r for r in rows if isinstance(r, dict)]
    lines = ["Roll | Result" + "".join(f" | {c.title()}" for c in extra_cols), "---|---" + "|---" * len(extra_cols)]
    for row in rows:
        lo, hi = row.get("min"), row.get("max")
        rng = f"{lo}" if lo == hi else f"{lo}-{hi}"
        text = esc(row.get("text") or row.get("description") or row.get("result") or "")
        text = text.replace("\n", " ")
        extras = "".join(f" | {esc(row.get(c, '')).replace(chr(10), ' ')}" for c in extra_cols)
        lines.append(f"{rng} | {text}{extras}")
    return "\n".join(lines)


def render_leaf(node, depth):
    out = []
    heading = "#" * min(depth + 2, 6)
    name = node.get("name") or node.get("label")
    if name:
        out.append(f"{heading} {name}\n")

    for key in ("summary", "description", "text"):
        if node.get(key):
            out.append(f"{node[key]}\n")

    if node.get("dice"):
        out.append(f"*Dice: {node['dice']}*\n")

    # Oracle-style row tables (oracles, truth options with min/max, site features/dangers)
    if isinstance(node.get("rows"), list) and node["rows"]:
        out.append(render_range_table(node["rows"]) + "\n")

    if isinstance(node.get("options"), list) and node["options"]:
        rows = node["options"]
        out.append(render_range_table(rows, extra_cols=("quest_starter",) if any("quest_starter" in r for r in rows) else ()) + "\n")

    for field in ("features", "dangers", "drives", "tactics"):
        items = node.get(field)
        if isinstance(items, list) and items:
            out.append(f"**{field.title()}**\n")
            if isinstance(items[0], dict):
                out.append(render_range_table(items) + "\n")
            else:
                out.append("\n".join(f"- {esc(i)}" for i in items) + "\n")

    if isinstance(node.get("denizens"), list) and node["denizens"]:
        out.append("**Denizens**\n")
        lines = ["Roll | Name | Rank", "---|---|---"]
        for d in node["denizens"]:
            lo, hi = d.get("min"), d.get("max")
            rng = f"{lo}" if lo == hi else f"{lo}-{hi}"
            lines.append(f"{rng} | {esc(d.get('name'))} | {esc(d.get('rank'))}")
        out.append("\n".join(lines) + "\n")

    if isinstance(node.get("abilities"), list) and node["abilities"]:
        for ab in node["abilities"]:
            if ab.get("text"):
                out.append(f"- {ab['text']}\n")

    for field in ("quest_starter", "your_character"):
        if node.get(field):
            out.append(f"**{field.replace('_', ' ').title()}:** {node[field]}\n")

    for field in ("region", "theme", "domain", "rank", "xp_cost"):
        if node.get(field) is not None and node.get("type") in ("delve_site", "rarity"):
            out.append(f"- **{field.replace('_', ' ').title()}:** {node[field]}")
    if node.get("type") in ("delve_site", "rarity"):
        out.append("")

    return "\n".join(out)


def walk(node, depth, out):
    if not isinstance(node, dict):
        return
    is_container = any(k in node for k in CONTAINER_KEYS)
    if is_container:
        name = node.get("name") or node.get("label")
        if name:
            heading = "#" * min(depth + 2, 6)
            out.append(f"{heading} {name}\n")
        for key in ("summary", "description"):
            if node.get(key):
                out.append(f"{node[key]}\n")
        for key in CONTAINER_KEYS:
            for child in node.get(key, {}).values():
                walk(child, depth + 1, out)
    else:
        out.append(render_leaf(node, depth))


def walk_flat_dict(d, depth, out):
    """For dicts of simple label->fields records without a 'type' wrapper
    (rules.stats, rules.condition_meters, rules.special_tracks)."""
    heading = "#" * min(depth + 2, 6)
    for _key, val in d.items():
        if not isinstance(val, dict):
            continue
        name = val.get("label", _key)
        out.append(f"{heading} {name}\n")
        if val.get("description"):
            out.append(f"{val['description']}\n")
        rng = []
        if "min" in val and "max" in val:
            rng.append(f"Range: {val['min']}-{val['max']}")
        if rng:
            out.append(f"*{'; '.join(rng)}*\n")


def render_section(key, data, out):
    if key == "rules":
        out.append("## Rules\n")
        for sub in ("stats", "condition_meters", "special_tracks"):
            if sub in data:
                out.append(f"### {sub.replace('_', ' ').title()}\n")
                walk_flat_dict(data[sub], 1, out)
        if "impacts" in data:
            out.append("### Impacts\n")
            for cat in data["impacts"].values():
                walk(cat, 1, out)
        return

    if key == "truths":
        out.append("## Truths\n")
        for truth in data.values():
            walk(truth, 0, out)
        return

    # Generic: dict of top-level category name -> collection/leaf tree
    label = key.replace("_", " ").title()
    out.append(f"## {label}\n")
    for child in data.values():
        walk(child, 0, out)


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    src = Path(sys.argv[1])
    out_dir = Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)

    data = json.loads(src.read_text())
    title = data.get("title", src.stem)

    for key in TOP_LEVEL_SECTIONS:
        if key not in data or not data[key]:
            continue
        out = [f"# {title} — {key.replace('_', ' ').title()}\n"]
        render_section(key, data[key], out)
        text = "\n".join(out)
        out_path = out_dir / f"{key}.md"
        out_path.write_text(text)
        print(f"wrote {out_path} ({len(text)} bytes)")


if __name__ == "__main__":
    main()
