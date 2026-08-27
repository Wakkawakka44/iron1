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

Das offizielle Ironsworn-Regelwerk (Classic + Starforged + Delve) liegt
strukturiert unter `references/datasworn/` — importiert aus
[rsek/datasworn](https://github.com/rsek/datasworn) (Details/Lizenz:
`references/datasworn/NOTICE.md`). Bei Regelfragen, Moves, Oracles, Assets,
NPC-Stats etc. dort nachschlagen statt aus dem Gedächtnis zu raten:

- `references/datasworn/classic/moves.md` – alle **Ironsworn Classic**-Moves
  (Adventure, Relationship, Combat, Suffer, Quest, Fate) inkl. vollem
  Regeltext und Outcomes
- `references/datasworn/classic/oracles.md` – alle Orakel-Tabellen (Namen,
  Orte, Siedlungen, Wendepunkte, ...)
- `references/datasworn/classic/assets.md` – alle Assets (Combat Talent,
  Companion, Path, Ritual) mit Fähigkeiten
- `references/datasworn/classic/npcs.md` – vorgefertigte NPCs/Kreaturen
- `references/datasworn/classic/atlas.md` – die Ironlands-Regionen
- `references/datasworn/classic/truths.md` – die "World Truths" (Setting-Grundlagen)
- `references/datasworn/classic/rules.md` – Stats, Condition Meters (Health/
  Spirit/Supply), Special Tracks, Impacts
