# Extraction: SOURCE-20260210-002

**Source**: `SOURCE-20260210-x-article-mastra-observational_memory_a_human_inspired_memory_system_for_ai_agents.md`
**Atoms extracted**: 20
**Categories**: analogy, claim, concept, framework, praxis_hook, prediction

---

## Analogy (1)

### ATOM-SOURCE-20260210-002-0004
**Lines**: 15-16
**Context**: consensus / evidence
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> The human brain processes millions of pixels but distills them into one or two observations, similar to how observational memory compresses context.

## Claim (11)

### ATOM-SOURCE-20260210-002-0002
**Lines**: 8-8
**Context**: consensus / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> Observational memory is state-of-the-art (SoTA) on benchmarks like LongMemEval and is compatible with prompt caching mechanisms from providers like Anthropic and OpenAI.

### ATOM-SOURCE-20260210-002-0006
**Lines**: 30-30
**Context**: consensus / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> Text is a universal interface, easier to use, optimized for LLMs, and simpler to debug compared to structured objects like knowledge graphs.

### ATOM-SOURCE-20260210-002-0010
**Lines**: 54-57
**Context**: consensus / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> Observational memory's structure enables consistent prompt caching: full cache hits occur until the raw message threshold is met, and partial cache hits occur during observation runs because the observation prefix remains consistent.

### ATOM-SOURCE-20260210-002-0011
**Lines**: 61-63
**Context**: consensus / evidence
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Mastra's Observational Memory achieved 94.87% on LongMemEval with gpt-5-mini, exceeding previous scores by over 3 points, and 84.23% with gpt-4o, beating the gpt-4o oracle by 2 points and Supermemory's gpt-4o SOTA by 2.6 points.

### ATOM-SOURCE-20260210-002-0012
**Lines**: 65-65
**Context**: consensus / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.60, actionability=0.70, epistemic_stability=0.70

> These benchmark scores were achieved with a completely stable, predictable, reproducible, and fully prompt-cacheable context window.

### ATOM-SOURCE-20260210-002-0013
**Lines**: 78-79
**Context**: rebuttal / limitation
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.30, speculation_risk=0.20, actionability=0.40, epistemic_stability=0.60

> EmergenceMem's reported 86.00% score for an 'Internal' configuration is not publicly reproducible, and both EmergenceMem and Hindsight use multi-stage retrieval and neural reranking, unlike OM's single-pass stable context window.

### ATOM-SOURCE-20260210-002-0014
**Lines**: 84-84
**Context**: anecdote / evidence
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.60

> Mastra previously shipped working memory and semantic recall systems in March and April, before 'context engineering' became a recognized concept.

### ATOM-SOURCE-20260210-002-0015
**Lines**: 86-86
**Context**: anecdote / evidence
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.60

> Working memory provided moderate, cacheable benchmark improvements, while semantic recall offered larger but non-cacheable improvements.

### ATOM-SOURCE-20260210-002-0016
**Lines**: 88-94
**Context**: consensus / evidence
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> The need for aggressive caching to reduce token costs and the explosion of context windows from tool call results and parallelizable agents (e.g., browser, coding, research agents) highlighted the problem observational memory addresses.

### ATOM-SOURCE-20260210-002-0017
**Lines**: 96-97
**Context**: consensus / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Observational memory is considered the new primary Mastra memory system, combining aspects of working memory and semantic recall, and users are encouraged to migrate to it.

### ATOM-SOURCE-20260210-002-0018
**Lines**: 100-100
**Context**: consensus / limitation
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.60

> A current limitation of observational memory is that observation runs synchronously, blocking the conversation when the token threshold is hit.

## Concept (1)

### ATOM-SOURCE-20260210-002-0001
**Lines**: 6-6
**Context**: consensus / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.60

> Observational memory is a text-based memory system for agentic AI systems that compresses context into discrete observations, designed to mimic human cognitive distillation.

## Framework (2)

### ATOM-SOURCE-20260210-002-0005
**Lines**: 28-37
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Observational memory uses a log-based message format characterized by formatted text (not structured objects), a three-date model for temporal reasoning (observation, referenced, and relative dates), and emoji-based prioritization (🔴 for important, 🟡 for maybe important, 🟢 for info only).

### ATOM-SOURCE-20260210-002-0007
**Lines**: 41-43
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> In observational memory, the context window is divided into two blocks: a list of observations and raw messages not yet compressed. New messages append to the raw message block.

## Praxis Hook (4)

### ATOM-SOURCE-20260210-002-0003
**Lines**: 10-10
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Mastra's implementation of observational memory is open-source.

### ATOM-SOURCE-20260210-002-0008
**Lines**: 45-46
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> When the raw message block hits a default threshold of 30k tokens, a separate 'observer agent' compresses these messages into new observations, which are appended to the observation block.

### ATOM-SOURCE-20260210-002-0009
**Lines**: 48-49
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> When the observation block hits a default threshold of 40k tokens, a separate 'reflector agent' garbage collects irrelevant observations.

### ATOM-SOURCE-20260210-002-0020
**Lines**: 105-109
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To use Mastra's observational memory, import `Memory` and `Agent` from `@mastra/memory` and `@mastra/core/agent` respectively, then instantiate `Agent` with `observationalMemory: true` in the memory options.

## Prediction (1)

### ATOM-SOURCE-20260210-002-0019
**Lines**: 101-101
**Context**: speculation / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.80, actionability=0.70, epistemic_stability=0.50

> Mastra is shipping an async background buffering mode this week that will run observation outside the conversation loop, solving the synchronous blocking issue.
