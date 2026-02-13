#!/bin/bash
# Intent Compass hook — fires on UserPromptSubmit
# Scans user input for intention-laden language and captures to queue file
# Lightweight: must complete fast since it runs on every prompt

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
if [ -z "$REPO_ROOT" ]; then exit 0; fi

# Preflight: jq required for JSON parsing
if ! command -v jq &>/dev/null; then
    exit 0  # Silent exit — hook must not block prompts
fi

# Read stdin JSON
INPUT=$(cat)
PROMPT=$(echo "$INPUT" | jq -r '.prompt // empty' 2>/dev/null)
if [ -z "$PROMPT" ]; then exit 0; fi

QUEUE_FILE="$REPO_ROOT/00-ORCHESTRATION/state/DYN-INTENTIONS_QUEUE.md"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Intention signal patterns (case-insensitive grep)
SIGNALS="I want|we should|we need|don't forget|make sure|priority|must have|let's|going forward|from now on|always|never again|remember to|important that|critical that|we'll need|tall order|massive|manhattan|codify|formalize|operationalize"

# Check for intention signals
MATCH=$(echo "$PROMPT" | grep -iE "$SIGNALS" 2>/dev/null)
if [ -z "$MATCH" ]; then exit 0; fi

# Create queue file with header if it doesn't exist
if [ ! -f "$QUEUE_FILE" ]; then
    cat > "$QUEUE_FILE" << 'HEADER'
# Intentions Queue
**Auto-captured by intent_compass.sh hook**
**Triage into ARCH-INTENTION_COMPASS.md during session checkpoints**

---
HEADER
fi

# Extract first matching line (truncate to 200 chars for brevity)
CAPTURED=$(echo "$MATCH" | head -1 | cut -c1-200)

# Append captured intention
cat >> "$QUEUE_FILE" << EOF

- **$TIMESTAMP** | \`$CAPTURED\`
EOF

# Inject subtle context reminder (non-blocking)
echo "{\"hookSpecificOutput\": {\"hookEventName\": \"UserPromptSubmit\", \"additionalContext\": \"[Intent Compass] Intention signal detected and queued for triage.\"}}"
exit 0
