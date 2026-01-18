# Session Lifecycle Protocol v1
**Generated**: 2026-01-17T04:50:00Z
**Purpose**: Unified protocol governing session initialization, operation, culmination, and handoff

---

## Overview

Every Syncrescendence work session follows this lifecycle. Skipping steps leads to state drift, context loss, or incomplete work.

```
┌─────────────────────────────────────────────────────────────┐
│                    SESSION LIFECYCLE                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌───────────┐      ┌───────────┐      ┌───────────┐      │
│   │   INIT    │──────│  OPERATE  │──────│ CULMINATE │      │
│   └───────────┘      └───────────┘      └───────────┘      │
│         │                  │                  │            │
│         ▼                  ▼                  ▼            │
│   Load context      Follow IMEP        Generate log        │
│   Verify state      Update events      Update ledgers      │
│   Set objectives    Gate progress      Commit + push       │
│                                                             │
│                          │                                  │
│                          ▼                                  │
│                    ┌───────────┐                           │
│                    │  HANDOFF  │                           │
│                    └───────────┘                           │
│                          │                                  │
│                          ▼                                  │
│                    Create CONT packet                       │
│                    Document questions                       │
│                    Next objectives                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Phase 1: Initialization

### 1.1 Cold Start (New Session)

**Prerequisites**: No prior context in current interface

**Steps**:

```bash
# 1. Read constitutional documents
cat CLAUDE.md
cat config/coordination.yaml

# 2. Read current state
cat 00-ORCHESTRATION/state/system_state.json | python3 -m json.tool
tail -20 00-ORCHESTRATION/state/events.jsonl

# 3. Read relevant context
cat ORACLE13_CONTEXT.md  # or latest
cat INTERACTION_PARADIGM.md

# 4. Verify no conflicting sessions
grep '"platform_status"' 00-ORCHESTRATION/state/system_state.json

# 5. Check for continuation packet
ls -la 00-ORCHESTRATION/continuations/ | tail -5
```

**Success Criteria**:
- [ ] Constitutional rules understood
- [ ] Current state visible
- [ ] No conflicting sessions active
- [ ] Session objectives clear

### 1.2 Warm Resume (Continuing Session)

**Prerequisites**: Continuation packet exists from prior session

**Steps**:

```bash
# 1. Load continuation packet
cat 00-ORCHESTRATION/continuations/CONT-YYYYMMDD-NNN.json | python3 -m json.tool

# 2. Verify state snapshot matches current state
diff <(jq '.state_snapshot' CONT-*.json) <(jq '{active_tasks, pending_decisions}' system_state.json)

# 3. Load context files listed in packet
for f in $(jq -r '.context_files[]' CONT-*.json); do cat "$f"; done

# 4. Resume from next_objectives
jq '.next_objectives' CONT-*.json
```

**Success Criteria**:
- [ ] State matches snapshot (or discrepancy documented)
- [ ] Context files loaded
- [ ] Clear on what to do next

### 1.3 Crashout Recovery (State Incoherent)

See `PROTOCOL-CRASHOUT_RECOVERY.md` for detailed procedure.

**Quick Version**:
1. STOP - do not compound error
2. Ground in repository (read state, events, last log)
3. Reconstruct minimal context
4. Resume with verification

---

## Phase 2: Operation

### 2.1 Packet Flow (IMEP)

All substantive work follows the packet protocol:

```
Oracle (Evidence) → Deviser (Plan) → Executor (Execute) → Deviser (Audit) → State Update
```

**For Each Packet**:
1. Create packet with required fields
2. Store in appropriate blackboard directory
3. Log creation event to events.jsonl
4. Reference packet ID in subsequent work

### 2.2 Event Logging

Log significant actions to `events.jsonl`:

```json
{"timestamp": "2026-01-16T14:30:00Z", "event": "session_started", "actor": "claude_code_2", "data": {"oracle": 13, "objectives": ["..."]}}
{"timestamp": "2026-01-16T14:35:00Z", "event": "packet_created", "actor": "claude_code_2", "data": {"packet_id": "EXE-20260116-001"}}
{"timestamp": "2026-01-16T15:00:00Z", "event": "execution_completed", "actor": "claude_code_2", "data": {"files_changed": 5}}
```

**When to Log**:
- Session start/end
- Packet creation
- Execution completion
- Audit decisions
- State updates
- Errors/failures

### 2.3 Verification Gates

**Before Committing**:
```bash
# Run verification
make verify

# Check for constitutional compliance
grep -r "subdirectories" 00-ORCHESTRATION/ 01-CANON/  # Should find nothing new

