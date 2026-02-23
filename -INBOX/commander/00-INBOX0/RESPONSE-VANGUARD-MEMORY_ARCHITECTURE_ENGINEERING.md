You already have the correct empirical prior: "files are source of truth, databases are derived indices." Treat Graphiti as a *cross-session, cross-agent, temporally-aware indexing layer* that you can lose at any moment without losing memory. That single stance keeps the system coherent under failure, compaction, contradictions, and multi-machine drift.

Below is an engineering-grade spec that assumes your Graphiti service is the `getzep/graphiti` HTTP graph service (FastAPI) running on port **8001** (their FalkorDB profile), which matches the upstream docker-compose mapping. ([GitHub][1])

---

## 1) Graphiti integration spec (HTTP service @ :8001)

### 1.1 What Graphiti's HTTP service actually exposes (and what it doesn't)

From the upstream `server/graph_service` routers:

**Episodic ingestion**

* `POST /messages` → queues message episodes for background processing; returns `202 Accepted`. ([GitHub][2])

**Entity node creation**

* `POST /entity-node` → creates/saves an `EntityNode` directly (name/uuid/summary). ([GitHub][2])

**Edge/episode/group deletion**

* `DELETE /entity-edge/{uuid}`
* `DELETE /episode/{uuid}`
* `DELETE /group/{group_id}`
* `POST /clear` ([GitHub][2])

**Retrieval**

* `POST /search` → returns "facts" (edges) via hybrid retrieval.
* `GET /entity-edge/{uuid}`
* `GET /episodes/{group_id}?last_n=N`
* `POST /get-memory` (composes a query from messages, then searches) ([GitHub][3])

**Critical gap**

* There is **no** first-class HTTP endpoint to "create an entity-edge / relationship" deterministically. Relationship creation happens implicitly via ingestion (LLM extraction) when you add episodes/messages, unless you extend the server. ([GitHub][2])

If you need deterministic edge writes (you do, for conflict resolution and inter-agent commitments), you should add one endpoint (`POST /triples`) that calls Graphiti's `add_triplet()` API. Graphiti documents manual triple insertion in the core library. ([Zep Documentation][4])

---

### 1.2 Exact API calls you can use today

Assume:

* `GRAPHITI_BASE=http://graphiti:8001` (Docker network) or `http://<host>:8001`
* `group_id` design below (shared + per-agent)

#### (A) Episodic memory insertion (append-only) — canonical write path

Use `POST /messages`. Each message becomes a Graphiti episode (`EpisodeType.message`) internally. ([GitHub][2])

```bash
curl -sS "$GRAPHITI_BASE/messages" \
  -H 'Content-Type: application/json' \
  -d '{
    "group_id": "CONSTELLATION",
    "messages": [
      {
        "content": "Commander(agent): We run 5 agents across 2 machines. Memory is file-first. Graphiti is the cross-session graph index.",
        "uuid": "mem_2026-02-22T20:10:31Z_commander_0001",
        "name": "Commander:observation",
        "role_type": "agent",
        "role": "Commander",
        "timestamp": "2026-02-22T20:10:31.000Z",
        "source_description": "memory/commander/journal/2026-02-22.jsonl@<git_sha>"
      }
    ]
  }'
```

Response is an ack ("queued"), not completion. The ingestion work (LLM extraction + embeddings + DB writes) happens asynchronously. ([GitHub][2])

#### (B) Entity creation (deterministic node upsert)

```bash
curl -sS "$GRAPHITI_BASE/entity-node" \
  -H 'Content-Type: application/json' \
  -d '{
    "group_id": "CONSTELLATION",
    "uuid": "ent_agent_commander",
    "name": "Commander",
    "summary": "Orchestrator agent; owns system-level decisions and integration specs."
  }'
```

([GitHub][2])

#### (C) Relationship creation (two viable modes)

**Mode 1: implicit edge creation via ingestion (works now, probabilistic)**
You write a message that states the relationship in a crisp triple-like sentence; Graphiti extracts edges/facts.

