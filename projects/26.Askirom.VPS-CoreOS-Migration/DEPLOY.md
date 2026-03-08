# Post-Bootstrap Deploy Guide

After running `bootstrap.sh`, follow these steps.

## 1. Enable lingering (user services start at boot)

```bash
sudo loginctl enable-linger askirom
```

## 2. Clone repos

```bash
# Add SSH key to GitHub first: cat ~/.ssh/id_ed25519.pub
git clone git@github.com:Askirom/askirom-mimir.git ~/mimir
git clone git@github.com:Askirom/mimir-dashboard.git ~/dashboard
```

## 3. Set up config files

```bash
# Caddy
mkdir -p ~/.config/caddy
cp ~/mimir/projects/26.Askirom.VPS-CoreOS-Migration/Caddyfile.new ~/.config/caddy/Caddyfile

# cloudflared (paste token from Cloudflare dashboard)
mkdir -p ~/.config/cloudflared
cp ~/mimir/projects/26.Askirom.VPS-CoreOS-Migration/env-templates/cloudflared.env ~/.config/cloudflared/env
# EDIT: paste actual token

# SilverBullet
mkdir -p ~/.config/silverbullet
cp ~/mimir/projects/26.Askirom.VPS-CoreOS-Migration/env-templates/silverbullet.env ~/.config/silverbullet/env
# EDIT: set actual password

# ntfy
mkdir -p ~/.config/ntfy
cp ~/mimir/projects/26.Askirom.VPS-CoreOS-Migration/ntfy-server.yml ~/.config/ntfy/server.yml
# Restore user.db into the ntfy-data volume after first start
```

## 4. Deploy quadlets

```bash
mkdir -p ~/.config/containers/systemd
cp ~/mimir/projects/26.Askirom.VPS-CoreOS-Migration/quadlets/*.container ~/.config/containers/systemd/
systemctl --user daemon-reload
systemctl --user start caddy cloudflared silverbullet ntfy filebrowser privatebin ttyd librespeed
```

## 5. Services that stay native (not containerized)

### Cockpit
```bash
sudo dnf install cockpit cockpit-podman
sudo systemctl enable --now cockpit.socket
```

### MIMIR Dashboard
Custom Bun app. Run natively since it reads ~/calendars/, ~/contacts/, ~/mimir/:
```bash
cd ~/dashboard && bun install
# Copy mimir-dash.service to ~/.config/systemd/user/
cp ~/dashboard/mimir-dash.service ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable --now mimir-dash
```

### OpenCode
Native binary. Install and run as user service:
```bash
# Install opencode (check latest install method)
# Create systemd user service similar to original
```

### Kimi
Was running manually (no service). Set up if still needed.

## 6. vdirsyncer (calendar/contacts sync)

```bash
# Install already done via bootstrap (dnf)
mkdir -p ~/.config/vdirsyncer
# Configure vdirsyncer for Fastmail CalDAV/CardDAV
# See Bitwarden for Fastmail app password
vdirsyncer discover
vdirsyncer sync
# Set up cron/timer for periodic sync
```

## 7. Hetzner Storage Box

```bash
sudo mkdir -p /mnt/storagebox
# Create credentials file
sudo bash -c 'cat > /etc/smbcredentials <<EOF
username=u558593
password=CHANGE_ME
EOF'
sudo chmod 600 /etc/smbcredentials

# Add to /etc/fstab
echo "//u558593.your-storagebox.de/backup /mnt/storagebox cifs credentials=/etc/smbcredentials,uid=1000,gid=1000,_netdev 0 0" | sudo tee -a /etc/fstab
sudo mount -a
```

## 8. himalaya (email)

```bash
# Already installed via bootstrap
mkdir -p ~/.config/himalaya
# Copy/recreate config.toml for Fastmail IMAP/SMTP
# See Bitwarden for Fastmail app password
```
