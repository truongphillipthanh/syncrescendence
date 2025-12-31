---
id: CANON-30430
name: Memory Systems
identity: MEMORY_SYSTEMS
tier: CANON
type: asteroid
chain: INTELLIGENCE
parent: CANON-30400
version: 1.0.0
status: canonical
created: 2025-12-30
updated: 2025-12-30
synopsis: Agent memory architectures, taxonomies, vector databases, context engineering, and production memory systems.
---

# CANON-30430: MEMORY SYSTEMS
## Intelligence Chain Asteroid

**Parent**: CANON-30400 (Agentic Architecture)

---

## PURPOSE

This asteroid provides detailed specifications for memory systems powering autonomous agents. Where CANON-30400 surveys memory types, this document provides implementation depth for memory architectures, vector databases, and context engineering.

---

## PART I: MEMORY TAXONOMY

### 1.1 Fundamental Memory Types

An agent's intelligence is fundamentally constrained by its ability to remember and learn. State-of-the-art agents employ multi-layered memory architecture managing information across different timescales and abstraction levels.

```yaml
Memory_Taxonomy:
  Working_Memory:
    function: Immediate task context
    characteristics:
      - Fast volatile store
      - Rapid access
      - Limited capacity
    implementation: Context window, in-memory structures
    analogy: Human working memory, LLM prompt window

  Episodic_Memory:
    function: Chronological record of experiences
    characteristics:
      - Event sequences
      - Actions and outcomes
      - Session transcripts
    implementation: Event logs, vector stores
    use: Case-based reasoning, learning from trial and error

  Semantic_Memory:
    function: Factual knowledge repository
    characteristics:
      - General facts
      - Concepts and relationships
      - Domain knowledge
    implementation: Knowledge graphs, RAG systems
    analogy: Internal encyclopedia

  Procedural_Memory:
    function: Learned skills and workflows
    characteristics:
      - Multi-step action sequences
      - Automated execution patterns
      - Tool usage knowledge
    implementation: Tool definitions, workflow templates
    benefit: Execute without reasoning from first principles

  Prospective_Memory:
    function: Future intentions and schedules
    characteristics:
      - Planned actions
      - Scheduled tasks
      - To-do queues
    implementation: Planning state, task queues
    purpose: Remember to do something in the future
```

### 1.2 Memory Interaction Patterns

```
┌─────────────────────────────────────────────────────────────┐
│                    PROSPECTIVE MEMORY                        │
│              Future intentions, scheduled actions            │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                      WORKING MEMORY                          │
│              Active context, current task state              │
└────────────────────────────┬────────────────────────────────┘
                             │
           ┌─────────────────┼─────────────────┐
           ▼                 ▼                 ▼
┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐
│  EPISODIC MEMORY │ │  SEMANTIC MEMORY │ │ PROCEDURAL MEMORY │
│  Past experiences │ │ Facts & concepts │ │ Skills & workflows │
└──────────────────┘ └──────────────────┘ └──────────────────┘
```

---

## PART II: ARCHITECTURAL INNOVATIONS

### 2.1 A-MEM (Agentic Memory)

**NeurIPS 2025 acceptance** — Most significant memory innovation of 2025.

```yaml
A_MEM:
  inspiration: Zettelkasten personal knowledge management

  paradigm_shift:
    from: Passive memory consumer
    to: Active knowledge curator

  mechanism:
    note_structure:
      - Contextual descriptions
      - Keywords and tags
      - Vector embeddings (all-MiniLM-L6-v2)

    dynamic_indexing:
      - New memories trigger existing memory updates
      - Semantic similarity creates interconnected networks
      - Attributes evolve based on new information

    linking:
      - Agent analyzes historical memories
      - Establishes meaningful connections
      - Memory network self-organizes

  results:
    - Superior improvements across 6 foundation models
    - Outperforms state-of-the-art baselines
    - No fixed schemas or manual annotation required
```

### 2.2 MIRIX (Multi-Agent Memory System)

```yaml
MIRIX:
  architecture: Six-tier memory taxonomy

  tiers:
    1_Core: Persistent user and task information (personality, goals)
    2_Episodic: Specific events and experiences
    3_Semantic: General knowledge and facts
    4_Procedural: Learned skills and routines
    5_Resource: External data sources and integrations
    6_Knowledge_Vaults: Long-term information storage

  benchmarks:
    ScreenshotVQA: 35% higher accuracy than RAG
    Storage: 99.9% reduction
    LOCOMO: 85.4% state-of-the-art performance

  capability: Real-time screen monitoring with personalized memory
```

