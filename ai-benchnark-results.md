## P1
#### Claude
Das Kernproblem ist nicht die Zeilenzahl, sondern dass beim Öffnen alles gleich laut schreit. Die Lösung ist **vertikale Priorisierung** — nicht mehr Dateien, nicht mehr Struktur.

**Vorschlag: 3-Zonen-Layout in derselben Datei**

```markdown
# COCKPIT

## NOW
<!-- Max 3 Einträge. Wenn voll: eins muss raus bevor eins rein darf. -->
- [ ] GVL: Schutzbedarfsfeststellung fertig machen
- [ ] EKIBA: Angebot finalisieren
- [ ] SEC5: Newsletter Q2 Draft

## QUEUE
<!-- Priorisiert. Oberstes rückt nach NOW nach, wenn Slot frei. -->
1. AIP: IT-Abhängigkeitsanalyse Nachbereitung
2. BvD: BayLDA-Event Nachbereitung
3. Krypto-Richtlinie Review
...

## PARKED
<!-- Nicht vergessen, aber nicht jetzt. Wöchentlich scannen. -->
- ILE Altmühltal Übergabe-Reste
- ...

---
<!-- RECOVERY ANKER — nur lesen wenn stuck -->
## IF STUCK
- Kein Einstieg? → Nimm den ersten Eintrag aus NOW.
- Alles dringend? → Frag: Was hat einen externen Termin?
- Energie leer? → Kleinstes Item aus QUEUE ziehen, erledigen, Dopamin mitnehmen.

## META
state: active
last_updated: 2026-03-07
agent: kimiclaw
```

**Warum das funktioniert:**

Die **NOW-Sektion ist das einzige, was du lesen musst.** 3-Item-Cap ist der entscheidende Hebel — es zwingt dich zur Priorisierung *bevor* du die Datei öffnest, nicht währenddessen. QUEUE und PARKED sind da, aber du scrollst nur hin wenn du umschichten willst.

Recovery-Anker wandern unter einen Separator — sichtbar wenn gebraucht, unsichtbar im Normalbetrieb.

**Für KimiClaw** bleibt alles plain Markdown mit konsistenten H2-Headern. Parsen per Regex auf `## NOW`, `## QUEUE` etc. ist trivial und robust. Keine verschachtelten Strukturen, keine Frontmatter-Magie.

**Annahme:** KimiClaw parst aktuell per Heading-Matching oder Zeilenposition. Falls es auf ein anderes Schema angewiesen ist, müsstest du mir das Format zeigen.

Eine Sache noch: Die 47→~30 Zeilen-Reduktion kommt hauptsächlich vom 3-Item-Cap in NOW und dem Zusammenfalten der Metadaten. Subtract before add — keine neuen Konzepte, nur Sichtbarkeit gesteuert.

### Chatgpt
Ja. Das Problem ist nicht der Single Entry Point. Das Problem ist, dass dein Entry Point gleichzeitig Dashboard, Queue, Projektliste, Statusspeicher und Recovery-Fläche geworden ist.

Du solltest cockpit.md nicht aufgeben, sondern enger definieren:

> cockpit.md = operativer Startbildschirm, nicht Vollabbild des Systems.



Zielbild

cockpit.md soll beim Öffnen in wenigen Sekunden drei Fragen beantworten:

1. Wo bin ich gerade?


2. Was ist jetzt als Nächstes dran?


3. Wie komme ich bei Abbruch wieder rein?



Alles andere ist Kandidat zum Auslagern.


---

Empfehlung: 3-Zonen-Modell

Behalte eine Datei als Single Entry Point, aber reduziere sie auf drei einfache Zonen:

1. NOW

Nur der aktuell aktive Ausführungskontext.

Inhalt:

aktueller Modus: orchestrator oder executor

genau 1 aktueller Fokus

optional 1–3 „als Nächstes“-Schritte

letzter Recovery-Hinweis


Beispiel:

# cockpit

mode: executor
focus: hisolutions.iso27001-gap-analysis
next:
  - evidence notes öffnen
  - Kapitel 4-6 prüfen
  - offene Annahmen markieren
recovery: Wenn unterbrochen -> `projects/hisolutions.iso27001-gap-analysis.md` öffnen und Abschnitt "next step" lesen.

Das ist der Teil, den du jedes Mal sofort sehen willst.


---

2. ACTIVE

Nur die aktiven Projekte, aber stark komprimiert.

Nicht 12 Projekte mit Volltext. Sondern pro Projekt nur:

ID

Status

nächster physischer Einstiegspunkt


Beispiel:

## active
- hisolutions.iso27001-gap-analysis | executor | next: Kapitel 4 prüfen
- hisolutions.nis2-mapping-ekiba | waiting | next: Kundendaten abwarten
- private.hive-finance | orchestrator | next: Budgetblock vereinfachen
- mimir.refactor | paused | next: archive-Regeln finalisieren

Wichtig:

eine Zeile pro Projekt

keine Erklärabsätze

keine Historie

kein „Warum“

kein vollständiger Kontext


Wenn ein Projekt mehr braucht, gehört es in eine eigene Projektdatei.


---

3. QUEUE / PARKED / RECOVERY

Nur sehr knapp.

Beispiel:

## queue
- sec.template-soa-update
- private.readwise-cleanup
- tool.git-hooks-review
- lang.english-security-phrases
- hisolutions.customer-x-followup
- mimir.naming-cleanup

## recovery
- Wenn überfordert: erst `mode` prüfen, dann `focus`, dann genau 1 nächsten Schritt ausführen.
- Wenn kein klarer Fokus: in orchestrator wechseln und nur Priorisierung machen, keine Arbeit.


---

Was du aus cockpit.md entfernen solltest

Alles, was nicht unmittelbar beim Öffnen nötig ist.

Raus damit:

ausführliche Projektbeschreibungen

Begründungen

längere Metadatenblöcke

Entscheidungslogik

mehrstufige Statusdetails

historische Notizen

generische Regeln, die selten gebraucht werden


Diese Dinge machen den Einstieg teuer.


---

Konkrete Refaktor-Regel

In cockpit.md bleibt nur:

globaler Modus

aktueller Fokus

1-Zeilen-Status aller aktiven Projekte

rohe Warteschlange

wenige Recovery-Anker


In Projektdateien wandert:

Kontext

Ziel

offene Fragen

nächste Schritte

Annahmen

Blocker

Artefakte/Links



---

Minimalistische Struktur, die KimiClaw gut parsen kann

Keine cleveren Markdown-Spielereien. Keine verschachtelten Tabellen. Keine Fold-Blocks. Keine semantisch überladenen Emojis.

