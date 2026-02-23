---
name: blitzkrieg_issue
description: Create blitzkrieg bundle skeleton with directive templates for 3-lane execution
allowed-tools: Bash, Read, Write, Glob
---
# Blitzkrieg Issue

Create a blitzkrieg bundle skeleton for 3-lane parallel execution.

**Usage**: `/project:blitzkrieg_issue <slug>`

Where `<slug>` is a short identifier (e.g., `platform-expand`, `iic-complete`).

## Execution

### Step 1: Validate and Create Bundle Directory

```bash
# Get slug from arguments or use default
SLUG="${1:-unnamed}"
DATE=$(date +%Y%m%d)
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
GIT_HEAD=$(git rev-parse HEAD 2>/dev/null || echo "unknown")
BRANCH=$(git branch --show-current 2>/dev/null || echo "unknown")

# Validate slug (alphanumeric and hyphens only)
if ! echo "$SLUG" | grep -qE '^[a-zA-Z0-9-]+$'; then
    echo "ERROR: Invalid slug '$SLUG'. Use alphanumeric characters and hyphens only."
    exit 1
fi

# Check for legacy OUTGOING
if ls -1 | grep -E "^(OUTGOING|outgoing)$" > /dev/null 2>&1; then
    echo "ERROR: Legacy OUTGOING/ or outgoing/ exists. Migrate to agents/commander/outbox/ first."
    exit 1
fi

# Ensure -OUTGOING exists (use ./ prefix to avoid flag interpretation)
mkdir -p "./agents/commander/outbox"

# Determine output path (append suffix if exists)
BASE="./agents/commander/outbox/${DATE}-blitzkrieg-${SLUG}"
OUTDIR="$BASE"
SUFFIX=2
while [ -d "$OUTDIR" ]; do
    OUTDIR="${BASE}-$(printf '%02d' $SUFFIX)"
    ((SUFFIX++))
done

echo "Creating blitzkrieg bundle: $OUTDIR"
mkdir -p "$OUTDIR"
```

### Step 2: Create Manifest

```bash
SLUG="${1:-unnamed}"
DATE=$(date +%Y%m%d)
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
GIT_HEAD=$(git rev-parse HEAD 2>/dev/null || echo "unknown")
BRANCH=$(git branch --show-current 2>/dev/null || echo "unknown")
GIT_STATUS=$(git status --short 2>/dev/null | head -20 || echo "unable to get status")

BASE="./agents/commander/outbox/${DATE}-blitzkrieg-${SLUG}"
OUTDIR="$BASE"
SUFFIX=2
while [ -d "$OUTDIR" ]; do
    OUTDIR="${BASE}-$(printf '%02d' $SUFFIX)"
    ((SUFFIX++))
done

mkdir -p "$OUTDIR/00_manifest"

cat > "$OUTDIR/00_manifest/environment.md" << ENVEOF
# Blitzkrieg Environment

**Generated**: $TIMESTAMP
**Blitzkrieg ID**: $(basename $OUTDIR)
**Git HEAD**: $GIT_HEAD
**Branch**: $BRANCH

## Git Status (at issue time)

\`\`\`
$GIT_STATUS
\`\`\`
ENVEOF

cat > "$OUTDIR/00_manifest/git_state.txt" << GITEOF
HEAD: $GIT_HEAD
Branch: $BRANCH
Timestamp: $TIMESTAMP
GITEOF

cat > "$OUTDIR/00_manifest/inputs_used.md" << INPUTSEOF
# Inputs Used

## Reference Documents
- CLAUDE.md (v2.3.0)
- orchestration/state/REF-BLITZKRIEG_PROTOCOL_VNEXT.md
- orchestration/state/ARCH-INTENTION_COMPASS.md
- orchestration/state/DYN-BACKLOG.md

## Operator-Provided
- 01_context/context.md (TO BE FILLED)
- 02_pedigree/pedigree.md (TO BE FILLED)
INPUTSEOF

echo "Created: $OUTDIR/00_manifest/"
```

