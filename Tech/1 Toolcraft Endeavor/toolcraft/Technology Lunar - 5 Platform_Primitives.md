# Platform Primitives: Feature Catalog and Composition Patterns

## I. Primitive Catalog Structure

### Purpose

The primitive catalog is not a comprehensive database of every possible feature—it's an operational tool for primitive-level thinking and bespoke composition. Catalog entries exist to enable decisions: which primitives to extract, how to combine them, when to build vs. buy.

### Catalog Philosophy

**Apps are transitional, primitives are eternal**: Tools come and go, but the fundamental capabilities they embody persist. Extract and catalog what endures.

**Observation over prescription**: The catalog grows through discovery, not exhaustive documentation. Add primitives when encountered, not speculatively.

**Quality over quantity**: 50 well-documented, frequently-reused primitives beat 500 cataloged-once-never-referenced entries.

**Composition is the goal**: Primitives exist to be combined. Catalog not just features, but how they compose.

### Entry Template

```markdown
# Primitive: [Descriptive Name]

## Classification
- **Category**: Memory | Orchestration | Communication | Context | Interface | Governance
- **Object Type**: O.FN | O.SVC | O.WF | O.AGT | O.DP | O.MOD | O.STM | O.ARC | O.SRF | O.SNS | O.ACT | O.INS | O.GRD | O.EVL | O.CPL | O.POL
- **Work Modes**: Creation | Transformation | Comprehension | Extraction
- **Platform**: Desktop | Mobile | XR | Ambient | CLI | Universal

## Description
[One-sentence essence of what this primitive does]

## Capability Contract
**Input requirements**: [What does it need to function?]
**Output guarantees**: [What does it reliably produce?]
**Performance characteristics**: [Latency, throughput, resource usage]
**Failure modes**: [How does it break? What are edge cases?]

## Composition Patterns
**Combines well with**: [Other primitives that enhance this one]
**Prerequisites**: [Primitives this depends on]
**Enables**: [What becomes possible with this primitive]
**Example compositions**: [Concrete combinations in use]

## Platform-Specific Notes
**Desktop**: [Optimizations, constraints, variations]
**Mobile**: [Adaptations needed, limitations]
**XR**: [Spatial considerations, gesture mappings]
**Ambient**: [Automation potential, background operation]
**CLI**: [Command patterns, scriptability]

## Extraction Source
**Tool(s)**: [Where this primitive was identified]
**Extraction difficulty**: Low | Medium | High
**Reuse validation**: [Has this been successfully reused? Where?]

## Metadata
- **Added**: [Date]
- **Last used**: [Date]
- **Reuse count**: [Number]
- **Quality score**: [1-5]
- **Maturity**: Experimental | Validated | Production | Deprecated
```

---

## II. Memory Primitive Catalog

### Tier 1: Working Memory Primitives

**Primitive: Conversation History Buffer**
- **Category**: Memory | **Object**: O.STM | **Platform**: Universal
- **Description**: Maintains recent conversation turns in active context window
- **Capability Contract**:
  - Input: Message exchanges (user + assistant)
  - Output: Chronological history up to context limit
  - Performance: <10ms access, limited capacity (context window)
  - Failure: Truncation when exceeding window, loss on session end
- **Composition**: Pairs with semantic memory for overflow, procedural memory for common patterns
- **Maturity**: Production

**Primitive: Context Window Management**
- **Category**: Memory | **Object**: O.FN | **Platform**: Universal
- **Description**: Intelligently allocate finite context budget across competing needs
- **Capability Contract**:
  - Input: Multiple context sources (memory, docs, examples) + priority weights
  - Output: Optimized context assembly fitting window
  - Performance: 50-200ms for assembly, depends on source count
  - Failure: Suboptimal selection if priorities miscalibrated
- **Composition**: Combines with all memory tiers, RAG systems, prompt caching
- **Maturity**: Production

### Tier 2: Episodic Memory Primitives

**Primitive: Interaction Logging**
- **Category**: Memory | **Object**: O.DP | **Platform**: Universal
- **Description**: Structured storage of past interactions with metadata
- **Capability Contract**:
  - Input: Interaction (user input, agent output, context, timestamp)
  - Output: Durable log entry with metadata (session ID, tags, outcome)
  - Performance: <50ms write, 100-500ms retrieval
  - Failure: Storage limits, corruption risk without backups
- **Composition**: Enables episodic retrieval, pattern mining, experience replay
- **Maturity**: Production

**Primitive: Temporal Retrieval**
- **Category**: Memory | **Object**: O.FN | **Platform**: Universal
- **Description**: Retrieve memories by time window or sequence
- **Capability Contract**:
  - Input: Time range or relative position (last 5 interactions, yesterday, etc.)
  - Output: Ordered set of matching episodes
  - Performance: 100-300ms for typical queries
  - Failure: Slow for large logs without indexing
- **Composition**: Combines with semantic retrieval for multi-criteria search
- **Maturity**: Production

### Tier 3: Semantic Memory Primitives

