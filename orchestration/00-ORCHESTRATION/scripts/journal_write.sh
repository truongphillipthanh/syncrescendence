#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE}")/config.sh"

set -euo pipefail

# journal_write.sh — Manual journal entry for mid-session memories.
# Captures what git CANNOT: decisions, directives, failures, continuity signals.
#
# Usage:
#   journal_write.sh <kind> "text"
#   journal_write.sh <kind> "text" [--agent NAME] [--entities "E1,E2"] [--files "path1,path2"]
#
# Kinds:
#   decision           — A choice made and WHY
#   sovereign_directive — Direct order from Sovereign
#   failure            — What was attempted and failed
#   continuity         — Cross-session signal ("next session must...")
#   discovery          — Entity/relationship/pattern found
#   observation        — General note worth remembering
#
# Examples:
#   journal_write.sh decision "Chose inbox drain over tooling because Sovereign trust is zero"
#   journal_write.sh sovereign_directive "Proceed comprehensively with content metabolism"
#   journal_write.sh failure "Quality gate abandoned at 5.8% coverage"
#   journal_write.sh continuity "Next session must synthesize atoms into canon"
#   journal_write.sh discovery "memsync daemon reads from journal/ not memory/" --entities "memsync,journal"

VALID_KINDS="decision sovereign_directive failure continuity discovery observation"

# --- Args ---
if [ $# -lt 2 ]; then
  echo "Usage: journal_write.sh <kind> \"text\" [--agent NAME] [--entities \"E1,E2\"] [--files \"path1,path2\"]"
  echo "Kinds: ${VALID_KINDS}"
  exit 1
fi

KIND="$1"
TEXT="$2"
shift 2

# Validate kind
if ! echo "$VALID_KINDS" | grep -qw "$KIND"; then
  echo "ERROR: Invalid kind '$KIND'. Valid: ${VALID_KINDS}"
  exit 1
fi

# Optional args
AGENT="commander"
ENTITIES=""
FILES=""

while [ $# -gt 0 ]; do
  case "$1" in
    --agent)   AGENT="$2"; shift 2 ;;
    --entities) ENTITIES="$2"; shift 2 ;;
    --files)   FILES="$2"; shift 2 ;;
    *) echo "Unknown option: $1"; exit 1 ;;
  esac
done

# --- Paths ---
REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || echo "/Users/system/syncrescendence")"
ISO_TS="$(date -u '+%Y-%m-%dT%H:%M:%S.000Z')"
DATE_FILE="$(date -u '+%Y-%m-%d')"
SHA="$(git rev-parse --short HEAD 2>/dev/null || echo 'no-git')"

JOURNAL_DIR="${REPO_ROOT}/agents/${AGENT}/memory/journal"
JOURNAL_FILE="${JOURNAL_DIR}/${DATE_FILE}.jsonl"

mkdir -p "$JOURNAL_DIR"

# Sequence number
if [ -f "$JOURNAL_FILE" ]; then
  SEQ=$(printf '%04d' $(( $(wc -l < "$JOURNAL_FILE") + 1 )))
else
  SEQ="0001"
fi

# Escape for JSON
escape_json() {
  printf '%s' "$1" | sed 's/\\/\\\\/g; s/"/\\"/g; s/	/\\t/g' | tr '\n' ' '
}

# Build optional fields
EXTRAS=""
if [ -n "$ENTITIES" ]; then
  EXTRAS="${EXTRAS},\"entities\":\"$(escape_json "$ENTITIES")\""
fi
if [ -n "$FILES" ]; then
  EXTRAS="${EXTRAS},\"files\":\"$(escape_json "$FILES")\""
fi

# --- Write ---
cat >> "$JOURNAL_FILE" <<JSONL
{"uuid":"mem_${ISO_TS}_${AGENT}_${SEQ}","ts":"${ISO_TS}","agent":"${AGENT}","scope":"shared","kind":"${KIND}","source":"manual","text":"$(escape_json "$TEXT")","refs":{"git":"${SHA}"}${EXTRAS}}
JSONL

echo "Wrote ${KIND} entry to ${JOURNAL_FILE} (seq ${SEQ})"
