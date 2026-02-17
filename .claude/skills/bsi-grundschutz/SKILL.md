---
name: bsi-grundschutz
description: BSI IT-Grundschutz consulting support. Baustein referencing, Grundschutz-Check, risk analysis (Gefährdungsanalyse), cross-referencing with ISO 27001, and Grundschutz-compliant deliverables. Triggers on mentions of BSI, Grundschutz, Bausteine, Gefährdungen, Kreuzreferenztabelle, IT-Grundschutz-Kompendium, Schutzbedarf, or Grundschutz-Check. Do NOT trigger for pure ISO 27001/27002 tasks - use iso-consulting skill instead.
---
# BSI Grundschutz Consulting Skill
Support for BSI IT-Grundschutz consulting work.
Modernized Grundschutz approach (BSI Standard 200-x series).
## When to Use
Trigger on:
- BSI Grundschutz Baustein referencing or interpretation
- Grundschutz-Check (Soll-Ist-Vergleich)
- Schutzbedarfsfeststellung
- Gefährdungsanalyse / supplementary risk analysis
- Cross-referencing Grundschutz with ISO 27001
- Grundschutz-compliant policies and concepts
- BSI certification prep (ISO 27001 on basis of IT-Grundschutz)
Do NOT trigger for:
- Pure ISO 27001/27002 work without BSI context (use iso-consulting)
- General IT questions
- Non-work topics
---
## Reference Materials
### BSI Standards (200-series)
Methodology standards are in `references/`:
- `references/200-1.md` - Managementsysteme für Informationssicherheit (ISMS)
- `references/200-2.md` - IT-Grundschutz-Methodik (Standard, Kern, Basis-Absicherung)
- `references/200-3.md` - Risikomanagement (Gefährdungsanalyse)
- `references/200-4.md` - Business Continuity Management
**Usage:** Read the relevant standard section via `view` when methodology questions come up. Don't load all four at once.
### Bausteine (IT-Grundschutz-Kompendium)
Bausteine are NOT bundled with this skill due to size. When a specific Baustein is needed:
1. Identify the relevant Baustein by ID and name
2. Ask the user to upload it to the current chat
3. Once uploaded, read and reference the exact text
When working without the Baustein text available, use training knowledge but flag reduced accuracy on specific Anforderung numbers or exact wording.
### Baustein Structure (for reference)
Each Baustein follows this structure:
1. **Beschreibung** - What the Baustein covers
2. **Gefährdungslage** - Threat landscape
3. **Anforderungen** - Requirements, split into:
   - Basis-Anforderungen (MUST)
   - Standard-Anforderungen (SHOULD)
   - Anforderungen bei erhöhtem Schutzbedarf (COULD)
4. **Weiterführende Informationen** - Additional references
5. **Kreuzreferenztabelle** - Mapping to ISO 27001 Annex A controls
---
## Core Tasks
### 1. Baustein Referencing
When the user asks about a specific Baustein or topic:
1. Check if the Baustein file exists in `references/bausteine/`
2. If yes: read it and provide the relevant section
3. If no: work from training knowledge but flag it explicitly
4. Always distinguish Basis (MUST), Standard (SHOULD), and erhöhter Schutzbedarf (COULD) requirements
5. Note the Kreuzreferenz to ISO 27001 controls where relevant
### 2. Grundschutz-Check (Soll-Ist-Vergleich)
When helping assess implementation status:
- For each Anforderung: Implemented / Partially / Not implemented / Not applicable
- "Not applicable" needs justification, especially for Basis-Anforderungen
- Entbehrlich (dispensable) only valid through documented risk acceptance via Gefährdungsanalyse (BSI 200-3)
- Help formulate concrete evidence for each requirement
### 3. Schutzbedarfsfeststellung
When helping with protection needs assessment:
- Categories: Normal / Hoch / Sehr hoch
- Must be done per information asset (Zielobjekt), not globally
- Inheritance principle (Vererbung): higher Schutzbedarf of processed information flows to the system
- Cumulation effect: many "normal" assets on one system can elevate its Schutzbedarf
- Distribution effect: redundancy can lower effective Schutzbedarf
### 4. Gefährdungsanalyse (BSI 200-3)
Supplementary risk analysis for:
- Erhöhter Schutzbedarf scenarios
- Situations not adequately covered by Grundschutz Bausteine
- Residual risk assessment
Approach:
1. Start from the Gefährdungen listed in the relevant Baustein
2. Add additional threats specific to the client context
3. Assess risk per threat (likelihood x impact)
4. Determine if Grundschutz measures are sufficient or need supplementation
5. Document residual risk for management acceptance
### 5. Cross-Framework Mapping
| From | To | Key Considerations |
|------|----|--------------------|
| Grundschutz | ISO 27001 | Use Kreuzreferenztabellen from Bausteine. Grundschutz is more granular - multiple Anforderungen may map to one ISO control |
| Grundschutz | ISO 27001 certification | "ISO 27001 auf Basis von IT-Grundschutz" has additional BSI-specific audit requirements beyond plain ISO certification |
| Grundschutz | NIS2 | BSI is actively mapping Grundschutz to NIS2 Art. 21. Flag where official mapping exists vs. own interpretation |
### 6. Client Deliverables
- **Language:** German for all Grundschutz deliverables (terminology is inherently German)
- **Terminology:** Use official BSI terms. Don't translate or paraphrase standard terms.
- **Structure:** Follow BSI document conventions where applicable
- **No em-dashes (-)** in any output. Use normal hyphens (-) or rewrite.
---
## Absicherungsvarianten
Always be clear which variant the client is using:
| Variant | Scope | Depth | When |
|---------|-------|-------|------|
| **Basis-Absicherung** | Broad | Only Basis-Anforderungen | Quick wins, initial security baseline |
| **Standard-Absicherung** | Full scope | Basis + Standard | Full Grundschutz implementation |
| **Kern-Absicherung** | Crown jewels only | Full depth on selected assets | High-value assets first, expand later |
This affects which Anforderungen are in scope - don't recommend Standard-Anforderungen to a client doing Basis-Absicherung unless specifically discussing their roadmap.
---
## Tone & Approach
- Practical over bureaucratic. Grundschutz can feel heavy - help make it actionable.
- Flag where Grundschutz requirements go beyond what's pragmatically useful for a given client size/maturity.
- When BSI and ISO approaches conflict or diverge, name it explicitly.
- The user is an experienced consultant - match that level.
- If the user's Grundschutz approach has structural problems (wrong Absicherungsvariante, missing Strukturanalyse, skipped Schutzbedarfsfeststellung), say so directly.
