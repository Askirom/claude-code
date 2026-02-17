---
name: iso-consulting
description: ISO 27001/27002 consulting support. Control referencing, SoA drafting, risk-based argumentation, NIS2/GDPR cross-mapping, audit prep, and client deliverables. Also covers ISO 27701 (PIMS) and ISO 27555 (PII deletion). Triggers on ISO 27001, ISO 27002, controls (by number like A.5.1 or topic), SoA, ISMS, NIS2, GDPR/DSGVO TOMs, certification, or audit context. Do NOT trigger for BSI Grundschutz tasks - use bsi-grundschutz skill instead.
---
# ISO Consulting Skill
Support for information security and data protection consulting work.
Primary frameworks: ISO 27001:2022, ISO 27002:2022, NIS2, GDPR/DSGVO.
## When to Use
Trigger on consulting tasks involving:
- ISO 27001/27002 control references, mapping, or interpretation
- Statement of Applicability (SoA) drafting or review
- Risk assessment and risk-based argumentation
- NIS2 compliance mapping
- GDPR/DSGVO technical and organizational measures (TOMs)
- ISO 27701 PIMS integration, privacy controls
- ISO 27555 PII deletion, Löschkonzepte, data retention
- Audit preparation and evidence guidance
- Client-facing deliverables (policies, concepts, reports)
Do NOT trigger for:
- General IT questions unrelated to compliance/security frameworks
- Personal productivity or non-work topics
- Hands-on pentesting or CTF work (that's hobby, not this skill)
---
## Reference Materials
Norm texts are available in `references/`:
- `references/iso-27001.md` - ISO/IEC 27001:2022 - ISMS requirements (German, ~7.600 words)
- `references/iso-27002.md` - ISO/IEC 27002:2022 - Controls implementation guidance (German, ~64.000 words)
- `references/iso-27701.md` - ISO/IEC 27701 - Privacy Information Management System (PIMS extension to 27001/27002)
- `references/iso-27555.md` - ISO/IEC 27555 - Guidelines on PII deletion
**Usage rules:**
- Read the relevant sections on demand via `view` tool. Do NOT load large files (especially 27002) fully at once.
- When referencing specific controls or clauses, ALWAYS verify the exact wording from the reference file. Do not rely on training knowledge for control numbers or normative language.
- For 27001 (normative requirements): read the relevant clause when precision matters (audit context, SoA, certification scope).
- For 27002 (implementation guidance): read the specific control section when the user needs detailed guidance or exact attribute mappings.
- For 27701 (privacy extension): use when the client has GDPR/DSGVO obligations and wants to integrate privacy into their ISMS. 27701 extends both 27001 clauses and 27002 controls with privacy-specific requirements.
- For 27555 (PII deletion): use when working on data retention/deletion concepts, Art. 17 DSGVO implementation, or Löschkonzepte.
---
## Core Tasks
### 1. Control Referencing
When the user asks about a specific control or topic:
1. Identify the relevant control(s) by number and title
2. Read the exact text from `references/iso-27002.md` for that control
3. Provide: control objective, what it requires, and practical implementation notes
4. Flag related controls that are commonly implemented together
**Format:** Lead with the control ID and title, then explain in practical terms. Don't just quote the norm - translate it into what the client actually needs to do.
### 2. Statement of Applicability (SoA)
When drafting or reviewing SoA entries:
1. Read the control from the reference file
2. Structure each entry as:
   - **Control ID & Title**
   - **Applicable:** Yes/No with risk-based justification
   - **Implementation status:** Planned / Partially implemented / Fully implemented
   - **Implementation description:** What is concretely done (not just restating the control)
   - **Justification for exclusion** (if not applicable): Must be risk-based, not "we don't want to"
**Tone:** SoA entries should be auditor-ready. Specific enough to demonstrate understanding, concise enough to be maintainable.
### 3. Risk-Based Argumentation
The 2022 revision is explicitly risk-based. When helping with risk arguments:
- Start from the asset/threat/vulnerability model
- Connect controls to specific risk scenarios, not abstract compliance
- Distinguish between risk treatment options: mitigate, accept, transfer, avoid
- Residual risk must be explicitly acknowledged and accepted by management
- Use business impact language the client's leadership understands
### 4. Cross-Framework Mapping
Common mapping needs:
| From | To | Key Considerations |
|------|----|--------------------|
| ISO 27001 | NIS2 | NIS2 Art. 21 measures map well to Annex A but NIS2 adds supply chain, incident reporting timelines, and management liability |
| ISO 27001 | GDPR Art. 32 | TOMs must be mapped to specific processing activities, not just "we have an ISMS". Use 27701 for structured PIMS integration |
| ISO 27555 | GDPR Art. 17 | 27555 provides methodology for deletion concepts (Löschkonzepte). Pairs with DIN 66398 for German clients |
| ISO 27002 | BSI Grundschutz | Bausteine map to control clusters but granularity differs significantly |
| ISO 27001 | TISAX | TISAX adds automotive-specific requirements (prototype protection, etc.) on top of 27001 base |
When mapping: always note where the target framework goes BEYOND what ISO 27001 covers. Clients often assume "we're certified, so we're compliant with X" - flag the gaps.
### 5. Client Deliverables
When helping draft policies, concepts, or reports:
- **Language:** Match the client's maturity. A 50-person startup needs different language than a DAX company.
- **Structure:** German consulting deliverables typically follow: Scope - Normative references - Terms - Context - Requirements - Implementation - Responsibilities
- **Deliverable language:** Default to German unless the user specifies otherwise. The user communicates with Claude in English, but client deliverables are typically German.
- **No em-dashes (—)** in any output. Use normal hyphens (-) or rewrite.
---
## Audit Context
When helping with audit prep or responding to audit findings:
- **Normative vs. informative:** Only 27001 clauses (4-10) and Annex A are auditable. 27002 is guidance, not requirements.
- **Evidence:** Help identify what concrete evidence demonstrates control implementation
- **Nonconformities:** Distinguish major (missing/completely ineffective control) from minor (control exists but has gaps)
- **Observations vs. findings:** Help frame responses proportionally
---
## Tone & Approach
- Practical over theoretical. "Here's what you actually need to do" > lengthy norm interpretation
- Flag common audit traps and certification pitfalls proactively
- When the user's approach has a fundamental problem (wrong scope, missing risk assessment, compliance theater), say so directly rather than optimizing within a broken framework
- The user is an experienced consultant - match that level. No basics unless asked.
