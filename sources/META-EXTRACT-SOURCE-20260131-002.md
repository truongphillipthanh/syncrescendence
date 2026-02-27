# Extraction: SOURCE-20260131-002

**Source**: `SOURCE-20260131-x-article-nateliason-agentic_personal_knowledge_management_with_openclaw_para_and_qmd.md`
**Atoms extracted**: 26
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (7)

### ATOM-SOURCE-20260131-002-0002
**Lines**: 24-27
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Most AI assistants have shallow memory features, often just a flat list of facts without structure, decay, or hierarchy, requiring users to repeat information constantly.

### ATOM-SOURCE-20260131-002-0011
**Lines**: 148-150
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Facts with high accessCount resist decay, preventing important-but-intermittent facts from falling off the radar.

### ATOM-SOURCE-20260131-002-0018
**Lines**: 190-191
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> The system ensures summary.md always reflects the current mental model of an entity, not its complete history, with the full history residing in items.json.

### ATOM-SOURCE-20260131-002-0021
**Lines**: 205-207
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> The system ensures no information loss through a no-deletion rule and an archive system, allowing tracing back to when something was learned and how it evolved.

### ATOM-SOURCE-20260131-002-0022
**Lines**: 209-211
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Tiered retrieval (summary first, then facts) improves context window efficiency by preventing the agent from loading everything it knows, as most conversations only need the summary.

### ATOM-SOURCE-20260131-002-0023
**Lines**: 213-215
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> The system has a natural lifecycle where entities flow from Projects to Archives when complete, and facts flow from Hot to Warm to Cold as they age, making it a dynamic rather than static database.

### ATOM-SOURCE-20260131-002-0026
**Lines**: 268-270
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> The system is deliberately low-tech, using markdown files and JSON backed up to a private git repo, without a database or special tooling, to avoid vendor lock-in and ensure memory portability across AI assistants.

## Concept (5)

### ATOM-SOURCE-20260131-002-0005
**Lines**: 68-80
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> The PARA method categorizes every entity in one of four buckets (Projects, Areas, Resources, Archives), with entities naturally flowing between them over time, and nothing ever being deleted, only archived.

### ATOM-SOURCE-20260131-002-0012
**Lines**: 150-153
**Context**: hypothesis / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.30, actionability=0.60, epistemic_stability=0.50

> Memory decay in an AI system mimics human memory by making recent and frequently-accessed information more available, implemented through recency weighting on summary files.

### ATOM-SOURCE-20260131-002-0019
**Lines**: 197-199
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Separation of concerns in a knowledge system means each layer (knowledge graph for 'what', daily notes for 'when', tacit knowledge for 'how') has a clear, distinct job.

### ATOM-SOURCE-20260131-002-0020
**Lines**: 201-203
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Graceful degradation in a knowledge system means there are fallbacks if a component fails, e.g., if heartbeat extraction misses something, it's still in daily notes; if a summary is stale, full facts are in items.json.

### ATOM-SOURCE-20260131-002-0024
**Lines**: 221-226
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> QMD is a local indexing and retrieval tool that indexes markdown files into a SQLite database and provides full-text search (BM25), vector similarity search, and combined query modes.

## Framework (6)

### ATOM-SOURCE-20260131-002-0003
**Lines**: 39-47
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> A three-layer memory architecture for personal AI assistants includes a Knowledge Graph (long-term declarative memory), Daily Notes (episodic memory), and Tacit Knowledge (procedural memory).

### ATOM-SOURCE-20260131-002-0004
**Lines**: 50-64
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> The Knowledge Graph layer is a directory tree organized using Tiago Forte's PARA method, comprising 'projects' (active work), 'areas' (ongoing responsibilities), 'resources' (reference material), and 'archives' (inactive items).

### ATOM-SOURCE-20260131-002-0007
**Lines**: 94-114
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.60

> The atomic fact schema includes fields like `id`, `fact`, `category` (milestone, status, preference, context), `timestamp`, `source`, `status` (active/superseded), `supersededBy` (pointer to new fact), `relatedEntities` (cross-references), `lastAccessed`, and `accessCount`.

### ATOM-SOURCE-20260131-002-0009
**Lines**: 129-136
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> Daily notes serve as a raw, chronological timeline of events, capturing conversation details without immediate structure, and are retained as the source-of-truth timeline after durable facts are extracted to the knowledge graph.

### ATOM-SOURCE-20260131-002-0010
**Lines**: 139-146
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> Tacit knowledge is stored in a single file, capturing user patterns and preferences (communication, working style, tools, rules) that change slowly and are updated only when new patterns emerge.

### ATOM-SOURCE-20260131-002-0013
**Lines**: 152-155
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.70

> The decay model for facts is simple, using three tiers based on recency (Hot, Warm, Cold) with frequency as a modifier, without exponential curves or tunable parameters.

## Praxis Hook (8)

### ATOM-SOURCE-20260131-002-0001
**Lines**: 17-20
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> To give an AI agent durable, structured memory, use a three-layer approach built on Tiago Forte's PARA framework, extended with atomic facts, memory decay, and automated extraction.

### ATOM-SOURCE-20260131-002-0006
**Lines**: 84-90
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.60

> For tiered retrieval in a knowledge graph, each entity should have two files: a concise `summary.md` for quick context and an `items.json` array of atomic facts for granular detail, loaded only when needed.

### ATOM-SOURCE-20260131-002-0008
**Lines**: 118-123
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> Implement a 'no-deletion rule' for facts: when information changes, mark the old fact as `superseded` and create a new one, preserving a full history and allowing tracing of evolution over time.

### ATOM-SOURCE-20260131-002-0014
**Lines**: 157-161
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.60

> Implement access tracking for memory decay: every time a fact is used, increment `accessCount` and update `lastAccessed` to create a usage signal independent of creation time.

### ATOM-SOURCE-20260131-002-0015
**Lines**: 161-168
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> An automated heartbeat process should periodically scan recent conversations for new information, extract durable facts (relationships, status changes, milestones, decisions), write them to the knowledge graph, update daily notes with timeline entries, and bump access metadata on referenced facts.

### ATOM-SOURCE-20260131-002-0016
**Lines**: 173-177
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> To prevent a knowledge graph from filling with one-off mentions, create an entity only if it's mentioned 3+ times, has a direct relationship to you, or is a significant project/company; otherwise, capture it in daily notes.

### ATOM-SOURCE-20260131-002-0017
**Lines**: 181-188
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> Once a week, rewrite summary.md files by loading all active facts, sorting them by recency tier (Hot → Warm → Cold) and then by accessCount, writing Hot and Warm facts into summary.md, and dropping Cold facts from the summary.

### ATOM-SOURCE-20260131-002-0025
**Lines**: 257-266
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> To implement a knowledge system for an AI assistant, start with the directory structure (PARA folders, index.md), then create summary.md and items.json for one active project and one important person, add daily notes, automate extraction later, and add decay last.
