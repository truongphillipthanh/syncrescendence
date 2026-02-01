#!/bin/bash
# dispatch_to_psyche.sh — Create a task dispatch file for Psyche
# Usage: bash dispatch_to_psyche.sh "TOPIC" "TASK_DESCRIPTION"
# Writes a DISPATCH file that Psyche's watcher picks up for autonomous processing

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
if [ -z "$REPO_ROOT" ]; then echo "Error: not in a git repo"; exit 1; fi

DISPATCH_DIR="$REPO_ROOT/00-ORCHESTRATION/state"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
DATE=$(date '+%Y%m%d')
FINGERPRINT=$(git rev-parse --short HEAD 2>/dev/null || echo "unknown")

TOPIC="${1:-TASK}"
DESCRIPTION="${2:-No description provided}"
TOPIC_SLUG=$(echo "$TOPIC" | tr '[:upper:]' '[:lower:]' | tr ' ' '_')

DISPATCH_FILE="$DISPATCH_DIR/DISPATCH-PSYCHE-${DATE}-${TOPIC_SLUG}.md"

cat > "$DISPATCH_FILE" << EOF
# DISPATCH: Psyche Task
**From**: Commander (Ajna)
**To**: Psyche
**Issued**: $TIMESTAMP
**Fingerprint**: $FINGERPRINT
**Status**: PENDING

---

## Task: $TOPIC

$DESCRIPTION

---

## Expected Output
- Write results to \`-OUTGOING/TWIN-PSYCHE-AJNA-${TOPIC_SLUG}.md\`
- Or commit directly if write access is available

## Context Files
Consult as needed:
- \`COCKPIT.md\` — Constellation overview
- \`00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md\` — Active intentions
- \`02-ENGINE/DEF-CONSTELLATION_VARIABLES.md\` — Global definitions

---

## Completion Protocol
1. Write output to specified location
2. Change Status line above from PENDING to COMPLETE
3. Notify Ajna via Slack or filesystem signal
EOF

echo "[Dispatch] Created: $DISPATCH_FILE"
echo "[Dispatch] Psyche watcher should pick this up autonomously."
echo "[Dispatch] Topic: $TOPIC"
