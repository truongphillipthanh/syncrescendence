# PACKET TEMPLATES: MINIMAL SET
## Copy/Paste Templates for Every Handoff Scenario
**Generated**: 2026-01-17
**Purpose**: Ready-to-use packet templates with required fields and acceptance criteria

---

## I. PACKET OVERVIEW

| Packet Type | Code | Purpose | When to Use |
|-------------|------|---------|-------------|
| Evidence | EVD | Sensing findings | After research/exploration |
| Plan | PLN | Specification for execution | Before implementation |
| Execution | EXE | What was done | After implementation |
| Audit | AUD | Verification of execution | After review |
| Continuation | CONT | Session handoff | When session can be deleted |

---

## II. EVIDENCE PACKET

**Purpose**: Structured findings from sensing, research, or exploration.

### Required Fields
- `id`: EVD-YYYYMMDD-NNN
- `created`: ISO 8601 timestamp
- `source`: Platform that produced this
- `query`: What was asked
- `findings`: List of findings with confidence
- `uncertainties`: What remains unclear

### Optional Fields
- `corpus_slice`: Which files/sources were examined
- `recommended_probe`: What to investigate next

### Template (Markdown)

```markdown
# EVIDENCE PACKET
**ID**: EVD-YYYYMMDD-NNN
**Created**: YYYY-MM-DD HH:MM UTC
**Source**: [gemini|perplexity|grok|claude]

## Query
[What was being investigated]

## Corpus/Sources Examined
- [file or URL 1]
- [file or URL 2]
- [file or URL 3]

## Findings

### Finding 1
**Statement**: [What was found]
**Confidence**: [high|medium|low]
**Source**: [specific file:line or URL]

### Finding 2
**Statement**: [What was found]
**Confidence**: [high|medium|low]
**Source**: [specific file:line or URL]

### Finding 3
**Statement**: [What was found]
**Confidence**: [high|medium|low]
**Source**: [specific file:line or URL]

## Uncertainties
- [What remains unclear]
- [What needs verification]

## Recommended Next Probe
[What to investigate next, if applicable]
```

### Template (JSON)

```json
{
  "packet_type": "EVIDENCE",
  "id": "EVD-YYYYMMDD-NNN",
  "created": "YYYY-MM-DDTHH:MM:SSZ",
  "source": "gemini",
  "query": "What was being investigated",
  "corpus_slice": ["file1.md", "file2.md"],
  "findings": [
    {
      "statement": "What was found",
      "confidence": "high",
      "source": "file:line"
    }
  ],
  "uncertainties": ["What remains unclear"],
  "recommended_probe": "What to investigate next"
}
```

### Acceptance Criteria
- [ ] Query is stated clearly
- [ ] Each finding has confidence level
- [ ] Uncertainties are explicit (not hidden)
- [ ] Sources are verifiable

---

## III. PLAN PACKET

**Purpose**: Specification with acceptance criteria for execution.

### Required Fields
- `id`: PLN-YYYYMMDD-NNN
- `created`: ISO 8601 timestamp
- `objective`: What we're trying to accomplish
- `deliverables`: What will be produced
- `acceptance_criteria`: How we know it's done

### Optional Fields
- `evidence_ids`: Evidence packets that informed this
- `stop_conditions`: When to stop even if not complete
- `tracks`: Parallel work streams

### Template (Markdown)

```markdown
# PLAN PACKET
**ID**: PLN-YYYYMMDD-NNN
**Created**: YYYY-MM-DD HH:MM UTC
**Based On**: [evidence packet IDs or directive]

## Objective
[What we're trying to accomplish - one clear sentence]

## Deliverables

| Artifact | Location | Format |
|----------|----------|--------|
| [What will be produced] | [path/to/file] | [md/json/csv] |
| [What will be produced] | [path/to/file] | [md/json/csv] |

## Acceptance Criteria

| # | Criterion | Verification |
|---|-----------|--------------|
| 1 | [How we know it's done] | [Command or check to run] |
| 2 | [How we know it's done] | [Command or check to run] |
| 3 | [How we know it's done] | [Command or check to run] |

## Stop Conditions
- [When to stop even if not complete]
- [Time limit: X minutes]

## Tracks (if parallel)

### Track A
1. [Task 1]
2. [Task 2]

### Track B (parallel with A)
1. [Task 1]
2. [Task 2]

## Risks
- [What could go wrong]
- [Mitigation]
```

