#!/usr/bin/env bash
# append_ledger.sh — Append an event to DYN-GLOBAL_LEDGER.md
# Usage: bash append_ledger.sh <EVENT> <FROM> <TO> <TASK_ID> [DECISION_ATOM] [INTENTION_LINK]
#
# Events: DISPATCH | CLAIM | COMPLETE | FAILED | DECISION
#
# Examples:
#   bash append_ledger.sh DISPATCH sovereign commander TASK-20260206-io_model.md
#   bash append_ledger.sh CLAIM commander commander TASK-20260206-io_model.md
#   bash append_ledger.sh COMPLETE commander sovereign TASK-20260206-io_model.md "" "INT-1202"
#   bash append_ledger.sh DECISION sovereign — SOVEREIGN-008 "DA-042" "INT-1209"

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
if [ -z "$REPO_ROOT" ]; then
    REPO_ROOT="$HOME/Desktop/syncrescendence"
fi

LEDGER="$REPO_ROOT/00-ORCHESTRATION/state/DYN-GLOBAL_LEDGER.md"

EVENT="${1:?Usage: append_ledger.sh EVENT FROM TO TASK_ID [DECISION_ATOM] [INTENTION_LINK]}"
FROM="${2:?Missing FROM}"
TO="${3:?Missing TO}"
TASK_ID="${4:?Missing TASK_ID}"
DECISION_ATOM="${5:-—}"
INTENTION_LINK="${6:-—}"

TIMESTAMP=$(date -u '+%Y-%m-%dT%H:%M:%S')
FINGERPRINT=$(git -C "$REPO_ROOT" rev-parse --short HEAD 2>/dev/null || echo "unknown")
COMMIT=$(git -C "$REPO_ROOT" rev-parse --short HEAD 2>/dev/null || echo "—")

# Validate event type
case "$EVENT" in
    DISPATCH|CLAIM|COMPLETE|FAILED|DECISION) ;;
    *) echo "[Ledger] Error: Invalid event '$EVENT'. Valid: DISPATCH|CLAIM|COMPLETE|FAILED|DECISION"; exit 1 ;;
esac

# Append to ledger (atomic: write to temp, then append)
ENTRY="| ${TIMESTAMP} | ${EVENT} | ${FROM} | ${TO} | ${TASK_ID} | ${FINGERPRINT} | ${COMMIT} | ${DECISION_ATOM} | ${INTENTION_LINK} |"

echo "$ENTRY" >> "$LEDGER"

echo "[Ledger] ${EVENT}: ${FROM} → ${TO} (${TASK_ID})"
