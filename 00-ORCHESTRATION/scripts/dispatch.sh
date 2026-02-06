#!/bin/bash
# dispatch.sh — Create a task dispatch file for any agent
# Usage: bash dispatch.sh <agent> "TOPIC" "TASK_DESCRIPTION" [CC]
#
# CC (optional): comma-separated list of additional inboxes to receive receipts
# Example: bash dispatch.sh ajna "FOO" "do bar" "psyche"
#
# Agents: commander, adjudicator, cartographer, psyche, ajna
# Writes a TASK file to -INBOX/<agent>/ for autonomous processing
#
# Examples:
#   bash dispatch.sh psyche "QA_REVIEW" "Review all files modified in last commit"
#   bash dispatch.sh cartographer "CORPUS_SURVEY" "Survey 01-CANON/ for orphaned refs"
#   bash dispatch.sh adjudicator "RUN_TESTS" "Execute make verify and report failures"

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
if [ -z "$REPO_ROOT" ]; then echo "Error: not in a git repo"; exit 1; fi

AGENT="${1:-psyche}"
TOPIC="${2:-TASK}"
DESCRIPTION="${3:-No description provided}"
CC_RAW="${4:-—}"

# Validate agent
VALID_AGENTS="commander adjudicator cartographer psyche ajna"
if ! echo "$VALID_AGENTS" | grep -qw "$AGENT"; then
    echo "Error: Unknown agent '$AGENT'. Valid: $VALID_AGENTS"
    exit 1
fi

INBOX_DIR="$REPO_ROOT/-INBOX/$AGENT"
if [ ! -d "$INBOX_DIR" ]; then
    mkdir -p "$INBOX_DIR"
fi

TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
DATE=$(date '+%Y%m%d')
FINGERPRINT=$(git rev-parse --short HEAD 2>/dev/null || echo "unknown")
TOPIC_SLUG=$(echo "$TOPIC" | tr '[:upper:]' '[:lower:]' | tr ' ' '_')
CALLER=$(basename "$0" .sh)

# Map agent to avatar name
case "$AGENT" in
    commander)    AVATAR="Commander (Claude Code Opus)" ;;
    adjudicator)  AVATAR="Adjudicator (Codex CLI)" ;;
    cartographer) AVATAR="Cartographer (Gemini CLI)" ;;
    psyche)       AVATAR="Psyche (OpenClaw GPT-5.2)" ;;
    ajna)         AVATAR="Ajna (OpenClaw Opus 4.5)" ;;
esac

TASK_FILE="$INBOX_DIR/TASK-${DATE}-${TOPIC_SLUG}.md"

cat > "$TASK_FILE" << EOF
# TASK-${DATE}-${TOPIC_SLUG}

**From**: ${CALLER}
**To**: ${AVATAR}
**Issued**: $TIMESTAMP
**Fingerprint**: $FINGERPRINT
**Priority**: P1
**Status**: PENDING
**Claimed-By**: —
**Claimed-At**: —
**Completed-At**: —
**Exit-Code**: —
**Timeout**: 30
**CC**: ${CC_RAW}

---

## Objective

$DESCRIPTION

---

## Context Files

Consult as needed:
- \`COCKPIT.md\` — Constellation overview
- \`CLAUDE.md\` — Constitutional rules
- \`00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md\` — Active intentions
- \`02-ENGINE/DEF-CONSTELLATION_VARIABLES.md\` — Global definitions

## Expected Output

- Write results to \`-OUTGOING/RESULT-${AGENT}-${DATE}-${TOPIC_SLUG}.md\`
- Or commit directly if you have write access

## Completion Protocol

1. Write output to the specified location
2. Update **Status** above from PENDING to COMPLETE
3. If cross-machine: \`git add -A && git commit -m "task: ${TOPIC_SLUG} complete" && git push\`
EOF

echo "[Dispatch] Created: $TASK_FILE"
echo "[Dispatch] Target: $AVATAR"
echo "[Dispatch] Topic: $TOPIC"
echo "[Dispatch] Agent watcher should pick this up autonomously."

# Append ledger: DISPATCH event
LEDGER_SCRIPT="$REPO_ROOT/00-ORCHESTRATION/scripts/append_ledger.sh"
if [ -x "$LEDGER_SCRIPT" ]; then
    bash "$LEDGER_SCRIPT" DISPATCH "$CALLER" "$AGENT" "TASK-${DATE}-${TOPIC_SLUG}.md" 2>/dev/null || true
fi
