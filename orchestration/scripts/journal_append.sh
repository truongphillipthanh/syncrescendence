#!/bin/bash
# journal_append.sh — Append a JSONL memory record to an agent's journal.
#
# Usage:
#   journal_append.sh <agent> <scope> <kind> <text> [git_sha]
#
# Example:
#   journal_append.sh commander shared observation "Docker PATH fixed on Mac mini"
#
# scope: shared | private
# kind: decision | preference | observation | task | fact | conflict

set -euo pipefail

AGENT="${1:?Usage: journal_append.sh <agent> <scope> <kind> <text> [git_sha]}"
SCOPE="${2:?Missing scope (shared|private)}"
KIND="${3:?Missing kind (decision|preference|observation|task|fact|conflict)}"
TEXT="${4:?Missing text}"
GIT_SHA="${5:-$(git rev-parse --short HEAD 2>/dev/null || echo 'unknown')}"

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
JOURNAL_DIR="$REPO_ROOT/agents/$AGENT/memory/journal"
mkdir -p "$JOURNAL_DIR"
TODAY="$(date -u +%Y-%m-%d)"
JOURNAL_FILE="$JOURNAL_DIR/$TODAY.jsonl"
TS="$(date -u +%Y-%m-%dT%H:%M:%S.000Z)"
if [ -f "$JOURNAL_FILE" ]; then
  SEQ="$(wc -l < "$JOURNAL_FILE" | tr -d ' ')"
else
  SEQ=0
fi
SEQ=$((SEQ + 1))
UUID="mem_${TS}_${AGENT}_$(printf '%04d' $SEQ)"

RECORD=$(python3 -c "
import json, sys
print(json.dumps({
    'uuid': sys.argv[1],
    'ts': sys.argv[2],
    'agent': sys.argv[3],
    'scope': sys.argv[4],
    'kind': sys.argv[5],
    'text': sys.argv[6],
    'refs': {'git': sys.argv[7], 'path': sys.argv[8]}
}, ensure_ascii=False))
" "$UUID" "$TS" "$AGENT" "$SCOPE" "$KIND" "$TEXT" "$GIT_SHA" "agents/$AGENT/memory/journal/$TODAY.jsonl")

mkdir -p "$JOURNAL_DIR"
echo "$RECORD" >> "$JOURNAL_FILE"
echo "$UUID"
