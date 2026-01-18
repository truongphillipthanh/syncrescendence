# PACKETS AND PROTOCOLS V2
## Unified Specification for Inter-Agent Communication

**Purpose**: Define standard packet formats for handoffs between platforms, sessions, and agents
**Version**: 2.0
**Generated**: 2026-01-16

---

## I. PACKET PHILOSOPHY

### Why Packets?

Packets solve the "chat deletion problem":
- Conversations are ephemeral (can be deleted anytime)
- Packets are persistent (written to repository)
- Packets are structured (can be parsed by any agent)
- Packets are self-contained (include all needed context)

### Packet Principles

1. **Self-Contained**: Any packet should be understandable without the conversation that produced it
2. **Structured**: Use JSON or structured markdown for parseability
3. **Typed**: Each packet has a defined type with known fields
4. **Timestamped**: Always include creation time
5. **Attributed**: Always include source (platform, session, agent)

---

## II. CONTINUATION PACKET

**Purpose**: Enable session deletion by capturing all state needed to continue

### Schema

```json
{
  "packet_type": "CONTINUATION",
  "id": "CONT-YYYYMMDD-NNN",
  "created": "YYYY-MM-DDTHH:MM:SSZ",
  "source": {
    "platform": "claude|chatgpt|gemini|perplexity|grok",
    "surface": "web|code|api|app",
    "session_id": "optional-session-identifier"
  },
  "status": "complete|partial|blocked",
  "summary": "One paragraph summary of session",
  "decisions_made": [
    {
      "decision": "What was decided",
      "rationale": "Why"
    }
  ],
  "work_completed": [
    {
      "artifact": "path/to/file.md",
      "description": "What it contains"
    }
  ],
  "work_remaining": [
    {
      "task": "What needs to be done",
      "priority": "P0|P1|P2|P3",
      "blocked_by": null
    }
  ],
  "context_for_next": "Paragraph of context the next session needs",
  "files_to_load": ["path/to/file1.md", "path/to/file2.md"],
  "safe_to_delete": true
}
```

### Copy/Paste Markdown Template

```markdown
# CONTINUATION PACKET
**ID**: CONT-YYYYMMDD-NNN
**Created**: YYYY-MM-DD HH:MM
**Source**: [Platform] / [Surface]
**Status**: [complete|partial|blocked]

## Summary
[One paragraph summary of session]

## Decisions Made
| Decision | Rationale |
|----------|-----------|
| [Decision 1] | [Why] |
| [Decision 2] | [Why] |

## Work Completed
| Artifact | Description |
|----------|-------------|
| [path/to/file.md] | [What it contains] |

## Work Remaining
| Task | Priority | Blocked By |
|------|----------|------------|
| [Task 1] | [P0-P3] | [blocker or none] |

## Context for Next Session
[Paragraph of context]

## Files to Load
- [path/to/file1.md]
- [path/to/file2.md]

## Safe to Delete?
[YES - this packet captures all state] or [NO - reason]
```

---

## III. CHORUS PACKET

**Purpose**: Aggregate signals from multiple platforms into unified perspective

### Schema

```json
{
  "packet_type": "CHORUS",
  "id": "CHR-YYYYMMDD-NNN",
  "created": "YYYY-MM-DDTHH:MM:SSZ",
  "query": "What was being asked/investigated",
  "perspectives": [
    {
      "platform": "claude",
      "finding": "What Claude contributed",
      "confidence": "high|medium|low"
    },
    {
      "platform": "chatgpt",
      "finding": "What ChatGPT contributed",
      "confidence": "high|medium|low"
    },
    {
      "platform": "gemini",
      "finding": "What Gemini contributed",
      "confidence": "high|medium|low"
    }
  ],
  "convergence": "Where they agree",
  "divergence": "Where they disagree",
  "synthesis": "Unified perspective after considering all",
  "recommended_action": "What to do next"
}
```

### Copy/Paste Markdown Template

```markdown
# CHORUS PACKET
**ID**: CHR-YYYYMMDD-NNN
**Created**: YYYY-MM-DD HH:MM
**Query**: [What was being investigated]

## Perspectives

### Claude
**Finding**: [What Claude contributed]
**Confidence**: [high|medium|low]

### ChatGPT
**Finding**: [What ChatGPT contributed]
**Confidence**: [high|medium|low]

### Gemini
**Finding**: [What Gemini contributed]
**Confidence**: [high|medium|low]

## Convergence (Agreement)
[Where they agree]

## Divergence (Disagreement)
[Where they disagree]

## Synthesis
[Unified perspective]

## Recommended Action
[What to do next]
```

---

## IV. SPRINT REVIEW PACKET

**Purpose**: Document what was accomplished in a work sprint

### Schema

