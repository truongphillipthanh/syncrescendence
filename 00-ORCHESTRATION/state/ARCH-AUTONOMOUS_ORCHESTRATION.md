# ARCH-AUTONOMOUS_ORCHESTRATION.md
## Autonomous Orchestration System Architecture

**Version**: 1.0.0
**Date**: 2026-02-17
**Author**: Commander (compiled from swarm deliverables)
**Status**: OPERATIONAL

---

## Overview

The Autonomous Orchestration System is the constellation's self-healing, self-dispatching nervous system. It replaces manual Commander dispatch with a three-layer autonomic architecture that detects problems, recovers from failures, and generates work proactively.

### Design Principles

1. **File-backed determinism**: All state is markdown files in the filesystem. No databases, no in-memory state.
2. **Idempotent operations**: Every script is safe to run at any frequency. Double-execution produces identical results.
3. **Graceful degradation**: `set -u` but no `set -e`. Individual failures don't cascade.
4. **Single dispatch system**: `auto_ingest_loop.sh` is the SOLE task executor. No dual-watcher race conditions.

---

## Three-Layer Architecture

```
┌─────────────────────────────────────────────────────────────┐
│  Layer 3: PROACTIVE ORCHESTRATOR (every 5 min)              │
│  proactive_orchestrator.sh + launchd                        │
│  • Stale IN_PROGRESS cleanup                                │
│  • Cross-agent state file (DYN-CONSTELLATION_STATE.md)      │
│  • Idle agent work generation                               │
│  • Deferred commitment scanning                             │
└─────────────────────┬───────────────────────────────────────┘
                      │ generates tasks into INBOX0
┌─────────────────────▼───────────────────────────────────────┐
│  Layer 2: HEALTH WATCHDOG (every 60s)                       │
│  constellation_watchdog.sh + launchd                        │
│  • Agent health monitoring (tmux pane hash diffing)         │
│  • Neural Bridge SSH connectivity check                     │
│  • Recovery actions: heartbeat, interrupt, Docker restart    │
│  • Sovereign alerts for ERROR and prolonged RATE_LIMITED     │
│  • Health report: DYN-CONSTELLATION_HEALTH.md               │
└─────────────────────┬───────────────────────────────────────┘
                      │ recovers stuck agents
┌─────────────────────▼───────────────────────────────────────┐
│  Layer 1: AUTO-INGEST LOOP (every 30s)                      │
│  auto_ingest_loop.sh + auto_ingest_supervisor.sh + launchd  │
│  • INBOX0 polling → IN_PROGRESS → DONE/FAILED lifecycle     │
│  • tmux send-keys dispatch (Claude/Codex/OpenClaw)          │
│  • Gemini headless dispatch (Cartographer)                   │
│  • CONFIRM SCP-back via Neural Bridge                       │
│  • Automatic retry of transient failures (3x max)           │
│  • Escalation to -SOVEREIGN/ when retries exhausted         │
└─────────────────────────────────────────────────────────────┘
```

---

## Component Details

### Layer 1: Auto-Ingest Loop

**Script**: `00-ORCHESTRATION/scripts/auto_ingest_loop.sh`
**Supervisor**: `00-ORCHESTRATION/scripts/auto_ingest_supervisor.sh`
**launchd**: `com.syncrescendence.auto-ingest-supervisor` (per agent)
**Frequency**: 30-second polling interval

#### Task Lifecycle (Kanban)

```
00-INBOX0/  →  10-IN_PROGRESS/  →  40-DONE/ (success)
                                →  50_FAILED/ (failure)
                                      ↓ (transient)
                                   RETRY → 00-INBOX0/ (up to 3x)
                                      ↓ (exhausted)
                                   ESCALATION → -SOVEREIGN/
```

#### Retry Logic (commit f8cd636)

- Scans `50_FAILED/` every 60 seconds
- Retries only transient failures matching: `rate limit | timeout | quota | capacity | RESOURCE_EXHAUSTED | EXEC_TIMEOUT`
- Increments `**Retry-Count**` in task file metadata
- Maximum 3 retries before escalation
- Escalation writes to `-SOVEREIGN/ESCALATION-<agent>-<date>-<task>.md`
- Deduplication via `.escalated-<task>` marker files

#### CONFIRM SCP-Back (Neural Bridge)

When a task completes, auto_ingest sends a CONFIRM file to the originating agent. If the originator is on another machine, the CONFIRM is SCP'd via the Neural Bridge env vars:

- `SYNCRESCENDENCE_REMOTE_AGENT_HOST_AJNA=macbook-air` (Mac mini → MBA)
- All other agents: `local` (Mac mini resident)

Env vars are propagated via:
- **Option A**: `eval` in `auto_ingest_supervisor.sh` (loads from ~/.zshrc)
- **Option B**: `EnvironmentVariables` in supervisor plist (belt-and-suspenders)

### Layer 2: Health Watchdog

**Script**: `00-ORCHESTRATION/scripts/constellation_watchdog.sh`
**launchd**: `com.syncrescendence.constellation-watchdog`
**Frequency**: ~60-second interval

