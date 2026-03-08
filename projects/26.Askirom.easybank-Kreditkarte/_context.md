# 26.Askirom.easybank-Kreditkarte

## State
Client/stakeholder: easybank (Robin)
Scope: Antrag Kreditkarte — Adressabweichung klären
Phase: build

## Context
Easybank credit card application submitted. Address on application differs from ID registration address.
Email received: 2026-03-06 from antragsanrufe@easybank.de
Subject: easybank Antragsbearbeitung

## Constraints
- Cards can only be sent to German registration address (Meldeadresse) for security
- Nachsendeauftrag (mail forwarding) not possible for card/PIN delivery
- Documents needed if sending to application address (not ID address)

## Decision
Chosen: **Option B** — Send to ID address

## Requirements
- Reply to email with full name
- Confirm ID address should be used
- State how long registered there
- If < 12 months: provide previous address ← **Needed**

## Registration Info
- Current address since: **13.02.2026** (< 12 months)
- Previous address: **Zur Heide 8, 91738 Pfofeld**

## Plan
- [x] 1. Decide which option (A or B) → **Option B**
- [x] 2. Gather info: how long registered at current ID address → Since 13.02.2026
- [x] 3. Provide previous address → Zur Heide 8, 91738 Pfofeld
- [x] 4. Draft reply email → See `email-reply-draft.md`
- [ ] 5. Send reply email
- [ ] 6. Wait for card delivery

## Checkpoint
Stopped at: Email draft ready. Review and send.