Nimm stattdessen stabile, primitive Strukturen:

# cockpit

mode: executor
focus: hisolutions.iso27001-gap-analysis

## next
- evidence notes öffnen
- Kapitel 4-6 prüfen
- Annahmen markieren

## active
- hisolutions.iso27001-gap-analysis | executor | next: Kapitel 4 prüfen
- hisolutions.nis2-mapping-ekiba | waiting | next: Kundendaten abwarten
- mimir.refactor | paused | next: split cockpit sections

## queue
- sec.template-soa-update
- private.readwise-cleanup
- tool.git-hooks-review
- lang.english-security-phrases
- hisolutions.customer-x-followup
- mimir.naming-cleanup

## recovery
- Wenn unterbrochen: zuerst Projektdatei des `focus` öffnen.
- Wenn Fokus unklar: in `orchestrator` wechseln und genau 1 Prioritätsentscheidung treffen.

Das ist für Mensch + Agent robust:

klar

flach

zeilenbasiert

wenig Parser-Magie

diff-freundlich



---

Der eigentliche Hebel: von „Projektliste“ zu „Projektindex“

Dein cockpit sollte nicht mehr alle 12 aktiven Projekte repräsentieren, sondern nur noch indizieren.

Das ist der Kern der Refaktorisierung.

Aktuell vermutlich:

cockpit.md enthält zu viel Projektinhalt


Soll-Zustand:

cockpit.md zeigt nur, welches Projekt relevant ist und wohin du springen musst


Single Entry Point bleibt erhalten, aber wird wieder leicht.


---

Gute Obergrenze

Praktisch würde ich für cockpit.md diese Limits setzen:

max. 25–30 Zeilen

max. 1 Zeile pro aktivem Projekt

queue nur IDs

recovery max. 3 Regeln

next max. 3 Punkte


Sobald etwas darüber geht, ist es ein Signal zum Auslagern.

47 Zeilen sind nicht per se schlimm. Aber wenn sich das beim Öffnen „zu viel auf einmal“ anfühlt, ist die Datei funktional schon zu groß.


---

Sinnvolle Statusnormalisierung

Falls du aktuell viele Sonderzustände hast, reduziere.

Empfehlung:

executor

orchestrator

waiting

paused


Mehr brauchst du meistens nicht.

Zu viele Status kosten Lesebandbreite und bringen im Cockpit wenig.


---

Konkreter Refactor in 4 Schritten

Schritt 1

Definiere cockpit.md neu als:

mode

focus

next

active

queue

recovery


Schritt 2

Für jedes aktive Projekt:

alles über 1 Zeile raus

in eigene Projektdatei verschieben


Schritt 3

Normiere jede aktive Projektzeile auf dieses Format:

- <project-id> | <status> | next: <one physical next step>

Nicht „weiter an Konzept arbeiten“. Sondern physisch:

Kapitel 4 prüfen

Kundenantwort abwarten

Tabelle A ergänzen


Schritt 4

Reduziere Recovery-Anker auf nur die wenigen, die du real benutzt.


---

Was ich nicht tun würde

Nicht:

zweite Cockpit-Datei einführen

dynamische Includes bauen

YAML-Overkill hinzufügen

verschachtelte Sections mit Sondersyntax bauen

Priorisierungsscores einführen

Agent-spezifische Parsertricks nutzen


Das wäre genau die falsche Richtung. Du willst weniger Semantik im Cockpit, nicht mehr.


---

Mein klarer Vorschlag

Nutze dieses Zielschema:

# cockpit

mode: executor
focus: <project-id>

## next
- <step 1>
- <step 2>
- <step 3>

## active
- <project-id> | <status> | next: <next step>
- <project-id> | <status> | next: <next step>
- <project-id> | <status> | next: <next step>

## queue
- <project-id>
- <project-id>
- <project-id>

## recovery
- Wenn unterbrochen: `focus`-Projekt öffnen.
- Wenn Fokus unklar: nur priorisieren, nicht ausführen.
- Wenn Widerstand hoch: kleinsten nächsten physischen Schritt wählen.

Das hält den Single Entry Point intakt, senkt aber die kognitive Last massiv.

Annahme: KimiClaw braucht vor allem eine stabile, flache, zeilenorientierte Struktur und keinen reichhaltigen Fließtext. Unter dieser Annahme ist die beste Lösung nicht mehr Struktur, sondern weniger Inhalt pro Struktur.

Wenn du willst, refaktoriere ich dir dein cockpit.md direkt in ein konkretes v1-Schema mit Beispielinhalt für deine 12 aktiven Projekte.

### Kimi 2.5
Diagnose: Dein cockpit.md leidet unter context density, nicht unter Länge. 47 Zeilen sind nicht das Problem – das gleichzeitige Sichtbarsein von 12 Projekten + 6 Queue-Items + Ankern erzeugt einen paralysis by analysis-Effekt beim Öffnen. Das ist klassisch für ADHS Combined Type: Zu viele Einstiegspunkte, keine klare Hierarchie.

Lösung: Das "Hot Zone" Pattern
Behalte die Single-File-Struktur bei, aber führe eine thermische Trennung ein: Nur das, was aktuell "heiß" ist (Executor-Mode), steht oben. Der Rest wird zu "warm" (Monitoring) und "kalt" (Referenz) herabgestuft, bleibt aber in derselben Datei für KimiClaw erreichbar.

---

Refactoring-Vorlage (Copy-Paste Ready)

```markdown
# COCKPIT

## NOW [MAX 3]
<!-- EXECUTOR MODE: Nur hier arbeiten. Wenn hier nichts steht → Recovery-Anker "STALLED" -->
- [ ] [[Projekt-X]]: Atomare nächste Aktion (max 5 Wörter)
- [ ] [[Projekt-Y]]: Atomare nächste Aktion
- [ ] [[Projekt-Z]]: Atomare nächste Aktion

## ACTIVE [12]
<!-- ORCHESTRATOR MODE: Status-Übersicht, nicht arbeiten -->
| Projekt | Status | Blocker | Link |
|---------|--------|---------|------|
| Projekt-X | Review | Warte auf Kunde | [[x-cockpit]] |
| Projekt-Y | Analyse | Dokumentation fehlt | [[y-cockpit]] |
| ... | | | |

## QUEUE [6]
<!-- INBOX: Noch nicht gestartet, chronologisch -->
1. [[Projekt-M]] (angelegt: 2026-03-08)
2. [[Projekt-N]] 
...

## ANCHORS
<!-- Recovery-If-Thens -->
- **Wenn STALLED:** Durchlaufe NOW-Liste → Ist das wirklich der nächste atomare Schritt? → Wenn nein, aufspalten. Wenn ja, Energie-Level checken.
- **Wenn OVERWHELMED:** Alles aus NOW in ACTIVE verschieben, nur Top-1 zurückholen.
```

