#!/bin/bash
# Deploy @psyche Slack bot to Mac mini
# Usage: ./deploy-psyche-slack.sh [MAC_MINI_USER@HOST]

set -e

MAC_MINI="${1:-home@192.168.1.2}"
REPO_ROOT="$(cd "$(dirname "$0")/../../../.." && pwd)"

echo "═══ Deploying @psyche Slack bot to Mac mini ═══"
echo "Target: $MAC_MINI"
echo "Source: $REPO_ROOT/00-ORCHESTRATION/state/impl/deploy/"
echo ""

# ── Pre-flight checks ──
if ! command -v ssh &>/dev/null; then
    echo "Error: ssh not found. Install: brew install openssh"
    exit 1
fi

echo "[1/5] Checking SSH connectivity..."
if ! ssh -o ConnectTimeout=5 "$MAC_MINI" "echo 'SSH OK'" 2>/dev/null; then
    echo "Error: Cannot SSH to $MAC_MINI"
    echo "Fix: Establish SSH access (IMPL-D-0044: SSH alias + host-key pinning)"
    exit 1
fi

echo "[2/5] Copying configuration files..."
# Create directory if needed
ssh "$MAC_MINI" "mkdir -p ~/.openclaw"

# Copy config template (with placeholder tokens)
scp "$REPO_ROOT/00-ORCHESTRATION/state/impl/deploy/PSYCHE-SLACK-CONFIG.json" \
    "$MAC_MINI:~/.openclaw/openclaw.json.psyche-slack"

# Copy env template (Sovereign must edit with real tokens)
scp "$REPO_ROOT/00-ORCHESTRATION/state/impl/deploy/psyche-slack-env-template.sh" \
    "$MAC_MINI:~/.openclaw/.env.psyche-template"

echo "[3/5] Checking token configuration..."
if ! ssh "$MAC_MINI" "grep -q 'xapp-[A-Z]' ~/.openclaw/.env 2>/dev/null"; then
    echo "Warning: SLACK_APP_TOKEN_PSYCHE not set in ~/.openclaw/.env"
    echo "Action: Sovereign must add tokens per template: ~/.openclaw/.env.psyche-template"
    echo ""
    echo "To complete configuration:"
    echo "  1. SSH to Mac mini: ssh $MAC_MINI"
    echo "  2. Edit ~/.openclaw/.env and add:"
    echo "     SLACK_APP_TOKEN_PSYCHE=xapp-YOUR_APP_TOKEN"
    echo "     SLACK_BOT_TOKEN_PSYCHE=xoxb-YOUR_BOT_TOKEN"
    echo "  3. chmod 600 ~/.openclaw/.env"
fi

echo "[4/5] Installing health check script..."
# Copy health check monitor
ssh "$MAC_MINI" "mkdir -p ~/.syncrescendence/scripts"
scp "$REPO_ROOT/00-ORCHESTRATION/scripts/slack_health_check.sh" \
    "$MAC_MINI:~/.syncrescendence/scripts/slack_health_check.sh" 2>/dev/null || echo "(health check script not found, skipping)"

echo "[5/5] Testing Slack connectivity (after token config)..."
# Only test if tokens are present
if ssh "$MAC_MINI" "grep -q 'xapp-[A-Z]' ~/.openclaw/.env 2>/dev/null && grep -q 'xoxb-[A-Z]' ~/.openclaw/.env 2>/dev/null"; then
    echo "Tokens present. Testing..."
    ssh "$MAC_MINI" "source ~/.openclaw/.env && openclaw skill slack send --channel psyche-ops --message 'Psyche deployed successfully'" || echo "Test failed - check logs: tail -20 /tmp/syncrescendence-openclaw-gateway.log"
else
    echo "Tokens not yet configured. Skipping test."
fi

echo ""
echo "═══ Deployment Summary ═══"
echo "Config templates copied: ~/.openclaw/openclaw.json.psyche-slack"
echo "Env template: ~/.openclaw/.env.psyche-template"
echo ""
echo "To complete deployment:"
echo "  1. Ensure Slack app created and tokens generated"
echo "  2. Add tokens to ~/.openclaw/.env"
echo "  3. Run this script again to test"
echo "  4. Restart OpenClaw gateway: launchctl kickstart gui/$(ssh $MAC_MINI 'id -u') com.syncrescendence.openclaw-gateway.plist"
