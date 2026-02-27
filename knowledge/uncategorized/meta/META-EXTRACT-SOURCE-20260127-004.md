# Extraction: SOURCE-20260127-004

**Source**: `SOURCE-20260127-x-article-spacepixel-the_three_layer_memory_system_upgrade_for_clawdbot.md`
**Atoms extracted**: 31
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (7)

### ATOM-SOURCE-20260127-004-0001
**Lines**: 10-10
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.10, epistemic_stability=0.90

> Most AI assistants forget by default.

### ATOM-SOURCE-20260127-004-0002
**Lines**: 10-37
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Clawdbot's out-of-the-box memory is static and requires manual maintenance.

### ATOM-SOURCE-20260127-004-0006
**Lines**: 44-52
**Context**: hypothesis / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> The Three-Layer Memory System allows for automatic fact extraction from conversations, entity-based storage of facts (by person, company, or project), weekly synthesis to rewrite summaries and prune stale context, and superseding (not deleting) old facts to preserve full history.

### ATOM-SOURCE-20260127-004-0007
**Lines**: 54-54
**Context**: hypothesis / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.60

> The Three-Layer Memory System results in Clawdbot's understanding updating itself and context staying current without manual edits.

### ATOM-SOURCE-20260127-004-0017
**Lines**: 187-198
**Context**: hypothesis / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.20, speculation_risk=0.30, actionability=0.80, epistemic_stability=0.70

