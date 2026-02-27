#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE}")/config.sh"

# triage_inbox.sh — List PENDING/IN_PROGRESS tasks for an agent's inbox
# Usage: bash triage_inbox.sh [AGENT]
#
# Shows:
#   - PENDING tasks (ready for pickup)
#   - IN_PROGRESS tasks (currently being worked)
#   - Stale IN_PROGRESS tasks (claimed > N minutes ago)
#   - Claimed files (.claimed-by-*)
#   - Completed/failed files
#
# Examples:
#   bash triage_inbox.sh commander
#   bash triage_inbox.sh          # defaults to all agents

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
if [ -z "$REPO_ROOT" ]; then
    REPO_ROOT="$HOME/Desktop/syncrescendence"
fi

AGENT="${1:-}"
STALE_MINUTES=60
INBOX_ROOT="$REPO_ROOT/-INBOX"

echo "=== INBOX TRIAGE ==="
echo "Time: $(date '+%Y-%m-%d %H:%M:%S')"
echo "Stale threshold: ${STALE_MINUTES} minutes"
echo ""

triage_agent() {
    local agent="$1"
    local agent_dir="$INBOX_ROOT/$agent"

    if [ ! -d "$agent_dir" ]; then
        return
    fi

    local has_items=false

    # PENDING tasks
    for file in "$agent_dir"/TASK-*.md; do
        [ -f "$file" ] || continue
        if grep -q "Status.*PENDING" "$file" 2>/dev/null; then
            if [ "$has_items" = false ]; then
                echo "── $agent ──"
                has_items=true
            fi
            local priority
            priority=$(grep -o "Priority.*P[0-3]" "$file" 2>/dev/null | head -1 | grep -o "P[0-3]" || echo "P?")
            echo "  PENDING  $(basename "$file")  ($priority)"
        fi
    done

    # IN_PROGRESS tasks
    for file in "$agent_dir"/TASK-*.md; do
        [ -f "$file" ] || continue
        if grep -q "Status.*IN_PROGRESS" "$file" 2>/dev/null; then
            if [ "$has_items" = false ]; then
                echo "── $agent ──"
                has_items=true
            fi
            # Check staleness
            local mod_time now_time age_min stale_marker=""
            if [[ "$(uname)" == "Darwin" ]]; then
                mod_time=$(stat -f %m "$file")
            else
                mod_time=$(stat -c %Y "$file")
            fi
            now_time=$(date +%s)
            age_min=$(( (now_time - mod_time) / 60 ))
            if [ "$age_min" -gt "$STALE_MINUTES" ]; then
                stale_marker=" [STALE ${age_min}m]"
            fi
            echo "  IN_PROGRESS  $(basename "$file")${stale_marker}"
        fi
    done

    # Claimed files
    for file in "$agent_dir"/TASK-*.md.claimed-by-*; do
        [ -f "$file" ] || continue
        if [ "$has_items" = false ]; then
            echo "── $agent ──"
            has_items=true
        fi
        echo "  CLAIMED  $(basename "$file")"
    done

    # Completed files
    for file in "$agent_dir"/TASK-*.md.complete; do
        [ -f "$file" ] || continue
        if [ "$has_items" = false ]; then
            echo "── $agent ──"
            has_items=true
        fi
        echo "  COMPLETE $(basename "$file")"
    done

    # Failed files
    for file in "$agent_dir"/TASK-*.md.failed; do
        [ -f "$file" ] || continue
        if [ "$has_items" = false ]; then
            echo "── $agent ──"
            has_items=true
        fi
        echo "  FAILED   $(basename "$file")"
    done

    if [ "$has_items" = true ]; then
        echo ""
    fi
}

if [ -n "$AGENT" ]; then
    triage_agent "$AGENT"
else
    for agent_dir in "$INBOX_ROOT"/*/; do
        [ -d "$agent_dir" ] || continue
        agent=$(basename "$agent_dir")
        [ "$agent" = "outputs" ] && continue
        triage_agent "$agent"
    done
fi

echo "=== END TRIAGE ==="