### 2.3 MemGPT (Letta)

```yaml
MemGPT:
  inspiration: Operating system memory hierarchy

  architecture:
    core_memory: RAM-equivalent, in-context
    conversational_memory: Recent history buffer
    archival_memory: Long-term storage with retrieval
    external_files: Disk-like persistence

  mechanism:
    - Agents manage memory through function calls
    - Autonomous tier management
    - Data moves between tiers as needed
    - Creates illusion of unlimited memory within fixed context

  LoCoMo_benchmark: 74% accuracy with filesystem approach

  principle: "Memory is context engineering"
```

---

## PART III: VECTOR DATABASES

### 3.1 Role in Agent Memory

Vector databases became cornerstone technology for long-term episodic and semantic memory.

```yaml
Vector_Database_Function:
  storage: High-dimensional numerical vectors (embeddings)
  capture: Semantic meaning of text, images, data
  retrieval: Nearest-neighbor search in vector space
  advantage: Conceptual similarity vs. keyword matching
```

### 3.2 Production Solutions

| Database | Adoption | Characteristics |
|----------|----------|-----------------|
| **Redis** | 43% | Fast, versatile, production-proven |
| **ChromaDB** | 20% | Open-source, developer-friendly |
| **pgvector** | 18% | PostgreSQL extension, SQL integration |
| **Pinecone** | Enterprise | Managed, scalable |
| **Milvus** | Enterprise | Open-source, distributed |
| **Weaviate** | Enterprise | GraphQL, modular vectorizer |

### 3.3 Memory Platform Ecosystem

| Platform | Architecture | Focus |
|----------|--------------|-------|
| **Mem0** | Hybrid (vector + graph + KV) | Personalization, adaptation |
| **Zep** | Long-term + session management | Graph-based organization |
| **LangMem** | LangChain ecosystem | Modular memory types |
| **Memary** | Knowledge graph-based | Entity relationships, temporal evolution |

---

## PART IV: CONTEXT ENGINEERING

### 4.1 The Critical Principle

> **Memory is context engineering**—what enters the context window determines agent capabilities more than raw storage capacity.

### 4.2 Context Window Evolution

```yaml
Context_Window_2025:
  Claude_3.5: 200K+ tokens
  Gemini_1.5: 200K+ tokens

  implication:
    - Reduced retrieval frequency
    - But: Indiscriminate stuffing degrades quality
    - Larger windows don't eliminate need for intelligent management
```

### 4.3 Context Engineering Strategies

```yaml
Optimization_Techniques:
  Semantic_Chunking:
    - Divide content by meaning, not arbitrary length
    - Preserve contextual coherence
    - Enable relevant retrieval

  Relevance_Scoring:
    - Score content by task relevance
    - Prioritize high-relevance in context
    - Deprioritize or exclude low-relevance

  Temporal_Decay:
    - Recent information weighted higher
    - Older information decays unless reinforced
    - Prevents context pollution from stale data

  Hierarchical_Summarization:
    - Compress older content into summaries
    - Retain detail for recent/relevant
    - Balance coverage with specificity
```

### 4.4 Sleep-Time Compute

```yaml
Sleep_Time_Compute:
  concept: Asynchronous memory management during idle periods

  operations:
    - Memory reorganization
    - Index optimization
    - Stale data pruning
    - Relationship discovery

  benefit: Management without blocking agent operations
```

---

## PART V: MEMORY COMPONENT ARCHITECTURE

### 5.1 Layered Memory Structure

```yaml
Memory_Layers:
  Layer_1_Message_Buffer:
    function: Recent conversational history
    implementation: Rolling window of messages
    access: Immediate, in working memory

  Layer_2_Core_Memory:
    function: Persistent facts and preferences
    implementation: Key-value store
    update: Explicit through function calls

  Layer_3_External_Database:
    function: Retrievable knowledge
    implementation: Vector store + knowledge graph
    access: Semantic search
```

### 5.2 Retrieval Optimization

