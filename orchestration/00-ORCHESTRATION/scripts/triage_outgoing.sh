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

echo "-- PENDING / IN_PROGRESS TASKS (agents/*/inbox) --"
for agent_dir in ./agents/*/inbox/pending; do
    agent=$(basename "$(dirname "$agent_dir")")
    tasks=$(ls "$agent_dir"/TASK-*.md 2>/dev/null)
    if [ -n "$tasks" ]; then
        count=$(echo "$tasks" | wc -l | tr -d ' ')
        echo "  [$agent] $count task(s):"
        for f in $tasks; do
            status=$(grep -o 'Status.*' "$f" 2>/dev/null | head -1 | sed 's/\*//g')
            echo "    - $(basename "$f") — $status"
        done
    fi
done
total=$(find ./agents -name "TASK-*.md" -path "*/inbox/pending/*" 2>/dev/null | wc -l | tr -d ' ')
[ "$total" -eq 0 ] && echo "(none)"
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
