#!/usr/bin/env bash
# BLITZKRIEG FINALIZE SCRIPT
# Processes dropbox contents and generates execution artifacts
#
# Version: 1.0.0
# Created: 2026-01-18
# Authority: BLITZKRIEG_PROTOCOL
#
# Usage: ./blitzkrieg_finalize.sh
#
# Prerequisites:
#   - -INBOX/blitzkrieg_drop/context.md must exist
#   - At least one -INBOX/blitzkrieg_drop/directive-*.md must exist
#   - Each directive must have required headers

set -euo pipefail

# PORTABLE REPO ROOT (Constitutional Rule #11)
REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || {
    echo "ERROR: Not in a git repository"
    exit 1
}

cd "$REPO_ROOT"

# Configuration
DATE=$(date +%Y%m%d)
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
DROPBOX="$REPO_ROOT/-INBOX/blitzkrieg_drop"
BASE_OUTPUT="$REPO_ROOT/-OUTGOING/${DATE}-blitzkrieg"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Logging
log() { echo "[$( date '+%H:%M:%S' )] $1"; }
error() { echo -e "${RED}[$( date '+%H:%M:%S' )] ERROR: $1${NC}"; exit 1; }
warn() { echo -e "${YELLOW}[$( date '+%H:%M:%S' )] WARN: $1${NC}"; }
pass() { echo -e "${GREEN}[$( date '+%H:%M:%S' )] ✓ $1${NC}"; }

echo "=== BLITZKRIEG FINALIZE ==="
echo "Repo: $REPO_ROOT"
echo ""

# PRE-FLIGHT CHECK 1: No legacy OUTGOING/ or lowercase outgoing/
log "Checking exchange directory invariants..."
LEGACY_OUTGOING=$(ls -1 "$REPO_ROOT" 2>/dev/null | grep -E "^(OUTGOING|outgoing)$" || true)

if [ -n "$LEGACY_OUTGOING" ]; then
    error "VIOLATION: legacy '$LEGACY_OUTGOING/' exists. Canonical form is -OUTGOING/. Migrate first."
fi
pass "No legacy OUTGOING forms"

# PRE-FLIGHT CHECK 2: Ensure -OUTGOING/ and -INBOX/ exist
if [ ! -d "$REPO_ROOT/-OUTGOING" ]; then
    log "Creating -OUTGOING/..."
    mkdir -p "$REPO_ROOT/-OUTGOING"
fi

if [ ! -d "$REPO_ROOT/-INBOX" ]; then
    log "Creating -INBOX/..."
    mkdir -p "$REPO_ROOT/-INBOX"
fi
pass "-OUTGOING/ and -INBOX/ exist"

# PRE-FLIGHT CHECK 3: Dropbox exists
if [ ! -d "$DROPBOX" ]; then
    error "Dropbox not found: $DROPBOX
Create it and add:
  - context.md (session context)
  - directive-01.md (at least one directive with required headers)"
fi
pass "Dropbox exists"

# PRE-FLIGHT CHECK 4: context.md exists
if [ ! -f "$DROPBOX/context.md" ]; then
    error "context.md not found in dropbox.
Create $DROPBOX/context.md with session context before running blitzkrieg_finalize."
fi
pass "context.md found"

# PRE-FLIGHT CHECK 5: At least one directive exists
DIRECTIVE_COUNT=$(ls -1 "$DROPBOX"/directive-*.md 2>/dev/null | wc -l | tr -d ' ')
if [ "$DIRECTIVE_COUNT" -eq 0 ]; then
    error "No directive-*.md files found in dropbox.
Create at least one directive file (e.g., directive-01.md) with required headers:
  BLITZKRIEG_DIRECTIVE_ID:
  TARGET_MODEL:
  RATIONALE:
  SUCCESS_CRITERIA:"
fi
pass "Found $DIRECTIVE_COUNT directive(s)"

# PRE-FLIGHT CHECK 6: Validate directive headers
log "Validating directive headers..."
HEADER_ERRORS=""

for directive in "$DROPBOX"/directive-*.md; do
    filename=$(basename "$directive")

    # Check for required headers (allow YAML frontmatter or plain headers)
    for header in "BLITZKRIEG_DIRECTIVE_ID" "TARGET_MODEL" "RATIONALE" "SUCCESS_CRITERIA"; do
        if ! grep -q "^${header}:" "$directive" 2>/dev/null; then
            HEADER_ERRORS="${HEADER_ERRORS}\n  - $filename missing: $header"
        fi
    done

    # Validate TARGET_MODEL value
    TARGET=$(grep "^TARGET_MODEL:" "$directive" 2>/dev/null | sed 's/^TARGET_MODEL:[[:space:]]*//' | tr -d '\r' || true)
    if [ -n "$TARGET" ]; then
        case "$TARGET" in
            opus-4.5|sonnet-4.5|haiku) ;;
            *)
                HEADER_ERRORS="${HEADER_ERRORS}\n  - $filename invalid TARGET_MODEL: '$TARGET' (must be opus-4.5, sonnet-4.5, or haiku)"
                ;;
        esac
    fi
done

if [ -n "$HEADER_ERRORS" ]; then
    error "Directive header validation failed:$HEADER_ERRORS"
fi
pass "All directive headers valid"