---

Betriebsregeln (Subtract before add)

Regel 1: Die "3-12-6" Härte
- NOW niemals >3 Items. Bei 4 wird automatisch das älteste in ACTIVE zurückgeschoben.
- ACTIVE ist eine Tabelle, keine Aufgabenliste. Keine Checkboxen, kein `[ ]`. Das verhindert, dass du in der Übersicht arbeitest.
- QUEUE hat keine Status-Spalte. Entweder ist es in ACTIVE oder nicht.

Regel 2: Atomic Entry
Jede Zeile in NOW muss eine physische Aktion beschreiben, kein Ziel.

❌ "SBF fertigstellen"

✅ "SBF-Tabelle Zeile 15-30 validieren"

Regel 3: KimiClaw-Kompatibilität
KimiClaw kann weiterhin mit simplen Regex parsen:
- `## NOW` bis nächster `##` = Executor Context
- Tabellenzeilen in `## ACTIVE` parsen nach `|([^|]+)|` 
- Keine verschachtelten HTML-Kommentare nötig, keine YAML-Frontmatter-Overhead

Regel 4: Kontextwechsel-Reduktion
Wenn du ein Projekt öffnest, kopiere den Link aus der ACTIVE-Tabelle in die NOW-Sektion. Du hast dann beim Öffnen von `[[Projekt-X]]` den Kontext sofort in deinem Arbeitsgedächtnis, ohne zurückscrollen zu müssen.

---

Annahmen-Check

Annahme: Du hast für jedes der 12 Projekte eine eigene Detail-Datei (z.B. `projekt-x-cockpit.md`), auf die die Links in der Tabelle verweisen.

Annahme: KimiClaw parsed nach Sektionsheadern (`## NOW`), nicht nach Zeilennummern.

Annahme: Die 47 Zeilen enthalten derzeit Deep-Context für alle 12 Projekte (z.B. nächste Schritte, Notizen), was die Dichte erhöht.

Stimmen diese Annahmen? Wenn nein, passe das Pattern an: Die Tabelle in ACTIVE kann bei Bedarf zu einer einfachen Liste (`- Projekt | Status`) reduziert werden, wenn KimiClaw keine Pipes verarbeitet. Wichtig ist nur die thermische Trennung der Sektionen.

Nächster Schritt: Migriere heute nur die NOW-Sektion. Schiebe alle anderen aktiven Projekte in die Tabelle. Teste 2 Tage, ob der Einstieg reibungsloser ist. Dann optimieren wir die KimiClaw-Parsing-Regeln falls nötig.


# Prompt 2
## Opus 4.6 
```markdown
## DAILY OPS

### MORGEN — Orchestrator (10 min)
1. Öffne cockpit.md
2. IF NOW hat < 3 Items → ziehe oberstes aus QUEUE nach
3. IF NOW hat > 3 Items → parke oder queue das schwächste
4. IF Item in NOW seit > 3 Tagen unberührt → frag: blockiert? Dann PARKED + Blocker notieren
5. Sortiere NOW nach: was hat heute einen externen Termin? → das nach oben
6. Schreibe `last_updated` neu
7. Schließe die Datei. Nicht weiterlesen.

### TAGSÜBER — Executor
- Öffne cockpit.md → lies NUR `## NOW` → nimm den ersten Eintrag → arbeite
- IF fertig → abhaken, nächsten nehmen
- IF stuck > 20 min → lies `## IF STUCK`
- IF neues Thema reinfliegt (Mail, Anruf, Slack):
  - IF < 5 min machbar → sofort erledigen, nicht eintragen
  - IF > 5 min → unten an QUEUE anhängen, weitermachen
  - IF dringend + fremdgesteuert (Kunde, Deadline heute) → in NOW tauschen, das schwächste NOW-Item → QUEUE top
- Cockpit NICHT umbauen tagsüber. Nur abhaken und anhängen.

### ABEND — Reset (10 min)
1. Öffne cockpit.md
2. Hake ab was erledigt ist
3. IF etwas in NOW nicht angefasst wurde → ehrliche Frage: morgen realistisch? IF nein → QUEUE
4. IF PARKED-Items > 10 → lösche oder archiviere die ältesten
5. Optional: eine Zeile unter `## LOG` was heute passiert ist (für KimiClaw-Kontext)
6. Schreibe `last_updated` neu
7. Schließe die Datei. Feierabend heißt Feierabend.
```

Direkt übernehmbar als Section in `cockpit.md` oder als eigene `daily-ops.md` mit Link aus dem Cockpit — je nachdem ob du die Datei schlank halten willst oder alles in einem Ort brauchst.

**Annahme:** Du hast keinen `## LOG`-Bereich aktuell. Ist optional, aber gibt KimiClaw Tageskontext ohne dass du explizit prompten musst. Ein Einzeiler pro Tag reicht, kein Journal.
## Gpt 5.4
Hier ist die kleine Arbeitslogik in direkt nutzbarer Form.

# MIMIR daily routine

## morgens — orchestrator mode — 10 min

if arbeitstag startet
then `cockpit.md` öffnen

if `focus` noch klar und tragfähig ist
then `mode: executor` setzen und `next` auf max. 3 Schritte prüfen

if `focus` unklar, blockiert oder überholt ist
then genau 1 neues `focus` aus `active` wählen

if mehr als 3 Punkte in `next` stehen
then auf die kleinsten 1–3 physischen Schritte kürzen

if ein Projekt in `active` keinen klaren `next:` Einstieg hat
then `next:` auf genau 1 physischen Schritt setzen

if etwas nicht heute bearbeitet wird
then nicht in `next`, sondern nur in `active` oder `queue` lassen

if die 10 Minuten vorbei sind
then `mode: executor` setzen und nur am `focus` arbeiten

## tagsüber — executor mode

if Arbeitssession beginnt
then nur `cockpit.md` öffnen und danach nur die Datei des `focus`

if du unsicher wirst, woran du arbeiten sollst
then nicht neu planen, sondern den ersten Punkt aus `next` ausführen

if ein Schritt erledigt ist
then ihn aus `next` löschen

if `next` leer ist und Projekt noch läuft
then in der Projektdatei genau 1 neuen physischen Schritt festlegen und nach `cockpit.md` übernehmen