### Step 3: Create Context Template

```bash
SLUG="${1:-unnamed}"
DATE=$(date +%Y%m%d)
BASE="./agents/commander/outbox/${DATE}-blitzkrieg-${SLUG}"
OUTDIR="$BASE"
SUFFIX=2
while [ -d "$OUTDIR" ]; do
    OUTDIR="${BASE}-$(printf '%02d' $SUFFIX)"
    ((SUFFIX++))
done

mkdir -p "$OUTDIR/01_context"

cat > "$OUTDIR/01_context/context.md" << 'CTXEOF'
# BLITZKRIEG CONTEXT

## Session Identity
- Oracle: [NUMBER]
- Platform: [chatgpt / claude / gemini]
- Timestamp: [ISO datetime]
- Thread Reference: [URL or identifier]

## Current State Summary

[Paste or summarize the current state from your Vanguard thread]

## Key Decisions Made

### Decision 1: [Title]
[Description]

### Decision 2: [Title]
[Description]

## Constraints and Boundaries

- [Constraint 1]
- [Constraint 2]

## What This Blitzkrieg Must Accomplish

[Clear statement of the blitzkrieg's purpose]

---
*Operator: Fill in the sections above before executing lanes.*
CTXEOF

echo "Created: $OUTDIR/01_context/context.md"
```

### Step 4: Create Pedigree Template

```bash
SLUG="${1:-unnamed}"
DATE=$(date +%Y%m%d)
BASE="./agents/commander/outbox/${DATE}-blitzkrieg-${SLUG}"
OUTDIR="$BASE"
SUFFIX=2
while [ -d "$OUTDIR" ]; do
    OUTDIR="${BASE}-$(printf '%02d' $SUFFIX)"
    ((SUFFIX++))
done

mkdir -p "$OUTDIR/02_pedigree"

cat > "$OUTDIR/02_pedigree/pedigree.md" << 'PEDEOF'
# BLITZKRIEG PEDIGREE

## Oracle Lineage
- Oracle 0-2: Vision, research foundations
- Oracle 3-5: Structure, defrag, recovery
- Oracle 6-9: Annealment, content processing
- Oracle 10-11: Infrastructure, multi-CLI
- Oracle 12: Constellation architecture
- Oracle 13+: [CURRENT PHASE]

## Active Decisions Inherited

| Decision | Oracle | Status |
|----------|--------|--------|
| [Decision 1] | [N] | active |
| [Decision 2] | [N] | active |

## Constitutional Reminders

1. FLAT PRINCIPLE: No subdirectories; use prefixes
2. LEDGER GROUND TRUTH: tasks.csv is authoritative
3. VERIFICATION BEFORE COMPLETION: Always verify
4. SANCTIONED EXCEPTIONS: agents/ only

## Critical Files

- CLAUDE.md — Constitutional rules
- coordination.yaml — Platform routing
- tasks.csv — Ground truth ledger
- ARCH-INTENTION_COMPASS.md — Intention archaeology

---
*Operator: Update lineage and inherited decisions before executing lanes.*
PEDEOF

echo "Created: $OUTDIR/02_pedigree/pedigree.md"
```

### Step 5: Create Intention Reference

```bash
SLUG="${1:-unnamed}"
DATE=$(date +%Y%m%d)
BASE="./agents/commander/outbox/${DATE}-blitzkrieg-${SLUG}"
OUTDIR="$BASE"
SUFFIX=2
while [ -d "$OUTDIR" ]; do
    OUTDIR="${BASE}-$(printf '%02d' $SUFFIX)"
    ((SUFFIX++))
done

mkdir -p "$OUTDIR/03_intention"

cat > "$OUTDIR/03_intention/intention_reference.md" << 'INTEOF'
# Intention Reference

This blitzkrieg should be grounded in the Sovereign's documented intentions.

## Reference Documents

- **ARCH-INTENTION_COMPASS.md**: `orchestration/state/ARCH-INTENTION_COMPASS.md`
  - Contains categorized intentions: urgent, sprint, backlog, pattern, capture
  - Extract relevant intentions for this blitzkrieg

- **DYN-BACKLOG.md**: `orchestration/state/DYN-BACKLOG.md`
  - Contains active sprint and project status
  - Reference active projects this blitzkrieg addresses

## Relevant Intentions (extract from compass)

| ID | Text | Category | Relevance |
|----|------|----------|-----------|
| INT-XXXX | "[intention text]" | sprint | [why relevant] |

## Active Projects Addressed

| Project | Status | How This Blitzkrieg Advances |
|---------|--------|------------------------------|
| PROJ-XXX | active | [contribution] |

---
*Operator: Extract relevant intentions from the compass before executing lanes.*
INTEOF

echo "Created: $OUTDIR/03_intention/intention_reference.md"
```