```json
{
  "packet_type": "SPRINT_REVIEW",
  "id": "SPR-YYYYMMDD-NNN",
  "created": "YYYY-MM-DDTHH:MM:SSZ",
  "sprint": {
    "name": "Sprint/Blitzkrieg identifier",
    "start": "YYYY-MM-DD",
    "end": "YYYY-MM-DD"
  },
  "goals": [
    {
      "goal": "What was planned",
      "status": "achieved|partial|missed",
      "evidence": "How we know"
    }
  ],
  "deliverables": [
    {
      "artifact": "path/to/file.md",
      "description": "What it is"
    }
  ],
  "metrics": {
    "planned_tasks": 10,
    "completed_tasks": 8,
    "completion_rate": 0.8
  },
  "highlights": ["Key accomplishment 1", "Key accomplishment 2"],
  "blockers_encountered": ["What blocked progress"],
  "carryover": ["What moves to next sprint"]
}
```

### Copy/Paste Markdown Template

```markdown
# SPRINT REVIEW PACKET
**ID**: SPR-YYYYMMDD-NNN
**Sprint**: [Name] ([Start Date] → [End Date])
**Created**: YYYY-MM-DD HH:MM

## Goals vs Outcomes
| Goal | Status | Evidence |
|------|--------|----------|
| [Goal 1] | [achieved|partial|missed] | [How we know] |
| [Goal 2] | [achieved|partial|missed] | [How we know] |

## Deliverables
| Artifact | Description |
|----------|-------------|
| [path/to/file.md] | [What it is] |

## Metrics
- **Planned tasks**: [N]
- **Completed tasks**: [N]
- **Completion rate**: [N%]

## Highlights
- [Key accomplishment 1]
- [Key accomplishment 2]

## Blockers Encountered
- [What blocked progress]

## Carryover to Next Sprint
- [What moves forward]
```

---

## V. SPRINT RETROSPECTIVE PACKET

**Purpose**: Document learnings and process improvements

### Schema

```json
{
  "packet_type": "SPRINT_RETRO",
  "id": "RET-YYYYMMDD-NNN",
  "created": "YYYY-MM-DDTHH:MM:SSZ",
  "sprint": "Sprint identifier",
  "went_well": ["What worked"],
  "went_poorly": ["What didn't work"],
  "learned": ["Key learnings"],
  "action_items": [
    {
      "improvement": "What to change",
      "owner": "Who owns it",
      "due": "When to complete"
    }
  ],
  "patterns_observed": {
    "success_patterns": ["What to keep doing"],
    "anti_patterns": ["What to stop doing"]
  }
}
```

### Copy/Paste Markdown Template

```markdown
# SPRINT RETROSPECTIVE PACKET
**ID**: RET-YYYYMMDD-NNN
**Sprint**: [Sprint identifier]
**Created**: YYYY-MM-DD HH:MM

## What Went Well
- [Success 1]
- [Success 2]

## What Went Poorly
- [Problem 1]
- [Problem 2]

## Key Learnings
- [Learning 1]
- [Learning 2]

## Action Items
| Improvement | Owner | Due |
|-------------|-------|-----|
| [What to change] | [Who] | [When] |

## Patterns Observed

### Success Patterns (Keep Doing)
- [Pattern 1]
- [Pattern 2]

### Anti-Patterns (Stop Doing)
- [Anti-pattern 1]
- [Anti-pattern 2]
```

---

## VI. SYMBOLIC COMPRESSION SNIPPET

**Purpose**: Memorialize a decision in the minimum necessary form

### When to Use
- Recording a decision that should persist
- Adding to ARCH-INTENTION_COMPASS.md
- Updating CANON documents
- Documenting in events.jsonl

### Schema

```json
{
  "id": "DEC-YYYYMMDD-NNN",
  "decision": "What was decided (one sentence)",
  "rationale": "Why (one sentence)",
  "alternatives_considered": ["Alt 1", "Alt 2"],
  "oracle": "Oracle session number or 'N/A'",
  "status": "active|superseded|experimental",
  "supersedes": null,
  "integrated_into": ["CANON-XXXXX", "ARCH-*.md"]
}
```

### Copy/Paste Markdown Template

```markdown
### DEC-YYYYMMDD-NNN: [Decision Title]

**Decision**: [What was decided - one sentence]

**Rationale**: [Why - one sentence]

**Alternatives Considered**:
- [Alternative 1] — rejected because [reason]
- [Alternative 2] — rejected because [reason]

**Source**: Oracle [N] / Session [date]

**Status**: [active|superseded|experimental]

**Integrated Into**: [CANON-XXXXX], [ARCH-*.md]
```

### Ultra-Compact Form (for events.jsonl)

```json
{"ts":"2026-01-16T23:00:00Z","type":"decision","id":"DEC-20260116-001","decision":"Adopt Ring 7 as enabling membrane","status":"active"}
```

---

## VII. EVIDENCE PACKET (Gemini → Others)

