# Quelle: Datasworn

Die Dateien in diesem Ordner stammen aus [rsek/datasworn](https://github.com/rsek/datasworn),
dem strukturierten JSON-Regelwerk für Ironsworn / Ironsworn: Starforged.

- Vendored von Commit `0e995ed485d7f6bf56e30342a4b91b8348282b4c` (datasworn_version 0.0.10)
- Lizenz der Inhalte (Text): CC-BY-4.0 (`https://creativecommons.org/licenses/by/4.0`)
- Lizenz von Schema/Tooling im Datasworn-Repo: MIT
- Ironsworn ist ein Pen-and-Paper-Rollenspiel von Shawn Tomkin

## Struktur

- `source/classic.json`, `source/starforged.json`, `source/delve.json` —
  Original-JSON von Datasworn (Quelle der Wahrheit für exakte Werte, IDs,
  Referenzen zwischen Objekten). Sind groß (400-700+ KB) — nicht direkt als
  Ganzes lesen, sondern gezielt mit `jq`/`grep` abfragen, wenn die
  generierten Markdown-Dateien nicht reichen.
- `classic/*.md`, `starforged/*.md`, `delve/*.md` — aus dem JSON generierte,
  nach Thema aufgeteilte Markdown-Referenzen (Moves, Oracles, Assets, NPCs,
  Atlas, Truths, Delve Sites, ...). Das ist die primäre Referenz, die der
  Skill beim Beantworten von Regelfragen lesen sollte.

**Wichtig — zwei getrennte Regelsysteme:** `classic/` (Ironsworn) und
`starforged/` (Ironsworn: Starforged) sind zwei eigenständige Regelwerke mit
teils gleichnamigen, aber unterschiedlich wirkenden Moves (z.B. hat
Starforged kein "Secure an Advantage", dafür z.B. "React Under Fire", das es
in Classic nicht gibt). Innerhalb einer Kampagne/Session gilt immer nur
**eines** der beiden für Moves — nicht mischen, außer der Nutzer sagt
ausdrücklich, dass er ein Hybrid-Regelwerk spielt. `delve/` (Ironsworn:
Delve) ist eine reine Dungeon-Crawling-Erweiterung (Delve Sites, Denizens,
Rarities) und funktioniert als Zusatz zu **beiden** Basisregelwerken.
`starforged/` selbst enthält keine eigenen `atlas`/`rarities`/`delve_sites`
-Daten — dafür wird bei Bedarf auf `delve/` zurückgegriffen.

## Aktualisieren

Falls Datasworn ein Update bekommt und die Regeln neu eingelesen werden
sollen:

```bash
# im datasworn-Repo (rsek/datasworn) die aktuelle classic.json / starforged.json /
# delve.json holen, dann in source/ ablegen und neu generieren:
python3 ../../scripts/build_reference_markdown.py source/classic.json classic
python3 ../../scripts/build_reference_markdown.py source/starforged.json starforged
python3 ../../scripts/build_reference_markdown.py source/delve.json delve
```
