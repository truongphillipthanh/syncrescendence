# Extraction: SOURCE-20250612-001

**Source**: `SOURCE-20250612-website-article-cognition-dont-build-multi-agents.md`
**Atoms extracted**: 9
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (5)

### ATOM-SOURCE-20250612-001-0002
**Lines**: 15-19
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> React's success stems from its philosophy of reactivity and modularity, which became a standard requirement for web development.

### ATOM-SOURCE-20250612-001-0003
**Lines**: 23-27
**Context**: rebuttal / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.80, speculation_risk=0.40, actionability=0.60, epistemic_stability=0.50

> Current multi-agent architectures, such as those promoted by OpenAI's Swarm and Microsoft's AutoGen, are the wrong way to build agents for serious production applications.

### ATOM-SOURCE-20250612-001-0005
**Lines**: 41-46
**Context**: hypothesis / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.70, speculation_risk=0.50, actionability=0.60, epistemic_stability=0.50

> A common multi-agent architecture where a main agent breaks work into parts, starts subagents, and combines results is very fragile and prone to compounding errors due to miscommunication between subagents.

### ATOM-SOURCE-20250612-001-0007
**Lines**: 50-51
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.60, actionability=0.60, epistemic_stability=0.80

> Compressing history into key details allows agents to be effective at longer contexts, though they will still eventually hit a limit.

### ATOM-SOURCE-20250612-001-0009
**Lines**: 63-69
**Context**: anecdote / evidence
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.80

> As of June 2025, Claude Code uses subagents for tasks like answering questions, but these subagents do not work in parallel with the main agent and lack sufficient context to perform complex tasks like writing code, which helps manage context history for the main agent.

## Concept (1)

### ATOM-SOURCE-20250612-001-0004
**Lines**: 35-39
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.30, actionability=0.70, epistemic_stability=0.60

> Context Engineering is the process of automatically and dynamically writing tasks in the ideal format for an LLM chatbot, going beyond 'prompt engineering' by integrating this into a dynamic system.

## Framework (1)

### ATOM-SOURCE-20250612-001-0001
**Lines**: 10-12
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> The principles of Context Engineering are: 1. Share context, and 2. Actions carry implicit decisions.

## Praxis Hook (2)

### ATOM-SOURCE-20250612-001-0006
**Lines**: 44-49
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> To manage long contexts for LLM agents, compress action and conversation history into key details, events, and decisions. This requires investment to identify key information and create an effective system, potentially involving fine-tuning smaller models for specific domains.

### ATOM-SOURCE-20250612-001-0008
**Lines**: 55-59
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> Agent builders should ensure every agent action is informed by the context of all relevant decisions made by other parts of the system, ideally by having every action 'see everything else,' though practical tradeoffs due to limited context windows may necessitate deciding on an acceptable complexity level for desired reliability.
