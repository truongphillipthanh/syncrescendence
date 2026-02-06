# IMPLEMENTATION-BACKLOG.md

> Queue of implementation paths (normalized) ready to map into Linear.
> Source of truth remains the repo; Linear is an execution surface.

## 2026-02-05 (Tranche A)

### P0
- IMPL-A-0008 — CANON-31150 rewrite (platform catalog expanded + deconflated)
- IMPL-A-0010 — DYN-TOOLCHAIN_INTERACTION_PROTOCOL.md
- IMPL-A-0002 — Chorus vs Medley correction (COCKPIT)

### P1
- IMPL-A-0001 — Fix outdated extended thinking guidance (CLAUDE.md)
- IMPL-A-0004 — Self-healing constitution hook
- IMPL-A-0005 — Git worktree isolation as canonical parallelism
- IMPL-A-0007 — Ralph Pattern implementation verification + canonical doc

### P2
- IMPL-A-0006 — Skill subagent delegation (`context: fork` guidance)
- IMPL-A-0009 — Missing avatar specs (OpenClaw / Commander)
- IMPL-A-0014 — MCP buildout plan (Slack/Linear)
- IMPL-A-0015 — Velocity management rules + budget alerts

### P3
- IMPL-A-0012 — Linear reconciliation design + sync spec
- IMPL-A-0013 — FDIS requirements + deployment surface

## 2026-02-06 (Tranche D) — Always-on watchers readiness

### P0
- IMPL-D-0036 — Watchers must auto-write RESULT receipts to -OUTGOING (durable proof of execution)
- IMPL-D-0037 — Unblock mini executors: install OpenClaw, fix Codex auth, resolve Claude billing for Commander

### P1
- IMPL-D-0038 — watcher_health.sh (launchctl+env+binary+log+ledger health report)
- IMPL-D-0039 — Align dispatch task contract vs watcher behavior (RESULT vs logs)
- IMPL-D-0041 — Self-test/precheck at watcher start (prevent false "running" health)

### P2
- IMPL-D-0040 — Standardize NODE_OPTIONS/NODE_NO_WARNINGS across watcher plists (mini + psyche)
- IMPL-D-0034 — Two-set watcher plist install (mini/home vs psyche/system) kept deterministic
- IMPL-D-0035 — Mini home base path hardcode to /Users/home (policy)


## 2026-02-06 (Tranche D) — Outfitment sync (Ajna ↔ Psyche)

### P0
- IMPL-D-0044 — SSH alias + host-key pinning procedure for Ajna↔Psyche (unblock rsync sync)
- IMPL-D-0045 — Fix Ajna OAuth dir missing (~/.openclaw/credentials) and add preflight

### P1
- IMPL-D-0047 — Deterministic parity smoke test: invoke workspace skill on Ajna and return PASS/FAIL receipt
- IMPL-D-0046 — Make sync_openclaw_skills.sh robust across remote usernames/paths (flags + receipts)

### P2
- IMPL-D-0049 — rearm_watchers verification step prints resolved paths + loaded labels
- IMPL-D-0048 — Add BLOCKED status / classifier to watcher lifecycle to distinguish env blockers from task failure
- IMPL-D-0050 — Ajna git stash hygiene: audit + policy


## 2026-02-06 (Tranche D) — Kanban + watcher hardening follow-ons

### P0
- IMPL-D-0051 — Executor wall-clock timeout + BLOCKED classification + RESULT on timeout
- IMPL-D-0055 — Truthful CANON regen log (actual IDs) + ledger REGEN events

### P1
- IMPL-D-0052 — Enforce Kind gating (TASK/SURVEY/PATCH only)
- IMPL-D-0053 — RESULT path determinism (prefer Expected Output header)
- IMPL-D-0054 — Log hygiene: no long-form diagnostics in watcher stderr

### P2
- IMPL-D-0056 — watch_canon --diagnose (missing watch_paths detection)
- IMPL-D-0057 — make ops-health aggregator target
- IMPL-D-0058 — Kanban protocol: integration hooks section (SaaS subscriptions)
