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

## 2026-02-06 (Tranche A) — Four-Systems operationalization

### P0
- IMPL-A-0019 — System 4 triage & qualification SOP + schema (signal_tier, value_modality)

### P1
- IMPL-A-0016 — System 1 scheduled monitoring runner + brief artifact output
- IMPL-A-0017 — System 2 ‘save-to-queue’ capture protocol + processor to 04-SOURCES/processed/
- IMPL-A-0021 — Executable interaction state machine (entrypoints → triage → route)

### P2
- IMPL-A-0018 — Research packet template + tool routing rules (System 3)
- IMPL-A-0020 — Value-modality decision tree → processing function mapping
- IMPL-A-0023 — DecisionAtom: automation substrate (launchd/cron vs n8n vs OpenClaw cron)
- IMPL-A-0025 — Verify/create missing cross-ref docs (SOURCES_SCHEMA/TRIAGE_PROTOCOL/PROCESSING_ROUTING)
- IMPL-A-0026 — Operator command reference / make targets per system

### P3
- IMPL-A-0022 — Automation milestones (M0→M2) + acceptance tests per system
- IMPL-A-0024 — System↔IIC stream mapping (default recipients, cadence, SLA)

## 2026-02-06 (Tranche B) — Twin coordination + Intent Compass mechanics + Dispatch Kanban

### P0
- IMPL-B-0009 — Establish -OUTBOX/<agent>/ structure + align watcher RESULT receipts + relay rule to -OUTGOING
- IMPL-B-0010 — Kanban schema linter: Kind gating + header validation (safety rail)

### P1
- IMPL-B-0006 — Intent Compass triage SOP (queue → compass flush semantics + cadence)
- IMPL-B-0001 — Sovereign contact rules as enforceable decision gate (notify reason required)
- IMPL-B-0012 — Wrong-agent prevention: enforce To + Claimed-By hostname + stale-claim scan

### P2
- IMPL-B-0002 — Durable TWIN handoff surface + indexing/ledger for twin relays
- IMPL-B-0004 — TWIN-UPDATE template + linter
- IMPL-B-0007 — INT ID generator/authority + uniqueness enforcement
- IMPL-B-0008 — Compass resolution requires evidence/integrated_into
- IMPL-B-0011 — Ledger policy for lifecycle completeness (add BLOCKED/WAITING if needed)
- IMPL-B-0005 — make twin-heartbeat command that emits update stub
- IMPL-B-0003 — Psyche contribution protocol (PATCH bundles/branches; Ajna commits)

## 2026-02-06 (Tranche C) — Canon hotspots: multi-agent orchestration + memory systems + tech stack DB

### P0
- IMPL-C-0012 — Tech Stack DB migration execution + integrity checks + receipt
- IMPL-C-0006 — Memory taxonomy mapping to concrete repo artifacts (working/episodic/semantic/procedural/prospective)

### P1
- IMPL-C-0001 — Orchestration-patterns → Syncrescendence mapping + router
- IMPL-C-0005 — Progressive trust ladder for lanes (allowed actions + promotion criteria)
- IMPL-C-0010 — Memory verification gates + stale/deprecated markers + re-verify policy

### P2
- IMPL-C-0002 — DecisionAtom: default collaboration topology + allowed deviations/triggers
- IMPL-C-0003 — Protocol posture: MCP vs A2A vs filesystem kanban (security + roadmap)
- IMPL-C-0004 — Message schema headers integrated into TASK header format
- IMPL-C-0007 — Context engineering policy (chunking/relevance/decay/summarization)
- IMPL-C-0008 — Sleep-time compute jobs (cron/launchd) for memory maintenance
- IMPL-C-0011 — Memory security policy (PII handling + audit)
- IMPL-C-0013 — Minimal Tech Stack DB CLI for search/routing/compare

### P3
- IMPL-C-0009 — Memory interface operations (write/read/update/forget) with logging
- IMPL-C-0014 — Tech Stack DB maintenance cadence as jobs
- IMPL-C-0015 — Tech Stack DB acceptance tests + metrics report

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
- IMPL-D-0059 — watch_canon regen log writes actual regenerated CANON IDs
- IMPL-D-0060 — Ledger REGEN events emitted by watch_canon (include IDs + trigger)
- IMPL-D-0062 — watch_canon concurrency lock (avoid overlapping regen)

### P1
- IMPL-D-0052 — Enforce Kind gating (TASK/SURVEY/PATCH only)
- IMPL-D-0053 — RESULT path determinism (prefer Expected Output header)
- IMPL-D-0054 — Log hygiene: no long-form diagnostics in watcher stderr

### P1
- IMPL-D-0067 — Makefile verify/update-ledgers: existence checks + align with verify_all
- IMPL-D-0065 — verify_all.sh: fix root .md allowance mismatch + explicit allowlist

### P2
- IMPL-D-0056 — watch_canon --diagnose (missing watch_paths detection)
- IMPL-D-0061 — watch_canon --diagnose mode (missing watch_paths detection + nonzero on critical missing)
- IMPL-D-0057 — make ops-health aggregator target
- IMPL-D-0068 — make ops-health: lint + verify-full + watcher_health (when available)
- IMPL-D-0069 — make canon-watch / canon-watch-once targets
- IMPL-D-0063 — ops_lint: validate kind/id conventions + YAML parse
- IMPL-D-0064 — ops_lint: detect duplicate ids across artifacts
- IMPL-D-0066 — verify_all.sh hardening: set -euo pipefail + missing-file resilience
- IMPL-D-0070 — verify JSON output mode for dashboards/health checks
- IMPL-D-0058 — Kanban protocol: integration hooks section (SaaS subscriptions)
