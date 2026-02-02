#!/usr/bin/env bash
# triage_outgoing.sh — Packet lifecycle observability
# Shows pending tasks, prompts, sovereign briefs, and git dirtiness
# Usage: bash triage_outgoing.sh

set -euo pipefail

cd "$(git rev-parse --show-toplevel)"

echo "=== TRIAGE: PIPE STATUS ==="
echo "Time: $(date '+%Y-%m-%d %H:%M:%S')"
echo "HEAD: $(git rev-parse --short HEAD 2>/dev/null || echo unknown)"
echo

echo "-- git status --"
git status --short || true
echo

echo "-- PENDING / IN_PROGRESS TASKS (-INBOX) --"
if command -v rg &>/dev/null; then
    rg -n "Status.*(PENDING|IN_PROGRESS)" --glob "TASK-*.md" "./-INBOX/" 2>/dev/null || echo "(none)"
else
    grep -rn "Status.*\(PENDING\|IN_PROGRESS\)" ./-INBOX/*/TASK-*.md 2>/dev/null || echo "(none)"
fi
echo

echo "-- PENDING PROMPTS (-OUTGOING) --"
if command -v rg &>/dev/null; then
    rg -n "Status.*PENDING" --glob "!README.md" "./-OUTGOING/" 2>/dev/null || echo "(none)"
else
    grep -rn "Status.*PENDING" ./-OUTGOING/PROMPT-*.md 2>/dev/null || echo "(none)"
fi
echo

echo "-- PENDING SOVEREIGN BRIEFS (-SOVEREIGN) --"
if command -v rg &>/dev/null; then
    rg -n "Status.*PENDING" --glob "SOVEREIGN-*.md" "./-SOVEREIGN/" 2>/dev/null || echo "(none)"
else
    grep -rn "Status.*PENDING" ./-SOVEREIGN/SOVEREIGN-*.md 2>/dev/null || echo "(none)"
fi
echo

echo "=== END TRIAGE ==="
