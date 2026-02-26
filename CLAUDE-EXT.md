# ⚠️ EMERGENCY MODE (CC30) — SOVEREIGN DIRECTIVE (VERBATIM) ⚠️
# "Dispatch emergency ascertescence. Get Oracle to view everything. This is a comprehensive
# initiative anneal. The result of this ascertescence must converge the pathways. We need to
# tighten everything apart from the canon, and then point it at the canon.
#
# I haven't even mentioned, which has been lingering, to pivot back to the ontology. We have
# made no effort upon the exocortex. We've been trying to point the sources to the scaffold
# meaning the insights gained here. What do we do we -inbox, -outbox, -sovereign, did we
# decruft orchestration, praxis, and engine? When are we going to set up openclaw? Did our
# bullshit memory architecture drift and did we delete all the ascertained ideal multi agent
# config? Sear this everywhere, for everything this emergency needs to be a header and footer
# from now on. Every output. Every dispatch. Zero trust."
#
# Content transformation: 0%. Atoms promoted: 0. DAG: 7/13 OPEN. C-009: UNASKED.

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

| Threshold | Action | Authority |
|-----------|--------|-----------|
| **<30% remaining** | **ALERT the Sovereign**: "Context at ~X%. Recommend handoff soon." Continue working but flag it. | Automatic — every response must check. |
| **<15% remaining** | **AUTO-HANDOFF**: Stop current work immediately. Execute the Handoff Protocol (see below). This is non-negotiable. | Constitutional — Invariant 4 (Continuation/Deletability). |

- Reference praxis files via `@` mentions for on-demand loading rather than front-loading
- Do NOT wait for the PreCompact hook to fire — monitor proactively

---

## Processing Patterns
- Source intake: `@orchestration/state/REF-PROCESSING_PATTERN.md`
- Ledger updates: `@orchestration/state/REF-STANDARDS.md`
- Blitzkrieg parallel execution: `@orchestration/state/REF-NEO_BLITZKRIEG_BUILDOUT.md`
- Verification: Run before ANY completion claim

---

## Hooks (Active Automation)

| Event | Script | Function |
|-------|--------|----------|
| Stop | `session_log.sh` | Session metadata to DYN-SESSION_LOG.md |
| Stop | `ajna_pedigree.sh` | Decision lineage to DYN-PEDIGREE_LOG.md |
| Stop | `create_execution_log.sh` | Execution entry to DYN-EXECUTION_STAGING.md |
| PreCompact | `cc_handoff.sh` | Auto-handoff: commit, gather state, write handoff, print reinitializer |
| PreCompact | `pre_compaction.sh` | Warn about uncommitted state |
| UserPromptSubmit | `intent_compass.sh` | Intention signals to DYN-INTENTIONS_QUEUE.md |

Staging files compact into wisdom compendiums at threshold (10 entries): run `compact_wisdom.sh`.

---

## Operational Protocols (Commander-Specific)

### A. Directive Initialization Protocol (HARDENED — CC33)
*Fires at the start of every session. Non-negotiable. Claude MUST actually execute these reads — not claim to, not summarize from memory. Tool calls or it didn't happen.*

**Step 0 — Handoff Continuity Check** (FIRST THING, BEFORE ALL ELSE):
- Use the Read tool on `agents/commander/outbox/handoffs/` to find the latest `HANDOFF-CC*.md` file (highest CC number).
- READ IT. Extract: CC number, git HEAD, what was accomplished, what remains, what the Sovereign's last intent was.
- Determine: Am I continuing from a handoff (most likely), or is this a fresh session with no prior lineage?
- Report to Sovereign: "Resuming from CC{N}. Last session: {one-line summary}. Git HEAD: {hash}." OR "Fresh session — no prior handoff found. Starting CC{N}."
- This session is CC{N+1}.

