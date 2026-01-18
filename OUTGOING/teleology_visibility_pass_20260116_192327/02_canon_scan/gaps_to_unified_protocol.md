# Gaps to Unified Protocol
**Generated**: 2026-01-17T03:23:54Z

---

## Executive Summary

The repository contains ~70% of protocol components but lacks binding documentation that unifies them into a coherent operational lifecycle. The gaps are primarily in **ceremony specification** and **retrospective discipline**.

---

## Gap Inventory

### Gap 1: Session Lifecycle Protocol
**What's Missing**: A single document defining how Oracle/Blitzkrieg sessions start, operate, and end.

**Current State**:
- `system_state.json` tracks session numbers but not session lifecycle
- `INTERACTION_PARADIGM.md` describes surfaces but not ceremonies
- No formal session initiation checklist
- No formal session termination checklist

**Required Content**:
```yaml
session_lifecycle:
  init:
    - Verify system_state.json current
    - Load relevant Oracle context
    - Confirm no conflicting active sessions
    - Set session objectives

  operate:
    - Follow packet protocol (EVD→PLN→EXE→AUD)
    - Update events.jsonl on significant actions
    - Checkpoint state at phase boundaries

  culminate:
    - Generate execution log
    - Update tasks.csv with completions
    - Commit with semantic message
    - Update system_state session numbers

  retrospect:
    - Document what worked/didn't
    - Generate kaizen items
    - Log to retrospective archive
```

**Proposed File**: `02-OPERATIONAL/PROTOCOL-SESSION_LIFECYCLE.md`

---

### Gap 2: Continuation Packet Specification
**What's Missing**: Formal structure for session-to-session handoff.

**Current State**:
- Oracle contexts exist but are ad-hoc
- `previous_thread.md` pattern exists but is not formalized
- No schema for continuation packets

**Required Content**:
```yaml
continuation_packet:
  id: "CONT-YYYYMMDD-NNN"
  source_session:
    oracle: N
    blitzkrieg: N
    stream: "A|B"
  state_snapshot:
    active_tasks: [...]
    pending_decisions: [...]
    open_questions: [...]
  context_files: [...]
  next_session_objectives: [...]
  estimated_complexity: "routine|moderate|complex"
```

**Proposed File**: `00-ORCHESTRATION/schemas/continuation_packet.json`

---

### Gap 3: Retrospective Protocol
**What's Missing**: Structured retrospective format and cadence.

**Current State**:
- `ARCH-REVIEW_VS_RETROSPECTIVE.md` in archive acknowledges concept
- No structured retrospective template
- No retrospective archive location

**Required Content**:
```markdown
# Retrospective: [Session ID]

## What Worked
- [item]

## What Didn't Work
- [item]

## Action Items (Kaizen)
| ID | Description | Owner | Status |
|----|-------------|-------|--------|
| K-001 | ... | ... | pending |

## Metrics
- Autonomous cycles completed: N
- Principal interventions required: N
- Drift incidents: N
```

**Proposed Files**:
- `06-EXEMPLA/RETROSPECTIVE_TEMPLATE.md`
- `00-ORCHESTRATION/retrospectives/` (new directory for archive)

---

### Gap 4: Symbolic Compression Protocol
**What's Missing**: When and how to compress artifacts into symbolic forms.

**Current State**:
- Implicit in Canon (celestial hierarchy as compression)
- 18 Lenses compress decisions
- No explicit "compression triggers" or methodology

**Required Content**:
```yaml
compression_protocol:
  triggers:
    - Three or more documents address same concept → compress into schema
    - Pattern repeats across Oracle sessions → compress into protocol
    - Decision made three times → compress into rule

  methods:
    - taxonomy: Create hierarchical classification
    - schema: Define structural template
    - checklist: Compress process into verifiable steps
    - diagram: Visual compression of relationships

  verification:
    - Original content recoverable from compression
    - No resolution loss per Lens #7
    - Navigation improved (2 decisions to file)
```

**Proposed File**: `02-OPERATIONAL/PROTOCOL-SYMBOLIC_COMPRESSION.md`

---

### Gap 5: Kaizen Tracking
**What's Missing**: Improvement item lifecycle management.

**Current State**:
- Implicit in Oracle arc (progressive refinement)
- No explicit kaizen backlog
- No improvement velocity metrics

**Required Content**:
- Kaizen backlog in `00-ORCHESTRATION/state/kaizen.csv`
- Format: `id,source_session,description,status,completed_date`
- Integration with retrospective output

**Proposed File**: `00-ORCHESTRATION/state/kaizen.csv`

---

### Gap 6: Verification Gate Specification
**What's Missing**: Explicit gates between protocol phases.

**Current State**:
- `make verify` exists but not integrated into protocol
- No phase-transition gates documented
- Verification is ad-hoc rather than systematic

**Required Content**:
```yaml
verification_gates:
  pre_commit:
    - CLAUDE.md constitutional compliance
    - No protected zone violations
    - Ledger validation passes

  pre_merge:
    - Execution log complete
    - tasks.csv updated
    - No drift from plan

  pre_culmination:
    - All deliverables present
    - Verification commands passed
    - State vector updated
```

**Proposed File**: Integrate into `02-OPERATIONAL/PROTOCOL-SESSION_LIFECYCLE.md`

---

## Priority Order

| Priority | Gap | Impact | Effort |
|----------|-----|--------|--------|
| 1 | Session Lifecycle Protocol | HIGH | MEDIUM |
| 2 | Continuation Packet Specification | HIGH | LOW |
| 3 | Retrospective Protocol | MEDIUM | LOW |
| 4 | Kaizen Tracking | MEDIUM | LOW |
| 5 | Verification Gate Specification | MEDIUM | LOW |
| 6 | Symbolic Compression Protocol | LOW | MEDIUM |

---

## Immediate Next Steps

1. **Create** `02-OPERATIONAL/PROTOCOL-SESSION_LIFECYCLE.md` unifying gaps 1, 5, 6
2. **Create** `00-ORCHESTRATION/schemas/continuation_packet.json` for gap 2
3. **Create** `06-EXEMPLA/RETROSPECTIVE_TEMPLATE.md` for gap 3
4. **Create** `00-ORCHESTRATION/state/kaizen.csv` for gap 5

Estimated effort: 1 focused Blitzkrieg session (2-3 hours).
