# PROJECT: VPS Fedora Migration

## State
**Phase:** ② Question → ③ Build transition
**Created:** 2026-03-08
**Done when:** CPX32 runs Fedora 43 with all 10 services containerized via Podman quadlets, reachable at their current subdomains, reproducible from quadlet files + setup script.

## Context

Robin's Hetzner VPS (askirom-mimir, CPX32, Ubuntu 24.04, Nürnberg DC) is being rebuilt on Fedora 43 Server. All services will be containerized with Podman quadlets.

Originally planned as CoreOS → uCore, but switched to Fedora Server for pragmatic reasons: Hetzner offers Fedora as a base image (clean reinstall), standard mutable OS is easier to debug and maintain, and the real value is in containerization, not the immutable OS. CoreOS remains a future option once all containers are proven.

All services currently run behind Cloudflare Tunnel → Caddy reverse proxy on the VPS. The domain is askirom.eu with DNS managed in Cloudflare.

## Current Services (all need containerization)

| Subdomain | Service | Container Image | Notes |
|---|---|---|---|
| notes.askirom.eu | SilverBullet | ghcr.io/silverbulletmd/silverbullet | Knowledge base, ~/mimir/ |
| dash.askirom.eu | MIMIR Dashboard | Custom (Bun) | ~/dashboard/, port 3002 |
| files.askirom.eu | Filebrowser | filebrowser/filebrowser | Port 8085 |
| opencode.askirom.eu | OpenCode Web | TBD | Port 3000, research needed |
| paste.askirom.eu | PrivateBin | privatebin/nginx-fpm-alpine | |
| admin.askirom.eu | Cockpit | Native (dnf install cockpit) | Runs on host, not containerized |
| ntfy.askirom.eu | ntfy push notifications | binwiederhier/ntfy | |
| speed.askirom.eu | librespeed-rs | TBD | Rust-based, check for image |
| tty.askirom.eu | ttyd terminal | tsl0922/ttyd | |
| kimi.askirom.eu | Kimi AI interface | TBD | Research needed |

## Infrastructure Stack (Target)

- **OS:** Fedora 43 Server (Hetzner base image)
- **Container runtime:** Podman with quadlets (systemd-native)
- **Reverse proxy:** Caddy (containerized)
- **Tunnel:** cloudflared (containerized)
- **Drive mount:** rclone (systemd unit with FUSE)
- **Admin:** Cockpit (native package, routed through Caddy)
- **DNS:** Cloudflare (unchanged)

## Constraints

- CPX32 is the production VPS. Snapshot before touching anything
- All services must remain reachable at same subdomains after migration
- Cloudflare Tunnel token/config must be preserved (grab before rebuild)
- rclone config + Google Drive mount needs to be set up again
- Some container images still need research (opencode, speed, kimi)

## Risks

- If migration fails, restore from Hetzner snapshot
- rclone FUSE mount needs `--allow-other` and `/etc/fuse.conf` config
- Dashboard is a custom Bun app. Needs a Dockerfile or run via bun container image
- Cockpit runs on host (not in container). Caddy must proxy to localhost:9090

## Open Questions

1. What is kimi.askirom.eu running? (Custom proxy to Kimi API?)
2. What is opencode.askirom.eu running exactly? (OpenCode CLI web wrapper?)
3. Is there a container image for librespeed-rs, or do we build one?
4. Current Caddy config. Export before rebuild
5. Current Cloudflare Tunnel config/token. Export before rebuild
6. Current rclone config. Export before rebuild
7. SSH public keys for new server

---

## Execution Plan

### Batch 1: Export & Backup (before touching anything)

1. Create Hetzner Cloud snapshot of CPX32. Confirm snapshot visible in console
2. Export `/etc/caddy/Caddyfile` (or wherever Caddy config lives)
3. Export Cloudflare Tunnel credentials (`~/.cloudflared/` or systemd config)
4. Export rclone config (`~/.config/rclone/rclone.conf`)
5. Export SSH public keys
6. Document each service: config files, persistent data paths
7. Export persistent data (SilverBullet notes are git-synced, ntfy db, PrivateBin data, etc.)

### Batch 2: Rebuild on Fedora 43

8. Rebuild CPX32 with Fedora 43 base image via Hetzner Console
9. SSH in, set hostname, timezone, locale
10. Install Podman, Cockpit: `dnf install podman cockpit cockpit-podman`
11. Enable and start Cockpit: `systemctl enable --now cockpit.socket`
12. Set up SSH keys, harden SSH config (disable password auth)
13. Set up firewall (firewalld): allow 80, 443, 9090 (Cockpit)

### Batch 3: Core Infrastructure

14. Write Podman quadlet for Caddy with Caddyfile mounted
15. Write Podman quadlet for cloudflared with tunnel token
16. Deploy quadlets to `/etc/containers/systemd/`, reload systemd
17. Verify Caddy + cloudflared are running, tunnel is connected
18. Set up rclone as systemd unit, mount Google Drive to ~/gdrive/

### Batch 4: Deploy Services

19. Write Podman quadlet for SilverBullet (mount ~/mimir/)
20. Write Podman quadlet for MIMIR Dashboard (build from ~/dashboard/ or use bun image)
21. Write Podman quadlet for Filebrowser
22. Write Podman quadlet for PrivateBin
23. Write Podman quadlet for ntfy
24. Write Podman quadlet for ttyd
25. Write Podman quadlet for librespeed-rs
26. Write Podman quadlet for opencode
27. Write Podman quadlet for kimi
28. Update Caddyfile with all service reverse proxy routes

### Batch 5: Verify & Harden

29. Test every subdomain from browser. Confirm all 10 work
30. Verify Cockpit accessible at admin.askirom.eu
31. Set up automatic updates: `dnf install dnf-automatic && systemctl enable --now dnf-automatic-install.timer`
32. Review SELinux status, fix any container denials
33. Document final config in Git repo for reproducibility
34. Delete old Hetzner snapshot once stable (or keep as insurance)

---

## Parking Lot

- Future: rebase to Fedora CoreOS / uCore once all containers are proven
- Future: automate full VPS provisioning with Terraform or Ansible
- Future: move quadlet files into a Git repo for GitOps-style management
