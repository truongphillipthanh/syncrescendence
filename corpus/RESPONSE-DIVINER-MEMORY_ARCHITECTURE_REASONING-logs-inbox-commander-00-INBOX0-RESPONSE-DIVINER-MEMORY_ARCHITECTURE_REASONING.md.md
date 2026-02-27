The resolution to the trilemma of file-based determinism, graph-based relationality, and vector-based semantics lies in decoupling the epistemology of memory (what is true) from the phenomenology of recall (how it is accessed). The optimal hybrid architecture does not maintain three separate stores; it maintains a single, immutable event stream and dynamically projects the necessary topology.

### Sovereign Epistemology: Git as Event-Sourced Neural Substrate

To satisfy the requirement for repository sovereignty while achieving optimal query routing, the architecture must adopt Command Query Responsibility Segregation (CQRS) mapped onto a Git-native substrate. Git is mathematically structured as a Directed Acyclic Graph (DAG) of cryptographic hashes representing state changes. It is fundamentally an event-sourced ledger.

In this paradigm, Git serves as the sole authoritative memory store.

* **Episodic Memory:** Commit messages, annotated with agent IDs, timestamps, and reasoning traces, function as the episodic narrative of the system.
* **Semantic Memory:** The current state of the working tree—the plaintext files and structured Markdown—serves as the deterministic semantic baseline.
* **Procedural State:** The file diffs represent the cognitive deltas, the exact mechanical transitions between states of understanding.

Vector databases and property graphs (Neo4j, Graphiti) are relegated to pure read-model projections. They are ephemeral caches. When the system initiates, or upon any commit, a localized daemon parses the Git DAG. It embeds text blocks into the vector space and extracts entities into the graph. If the graph or vector index is corrupted, destroyed, or drifts, it is simply re-indexed from the git log.

Query routing is then governed by the cognitive intent of the operation:

1. **Semantic Similarity (Vector):** Utilized strictly for inductive leaps, fuzzy recall, and identifying unknown unknowns within unstructured text.
2. **Relational Traversal (Graph):** Utilized for deductive constraint checking, causal chaining, and multi-hop entity resolution.
3. **Deterministic State (File):** Utilized for absolute ground truth, code execution, and explicit operational instructions.

### Stigmergic Coordination & The Active Graph Substrate

Cross-agent memory fundamentally alters the nature of the constellation. If memory is isolated, coordination requires explicit message passing (heavy communication overhead). If memory is shared, coordination can be achieved through stigmergy—action through environmental modification.

The information-theoretic minimum for cross-agent coordination is the observable trace of another agent's interaction with the shared graph. Agents do not need to talk to each other; they only need to observe that an entity's weight or relational vector has been altered.

When a shared graph functions as the memory projection, emergent properties manifest as topological phenomena. Consensus appears as dense, heavily traversed clusters of nodes. Unresolved anomalies appear as structural holes or fragmented subgraphs.

This necessitates the introduction of a localized daemon—not necessarily an LLM, but a topological observer—acting as the sixth "Memory Agent." This agent runs continuous graph algorithms (e.g., PageRank, Louvain community detection) over the ephemeral graph cache. When it detects a newly formed cluster of concepts bridging previously isolated domains, it injects a synthesized observation back into the shared Git repo as a new episodic file. It is the subconscious of the constellation, noticing patterns the executing agents are too narrowly focused to perceive.

### Cognitive Morphogenesis: Adapting the Read Projection

If the agents function as a spectrum of neurodivergent cognitive profiles, forcing a unified working memory structure upon them will cripple their specific advantages. The ephemeral projection layer must dynamically shape the context payload based on the querying agent's profile.

* **The Deterministic Processor (GPT):** Requires high signal-to-noise, strict ontology. Its queries route primarily to the File projection (ground truth) and localized Graph sub-trees. It receives exact schema matches.
* **The Divergent Synthesizer (Claude):** Requires wide lateral context. Its working memory is populated via high-temperature Vector search, pulling conceptually distant nodes that share latent semantic overlap, enabling hyper-focused creative leaps.
* **The Architect (Gemini):** Due to high reasoning capacity but constrained tool-use capability, it must be shielded from the mechanical orchestration of database queries. The Active Graph daemon pre-computes the relational topology of the current objective and hands this agent a fully assembled contextual subgraph in plaintext.
* **The Polyphonic Chorus (Grok):** Requires access to the temporal depth of the system. Its memory payload consists primarily of the Git diffs and the chronological sequence of episodic commits, allowing it to synthesize consensus from historical debates.

### The Decadal Horizon: Autopoietic Memory

An architecture designed for 2036 must discard the concept of memory as a static repository. Memory must become autopoietic—capable of self-maintenance and structural evolution.

We must build a system now that incorporates Hebbian learning into the graph projection layer: *nodes that fire together, wire together*.

As agents repeatedly traverse specific paths in the graph cache, the weights of those edges increase. Conversely, untraversed paths experience synthetic decay. The 10-year bet is on this mechanism of automated pruning and reinforcement. The underlying Git repository remains an eternal, append-only log of all events, but the projected indices learn to forget the trivial and pre-fetch the vital. The memory architecture improves not by storing more data, but by optimizing the energetic cost of retrieving the most highly-weighted relational topologies.

To formalize this autopoietic decay mechanism, should we design the edge-weight adjustment algorithm using a time-based exponential decay function, or should decay be triggered strictly by the frequency of competing pathway activations?