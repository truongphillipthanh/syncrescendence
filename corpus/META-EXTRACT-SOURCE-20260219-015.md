# Extraction: SOURCE-20260219-015

**Source**: `SOURCE-20260219-x-article-trq212-lessons_from_building_claude_code_prompt_caching_is_everything.md`
**Atoms extracted**: 12
**Categories**: claim, praxis_hook

---

## Claim (3)

### ATOM-SOURCE-20260219-015-0001
**Lines**: 3-5
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> Prompt caching is essential for making long-running agentic products like Claude Code feasible, as it reuses computation from previous interactions, reducing latency and cost.

### ATOM-SOURCE-20260219-015-0002
**Lines**: 14-16
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.90

> Prompt caching operates on prefix matching, meaning the order of elements in a prompt significantly impacts cache effectiveness; any change in the prefix invalidates subsequent cached content.

### ATOM-SOURCE-20260219-015-0005
**Lines**: 35-38
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Prompt caches are model-specific, making the economics of switching models mid-session counter-intuitive; rebuilding a cache for a new model can be more expensive than continuing with the current one, even for simpler tasks.

## Praxis Hook (9)

### ATOM-SOURCE-20260219-015-0003
**Lines**: 16-23
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To maximize prompt cache hit rates and reduce costs, design your prompt layout with static content first and dynamic content last. For Claude Code, this means ordering: Static system prompt & Tools (globally cached), Claude.MD (cached per project), Session context (cached per session), and finally Conversation messages.

### ATOM-SOURCE-20260219-015-0004
**Lines**: 28-32
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.60, actionability=0.90, epistemic_stability=0.70

> Instead of updating the system prompt with new information (e.g., time changes, file updates), which causes a cache miss, pass this information via messages in the next turn. Claude Code uses a `<system-reminder>` tag in user messages or tool results for this purpose.

### ATOM-SOURCE-20260219-015-0006
**Lines**: 39-42
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> If model switching is necessary mid-session, use subagents where the initial model prepares a 'handoff' message for another model to complete the task, as exemplified by Claude Code's Explore agents using Haiku.

### ATOM-SOURCE-20260219-015-0007
**Lines**: 44-45
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Avoid adding or removing tools mid-conversation, as tools are part of the cached prefix, and such changes invalidate the cache for the entire conversation.

### ATOM-SOURCE-20260219-015-0008
**Lines**: 44-45
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> When designing systems that use prompt caching, ensure the entire system is built around the constraint that any change in the prefix invalidates everything after it, and prioritize correct ordering for optimal caching.

### ATOM-SOURCE-20260219-015-0009
**Lines**: 46-46
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> To maintain prompt cache efficiency, use messages to convey changes like entering plan mode or updating dates within a conversation, rather than modifying the system prompt.

### ATOM-SOURCE-20260219-015-0010
**Lines**: 47-47
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Avoid changing tools or models mid-conversation; instead, use tools to model state transitions (e.g., plan mode) and defer tool loading rather than removing tools.

### ATOM-SOURCE-20260219-015-0011
**Lines**: 48-48
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Monitor your cache hit rate as diligently as uptime, treating cache breaks as incidents, because even small cache miss rates can significantly impact cost and latency.

### ATOM-SOURCE-20260219-015-0012
**Lines**: 49-49
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> When performing side computations (e.g., compaction, summarization, skill execution) that fork from a parent operation, use identical cache-safe parameters to ensure cache hits on the parent's prefix.