```bash
curl -sS "$GRAPHITI_BASE/messages" \
  -H 'Content-Type: application/json' \
  -d '{
    "group_id": "CONSTELLATION",
    "messages": [
      {
        "content": "Ajna(agent): OpenClaw OWNS Layer2 for Ajna and Psyche. Commander stays file-based Layer2.",
        "uuid": "mem_2026-02-22T20:12:00Z_ajna_0001",
        "name": "Ajna:decision",
        "role_type": "agent",
        "role": "Ajna",
        "timestamp": "2026-02-22T20:12:00.000Z",
        "source_description": "memory/ajna/journal/2026-02-22.jsonl@<git_sha>"
      }
    ]
  }'
```

**Mode 2: deterministic edge write (recommended; requires a tiny server extension)**
Graphiti core supports manually adding a "fact triple" via `add_triplet(source_node, edge, target_node)` / `add_triplet()` wrapper. ([Zep Documentation][4])
You add `POST /triples` to the HTTP service so agents can write commitments deterministically (see §1.5).

---

### 1.3 Bidirectional sync: MEMORY.md ↔ Graphiti (safe, lossless)

You want "bidirectional," but you also want "no footguns." The way to satisfy both is:

1. **Files are authoritative** for human-curated memory and auditability (git history).
2. **Graphiti is authoritative** for derived graph structures (entity resolution, temporal edges, search).
3. "Graph → file" happens as **generated exports** into clearly-marked files that are safe to overwrite.

Concretely:

* **File → Graphiti (continuous):** journal append produces an outbox event; memsync posts it to Graphiti (`/messages`).
* **Graphiti → File (scheduled or on-demand):** memsync queries Graphiti for *high-salience* facts and entity summaries, then writes:

  * `memory/<agent>/cache/GRAPHITI_FACTS.md` (generated)
  * `memory/<agent>/cache/GRAPHITI_ENTITIES/<uuid>.md` (generated)

These caches are what keep agents functional when Graphiti is down.

---

### 1.4 Schema for a 5-agent constellation (entities, relationships, properties)

Graphiti can infer entities/edges from text episodes. You get higher precision if you constrain extraction with custom entity/edge types in the core library (Pydantic models), but the stock HTTP service does not expose those knobs yet. ([Zep Documentation][5])
So the practical schema is:

#### Namespacing via group_id (do this immediately)

* `CONSTELLATION` — shared, cross-agent memory
* `AGENT:Commander`, `AGENT:Ajna`, `AGENT:Psyche`, `AGENT:Oracle`, `AGENT:Vanguard` — private-ish partitions
* Optional: `PROJECT:<name>` partitions when you want a bounded memory slice

Because `/search` accepts a list of `group_ids`, you can query "shared + local" in one call. ([GitHub][3])

#### Canonical entities (you should upsert deterministically via `/entity-node`)

* `Agent` nodes: `ent_agent_<id>`
* `Machine` nodes: `ent_machine_<hostname>`
* `Service` nodes: `ent_service_graphiti`, `ent_service_neo4j`, `ent_service_qdrant`, `ent_service_chroma`
* `MemoryRecord` entities are not necessary as nodes because episodes already exist; store record UUIDs as episode UUIDs.

#### Relationship types (two layers)

1. **Semantic fact edges** (Graphiti-native): extracted from episodes, returned by `/search` as facts. ([GitHub][3])
2. **Control-plane edges** (your deterministic layer): you create these via `POST /triples` (server extension), e.g.

   * `OWNS_LAYER` (Agent → MemoryLayer)
   * `RUNS_ON` (Service → Machine)
   * `SOURCE_OF_TRUTH_FOR` (Storage → MemoryLayer)
   * `CONFLICTS_WITH` (FactEdge → FactEdge) (or record-level conflicts)

Graphiti's temporal model is designed to represent evolving facts and "changing relationships" over time. You should exploit that by representing contradictions as "this was true, then invalidated," rather than deleting history. ([GitHub][6])

---

### 1.5 Server extension: add deterministic edge writes (PATCH you should apply)

Add one router endpoint to the Graphiti HTTP service:

`POST /triples` accepts:

* `group_id`
* `source_uuid`, `source_name`
* `edge_uuid` (optional, generate if absent), `edge_name`, `edge_fact`
* `target_uuid`, `target_name`
* `created_at`, `valid_at` (optional; otherwise now)

This endpoint constructs `EntityNode` + `EntityEdge` and calls `graphiti.add_triplet(...)`. That call is the canonical manual "relationship creation" mechanism in Graphiti core. ([Zep Documentation][4])

Example implementation (drop into `server/graph_service/routers/ingest.py`, plus DTOs):

