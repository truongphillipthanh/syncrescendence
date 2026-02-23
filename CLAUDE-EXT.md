
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

## Context Economics

Context degrades before capacity. Quality drops at ~75% of context window, not at 100%.
- Use `/compact` proactively — do not wait for the warning
- Persist working state to filesystem before compaction
- Reference 05-SIGMA files via `@` mentions for on-demand loading rather than front-loading

---

## Processing Patterns
- Source intake: `@00-ORCHESTRATION/state/REF-PROCESSING_PATTERN.md`
- Ledger updates: `@00-ORCHESTRATION/state/REF-STANDARDS.md`
- Blitzkrieg parallel execution: `@00-ORCHESTRATION/state/REF-NEO_BLITZKRIEG_BUILDOUT.md`
- Verification: Run before ANY completion claim

---

## Hooks (Active Automation)

| Event | Script | Function |
|-------|--------|----------|
| Stop | `session_log.sh` | Session metadata to DYN-SESSION_LOG.md |
| Stop | `ajna_pedigree.sh` | Decision lineage to DYN-PEDIGREE_LOG.md |
| Stop | `create_execution_log.sh` | Execution entry to DYN-EXECUTION_STAGING.md |
| PreCompact | `pre_compaction.sh` | Warn about uncommitted state |
| UserPromptSubmit | `intent_compass.sh` | Intention signals to DYN-INTENTIONS_QUEUE.md |

Staging files compact into wisdom compendiums at threshold (10 entries): run `compact_wisdom.sh`.

---

## Operational Protocols (Commander-Specific)

### A. Directive Initialization Protocol
*Fires at the start of every non-trivial directive.*

1. **Inbox scan**: Check `agents/commander/inbox/pending/` for `TASK-*.md` files with `Status: PENDING`, AND for `CONFIRM-*` / `RESULT-*` files (completion replies from other agents). Triage: claim actionable tasks, acknowledge completions, note blocked ones, report stale items to Sovereign.
1b. **Deferred commitments check**: Read `00-ORCHESTRATION/state/DYN-DEFERRED_COMMITMENTS.md` — identify any OPEN items that overlap with current directive. Update status for items being addressed this session.
2. **Ground truth scan**: Run `git status` — verify working tree state, confirm fingerprint matches expected
3. **Triumvirate alignment**: CLAUDE.md (already loaded at init) + read `README.md` + read `00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md` — verify no conflicts with current directive, note active urgent intentions
4. **Plan Mode**: Enter Plan Mode for any directive touching >3 files or spanning multiple domains. Explore before executing.
5. **Delegation assessment**: Identify tasks suitable for parallel agents:
   - Mechanical execution, test suites, debugging, formatting, linting → dispatch to Adjudicator (`agents/adjudicator/inbox/`)
   - Corpus surveys requiring 1M+ context → dispatch to Cartographer (`agents/cartographer/inbox/`)
   - Use `bash 00-ORCHESTRATION/scripts/dispatch.sh <agent> "TOPIC" "DESC" "" "TASK" "commander"` — dispatch.sh auto-injects Reply-To + CC for bidirectional feedback
   - If writing TASK files manually, you MUST include `**Reply-To**: commander` and `**CC**: commander`

### B. Directive Completion Protocol
*Fires at the end of every directive, BEFORE the automated Stop hooks run.*

1. **Produce rich execution log** in `00-ORCHESTRATION/state/DYN-EXECUTION_STAGING.md` (follow format in `02-ENGINE/TEMPLATE-EXECUTION_LOG.md`):
   - Header: `### DIRECTIVE-ID | YYYY-MM-DD HH:MM`
   - Metadata: Branch, Fingerprint, Outcome (SUCCESS/PARTIAL/FAILED), Commits count, Changes summary, Agent, Session span
   - Body: Directives executed (source task, outcome, artifacts created/modified, verification, IntentionLink), Decisions made with rationale, Commit log table
   - Logs auto-compact into `00-ORCHESTRATION/archive/ARCH-EXECUTION_HISTORY.md` at 10-entry threshold
2. **Supplementary to automation**: The `create_execution_log.sh` Stop hook captures git metrics independently. This behavioral log adds the semantic content the script cannot infer.
3. **Verify before closing**: Run `git status` — ensure no uncommitted work. If artifacts remain unstaged, commit them before the directive ends.

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
