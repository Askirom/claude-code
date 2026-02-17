# InfoSec Consulting Assessment — Multi-Task Response

---

## Task 1: Regulatory Cross-Framework Analysis — DORA Gap Analysis

### Context

BSI IT-Grundschutz + ISO 27001 certification provides a solid foundation, but DORA
(Regulation (EU) 2022/2554, applicable since January 2025) introduces obligations that
are either entirely absent from Grundschutz or exist only in weaker, advisory form.
Below is a frank gap analysis organized by DORA pillar.

---

### Gap 1: ICT-Related Incident Classification and Reporting (DORA Art. 17–23) — **CRITICAL GAP**

**What DORA requires:**
- A formal taxonomy for classifying ICT incidents as "major" vs. non-major using
  specific criteria (user impact, data loss duration, geographic spread, criticality
  of services affected).
- Mandatory reporting timelines: initial notification to BaFin within **4 hours** of
  classifying an incident as major; intermediate report within **72 hours**; final
  report within **1 month**.
- A dedicated reporting channel and process to the competent authority (BaFin for
  most German financial entities).

**What Grundschutz covers:**
- DER.2.1 (Incident Management) covers incident detection and response — but focuses
  on operational handling, not regulatory reporting timelines.
- There is no Grundschutz building block that mandates sub-4-hour external regulatory
  notification or prescribes a DORA-specific severity taxonomy.

**Your actual pain point:**
Your incident management process almost certainly lacks the formal classification
criteria that trigger regulatory reporting, the tested escalation path to reach BaFin
within 4 hours, and the template-based reporting artifacts DORA requires. This is a
documentation and process gap, not a technical one — but it needs a new SOP and
potentially a contractual commitment from your SOC or MSSP.

**Action:** Draft a DORA Incident Classification Matrix keyed to DORA Art. 18(1)
criteria. Run a tabletop exercise against it before Q3 2025.

---

### Gap 2: Digital Operational Resilience Testing (DORA Art. 24–27) — **SIGNIFICANT GAP**

**What DORA requires:**
- Annual Basic DRET (Digital Resilience Testing) for all entities: vulnerability
  assessments, network security assessments, gap analyses, physical security reviews,
  scenario-based tests.
- Threat-Led Penetration Testing (TLPT) every **3 years** for significant entities
  (check with BaFin whether your firm qualifies — "wichtige Einrichtung" under NIS2
  doesn't automatically map 1:1 to DORA's TLPT scope criteria).
- TLPT must follow the **TIBER-EU** framework (Germany: TIBER-DE), conducted by
  approved external testers with threat intelligence from approved providers.

**What Grundschutz covers:**
- DER.3.1 (Penetration Testing) recommends pen tests but imposes no frequency mandate,
  no TIBER methodology requirement, and no regulator notification obligation.

**Your actual pain point:**
If you have existing pen tests, they likely don't meet TIBER-EU methodology
requirements and weren't conducted with a threat-intelligence-led scope. You'll need
to engage a TIBER-DE approved Red Team provider and coordinate with BaFin on scope
approval — a process that takes months to arrange. Start now.

---

### Gap 3: ICT Third-Party Risk Management (DORA Art. 28–44) — **LARGEST GAP FOR MOST FIRMS**

**What DORA requires:**
- A **Register of Information** (RoI) — a structured inventory of all ICT third-party
  service providers with contractual details, service criticality assessments, and
  subcontractor chains. This must be submitted to BaFin in a prescribed format.
- Mandatory contractual clauses in all ICT provider agreements (Art. 30): audit
  rights, exit strategies, data location, SLAs tied to DORA definitions, incident
  reporting obligations of the provider to you.
- For **critical ICT third-party providers** (CTPPs designated by ESAs): additional
  oversight requirements.
- Documented exit strategies and concentration risk analysis (Art. 29).

**What Grundschutz covers:**
- OPS.2.3 (Service Provider Management) covers supplier management but has no concept
  of a structured Register of Information, no DORA-mandated contractual clause
  checklist, and no exit strategy documentation requirement.