**Primitive: Vector Similarity Search**
- **Category**: Memory | **Object**: O.FN + O.SVC | **Platform**: Universal
- **Description**: Retrieve semantically similar content via embedding comparison
- **Capability Contract**:
  - Input: Query text or embedding vector
  - Output: Top-K most similar items with similarity scores
  - Performance: 50-200ms for millions of vectors (with proper indexing)
  - Failure: Quality depends on embedding model, can miss lexical matches
- **Composition**: Core RAG primitive, combines with keyword search (hybrid retrieval)
- **Source**: Pinecone, Weaviate, pgvector
- **Maturity**: Production

**Primitive: Knowledge Graph Traversal**
- **Category**: Memory | **Object**: O.FN + O.DP | **Platform**: Universal
- **Description**: Navigate entity relationships for connected knowledge
- **Capability Contract**:
  - Input: Starting entity + relationship types + depth limit
  - Output: Connected entities with relationship paths
  - Performance: 100-500ms depending on graph size and depth
  - Failure: Exponential complexity with depth, requires graph structure
- **Composition**: Enables GraphRAG, multi-hop reasoning, entity-centric retrieval
- **Source**: Neo4j, knowledge graphs
- **Maturity**: Production

**Primitive: Fact Extraction**
- **Category**: Memory | **Object**: O.FN + O.MOD | **Platform**: Universal
- **Description**: Distill factual knowledge from conversations/documents
- **Capability Contract**:
  - Input: Text content (conversation, document)
  - Output: Structured facts with confidence scores
  - Performance: 1-5 seconds depending on content length
  - Failure: Hallucination risk, requires validation
- **Composition**: Populates semantic memory from episodic, enables knowledge accumulation
- **Maturity**: Validated

### Tier 4: Procedural Memory Primitives

**Primitive: Workflow Caching**
- **Category**: Memory | **Object**: O.FN + O.DP | **Platform**: Universal
- **Description**: Store and retrieve frequently-used workflows for direct execution
- **Capability Contract**:
  - Input: Workflow specification (steps, parameters, success criteria)
  - Output: Cached workflow ready for execution
  - Performance: <10ms retrieval, instant execution without reasoning
  - Failure: Staleness if underlying tools change
- **Composition**: Enables procedural skill learning, reduces reasoning overhead
- **Maturity**: Validated

**Primitive: Pattern Mining**
- **Category**: Memory | **Object**: O.FN + O.EVL | **Platform**: Universal
- **Description**: Detect high-frequency action sequences from episodic memory
- **Capability Contract**:
  - Input: Episodic log, frequency threshold, stability criteria
  - Output: Candidate procedures with usage statistics
  - Performance: Minutes for full log analysis (offline process)
  - Failure: False positives if threshold too low, misses if too high
- **Composition**: Feeds workflow caching, enables apparatus recognition
- **Maturity**: Validated

### Tier 5: Memory Management Primitives

**Primitive: Summarization Trigger**
- **Category**: Memory | **Object**: O.FN + O.WF | **Platform**: Universal
- **Description**: Periodically condense detailed memories into compressed summaries
- **Capability Contract**:
  - Input: Old memories below recency threshold
  - Output: Compressed summaries preserving key information
  - Performance: 2-10 seconds per batch
  - Failure: Information loss inevitable, tuning preserves essential details
- **Composition**: Enables long-term memory without unbounded growth
- **Maturity**: Production