### Step 6: Create Directive Templates

```bash
SLUG="${1:-unnamed}"
DATE=$(date +%Y%m%d)
BASE="./agents/commander/outbox/${DATE}-blitzkrieg-${SLUG}"
OUTDIR="$BASE"
SUFFIX=2
while [ -d "$OUTDIR" ]; do
    OUTDIR="${BASE}-$(printf '%02d' $SUFFIX)"
    ((SUFFIX++))
done

mkdir -p "$OUTDIR/04_directives"

# Directive A - Strategic
cat > "$OUTDIR/04_directives/directive-A.md" << 'DIREAEOF'
Lane: A
Toolchain: claude_code
Model: opus-4.5
Thinking: ultrathink
Success_Criteria: [Define measurable completion conditions]
Inputs: [List files/artifacts this lane reads]
Outputs: [List files/artifacts this lane produces]

---

# DIRECTIVE-A: [TITLE]

## Objective

[Strategic/architectural objective for Lane A]

## Scope

**In Scope**:
- [Item 1]
- [Item 2]

**Out of Scope**:
- [Item 1]

## Approach

[Step-by-step approach]

## Deliverables

- [ ] [Deliverable 1]
- [ ] [Deliverable 2]

## Dependencies

- Depends on: [none / other lanes / external]
- Blocks: [none / other lanes]

---
*Lane A is typically reserved for strategic/architectural work requiring deep reasoning.*
DIREAEOF

# Directive B - Tactical
cat > "$OUTDIR/04_directives/directive-B.md" << 'DIREBEOF'
Lane: B
Toolchain: claude_code
Model: sonnet-4.5
Thinking: think
Success_Criteria: [Define measurable completion conditions]
Inputs: [List files/artifacts this lane reads]
Outputs: [List files/artifacts this lane produces]

---

# DIRECTIVE-B: [TITLE]

## Objective

[Tactical execution objective for Lane B]

## Scope

**In Scope**:
- [Item 1]
- [Item 2]

**Out of Scope**:
- [Item 1]

## Approach

[Step-by-step approach]

## Deliverables

- [ ] [Deliverable 1]
- [ ] [Deliverable 2]

## Dependencies

- Depends on: [none / other lanes / external]
- Blocks: [none / other lanes]

---
*Lane B is typically reserved for tactical execution with clear instructions.*
DIREBEOF

# Directive C - Validation/Secondary
cat > "$OUTDIR/04_directives/directive-C.md" << 'DIRECEOF'
Lane: C
Toolchain: gemini_cli
Model: gemini-2.0-flash
Thinking: default
Success_Criteria: [Define measurable completion conditions]
Inputs: [List files/artifacts this lane reads]
Outputs: [List files/artifacts this lane produces]

---

# DIRECTIVE-C: [TITLE]

## Objective

[Validation/secondary objective for Lane C]

## Scope

**In Scope**:
- [Item 1]
- [Item 2]

**Out of Scope**:
- [Item 1]

## Approach

[Step-by-step approach]

## Deliverables

- [ ] [Deliverable 1]
- [ ] [Deliverable 2]

## Dependencies

- Depends on: [none / other lanes / external]
- Blocks: [none / other lanes]

---
*Lane C is typically reserved for validation, secondary work, or alternative toolchain testing.*
DIRECEOF

echo "Created: $OUTDIR/04_directives/directive-{A,B,C}.md"
```

