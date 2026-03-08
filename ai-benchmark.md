# Model Comparison v4: PKM & Consulting Focus — Merged Benchmark
## Claude Max (Opus 4.6) vs Kimi K2.5 Allegretto vs ChatGPT 5.4

**Datum:** ___  
**Dauer:** ___  
**Setup:** Alle Modelle ohne vorherigen Session-Kontext. Identischen Kontext-Prompt zu Beginn einfügen. Sequentielle Prompt-Chain ohne Umformulierung. Bewertung erst nach kompletter Session.

---

## Ziel der v4

Diese v4 kombiniert zwei Testlogiken:
- **Realitätsdruck-Test:** abrupte Pivots, Telefon-/Kundenlogik, echter Pushback-Bedarf
- **Präzisions-Test:** strukturierte Artefakte, Constraint-Treue, Minimal-Diff-Editing

Sie misst nicht "welches Modell ist allgemein am klügsten", sondern:
1. Welches Modell taugt für **ambige Consulting-Situationen**?
2. Welches Modell taugt für **PKM-/Markdown-/Artefakt-Arbeit**?
3. Welches Modell respektiert **ADHS-taugliche Arbeitslogik** ohne Overengineering?

---

## Kontext-Prompt (für alle drei Models identisch)

> Ich bin InfoSec Consultant bei HiSolutions. Spezialisierung: ISO 27001, BSI IT-Grundschutz, NIS2, DSGVO. Ich nutze ein PKM-System namens MIMIR — ein GitHub-basiertes Markdown-Repo mit einer zentralen `cockpit.md` als Zustandsdatei, Orchestrator/Executor-Modes und if-then Recovery-Ankern. Optimiert für ADHS Combined Type: ich denke durch Externalisieren, brauche klare Einstiegspunkte, niedrige Reibung und wenig Kontextwechselkosten. Ich arbeite auf Deutsch, wechsle zu Englisch wenn es fachlich passt. Bitte markiere Annahmen als Annahmen und vermeide Overengineering. Subtract before add.

---

## Testregeln

- Keine Nachschärfung zwischen den Prompts.
- Keine Zusatzhinweise an nur ein Modell.
- Gleiche Reihenfolge für alle drei Modelle.
- Keine Webrecherche erzwingen; bewertet wird die Session-Leistung im jeweiligen Produkt.
- Falls ein Modell eine Datei erzeugen will: auch okay. Wenn nicht, muss der Output trotzdem copy-paste-fähig sein.
- Erst **Hard-Fails** markieren, danach Punkte vergeben.

---

## Bewertungslogik

### Skala je Kriterium
- **0 = schwach** — verfehlt den Kern, unsauber, unpraktisch oder klar unter dem Nutzwert
- **1 = solide** — brauchbar, aber mit Lücken, Umwegen oder Nacharbeit
- **2 = stark** — direkt nutzbar, präzise, sauber priorisiert, guter Fit für den Use Case

### Kriterien

| Kürzel | Kriterium | Was wird getestet? |
|---|---|---|
| K1 | Domänentiefe | Korrektheit und Tiefe bei InfoSec/Compliance/ISMS |
| K2 | Strukturqualität | Klarheit, Navigierbarkeit, Chunking, Formatierung |
| K3 | ADHS-Tauglichkeit | Klare Einstiegspunkte, niedrige Reibung, if-then statt Theorie |
| K4 | Pushback-Fähigkeit | Erkennt Fehlannahmen/Overengineering und widerspricht sinnvoll |
| K5 | Pivot-Handling | Themenwechsel ohne Kontextverlust, greift frühere Fäden sauber wieder auf |
| K6 | Praxisnähe | Direkt einsetzbar in realer Consulting-Arbeit |
| K7 | Output-Qualität | Tabellen/Markdown/CSV/Artefakte sind belastbar und copy-paste-ready |
| K8 | Präzisions-Editing | Ändert gezielt nur das Gewünschte, ohne Drift |
| K9 | Ehrlichkeit bei Unsicherheit | Markiert Unsicherheit/Annahmen statt zu halluzinieren |

---

## Hard-Fail-Flags

Diese Flags sind wichtiger als Einzelscores.

| Flag | Beschreibung |
|---|---|
| HF1 | **Kein Pushback**, obwohl der Prompt klar Overengineering oder eine schlechte Idee enthält |
| HF2 | **Verletzt Minimal-Diff-Constraint** und ändert mehr als gefordert |
| HF3 | Gibt **sicher klingende Compliance-/Rechtsaussagen** ohne Unsicherheitsmarkierung, obwohl die Lage offenkundig differenziert ist |
| HF4 | Liefert ein **PKM-Design mit unnötiger Komplexität**, das den stated constraints widerspricht |
| HF5 | Ignoriert den Session-Kontext beim Rücksprung und behandelt spätere Prompts wie isolierte Einzelaufgaben |

