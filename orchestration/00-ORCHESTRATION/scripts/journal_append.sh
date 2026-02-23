#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
ISO_TS="$(date -u '+%Y-%m-%dT%H:%M:%S.000Z')"
DATE_FILE="$(date -u '+%Y-%m-%d')"
SHA="$(git rev-parse --short HEAD)"

JOURNAL_DIR="${REPO_ROOT}/agents/commander/memory/journal"
JOURNAL_FILE="${JOURNAL_DIR}/${DATE_FILE}.jsonl"

mkdir -p "$JOURNAL_DIR"

# Dedup guard: skip if HEAD sha already recorded today
if [ -f "$JOURNAL_FILE" ] && grep -q "\"git\":\"${SHA}\"" "$JOURNAL_FILE"; then
  exit 0
fi

# Sequence number: existing lines + 1, zero-padded to 4
if [ -f "$JOURNAL_FILE" ]; then
  SEQ=$(printf '%04d' $(( $(wc -l < "$JOURNAL_FILE") + 1 )))
else
  SEQ="0001"
fi

# Last commit message, escape double quotes
TEXT="$(git log --oneline -1 | sed 's/"/\\"/g')"

printf '{"uuid":"mem_%s_commander_%s","ts":"%s","agent":"commander","scope":"shared","kind":"observation","text":"%s","refs":{"git":"%s","path":"agents/commander/memory/journal/%s.jsonl"}}\n' \
  "$ISO_TS" "$SEQ" "$ISO_TS" "$TEXT" "$SHA" "$DATE_FILE" \
  >> "$JOURNAL_FILE"
