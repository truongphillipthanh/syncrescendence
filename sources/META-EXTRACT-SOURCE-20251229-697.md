# Extraction: SOURCE-20251229-697

**Source**: `SOURCE-20251229-youtube-tutorial-ai_engineer-jack_morris_stuffing_context_is_not_memory_updating_weights.md`
**Atoms extracted**: 8
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (5)

### ATOM-SOURCE-20251229-697-0001
**Lines**: 19-21
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Current Large Language Models (LLMs) struggle with niche, "long-tail" knowledge that falls outside their training data or within knowledge cutoffs.

### ATOM-SOURCE-20251229-697-0004
**Lines**: 40-41
**Context**: consensus / evidence
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.10, epistemic_stability=0.80

> The "Long Tail" Knowledge Problem arises because these niche tasks are either outside the LLM's training data, subject to knowledge cutoffs, or require private data.

### ATOM-SOURCE-20251229-697-0005
**Lines**: 42-43
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.10, epistemic_stability=0.90

> No amount of prompting or prompt engineering can force an LLM to know facts it does not have stored.

### ATOM-SOURCE-20251229-697-0007
**Lines**: 55-56
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.10, epistemic_stability=0.90

> The self-attention mechanism in Transformers has a quadratic compute cost because it requires every token to look at every other token.

### ATOM-SOURCE-20251229-697-0008
**Lines**: 57-59
**Context**: anecdote / evidence
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.40, epistemic_stability=0.70

> Increasing context length significantly impacts LLM output latency: 1,000 tokens of context allow 10,000 tokens per second output, while 128k tokens of context reduce output to 130 tokens per second.

## Concept (1)

### ATOM-SOURCE-20251229-697-0003
**Lines**: 36-39
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> The "Long Tail" Knowledge Problem refers to the critical failure mode in current LLMs where they excel at general knowledge but fail catastrophically at niche, specific tasks (e.g., optimizing an AMD GPU kernel or knowing terms of a specific partnership).

## Framework (1)

### ATOM-SOURCE-20251229-697-0006
**Lines**: 46-51
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.60

> There are three paradigms for knowledge injection into LLMs: Full Context (stuffing all relevant data into the prompt), RAG (Retrieval Augmented Generation, retrieving only relevant chunks), and Training into Weights (injecting knowledge directly into the model's parameters).

## Praxis Hook (1)

### ATOM-SOURCE-20251229-697-0002
**Lines**: 24-27
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.30, contradiction_load=0.20, speculation_risk=0.60, actionability=0.70, epistemic_stability=0.50

> A third paradigm for knowledge injection into LLMs, beyond massive context windows and Retrieval Augmented Generation (RAG), is "training things into weights," which involves efficiently injecting specific knowledge directly into model parameters.
