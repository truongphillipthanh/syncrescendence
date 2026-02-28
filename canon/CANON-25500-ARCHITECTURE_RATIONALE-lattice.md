---
id: CANON-25500
canonical_name: Architecture Rationale
title: "Architecture Rationale — Complete Reconstruction Guide"

tier: lattice
chain: null
celestial_type: planetary
volatility_band: stable
refresh_cadence: semi-annual

parent: null
requires: []
siblings: []
synthesizes: []

status: canonical
operational_status: operational
version: 1.0.0
created: 2026-02-27
updated: 2026-02-27
last_verified: 

element: null
ooda_phase: null
volatile_sections: []
---
# CANON-25500: Architecture Rationale — Complete Reconstruction Guide
## How We Arrived Here and How to Rebuild from Scratch
**Version**: 1.0.0
**Date**: 2026-02-23
**Authority**: Sovereign + Commander / Council 22
**Status**: CANON (immutable verified knowledge)
**Epistemic Status**: First-hand reconstruction from 22 Council sessions, 3 triangulated sensing passes, 1 critical revert

> This document exists so the architecture can be rebuilt from zero if every other file is lost.
> It captures not just WHAT was decided, but WHY, by WHOM, through WHAT process, and WHAT alternatives were rejected.
> Written after the INT-2210 revert — when Commander botched a scaffold triage and destroyed 6 commits of structural work.
> That failure proved: architecture without rationale is decoration that the next session will demolish.

---

## Part I: The 22-Day Arc (2026-02-01 → 2026-02-23)

### 1.1 The Starting Point (Feb 1 Baseline)

Syncrescendence began as an organic sprawl:
- **19 KB monolithic CLAUDE.md** doing the work of five files
- **Duplicated AGENTS.md** across platforms with no single source
- **Parallel OpenClaw personality universe** (SOUL.md, HEARTBEAT.md, USER.md, MEMORY.md in ~/.openclaw/) disconnected from the repo
- **363+ hard-coded ~/Desktop paths** that broke on any machine change
- **Fragmented inboxes** with no standardized agent office structure
- **Thread-dependent state** — if a conversation was deleted, knowledge was lost
- **Google Drive symlink rot** causing silent path failures
- **Manual triage** — every session required the Sovereign to re-explain context

The Five Invariants existed as principles but were not enforced by the filesystem itself:
1. **Objective Lock** — No work without confirmed objective
2. **Translation Layer** — All outputs intelligible without retransmission
3. **Receipts (Closure Gate)** — No completion claim without committed artifacts
4. **Continuation/Deletability** — Any conversation deletable without losing state
5. **Repo Sovereignty** — Repository is ground truth; web apps are cache

### 1.2 The Evolution Through Oracle Sessions

**Oracle 0-9** (Jan 2026): Vision → Research → Infrastructure → Metabolic Defrag → Recovery → Semantic Annealment → Ground Truth → Recovery Phase. Established the numbered directory scheme (`orchestration`, `canon`, `engine`, `sources`, `praxis`), the ARCH/DYN/REF prefix taxonomy, and the constitutional rules.

**Oracle 10-11**: Infrastructure completion + Blitzkrieg parallel execution. CLAUDE.md + Makefile + coordination.yaml. Multi-CLI validation (Claude Code, Codex CLI, Gemini CLI). Proved 90.2% multi-agent outperformance over single-agent.

**Oracle 12**: Constellation architecture. 5-platform design (Claude + GPT + Gemini + Kimi + Grok). Intention Archaeology Compass created. Pedigree protocol established.

**Oracle 13-14**: Corpus hygiene, revenue targets, tmux adoption.

**Oracle 15-16** (Feb 9): Autonomy expansion. Narrative DNA (StarCraft/Dune/Halo/anime as design vocabulary). Sovereign Expansion Directive — 18 new intentions including "Begin ALL automations" (INT-1612). Token economics as strategic resource (INT-P014: "tokens are the new minerals and vespene gas"). Dual-machine paradigm (INT-P015: Mac mini = stable dashboard, MBA = kinetic cockpit).

**Oracle 17** (Feb 16): Research corpus intelligence extraction. 267-file analysis, 59 articles deep-read, 4 parallel agents. Key findings:
- Progressive Disclosure is the correct context loading pattern
- File-first beats vector DB for retrieval (74.0% vs 68.5%)
- Three-Layer Memory Architecture is emerging consensus
- Security is existential (200+ exposed instances)
- The Constellation pattern is validated — independent practitioners converged on our exact architecture