**Purpose**: Structured findings from sensing/research

### Schema

```json
{
  "packet_type": "EVIDENCE",
  "id": "EVD-YYYYMMDD-NNN",
  "created": "YYYY-MM-DDTHH:MM:SSZ",
  "source": "gemini|perplexity",
  "query": "What was asked",
  "corpus_slice": ["file1.md", "file2.md"],
  "findings": [
    {
      "finding": "What was found",
      "source": "file:line or URL",
      "confidence": "high|medium|low"
    }
  ],
  "uncertainties": ["What we're not sure about"],
  "recommended_probe": "What to investigate next"
}
```

---

## VIII. PLAN PACKET (ChatGPT → Claude Code)

**Purpose**: Specification with acceptance criteria for execution

### Schema

```json
{
  "packet_type": "PLAN",
  "id": "PLN-YYYYMMDD-NNN",
  "created": "YYYY-MM-DDTHH:MM:SSZ",
  "objective": "What we're trying to accomplish",
  "deliverables": [
    {
      "artifact": "What will be produced",
      "location": "Where it goes",
      "format": "File type"
    }
  ],
  "acceptance_criteria": [
    {
      "criterion": "How we know it's done",
      "verification": "Command or check to run"
    }
  ],
  "stop_conditions": [
    "When to stop even if not complete"
  ],
  "tracks": [
    {
      "track": "A",
      "tasks": ["Task 1", "Task 2"],
      "parallel": true
    }
  ]
}
```

---

## IX. EXECUTION PACKET (Claude Code → Audit)

**Purpose**: Document what was executed with evidence

### Schema

```json
{
  "packet_type": "EXECUTION",
  "id": "EXE-YYYYMMDD-NNN",
  "created": "YYYY-MM-DDTHH:MM:SSZ",
  "plan_id": "PLN-YYYYMMDD-NNN",
  "status": "complete|partial|failed",
  "changes": [
    {
      "file": "path/to/file.md",
      "action": "created|modified|deleted",
      "summary": "What changed"
    }
  ],
  "verification": [
    {
      "command": "command run",
      "output": "result",
      "passed": true
    }
  ],
  "issues_encountered": ["Any problems"],
  "commits": ["commit-hash-1", "commit-hash-2"]
}
```

---

## X. AUDIT PACKET (ChatGPT → Repo)

**Purpose**: Verify execution against plan

### Schema

```json
{
  "packet_type": "AUDIT",
  "id": "AUD-YYYYMMDD-NNN",
  "created": "YYYY-MM-DDTHH:MM:SSZ",
  "execution_id": "EXE-YYYYMMDD-NNN",
  "plan_id": "PLN-YYYYMMDD-NNN",
  "criteria_results": [
    {
      "criterion": "What was checked",
      "result": "pass|fail",
      "evidence": "How we know"
    }
  ],
  "drift_analysis": "How execution differed from plan",
  "recommendation": "accept|reject|revise",
  "follow_up_actions": ["What to do next"]
}
```

---

## XI. PACKET FLOW DIAGRAM

```
┌─────────────┐     EVIDENCE      ┌─────────────┐
│   GEMINI    │ ───────────────→ │   CHATGPT   │
│  (Sensor)   │                   │  (Deviser)  │
└─────────────┘                   └──────┬──────┘
                                         │
                                    PLAN │
                                         ↓
                                  ┌─────────────┐
                                  │ CLAUDE CODE │
                                  │ (Executor)  │
                                  └──────┬──────┘
                                         │
                                   EXEC  │
                                         ↓
┌─────────────┐     AUDIT         ┌─────────────┐
│ REPOSITORY  │ ←───────────────  │   CHATGPT   │
│  (Ground)   │                   │  (Auditor)  │
└─────────────┘                   └─────────────┘
       │
       │ CONTINUATION
       ↓
[NEXT SESSION]
```

---

## XII. PROTOCOL RULES

### Rule 1: Every Significant Session Ends with a Packet
No session producing decisions or artifacts should end without at least a CONTINUATION packet.

### Rule 2: Packets Go to Repository
All packets are written to repository, not left in chat. Location: `00-ORCHESTRATION/blackboard/[type]/`

### Rule 3: Packets Reference Each Other
- EXECUTION references PLAN
- AUDIT references EXECUTION and PLAN
- CONTINUATION references all relevant packets

### Rule 4: IDs Are Unique and Parseable
Format: `[TYPE]-YYYYMMDD-NNN`
- TYPE: 3-letter code (EVD, PLN, EXE, AUD, CHR, SPR, RET, DEC, CONT)
- YYYYMMDD: Date
- NNN: Sequential number for that day

### Rule 5: Timestamps Are UTC
All `created` fields use ISO 8601 format in UTC: `YYYY-MM-DDTHH:MM:SSZ`

---

**Packets make conversations deletable. Use them.**