```yaml
Retrieval_Strategies:
  ANN_Indexing:
    technique: Approximate Nearest Neighbor
    benefit: Sub-linear search complexity
    tradeoff: Slight accuracy loss for speed

  Hybrid_Search:
    technique: Combine semantic + keyword
    benefit: Precision of keywords + coverage of semantics
    implementation: BM25 + vector similarity fusion

  Reranking:
    technique: LLM-based result reranking
    benefit: Context-aware relevance assessment
    cost: Additional inference latency
```

---

## PART VI: MEMORY INTERFACES

### 6.1 Standard Memory Operations

```yaml
Memory_Interface:
  write:
    parameters: content, type, metadata
    function: Store new information
    triggers: Indexing, linking to existing memories

  read:
    parameters: query, type, top_k
    function: Retrieve relevant information
    returns: Ranked list of memory items

  update:
    parameters: id, delta
    function: Modify existing memory
    triggers: Re-indexing, propagation to linked items

  forget:
    parameters: criteria
    function: Remove or deprecate memories
    use: Privacy, relevance maintenance
```

### 6.2 Memory-Aware Planning

```yaml
Memory_Integrated_Planning:
  before_action:
    - Query episodic: "Have I done this before?"
    - Query semantic: "What facts are relevant?"
    - Query procedural: "What's the known approach?"

  during_action:
    - Update working memory with intermediate state
    - Log to episodic for future reference

  after_action:
    - Extract learnings to semantic memory
    - Update procedural if new skill acquired
    - Schedule follow-ups in prospective memory
```

---

## PART VII: CONSISTENCY AND COHERENCE

### 7.1 Memory Consistency Challenges

```yaml
Consistency_Issues:
  contradiction:
    problem: New information contradicts stored memory
    resolution: Version tracking, recency weighting, explicit conflict resolution

  staleness:
    problem: Stored information becomes outdated
    resolution: TTL mechanisms, periodic refresh, source re-verification

  fragmentation:
    problem: Related information scattered across memories
    resolution: Linking mechanisms, periodic consolidation

  hallucination_propagation:
    problem: Incorrect information persists and propagates
    resolution: Confidence scoring, source attribution, verification gates
```

### 7.2 Cross-Session Continuity

```yaml
Session_Continuity:
  challenge: Maintaining coherent identity across sessions

  solutions:
    persistent_core:
      - User preferences
      - Relationship history
      - Learned patterns

    session_bridging:
      - Session start: Load relevant context
      - Session end: Summarize and persist key information

    identity_preservation:
      - Consistent behavioral patterns
      - Accumulated knowledge retention
      - Relationship continuity
```

---

## PART VIII: PRODUCTION CONSIDERATIONS

### 8.1 Performance Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Retrieval latency | <100ms | P95 search time |
| Storage efficiency | High compression | Bytes per memory item |
| Relevance precision | >80% | Retrieved item usefulness |
| Context utilization | >60% | Useful tokens / total tokens |

### 8.2 Scalability Patterns

```yaml
Scaling_Strategies:
  horizontal:
    - Shard memory by user/session
    - Distribute index across nodes
    - Load balance retrieval queries

  hierarchical:
    - Hot tier: Frequent access, fast storage
    - Warm tier: Periodic access, balanced storage
    - Cold tier: Rare access, compressed storage

  pruning:
    - Age-based expiration
    - Access-frequency thresholds
    - Relevance score minimums
```

### 8.3 Security Considerations

```yaml
Memory_Security:
  access_control:
    - Agent-specific memory isolation
    - User data segregation
    - Capability-based memory access

  data_protection:
    - Encryption at rest
    - Encryption in transit
    - PII detection and handling

  audit:
    - Memory access logging
    - Modification tracking
    - Compliance reporting
```

---

## PART IX: TOOL OVERLOAD INSIGHT

Research demonstrates diminishing returns beyond 8-10 tools in single-agent configurations due to context window constraints and selection complexity.

**Solution**: Multi-agent architectures where specialized agents each access focused tool subsets rather than monolithic agents attempting to master dozens of capabilities.

---

## SATELLITES

None. This is a leaf asteroid.

---

## VERSION HISTORY

**Version 1.0.0** (December 2025): Genesis establishment
- Canonized from Technology Lunar - Agents.md
- Memory taxonomies and architectures documented
- Context engineering principles established
