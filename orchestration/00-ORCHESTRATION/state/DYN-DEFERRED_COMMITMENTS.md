# Deferred Commitments Register
**Purpose**: Cross-session promise tracking. Checked at every Directive Initialization.
**Authority**: Commander (COO) / Sovereign-Commander Council 2026-02-23
**Created**: 2026-02-15
**Last Reviewed**: 2026-02-23
**Cadence**: on-change

> This file exists because 14+ "next session" commitments evaporated with a 14% delivery rate.
> Every agent checks this file at session start. No commitment disappears silently.
>
> **2026-02-23 RESET**: Overwritten by Sovereign directive after INT-2210 revert.
> Old commitments triaged against triangulated Oracle/Vanguard/Diviner architecture specs.
> Order of operations now reflects dependency chain, not wish list.

---

## Critical Path (Sequential — each phase unblocks the next)

### Phase 0: Infrastructure Alive (THIS SESSION)

| ID | Source | Commitment | Pri | Status | Target | Notes |
|----|--------|-----------|-----|--------|--------|-------|
| DC-100 | Council-23 | Fix Docker PATH on Mac mini, bring up Neo4j + Graphiti containers | P0 | OPEN | 2026-02-23 | Docker Desktop installed but CLI not in PATH. Neo4j/Graphiti DOWN. Memory arch dead without this. |
| DC-101 | Council-23 | Agent fleet audit: verify which tmux panes are functional, fix dead agents | P0 | OPEN | 2026-02-23 | 4 node panes + 4 nvim panes + 2 sleep panes visible. 3/5 agents unreliable (DC-005 legacy). |
| DC-102 | Council-23 | Graphiti health check: `curl http://localhost:8001/healthcheck` passes | P0 | OPEN | 2026-02-23 | Blocked by DC-100. Gate: no Phase 1 work until this returns 200. |

### Phase 1: Memory (THIS WEEK — Days 1-3)

| ID | Source | Commitment | Pri | Status | Target | Notes |
|----|--------|-----------|-----|--------|--------|-------|
| DC-110 | ARCH-MEMORY_ARCHITECTURE / Vanguard spec | Create per-agent memory layout: `agents/<name>/memory/{MEMORY.md,entities/,journal/,cache/,sync/}` | P0 | OPEN | 2026-02-25 | Directory creation only. No content migration. |
| DC-111 | ARCH-MEMORY_ARCHITECTURE / Vanguard spec | Build `scripts/memsync_daemon.py`: JSONL journal watcher → Graphiti `/messages` poster → outbox retry | P0 | OPEN | 2026-02-25 | Vanguard wrote the full spec (§3.1). Execute it. |
| DC-112 | ARCH-MEMORY_ARCHITECTURE / Vanguard spec | Add JSONL journal append to Commander's session hooks (extend `create_execution_log.sh`) | P0 | OPEN | 2026-02-25 | Record format defined in ARCH-MEMORY_ARCHITECTURE.md §Journal Record Format. |
| DC-113 | ARCH-MEMORY_ARCHITECTURE / Vanguard spec | Test write path end-to-end: Commander journal entry → memsync → Graphiti → entity materialized | P0 | OPEN | 2026-02-26 | Gate: no Phase 2 until this works. Vanguard provided bench_graphiti.py skeleton. |

### Phase 2: Antifragile Scaffold (NEXT WEEK — Days 4-7)

| ID | Source | Commitment | Pri | Status | Target | Notes |
|----|--------|-----------|-----|--------|--------|-------|
| DC-120 | Vanguard ANTIFRAGILE_SCAFFOLD | Install `scripts/scaffold_validate.sh` — structural integrity check (JSON output, pre-commit hookable) | P0 | OPEN | 2026-02-28 | Vanguard wrote complete script. Install, test, wire to pre-commit. |
| DC-121 | Vanguard ANTIFRAGILE_SCAFFOLD | Install `scripts/scaffold_heal.sh` — safe auto-repair (mkdirs, INIT templates, link fixes) | P0 | OPEN | 2026-02-28 | Depends on DC-120 (heal calls validate). |
| DC-122 | Oracle+Diviner ANTIFRAGILE_SCAFFOLD | Rename `praxis` → `praxis/` (Diviner consensus: "where theory meets friction of reality") | P1 | OPEN | 2026-03-01 | Oracle recommended `playbook`, Diviner reasoned `praxis`. Sovereign to decide. Do NOT rename numbered dirs yet — only sigma. |
| DC-123 | Vanguard ANTIFRAGILE_SCAFFOLD | Install `scripts/scaffold_rename.sh` for future numbered→semantic migration | P1 | OPEN | 2026-03-01 | Script ready. Do NOT execute until memory is working and scaffold_validate passes. The INT-2210 disaster was running this prematurely. |
| DC-124 | Oracle SCAFFOLD_CONSENSUS | Convert top 10 ARCH-* files to ADR format (ADR-0001 through ADR-0010) | P1 | OPEN | 2026-03-01 | Oracle REPO-003 spec. Standardized template with context/decision/status/consequences. |

