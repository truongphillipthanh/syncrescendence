# Extraction: SOURCE-20260218-010

**Source**: `SOURCE-20260218-x-article-ksimback-give_your_openclaw_the_memory_it_needs_full_guide.md`
**Atoms extracted**: 23
**Categories**: analogy, claim, concept, framework, praxis_hook

---

## Analogy (3)

### ATOM-SOURCE-20260218-010-0005
**Lines**: 42-42
**Context**: anecdote / evidence
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.60

> OpenClaw's memory saving mechanism, where the LLM decides what to save, is like an employee who decides on their own which meeting notes to keep and which to throw away.

### ATOM-SOURCE-20260218-010-0007
**Lines**: 50-51
**Context**: anecdote / evidence
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.60

> OpenClaw's memory retrieval issue, where an agent answers from its context window instead of searching saved memory, is like an employee who saved a document but answers from memory instead of checking the actual document when asked.

### ATOM-SOURCE-20260218-010-0010
**Lines**: 61-62
**Context**: anecdote / evidence
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.60

> OpenClaw's context compaction, which removes older messages to make room, is like an employee with a stack of papers who throws out the oldest ones without saving important information when the stack gets too tall.

## Claim (9)

### ATOM-SOURCE-20260218-010-0001
**Lines**: 15-17
**Context**: anecdote / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.70

> OpenClaw agents frequently forget basic information, lose critical project context mid-conversation, and fail to recall decisions made shortly before.

### ATOM-SOURCE-20260218-010-0002
**Lines**: 25-27
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> OpenClaw treats memory as a suggestion, not a requirement, allowing the agent to decide what to save, when to search, and what to recall, leading to forgetting by default without explicit configuration.

### ATOM-SOURCE-20260218-010-0004
**Lines**: 34-36
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> In OpenClaw, the LLM decides whether information is worth saving to disk, meaning important context can be lost if the model deems it not worth storing.

### ATOM-SOURCE-20260218-010-0006
**Lines**: 45-48
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> Even when facts are saved to disk in OpenClaw, recall is not guaranteed because the agent must decide to use the `memory_search` tool, often answering from its current context window instead.

### ATOM-SOURCE-20260218-010-0008
**Lines**: 54-56
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> OpenClaw compacts context to avoid token limits, summarizing or removing older messages, which destroys any information that only existed in the active conversation and was not yet saved to disk.

### ATOM-SOURCE-20260218-010-0009
**Lines**: 57-59
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> Even content in MEMORY.md can be summarized away during a long session due to context compaction, causing the agent to forget mid-conversation.

### ATOM-SOURCE-20260218-010-0016
**Lines**: 97-99
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> QMD's killer feature is its ability to index external document collections like Obsidian vaults, project documentation, and Notion exports, making them searchable via memory_search.

### ATOM-SOURCE-20260218-010-0019
**Lines**: 109-110
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.70

> Mem0's auto-capture and auto-recall mechanisms completely solve memory failure modes related to automatic capture and compaction.

### ATOM-SOURCE-20260218-010-0021
**Lines**: 118-120
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.50, epistemic_stability=0.60

> Cognee is suitable for scenarios requiring deep understanding of relationships and structured knowledge, such as enterprise settings or multi-agent teams, but might be overkill for basic OpenClaw setups.

## Concept (2)

### ATOM-SOURCE-20260218-010-0017
**Lines**: 102-104
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> Mem0 is a memory layer for AI applications that stores memories outside the context window, preventing compaction from destroying them.

### ATOM-SOURCE-20260218-010-0020
**Lines**: 114-117
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> Cognee builds a knowledge graph from data, ingesting OpenClaw's memory files to construct a graph of entities and relationships, which allows for structured representation of concepts and their connections.

## Framework (2)

### ATOM-SOURCE-20260218-010-0003
**Lines**: 29-30
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.70

> There are three common failure modes for memory in OpenClaw: memory is never saved, memory is saved but never retrieved, and context compaction destroys knowledge.

### ATOM-SOURCE-20260218-010-0018
**Lines**: 105-108
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> Mem0 operates with two processes per turn: Auto-Capture, which detects and stores information without LLM judgment, and Auto-Recall, which searches and injects relevant memories before the agent responds.

## Praxis Hook (7)

### ATOM-SOURCE-20260218-010-0011
**Lines**: 65-67
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> To fix OpenClaw memory issues, configure memory flush, context pruning, hybrid search, and session indexing before resorting to external plugins or databases.

### ATOM-SOURCE-20260218-010-0012
**Lines**: 70-81
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Enable memory flush in OpenClaw's compaction settings by setting `enabled: true` and customizing the prompt to specifically capture decisions, state changes, lessons, and blockers, while also raising `softThresholdTokens` to 40000.

### ATOM-SOURCE-20260218-010-0013
**Lines**: 83-89
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Configure context pruning in OpenClaw using `cache-ttl` mode with a `ttl` of '6h' and `keepLastAssistants` set to 3 to retain recent messages and prevent their removal during compaction.

### ATOM-SOURCE-20260218-010-0014
**Lines**: 91-98
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Enable hybrid search in OpenClaw's `memorySearch` configuration by setting `hybrid.enabled: true` and adjusting `vectorWeight` (e.g., 0.7) and `textWeight` (e.g., 0.3) to combine vector similarity and BM25 keyword search for improved retrieval accuracy.

### ATOM-SOURCE-20260218-010-0015
**Lines**: 93-96
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To get started with QMD, have your agent review the QMD Github repository and discuss it before implementation, then install it. Always back up your system before installing new memory systems.

### ATOM-SOURCE-20260218-010-0022
**Lines**: 125-128
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> One way to integrate Obsidian with OpenClaw is to symlink your agent's memory folder to your Obsidian vault, allowing daily notes to appear in Obsidian for review, editing, and annotation across devices.

### ATOM-SOURCE-20260218-010-0023
**Lines**: 130-133
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Another robust approach for Obsidian integration is to index your vault via QMD, making all captured Obsidian content searchable by agents, which also saves token costs as Obsidian 1.12's CLI allows querying metadata instead of reading entire files.
