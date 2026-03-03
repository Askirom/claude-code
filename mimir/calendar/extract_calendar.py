#!/usr/bin/env python3
"""
Calendar ICS Extractor for MIMIR Pro

Extracts events from Google Calendar ICS file, expands recurring events (RRULE),
and writes a human-readable summary to the repo. Any AI can read this to know
your schedule without needing auth.

Usage:
    python3 extract_calendar.py [--date YYYY-MM-DD] [--days 7]
"""

import argparse
import sys
from datetime import datetime, timedelta, date
from pathlib import Path
from typing import List, Optional

try:
    from icalendar import Calendar
    from dateutil.rrule import rrulestr, rruleset
    from dateutil.tz import gettz
except ImportError:
    print("ERROR: Missing dependencies. Install: pip install icalendar python-dateutil")
    sys.exit(1)


REPO_ROOT = Path("/root/.openclaw/workspace/claude-code")
ICS_SOURCE = Path.home() / ".calendars/google.ics"
OUTPUT_DIR = REPO_ROOT / "mimir/calendar"


def parse_ics(ics_path: Path) -> Calendar:
    """Parse the ICS file and return a Calendar object."""
    with open(ics_path, 'rb') as f:
        return Calendar.from_ical(f.read())


def get_event_instances(event, start_date: date, end_date: date) -> List[datetime]:
    """
    Get all occurrences of an event within a date range.
    Handles both single events and recurring events (RRULE).
    """
    dtstart = event.get('dtstart').dt
    
    # Handle date-only events (all-day)
    is_all_day = isinstance(dtstart, date) and not isinstance(dtstart, datetime)
    if is_all_day:
        dtstart = datetime.combine(dtstart, datetime.min.time())
    
    # If event starts after our range, skip
    if dtstart.date() > end_date:
        return []
    
    rrule = event.get('rrule')
    
    if not rrule:
        # Single event
        if start_date <= dtstart.date() <= end_date:
            return [dtstart]
        return []
    
    # Recurring event - expand RRULE
    try:
        # Get timezone info
        tz = dtstart.tzinfo or gettz('Europe/Berlin')
        
        # Build rruleset from the event
        ruleset = rruleset()
        
        # Parse the main RRULE
        rule_str = rrule.to_ical().decode('utf-8') if isinstance(rrule.to_ical(), bytes) else str(rrule.to_ical())
        
        # Handle the UNTIL timezone issue - convert to UTC format if needed
        # Google Calendar exports UNTIL in local time which breaks rrulestr
        if 'UNTIL=' in rule_str:
            import re
            # Find UNTIL value and ensure it's in UTC format (ends with Z)
            until_match = re.search(r'UNTIL=(\d{8}T\d{6})', rule_str)
            if until_match and not rule_str.endswith('Z'):
                # Replace with UTC format by adding Z
                until_val = until_match.group(1)
                rule_str = rule_str.replace(f'UNTIL={until_val}', f'UNTIL={until_val}Z')
        
        # Parse with dtstart
        rule = rrulestr(rule_str, dtstart=dtstart.replace(tzinfo=None) if dtstart.tzinfo else dtstart, 
                       ignoretz=True)
        ruleset.rrule(rule)
        
        # Handle EXDATE (excluded dates)
        exdates = event.get('exdate')
        if exdates:
            if not isinstance(exdates, list):
                exdates = [exdates]
            for exdate in exdates:
                if hasattr(exdate, 'dt'):
                    exdt = exdate.dt
                    if isinstance(exdt, datetime):
                        ruleset.exdate(exdt.replace(tzinfo=None))
                    else:
                        ruleset.exdate(datetime.combine(exdt, datetime.min.time()))
        
        # Create datetime range for expansion (naive, we'll handle tz separately)
        range_start = datetime.combine(start_date, datetime.min.time())
        range_end = datetime.combine(end_date, datetime.max.time().replace(microsecond=0))
        
        # Get occurrences within range
        occurrences = list(ruleset.between(range_start, range_end, inc=True))
        
        # Add timezone back to occurrences
        if dtstart.tzinfo:
            occurrences = [o.replace(tzinfo=tz) for o in occurrences]
        else:
            occurrences = [o.replace(tzinfo=gettz('Europe/Berlin')) for o in occurrences]
        
        return occurrences
        
    except Exception as e:
        print(f"Warning: Could not expand RRULE for '{event.get('summary', 'Unknown')}': {e}")
        # Fallback: include original date if in range
        if start_date <= dtstart.date() <= end_date:
            return [dtstart]
        return []


