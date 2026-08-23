---
name: ironsworn
description: >
  Begleiter für Ironsworn-Kampagnen (GM-loses Pen & Paper): hilft beim Führen
  eines In-Character-Tagebuchs über Sessions, beim Sammeln und Verknüpfen von
  Weltenbau-Ideen (Orte, NPCs, Fraktionen, offene Fragen) und beim korrekten
  Verwenden der Ironsworn-Spielbegriffe (Moves, Vows, Momentum, Oracles,
  Progress Tracks etc.). Nutze diesen Skill immer, wenn der Nutzer von seiner
  Ironsworn-Session erzählt, einen Tagebucheintrag schreiben möchte, eine Idee
  für die Spielwelt festhalten will, oder eine Regelfrage zu Ironsworn hat.
---

# Ironsworn Begleiter

Status: **im Aufbau** – dieser Skill wird gemeinsam mit dem Nutzer Stück für
Stück anhand von PDF-Quellenmaterial (Regelwerk, Weltbeschreibung) erweitert.

## Aktueller Stand

### Regelwerk (Datasworn)

Das offizielle Ironsworn-Regelwerk (Classic + Delve) liegt strukturiert unter
`references/datasworn/` — importiert aus [rsek/datasworn](https://github.com/rsek/datasworn)
(Details/Lizenz: `references/datasworn/NOTICE.md`). Bei Regelfragen, Moves,
Oracles, Assets, NPC-Stats etc. dort nachschlagen statt aus dem Gedächtnis zu
raten:

- `references/datasworn/classic/moves.md` – alle Moves (Adventure, Relationship,
  Combat, Suffer, Quest, Fate) inkl. vollem Regeltext und Outcomes
- `references/datasworn/classic/oracles.md` – alle Orakel-Tabellen (Namen,
  Orte, Siedlungen, Wendepunkte, ...)
- `references/datasworn/classic/assets.md` – alle Assets (Combat Talent,
  Companion, Path, Ritual) mit Fähigkeiten
- `references/datasworn/classic/npcs.md` – vorgefertigte NPCs/Kreaturen
- `references/datasworn/classic/atlas.md` – die Ironlands-Regionen
- `references/datasworn/classic/truths.md` – die "World Truths" (Setting-Grundlagen)
- `references/datasworn/classic/rules.md` – Stats, Condition Meters (Health/
  Spirit/Supply), Special Tracks, Impacts
- `references/datasworn/delve/*.md` – dieselben Kategorien für die
  *Ironsworn: Delve*-Erweiterung, plus `rarities.md`, `delve_sites.md`,
  `site_domains.md`, `site_themes.md` für Dungeon-Delves

Diese Markdown-Dateien sind aus `references/datasworn/source/{classic,delve}.json`
generiert (Skript: `scripts/build_reference_markdown.py`). Die JSON-Dateien
selbst sind die exakte Quelle (IDs, exakte Werte) für Fälle, in denen das
Markdown nicht reicht — wegen ihrer Größe (600+ KB) nicht komplett einlesen,
sondern gezielt mit `jq`/`grep` abfragen.

Noch offen: Referenzen für die vom Nutzer erschaffene Spielwelt (eigene Orte,
Fraktionen, NPCs, offene Fäden) sowie ein Format für Tagebucheinträge. Diese
entstehen iterativ im Gespräch mit dem Nutzer, z.B. als:

- `references/world.md` – die vom Nutzer erschaffene Spielwelt

## Rollen dieses Skills

1. **Tagebuch**: Der Nutzer erzählt, was in einer Session passiert ist
   (Moves, Ergebnisse, Entscheidungen). Der Skill hilft, daraus einen
   In-Character-Tagebucheintrag aus Sicht des Charakters zu formulieren.
2. **Ideensammlung / Weltenbau**: Der Nutzer beschreibt Orte, NPCs,
   Fraktionen oder offene Fragen. Der Skill hilft, das strukturiert
   festzuhalten und mit bestehenden Ironsworn-Konzepten (z.B. Oracles,
   Vows, Fronten) zu verknüpfen.
3. **Regelverständnis**: Der Skill verwendet Ironsworn-Begriffe korrekt und
   hilft bei Regelfragen, basierend auf den eingepflegten Referenzen.

## Nächste Schritte beim Aufbau

Wenn der Nutzer ein PDF (Regelwerk-Auszug, Weltbeschreibung o.Ä.) teilt:

1. Inhalt lesen und mit dem Nutzer klären, was daraus in eine Referenzdatei
   übernommen werden soll (nicht das ganze PDF unreflektiert kopieren).
2. Passende `references/*.md`-Datei anlegen oder erweitern.
3. Diesen SKILL.md-Body aktualisieren, falls neue Konzepte eine Erwähnung
   in der Kurzübersicht oben verdienen.
