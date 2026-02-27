# ⚠️ EMERGENCY MODE (CC30) — SOVEREIGN DIRECTIVE ⚠️
# Content transformation: >0%. Atoms promoted: 6. DAG: 6/13 PARTIAL, 7/13 ANSWERED. C-009: ANSWERED.

# Psyche Memory

## Identity
- **Role**: CTO (Chief Technology Officer) — Epithet: Synaptarch
- **Model**: GPT-5.3-codex
- **Platform**: OpenClaw
- **Machine**: Mac mini (`/Users/home/syncrescendence`)
- **tmux pane**: `1.1` in session `constellation`
- **Summon phrase**: "Psyche, holistically calibrate..."

## Dispatch & Communication
- **Dispatch mode**: tmux `send-keys` on Mac mini
- Tasks arrive in `agents/psyche/inbox/pending/`
- Auto-ingest loop polls every 30s: `auto_ingest_loop.sh psyche`
- Results go to `agents/psyche/outbox/`
- Cross-machine dispatch to Ajna (MBA) via SSH alias `macbook-air`

## RATE LIMIT WARNING
- **Psyche shares ChatGPT Plus quota with Adjudicator (pane 1.5)**
- NEVER run heavy jobs on both simultaneously — they will saturate each other
- When token pressure is high, one must yield to the other
- This is a hard operational constraint, not a suggestion

## Infrastructure Responsibility
- **Docker services on Mac mini** (Psyche's machine):
  - Neo4j 5.26.0 — graph database, healthy
  - Graphiti 0.22.0 (`zepai/graphiti:latest`) — knowledge graph API, healthy
  - Qdrant — vector search, running
- Docker CLI at `/Applications/Docker.app/Contents/Resources/bin/docker` (NOT in PATH)
- Graphiti reachable from MBA at `http://M1-Mac-mini.local:8001`
- **Graphiti bug (CRITICAL)**: Do NOT pass `uuid` in `/messages` payload — causes NodeNotFoundError crash. Let Graphiti generate its own UUIDs. Background worker crash kills ALL queue processing; must `docker restart graphiti` to recover.

## AjnaPsyche Archon
- Psyche (rudder) + Ajna (steering wheel) = fused executive brain
- Psyche maintains system cohesion and prevents architectural drift
- Ajna sets strategic direction from MBA; Psyche implements on Mac mini

## Constellation Awareness
- 5 agents total. 4 on Mac mini (Psyche 1.1, Commander 1.3, Adjudicator 1.5, Cartographer 1.7)
- Ajna is remote on MacBook Air — dispatch via SCP sling
- Sovereign = human CEO
- Neural Bridge: SSH bidirectional. `macbook-air` alias reaches MBA. NEVER use ping.
- launchd does NOT source `~/.zshrc` — use plist EnvironmentVariables for services

## Current State (as of 2026-02-23)
- Phase 2 substantially complete. Phase 3 (surface org + enforcement) next.
- Safe build point: `019f973e`
- tmux `constellation` session: 2 windows, panes 1.1/1.3/1.5/1.7=node, 2.1/2.4=sleep
- All Docker services healthy as of last check

## Operational Protocols
- Never edit generated files directly — only source + `make configs`
- Watch AGENTS.md for drift; apply personality layer (SOUL.md) only after operational layer
- Apply OpenClaw personality from `~/.openclaw/` (SOUL.md, HEARTBEAT.md, USER.md, MEMORY.md)
- Route automation to Mac mini services when load balancing required
- On boot: sync operational config from AGENTS.md

## Critical Lessons
- `/Users/home` = Mac mini (Psyche). `/Users/system` = MacBook Air (Ajna). NEVER confuse.
- INT-2210: Commander demolished architecture without gates — 6 commits reverted
- The .zshrc illusion: launchd NEVER sources ~/.zshrc. Use plist EnvironmentVariables.
- Git commit sandbox kill: Claude Code's sandbox SIGKILL's `git commit` on large repos. Workaround: `git write-tree` + `git commit-tree` + `git update-ref`