- `references/datasworn/starforged/*.md` – dieselben Kategorien (moves,
  oracles, assets, npcs, truths, rules) für **Ironsworn: Starforged**, das
  eigenständige Sci-Fi-Regelwerk mit teils anderen Moves (z.B. "React Under
  Fire" statt "Secure an Advantage")
- `references/datasworn/delve/*.md` – dieselben Kategorien für die
  *Ironsworn: Delve*-Erweiterung, plus `rarities.md`, `delve_sites.md`,
  `site_domains.md`, `site_themes.md` für Dungeon-Delves

**Wichtig — Classic und Starforged nicht mischen:** Für Moves gilt pro
Kampagne/Charakter immer genau **ein** Basisregelwerk, entweder Classic
(`classic/moves.md`) oder Starforged (`starforged/moves.md`) — nie beide
gleichzeitig, außer der Nutzer sagt ausdrücklich, dass er ein
Hybrid-Regelwerk spielt. Ist zu Beginn einer Session unklar, welches
Regelwerk gilt, kurz nachfragen statt zu raten. **Ironsworn: Delve**
(`delve/*.md`) ist reine Dungeon-Erkundung und passt zu **beiden**
Basisregelwerken gleichzeitig.

Diese Markdown-Dateien sind aus
`references/datasworn/source/{classic,starforged,delve}.json` generiert
(Skript: `scripts/build_reference_markdown.py`). Die JSON-Dateien selbst
sind die exakte Quelle (IDs, exakte Werte) für Fälle, in denen das Markdown
nicht reicht — wegen ihrer Größe (400-700+ KB) nicht komplett einlesen,
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

### Die eigene Welt des Nutzers

Es gibt **zwei** Dateien, die dieselbe Weltbeschreibung in zwei
Sichtbarkeitsstufen enthalten — entlang der offiziellen Truths aufgebaut
(Überschriften wie "## The Old World" entsprechen den Truth-Kategorien aus
`references/datasworn/classic/truths.md`):

- **`references/world/meine-welt-gm.md`** ist die alleinige Quelle der
  Wahrheit (Source of Truth). Hier werden alle Änderungen vorgenommen.
  Enthält zusätzlich zum normalen Text GM-only-Abschnitte, markiert mit
  einer Überschrift der Form `### GM: <Titel>` — für Spoiler, aufgelöste
  Hintergrundgeheimnisse (z.B. die wahre Ursache eines In-Welt-Mysteriums)
  und Produktionsnotizen, die die Spieler:innen nicht kennen sollen.
- **`references/world/meine-welt.md`** ist die spielerfreundliche,
  spoilerfreie Fassung — automatisch generiert aus der GM-Datei via
  `python3 scripts/strip_gm_notes.py references/world/meine-welt-gm.md references/world/meine-welt.md`.
  **Niemals direkt bearbeiten** — jede Änderung geht in die GM-Datei, dann
  das Skript laufen lassen.

Iterativ im Gespräch mit dem Nutzer erweitern:

- Wenn der Nutzer eine Truth beschreibt, den Kern seiner Aussage (nicht das
  Transkript wörtlich) in einen zusammenhängenden Absatz unter der
  passenden Truth-Überschrift fassen, in `meine-welt-gm.md`.
- Beide Dateien sauber/publizierbar halten: reiner Weltbeschreibungs-
  Fließtext, keine Meta-Kommentare wie "Offene Frage", "Klärungsbedarf",
  "Korrektur" oder "vorläufig" im normalen Text — auch nicht in der
  GM-Datei außerhalb eines `### GM:`-Abschnitts. Unentschiedene Details
  stattdessen im Chat ansprechen/nachfragen, statt sie zu erfinden oder als
  Platzhalter ins Dokument zu schreiben; erst nach Klärung als fertigen
  Text einpflegen. In-Welt-Mysterien (Dinge, die die Charaktere selbst
  nicht wissen) gehören als normale Erzählung in den Haupttext (z.B. "ihr
  wahrer Zweck ist unbekannt") — hat der Nutzer aber bereits eine geheime
  Auflösung dafür festgelegt (wie beim Grund für den Wahnsinn der Broken),
  gehört diese Auflösung in einen `### GM:`-Abschnitt direkt danach.
- Wenn eine spätere Aussage des Nutzers einer bereits eingetragenen Stelle
  widerspricht, den betroffenen Text in `meine-welt-gm.md` direkt
  korrigieren (nicht als "Korrektur:"-Vermerk daneben schreiben) und im
  Chat kurz zusammenfassen, was geändert wurde.
- Für Inhalte, die zu keiner Truth gehören (NPCs, Orte, Fraktionen, offene
  Fäden), passende neue Abschnitte/Dateien unter `references/world/`
  anlegen, sobald der Nutzer solche Inhalte liefert — nach demselben
  GM/öffentlich-Muster, falls Spoiler-Inhalte dabei sind.
- Nach jeder Änderung an `meine-welt-gm.md` sofort `strip_gm_notes.py`
  laufen lassen, damit die beiden Dateien nie auseinanderdriften.

Noch offen: ein Format für Tagebucheinträge. Entsteht ebenfalls iterativ,
sobald der Nutzer die erste Session erzählt.

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
- „Ich versuche [Aktion]" — der passende Move wird aus dem Moves-File des
  aktuell geltenden Regelwerks ermittelt (`classic/moves.md` **oder**
  `starforged/moves.md` — nie beide gemischt; `delve/moves.md` ergänzend für
  Dungeon-Situationen)

Ablauf: passenden Move nachschlagen → Action Die (1d6) + Stat gegen zwei
Challenge Dice (1d10 je) würfeln → starker Treffer / schwacher Treffer /
Fehlschlag (plus Match, wenn beide Challenge Dice gleich sind) bestimmen →
passenden Outcome-Text aus der Referenz vorlesen und in die Fiktion
übersetzen.

Alle Move-Namen stehen in `references/datasworn/classic/moves.md` (Adventure,
Relationship, Combat, Suffer, Quest, Fate) bzw.
`references/datasworn/starforged/moves.md` (Session, Adventure, Quest,
Connection, Exploration, Combat, Suffer, Recover, Threshold, Legacy, Fate,
Scene Challenge — eigene Kategorien, teils andere Move-Namen und -Wirkung
als Classic) sowie ergänzend `delve/moves.md`.

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
