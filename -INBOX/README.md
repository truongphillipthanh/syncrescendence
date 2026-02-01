# -INBOX: Agent Watch Folders

**Purpose**: Autonomous task dispatch surface for CLI agents. Each agent watches its subfolder for incoming task files.

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
3. The agent **processes** the task and writes results to `-OUTGOING/`
4. Processed task files are **marked COMPLETE** and archived

## Task File Format

```markdown
# TASK-{YYYY-MM-DD}-{TOPIC}

**From**: {originating agent or Sovereign}
**Priority**: P0 | P1 | P2 | P3
**Status**: PENDING | IN_PROGRESS | COMPLETE

## Objective
{What needs to be done}

## Context
{Relevant files, background, constraints}

## Expected Output
{Where results should go, what format}

## Completion Protocol
1. Write results to -OUTGOING/ or commit directly
2. Update Status to COMPLETE in this file
3. Notify originator (if cross-machine, via git push)
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

## Cross-Machine Sync

Agents on different machines sync via git:
- **M1 Mac mini** (Ajna): watches `ajna/`, commits results
- **M4 MacBook Air** (Psyche): watches `psyche/`, writes to `-OUTGOING/`
- Both machines: `git pull` before processing, `git push` after completing
