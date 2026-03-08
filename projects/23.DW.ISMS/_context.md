# 23.DW.ISMS

## State
Client/stakeholder: Deutsche Welle (DW)
Scope: ISMS-Beratung, Erstellung von Richtlinien und Konzepten
Phase: build
Waiting:
Next review:

## Constraints
- Ressource: Halber bis ganzer Tag pro Woche
- Format: Richtlinien nach SOLL/KANN/MUSS, wenig Prosa
- Workflow: Drafting in HiSolutions SharePoint
- Freigabe: Intendantin unterschreibt final, aber Konsens vorher noetig
- Parallel: BCM-Projekt laeuft ebenfalls

## Decisions
- Richtlinien-Format: Wenig Text, strukturiert SOLL/KANN/MUSS
- Schwachstellenmanagement: Environmental CVSS fuer kontextbezogene Bewertung, nicht nur Base Score
- Vorfallsmanagement: Nur Outlier-Schwachstellen gehen in den Vorfallsprozess, nicht alle

## Plan
- [x] Kryptokonzept erstellen
- [ ] Kryptokonzept mit Johannes Klemm und Eike Zimmermann abstimmen
- [ ] Schwachstellenmanagement: Environmental CVSS Einflussfaktoren recherchieren
- [ ] Schwachstellenmanagement: ECVSS-Faktoren auf DW-Kontext mappen (ca. 20 Faktoren)
- [ ] Schwachstellenmanagement: Kreuzreferenz ECVSS zu Base CVSS erstellen
- [ ] Schwachstellenmanagement: Selbstberechnungsmethode fuer unbekannte Schwachstellen definieren
- [ ] Schwachstellenmanagement: Richtlinie finalisieren

## Links
- HiS Kundenportal: <https://kunden.hisolutions.com/sites/10641/PRJ7637/>
- Schwachstellenmanagement V0.3: <https://kunden.hisolutions.com/sites/10641/PRJ7637/_layouts/15/WopiFrame.aspx?sourcedoc=%7BA62C9B93-5FF2-4EC4-8E11-3C32E60A2B59%7D&file=25.DW.Schwachstellenmanagement.V0.3.docx&action=default>
- Schwachstellenmanagement Review: [[schwachstellenmanagement-review]]

## Notes
- CISO bei DW: War Redakteur der Leitlinie
- Intendantin: Unterschreibt final, aber Konsens vorher noetig
- BCM-Projekt: Parallel aktiv, Abstimmung beachten

## Checkpoint
Stopped at: Schwachstellenmanagement V0.3 Review. CVSS-Ansatz zu aufwaendig, Environmental CVSS als kontextbezogene Alternative. Naechster Schritt: Environmental CVSS Faktoren recherchieren und DW-spezifisch definieren.
