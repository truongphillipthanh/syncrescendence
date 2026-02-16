#!/usr/bin/env bash
# MBA Cascade Supplement - Homebrew Formula Installation
# Run: bash 00-ORCHESTRATION/scripts/mba-cascade-install.sh
# TASK-20260211-MBA_CASCADE_SUPPLEMENT | 2026-02-11
set -euo pipefail

echo "=== MBA Cascade: Homebrew Formula Installation ==="

MISSING=(atuin ncdu procs tig yazi neovim fastfetch sesh zsh-autosuggestions zsh-syntax-highlighting terminal-notifier tokei tldr mas topgrade)

for pkg in "${MISSING[@]}"; do
    echo "[INSTALL] $pkg..."
    brew install "$pkg" || echo "[WARN] $pkg failed"
done

echo ""
echo "=== Verification ==="
TOOLS="bat eza fd rg sd dust duf btop fzf zoxide starship lazygit glow delta gh atuin ncdu procs tig yazi nvim fastfetch sesh tokei tldr mas topgrade terminal-notifier"
for tool in $TOOLS; do
    if command -v "$tool" >/dev/null 2>&1; then
        echo "  [OK] $tool"
    else
        echo "  [MISS] $tool"
    fi
done
