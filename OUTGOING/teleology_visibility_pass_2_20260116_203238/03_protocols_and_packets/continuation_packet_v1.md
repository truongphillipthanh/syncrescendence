# Continuation Packet v1
**Generated**: 2026-01-17T04:50:00Z
**Purpose**: Template and schema for session-to-session handoff

---

## Purpose

A Continuation Packet makes any web-app conversation deletable without losing continuity. It captures the minimum viable context required to resume work in a new session.

---

## Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["id", "timestamp", "source_session", "state_snapshot", "context_files", "next_objectives"],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^CONT-[0-9]{8}-[0-9]{3}$",
      "description": "Format: CONT-YYYYMMDD-NNN"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time"
    },
    "source_session": {
      "type": "object",
      "required": ["oracle", "blitzkrieg"],
      "properties": {
        "oracle": {"type": "integer"},
        "blitzkrieg": {"type": "integer"},
        "stream": {"type": "string", "enum": ["A", "B", null]},
        "platform": {"type": "string"},
        "thread_id": {"type": "string", "description": "If available, for audit trail"}
      }
    },
    "state_snapshot": {
      "type": "object",
      "required": ["active_tasks", "pending_decisions"],
      "properties": {
        "active_tasks": {
          "type": "array",
          "items": {"type": "string"},
          "description": "Tasks that are in_progress"
        },
        "pending_decisions": {
          "type": "array",
          "items": {"type": "string"},
          "description": "Decisions awaiting Principal input"
        },
        "blocking_issues": {
          "type": "array",
          "items": {"type": "string"},
          "description": "Issues preventing progress"
        },
        "key_state_values": {
          "type": "object",
          "description": "Relevant values from system_state.json"
        }
      }
    },
    "context_files": {
      "type": "array",
      "items": {"type": "string"},
      "description": "File paths to read for context restoration"
    },
    "next_objectives": {
      "type": "array",
      "items": {"type": "string"},
      "description": "What the next session should accomplish"
    },
    "open_questions": {
      "type": "array",
      "items": {"type": "string"},
      "description": "Questions that remained unresolved"
    },
    "estimated_complexity": {
      "type": "string",
      "enum": ["routine", "moderate", "complex"],
      "description": "Expected difficulty of next session"
    }
  }
}
```

---

## Template (Markdown for Human Readability)

```markdown
# Continuation Packet: CONT-YYYYMMDD-NNN

## Source Session
- **Oracle**: N
- **Blitzkrieg**: N
- **Stream**: A/B
- **Platform**: claude_web / chatgpt / gemini
- **Date**: YYYY-MM-DD

## State Snapshot

### Active Tasks
- [ ] [Task 1 description]
- [ ] [Task 2 description]

### Pending Decisions
- [Decision 1 requiring Principal input]

### Blocking Issues
- [Issue preventing progress]

### Key State Values
```json
{
  "autonomous_cycles": N,
  "relay_cycles": N,
  "sources_processed": N
}
```

## Context Files
Load these for full context:
1. `CLAUDE.md` (always)
2. `ORACLE13_CONTEXT.md`
3. `INTERACTION_PARADIGM.md`
4. `previous_thread.md` (if exists)

## Next Objectives
1. [Primary objective]
2. [Secondary objective]
3. [Tertiary objective]

## Open Questions
- [Question 1]
- [Question 2]

## Estimated Complexity
**[routine / moderate / complex]**

Rationale: [Why this complexity level]

---

## Verification Checklist
- [ ] State snapshot matches `system_state.json`
- [ ] All context files exist and are current
- [ ] Objectives are achievable in single session
- [ ] No blocking issues require resolution first
```

---

## Usage Protocol

### When to Create
1. At end of every Oracle session
2. Before deleting any conversation with accumulated context
3. When switching between platforms mid-task
4. Before any significant break (>24 hours)

### How to Create
1. Review current session accomplishments
2. Read `system_state.json` for accurate state snapshot
3. Identify files that would be needed to resume
4. Define concrete next-session objectives
5. Note unresolved questions

### How to Use
1. New session: Load continuation packet as initial context
2. Verify state snapshot against repo state
3. If mismatch, trust repo, update packet
4. Resume from next_objectives

### Storage Location
`00-ORCHESTRATION/continuations/CONT-YYYYMMDD-NNN.json`

---

## Example

```json
{
  "id": "CONT-20260116-001",
  "timestamp": "2026-01-16T20:30:00Z",
  "source_session": {
    "oracle": 13,
    "blitzkrieg": 46,
    "stream": "A",
    "platform": "claude_web"
  },
  "state_snapshot": {
    "active_tasks": [
      "Complete teleology visibility pass 2"
    ],
    "pending_decisions": [],
    "blocking_issues": [],
    "key_state_values": {
      "autonomous_cycles": 5,
      "sources_processed": 0,
      "last_directive": "046B"
    }
  },
  "context_files": [
    "CLAUDE.md",
    "ORACLE13_CONTEXT.md",
    "INTERACTION_PARADIGM.md",
    "00-ORCHESTRATION/state/system_state.json"
  ],
  "next_objectives": [
    "Complete sections 02-08 of visibility pass 2",
    "Generate crashout forensics based on previous_thread.md",
    "Create minimal canonization sprint"
  ],
  "open_questions": [
    "Should continuation packets be JSON or Markdown?"
  ],
  "estimated_complexity": "moderate"
}
```

---

## Integration with Packet Protocol

Add to `00-ORCHESTRATION/schemas/packet_protocol.json`:

```json
{
  "continuation": {
    "id_format": "CONT-YYYYMMDD-NNN",
    "location": "00-ORCHESTRATION/continuations/",
    "producer": "any_platform",
    "consumer": "new_session",
    "required_fields": ["source_session", "state_snapshot", "context_files", "next_objectives"],
    "validation": "required"
  }
}
```
