---
name: blitzkrieg_finalize
description: Finalize blitzkrieg bundle with return packet, audio scripts, and agent relay JSON
allowed-tools: Bash, Read, Write, Glob
---
# Blitzkrieg Finalize (vNext)

Finalize a blitzkrieg bundle by generating:
- `merged_return_packet.md` (pasteable back to Vanguard)
- Audized scripts (TTS-optimized, no markdown)
- Agent relay JSON (structured LLM-to-LLM format)

## Prerequisites

Before running this command, ensure:
1. A blitzkrieg bundle exists at `-OUTGOING/YYYYMMDD-blitzkrieg-<slug>/`
2. `01_context/context.md` is filled in
3. `02_pedigree/pedigree.md` is filled in
4. At least one `04_directives/directive-*.md` exists with required headers
5. Lane execution logs in `05_execution/` are updated

## Execution

### Step 1: Find Latest Bundle

```bash
# Find most recent blitzkrieg bundle
BUNDLE=$(ls -dt ./-OUTGOING/*-blitzkrieg-* 2>/dev/null | head -1)

if [ -z "$BUNDLE" ]; then
    echo "ERROR: No blitzkrieg bundle found in -OUTGOING/"
    echo "Run /project:blitzkrieg_issue <slug> first."
    exit 1
fi

echo "Found bundle: $BUNDLE"
```

### Step 2: Validate Required Files

```bash
BUNDLE=$(ls -dt ./-OUTGOING/*-blitzkrieg-* 2>/dev/null | head -1)

# Check context
if [ ! -f "$BUNDLE/01_context/context.md" ] || [ ! -s "$BUNDLE/01_context/context.md" ]; then
    echo "ERROR: $BUNDLE/01_context/context.md not found or empty."
    echo "Fill in the context template before finalizing."
    exit 1
fi

# Check pedigree
if [ ! -f "$BUNDLE/02_pedigree/pedigree.md" ] || [ ! -s "$BUNDLE/02_pedigree/pedigree.md" ]; then
    echo "ERROR: $BUNDLE/02_pedigree/pedigree.md not found or empty."
    echo "Fill in the pedigree template before finalizing."
    exit 1
fi

# Check directives
DIRECTIVE_COUNT=$(ls -1 "$BUNDLE/04_directives"/directive-*.md 2>/dev/null | wc -l | tr -d ' ')
if [ "$DIRECTIVE_COUNT" -eq 0 ]; then
    echo "ERROR: No directive-*.md files found in $BUNDLE/04_directives/"
    exit 1
fi

echo "Validation passed: context, pedigree, and $DIRECTIVE_COUNT directive(s) found"
```

### Step 3: Extract Directive Metadata

```bash
BUNDLE=$(ls -dt ./-OUTGOING/*-blitzkrieg-* 2>/dev/null | head -1)
BLITZKRIEG_ID=$(basename "$BUNDLE")
DATE=$(echo "$BLITZKRIEG_ID" | cut -d'-' -f1)
SLUG=$(echo "$BLITZKRIEG_ID" | sed 's/^[0-9]*-blitzkrieg-//')
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
GIT_HEAD=$(git rev-parse HEAD 2>/dev/null || echo "unknown")

# Extract lane info
LANE_SUMMARY=""
LANE_JSON=""

for directive in "$BUNDLE/04_directives"/directive-*.md; do
    [ -f "$directive" ] || continue

    LANE=$(grep "^Lane:" "$directive" 2>/dev/null | sed 's/^Lane:[[:space:]]*//' | tr -d '\r' || echo "?")
    TOOLCHAIN=$(grep "^Toolchain:" "$directive" 2>/dev/null | sed 's/^Toolchain:[[:space:]]*//' | tr -d '\r' || echo "unknown")
    MODEL=$(grep "^Model:" "$directive" 2>/dev/null | sed 's/^Model:[[:space:]]*//' | tr -d '\r' || echo "unknown")
    THINKING=$(grep "^Thinking:" "$directive" 2>/dev/null | sed 's/^Thinking:[[:space:]]*//' | tr -d '\r' || echo "default")
    SUCCESS=$(grep "^Success_Criteria:" "$directive" 2>/dev/null | sed 's/^Success_Criteria:[[:space:]]*//' | tr -d '\r' || echo "")

    # Check execution log status
    EXEC_LOG="$BUNDLE/05_execution/lane-${LANE}/execution_log.md"
    if [ -f "$EXEC_LOG" ]; then
        STATUS=$(grep "^\*\*Status\*\*:" "$EXEC_LOG" 2>/dev/null | sed 's/.*:[[:space:]]*//' | tr -d '\r' || echo "unknown")
    else
        STATUS="NOT_STARTED"
    fi

    LANE_SUMMARY="${LANE_SUMMARY}Lane $LANE ($TOOLCHAIN/$MODEL): $STATUS\n"
done

echo "Extracted lane metadata"
```

