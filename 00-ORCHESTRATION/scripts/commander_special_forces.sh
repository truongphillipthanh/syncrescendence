#!/usr/bin/env bash
# commander_special_forces.sh — Commander session entry (manual on Psyche laptop)
#
# Philosophy: this shell is an intervention lane. Assume you're about to do high-impact work.
# - Hydrate state quickly
# - Make current context obvious
# - Enter Claude Code in dangerously-skip-permissions mode

set -euo pipefail

REPO="$HOME/Desktop/syncrescendence"
cd "$REPO"

echo "[Commander] SPECIAL FORCES MODE"
echo "Repo: $REPO"
echo "Time: $(date '+%Y-%m-%d %H:%M:%S')"
echo

echo "--- git status"
git status --short || true
echo

echo "--- triage (pipes)"
# triage_outgoing.sh is expected post-plumbing-hardening
bash 00-ORCHESTRATION/scripts/triage_outgoing.sh 2>/dev/null || true
echo

echo "--- inbox: commander"
ls -1 -t agents/commander/inbox/ 2>/dev/null | head -n 20 || true

echo

echo "Entering Claude Code (dangerously-skip-permissions)…"
# Prefer dangerously-skip-permissions for this intervention lane.
# If your claude binary uses a different flag name on your machine, adjust here.
exec claude --dangerously-skip-permissions
