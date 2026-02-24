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
| DC-205 | Phase 2C | Sentence-by-sentence action on every file: canonical stays, stale archives, orphans wire or archive | P0 | **DONE** | T1/T2 tightening + 4-lane decruft swarm (`5426d51c`). 32 files changed. |
| DC-208 | Phase 2C | Source mining pipeline design — full triangulation playbook complete | P1 | **DESIGN DONE** | Second playbook cycle complete. 9 components engineered. Build phase next. |
| DC-208-1 | Adjudicator | Triage script — Python, all-MiniLM-L6-v2, 996 LOC | P0 | **DONE** | Built `138b70bf`, R1 fix `2ada4b40`, R2 pass. 1,152 sources scored, DAG 5,676 edges. |
| DC-208-2 | Adjudicator | Extraction template — 6-cat JSONL + chaperone + prompt, 1089 LOC | P0 | **DONE** | Built `138b70bf`, R1+R2 fixes, hybrid frontmatter fix `bc5ac112`. OpenRouter backend restored. |
| DC-208-5 | Adjudicator | Integration bridge — memsync extension + durable retry queue, 952 LOC | P0 | **DONE** | Built `138b70bf`, R1 fix: sent_records + BEGIN IMMEDIATE + backoff. R2 pass. |
| DC-208-8 | Adjudicator | Negative knowledge store — FAILED_PATH edges + decay, 494 LOC | P1 | **DONE** | Built `138b70bf`, R1 fix: schema alignment + decay bug. R2 pass. |
| DC-208-PILOT | Commander | Pilot extraction: top-5 sources via Gemini 2.5 Flash | P0 | **DONE** | 820 atoms, 63 chunks, 0 errors, 100% JSON. Committed `01db01fd`. |
| DC-209 | Oracle (Grok) | Model routing strategy — triangulated convergence | P0 | **DONE** | DC-209 + DC-209R. Gemini 2.5 Flash confirmed primary. GPT-4o-mini fallback. <$2.50 full corpus. |
| DC-208-6 | Commander | Quality gate — 4+1 gates + surprise×precision, 746 LOC | P0 | **DONE** | Built `b35437b7`. Pilot: 820 atoms, 100% consistency, 60% canon coverage. |
| DC-208-4 | Commander | Batch orchestrator — resume-capable, concurrent, 601 LOC | P0 | **DONE** | Built `b35437b7`. Full corpus extraction RUNNING (1,152 sources, 118 batches). |
| DC-208-3 | Adjudicator | Cluster engine — hybrid HDBSCAN + constrained K-means, 560-760 LOC | P1 | OPEN | 7/10 feasibility. After full extraction completes. |
| DC-208-7 | Adjudicator | Lineage engine — memetic cladistics, 760-1080 LOC | P2 | **DEFER** | 6/10. After ≥50 mined sources. |
| DC-208-9 | Adjudicator | Cyclical relevance model — DC-147 plugin, 260-420 LOC | P2 | **DEFER** | 5/10. After DC-147 + telemetry. |

#### 2D — Triangulated Improvement (DC-206) — ⬜ AFTER 2C

> Agents propose improvements and innovations on surviving + newly-mined content. Convergence required before anything lands.

| ID | Source | Commitment | Pri | Status | Notes |
|----|--------|-----------|-----|--------|-------|
| DC-206 | Phase 2D | Agents propose improvements on surviving + newly-mined content. Convergence required. | P0 | OPEN | |
| DC-147 | Oracle+Adjudicator | **BUILD**: Model router — salience-gated, fail-open, 220-320 LOC | P1 | OPEN | Adjudicator: 9/10 feasibility, S complexity. Informed by DC-209 convergence. |
| DC-150 | Oracle+Adjudicator | **BUILD**: Git-native tracking (Beads) — trailers, commit wrapper, index, 480-720 LOC | P1 | OPEN | Adjudicator: 8/10 feasibility, M complexity. Prerequisite for DC-149. |
| DC-148 | Oracle+Adjudicator | **REDESIGN→BUILD**: Knowledge graph — Python core, fuzzy repair, 420-620 LOC | P1 | OPEN | Adjudicator: 7/10 feasibility, M complexity. Bash/jq→Python. |

### Phase 3: Surface Organization + Enforcement — ⬜ AFTER Phase 2

> Only now — with content audited, architecture decided, sources mined — does the veneer go on.

