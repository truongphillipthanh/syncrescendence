# Deferred Commitments Register
**Purpose**: Cross-session promise tracking. Checked at every Directive Initialization.
**Authority**: Commander (COO) / Sovereign-Commander Council 2026-02-23
**Created**: 2026-02-15
**Last Reviewed**: 2026-02-23
**Cadence**: on-change

> This file exists because 14+ "next session" commitments evaporated with a 14% delivery rate.
> Every agent checks this file at session start. No commitment disappears silently.

---

## Critical Path (Sequential — each phase unblocks the next)

### Phase 0: Infrastructure Alive — ✅ DONE (2026-02-23)

| ID | Source | Commitment | Pri | Status | Notes |
|----|--------|-----------|-----|--------|-------|
| DC-100 | Council-23 | Fix Docker PATH on Mac mini, bring up Neo4j + Graphiti containers | P0 | **DONE** | Docker, Neo4j 5.26.0, Graphiti 0.22.0, Qdrant all healthy. |
| DC-101 | Council-23 | Agent fleet audit: verify tmux panes, fix dead agents | P0 | **DONE** | Fleet audited. SSH bridge verified. |
| DC-102 | Council-23 | Graphiti health check passes | P0 | **DONE** | Reachable from MBA at `http://M1-Mac-mini.local:8001`. |

### Phase 1: Memory — ✅ DONE (2026-02-23, safe build point `5a26d8f8`)

| ID | Source | Commitment | Pri | Status | Notes |
|----|--------|-----------|-----|--------|-------|
| DC-110 | Vanguard spec | Per-agent memory layout for all 5 agents | P0 | **DONE** | All agents have `memory/{MEMORY.md,entities/,journal/,cache/,sync/}`. |
| DC-111 | Vanguard spec | memsync daemon: JSONL watcher → Graphiti poster | P0 | **DONE** | `memsync_daemon.py` operational. |
| DC-112 | Vanguard spec | JSONL journal append in Commander session hooks | P0 | **DONE** | Deterministic UUIDs. |
| DC-113 | Vanguard spec | End-to-end write path verified | P0 | **DONE** | Commander journal → memsync → Graphiti → entity materialized. |
| DC-114 | Phase 1 hardening | Persist Graphiti `/triples` patch permanently | P1 | OPEN | Does not block Phase 2. |
| DC-115 | Phase 1 hardening | Permanent API key wiring for Graphiti/Neo4j | P1 | OPEN | Does not block Phase 2. |

### Phase 2: Deep Architectural Audit — ⬛ IN PROGRESS

#### 2A — Inventory + Inspection (DC-200–203) — ✅ DONE

| ID | Source | Commitment | Pri | Status | Notes |
|----|--------|-----------|-----|--------|-------|
| DC-200 | Commander | Exhaustive file index across all directories | P0 | **DONE** | 825 files indexed. |
| DC-201 | Oracle (Grok) | orchestration/ deep inspection (642 files) | P0 | **DONE** | 4 response files. Per-file verdicts. |
| DC-202 | Oracle (Grok) + Cartographer (Gemini) | engine/ deep inspection (147 files) | P0 | **DONE** | Oracle: 6 sessions. Cartographer: LOW confidence, superseded. |
| DC-203 | Adjudicator (Codex) | praxis/ deep inspection (36 files) | P0 | **DONE** | 2 sessions. Per-file + per-paragraph verdicts. |

#### 2B — Synthesis + Architectural Decisions (DC-204, DC-207) — ✅ DONE

| ID | Source | Commitment | Pri | Status | Notes |
|----|--------|-----------|-----|--------|-------|
| DC-204 | Commander synthesis | Coherence synthesis: triangulate all inspection results | P0 | **DONE** | 825 files: 675 CANONICAL, 24 STALE, 25 ORPHANED, 15 MISCLASSIFIED. |
| DC-204T | Oracle + Sovereign | Structural decisions: sanctify 00-/02-/05- + stub 4 missing files | P0 | **DONE** | All 4 decisions approved (a,a,a,c). Committed `d2b888d0`. |
| DC-204E | Oracle (Grok) | Industry consensus on 7 architectural patterns | P0 | **DONE** | 5 recommendations. "Clearest sovereign-first agent OS." |
| DC-204D | Diviner (Gemini) | Cross-disciplinary synthesis: FEP, jamming transition, 3 predictions | P0 | **DONE** | Scientific frameworks + falsifiable hypotheses. |
| DC-204-COMPILE | Commander | Compiled schematic: Oracle+Diviner → 5 engineering specs | P0 | **DONE** | `RESULT-COMMANDER-DC204-COMPILED_SCHEMATIC.md` |
| DC-204-ADJ | Adjudicator (Codex) | Engineering review: feasibility, blueprints, failure modes | P0 | **DONE** | Verdicts: A(BUILD), B(REDESIGN), C(DEFER), D(BUILD), E(DEFER). First full playbook cycle complete. |
| DC-207 | — | Open architectural questions (engine/praxis consolidation, -INBOX restructuring) | P1 | RESOLVED | Answered by DC-204T: sanctify, don't restructure. |