```python
# dto.py (add)
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AddTripleRequest(BaseModel):
    group_id: str
    source_uuid: str
    source_name: str
    target_uuid: str
    target_name: str
    edge_name: str
    edge_fact: str
    edge_uuid: Optional[str] = None
    created_at: Optional[datetime] = None
```

```python
# ingest.py (add)
import uuid as uuidlib
from datetime import datetime, timezone
from graphiti_core.nodes import EntityNode
from graphiti_core.edges import EntityEdge
from graph_service.dto import AddTripleRequest

@router.post("/triples", status_code=status.HTTP_201_CREATED)
async def add_triple(request: AddTripleRequest, graphiti: ZepGraphitiDep):
    now = datetime.now(timezone.utc)
    edge_uuid = request.edge_uuid or str(uuidlib.uuid4())
    created_at = request.created_at or now

    source_node = EntityNode(uuid=request.source_uuid, name=request.source_name, group_id=request.group_id)
    target_node = EntityNode(uuid=request.target_uuid, name=request.target_name, group_id=request.group_id)

    edge = EntityEdge(
        uuid=edge_uuid,
        group_id=request.group_id,
        source_node_uuid=request.source_uuid,
        target_node_uuid=request.target_uuid,
        created_at=created_at,
        name=request.edge_name,
        fact=request.edge_fact,
    )

    await graphiti.add_triplet(source_node, edge, target_node)
    return {"success": True, "edge_uuid": edge_uuid}
```

Then your deterministic relationship creation API call becomes:

```bash
curl -sS "$GRAPHITI_BASE/triples" \
  -H 'Content-Type: application/json' \
  -d '{
    "group_id": "CONSTELLATION",
    "source_uuid": "ent_agent_commander",
    "source_name": "Commander",
    "target_uuid": "ent_layer_2",
    "target_name": "SessionMemory",
    "edge_name": "OWNS_LAYER",
    "edge_fact": "Commander owns Layer 2 (file-based MEMORY.md + journal/)."
  }'
```

---

### 1.6 Failure modes + graceful degradation

**Graphiti HTTP down**

* Writes: append to file (always), enqueue to outbox, return success to agent, retry later.
* Reads: fall back to:

  1. local `entities/` + `MEMORY.md` grep/rg,
  2. OpenClaw `memory_search` (for agents under OpenClaw),
  3. optional vector DBs (Qdrant/Chroma) if you want, but your own benchmark says "file-first wins" so keep it optional.

**Graphiti DB backend degraded (Neo4j/FalkorDB issues)**