def extract_events(calendar: Calendar, start_date: date, end_date: date) -> List[dict]:
    """
    Extract all events from calendar that occur within the date range.
    Expands recurring events into individual instances.
    """
    events = []
    
    for component in calendar.walk():
        if component.name != "VEVENT":
            continue
        
        summary = str(component.get('summary', 'No Title'))
        
        # Get all occurrences within range
        occurrences = get_event_instances(component, start_date, end_date)
        
        for occ in occurrences:
            # Calculate duration
            dtend = component.get('dtend')
            if dtend:
                duration = dtend.dt - component.get('dtstart').dt
                occ_end = occ + duration
            else:
                occ_end = occ
            
            events.append({
                'summary': summary,
                'start': occ,
                'end': occ_end,
                'location': str(component.get('location', '')),
                'description': str(component.get('description', '')),
                'uid': str(component.get('uid', ''))
            })
    
    # Sort by start time
    events.sort(key=lambda e: e['start'])
    return events


def format_event(event: dict) -> str:
    """Format a single event as markdown."""
    start = event['start']
    
    # Format based on whether it's all-day or timed
    if start.hour == 0 and start.minute == 0:
        # All-day event
        date_str = start.strftime("%Y-%m-%d")
        time_str = "(all day)"
    else:
        date_str = start.strftime("%Y-%m-%d")
        time_str = start.strftime("%H:%M")
        if event['end'] != event['start']:
            time_str += f" - {event['end'].strftime('%H:%M')}"
    
    lines = [f"- **{date_str}** {time_str} — {event['summary']}"]
    
    if event['location']:
        lines.append(f"  📍 {event['location']}")
    
    return "\n".join(lines)


def generate_summary(events: List[dict], start_date: date, end_date: date) -> str:
    """Generate a markdown summary of events."""
    lines = [
        f"# Calendar: {start_date} to {end_date}",
        "",
        f"_Extracted from Google Calendar. {len(events)} events._",
        ""
    ]
    
    if not events:
        lines.append("*No events in this period.*")
        return "\n".join(lines)
    
    # Group by date
    current_date = None
    for event in events:
        event_date = event['start'].date()
        
        if event_date != current_date:
            current_date = event_date
            day_name = event_date.strftime("%A")
            lines.append(f"\n## {day_name}, {event_date}")
            lines.append("")
        
        lines.append(format_event(event))
    
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Extract calendar events from ICS")
    parser.add_argument("--date", type=str, help="Start date (YYYY-MM-DD), default: today")
    parser.add_argument("--days", type=int, default=7, help="Number of days to extract (default: 7)")
    parser.add_argument("--output", type=str, help="Output file (default: auto-generated)")
    args = parser.parse_args()
    
    # Determine date range
    if args.date:
        start_date = datetime.strptime(args.date, "%Y-%m-%d").date()
    else:
        start_date = date.today()
    
    end_date = start_date + timedelta(days=args.days - 1)
    
    # Parse ICS
    if not ICS_SOURCE.exists():
        print(f"ERROR: ICS file not found: {ICS_SOURCE}")
        print("Run: vdirsyncer sync  (to fetch from Google)")
        sys.exit(1)
    
    print(f"Parsing {ICS_SOURCE}...")
    calendar = parse_ics(ICS_SOURCE)
    
    # Extract events
    print(f"Extracting events from {start_date} to {end_date}...")
    events = extract_events(calendar, start_date, end_date)
    
    # Generate summary
    summary = generate_summary(events, start_date, end_date)
    
    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        output_path = OUTPUT_DIR / f"{start_date}_to_{end_date}.md"
    
    # Write output
    output_path.write_text(summary)
    print(f"✓ Wrote {len(events)} events to {output_path}")
    
    # Also write a "today" file for quick access
    today_path = OUTPUT_DIR / "today.md"
    today_events = [e for e in events if e['start'].date() == date.today()]
    today_summary = generate_summary(today_events, date.today(), date.today())
    today_path.write_text(today_summary)
    print(f"✓ Wrote today's events to {today_path}")


if __name__ == "__main__":
    main()
