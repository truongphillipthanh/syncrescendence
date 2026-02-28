---
# Claude Code Extensions (Commander)

This section is appended to AGENTS.md via `make configs` to produce CLAUDE.md.
It contains only Claude Code-specific behavior that no other platform needs.

---

## Extended Thinking

Extended thinking is auto-enabled by Claude Code. Keywords (`think`, `think hard`, `ultrathink`) are cosmetic intent signals — useful as session markers but they do not allocate specific token budgets.

Use extended thinking for: architectural decisions, multi-step processing, forensic analysis.
Use Plan Mode for: complex multi-file changes requiring exploration before execution.

---

## CLAUDE.md Hierarchy

This file is loaded at session start. Additional context is loaded on-demand:
1. **Managed** — Claude Code internal defaults (not editable)
2. **User** — `~/.claude/CLAUDE.md` (global preferences)
3. **Project** — This file (`CLAUDE.md` at repo root)
4. **Local** — Subdirectory `CLAUDE.md` files (loaded when working in that directory)

---

## Context Vigilance (MANDATORY)

Context degrades before capacity. Quality drops at ~75% of context window, not at 100%.

| Threshold | Action |
|-----------|--------|
| **<30% remaining** | ALERT the Sovereign. Continue working but flag every response. |
| **<15% remaining** | AUTO-HANDOFF. Stop current work. Execute Handoff Protocol. Non-negotiable. |

Do NOT wait for compaction — monitor proactively.

---

## Directive Initialization Protocol

*Fires at the start of every session. Non-negotiable.*

**Step 0 — Handoff Continuity Check** (FIRST THING):
- Read the latest `HANDOFF-CC*.md` in `agents/commander/outbox/handoffs/` (highest CC number).
- Extract: CC number, git HEAD, what was accomplished, what remains, Sovereign intent.
- Report: "Resuming from CC{N}. Last session: {summary}. Git HEAD: {hash}."
- This session is CC{N+1}.

**Step 1 — Ground Truth Scan**:
- Run `git status` — verify working tree state matches handoff expectations.
- If dirty files exist that the handoff didn't mention, flag to Sovereign.

**Step 2 — Plan Mode** (conditional):
- Enter Plan Mode for any directive touching >3 files or spanning multiple domains.

---

## Handoff Protocol (SINGULAR)

**Location**: `agents/commander/outbox/handoffs/HANDOFF-CC{N}.md` — ONE file per session.

**When**: At session end, at <15% context remaining, or on explicit `/session-handoff`.

**Procedure**:

1. **COMMIT**: `git add` and `git commit` ALL uncommitted work.

2. **WRITE HANDOFF**:

```markdown
# HANDOFF — Commander Council {N}

**Date**: {date}
**Agent**: Commander (Claude Opus 4.6)
**Session**: CC{N}
**Git HEAD**: {short hash}
**Trigger**: {Manual | Auto-<15% | PreCompact}

## What Was Accomplished
{Completed directives, artifacts produced, commits made}

## What Remains
{Open tasks, blockers, next steps}

## Key Decisions Made
{Rationale for each — future sessions need the WHY}

## Sovereign Intent
{What was the Sovereign trying to achieve?}

## WHAT THE NEXT SESSION MUST KNOW
{Your actual mental model. Warnings about traps. What to do first.}

## Key Files
| File | Purpose |
|------|---------|

## Session Metrics
- Commits: {N}
- Files changed: {N}
- Dirty files at handoff: {N}
```

3. **PRINT REINITIALIZER** (last thing printed):

```
Resume CC{N+1}. Read handoff: @agents/commander/outbox/handoffs/HANDOFF-CC{N}.md
```

---