### Step 4: Generate Merged Return Packet

```bash
BUNDLE=$(ls -dt ./-OUTGOING/*-blitzkrieg-* 2>/dev/null | head -1)
BLITZKRIEG_ID=$(basename "$BUNDLE")
DATE_PART=$(echo "$BLITZKRIEG_ID" | cut -d'-' -f1)
SLUG=$(echo "$BLITZKRIEG_ID" | sed 's/^[0-9]*-blitzkrieg-//')
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
GIT_HEAD=$(git rev-parse HEAD 2>/dev/null || echo "unknown")

# Build lane summaries
LANES_EXECUTED=""
for directive in "$BUNDLE/04_directives"/directive-*.md; do
    [ -f "$directive" ] || continue

    LANE=$(grep "^Lane:" "$directive" 2>/dev/null | sed 's/^Lane:[[:space:]]*//' | tr -d '\r' || echo "?")
    TOOLCHAIN=$(grep "^Toolchain:" "$directive" 2>/dev/null | sed 's/^Toolchain:[[:space:]]*//' | tr -d '\r' || echo "unknown")
    MODEL=$(grep "^Model:" "$directive" 2>/dev/null | sed 's/^Model:[[:space:]]*//' | tr -d '\r' || echo "unknown")

    EXEC_LOG="$BUNDLE/05_execution/lane-${LANE}/execution_log.md"
    if [ -f "$EXEC_LOG" ]; then
        STATUS=$(grep "^\*\*Status\*\*:" "$EXEC_LOG" 2>/dev/null | sed 's/.*:[[:space:]]*//' | tr -d '\r' || echo "unknown")
    else
        STATUS="NOT_STARTED"
    fi

    LANES_EXECUTED="${LANES_EXECUTED}Lane $LANE ($TOOLCHAIN/$MODEL): $STATUS\n"
done

# Generate return packet (NO PREAMBLE - starts immediately with content)
cat > "$BUNDLE/06_return_to_webapp/merged_return_packet.md" << RETURNEOF
BLITZKRIEG RETURN: $SLUG | $DATE_PART

LANES EXECUTED
$(echo -e "$LANES_EXECUTED")
EXECUTION SUMMARY

[Summary of what was accomplished across all lanes - TO BE FILLED]

Git HEAD at finalization: $GIT_HEAD

WHAT CHANGED

- [File or artifact]: [Change description]
- [File or artifact]: [Change description]

WHAT REMAINS

- [Incomplete item or blocker]

NEXT ACTIONS

1. [Immediate priority]
2. [Second priority]
3. [Third priority]

ATTACHMENTS TO CARRY FORWARD

- [Filename]: [Why needed for continuation]
RETURNEOF

echo "Generated: $BUNDLE/06_return_to_webapp/merged_return_packet.md"
```

### Step 5: Generate Audized Scripts

