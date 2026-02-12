#!/bin/bash
# dispatch.sh — Create a task dispatch file for any agent
# Usage:
#   bash dispatch.sh <agent> "TOPIC" "TASK_DESCRIPTION" [CC] [KIND] [FROM]
#
# CC (optional): comma-separated list of additional inboxes to receive receipts (e.g. "psyche")
# KIND (optional): TASK|SURVEY|DIRECTIVE|EVIDENCE|RESULT|RECEIPT|PATCH|NOTE (default: TASK)
# FROM (optional): dispatching agent name for Reply-To routing (default: auto-detect)
#
# Example:
#   bash dispatch.sh ajna "FOO" "do bar" "psyche" TASK commander
#
# Agents: commander, adjudicator, cartographer, psyche, ajna
# Writes a TASK file to -INBOX/<agent>/ for autonomous processing
#
# BIDIRECTIONAL FEEDBACK: The dispatching agent is automatically added to CC
# and a Reply-To header routes the RESULT back to the sender's inbox.
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
KIND_RAW="${5:-TASK}"
FROM_RAW="${6:-${SYNCRESCENDENCE_AGENT:-}}"

# Auto-detect dispatching agent if not provided
if [ -z "$FROM_RAW" ]; then
  # Heuristic: if running inside Claude Code, assume commander
  if [ -n "${CLAUDE_CODE_SESSION:-}" ] || [ -n "${CLAUDE_SESSION_ID:-}" ]; then
    FROM_RAW="commander"
  else
    FROM_RAW="dispatch"
  fi
fi

# Auto-inject dispatching agent into CC for bidirectional feedback
# (only if FROM is a known agent AND not the same as the target)
if [ "$FROM_RAW" != "$AGENT" ] && [ "$FROM_RAW" != "dispatch" ]; then
  if echo "commander adjudicator cartographer psyche ajna" | grep -qw "$FROM_RAW"; then
    if [ "$CC_RAW" = "—" ] || [ -z "$CC_RAW" ]; then
      CC_RAW="$FROM_RAW"
    elif ! echo "$CC_RAW" | grep -qw "$FROM_RAW"; then
      CC_RAW="${CC_RAW},${FROM_RAW}"
    fi
  fi
fi

# Validate agent
VALID_AGENTS="commander adjudicator cartographer psyche ajna"
if ! echo "$VALID_AGENTS" | grep -qw "$AGENT"; then
    echo "Error: Unknown agent '$AGENT'. Valid: $VALID_AGENTS"
    exit 1
fi

INBOX0_DIR="$REPO_ROOT/-INBOX/$AGENT/00-INBOX0"
INPROG_DIR="$REPO_ROOT/-INBOX/$AGENT/10-IN_PROGRESS"
DONE_DIR="$REPO_ROOT/-INBOX/$AGENT/40-DONE"
FAILED_DIR="$REPO_ROOT/-INBOX/$AGENT/50_FAILED"
RECEIPTS_DIR="$REPO_ROOT/-INBOX/$AGENT/RECEIPTS"

# Ensure kanban dirs exist (do not rely on git tracking empty dirs)
mkdir -p "$INBOX0_DIR" "$INPROG_DIR" "$DONE_DIR" "$FAILED_DIR" "$RECEIPTS_DIR"

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
    psyche)       AVATAR="Psyche (OpenClaw GPT-5.3-codex)" ;;
    ajna)         AVATAR="Ajna (OpenClaw Opus 4.5)" ;;
esac

# Map FROM_RAW to avatar name for the From header
case "$FROM_RAW" in
    commander)    FROM_AVATAR="Commander (Claude Code Opus)" ;;
    adjudicator)  FROM_AVATAR="Adjudicator (Codex CLI)" ;;
    cartographer) FROM_AVATAR="Cartographer (Gemini CLI)" ;;
    psyche)       FROM_AVATAR="Psyche (OpenClaw GPT-5.3-codex)" ;;
    ajna)         FROM_AVATAR="Ajna (OpenClaw Opus 4.5)" ;;
    *)            FROM_AVATAR="$FROM_RAW" ;;
esac

TASK_FILE="$INBOX0_DIR/TASK-${DATE}-${TOPIC_SLUG}.md"
RECEIPTS_TO="-OUTBOX/${AGENT}/RESULTS"
RESULT_FILE="${RECEIPTS_TO}/RESULT-${AGENT}-${DATE}-${TOPIC_SLUG}.md"

cat > "$TASK_FILE" << EOF
# TASK-${DATE}-${TOPIC_SLUG}

**From**: ${FROM_AVATAR}
**To**: ${AVATAR}
**Reply-To**: ${FROM_RAW}
**Issued**: ${TIMESTAMP}
**Fingerprint**: ${FINGERPRINT}
**Kind**: ${KIND_RAW}
**Priority**: P1
**Status**: PENDING
**Kanban**: INBOX0
**Claimed-By**: —
**Claimed-At**: —
**Completed-At**: —
**Exit-Code**: —
**Timeout**: 30
**CC**: ${CC_RAW}
**Receipts-To**: ${RECEIPTS_TO}
**Escalation-Contact**: ${FROM_RAW}
**Escalation-Delay**: 10

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

- Write results to \`-OUTBOX/${AGENT}/RESULTS/RESULT-${AGENT}-${DATE}-${TOPIC_SLUG}.md\`
- Or commit directly if you have write access

## Completion Protocol

1. Write output to the specified location
2. Update **Status** above from PENDING to COMPLETE
3. If cross-machine: \`git add -A && git commit -m "task: ${TOPIC_SLUG} complete" && git push\`
EOF

echo "[Dispatch] Created: $TASK_FILE"
echo "[Dispatch] Kanban: INBOX0"
echo "[Dispatch] Kind: $KIND_RAW"
echo "[Dispatch] Target: $AVATAR"
echo "[Dispatch] Topic: $TOPIC"
echo "[Dispatch] Agent watcher should pick this up autonomously."

# Append ledger: DISPATCH event
LEDGER_SCRIPT="$REPO_ROOT/00-ORCHESTRATION/scripts/append_ledger.sh"
if [ -x "$LEDGER_SCRIPT" ]; then
    bash "$LEDGER_SCRIPT" DISPATCH "$CALLER" "$AGENT" "TASK-${DATE}-${TOPIC_SLUG}.md" 2>/dev/null || true
fi