### Template (JSON)

```json
{
  "packet_type": "PLAN",
  "id": "PLN-YYYYMMDD-NNN",
  "created": "YYYY-MM-DDTHH:MM:SSZ",
  "evidence_ids": ["EVD-YYYYMMDD-NNN"],
  "objective": "What we're trying to accomplish",
  "deliverables": [
    {
      "artifact": "What will be produced",
      "location": "path/to/file",
      "format": "md"
    }
  ],
  "acceptance_criteria": [
    {
      "criterion": "How we know it's done",
      "verification": "Command or check to run"
    }
  ],
  "stop_conditions": ["When to stop"],
  "tracks": [
    {
      "track": "A",
      "tasks": ["Task 1", "Task 2"],
      "parallel": true
    }
  ]
}
```

### Acceptance Criteria for the Plan
- [ ] Objective is one clear sentence
- [ ] Each deliverable has a location
- [ ] Each acceptance criterion has a verification method
- [ ] Stop conditions prevent runaway

---

## IV. EXECUTION PACKET

**Purpose**: Document what was executed with evidence.

### Required Fields
- `id`: EXE-YYYYMMDD-NNN
- `created`: ISO 8601 timestamp
- `plan_id`: Which plan was executed
- `status`: complete/partial/failed
- `changes`: What files were modified
- `verification`: Verification results

### Optional Fields
- `issues_encountered`: Problems hit during execution
- `commits`: Git commit hashes

### Template (Markdown)

```markdown
# EXECUTION PACKET
**ID**: EXE-YYYYMMDD-NNN
**Created**: YYYY-MM-DD HH:MM UTC
**Plan ID**: PLN-YYYYMMDD-NNN
**Status**: [complete|partial|failed]

## Changes Made

| File | Action | Summary |
|------|--------|---------|
| [path/to/file] | [created|modified|deleted] | [What changed] |
| [path/to/file] | [created|modified|deleted] | [What changed] |

## Verification Results

| Criterion | Verification | Result |
|-----------|--------------|--------|
| [From plan] | [Command run] | [PASS/FAIL] |
| [From plan] | [Command run] | [PASS/FAIL] |

## Issues Encountered
- [Problem 1] → [How resolved]
- [Problem 2] → [Still open]

## Commits
- `abc1234` — [Commit message]
- `def5678` — [Commit message]

## Remaining Work (if partial)
- [What wasn't completed]
- [Why not]
```

### Template (JSON)

```json
{
  "packet_type": "EXECUTION",
  "id": "EXE-YYYYMMDD-NNN",
  "created": "YYYY-MM-DDTHH:MM:SSZ",
  "plan_id": "PLN-YYYYMMDD-NNN",
  "status": "complete",
  "changes": [
    {
      "file": "path/to/file",
      "action": "modified",
      "summary": "What changed"
    }
  ],
  "verification": [
    {
      "criterion": "From plan",
      "command": "Command run",
      "result": "PASS"
    }
  ],
  "issues_encountered": ["Problem description"],
  "commits": ["abc1234", "def5678"]
}
```

### Acceptance Criteria for Execution
- [ ] Plan ID is referenced
- [ ] All changes are listed with actions
- [ ] Verification matches plan criteria
- [ ] Commits are recorded

---

## V. AUDIT PACKET

**Purpose**: Verify execution against plan.

### Required Fields
- `id`: AUD-YYYYMMDD-NNN
- `created`: ISO 8601 timestamp
- `execution_id`: Which execution was audited
- `plan_id`: Which plan it was against
- `criteria_results`: Pass/fail per criterion
- `recommendation`: accept/reject/revise

