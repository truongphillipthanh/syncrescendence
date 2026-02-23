#!/usr/bin/env bash
# append_ledger.sh — Append an event to DYN-GLOBAL_LEDGER.md
# Usage: bash append_ledger.sh <EVENT> <FROM> <TO> <TASK_ID> [DECISION_ATOM] [INTENTION_LINK]
#
# Events: DISPATCH | CLAIM | COMPLETE | FAILED | BLOCKED | ESCALATION | COMMIT | DECISION | COMPACT | REGEN | ACKNOWLEDGE
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

LEDGER="$REPO_ROOT/orchestration/state/DYN-GLOBAL_LEDGER.md"

EVENT="${1:?Usage: append_ledger.sh EVENT FROM TO TASK_ID [DECISION_ATOM] [INTENTION_LINK]}"
FROM="${2:?Missing FROM}"
TO="${3:?Missing TO}"
TASK_ID="${4:?Missing TASK_ID}"
DECISION_ATOM="${5:-—}"
INTENTION_LINK="${6:-—}"

TIMESTAMP=$(date -u '+%Y-%m-%dT%H:%M:%S')
FINGERPRINT=$(git -C "$REPO_ROOT" rev-parse --short HEAD 2>/dev/null || echo "unknown")
COMMIT=$(git -C "$REPO_ROOT" rev-parse --short HEAD 2>/dev/null || echo "—")

# Ensure ledger exists with header
if [ ! -f "$LEDGER" ]; then
    mkdir -p "$(dirname "$LEDGER")"
    cat > "$LEDGER" << 'HEADER'
# DYN-GLOBAL_LEDGER.md
## Append-Only Event Log for Task Lifecycle + Sovereign Decisions

**Created**: 2026-02-06
**Protocol**: Append only. Never edit existing entries. One entry per event.
**Script**: `orchestration/scripts/append_ledger.sh`

---

## Schema

```
| Timestamp | Event | From | To | Task ID | Fingerprint | Commit | DecisionAtom | IntentionLink |
```

- **Timestamp**: ISO 8601 (YYYY-MM-DDTHH:MM:SS)
- **Event**: DISPATCH | CLAIM | COMPLETE | FAILED | DECISION | COMPACT | REGEN
- **From**: Originating agent or Sovereign
- **To**: Target agent or platform
- **Task ID**: TASK filename (without path)
- **Fingerprint**: Git short hash at event time
- **Commit**: Commit hash if event produced a commit (else `—`)
- **DecisionAtom**: Reference to REF-DECISION_ATOMS.md entry (if applicable)
- **IntentionLink**: Reference to ARCH-INTENTION_COMPASS.md entry (if applicable)

---

## Ledger

| Timestamp | Event | From | To | Task ID | Fingerprint | Commit | DecisionAtom | IntentionLink |
|-----------|-------|------|----|---------|-------------|--------|--------------|---------------|
HEADER
fi

# Validate event type
case "$EVENT" in
    DISPATCH|CLAIM|COMPLETE|FAILED|BLOCKED|ESCALATION|COMMIT|DECISION|COMPACT|REGEN|ACKNOWLEDGE) ;;
    *) echo "[Ledger] Error: Invalid event '$EVENT'. Valid: DISPATCH|CLAIM|COMPLETE|FAILED|BLOCKED|ESCALATION|COMMIT|DECISION|COMPACT|REGEN|ACKNOWLEDGE"; exit 1 ;;
esac

# Atomic-ish append with a simple lock (portable; avoids flock dependency)
LOCK_DIR="/tmp/syncrescendence-ledger.lock"
LOCK_WAIT_SEC=5
START_TS=$(date +%s)

while ! mkdir "$LOCK_DIR" 2>/dev/null; do
    if [ $(( $(date +%s) - START_TS )) -ge "$LOCK_WAIT_SEC" ]; then
        echo "[Ledger] Error: could not acquire lock: $LOCK_DIR"
        exit 2
    fi
    sleep 0.1
done

cleanup() { rmdir "$LOCK_DIR" 2>/dev/null || true; }
trap cleanup EXIT

ENTRY="| ${TIMESTAMP} | ${EVENT} | ${FROM} | ${TO} | ${TASK_ID} | ${FINGERPRINT} | ${COMMIT} | ${DECISION_ATOM} | ${INTENTION_LINK} |"

# Write entry to temp then append
TMP_FILE="/tmp/syncrescendence-ledger-entry.$$.$RANDOM"
printf "%s\n" "$ENTRY" > "$TMP_FILE"
cat "$TMP_FILE" >> "$LEDGER"
rm -f "$TMP_FILE"

echo "[Ledger] ${EVENT}: ${FROM} → ${TO} (${TASK_ID})"
