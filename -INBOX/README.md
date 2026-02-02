# -INBOX: Agent Watch Folders

**Purpose**: Autonomous task dispatch surface for CLI agents. Each agent watches its subfolder for incoming task files. Architecture validated against community agent orchestration patterns (Supervisor, Coordinator, Self-Discovery).

**IO Model**: v2.0 (2026-02-06)

---

## Architecture

```
-INBOX/
  commander/      Claude Code (Opus) — primary execution tasks
  adjudicator/    Codex CLI — mechanical code, tests, formatting
  cartographer/   Gemini CLI — corpus surveys, evidence packs
  psyche/         OpenClaw GPT-5.2 — extraction, QA, specs
  ajna/           OpenClaw Opus 4.5 — integration, orchestration
```

## IO Model v2

### Agent-to-Agent = Direct Inbox Delivery

Agents write directly to the destination agent's inbox folder. No intermediate staging.

```
Ajna results for Psyche   → -INBOX/psyche/
Psyche tasks for Ajna     → -INBOX/ajna/
Commander results for Ajna → -INBOX/ajna/
```

### Agent-to-Web = -OUTGOING (PROMPT-* only)

Web relay prompts go to `-OUTGOING/` with the `PROMPT-` prefix for Sovereign relay. See `-OUTGOING/README.md`.

### Sovereign Decisions = -SOVEREIGN/

Human-in-the-loop decisions that require Phillip's judgment. Different pattern from agent-to-agent dispatch.

---

## How It Works

1. **Any agent** (or the Sovereign) writes a task file to a target agent's folder
2. The target agent's **filesystem watcher** (`watch_dispatch.sh`) detects the new file
3. Watcher **atomically claims** the file: `TASK-xxx.md` → `TASK-xxx.md.claimed-by-{agent}-{hostname}`
4. Agent processes the task, writes results to the originator's inbox (or commits directly)
5. On completion: file renamed to `.complete` and **ledger entry appended** (`DYN-GLOBAL_LEDGER.md`)
6. On failure: file renamed to `.failed` and ledger entry appended

## Claim-Locking Protocol

To prevent duplicate consumers when multiple watchers run concurrently:

```
# Claim phase (atomic rename)
mv TASK-xxx.md TASK-xxx.md.claimed-by-{agent}-{hostname}

# Only the claimer proceeds to execution

# Completion phase
mv TASK-xxx.md.claimed-by-{agent}-{hostname} TASK-xxx.md.complete
# (or .failed on error)
```

The atomic rename ensures exactly one consumer processes each task, even across machines syncing via git.

## Task File Format

```markdown
# TASK-{YYYY-MM-DD}-{TOPIC}

**From**: {originating agent or Sovereign}
**To**: {target avatar name}
**Priority**: P0 | P1 | P2 | P3
**Status**: PENDING | IN_PROGRESS | COMPLETE | FAILED
**Fingerprint**: {git short hash at dispatch time}
**Timeout**: {max minutes, default 30}

## Objective
{What needs to be done}

## Context
{Relevant files, background, constraints}

## Expected Output
{Where results should go, what format}
```

## Result File Format

Results are written to the **originating agent's inbox** (not -OUTGOING):

```markdown
# RESULT-{source-agent}-{DATE}-{TOPIC}

**From**: {executing agent}
**To**: {originating agent}
**Task**: {original TASK filename}
**Status**: COMPLETE | PARTIAL
**Fingerprint**: {git short hash at completion}

## Results
{What was accomplished}

## Artifacts
{Files created/modified}
```

## Routing Guide

| Task Type | Route To | Rationale |
|-----------|----------|-----------|
| Architectural decisions | commander/ | Opus-grade reasoning |
| Code execution, tests, formatting | adjudicator/ | Mechanical, parallelizable |
| Corpus surveys, evidence packs | cartographer/ | 1M context, stateless sensing |
| QA, extraction, specs | psyche/ | GPT-5.2 synthesis |
| Integration, orchestration | ajna/ | Local commit authority |
| Sovereign judgment needed | -SOVEREIGN/ | Human decision required |
| Web app prompts | -OUTGOING/ | PROMPT-* files for Sovereign relay |

## Research-Backed Patterns (from 05-SIGMA corpus)

### Self-Discovery Assignment
Agents can poll for their own work by scanning their inbox folder, filtering for `Status: PENDING`, and self-selecting tasks matching their capabilities. No centralized scheduler needed.

### Coordinator Pattern (Neo-Blitzkrieg)
Commander acts as central orchestrator: reads plan → identifies parallelizable tracks → dispatches to agent folders → monitors completion → hands to reviewers → cycles until done. See REF-ROSETTA_STONE.md entry #14 for full pipeline.

### Error Propagation Defense
- **Timeout**: Each task has a max duration (default 30 min). Watcher marks as FAILED if exceeded.
- **Circuit breaker**: After 3 consecutive FAILED tasks to same agent, route to fallback agent.
- **Graceful degradation**: System works with subset of agents. Missing agent = tasks queue until available.
- **State isolation**: Task failures don't corrupt shared repo state (atomic commits).

### FINGERPRINT-Back Protocol
Every agent receiving a FINGERPRINT.md (web handoff) or TASK file must write state back before releasing control. This ensures durable cognition — no work is lost in ephemeral context.

## Cross-Machine Sync

Agents on different machines sync via git:
- **M1 Mac mini** (Ajna): watches `ajna/`, commits results
- **M4 MacBook Air** (Psyche): watches `psyche/`, writes to originator inbox
- Both machines: `git pull` before processing, `git push` after completing

## Tooling

| Script | Purpose |
|--------|---------|
| `dispatch.sh <agent> "TOPIC" "DESC"` | Create task file in agent's folder |
| `watch_dispatch.sh [agent]` | Watch an agent's folder for new tasks (with claim-locking) |
| `dispatch_to_psyche.sh` | Convenience wrapper for Psyche dispatch |
| `triage_inbox.sh <agent>` | List PENDING/IN_PROGRESS tasks, highlight stale |
| `append_ledger.sh` | Append event to DYN-GLOBAL_LEDGER.md |
| `triage_outgoing.sh` | Full pipeline observability |
