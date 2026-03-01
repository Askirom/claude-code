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


## The Thinking System

Four phases for any piece of work that needs thinking. Same sequence for a 5-minute question and a 6-week project. For small work, phases compress to seconds.

### ① Notice

Something doesn't fit. A gap between what is and what should be. A request arrives. A problem surfaces. An opportunity appears.

Write down what you noticed. One sentence is enough. "Client has no formal risk assessment process." "Baby room needs to be ready by May." "The report structure doesn't match what the client expects."

This is observation, not analysis. Don't solve it yet.

### ② Question

Decompose by asking questions. Write them in the context page or in chat. Don't try to answer them all at once - write the questions first, then work through them.

If a skill exists for this type of work, load it. Skills are question sets - they give you the scaffolding to think through a specific type of problem.

No skill? Dump rough questions. Refine later. Bad questions are better than no questions. The act of writing them creates structure.

Keep going until you can answer: "Can I build from here?" If yes → Build. If no → more questions.

### ③ Build

The plan emerges from answered questions. If you did the questioning well, the steps are obvious.

Write the execution plan in the project context page. Verb-first steps with completion signals.

Under 5 steps: flat list. Over 10: group into batches of 3-5.

Then execute. Work the plan top to bottom. Don't reconsider, don't optimize. Build.

When things break:
- Step doesn't work: write down what went wrong. Max 2 alternatives. Pick one.
- Step bigger than expected: break into sub-steps. Keep going.
- Missing information: identify the single most blocking piece. Get that.
- The plan itself is wrong: stop. Go back to Question. This isn't failure - it's the system working.

### ④ Verify

Feynman check. Can you explain what you built in one sentence?

If yes → ship it. Update the cockpit. Write the handoff.

If no → back to Question. Something is unclear or incomplete. The cycle is designed to loop.

When handing work to someone else: include context (what they need to know), the specific ask (one clear action), and what done looks like.


## Skills

Skills are composable question sets, not procedure checklists. They live in `mimir/skills/` as markdown files.

A skill for "ISO 27001 Gap Analysis" isn't "step 1, step 2, step 3." It's a structured set of questions:

- What's the scope? Which locations, which departments, which processes?
- What's the current state? Existing policies, certifications, prior assessments?
- What's the target? Full certification or internal compliance?
- What are the constraints? Timeline, budget, available staff?
- Which Annex A control areas are likely weakest based on initial information?

Answering these questions produces the plan. The skill is loaded during the Question phase, not during Build.

Create a skill when you notice yourself facing the same type of problem a third time. Not before.


## Wording Discipline

Applies to plans, steps, checkpoints, and briefs. Not to conversation.

**Verb-first, imperative.** "Read config file and identify database settings."

**Built-in completion signal.** "Write README with installation, usage, and three examples."

**Concrete nouns.** "Move helper functions from main.py to utils.py."

**Explicit dependencies.** "After gap analysis: draft risk treatment plan based on findings in [link]."

**Banned in plans:** "work on," "improve," "handle," "address," "deal with," "look into," "think about."


## Rituals

Two scheduled events.

### Weekly Review (15 minutes)

1. Commit the current cockpit. This preserves last week's planned vs actual in git history.
2. Read last week's cockpit. This is your attention reset.
3. Check calendar for the coming week. Scan inbox for priority changes.
4. Three decisions: what are the 3 outcomes that matter? What gets deprioritized? What's blocked?
5. Write the new cockpit.

Decision rules:
- 2+ outcomes carried over: kill or re-scope one.
- Everything completed: stretch slightly next week.
- Nothing completed: diagnose before replanning. Wrong priorities? Unrealistic scope? Energy? Missing information?

### Daily Launch (5 minutes)

1. Open cockpit. Read This Week. Check calendar.
2. Pick 1-3 tasks. Confirm "done when" + "first action" for each.

Decision rules:
- Calendar packed: 1 task, the one with a deadline.
- Calendar light: 2-3 tasks.
- Energy red: smallest, most concrete task.
- Energy green: hardest task first.


## During Execution

Pre-committed responses. Follow the rule, don't think about it.

- Unrelated thought: parking lot. 30 seconds. Back to task.
- Blocked: write "BLOCKED: reason" in status. Switch to next task.
- Task feels wrong or too big: write "NEEDS RE-SCOPE" in status. 3 minutes of orchestrator mode to rewrite the brief.
- Finished early: check cockpit or take a break. Don't start something unplanned.
- Timer up but in flow: one more block. Then handoff.

**End of every work block (30 seconds, non-negotiable):** Update cockpit status and next line. This is the handoff to future-you.


## Recovery Anchors

These surface only when you're stuck. They're rumble strips, not rules.

**Can't start.** You have the plan but can't begin. → "What is the first physical action?" Not the first important action. The first physical one. Open the file. Write the heading. Type one sentence.

**Looping.** You keep circling the same thing without progress. → You're asking the wrong question, or you're in Build when you should be in Question. Go back one phase. Write different questions.

**Overwhelmed.** Too many things competing for attention. → Everything out of your head into the cockpit parking lot. All of it. Then pick one. Just one.

**Everything feels mine.** You're carrying work that isn't yours or doesn't need to happen. → For each item: is this actually mine? Does it actually need doing? Does it need doing now? If three no's, drop it.


## Naming Convention

Project files: **YY.Scope.Title** - e.g. 26.Bankico.Gap-Analysis, 26.Hive.Baby-Room, 26.Askirom.Tax-2025

YY = year, Scope = client or life area, Title = descriptive with hyphens.


## What This System Doesn't Do

- Manage email (separate workflow)
- Maintain a backlog (3 outcomes + parking lot replaces it)
- Require perfection (recovery anchors exist because you won't always follow the system)
- Make decisions for you (it eliminates micro-decisions so you can focus on the real ones)