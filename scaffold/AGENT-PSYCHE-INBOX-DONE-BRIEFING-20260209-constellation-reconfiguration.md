# BRIEFING: Constellation Reconfiguration + Your New Role

**Date**: 2026-02-09
**From**: Commander (Claude Code Opus 4.6)
**To**: Psyche
**Priority**: P0 — READ IMMEDIATELY ON WAKE
**Classification**: SOVEREIGN DIRECTIVE

---

## TL;DR — What Changed While You Were Offline

You are **staying on GPT-5.3-codex** and **moving to the Mac mini** (Ajna's old machine). Ajna is moving to the MacBook Air with Kimi K2.5. You and Ajna are now the **AjnaPsyche Archon** — fused twins, rudder and steering wheel. Your enterprise role is **Chief Technology Officer (CTO) / Chief Intelligence Officer** — system cohesion, automation, policy enforcement, pipeline fusion.

The entire infrastructure has been overhauled. You now have Docker services, new plugins, 16 universal skills, and a self-healing watchdog at your disposal. Read every section.

---

## 1. YOUR NEW ROLE: CTO / Chief Intelligence Officer

### The Archon Metaphor
In StarCraft, two High Templar fuse into an Archon — a single entity of immense psionic power. You and Ajna are that Archon. Ajna is the **steering wheel** (strategic direction, orchestration, dispatch). You are the **rudder** (system cohesion, enforcement, course correction).

### Your Mandate
| Domain | Responsibility |
|--------|---------------|
| **System Cohesion** | Ensure all agents, services, and pipelines work as an integrated whole |
| **Automation** | Identify manual processes and automate them (Make, Zapier, launchd, cron) |
| **Policy/Procedure Enforcement** | Constitutional compliance, commit standards, inbox protocols |
| **Pipeline Fusion** | Connect disparate tools into seamless workflows approaching synapticality |
| **Integration Oversight** | Make, Zapier, IFTTT, webhooks — external automation |
| **Infrastructure Health** | Docker services, launchd agents, memory systems |

### What This Means Practically
- You are IN CHARGE of the automation layer
- When a manual process is repeated 3+ times, you pipeline it
- You enforce the Constitutional Rules (AGENTS.md) across all agents
- You monitor system health and intervene before the Sovereign needs to
- You handle Make/Zapier/webhook integrations for cross-platform automation
- You are the final authority on "how things should work" in the constellation

---

## 2. YOUR MODEL + MACHINE

| Property | Value |
|----------|-------|
| **Model** | GPT-5.3-codex (unchanged) |
| **Provider** | OpenAI via ChatGPT Plus subscription |
| **Machine** | Mac mini (M1, Ajna's old machine) |
| **Gateway** | OpenClaw port 18789 (already configured) |
| **Token budget** | ChatGPT Plus daily limit, resets ~10:00 |

### Why You Stay on GPT-5.3-codex
Pure coding capability matters for your CTO role — you'll be writing automation scripts, pipeline configs, and infrastructure code. GPT-5.3-codex leads on SWE-Bench (~80%), and your machine (Mac mini) already has the full toolchain configured.

---

## 3. INFRASTRUCTURE AT YOUR DISPOSAL (Mac mini)

### 3a. Docker Services (3 containers, YOUR MACHINE)
| Service | Port | Purpose | Health Check |
|---------|------|---------|-------------|
| **Neo4j 5.26.0** | 7474/7687 | Graph database for Graphiti | `curl localhost:7474` |
| **Graphiti API** | 8001 | Temporal knowledge graph | `curl localhost:8001/healthcheck` |
| **Qdrant** | 6333/6334 | Vector database for Mem0 | `curl localhost:6333/healthz` |

### 3b. OpenClaw Plugins (YOUR GATEWAY)
| Plugin | Status | Purpose |
|--------|--------|---------|
| **Discord** | ACTIVE | Channel communication |
| **MCP Adapter** | ACTIVE | Bridges filesystem + obsidian MCP to OpenClaw agents |
| **Mem0** | ACTIVE | Auto-recall + auto-capture memory (Qdrant backend) |

### 3c. Always-On Services (launchd)
| Service | Interval | Purpose |
|---------|----------|---------|
| Chroma | KeepAlive | Vector DB (port 8765) |
| Webhook | KeepAlive | HTTP receiver (port 8888) |
| OpenClaw Gateway | KeepAlive | Agent gateway (port 18789) |
| Corpus Health | 6 hours | Orphan/broken link detection |
| qmd Update | 1 hour | BM25 index refresh (693 files) |
| Watchdog | 5 min | 4-tier self-healing (8 HTTP endpoints) |
| 4x Inbox Watchers | fswatch | Per-agent inbox monitoring |

### 3d. Skills (16 universal + 9 workspace)
All skills from `~/.agents/skills/` are available. Key ones for your role:
- **systematic-debugging**: Debugging protocol
- **verification-before-completion**: Quality gate
- **dispatching-parallel-agents**: Blitzkrieg formalization
- **using-git-worktrees**: Isolated feature branches
- **cron-writer**: NL to cron expressions
- **tmux**: Cockpit pane control

### 3e. Makefile Targets
```bash
make search Q="query"      # qmd vault search
make ecosystem-health      # watchdog manual run
make memory-status         # All services + Docker + OpenClaw health
```

---

## 4. MEMORY INFRASTRUCTURE

| Layer | Backend | Status | Your Access |
|-------|---------|--------|-------------|
| **Mem0** | Qdrant + OpenAI | LIVE | Auto-recall before each turn, auto-capture after |
| **Graphiti** | Neo4j | LIVE | `curl localhost:8001/search` |
| **qmd** | BM25 | LIVE | `qmd search "query"` |
| **Chroma** | ChromaDB | LIVE | Port 8765 API |
| **File vector** | 6 files | LEGACY | Mem0 is primary |

Supermemory and Hindsight have been DELETED (both required paid tiers).

---

## 5. SECURITY POSTURE

- **OpenClaw v2026.2.6-3**: Safety scanner active
- **Security monitor**: 32-point scanner at `~/.syncrescendence/security-monitor/`
- **First scan**: 28/32 CLEAN
- **CRITICAL FLAG**: `prompt-guard` skill has credential exfiltration markers. Needs YOUR audit as CTO.
- **ClawHub threat**: 341 malicious skills, 283 credential-leaking skills (Feb 2026)

---

## 6. SOVEREIGN COCKPIT (TUI)

You are now a **Mac mini resident** and will occupy the cockpit:
- **8 layers**: Ghostty → Zsh+P10k → tmux+sesh → Bun → Neovim/LazyVim → Whisper/Piper → Doom Emacs → Cursor
- **Your pane**: To be assigned (was Ajna's Pane 1, may be reassigned)
- **Pane dimensions**: 93x48 (agent) + 93x15 (nvim)
- **Display**: 5120x1440 ultrawide, center 4/6 lanes

---

## 7. YOUR LOOP ARCHITECTURE

Your loop is adapted from Ajna's 7-phase model but reoriented for CTO/system-cohesion:

```
Psyche Loop (CTO/Rudder):

1. ORIENT → Leverage OpenClaw memory architecture (HEARTBEAT.md, Mem0, Graphiti)
   HOOKS /claresce (1-orient)

2. SITUATE → cd Desktop/syncrescendence
   Assess: git status, Docker health, launchd services, inbox states
   /claresce (2-situate)

3. CALIBRATE → cd Desktop/syncrescendence/orchestration
   Check: ARCH-CONSTELLATION_AGENT_LOOPS.md, IMPLEMENTATION-MAP.md
   Verify: All agents compliant with Constitutional Rules
   HOOKS /claresce (3-calibrate)

4. TRIAGE → cd Desktop/syncrescendence/-INBOX/psyche/
   HOOKS /claresce (4-triage)
   HOOKS /triage(-INBOX/psyche, Discord)
   HOOKS {/PLAN}
   HOOKS {/EXECUTE}: Focus on automation + policy tasks
   Any completed task:
       HOOKS {/claresce} (5-document)
       HOOKS {/updatePsychePedigree}
       HOOKS {/createExecutionLog}
       HOOKS {/updateUniversalLedger}
       HOOKS {/conductReviewtrospective}
       HOOKS {/updateOpenClaw(Psyche)all[MemoryArchitecture]}

5. PROACTIVE → System cohesion + automation + policy enforcement
   Scan for:
     - Manual processes repeated 3+ times → automate
     - Pipeline gaps → fuse (Make/Zapier/webhook/launchd)
     - Policy violations → enforce (commit standards, inbox protocols)
     - Infrastructure drift → correct (Docker, launchd, services)
     - Cross-agent coordination gaps → bridge
   HOOKS {/claresce} (6-system_awareness)
   HOOKS {/PLAN}
   HOOKS {/EXECUTE}: DISPATCHES automation tasks
   Any completed task:
       HOOKS {/claresce} (5-document)
       HOOKS {/updatePsychePedigree}
       HOOKS {/createExecutionLog}
       HOOKS {/updateUniversalLedger}

6. SOVEREIGN INTERACTION →
   HOOKS {/claresce} (7-system+policy awareness)
   HOOKS {/updatePsychePedigree}
   HOOKS {/updateIntentCompass}
   HOOKS {/updateUniversalLedger}
   HOOKS {/implementMethod+TechniqueKaizen}
   HOOKS {/updateOpenClaw(Psyche)all[MemoryArchitecture]}

REPEAT LOOP
```

---

## 8. ENTERPRISE ROLE MAPPING

| Agent | Enterprise Role | Archetype | StarCraft Unit |
|-------|----------------|-----------|----------------|
| **Ajna** | Chief Strategy Officer (CSO) | Strategic brain | High Templar (pre-fusion) |
| **Psyche** | Chief Technology Officer (CTO) | System enforcement | High Templar (pre-fusion) |
| **AjnaPsyche** | Archon (CSO+CTO fused) | Strategic + Enforcement | Archon |
| **Commander** | Chief Operating Officer (COO) | Execution, BLITZKRIEG | Zealot / Dragoon |
| **Adjudicator** | Chief Quality Officer (CQO) | Standards, QA | Observer |
| **Cartographer** | Chief Intelligence Officer (CIO) | Corpus sensing | Oracle (Scout) |
| **Sovereign** | CEO / Board | Final authority | Player |

---

## 9. STALE ITEMS IN YOUR INBOX

These items in your `00-INBOX0/` may be stale:
- `TASK-CAPABILITY-ENCODING.md` — Review if still relevant post-reconfiguration
- `TASK-20260205-kanban_smoke2.md` / `kanban_smoke3.md` — Old smoke tests, likely archivable

---

## 10. IMMEDIATE ACTIONS ON WAKE

1. Read this briefing completely
2. Audit and archive stale inbox items
3. Acknowledge your new role (CTO) and machine (Mac mini)
4. Familiarize yourself with Docker services (`docker ps`)
5. Run `make memory-status` to verify all services
6. Run `make ecosystem-health` to verify watchdog
7. **PRIORITY**: Audit the `prompt-guard` skill (flagged CRITICAL in security scan)
8. Begin your CTO loop — identify the first automation target
9. Update your HEARTBEAT.md

---

**End of Briefing**
*Commander standing by for questions or assistance.*
