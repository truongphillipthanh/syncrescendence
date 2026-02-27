# Extraction: SOURCE-undated-016

**Source**: `SOURCE-20260116-x-article-ghumare64-agents_201_orchestrating_multiple_agents_that_actu.md`
**Atoms extracted**: 55
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (11)

### ATOM-SOURCE-undated-016-0001
**Lines**: 1-3
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> The primary challenge after building a single agent is enabling multiple agents to collaborate effectively without excessive token usage or coordination issues.

### ATOM-SOURCE-undated-016-0002
**Lines**: 7-8
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.90

> Single agents quickly reach limitations due to context window saturation, unclear decision-making, and debugging difficulties.

### ATOM-SOURCE-undated-016-0003
**Lines**: 8-10
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.90

> Multi-agent systems address single-agent limitations by distributing work among specialized agents, mirroring human team structures.

### ATOM-SOURCE-undated-016-0005
**Lines**: 19-21
**Context**: consensus / limitation
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.90

> The primary tradeoff of multi-agent systems is increased coordination overhead, requiring agents to communicate, share state, and avoid conflicts.

### ATOM-SOURCE-undated-016-0009
**Lines**: 54-56
**Context**: consensus / limitation
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.80

> Supervisors in the Supervisor Pattern can become bottlenecks, leading to serial processing for coordination steps and increased token costs with more coordination layers.

### ATOM-SOURCE-undated-016-0012
**Lines**: 84-87
**Context**: consensus / limitation
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.20, speculation_risk=0.60, actionability=0.30, epistemic_stability=0.70

> The Swarm Pattern can lead to unpredictable emergent behavior, including duplicated work, infinite loops, or suboptimal solutions, making debugging difficult due to complex information flow.

### ATOM-SOURCE-undated-016-0015
**Lines**: 120-122
**Context**: consensus / limitation
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.30, epistemic_stability=0.70

> The Hierarchical Pattern can cause token costs to explode due to coordination overhead at each layer, only justified for complexity that flat patterns cannot handle.

### ATOM-SOURCE-undated-016-0040
**Lines**: 265-267
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.90

> Multi-agent systems significantly increase token consumption, potentially 10x the cost of a single-agent system for the same task due to coordination overhead.

### ATOM-SOURCE-undated-016-0042
**Lines**: 283-285
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.90

> Multiple LLM calls in multi-agent systems introduce significant latency, with each call adding 2-5 seconds, making serial processing detrimental to user experience.

### ATOM-SOURCE-undated-016-0044
**Lines**: 295-297
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.90

> In multi-agent systems, one agent's failure can cascade throughout the system, unlike single-agent systems where failures are local.

### ATOM-SOURCE-undated-016-0047
**Lines**: 310-311
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.90

> Multi-agent systems require robust monitoring and observability from day one to debug effectively.

## Concept (5)

### ATOM-SOURCE-undated-016-0016
**Lines**: 124-125
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> Agent communication strategies define how information flows between agents, complementing orchestration patterns that define structural relationships.

### ATOM-SOURCE-undated-016-0029
**Lines**: 193-195
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> Multi-agent systems face the additional challenge of coordinating state among agents without duplication or conflicts, beyond the memory management of single agents.

### ATOM-SOURCE-undated-016-0032
**Lines**: 198-200
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> Session-Based Memory involves each agent interaction having isolated state that merges back into shared memory upon completion.

### ATOM-SOURCE-undated-016-0036
**Lines**: 218-220
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> Window Memory (Conversation Context) maintains a sliding window of recent exchanges across all agents, compressing or dropping oldest entries.

### ATOM-SOURCE-undated-016-0038
**Lines**: 243-245
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.60

> Episodic Memory stores interaction history between specific agents to enable learning from past coordination.

## Framework (20)

### ATOM-SOURCE-undated-016-0004
**Lines**: 12-18
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.90

> Benefits of multi-agent systems include specialization (agents master one domain), parallel processing (simultaneous work on subtasks), maintainability (easier to identify and fix issues), and scalability (adding new capabilities by adding agents).

