# ARCH-MEMORY_ARCHITECTURE.md
## Triangulated Memory Architecture Decision
**Version**: 1.0.0
**Created**: 2026-02-22
**Authority**: Sovereign directive + Oracle/Vanguard/Diviner triangulation
**Status**: ARCHITECTURE DECIDED — awaiting execution

---

## Decision: Sovereign Temporal Hybrid (STH)

Three independent sensing passes converged on the same fundamental architecture. This is rare and high-confidence.

### Triangulation Summary

| Agent | Role | Core Finding | Confidence |
|-------|------|-------------|------------|
| **Oracle (Grok)** | RECON | Graphiti on Neo4j is the best production graph memory; file-first remains constitutional; 7-day migration viable | HIGH |
| **Vanguard (GPT)** | ENGINEER | Full implementation spec: JSONL journals, memsync daemon, `/triples` server extension, 3-phase migration | HIGH |
| **Diviner (Gemini)** | REASON | CQRS on git substrate; graph/vector are ephemeral projections; per-agent cognitive morphogenesis; autopoietic decay | HIGH (speculative on decay) |

### Where They Agree (CONSENSUS = ACT ON)
1. **File-first is constitutional — never abandon it**
2. **Graphiti on Neo4j is the right graph layer** (we already run it)
3. **Three-layer architecture**: Working Memory (context) → Session Memory (files) → Long-term Memory (graph)
4. **Graph and vector are PROJECTIONS, not source of truth** — rebuildable from git
5. **Cross-agent memory via shared graph partitions** (group_id scoping)
6. **JSONL journals as the machine-parseable event stream** bridging file ↔ graph

### Where They Diverge (DECISIONS NEEDED)
1. **Vector DB role**: Oracle says optional; Vanguard says skip for now; Diviner says use for Claude's divergent recall specifically. **Decision**: DEFER — vector stays dormant until we have a concrete Claude-specific use case.
2. **Sixth "Memory Agent"**: Diviner proposes a topological observer daemon running graph algorithms. **Decision**: DEFER to Phase 3 — brilliant but premature. Note for Ajna's strategic horizon.
3. **Autopoietic decay**: Diviner proposes Hebbian learning on edge weights. **Decision**: CAPTURE as long-term vision. Current staleness detection (timestamp-based) is sufficient for now.
4. **Per-agent cognitive shaping of memory retrieval**: Diviner proposes different query routing per cognitive style. **Decision**: ADOPT IN PRINCIPLE — implement as different default `max_facts` and `group_ids` per agent in their harness configs.

---

## The Three Layers (Decided Architecture)

### Layer 0: Constitutional Truth (Git)
- **What**: Git-tracked Markdown files — MEMORY.md, entities/, journal/
- **Authority**: ABSOLUTE — this is ground truth per Repo Sovereignty invariant
- **Failure mode**: None — if git works, Layer 0 works
- **Who writes**: ALL agents
- **Who reads**: ALL agents (always available)

### Layer 1: Working Memory (Context Window)
- **What**: Current context window contents — task state, active entities, tool outputs
- **Authority**: Ephemeral — dies with the session
- **Rule**: Only what's needed to decide the next action safely
- **Per-agent tuning**:
  - Claude (Commander): Wide lateral context, high `max_facts` from graph
  - GPT (Psyche/Adjudicator): Narrow, precise, schema-matched
  - Gemini (Cartographer): Pre-computed relational subgraph in plaintext (shield from tool orchestration)
  - Kimi (Ajna): Strategic context only, no tactical noise

### Layer 2: Session Memory (File-Based, Git-Tracked)
- **What**: `agents/<name>/memory/` — MEMORY.md + entities/ + journal/ + cache/ + sync/
- **Authority**: Durable — survives session death, context compaction, machine restart
- **Format**: JSONL journals (machine-parseable, stable UUIDs, idempotent sync)
- **Ownership**:
  - Psyche/Ajna: OpenClaw OWNS Layer 2 (its workspace memory IS our Layer 2)
  - Commander/Adjudicator/Cartographer: File-based Layer 2 (same format, no OpenClaw dependency)

### Layer 3: Long-Term Memory (Graphiti on Neo4j)
- **What**: Temporal knowledge graph — entities, relationships, episodes, facts
- **Authority**: DERIVED — projection of Layer 0/2, rebuildable from git
- **Access**: Via Graphiti HTTP API (port 8001) — `/messages`, `/search`, `/entity-node`
- **Scoping**: `group_id` partitions — `CONSTELLATION` (shared), `AGENT:<name>` (private)
- **Failure mode**: Graceful degradation to file-only (cache/ files serve as offline snapshot)

---

## Sync Protocol (Vanguard Spec — Adopted)

### Write Path: Agent → File → Graph
1. Agent writes JSONL record to `journal/YYYY-MM-DD.jsonl` (append-only, stable UUID)
2. memsync daemon tails journal, posts to Graphiti `/messages`
3. Graphiti processes asynchronously (LLM extraction → entity/edge materialization)
4. memsync tracks sync state in `sync/state.json`, retries via `sync/outbox.jsonl`

