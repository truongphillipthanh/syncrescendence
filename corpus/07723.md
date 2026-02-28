# Extraction: SOURCE-20260216-010

**Source**: `SOURCE-20260216-x-article-ksimback-how_to_reduce_openclaw_model_costs_by_up_to_90_percent_full_guide.md`
**Atoms extracted**: 14
**Categories**: claim, concept, framework, praxis_hook, prediction

---

## Claim (4)

### ATOM-SOURCE-20260216-010-0001
**Lines**: 17-18
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Running OpenClaw with a single frontier model for all tasks is the primary reason users incur high costs.

### ATOM-SOURCE-20260216-010-0002
**Lines**: 20-25
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> OpenClaw's default behavior of sending all tasks, including heartbeats, sub-agent tasks, simple calendar lookups, and web searches, to the primary model leads to excessive costs.

### ATOM-SOURCE-20260216-010-0003
**Lines**: 28-40
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> OpenClaw's architecture compounds costs through context accumulation, system prompt re-injection, tool output storage, heartbeat overhead, and cron job overhead.

### ATOM-SOURCE-20260216-010-0005
**Lines**: 45-47
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> Using a Claude Max Plan with OpenClaw is against Anthropic's terms of service, and users have reported being banned for it.

## Concept (2)

### ATOM-SOURCE-20260216-010-0010
**Lines**: 93-103
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> ClawRouter is an OpenClaw-native intermediary layer that analyzes incoming queries locally using a lightweight classifier based on weighted scoring dimensions (e.g., query length, code presence, reasoning markers, multi-step intent, tool usage signals) to classify requests into complexity tiers.

### ATOM-SOURCE-20260216-010-0013
**Lines**: 116-124
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Prompt caching allows LLM providers to remember static parts of a prompt (like OpenClaw's SOUL.md, AGENTS.md, MEMORY.md, and system instructions) and reuse them across calls, significantly reducing costs for subsequent requests within the cache's Time-To-Live (TTL).

## Framework (3)

### ATOM-SOURCE-20260216-010-0008
**Lines**: 66-69
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> A simple framework for optimizing OpenClaw costs involves categorizing tasks into four tiers: Heartbeat/Status (e.g., Gemini Flash-Lite), Simple Queries (e.g., Haiku 4.5), Standard Work (e.g., Sonnet 4.5), and Complex Reasoning (e.g., Opus 4.6), and assigning models based on their cost profile and capability.

### ATOM-SOURCE-20260216-010-0009
**Lines**: 75-89
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> OpenRouter's built-in routing uses prompt analysis to automatically select models based on auto-detected tasks (e.g., 'routine', 'coding'), allowing configuration of specific models and maximum costs per task, with a fallback model.

### ATOM-SOURCE-20260216-010-0011
**Lines**: 103-109
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> ClawRouter classifies requests into complexity tiers: 'Simple' for cheap/fast models, 'Medium' for mid-tier, 'Complex' for strong models, and 'Heavy reasoning/agentic/multi-step' for frontier models, routing to the cheapest capable model for each level.

## Praxis Hook (4)

### ATOM-SOURCE-20260216-010-0006
**Lines**: 52-69
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To implement custom model routing in OpenClaw, define a `RouterSkill` with a `rules` dictionary mapping regex patterns in prompts to specific LLM models, then enable the skill.

### ATOM-SOURCE-20260216-010-0007
**Lines**: 63-64
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> To optimize model routing in OpenClaw, match model capability to task complexity using OpenClaw's per-function model assignment.

### ATOM-SOURCE-20260216-010-0012
**Lines**: 110-112
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> ClawRouter supports multiple profiles: Auto (balanced), Eco (max savings, up to 95–100% on simple queries), Premium (best quality), and Free (zero-cost models).

### ATOM-SOURCE-20260216-010-0014
**Lines**: 125-131
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To enable prompt caching for an LLM in OpenClaw, configure `cacheRetention` (e.g., 'long'), `cacheSystemPrompts: true`, and `cacheThresholdTokens` (e.g., 2048) in the model's configuration.

## Prediction (1)

### ATOM-SOURCE-20260216-010-0004
**Lines**: 41-42
**Context**: speculation / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.60, actionability=0.80, epistemic_stability=0.70

> A well-configured multi-model setup can reduce monthly API costs by up to 90% while maintaining or improving output quality.