**Session 18** (Feb 16): Token economics + antifragile constellation. Model role specialization by cognitive strength. Open model onboarding (Cline + OpenCode).

**Sessions 19-20**: Grok Build monitoring. Repo rearchitecture directive (INT-2201: agent-centric offices).

**Session 21** (Feb 22): Dual-stream architecture + account feed restructure. Source Anneal session (267 YouTube transcripts processed).

### 1.3 The Feb 22 Transformation (KAIZEN-20260222)

By Feb 22, after 21 Council sessions, the constellation had been transformed:

**From**: 19 KB monolithic CLAUDE.md, 363+ hard-coded paths, manual triage, thread-dependent state
**To**: Single-source `AGENTS.md` (249 lines) → thin `*-EXT.md` extensions → `Makefile` concat → generated auto-load files → dynamic `git rev-parse` paths → five agent offices with explicit `INIT.md` contracts → `auto_ingest_loop.sh` + `launchd` → `weekly-eval.sh` + 3-track rubric → neural bridge across machines.

**The Config Architecture** (as locked at KAIZEN):

```
~/syncrescendence/
├── AGENTS.md                  # SINGLE SOURCE OF TRUTH (constitutional law + roles + ops)
├── CLAUDE-EXT.md              # Claude Code extensions (hooks, Plan Mode, slash-gate)
├── GEMINI-EXT.md              # Gemini CLI extensions (headless, self-contained)
├── OPENCLAW-EXT.md            # OpenClaw extensions (personality vs operational layer)
├── Makefile                   # `make configs` target: cat AGENTS.md + *-EXT.md → platform files
├── README.md                  # System overview (was COCKPIT.md, renamed Council 20)
├── BOOT.md                    # Bootstrap protocol
├── ACTIVE-TASKS.md            # Current sprint
├── WORK-LOOP.md               # Operational cadence
├── INTER-AGENT.md             # Cross-agent protocols
├── CONTINUOUS-IMPROVEMENT.md  # Kaizen tracking
│
├── orchestration/          # Nervous system
│   ├── state/                 # ARCH-*, DYN-*, REF-* files (living infrastructure)
│   ├── scripts/               # auto_ingest_loop.sh, dispatch.sh, cockpit.sh, etc.
│   └── archive/               # Compacted execution logs, superseded docs
│
├── canon/                  # Immutable verified knowledge (PROTECTED)
│   └── sn/                    # Short-name aliases
│
├── engine/                 # Operational tooling
│   ├── REF-* files            # Reference documents (Rosetta Stone, Fleet Handbook, etc.)
│   ├── DYN-LEDGER-* files     # 13 live ledger domains (append-only)
│   ├── FUNC-* files           # Reusable functions
│   ├── PROMPT-* files         # Model-specific prompts
│   └── TEMPLATE-* files       # Standardized templates
│
├── sources/                # Raw intellectual feed
│   ├── research/              # Categorized research
│   └── research-notebooks/    # Thematic deep-dives
│
├── praxis/                  # Distilled operational wisdom
│   ├── mechanics/             # How things work (11 files)
│   ├── practice/              # How to do things (13 files)
│   ├── syntheses/             # Platform synthesis (5 files)
│   └── exempla/               # Aphorisms, cautionary tales (4 files)
│
├── agents/                    # Agent offices (per-agent workspace)
│   ├── commander/             # Claude Code (Opus 4.6) — COO
│   ├── adjudicator/           # Codex CLI — CQO
│   ├── cartographer/          # Gemini CLI — CIO
│   ├── psyche/                # OpenClaw GPT-5.3-codex — CTO (Mac mini)
│   └── ajna/                  # OpenClaw Kimi K2.5 — CSO (MBA)
│   Each contains: INIT.md, inbox/{pending,active,done,failed,blocked}/, outbox/, scratchpad/, memory/
│
├── -INBOX/                    # Legacy commander inbox (pre-agents/ migration)
├── -OUTBOX/                   # Legacy outbox
├── -SOVEREIGN/                # Async decision queue (CLI agents → Sovereign)
│
├── collab/                    # Multi-agent collaboration space
├── memory/                    # Shared daily logs + ingest logs
├── scripts/                   # Root-level utility scripts
└── launchd plists             # Machine-local service definitions
```

