# Gaps to Unified Protocol v2
**Generated**: 2026-01-17T04:45:00Z
**Purpose**: Exact missing pieces with minimal set to canonize

---

## Critical Gaps (Must Fix Immediately)

### Gap C1: Continuation Packet Schema

**Problem**: Web app conversations are deletable. No formalized handoff structure ensures continuity survives thread deletion.

**Current State**:
- `previous_thread.md` exists as ad-hoc pattern
- Oracle contexts exist but are session-specific
- No schema enforces required fields

**Required Artifact**:

```yaml
# 00-ORCHESTRATION/schemas/continuation_packet.json
{
  "type": "continuation",
  "id_format": "CONT-YYYYMMDD-NNN",
  "required_fields": {
    "source_session": {
      "oracle": "number",
      "blitzkrieg": "number",
      "stream": "A|B|null"
    },
    "state_snapshot": {
      "active_tasks": "array",
      "pending_decisions": "array",
      "blocking_issues": "array"
    },
    "context_files": "array of file paths",
    "next_objectives": "array of strings"
  },
  "optional_fields": {
    "open_questions": "array",
    "estimated_complexity": "routine|moderate|complex",
    "platform_assignments": "object"
  }
}
```

**Integration Point**: Add to `packet_protocol.json` alongside EVD/PLN/EXE/AUD.

**Effort**: 30 minutes
**Priority**: CRITICAL

---

### Gap C2: Session Lifecycle Protocol

**Problem**: No unified document governs session start→operate→culminate→retrospect flow.

**Current State**:
- `INTERACTION_PARADIGM.md` describes surfaces, not ceremonies
- Definition of Done exists but not integrated into lifecycle
- Verification gates exist but not assembled into sequence

**Required Artifact**:

```markdown
# 02-OPERATIONAL/PROTOCOL-SESSION_LIFECYCLE.md

## 1. Cold Start (New Session)
1. Load CLAUDE.md constitution
2. Load relevant Oracle context or continuation packet
3. Read system_state.json for current position
4. Verify no conflicting active sessions
5. Set session objectives

## 2. Warm Resume (Continuing Session)
1. Read continuation packet
2. Verify state matches snapshot
3. Resume from last checkpoint

## 3. Operation
1. Follow packet protocol (EVD→PLN→EXE→AUD)
2. Update events.jsonl on significant actions
3. Checkpoint at phase boundaries
4. Maintain single in_progress task

## 4. Culmination
1. Generate execution log (EXECUTION_LOG-DATE-DIRECTIVE.md)
2. Update tasks.csv with completions
3. Update system_state.json counters
4. Commit with semantic prefix
5. Push to remotes

## 5. Failure Recovery
1. If crash before culmination: read last events.jsonl entry
2. Reconstruct state from events
3. Resume from last logged action

## 6. Session Handoff
1. Generate continuation packet
2. Document open questions
3. Set next session objectives
4. Store in 00-ORCHESTRATION/continuations/
```

**Effort**: 1 hour
**Priority**: CRITICAL

---

## High Priority Gaps

### Gap H1: Kaizen Tracking System

**Problem**: System claims continuous improvement but has no improvement backlog.

**Current State**:
- Improvement ideas scatter across execution logs
- No structured capture mechanism
- No velocity metrics

**Required Artifacts**:

1. `00-ORCHESTRATION/state/kaizen.csv`:
```csv
id,source_session,date_created,description,priority,status,date_completed,notes
```

2. Integration with retrospective template:
```markdown
## Kaizen Items
| ID | Description | Owner | Priority | Status |
|----|-------------|-------|----------|--------|
| K-NNN | [item] | [owner] | High/Med/Low | pending |
```

**Effort**: 30 minutes
**Priority**: HIGH

---

### Gap H2: Escalation Paths

**Problem**: Routing exists but no formal escalation when routing fails.

**Current State**:
- `route_task.py` routes by task_type
- No documented fallback when primary fails
- No documentation of "when to escalate to Principal"

**Required Content** (add to coordination.yaml or new doc):

```yaml
escalation_paths:
  execution_failure:
    attempt_1: retry_with_different_prompt
    attempt_2: fallback_to_haiku
    attempt_3: escalate_to_principal

  planning_deadlock:
    attempt_1: request_evidence_packet
    attempt_2: use_chorus_for_reconciliation
    attempt_3: escalate_to_principal

  audit_rejection:
    first_rejection: fix_and_resubmit
    second_rejection: escalate_to_principal

  protected_zone_modification:
    always: escalate_to_principal
```

**Effort**: 45 minutes
**Priority**: HIGH

---