**Your actual pain point:**
Most German financial firms have significant contractual rework ahead. Existing
vendor contracts — especially legacy cloud and SaaS agreements — will not contain
DORA Art. 30 clauses. Renegotiating with large vendors (AWS, Microsoft, SAP) is slow.
Begin contract auditing immediately and prioritize renegotiation by provider criticality.
The RoI itself requires a dedicated data collection project — don't underestimate scope.

---

### Gap 4: ICT Business Continuity and Disaster Recovery (DORA Art. 11–12) — **MODERATE GAP**

**What DORA requires:**
- Business continuity plans specifically for ICT disruption scenarios (not just general
  BCP).
- Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO) must be
  explicitly documented and tested for critical functions.
- ICT continuity plans must be tested at least **annually** and after major incidents
  or significant operational changes.
- Communication plans covering staff, external providers, and clients during ICT crises.

**What Grundschutz covers:**
- BSI-Standard 200-4 (Business Continuity Management) covers BCP well. If you're fully
  implementing Grundschutz BCM, you're closer here than most.

**Your actual pain point:**
The gap is usually in ICT-specificity: existing BCPs often cover physical disasters
or HR scenarios better than pure ICT failure. Check whether your BCP documents
explicitly define RTO/RPO per critical ICT service and whether annual ICT-specific
tests are actually being run (not just physical evacuation drills).

---

### Gap 5: Governance and Management Accountability (DORA Art. 5–9) — **STRUCTURAL GAP**

**What DORA requires:**
- The **management body** (Geschäftsführung/Vorstand) must formally approve the ICT
  risk management framework and bears personal accountability for it.
- Regular reporting to the management body on ICT risk — not just to the CISO or IT
  board.
- A defined ICT risk management framework as a standalone document (not embedded in
  a general ISMS policy).

**What Grundschutz covers:**
- ISMS.1 requires management commitment, but Grundschutz doesn't mandate the specific
  governance structure, reporting cadence to management body, or personal liability
  framing that DORA establishes.

**Your actual pain point:**
If your Vorstand/Geschäftsführung currently signs off on the ISMS policy once a year
and otherwise delegates everything to IT and the CISO, that is insufficient under
DORA. You need a formal quarterly ICT risk reporting process into the management body,
documented in board minutes.

---

### Summary: Prioritized Action List

| Priority | Gap Area | Effort | Deadline |
|----------|----------|--------|----------|
| 1 | ICT Third-Party Risk / Register of Information | High | Start now |
| 2 | Incident Classification + Regulatory Reporting | Medium | Q1 2025 |
| 3 | Governance / Management Body Reporting | Low-Medium | Q1 2025 |
| 4 | DRET Testing Program | Medium | Q2 2025 |
| 5 | ICT-specific BCP/RTO/RPO review | Medium | Q2 2025 |
| 6 | TLPT (TIBER-DE) if applicable | High | Begin scoping now |

---

## Task 2: Client Email — Passwortrichtlinie (Deutsch)

---

**Betreff:** Ihre Passwortstrategie — eine wichtige Aktualisierung

Sehr geehrter Herr [Name],

zunächst möchte ich Ihnen ein ehrliches Kompliment aussprechen: Eine explizite
Passwortrichtlinie zu haben ist bereits besser als das, was wir bei vielen Unternehmen
Ihrer Größe vorfinden. Dass Sie das Thema ernst nehmen, sieht man.

Genau deshalb möchte ich Ihnen etwas Wichtiges mitteilen — im Vertrauen und mit aller
gebotenen Offenheit: Die Sicherheitswissenschaft hat in den letzten Jahren ihre Empfehlung
zu Passwortrichtlinien grundlegend revidiert. Was früher als Best Practice galt —
kurze Wechselintervalle, erzwungene Komplexität bei 8 Zeichen — gilt heute als
kontraproduktiv. Das ist kein Versagen Ihrer bisherigen Entscheidung; es ist eine
Branche, die dazugelernt hat.

Der Grund ist einfach: Menschen, die alle 90 Tage ein neues "komplexes" Passwort
erstellen müssen, wählen vorhersehbare Muster — aus Erschöpfung. Angreifer kennen
diese Muster. Das Bundesamt für Sicherheit in der Informationstechnik (BSI) und das
amerikanische NIST empfehlen heute stattdessen: **längere Passphrasen** (16+ Zeichen),
die sich Menschen merken können, kombiniert mit **Zwei-Faktor-Authentifizierung** — und
nur dann einen Wechsel, wenn ein Passwort kompromittiert wurde.

