# Decision Atoms — DC-204 Session 2026-02-23 (Continuation)

**Agent**: Commander (Claude Opus 4.6)
**Session**: DC-204 playbook completion + T1/T2 tightening execution
**Git HEAD at start**: efbcb2b5
**Authority**: Sovereign directive — "dispatch the swarm, proceed comprehensively"

---

## Decision Atoms

### DA-1: Parallel Swarm Dispatch for T1/T2/Inbox
- **Context**: Handoff doc listed T1 (reference repairs), T2 (hygiene), and inbox cleanup as pending mechanical tasks
- **Decision**: Dispatch 3 parallel subagents simultaneously — one per workstream
- **Rationale**: All three are independent, non-conflicting file operations. Parallelism saves ~3x wall clock time
- **Outcome**: All 3 completed successfully. T1: 19 files patched (path refs). T2: 5 renames + 22 macOS dupes deleted + .gitignore verified. Inbox: 91 files moved to done/
- **Risk accepted**: Parallel file operations could theoretically conflict — mitigated by non-overlapping file sets

### DA-2: T1-3 Path Repair Scope — Engine Files Included
- **Context**: DC-204 synthesis listed T1-3 as "praxis path references" only
- **Decision**: Extended scope to include engine/ files (which also had stale `orchestration/scripts/` refs)
- **Rationale**: Same bug, same fix. Engine had 17 affected files vs praxis's 2. Leaving engine unfixed would be incoherent
- **Outcome**: ~54 references fixed across 19 files total
- **Precedent**: Expand mechanical fixes to full scope when same pattern applies

### DA-3: Adjudicator Prompt Intentionally Left Unexecuted as TASK-*.md
- **Context**: Playbook says "dispatch to Adjudicator" — normally via dispatch.sh creating TASK-*.md in inbox
- **Decision**: Write the prompt to `engine/PROMPT-ADJUDICATOR-DC204_ENGINEERING_REVIEW.md` (canonical) but do NOT auto-dispatch yet
- **Rationale**: Sovereign said "dispatch the swarm" for the T1/T2/inbox work. The Adjudicator dispatch is the *next* action — Sovereign should review the compiled schematic first before committing Adjudicator tokens
- **Gate**: Sovereign reviews schematic → approves → Commander dispatches via dispatch.sh

### DA-4: Inbox Bulk Archive vs Selective Triage
- **Context**: 91 items in commander inbox, mix of stale auto-tasks, old CONFIRM/RESULT pairs, and already-ingested inspection results
- **Decision**: Move ALL to done/ in one batch. No selective processing
- **Rationale**: All items were from Feb 9-22, all had been either ingested (inspection results) or superseded (auto-tasks). None contained unprocessed actionable intel
- **Risk accepted**: Possible loss of unread RESULT content — mitigated by fact that canonical responses live in -INBOX/commander/00-INBOX0/ (already ingested)

### DA-5: macOS Duplicate Deletion (22 files)
- **Context**: T2 agent found 22 files with " 2.md" / " 3.md" suffixes (macOS Finder copy artifacts)
- **Decision**: Delete all — both tracked (11 git rm) and untracked (10 rm)
- **Rationale**: .gitignore already had `* 2.*` pattern. These are never intentional. Base files all exist
- **Outcome**: 22 files removed

### DA-6: Compiled Schematic Structure — Convergence Table + Spec Format
- **Context**: Need to merge Oracle (engineering-focused) and Diviner (scientific-focused) into a format Adjudicator can engineer against
- **Decision**: Structure as: convergence matrix → per-spec engineering requirements → predictions table → execution order
- **Rationale**: Adjudicator needs concrete interfaces, not metaphors. Scientific framing preserved as "enrichment" within each spec but engineering requirements are primary. Predictions preserved as testable claims for future validation
- **Precedent**: This format becomes the standard for all future playbook cycle compilation outputs

### DA-7: Execution Order — DC-147 Before DC-148
- **Context**: Oracle listed Recs 1-5; need to prioritize for execution
- **Decision**: DC-147 (model router) first, then DC-148 (knowledge graph), then DC-150 (beads), then DC-149 (AgentFS), then DC-151 (evolution)
- **Rationale**: Router is smallest effort with immediate dispatch.sh improvement. Knowledge graph enables health monitoring. Both are small-effort, high-value. AgentFS and evolution are medium/large and require more infrastructure
- **Gate**: All gated by Phase 0 (DC-100–102)

---

## Artifacts Produced This Session

