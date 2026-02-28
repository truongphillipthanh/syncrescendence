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

2. **KAIZEN SWEEP** (before writing the handoff — this IS the process improvement):

   **a. Seared Lessons Extraction**: Did this session produce any new lesson that future sessions must never forget? If yes, append it to `critical-lessons.md` in auto-memory. Lessons are patterns, not events — "mass-editing generated files corrupts the build" not "in CC31 we edited 29 files." If no new lesson, skip.

   **b. Config Drift Check**: Run `make configs` and verify no phantom paths crept into AGENTS.md or CLAUDE-EXT.md during the session. If any directory referenced in the config files was created, moved, or deleted this session, update the Directory Structure section and FLAT PRINCIPLE sanctioned exceptions NOW. The CC52-CC57 catastrophe (16 sessions of phantom paths) happened because nobody checked.

   **c. Memory Hygiene**: Read MEMORY.md. Is anything stale, contradictory, or missing? Does the directory structure still match? Are topic file references still valid? Fix now — not "next session." Memory is cache; if the cache is wrong, every future session inherits the error.

3. **WRITE HANDOFF**:

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

## Kaizen
- Seared lessons extracted: {yes — topic | no new lessons}
- Config drift: {clean | fixed — what changed}
- Memory hygiene: {clean | fixed — what was stale}

## Session Metrics
- Commits: {N}
- Files changed: {N}
- Dirty files at handoff: {N}
```

4. **SOVEREIGN FEEDBACK** (post-handoff, async):

The Sovereign may grade any handoff 1-5 and flag what was missing. This feedback is cumulative — patterns in low scores drive protocol evolution. Feedback lives as a comment at the bottom of the handoff file, added by the Sovereign at their discretion.

5. **PRINT REINITIALIZER** (last thing printed):

```
Resume CC{N+1}. Read handoff: @agents/commander/outbox/handoffs/HANDOFF-CC{N}.md
```

---