### Optional Fields
- `drift_analysis`: How execution differed from plan
- `follow_up_actions`: What to do next

### Template (Markdown)

```markdown
# AUDIT PACKET
**ID**: AUD-YYYYMMDD-NNN
**Created**: YYYY-MM-DD HH:MM UTC
**Execution ID**: EXE-YYYYMMDD-NNN
**Plan ID**: PLN-YYYYMMDD-NNN

## Criteria Results

| # | Criterion | Expected | Actual | Result |
|---|-----------|----------|--------|--------|
| 1 | [From plan] | [Expected outcome] | [What happened] | [PASS/FAIL] |
| 2 | [From plan] | [Expected outcome] | [What happened] | [PASS/FAIL] |
| 3 | [From plan] | [Expected outcome] | [What happened] | [PASS/FAIL] |

## Drift Analysis
[How execution differed from plan, if at all]

## Issues Found
- [Issue 1] — Severity: [high/medium/low]
- [Issue 2] — Severity: [high/medium/low]

## Recommendation
**[ACCEPT / REJECT / REVISE]**

Rationale: [Why this recommendation]

## Follow-Up Actions
- [Action 1]
- [Action 2]
```

### Template (JSON)

```json
{
  "packet_type": "AUDIT",
  "id": "AUD-YYYYMMDD-NNN",
  "created": "YYYY-MM-DDTHH:MM:SSZ",
  "execution_id": "EXE-YYYYMMDD-NNN",
  "plan_id": "PLN-YYYYMMDD-NNN",
  "criteria_results": [
    {
      "criterion": "From plan",
      "expected": "Expected outcome",
      "actual": "What happened",
      "result": "PASS"
    }
  ],
  "drift_analysis": "How execution differed",
  "recommendation": "accept",
  "follow_up_actions": ["Action 1"]
}
```

### Acceptance Criteria for Audit
- [ ] References both execution and plan
- [ ] Each criterion from plan is evaluated
- [ ] Clear ACCEPT/REJECT/REVISE recommendation
- [ ] Rationale provided

---

## VI. CONTINUATION PACKET

**Purpose**: Enable session deletion by capturing all state needed to continue.

### Required Fields
- `id`: CONT-YYYYMMDD-NNN
- `created`: ISO 8601 timestamp
- `source`: Platform and surface
- `status`: complete/partial/blocked
- `summary`: One paragraph session summary
- `work_completed`: List of artifacts created
- `work_remaining`: List of remaining tasks
- `safe_to_delete`: Boolean

### Optional Fields
- `decisions_made`: Key decisions with rationale
- `context_for_next`: Paragraph for next session
- `files_to_load`: Files the next session should read

### Template (Markdown)

```markdown
# CONTINUATION PACKET
**ID**: CONT-YYYYMMDD-NNN
**Created**: YYYY-MM-DD HH:MM UTC
**Source**: [platform] / [surface]
**Status**: [complete|partial|blocked]

## Summary
[One paragraph summary of what this session accomplished, what decisions were made, and what the state is now]

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| [What was decided] | [Why] |
| [What was decided] | [Why] |

## Work Completed

| Artifact | Location | Description |
|----------|----------|-------------|
| [What was created] | [path/to/file] | [What it contains] |
| [What was created] | [path/to/file] | [What it contains] |

## Work Remaining

| Task | Priority | Blocked By |
|------|----------|------------|
| [What needs to be done] | [P0-P3] | [blocker or none] |
| [What needs to be done] | [P0-P3] | [blocker or none] |

## Context for Next Session
[Paragraph of context the next session needs to understand to pick up seamlessly. Include: what was the objective, what approach was taken, what's the current state, what's the next step.]

## Files to Load
- [path/to/file1.md] — [why this file is relevant]
- [path/to/file2.md] — [why this file is relevant]

## Safe to Delete?
**[YES — this packet captures all state]**

or

**[NO — reason: (e.g., "blocked on Principal decision about X")]**
```

### Template (JSON)

