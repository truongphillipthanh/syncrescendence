# Extraction: SOURCE-20260205-025

**Source**: `SOURCE-20260205-x-thread-rryssf_-meta_amazon_deepmind_published_comprehensive.md`
**Atoms extracted**: 15
**Categories**: analogy, claim, concept, framework

---

## Analogy (1)

### ATOM-SOURCE-20260205-025-0015
**Lines**: 109-111
**Context**: anecdote / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.30, epistemic_stability=0.70

> The survey provides a 'map' of agentic reasoning, while failure data provides the 'territory,' and they are not the same.

## Claim (11)

### ATOM-SOURCE-20260205-025-0002
**Lines**: 32-34
**Context**: anecdote / evidence
**Tension**: novelty=0.40, consensus_pressure=0.30, contradiction_load=0.20, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> Multi-agent LLM systems fail 41-86.7% of the time in production, not due to edge cases or adversarial attacks, but in standard deployment across 7 state-of-the-art frameworks.

### ATOM-SOURCE-20260205-025-0003
**Lines**: 36-39
**Context**: anecdote / evidence
**Tension**: novelty=0.40, consensus_pressure=0.30, contradiction_load=0.20, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> Berkeley researchers analyzed 1,642 execution traces of multi-agent LLM systems and identified 14 unique failure modes, with most failures stemming from system design and coordination issues.

### ATOM-SOURCE-20260205-025-0005
**Lines**: 48-51
**Context**: anecdote / evidence
**Tension**: novelty=0.50, consensus_pressure=0.30, contradiction_load=0.20, speculation_risk=0.30, actionability=0.60, epistemic_stability=0.50

> Agents achieving 60% pass@1 on benchmarks may only exhibit 25% consistency across multiple trials, indicating that benchmark performance does not equate to production reliability.

### ATOM-SOURCE-20260205-025-0006
**Lines**: 58-59
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.30, actionability=0.60, epistemic_stability=0.50

> If a benchmark reports 90% accuracy for LLM agents, expect 70-80% in production when accounting for consistency and faults.

### ATOM-SOURCE-20260205-025-0007
**Lines**: 61-63
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.50, epistemic_stability=0.70

> Simpler LLM agent architectures often outperform complex ones under realistic conditions because additional complexity introduces failure modes that outweigh the benefits.

### ATOM-SOURCE-20260205-025-0008
**Lines**: 72-76
**Context**: anecdote / evidence
**Tension**: novelty=0.40, consensus_pressure=0.30, contradiction_load=0.20, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> The 14 failure modes identified by Berkeley researchers for multi-agent LLM systems cluster into three categories: system design issues (~44% of failures), inter-agent misalignment (~32% of failures), and task verification failures (~24% of failures).

### ATOM-SOURCE-20260205-025-0009
**Lines**: 78-78
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.60

> Most failures in multi-agent LLM systems are not due to model limitations but rather coordination issues.

### ATOM-SOURCE-20260205-025-0010
**Lines**: 82-86
**Context**: rebuttal / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.40, speculation_risk=0.30, actionability=0.50, epistemic_stability=0.50

> The 'open challenges' listed in the survey, such as personalization, long-horizon interaction, world modeling, scalable multi-agent training, and governance for deployment, are not future problems but current, fundamental gaps.

### ATOM-SOURCE-20260205-025-0012
**Lines**: 91-93
**Context**: rebuttal / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.40, speculation_risk=0.30, actionability=0.70, epistemic_stability=0.50

> Techniques for agentic reasoning in LLMs that work on benchmarks often fail 41-86% of the time in production due to fundamental gaps in reliability and coordination.

### ATOM-SOURCE-20260205-025-0013
**Lines**: 102-105
**Context**: consensus / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.30, actionability=0.60, epistemic_stability=0.50

> The gap between benchmark accuracy (60-90%) and production consistency (25-70%) or multi-agent failure rates (41-86.7%) for LLM agents is fundamental, not incremental.

### ATOM-SOURCE-20260205-025-0014
**Lines**: 107-107
**Context**: consensus / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.30, actionability=0.60, epistemic_stability=0.50

> LLM agents are currently research projects, not production infrastructure.

## Concept (1)

### ATOM-SOURCE-20260205-025-0011
**Lines**: 88-88
**Context**: hypothesis / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.40, speculation_risk=0.30, actionability=0.40, epistemic_stability=0.50

> 'Long-horizon interaction' is a euphemism for agents losing coherence after a few steps.

## Framework (2)

### ATOM-SOURCE-20260205-025-0001
**Lines**: 18-21
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Agentic reasoning for LLMs can be organized into foundational agentic reasoning (planning, tool use, search), self-evolving agents (feedback, memory, adaptation), and multi-agent systems (coordination, knowledge sharing).

### ATOM-SOURCE-20260205-025-0004
**Lines**: 43-46
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> The survey distinguishes two approaches to agentic reasoning: in-context reasoning (scales test-time interaction without changing weights) and post-training (optimizes via reinforcement learning).
