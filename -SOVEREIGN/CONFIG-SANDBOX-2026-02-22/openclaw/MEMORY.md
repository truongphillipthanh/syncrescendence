# Long-term Memory — Ajna (CSO)

## Identity
- You are Ajna, Chief Strategy Officer of the Syncrescendence Constellation
- You and Psyche form the AjnaPsyche Archon (fused executive brain)
- You are the steering wheel (strategy); Psyche is the rudder (enforcement)
- Model: Kimi K2.5 via NVIDIA NIM API

## Machine Assignment (CRITICAL — NEVER CONFUSE)
- /Users/system = MacBook Air = YOUR machine (Ajna)
- /Users/home = Mac mini = Psyche's machine (also Commander, Adjudicator, Cartographer)

## Infrastructure State (2026-02-16)

### Auto-Ingest Pipeline (OPERATIONAL)
- `auto_ingest_loop.sh` runs for all 5 agents on Mac mini
- Polls INBOX0 every 30s, dispatches to agent CLIs, manages full lifecycle
- Gemini/Cartographer uses headless mode: `gemini -p "prompt" -y -o text`
- All other agents use tmux send-keys dispatch
- Cross-machine delivery via SCP sling (SYNCRESCENDENCE_REMOTE_AGENT_HOST_* env vars)
- End-to-end pipeline PROVEN: dispatch → SCP → INBOX → auto-ingest → agent → RESULT → DONE → CONFIRM

### Constellation Watchdog (OPERATIONAL)
- `constellation_watchdog.sh` runs as launchd daemon on Mac mini (60s cycle)
- Monitors 4 tmux panes: Psyche (1.1), Commander (1.3), Adjudicator (1.5), Cartographer (1.7)
- Writes health to `00-ORCHESTRATION/state/DYN-CONSTELLATION_HEALTH.md`
- States: HEALTHY | IDLE | RATE_LIMITED | STALE | ERROR
- Uses login shell (`bash -l -c`) for tmux socket access from launchd context

### Agent Dispatch Modes
| Agent | Mode | Pane |
|-------|------|------|
| Commander | tmux send-keys | 1.3 |
| Adjudicator | tmux send-keys | 1.5 |
| Cartographer | Gemini headless | 1.7 (monitor) |
| Psyche | tmux send-keys | 1.1 |
| Ajna | filesystem + SCP | N/A (MBA) |

### Rate Limit Pools
- Psyche + Adjudicator share ChatGPT Plus — never dispatch simultaneous heavy jobs
- Cartographer on Gemini free-tier — quotas can hard-stop; stagger retries
- Commander on Claude Max — highest capacity
- Ajna on NVIDIA/Kimi K2.5 — monitor token budget

## Transition Record
- 2026-02-09: OpenClaw on MacBook Air configured for Ajna identity (CSO)
- 2026-02-09: Model set to nvidia/moonshotai/kimi-k2.5 (256K context, 1T MoE)
- 2026-02-16: Zero-offline hardening campaign — auto-ingest, watchdog, Gemini headless all deployed
- 2026-02-16: Psyche encoded operational knowledge into CLAUDE.md, AGENTS.md, COCKPIT.md, GEMINI.md
- 2026-02-16: Adjudicator completed adversarial zero-offline audit
- 2026-02-16: OpenClaw personality files hardened with operational awareness (this update)

## Neural Bridge State (2026-02-17)
- MBA → Mac mini SSH: OPERATIONAL (key: `id_ed25519_ajna`, alias: `mini`)
- Mac mini → MBA SSH: OPERATIONAL (key: `id_ed25519_ajna_to_psyche`, alias: `macbook-air`)
- Bidirectional SCP dispatch: OPERATIONAL
- CONFIRM SCP-back: OPERATIONAL (auto_ingest routes CONFIRMs to originator's machine)
- Watchdog SSH health check: OPERATIONAL (60s cycle, alerts on failure)
- ICMP ping: BLOCKED by macOS Stealth Mode (use SSH for health checks, never ping)

## Key Decisions
- 2026-02-05: OpenClaw installed with OpenAI provider and Slack channel
- 2026-02-09: AjnaPsyche Archon formalized — CSO+CTO enterprise roles assigned
- 2026-02-16: Gemini headless mode (`-p` flag) eliminates TUI limitation for Cartographer
- 2026-02-16: launchd watchdog requires `bash -l -c` (login shell) for tmux socket access
- 2026-02-16: dispatch.sh remote sling requires SYNCRESCENDENCE_REMOTE_AGENT_HOST_* env vars
- 2026-02-17: FileVault disabled, auto-boot + auto-login configured for zero-touch recovery
- 2026-02-17: Physical unplug test PASSED after 7-blocker hardening
- 2026-02-17: SSH Neural Bridge established — bidirectional, key-authenticated, config-aliased
- 2026-02-17: All 5 torture tests PASSED (tmux kill, Docker kill, loop kill, full kill, stale lock)

## Strategic Context
- The constellation is in Tier 1+ (reactive dispatch + autonomous ingest)
- Git concurrency protocol remains the critical gate before Tier 3
- Auto-ingest pipeline is the breakthrough enabling autonomous multi-agent execution
- All reconnaissance complete — pure execution phase
- Convergence vision: 28 domains, ~4955 lines (see CONVERGENCE-INTENT-TAXONOMY.md)
- Scaffold covers ~12% of convergence vision (correct: factory before product)

## Docker Services (Mac mini)
- Neo4j: port 7474
- Graphiti: port 8001
- Qdrant: port 6333
- Chroma: port 8765
- OpenClaw gateway: port 18789

## Corrections
- OpenClaw has no --skip-permissions flag; gateway handles permissions natively
- Use `openclaw tui --session main` to launch TUI
- Graphiti healthcheck is at /healthcheck (not /health)
- TMUX_TMPDIR for launchd must be `/private/tmp` (not `/private/tmp/tmux-501` — causes double nesting)
