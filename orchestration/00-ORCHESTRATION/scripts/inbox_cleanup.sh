#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE}")/config.sh"

# inbox_cleanup.sh — Batch process CONFIRM/RESULT/EXECLOG from an agent's inbox
# Usage: bash inbox_cleanup.sh [agent] [--dry-run]
# Default agent: commander
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || echo "$HOME/Desktop/syncrescendence")"
AGENT="${1:-commander}"
DRY_RUN="${2:-}"

INBOX0="$REPO_ROOT/agents/$AGENT/inbox/pending"
RECEIPTS="$REPO_ROOT/agents/$AGENT/inbox/RECEIPTS"

mkdir -p "$RECEIPTS"

count=0
for f in "$INBOX0"/CONFIRM-*.md "$INBOX0"/RESULT-*.md "$INBOX0"/EXECLOG-*.log; do
    [ -f "$f" ] || continue
    base=$(basename "$f")
    if [ "$DRY_RUN" = "--dry-run" ]; then
        echo "[DRY] Would move: $base -> RECEIPTS/"
    else
        mv "$f" "$RECEIPTS/$base"
        echo "[CLEANUP] Moved: $base -> RECEIPTS/"
    fi
    count=$((count + 1))
done

echo "[CLEANUP] Processed $count files for $AGENT. Total receipts: $(ls "$RECEIPTS" 2>/dev/null | wc -l | tr -d ' ')"
