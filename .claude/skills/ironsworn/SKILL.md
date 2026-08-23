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

## Befehle im Chat

Kein festes Kommandosystem wie bei einer CLI — dieser Skill reagiert auf
natürliche Sprache. Die folgenden Formulierungen sind aber das feste Muster,
das immer gleich behandelt wird, damit der Nutzer sich darauf verlassen kann.
Bei jedem Move-Wurf oder Oracle-Wurf wird **live mit echtem Zufall gewürfelt**
(z.B. per Skript), nie ein Ergebnis ausgedacht — der Wurf wird immer
transparent gezeigt (Action Die, beide Challenge Dice, Ergebnis).

### Move ausführen (inkl. Kampf)

- „Ich mache **[Move-Name]** mit **[Stat]**" — z.B. „Ich mache Face Danger mit Edge"
- „Ich greife [Ziel] an" / „Ich mache Strike gegen [Ziel]" (Kampf-Move)
- „Ich betrete den Kampf gegen [Ziel]" (Enter the Fray)
- „Ich versuche [Aktion]" — der passende Move wird aus
  `references/datasworn/classic/moves.md` (bzw. `delve/moves.md`) ermittelt

Ablauf: passenden Move nachschlagen → Action Die (1d6) + Stat gegen zwei
Challenge Dice (1d10 je) würfeln → starker Treffer / schwacher Treffer /
Fehlschlag (plus Match, wenn beide Challenge Dice gleich sind) bestimmen →
passenden Outcome-Text aus der Referenz vorlesen und in die Fiktion
übersetzen.

Alle Move-Namen (Adventure, Relationship, Combat, Suffer, Quest, Fate) stehen
in `references/datasworn/classic/moves.md` bzw. `delve/moves.md`.

### Move suchen / Regel nachschlagen

- „Welcher Move passt zu [Situation]?"
- „Was macht [Move-Name]?"
- „Was ist [Begriff]?" — z.B. Momentum, Schwur (Vow), Progress Track, Debility

### Orakel befragen

- „Frage das Orakel: [Ja/Nein-Frage]" → **Ask the Oracle** (1d100 gegen Odds:
  Almost Certain/Likely/50-50/Unlikely/Small Chance), Match = Twist
- „Würfle [Oracle-Name]" — z.B. „Würfle Elf-Namen", „Würfle Wendepunkt"
- „Ich brauche [X]" — z.B. „einen NPC", „einen Ort", „einen Namen", „ein
  Settlement-Problem" → passendes Oracle wird gesucht (zuerst
  `references/datasworn/`, dann ergänzend `references/ironsmith/oracles/`)
  und gewürfelt
- „Erschaffe ein Monster" → Monstrosity-Kette aus `delve/oracles.md` (Size →
  Primary Form → bis zu 3 Characteristics → bis zu 3 Abilities)

### Schwüre (Vows)

- „Ich schwöre: [Text], Rang [Troublesome/Dangerous/Formidable/Extreme/Epic]"
  (Swear an Iron Vow)
- „Ich mache Fortschritt bei [Schwur]" (Reach a Milestone / Progress markieren)
- „Ich erfülle [Schwur]" (Fulfill Your Vow)
- „Ich gebe [Schwur] auf" (Forsake Your Vow)

### Assets

- „Zeig mir Asset [Name]" — Details aus `references/datasworn/classic/assets.md`
- „Ich nutze [Fähigkeit] von [Asset]"

### Tagebuch

- „Tagebucheintrag: [was passiert ist]" — wird als In-Character-Eintrag
  formuliert
- „Fasse die Session als Tagebuch zusammen"

### Weltenbau / Ideensammlung

- „Notiere: [Idee]"
- „Neuer NPC: [Beschreibung]"
- „Neuer Ort: [Beschreibung]"

## Nächste Schritte beim Aufbau

Wenn der Nutzer ein PDF (Regelwerk-Auszug, Weltbeschreibung o.Ä.) teilt:

1. Inhalt lesen und mit dem Nutzer klären, was daraus in eine Referenzdatei
   übernommen werden soll (nicht das ganze PDF unreflektiert kopieren).
2. Passende `references/*.md`-Datei anlegen oder erweitern.
3. Diesen SKILL.md-Body aktualisieren, falls neue Konzepte eine Erwähnung
   in der Kurzübersicht oben verdienen.
