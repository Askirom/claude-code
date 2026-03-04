---
name: vps-pim
description: Local PIM (Personal Information Management) tools on the VPS. Use khal for calendar, khard for contacts, and mbsync for mail. All tools sync bidirectionally with remote servers.
---

# VPS PIM Tools

Local Personal Information Management stack on the VPS. All tools support **two-way synchronization** with remote servers.

## Tools

### khal – Calendar

CLI calendar viewer. Reads from local vdir (`~/.calendars/`).

```bash
# Today's events + next 7 days
khal list today 7d

# Specific date range
khal list 2026-03-04 14d

# Interactive calendar
khal interactive
```

**Sync:** `vdirsyncer sync` (two-way with CalDAV server)

### khard – Contacts

CLI contact manager. Reads from local vdir (`~/.contacts/`).

```bash
# List all contacts
khard list

# Search contacts
khard list "max muster"

# Show contact details
khard show "max muster"

# Add new contact
khard add
```

**Sync:** `vdirsyncer sync` (two-way with CardDAV server)

### mbsync – Mail

IMAP mailbox synchronizer. Syncs Maildirs with remote IMAP server.

```bash
# Sync all channels
mbsync -a

# Sync specific channel
mbsync gmail

# List mailboxes
mbsync -l

# Dry run (no changes)
mbsync -n -a
```

**Config:** `~/.mbsyncrc`

**Two-way:** Propagates new mails, deletions, and flag changes (read/unread) in both directions.

## Quick Reference

| Task | Command |
|------|---------|
| Calendar today | `khal list today` |
| Calendar week | `khal list today 7d` |
| Find contact | `khard list "name"` |
| Sync calendars | `vdirsyncer sync` |
| Sync contacts | `vdirsyncer sync` |
| Sync mail | `mbsync -a` |

## Sync All

```bash
# Full PIM sync
vdirsyncer sync && mbsync -a
```

## Notes

- **khal/khard:** Require `vdirsyncer` to populate local vdirs from CalDAV/CardDAV
- **mbsync:** Direct IMAP sync, no intermediate tool needed
- All syncs are **bidirectional** – local changes push to server, remote changes pull to local
