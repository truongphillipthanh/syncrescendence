# Minimal Replay Instructions
**Generated**: 2026-01-17T03:23:54Z
**Purpose**: How to reinitialize the Syncrescendence system from repository alone

---

## Prerequisites

### Required Artifacts in Repository
```
CLAUDE.md                                    # Constitutional rules
config/coordination.yaml                      # Platform coordination
00-ORCHESTRATION/state/system_state.json     # Current state vector
00-ORCHESTRATION/state/events.jsonl          # Event history
00-ORCHESTRATION/state/tasks.csv             # Task ledger
00-ORCHESTRATION/schemas/packet_protocol.json # Packet schemas
```

### Required External State
| Item | Location | Purpose |
|------|----------|---------|
| Claude Pro subscription | Account 1, 2, 3 | Execution capability |
| Gemini Advanced subscription | Google account | Corpus sensing |
| ChatGPT Plus subscription | OpenAI account | Planning/audit |
| Git repository access | GitHub/remote | Version control |
| Claude Code CLI | Local install | Execution surface |

---

## Replay Sequence

### Step 1: Clone Repository
```bash
git clone <remote-url> syncrescendence
cd syncrescendence
git checkout main
```

### Step 2: Verify State Vector
```bash
cat 00-ORCHESTRATION/state/system_state.json | python3 -m json.tool
```

Expected structure:
```json
{
  "schema_version": "1.0.0",
  "session": { "oracle": N, "blitzkrieg": N, "stream": "A" },
  "platform_status": {...},
  "metrics": {...}
}
```

### Step 3: Verify Event Log
```bash
tail -10 00-ORCHESTRATION/state/events.jsonl
```

Should show recent events. If empty or corrupted, system context is lost.

### Step 4: Verify Blackboard
```bash
ls 00-ORCHESTRATION/blackboard/*/
```

Expected directories:
- evidence/
- plans/
- executions/
- audits/
- capabilities/

### Step 5: Load Context Document
The most recent Oracle context contains session-specific understanding:
```bash
ls -la *.md | grep -i oracle
# or
ls 00-ORCHESTRATION/oracle_contexts/
```

Read the most recent:
```bash
cat ORACLE13_CONTEXT.md  # or similar
```

### Step 6: Initialize Claude Code Session
```bash
# Read context first
cat CLAUDE.md
cat INTERACTION_PARADIGM.md

# Start Claude Code
claude

# In Claude Code:
# "Resume from Oracle 13 context. Read system_state.json to understand current state."
```

### Step 7: Verify Routing Script
```bash
python3 00-ORCHESTRATION/scripts/route_task.py execution
```

Should return valid routing decision.

### Step 8: Run Verification
```bash
make verify  # If Makefile exists
# OR manually:
python3 00-ORCHESTRATION/scripts/verify_all.sh 2>/dev/null || echo "Manual verification required"
```

---

## What Cannot Be Replayed

### Lost Without Conversation History
1. **Reasoning chains** that led to decisions (only conclusions in Canon)
2. **Intermediate explorations** that didn't culminate
3. **Principal preferences** not codified in CLAUDE.md
4. **Session-specific context** that wasn't logged to events.jsonl

### Requires External Restoration
1. **Platform credentials** (must re-authenticate)
2. **MCP server connections** (must re-establish)
3. **Claude Project memory** (if using web app Project feature)
4. **ChatGPT Custom Instructions** (must re-apply)
5. **Gemini Custom Gem** (must re-configure)

---

## Cold Start vs Warm Resume

### Cold Start (New Session, No Prior Context)
```bash
# Read constitutional docs
cat CLAUDE.md INTERACTION_PARADIGM.md

# Read current state
cat 00-ORCHESTRATION/state/system_state.json

# Start fresh Oracle session
# Increment oracle number, generate new context
```

### Warm Resume (Continuing Prior Session)
```bash
# Read existing context
cat ORACLE*_CONTEXT.md

# Verify state matches expectations
cat 00-ORCHESTRATION/state/system_state.json

# Continue from last event
tail -1 00-ORCHESTRATION/state/events.jsonl
```

---

## Recovery Scenarios

### Scenario 1: Corrupted system_state.json
1. Check backup: `ls 00-ORCHESTRATION/state/*.bak*`
2. If no backup, reconstruct from events.jsonl:
   ```bash
   tail -50 00-ORCHESTRATION/state/events.jsonl | grep session
   ```
3. Reset metrics to 0, update timestamp

### Scenario 2: Empty events.jsonl
1. Critical context loss—system history unavailable
2. Reconstruct from execution logs:
   ```bash
   ls 00-ORCHESTRATION/execution_logs/ | tail -5
   ```
3. Initialize fresh event log with system_init event

### Scenario 3: Missing Oracle Context
1. Check archive: `ls 00-ORCHESTRATION/oracle_contexts/`
2. If missing, search root: `ls *.md | grep -i oracle`
3. Generate new context from CLAUDE.md + recent directives

### Scenario 4: Ledger Corruption (tasks.csv)
1. Check backup: `ls 00-ORCHESTRATION/state/tasks.csv.bak*`
2. Restore from most recent backup
3. Verify row count matches expectations

---

## Minimum Viable State

To operate the system, you need at minimum:

| Artifact | Purpose | Can Be Reconstructed? |
|----------|---------|----------------------|
| CLAUDE.md | Constitutional rules | No—must exist |
| coordination.yaml | Platform config | Yes—from documentation |
| system_state.json | Current state | Yes—with effort |
| events.jsonl | Event history | Partial—from logs |
| tasks.csv | Task ledger | Yes—from execution logs |
| packet_protocol.json | Packet schemas | Yes—from documentation |

**Critical**: CLAUDE.md and coordination.yaml are the irreplaceable foundation. Everything else can be reconstructed with sufficient effort.

---

## Verification Checklist

Before considering system operational:

- [ ] CLAUDE.md exists and readable
- [ ] coordination.yaml exists and valid YAML
- [ ] system_state.json exists and valid JSON
- [ ] events.jsonl exists (can be empty for fresh start)
- [ ] tasks.csv exists with header row
- [ ] Blackboard directories exist
- [ ] route_task.py executes without error
- [ ] Git status shows clean or known changes