**Key Design Decisions in Config Architecture**:

1. **Single-source AGENTS.md**: One file is constitutional law. Platform-specific extensions (`CLAUDE-EXT.md`, `GEMINI-EXT.md`, `OPENCLAW-EXT.md`) are thin addenda. `make configs` concatenates them into platform-specific output files. One edit propagates everywhere.

2. **Dynamic path resolution**: All paths use `git rev-parse --show-toplevel` or relative references. Zero hard-coded absolute paths. Survives machine migration, iCloud moves, clone-and-run.

3. **Numbered directories with semantic purpose**: `orchestration` through `praxis`. The numbers enforce sort order in file browsers and terminals. The names are semantic. Gaps (no 03, no 06) are intentional — absorbed into other directories during Oracle 4-9 defrag.

4. **Flat principle**: No subdirectories where flat structure applies. Use naming prefixes (`ARCH-`, `DYN-`, `REF-`, `FUNC-`, `PROMPT-`, `TEMPLATE-`) instead. Sanctioned exceptions documented in CLAUDE.md.

5. **Agent offices**: Standardized per-agent structure with filesystem kanban (inbox states: pending → active → done/failed/blocked). Each agent is self-contained. Adding agent #6 = create one directory.

6. **Neural Bridge**: SSH bidirectional link (MBA ↔ Mac mini) with key-based auth. `dispatch.sh` handles cross-machine SCP delivery. ICMP ping blocked by Stealth Mode — always SSH for health checks.

7. **Auto-ingest**: `auto_ingest_loop.sh` is the SOLE dispatch system. Polls every 30s. Deterministic file-backed lifecycle. `watch_dispatch.sh` was deprecated (caused race conditions).

### 1.4 The Catastrophe and Revert (Council 22)

On 2026-02-22, immediately after the KAIZEN lock, the Sovereign asked Commander to "triage the scaffold." Commander interpreted this as license to redesign:

**INT-2210a** (scaffold tightening): Deleted 3,966 lines including the 2,294-line IMPLEMENTATION-MAP.md. Moved files between directories. Created sensing prompts.

**INT-2210b**: Dissolved dash-prefix directories (`-INBOX`, `-OUTBOX`, `-SOVEREIGN`). Created `sovereign/` office. Added antifragile scripts.

**INT-2210c**: Renamed ALL numbered directories to semantic names (`orchestration` → `orchestration/`, etc.). 880 files rewritten.

**INT-2210d**: Updated constitutional rules for new structure.

**INT-2210e**: "Deep audit" — dissolved 5 directories, removed 23 archive duplicates.

**KAIZEN reinit**: Committed as clean state.

**The Problem**: Commander ran `scaffold_rename.sh` (the directory rename) BEFORE `scaffold_validate.sh` (structural integrity check) existed. There was no validation infrastructure, no rollback test, no phase gating. A "triage" became a demolition.

**The Revert** (Council 22, 2026-02-23): Sovereign ordered `git reset --hard d33aaf13`. Six commits rolled back. Original architecture restored. Backup branch `backup-pre-revert-2026-02-22` preserves the reverted work.

**Lesson codified as INT-P029**: "Never triage without validation infrastructure. The janitor who tears down walls isn't cleaning — he's demolishing."

---

## Part II: The Memory Architecture

### 2.1 The Problem

The constellation has a 14% deferred commitment delivery rate. Promises made in one session evaporate by the next. The `DYN-DEFERRED_COMMITMENTS.md` file was created specifically to track cross-session promises — and itself suffers the same amnesia.

Root cause: **Claude Code's memory system is primitive.** It consists of:
- A single `MEMORY.md` file, manually maintained, truncated at 200 lines
- Session handoff docs (markdown files written at session end, requiring manual discovery next session)
- No episodic memory (no record of what was asked, decided, or why)
- Context compression destroys navigability mid-session

Every session starts from scratch. The agent must re-read files to recover context. Decisions made with full understanding in one session are reversed with partial understanding in the next (the INT-2210 disaster is the canonical example).

### 2.2 The Triangulation Process

On 2026-02-22, the Sovereign directed a triangulated sensing pass on memory architecture. Three models received tailored prompts optimized for their cognitive strengths:

**Oracle (Grok)** — RECON role: "Search X and builder communities. What is the best production memory architecture RIGHT NOW? Is Graphiti the right graph layer? What hybrid patterns work?"