* Detect via `/healthcheck`.
* Freeze graph export (don't overwrite caches).
* Keep outbox growing with backpressure alarms.

**Asynchronous ingestion queue stuck**
Graphiti `/messages` queues work (202) and processes in a background worker. If you stop seeing new episodes appear in `GET /episodes/...`, treat it as "write accepted, not committed," and keep retry logic idempotent via UUIDs. ([GitHub][2])

---

### 1.7 Performance expectations at your scale (and how to measure them properly)

At ~5k entities / ~2k relationships you're well below the "graph becomes hard" regime. What will dominate latency is **LLM extraction + embeddings** during ingestion, not DB writes. Graphiti's own positioning emphasizes hybrid retrieval and typically sub-second query latency, but ingestion is workload/model dependent. ([GitHub][6])

So define performance in two numbers:

1. **Ack latency (API round-trip):** `POST /messages` returns immediately after enqueue (typically tens of ms on LAN).
2. **Commit latency (episode → entities/edges materialized):** depends on model and rate limits; measure.

A minimal benchmark harness:

```python
# bench_graphiti.py
import time, uuid, requests, datetime

BASE = "http://localhost:8001"
GROUP = "CONSTELLATION"

def post_msg(i: int):
    u = f"bench_{uuid.uuid4()}"
    payload = {
        "group_id": GROUP,
        "messages": [{
            "content": f"Commander(agent): benchmark message {i} — Bob likes bananas.",
            "uuid": u,
            "name": "Commander:bench",
            "role_type": "agent",
            "role": "Commander",
            "timestamp": datetime.datetime.utcnow().isoformat(timespec="milliseconds")+"Z",
            "source_description": "bench"
        }]
    }
    t0 = time.time()
    r = requests.post(f"{BASE}/messages", json=payload, timeout=5)
    r.raise_for_status()
    return u, (time.time() - t0)

def wait_commit(last_n=50, timeout_s=30):
    t0 = time.time()
    while time.time() - t0 < timeout_s:
        r = requests.get(f"{BASE}/episodes/{GROUP}", params={"last_n": last_n}, timeout=5)
        r.raise_for_status()
        return r.json()
    raise TimeoutError("commit not observed")

if __name__ == "__main__":
    acks = []
    for i in range(20):
        u, ack = post_msg(i)
        acks.append(ack)
    print("ack_p50_s:", sorted(acks)[len(acks)//2])
    print("ack_p95_s:", sorted(acks)[int(len(acks)*0.95)-1])
    print("sample_episodes:", wait_commit())
```

You then extend this to poll until the specific UUID appears in episodes (your commit detector).

---

## 2) Three-layer memory implementation (exact architecture)

### Layer 1 — Working memory (context window)

This is a *runtime construct*, not a store.

Rule: L1 contains only what is needed to decide the next action safely.

* current task state (goal, constraints, immediate plan)
* short "active entities" set (the handful you're manipulating)
* tool outputs only if (a) bounded and (b) immediately actionable
* never stream raw web/page dumps into L1; store them in L2 and reference by pointer

If you want a hard engineering boundary, implement an "ingestion worker" pattern: any untrusted content is processed in an isolated sub-agent context and only schema-validated outputs are promoted to L1.

### Layer 2 — Session memory (file-based, git-tracked, immediate)

Your current structure is correct: `MEMORY.md + entities/ + journal/` per agent.

I recommend one strict addition: **journal becomes machine-parseable** with stable UUIDs so sync is deterministic and idempotent.

Proposed per-agent layout:

```
memory/<agent_id>/
  MEMORY.md                 # curated
  entities/                 # human-curated entity pages
  journal/
    2026-02-22.jsonl        # append-only, machine-parseable
  cache/
    GRAPHITI_FACTS.md       # generated (overwrite ok)
    GRAPHITI_ENTITIES/      # generated (overwrite ok)
  sync/
    state.json              # last processed offsets/uuids
    outbox.jsonl            # failed graph writes, retry queue
```

Journal record format (JSONL, one object per line):

```json
{"uuid":"mem_2026-02-22T20:10:31Z_commander_0001","ts":"2026-02-22T20:10:31.000Z","agent":"Commander","scope":"shared","kind":"observation","text":"We run 5 agents across 2 machines...","refs":{"git":"<sha>","path":"memory/commander/journal/2026-02-22.jsonl"}}
```

### Layer 3 — Long-term memory (Graphiti/Neo4j graph store)

Graphiti stores:

* episodic nodes (your journal lines ingested as episodes)
* entity nodes (deduplicated, summarized)
* entity edges (facts with temporal validity)

Graphiti is well-suited to "what changed when" because it's designed around temporal knowledge graphs and incremental updates. ([GitHub][6])

---

## 3) Memory sync protocol (exact sequences)

### 3.1 Write path: observation → file → graph sync (idempotent)

**Step 0 (agent runtime)**

* Agent decides "this is durable."
* Agent writes a JSONL record to `journal/YYYY-MM-DD.jsonl` (append-only).
* Agent may also update `MEMORY.md` or an entity page (curation).

**Step 1 (memsync daemon, local)**

* Tails `journal/*.jsonl`.
* For each new line:

  * validate JSON schema
  * compute deterministic `source_description = <path>@<git_sha>`
  * choose Graphiti `group_id`:

    * `scope == shared` → `CONSTELLATION`
    * else → `AGENT:<agent_id>`
  * POST to `/messages` with UUID = record.uuid

**Step 2 (commit observation)**

* Because `/messages` is async, memsync optionally polls `GET /episodes/<group_id>?last_n=N` until it sees UUID (or times out and leaves it in outbox). ([GitHub][3])

**Idempotency**

* Reposting the same UUID should be safe; if the backend does "find or create" by UUID, duplicates collapse. If it doesn't, you wrap it: your memsync keeps a `sent_uuids` set (SQLite or state.json).

### 3.2 Read path: cross-agent query → graph → file cache

**Step 0**

* Agent forms query using "active entities" + question.

**Step 1**

* Call Graphiti `/search` with `group_ids=[CONSTELLATION, AGENT:<self>]` and `max_facts` tuned (start 25). ([GitHub][3])

```bash
curl -sS "$GRAPHITI_BASE/search" \
  -H 'Content-Type: application/json' \
  -d '{
    "group_ids": ["CONSTELLATION","AGENT:Commander"],
    "query": "What is the current three-layer memory architecture and who owns Layer 2?",
    "max_facts": 25
  }'
```

**Step 2**

* memsync writes the returned facts into `cache/GRAPHITI_FACTS.md` with timestamp and edge UUIDs (generated, overwrite OK).

**Step 3**

* If Graphiti is down, the agent reads the cache file + local MEMORY.md + entities.

### 3.3 Memory compaction (journal growth management)

Trigger compaction when either:

* daily file exceeds N lines (e.g. 500), or
* weekly boundary, or
* "compaction marker" committed by Commander.

Compaction algorithm:

1. Select a contiguous slice of journal records (oldest first).
2. Summarize into:

   * updates to `MEMORY.md` (curated)
   * entity page deltas (entities/)
   * a single "compaction episode" JSONL record containing:

     * list of absorbed UUIDs
     * the resulting distilled facts
3. Move the absorbed records to `journal/archive/YYYY-MM-DD.jsonl` (or keep them; git can handle it, but your retrieval noise grows).
4. In Graphiti, do not delete old episodes unless you have to; instead, add the compaction episode so retrieval prefers the summary.

OpenClaw already has a "pre-compaction memory flush" concept; you can align your compaction trigger with its thresholds for the agents it runs. ([OpenClaw][7])

### 3.4 Conflict resolution (two agents contradict)

Represent contradictions explicitly; do not overwrite history.

Minimum viable conflict protocol:

* Every durable fact has: `uuid`, `agent`, `ts`, `confidence`, `evidence_refs[]`.
* If a new record contradicts an existing claim:

  1. write a `conflict` record in journal (scope shared)
  2. add deterministic control-plane edges (via `/triples`) once you have it:

     * `CONFLICTS_WITH(edge_uuid_A, edge_uuid_B)`
     * `PREFERRED(edge_uuid_X)` with justification
  3. if you stay purely in Graphiti-native semantics, you instead add an episode that states invalidation with time:

     * "As of 2026-02-22, claim A is considered outdated; claim B is current."

Graphiti's temporal orientation is designed to keep "what was true when," so you should treat "resolution" as a temporal update rather than deletion. ([GitHub][6])

---

## 4) OpenClaw memory integration (mapping to three layers + ownership)

OpenClaw's upstream memory model:

* Memory is Markdown in workspace; daily logs + optional curated `MEMORY.md`.
* Tools: `memory_search`, `memory_get`.
* Hybrid search (BM25 + vector) and graceful degradation on missing files are built in. ([OpenClaw][7])

### Mapping

* **Layer 1:** OpenClaw session context window (managed by OpenClaw's pruning/compaction).
* **Layer 2:** OpenClaw workspace memory files (`memory/YYYY-MM-DD.md`, `MEMORY.md`) — aligns perfectly with your file-first Layer 2. ([OpenClaw][7])
* **Layer 3:** Graphiti graph store — you add this.

### Ownership recommendation

* Let OpenClaw "own" Layer 2 *for the agents it runs* (Ajna, Psyche), by pointing their workspace memory directory at your git-tracked repo paths (symlink or bind mount).
* Commander can remain purely file-driven (same format), no OpenClaw dependency.
* Vanguard/Oracle can be whichever runtime you prefer; the sync protocol is the same as long as they append JSONL records.

### Data flow: OpenClaw memory ↔ git-tracked memory ↔ Graphiti

1. OpenClaw writes to its workspace memory markdown files.
2. You add a small "export hook" (or a cron) that converts those markdown writes into your JSONL journal records (or you standardize OpenClaw to write JSONL directly via an agent tool—either works).
3. memsync picks up JSONL records and posts them to Graphiti.
4. Graphiti facts are exported back into `cache/` files, which OpenClaw agents can read via `memory_get` even during Graphiti downtime.

If you decide to build an OpenClaw plugin: OpenClaw supports plugins and has an exclusive "memory" slot for alternate backends (e.g., memory-lancedb). A "memory-graphiti" plugin could merge Graphiti recall with file recall, but you don't need that in phase 1; you can just expose a new tool (`graphiti_search`) via plugin and let the agent call it. ([OpenClaw][8])

---

## 5) Migration plan (THIS WEEK / 2 WEEKS / 30 DAYS)

### Phase 1 (this week): stabilize write/read paths, no backfill yet

**1) Ensure Graphiti is up and health-checked**
If you're using upstream compose profiles for FalkorDB mode, Graphiti maps to `8001`. ([GitHub][1])

```bash
# if you adopted upstream compose
docker compose --profile falkordb up -d falkordb graph-falkordb
curl -sS http://localhost:8001/healthcheck
```

**2) Add memsync daemon (single responsibility)**

* Watches `memory/**/journal/*.jsonl`
* Posts to Graphiti `/messages`
* Maintains:

  * `sync/state.json` (per agent)
  * `sync/outbox.jsonl` (per agent)

Run it as a container so both machines behave the same:

```yaml
# docker-compose.memsync.yml
services:
  memsync:
    image: python:3.12-slim
    working_dir: /app
    volumes:
      - ./memsync:/app
      - ./memory:/memory
      - ./.git:/repo_git:ro
    environment:
      - GRAPHITI_BASE=http://graphiti:8001
    command: ["python","-u","memsync_daemon.py"]
```

**3) Update your agents to write JSONL records**
No restructuring required; just add the JSONL append when something is "durable."

