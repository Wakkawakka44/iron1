# Quelle: Ironsmith Expanded Oracles

Die Dateien unter `oracles/` stammen aus dem FoundryVTT-Modul
[jendave/ironsmith-compendiums](https://github.com/jendave/ironsmith-compendiums),
Pack `ironsmith-expanded-oracles` (168 zusätzliche Orakel-Tabellen).

Ursprünglich aus dem **Ironsmith Expanded Oracles**-Supplement von
[Eric Bright](https://playeveryrole.com/) (DriveThruRPG), als FoundryVTT-Modul
gepflegt von David Y. Hudson (jendave).

- Vendored von Commit `ef926fc77b023ff56e59e07b69dfa003f67453c7`
- **Lizenz der Oracle-Inhalte: CC-BY-NC-SA-4.0** (Namensnennung –
  Nicht-kommerziell – Weitergabe unter gleichen Bedingungen), siehe
  `LICENSE-Oracles` im Quell-Repo. Das ist **restriktiver** als die
  CC-BY-4.0-Inhalte unter `../datasworn/` (dort: Namensnennung reicht,
  auch kommerzielle Nutzung erlaubt). Für privaten, nicht-kommerziellen
  Gebrauch (Tagebuch/Ideensammlung) unproblematisch — bei Veröffentlichung
  oder Weitergabe dieses Skills muss NC+SA beachtet werden.
- Dies ist **inoffizielles Drittanbieter-Material**, kein offizielles
  Ironsworn-Regelwerk von Shawn Tomkin (im Gegensatz zu `../datasworn/`).

## Warum keine Roh-JSON vendored ist

Anders als bei Datasworn ist das Quellformat hier reines FoundryVTT-VTT-
Plumbing (ein JSON-File pro Tabelle/Ordner, mit viel Metadaten wie `_id`,
`_stats`, `ownership`, Icon-Pfaden), das für uns keinen Mehrwert über die
generierten Markdown-Dateien hinaus bietet. Deshalb wurde nur das Ergebnis
der Konvertierung (`oracles/*.md`) übernommen, nicht die 200+ Roh-Dateien.
Bei Bedarf lässt sich alles aus dem Quell-Repo neu erzeugen (siehe unten).

## Bekannte Datenmacke

In der Tabelle „Primary Form" (unter `oracles/monster-hunting.md`, im
Unterordner „Design the Monster") hat der Wertebereich für „Mammal"
`21-350` statt vermutlich `21-50` — das ist ein Tippfehler in der
Originalquelle, kein durch die Konvertierung eingeführter Fehler. Praktisch
harmlos, da bei einem 1-100-Wurf nur 21-50 überhaupt erreichbar ist.

## Struktur

- `oracles/*.md` – aus dem `ironsmith-expanded-oracles`-Pack generierte,
  nach Themenordner aufgeteilte Markdown-Referenzen (eine Datei pro
  Root-Kategorie, z.B. Vows and Milestones, Monster Hunting, Character,
  Name, Place Oracles, ...)

## Aktualisieren / weitere Packs hinzufügen

```bash
# im geklonten jendave/ironsmith-compendiums-Repo:
python3 ../../scripts/build_ironsmith_oracles.py \
  json-packs/ironsmith-expanded-oracles \
  <skill>/references/ironsmith/oracles

# funktioniert genauso für die anderen Oracle-Packs im selben Repo, z.B.
# json-packs/ironsmith-japanese-oracles, ironsmith-indian-oracles, etc.
# (noch nicht eingebaut — siehe Analyse zu Flavor Packs)
```
