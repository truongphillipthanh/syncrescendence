# HANDOFF: Council 22 → Next Session
**Date**: 2026-02-23
**Safe Build**: `85140aff` (if anything goes wrong: `git reset --hard 85140aff`)
**Backup of reverted work**: branch `backup-pre-revert-2026-02-22`

---

## What Just Happened

Council 22 was a recovery session. Commander botched a scaffold triage (INT-2210: 6 commits that deleted 3,966 lines of architectural docs and renamed every directory without validation infrastructure). Sovereign ordered a hard revert to `d33aaf13`, then directed a clean rebuild:

1. Wrote `canon/CANON-25500-ARCHITECTURE_RATIONALE-lattice.md` — comprehensive zero-loss reconstruction guide covering the entire 22-day arc, memory architecture, scaffold architecture, and how to rebuild from scratch
2. Rewrote `orchestration/state/DYN-DEFERRED_COMMITMENTS.md` — phased execution plan with gate rules
3. Updated `orchestration/state/ARCH-INTENTION_COMPASS.md` — v3.4.0 with Council 22 session
4. Performed semantic directory rename (properly this time): `00-ORCHESTRATION` → `orchestration`, `01-CANON` → `canon`, `02-ENGINE` → `engine`, `04-SOURCES` → `sources`, `05-SIGMA` → `praxis`. All ~1700 internal references rewritten. Zero deletions.
5. Updated `AGENTS.md` to v6.0.0 with semantic directory rules and phase gate rule
6. Copied antifragile scaffold archive from Desktop into `-SOVEREIGN/antifragile-scaffold-archive/`
7. Regenerated `CLAUDE.md` and `GEMINI.md` via `make configs`

---

## Current State

### Infrastructure
- **Mac mini**: reachable via `ssh mini`. tmux `constellation` session alive (2 windows).
- **Docker**: Desktop installed but **CLI not in PATH**. Zero containers running. **Neo4j and Graphiti are DOWN.**
- **Agents**: Panes 1.1/1.3/1.5/1.7 = `node` (OpenClaw), 1.2/1.4/1.6/1.8 = `nvim`, 2.1/2.4 = `sleep` (dead agents). 3/5 agents unreliable.

### Architecture
- Semantic directory rename complete. All refs updated.
- Memory architecture DECIDED (triangulated by Oracle/Vanguard/Diviner) but **0% executed**.
- Antifragile scaffold scripts written by Vanguard but **not installed**.
- 14% deferred commitment delivery rate.

---

## YOUR DIRECTIVE: Execute Phase 0 (Infrastructure Alive)

### DC-100: Fix Docker PATH on Mac mini
```bash
ssh mini
# Find Docker CLI
ls /Applications/Docker.app/Contents/Resources/bin/docker
# Add to PATH permanently
echo 'export PATH="/Applications/Docker.app/Contents/Resources/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
# Verify
docker --version
docker ps
```
If Docker Desktop is not running, open it:
```bash
open -a Docker
```

### DC-101: Agent fleet audit
```bash
ssh mini
export PATH=/opt/homebrew/bin:$PATH
tmux list-panes -a -F '#{session_name}:#{window_index}.#{pane_index} #{pane_current_command} #{pane_pid}'
```
Determine: which panes are Commander, Psyche, Adjudicator, Cartographer? Which are alive vs dead (`sleep`)? Document findings.

### DC-102: Graphiti health check
After Docker is running with Neo4j + Graphiti containers:
```bash
curl -sS http://localhost:8001/healthcheck
```
**GATE**: Phase 1 does not begin until this returns 200.

---

## After Phase 0: Phase 1 (Memory)

Read the full spec: `orchestration/state/ARCH-MEMORY_ARCHITECTURE.md`

1. **DC-110**: Create per-agent memory layout: `agents/<name>/memory/{MEMORY.md,entities/,journal/,cache/,sync/}`
2. **DC-111**: Build `scripts/memsync_daemon.py` per Vanguard spec in `-INBOX/commander/00-INBOX0/RESPONSE-VANGUARD-MEMORY_ARCHITECTURE_ENGINEERING.md` §3.1
3. **DC-112**: Add JSONL journal append to Commander's session hooks
4. **DC-113**: Test write path end-to-end: journal → memsync → Graphiti → entity materialized

**GATE**: Phase 2 does not begin until DC-113 works.

---

## Key Files to Read First

| Priority | File | Why |
|----------|------|-----|
| 1 | `AGENTS.md` | Constitutional law v6.0.0 |
| 2 | `orchestration/state/ARCH-INTENTION_COMPASS.md` | All Sovereign intentions (v3.4.0) |
| 3 | `orchestration/state/DYN-DEFERRED_COMMITMENTS.md` | Phased execution plan |
| 4 | `orchestration/state/ARCH-MEMORY_ARCHITECTURE.md` | Memory spec (execute this) |
| 5 | `canon/CANON-25500-ARCHITECTURE_RATIONALE-lattice.md` | Full reconstruction guide |
| 6 | `-INBOX/commander/00-INBOX0/RESPONSE-VANGUARD-MEMORY_ARCHITECTURE_ENGINEERING.md` | Exact code for memsync daemon |

---

## Rules (SEARED)

1. **Phase gates are constitutional.** Infrastructure → Memory → Scaffold → Automations → Hardening. No skipping.
2. **Delete nothing.** The INT-2210 disaster was caused by treating "triage" as "redesign." Archive, don't delete.
3. **Triangulated specs are execution-ready.** Oracle/Vanguard/Diviner converged on memory architecture. Don't redesign it. Execute it.
4. **Git plumbing for large commits.** `git write-tree` → `git commit-tree` → `git update-ref`. The sandbox kills `git commit` on 1700+ files.
5. **SSH not ping.** Both machines have Stealth Mode. `ssh mini hostname` for health checks.
6. **launchd ignores .zshrc.** Use plist EnvironmentVariables for service env vars.

---

## What Success Looks Like

At the end of the next session:
- Docker running on Mac mini with Neo4j + Graphiti containers
- `curl http://localhost:8001/healthcheck` returns 200
- Agent fleet documented (which panes = which agents, alive vs dead)
- If time permits: Phase 1 memory layout created (`agents/*/memory/` structure)

This is execution work. The architecture is done. Build the thing.