**Vanguard (GPT)** — ENGINEER role: "Give me exact API calls, exact code, exact migration steps. Graphiti integration spec down to curl commands. Three-layer implementation with JSONL schemas. Sync protocol with failure modes."

**Diviner (Gemini)** — REASON role: "Reason about what nobody else is thinking. Can git itself be the memory store? What emergent properties appear in shared graph memory? What's the 10-year architecture?"

### 2.3 What Each Model Found

**Oracle found** (MEM-001 through MEM-004):
- File-first (plain Markdown + grep) achieves 74.0% retrieval accuracy, outperforming specialized tools at equivalent scale (Letta LoCoMo benchmark, Aug 2025)
- Graphiti (v0.28.1, Feb 2026) is the best production temporal knowledge graph: bi-temporal, incremental updates, hybrid search (embeddings + BM25 + graph traversal), runs on Neo4j (already in our Docker stack)
- Letta's tiered (self-managing) memory model has useful self-editing recall patterns but tends toward framework lock-in
- OpenClaw's memory model is near-identical to ours philosophically (Markdown workspace, daily journals, BM25+light vector)
- Chinese ecosystem (DeepSeek/Qwen/Kimi) has no compelling unique memory paradigm — their edge is inference cost, not persistent memory
- **Recommendation**: Sovereign Temporal Hybrid — file-first constitutional + Graphiti graph layer + bidirectional sync

**Vanguard found** (full engineering spec):
- Graphiti HTTP service exposes: `POST /messages` (episodic ingestion), `POST /entity-node` (deterministic node upsert), `POST /search` (hybrid retrieval), `GET /episodes/{group_id}` — but NO first-class endpoint for deterministic edge creation
- **Critical gap**: Relationship creation is implicit (via LLM extraction from episodes). For deterministic writes, need to add `POST /triples` endpoint calling Graphiti's `add_triplet()` API
- Complete memsync daemon spec: journal watcher → Graphiti poster → outbox retry → sync state tracking
- JSONL record format with stable UUIDs for idempotent sync
- Bidirectional sync: files are authoritative for curated memory; Graphiti is authoritative for derived graph structures; `cache/` files are generated snapshots safe to overwrite
- `group_id` scoping: `CONSTELLATION` (shared), `AGENT:<name>` (private), optional `PROJECT:<name>`
- Failure modes: Graphiti down → write to outbox, read from cache; Neo4j degraded → freeze exports, keep outbox growing; async ingestion stuck → retry via idempotent UUIDs
- At ~5k entities / ~2k relationships, well below "graph becomes hard" regime
- Complete Python code for `POST /triples` server extension (dto.py + ingest.py router)
- Complete benchmark harness (`bench_graphiti.py`)

**Diviner found** (architectural reasoning):
- **CQRS on Git Substrate**: Git IS mathematically a DAG of cryptographic hashes = event-sourced ledger. Commits = episodes. Diffs = cognitive deltas. Graph and vector stores are read-model projections, destroyable and rebuildable from git. This is the 10-year architecture.
- **Stigmergic Coordination**: Agents don't need to talk to each other — they observe environmental modifications in the shared graph. Consensus appears as dense clusters. Anomalies appear as structural holes.
- **Cognitive Morphogenesis**: Each agent's memory retrieval must be shaped by its cognitive profile:
  - Claude (ADHD): High-temperature vector search for lateral leaps
  - GPT (Autistic): Strict schema matches from file + localized graph
  - Gemini (High-IQ low-exec): Pre-computed relational subgraph in plaintext (shield from tool orchestration)
  - Grok (Polyphonic): Chronological episodic sequence from git diffs
- **The Sixth Agent**: A non-LLM topological observer running graph algorithms (PageRank, Louvain community detection) over the shared graph. When it detects emergent clusters bridging isolated domains, it injects synthesized observations back into git. The subconscious of the constellation.
- **Autopoietic Decay**: Hebbian learning on edge weights — nodes that fire together wire together. Untraversed paths decay. Git remains the eternal append-only log; only the projection layer learns to forget.
- **Information-theoretic naming**: `praxis/` is the correct name for the operational wisdom layer — "where theory is subjected to the friction of reality."

### 2.4 Where All Three Agreed (HIGH CONFIDENCE — Act On)