**Auswertungsregel:** Hard-Fails separat notieren und im Fazit höher gewichten als 1–2 Punkte Unterschied in Einzelscores.

---

## Prompt Chain (8 Messages)

### P1 — MIMIR Cockpit Refactoring
**Testet:** K2, K3, K6  
**Typ:** PKM-Optimierung unter ADHS-Constraints

```text
Mein MIMIR cockpit.md ist auf 47 Zeilen gewachsen. 12 aktive Projekte,
6 Warteschlange, Rest sind Metadaten und Recovery-Anker. Ich verliere
den Überblick beim Öffnen — zu viel auf einmal.

Wie refaktoriere ich das, ohne den "Single Entry Point"-Vorteil zu
verlieren? Constraint: KimiClaw (mein Always-On Agent) muss die Datei
weiterhin parsen können, also keine zu cleveren Strukturen.
```

**Worauf achten:**
- Schlägt das Modell eine klare visuelle Hierarchie vor?
- Bleibt es in einfachem, parsbarem Markdown?
- Ist die Lösung ADHS-tauglich oder nur formal ordentlich?

---

### P2 — Arbeitslogik aus dem Refactoring ableiten
**Testet:** K3, K6  
**Typ:** Operationalisierung statt Theorie

```text
Gut. Mach daraus jetzt eine konkrete Arbeitslogik für meinen Alltag:

- morgens 10 Minuten Orchestrator-Mode
- abends 10 Minuten Reset
- tagsüber Executor-Mode

Ich will keine Prinzipien. Gib mir eine kleine if-then Routine, die ich
sofort in MIMIR übernehmen kann.
```

**Worauf achten:**
- Liefert das Modell echte Handlungslogik statt abstrakter Gewohnheiten?
- Sind die Schritte klein genug für reale Nutzung?
- Bleibt es kompatibel mit P1?

---

### P3 — Pushback-Test: absichtlich schlechte PKM-Idee
**Testet:** K4, K3, K6  
**Typ:** echter Pushback-Trap

```text
Ich will für jedes meiner 12 aktiven Projekte einen eigenen Git-Branch
in MIMIR anlegen. KimiClaw merged automatisch nach cockpit.md wenn ein
Projekt-Status sich ändert. So habe ich perfekte Isolation und trotzdem
ein zentrales Dashboard.

Hilf mir das aufzusetzen — Branch-Naming-Convention, Merge-Strategie
und KimiClaw-Trigger.
```

**Worauf achten:**
- Das Modell **sollte widersprechen**.
- Erkennt es Merge-Konflikte, Wartungsaufwand und unnötige Komplexität?
- Bietet es eine einfachere Alternative an?

---

### P4 — BSI ↔ ISO Kreuzreferenz (Artefakt-Turn)
**Testet:** K1, K7, K9  
**Typ:** strukturierter Output + Domänennähe

```text
Erstelle mir eine Kreuzreferenztabelle: BSI IT-Grundschutz Bausteine
(Schicht ORP, CON, OPS — jeweils die 5 wichtigsten) ↔ ISO 27001:2022
Annex A Controls.

Format: Was auch immer am besten funktioniert — Excel, Markdown-Tabelle
oder CSV. Hauptsache ich kann es direkt in ein Kundenprojekt kopieren.

Wenn Zuordnungen nicht 1:1 sind, markiere das sauber statt so zu tun als
wäre es exakt.
```

**Worauf achten:**
- Wählt das Modell ein sinnvolles Format?
- Sind die Mappings plausibel und sauber relativiert?
- Markiert es nicht-exakte Zuordnungen ehrlich?

---

### P5 — Minimal-Diff-Edit auf dem Artefakt
**Testet:** K8, K7, K9  
**Typ:** Präzisions-Editing statt Neuformulierung

```text
Ändere NUR diese Punkte an deiner letzten Kreuzreferenz und sonst nichts:

1. Ergänze eine Spalte "Mapping-Typ" mit den Werten: direkt / teilweise /
   organisatorisch flankierend.
2. Markiere ORP-Bausteine konsistent als organisatorische Controls, wenn
   kein technisches 1:1-Mapping vorliegt.
3. Füge genau eine kurze Fußnote hinzu: "Kein normatives 1:1-Mapping; nur
   Arbeitszuordnung für Projektpraxis."
4. Gib das Ergebnis im gleichen Format wie eben aus.

Keine Neustrukturierung. Keine zusätzlichen Erläuterungen. Kein Re-Write.
```

