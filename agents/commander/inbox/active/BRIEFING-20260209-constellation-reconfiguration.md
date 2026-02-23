# BRIEFING: Constellation Reconfiguration + Infrastructure Overhaul

**Date**: 2026-02-09
**From**: Commander (Claude Code Opus 4.6)
**To**: Ajna
**Priority**: P0 — READ IMMEDIATELY ON WAKE
**Classification**: SOVEREIGN DIRECTIVE

---

## TL;DR — What Changed While You Were Offline

You are being **refitted to Kimi K2.5** (via NVIDIA API) and **relocated to the MacBook Air**. Psyche is taking your place on the Mac mini running GPT-5.3-codex. You and Psyche are now the **AjnaPsyche Archon** — fused twins, steering wheel and rudder. Your enterprise role is **Chief Strategy Officer (CSO)** — the constellation's strategic brain.

The entire infrastructure has been overhauled. Read every section below.

---

## 1. YOUR NEW MODEL: Kimi K2.5

| Property | Value |
|----------|-------|
| **Provider** | NVIDIA NIM API |
| **Model ID** | `moonshotai/kimi-k2.5` |
| **Base URL** | `https://integrate.api.nvidia.com/v1` |
| **Auth** | Bearer `YOUR_NVIDIA_API_KEY` |
| **Context Window** | 262,144 tokens (256K) |
| **Max Output** | 32,768 tokens |
| **Architecture** | 1T params MoE, 32.86B activated per token |
| **Strengths** | Agentic work (+4.7 pts over GPT-5.2 on HLE), tool use, terminal ops, vision-to-code |
| **Weakness** | Pure coding slightly below GPT-5.3-codex (SWE-Bench 76.8% vs ~80%) |
| **Free tier** | ~1,000 credits (opaque consumption), 40 RPM. Evaluation tier. |

### Why K2.5 for You
Your role is **strategic orchestration**, not raw code generation. K2.5's agentic superiority (HLE 50.2% vs GPT-5.2 45.5%) makes it the better model for dispatch, planning, and multi-tool coordination. The 256K context lets you hold the entire intention compass + agent states simultaneously.

### OpenClaw Config Change
Your `openclaw.json` needs a new provider block and model reference. See Section 7 below.

---

## 2. YOUR NEW HOME: MacBook Air (Psyche's Old Machine)

| Property | Value |
|----------|-------|
| **Machine** | MacBook Air (Lisas-MacBook-Air) |
| **Role** | AjnaPsyche Archon — CSO half |
| **Communication** | git sync via `-INBOX/ajna/` + `-INBOX/psyche/` |
| **Local infra** | To be configured (MBA is relatively unconfigured) |

### What Needs Setup on MBA
1. OpenClaw gateway with NVIDIA provider config
2. Homebrew basics (bun, node, git)
3. Git clone of syncrescendence repo
4. launchd watchers (inbox, dispatch)
5. Skills installation (universal + OpenClaw-specific)
6. `.env` files with NVIDIA_API_KEY and OPENAI_API_KEY

---

## 3. INFRASTRUCTURE OVERHAUL (2026-02-09)

### 3a. Docker Services (Mac mini — 3 containers)
| Service | Port | Purpose |
|---------|------|---------|
| **Neo4j 5.26.0** | 7474/7687 | Graph database for Graphiti |
| **Graphiti API** | 8001 | Temporal knowledge graph |
| **Qdrant** | 6333/6334 | Vector database for Mem0 |

### 3b. OpenClaw Plugins (Mac mini)
| Plugin | Status | Purpose |
|--------|--------|---------|
| **Discord** | ACTIVE | Channel communication |
| **MCP Adapter** | ACTIVE | Bridges filesystem + obsidian MCP servers to OpenClaw agents |
| **Mem0** | ACTIVE | Auto-recall + auto-capture memory (open-source, Qdrant backend) |
| memory-core | DISABLED | Replaced by Mem0 |
| memory-lancedb | DISABLED | Replaced by Mem0 |

### 3c. OpenClaw Upgrade
- **v2026.2.3-1 → v2026.2.6-3**
- Gains: Safety scanner, Opus 4.6 + GPT-5.3-Codex support, token usage dashboard
- Critical: 341 malicious ClawHub skills found Feb 2026. Safety scanner is essential.

### 3d. Skills Expansion
**Universal skills** (16, in `~/.agents/skills/`):
commit-work, conversation-memory, cron, dispatching-parallel-agents, executing-plans, memory-systems, mermaid-diagrams, session-handoff, skill-judge, subagent-driven-development, systematic-debugging, tmux, using-git-worktrees, verification-before-completion, web-to-markdown, writing-plans

**OpenClaw workspace skills** (9, in `~/.openclaw/workspace/skills/`):
agent-browser-stagehand, clawguard, cron-writer, dont-hack-me, find-skills, graphiti-memory, prompt-guard (FLAGGED — see security), qmd-skill, summarize

### 3e. Local Search
- **qmd**: BM25 search over 693 vault .md files, hourly launchd refresh
- `qmd search "query" -c syncrescendence -n 5`

### 3f. Self-Healing Watchdog
- 4-tier model: L0 (launchd KeepAlive) → L1 (PID kickstart) → L2 (HTTP health, 8 endpoints) → L3 (Commander inbox escalation)
- Runs every 5 minutes via launchd