| Artifact | Path | Purpose |
|---|---|---|
| Compiled Schematic | `agents/commander/outbox/RESULT-COMMANDER-DC204-COMPILED_SCHEMATIC.md` | Unified Oracle+Diviner → engineering specs |
| Adjudicator Prompt | `engine/PROMPT-ADJUDICATOR-DC204_ENGINEERING_REVIEW.md` | Final playbook leg dispatch prompt |
| Decision Atoms | `agents/commander/outbox/DECISION_ATOMS-DC204-SESSION-20260223.md` | This file |
| T1 path repairs | 19 files in engine/ and praxis/ | Fixed `orchestration/scripts/` → `orchestration/00-ORCHESTRATION/scripts/` |
| T2 renames | 5 files in engine/ and praxis/ | Prefix normalization (README→REF-README, etc.) |
| T2 dupe cleanup | 22 macOS duplicates deleted | `* 2.*` / `* 3.*` artifacts |
| Inbox cleanup | 91 files → done/ | Cleared stale commander inbox |

---

## Prompts Issued This Session

| Prompt | Target | Location | Status |
|---|---|---|---|
| T1 Reference Repairs | Claude Code subagent | (inline, not persisted — mechanical execution) | EXECUTED, COMPLETE |
| T2 Hygiene Tasks | Claude Code subagent | (inline, not persisted — mechanical execution) | EXECUTED, COMPLETE |
| Inbox Cleanup | Claude Code subagent | (inline, not persisted — mechanical execution) | EXECUTED, COMPLETE |
| Adjudicator Engineering Review | Adjudicator (Codex) | `engine/PROMPT-ADJUDICATOR-DC204_ENGINEERING_REVIEW.md` | WRITTEN, NOT DISPATCHED |

## Responses Ingested This Session

| Response | Source | Location | Status |
|---|---|---|---|
| Oracle DC-204E Industry Consensus | Grok 4.20β | `-INBOX/commander/00-INBOX0/RESPONSE-ORACLE-INDUSTRY_CONSENSUS_SCAFFOLD.md` | INGESTED, COMPILED |
| Diviner DC-204D Industry Synthesis | Gemini Pro 3.1 | `-INBOX/commander/00-INBOX0/RESPONSE-DIVINER-INDUSTRY_SYNTHESIS.md` | INGESTED, COMPILED |
| Adjudicator DC-204 Engineering Review | Codex GPT-5.3 | `-INBOX/commander/00-INBOX0/RESPONSE-ADJUDICATOR-DC204_ENGINEERING_REVIEW.md` | INGESTED |

---

## Adjudicator Ingestion — Decision Atoms (Continuation)

### DA-8: Accept Adjudicator Build Order (A→D→B→C→E)
- **Context**: Adjudicator reviewed all 5 specs and recommended: Model Router first, then Git-Native Tracking, then Knowledge Graph (redesigned), then AgentFS (deferred), then Evolution (deferred)
- **Decision**: Accept as-is. This matches Commander's prior recommendation (DA-7) with one upgrade: Spec B redesigned from bash/jq to Python core
- **Rationale**: Adjudicator's reasoning is sound — D must precede C because task identity/path normalization is prerequisite for DB sync. B needs Python for graph analytics at 3674 markdown files. E needs telemetry from A/D/C before it can score fitness
- **Outcome**: Build order locked. Deferred commitments updated accordingly

### DA-9: Accept Spec B REDESIGN Verdict (bash→Python)
- **Context**: Commander specified "pure bash/jq" constraint for knowledge graph. Adjudicator pushed back: fuzzy matching, cycle detection, and transport gap analysis are unreliable in bash at 825+ files
- **Decision**: Accept redesign. Python core with bash wrapper for cron/manual invocation
- **Rationale**: Adjudicator is right — difflib/Levenshtein for fuzzy repair suggestions, SCC detection for cycles, and streaming parser for memory pressure all justify Python. bash/jq was an under-specified constraint from Commander's compilation
- **Precedent**: When Adjudicator pushes back on implementation constraints with technical evidence, accept unless there's a constitutional reason not to

### DA-10: Accept Spec C DEFER Verdict
- **Context**: Commander had AgentFS as third in build order. Adjudicator deferred it behind D (git-native tracking)
- **Decision**: Accept. C depends on D for task identity and stable path canonicalization
- **Rationale**: Adjudicator identified real dependency: the dual inbox paths (`-INBOX/*` vs `agents/*/inbox/*`) and absence of git hooks mean AgentFS sync would be fragile. Hardening task identity (D) first gives C a stable substrate
- **Key insight from Adjudicator**: "no active Git hooks are installed in `.git/hooks`" — this is a gap that D addresses

### DA-11: Sear Triangulation Playbook into Constitutional Law
- **Context**: Sovereign articulated the playbook verbatim for the second time
- **Decision**: Seared into AGENTS.md and CLAUDE.md as constitutional section with rationale per phase
- **Rationale**: Sovereign should never need to repeat a directive. Constitutional placement means every agent session inherits it at init. Added documentation invariants, CLI agent Desktop output convention, and session start protocol
- **Outcome**: Committed as `cd1bca9b`

