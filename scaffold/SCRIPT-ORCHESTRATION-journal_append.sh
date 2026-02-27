#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE}")/config.sh"

set -euo pipefail

# journal_append.sh — Session-stop hook that captures what git CANNOT:
# files changed, handoffs created, deferred commitment state, session summary.
# Fires automatically at session end via Claude Code stop hook.

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || echo "/Users/system/syncrescendence")"
ISO_TS="$(date -u '+%Y-%m-%dT%H:%M:%S.000Z')"
DATE_FILE="$(date -u '+%Y-%m-%d')"
SHA="$(git rev-parse --short HEAD 2>/dev/null || echo 'no-git')"

JOURNAL_DIR="${REPO_ROOT}/agents/commander/memory/journal"
JOURNAL_FILE="${JOURNAL_DIR}/${DATE_FILE}.jsonl"

mkdir -p "$JOURNAL_DIR"

# Dedup guard: skip if HEAD sha already recorded today as session_end
if [ -f "$JOURNAL_FILE" ] && grep -q "\"session_end\".*\"git\":\"${SHA}\"" "$JOURNAL_FILE" 2>/dev/null; then
  exit 0
fi

# Sequence number
if [ -f "$JOURNAL_FILE" ]; then
  SEQ=$(printf '%04d' $(( $(wc -l < "$JOURNAL_FILE") + 1 )))
else
  SEQ="0001"
fi

# --- Gather signals git doesn't capture ---

# 1. Files changed (staged + unstaged, just names)
FILES_CHANGED="$(git diff --name-only HEAD~1 HEAD 2>/dev/null | head -20 | tr '\n' ',' | sed 's/,$//')"
FILES_CHANGED="${FILES_CHANGED:-none}"
FILE_COUNT="$(git diff --name-only HEAD~1 HEAD 2>/dev/null | wc -l | tr -d ' ')"

# 2. Uncommitted work still in tree
DIRTY_COUNT="$(git status --porcelain 2>/dev/null | wc -l | tr -d ' ')"

# 3. Handoff files created this session (modified today)
HANDOFFS="$(find "${REPO_ROOT}/agents" -name 'HANDOFF-*' -newer "${REPO_ROOT}/.git/HEAD" 2>/dev/null | head -5 | tr '\n' ',' | sed 's/,$//')"
HANDOFFS="${HANDOFFS:-none}"

# 4. Deferred commitments summary
DC_FILE="${REPO_ROOT}/orchestration/state/DYN-DEFERRED_COMMITMENTS.md"
if [ -f "$DC_FILE" ]; then
  DC_OPEN="$(grep -c 'OPEN' "$DC_FILE" 2>/dev/null || echo 0)"
  DC_DONE="$(grep -c 'DONE\|CLOSED\|COMPLETE' "$DC_FILE" 2>/dev/null || echo 0)"
  DC_SUMMARY="open=${DC_OPEN},done=${DC_DONE}"
else
  DC_SUMMARY="no-file"
fi

# 5. Commits this session (rough: commits in last 2 hours by any author)
SESSION_COMMITS="$(git log --oneline --since='2 hours ago' 2>/dev/null | wc -l | tr -d ' ')"

# 6. Last commit message (the "what")
LAST_MSG="$(git log --oneline -1 2>/dev/null | sed 's/"/\\"/g')"

# 7. Inbox state
PENDING="$(find "${REPO_ROOT}/agents/commander/inbox/pending" -name 'TASK-*' 2>/dev/null | wc -l | tr -d ' ')"
ACTIVE="$(find "${REPO_ROOT}/agents/commander/inbox/active" -name 'TASK-*' 2>/dev/null | wc -l | tr -d ' ')"

# 8. Any manual journal entries this session (to link them)
MANUAL_ENTRIES="$(grep -c '"source":"manual"' "$JOURNAL_FILE" 2>/dev/null || echo 0)"

# --- Escape helper ---
escape_json() {
  printf '%s' "$1" | sed 's/\\/\\\\/g; s/"/\\"/g; s/	/\\t/g' | tr '\n' ' '
}

# --- Write the entry ---
cat >> "$JOURNAL_FILE" <<JSONL
{"uuid":"mem_${ISO_TS}_commander_${SEQ}","ts":"${ISO_TS}","agent":"commander","scope":"shared","kind":"session_end","source":"hook","text":"$(escape_json "$LAST_MSG")","session":{"commits":${SESSION_COMMITS},"files_changed":${FILE_COUNT},"dirty_files":${DIRTY_COUNT},"pending_tasks":${PENDING},"active_tasks":${ACTIVE},"manual_entries":${MANUAL_ENTRIES},"deferred":"${DC_SUMMARY}"},"refs":{"git":"${SHA}","files":"$(escape_json "$FILES_CHANGED")","handoffs":"$(escape_json "$HANDOFFS")"}}
JSONL