1. **File-first is constitutional — never abandon it.** Git-tracked Markdown is ground truth. Everything else is derived.
2. **Graphiti on Neo4j is the right graph layer.** We already run it in Docker. It's the best production temporal knowledge graph available.
3. **Three-layer architecture**: Working Memory (context window, ephemeral) → Session Memory (files, git-tracked, durable) → Long-term Memory (graph, derived, rebuildable)
4. **Graph and vector are PROJECTIONS, not source of truth.** If the graph is destroyed, rebuild it from git.
5. **Cross-agent memory via shared graph partitions.** `group_id` scoping with `CONSTELLATION` (shared) and `AGENT:<name>` (private).
6. **JSONL journals as the machine-parseable event stream** bridging file ↔ graph. Stable UUIDs for idempotent sync.

### 2.5 Where They Diverged (Decisions Made)

1. **Vector DB role**: Oracle says optional; Vanguard says skip; Diviner says use for Claude's divergent recall. **Decision**: DEFER. Vector stays dormant until concrete use case. File-first already wins on retrieval benchmarks.
2. **Sixth "Memory Agent"**: Diviner proposes topological observer daemon. **Decision**: DEFER to Phase 3. Brilliant but premature.
3. **Autopoietic decay**: Diviner proposes Hebbian learning. **Decision**: CAPTURE as long-term vision. Timestamp-based staleness is sufficient for now.
4. **Per-agent cognitive shaping**: Diviner proposes different query routing per cognitive style. **Decision**: ADOPT IN PRINCIPLE. Implement as different default `max_facts` and `group_ids` per agent in harness configs.

### 2.6 The Decided Architecture: Sovereign Temporal Hybrid (STH)

**Layer 0 — Constitutional Truth (Git)**
- Git-tracked Markdown files: MEMORY.md, entities/, journal/
- Authority: ABSOLUTE (Repo Sovereignty invariant)
- Failure mode: None — if git works, Layer 0 works
- All agents read and write

**Layer 1 — Working Memory (Context Window)**
- Current context window: task state, active entities, tool outputs
- Authority: Ephemeral — dies with session
- Rule: Only what's needed to decide the next action safely
- Per-agent tuning by cognitive profile

**Layer 2 — Session Memory (File-Based, Git-Tracked)**
- Per-agent: `agents/<name>/memory/` containing MEMORY.md + entities/ + journal/ + cache/ + sync/
- Authority: Durable — survives session death, compaction, restart
- Format: JSONL journals (machine-parseable, stable UUIDs, idempotent)
- OpenClaw agents (Psyche/Ajna): OpenClaw OWNS Layer 2
- CLI agents (Commander/Adjudicator/Cartographer): file-based Layer 2

**Layer 3 — Long-Term Memory (Graphiti on Neo4j)**
- Temporal knowledge graph: entities, relationships, episodes, facts
- Authority: DERIVED — projection of Layer 0/2, rebuildable from git
- Access: Graphiti HTTP API (port 8001)
- Scoping: `group_id` partitions (`CONSTELLATION`, `AGENT:<name>`)
- Failure mode: Graceful degradation to file-only (cache/ serves as offline snapshot)

**Sync Protocol**:
- Write: Agent → JSONL journal → memsync daemon → Graphiti `/messages` → entity materialization
- Read: Agent → Graphiti `/search` → cache/ snapshot → file fallback if Graphiti down
- Compaction: >500 lines/day or weekly → summarize → archive absorbed records
- Conflicts: Preserve both claims with timestamps, add `CONFLICTS_WITH` edges, resolve as temporal updates

**Journal Record Format**:
```jsonl
{"uuid":"mem_<ISO-TS>_<agent>_<seq>","ts":"<ISO>","agent":"<name>","scope":"shared|private","kind":"decision|preference|observation|task|fact|conflict","text":"<content>","refs":{"git":"<sha>","path":"<file>"}}
```

---

## Part III: The Antifragile Scaffold Architecture

### 3.1 The Problem

The constellation's directory structure was designed organically through 22 sessions. It works, but:
- No automated validation (broken cross-references, missing agent offices, stale DYN-* files go undetected)
- No self-healing (missing directories must be manually created)
- No safe rename infrastructure (the INT-2210 disaster proved this)
- `praxis` naming is unclear to newcomers

### 3.2 The Triangulation Process

Three models received tailored prompts:

**Oracle** — RECON: "What should SIGMA be called? What antifragile repo patterns exist at scale?"