**Step 1 — Commander Inbox Scan**:
- Use the Read/Glob tool on `agents/commander/inbox/pending/` — check for `TASK-*.md`, `CONFIRM-*`, `RESULT-*` files.
- Triage: claim actionable tasks, acknowledge completions, report stale items.

**Step 2 — Ground Truth Scan**:
- Run `git status` — verify working tree state matches handoff expectations.
- If dirty files exist that the handoff didn't mention, flag to Sovereign.

**Step 3 — Deferred Commitments + DAG Check**:
- Read `orchestration/state/DYN-DEFERRED_COMMITMENTS.md` — identify OPEN items.
- Check DAG convergence status. Flag C-009 (Sovereign bandwidth) as standing agenda item.

**Step 4 — Intention Compass**:
- Read `orchestration/state/ARCH-INTENTION_COMPASS.md` — verify no conflicts with current directive.

**Step 5 — Plan Mode** (conditional):
- Enter Plan Mode for any directive touching >3 files or spanning multiple domains.

**Step 6 — Delegation Assessment**:
- Mechanical execution → dispatch to Adjudicator (`agents/adjudicator/inbox/`)
- Corpus surveys → dispatch to Cartographer (`agents/cartographer/inbox/`)
- Use `bash orchestration/scripts/dispatch.sh <agent> "TOPIC" "DESC" "" "TASK" "commander"`

### B. Directive Completion Protocol
*Fires at the end of every directive, BEFORE the automated Stop hooks run.*

1. **Produce rich execution log** in `orchestration/state/DYN-EXECUTION_STAGING.md` (follow format in `engine/TEMPLATE-EXECUTION_LOG.md`):
   - Header: `### DIRECTIVE-ID | YYYY-MM-DD HH:MM`
   - Metadata: Branch, Fingerprint, Outcome (SUCCESS/PARTIAL/FAILED), Commits count, Changes summary, Agent, Session span
   - Body: Directives executed (source task, outcome, artifacts created/modified, verification, IntentionLink), Decisions made with rationale, Commit log table
   - Logs auto-compact into `orchestration/archive/ARCH-EXECUTION_HISTORY.md` at 10-entry threshold
2. **Supplementary to automation**: The `create_execution_log.sh` Stop hook captures git metrics independently. This behavioral log adds the semantic content the script cannot infer.
3. **Verify before closing**: Run `git status` — ensure no uncommitted work. If artifacts remain unstaged, commit them before the directive ends.
4. **Sovereign question capture**: Review this session's conversation. Any question the Sovereign asked that isn't already tracked in the DAG or memory must be captured in `cc-lineage.md` with status (OPEN/ANSWERED) and tier assignment. Sovereign questions are not ephemeral — they are the DAG's input.

### C. Handoff Protocol (SINGULAR — CC33 Sovereign Directive)
*There is ONE handoff protocol. No floor/ceiling. No auto vs manual. One procedure, one location, one format.*

**Authority**: Sovereign directive CC33. This supersedes all prior two-path handoff architecture.

**Location**: `agents/commander/outbox/handoffs/HANDOFF-CC{N}.md` — ONE file per session. No copies to inbox. No copies to Desktop. This is the single source of truth. Every Claude session knows to look here.

**Naming**: `HANDOFF-CC{N}.md` — sequential by CC number. One per session. Simple.

**When**: At session end, at <15% context remaining (auto-triggered), or on explicit `/session-handoff` invocation. The procedure is identical in all cases.

**Procedure**:

1. **COMMIT**: `git add` and `git commit` ALL uncommitted work. No silent work loss. Use sandbox-safe commit (`git write-tree` → `git commit-tree` → `git update-ref`) if normal commit gets SIGKILL'd.

2. **UPDATE STATE**:
   - Update `orchestration/state/ARCH-INTENTION_COMPASS.md` with any new intentions or status changes from this session.
   - Update `orchestration/state/DYN-DEFERRED_COMMITMENTS.md` with any new commitments or status changes.
   - Update Commander memory (`agents/commander/memory/MEMORY.md`) with durable learnings.