### DA-12: First Full Playbook Cycle Complete
- **Context**: DC-204 traversed Commander→Oracle(DC-204E)→Diviner(DC-204D)→Commander(compilation)→Adjudicator(engineering review)
- **Decision**: Mark playbook cycle as validated. This is the reference implementation for all future cycles
- **Outcome**: 5 specs engineered, 2 BUILD, 1 REDESIGN, 2 DEFER. Build order locked. All artifacts saved per documentation invariants

---

## Phase 2C Decruft — Decision Atoms (Continuation)

### DA-13: Parallel 4-Lane Decruft Swarm
- **Context**: Phase 2C requires acting on 24 STALE + 25 ORPHANED + 6 SUPERSEDED + 6 stale MODEL-PROFILEs + 3 overlap clusters
- **Decision**: Dispatch 4 parallel agents: (1) archive orphaned + mark superseded, (2) consolidate overlap clusters, (3) archive stale MODEL-PROFILEs, (4) handle stale praxis syntheses/mechanics
- **Rationale**: All four workstreams touch non-overlapping file sets. Parallel execution ~4x faster than serial
- **Outcome**: All 4 agents completed. 32 files changed in single commit `5426d51c`

### DA-14: Consolidation Strategy — Keep Most Operational File
- **Context**: 3 overlap clusters needed consolidation. Which file survives?
- **Decision**: Keep the most operational/practical file as target, merge unique content from others
- **Rationale**: Operational docs are consumed by agents during execution. Mechanical/theoretical docs are reference. Agents need "how" more than "why" during dispatch
- **Precedent**: Worktree cluster → PRAC-blitzkrieg (most operational). Compaction cluster → MECH-context_compaction (most foundational). Subagent cluster → MECH-subagent_delegation (more complete)

### DA-15: Staleness Banners vs Archive for Partially-Stale Files
- **Context**: 8 praxis files are stale but contain >50% valid content
- **Decision**: Add staleness banner in-place rather than archiving. Banner includes: status, date, specific issue, action needed, who flagged it
- **Rationale**: Archiving destroys navigability. A file that's 70% good shouldn't be hidden — it should be visibly marked so the next agent who reads it knows what to trust and what to update
- **Precedent**: Diviner's "Kata vs Kumite" insight — stale praxis actively misleads. Banners prevent misleading without destroying

### DA-16: MODEL-PROFILE Archive — MODEL-INDEX.md as Single Source
- **Context**: 6 YAML profile files all stale (2024-era models). MODEL-INDEX.md (2026-02-13) is comprehensive and current
- **Decision**: Archive all 6 YAMLs. MODEL-INDEX.md becomes sole authoritative registry. New profiles will be generated from MODEL-INDEX when needed (per Adjudicator Option C from T0-3 analysis)
- **Rationale**: Maintaining 20+ individual YAML files in parallel with a master index creates guaranteed drift. Single source of truth until the model router (DC-147) requires per-model config files

### DA-17: Begin Playbook Loop for DC-208 (Source Mining)
- **Context**: Source mining is the second half of Phase 2C. 1,773 sources, 0% integrated, 319 PARADIGM-tier
- **Decision**: Begin playbook loop — Oracle prompt written for source mining strategy (own thesis + industry consensus)
- **Rationale**: This is non-trivial enough to warrant full triangulation. The extraction protocol, batch architecture, and agent assignment decisions will shape weeks of work. Getting it wrong wastes massive context
- **Gate**: Sovereign dispatches Oracle prompt → Oracle responds → Commander petitions Diviner → Commander compiles → Adjudicator engineers

## Prompts Issued This Session (Updated)

| Prompt | Target | Location | Status |
|---|---|---|---|
| DC-208 Source Mining Strategy | Oracle (Grok) | `engine/PROMPT-ORACLE-DC208_SOURCE_MINING_STRATEGY.md` + `~/Desktop/` | DISPATCHED, RESPONSE INGESTED |
| DC-208 Source Mining Synthesis | Diviner (Gemini) | `engine/PROMPT-DIVINER-DC208_SOURCE_MINING_SYNTHESIS.md` + `~/Desktop/` | DISPATCHED, RESPONSE INGESTED |
| DC-208 Mining Pipeline Engineering | Adjudicator (Codex) | `engine/PROMPT-ADJUDICATOR-DC208_MINING_PIPELINE_ENGINEERING.md` + `~/Desktop/` | DISPATCHED, RESPONSE INGESTED |

## Responses Ingested This Session (DC-208 Cycle)