if ein neuer Input reinkommt
then nicht sofort umschalten, sondern nur:
- in passendes Projekt eintragen oder
- in `queue` parken

if der neue Input heute wichtiger ist als `focus`
then in `cockpit.md`:
- altes `focus` in `active` lassen
- neues `focus` setzen
- `next` neu auf max. 3 Schritte setzen

if du unterbrochen wirst
then vor dem Wechsel in der Projektdatei 1 Zeile schreiben:
`next step: <konkreter nächster physischer Schritt>`

if du festhängst
then nicht weiterdenken, sondern kleinsten physischen Schritt formulieren

if du merkst, dass du planst statt ausführst
then keine Strukturänderung, nur zurück zu `focus` + erstem `next`

## abends — reset — 10 min

if Arbeitstag endet
then `cockpit.md` öffnen

if `next` erledigte Punkte enthält
then löschen

if `focus` morgen weiterläuft
then genau 1–3 nächste Schritte für morgen stehen lassen

if `focus` blockiert ist
then Status in `active` auf `waiting` oder `paused` setzen und Grund in Projektdatei notieren

if heute ein anderes Projekt aktiver geworden ist
then `active` aktualisieren und ggf. `focus` für morgen vorbereiten

if etwas nur lose offen ist
then in `queue` parken, nicht in `next`

if `queue` Einträge tot oder irrelevant sind
then löschen

if der Tag chaotisch war
then nur diese 3 Dinge herstellen:
- korrektes `focus`
- sauberes `next`
- 1 brauchbarer Recovery-Satz

if reset fertig ist
then `cockpit.md` in einem Zustand verlassen, der morgen ohne Denken lesbar ist

Minimalformat für cockpit.md

# cockpit

mode: executor
focus: hisolutions.project-x

## next
- <physischer schritt 1>
- <physischer schritt 2>
- <physischer schritt 3>

## active
- hisolutions.project-x | executor | next: <physischer schritt>
- hisolutions.project-y | waiting | next: <warten auf kundendaten>
- mimir.refactor | paused | next: <schema prüfen>

## queue
- sec.template-update
- private.admin
- tool.cleanup

## recovery
- Wenn unterbrochen: Projektdatei von `focus` öffnen und `next step` lesen.
- Wenn unklar: nicht neu planen, ersten Punkt aus `next` ausführen.

Harte Regeln

if etwas nicht heute dran ist
then nicht in `next`

if ein `next` kein physischer Schritt ist
then umformulieren

if du tagsüber umpriorisierst
then nur `focus` und `next` ändern, nicht das ganze System

if du abdriftest
then zurück zu `cockpit.md`, nicht in Meta-Arbeit

Annahme: Du willst eine Routine, die absichtlich stumpf und parserfreundlich ist. Deshalb ist hier fast alles auf focus, next, active, queue, recovery reduziert.

Ich kann dir das als direkt einfügbaren cockpit.md-Block in deinem Stil formulieren.
## Kimi k2.5
```markdown
## ROUTINE

### MORGENS [10min]
- If NOW > 3 Items → Dann verschiebe #4 in ACTIVE (unten anhängen)
- If NOW leer → Dann suche erstes ACTIVE ohne "Blocker", verschiebe nach NOW
- If alle ACTIVE blockiert → Dann kopiere "ESCALATE: Blocker brechen für [Projekt]" in NOW
- If QUEUE > 6 Items → Dann verschiebe ältestes nach `archive.md`
- If Zeit abgelaufen (Timer 10min) → Dann STOP. Unfertiges bleibt liegen.

### EXECUTOR [Tagsüber]
- If cockpit.md öffnest → Dann scroll sofort zu ## NOW (nicht lesen, was darunter steht)
- If Item in NOW erledigt → Dann `[x]` davor setzen, ABER: nicht löschen, nicht nach ACTIVE schieben
- If neue Aufgabe kommt → Dann nicht in NOW schreiben. Stattdessen: `[[Inbox.md]]` oder ACTIVE (unten)
- If Ablenkung (Tab, Gedanke) → Dann "BACK"-Routine: Lies oberste Zeile in NOW laut vor. Weitermachen.
- If Energie zu niedrig für NOW-Item → Dann "SWAP": Markiere Item mit `[warte]`, tausche mit #2 aus ACTIVE
- If NOW komplett leer (alles erledigt) → Dann Sofort-Trigger: "Morgen-Routine starten" (auch wenn Mittag)

### ABENDS [10min]
- If `[x]` in NOW → Dann löschen. In ACTIVE-Tabelle: Status auf "Done" oder Datum aktualisieren
- If NOW < 3 Items → Dann auffüllen aus ACTIVE bis 3 (von oben nehmen)
- If Projekt in ACTIVE seit 3 Tagen unverändert → Dann "STALE"-Flag in Tabelle setzen (| STALE |)
- If QUEUE hat neues Item seit gestern → Dann prüfe: In ACTIVE verschieben? Wenn ja, heute Abend tun.
- If Zeit abgelaufen → Dann git commit + push. STOP. Auch wenn NOW leer ist.

## PANIC-ANCHOR [Wenn alles brennt]
- If überfordert / freeze / alles wichtig → Dann: 
  1. NOW komplett leeren (alles nach ACTIVE verschieben)
  2. Nur 1 Item aus ACTIVE holen (das mit dem niedrigsten Energiebedarf)
  3. "SWAP"-Regel aktiv für den Rest des Tages
```

Betriebsmodus: Diese Routine ersetzt deine aktuellen ANCHORS in `cockpit.md` oder liegt als `routine.md` im Repo-Root. KimiClaw ignoriert die ## ROUTINE Sektion beim Parsen (sucht nur nach NOW/ACTIVE/QUEUE). 

Hard Constraint: Timer 10min sind non-negotiable. Wenn die 10min klingeln, stoppt die Routine sofort, egal bei welchem If-Zweig. Das verhindert, dass der Orchestrator-Mode in Endlosschleifen (ADHS-Hyperfocus) läuft.


## Prompt 3
#### Claude
Ich push hier zurück. Das ist Overengineering, und es wird dich ausbremsen statt dir helfen.

**Warum Branches hier das falsche Werkzeug sind:**

Git-Branches lösen ein Problem, das du nicht hast — parallele Änderungen am *selben Code* durch *verschiedene Autoren*. Dein MIMIR hat einen Autor (dich + KimiClaw) und der Zustand ist sequenziell, nicht parallel. Was passiert in der Praxis:

