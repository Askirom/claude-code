# Architecture and Workflow Update Plan

## Goal

Improve Mimir's architecture and workflow support without changing its core philosophy:

- single-user and personal
- local-first
- files and Markdown remain the source of truth
- the dashboard stays a derived control surface
- SilverBullet stays the primary editing surface
- Himalaya is the live mail source

## Working Assumptions

- `/home/askirom/mail` is legacy state from the old mbsync setup, not a live integration target.
- `cockpit.md` and project `_context.md` files are the operational schema for the system.
- The current dashboard architecture is directionally right; the next step is hardening and clarifying it.

## Main Architecture Findings

1. The real data model is an implicit Markdown schema.
2. `dashboard/index.ts` currently carries too many responsibilities.
3. Adapter failures are too easy to confuse with empty states.
4. Small write actions are coupled to whole-dashboard refreshes.
5. The dashboard service is both UI host and automation runtime.

## Main Workflow Findings

1. The overall workflow is coherent and role-separated.
2. The system is better at "what do I do now?" than "what am I waiting on?"
3. Mail is currently surfaced as pressure, not as workflow.

## Update Principles

1. Keep the philosophy; improve the shape.
2. Prefer explicit contracts over silent conventions.
3. Prefer visible degraded states over false calm.
4. Keep the dashboard thin where possible.
5. Add only workflow concepts that directly improve decisions.

## Phase 1: Stabilize the data contracts

### Objective

Make the note formats explicit and validated instead of only convention-based.

### Work

- Define the expected structure of `cockpit.md`.
- Define the expected structure of project `_context.md`.
- Add validation helpers for cockpit and project parsing.
- Decide how validation failures should surface:
  - log warnings
  - API health flags
  - optional UI badge
- Document the schema near the code and near the note templates.

### Expected Outcome

- malformed notes produce visible warnings
- parsing failures stop being silent
- note evolution becomes safer

## Phase 2: Split the dashboard server by domain

### Objective

Reduce structural coupling without changing the product model.

### Target module split

- `cockpit.ts`
- `projects.ts`
- `calendar.ts`
- `mail.ts`
- `news.ts`
- `automation.ts`
- `server.ts` or `routes.ts`
- `types.ts`

### Work

- move parsing logic into source-specific modules
- move CLI adapter code into dedicated modules
- keep route wiring thin
- preserve current behavior during the split

### Expected Outcome

- easier local reasoning
- easier testing
- less risk when changing one data source

## Phase 3: Make source health visible

### Objective

Separate "empty" from "unavailable."

### Work

- change calendar and mail adapters to return structured status
- include optional error message and last successful refresh
- add aggregated source health to the dashboard payload or a dedicated endpoint
- show degraded-state indicators in the UI

### Expected Outcome

- mail `0` unread no longer hides adapter failures
- calendar empty state no longer hides fetch failures
- the dashboard becomes a more trustworthy control surface

## Phase 4: Decouple writes from full refreshes

### Objective

Keep the UI simple while removing unnecessary read-path coupling after small mutations.

### Work

- change task add/toggle routes to return updated task state
- change week toggle route to return updated weekly state
- change parking lot add route to return updated parking state
- rerender only the affected UI slice after a successful mutation
- keep full refresh for startup, polling, and recovery

### Expected Outcome

- faster interaction loops
- fewer unrelated dependencies per action
- lower chance that a slow adapter harms simple write flows

## Phase 5: Clarify the automation boundary

### Objective

Keep automation in the same service if desired, but make the boundary explicit.

### Work

- move task archiving, news refresh, and timebox scheduling into `automation.ts`
- document that the dashboard service is also the automation host
- add clear startup logging for active automation jobs
- add failure logging that is easy to distinguish from route failures

### Expected Outcome

- a clearer operating model
- easier troubleshooting
- less hidden behavior in the main route file

## Phase 6: Upgrade the project workflow model

### Objective

Improve support for blocked and waiting work without creating a separate project system.

### Work

- extend the project template with one explicit field:
  - `Waiting:`
  - or `Blocked by:`
- optionally add `Next review:`
- parse and surface that field in project summaries
- expose it in the project cards

### Expected Outcome

- the dashboard reflects dependency state, not only action state
- consulting and coordination work becomes easier to review

## Phase 7: Upgrade the mail workflow

### Objective

Move mail from interruption signal toward workflow signal.

### Work

- keep Himalaya as the integration surface
- expand beyond unread count with a small set of signals such as:
  - unread count
  - flagged count
  - shortlist of threads needing attention
- if practical, include sender, subject, and age for a few items
- keep action in the real mail surface, not in the dashboard

### Expected Outcome

- mail becomes reviewable, not just alarming
- project follow-up work becomes easier to notice

## Phase 8: Add review-oriented views

### Objective

Support both execution mode and review mode.

### Work

- add one view or section for waiting/blocker state
- add one view or signal for stale projects
- optionally use `Next review:` to drive review prompts
- keep `cockpit.md` focused on execution rather than turning it into a backlog dump

### Expected Outcome

- better weekly review support
- better follow-up discipline
- less chance that low-motion projects disappear from view

## Phase 9: Test the real failure modes

### Objective

Test the system at the points where trust can break.

### Work

- keep the current parser validation tests
- add fixture tests for malformed cockpit notes
- add fixture tests for malformed project contexts
- add adapter tests for Himalaya and calendar failures
- add mutation tests for task toggling, parking insertion, and task archiving

### Expected Outcome

- higher confidence in refactors
- safer note evolution
- safer adapter behavior

## Recommended Order

1. Stabilize schemas and add validation
2. Make source health visible
3. Split the server by domain
4. Decouple writes from full refreshes
5. Clarify automation boundaries
6. Extend project waiting/blocker state
7. Improve mail workflow signals
8. Add review-oriented views
9. Expand failure-mode tests

## Non-goals

- replacing Markdown/files with a database
- building a multi-user product
- replacing SilverBullet as the editing surface
- turning the dashboard into a full mail client
- over-abstracting a personal system into enterprise architecture

## Done Criteria

- cockpit and project schemas are explicit and validated
- source degradation is visible instead of silent
- the server is split into clear domain modules
- small write actions do not require whole-dashboard redraws
- project cards surface next action plus waiting/blocker state
- mail uses Himalaya as the live path and exposes workflow-relevant signals
- review mode is supported alongside execution mode