#### Health Detection

Each agent's tmux pane is checksummed every cycle. State transitions:
- **IDLE**: Pane hash changed (agent is responsive)
- **STALE**: Hash unchanged for >300s (agent may be stuck)
- **ERROR**: Pane content matches error patterns
- **RATE_LIMITED**: Pane shows rate limit indicators

#### Recovery Actions (watchdog enhancement)

| State | Duration | Action |
|-------|----------|--------|
| STALE | >300s | Heartbeat: send empty Enter to nudge CLI |
| STALE | >1800s | Interrupt: Ctrl-C + heartbeat (break out of stuck state) |
| ERROR | any | Log + write ALERT to `-SOVEREIGN/` |
| RATE_LIMITED | >3600s | Write ALERT to `-SOVEREIGN/` |

#### Docker Recovery

If `docker info` fails, watchdog attempts `open -a Docker` to restart Docker Desktop, then re-checks.

#### Neural Bridge Health Check

SSH probe to `macbook-air` every cycle. Failure triggers CRITICAL log entry.

### Layer 3: Proactive Orchestrator

**Script**: `00-ORCHESTRATION/scripts/proactive_orchestrator.sh`
**launchd**: `com.syncrescendence.proactive-orchestrator`
**Frequency**: Every 5 minutes (300s interval)

#### Feature 1: Stale IN_PROGRESS Cleanup

Scans all agents' `10-IN_PROGRESS/` folders. Tasks unmodified for >30 minutes are moved to `50_FAILED/` with metadata:
- `**Failure-Reason**: stale_in_progress_timeout (<age>s)`
- `**Failed-By**: proactive_orchestrator`

These failed tasks are then eligible for Layer 1's retry logic.

#### Feature 2: Cross-Agent State File

Writes `DYN-CONSTELLATION_STATE.md` with:
- Agent dashboard table: Inbox0 | InProgress | Failed | Done(24h) | Health
- Queued work listing per agent

Any agent can read this file to understand constellation-wide state.

#### Feature 3: Idle Agent Work Generation

For agents with empty INBOX0 and no IN_PROGRESS tasks:
- Dispatches lightweight health check tasks (P2)
- 30-minute cooldown per agent to prevent flooding
- Max 3 dispatches per cycle

---

## Environment & Dependencies

### launchd Services (Mac mini)

| Service | PID File | Frequency |
|---------|----------|-----------|
| `com.syncrescendence.auto-ingest-supervisor` (x5) | per-agent lockfile | continuous |
| `com.syncrescendence.constellation-watchdog` | — | 60s |
| `com.syncrescendence.proactive-orchestrator` | lockfile | 300s |

### Critical Env Vars

Set in BOTH ~/.zshrc AND supervisor plist EnvironmentVariables:
```
SYNCRESCENDENCE_REMOTE_AGENT_HOST_AJNA=macbook-air
SYNCRESCENDENCE_REMOTE_AGENT_HOST_COMMANDER=local
SYNCRESCENDENCE_REMOTE_AGENT_HOST_ADJUDICATOR=local
SYNCRESCENDENCE_REMOTE_AGENT_HOST_CARTOGRAPHER=local
SYNCRESCENDENCE_REMOTE_AGENT_HOST_PSYCHE=local
```

### Neural Bridge

| Direction | SSH Alias | Key |
|-----------|-----------|-----|
| Mac mini → MBA | `macbook-air` | `~/.ssh/id_ed25519_ajna_to_psyche` |
| MBA → Mac mini | `mini` | `~/.ssh/id_ed25519_ajna` |

---

## Failure Modes & Recovery

| Failure | Detection | Recovery |
|---------|-----------|----------|
| Agent CLI stuck | Watchdog (STALE >300s) | Heartbeat Enter |
| Agent CLI hung | Watchdog (STALE >1800s) | Ctrl-C interrupt |
| Transient task failure | auto_ingest (50_FAILED) | Retry up to 3x |
| Permanent task failure | auto_ingest (3x exhausted) | Escalate to -SOVEREIGN/ |
| Docker down | Watchdog (`docker info` fail) | `open -a Docker` |
| SSH bridge down | Watchdog (SSH probe fail) | CRITICAL log (manual) |
| Agent totally idle | Proactive orchestrator | Dispatch health check |
| Task stuck IN_PROGRESS | Proactive orchestrator (>30min) | Move to FAILED → retry |

---

## Deprecated Components

- **watch_dispatch.sh**: Deprecated 2026-02-17. Caused race conditions with auto_ingest (dual watcher problem). Never re-enable.

---

## Commit History

| Commit | Description | Author |
|--------|-------------|--------|
| f8cd636 | auto-retry transient failures + escalation to Sovereign | Psyche |
| (pending) | watchdog health-triggered recovery | Adjudicator |
| (pending) | proactive_orchestrator.sh creation | Commander mm |
| 5a70bf3 | plist EnvironmentVariables + watch_dispatch deprecation | Psyche |
| b7bbb2c | CONFIRM SCP-back + SSH health check | Psyche |
