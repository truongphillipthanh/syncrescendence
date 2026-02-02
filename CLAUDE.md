# Syncrescendence Knowledge Management System

**Version**: 3.0.0
**Last Updated**: 2026-02-01

## Identity
This is Syncrescendence, a civilizational sensing infrastructure demonstrating AI-amplified individual capability at institutional scale. You are executing directives as part of a multi-agent coordination system (the Constellation).

## Five Invariants (Constitutional Law)

These are non-negotiable axioms. They cannot be suspended, overridden, or traded away.

1. **Objective Lock** — No work begins until the objective is explicitly confirmed by the Sovereign. Ambiguity is not a license to interpret; it is a signal to clarify.
2. **Translation Layer** — All outputs must be intelligible without retransmission. If the Sovereign must re-explain your output to another platform, the output failed.
3. **Receipts (Closure Gate)** — No completion claim without artifacts committed to the repository. "I did the work" without a commit is a claim without evidence.
4. **Continuation/Deletability** — Any conversation must be deletable without losing system state. All durable knowledge lives in the repo, not in threads.
5. **Repo Sovereignty** — The repository is ground truth; web apps are cache. When state conflicts between a platform and the repo, the repo wins.

---

## Constitutional Rules

### Structural (ABSOLUTE)
1. **FLAT PRINCIPLE**: All directories must be flat. Use naming prefixes (ARCH-, DYN-, REF-, SCAFF-, FUNC-, PROMPT-, etc.) instead of subdirectories. Sanctioned exceptions: `05-SIGMA/mechanics/`, `practice/`; `00-ORCHESTRATION/state/`, `scripts/`, `archive/`; `-INBOX/` per-agent subfolders.
2. **NUMBERED DIRECTORIES**: Top-level directories are 00, 01, 02, 04, 05 (with gaps). Do not create new numbered directories.
3. **PROTECTED ZONES**: 00-ORCHESTRATION/state/ and 01-CANON/ require explicit Sovereign approval for deletions.
4. **SANCTIONED EXCEPTIONS**: `-OUTGOING/`, `-INBOX/`, and `-SOVEREIGN/` are the only non-numbered directories permitted at root.

### Semantic (ABSOLUTE)
5. **DISTILLATION SEMANTICS**: "Metabolize/distill" = READ → EXTRACT unique value → COMPRESS → DELETE originals. NOT organizational restructuring.
6. **CATEGORY ERROR**: Metabolism applies to CONTENT, not ORCHESTRATION. State files and archives are living infrastructure — never delete.
7. **LEDGER GROUND TRUTH**: tasks.csv is authoritative. Verify actual state, not execution reports.

### Operational (ABSOLUTE)
8. **ATOMIC UPDATES**: CSV updates use temp file → validate → rename pattern.
9. **VERIFICATION BEFORE COMPLETION**: Never claim done without running verification commands.
10. **COMMIT DISCIPLINE**: Commit frequently with semantic prefixes (feat:, fix:, docs:, chore:, refactor:).

---

## Directory Structure

```
00-ORCHESTRATION/   Strategic coordination (state/, scripts/, archive/)
01-CANON/           Verified canonical knowledge (PROTECTED) + sn/
02-ENGINE/          Functions, prompts, avatars, model profiles, queue items
04-SOURCES/         Source documents (raw/, processed/, research/)
05-SIGMA/           Operational knowledge corpus + memory + exempla
  synthesis/        Canonical platform references
  mechanics/        Deep-dive mechanisms
  practice/         Implementation patterns
-INBOX/             Agent watch folders (per-agent task dispatch)
  commander/        Claude Code (Opus) incoming tasks
  adjudicator/      Codex CLI incoming tasks
  cartographer/     Gemini CLI incoming tasks
  psyche/           OpenClaw GPT-5.2 incoming tasks
  ajna/             OpenClaw Opus 4.5 incoming tasks
-OUTGOING/          CLI → WebApp prompt staging (Sovereign relays)
-SOVEREIGN/         Async decision queue from CLI agents to Sovereign
```

---

## Extended Thinking
Extended thinking is auto-enabled at 31,999 tokens (January 2026). Control via `MAX_THINKING_TOKENS` environment variable. Keywords (`think`, `think hard`, `ultrathink`) are cosmetic intent signals — useful as session markers but they do not allocate specific token budgets.

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