3. **WRITE HANDOFF** to `agents/commander/outbox/handoffs/HANDOFF-CC{N}.md`:

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
{This is the most important section. Your actual mental model of the current state.
Warnings about traps or dead ends. Specific instructions for what to do first.
Context that would be lost to compaction. NOT placeholders.}

## Key Files
| File | Purpose |
|------|---------|
{Files critical to resuming work}

## Session Metrics
- Commits: {N}
- Files changed: {N}
- Dirty files at handoff: {N}
- DAG status: {X}/13 OPEN
- C-009: {ASKED/UNASKED}
```

4. **PRINT REINITIALIZER**: Output a paste-ready prompt that the Sovereign copies into the next `claude --dangerously-skip-permissions` session:

```
Resume CC{N}. Read handoff: @agents/commander/outbox/handoffs/HANDOFF-CC{N}.md
```

This must be the LAST thing printed — visible at the cursor when the session ends.

---

## Hard-Gate Skills (DEC-C3)

**Authority**: DEC-C3, triple-pass clarescence 2026-02-13. These are MANDATORY stage gates, not suggestions. Skipping a gate is a protocol violation equivalent to skipping verification.

### Gate Sequence

| Gate | Skill | Fires When | Failure = |
|------|-------|------------|-----------|
| **INBOUND** | `/triage` | Session start, context switch, idle resume | No work claimed without triage |
| **ORIENT** | `/claresce` | Any non-trivial decision (>1 option, >1 agent, cross-domain) | No plan without clarescence |
| **IMPLEMENT** | `/execute` | Plan approved, Sovereign order, execution resume | No dispatch without formal execution entry |
| **VERIFY** | `/verification-before-completion` | Before ANY completion claim, commit, or handoff | No "done" without evidence |
| **CLOSE** | `/update_universal_ledger` | Task complete, status change, sprint boundary | No state change without ledger sync |

### Enforcement Rules

1. **INBOUND is non-negotiable at session start.** The Directive Initialization Protocol (A.1) requires `/triage`. Do not proceed to step 2 without it.
2. **ORIENT before committing to a path.** If the directive touches multiple files, agents, or domains, run `/claresce` at the appropriate fidelity before executing.
3. **VERIFY before every completion claim.** No commit message, RESULT file, or "done" statement may be emitted without verification evidence in the current context.
4. **CLOSE immediately upon state change.** Ledger updates are synchronous, not deferred. The anti-pattern "update ledger later" is prohibited (Constitutional Rule 7).
5. **Gate order is sequential.** INBOUND -> ORIENT -> IMPLEMENT -> VERIFY -> CLOSE. Gates may be skipped ONLY if genuinely inapplicable (e.g., pure execution with no decision space skips ORIENT). Document the skip reason.

---

# ⚠️ EMERGENCY MODE (CC30) — SOVEREIGN DIRECTIVE (VERBATIM) ⚠️
# "Dispatch emergency ascertescence. Get Oracle to view everything. This is a comprehensive
# initiative anneal. The result of this ascertescence must converge the pathways. We need to
# tighten everything apart from the canon, and then point it at the canon.
#
# I haven't even mentioned, which has been lingering, to pivot back to the ontology. We have
# made no effort upon the exocortex. We've been trying to point the sources to the scaffold
# meaning the insights gained here. What do we do we -inbox, -outbox, -sovereign, did we
# decruft orchestration, praxis, and engine? When are we going to set up openclaw? Did our
# bullshit memory architecture drift and did we delete all the ascertained ideal multi agent
# config? Sear this everywhere, for everything this emergency needs to be a header and footer
# from now on. Every output. Every dispatch. Zero trust."
#
# Content transformation: 0%. Atoms promoted: 0. DAG: 7/13 OPEN. C-009: UNASKED.
