# Blitzkrieg Protocol
## Parallel Directive Execution Framework

**Version**: 1.0.0
**Created**: 2026-01-18
**Authority**: Oracle13
**Status**: SUPERSEDED by Neo-Blitzkrieg (see REF-ROSETTA_STONE.md entry #14)
**Note**: This v1.0 Lane A/B/C model is superseded by the full constellation pipeline defined in the Neo-Blitzkrieg. Preserved as historical reference.

---

## Overview

Blitzkrieg is a structured parallel execution pattern for Claude Code directives. It enables the Sovereign to issue multiple concurrent task streams, each targeting a specific model with explicit success criteria, and produces canonical artifacts suitable for cross-platform continuation.

---

## Core Concepts

### What is a Blitzkrieg?

A blitzkrieg is a bounded execution burst consisting of:
1. **Context** — Shared situational awareness for all directives
2. **Directives** — Parallel task specifications with model targeting
3. **Execution Log** — Auditable record of what was attempted, completed, and deferred

### When to Use Blitzkrieg

- Multiple independent tasks can be parallelized
- Work needs to span multiple Claude Code sessions
- Cross-platform handoff is required (e.g., Claude Code → ChatGPT)
- Audit trail is important

---

## Artifact Specifications

### 1. Context (`context.md`)

The shared context document provides situational awareness for all directives.

**Location**: `-INBOX/blitzkrieg_drop/context.md` (dropbox) → `-OUTGOING/${DATE}-blitzkrieg/01_context/context.md` (archived)

**Required Sections**:
```markdown
# Blitzkrieg Context

## Session Identity
- Oracle: [N]
- Blitzkrieg ID: [YYYYMMDD-NN]
- Sovereign Intent: [1-2 sentences]

## Repository State
- Branch: [current branch]
- Recent commits: [last 3-5 relevant]
- Active concerns: [blockers, risks]

## Shared Constraints
- [List any constraints all directives must respect]

## Cross-References
- [Links to relevant CANON, directives, or external resources]
```

### 2. Directives (`directive-NN.md`)

Individual task specifications with required metadata headers.

**Location**: `-INBOX/blitzkrieg_drop/directive-*.md` (dropbox) → `-OUTGOING/${DATE}-blitzkrieg/02_directives/` (archived)

**Required Headers** (must appear at top of file):
```markdown
---
BLITZKRIEG_DIRECTIVE_ID: DIRECTIVE-XXXN
TARGET_MODEL: opus-4.5 | sonnet-4.5 | haiku
RATIONALE: [Why this model for this task]
SUCCESS_CRITERIA: [Measurable completion conditions]
---
```

**Valid TARGET_MODEL Values**:
| Model | When to Use |
|-------|-------------|
| `opus-4.5` | Architectural decisions, complex synthesis, strategic reasoning |
| `sonnet-4.5` | Well-defined execution, moderate complexity, cost-effective |
| `haiku` | Simple lookups, quick validations, high-volume low-complexity |

**Body Structure**:
```markdown
## Objective
[What this directive aims to accomplish]

## Scope
[Boundaries — what IS and IS NOT in scope]

## Approach
[Suggested implementation path]

## Deliverables
[Concrete outputs expected]

## Dependencies
[Other directives this depends on, or provides to]
```

### 3. Execution Log (`execution_log.md`)

Generated record of blitzkrieg execution, designed for "select all + copy" into ChatGPT.

**Location**: `-OUTGOING/${DATE}-blitzkrieg/03_execution/execution_log.md`

**Generated Structure**:
```markdown
# Blitzkrieg Execution Log

**Generated**: YYYY-MM-DD HH:MM:SS
**Git HEAD**: [commit hash]
**Blitzkrieg ID**: YYYYMMDD-blitzkrieg[-NN]

## Repository State

```
[git status summary]
```

## Directives Processed

| Directive | Target Model | Rationale | Status |
|-----------|--------------|-----------|--------|
| DIRECTIVE-XXX | opus-4.5 | [extracted] | pending |
| DIRECTIVE-YYY | sonnet-4.5 | [extracted] | pending |

## What Changed

[Summary of changes made during this blitzkrieg]

## What Remains

[Open items, incomplete work]

## Next Actions

[Prioritized list of follow-up tasks]

## Attachments to Carry Forward

[Files or artifacts that must accompany continuation]
```

### 4. Execution Log JSON (`execution_log.json`)

Structured variant compatible with orchestration packet protocol.

**Location**: `-OUTGOING/${DATE}-blitzkrieg/03_execution/execution_log.json`

**Schema**:
```json
{
  "type": "blitzkrieg_execution",
  "version": "1.0.0",
  "generated": "ISO8601 timestamp",
  "git_head": "commit hash",
  "blitzkrieg_id": "YYYYMMDD-blitzkrieg[-NN]",
  "directives": [
    {
      "id": "DIRECTIVE-XXX",
      "target_model": "opus-4.5",
      "rationale": "...",
      "success_criteria": "...",
      "status": "pending|in_progress|completed|blocked"
    }
  ],
  "summary": {
    "what_changed": "...",
    "what_remains": "...",
    "next_actions": ["..."],
    "attachments": ["..."]
  }
}
```

---

## Workflow

### Phase 1: Preparation (Operator)

1. Create dropbox: `mkdir -p -INBOX/blitzkrieg_drop/`
2. Write `context.md` with session state
3. Write `directive-01.md`, `directive-02.md`, etc. with required headers
4. Validate headers are present and correctly formatted

### Phase 2: Finalization (Claude Code)

Run `/project:blitzkrieg_finalize` which:
1. Validates dropbox contents
2. Creates timestamped output folder
3. Copies context and directives
4. Generates execution logs (md + json)

### Phase 3: Execution (Claude Code)

For each directive:
1. Open directive in appropriate model context
2. Execute per specifications
3. Mark status in execution log
4. Commit changes with directive reference

### Phase 4: Archival

The finalized blitzkrieg folder in `-OUTGOING/` becomes the permanent record.
Reference it in subsequent `/deviser_reint` exports via session archaeology.

---

## Naming Conventions

| Item | Pattern | Example |
|------|---------|---------|
| Blitzkrieg folder | `${DATE}-blitzkrieg[-NN]` | `20260118-blitzkrieg`, `20260118-blitzkrieg-02` |
| Directive file | `directive-NN.md` | `directive-01.md`, `directive-02.md` |
| Directive ID header | `DIRECTIVE-XXXN` | `DIRECTIVE-047A`, `DIRECTIVE-047B` |

---

## Integration with /deviser_reint

The `/deviser_reint` command generates session continuity exports. Blitzkriegs complement this by:

1. **Session Archaeology**: `/deviser_reint` should reference the latest blitzkrieg folder in its `session_archaeology.md`
2. **Artifact Manifest**: Blitzkrieg execution logs can be listed in the artifacts manifest
3. **Ground Truth**: Both commands write to `-OUTGOING/` with dated folders

**Recommended Workflow**:
1. Run blitzkrieg execution
2. Complete directives
3. Run `/deviser_reint` to capture full session state (including blitzkrieg references)

---

## Validation Rules

The structural validator enforces:
- `-INBOX/blitzkrieg_drop/` is permitted (transient dropbox)
- No legacy `OUTGOING/` or lowercase `outgoing/` at root
- Blitzkrieg output folders must be in `-OUTGOING/`

---

## Error Handling

### Missing Context
```
ERROR: -INBOX/blitzkrieg_drop/context.md not found.
Create this file with session context before running blitzkrieg_finalize.
```

### Missing Directives
```
ERROR: No directive-*.md files found in -INBOX/blitzkrieg_drop/.
Create at least one directive file (e.g., directive-01.md) with required headers.
```

### Invalid Headers
```
ERROR: directive-01.md missing required header: TARGET_MODEL
Required headers: BLITZKRIEG_DIRECTIVE_ID, TARGET_MODEL, RATIONALE, SUCCESS_CRITERIA
```

---

## Quick Reference

### Commands

| Command | Purpose |
|---------|---------|
| `/project:blitzkrieg_finalize` | Process dropbox and generate execution artifacts |
| `./00-ORCHESTRATION/scripts/blitzkrieg_finalize.sh` | Shell script equivalent |

### Locations

| Item | Path |
|------|------|
| Dropbox | `-INBOX/blitzkrieg_drop/` |
| Output | `-OUTGOING/${DATE}-blitzkrieg[-NN]/` |
| Protocol doc | `02-ENGINE/BLITZKRIEG_PROTOCOL.md` |

### Required Headers

```yaml
BLITZKRIEG_DIRECTIVE_ID: DIRECTIVE-XXXN
TARGET_MODEL: opus-4.5 | sonnet-4.5 | haiku
RATIONALE: [Why this model]
SUCCESS_CRITERIA: [Completion conditions]
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-18 | Initial protocol formalization |

---

*This document is an operational reference. Modifications require Oracle approval.*
