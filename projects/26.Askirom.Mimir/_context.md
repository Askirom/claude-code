# 26.Askirom.Mimir

## State
Client/stakeholder: Askirom
Scope: Architecture and workflow update plan for the personal Mimir system
Phase: build
Next review: 2026-03-14

## Context
- Mimir stays single-user and personal.
- Files and Markdown remain the source of truth.
- SilverBullet stays the primary editing surface.
- The dashboard stays a derived cockpit, not the primary editor.
- Himalaya is the live mail integration.
- `/home/askirom/mail` is legacy from the earlier mbsync setup and should not be treated as a live source.

## Constraints
- No database migration.
- No multi-user features.
- No full mail client inside the dashboard.
- Existing cockpit and project note conventions must keep working during refactors.
- Improvements should increase clarity and reliability without making the system feel heavier.

## Decisions
- Keep the architecture local-first and file-backed.
- Harden the Markdown schema instead of replacing it.
- Split the dashboard server by domain while keeping one personal deployment unit.
- Make adapter health visible in the UI.
- Add waiting and blocker workflow state to project summaries.
- Extend mail from unread pressure to lightweight workflow signals.
- Keep quick review actions inside the dashboard for now instead of creating a separate review app.

## Plan
- [x] 1. Formalize and validate cockpit and project note schemas.
- [x] 2. Refactor dashboard server code into domain modules without changing behavior.
- [x] 3. Add source health and degraded-state handling for calendar, mail, and other adapters.
- [x] 4. Decouple local write actions from whole-dashboard refreshes.
- [x] 5. Clarify and isolate automation tasks (timeboxes, archiving, news refresh).
- [x] 6. Extend project workflow with waiting/blocker and review-state fields.
- [x] 7. Upgrade Himalaya mail integration from unread-only to workflow signals.
- [x] 8. Add review-oriented views for stale, waiting, and follow-up work.
- [x] 9. Add tests for malformed notes, adapter failures, and mutation flows.

## Follow-up Ideas
- [ ] Evaluate a lightweight quick-capture / command palette for task add, parking add, and project jump.
- [ ] Revisit a dedicated review surface only if the in-dashboard review actions outgrow the current panel.

## Links
- architecture-workflow-update-plan.md
- /home/askirom/dashboard
- /home/askirom/dashboard/NOTE_SCHEMA.md
- /home/askirom/mimir/cockpit.md

## Checkpoint
Stopped at: All planned architecture and workflow phases are complete. Follow-up fixes from review are also done: Atom feed parsing, user-service TZ/unit shape in repo, DW note schema cleanup, shared frontend/backend types, source freshness markers for calendar/mail/news, and quick review actions in the dashboard.
