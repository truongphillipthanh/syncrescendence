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
# Writes a TASK file to agents/<agent>/inbox/pending for autonomous processing
#
# BIDIRECTIONAL FEEDBACK: The dispatching agent is automatically added to CC
# and a Reply-To header routes the RESULT back to the sender's inbox.
#
# Examples:
#   bash dispatch.sh psyche "QA_REVIEW" "Review all files modified in last commit"
#   bash dispatch.sh cartographer "CORPUS_SURVEY" "Survey canon/ for orphaned refs"
#   bash dispatch.sh adjudicator "RUN_TESTS" "Execute make verify and report failures"

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
if [ -z "$REPO_ROOT" ]; then echo "Error: not in a git repo"; exit 1; fi
INTEGRITY_GATE="${REPO_ROOT}/orchestration/scripts/repo_integrity_gate.sh"
BREAKER_FILE="${REPO_ROOT}/orchestration/state/breakers/orchestration.breaker"

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

# Guardrails: fail-closed when integrity is unsafe or breaker is OPEN.
if [ -x "$INTEGRITY_GATE" ]; then
    if ! bash "$INTEGRITY_GATE" --repo "$REPO_ROOT" --context dispatch --quiet; then
        echo "Error: integrity gate failed; dispatch aborted"
        exit 1
    fi
fi
if [ -f "$BREAKER_FILE" ]; then
    BREAKER_STATE=$(grep '^state=' "$BREAKER_FILE" 2>/dev/null | head -1 | cut -d'=' -f2)
    if [ "$BREAKER_STATE" = "OPEN" ]; then
        echo "Error: circuit breaker OPEN; dispatch aborted"
        exit 1
    fi
fi

INBOX0_DIR="$REPO_ROOT/agents/$AGENT/inbox/pending"
INPROG_DIR="$REPO_ROOT/agents/$AGENT/inbox/active"
DONE_DIR="$REPO_ROOT/agents/$AGENT/inbox/done"
FAILED_DIR="$REPO_ROOT/agents/$AGENT/inbox/failed"
RECEIPTS_DIR="$REPO_ROOT/agents/$AGENT/outbox"

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
RECEIPTS_TO="agents/${AGENT}/outbox"
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
- \`README.md\` — Constellation overview
- \`CLAUDE.md\` — Constitutional rules
- \`orchestration/state/ARCH-INTENTION_COMPASS.md\` — Active intentions
- \`engine/DEF-CONSTELLATION_VARIABLES.md\` — Global definitions

## Expected Output

- Write results to \`agents/${AGENT}/outbox/RESULT-${AGENT}-${DATE}-${TOPIC_SLUG}.md\`
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

# Best-effort cross-machine dispatch: if the target agent is on another host,
# sling the same task file directly to its remote INBOX0 over SSH/SCP.
AGENT_UPPER=$(echo "$AGENT" | tr '[:lower:]' '[:upper:]')
REMOTE_HOST_VAR="SYNCRESCENDENCE_REMOTE_AGENT_HOST_${AGENT_UPPER}"
REMOTE_HOST="${!REMOTE_HOST_VAR:-$AGENT}"
if [ -n "$REMOTE_HOST" ] && [ "$REMOTE_HOST" != "local" ] && [ "$REMOTE_HOST" != "localhost" ]; then
    if ssh -o BatchMode=yes -o ConnectTimeout=3 "$REMOTE_HOST" "test -d ~/Desktop/syncrescendence/agents/$AGENT/inbox/pending" 2>/dev/null; then
        scp -q -o BatchMode=yes -o ConnectTimeout=5 "$TASK_FILE" \
            "$REMOTE_HOST:~/Desktop/syncrescendence/agents/$AGENT/inbox/pending/" 2>/dev/null || true
        echo "[Dispatch] Remote sling: copied task to $REMOTE_HOST:agents/$AGENT/inbox/pending/"
    fi
fi

# Append ledger: DISPATCH event
LEDGER_SCRIPT="$REPO_ROOT/orchestration/scripts/append_ledger.sh"
if [ -x "$LEDGER_SCRIPT" ]; then
    bash "$LEDGER_SCRIPT" DISPATCH "$CALLER" "$AGENT" "TASK-${DATE}-${TOPIC_SLUG}.md" 2>/dev/null || true
fi
