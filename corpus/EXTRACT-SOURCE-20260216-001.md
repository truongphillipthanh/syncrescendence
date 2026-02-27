# Extraction: SOURCE-20260216-001

**Source**: `SOURCE-20260216-website-article-georgeguimaraes-your-agent-framework-is-just.md`
**Atoms extracted**: 18
**Categories**: analogy, claim, concept, framework, praxis_hook

---

## Analogy (1)

### ATOM-SOURCE-20260216-001-0006
**Lines**: 48-50
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> The problems faced by modern AI agent frameworks are analogous to those solved by the Erlang Open Telecom Platform (OTP) formalized in 1998 for telephone switches, which required handling millions of concurrent calls with zero downtime.

## Claim (9)

### ATOM-SOURCE-20260216-001-0001
**Lines**: 20-22
**Context**: consensus / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.40, epistemic_stability=0.80

> The actor model introduced by Erlang in 1986 is the agent model that AI is rediscovering in 2026.

### ATOM-SOURCE-20260216-001-0002
**Lines**: 22-25
**Context**: consensus / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.40, epistemic_stability=0.80

> Every pattern the Python AI ecosystem is building (isolated state, message passing, supervision hierarchies, fault recovery) already exists in the BEAM virtual machine.

### ATOM-SOURCE-20260216-001-0004
**Lines**: 37-40
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.00, speculation_risk=0.00, actionability=0.10, epistemic_stability=0.90

> Traditional web frameworks like Rails, Django, and Laravel are optimized for requests that take milliseconds, involving database queries and HTML rendering in under 100ms.

### ATOM-SOURCE-20260216-001-0011
**Lines**: 109-113
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.60, actionability=0.40, epistemic_stability=0.80

> The BEAM's "let it crash" philosophy is particularly suitable for AI agents because it's impossible to predict all failure modes of non-deterministic systems like LLMs, which can exhibit unexpected behaviors.

### ATOM-SOURCE-20260216-001-0014
**Lines**: 130-131
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> The goal of Tribunal is to make AI agent testing as natural as testing any other Elixir code, leveraging the fact that agents are processes and processes are testable within the Elixir ecosystem.

### ATOM-SOURCE-20260216-001-0015
**Lines**: 136-140
**Context**: consensus / limitation
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> Python's Global Interpreter Lock (GIL) prevents true parallel execution of lightweight processes, and its asyncio offers concurrency without isolation, meaning coroutines share memory and lack per-coroutine garbage collection.

### ATOM-SOURCE-20260216-001-0016
**Lines**: 140-142
**Context**: consensus / limitation
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> Python's supervision mechanisms are limited to 'try/except' patterns, making it difficult to restart coroutines in a clean state or transparently.

### ATOM-SOURCE-20260216-001-0017
**Lines**: 144-147
**Context**: consensus / limitation
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> TypeScript/Node.js offers better concurrency than Python due to its event loop but remains fundamentally single-threaded, with heavyweight OS worker threads and no preemptive scheduling, hot code swapping, or built-in distribution.

### ATOM-SOURCE-20260216-001-0018
**Lines**: 148-148
**Context**: consensus / evidence
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> Building actor runtimes on top of existing VMs, like Akka on JVM or Microsoft Orleans on .NET, demonstrates that deep runtime support is necessary for effective actor models, requiring massive engineering effort to approximate what the BEAM provides natively.

## Concept (2)

### ATOM-SOURCE-20260216-001-0003
**Lines**: 30-32
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.00, speculation_risk=0.00, actionability=0.10, epistemic_stability=0.90

> The BEAM is the virtual machine that runs both Erlang and Elixir code, similar to how the JVM runs both Java and Kotlin.

### ATOM-SOURCE-20260216-001-0008
**Lines**: 74-78
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.60, actionability=0.20, epistemic_stability=0.80

> AI agents are inherently non-deterministic, meaning their behavior and outcomes are unpredictable due to factors like varying LLM responses, tool failures, rate limits, context window overflows, and parsing errors.

## Framework (2)

### ATOM-SOURCE-20260216-001-0005
**Lines**: 39-47
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.70

> Current AI agent frameworks (Langroid, AutoGen 0.4, LangGraph, CrewAI) are converging on common problems: agent communication (message passing, shared state, task output chaining), workflow orchestration (state graphs, task sequences, conversation patterns, task loops), failure handling (retry policies, checkpointing, application-level try/except), and agent lifecycle management.

### ATOM-SOURCE-20260216-001-0007
**Lines**: 52-69
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.90

> The BEAM/OTP runtime provides built-in primitives for agent-like problems: Erlang processes for isolated state (since 1986), message passing for communication (since 1986), supervisor trees for workflow orchestration (since 1998), supervisor restart strategies for error recovery (since 1998), a global process registry for agent discovery (since 1998), process groups for event broadcasting (since 1998), ETS for state persistence (since 1998), and built-in distribution for distributed agents (since 1990).

## Praxis Hook (4)

### ATOM-SOURCE-20260216-001-0009
**Lines**: 79-84
**Context**: method / evidence
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> In Python, handling non-deterministic AI agent failures typically involves defensive coding with `try/except` blocks, retry logic, error state management, fallback chains, and exponential backoff for every LLM call, tool invocation, and API request.

### ATOM-SOURCE-20260216-001-0010
**Lines**: 91-94
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.20, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> The BEAM's "let it crash" philosophy for AI agents involves writing only the 'happy path' code and allowing processes to crash, with supervisors automatically detecting crashes and restarting processes in a clean state without affecting the rest of the system.

### ATOM-SOURCE-20260216-001-0012
**Lines**: 113-116
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.60, actionability=0.80, epistemic_stability=0.70

> With BEAM's supervision trees, developers don't need to predict every failure mode for AI agents; instead, they define recovery strategies (e.g., restart agent, restart with different parameters, restart conversation, give up after N attempts), and the runtime handles the rest.

### ATOM-SOURCE-20260216-001-0013
**Lines**: 121-122
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> Tribunal is an LLM evaluation framework for Elixir that integrates with ExUnit, allowing developers to test AI agent responses for faithfulness to context, absence of hallucination, and lack of bias.