### Read Path: Agent → Graph → Cache → File
1. Agent queries Graphiti `/search` with `group_ids=[CONSTELLATION, AGENT:<self>]`
2. Results cached to `cache/GRAPHITI_FACTS.md` (overwrite OK — generated)
3. If Graphiti down: agent reads cache + local MEMORY.md + entities/

### Compaction: Journal → Summary → Archive
1. Trigger: >500 lines/day OR weekly boundary
2. Summarize into MEMORY.md updates + entity page deltas
3. Emit compaction episode with absorbed UUIDs
4. Archive absorbed records to `journal/archive/`

### Conflict Resolution: Preserve Contradictions
- Contradictions are SIGNAL, not errors
- Both claims preserved with timestamps
- `CONFLICTS_WITH` edges added to graph
- Resolution recorded as temporal update ("as of DATE, claim B supersedes claim A")

---

## Journal Record Format (Adopted from Vanguard)

```jsonl
{"uuid":"mem_2026-02-22T20:10:31Z_commander_0001","ts":"2026-02-22T20:10:31.000Z","agent":"Commander","scope":"shared","kind":"observation","text":"Description of durable memory","refs":{"git":"<sha>","path":"memory/commander/journal/2026-02-22.jsonl"}}
```

Fields:
- `uuid`: Deterministic, stable, idempotent
- `ts`: ISO timestamp
- `agent`: Agent name
- `scope`: `shared` (→ CONSTELLATION group) or `private` (→ AGENT:<name> group)
- `kind`: `decision` | `preference` | `observation` | `task` | `fact` | `conflict`
- `text`: The memory content
- `refs`: Evidence pointers (git sha, file path)

---

## Per-Agent Memory Layout (Target State)

```
agents/<agent>/memory/
├── MEMORY.md              # curated, human-readable
├── entities/              # semantic anchor pages
├── journal/
│   ├── 2026-02-22.jsonl   # append-only event stream
│   └── archive/           # compacted records
├── cache/
│   ├── GRAPHITI_FACTS.md  # generated graph snapshot
│   └── GRAPHITI_ENTITIES/ # generated entity pages
└── sync/
    ├── state.json         # last processed offsets
    └── outbox.jsonl       # failed writes, retry queue
```

---

## Migration Plan

### Phase 1: THIS WEEK (Days 1-3)
1. Verify Graphiti health on Mac mini (`curl http://localhost:8001/healthcheck`)
2. Create `scripts/memsync_daemon.py` — journal watcher + Graphiti poster + outbox retry
3. Add JSONL journal append to Commander's session hooks (extend `create_execution_log.sh`)
4. Create `cache/` and `sync/` directories in each agent's memory/
5. Test write path: Commander journal entry → memsync → Graphiti → entity materialized

### Phase 2: NEXT 2 WEEKS (Days 4-10)
1. Patch Graphiti server with `POST /triples` endpoint (Vanguard's spec, §1.5)
2. Backfill existing MEMORY.md + entity pages into Graphiti
3. Add Graphiti query tools to agent harnesses via *-EXT.md
4. Implement read path: Commander queries graph → cache → file fallback
5. Wire OpenClaw Psyche/Ajna to JSONL journal format

### Phase 3: 30 DAYS
1. Compaction job (weekly per agent)
2. Conflict detection + resolution protocol
3. Staleness-based edge decay (timestamp, not Hebbian — yet)
4. Cross-machine sync testing (MBA ↔ Mac mini via git + Graphiti)
5. Evaluate "Memory Agent" daemon (Diviner's topological observer proposal)

---

## Strategic Horizon (Diviner's Vision — Captured for Ajna)

### CQRS on Git Substrate
Git IS an event-sourced ledger. Commits = episodes. Diffs = cognitive deltas. The graph and vector stores are read-model projections that can be destroyed and rebuilt from git history. This is the 10-year architecture.

### Cognitive Morphogenesis
Each agent's memory retrieval should be shaped by its cognitive profile:
- Claude: High-temperature vector search for lateral leaps
- GPT: Strict schema matches from file + localized graph
- Gemini: Pre-computed relational subgraph in plaintext
- Grok: Chronological episodic sequence from git diffs

### Autopoietic Decay (Long-Term)
Edges that are frequently traversed gain weight. Untraversed edges decay. The memory system improves its own retrieval efficiency over time. Git remains the eternal append-only log; only the projection layer learns to forget.

### The Sixth Agent
A non-LLM topological observer running graph algorithms (PageRank, community detection) over the shared graph. When it detects emergent clusters bridging isolated domains, it injects synthesized observations back into git. The subconscious of the constellation.

---

## References

- Oracle RECON: `-INBOX/commander/00-INBOX0/RESPONSE-ORACLE-MEMORY_ARCHITECTURE_SENSING.md`
- Vanguard SPEC: `-INBOX/commander/00-INBOX0/RESPONSE-VANGUARD-MEMORY_ARCHITECTURE_ENGINEERING.md`
- Diviner REASONING: `-INBOX/commander/00-INBOX0/RESPONSE-DIVINER-MEMORY_ARCHITECTURE_REASONING.md`
- Graphiti docs: https://help.getzep.com/graphiti/
- Graphiti repo: https://github.com/getzep/graphiti
- OpenClaw memory: https://docs.openclaw.ai/concepts/memory