### Phase 2 (two weeks): deterministic edges + backfill

**1) Patch Graphiti server with `POST /triples`**
(§1.5). This unlocks deterministic relationship writes for:

* agent ownership
* capability declarations
* conflict edges
* "current truth" markers

**2) Backfill existing `MEMORY.md` + entity pages**

* Convert each paragraph/section into a synthetic JSONL record with stable UUID.
* Ingest as `/messages` with `source_description = backfill:<path>@<sha>`

Backfill script skeleton:

```python
# backfill_memory_md.py
import hashlib, pathlib, datetime, requests

BASE="http://localhost:8001"
GROUP="CONSTELLATION"

def stable_uuid(path:str, chunk:str)->str:
    h = hashlib.sha256((path+"\n"+chunk).encode()).hexdigest()[:16]
    return f"backfill_{h}"

# parse your markdown into chunks, then POST /messages per chunk
```

### Phase 3 (30 days): compaction + conflict + observability

**1) Implement compaction job**

* weekly roll-up per agent
* emits compaction episodes
* updates curated MEMORY.md

**2) Implement conflict protocol**

* detect likely contradictions (simple heuristics first: same subject, opposing predicates)
* represent them explicitly in file + graph
* use deterministic edges once `/triples` exists

**3) Add monitoring**