### Phase 3: Automations + Sensing (WEEK 2 — Days 8-14)

| ID | Source | Commitment | Pri | Status | Target | Notes |
|----|--------|-----------|-----|--------|--------|-------|
| DC-130 | INT-1612 / DC-006 legacy | Cockpit activation: test and turn on the 16-min HQ + 30-min Phase 0 startup sequence | P0 | OPEN | 2026-03-03 | "Configured but never turned on." Requires agents alive (Phase 0) + memory working (Phase 1). |
| DC-131 | ARCH-MEMORY_ARCHITECTURE Phase 2 | Patch Graphiti server with `POST /triples` endpoint for deterministic edge writes | P1 | OPEN | 2026-03-05 | Vanguard wrote exact Python code (§1.5). Unlocks conflict resolution + ownership edges. |
| DC-132 | ARCH-MEMORY_ARCHITECTURE Phase 2 | Backfill existing MEMORY.md + entity pages into Graphiti | P1 | OPEN | 2026-03-05 | Vanguard provided `backfill_memory_md.py` skeleton. |
| DC-133 | ARCH-MEMORY_ARCHITECTURE Phase 2 | Add Graphiti query tools to agent harnesses via *-EXT.md | P1 | OPEN | 2026-03-05 | Enables read path: agent → graph → cache → file fallback. |
| DC-134 | DC-010 legacy | Live Ledger sensing Phases 2-4: cron-dispatched intelligence, MODEL-INDEX refresh | P1 | OPEN | 2026-03-07 | 12 DYN-LEDGER files created. Automation layer missing. |
| DC-135 | Diviner ANTIFRAGILE_SCAFFOLD | Root `.obsidian/` stub + README note "Open repo root as Obsidian vault" | P2 | OPEN | 2026-03-07 | Oracle+Diviner both recommend. Trivial. |

### Phase 4: Hardening + Scale (30 DAYS)

| ID | Source | Commitment | Pri | Status | Target | Notes |
|----|--------|-----------|-----|--------|--------|-------|
| DC-140 | DC-002 legacy | Security audit of 234+ skills: credential exfiltration risk assessment | P0 | OPEN | 2026-03-10 | P0-CRITICAL. Deferred from 2026-02-17. Cannot ship anything external without this. |
| DC-141 | DC-003 legacy | API key rotation: plaintext keys in openclaw.json (NVIDIA, OpenAI, Slack, Discord) | P0 | OPEN | 2026-03-10 | Sovereign action required. |
| DC-142 | ARCH-MEMORY_ARCHITECTURE Phase 3 | Memory compaction job (weekly per agent) + conflict detection protocol | P1 | OPEN | 2026-03-15 | |
| DC-143 | ARCH-MEMORY_ARCHITECTURE Phase 3 | Cross-machine sync testing (MBA ↔ Mac mini via git + Graphiti) | P1 | OPEN | 2026-03-15 | |
| DC-144 | Diviner MEMORY_ARCHITECTURE | Evaluate "Memory Agent" daemon (topological observer — the Sixth Agent) | P2 | OPEN | 2026-03-20 | Diviner's subconscious agent. PageRank, community detection over shared graph. |
| DC-145 | Diviner ANTIFRAGILE_SCAFFOLD | Quarantine/limbo namespace for anomalous artifacts + promotion algorithm | P2 | OPEN | 2026-03-20 | Structural mutagenesis. Tracks desire paths. |
| DC-146 | DC-123 gate | Execute numbered→semantic directory rename (ONLY after validate passes + memory works) | P2 | OPEN | 2026-03-20 | The rename that INT-2210 botched. This time: scaffold_validate PASSES first, memory persists the decision, rollback tested. |