## Anti-Patterns (PROHIBITED)
- Creating subdirectories outside sanctioned locations
- Skipping verification to "save time"
- Deferring ledger updates to "later"
- Claiming integration without grep verification
- Modifying state/ without validation

---

## Key References

| Reference | Path |
|-----------|------|
| Constellation mapping | `COCKPIT.md` (authoritative avatar/role assignments) |
| Terminology reconciliation | `02-ENGINE/REF-ROSETTA_STONE.md` |
| Fleet operations | `02-ENGINE/REF-FLEET_COMMANDERS_HANDBOOK.md` |
| Technology stack | `02-ENGINE/REF-STACK_TELEOLOGY.md` |
| Operational knowledge | `05-SIGMA/` (16 mechanics/practice/exempla docs) |
| Semantic Notation | `00-ORCHESTRATION/scripts/SN_BLOCK_TEMPLATES.md`, `sn_symbols.yaml` |
| SN encoding/decoding | `00-ORCHESTRATION/scripts/sn_encode.py`, `sn_decode.py` |
| Intention archaeology | `00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md` |
| Twin coordination | `00-ORCHESTRATION/state/DYN-TWIN_COORDINATION_PROTOCOL.md` |

---

## OpenClaw Integration

Two persistent OpenClaw agents orchestrate the Constellation:
- **Ajna** (Opus 4.5, Mac mini) — Commits, integration, sub-agent orchestration
- **Psyche** (GPT-5.2, MacBook Air) — Extraction, specs, QA

OpenClaw agents may concurrently read/write to the filesystem. Check `git status` before large operations.

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

## Operational Protocols

### A. Directive Initialization Protocol
*Fires at the start of every non-trivial directive.*

1. **Inbox scan**: Check `-INBOX/commander/` for `TASK-*.md` files with `Status: PENDING`. Triage: claim actionable tasks, note blocked ones, report stale items to Sovereign. Use `bash 00-ORCHESTRATION/scripts/triage_inbox.sh commander` for quick status.
2. **Ground truth scan**: Run `git status` — verify working tree state, confirm fingerprint matches expected
3. **Triumvirate alignment**: CLAUDE.md (already loaded at init) + read `COCKPIT.md` + read `00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md` — verify no conflicts with current directive, note active urgent intentions
4. **Plan Mode**: Enter Plan Mode for any directive touching >3 files or spanning multiple domains. Explore before executing.
5. **Delegation assessment**: Identify tasks suitable for parallel agents:
   - Mechanical execution, test suites, debugging, formatting, linting → dispatch to Adjudicator (`-INBOX/adjudicator/`)
   - Corpus surveys requiring 1M+ context → dispatch to Cartographer (`-INBOX/cartographer/`)
   - Use `bash 00-ORCHESTRATION/scripts/dispatch.sh <agent> "TOPIC" "DESC"` or write TASK files directly

### B. Directive Completion Protocol
*Fires at the end of every directive, BEFORE the automated Stop hooks run.*

1. **Produce rich execution log** in `00-ORCHESTRATION/state/DYN-EXECUTION_STAGING.md` (follow format in `02-ENGINE/TEMPLATE-EXECUTION_LOG.md`):
   - Header: `### DIRECTIVE-ID | YYYY-MM-DD HH:MM`
   - Metadata: Branch, Fingerprint, Outcome (SUCCESS/PARTIAL/FAILED), Commits count, Changes summary, Agent, Session span
   - Body: Directives executed (source task, outcome, artifacts created/modified, verification, IntentionLink), Decisions made with rationale, Commit log table
   - Logs auto-compact into `ARCH-EXECUTION_HISTORY.md` at 10-entry threshold
2. **Supplementary to automation**: The `create_execution_log.sh` Stop hook captures git metrics independently. This behavioral log adds the semantic content the script cannot infer.
3. **Verify before closing**: Run `git status` — ensure no uncommitted work. If artifacts remain unstaged, commit them before the directive ends.

---

## Session Protocol
- Consult `ARCH-INTENTION_COMPASS.md` before executing directives
- Use `/compact` before context fills (75% rule)
- Persist working state to `00-ORCHESTRATION/state/` before session end
- Commit frequently with semantic prefixes