* scrape Graphiti `/healthcheck`
* track outbox backlog length
* alert on "ack ok, commit not observed" rate

---

## One thing I would enforce immediately (because it makes everything else tractable)

Make "durable memory" a first-class record type with:

* stable UUID
* timestamp
* scope (shared vs agent)
* kind (decision / preference / observation / task / fact / conflict)
* evidence refs

That single discipline converts "memory" from prose into an append-only event log that can be indexed by Graphiti, searched by OpenClaw, audited via git, compacted safely, and reconciled across two machines without guesswork.

If you want, I can also give you a concrete `memsync_daemon.py` (watcher + outbox + retry + polling) and a minimal JSON Schema for record validation, tuned to your five-agent constellation and your existing directory conventions.

: https://raw.githubusercontent.com/getzep/graphiti/main/docker-compose.yml "raw.githubusercontent.com"
: https://raw.githubusercontent.com/getzep/graphiti/main/server/graph_service/routers/ingest.py "raw.githubusercontent.com"
: https://raw.githubusercontent.com/getzep/graphiti/main/server/graph_service/routers/retrieve.py "raw.githubusercontent.com"
: https://help.getzep.com/graphiti/working-with-data/adding-fact-triples "Adding Fact Triples | Zep Documentation"
: https://help.getzep.com/graphiti/core-concepts/custom-entity-and-edge-types "Custom Entity and Edge Types | Zep Documentation"
: https://github.com/getzep/graphiti "GitHub - getzep/graphiti: Build Real-Time Knowledge Graphs for AI Agents"
: https://docs.openclaw.ai/concepts/memory "Memory - OpenClaw"
: https://docs.openclaw.ai/tools/plugin "Plugins - OpenClaw"
