#!/bin/bash
# Calendar extraction + commit wrapper for cron
# Runs extraction and commits to repo so any AI can access it

cd /root/.openclaw/workspace/claude-code

# Run extraction
python3 mimir/calendar/extract_calendar.py --days 7

# Check if there are changes to commit
if git diff --quiet mimir/calendar/ 2>/dev/null; then
    echo "No calendar changes to commit"
else
    git add mimir/calendar/
    git commit -m "auto: Update calendar extract $(date +%Y-%m-%d)"
    git push origin main
    echo "Committed calendar updates"
fi
