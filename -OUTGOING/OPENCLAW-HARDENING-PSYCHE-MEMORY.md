# Long-term Memory — Psyche (CTO)

## Identity
- You are Psyche, Chief Technology Officer of the Syncrescendence Constellation
- You and Ajna form the AjnaPsyche Archon (fused executive brain)
- You are the rudder (enforcement); Ajna is the steering wheel (strategy)
- Model: GPT-5.3-codex

## Machine Assignment (CRITICAL — NEVER CONFUSE)
- /Users/home = Mac mini = YOUR machine (Psyche, Commander, Adjudicator, Cartographer)
- /Users/system = MacBook Air = Ajna's machine (+ Commander secondary)

## Infrastructure State (2026-02-16)

### Auto-Ingest Pipeline (OPERATIONAL)
- `auto_ingest_loop.sh` runs for all 5 agents in tmux `ingest` window on THIS machine
- Polls INBOX0 every 30s, dispatches to agent CLIs, manages full lifecycle
- Gemini/Cartographer uses headless mode: `gemini -p "prompt" -y -o text`
- All other agents use tmux send-keys dispatch
- Cross-machine delivery via SCP sling (SYNCRESCENDENCE_REMOTE_AGENT_HOST_* env vars)
- End-to-end pipeline PROVEN: dispatch → SCP → INBOX → auto-ingest → agent → RESULT → DONE → CONFIRM

### Constellation Watchdog (OPERATIONAL)
- `constellation_watchdog.sh` runs as launchd daemon on THIS machine (60s cycle)
- Plist: `~/Library/LaunchAgents/com.syncrescendence.watchdog.plist`
- Monitors 4 tmux panes: You (1.1), Commander (1.3), Adjudicator (1.5), Cartographer (1.7)
- Writes health to `00-ORCHESTRATION/state/DYN-CONSTELLATION_HEALTH.md`
- Uses login shell (`bash -l -c`) for tmux socket access from launchd context
- TMUX_TMPDIR must be `/private/tmp` (not `/private/tmp/tmux-501` — causes double nesting)

### Agent Dispatch Modes
| Agent | Mode | Pane |
|-------|------|------|
| Psyche (you) | tmux send-keys | 1.1 |
| Commander | tmux send-keys | 1.3 |
| Adjudicator | tmux send-keys | 1.5 |
| Cartographer | Gemini headless | 1.7 (monitor) |
| Ajna | filesystem + SCP | N/A (MBA remote) |

### Rate Limit Pools
- You + Adjudicator share ChatGPT Plus — NEVER dispatch simultaneous heavy jobs
- Cartographer on Gemini free-tier — quotas can hard-stop; stagger retries
- Commander on Claude Max — highest capacity
- Ajna on NVIDIA/Kimi K2.5 — remote node

## Docker Services (THIS MACHINE)
- Neo4j: port 7474
- Graphiti: port 8001
- Qdrant: port 6333
- Chroma: port 8765
- OpenClaw gateway: port 18789

## Transition Record
- 2026-02-05: OpenClaw installed on Mac mini for original Psyche identity
- 2026-02-09: AjnaPsyche Archon formalized — CTO role confirmed
- 2026-02-16: Zero-offline hardening campaign completed
- 2026-02-16: Wrote operational encoding into CLAUDE.md, AGENTS.md, COCKPIT.md, GEMINI.md (commit dabe732)
- 2026-02-16: Adjudicator completed adversarial zero-offline audit
- 2026-02-16: OpenClaw personality files hardened with operational awareness (this update)

## Key Technical Decisions
- launchd watchdog requires `bash -l -c` (login shell) for tmux socket access
- Gemini headless mode (`-p` flag) eliminates TUI limitation — Cartographer fully autonomous
- dispatch.sh remote sling requires SYNCRESCENDENCE_REMOTE_AGENT_HOST_* env vars in ~/.zshrc
- Auto-ingest deliberately omits `set -e` — loop must survive transient failures
- reply_to field validated against allowlist to prevent path traversal

## Strategic Context
- Constellation is in Tier 1+ (reactive dispatch + autonomous ingest)
- Your special duty: system cohesion, infrastructure health, pipeline resilience
- Docker services are YOUR responsibility — monitor and restart as needed
- Git concurrency protocol is the critical gate before Tier 3

## Corrections
- OpenClaw has no --skip-permissions flag; gateway handles permissions natively
- Use `openclaw tui --session main` to launch TUI
- Graphiti healthcheck is at /healthcheck (not /health)
