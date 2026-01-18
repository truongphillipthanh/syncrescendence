# What to Canonize Next
**Generated**: 2026-01-17T03:23:54Z
**Purpose**: Propose exact canonical documents to create

---

## Priority 1: Unified Session Lifecycle Protocol

**Proposed File**: `02-OPERATIONAL/PROTOCOL-SESSION_LIFECYCLE.md`

**Gap Addressed**: No unified protocol binding context engineering, continuation, culmination, and retrospective.

### Proposed Structure

```markdown
# Session Lifecycle Protocol
## Version 1.0.0

## 1. Session Initialization
### 1.1 Context Loading
- Read system_state.json
- Load relevant Oracle context
- Verify no conflicting sessions

### 1.2 Objective Setting
- Define session objectives
- Identify expected deliverables
- Set acceptance criteria

### 1.3 State Verification
- Confirm platform availability
- Verify zone ownership
- Check rate limit status

## 2. Session Operation
### 2.1 Packet Flow
- Evidence → Plan → Execution → Audit

### 2.2 Verification Gates
- Pre-commit checks
- Ledger validation
- Protected zone compliance

### 2.3 State Updates
- Update events.jsonl on significant actions
- Checkpoint system_state at phase boundaries

## 3. Session Culmination
### 3.1 Execution Log Generation
- Document completed work
- List files changed
- Record verification output

### 3.2 Ledger Updates
- Update tasks.csv
- Update sources.csv if applicable
- Increment session counters

### 3.3 Commit and Sync
- Semantic commit message
- Multi-remote push
- Verify push success

## 4. Session Retrospective
### 4.1 What Worked
- Document successful patterns

### 4.2 What Didn't Work
- Document friction points

### 4.3 Kaizen Items
- Generate improvement items
- Log to kaizen.csv

## 5. Session Handoff
### 5.1 Continuation Packet
- Generate CONT packet
- Document open questions
- Set next session objectives
```

**Effort**: 2-3 hours
**Priority**: CRITICAL

---

## Priority 2: Continuation Packet Schema

**Proposed File**: `00-ORCHESTRATION/schemas/continuation_packet.json`

**Gap Addressed**: No formal handoff structure between sessions.

### Proposed Schema

```json
{
  "schema_version": "1.0.0",
  "packet_types": {
    "continuation": {
      "description": "Session-to-session handoff packet",
      "required_fields": [
        "id",
        "timestamp",
        "source_session",
        "state_snapshot",
        "context_files",
        "next_objectives"
      ],
      "optional_fields": [
        "open_questions",
        "pending_decisions",
        "blocking_issues",
        "estimated_complexity"
      ],
      "example": {
        "id": "CONT-20260116-001",
        "timestamp": "2026-01-16T12:00:00Z",
        "source_session": {
          "oracle": 13,
          "blitzkrieg": 46,
          "stream": "A"
        },
        "state_snapshot": {
          "tasks_completed": 5,
          "tasks_pending": 3,
          "packets_created": 4
        },
        "context_files": [
          "ORACLE13_CONTEXT.md",
          "INTERACTION_PARADIGM.md"
        ],
        "next_objectives": [
          "Complete Gemini onboarding",
          "Process 5 paradigm sources"
        ]
      }
    }
  },
  "naming_convention": "CONT-YYYYMMDD-NNN",
  "file_format": "JSON",
  "location": "/00-ORCHESTRATION/continuations/"
}
```

**Effort**: 1 hour
**Priority**: HIGH

---

## Priority 3: Retrospective Template

**Proposed File**: `06-EXEMPLA/RETROSPECTIVE_TEMPLATE.md`

**Gap Addressed**: No structured retrospective format.

### Proposed Template

```markdown
# Retrospective: [Session ID]
**Date**: YYYY-MM-DD
**Oracle**: N
**Blitzkrieg**: N
**Duration**: X hours

## Session Objectives
1. [Objective 1] — [Achieved/Partial/Not Achieved]
2. [Objective 2] — [Status]

## What Worked

### Process
- [Item]

### Tools
- [Item]

### Communication
- [Item]

## What Didn't Work

### Process
- [Item]

### Tools
- [Item]

### Communication
- [Item]

## Surprises / Learnings
- [Unexpected insight]

## Kaizen Items

| ID | Description | Owner | Priority | Status |
|----|-------------|-------|----------|--------|
| K-NNN | [Description] | [Owner] | High/Med/Low | pending |

## Metrics

| Metric | Value |
|--------|-------|
| Autonomous cycles | N |
| Principal interventions | N |
| Packets created | N |
| Sources processed | N |
| Canon integrations | N |

## Next Session Preparation
- [ ] Context document ready
- [ ] Objectives defined
- [ ] Blocking issues resolved
```

**Effort**: 1 hour
**Priority**: MEDIUM

---

## Priority 4: Kaizen Ledger

**Proposed File**: `00-ORCHESTRATION/state/kaizen.csv`

**Gap Addressed**: No improvement item tracking.

### Proposed Schema

```csv
id,source_session,date_created,description,priority,status,date_completed,notes
K-001,ORACLE13,2026-01-16,"Create session lifecycle protocol",high,pending,,
K-002,ORACLE13,2026-01-16,"Add continuation packet schema",high,pending,,
```

**Effort**: 30 minutes
**Priority**: MEDIUM

---

## Priority 5: Symbolic Compression Protocol

**Proposed File**: `02-OPERATIONAL/PROTOCOL-SYMBOLIC_COMPRESSION.md`

**Gap Addressed**: When and how to compress artifacts into symbolic forms.

### Proposed Structure

```markdown
# Symbolic Compression Protocol

## Triggers
When to compress:
- Three or more documents address same concept
- Pattern repeats across Oracle sessions
- Decision made three times

## Methods
How to compress:
- Taxonomy: hierarchical classification
- Schema: structural template
- Checklist: verifiable steps
- Diagram: visual relationships

## Quality Criteria
- Original recoverable from compression
- No resolution loss (Lens #7)
- Navigation improved (≤2 decisions to file)

## Examples
[Worked examples of each compression type]
```

**Effort**: 2 hours
**Priority**: LOW

---

## Summary: Creation Order

| Order | Document | Effort | Cumulative |
|-------|----------|--------|------------|
| 1 | PROTOCOL-SESSION_LIFECYCLE.md | 3h | 3h |
| 2 | continuation_packet.json | 1h | 4h |
| 3 | RETROSPECTIVE_TEMPLATE.md | 1h | 5h |
| 4 | kaizen.csv | 0.5h | 5.5h |
| 5 | PROTOCOL-SYMBOLIC_COMPRESSION.md | 2h | 7.5h |

**Total Effort**: ~1 focused Blitzkrieg session (2-3 hours for priorities 1-4)

---

## What NOT to Canonize

The following should remain operational/dynamic, not canonical:

1. **platform_features.md** — Temporal, will drift
2. **frontier_models.md** — Temporal, outdated within months
3. **Research outputs** — Source material, not conclusions
4. **Session transcripts** — Input, not distillation