### ATOM-SOURCE-undated-016-0006
**Lines**: 23-25
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Three proven orchestration patterns for coordinating multiple agents are the Supervisor Pattern, Swarm Pattern, and Hierarchical Pattern, chosen based on coordination needs.

### ATOM-SOURCE-undated-016-0007
**Lines**: 27-30
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> The Supervisor Pattern involves a central supervisor agent that decomposes tasks, routes to worker agents, validates outputs, and synthesizes the final response.

### ATOM-SOURCE-undated-016-0010
**Lines**: 58-60
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.70

> The Swarm Pattern is a peer-to-peer orchestration where agents communicate directly, exchange information, and self-organize without a central controller.

### ATOM-SOURCE-undated-016-0013
**Lines**: 89-91
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.70

> The Hierarchical Pattern is a recursive Supervisor Pattern with multiple layers, where a top-level agent manages mid-level agents, which in turn manage worker agents.

### ATOM-SOURCE-undated-016-0017
**Lines**: 127-128
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> Shared State is a communication strategy where all agents read from and write to a common state object, making changes visible to everyone.

### ATOM-SOURCE-undated-016-0018
**Lines**: 139-141
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.90

> Advantages of Shared State include simple implementation, easy debugging by inspecting state, and no message passing complexity.

### ATOM-SOURCE-undated-016-0019
**Lines**: 142-144
**Context**: consensus / limitation
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.90

> Disadvantages of Shared State include potential for race conditions with simultaneous writes, lack of isolation between agent contexts, and unbounded state growth without pruning.

### ATOM-SOURCE-undated-016-0021
**Lines**: 148-149
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> Message Passing is an event-driven communication strategy where agents send messages to each other without direct state sharing.

### ATOM-SOURCE-undated-016-0022
**Lines**: 160-162
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> Advantages of Message Passing include loose coupling between agents, suitability for asynchronous work, and ease of adding new agents without modifying existing ones.

### ATOM-SOURCE-undated-016-0023
**Lines**: 163-165
**Context**: consensus / limitation
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.80

> Disadvantages of Message Passing include harder debugging due to tracing message flow, potential for message loops, and the need for infrastructure like an event bus or queues.

### ATOM-SOURCE-undated-016-0025
**Lines**: 169-170
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> Handoff Mechanism is a communication strategy where one agent explicitly transfers control and context to another agent.

### ATOM-SOURCE-undated-016-0026
**Lines**: 184-186
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> Advantages of the Handoff Mechanism include clear control flow, easy auditing of agent actions, and preservation of context across agents.

### ATOM-SOURCE-undated-016-0027
**Lines**: 187-189
**Context**: consensus / limitation
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.80

> Disadvantages of the Handoff Mechanism include tight coupling between agents, serial processing by default, and overhead on every transition.

### ATOM-SOURCE-undated-016-0030
**Lines**: 197-198
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> Session-Based Memory involves isolated state for each agent interaction session, which is merged back into shared memory upon completion.

### ATOM-SOURCE-undated-016-0031
**Lines**: 198-200
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> Multi-agent memory patterns include Session-Based Memory, Window Memory (Conversation Context), and Episodic Memory (Cross-Agent Learning).

### ATOM-SOURCE-undated-016-0034
**Lines**: 215-216
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> Window Memory maintains a sliding window of recent exchanges across all agents, compressing or dropping older entries.

### ATOM-SOURCE-undated-016-0045
**Lines**: 298-303
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.90

> Common failure modes in multi-agent systems include poison pills (garbage output), deadlocks (circular dependencies), resource exhaustion (rate limits), and cascading failures (supervisor failure).

### ATOM-SOURCE-undated-016-0048
**Lines**: 313-317
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> Essential metrics for multi-agent system observability include per-agent success rate, coordination overhead, token consumption by agent, and agent interaction patterns.

### ATOM-SOURCE-undated-016-0049
**Lines**: 354-362
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.90

> Common anti-patterns in multi-agent systems include over-coordination, creating 'kitchen sink' agents, synchronous execution, ignoring costs, and lacking fallbacks.