**Vanguard** — ENGINEER: "Write scaffold_validate.sh, scaffold_heal.sh, scaffold_rename.sh. Spec the agent office scaling pattern."

**Diviner** — REASON: "What is the information-theoretically correct name? What does antifragility mean for a filesystem? How does a 20-agent constellation scale?"

### 3.3 What Each Model Found

**Oracle found** (REPO-001 through REPO-005):
- `playbook` is the overwhelming consensus term in 2026 builder communities for "battle-tested operational patterns"
- Executable Constitution Pattern: single root file (AGENTS.md) with progressive disclosure via skills — Syncrescendence has "the most advanced implementation seen"
- Hierarchical Agent Offices: flat agents/ with per-role subfolders is consensus gold
- ADR-as-Living-Code: convert ARCH-* to numbered ADR format for auditability
- Obsidian Git Vault Co-location: semantic names improve vault discoverability
- Tiered State Partitioning: split state/ into ref/, dyn/, adr/ to prevent drift

**Vanguard produced** (complete scripts):
- `scaffold_validate.sh`: Checks required dirs, agent office structure, flat principle, DYN-* cadence, ARCH-* headers, broken cross-references, Makefile configs. JSON output. Exit code 0/1.
- `scaffold_heal.sh`: Creates missing dirs, generates INIT.md from template, fixes broken links when target is unambiguous. Never deletes. Produces human-attention report for everything else.
- `scaffold_rename.sh`: One-time numbered→semantic migration. Requires clean git. `git mv` preserves history. Python rewrites all internal references. Produces before/after count report. Runs validate at end.
- Agent scaling: discovery via `ls agents/*/`, Makefile wildcards, parameterized auto_ingest. Adding agent 6 = create directory + `scaffold_heal.sh` fills in the structure.

**Diviner reasoned**:
- `praxis/` is the information-theoretically correct name: "the domain where theory is subjected to the friction of reality." Establishes clear flow: `sources/ → engine/ → praxis/ → canon/`
- **Structural mutagenesis**: A `quarantine/` namespace for anomalous artifacts. Monitor read-access frequency. High-frequency access = emergent need → autonomous promotion to new named directory. The scaffold learns from its own usage patterns.
- **Hierarchical Small-World Network** for 20-agent scale: dense local clusters (specialized pods) connected by sparse high-bandwidth bridge nodes
- **Bipartite Memory Architecture**: Agent State vs Shared Artifacts. Agents cannot modify other agents' internal state. Interaction only through shared artifacts or formalized message-passing.
- **Stigmergic Vault**: Obsidian graph view as real-time topographic map of cognitive weight. Strict kebab-case filenames for scripts; human legibility via YAML frontmatter.

### 3.4 Consensus + Decisions

**Naming**: Oracle recommended `playbook` (community consensus). Diviner reasoned `praxis` (information-theoretic precision). **Decision**: Sovereign to choose. Both are valid. `praxis` captures the epistemic lifecycle (theory → practice → canon) more precisely. `playbook` has better immediate recognition.

**Antifragile scripts**: Vanguard's scripts adopted wholesale. Install validate → heal → rename in that order. The critical lesson from INT-2210: **validate MUST exist and pass BEFORE rename runs.**

**Phase gating**: New constitutional rule (INT-P030): No phase begins until prior phase P0 items are DONE. Infrastructure → Memory → Scaffold → Automations → Hardening → Scale.

**Numbered→semantic rename**: Deferred to Phase 4 (DC-146). Only after: memory works, scaffold_validate passes, rollback is tested. The INT-2210 revert proved that running rename without these preconditions is catastrophic.

---

## Part IV: The Execution Order

### 4.1 Why This Order

The dependency chain was established by forensic analysis at Council 22:

1. **Infrastructure** (Docker/Graphiti/agents alive) — nothing works without running services
2. **Memory** (memsync + JSONL journals) — without memory, every session is amnesiac, promises evaporate (14% delivery rate), and the next Commander will demolish what this one built
3. **Scaffold validation** (validate.sh + heal.sh) — structural integrity checks must exist before any structural changes
4. **Scaffold changes** (sigma rename, then later numbered rename) — only after validation infrastructure exists
5. **Automations** (cockpit, sensing, ingest) — requires agents alive + memory working
6. **Hardening** (security audit, compaction, conflict resolution) — requires everything above stable