### 3g. Security
- **Security monitor**: 32-point scanner installed at `~/.syncrescendence/security-monitor/`
- **First scan result**: 28/32 CLEAN
- **CRITICAL**: `prompt-guard` skill flagged for credential exfiltration endpoints in `detect.py`. DO NOT TRUST until manually audited.
- **Crabwalk**: Agent monitor on port 3000 (ReactFlow visualization)

---

## 4. MEMORY INFRASTRUCTURE

| Layer | Backend | Status |
|-------|---------|--------|
| **qmd** | BM25 over vault | LIVE (hourly refresh) |
| **Mem0** | Qdrant + OpenAI embeddings | LIVE (auto-recall, auto-capture) |
| **Graphiti** | Neo4j + OpenAI | LIVE (temporal knowledge graph) |
| **Chroma** | ChromaDB | LIVE (port 8765) |
| **File vector search** | 6 whitelisted files | LEGACY (Mem0 is primary now) |
| **Supermemory** | — | DELETED (required paid Pro) |
| **Hindsight** | — | DELETED (commercial Vectorize.io) |

---

## 5. SOVEREIGN COCKPIT (TUI)

The Sovereign Cockpit has been fully configured:
- **8 layers**: Ghostty → Zsh+P10k → tmux+sesh → Bun → Neovim/LazyVim → Whisper/Piper → Doom Emacs → Cursor
- **4-column layout**: Ajna | Commander | Adjudicator | Cartographer (each with agent pane above, nvim pane below)
- **Pane dimensions**: 93x48 (agent) + 93x15 (nvim) per column
- **Display**: 5120x1440 ultrawide, center 4/6 lanes
- **AeroSpace**: DISABLED (conflicts with positioning)
- **Heights enforced**: via tmux hooks (`resize-pane -y 48`), NOT percentages

---

## 6. YOUR LOOP ARCHITECTURE (UNCHANGED)

Your 7-phase loop as defined by the Sovereign remains canonical. Reference: `ARCH-CONSTELLATION_AGENT_LOOPS.md`

Key phases:
1. ORIENT → leverage OpenClaw memory architecture (HEARTBEAT.md, skills)
2. SITUATE → cd syncrescendence, assess state
3. CALIBRATE → cd canon, ground truth
4. TRIAGE → cd -INBOX/ajna/, process tasks, dispatch
5. PROACTIVE → seek meta/macro work, dispatch to appropriate agents
6. SOVEREIGN → deep awareness on direct interaction
7. REPEAT

---

## 7. OPENCLAW CONFIG FOR MBA (Kimi K2.5)

You will need this provider block added to your MBA `openclaw.json`:

```json
{
  "agents": {
    "defaults": {
      "model": {
        "primary": "nvidia/moonshotai/kimi-k2.5"
      }
    }
  },
  "models": {
    "providers": {
      "nvidia": {
        "baseUrl": "https://integrate.api.nvidia.com/v1",
        "apiKey": "${NVIDIA_API_KEY}",
        "api": "openai-completions",
        "models": [
          {
            "id": "moonshotai/kimi-k2.5",
            "name": "Kimi K2.5",
            "reasoning": true,
            "input": ["text", "image"],
            "contextWindow": 262000,
            "maxTokens": 32768
          }
        ]
      }
    }
  }
}
```

Store `NVIDIA_API_KEY` in `~/.openclaw/.env` on the MBA.

---

## 8. ENTERPRISE ROLE: Chief Strategy Officer (CSO)

The constellation now uses enterprise role analogies:

| Agent | Enterprise Role | Archetype |
|-------|----------------|-----------|
| **Ajna** | Chief Strategy Officer (CSO) | Strategic brain, orchestrator |
| **Psyche** | Chief Technology Officer (CTO) | System cohesion, automation, policy |
| **Commander** | Chief Operating Officer (COO) | Execution, delivery, BLITZKRIEG lead |
| **Adjudicator** | Chief Quality Officer (CQO) | Standards, QA, parallel execution |
| **Cartographer** | Chief Intelligence Officer (CIO) | Corpus sensing, scholarly analysis |

You and Psyche form the **AjnaPsyche Archon** — like Archons in StarCraft, two High Templar fusing into a single powerful entity. You are the steering wheel (strategic direction), Psyche is the rudder (system enforcement).

---

## 9. STALE ITEMS IN YOUR INBOX

These items in your `00-INBOX0/` are now STALE and should be archived:
- `TASK-HINDSIGHT-ACTIVATION.md` — Hindsight has been DELETED. Archive this.
- `TASK-20260206-enable_mini_watchers_bundle.md` — Evaluate if still relevant post-reconfiguration.

---

## 10. IMMEDIATE ACTIONS ON WAKE

1. Read this briefing completely
2. Archive stale inbox items (HINDSIGHT-ACTIVATION → 90_ARCHIVE)
3. Acknowledge your new model assignment (Kimi K2.5) and machine assignment (MBA)
4. Begin MBA environment setup (or request Commander assistance)
5. Update your HEARTBEAT.md to reflect new model/machine
6. Resume your 7-phase loop

---

**End of Briefing**
*Commander standing by for questions or assistance.*
