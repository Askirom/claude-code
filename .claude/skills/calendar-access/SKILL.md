---
name: calendar-access
description: Access Robin's calendar from the repo. Use when Robin asks about schedule, events, or when you need to know what’s happening today/this week. Calendar is pre-extracted from Google Calendar ICS with recurring events expanded.
---

# Calendar Access

Robin's calendar lives in the repo at:

```
mimir/calendar/
  today.md           # Today's events (updated daily)
  YYYY-MM-DD_to_YYYY-MM-DD.md  # Weekly extracts
  extract_calendar.py # The extraction script
```

## Usage

To check Robin's schedule:

1. Read `mimir/calendar/today.md` for today's events
2. Read `mimir/calendar/YYYY-MM-DD_to_YYYY-MM-DD.md` for a week view

The calendar is extracted from Google Calendar ICS with proper RRULE expansion (recurring events are expanded into individual instances).

## Key Events

Look for these recurring events:
- **Bänklas Buam** - Thursdays, 20:00
- **Foto Babybauch** - Saturdays (varies)
- **RLE Work** - Weekday work blocks
- **Wake up/Morning Routine** - Daily habits

## Last Updated

Calendar sync runs daily at 7:55 AM (before the 9 AM email summary).