```json
{
  "packet_type": "CONTINUATION",
  "id": "CONT-YYYYMMDD-NNN",
  "created": "YYYY-MM-DDTHH:MM:SSZ",
  "source": {
    "platform": "claude",
    "surface": "code"
  },
  "status": "complete",
  "summary": "One paragraph summary",
  "decisions_made": [
    {
      "decision": "What was decided",
      "rationale": "Why"
    }
  ],
  "work_completed": [
    {
      "artifact": "What was created",
      "location": "path/to/file",
      "description": "What it contains"
    }
  ],
  "work_remaining": [
    {
      "task": "What needs to be done",
      "priority": "P1",
      "blocked_by": null
    }
  ],
  "context_for_next": "Paragraph of context",
  "files_to_load": ["path/to/file1.md"],
  "safe_to_delete": true
}
```

### Acceptance Criteria for Continuation
- [ ] Summary is self-contained (understandable without chat)
- [ ] All work completed has locations
- [ ] Work remaining is prioritized
- [ ] Context for next is actionable
- [ ] Safe to delete is explicitly stated with reason

---

## VII. PACKET FILING LOCATIONS

```
00-ORCHESTRATION/
├── blackboard/
│   ├── evidence/
│   │   └── EVD-YYYYMMDD-NNN.md
│   ├── plans/
│   │   └── PLN-YYYYMMDD-NNN.md
│   ├── executions/
│   │   └── EXE-YYYYMMDD-NNN.md
│   ├── audits/
│   │   └── AUD-YYYYMMDD-NNN.md
│   └── continuations/
│       └── CONT-YYYYMMDD-NNN.md
```

---

## VIII. PACKET FLOW

```
SENSING          PLANNING         EXECUTION        VERIFICATION
   │                 │                 │                 │
   ↓                 ↓                 ↓                 ↓
┌───────┐       ┌───────┐       ┌───────┐       ┌───────┐
│  EVD  │ ────→ │  PLN  │ ────→ │  EXE  │ ────→ │  AUD  │
└───────┘       └───────┘       └───────┘       └───────┘
                                                     │
                                                     ↓
                                               ┌───────────┐
                                               │   CONT    │
                                               │ (at end)  │
                                               └───────────┘
```

---

## IX. QUICK REFERENCE

### Packet ID Formats
- Evidence: `EVD-YYYYMMDD-NNN`
- Plan: `PLN-YYYYMMDD-NNN`
- Execution: `EXE-YYYYMMDD-NNN`
- Audit: `AUD-YYYYMMDD-NNN`
- Continuation: `CONT-YYYYMMDD-NNN`

### Minimum Viable Packets

**Evidence (minimum)**:
```markdown
# EVIDENCE PACKET
**ID**: EVD-20260117-001
**Created**: 2026-01-17 14:30 UTC
**Source**: gemini

## Query
[Question]

## Findings
- [Finding 1] (confidence: high)
- [Finding 2] (confidence: medium)

## Uncertainties
- [What's unclear]
```

**Plan (minimum)**:
```markdown
# PLAN PACKET
**ID**: PLN-20260117-001
**Created**: 2026-01-17 14:30 UTC

## Objective
[One sentence]

## Deliverables
- [Artifact 1] → [location]

## Acceptance Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]
```

**Execution (minimum)**:
```markdown
# EXECUTION PACKET
**ID**: EXE-20260117-001
**Created**: 2026-01-17 14:30 UTC
**Plan ID**: PLN-20260117-001
**Status**: complete

## Changes
- [file] — [action] — [summary]

## Verification
- [criterion] — PASS
```

**Continuation (minimum)**:
```markdown
# CONTINUATION PACKET
**ID**: CONT-20260117-001
**Created**: 2026-01-17 14:30 UTC
**Source**: claude / code
**Status**: complete

## Summary
[One paragraph]

## Work Completed
- [artifact] — [location]

## Work Remaining
- [task] — P1

## Safe to Delete?
YES
```

---

**Packets make conversations deletable. Use them.**