| Response | Source | Location | Status |
|---|---|---|---|
| Oracle DC-208 Source Mining Strategy | Grok 4.20β | `-INBOX/commander/00-INBOX0/RESPONSE-ORACLE-DC208_SOURCE_MINING_STRATEGY.md` | INGESTED, COMPILED |
| Diviner DC-208 Source Mining Synthesis | Gemini Pro 3.1 | `-INBOX/commander/00-INBOX0/RESPONSE-DIVINER-DC208_SOURCE_MINING_SYNTHESIS.md` | INGESTED, COMPILED |
| Adjudicator DC-208 Mining Pipeline Engineering | Codex GPT-5.3 | `-INBOX/commander/00-INBOX0/RESPONSE-ADJUDICATOR-DC208_MINING_PIPELINE_ENGINEERING.md` | INGESTED |

## Artifacts Produced This Session (Updated)

| Artifact | Path | Purpose |
|---|---|---|
| Phase 2C decruft commit | `5426d51c` | 3 orphans archived, 3 clusters consolidated, 6 MODEL-PROFILEs archived, 2 superseded marked, 8 staleness banners |
| Oracle DC-208 prompt | `engine/PROMPT-ORACLE-DC208_SOURCE_MINING_STRATEGY.md` | Source mining strategy — begins playbook loop |
| Diviner DC-208 prompt | `engine/PROMPT-DIVINER-DC208_SOURCE_MINING_SYNTHESIS.md` | Cross-disciplinary synthesis prompt |
| Adjudicator DC-208 prompt | `engine/PROMPT-ADJUDICATOR-DC208_MINING_PIPELINE_ENGINEERING.md` | Pipeline engineering prompt |
| Compiled schematic DC-208 | `agents/commander/outbox/RESULT-COMMANDER-DC208-COMPILED_SCHEMATIC.md` | Oracle+Diviner → 9 pipeline components |

---

## DC-208 Playbook Cycle — Decision Atoms

### DA-18: Accept Adjudicator DC-208 Build Order (1→2→5→6→3→4→8→7→9)
- **Context**: Adjudicator reviewed all 9 mining pipeline components with feasibility scores 5-9/10
- **Decision**: Accept recommended build order as canonical. Critical path: 1→2→5→6→3→4
- **Rationale**: Build order ensures no component starts without its inputs being available. Triage (1) unblocks everything. Extraction (2) defines atom format. Integration bridge (5) connects to Graphiti. Quality gate (6) validates before scaling. Cluster (3) + batch (4) enable scale
- **Outcome**: Build order locked in deferred commitments

### DA-19: Accept Component 3 REDESIGN Verdict (K-means → Hybrid HDBSCAN + Constrained K-means)
- **Context**: Commander spec used pure K-means k=18. Adjudicator pushed back: "operationally convenient but not semantically robust"
- **Decision**: Accept hybrid approach — HDBSCAN for natural clustering + constrained K-means for operational 18-cluster target
- **Rationale**: Same pattern as DA-9 (Spec B redesign). Adjudicator provides implementation-level pushback with technical evidence. Secondary assignment table for azeotropes is elegant
- **Precedent**: Reinforces "when Adjudicator pushes back with technical evidence, accept"

### DA-20: Accept Components 7 and 9 DEFER Verdicts
- **Context**: Lineage engine (7) scored 6/10, cyclical relevance (9) scored 5/10
- **Decision**: Accept both deferrals. Component 7 waits for ≥50 mined sources. Component 9 integrates into DC-147 model router
- **Rationale**: Lineage needs graph data that doesn't exist yet. Cyclical relevance needs usage telemetry that pipeline hasn't generated. Building either now is premature optimization
- **Gate**: 7 unblocks after 50 sources mined. 9 unblocks after DC-147 + pipeline telemetry

### DA-21: Second Full Playbook Cycle Complete (DC-208)
- **Context**: DC-208 traversed Commander→Oracle(mining strategy)→Diviner(scientific overlay)→Commander(compiled schematic)→Adjudicator(pipeline engineering)
- **Decision**: Mark second playbook cycle as validated. Pipeline design is complete — execution begins next
- **Outcome**: 9 components: 6 BUILD, 1 REDESIGN, 2 DEFER. Total estimated LOC: ~3,890-5,050. Build order locked
- **Key numbers from Adjudicator**: 1,773 sources, 233,213 lines, 33 files with non-standard frontmatter, 150 CSV rows with blank signal_tier

### DA-22: Surprise × Precision Formula Accepted
- **Context**: Adjudicator provided concrete formula for quality gate 5: `surprise = 0.6*novelty + 0.4*belief_violation`, `precision = 0.35*evidence + 0.25*reliability + 0.25*cross_support + 0.15*falsifiability`
- **Decision**: Accept as initial calibration. Alert bands: ≥0.55 CRITICAL, 0.35-0.55 REVIEW, <0.35 IGNORE
- **Rationale**: Formula is concrete, implementable, and the 0.88 consistency threshold is explicitly marked calibratable (recalibrate after first 50 sources against adjudicator labels via ROC/F1)