### Gap H3: Crashout Recovery Protocol

**Problem**: When context is lost or system state becomes incoherent, no documented recovery procedure exists.

**Current State**:
- Implicit recovery via reading repo state
- No explicit checklist
- No documented minimal viable restart

**Required Artifact**:

```markdown
# 02-OPERATIONAL/PROTOCOL-CRASHOUT_RECOVERY.md

## Symptoms
- Web app conversation lost/deleted
- Context doesn't load correctly
- Assistant asks questions already answered
- State seems out of sync with reality

## Recovery Procedure

### Step 1: Stop (Do Not Compound Error)
- Do not attempt to "fix" without grounding
- Do not accept assistant's guesses about state

### Step 2: Ground in Repository
1. Read system_state.json
2. Read last 20 events in events.jsonl
3. Read last execution log
4. Verify tasks.csv matches filesystem

### Step 3: Reconstruct Minimal Context
1. Read CLAUDE.md
2. Read most recent Oracle context
3. Read most recent continuation packet (if exists)
4. Construct minimal prompt with verified state

### Step 4: Resume with Verification
1. Start new session with reconstructed context
2. Have assistant verify its understanding against repo
3. Proceed only when alignment confirmed

### Step 5: Post-Incident
1. Log crashout event to events.jsonl
2. Create kaizen item for prevention
3. Consider what artifact was missing that would have helped
```

**Effort**: 45 minutes
**Priority**: HIGH

---

## Medium Priority Gaps

### Gap M1: Retrospective Template

**Problem**: No structured format for session retrospectives.

**Required Artifact**: `06-EXEMPLA/RETROSPECTIVE_TEMPLATE.md` (content specified in pass 1)

**Effort**: 30 minutes
**Priority**: MEDIUM

---

### Gap M2: Symbolic Compression Protocol

**Problem**: Compression is practiced but not documented.

**Required Artifact**: `02-OPERATIONAL/PROTOCOL-SYMBOLIC_COMPRESSION.md` with triggers, methods, quality criteria.

**Effort**: 1 hour
**Priority**: MEDIUM

---

### Gap M3: Replay Procedure

**Problem**: System state should be reconstructable from events, but procedure isn't documented.

**Required Content**:

```markdown
# Replay Procedure

## Purpose
Reconstruct system state from events.jsonl for audit or recovery.

## Procedure
1. Read events.jsonl from start (or from known-good checkpoint)
2. For each event, update simulated state:
   - session_started: reset session state
   - packet_created: track packet
   - execution_completed: mark task done
   - state_updated: apply state change
3. Compare simulated state to system_state.json
4. Discrepancies indicate state corruption

## Verification Commands
```bash
# Count events
wc -l 00-ORCHESTRATION/state/events.jsonl

# Extract event types
jq -r '.event' 00-ORCHESTRATION/state/events.jsonl | sort | uniq -c

# Verify state coherence
python3 scripts/replay_events.py --verify
```
```

**Effort**: 1 hour (including script skeleton)
**Priority**: MEDIUM

---

## Low Priority Gaps

### Gap L1: Chorus Reconciliation Protocol

**Problem**: When to use chorus (multiple platforms), how to reconcile outputs.

**Current State**: Implicit in nth_order_effects.md analysis. Not formalized.

**Effort**: 45 minutes
**Priority**: LOW (minimize chorus use anyway)

---

### Gap L2: Operator Translation Layer

**Problem**: Technical outputs often unintelligible to Principal during stress/fatigue.

**Required**: Guidelines for output formatting that reduce cognitive load. Consider as kaizen item.

**Effort**: 30 minutes
**Priority**: LOW

---

## Minimal Canonization Set

To close all critical and high-priority gaps:

| Order | Document | Location | Effort |
|-------|----------|----------|--------|
| 1 | Continuation packet schema | schemas/continuation_packet.json | 30m |
| 2 | Session lifecycle protocol | 02-OPERATIONAL/PROTOCOL-SESSION_LIFECYCLE.md | 1h |
| 3 | Kaizen ledger | state/kaizen.csv | 15m |
| 4 | Escalation paths | Add to coordination.yaml | 30m |
| 5 | Crashout recovery | 02-OPERATIONAL/PROTOCOL-CRASHOUT_RECOVERY.md | 45m |

**Total Effort**: ~3 hours for critical+high priority gaps

---

## What NOT to Canonize

1. **Temporal capability data** — Use metabolic pattern (JSON → generated views)
2. **Platform comparison docs** — Drift within weeks
3. **Session transcripts** — Input, not distillation
4. **Intermediate reasoning** — Keep conclusions, not journey
