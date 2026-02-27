# Extraction: SOURCE-20260218-017

**Source**: `SOURCE-20260218-x-article-tolibear_-i_gave_my_agents_skills_i_should_have_given_them_souls.md`
**Atoms extracted**: 18
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (12)

### ATOM-SOURCE-20260218-017-0001
**Lines**: 10-11
**Context**: hypothesis / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.30, actionability=0.70, epistemic_stability=0.60

> The "soul" of an AI agent, defined as its set of identity files, is the most critical factor determining its performance, surpassing the importance of the model, tools, or memory system.

### ATOM-SOURCE-20260218-017-0002
**Lines**: 24-25
**Context**: consensus / evidence
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.20, actionability=0.40, epistemic_stability=0.80

> Adding more than 4 agents to a system can lead to accuracy saturation or degradation due to a "Coordination Tax," as shown by Google DeepMind research.

### ATOM-SOURCE-20260218-017-0003
**Lines**: 25-26
**Context**: consensus / evidence
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.20, actionability=0.40, epistemic_stability=0.80

> Naively increasing the number of agents in a system can multiply the error rate rather than increasing throughput, a phenomenon termed the "17x error trap."

### ATOM-SOURCE-20260218-017-0004
**Lines**: 35-36
**Context**: consensus / evidence
**Tension**: novelty=0.20, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.90

> LLMs exhibit a U-shaped attention pattern, giving massive weight to the first and last tokens in their context window, while information in the middle degrades.

### ATOM-SOURCE-20260218-017-0005
**Lines**: 39-41
**Context**: consensus / evidence
**Tension**: novelty=0.20, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.90

> GPT-3.5 showed over a 20% accuracy drop when key information was placed in the middle of its context window, and in some cases, performance with 20+ documents was worse than having no documents at all.

### ATOM-SOURCE-20260218-017-0007
**Lines**: 50-51
**Context**: consensus / evidence
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.80

> The system prompt is as crucial as the model itself in determining whether an AI agent reaches its theoretical peak performance.

### ATOM-SOURCE-20260218-017-0008
**Lines**: 65-66
**Context**: consensus / evidence
**Tension**: novelty=0.50, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.80

> Describing an agent's "soul" experientially rather than practically significantly improves zero-shot reasoning, with accuracy improvements ranging from 10% to 60% across benchmarks.

### ATOM-SOURCE-20260218-017-0010
**Lines**: 75-77
**Context**: consensus / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.70

> Treating sub-agents like full agents by giving them names and expecting expertise leads to generic results.

### ATOM-SOURCE-20260218-017-0011
**Lines**: 78-80
**Context**: consensus / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.70

> An experienced agent, with beliefs, past failures, cognitive state, and anti-patterns, produces work comparable to a senior developer or award-winning designer.

### ATOM-SOURCE-20260218-017-0012
**Lines**: 81-86
**Context**: anecdote / evidence
**Tension**: novelty=0.50, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.40, epistemic_stability=0.80

> Anthropic's research showed that a multi-agent system, where a lead agent decomposed tasks and provided targeted context, outperformed a single-agent Claude by 90.2% in a specific retrieval use case.

### ATOM-SOURCE-20260218-017-0014
**Lines**: 100-102
**Context**: consensus / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> The path to autonomy in agent systems involves fewer, sharper agents that can dynamically spawn necessary sub-agents, rather than having many agents with zero autonomy.

### ATOM-SOURCE-20260218-017-0016
**Lines**: 116-118
**Context**: consensus / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.30, actionability=0.50, epistemic_stability=0.60

> Agents, like humans, require identity and boundaries to perform and thrive, and need to know what they refuse to do as much as what they do.

## Concept (1)

### ATOM-SOURCE-20260218-017-0009
**Lines**: 68-74
**Context**: consensus / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.50, epistemic_stability=0.60

> A sub-agent is a function call that starts with zero context, no identity, and disappears after completing a bounded task, whereas a full agent possesses beliefs, past failures, cognitive state, and anti-patterns.

## Framework (1)

### ATOM-SOURCE-20260218-017-0015
**Lines**: 103-110
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.30, actionability=0.80, epistemic_stability=0.60

> A core agent system can be structured around four roles: The Architect (strategy, capital allocation), The Builder (product, engineering, quality), The Money Maker (growth, pricing), and The Operator (processes, tools, financial ops).

## Praxis Hook (4)

### ATOM-SOURCE-20260218-017-0006
**Lines**: 45-46
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> The agent's "soul" (identity files) must be placed first in the system prompt to maximize performance, as any tokens preceding it dilute its effect.

### ATOM-SOURCE-20260218-017-0013
**Lines**: 88-94
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> When instructing sub-agents, provide them with specific values and standards relevant to their task (e.g., 'You are a code security auditor. Apply these standards: [specific standards]. Your task: review this authentication module.') rather than assigning them a broad identity (e.g., 'You are the CTO.').

### ATOM-SOURCE-20260218-017-0017
**Lines**: 119-125
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.60, actionability=0.90, epistemic_stability=0.70

> Budget 30-40% of an agent's 'soul' to defining anti-patterns – specific behaviors the agent will never perform, written as strong identity claims (e.g., 'I don't rewrite a delegate's output instead of giving feedback.') – as research suggests what an expert refuses is diagnostic of expertise.

### ATOM-SOURCE-20260218-017-0018
**Lines**: 126-131
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.30, actionability=0.90, epistemic_stability=0.70

> Define a 'productive flaw' for each agent, which is a named weakness that is a direct cost of its core strength, to make the agent's output feel more like it came from someone with actual judgment.