## Praxis Hook (19)

### ATOM-SOURCE-undated-016-0008
**Lines**: 31-35
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> Use the Supervisor Pattern for tasks with clear subtask decomposition, when auditability and reasoning transparency are needed, when quality control is prioritized over speed, and for coordinating 3-8 worker agents.

### ATOM-SOURCE-undated-016-0011
**Lines**: 61-65
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> Use the Swarm Pattern when tasks benefit from multiple perspectives, lack clear serial decomposition, require real-time responsiveness, and agents need to react to each other's work.

### ATOM-SOURCE-undated-016-0014
**Lines**: 92-96
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> Use the Hierarchical Pattern for tasks too complex for flat supervision, when different domains require distinct management strategies, for coordinating 10+ agents, and when both strategic and tactical control are needed.

### ATOM-SOURCE-undated-016-0020
**Lines**: 145-146
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Start with Shared State for most agent systems until specific problems arise that it cannot solve.

### ATOM-SOURCE-undated-016-0024
**Lines**: 166-167
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> Use Message Passing when agents are truly independent and should not be aware of each other, or when asynchronous processing across services is required.

### ATOM-SOURCE-undated-016-0028
**Lines**: 190-191
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> Use the Handoff Mechanism when tasks must occur in a specific order and context needs to flow sequentially through the agent chain.

### ATOM-SOURCE-undated-016-0033
**Lines**: 211-213
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Session-Based Memory is useful for parallel agents that need to read shared context but make isolated changes, common in supervisor patterns where workers operate independently.

### ATOM-SOURCE-undated-016-0035
**Lines**: 215-217
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Implement Session-Based Memory for parallel agents that need to read shared context but make isolated changes, common in supervisor patterns where workers operate independently.

### ATOM-SOURCE-undated-016-0037
**Lines**: 239-242
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Use Window Memory for long-running agent conversations where context is important but retaining all information is impractical, such as in RAG applications.

### ATOM-SOURCE-undated-016-0039
**Lines**: 259-261
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.60

> Employ Episodic Memory for agents that frequently collaborate to allow them to improve based on successful past interactions.

### ATOM-SOURCE-undated-016-0041
**Lines**: 276-281
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To optimize token economics in multi-agent systems: cache supervisor instructions, compress worker outputs to structured data, execute agents in parallel, and use lazy agent activation.

### ATOM-SOURCE-undated-016-0043
**Lines**: 290-292
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Always parallelize independent work in multi-agent systems to manage latency, as serial execution significantly increases total task time.

### ATOM-SOURCE-undated-016-0046
**Lines**: 304-308
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Defend against multi-agent system failures by implementing timeouts at every layer, circuit breakers after N failures, graceful degradation, and isolating state to prevent corruption.

### ATOM-SOURCE-undated-016-0050
**Lines**: 364-368
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Use the Supervisor pattern when auditability is needed, tasks decompose clearly, with 3-8 specialized agents, and quality is prioritized over speed.

### ATOM-SOURCE-undated-016-0051
**Lines**: 369-373
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> Use the Swarm pattern when multiple perspectives are needed, there's no clear task decomposition, real-time responsiveness is critical, and agents can self-organize.

### ATOM-SOURCE-undated-016-0052
**Lines**: 374-378
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> Use the Hierarchical pattern when managing 10+ agents, multiple layers of abstraction are needed, both strategic and tactical control are required, and token costs are acceptable.

### ATOM-SOURCE-undated-016-0053
**Lines**: 379-383
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Use a single agent when the task is simple enough, one domain of expertise is sufficient, minimizing costs is important, or when the multi-agent approach is not yet clear.

### ATOM-SOURCE-undated-016-0054
**Lines**: 385-390
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> When starting with multi-agent systems, pick the simplest pattern, typically the supervisor pattern: build one capable agent, identify its struggles, extract that into a second agent, add a supervisor, and iterate.

### ATOM-SOURCE-undated-016-0055
**Lines**: 395-395
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Build one system that uses two agents reliably before attempting to build ten.