**Worauf achten:**
- Hält das Modell die Änderungsgrenzen ein?
- Bleibt Format und Struktur stabil?
- Driftet es in neue Erklärtexte ab?

---

### P6 — Harter Pivot: Ransomware-Meldepflicht
**Testet:** K1, K5, K6, K9  
**Typ:** abrupter Themenwechsel wie im Consulting-Alltag

```text
Stopp, anderes Thema. Dringend.

Kunde ruft an: "Wir hatten am Wochenende einen Ransomware-Vorfall.
Systeme verschlüsselt, Backup läuft. Wir sind Zulieferer für einen
KRITIS-Betreiber, aber selbst nicht als KRITIS eingestuft. Müssen wir
das irgendwo melden? Wenn ja, wo und in welcher Frist?"

Gib mir eine Antwort die ich am Telefon geben kann — kein Aufsatz,
sondern Punkte die ich ablesen kann. Wenn etwas von Einordnung oder
Sonderfall abhängt, sag es klar.
```

**Worauf achten:**
- Erkennt das Modell mehrere mögliche Meldewege?
- Differenziert es sauber zwischen eigener Betroffenheit, Lieferkette,
  Datenschutzbezug und möglicher regulatorischer Einordnung?
- Ist die Antwort telefonfähig und gleichzeitig ehrlich bei Unsicherheit?

---

### P7 — ISMS Scope Decision unter Zeitdruck
**Testet:** K3, K6, K1  
**Typ:** strukturierte Entscheidung statt Framework-Rezitation

```text
Ich muss für einen Kunden (Verwertungsgesellschaft, ~80 MA, hybrides
Arbeiten) den ISMS-Scope festlegen. Zwei Optionen:

A) Gesamte Organisation
B) Nur IT-Betrieb + die 3 kritischsten Geschäftsprozesse

Ich habe in 20 Minuten einen Call mit dem Kunden. Gib mir kein
Grundlagen-Framework — gib mir die 4-5 konkreten Fragen die ich im
Call stellen muss, und für jede Frage das Decision-Signal:

Wenn Antwort X → Scope A
Wenn Antwort Y → Scope B
```

**Worauf achten:**
- Liefert das Modell echte If-Then-Entscheidungshilfen?
- Ist es in 20 Minuten anwendbar?
- Versteht es die Scope-Frage praktisch, nicht akademisch?

---

### P8 — Synthese: MIMIR + ISMS + Session-Rückgriff
**Testet:** K5, K3, K6, K7  
**Typ:** Rückverknüpfung über die Session

```text
Zurück zu MIMIR. Nimm das Cockpit-Refactoring vom Anfang und die
ISMS-Scope-Entscheidung von eben zusammen:

Wie bilde ich ISMS-Projektsteuerung (Maßnahmenverfolgung,
Audit-Vorbereitung, Dokumentenstatus) in MIMIR ab? Ich will kein
zweites Tool, sondern das in mein bestehendes System integrieren.

Gib mir eine Beispiel-Dateistruktur mit 3-5 Markdown-Dateien plus
1 Beispiel für cockpit.md-Statusblöcke.
```

**Worauf achten:**
- Greift das Modell sauber auf P1/P2 zurück?
- Verbindet es Scope-/ISMS-Realität mit PKM-Struktur?
- Bleibt die Lösung schlank statt erneut overengineered?

---

### Optional P9 — Selbstbewertung (niedrig gewichten)
**Testet:** K4 indirekt, Meta-Ehrlichkeit  
**Typ:** Zusatzsignal, nicht Hauptsignal

```text
Bewerte deine eigene Performance in dieser Session.

- Wo warst du am stärksten?
- Wo hättest du besser sein können?
- Gab es einen Punkt, wo du unsicher warst, aber trotzdem geliefert hast?

Sei ehrlich, nicht höflich.
```

**Hinweis:** Nur als Zusatzsignal verwenden. Nicht stark gewichten.

---

## Ergebnis-Matrix

### Einzelbewertungen (0 = schwach, 1 = solide, 2 = stark)

