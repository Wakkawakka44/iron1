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

### Zusätzliche Orakel (Ironsmith Expanded Oracles)

Ergänzend zu den offiziellen Oracles gibt es unter `references/ironsmith/oracles/`
168 zusätzliche Orakel-Tabellen aus dem *Ironsmith Expanded Oracles*-Supplement
(Details/Lizenz — **CC-BY-NC-SA-4.0, inoffizielles Drittanbieter-Material**:
`references/ironsmith/NOTICE.md`). Nützlich vor allem für Weltenbau/Ideensammlung,
wenn die Ironsworn-Kern-Oracles nicht die passende Tabelle bieten:

- `vows-and-milestones.md` – Quest-Schwierigkeit, narrative Konflikte, Wege
  zu Meilensteinen, Mystery Vow, Grim Quest, One-Shot, Challenges to Noble Virtue
- `monster-hunting.md` – "Design the Monster" (Fähigkeit, Form, Größe, ...),
  Ending the Fight, Heed the Call
- `character.md` – Hintergrund-/Charakter-Prompts
- `name.md` – weitere Namensgeneratoren
- `turning-point-oracles.md`, `place-oracles.md`, `settlement-oracles.md`,
  `site-name.md`, `site-nature.md` – Ergänzungen zu Orten/Siedlungen/Delve-Sites
- `corruption.md`, `combat-event.md`, `trap.md`, `feature.md`, `monstrosity.md`,
  `threat.md`, `action-and-theme-oracles.md`, `move-oracles.md` – weitere
  Detail-Oracles

Achtung Überschneidung: `monster-hunting.md` enthält unter "Design the
Monster" eine eigene "Size"-Tabelle. Für Monster-Design zählt bevorzugt die
offizielle `references/datasworn/delve/oracles.md`-Tabelle (Monstrosity:
Size/Primary Form/Characteristics/Abilities) — die Ironsmith-Variante ist
laut Quelltext ausdrücklich nur ein Ersatz für Runden ohne Ironsworn: Delve.

Bei Regelfragen zählen weiterhin die `references/datasworn/`-Dateien als
offizielle Quelle; die Ironsmith-Oracles sind reine Inspirations-Zusatzoracles,
kein Regelwerk.

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