**Primitive: Sleep-Time Reorganization**
- **Category**: Memory | **Object**: O.WF | **Platform**: Universal
- **Description**: Background memory optimization during idle periods
- **Capability Contract**:
  - Input: Idle signal + full memory state
  - Output: Reorganized memory with updated indices, pruned low-value entries
  - Performance: Minutes to hours (async, non-blocking)
  - Failure: None (runs in background, doesn't block active use)
- **Composition**: Maintains memory quality, improves retrieval performance
- **Maturity**: Validated

---

## III. Orchestration Primitive Catalog

### Coordination Pattern Primitives

**Primitive: Sequential Handoff**
- **Category**: Orchestration | **Object**: O.WF | **Platform**: Universal
- **Description**: Linear agent coordination with explicit state transfer
- **Capability Contract**:
  - Input: Ordered list of agents + initial state
  - Output: Final result after sequential processing
  - Performance: Sum of agent latencies (no parallelism)
  - Failure: Early failure aborts pipeline unless recovery logic added
- **Composition**: Default pattern, simplest orchestration, enables audit trail
- **Maturity**: Production

**Primitive: Parallel Dispatch**
- **Category**: Orchestration | **Object**: O.WF | **Platform**: Desktop, Cloud
- **Description**: Concurrent execution of independent subtasks
- **Capability Contract**:
  - Input: List of independent tasks + aggregation function
  - Output: Aggregated results from parallel execution
  - Performance: Max latency = slowest agent (vs. sum for sequential)
  - Failure: One slow/failed task can delay all, needs timeout handling
- **Composition**: Fastest for independent work, requires aggregation primitive
- **Production validation**: 45% faster than sequential
- **Maturity**: Production

**Primitive: Critic-Refiner Loop**
- **Category**: Orchestration | **Object**: O.WF + O.AGT | **Platform**: Universal
- **Description**: Iterative improvement through feedback cycles
- **Capability Contract**:
  - Input: Actor agent + Critic agent + quality threshold + max iterations
  - Output: Refined output meeting quality criteria (or best effort)
  - Performance: 2-5x base latency (depends on iterations)
  - Failure: May not converge, limit iterations to prevent infinite loop
- **Composition**: Dramatically improves quality, combines with any generation task
- **Production validation**: 30-40% quality improvement
- **Maturity**: Production

**Primitive: Specialist Routing**
- **Category**: Orchestration | **Object**: O.AGT + O.FN | **Platform**: Universal
- **Description**: Dynamic selection of specialist agent based on task characteristics
- **Capability Contract**:
  - Input: Task + routing logic + specialist pool
  - Output: Selected specialist + routing confidence
  - Performance: 50-200ms routing decision
  - Failure: Poor routing if task characteristics misclassified
- **Composition**: Enables magnetic orchestration, adaptive workflows
- **Maturity**: Production

### Topology Primitives

**Primitive: Hub-and-Spoke Coordinator**
- **Category**: Orchestration | **Object**: O.AGT | **Platform**: Universal
- **Description**: Central orchestrator managing all agent interactions
- **Capability Contract**:
  - Input: Orchestrator logic + specialist agents
  - Output: Coordinated execution with centralized oversight
  - Performance: Orchestrator is bottleneck but provides oversight
  - Failure: Single point of failure without failover
- **Composition**: Mission-critical systems, clear authority, easy monitoring
- **Maturity**: Production

**Primitive: Mesh Communication**
- **Category**: Orchestration | **Object**: O.SVC | **Platform**: Desktop, Cloud
- **Description**: Peer-to-peer agent communication without central authority
- **Capability Contract**:
  - Input: Agents with peer communication capability
  - Output: Decentralized coordination
  - Performance: No single bottleneck, distributed load
  - Failure: Complex coordination, potential conflicts without consensus
- **Composition**: High-scale systems, fault-tolerant architectures
- **Maturity**: Validated

### Sub-Pattern Primitives

**Primitive: Plan-Execute Split**
- **Category**: Orchestration | **Object**: O.AGT | **Platform**: Universal
- **Description**: Separate planning agent from execution agents
- **Capability Contract**:
  - Input: High-level goal
  - Output: Plan (from planner) → Execution (from executors)
  - Performance: Plan latency + execution latency
  - Failure: Plan quality determines success, replanning if execution fails
- **Composition**: Clean separation of strategy vs. tactics
- **Maturity**: Production

---

## IV. Communication Primitive Catalog

### Protocol Primitives

**Primitive: Model Context Protocol (MCP)**
- **Category**: Communication | **Object**: O.SVC | **Platform**: Universal
- **Description**: Universal standard for agent-to-tool communication
- **Capability Contract**:
  - Input: Tool discovery request or invocation
  - Output: Tool descriptions or execution results
  - Performance: Protocol overhead minimal (<50ms)
  - Failure: Tool-specific failures, not protocol failures
- **Composition**: Enables portable agent-tool integration
- **Adoption**: Universal (OpenAI, Anthropic, Google, Microsoft)
- **Maturity**: Production

**Primitive: Agent-to-Agent Protocol (A2A)**
- **Category**: Communication | **Object**: O.SVC | **Platform**: Universal
- **Description**: Standardized peer agent communication
- **Capability Contract**:
  - Input: Agent messages with typed envelopes
  - Output: Structured responses with conversation context
  - Performance: Minimal overhead, depends on transport
  - Failure: Requires both agents support protocol
- **Composition**: Enables mesh topologies, peer collaboration
- **Adoption**: Emerging (150+ organizations)
- **Maturity**: Validated

**Primitive: Structured Message Envelope**
- **Category**: Communication | **Object**: O.FN | **Platform**: Universal
- **Description**: Typed message format with metadata
- **Capability Contract**:
  - Input: Content + type + metadata
  - Output: Structured envelope for transmission
  - Performance: <10ms serialization
  - Failure: Schema mismatches if not validated
- **Composition**: Foundation for A2A, enables type safety
- **Maturity**: Production

### Coordination Primitives

**Primitive: Task Lifecycle Management**
- **Category**: Communication | **Object**: O.WF | **Platform**: Universal
- **Description**: State machine for task coordination
- **Capability Contract**:
  - Input: Task state transitions (proposed, accepted, in-progress, completed, failed)
  - Output: Current state + transition history
  - Performance: <50ms state updates
  - Failure: Deadlock if coordination logic flawed
- **Composition**: Enables reliable handoffs, audit trails
- **Maturity**: Production

**Primitive: Conversation Protocol**
- **Category**: Communication | **Object**: O.WF | **Platform**: Universal
- **Description**: Multi-turn interaction patterns between agents
- **Capability Contract**:
  - Input: Conversation rules (turn-taking, context preservation)
  - Output: Coordinated dialogue
  - Performance: Minimal overhead per turn
  - Failure: Confusion if context lost, infinite loops without termination
- **Composition**: Enables group chat, negotiation, collaborative problem-solving
- **Maturity**: Validated

---

## V. Context Engineering Primitive Catalog

### Retrieval Primitives

**Primitive: Hybrid Search**
- **Category**: Context | **Object**: O.WF + O.FN | **Platform**: Universal
- **Description**: Combined vector similarity + keyword + metadata filtering
- **Capability Contract**:
  - Input: Query + search strategies + weights
  - Output: Merged, deduplicated, reranked results
  - Performance: 200-500ms (parallel searches + merge)
  - Failure: Complexity increases tuning difficulty
- **Composition**: Production RAG primitive, significantly improves accuracy
- **Production validation**: 49% reduction in retrieval misses vs. vector-only
- **Maturity**: Production

**Primitive: Query Transformation**
- **Category**: Context | **Object**: O.FN + O.AGT | **Platform**: Universal
- **Description**: Optimize search queries based on initial results
- **Capability Contract**:
  - Input: Original query + initial results + gaps identified
  - Output: Refined query likely to retrieve missing information
  - Performance: 1-3 seconds (agent reasoning)
  - Failure: May not improve if problem is corpus, not query
- **Composition**: Enables agentic RAG, iterative refinement
- **Maturity**: Validated

**Primitive: Reranking Model**
- **Category**: Context | **Object**: O.MOD + O.FN | **Platform**: Universal
- **Description**: Score retrieved documents by relevance to query
- **Capability Contract**:
  - Input: Query + candidate documents (10-100)
  - Output: Reranked list by relevance
  - Performance: 100-300ms for reranking
  - Failure: Adds latency, quality depends on reranker model
- **Composition**: Improves precision after recall, part of hybrid search
- **Maturity**: Production

### Assembly Primitives

**Primitive: Hierarchical Summarization**
- **Category**: Context | **Object**: O.FN + O.WF | **Platform**: Universal
- **Description**: Multi-level document compression (sections → summaries → gist)
- **Capability Contract**:
  - Input: Long document exceeding context window
  - Output: Compressed representation fitting window
  - Performance: 10-60 seconds depending on length
  - Failure: Information loss proportional to compression ratio
- **Composition**: Enables processing arbitrarily long documents
- **Maturity**: Production

**Primitive: Sliding Window Processing**
- **Category**: Context | **Object**: O.FN | **Platform**: Universal
- **Description**: Process long content in overlapping segments
- **Capability Contract**:
  - Input: Document + window size + overlap size
  - Output: Processed chunks with maintained continuity
  - Performance: Linear in document length
  - Failure: Seam artifacts if overlap insufficient
- **Composition**: Alternative to summarization, preserves detail
- **Maturity**: Production

**Primitive: Context Prioritization**
- **Category**: Context | **Object**: O.FN | **Platform**: Universal
- **Description**: Rank context sources by relevance for inclusion
- **Capability Contract**:
  - Input: Context sources + relevance scoring function + token budget
  - Output: Prioritized subset fitting budget
  - Performance: 50-200ms for scoring
  - Failure: Suboptimal if scoring function miscalibrated
- **Composition**: Combines with all context assembly strategies
- **Maturity**: Production

### Caching Primitives

**Primitive: Prompt Caching**
- **Category**: Context | **Object**: O.SVC | **Platform**: Universal (Anthropic, OpenAI, Google)
- **Description**: Reuse static context portions across requests
- **Capability Contract**:
  - Input: Cacheable content + TTL specification
  - Output: 90% cost reduction on cache hits, 10-85% latency reduction
  - Performance: Cache write 1.25x-2x cost, cache read 0.1x cost
  - Failure: Cache miss incurs full cost
- **Composition**: Foundational cost optimization, combines with all workflows
- **Production validation**: 40-90% cost reduction in production
- **Maturity**: Production

**Primitive: Embedding Cache**
- **Category**: Context | **Object**: O.DP + O.MOD | **Platform**: Universal
- **Description**: Store pre-computed embeddings for documents
- **Capability Contract**:
  - Input: Document content
  - Output: Cached embedding (or compute + cache if miss)
  - Performance: <10ms for cache hit, 100-500ms for miss
  - Failure: Staleness if document updated
- **Composition**: Accelerates vector search, reduces embedding costs
- **Maturity**: Production

### Optimization Primitives

**Primitive: Context Pruning**
- **Category**: Context | **Object**: O.FN + O.EVL | **Platform**: Universal
- **Description**: Remove outdated or contradictory information
- **Capability Contract**:
  - Input: Current context + pruning rules (temporal decay, contradiction detection)
  - Output: Cleaned context with stale/conflicting info removed
  - Performance: 100-500ms depending on context size
  - Failure: May remove valuable information if rules too aggressive
- **Composition**: Maintains context quality in long interactions
- **Production validation**: 54% improvement in specialized agent benchmarks
- **Maturity**: Production

**Primitive: Context Offloading**
- **Category**: Context | **Object**: O.WF | **Platform**: Desktop, Cloud
- **Description**: Process heavy analysis off-thread, return summaries only
- **Capability Contract**:
  - Input: Large data + processing function + summary specification
  - Output: Summary (not full processing results)
  - Performance: Processing time + summarization time
  - Failure: Summary quality determines value
- **Composition**: Keeps main thread clean, enables large-scale processing
- **Production validation**: 8x cleaner signal (76% vs. 9% when inline)
- **Maturity**: Production

---

## VI. Interface Primitive Catalog

### Navigation Primitives

**Primitive: Command Palette**
- **Category**: Interface | **Object**: O.SRF | **Platform**: Desktop, CLI
- **Description**: Text-driven search for commands/functions
- **Capability Contract**:
  - Input: Text query (fuzzy matching)
  - Output: Ranked list of matching commands
  - Performance: <50ms for search, instant execution
  - Failure: Discoverability depends on search quality
- **Composition**: Enables keyboard-driven workflows, thought-speed navigation
- **Source**: VSCode, Raycast, Spotlight
- **Maturity**: Production

**Primitive: Vim Motion System**
- **Category**: Interface | **Object**: O.INS | **Platform**: Desktop, CLI
- **Description**: Modal editing with composable motion commands
- **Capability Contract**:
  - Input: Motion commands (hjkl, w, b, etc.) + operators (d, c, y)
  - Output: Efficient text navigation and editing
  - Performance: Thought-speed once learned
  - Failure: Steep learning curve
- **Composition**: Pairs with any text editor, enables expert-level speed
- **Source**: Vim, Neovim
- **Maturity**: Production

**Primitive: Spatial Navigation**
- **Category**: Interface | **Object**: O.SRF | **Platform**: XR
- **Description**: Navigate using 3D spatial relationships
- **Capability Contract**:
  - Input: Gaze direction + gesture or voice command
  - Output: Navigate to spatial location
  - Performance: <100ms for spatial tracking
  - Failure: Requires calibrated space, can be disorienting
- **Composition**: Enables immersive workflows, spatial memory
- **Source**: VisionOS
- **Maturity**: Validated

### Input Primitives

**Primitive: Voice-to-Text**
- **Category**: Interface | **Object**: O.SNS + O.FN | **Platform**: Mobile, Ambient
- **Description**: Continuous speech recognition with punctuation
- **Capability Contract**:
  - Input: Audio stream
  - Output: Transcribed text with punctuation
  - Performance: Real-time or faster (1.0x-1.5x speed)
  - Failure: Accuracy drops in noisy environments
- **Composition**: Enables hands-free workflows, mobile-optimized
- **Source**: Whisper, platform speech recognition
- **Maturity**: Production

**Primitive: Autocomplete Intelligence**
- **Category**: Interface | **Object**: O.FN + O.MOD | **Platform**: Universal
- **Description**: Context-aware suggestion of next input
- **Capability Contract**:
  - Input: Current context + partial input
  - Output: Ranked completion suggestions
  - Performance: <100ms for suggestion generation
  - Failure: Annoying if suggestions poor quality
- **Composition**: Reduces typing burden, pairs with any text input
- **Source**: IDE autocomplete, Gmail smart compose
- **Maturity**: Production

**Primitive: Collaborative Cursor**
- **Category**: Interface | **Object**: O.SRF + O.SVC | **Platform**: Desktop, Mobile
- **Description**: Real-time multi-user cursor presence and edits
- **Capability Contract**:
  - Input: User edits + cursor positions
  - Output: Conflict-free synchronized state
  - Performance: <100ms for sync (good network)
  - Failure: Conflicts on simultaneous edits, requires resolution
- **Composition**: Enables real-time collaboration
- **Source**: Figma, Google Docs
- **Maturity**: Production

### Layout Primitives

**Primitive: Split-Pane Layouts**
- **Category**: Interface | **Object**: O.SRF | **Platform**: Desktop, XR
- **Description**: Resizable workspace subdivisions
- **Capability Contract**:
  - Input: Split commands (horizontal/vertical) + resize operations
  - Output: Nested pane structure with preserved ratios
  - Performance: Instant
  - Failure: Complexity increases with nesting depth
- **Composition**: Enables parallel workflows, pairs with tab management
- **Source**: tmux, IDE splits
- **Maturity**: Production

**Primitive: Tab Management**
- **Category**: Interface | **Object**: O.SRF | **Platform**: Desktop, Mobile
- **Description**: Parallel contexts with quick switching
- **Capability Contract**:
  - Input: Tab creation/switching/closing commands
  - Output: Multiple parallel contexts with fast switching
  - Performance: <50ms for tab switch
  - Failure: Cognitive overhead with too many tabs
- **Composition**: Reduces context switching cost
- **Source**: Browser tabs, terminal tabs
- **Maturity**: Production

**Primitive: Infinite Canvas**
- **Category**: Interface | **Object**: O.SRF | **Platform**: Desktop, XR
- **Description**: Unlimited 2D/3D workspace with pan/zoom
- **Capability Contract**:
  - Input: Pan/zoom gestures + object placement
  - Output: Spatially organized unlimited workspace
  - Performance: 60fps rendering
  - Failure: Can get lost without minimap
- **Composition**: Enables freeform thinking, spatial organization
- **Source**: Miro, FigJam, Obsidian canvas
- **Maturity**: Production

---

## VII. Governance Primitive Catalog

### Security Primitives

**Primitive: Input Validation**
- **Category**: Governance | **Object**: O.GRD | **Platform**: Universal
- **Description**: Detect and block malicious inputs
- **Capability Contract**:
  - Input: User input
  - Output: Validation result (safe/unsafe) + sanitized version
  - Performance: <50ms for validation
  - Failure: False positives block legitimate inputs, false negatives allow attacks
- **Composition**: Required for all user-facing systems
- **Maturity**: Production

**Primitive: PII Detection and Masking**
- **Category**: Governance | **Object**: O.GRD | **Platform**: Universal
- **Description**: Identify and redact personally identifiable information
- **Capability Contract**:
  - Input: Text content
  - Output: PII locations + masked version
  - Performance: 100-500ms depending on text length
  - Failure: May miss novel PII formats, may over-mask
- **Composition**: Required for privacy compliance
- **Maturity**: Production

**Primitive: Circuit Breaker**
- **Category**: Governance | **Object**: O.GRD | **Platform**: Universal
- **Description**: Halt cascading failures, prevent overload
- **Capability Contract**:
  - Input: Operation + failure threshold + timeout
  - Output: Operation result or circuit open error
  - Performance: Minimal overhead (<10ms)
  - Failure: May reject legitimate requests after failures
- **Composition**: Protects systems from cascading failures
- **Maturity**: Production

**Primitive: Rate Limiting**
- **Category**: Governance | **Object**: O.GRD | **Platform**: Universal
- **Description**: Control request frequency per user/resource
- **Capability Contract**:
  - Input: Request + rate limit specification
  - Output: Allow or deny + remaining quota
  - Performance: <10ms for check
  - Failure: Legitimate burst traffic may be rejected
- **Composition**: Prevents abuse, protects resources
- **Maturity**: Production

### Quality Primitives

**Primitive: Output Validation**
- **Category**: Governance | **Object**: O.EVL | **Platform**: Universal
- **Description**: Verify agent outputs meet quality criteria
- **Capability Contract**:
  - Input: Output + quality criteria
  - Output: Validation result + quality score
  - Performance: 500ms-2s depending on criteria
  - Failure: May reject valid outputs if criteria too strict
- **Composition**: Quality gates for high-stakes outputs
- **Maturity**: Production

**Primitive: Content Filtering**
- **Category**: Governance | **Object**: O.GRD | **Platform**: Universal
- **Description**: Block inappropriate or harmful content
- **Capability Contract**:
  - Input: Content + policy rules
  - Output: Filter result (pass/block) + reason
  - Performance: 100-500ms
  - Failure: False positives block legitimate content
- **Composition**: Safety layer for user-facing systems
- **Maturity**: Production

### Compliance Primitives

**Primitive: Audit Logging**
- **Category**: Governance | **Object**: O.CPL | **Platform**: Universal
- **Description**: Immutable record of all system actions
- **Capability Contract**:
  - Input: Action + actor + context + timestamp
  - Output: Logged entry with unique ID
  - Performance: <50ms write, queryable
  - Failure: Storage growth unbounded without rotation
- **Composition**: Required for compliance, enables accountability
- **Maturity**: Production

**Primitive: Approval Gate**
- **Category**: Governance | **Object**: O.GRD | **Platform**: Universal
- **Description**: Human-in-loop for high-impact decisions
- **Capability Contract**:
  - Input: Action + impact assessment
  - Output: Approval (granted/denied) with reasoning
  - Performance: Human-dependent (minutes to hours)
  - Failure: Blocks workflow if approval not available
- **Composition**: Governance for high-stakes automation
- **Maturity**: Production

---

## VIII. Feedback Primitive Catalog

### Observation Primitives

**Primitive: Usage Tracking**
- **Category**: Feedback | **Object**: O.STM + O.DP | **Platform**: Universal
- **Description**: Record tool/feature usage with context
- **Capability Contract**:
  - Input: Tool invocation + context metadata
  - Output: Usage log entry
  - Performance: <10ms (non-blocking)
  - Failure: None if async
- **Composition**: Foundation for all meta-orchestration
- **Maturity**: Production

**Primitive: Sequence Detection**
- **Category**: Feedback | **Object**: O.FN + O.EVL | **Platform**: Universal
- **Description**: Identify temporal patterns in tool/action sequences
- **Capability Contract**:
  - Input: Usage logs + frequency threshold + temporal window
  - Output: Candidate patterns with statistics
  - Performance: Minutes (offline analysis)
  - Failure: False positives if threshold too low
- **Composition**: Enables apparatus recognition
- **Maturity**: Validated

**Primitive: Context Capture**
- **Category**: Feedback | **Object**: O.SNS + O.DP | **Platform**: Universal
- **Description**: Record relevant context for actions
- **Capability Contract**:
  - Input: Action + environment state
  - Output: Contextualized log entry
  - Performance: <50ms
  - Failure: Privacy concerns if too detailed
- **Composition**: Enables context-aware routing
- **Maturity**: Validated

### Learning Primitives

**Primitive: Pattern Recognition**
- **Category**: Feedback | **Object**: O.FN + O.AGT | **Platform**: Universal
- **Description**: Identify repeated structures in data
- **Capability Contract**:
  - Input: Usage data + pattern specification
  - Output: Identified patterns with confidence scores
  - Performance: Minutes to hours (depends on data size)
  - Failure: Requires sufficient data, tuning threshold
- **Composition**: Enables automation, pairs with observation
- **Maturity**: Validated

**Primitive: Confidence Calibration**
- **Category**: Feedback | **Object**: O.EVL + O.FN | **Platform**: Universal
- **Description**: Adjust confidence scores based on historical accuracy
- **Capability Contract**:
  - Input: Historical predictions + outcomes
  - Output: Calibrated confidence function
  - Performance: Minutes (offline training)
  - Failure: Requires sufficient calibration data
- **Composition**: Enables trust calibration, improves routing
- **Maturity**: Validated

### Suggestion Primitives

**Primitive: Apparatus Recognition**
- **Category**: Feedback | **Object**: O.AGT + O.EVL | **Platform**: Universal
- **Description**: Auto-detect repeated tool sequences worthy of naming
- **Capability Contract**:
  - Input: Usage logs + threshold (frequency, stability)
  - Output: Apparatus candidates with justification
  - Performance: Minutes (offline analysis)
  - Failure: False positives if threshold miscalibrated
- **Composition**: Enables workflow optimization
- **Maturity**: Validated

**Primitive: Consolidation Detection**
- **Category**: Feedback | **Object**: O.EVL + O.FN | **Platform**: Universal
- **Description**: Identify redundant tools with overlapping capabilities
- **Capability Contract**:
  - Input: Tool inventory + usage patterns + primitive catalog
  - Output: Consolidation opportunities with justification
  - Performance: Minutes to hours (offline analysis)
  - Failure: May miss subtle differences between tools
- **Composition**: Enables primitive extraction
- **Maturity**: Validated

**Primitive: Routing Optimization**
- **Category**: Feedback | **Object**: O.AGT + O.WF | **Platform**: Universal
- **Description**: Suggest better tool choices based on historical success
- **Capability Contract**:
  - Input: Historical routing decisions + outcomes + context
  - Output: Routing suggestions with confidence
  - Performance: <100ms for suggestion
  - Failure: Requires historical data, cold start problem
- **Composition**: Enables intelligent routing
- **Maturity**: Validated

---

## IX. Composition Pattern Library

### Pattern: Memory-Enhanced Agent

**Components**:
- O.AGT (base agent)
- O.STM (working memory / conversation history)
- O.DP (episodic memory / interaction log)
- O.DP + O.MOD (semantic memory / vector store)

**Architecture**:
```
User query → Retrieve from semantic memory
            ↓
          Recall relevant episodes
            ↓
          Load working memory context
            ↓
          Agent generates response
            ↓
          Log to episodic memory
            ↓
          Extract facts to semantic memory
```

**Production validation**: 35% higher accuracy vs. memory-less baseline

**Use case**: Conversational agents, personal assistants, learning systems

### Pattern: Production RAG System

**Components**:
- Hybrid Search (O.WF + O.FN)
- Reranking Model (O.MOD)
- Prompt Caching (O.SVC)
- Context Assembly (O.FN)

**Architecture**:
```
Query → Hybrid search (vector + keyword + metadata)
       ↓
     Rerank results by relevance
       ↓
     Assemble context (prioritize + cache static)
       ↓
     Generate response
       ↓
     Return with source citations
```

**Production validation**: 49% fewer retrieval misses, 40-90% cost reduction

**Use case**: Knowledge-intensive Q&A, document analysis, research

### Pattern: Critic-Enhanced Generation

**Components**:
- Actor Agent (O.AGT)
- Critic Agent (O.AGT)
- Iteration Logic (O.WF)

**Architecture**:
```
Task → Actor generates draft
      ↓
    Critic evaluates (score + feedback)
      ↓
    Quality threshold met? → Yes → Return
      ↓ No
    Actor refines based on feedback
      ↓
    Repeat (max 3 iterations)
```

**Production validation**: 30-40% quality improvement

**Use case**: High-quality content generation, code generation, analysis

### Pattern: Specialist Swarm

**Components**:
- Multiple Specialist Agents (O.AGT)
- Coordinator Agent (O.AGT)
- Parallel Dispatch (O.WF)

**Architecture**:
```
Complex task → Coordinator decomposes
              ↓
            Parallel dispatch to specialists
            (fundamental, technical, sentiment, etc.)
              ↓
            Coordinator synthesizes diverse analyses
              ↓
            Return integrated insights
```

**Production validation**: 45% faster, 60% higher accuracy

**Use case**: Multi-faceted analysis, complex decision-making

### Pattern: Cached Multi-Agent Pipeline

**Components**:
- Sequential Coordination (O.WF)
- Multiple Agents (O.AGT)
- Prompt Caching (O.SVC)
- Checkpoint Storage (O.DP)

**Architecture**:
```
Task → Agent 1 (research) [cached system prompt]
      ↓
    Checkpoint results
      ↓
    Agent 2 (draft) [cached prompt + results]
      ↓
    Checkpoint results
      ↓
    Agent 3 (edit) [cached prompt + draft]
      ↓
    Final output
```

**Economics**: 70-80% cost reduction via caching

**Use case**: Multi-stage content pipelines, repeated workflows

---

## X. Platform-Specific Primitive Adaptations

### Desktop Primitives

**Emphasize**:
- Complex orchestration (multi-agent coordination)
- Deep analysis (memory-intensive operations)
- Precision editing (vim motions, keyboard shortcuts)
- Visualization (split panes, multiple windows)

**Avoid**:
- Touch-optimized interfaces
- Voice-first interactions
- Mobile sensors

### Mobile Primitives

**Emphasize**:
- Voice-to-text (hands-free input)
- Quick capture (photos, voice notes, location)
- Glanceable information (summaries, dashboards)
- Gesture shortcuts (swipe patterns)

**Avoid**:
- Keyboard-heavy workflows
- Multi-window layouts
- Extended focus sessions

### XR Primitives

**Emphasize**:
- Spatial navigation (3D positioning)
- Gesture-based interaction (hand tracking)
- Immersive visualization (spatial data)
- Embodied workflows (physical movement)

**Avoid**:
- Text-heavy interfaces
- Precise keyboard input
- Extended typing sessions

### Ambient Primitives

**Emphasize**:
- Continuous monitoring (always-on sensors)
- Proactive suggestions (anticipatory)
- Background processing (invisible work)
- Context-aware triggering (right time/place)

**Avoid**:
- Explicit user interfaces
- Manual invocations
- Synchronous interactions

### CLI Primitives

**Emphasize**:
- Scriptable operations (automation)
- Pipeable composition (combine primitives)
- Batch processing (large-scale operations)
- System-level access (low-level control)

**Avoid**:
- Graphical interfaces
- Mouse interactions
- Real-time visualizations

---

## XI. Primitive Lifecycle Management

### Discovery Phase

**Sources**:
- Tools actively used (extraction from existing)
- Tools in evaluation (assessment for adoption)
- Gap analysis (capabilities needed but missing)
- User friction (where tools fail)

**Minimal documentation**:
- Name and one-sentence description
- Extraction source
- Initial reuse potential assessment

### Validation Phase

**Criteria**:
- Successfully used in at least one composition
- Meets performance requirements
- Platform compatibility confirmed
- No major bugs/limitations discovered

**Quality scoring** (1-5):
- Reliability: Does it work consistently?
- Performance: Meets latency requirements?
- Compatibility: Works across expected platforms?
- Composability: Combines well with others?
- Maintainability: Easy to update/fix?

### Production Phase

**Characteristics**:
- Used in multiple compositions
- Quality score 4-5
- Complete documentation
- Platform variations documented
- Composition patterns identified

**Maintenance**:
- Version tracking (source tool updates)
- Performance monitoring
- Usage statistics
- Deprecation planning if superseded

### Deprecation Phase

**Triggers**:
- Better alternative identified
- Source tool abandoned
- Unused (silent for 6+ months)
- Platform incompatibility

**Process**:
- Mark deprecated (don't delete immediately)
- Document replacement/migration path
- Notify dependent compositions
- Archive after grace period

---

## XII. Catalog Maintenance

### Weekly (15 minutes)
- Review recent tool usage
- Add 1-2 new primitives if discovered
- Update "last used" dates
- Note composition ideas

### Monthly (1-2 hours)
- Review reuse statistics
- Identify high-value primitives (promote)
- Identify unused primitives (deprecate candidates)
- Update quality scores
- Document new composition patterns

### Quarterly (3-4 hours)
- Comprehensive catalog assessment
- Platform coverage analysis
- Gap identification (missing capabilities)
- Major consolidations
- Strategic direction

---

## XIII. Success Metrics

### Catalog Health
- **Coverage**: Primitives for common workflows?
- **Reuse rate**: Average uses per primitive
- **Quality distribution**: Percentage at each level
- **Platform balance**: Coverage across platforms

### Composition Success
- **Time to build**: Speed of bespoke tool creation
- **Composition reliability**: Do composed tools work?
- **Maintenance burden**: Effort to maintain
- **User satisfaction**: Do tools serve needs?

### Extraction Efficiency
- **Extraction rate**: Primitives per tool evaluated
- **Reuse validation**: Percentage actually reused
- **Consolidation success**: Reduced redundancy without capability loss

---

## XIV. Conclusion

**The primitive catalog is a living tool**—growing through observation, improving through validation, optimizing through composition.

**Key principles**:
1. Apps are transitional, primitives are eternal
2. Observation over prescription
3. Quality over quantity
4. Composition over adoption
5. Platform context matters
6. Intelligence emerges from usage data

**The goal**: Thought-speed navigation from intention to execution via optimal primitive composition.

**The mechanism**: Extract what persists, catalog what's valuable, compose what's needed, learn what works.

**The displacement**: Tools become invisible raw material. Primitives become the vocabulary of work. Intelligence mediates composition.

**Begin cataloging. Begin composing. Begin displacing.**