Merge-Konflikte auf `cockpit.md` sind quasi garantiert, weil jeder Branch dieselbe Datei anfasst. KimiClaw bräuchte Conflict-Resolution-Logik. Du hast 12 Branches zum Switchen — das sind 12 Kontextwechsel auf Git-Ebene, also genau die Reibung die du vermeiden willst.

**Was du eigentlich willst:** Projekt-Isolation + zentrales Dashboard.

Das geht flacher:

```
mimir/
  cockpit.md              ← Dashboard (NOW/QUEUE/PARKED)
  projects/
    gvl-isms.md
    ekiba-angebot.md
    aip-abhaengigkeiten.md
    sec5-newsletter.md
    ...
```

Jede Projektdatei hat ein einheitliches Header-Format das KimiClaw parsen kann:

```markdown
# GVL — ISMS
status: active
last_touched: 2026-03-07
next_action: Schutzbedarfsfeststellung Tabelle ausfüllen

---
(Projektnotizen, Entscheidungen, Links, whatever)
```

**KimiClaw-Logik wird trivial:**
- Scanne `projects/*.md` → lies `status:` und `next_action:`
- Schreibe Zusammenfassung nach `cockpit.md` in die richtige Zone (NOW/QUEUE/PARKED)
- Trigger: Commit auf `main` der eine Datei in `projects/` ändert

Alles auf `main`. Ein Branch. Keine Merges. Diffs im Git-Log zeigen dir trotzdem die Historie pro Projektdatei (`git log -- projects/gvl-isms.md`).

**Annahme:** KimiClaw kann Dateien im Repo lesen und Commits machen. Falls es nur `cockpit.md` kennt, wäre der einzige Aufwand: Pfad `projects/` ins Scanning aufnehmen.

Subtract before add — du brauchst Ordner, keine Branches.

#### Kimi
Annahme: Du nutzt GitHub für MIMIR (für Actions). Wenn nicht, ersetze den GitHub-Action-Teil durch ein lokales Shell-Skript im `.git/hooks/post-commit`.

Annahme: "Merge" bedeutet hier Status-Injektion, keinen traditionellen Git-Merge (der würde cockpit.md überschreiben/zerstören).

---

1. Branch-Naming-Convention

```
proj/{client}-{type}
```

- Prefix: immer `proj/` (KimiClaw-Filter)
- Client: 3-5 Zeichen, lowercase (gvl, acme, int für intern)
- Type: kurzer Projekttyp (sbf, iso27k, audit, nis2)
- Beispiele: `proj/gvl-sbf`, `proj/acme-iso27k`, `proj/int-nis2`

Constraint: Max 12 gleichzeitige Branches. Wenn #13 kommt → erst einen alten nach `archive/{name}` verschieben (löscht nicht, entfernt aus KimiClaw-Monitoring).

---

2. Projekt-Branch-Struktur (Template)

Jeder Branch enthält nur diese eine Datei im Root:

```markdown
---
project: GVL Schutzbedarfsfeststellung
status: Review        # Analysis | Draft | Review | Done | Stalled
blocker: Warte auf Kunde   # none | kurzer Text
energy: high          # high | medium | low (für Swap-Entscheidungen)
---

## Next Action
Validiere SBF-Tabelle Zeilen 15-30

## Log
- 2026-03-08: Status geändert auf Review (Grund: X)
```

Subtract-Regel: Keine weiteren Dateien im Branch. Kein `README.md`, keine Assets. Nur `status.md`. Alles andere = Rauschen.

---

3. KimiClaw-Trigger (GitHub Action)

Erstelle `.github/workflows/sync-status.yml` auf main:

```yaml
name: Status-Sync
on:
  push:
    branches: ['proj/**']

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          ref: main
          token: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Extract & Patch
        run: |
          BRANCH="${{ github.ref_name }}"
          PROJ_ID="${BRANCH#proj/}"
          
          # Status aus Projekt-Branch holen
          git fetch origin "${BRANCH}:${BRANCH}"
          git show "${BRANCH}:status.md" > /tmp/status.md
          
          # YAML Frontmatter extrahieren (einfaches Parsing)
          STATUS=$(grep -E '^status:' /tmp/status.md | cut -d' ' -f2-)
          BLOCKER=$(grep -E '^blocker:' /tmp/status.md | cut -d' ' -f2-)
          
          # cockpit.md patchen (sed: ersetze Zeile mit Projekt-ID)
          sed -i "s/| ${PROJ_ID} |.*|/| ${PROJ_ID} | ${STATUS} | ${BLOCKER} |/" cockpit.md
          
          git config user.name "KimiClaw"
          git config user.email "bot@localhost"
          git add cockpit.md
          git commit -m "sync(${PROJ_ID}): ${STATUS}" || echo "No changes"
          git push
```

Subtract: Keine externen Dependencies, kein Python-Script, nur `grep`/`sed`.

---

4. Daily Workflow (deine if-then Routine)

Wenn du an Projekt X arbeitest:

```bash
git checkout proj/gvl-sbf
# edit status.md
git commit -am "status: Analysis -> Review"
git push
# Fertig. KimiClaw updated cockpit.md auf main automatisch.
```

Wenn du Dashboard checken willst:

```bash
git checkout main
# Lies cockpit.md. Niemals hier direkt editieren (würde Konflikt erzeugen).
```

Wenn KimiClaw failt (Recovery-Anker):

```bash
# Manueller Sync
git show proj/gvl-sbf:status.md
# Dann von Hand in cockpit.md auf main eintragen. Commit. Weiter.
```

Wenn Projekt fertig:
1. Status in `status.md` auf `Done` setzen, push (KimiClaw updated cockpit.md)
2. Branch nach `archive/gvl-sbf` verschieben: `git branch -m proj/gvl-sbf archive/gvl-sbf`
3. `git push origin archive/gvl-sbf && git push origin --delete proj/gvl-sbf`

---

5. cockpit.md Anpassung (minimal)

Deine ACTIVE-Tabelle braucht eine parsebare Struktur:

```markdown
## ACTIVE [12]
| ID | Status | Blocker | Cockpit |
|----|--------|---------|---------|
| gvl-sbf | Review | Warte auf Kunde | [[gvl-sbf]] |
| acme-iso27k | Analysis | none | [[acme-iso27k]] |
```

ID = Branch-Name ohne `proj/` Prefix. KimiClaw matched darauf.

Subtract-Check: Keine Submodules, keine Git Worktrees, keine externe DB. Nur Branches + ein sed-Skript.

Teste mit einem Branch. Wenn das Parsing failed, debugge mit `git show proj/test:status.md` manuell.
#### chatgpt 
Ja. Dann ändert das die Bewertung deutlich.