```bash
BUNDLE=$(ls -dt ./-OUTGOING/*-blitzkrieg-* 2>/dev/null | head -1)

# Audize context (following audizer.md protocol strictly)
# NO markdown, NO preamble, capitalize signposts, punctuation for breath
cat > "$BUNDLE/07_audio/audized_context.txt" << 'AUDCTXEOF'
SECTION: BLITZKRIEG CONTEXT.

AUDCTXEOF

# Extract and transform context
if [ -f "$BUNDLE/01_context/context.md" ]; then
    # Strip markdown and transform to audio script
    sed -E '
        s/^#+[[:space:]]*/SECTION: /
        s/\*\*([^*]+)\*\*/\1/g
        s/\*([^*]+)\*/\1/g
        s/`([^`]+)`/\1/g
        s/^-[[:space:]]+/First, /
        s/^[0-9]+\.[[:space:]]+/Next, /
    ' "$BUNDLE/01_context/context.md" | grep -v "^---" | grep -v "^\*" >> "$BUNDLE/07_audio/audized_context.txt"
fi

# Audize pedigree
cat > "$BUNDLE/07_audio/audized_pedigree.txt" << 'AUDPEDEOF'
SECTION: BLITZKRIEG PEDIGREE.

AUDPEDEOF

if [ -f "$BUNDLE/02_pedigree/pedigree.md" ]; then
    sed -E '
        s/^#+[[:space:]]*/SECTION: /
        s/\*\*([^*]+)\*\*/\1/g
        s/\*([^*]+)\*/\1/g
        s/`([^`]+)`/\1/g
        s/^-[[:space:]]+/First, /
        s/^[0-9]+\.[[:space:]]+/Next, /
    ' "$BUNDLE/02_pedigree/pedigree.md" | grep -v "^---" | grep -v "^\*" >> "$BUNDLE/07_audio/audized_pedigree.txt"
fi

# Audize return packet
cat > "$BUNDLE/07_audio/audized_return_packet.txt" << 'AUDRETEOF'
SECTION: BLITZKRIEG RETURN.

AUDRETEOF

if [ -f "$BUNDLE/06_return_to_webapp/merged_return_packet.md" ]; then
    sed -E '
        s/^#+[[:space:]]*/SECTION: /
        s/\*\*([^*]+)\*\*/\1/g
        s/\*([^*]+)\*/\1/g
        s/`([^`]+)`/\1/g
        s/^-[[:space:]]+/First, /
        s/^[0-9]+\.[[:space:]]+/Next, /
        s/BLITZKRIEG RETURN:/BLITZKRIEG RETURN./
        s/LANES EXECUTED/SECTION: LANES EXECUTED./
        s/EXECUTION SUMMARY/SECTION: EXECUTION SUMMARY./
        s/WHAT CHANGED/SECTION: WHAT CHANGED./
        s/WHAT REMAINS/SECTION: WHAT REMAINS./
        s/NEXT ACTIONS/SECTION: NEXT ACTIONS./
        s/ATTACHMENTS TO CARRY FORWARD/SECTION: ATTACHMENTS TO CARRY FORWARD./
    ' "$BUNDLE/06_return_to_webapp/merged_return_packet.md" >> "$BUNDLE/07_audio/audized_return_packet.txt"
fi

echo "Generated audized scripts in $BUNDLE/07_audio/"
```

### Step 6: Generate Agent Relay JSON

```bash
BUNDLE=$(ls -dt ./-OUTGOING/*-blitzkrieg-* 2>/dev/null | head -1)
BLITZKRIEG_ID=$(basename "$BUNDLE")
TIMESTAMP=$(date '+%Y-%m-%dT%H:%M:%S')
GIT_HEAD=$(git rev-parse HEAD 2>/dev/null || echo "unknown")

# Build lanes JSON
LANES_JSON=""
FIRST=true

for directive in "$BUNDLE/04_directives"/directive-*.md; do
    [ -f "$directive" ] || continue

    LANE=$(grep "^Lane:" "$directive" 2>/dev/null | sed 's/^Lane:[[:space:]]*//' | tr -d '\r' || echo "?")
    TOOLCHAIN=$(grep "^Toolchain:" "$directive" 2>/dev/null | sed 's/^Toolchain:[[:space:]]*//' | tr -d '\r' || echo "unknown")
    MODEL=$(grep "^Model:" "$directive" 2>/dev/null | sed 's/^Model:[[:space:]]*//' | tr -d '\r' || echo "unknown")
    THINKING=$(grep "^Thinking:" "$directive" 2>/dev/null | sed 's/^Thinking:[[:space:]]*//' | tr -d '\r' || echo "default")
    SUCCESS=$(grep "^Success_Criteria:" "$directive" 2>/dev/null | sed 's/^Success_Criteria:[[:space:]]*//' | tr -d '\r' | sed 's/"/\\"/g' || echo "")
    INPUTS=$(grep "^Inputs:" "$directive" 2>/dev/null | sed 's/^Inputs:[[:space:]]*//' | tr -d '\r' | sed 's/"/\\"/g' || echo "")
    OUTPUTS=$(grep "^Outputs:" "$directive" 2>/dev/null | sed 's/^Outputs:[[:space:]]*//' | tr -d '\r' | sed 's/"/\\"/g' || echo "")

    EXEC_LOG="$BUNDLE/05_execution/lane-${LANE}/execution_log.md"
    if [ -f "$EXEC_LOG" ]; then
        STATUS=$(grep "^\*\*Status\*\*:" "$EXEC_LOG" 2>/dev/null | sed 's/.*:[[:space:]]*//' | tr -d '\r' || echo "unknown")
    else
        STATUS="NOT_STARTED"
    fi

    if [ "$FIRST" = true ]; then
        FIRST=false
    else
        LANES_JSON="${LANES_JSON},"
    fi

    LANES_JSON="${LANES_JSON}
    \"$LANE\": {
      \"toolchain\": \"$TOOLCHAIN\",
      \"model\": \"$MODEL\",
      \"thinking\": \"$THINKING\",
      \"status\": \"$STATUS\",
      \"success_criteria\": \"$SUCCESS\",
      \"inputs\": \"$INPUTS\",
      \"outputs\": \"$OUTPUTS\"
    }"

    # Generate per-lane JSON
    cat > "$BUNDLE/08_agent_relay/lane-${LANE}.json" << LANEJSONEOF
{
  "type": "blitzkrieg_lane_execution",
  "version": "2.0.0",
  "lane": "$LANE",
  "blitzkrieg_id": "$BLITZKRIEG_ID",
  "toolchain": "$TOOLCHAIN",
  "model": "$MODEL",
  "thinking": "$THINKING",
  "status": "$STATUS",
  "success_criteria": "$SUCCESS",
  "inputs": "$INPUTS",
  "outputs": "$OUTPUTS"
}
LANEJSONEOF
done

# Generate main return packet JSON
cat > "$BUNDLE/08_agent_relay/return_packet.json" << RELAYJSONEOF
{
  "type": "blitzkrieg_return",
  "version": "2.0.0",
  "blitzkrieg_id": "$BLITZKRIEG_ID",
  "generated": "$TIMESTAMP",
  "git_head": "$GIT_HEAD",
  "lanes": {$LANES_JSON
  },
  "execution_summary": "",
  "what_changed": [],
  "what_remains": [],
  "next_actions": [],
  "attachments": []
}
RELAYJSONEOF

echo "Generated agent relay JSON in $BUNDLE/08_agent_relay/"
```

### Step 7: Summary

```bash
BUNDLE=$(ls -dt ./-OUTGOING/*-blitzkrieg-* 2>/dev/null | head -1)

echo ""
echo "=== BLITZKRIEG FINALIZE COMPLETE ==="
echo ""
echo "Bundle: $BUNDLE"
echo ""
echo "Generated artifacts:"
echo "  - 06_return_to_webapp/merged_return_packet.md (paste into Vanguard)"
echo "  - 07_audio/audized_*.txt (TTS-ready, no markdown)"
echo "  - 08_agent_relay/*.json (LLM-to-LLM structured data)"
echo ""
echo "Return packet preview:"
head -20 "$BUNDLE/06_return_to_webapp/merged_return_packet.md"
echo ""
echo "=== NEXT STEPS ==="
echo "1. Review merged_return_packet.md"
echo "2. Fill in execution summary and what changed sections"
echo "3. Copy and paste into originating Vanguard thread"
echo "4. Optionally run /project:deviser_reint for full session export"
```

## Output

Generates in the blitzkrieg bundle:
- `06_return_to_webapp/merged_return_packet.md` — Pasteable return packet (no preamble)
- `07_audio/audized_context.txt` — TTS-ready context
- `07_audio/audized_pedigree.txt` — TTS-ready pedigree
- `07_audio/audized_return_packet.txt` — TTS-ready return packet
- `08_agent_relay/return_packet.json` — Structured return data
- `08_agent_relay/lane-{A,B,C}.json` — Per-lane structured data

## See Also

- `orchestration/state/REF-BLITZKRIEG_PROTOCOL_VNEXT.md` — Full protocol documentation
- `/project:blitzkrieg_issue` — Create bundle skeleton
- `/project:deviser_reint` — Session continuity export
- `audizer.md` — TTS transcoding protocol
