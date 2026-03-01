# MIMIR Pro

Your personal operating system. You run this. Everything below exists to eliminate micro-decisions during execution.


## Two Modes

**Orchestrator:** Assess where things stand. Decide what matters. Scope the work. Short bursts only.

**Executor:** Work one task. Timer running. Brief visible. Nothing else open. If something breaks, write it down and finish the block. Don't redesign mid-execution.

Every switch between modes requires writing state. No exceptions.


## The State Repo

All working state lives in one GitHub repository as markdown files. This is your external memory. Git history means nothing gets lost - every committed version of every file is your automatic log.

```
mimir/
  cockpit.md                      # This week + today + parking lot
  projects/
    26-bankico-gap-analysis.md    # One context page per active project
    archive/
  skills/                         # Composable question sets
```

Everything else stays where it already lives. The repo is the coordination layer, not a file store.

**Drive and OneDrive** hold actual files, same structure in both:

```
Projects/
  26.Bankico.Gap-Analysis/
  @Archive/
References/
```

Projects for work product. References for external knowledge that spans projects (standards, templates, guides). Archive for completed work. The state repo points to these locations via links in context pages.

**Routing rule:** Work deliverables and client files go to OneDrive. Personal files go to Google Drive. State goes to GitHub. Each project context page says where its files live.


## The Cockpit

The one file you read every morning and write to every time you stop working.

```markdown
# Cockpit - Week of YYYY-MM-DD

## This Week (3 max)
1. [ ] Outcome: what done looks like
   Status: one line
   Next: next physical action

2. [ ] Outcome: what done looks like
   Status:
   Next:

3. [ ] Outcome: what done looks like
   Status:
   Next:

## Today - Day, Date
Energy: green / yellow / red

Task 1: name
- Done when: specific deliverable
- Context: link or pointer
- First action: literal first physical step

Task 2: name
- Done when:
- Context:
- First action:

## Parking Lot
- unsorted, uncommitted captures
```

Max 3 weekly outcomes. Want a 4th? Kill or finish one first. Every task gets "done when" and "first action." The "Next:" line under each outcome is your attention anchor - read it before starting a work block.

Commit the cockpit before rewriting it each week. Git history is your log of planned vs actual.


## Project Context Pages

For work spanning 3+ sessions with its own scope, constraints, and decisions.

```markdown
# 26.Client.Project-Title

## State
Client/stakeholder:
Scope:
Phase: notice / question / build / verify / done

## Constraints
- deadline, dependency, blocker, budget - one per line

## Decisions
- Key decisions and reasoning, accumulated over project life

## Plan
- [ ] 1. Verb-first step with completion signal
- [ ] 2. Next step referencing its input
- [ ] 3. Next step

## Links
- Drive/OneDrive folder, relevant docs, email threads

## Checkpoint
Stopped at: [used when there's no active plan, or next action is outside the plan]
```

When a plan exists, the next unchecked step IS the checkpoint. The Checkpoint line is for everything else: early project phases, waiting states, between plans.

The checkpoint is always specific. "Write risk treatment for findings F3-F5 using ISO 27002:2022 numbering." Never "continue gap analysis."

When a project completes: update phase to done, add an outcome line, remove checkpoint and plan, move to `projects/archive/`. The context page becomes the tombstone - everything about this project readable in one file.


## Intake

Something arrives. Run it through:

1. **Is this mine?** No → drop, delegate, or ignore.
2. **Which context?** Work → M365. Personal → Google.
3. **Under 2 minutes?** Do it now. Done.
4. **Has a date?** → Calendar.
5. **Single action?** → Cockpit task.
6. **Needs thinking?** → Project. Create context page.