# DETERMINE OUTPUT FOLDER (monotonic suffix if needed)
OUTPUT="$BASE_OUTPUT"
SUFFIX=2
while [ -d "$OUTPUT" ]; do
    OUTPUT="${BASE_OUTPUT}-$(printf '%02d' $SUFFIX)"
    ((SUFFIX++))
done

log "Output folder: $OUTPUT"

# CREATE OUTPUT STRUCTURE
mkdir -p "$OUTPUT/01_context"
mkdir -p "$OUTPUT/02_directives"
mkdir -p "$OUTPUT/03_execution"

# COPY CONTEXT
cp "$DROPBOX/context.md" "$OUTPUT/01_context/"
pass "Copied context.md"

# COPY DIRECTIVES
for directive in "$DROPBOX"/directive-*.md; do
    cp "$directive" "$OUTPUT/02_directives/"
done
pass "Copied $DIRECTIVE_COUNT directive(s)"

# EXTRACT DIRECTIVE METADATA
log "Extracting directive metadata..."
DIRECTIVE_TABLE=""
DIRECTIVE_JSON="["

FIRST=true
for directive in "$OUTPUT/02_directives"/directive-*.md; do
    filename=$(basename "$directive")

    # Extract headers
    DIRECTIVE_ID=$(grep "^BLITZKRIEG_DIRECTIVE_ID:" "$directive" | sed 's/^BLITZKRIEG_DIRECTIVE_ID:[[:space:]]*//' | tr -d '\r')
    TARGET_MODEL=$(grep "^TARGET_MODEL:" "$directive" | sed 's/^TARGET_MODEL:[[:space:]]*//' | tr -d '\r')
    RATIONALE=$(grep "^RATIONALE:" "$directive" | sed 's/^RATIONALE:[[:space:]]*//' | tr -d '\r')
    SUCCESS_CRITERIA=$(grep "^SUCCESS_CRITERIA:" "$directive" | sed 's/^SUCCESS_CRITERIA:[[:space:]]*//' | tr -d '\r')

    # Build table row
    DIRECTIVE_TABLE="${DIRECTIVE_TABLE}| $DIRECTIVE_ID | $TARGET_MODEL | $RATIONALE | pending |\n"

    # Build JSON entry
    if [ "$FIRST" = true ]; then
        FIRST=false
    else
        DIRECTIVE_JSON="${DIRECTIVE_JSON},"
    fi

    # Escape quotes for JSON
    RATIONALE_ESC=$(echo "$RATIONALE" | sed 's/"/\\"/g')
    SUCCESS_ESC=$(echo "$SUCCESS_CRITERIA" | sed 's/"/\\"/g')

    DIRECTIVE_JSON="${DIRECTIVE_JSON}
    {
      \"id\": \"$DIRECTIVE_ID\",
      \"filename\": \"$filename\",
      \"target_model\": \"$TARGET_MODEL\",
      \"rationale\": \"$RATIONALE_ESC\",
      \"success_criteria\": \"$SUCCESS_ESC\",
      \"status\": \"pending\"
    }"
done

DIRECTIVE_JSON="${DIRECTIVE_JSON}
  ]"

# GET GIT STATE
GIT_HEAD=$(git rev-parse HEAD 2>/dev/null || echo "unknown")
GIT_STATUS=$(git status --short 2>/dev/null || echo "unable to get status")
BLITZKRIEG_ID=$(basename "$OUTPUT")

# GENERATE EXECUTION LOG (MARKDOWN)
cat > "$OUTPUT/03_execution/execution_log.md" << LOGEOF
# Blitzkrieg Execution Log

**Generated**: $TIMESTAMP
**Git HEAD**: $GIT_HEAD
**Blitzkrieg ID**: $BLITZKRIEG_ID

## Repository State

\`\`\`
$GIT_STATUS
\`\`\`

## Directives Processed

| Directive | Target Model | Rationale | Status |
|-----------|--------------|-----------|--------|
$(echo -e "$DIRECTIVE_TABLE")

## What Changed

[To be filled during/after execution]

## What Remains

[To be filled during/after execution]

## Next Actions

[To be filled during/after execution]

## Attachments to Carry Forward

[To be filled during/after execution]

---

*This execution log is designed for "select all + copy" into ChatGPT or other platforms.*
LOGEOF

pass "Generated execution_log.md"

# GENERATE EXECUTION LOG (JSON)
cat > "$OUTPUT/03_execution/execution_log.json" << JSONEOF
{
  "type": "blitzkrieg_execution",
  "version": "1.0.0",
  "generated": "$TIMESTAMP",
  "git_head": "$GIT_HEAD",
  "blitzkrieg_id": "$BLITZKRIEG_ID",
  "directives": $DIRECTIVE_JSON,
  "summary": {
    "what_changed": "",
    "what_remains": "",
    "next_actions": [],
    "attachments": []
  }
}
JSONEOF

pass "Generated execution_log.json"

# SUMMARY
echo ""
echo "=== BLITZKRIEG FINALIZE COMPLETE ==="
echo ""
echo "Output: $OUTPUT/"
echo ""
echo "Contents:"
ls -la "$OUTPUT/"
echo ""
echo "Directives:"
ls -la "$OUTPUT/02_directives/"
echo ""
echo "Execution artifacts:"
ls -la "$OUTPUT/03_execution/"
echo ""
echo "=== NEXT STEPS ==="
echo "1. Execute directives using specified models"
echo "2. Update execution_log.md with results"
echo "3. Commit changes with blitzkrieg reference"
echo "4. Optionally run /deviser_reint for full session export"
