#!/bin/bash
# Generic Claude Code headless task runner for launchd
# Usage: run_claude_task.sh <task-name> <prompt-file-or-string>
set -euo pipefail

export HOME=/Users/home
export PATH="/Users/home/.nvm/versions/node/v24.13.0/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"

TASK_NAME="${1:-unnamed}"
PROMPT_SOURCE="${2:-}"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
LOG_DIR="/tmp/syncrescendence-claude"
LOG_FILE="${LOG_DIR}/${TASK_NAME}-${TIMESTAMP}.log"
REPO="/Users/home/Desktop/syncrescendence"

mkdir -p "$LOG_DIR"

# Source env vars (API keys)
if [ -f "$HOME/.syncrescendence/.env" ]; then
  set -a
  source "$HOME/.syncrescendence/.env"
  set +a
fi

# Resolve prompt: if it's a file path, read it; otherwise treat as literal prompt
if [ -f "$PROMPT_SOURCE" ]; then
  PROMPT=$(cat "$PROMPT_SOURCE")
else
  PROMPT="$PROMPT_SOURCE"
fi

if [ -z "$PROMPT" ]; then
  echo "ERROR: No prompt provided" | tee "$LOG_FILE"
  exit 1
fi

echo "=== Claude Task: $TASK_NAME ===" | tee "$LOG_FILE"
echo "Started: $(date)" | tee -a "$LOG_FILE"
echo "---" >> "$LOG_FILE"

# Run Claude non-interactively
claude -p "$PROMPT" \
  --allowedTools "Bash(curl *),Bash(jq *),Bash(date *),Bash(grep *),Bash(cd *),Bash(find *),Bash(cat *),Bash(head *),Bash(tail *),Bash(wc *),Read,Write,Glob,Grep" \
  --output-format text \
  --add-dir "$REPO" \
  --max-budget-usd 0.50 \
  >> "$LOG_FILE" 2>&1 || {
    echo "ERROR: Claude exited with code $?" | tee -a "$LOG_FILE"
  }

echo "---" >> "$LOG_FILE"
echo "Completed: $(date)" >> "$LOG_FILE"

# Rotate: keep last 20 logs per task
ls -t "${LOG_DIR}/${TASK_NAME}"-*.log 2>/dev/null | tail -n +21 | xargs rm -f 2>/dev/null || true

echo "Log: $LOG_FILE"
