# VPS — askirom-mimir

## Specs
Hetzner CPX22 — 4 vCPU, 8GB RAM, 80GB SSD, Ubuntu 24.04
IP: 46.224.192.48 | User: askirom

## Access
Cloudflare Zero Trust Tunnel "mimir" — kein Port-Exposure
Alle Services über HTTPS via Cloudflare Edge

## Services
| Domain | Service | Port | Auth |
|--------|---------|------|------|
| notes.askirom.eu | SilverBullet 2.4.1 | 3001 | Basic Auth (SB intern) |
| opencode.askirom.eu | OpenCode | 3000 | CF Access |
| admin.askirom.eu | Cockpit | 9090 | CF Access + Linux Login |
| paste.askirom.eu | PrivateBin | via Caddy | — |
| speed.askirom.eu | LibreSpeed | via Caddy | — |
| ntfy.askirom.eu | ntfy 2.17.0 | 2586 | ntfy Auth |

## Infrastruktur
- **Caddy** — zentraler Reverse Proxy, Port 80, auto_https off
- **cloudflared** — Tunnel managed via CF Dashboard
- **CF Access** — opencode + admin geschützt

## Daten
- `~/mimir/` — MIMIR Git-Repo (GitHub), auto-commit alle 30min
- `~/drive/` — Google Drive 2TB via rclone
- `~/calendars/` + `~/contacts/` — Fastmail via vdirsyncer
- `~/mail/` — Fastmail via mbsync

## Cron Jobs
- vdirsyncer sync alle 5min → ntfy bei Fehler
- mbsync alle 5min → ntfy bei Fehler
- mimir git push alle 30min → ntfy bei Fehler
- Disk-Check täglich 9 Uhr → ntfy über 80%
- RAM-Check täglich 9 Uhr → ntfy über 85%

## Installierte Tools
zsh, tmux, fzf, eza, ripgrep, bun, Claude Code, OpenCode, SilverBullet, Caddy, cloudflared, rclone, vdirsyncer, mbsync, khal, khard, ntfy, PrivateBin, Cockpit

## Offener Backlog
- [ ] fail2ban installieren
- [ ] Caddy/cron config in mimir/.system committen