### Step 7: Create Execution Placeholders

```bash
SLUG="${1:-unnamed}"
DATE=$(date +%Y%m%d)
BASE="./agents/commander/outbox/${DATE}-blitzkrieg-${SLUG}"
OUTDIR="$BASE"
SUFFIX=2
while [ -d "$OUTDIR" ]; do
    OUTDIR="${BASE}-$(printf '%02d' $SUFFIX)"
    ((SUFFIX++))
done

mkdir -p "$OUTDIR/05_execution/lane-A"
mkdir -p "$OUTDIR/05_execution/lane-B"
mkdir -p "$OUTDIR/05_execution/lane-C"
mkdir -p "$OUTDIR/06_return_to_webapp"
mkdir -p "$OUTDIR/07_audio"
mkdir -p "$OUTDIR/08_agent_relay"

# Lane execution log placeholders
for lane in A B C; do
    cat > "$OUTDIR/05_execution/lane-${lane}/execution_log.md" << LANEEOF
# Lane $lane Execution Log

**Status**: NOT_STARTED
**Started**: [timestamp]
**Completed**: [timestamp]

## Execution Notes

[To be filled during lane execution]

## What Changed

[Files modified, created, deleted]

## Issues Encountered

[Blockers, errors, decisions made]

## Success Criteria Met

- [ ] [Criterion 1]
- [ ] [Criterion 2]
LANEEOF
done

# Return packet placeholder
cat > "$OUTDIR/06_return_to_webapp/.gitkeep" << 'KEEPEOF'
# Placeholder
Run /project:blitzkrieg_finalize to generate merged_return_packet.md
KEEPEOF

# Audio placeholder
cat > "$OUTDIR/07_audio/.gitkeep" << 'KEEPEOF'
# Placeholder
Run /project:blitzkrieg_finalize to generate audized scripts
KEEPEOF

# Agent relay placeholder
cat > "$OUTDIR/08_agent_relay/.gitkeep" << 'KEEPEOF'
# Placeholder
Run /project:blitzkrieg_finalize to generate JSON relay files
KEEPEOF

echo "Created execution placeholders"
```

### Step 8: Summary

```bash
SLUG="${1:-unnamed}"
DATE=$(date +%Y%m%d)
BASE="./agents/commander/outbox/${DATE}-blitzkrieg-${SLUG}"
OUTDIR="$BASE"
SUFFIX=2
while [ -d "$OUTDIR" ]; do
    OUTDIR="${BASE}-$(printf '%02d' $SUFFIX)"
    ((SUFFIX++))
done

echo ""
echo "=== BLITZKRIEG ISSUE COMPLETE ==="
echo ""
echo "Bundle created: $OUTDIR"
echo ""
echo "Structure:"
find "$OUTDIR" -type f | head -20
echo ""
echo "=== NEXT STEPS ==="
echo "1. Fill in 01_context/context.md with decision snapshot from Vanguard"
echo "2. Fill in 02_pedigree/pedigree.md with Oracle lineage"
echo "3. Review 03_intention/intention_reference.md"
echo "4. Customize 04_directives/directive-{A,B,C}.md for your lanes"
echo "5. Execute lanes using specified toolchains"
echo "6. Run /project:blitzkrieg_finalize when complete"
```

## Output

Creates blitzkrieg bundle at `agents/commander/outbox/YYYYMMDD-blitzkrieg-<slug>/` with:
- `00_manifest/` — Environment info
- `01_context/` — Context template (operator fills)
- `02_pedigree/` — Pedigree template (operator fills)
- `03_intention/` — Intention reference
- `04_directives/` — Directive templates for lanes A/B/C
- `05_execution/` — Lane execution log placeholders
- `06_return_to_webapp/` — Placeholder for return packet
- `07_audio/` — Placeholder for audized scripts
- `08_agent_relay/` — Placeholder for JSON relay