---

## Parked (Valid but not on critical path)

| ID | Source | Commitment | Pri | Status | Notes |
|----|--------|-----------|-----|--------|-------|
| DC-P01 | DC-004 legacy | Rosetta Stone expansion: ~25 ontological terms | P1 | PARKED | 30 min work. Do during any session lull. |
| DC-P02 | DC-008 legacy | SYN-51/53 (Jira/Todoist integration) | P1 | PARKED | Linear items. Not on infrastructure critical path. |
| DC-P03 | DC-011 legacy | CANON annotations: Physics/Three-Pillar on CANON-30300+ | P1 | PARKED | 1 of 3 done. Content work, not infrastructure. |
| DC-P04 | DC-012 legacy | Document formalization: promote clarescence decisions to ARCH-/REF- docs | P1 | PARKED | Systemic gap (17% delivery). Fix memory first — then docs stop evaporating. |
| DC-P05 | DC-013 legacy | Protocol changes to CLAUDE.md: 4 proposed, 0 enacted | P1 | PARKED | Will be addressed as part of scaffold tightening (Phase 2). |
| DC-P06 | DC-014 legacy | MCP server activation on MBA (Linear) | P1 | PARKED | OAuth flow needs Sovereign. Not blocking. |
| DC-P07 | DC-015 legacy | SOVEREIGN queue drain: 13 items | P1 | PARKED | Requires focused Sovereign decision sprint. |
| DC-P08 | INT-1803 | Open model onboarding (Cline + OpenCode) | P2 | PARKED | Cline installed, never configured. Needs stable Tier 1-3 agents first. |
| DC-P09 | INT-2101/2102 | Dual-stream intelligence architecture + 3-tier consumption model | P2 | PARKED | Depends on Google Account 2, NotebookLM, memory working. |
| DC-P10 | INT-2108 | Three-track evaluation framework (onboard/white-label/verticalize) | P2 | PARKED | Framework designed. Operationalize after scaffold stable. |

---

## Completed / Dropped

| ID | Source | Commitment | Status | Resolved | Notes |
|----|--------|-----------|--------|----------|-------|
| DC-001 | CLAR-0212-triple-pass | Hard-gate skills in CLAUDE.md (DEC-C3) | DONE | 2026-02-15 | Enacted in CLAUDE.md |
| DC-007 | CLAR-0212-pulse-check | Cross-session promise tracking mechanism | DONE | 2026-02-15 | This file |
| DC-009 | CLAR-0208 | TERMINAL-STACK-CONFIG.md reference resolution | DONE | 2026-02-15 | Created REF-TERMINAL_STACK_CONFIG.md |
| DC-005 | CLAR-0209/0212 | Agent fleet remediation (original) | SUPERSEDED | 2026-02-23 | Replaced by DC-101 with ground truth from tmux audit |
| DC-006 | CLAR-0208 | Cockpit activation (original) | SUPERSEDED | 2026-02-23 | Replaced by DC-130 with correct dependency chain |
| DC-010 | CLAR-0209 | Live Ledger sensing (original) | SUPERSEDED | 2026-02-23 | Replaced by DC-134 with correct phase gating |

---

## Protocol

### At Session Start (Directive Initialization)
1. Read this file after the inbox scan (step 1.5 in Directive Initialization Protocol)
2. Identify the LOWEST-NUMBERED OPEN item — that is the current work
3. Do NOT skip phases. Each phase gates the next.

### During Execution
4. Update Status to IN_PROGRESS when starting, DONE when verified complete
5. New commitments append to the correct phase, not the bottom

### Phase Gate Rule (NEW — 2026-02-23)
**No phase may begin until all P0 items in the prior phase are DONE.**
This is the rule that prevents the INT-2210 pattern: running rename before validate exists, running scaffold triage before memory works.

---

## Metrics

- **Total**: 27 commitments (16 active + 10 parked + 1 superseded batch)
- **Phase 0**: 3 OPEN | **Phase 1**: 4 OPEN | **Phase 2**: 5 OPEN | **Phase 3**: 6 OPEN | **Phase 4**: 7 OPEN
- **Delivery rate at reset**: 14% (unchanged — this is what we're fixing)
- **Target delivery rate**: >80% within 30 days

---

*This file is living infrastructure (DYN- prefix). Do not delete or archive. Compact the Completed/Dropped table quarterly.*
