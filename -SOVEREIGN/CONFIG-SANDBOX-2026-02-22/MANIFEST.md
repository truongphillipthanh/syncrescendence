# CONFIG SANDBOX — 2026-02-22
## Complete Syncrescendence Configuration Inventory

**Generated**: 2026-02-22 | **Files**: 108 | **Size**: 780K
**Purpose**: Flat clone of every configuration surface across the constellation

---

## Directory Layout

```
root-platform/          Platform init files (repo root)
  CLAUDE.md             Claude Code constitutional law (v4.0.0)
  AGENTS.md             Codex CLI / Cursor / open-source agent init
  GEMINI.md             Gemini CLI init
  README.md             Constellation overview (formerly COCKPIT.md)
  Makefile              Build targets

agents/                 Per-agent office init files
  adjudicator/INIT.md   Codex CLI agent identity + protocols
  cartographer/INIT.md  Gemini CLI agent identity + protocols

dotfiles/               Repo dotfile directories
  claude/
    settings/           .claude/settings.json, local overrides, template
    commands/           9 slash commands (blitzkrieg, claresce, verify, etc.)
  gemini/
    GEMINI.md           .gemini/ mirror
    commands/           initialize.md
  github/
    CONNECTOR_PROTOCOL.md
    workflows/          lint.yml, verify.yml
  constellation/
    phase-specs/        README.md
    state/              current.yaml
    tokens/             active.json, active.txt
  obsidian/             5 JSON configs (app, appearance, core-plugins, graph, workspace)

git-config/             .gitignore, .gitattributes

openclaw/               ~/.openclaw/ (Ajna's OpenClaw on MBA)
  SOUL.md               Agent soul/personality
  AGENTS.md             Multi-agent routing config
  HEARTBEAT.md          Periodic reflection prompts
  MEMORY.md             Persistent memory
  USER.md               User profile
  openclaw.json         Main config (provider, model, extensions)
  .env.redacted         Environment variables (secrets stripped)
  exec-blocklist.json   Blocked commands

claude-user-config/     ~/.claude/settings.json (global user prefs)

ssh/                    ~/.ssh/config (Neural Bridge aliases: mini, macbook-air)

launchd/                ~/Library/LaunchAgents/ plists
  com.syncrescendence.git-sync.plist
  com.syncrescendence.skill-sync.plist
  com.syncrescendence.proactive-orchestrator.plist
  com.syncrescendence.youtube-ingest.plist

engine/                 02-ENGINE/ machine-readable configs
  yaml/                 DYN-COORDINATION, DYN-IIC_REGISTRY, TOOL-001..004, WF-001
  json/                 DYN-CONSTELLATION_CONFIGURATION, gemini-settings
  csv/                  DYN-ACCOUNTS, DYN-PLATFORMS, DYN-ROLES
  model-profiles/       MODEL-PROFILE-*.yaml (Claude, Gemini, GPT, Grok)
  capabilities/         CAP-001..005 (context, routing, retrieval, memory, automation)

skills/                 35 skill modules (SKILL.md each)
  audize, blitzkrieg_teams, brainstorming, claresce, commit-work,
  compact-wisdom, dispatching-parallel-agents, execute, google-ai-mode-skill,
  integrate, intentions, last30days, lastday, lastweek, listenize,
  mba-commander-init, memory-systems, mermaid-diagrams, method_kaizen,
  pedigree, plan, planning-with-files, readize, reviewtrospective,
  session-handoff, skill-judge, subagent-driven-development,
  systematic-debugging, tmux, transcribe_interview, transcribe_youtube,
  triage, update_agent_memory, update_universal_ledger,
  verification-before-completion, web-to-markdown
```

---

## What's NOT Included (by design)

- **OpenClaw backups** (`.bak` files) — historical, not active config
- **OpenClaw runtime dirs** (agents/, logs/, completions/, credentials/) — ephemeral state
- **Git history** — use repo for that
- **Script source code** — configs only, not executables
- **Secrets** — .env redacted, API keys stripped
- **Mac mini configs** — this sandbox is MBA-only; Mac mini has its own launchd plists, OpenClaw config, and SSH keys

## Notes

- OpenClaw `.env` is redacted — original at `~/.openclaw/.env`
- SSH config contains Neural Bridge aliases (`mini`, `macbook-air`) with key paths
- launchd plists reference scripts in `00-ORCHESTRATION/scripts/`
- Skills are resolved from symlinks — these are the actual SKILL.md content