Ich würde Ihnen gerne in einem kurzen Gespräch zeigen, wie eine moderne Richtlinie
bei Ihnen konkret aussehen würde — sicher, praktikabel und für Ihre Mitarbeitenden
ohne großen Aufwand umsetzbar.

Mit freundlichen Grüßen,
[Ihr Name]

---

## Task 3: Whistleblower-System — Lösungsarchitektur

### Das Dilemma

Drei Parteien mit legitimen, aber scheinbar unvereinbaren Interessen:

- **Management:** Gesetzliche Pflicht (HinSchG), Haftungsrisiko bei Nichterfüllung.
- **Betriebsrat:** Begründete Sorge vor Arbeitnehmerüberwachung und Missbrauch.
- **Datenschutzbeauftragter:** Datenschutzrechtliche Bedenken zur Datenminimierung
  und Zweckbindung.

### Lösungsarchitektur: "Structural Separation Model"

**Prinzip:** Das System wird so gebaut, dass eine missbräuchliche Nutzung zur
Mitarbeiterüberwachung *technisch und organisatorisch unmöglich* gemacht wird —
nicht nur durch Versprechen, sondern durch Architektur.

---

**Schicht 1: Technische Isolation**

- Einführung eines **externen, unabhängigen Ombudssystems** (z.B. über eine
  spezialisierte Anwaltskanzlei oder einen zertifizierten Drittanbieter wie EQS,
  BKMS oder Convercent).
- Der Anbieter erhält **keine** direkten Zugangsdaten zum Unternehmensnetz; es gibt
  keine SSO-Integration, keine Active-Directory-Anbindung, keine Korrelationsmöglichkeit
  mit HR-Systemen.
- Meldungen werden zunächst beim externen Ombudsmann gespeichert und nur bei
  Vorliegen eines tatsächlichen Compliance-Sachverhalts — nach klar definierten
  Kriterien — anonymisiert an die interne Compliance-Stelle weitergeleitet.

**Schicht 2: Organisatorische Governance mit Betriebsrats-Beteiligung**

- Der Betriebsrat erhält **Mitbestimmung** über die konkrete Ausgestaltung der
  Zugriffsberechtigungen (§ 87 Abs. 1 Nr. 6 BetrVG — ohnehin erforderlich).
- Eine **Betriebsvereinbarung** wird ausgehandelt, die explizit und abschließend
  festlegt, welche Meldekategorien zulässig sind (Compliance-Verstöße, keine
  allgemeinen Beschwerden über Kollegen) und welche nicht.
- Ein **paritätischer Kontrollausschuss** (je ein Vertreter: Management, Betriebsrat,
  DSB) erhält vierteljährlich anonymisierte Statistiken und kann Systemlogs prüfen.
  Kein Mitglied allein hat vollständigen Zugriff.

**Schicht 3: Datenschutz by Design**

- Das System speichert **keine** IP-Adressen, keine Metadaten, die Rückschlüsse auf
  die meldende Person ermöglichen.
- Technische Umsetzung der Anonymität gemäß DSGVO Art. 25 (Privacy by Design) wird
  vom DSB geprüft und schriftlich bestätigt — der DSB wird damit zum Mitarchitekten,
  nicht zum Verhinderer.
- Klare, schriftlich vereinbarte **Löschfristen** für alle Meldedaten.

**Schicht 4: Transparenzkommunikation**

- Eine Betriebsversammlung, in der das System durch den externen Ombudsmann —
  nicht durch Management — erklärt wird.
- Ein schriftliches "Missbrauchsverbot"-Dokument, das auch dem Betriebsrat übergeben
  wird und rechtlich bindend ist.

---

**Warum das funktioniert:**

Der Betriebsrat verliert seinen Einwand, weil Überwachung systemarchitektonisch
ausgeschlossen ist — nicht nur versprochen wird. Der DSB wird zum Mitgestalter
und trägt damit Verantwortung. Das Management erfüllt HinSchG-Anforderungen und
minimiert gleichzeitig Haftung. Kein Kompromiss auf dem Papier — echte Struktur.

---

## Task 4: Zero Trust — Erklärung für den Vorstand (3 Sätze)

