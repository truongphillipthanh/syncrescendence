---
name: session-handoff
description: Commander Council handoff protocol — ensures bulletproof state persistence and CC lineage continuity at session end or compaction
wraps: session-handoff (vibeship)
provenance: vibeship (MIT), upgraded CC27
vetted: 2026-02-24
pipeline_stages: [COMMIT, MEMORY]
---

# Session Handoff — Commander Council Edition

## Overview

This skill defines the terminal node protocol for Commander Council (CC) sessions. It fires at session end, compaction, or explicit `/session-handoff` invocation. The goal: the next session loads cold and knows exactly where to pick up.

**Two paths exist:**
1. **Automated (floor)**: `cc_handoff.sh` fires on PreCompact hook. Gathers git state, inbox, journal, deferred commitments, priorities. Writes a structured handoff file. This is the MINIMUM.
2. **Manual (ceiling)**: The agent invokes `/session-handoff` and produces a RICHER handoff with actual context, reasoning, and in-progress thought.

## CC Lineage

Commander Council sessions are numbered sequentially (CC26, CC27, ...). The handoff file is the session's legacy artifact.

- Automated handoffs: `agents/commander/outbox/HANDOFF-CC{N}-AUTOCOMPACT-{timestamp}.md`
- Manual handoffs: `agents/commander/outbox/HANDOFF-CC{N}-{TOPIC}-SESSION_TERMINAL.md`
- The latest CC number is determined from `ls agents/commander/outbox/HANDOFF-CC*` — extract highest number.

## Manual Invocation Protocol (`/session-handoff`)

When the agent explicitly runs this skill, produce a handoff that is RICHER than the automated floor:

### 1. COMMIT Stage (final)
- Run `git status`. Any uncommitted work must be committed or explicitly stashed with a note. No silent work loss.
- Use sandbox-safe commit: `git write-tree` -> `git commit-tree` -> `git update-ref` (git commit gets SIGKILL'd on large repos).

### 2. MEMORY Stage (final)
Write a handoff file to `agents/commander/outbox/HANDOFF-CC{N}-{TOPIC}-SESSION_TERMINAL.md` containing:

#### Required Sections
- **Header**: Date, Agent, Session (CC number), Git HEAD, Trust Level, Trigger (Manual/PreCompact)
- **What Was Accomplished**: Completed directives, artifacts produced, commits made
- **What Remains**: Open tasks, blockers, in-progress work with specific next steps
- **Key Decisions Made**: Rationale for each — future sessions need the WHY
- **State Changes**: Anything the next session must know that changed this session
- **WHAT THE NEXT SESSION MUST KNOW**: Fill this with ACTUAL context. Not placeholders. What were you thinking? What was the Sovereign's intent? What gotchas did you discover? What would you do differently?
- **Key Files**: Table of files critical to resuming work
- **Deferred Commitments**: Any new items added or status changes

#### The "WHAT THE NEXT SESSION MUST KNOW" Section
This is the most important section. The automated handoff writes placeholders here. When you invoke `/session-handoff` manually, you MUST fill this with:
- Your actual mental model of the current state
- Warnings about traps or dead ends you discovered
- The Sovereign's most recent intent/direction
- Specific instructions for what to do first
- Any context that would be lost to compaction

### 3. Pedigree Chain
The handoff artifact feeds the pedigree system, creating traceable lineage from session to session.

### 4. Copy to Desktop
Copy the handoff to `~/Desktop/HANDOFF-LATEST.md` for quick Sovereign access.

### 5. Kaizen
Every handoff should end with a brief note on what could be improved about the handoff FORMAT itself. This is how the protocol evolves:
```
## Kaizen (Handoff Format Improvement)
- [observation about what was hard to capture or would help the next session]
```

## Automated Path Reference

The `cc_handoff.sh` script (`orchestration/00-ORCHESTRATION/scripts/cc_handoff.sh`) fires automatically on PreCompact. It:
1. Determines current CC number from latest handoff file
2. Gathers: git log/status/HEAD, autonomy ledger, session state brief, deferred commitments, inbox items, pending tasks, journal entries
3. Writes structured handoff to `agents/commander/outbox/`
4. Copies to `~/Desktop/HANDOFF-LATEST.md`
5. Commits via sandbox-safe git method

The automated handoff is the FLOOR. Manual `/session-handoff` is the CEILING.

## Agent Scope

- **Commander**: CC lineage handoffs (this protocol), dispatch queue status, plan state
- **Cartographer**: Updated dependency graphs or architecture maps
- **All agents**: Session ID, timestamp, agent identity, completed items, pending items, blockers

## Config Notes

- Handoff files live in `agents/<agent>/outbox/`
- PreCompact hook in `~/.claude/settings.json` fires `cc_handoff.sh` BEFORE `pre_compaction.sh`
- Desktop copy enables Sovereign to relay handoff context to next session without repo navigation