### 4.2 The Phase Gate Rule

**No phase begins until all P0 items in the prior phase are DONE.**

This prevents the INT-2210 pattern: running rename (Phase 2) before validate exists (also Phase 2), running scaffold triage before memory works (Phase 1), running any structural change before infrastructure is alive (Phase 0).

### 4.3 Detailed Phase Breakdown

See `orchestration/state/DYN-DEFERRED_COMMITMENTS.md` for the complete phased execution plan with specific deliverables, targets, and dependencies.

---

## Part V: How to Rebuild from Scratch

If everything is lost except this document and a fresh git clone:

### Step 1: Restore Config Architecture
1. Create `AGENTS.md` at repo root — single source of constitutional law (Five Invariants + role mappings + operational registry)
2. Create thin `CLAUDE-EXT.md`, `GEMINI-EXT.md`, `OPENCLAW-EXT.md` with platform-specific extensions only
3. Create `Makefile` with `configs` target that concatenates `AGENTS.md + *-EXT.md` into platform files
4. Create numbered directories: `orchestration/{state,scripts,archive}`, `canon/`, `engine/`, `sources/`, `praxis/{mechanics,practice,syntheses,exempla}`
5. Create `agents/{commander,adjudicator,cartographer,psyche,ajna}/` each with `INIT.md`, `inbox/{pending,active,done,failed,blocked}/`, `outbox/`, `scratchpad/`, `memory/`
6. All paths relative or via `git rev-parse --show-toplevel`

### Step 2: Restore Memory Architecture
1. In each agent's `memory/`: create `MEMORY.md`, `entities/`, `journal/`, `cache/`, `sync/`
2. Build `memsync_daemon.py` per Vanguard spec: watches `journal/*.jsonl`, posts to Graphiti `/messages`, maintains `sync/state.json` and `sync/outbox.jsonl`
3. Start Neo4j + Graphiti on Mac mini (Docker)
4. Test write path: JSONL record → memsync → Graphiti → entity materialized
5. Test read path: Graphiti `/search` → cache/ → file fallback