> The Three-Layer Clawdbot system is superior to vector databases/RAG (which are black boxes), monolithic context files (which don't scale, go stale, and are expensive), and basic static Clawdbot by offering readable files, automatic maintenance, and compounding intelligence.

### ATOM-SOURCE-20260127-004-0028
**Lines**: 294-298
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.60, actionability=0.70, epistemic_stability=0.60

> A Clawdbot implementing the described memory system will never forget, never go stale, cost pennies to maintain, understand complex relationships like 'boss vs former boss', and get smarter every week.

### ATOM-SOURCE-20260127-004-0029
**Lines**: 300-303
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.60, actionability=0.70, epistemic_stability=0.60

> An AI assistant that implements the Three-Layer Memory System will wake up better informed than yesterday, leading to a growing knowledge graph, improved context, and better responses.

## Concept (4)

### ATOM-SOURCE-20260127-004-0008
**Lines**: 70-72
**Context**: hypothesis / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.30, actionability=0.70, epistemic_stability=0.60

> Compounding intelligence refers to a system where every conversation adds signal, which is then distilled weekly, leading to a richer, structured, searchable, and current understanding of one's life over time.

### ATOM-SOURCE-20260127-004-0010
**Lines**: 91-107
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Atomic facts are discrete, timestamped units of information stored in `items.json` for each entity, which are superseded (marked as 'superseded' with a reference to the new fact) rather than erased when reality changes, preserving a full history.

### ATOM-SOURCE-20260127-004-0011
**Lines**: 110-116
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Living summaries are weekly-rewritten snapshots for each entity, stored in `summary.md`, which prevent Clawdbot from loading hundreds of raw facts into context and ensure old information fades naturally while context remains lean and accurate.

### ATOM-SOURCE-20260127-004-0030
**Lines**: 305-305
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.70

> The difference between an AI assistant and an AI that actually knows you lies in the latter's ability to continuously improve its knowledge and context.

## Framework (8)

### ATOM-SOURCE-20260127-004-0003
**Lines**: 12-14
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> The Three-Layer Memory System upgrades Clawdbot's memory into a self-maintaining, compounding knowledge graph, consisting of Layer 1: Knowledge Graph (/life/areas/) for entities with atomic facts and living summaries, Layer 2: Daily Notes (memory/YYYY-MM-DD.md) for raw event logs, and Layer 3: Tacit Knowledge (MEMORY.md) for patterns, preferences, and lessons learned.

### ATOM-SOURCE-20260127-004-0005
**Lines**: 25-30
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Clawdbot's out-of-the-box memory primitives include AGENTS.md for behavioral rules, MEMORY.md for persistent user preferences, Heartbeats for periodic wake-ups, and Cron jobs for scheduled automation.

### ATOM-SOURCE-20260127-004-0009
**Lines**: 78-88
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Layer 1 of the Three-Layer Memory System, the Knowledge Graph, organizes meaningful entities (people, companies, projects) into folders, each containing atomic facts in `items.json` and living summaries in `summary.md`.

### ATOM-SOURCE-20260127-004-0012
**Lines**: 119-127
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Layer 2 of the Three-Layer Memory System, Daily Notes (`memory/YYYY-MM-DD.md`), serves as a raw timeline where Clawdbot continuously writes event logs, from which durable facts are later extracted into Layer 1.

### ATOM-SOURCE-20260127-004-0013
**Lines**: 130-142
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Layer 3 of the Three-Layer Memory System, Tacit Knowledge (`MEMORY.md`), captures how the user operates, including work habits, contact preferences, and lessons learned, distinguishing these as facts about the user rather than facts about the world.

### ATOM-SOURCE-20260127-004-0016
**Lines**: 168-178
**Context**: hypothesis / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.30, actionability=0.70, epistemic_stability=0.60

> The 'Flywheel' describes a compounding process where conversation leads to extracted facts, which grows the knowledge graph, leading to weekly synthesis, resulting in better context for the next chat, better responses, and more conversation.

### ATOM-SOURCE-20260127-004-0022
**Lines**: 243-252
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> The atomic fact schema for `items.json` includes `id`, `fact`, `category` (e.g., relationship, milestone, status, preference), `timestamp`, `source` (e.g., conversation), `status` (active, superseded), and `supersededBy`.

### ATOM-SOURCE-20260127-004-0027
**Lines**: 283-290
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> An atomic fact schema for a Clawbot includes fields for `id`, `fact`, `category` (relationship, milestone, status, preference), `timestamp`, `source`, `status` (active, superseded), and `supersededBy`.

## Praxis Hook (12)

### ATOM-SOURCE-20260127-004-0004
**Lines**: 16-16
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=1.00, epistemic_stability=0.60

> To upgrade Clawdbot's memory, copy this article into Clawdbot.

### ATOM-SOURCE-20260127-004-0014
**Lines**: 149-157
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=1.00, epistemic_stability=0.70

> A cheap sub-agent (e.g., Haiku) should scan recent conversations every ~30 minutes to extract durable facts, such as relationships, status changes, and milestones, writing them to the relevant entity's `items.json`.

### ATOM-SOURCE-20260127-004-0015
**Lines**: 160-165
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=1.00, epistemic_stability=0.70

> Clawdbot should perform a weekly synthesis on Sunday, reviewing newly added facts, updating relevant summaries, marking contradicted facts as historical, and producing a clean, current snapshot.

### ATOM-SOURCE-20260127-004-0018
**Lines**: 203-206
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=1.00, epistemic_stability=0.70

> To implement the Three-Layer Memory System, create the folder structure: `~/life/areas/people`, `~/life/areas/companies`, and `~/clawd/memory`.

### ATOM-SOURCE-20260127-004-0019
**Lines**: 208-220
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=1.00, epistemic_stability=0.70

> Add rules to `AGENTS.md` for Layer 1: Knowledge Graph, specifying `people/` and `companies/` folders, tiered retrieval (summary.md for quick context, items.json for atomic facts), and rules to save facts immediately, rewrite `summary.md` weekly from active facts, and supersede rather than delete facts.

### ATOM-SOURCE-20260127-004-0020
**Lines**: 222-232
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=1.00, epistemic_stability=0.70

> Add a 'Fact Extraction' section to `HEARTBEAT.md` that instructs Clawdbot to check for new conversations on each heartbeat, spawn a cheap sub-agent to extract durable facts (focusing on relationships, status changes, milestones, skipping casual/temporary info), write them to relevant entity `items.json`, and track `lastExtractedTimestamp`.

### ATOM-SOURCE-20260127-004-0021
**Lines**: 234-241
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=1.00, epistemic_stability=0.70

> Implement a weekly synthesis cron job (on Sunday) that, for each entity with new facts, loads `summary.md` and active `items.json`, rewrites `summary.md` for the current state, and marks contradicted facts as superseded.

### ATOM-SOURCE-20260127-004-0023
**Lines**: 252-253
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To maintain a Clawdbot's memory, rewrite `summary.md` weekly based on active facts and supersede old facts instead of deleting them.

### ATOM-SOURCE-20260127-004-0024
**Lines**: 260-265
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> On each heartbeat, a Clawbot should check for new conversations, spawn a sub-agent to extract durable facts, write them to relevant `items.json` files, and track the `lastExtractedTimestamp`.

### ATOM-SOURCE-20260127-004-0025
**Lines**: 267-268
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Fact extraction for a Clawbot should focus on relationships, status changes, and milestones, while skipping casual chat and temporary information.

### ATOM-SOURCE-20260127-004-0026
**Lines**: 275-279
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> For weekly memory review, a Clawbot should load `summary.md` and `active items.json` for each entity with new facts, rewrite `summary.md` for the current state, and mark contradicted facts as superseded.

### ATOM-SOURCE-20260127-004-0031
**Lines**: 307-308
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To set up the Three-Layer Memory System, copy this article into your Clawbot and instruct it to implement the system.