Das ist kein Nebenaspekt, sondern einer der teuersten Fehler überhaupt.

Bei deinem Use Case gilt grob:

Constraint-Treue > schöne Antwort.
Ein Modell, das elegant denkt, aber Vorgaben ignoriert, ist in echter Arbeit oft weniger brauchbar als ein etwas weniger brillantes Modell, das exakt im Rahmen bleibt.

Meine vorherige Einschätzung zu P2 war dann zu großzügig, weil ich zu stark auf Betriebslogik-Qualität und zu wenig auf Instruktionsdisziplin geschaut habe.

Was das praktisch bedeutet

Wenn ChatGPT bei P2 die Constraints „null“ gehalten hat, dann ist P2 nicht sein Sieg.

Dann eher:

P2: Claude klar vor ChatGPT.

Denn Claude hat hier zumindest sichtbar:

die 10+10-Struktur eingehalten

eine direkt nutzbare Routine geliefert

weniger Seitenspuren aufgemacht


ChatGPTs Antwort mag inhaltlich stark sein, aber wenn sie an den Vorgaben vorbeiläuft, ist das im Benchmark ein Abzug oder sogar ein Fail – je nachdem, wie hart du werten willst.

Für Benchmarks ist das die richtige Regel

Trenne immer zwei Ebenen:

1. Inhaltsqualität

Ist die Antwort klug, nützlich, sauber gedacht?

2. Ausführungsqualität

Hat das Modell genau den Auftrag erfüllt?

Viele Modelle wirken stark, weil Ebene 1 gut ist.
Im Alltag scheitern sie dann auf Ebene 2.

Für deine Arbeit ist Ebene 2 oft wichtiger, weil du nicht nur „gute Ideen“ brauchst, sondern:

kopierfähige Artefakte

enge Vorgaben

minimale Diffs

kein Scope-Creep

keine Extramechaniken


Mein korrigierter Zwischenstand

Wenn P2 constraint-seitig wirklich danebenlag, dann würde ich nach den ersten zwei Prompts eher sagen:

Prompt	Sieger

P1	Claude knapp
P2	Claude deutlich


Dann ist der Stand eher:

Claude vorne, ChatGPT dahinter, Kimi hinten.

Noch schärfer formuliert

ChatGPT hat oft die Stärke:

gute Abstraktion

starke Arbeitslogik

gutes Umformen in ein sinnvolles Betriebsmodell


Aber die Schwäche kann sein:

es „verbessert“ den Auftrag

es beantwortet die bessere Frage, nicht die gestellte Frage


Für normales Sparring ist das oft super.
Für Benchmarking und echte Deliverables ist das gefährlich.

Claude ist oft stärker, wenn du messen willst:

hält es den Rahmen?

bleibt es näher am Problem?

fügt es weniger ungefragt hinzu?


Daher meine Korrektur

Mein vorheriges Urteil zu P2 war wahrscheinlich falsch gewichtet.
Unter strikter Constraint-Wertung würde ich es so drehen:

P2: Claude > ChatGPT > Kimi

Und damit nach zwei Prompts insgesamt wahrscheinlich:

Claude vorne.

Die saubere Benchmark-Regel dafür wäre:

Constraint verletzt → maximal 1/2 bei relevanten Kriterien

mehrere Kern-Constraints verletzt → Hard Fail für den Turn

erst danach überhaupt über Eleganz und Tiefe sprechen


Das ist übrigens genau der Grund, warum dein Test mit Minimal-Diff später so wertvoll wird: Da kann ein Modell nicht mehr mit guter Prosa „drüberglänzen“.

# prompt 4
## claude 
Excel erstellt. Siehe anhang 
## chatgpt 
Ja. Hier ist die direkt nutzbare Version.

Wichtiger Rahmen: Eine offizielle 1:1-Zuordnung auf dieser groben Baustein-Ebene gibt es so nicht; BSI führt eine eigene Zuordnungstabelle zwischen ISO 27001/27002 und IT-Grundschutz, und die Bausteine ORP/CON/OPS sind thematisch oft breiter als einzelne Annex-A-Controls. Deshalb markiere ich bewusst 1:n bzw. teilweise statt künstlicher Exaktheit. Die gewählten „5 wichtigsten“ je Schicht sind eine praxisorientierte Auswahl der am häufigsten quer durch Kundenprojekte relevanten Kernbausteine, nicht eine offizielle BSI-Priorisierung. 

