# OpenClaw Outfitment Sync (Ajna ↔ Psyche)

## Goal
Ajna (Mac mini, user `home`) and Psyche (MacBook Air, user `system`) should have **the same OpenClaw capability surface** (skills + plugins + core config scaffolding), while keeping **role-specific settings** and **secrets local**.

## Non-goals
- Do **not** copy API keys/tokens/bot secrets between machines via git.
- Do **not** make the repo depend on absolute paths inside `~/.openclaw/openclaw.json`.

## What counts as “outfitment” (sync)
1) **OpenClaw version** (keep aligned)
2) **Workspace skill packs** under `~/.openclaw/workspace/skills/` (e.g. `supermemory`, `hindsight` integration)
3) **plugins.load.paths** in OpenClaw config (so installed local skills are discoverable)
4) **Enabled/disabled plugin entries** (scaffolding, not secrets)
5) **LaunchAgents / watcher plists** for Syncrescendence (already split by host persona)

## What must remain per-host (do not sync)
- `env.vars` secrets: OPENAI_API_KEY, Slack tokens, gateway tokens, etc.
- `channels.*` provider credentials
- any machine-specific paths outside the agreed `~/Desktop/syncrescendence` repo root

## Proposed mechanism (canonical)
### A) Repo is the *blueprint*
Store a **redacted template** for OpenClaw config in repo:
- `00-ORCHESTRATION/openclaw/openclaw.template.json` (no secrets)
- optional `00-ORCHESTRATION/openclaw/openclaw.<persona>.json` overlays:
  - `openclaw.ajna.json` (bind loopback, different channel policies)
  - `openclaw.psyche.json`

Then provide an installer script that:
1) merges template + persona overlay + local secrets file
2) writes `~/.openclaw/openclaw.json`
3) restarts gateway

### B) Skills as vendored subtrees (best portability)
Prefer vendoring any non-core skills into the Syncrescendence repo *if they are small and license-clean*.

Note: some workspace skills are large (hundreds of MB). Vendoring them may be undesirable.

### C) Canonical interim: sync local workspace skills via rsync (no secrets)
Implemented:
- `00-ORCHESTRATION/scripts/sync_openclaw_skills.sh`
  - rsyncs an allowlist of skill/plugin directories
  - never touches `~/.openclaw/openclaw.json` or `~/.openclaw/credentials`
  - excludes `node_modules/` and `dist/`

This makes “same outfitment” a one-command pull on the mini whenever Psyche gains a capability.

## Verification (must-have receipts)
- `openclaw doctor --non-interactive` on both machines
- `openclaw plugins list` / `openclaw skills list` (or equivalent) and diffs
- A smoke task that uses a “non-default” skill on Ajna that previously only existed on Psyche.

## Current state
- Psyche has plugin installs for:
  - `openclaw-supermemory` (disabled)
  - `hindsight-openclaw` (disabled)
  - `memory-core` (enabled)
- Psyche loads plugin paths from:
  - `~/.openclaw/workspace/skills/supermemory`
  - `~/.openclaw/workspace/skills/hindsight/hindsight-integrations/openclaw`

Next: run Ajna audit + mirror.