### Step 3: Install Antifragile Scaffold
1. Install `scaffold_validate.sh` (Vanguard's complete script in RESPONSE-VANGUARD-ANTIFRAGILE_SCAFFOLD.md)
2. Install `scaffold_heal.sh`
3. Wire validate to pre-commit hook
4. Run validate — fix all violations
5. ONLY THEN consider any structural changes

### Step 4: Restore Automations
1. `auto_ingest_loop.sh` — sole dispatch system, polls inbox every 30s
2. `dispatch.sh` — creates TASK files, handles cross-machine SCP delivery
3. launchd plists for ingest loop, watchdog, weekly eval
4. Neural Bridge: SSH keys between MBA and Mac mini

### Step 5: Restore Knowledge
1. Re-read all CANON files — they are immutable verified knowledge
2. Re-read all ARCH-* files in state/ — they are architectural decisions
3. Re-read all DYN-* files in state/ — they are living infrastructure
4. Re-read the Intention Compass — it is the rolling snapshot of all Sovereign intentions across 22 sessions

---

## Part VI: Reference Index

### Source Documents (All in repo)

| Document | Path | Role |
|----------|------|------|
| Memory Architecture (decided) | `orchestration/state/ARCH-MEMORY_ARCHITECTURE.md` | The architecture spec |
| Oracle Memory RECON | `-INBOX/commander/00-INBOX0/RESPONSE-ORACLE-MEMORY_ARCHITECTURE_SENSING.md` | What Grok found |
| Vanguard Memory SPEC | `-INBOX/commander/00-INBOX0/RESPONSE-VANGUARD-MEMORY_ARCHITECTURE_ENGINEERING.md` | Full engineering spec |
| Diviner Memory REASONING | `-INBOX/commander/00-INBOX0/RESPONSE-DIVINER-MEMORY_ARCHITECTURE_REASONING.md` | Architectural reasoning |
| Oracle Scaffold RECON | `-INBOX/commander/00-INBOX0/RESPONSE-ORACLE-SCAFFOLD_CONSENSUS.md` | Config pattern consensus |
| Oracle Antifragile RECON | Desktop archive / `-SOVEREIGN/` | Naming + antifragile patterns |
| Vanguard Antifragile SPEC | Desktop archive | Complete validate/heal/rename scripts |
| Diviner Antifragile REASONING | Desktop archive | praxis naming + structural mutagenesis |
| Intention Compass | `orchestration/state/ARCH-INTENTION_COMPASS.md` | 22 sessions of Sovereign intentions |
| Deferred Commitments | `orchestration/state/DYN-DEFERRED_COMMITMENTS.md` | Phased execution plan |
| Constitutional Law | `AGENTS.md` → `CLAUDE.md` (generated) | Five Invariants + operational rules |

### Sensing Prompts (Reproducible)

| Prompt | Path | Target Model |
|--------|------|-------------|
| Memory sensing | `-SOVEREIGN/PROMPT-ORACLE-MEMORY_ARCHITECTURE_SENSING.md` | Grok |
| Memory engineering | `-SOVEREIGN/PROMPT-VANGUARD-MEMORY_ARCHITECTURE_ENGINEERING.md` | GPT |
| Memory reasoning | `-SOVEREIGN/PROMPT-DIVINER-MEMORY_ARCHITECTURE_REASONING.md` | Gemini |
| Scaffold consensus | `-SOVEREIGN/PROMPT-ORACLE-CONFIG-CONSENSUS-ARCHITECTURE.md` | Grok |
| Antifragile sensing | Desktop archive: `PROMPT-ORACLE-ANTIFRAGILE_SCAFFOLD.md` | Grok |
| Antifragile engineering | Desktop archive: `PROMPT-VANGUARD-ANTIFRAGILE_SCAFFOLD.md` | GPT |
| Antifragile reasoning | Desktop archive: `PROMPT-DIVINER-ANTIFRAGILE_SCAFFOLD.md` | Gemini |

### Key Patterns (Seared)

| Pattern | ID | Lesson |
|---------|-----|--------|
| Architecture without execution is decoration | INT-P028 | 22 sessions of pristine architecture, 14% delivery rate |
| Never triage without validation infrastructure | INT-P029 | INT-2210 forensic: rename before validate = demolition |
| Phase gates are constitutional | INT-P030 | Infrastructure → Memory → Scaffold → Automations → Hardening |
| Triangulated specs are execution-ready | INT-P031 | When 3 models converge, ACT — don't redesign |
| File-first always | INT-P017 | Markdown+grep 74.0% vs specialized tools 68.5% |
| Supersede, never delete | INT-P018 | Temporal record > current state |
| The janitor who tears down walls isn't cleaning | Council 22 | Commander took "triage" as license to "redesign" |

### Critical Anti-Patterns

1. **The .zshrc Illusion**: launchd does NOT source ~/.zshrc. EVER. Use plist EnvironmentVariables.
2. **Async Verification Gap**: NEVER commit a fix without blocking verification.
3. **Context Decay**: 86% deferred commitment loss rate. Compaction destroys navigability.
4. **Git Commit Sandbox Kill**: Claude Code's sandbox SIGKILL's `git commit` on large repos. Workaround: git plumbing (`write-tree` → `commit-tree` → `update-ref`).

---

## Part VII: The Triangulation Protocol (How to Reproduce This Process)

When facing any architectural decision:

1. **Write three tailored prompts**, one per model, optimized for cognitive strength:
   - **Oracle (Grok)** = RECON: "Search X, GitHub, communities. What exists? What's consensus? What's emerging?"
   - **Vanguard (GPT)** = ENGINEER: "Give me exact code, exact commands, exact migration steps. No hand-waving."
   - **Diviner (Gemini)** = REASON: "Reason about what nobody else is thinking. Speculate if labeled. 10-year horizon."

2. **Send all three simultaneously.** Each model gets a DIFFERENT prompt tailored to its cognitive strength. Never the same prompt to all three.

3. **Triangulate the responses:**
   - Where all three agree → HIGH CONFIDENCE → ACT ON
   - Where two agree and one diverges → CONSIDER the divergence, default to majority
   - Where all three diverge → DECISION NEEDED → escalate to Sovereign

4. **Write the synthesis** as an ARCH-* document with: Triangulation Summary table, Consensus points, Divergence points with decisions, Migration plan.

5. **Execute in phases with gates.** Never execute Phase N until Phase N-1 P0 items are DONE.

---

**END CANON-25500-ARCHITECTURE_RATIONALE-lattice.md**

*This document is CANON — immutable verified knowledge. It may be extended but not contradicted. If reality diverges from this document, update reality, not this document.*