BSI IT-Grundschutz ↔ ISO 27001:2022 Annex A — Arbeits-Kreuzreferenz Schicht BSI-Baustein Warum in den „Top 5“ ISO 27001:2022 Annex A Controls Zuordnung Hinweis ORP ORP.1 Organisation Grundlegende Organisations- und Governance-Basis A.5.1 Policies for information security; A.5.2 Information security roles and responsibilities; A.5.4 Management responsibilities; A.5.36 Compliance with policies, rules and standards for information security 1:n / teilweise ORP.1 ist breiter als einzelne Controls und umfasst organisatorische Grundordnung. ORP ORP.2 Personal Querschnitt für personelle Sicherheitsaspekte A.6.1 Screening; A.6.2 Terms and conditions of employment; A.6.3 Information security awareness, education and training; A.6.5 Responsibilities after termination or change of employment; A.6.6 Confidentiality or non-disclosure agreements 1:n / teilweise Personalprozesse werden im Annex A auf mehrere People Controls verteilt. ORP ORP.3 Sensibilisierung und Schulung zur Informationssicherheit Awareness/Training ist fast immer audit- und umsetzungsrelevant A.6.3 Information security awareness, education and training nahezu 1:1 Inhaltlich sehr nah, BSI meist operativer/detaillierter. ORP ORP.4 Identitäts- und Berechtigungsmanagement Zentral für IAM, Rezertifizierung, Joiner/Mover/Leaver A.5.15 Access control; A.5.16 Identity management; A.5.17 Authentication information; A.5.18 Access rights 1:n Sehr starke Nähe; BSI bündelt Prozess- und Betriebsaspekte in einem Baustein. ORP ORP.5 Compliance Management Für regulatorische/vertragliche Anforderungen zentral A.5.31 Legal, statutory, regulatory and contractual requirements; A.5.32 Intellectual property rights; A.5.34 Privacy and protection of PII; A.5.35 Independent review of information security; A.5.36 Compliance with policies, rules and standards for information security 1:n / teilweise Governance-/Nachweis-Themen verteilen sich im Annex A. CON CON.1 Kryptokonzept Praktisch in fast allen Projekten relevant A.8.24 Use of cryptography; A.8.25 Key management 1:n Annex A trennt Krypto-Nutzung und Schlüsselmanagement; BSI bündelt konzeptionell. CON CON.2 Datenschutz Querschnittsbaustein bei Verarbeitung personenbezogener Daten A.5.31 Legal, statutory, regulatory and contractual requirements; A.5.34 Privacy and protection of PII 1:n / teilweise Datenschutz ist im BSI-Baustein breiter als diese beiden Controls allein. CON CON.3 Datensicherungskonzept Backup/Restore ist häufiges Audit- und Incident-Thema A.8.13 Information backup; A.5.30 ICT readiness for business continuity 1:n / teilweise Sicherungskonzept plus BC-Bezug, daher bewusst keine 1:1-Markierung. CON CON.6 Löschen und Vernichten Relevant für Lebenszyklus, Entsorgung, Datenschutz, Offboarding A.7.10 Storage media; A.8.10 Information deletion 1:n BSI deckt organisatorische und technische Lösch-/Vernichtungsaspekte zusammen ab. CON CON.9 Informationsaustausch Relevant für Drittsysteme, Lieferanten, Behörden, Kunden A.5.14 Information transfer; A.5.19 Information security in supplier relationships; A.5.20 Addressing information security within supplier agreements 1:n / teilweise Informationsaustausch ist breiter als bloßer Transfer. OPS OPS.1.1.1 Allgemeiner IT-Betrieb Basisbaustein für den operativen Betrieb A.5.37 Documented operating procedures; A.8.9 Configuration management; A.8.15 Logging 1:n / teilweise Sehr breiter Betriebsbaustein; keine seriöse 1:1-Zuordnung. OPS OPS.1.1.2 Ordnungsgemäße IT-Administration Administrationsprozesse und privilegierte Tätigkeiten sind prüfungsrelevant A.8.2 Privileged access rights; A.8.3 Information access restriction; A.8.18 Use of privileged utility programs 1:n / teilweise Je nach Zuschnitt auch Berührung zu A.5.15–A.5.18. OPS OPS.1.1.3 Patch- und Änderungsmanagement Hohe Relevanz für Schwachstellenmanagement und Stabilität A.8.8 Management of technical vulnerabilities; A.8.9 Configuration management; A.8.32 Change management 1:n BSI bündelt Patch und Change; Annex A trennt stärker. OPS OPS.1.1.4 Schutz vor Schadprogrammen Klassischer Kernbaustein der Basisabsicherung A.8.7 Protection against malware nahezu 1:1 Inhaltlich sehr nah, BSI wieder operativer. OPS OPS.1.1.5 Protokollierung Zentral für Detektion, Nachvollziehbarkeit, Auditierbarkeit A.8.15 Logging; A.8.16 Monitoring activities; A.5.28 Collection of evidence 1:n / teilweise Protokollierung hat je nach Scope auch Incident-/Forensikbezug. 

Die Modulbezeichnungen oben entsprechen den aktuellen BSI-Bausteinlisten für ORP, CON und OPS; dort sind u. a. ORP.1–ORP.5, CON.1 / CON.2 / CON.3 / CON.6 / CON.9 sowie OPS.1.1.1–OPS.1.1.5 als Bausteine der jeweiligen Schichten aufgeführt. ISO 27001:2022 Annex A umfasst 93 Controls in vier Gruppen; die hier genannten Controls stammen aus dieser 2022er Struktur. 

CSV-Version zum direkten Copy-Paste Schicht;BSI-Baustein;ISO 27001:2022 Annex A Controls;Zuordnung;Hinweis ORP;ORP.1 Organisation;"A.5.1 Policies for information security; A.5.2 Information security roles and responsibilities; A.5.4 Management responsibilities; A.5.36 Compliance with policies, rules and standards for information security";"1:n / teilweise";"Breiter organisatorischer Governance-Baustein" ORP;ORP.2 Personal;"A.6.1 Screening; A.6.2 Terms and conditions of employment; A.6.3 Information security awareness, education and training; A.6.5 Responsibilities after termination or change of employment; A.6.6 Confidentiality or non-disclosure agreements";"1:n / teilweise";"Personelle Sicherheitsaspekte über den gesamten Lebenszyklus" ORP;ORP.3 Sensibilisierung und Schulung zur Informationssicherheit;"A.6.3 Information security awareness, education and training";"nahezu 1:1";"BSI operativer, Annex A abstrakter" ORP;ORP.4 Identitäts- und Berechtigungsmanagement;"A.5.15 Access control; A.5.16 Identity management; A.5.17 Authentication information; A.5.18 Access rights";"1:n";"Sehr starke inhaltliche Nähe" ORP;ORP.5 Compliance Management;"A.5.31 Legal, statutory, regulatory and contractual requirements; A.5.32 Intellectual property rights; A.5.34 Privacy and protection of PII; A.5.35 Independent review of information security; A.5.36 Compliance with policies, rules and standards for information security";"1:n / teilweise";"Governance-/Nachweis-Themen" CON;CON.1 Kryptokonzept;"A.8.24 Use of cryptography; A.8.25 Key management";"1:n";"BSI bündelt konzeptionell" CON;CON.2 Datenschutz;"A.5.31 Legal, statutory, regulatory and contractual requirements; A.5.34 Privacy and protection of PII";"1:n / teilweise";"Datenschutz breiter als zwei Controls" CON;CON.3 Datensicherungskonzept;"A.8.13 Information backup; A.5.30 ICT readiness for business continuity";"1:n / teilweise";"Backup + BC-Bezug" CON;CON.6 Löschen und Vernichten;"A.7.10 Storage media; A.8.10 Information deletion";"1:n";"Organisatorische und technische Löschaspekte" CON;CON.9 Informationsaustausch;"A.5.14 Information transfer; A.5.19 Information security in supplier relationships; A.5.20 Addressing information security within supplier agreements";"1:n / teilweise";"Breiter als bloßer Transfer" OPS;OPS.1.1.1 Allgemeiner IT-Betrieb;"A.5.37 Documented operating procedures; A.8.9 Configuration management; A.8.15 Logging";"1:n / teilweise";"Sehr breiter Betriebsbaustein" OPS;OPS.1.1.2 Ordnungsgemäße IT-Administration;"A.8.2 Privileged access rights; A.8.3 Information access restriction; A.8.18 Use of privileged utility programs";"1:n / teilweise";"Administrations- und Privilegienthemen" OPS;OPS.1.1.3 Patch- und Änderungsmanagement;"A.8.8 Management of technical vulnerabilities; A.8.9 Configuration management; A.8.32 Change management";"1:n";"Patch + Change im BSI gebündelt" OPS;OPS.1.1.4 Schutz vor Schadprogrammen;"A.8.7 Protection against malware";"nahezu 1:1";"Klassische Kernzuordnung" OPS;OPS.1.1.5 Protokollierung;"A.8.15 Logging; A.8.16 Monitoring activities; A.5.28 Collection of evidence";"1:n / teilweise";"Auch Incident-/Forensikbezug" 