| ID | Source | Commitment | Pri | Status | Notes |
|----|--------|-----------|-----|--------|-------|
| DC-120 | Vanguard | Install `scaffold_validate.sh` — structural integrity check | P0 | OPEN | Vanguard wrote complete script. Wire to pre-commit. |
| DC-121 | Vanguard | Install `scaffold_heal.sh` — safe auto-repair | P0 | OPEN | Depends on DC-120. |
| DC-300 | Phase 3 | Formalize naming conventions across all directories | P1 | OPEN | Derived from Phase 2 evidence, not imposed top-down. |
| DC-301 | Phase 3 | Standardize headers and metadata across all files | P1 | OPEN | |
| DC-302 | Phase 3 | Normalize duplicate concepts against Rosetta Stone | P1 | OPEN | |
| DC-303 | DC-207 | Execute dispatch restructuring if DC-207 decided one needed | P1 | **RESOLVED** | DC-207 resolved: sanctify, don't restructure. No action needed. |
| DC-304 | DC-124 | Convert top ARCH-* files to ADR format | P1 | OPEN | Oracle REPO-003 spec. |
| DC-122 | Oracle+Diviner | Rename decision for praxis sigma container | P1 | OPEN | Sovereign to decide. |
| DC-123 | Vanguard | Install `scaffold_rename.sh` for future migration | P1 | OPEN | Do NOT execute until DC-120 passes. INT-2210 lesson. |

### Phase 4: Automations + Sensing — ⬜ AFTER Phase 3

| ID | Source | Commitment | Pri | Status | Notes |
|----|--------|-----------|-----|--------|-------|
| DC-130 | INT-1612 | Cockpit activation: 16-min HQ + 30-min startup sequence | P0 | OPEN | Requires Phase 0 + Phase 1 (both DONE). |
| DC-131 | Vanguard | Graphiti `POST /triples` endpoint for deterministic edges | P1 | OPEN | Vanguard wrote exact code. |
| DC-132 | Vanguard | Backfill MEMORY.md + entities into Graphiti | P1 | OPEN | `backfill_memory_md.py` skeleton ready. |
| DC-133 | Vanguard | Graphiti query tools in agent harnesses via *-EXT.md | P1 | OPEN | Enables read path: agent → graph → cache → file. |
| DC-134 | DC-010 | Live Ledger sensing: cron-dispatched intel, MODEL-INDEX refresh | P1 | OPEN | 12 DYN-LEDGER files exist. Automation missing. |
| DC-135 | Diviner | Root `.obsidian/` stub | P2 | OPEN | Trivial. |

### Phase 5: Hardening + Scale — ⬜ AFTER Phase 4

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
| DC-205 | Content decruft | DONE | 2026-02-23 | Phase 2C. 4-lane swarm: orphans, clusters, MODEL-PROFILEs, staleness banners. |
| DC-208 | Source mining pipeline design | DONE | 2026-02-23 | Phase 2C. Second full playbook cycle. 9 components engineered. |
| DC-208-1 | Triage script | DONE | 2026-02-23 | 996 LOC. R1 FAIL→fix→R2 PASS. 1,152 sources scored. |
| DC-208-2 | Extraction template + prompt | DONE | 2026-02-23 | 1,089 LOC. R1→R2→hybrid fix. OpenRouter backend. |
| DC-208-5 | Integration bridge | DONE | 2026-02-23 | 952 LOC. sent_records + BEGIN IMMEDIATE. R2 PASS. |
| DC-208-8 | Negative knowledge store | DONE | 2026-02-23 | 494 LOC. Schema alignment + decay fix. R2 PASS. |
| DC-208-PILOT | Pilot extraction (top-5) | DONE | 2026-02-23 | 820 atoms via Gemini 2.5 Flash. 0 errors. `01db01fd`. |
| DC-209 | Model routing convergence | DONE | 2026-02-23 | Oracle DC-209+DC-209R. Gemini 2.5 Flash primary. <$2.50 full corpus. |

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

- **Total**: 66 commitments (27 DONE + 3 OPEN-BUILD + 15 OPEN + 10 PARKED + 5 SUPERSEDED/RESOLVED + 4 DEFER + 2 DESIGN DONE)
- **Phase 0**: ✅ 3/3 DONE | **Phase 1**: ✅ 4/4 P0 DONE (2 P1 hardening remain) | **Phase 2**: 2A+2B DONE, 2C 6/11 DONE (pilot complete, 3 components + 2 defer remain), 2D OPEN (4 items) | **Phase 3**: 9 items (surface org) | **Phase 4**: 6 items (automations) | **Phase 5**: 9 items (hardening)
- **Delivery rate**: 41% (27/66) — 6 new items DONE this session (4 pipeline builds + pilot + model routing)
- **Target**: >80% within 30 days
- **Current position**: Phase 2C → DC-208-6 (quality gate BUILD), then scale extraction to full corpus

---

*This file is living infrastructure (DYN- prefix). Do not delete or archive. Compact the Completed/Dropped table quarterly.*
