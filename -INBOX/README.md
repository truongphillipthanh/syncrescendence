# -INBOX: Agent Watch Folders

**Purpose**: Autonomous task dispatch surface for CLI agents. Each agent watches its subfolder for incoming task files. Architecture validated against community agent orchestration patterns (Supervisor, Coordinator, Self-Discovery).

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

## How It Works

1. **Any agent** (or the Sovereign) writes a task file to a target agent's folder
2. The target agent's **filesystem watcher** (`watch_dispatch.sh`) detects the new file
3. Agent marks task **IN_PROGRESS**, processes it, writes results
4. On completion: agent **FINGERPRINTs back** (writes state before releasing)
5. Results go to `-OUTGOING/` (for web relay) or committed directly (for CLI agents)
6. Processed task files are **marked COMPLETE** and archived

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

## Completion Protocol
1. Write results to -OUTGOING/ or commit directly
2. FINGERPRINT back: write completion state before releasing
3. Update Status to COMPLETE (or FAILED with reason)
4. Notify originator (if cross-machine, via git push)
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
- **M4 MacBook Air** (Psyche): watches `psyche/`, writes to `-OUTGOING/`
- Both machines: `git pull` before processing, `git push` after completing

## Tooling

| Script | Purpose |
|--------|---------|
| `dispatch.sh <agent> "TOPIC" "DESC"` | Create task file in agent's folder |
| `watch_dispatch.sh [agent]` | Watch an agent's folder for new tasks |
| `dispatch_to_psyche.sh` | Convenience wrapper for Psyche dispatch |