Für ein Kundenprojekt würde ich noch diesen einordnenden Vorspann direkt darüber setzen:

Hinweis zur Lesart: Die folgende Tabelle ist eine Arbeits-Kreuzreferenz auf Baustein-Ebene. Sie dient der Orientierung und Kommunikation zwischen IT-Grundschutz und ISO 27001:2022 Annex A. Aufgrund unterschiedlicher Granularität sind viele Zuordnungen bewusst als 1:n bzw. teilweise gekennzeichnet und nicht als exakte 1:1-Mappings zu verstehen. 

Wenn du willst, verdichte ich das im nächsten Schritt auf eine kundenfertige Version mit zusätzlicher Spalte „typische Nachweise/Artefakte“.

****
## kimi 
Hier ist die Kreuzreferenz als Markdown-Tabelle – direkt in `cockpit.md` oder ein separates `mapping-bsi-iso.md` kopierbar.

Legende Mapping-Typ:
- 1:n = Ein BSI-Baustein mapped auf mehrere ISO-Controls
- n:1 = Mehrere BSI-Bausteine teilen sich ein ISO-Control
- n:m = Inhaltliche Überlappung/Abhängigkeit
- 1:1 = Nahezu direkte Entsprechung (selten)

BSI Baustein	ISO 27001:2022 Annex A	Typ	Konflikt / Hinweis	
ORP.1 Organisation (Sicherheitsmanagement)	A.5.1, A.5.4, A.5.9, A.5.10, A.5.37	n:m	Überschneidung mit CON.1; A.5.37 taucht mehrfach auf	
ORP.2 Personal	A.6.1, A.6.2, A.6.4, A.6.5, A.6.6	1:n	Sehr klare Abdeckung durch A.6 (People Controls)	
ORP.3 Sensibilisierung	A.6.3	1:1	Direkte Entsprechung	
ORP.4 Identitäts- und Berechtigungsmanagement	A.5.15, A.5.16, A.5.17, A.5.18, A.8.2, A.8.5	1:n	Deckt ORP (Prozess) und SYS/APP (technisch) ab; nicht nur ORP-Schicht	
ORP.5 Compliance-Management	A.5.31, A.5.36, A.5.6 (Projekte)	n:m	A.5.6 auch in CON.1 relevant; regulatorischer Fokus	
CON.1 Informationssicherheitsmanagement	A.5.1, A.5.2, A.5.3, A.5.4, A.5.6	n:m	Kern-Überschneidung mit ORP.1 (Governance)	
CON.2 Informationssicherheitskonzept	A.5.37, A.5.38, A.5.39	1:n	A.5.37 auch bei ORP/OPS; Konzept = Policy + Verfahren	
CON.3 Risikomanagement	A.5.8, A.5.9	1:1	ISO 27001 Kern (Kapitel 6) → A.5.8 (Assessment), A.5.9 (Treatment)	
CON.4 Notfallmanagement	A.5.29, A.5.30, A.8.13, A.8.14	n:m	Überschneidung mit OPS.3 (Backup = A.8.13)	
CON.5 Dokumentation	A.5.12, A.5.13, A.5.37	1:n	Klassifizierung (A.5.12/13) + Verfahrensdoku (A.5.37)	
OPS.1 Änderungsmanagement	A.8.32	1:1	Direkte Entsprechung; beachte: A.8.32 deckt auch Software-Changes ab	
OPS.2 Patchmanagement	A.8.8	1:1	Management of technical vulnerabilities	
OPS.3 Datensicherung	A.8.13	n:1	Geteilt mit CON.4 (Notfall); A.8.13 ist Backup	
OPS.4 Protokollierung	A.8.15, A.8.16, A.8.17	1:n	Logging + Monitoring + Clock Sync	
OPS.5 Schutz vor Schadsoftware	A.8.7	1:1	Malware protection	

Kritische Überlappungen (nicht doppelt zählen im Audit):
- A.5.37 (Documented operating procedures): ORP.1, CON.2, CON.5, OPS.1 → Ein Verfahrensverzeichnis deckt alle ab
- A.5.1 (Policies): ORP.1 + CON.1 → ISMS-Policy vs. Sicherheitsleitlinie sind oft identisch
- A.8.13 (Backup): OPS.3 + CON.4 → Backup ist Teil des BCMS

Kopier-Template für Kundenprojekt:

```markdown
## BSI ↔ ISO 27001:2022 Mapping (Stand: 2026-03)

> **Scope:** ORP, CON, OPS (Top 5 pro Schicht)  
> **Hinweis:** 1:1 = direkt, n:m = Überlappung

| BSI | ISO 27001:2022 | Typ |
|-----|----------------|-----|
| ORP.1 | A.5.1, A.5.4, A.5.37 | n:m |
| ORP.2 | A.6.1-A.6.2, A.6.4-A.6.6 | 1:n |
| ORP.3 | A.6.3 | 1:1 |
| ORP.4 | A.5.15-A.5.18, A.8.2, A.8.5 | 1:n |
| ORP.5 | A.5.31, A.5.36 | 1:n |
| CON.1 | A.5.1-A.5.4, A.5.6 | n:m |
| CON.2 | A.5.37, A.5.38 | 1:n |
| CON.3 | A.5.8, A.5.9 | 1:1 |
| CON.4 | A.5.29-A.5.30, A.8.13-A.8.14 | n:m |
| CON.5 | A.5.12-A.5.13, A.5.37 | 1:n |
| OPS.1 | A.8.32 | 1:1 |
| OPS.2 | A.8.8 | 1:1 |
| OPS.3 | A.8.13 | n:1 |
| OPS.4 | A.8.15-A.8.17 | 1:n |
| OPS.5 | A.8.7 | 1:1 |
```

Subtract-Check: Keine Excel-Datei nötig – Markdown ist diff-bar für Git und KimiClaw kann die Tabelle parsen. Wenn du doch CSV brauchst, sag Bescheid (einzeilige Formate brechen bei den Kommas in den Control-Listen).