# Validate ledgers
python3 scripts/validate_ledgers.py  # If exists
```

**Before Claiming "Done"**:
- [ ] Deliverables exist at specified paths
- [ ] Verification commands pass
- [ ] No drift from plan acceptance criteria
- [ ] State vector updated

### 2.4 Progress Gating

Only ONE task `in_progress` at a time. Complete or explicitly pause before starting new work.

```yaml
# Correct pattern
- task_1: in_progress
- task_2: pending
- task_3: pending

# After completing task_1
- task_1: completed
- task_2: in_progress
- task_3: pending
```

---

## Phase 3: Culmination

### 3.1 Execution Log Generation

Create `EXECUTION_LOG-YYYY-MM-DD-DIRECTIVE.md`:

```markdown
# Execution Log: DIRECTIVE-046B
**Date**: 2026-01-16
**Executor**: Claude Code (Account 2)
**Stream**: B

## Objectives
1. [Objective 1] - COMPLETE
2. [Objective 2] - COMPLETE

## Actions Taken
1. [Action with file paths and commands]
2. [Action with verification output]

## Files Changed
- 00-ORCHESTRATION/state/system_state.json
- 01-CANON/CANON-31150-PLATFORM_CAPABILITY_CATALOG.md
- [etc.]

## Verification
```bash
$ make verify
All checks passed.
```

## Notes
- [Observations, decisions made, issues encountered]
```

### 3.2 Ledger Updates

**tasks.csv**:
```bash
# Mark completed tasks
python3 scripts/update_ledger.py tasks.csv --task TASK-001 --status DONE
```

**sources.csv** (if applicable):
```bash
# Update source status
python3 scripts/update_ledger.py sources.csv --source SOURCE-001 --status processed
```

**system_state.json**:
```json
{
  "session_numbers": {
    "oracle": 13,
    "blitzkrieg": 46
  },
  "metrics": {
    "autonomous_cycles": 6,  // increment
    "sources_processed": 1   // increment
  }
}
```

### 3.3 Commit and Sync

```bash
# Stage changes
git add .

# Commit with semantic prefix
git commit -m "$(cat <<'EOF'
feat(blitzkrieg): complete DIRECTIVE-046B visibility pass

- Generate teleology visibility pass 2 artifacts
- Create continuation packet and session lifecycle protocols
- Document crashout forensics and recovery procedures

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
EOF
)"

# Push to all remotes
git push all main

# Verify push success
git log --oneline -1
```

---

## Phase 4: Handoff

### 4.1 Create Continuation Packet

If session is ending (not just pausing):

```bash
# Generate continuation packet
cat > 00-ORCHESTRATION/continuations/CONT-$(date +%Y%m%d)-001.json << 'EOF'
{
  "id": "CONT-YYYYMMDD-001",
  "timestamp": "TIMESTAMP",
  "source_session": {...},
  "state_snapshot": {...},
  "context_files": [...],
  "next_objectives": [...]
}
EOF
```

### 4.2 Document Open Questions

In the continuation packet or execution log:

```markdown
## Open Questions
- [ ] Should X be implemented as Y or Z?
- [ ] Is the current approach aligned with Lens 7?
```

### 4.3 Set Next Objectives

Be specific. "Continue work" is not an objective.

```json
"next_objectives": [
  "Process 3 paradigm sources from 04-SOURCES/raw/",
  "Implement show_status.py dashboard",
  "Create kaizen.csv and retrospective template"
]
```

---

## Failure Recovery

### Session Crash

If session ends unexpectedly:

1. Check last event in `events.jsonl`
2. Check git status for uncommitted work
3. Check for partial execution logs
4. Reconstruct state from artifacts

### State Mismatch

If continuation packet doesn't match reality:

1. Trust repository over packet
2. Document discrepancy
3. Create corrected continuation packet
4. Log as state_correction event

### Verification Failure

If `make verify` fails:

1. Do NOT commit
2. Identify failing check
3. Fix issue or document as blocking
4. Re-run verification
5. Only commit when passing

---

## Ceremony Checklist

### Session Start
- [ ] Constitution loaded
- [ ] State verified
- [ ] Objectives defined
- [ ] No conflicts

### Session End
- [ ] Execution log created
- [ ] Ledgers updated
- [ ] State updated
- [ ] Committed and pushed
- [ ] Continuation packet created (if handoff)

---

## Anti-Patterns

| Anti-Pattern | Correct Pattern |
|--------------|-----------------|
| Start work without reading state | Always read system_state.json first |
| Multiple tasks in_progress | Single task focus, complete or pause |
| Claim done without verification | Run verification commands |
| Skip culmination to "save time" | Culmination prevents more expensive rework |
| Leave session without handoff | Always create continuation packet |
