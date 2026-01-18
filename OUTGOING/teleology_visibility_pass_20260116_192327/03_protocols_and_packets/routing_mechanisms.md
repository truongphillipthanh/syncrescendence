# Routing Mechanisms
**Generated**: 2026-01-17T03:23:54Z

---

## Overview

Task routing in Syncrescendence follows deterministic rules based on task type, platform capabilities, and availability. This document describes all routing mechanisms.

---

## 1. Task Type → Platform Routing

**Source**: `00-ORCHESTRATION/scripts/route_task.py`

| Task Type | Primary Platform | Rationale |
|-----------|------------------|-----------|
| corpus_sensing | gemini | 2M context window, Drive connector, NotebookLM integration |
| video_processing | gemini | Native multimodal, 263 tok/sec video processing |
| planning | chatgpt | GPT-5.2 Thinking excels at long-horizon decomposition |
| specification | chatgpt | Abstract reasoning for acceptance criteria definition |
| audit | chatgpt | Verification against spec, drift analysis |
| execution | claude_code | Filesystem sovereignty, agentic implementation |
| code_generation | claude_code | Production code, repo-native execution |
| file_manipulation | claude_code | Direct filesystem access, atomic operations |

---

## 2. Zone Ownership

**Source**: `config/coordination.yaml:zones`

Each platform owns specific filesystem zones for exclusive write access:

| Zone | Writable Patterns | Owner | Description |
|------|-------------------|-------|-------------|
| alpha | `04-SOURCES/processed/a-*`, `00-ORCHESTRATION/logs/*-A.md` | Claude Code (Account 2) | Stream A processing |
| beta | `04-SOURCES/processed/b-*`, `00-ORCHESTRATION/logs/*-B.md` | Claude Code (Account 3) | Stream B processing |
| gemini | `04-SOURCES/raw/*`, `04-SOURCES/processed/g-*` | Gemini | Source ingestion |
| chatgpt | `.github/*` | ChatGPT (Codex) | GitHub workflow config |
| shared | `00-ORCHESTRATION/state/*.csv`, `04-SOURCES/sources.csv` | All (append-only) | Ledgers |

**Protected Zones** (require Principal approval):
- `01-CANON/`
- `00-ORCHESTRATION/oracle_contexts/`
- `CLAUDE.md`
- `config/coordination.yaml`

---

## 3. Model Selection

**Source**: `config/coordination.yaml:model_routing`

### Default Model
```yaml
default: sonnet-4.5
```

### By Task Type
| Task Type | Model |
|-----------|-------|
| oracle_synthesis | opus-4.5 |
| architectural_decisions | opus-4.5 |
| complex_integration | opus-4.5 |
| repository_maintenance | sonnet-4.5 |
| ledger_updates | sonnet-4.5 |
| content_processing | sonnet-4.5 |
| verification_tasks | sonnet-4.5 |

### Thinking Level
| Task Type | Thinking Level | Approx Tokens |
|-----------|----------------|---------------|
| oracle_synthesis | ultrathink | ~32K |
| architectural_decisions | megathink | ~10K |
| complex_integration | megathink | ~10K |
| repository_maintenance | think | ~4K |
| ledger_updates | default | Model decides |
| content_processing | think | ~4K |
| verification_tasks | default | Model decides |

---

## 4. Routing Script API

### Usage
```bash
python3 00-ORCHESTRATION/scripts/route_task.py <task_type> [task_details_json]
```

### Available Task Types
```
corpus_sensing, video_processing, planning, specification,
audit, execution, code_generation, file_manipulation
```

### Output Format
```json
{
  "status": "routed",
  "task_type": "execution",
  "assigned_platform": "claude_code",
  "rationale": "Filesystem sovereignty, agentic implementation",
  "platform_status": "executing",
  "timestamp": "2026-01-16T00:35:43.201498Z",
  "warning": "Platform claude_code status is unknown"
}
```

### Side Effects
Each routing decision is logged to `events.jsonl`:
```json
{
  "timestamp": "2026-01-16T00:35:43.202066Z",
  "event": "routing_decision",
  "type": "routing",
  "task_type": "execution",
  "decision": {...}
}
```

---

## 5. Account Coordination

**Source**: `config/coordination.yaml:accounts`

### Claude Accounts (3x Pro @ $20/mo = $60/mo)
| Account | Role | Surface | Function |
|---------|------|---------|----------|
| Oracle Thread | Strategic synthesis | web | Strategic synthesis, directive generation |
| Alpha | Primary executor | code | Primary execution, Stream A |
| Beta | Parallel executor | code | Parallel execution, Stream B |

### Gemini Account (1x Advanced @ $20/mo)
| Role | Surface | Function |
|------|---------|----------|
| Ingestion layer | cli | YouTube processing, corpus sensing |

### ChatGPT Account (1x Plus @ $20/mo)
| Role | Surface | Function |
|------|---------|----------|
| Reasoning + GitHub | codex_cli | Planning, audit, GitHub workflows |

**Total Monthly**: $100

---

## 6. Conflict Resolution

**Source**: `config/coordination.yaml:conflict_resolution`

```yaml
conflict_resolution:
  strategy: "branch_per_instance"
  merge_target: "develop"
  merge_method: "rebase"
```

### Pattern
1. Each instance works in isolated branch
2. PRs merge to develop branch
3. Main branch updated only after verification
4. No direct inter-instance communication—coordinate via repository

---

## 7. Routing Decision Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                        TASK ARRIVES                             │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
                    ┌──────────────────┐
                    │ Identify task    │
                    │ type from        │
                    │ routing_table    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Check platform   │
                    │ status in        │
                    │ system_state     │
                    └────────┬─────────┘
                             │
         ┌───────────────────┼───────────────────┐
         ▼                   ▼                   ▼
    ┌─────────┐        ┌─────────┐        ┌─────────┐
    │AVAILABLE│        │EXECUTING│        │ PENDING │
    │ Route   │        │ Queue   │        │ ONBOARD │
    └────┬────┘        └────┬────┘        └────┬────┘
         │                  │                  │
         │                  │                  ▼
         │                  │           ┌─────────────┐
         │                  │           │ Add warning │
         │                  │           │ to decision │
         │                  │           └─────────────┘
         │                  │                  │
         └──────────────────┼──────────────────┘
                            │
                            ▼
                    ┌──────────────────┐
                    │ Select model     │
                    │ from model_      │
                    │ routing table    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Log to           │
                    │ events.jsonl     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Return routing   │
                    │ decision JSON    │
                    └──────────────────┘
```

---

## 8. Platform Status Values

| Status | Meaning |
|--------|---------|
| available | Ready to accept tasks |
| executing | Currently working on a task |
| pending_onboard | Not yet initialized (Gemini, ChatGPT as of 2026-01-16) |
| rate_limited | Quota exhausted, temporarily unavailable |
| error | Platform experiencing issues |
| offline | Intentionally disabled |

---

## 9. Rate Limit Management

From `INTERACTION_PARADIGM.md`:

| Platform | Limit | Strategy |
|----------|-------|----------|
| Claude Pro | ~45 Opus msg/5hr | Use Sonnet for routine work |
| ChatGPT Plus | ~160 Instant/3hr, ~3K Thinking/week | Reserve Thinking for complex planning |
| Gemini Advanced | Less restrictive | Primary workhorse for bulk processing |

**Pattern**: Expensive operations (Opus, GPT-5.2 Thinking) for judgment. Cheaper operations (Sonnet, Instant, Flash) for volume.
