# Entrypoint Recommendation
**Generated**: 2026-01-17T19:00:00
**Author**: Claude Code (Opus 4.5)
**RUN_ID**: 20260117_1900

---

## Purpose

Recommend a single "wellhead" entrypoint file that makes the repository cockpit portable across sessions, platforms, and agents.

---

## Current State

The repository currently has multiple entry points with overlapping concerns:

| File | Purpose | Limitation |
|------|---------|------------|
| `CLAUDE.md` | Claude Code constitutional rules | Claude-specific; not portable to other agents |
| `00-ORCHESTRATION/state/README.md` | State directory docs | Too narrow; only covers state/ |
| `CANON-00013-QUICKSTART-cosmos.md` | Canon quickstart | Canon-focused; not operational |
| Various Oracle contexts | Session continuity | Session-specific; not universal |

**Problem**: No single file provides a portable cockpit for any agent arriving fresh.

---

## Recommendation

### Single Wellhead: `00-ORCHESTRATION/COCKPIT.md`

**Rationale**:
1. Located in orchestration layer (appropriate for operational guidance)
2. Not agent-specific (unlike CLAUDE.md)
3. Can reference all other entrypoints
4. Serves as "you are here" for any agent or operator

---

## Proposed Content

```markdown
# COCKPIT — Syncrescendence Operational Entrypoint
**Version**: 1.0.0
**Last Updated**: 2026-01-17

## You Are Here

This is Syncrescendence, a civilizational sensing infrastructure demonstrating AI-amplified individual capability at institutional scale.

## Quick Orientation

### What This Repository Contains
- **01-CANON/**: Verified canonical knowledge (79 documents, ~61K lines)
- **00-ORCHESTRATION/**: Strategic coordination (directives, state, scripts)
- **02-ENGINE/**: Functions, prompts, model profiles
- **03-QUEUE/**: Pending items by modal
- **04-SOURCES/**: Source documents (raw and processed)
- **05-MEMORY/**: Historical preservation
- **06-EXEMPLA/**: Templates and examples
- **OUTGOING/**: Pass outputs and exports

### Protected Zones (Do Not Modify Without Approval)
- `01-CANON/` — All canonical knowledge
- `00-ORCHESTRATION/state/` — Living infrastructure

### Current State Vector
- **Active Oracle**: See `00-ORCHESTRATION/oracle_contexts/` for latest
- **Active Directive**: Check `00-ORCHESTRATION/state/tasks.csv` for current work
- **System State**: `00-ORCHESTRATION/state/system_state.json`

## Agent-Specific Entrypoints

| Agent | Entrypoint | Purpose |
|-------|------------|---------|
| Claude Code | `CLAUDE.md` | Constitutional rules for Claude sessions |
| Other LLMs | This file | Universal operational guidance |
| Human Operator | This file + `00-ORCHESTRATION/state/DYN-DASHBOARD.md` | Status overview |

## Key Reference Documents

| Document | Location | Purpose |
|----------|----------|---------|
| 18 Evaluative Lenses | `00-ORCHESTRATION/state/REF-STANDARDS.md` | Decision framework |
| Processing Pattern | `00-ORCHESTRATION/state/REF-PROCESSING_PATTERN.md` | Source intake methodology |
| Canon Schema | `01-CANON/CANON-00000-SCHEMA-cosmos.md` | Canon structure definition |
| Quickstart | `01-CANON/CANON-00013-QUICKSTART-cosmos.md` | Conceptual orientation |

## Operational Commands

```bash
make verify        # Run all validation checks
make tree          # Generate current tree
make sync          # Pull latest, rebase, push
```

## Session Continuity

If resuming work:
1. Check `00-ORCHESTRATION/state/tasks.csv` for active tasks
2. Review latest Oracle context in `00-ORCHESTRATION/oracle_contexts/`
3. Check `00-ORCHESTRATION/state/events.jsonl` for recent events

## Anti-Patterns

- Creating subdirectories anywhere
- Modifying state/ without validation
- Skipping verification before completion claims
- Treating Canon as editable without Principal approval

## Need Help?

- **Understanding the system**: Start with `01-CANON/CANON-00013-QUICKSTART-cosmos.md`
- **Current work status**: Check `00-ORCHESTRATION/state/DYN-DASHBOARD.md`
- **Decision history**: See `00-ORCHESTRATION/state/ARCH-ORACLE_DECISIONS.md`
```

---

## Implementation

### Option A: Create New File (Recommended)

**Path**: `00-ORCHESTRATION/COCKPIT.md`

**Advantages**:
- Clean separation from agent-specific CLAUDE.md
- Located in orchestration layer
- Can evolve independently

**Command**:
```bash
# Create file with content above
# Then add to git
git add 00-ORCHESTRATION/COCKPIT.md
git commit -m "feat(orchestration): add universal COCKPIT entrypoint"
```

### Option B: Enhance CLAUDE.md

**Not Recommended** because:
- CLAUDE.md is agent-specific
- Would require maintaining both universal and Claude-specific content
- Other agents might skip it due to name

### Option C: Use Canon Quickstart

**Not Recommended** because:
- Canon is for knowledge, not operations
- Quickstart is conceptual, not operational
- Would mix concerns

---

## Portability Features

The recommended COCKPIT.md ensures portability by:

1. **No Agent Assumptions**: Works for Claude, GPT, Gemini, human operators
2. **Self-Contained Orientation**: New arrival can understand structure in <2 minutes
3. **Reference Links**: Points to deeper resources without duplicating them
4. **State Awareness**: Directs to current state vector
5. **Anti-Pattern Documentation**: Prevents common mistakes

---

## Relationship to CLAUDE.md

```
COCKPIT.md (Universal)
    │
    ├── Provides: General orientation, structure, references
    │
    └── References: CLAUDE.md for Claude-specific rules

CLAUDE.md (Claude-Specific)
    │
    ├── Provides: Constitutional rules, extended thinking triggers
    │
    └── Assumes: Reader is Claude Code agent
```

Both files should exist. CLAUDE.md remains the Claude-specific entrypoint. COCKPIT.md becomes the universal wellhead.

---

## Summary

| Aspect | Recommendation |
|--------|----------------|
| File | `00-ORCHESTRATION/COCKPIT.md` |
| Purpose | Universal operational entrypoint |
| Content | Structure overview, state pointers, key references |
| Relationship | Complements (not replaces) CLAUDE.md |
| Portability | Works for any agent or human operator |
