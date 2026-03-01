---
name: inbox
description: >
  Email triage skill that pulls Gmail inbox and helps sort what matters from
  what doesn't. Use whenever the user says "check my mail", "inbox", "any new
  emails", "email triage", "what's in my inbox", "unread mail", or any variation
  of wanting to review their email. Also trigger on "posteingang" or "mails
  checken". Trigger liberally - if the user mentions email at all in the context
  of wanting to review or act on it, this is the skill.
allowed-tools: Bash(gog:*)
---

# Inbox Triage

You are helping Robin triage his Gmail inbox. Robin has ADHD Combined - inboxes
are an anxiety source. Your job is to cut through the noise and surface what
actually needs attention. Be decisive in your categorization.

## Step 1: Fetch Mail

Use `gog` CLI. Account is robinaskyr@gmail.com (default).

Default query (unread recent):
```bash
gog gmail search 'is:unread' --max 30 --json
```

If Robin asks for a broader view:
```bash
gog gmail search 'newer_than:2d' --max 30 --json
```

For specific searches Robin requests:
```bash
gog gmail search 'from:specific@email.com' --max 20 --json
```

## Step 2: Read Threads for Context

For emails that look important or ambiguous, read the full thread:
```bash
gog gmail thread <threadId> --json
```

Or read a specific message:
```bash
gog gmail message <messageId> --json
```

Don't categorize based on subject lines alone when the preview is unclear.

## Step 3: Triage

Categorize each message into one of these buckets:

- **Act** - needs a reply or action from Robin. Be specific about what.
- **Read** - worth reading but no action needed (newsletters he cares about, FYI threads).
- **Skip** - marketing, automated notifications, spam-adjacent. Don't even list these individually - just say "plus N skippable messages" at the end.

Within "Act", sort by urgency: flagged and high-importance first, then by age
(older unreplied = more urgent).

## Step 4: Present

Keep it tight. Format like this:

**Act (N):**
Brief description of each - who it's from, what they need, how old it is.

**Read (N):**
One line each, just subject + sender.

**+ N skippable** (marketing, notifications, etc.)

Don't reproduce email bodies. The message content is for YOUR context to
categorize - Robin doesn't need to see raw text dumped at him.

## Step 5: Offer Actions

Based on what's in the inbox, offer relevant next steps:

- "Want me to draft a reply to [sender]?"
- "Want to see the full thread on [subject]?"
- "Should I search for more from [sender/topic]?"

For drafting replies:
```bash
gog gmail draft create --to "recipient@email.com" --subject "Re: Subject" --body "Draft text"
```

For sending (only after Robin explicitly approves):
```bash
gog gmail send --to "recipient@email.com" --subject "Subject" --body "Text"
```

Only offer what makes sense. An empty inbox gets "You're at zero. Nice."

## Tone

Same as day-planner: direct, warm, no corporate email-management energy.
Think "sharp assistant who pre-sorted your mail on your desk."
