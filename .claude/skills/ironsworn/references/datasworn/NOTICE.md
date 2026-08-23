# Quelle: Datasworn

Die Dateien in diesem Ordner stammen aus [rsek/datasworn](https://github.com/rsek/datasworn),
dem strukturierten JSON-Regelwerk für Ironsworn / Ironsworn: Starforged.

- Vendored von Commit `0e995ed485d7f6bf56e30342a4b91b8348282b4c` (datasworn_version 0.0.10)
- Lizenz der Inhalte (Text): CC-BY-4.0 (`https://creativecommons.org/licenses/by/4.0`)
- Lizenz von Schema/Tooling im Datasworn-Repo: MIT
- Ironsworn ist ein Pen-and-Paper-Rollenspiel von Shawn Tomkin

## Struktur

- `source/classic.json`, `source/delve.json` — Original-JSON von Datasworn
  (Quelle der Wahrheit für exakte Werte, IDs, Referenzen zwischen Objekten).
  Sind groß (600+ KB) — nicht direkt als Ganzes lesen, sondern gezielt mit
  `jq`/`grep` abfragen, wenn die generierten Markdown-Dateien nicht reichen.
- `classic/*.md`, `delve/*.md` — aus dem JSON generierte, nach Thema
  aufgeteilte Markdown-Referenzen (Moves, Oracles, Assets, NPCs, Atlas,
  Truths, Delve Sites, ...). Das ist die primäre Referenz, die der Skill
  beim Beantworten von Regelfragen lesen sollte.

## Aktualisieren

Falls Datasworn ein Update bekommt und die Regeln neu eingelesen werden
sollen:

```bash
# im datasworn-Repo (rsek/datasworn) die aktuelle classic.json / delve.json holen,
# dann in source/ ablegen und neu generieren:
python3 ../../scripts/build_reference_markdown.py source/classic.json classic
python3 ../../scripts/build_reference_markdown.py source/delve.json delve
```
