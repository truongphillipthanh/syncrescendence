# Minimal Next Sprint v2
**Generated**: 2026-01-17T05:15:00Z
**Purpose**: Single coherent sprint that maximally reduces fragility

---

## Sprint Objective

**Reduce crashout-class failures to near-zero by implementing the minimum viable resilience layer.**

This sprint prioritizes **prevention architecture** over feature development. The goal is making the system deletable-safe: any single conversation can be deleted without losing continuity.

---

## Sprint Scope

### In Scope
- Session lifecycle protocol implementation
- Continuation packet schema and first instances
- Crashout recovery protocol
- Guardrail enforcement (soft, via protocol)

### Out of Scope (defer to next sprint)
- Dashboard/show_status.py (nice to have)
- Backlog processing (blocked by resilience)
- Platform onboarding completion (depends on stability)
- Validator scripts (incremental improvement)

---

## Deliverables

### D-001: Session Lifecycle Protocol

**File**: `02-OPERATIONAL/PROTOCOL-SESSION_LIFECYCLE.md`

**Content**: Unified protocol for init → operate → culminate → handoff

**Acceptance Criteria**:
- [ ] Cold start procedure documented
- [ ] Warm resume procedure documented
- [ ] Culmination checklist complete
- [ ] Handoff procedure documented
- [ ] Integration with existing INTERACTION_PARADIGM.md

**Effort**: 1 hour
**Priority**: CRITICAL

---

### D-002: Continuation Packet Schema

**File**: `00-ORCHESTRATION/schemas/continuation_packet.json`

**Content**: JSON schema added to packet_protocol.json

**Acceptance Criteria**:
- [ ] Schema defines required fields
- [ ] Schema defines optional fields
- [ ] Naming convention specified (CONT-YYYYMMDD-NNN)
- [ ] Storage location specified
- [ ] Example packet provided

**Effort**: 30 minutes
**Priority**: CRITICAL

---

### D-003: First Continuation Packet

**File**: `00-ORCHESTRATION/continuations/CONT-20260116-001.json`

**Content**: Actual continuation packet for current session

**Acceptance Criteria**:
- [ ] Valid against schema
- [ ] State snapshot accurate
- [ ] Context files listed correctly
- [ ] Next objectives actionable

**Effort**: 15 minutes
**Priority**: HIGH

---

### D-004: Crashout Recovery Protocol

**File**: `02-OPERATIONAL/PROTOCOL-CRASHOUT_RECOVERY.md`

**Content**: Step-by-step recovery procedure

**Acceptance Criteria**:
- [ ] Symptom identification documented
- [ ] Recovery steps explicit and copy-pasteable
- [ ] Ground-in-repo procedure clear
- [ ] Post-incident actions specified

**Effort**: 45 minutes
**Priority**: HIGH

---

### D-005: Kaizen Ledger Initialization

**File**: `00-ORCHESTRATION/state/kaizen.csv`

**Content**: Initial improvement items from this analysis

**Acceptance Criteria**:
- [ ] CSV schema matches proposed format
- [ ] Initial items from crashout analysis
- [ ] Integrated with retrospective template

**Effort**: 15 minutes
**Priority**: MEDIUM

---

### D-006: Retrospective Template

**File**: `06-EXEMPLA/RETROSPECTIVE_TEMPLATE.md`

**Content**: Structured retrospective format

**Acceptance Criteria**:
- [ ] What worked / didn't work sections
- [ ] Kaizen items section
- [ ] Metrics section
- [ ] Next session preparation checklist

**Effort**: 30 minutes
**Priority**: MEDIUM

---

## Sprint Execution Plan

### Phase 1: Protocol Creation (2 hours)

```
D-001 (Session Lifecycle)     ──── 1 hour
         │
         ├──► D-002 (Continuation Schema) ──── 30 min
         │
         └──► D-004 (Crashout Recovery) ──── 45 min
```

### Phase 2: Implementation (1 hour)

```
D-003 (First Continuation Packet) ──── 15 min
         │
         └──► D-005 (Kaizen Ledger) ──── 15 min
                  │
                  └──► D-006 (Retrospective Template) ──── 30 min
```

### Phase 3: Integration (30 minutes)

- Update INTERACTION_PARADIGM.md to reference new protocols
- Add continuation packet type to packet_protocol.json
- Create first retrospective using template
- Commit with semantic message

---

## Success Criteria

### Quantitative
- [ ] 6 deliverables complete
- [ ] 0 protocol gaps in crashout prevention
- [ ] 1 continuation packet exists

### Qualitative
- [ ] Principal can delete any thread with confidence
- [ ] Recovery from crashout takes <15 minutes
- [ ] New sessions start with verifiable state

---

## Anti-Patterns to Avoid

| Anti-Pattern | Correct Pattern |
|--------------|-----------------|
| "Let's also add..." | Stick to scope |
| "This could be better if..." | Ship minimal, iterate |
| "We should think about..." | Think is done; execute |
| "Just one more thing..." | No scope creep |

---

## Sprint Ceremony

### Start
1. Read this document
2. Verify state matches expectations
3. Begin Phase 1

### Progress Check (midpoint)
1. D-001 and D-002 complete?
2. Any blockers?
3. Adjust if needed

### End
1. All deliverables complete?
2. Verification passes?
3. Commit and push
4. Create retrospective using D-006 template
5. Create continuation packet using D-002 schema

---

## Post-Sprint State

After this sprint:

```
00-ORCHESTRATION/
├── schemas/
│   └── packet_protocol.json  # Updated with continuation type
├── continuations/
│   └── CONT-20260116-001.json  # First instance
├── state/
│   └── kaizen.csv  # Initialized

02-OPERATIONAL/
├── PROTOCOL-SESSION_LIFECYCLE.md  # NEW
└── PROTOCOL-CRASHOUT_RECOVERY.md  # NEW

06-EXEMPLA/
└── RETROSPECTIVE_TEMPLATE.md  # NEW
```

---

## What This Enables

With this sprint complete:

1. **Any conversation is deletable** → continuation packets exist
2. **Crashes are recoverable** → crashout protocol is documented
3. **Sessions have consistent structure** → lifecycle protocol enforced
4. **Improvements are tracked** → kaizen ledger captures items
5. **Learning is structured** → retrospective template enables

The system moves from "fragile" to "resilient" with minimal overhead.
