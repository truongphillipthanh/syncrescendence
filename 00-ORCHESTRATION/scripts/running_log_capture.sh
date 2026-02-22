#!/usr/bin/env bash
# running_log_capture.sh — Auto-capture conversation transcript to running logs
# Fires on: Stop hook, PreCompact hook
# Purpose: Hedge against context loss during autocompaction
#
# Extracts user prompts and assistant responses from the current session JSONL
# and appends them to the appropriate running log file.

set -euo pipefail

LOG_DIR="/Users/system/Desktop/-surface/running_logs"
mkdir -p "$LOG_DIR"

# Determine agent identity from env or fallback
AGENT_NAME="${SYNCRESCENDENCE_AGENT_NAME:-mba-commander}"
LOG_FILE="$LOG_DIR/${AGENT_NAME}-log.md"
REQUEST_FILE="$LOG_DIR/${AGENT_NAME}-request.md"

# Find the most recent JSONL for this project directory
PROJECT_HASH=$(echo -n "$PWD" | sed 's|/|-|g')
SESSION_DIR="$HOME/.claude/projects/$PROJECT_HASH"

if [ ! -d "$SESSION_DIR" ]; then
    # Try the home directory project
    SESSION_DIR="$HOME/.claude/projects/-Users-system"
fi

if [ ! -d "$SESSION_DIR" ]; then
    echo "[running_log_capture] No session dir found at $SESSION_DIR" >&2
    exit 0
fi

# Get the most recently modified JSONL (current session)
JSONL=$(ls -t "$SESSION_DIR"/*.jsonl 2>/dev/null | head -1)

if [ -z "$JSONL" ] || [ ! -f "$JSONL" ]; then
    echo "[running_log_capture] No JSONL found in $SESSION_DIR" >&2
    exit 0
fi

SESSION_ID=$(basename "$JSONL" .jsonl)
MARKER_FILE="$LOG_DIR/.last_capture_${AGENT_NAME}_${SESSION_ID}"
LAST_LINE=0

if [ -f "$MARKER_FILE" ]; then
    LAST_LINE=$(cat "$MARKER_FILE")
fi

# Extract new user and assistant messages since last capture
# Uses python for reliable JSONL parsing
python3 << 'PYEOF' - "$JSONL" "$LAST_LINE" "$LOG_FILE" "$REQUEST_FILE" "$MARKER_FILE"
import json, sys, os
from datetime import datetime

jsonl_path = sys.argv[1]
last_line = int(sys.argv[2])
log_file = sys.argv[3]
request_file = sys.argv[4]
marker_file = sys.argv[5]

new_assistant = []
new_user = []
line_count = 0

with open(jsonl_path) as f:
    for i, line in enumerate(f):
        line_count = i + 1
        if i < last_line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            continue

        msg_type = msg.get("type", "")

        if msg_type == "assistant":
            # Extract text content from assistant message
            content = msg.get("message", {}).get("content", [])
            texts = []
            for block in content:
                if isinstance(block, dict) and block.get("type") == "text":
                    texts.append(block.get("text", ""))
                elif isinstance(block, str):
                    texts.append(block)
            if texts:
                new_assistant.append("\n".join(texts))

        elif msg_type == "user":
            # Extract text content from user message
            content = msg.get("message", {}).get("content", "")
            if isinstance(content, str) and content.strip():
                new_user.append(content)
            elif isinstance(content, list):
                texts = []
                for block in content:
                    if isinstance(block, dict) and block.get("type") == "text":
                        texts.append(block.get("text", ""))
                    elif isinstance(block, str):
                        texts.append(block)
                if texts:
                    new_user.append("\n".join(texts))

# Append to log files if there's new content
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

if new_assistant:
    with open(log_file, "a") as f:
        for text in new_assistant:
            # Truncate very long tool outputs but keep substance
            if len(text) > 5000:
                text = text[:4500] + "\n[...truncated...]\n" + text[-500:]
            f.write(text + "\n\n***\n\n")

if new_user:
    with open(request_file, "a") as f:
        for text in new_user:
            f.write(text + "\n\n***\n\n")

# Update marker
with open(marker_file, "w") as f:
    f.write(str(line_count))

captured = len(new_assistant) + len(new_user)
if captured > 0:
    print(f"[running_log_capture] Captured {len(new_assistant)} assistant + {len(new_user)} user messages")
PYEOF