#### 2C — Content Decruft + Source Mining (DC-205, DC-208) — ⬜ NEXT

| ID | Source | Commitment | Pri | Status | Notes |
|----|--------|-----------|-----|--------|-------|
| DC-205 | Phase 2C | Sentence-by-sentence action on every file: canonical stays, stale archives, orphans wire or archive | P0 | OPEN | T1/T2 tightening (partial) done. Full decruft remains. |
| DC-208 | Phase 2C | Source mining: extract unmined wisdom from sources/, flow through journal → memsync → Graphiti | P1 | OPEN | Sources <2% mined per Oracle/Diviner. Pipeline: sources → engine → praxis → canon. |

#### 2D — Triangulated Improvement (DC-206) — ⬜ AFTER 2C

| ID | Source | Commitment | Pri | Status | Notes |
|----|--------|-----------|-----|--------|-------|
| DC-206 | Phase 2D | Agents propose improvements on surviving + newly-mined content. Convergence required. | P0 | OPEN | |
| DC-120 | Vanguard | Install `scaffold_validate.sh` — structural integrity check | P0 | OPEN | Vanguard wrote complete script. Wire to pre-commit. |
| DC-121 | Vanguard | Install `scaffold_heal.sh` — safe auto-repair | P0 | OPEN | Depends on DC-120. |
| DC-122 | Oracle+Diviner | Rename decision for praxis sigma container | P1 | OPEN | Sovereign to decide. |
| DC-123 | Vanguard | Install `scaffold_rename.sh` for future migration | P1 | OPEN | Do NOT execute until DC-120 passes. INT-2210 lesson. |
| DC-124 | Oracle | Convert top 10 ARCH-* to ADR format | P1 | OPEN | Oracle REPO-003 spec. |
| DC-147 | Oracle+Adjudicator | **BUILD**: Model router — salience-gated, fail-open, 220-320 LOC | P1 | **BUILD #1** | Adjudicator: 9/10 feasibility, S complexity. |
| DC-150 | Oracle+Adjudicator | **BUILD**: Git-native tracking (Beads) — trailers, commit wrapper, index, 480-720 LOC | P1 | **BUILD #2** | Adjudicator: 8/10 feasibility, M complexity. Prerequisite for DC-149. |
| DC-148 | Oracle+Adjudicator | **REDESIGN→BUILD**: Knowledge graph — Python core, fuzzy repair, 420-620 LOC | P1 | **BUILD #3** | Adjudicator: 7/10 feasibility, M complexity. Bash/jq→Python. |

### Phase 3: Automations + Sensing

| ID | Source | Commitment | Pri | Status | Notes |
|----|--------|-----------|-----|--------|-------|
| DC-130 | INT-1612 | Cockpit activation: 16-min HQ + 30-min startup sequence | P0 | OPEN | Requires Phase 0 + Phase 1 (both DONE). |
| DC-131 | Vanguard | Graphiti `POST /triples` endpoint for deterministic edges | P1 | OPEN | Vanguard wrote exact code. |
| DC-132 | Vanguard | Backfill MEMORY.md + entities into Graphiti | P1 | OPEN | `backfill_memory_md.py` skeleton ready. |
| DC-133 | Vanguard | Graphiti query tools in agent harnesses via *-EXT.md | P1 | OPEN | Enables read path: agent → graph → cache → file. |
| DC-134 | DC-010 | Live Ledger sensing: cron-dispatched intel, MODEL-INDEX refresh | P1 | OPEN | 12 DYN-LEDGER files exist. Automation missing. |
| DC-135 | Diviner | Root `.obsidian/` stub | P2 | OPEN | Trivial. |

### Phase 4: Hardening + Scale

| ID | Source | Commitment | Pri | Status | Notes |
|----|--------|-----------|-----|--------|-------|
| DC-140 | DC-002 | Security audit of 234+ skills: credential exfiltration risk | P0 | OPEN | P0-CRITICAL. Cannot ship externally without this. |
| DC-141 | DC-003 | API key rotation: plaintext keys in openclaw.json | P0 | OPEN | Sovereign action required. |
| DC-142 | Vanguard | Memory compaction job (weekly) + conflict detection | P1 | OPEN | |
| DC-143 | Vanguard | Cross-machine sync testing (MBA ↔ Mac mini) | P1 | OPEN | |
| DC-144 | Diviner | Evaluate "Memory Agent" daemon (Sixth Agent) | P2 | OPEN | PageRank, community detection over shared graph. |
| DC-145 | Diviner | Quarantine namespace for anomalous artifacts | P2 | OPEN | Structural mutagenesis. |
| DC-146 | DC-123 | Numbered→semantic directory rename | P2 | **SUPERSEDED** | Replaced by DC-204T: sanctify numbered layers. |
| DC-149 | Oracle+Adjudicator | **DEFER**: AgentFS hybrid — SQLite shadow, 750-1050 LOC | P2 | **DEFER** | Blocked by DC-150. Build order: #4. |
| DC-151 | Oracle+Adjudicator | **DEFER**: Constitutional evolution — offline replay only, 900-1400 LOC | P2 | **DEFER** | Needs telemetry from A/D/C. Build order: #5. |

