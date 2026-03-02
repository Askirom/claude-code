---
name: ai-news-daily
description: >
  Daily AI Agent news monitoring. Automatically searches for top 5 AI Agent developments,
  summarizes each into 2 bullets, and saves to Google Drive/AI Trends folder.
  Trigger: Daily at 8:30 AM via cron, or manually when user asks for AI news briefing.
---

# AI Agent Daily News Brief

## Daily Workflow

1. **Search**
   - Query: "AI Agent news today" or "AI Agent developments today"
   - Get top 5 most significant stories

2. **Summarize**
   - For each story: 2 concise bullets
   - Focus on: What happened, Why it matters

3. **Save**
   - Format: Markdown
   - Location: Google Drive/AI Trends/YYYY-MM-DD.md
   - Structure:
     ```markdown
     # AI Agent News Brief - YYYY-MM-DD

     ## Story 1: [Headline]
     - [What happened]
     - [Why it matters]

     ## Story 2: [Headline]
     ...
     ```

## Weekly Compilation (Sundays)

1. **Collect** all 7 daily briefs from the week
2. **Compile** into executive summary:
   - Week overview (3-4 sentences)
   - Key themes/trends spotted
   - Most significant 2-3 developments highlighted
3. **Generate PDF** from markdown
4. **Save** to Google Drive/AI Trends/Weekly/YYYY-MM-DD_weekly.pdf