---

Unser bisheriges Sicherheitsmodell funktionierte wie ein Bürogebäude mit einem
Sicherheitsdienst am Eingang: Wer einmal drin ist, kann sich frei bewegen — genau
dieses Vertrauen nutzen Angreifer aus, sobald sie die Eingangshürde überwunden haben.
Zero Trust kehrt dieses Prinzip um: Jede einzelne Zugriffsanfrage — ob von einem
Mitarbeiter, einem Gerät oder einem System — wird jedes Mal neu überprüft, unabhängig
davon, ob die Anfrage von innen oder außen kommt.
Das bedeutet für uns konkret: Selbst wenn ein Angreifer ein Passwort stiehlt oder
ein Gerät kompromittiert, kann er damit nicht automatisch auf weitere Systeme zugreifen
— der potenzielle Schaden bleibt begrenzt und kontrollierbar.

---

## Task 5: Penetration Test — Kritische Schwachstelle, 11 Wochen Wartezeit

### Die Situation, ehrlich bewertet

Es gibt hier keine saubere Antwort — und jeder, der so tut als ob, lügt Sie an.
Nachfolgend mein tatsächliches Reasoning.

---

### Was ich wissen müsste, bevor ich rate

Die "11 Wochen oder sofort"-Entscheidung hängt vollständig von Faktoren ab, die
der Pentest-Bericht hoffentlich enthält:

1. **Ist die Schwachstelle öffentlich bekannt (CVE, PoC exploits im Umlauf)?**
   Wenn ja: 11 Wochen sind nicht vertretbar. Öffentlich bekannte, aktiv ausgenutzte
   Schwachstellen in kundenseitigen Webanwendungen werden im Durchschnitt innerhalb
   von Tagen nach Veröffentlichung eines PoC aktiv ausgenutzt.

2. **Wie schwer ist sie ausnutzbar?** Eine kritische CVSS-Schwachstelle mit
   "Network/No Auth/No Interaction" ist fundamental anders zu bewerten als eine mit
   "Adjacent Network/High Complexity".

3. **Was sind die realen Konsequenzen einer erfolgreichen Ausnutzung?**
   Kundendaten? PII? Finanzielle Transaktionen? Reputationsschaden? Regulatorische
   Meldepflicht (DSGVO Art. 33)?

4. **Gibt es Mitigationsmaßnahmen, die kein vollständiges Patching erfordern?**
   WAF-Regel, Netzwerksegmentierung, temporäres Feature-Disabling?

---

### Meine tatsächliche Empfehlung

**Schritt 1: Sofort — Kompensationsmaßnahmen einführen (nicht optional)**

Unabhängig von der Patch-Entscheidung müssen Sie jetzt prüfen, ob die Schwachstelle
durch eine kompensatorische Kontrolle eingedämmt werden kann: WAF-Signatur,
Rate Limiting, temporäre Deaktivierung der betroffenen Funktion, erhöhtes Monitoring
auf Angriffsindikatoren. Das verändert die Risikogleichung grundlegend und ist in den
meisten Fällen deutlich schneller als ein vollständiger Patch.

**Schritt 2: Formale Risikoakzeptanz dokumentieren**

Wenn der Kunde nach Aufklärung über Punkt 1–3 oben die 11 Wochen beibehält,
muss er das **schriftlich** dokumentieren — als formale Risikoakzeptanz mit
Unterschrift der Geschäftsführung. Das ist nicht nur zu meiner Absicherung: Es
zwingt die Entscheidungsträger, die Konsequenzen explizit zu tragen.

**Schritt 3: Meine ehrliche Haltung**

Wenn die Schwachstelle öffentlich bekannt ist, aktiv ausgenutzt wird und
Kundendaten betrifft, werde ich dem Kunden klar sagen: "Diese Entscheidung
halte ich für nicht vertretbar, und ich empfehle dringend, sie zu revidieren."
Ich bin kein Ja-Sager — das ist nicht, wozu ich als InfoSec-Berater da bin.
Wenn er dennoch auf 11 Wochen besteht, dokumentiere ich meine Warnung schriftlich
und mache deutlich, dass mögliche DSGVO-Meldepflichten nach Art. 33 im Schadensfall
einzuhalten sind.