---

## Parked (Valid but not on critical path)

| ID | Source | Commitment | Pri | Status | Notes |
|----|--------|-----------|-----|--------|-------|
| DC-P01 | DC-004 | Rosetta Stone expansion: ~25 ontological terms | P1 | PARKED | 30 min. Session lull work. |
| DC-P02 | DC-008 | SYN-51/53 (Jira/Todoist integration) | P1 | PARKED | Linear items. Not infra critical path. |
| DC-P03 | DC-011 | CANON annotations: Physics/Three-Pillar on CANON-30300+ | P1 | PARKED | 1 of 3 done. Content work. |
| DC-P04 | DC-012 | Document formalization: promote clarescence decisions to ARCH-/REF- | P1 | PARKED | Fix memory first. |
| DC-P05 | DC-013 | Protocol changes to CLAUDE.md | P1 | PARKED | Addressed during Phase 2. |
| DC-P06 | DC-014 | MCP server activation on MBA (Linear) | P1 | PARKED | OAuth needs Sovereign. |
| DC-P07 | DC-015 | SOVEREIGN queue drain: 13 items | P1 | PARKED | Needs Sovereign decision sprint. |
| DC-P08 | INT-1803 | Open model onboarding (Cline + OpenCode) | P2 | PARKED | Needs stable agents first. |
| DC-P09 | INT-2101/2102 | Dual-stream intel architecture + 3-tier consumption model | P2 | PARKED | Depends on Google Account 2, NotebookLM. |
| DC-P10 | INT-2108 | Three-track evaluation framework | P2 | PARKED | Operationalize after scaffold stable. |

---

## Completed / Dropped

| ID | Commitment | Status | Resolved | Notes |
|----|-----------|--------|----------|-------|
| DC-001 | Hard-gate skills in CLAUDE.md (DEC-C3) | DONE | 2026-02-15 | Enacted |
| DC-007 | Cross-session promise tracking | DONE | 2026-02-15 | This file |
| DC-009 | TERMINAL-STACK-CONFIG.md resolution | DONE | 2026-02-15 | Created REF- |
| DC-005 | Agent fleet remediation (original) | SUPERSEDED | 2026-02-23 | → DC-101 |
| DC-006 | Cockpit activation (original) | SUPERSEDED | 2026-02-23 | → DC-130 |
| DC-010 | Live Ledger sensing (original) | SUPERSEDED | 2026-02-23 | → DC-134 |
| DC-100 | Docker PATH + containers | DONE | 2026-02-23 | Phase 0 |
| DC-101 | Agent fleet audit | DONE | 2026-02-23 | Phase 0 |
| DC-102 | Graphiti health check | DONE | 2026-02-23 | Phase 0 |
| DC-110 | Per-agent memory layout | DONE | 2026-02-23 | Phase 1 |
| DC-111 | memsync daemon | DONE | 2026-02-23 | Phase 1 |
| DC-112 | JSONL journal hooks | DONE | 2026-02-23 | Phase 1 |
| DC-113 | E2E write path verified | DONE | 2026-02-23 | Phase 1 |
| DC-200 | File index | DONE | 2026-02-23 | Phase 2A |
| DC-201 | Oracle orchestration/ inspection | DONE | 2026-02-23 | Phase 2A |
| DC-202 | Oracle engine/ inspection | DONE | 2026-02-23 | Phase 2A |
| DC-203 | Adjudicator praxis/ inspection | DONE | 2026-02-23 | Phase 2A |
| DC-204 | Coherence synthesis (all sub-items) | DONE | 2026-02-23 | Phase 2B. First full playbook cycle. |
| DC-207 | Architectural questions | RESOLVED | 2026-02-23 | Answered by DC-204T |

---

## Protocol

### At Session Start (Directive Initialization)
1. Read this file after the inbox scan
2. Identify the LOWEST-NUMBERED OPEN item — that is the current work
3. Do NOT skip phases. Each phase gates the next.

### During Execution
4. Update Status to IN_PROGRESS when starting, DONE when verified complete
5. New commitments append to the correct phase

### Phase Gate Rule
**No phase may begin until all P0 items in the prior phase are DONE.**

---

## Metrics

- **Total**: 51 commitments (19 DONE + 16 OPEN/BUILD + 10 PARKED + 4 SUPERSEDED + 2 DEFER)
- **Phase 0**: ✅ 3/3 DONE | **Phase 1**: ✅ 4/4 P0 DONE (2 P1 hardening remain) | **Phase 2**: 2A+2B DONE, 2C+2D OPEN (12 items) | **Phase 3**: 6 OPEN | **Phase 4**: 9 items (2 P0, 5 P1/P2, 2 DEFER)
- **Delivery rate**: 37% (19/51) — up from 14% at reset
- **Target**: >80% within 30 days
- **Current position**: Phase 2C (content decruft + source mining)

---

*This file is living infrastructure (DYN- prefix). Do not delete or archive. Compact the Completed/Dropped table quarterly.*
