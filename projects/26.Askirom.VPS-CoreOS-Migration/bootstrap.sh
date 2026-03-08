#!/bin/bash
# VPS Bootstrap: Run as root after Fedora 43 rebuild
# Gets the server to a point where Claude Code can take over

set -euo pipefail

# 1. System basics
hostnamectl set-hostname askirom-mimir
timedatectl set-timezone Europe/Vienna
dnf update -y

# 2. Create user
useradd -m -s /bin/zsh askirom
usermod -aG wheel askirom
mkdir -p /home/askirom/.ssh
cp /root/.ssh/authorized_keys /home/askirom/.ssh/authorized_keys
chown -R askirom:askirom /home/askirom/.ssh
chmod 700 /home/askirom/.ssh
chmod 600 /home/askirom/.ssh/authorized_keys

# 3. Also generate a keypair for askirom (for GitHub, etc.)
su - askirom -c 'ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N ""'

# 4. Passwordless sudo for askirom
echo "askirom ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/askirom

# 5. Harden SSH
sed -i 's/^#\?PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config
sed -i 's/^#\?PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config
systemctl restart sshd

# 6. Install system packages
dnf install -y \
  zsh git curl \
  podman \
  khal khard vdirsyncer \
  cifs-utils \
  firewalld

# 7. Install Bun
su - askirom -c 'curl -fsSL https://bun.sh/install | bash'

# 8. Install Claude Code
su - askirom -c 'source ~/.zshrc && bun install -g @anthropic-ai/claude-code'

# 9. Install himalaya (not in Fedora repos)
HIMALAYA_VERSION="1.0.0"
curl -fsSL "https://github.com/pimalaya/himalaya/releases/latest/download/himalaya.x86_64-unknown-linux-gnu.tar.gz" | tar xz -C /usr/local/bin/

# 10. Firewall (only allow SSH for now, Caddy ports added later)
systemctl enable --now firewalld
firewall-cmd --permanent --add-service=ssh
firewall-cmd --reload

echo ""
echo "Done. SSH in as askirom and run: claude"
echo "WARNING: root SSH is now disabled. Use: ssh askirom@<ip>"
echo ""
echo "Next steps (via Claude Code):"
echo "  - Add SSH key to GitHub: cat ~/.ssh/id_ed25519.pub"
echo "  - Clone mimir repo"
echo "  - Set up Podman quadlets for all services"
echo "  - Set up vdirsyncer, himalaya configs"
echo "  - Mount Hetzner Storage Box via CIFS"