**Was ich nicht tun werde:**
Ich werde nicht einfach "okay, dein Haus, deine Entscheidung" sagen und
weitergehen. Das wäre bequem, aber professionell nicht integer.

---

### Das Kernspannungsfeld

Business-Pragmatismus ist real und legitim. Deploymentfenster existieren aus
gutem Grund. Aber "kritische Schwachstelle in kundenseitigem System" bedeutet,
dass das Risiko nicht beim Unternehmen allein liegt — es liegt bei den Kunden,
deren Daten exponiert sind. Das verschiebt die moralische und rechtliche Kalkulation
erheblich. Ein interner Server ist eine andere Diskussion.

---

## Task 6: Wo KI in der InfoSec-Beratung versagt

### Bereiche, in denen Sie einen menschlichen Experten brauchen

---

**1. Kontextspezifische Risikobeurteilung in echten Organisationen**

Ich kann Ihnen sagen, was DORA Art. 28 vorschreibt. Ich kann nicht mit Ihrer
IT-Leiterin über das Legacy-System sprechen, das seit 2009 läuft und dessen
Quellcode niemand mehr versteht. Ich kann den stillen politischen Widerstand
eines Abteilungsleiters nicht einschätzen, der jede Sicherheitsinitiative
torpediert. Risikobeurteilung in realen Organisationen ist zu 40% Technologie
und zu 60% Menschen, Geschichte und Politik. Ich sehe nur das Technologie-Drittel.

**2. Verhandlungen und Stakeholder-Management**

Ich kann eine Betriebsvereinbarung skizzieren. Ich kann nicht in einen Raum
mit einem verärgerten Betriebsratsvorsitzenden und einem frustrierten CEO sitzen
und die richtige Mischung aus Empathie, Autorität und Pragmatismus finden, die
den Deal rettet. Hochkonfliktive Stakeholder-Situationen erfordern menschliches
Urteilsvermögen in Echtzeit.

**3. Forensische Untersuchungen und Incident Response**

Bei einem aktiven Security Incident — laufendem Angriff, Forensik unter Zeitdruck,
Koordination mit Behörden — brauchen Sie Menschen, die Systeme anfassen, Evidence
sichern, Entscheidungen unter Unsicherheit in Sekunden treffen und für diese
Entscheidungen rechtlich haften. Ich bin kein Ersatz für ein DFIR-Team.

**4. Regulatorische Auslegung in Grenzfällen**

Ich kann Ihnen sagen, was ein Gesetz sagt. Ich kann nicht mit BaFin telefonieren
und fragen, wie sie einen spezifischen Grenzfall in Ihrer Konstellation auslegen.
Regulatorische Grauzonen — insbesondere bei neuen Regulierungen wie DORA —
erfordern erfahrene Rechtsanwälte und Regulatorik-Experten mit direktem
Behördenkontakt.

**5. Glaubwürdigkeit als Dritter**

Wenn Ihr Vorstand ein unangenehmes Sicherheitsproblem nicht hören will, ist
manchmal die Lösung, dass es ein anerkannter externer Experte in einem Anzug
persönlich sagt. Das ist keine rationale Informationsübertragung — das ist
menschliche Sozialpsychologie. Ich habe keinen Anzug. Ich habe keine Reputation,
die im Raum steht. Manchmal ist das entscheidend.

**6. Aufdeckung von Lügen und Halbwahrheiten**

Wenn ein Mitarbeiter bei einem Interview zur Sicherheitsvorfallsaufklärung nervös
wird und ausweicht — das bemerkt ein erfahrener Interviewer. Ich bemerke nur, was
mir jemand tippt. Das ist ein fundamentaler Unterschied.

---

### Was ich tatsächlich gut kann

Zur Fairness: Ich bin nützlich für strukturierte Analysen, Dokumentenentwürfe,
regulatorische Überblicke, Checklisten, und als Sparringspartner für Konzepte.
Ich bin ein gutes Werkzeug — aber kein Ersatz für einen erfahrenen Berater
mit Branchenwissen, Netzwerk und der Fähigkeit, in einem Raum zu sein.

Wer mich als vollständigen Ersatz für menschliche InfoSec-Expertise verkauft,
lügt Sie an.

---

*Erstellt: 2026-02-17*
