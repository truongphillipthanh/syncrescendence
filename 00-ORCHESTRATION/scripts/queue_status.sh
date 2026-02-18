#!/bin/bash
# queue_status.sh — Print kanban queue status for all agents
# Usage: bash queue_status.sh [AGENT]
#
# If no agent is specified, prints status for all agents.
# Protocol: DYN-DISPATCH_KANBAN_PROTOCOL.md

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
if [ -z "$REPO_ROOT" ]; then
    REPO_ROOT="$HOME/Desktop/syncrescendence"
fi

TARGET_AGENT="${1:-}"
AGENTS="commander adjudicator cartographer psyche ajna"
LANES="00-INBOX0 10-IN_PROGRESS 20-WAITING 30-BLOCKED 40-DONE 50_FAILED"

echo "=== DISPATCH QUEUE STATUS ==="
echo "$(date '+%Y-%m-%d %H:%M:%S')"
echo ""

for agent in $AGENTS; do
    if [ -n "$TARGET_AGENT" ] && [ "$agent" != "$TARGET_AGENT" ]; then
        continue
    fi

    agent_dir="$REPO_ROOT/-INBOX/$agent"
    if [ ! -d "$agent_dir" ]; then
        continue
    fi

    has_items=false
    counts=""
    for lane in $LANES; do
        lane_dir="$agent_dir/$lane"
        if [ ! -d "$lane_dir" ]; then
            continue
        fi
        count=$(find "$lane_dir" -maxdepth 1 -name "*.md" -not -name ".gitkeep" -type f 2>/dev/null | wc -l | tr -d ' ')
        if [ "$count" -gt 0 ]; then
            has_items=true
            counts="$counts  $lane: $count"
        fi
    done

    # Also count receipts
    receipts_dir="$agent_dir/RECEIPTS"
    if [ -d "$receipts_dir" ]; then
        rcount=$(find "$receipts_dir" -maxdepth 1 -name "*.md" -not -name ".gitkeep" -type f 2>/dev/null | wc -l | tr -d ' ')
        if [ "$rcount" -gt 0 ]; then
            counts="$counts  RECEIPTS: $rcount"
        fi
    fi

    if [ "$has_items" = true ] || [ -n "$counts" ]; then
        echo "[$agent]"
        echo "$counts"

        # List items in active lanes (INBOX0 and IN_PROGRESS)
        for active_lane in 00-INBOX0 10-IN_PROGRESS; do
            active_dir="$agent_dir/$active_lane"
            if [ -d "$active_dir" ]; then
                for file in "$active_dir"/*.md; do
                    [ -f "$file" ] || continue
                    fname=$(basename "$file")
                    [ "$fname" = ".gitkeep" ] && continue
                    echo "    [$active_lane] $fname"
                done
            fi
        done
        echo ""
    else
        echo "[$agent] (empty)"
        echo ""
    fi
done

# Outbox summary
echo "--- OUTBOX ---"
for agent in $AGENTS; do
    outbox="$REPO_ROOT/-OUTBOX/$agent"
    if [ -d "$outbox" ]; then
        rcount=$(find "$outbox/RESULTS" -maxdepth 1 -name "*.md" -not -name ".gitkeep" -type f 2>/dev/null | wc -l | tr -d ' ')
        acount=$(find "$outbox/ARTIFACTS" -maxdepth 1 -not -name ".gitkeep" -type f 2>/dev/null | wc -l | tr -d ' ')
        if [ "$rcount" -gt 0 ] || [ "$acount" -gt 0 ]; then
            echo "  $agent: $rcount results, $acount artifacts"
        fi
    fi
done
