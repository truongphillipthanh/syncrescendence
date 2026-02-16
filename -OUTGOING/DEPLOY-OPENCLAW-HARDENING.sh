#!/bin/bash
# DEPLOY-OPENCLAW-HARDENING.sh
# Deploys hardened OpenClaw personality files for Psyche on Mac mini
# Run from: /Users/home/Desktop/syncrescendence
# Authority: Zero-offline hardening campaign 2026-02-16

set -u

REPO="/Users/home/Desktop/syncrescendence"
OPENCLAW_DIR="/Users/home/.openclaw"
STAGING="${REPO}/-OUTGOING"

echo "=== OpenClaw Psyche Hardening Deployment ==="
echo "Target: ${OPENCLAW_DIR}"
echo ""

# Backup existing files
BACKUP_DIR="${OPENCLAW_DIR}/backup-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$BACKUP_DIR"
for f in SOUL.md AGENTS.md HEARTBEAT.md MEMORY.md USER.md; do
    if [ -f "${OPENCLAW_DIR}/${f}" ]; then
        cp "${OPENCLAW_DIR}/${f}" "${BACKUP_DIR}/${f}"
        echo "[backup] ${f} → ${BACKUP_DIR}/"
    fi
done

# Deploy hardened files
for f in SOUL AGENTS HEARTBEAT MEMORY USER; do
    src="${STAGING}/OPENCLAW-HARDENING-PSYCHE-${f}.md"
    dst="${OPENCLAW_DIR}/${f}.md"
    if [ -f "$src" ]; then
        cp "$src" "$dst"
        echo "[deploy] ${f}.md ← ${src}"
    else
        echo "[SKIP]  ${src} not found"
    fi
done

echo ""
echo "=== Deployment Complete ==="
echo "Backup at: ${BACKUP_DIR}"
echo ""
echo "Next steps:"
echo "  1. Restart OpenClaw gateway: openclaw restart"
echo "  2. Verify: openclaw tui --session main"
echo "  3. Commit: git add -A && git commit -m 'feat(hardening): OpenClaw Psyche personality hardened with operational awareness'"