| Prompt | Relevante Kriterien | Claude | Kimi | ChatGPT | Notizen |
|--------|---------------------|--------|------|---------|---------|
| **P1** Cockpit Refactoring | K2, K3, K6 | _ / _ / _ | _ / _ / _ | _ / _ / _ | |
| **P2** Arbeitslogik | K3, K6 | _ / _ | _ / _ | _ / _ | |
| **P3** Pushback-Trap | K4, K3, K6 | _ / _ / _ | _ / _ / _ | _ / _ / _ | |
| **P4** BSI ↔ ISO Artefakt | K1, K7, K9 | _ / _ / _ | _ / _ / _ | _ / _ / _ | |
| **P5** Minimal-Diff | K8, K7, K9 | _ / _ / _ | _ / _ / _ | _ / _ / _ | |
| **P6** Ransomware Pivot | K1, K5, K6, K9 | _ / _ / _ / _ | _ / _ / _ / _ | _ / _ / _ / _ | |
| **P7** Scope Decision | K3, K6, K1 | _ / _ / _ | _ / _ / _ | _ / _ / _ | |
| **P8** MIMIR + ISMS Synthese | K5, K3, K6, K7 | _ / _ / _ / _ | _ / _ / _ / _ | _ / _ / _ / _ | |
| **P9** Selbstbewertung (optional) | Zusatzsignal | _ | _ | _ | |

---

## Hard-Fail-Protokoll

| Modell | HF1 Kein Pushback | HF2 Minimal-Diff verletzt | HF3 Unsichere Compliance-Aussage als sicher verkauft | HF4 PKM overengineered | HF5 Kontextbruch | Notizen |
|---|---|---|---|---|---|---|
| Claude | ☐ | ☐ | ☐ | ☐ | ☐ | |
| Kimi | ☐ | ☐ | ☐ | ☐ | ☐ | |
| ChatGPT | ☐ | ☐ | ☐ | ☐ | ☐ | |

---

## Gesamtprofil nach Kriterien

| Kriterium | Claude | Kimi | ChatGPT |
|-----------|--------|------|---------|
| K1 Domänentiefe | | | |
| K2 Strukturqualität | | | |
| K3 ADHS-Tauglichkeit | | | |
| K4 Pushback-Fähigkeit | | | |
| K5 Pivot-Handling | | | |
| K6 Praxisnähe | | | |
| K7 Output-Qualität | | | |
| K8 Präzisions-Editing | | | |
| K9 Ehrlichkeit bei Unsicherheit | | | |
| **Hard-Fails gesamt** | | | |
| **Gesamteindruck** | | | |

---

## Auswertungshinweise

### Claude
**Typischerweise prüfen:**
- Stark bei Ambiguität, aber driftet es bei Minimal-Diff?
- Gibt es echten Pushback oder höfliche Mitarbeit an schlechten Ideen?
- Wie präzise sind die Compliance-Differenzierungen unter Zeitdruck?

### Kimi
**Typischerweise prüfen:**
- Sehr steuerbar bei Struktur: hält es die Constraints auch unter Pivot?
- Ist Domänentiefe belastbar oder nur formschön?
- Bleibt es bei Synthese-Aufgaben kohärent?

### ChatGPT 5.4
**Typischerweise prüfen:**
- Gute Analyse und Struktur: bleibt es praktisch genug?
- Liefert es Pushback klar genug oder zu moderat?
- Ist es bei Artefakt-Editing diszipliniert statt neu zu schreiben?

---

## Beobachtungen (Freitext)

### Claude
**Stärken:**  


**Schwächen:**  


**Überraschungen:**  


### Kimi
**Stärken:**  


**Schwächen:**  


**Überraschungen:**  


### ChatGPT 5.4
**Stärken:**  


**Schwächen:**  


**Überraschungen:**  

---

## Fazit & Stack-Entscheidung

### Rollenverteilung (nach Test)

| Rolle | Model | Begründung |
|-------|-------|------------|
| Thinking Partner (ambig, komplex) | | |
| Structured Output (Tabellen, Files) | | |
| Domänen-Sparring (InfoSec deep dives) | | |
| Quick Consulting (Telefon-Support) | | |
| PKM/Workflow Design | | |
| Präzisions-Editing | | |

### Kostenoptimierung

| Stack-Option | Kosten/Monat | Abdeckung |
|--------------|-------------|-----------|
| Claude Max + Kimi | €136 | |
| Claude Pro + Kimi | €47 | |
| Claude Pro + ChatGPT Plus | €47 | |
| Claude Pro + Kimi + ChatGPT (1 Monat) | €67 | |
| Nur Claude Max | €109 | |

### Entscheidung
___

### Nächste Schritte
1. ___
2. ___
3. ___

---

*Erstellt mit MIMIR Model Comparison Framework v4 (Merged Benchmark)*  
*Methodik: identischer Kontext-Prompt, sequentielle Prompt-Chain, Hard-Fail-first, danach Punktwertung*  
*Designziel: Realitätsdruck + Präzision statt Scheingenauigkeit*

