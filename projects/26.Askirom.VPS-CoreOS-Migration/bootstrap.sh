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

# 3. Passwordless sudo for askirom
echo "askirom ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/askirom

# 4. Harden SSH
sed -i 's/^#\?PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config
sed -i 's/^#\?PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config
systemctl restart sshd

# 5. Install essentials
dnf install -y zsh git curl podman

# 6. Install Bun
su - askirom -c 'curl -fsSL https://bun.sh/install | bash'

# 7. Install Claude Code
su - askirom -c 'source ~/.zshrc && bun install -g @anthropic-ai/claude-code'

echo ""
echo "Done. SSH in as askirom and run: claude"
echo "WARNING: root SSH is now disabled. Use: ssh askirom@<ip>"
