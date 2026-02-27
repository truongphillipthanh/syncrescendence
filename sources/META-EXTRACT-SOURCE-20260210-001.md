# Extraction: SOURCE-20260210-001

**Source**: `SOURCE-20260210-website-article-dbreunig-how_system_prompts_define_agent.md`
**Atoms extracted**: 13
**Categories**: claim, concept, praxis_hook

---

## Claim (10)

### ATOM-SOURCE-20260210-001-0001
**Lines**: 9-12
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> A system prompt is a critical part of an AI agent's harness, providing baseline instructions that are present in every call to the model, defining core behaviors, strategies, and tone.

### ATOM-SOURCE-20260210-001-0002
**Lines**: 19-20
**Context**: hypothesis / claim
**Tension**: novelty=0.30, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.30, epistemic_stability=0.70

> System prompts matter significantly more than commonly assumed in determining an AI agent's effectiveness.

### ATOM-SOURCE-20260210-001-0003
**Lines**: 20-21
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.40, epistemic_stability=0.80

> While the AI model sets the theoretical performance ceiling for an agent, the system prompt dictates whether that peak performance is achieved.

### ATOM-SOURCE-20260210-001-0005
**Lines**: 29-33
**Context**: consensus / evidence
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> System prompts for CLI coding agents like Claude Code, Cursor, Gemini CLI, Codex CLI, OpenHands, and Kimi CLI, despite performing similar basic functions, exhibit significant variety in their structure and content.

### ATOM-SOURCE-20260210-001-0006
**Lines**: 36-44
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> System prompts for AI coding agents consistently instruct models to add comments sparingly and avoid conversational comments, reflecting a common problem in existing codebases.

### ATOM-SOURCE-20260210-001-0007
**Lines**: 44-46
**Context**: anecdote / evidence
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.20, speculation_risk=0.30, actionability=0.10, epistemic_stability=0.60

> AI models like Opus 4.5 have been observed to reason within code comments if their 'thinking' process is disabled, indicating an inherent tendency that system prompts must counteract.

### ATOM-SOURCE-20260210-001-0008
**Lines**: 47-57
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.20, actionability=0.30, epistemic_stability=0.70

> System prompts for AI coding agents frequently emphasize the use of parallel tool calls, overriding the models' likely serial reasoning patterns developed during training, to improve user experience speed.

### ATOM-SOURCE-20260210-001-0010
**Lines**: 62-64
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.70

> While many system prompt specifications are shared across different AI coding agents, their differences significantly impact application behavior.

### ATOM-SOURCE-20260210-001-0012
**Lines**: 71-73
**Context**: anecdote / evidence
**Tension**: novelty=0.40, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.30, epistemic_stability=0.60

> Testing two OpenCode agents running Opus 4.5 with different system prompts (Claude Code vs. Codex) on SWE-Bench Pro questions revealed immediate and significant divergence in their workflows.

### ATOM-SOURCE-20260210-001-0013
**Lines**: 80-82
**Context**: anecdote / evidence
**Tension**: novelty=0.40, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> The Codex prompt led to a methodical, documentation-first approach, while the Claude prompt resulted in an iterative, test-driven strategy for solving SWE-Bench problems.

## Concept (1)

### ATOM-SOURCE-20260210-001-0009
**Lines**: 58-61
**Context**: hypothesis / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.30, epistemic_stability=0.60

> The concept of 'fighting the weights' describes how system prompts are used to mitigate inherent quirks or biases of AI models, acquired during training, to enhance user experience in agentic applications.

## Praxis Hook (2)

### ATOM-SOURCE-20260210-001-0004
**Lines**: 22-25
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> To analyze system prompt effectiveness, one can obtain and analyze system prompts from various agents, semantically cluster them, compare their instructions, swap prompts between agents, and observe behavioral changes.

### ATOM-SOURCE-20260210-001-0011
**Lines**: 68-70
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.60

> OpenCode allows users to customize system prompts, enabling experimentation with different instructions (e.g., from Kimi, Gemini, Codex) to measure their impact on agent behavior.
