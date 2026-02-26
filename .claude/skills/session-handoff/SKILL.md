---
name: session-handoff
description: Commander Council handoff protocol — singular procedure for session continuity
provenance: syncrescendence
vetted: 2026-02-25 (CC33 — Sovereign directive, unified protocol)
pipeline_stages: [COMMIT, UPDATE, HANDOFF, REINITIALIZE]
---

# Session Handoff — Singular Protocol (CC33)

## Authority

Sovereign directive CC33: "There should only be a singular handoff protocol."

This supersedes all prior two-path (auto/manual, floor/ceiling) architecture. There is ONE procedure.

## Location

`agents/commander/outbox/handoffs/HANDOFF-CC{N}.md`

- ONE file per session
- Sequential by CC number
- Never copied to inbox, Desktop, or anywhere else
- This is where every Claude session looks at init

## When This Fires

- Explicit `/session-handoff` invocation
- Context at <15% remaining (auto-triggered — non-negotiable)
- PreCompact hook (`cc_handoff.sh`)
- Session end

The procedure is IDENTICAL in all cases.

## Procedure

### 1. COMMIT
- `git add` and `git commit` ALL uncommitted work
- No silent work loss
- Use sandbox-safe commit (`git write-tree` → `git commit-tree` → `git update-ref`) if normal commit gets SIGKILL'd

### 2. UPDATE STATE
- Update `orchestration/state/ARCH-INTENTION_COMPASS.md` — new intentions or status changes
- Update `orchestration/state/DYN-DEFERRED_COMMITMENTS.md` — new commitments or status changes
- Update `agents/commander/memory/MEMORY.md` — durable learnings from this session

### 3. WRITE HANDOFF
Write to `agents/commander/outbox/handoffs/HANDOFF-CC{N}.md`:

```markdown
# HANDOFF — Commander Council {N}

**Date**: {ISO timestamp}
**Agent**: Commander (Claude Opus 4.6)
**Session**: CC{N}
**Git HEAD**: {short hash}
**Trigger**: {Manual | Auto-<15% | PreCompact}

## What Was Accomplished
{Completed directives, artifacts produced, commits made — be specific}

## What Remains
{Open tasks, blockers, in-progress work with specific next steps}

## Key Decisions Made
{Rationale for each — future sessions need the WHY}

## Sovereign Intent
{What was the Sovereign trying to achieve? What direction were they pushing?}

## WHAT THE NEXT SESSION MUST KNOW
{Your actual mental model. Warnings about traps. Specific first-action instructions.
Context that would be lost. NOT placeholders. NOT "[AUTO-GENERATED]" stubs.}

## Key Files
| File | Purpose |
|------|---------|

## Session Metrics
- Commits: {N}
- Files changed: {N}
- Dirty files at handoff: {N}
- DAG status: {X}/13 OPEN
- C-009: {ASKED/UNASKED}
```

### 4. PRINT REINITIALIZER
Output a paste-ready prompt as the LAST thing printed. This is what the Sovereign copies when `> claude --dangerously-skip-permissions` shows a cursor:

```
Resume CC{N}. Read handoff: @agents/commander/outbox/handoffs/HANDOFF-CC{N}.md
```

## Session Initialization (the other half)

Every Claude session begins by:
1. Reading the latest `HANDOFF-CC*.md` from `agents/commander/outbox/handoffs/` (highest CC number)
2. Confirming to Sovereign: continuing from handoff or fresh session
3. Checking `agents/commander/inbox/pending/` for tasks/confirms/results
4. This is NOT optional. Tool calls (Read) or it didn't happen. CLAUDE.md being "loaded at init" does NOT mean Claude read the handoff.

## CC Lineage

Commander Council sessions are numbered sequentially (CC26, CC27, ...). The handoff file IS the session's legacy artifact. The chain of `HANDOFF-CC{N}.md` files is the complete lineage.
