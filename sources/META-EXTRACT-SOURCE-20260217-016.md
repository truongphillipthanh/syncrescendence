# Extraction: SOURCE-20260217-016

**Source**: `SOURCE-20260217-x-article-vtrivedy10-improving_deep_agents_with_harness_engineering.md`
**Atoms extracted**: 19
**Categories**: analogy, claim, concept, framework, praxis_hook

---

## Analogy (1)

### ATOM-SOURCE-20260217-016-0007
**Lines**: 44-45
**Context**: consensus / evidence
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.30, epistemic_stability=0.70

> The Trace Analyzer Skill's approach of focusing on mistakes from previous runs to make improvements is similar to 'boosting' in machine learning.

## Claim (10)

### ATOM-SOURCE-20260217-016-0001
**Lines**: 4-5
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> Harness engineering improved a coding agent's performance from Top 30 to Top 5 on Terminal Bench 2.0 by solely changing the harness, not the underlying model.

### ATOM-SOURCE-20260217-016-0004
**Lines**: 18-20
**Context**: consensus / evidence
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> The deepagents-cli coding agent improved by 13.7 points (from 52.8% to 66.5%) on Terminal Bench 2.0 by only tweaking its harness, while keeping the gpt-5.2-codex model fixed.

### ATOM-SOURCE-20260217-016-0009
**Lines**: 48-49
**Context**: consensus / evidence
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> Automated trace analysis saves significant time and facilitates rapid experimentation for agent improvement.

### ATOM-SOURCE-20260217-016-0010
**Lines**: 52-53
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> Agents perform better when they have more knowledge about their environment, constraints, and evaluation criteria, enabling them to self-direct their work autonomously.

### ATOM-SOURCE-20260217-016-0012
**Lines**: 57-58
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.40, epistemic_stability=0.70

> Agents can become myopic and enter 'doom loops' where they make small variations to the same broken approach repeatedly.

### ATOM-SOURCE-20260217-016-0014
**Lines**: 63-65
**Context**: consensus / limitation
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.50, epistemic_stability=0.70

> Guardrails and design heuristics, like LoopDetectionMiddleware, are currently necessary to help agents execute correctly and autonomously due to perceived model issues, but may become unnecessary as models improve.

### ATOM-SOURCE-20260217-016-0015
**Lines**: 68-69
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.50, epistemic_stability=0.70

> Optimizing reasoning compute spend is beneficial for most subtasks, even though the maximum reasoning budget can be used for every task.

### ATOM-SOURCE-20260217-016-0016
**Lines**: 71-71
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.50, epistemic_stability=0.70

> More reasoning helps agents evaluate each step, but can burn over 2x more tokens/time, creating a tradeoff with terminal bench timeout limits.

### ATOM-SOURCE-20260217-016-0017
**Lines**: 73-75
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.50, epistemic_stability=0.70

> Reasoning is beneficial for planning to fully understand difficult problems and for later-stage verification to catch mistakes and submit solutions.

### ATOM-SOURCE-20260217-016-0019
**Lines**: 80-81
**Context**: anecdote / evidence
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.30, epistemic_stability=0.70

> Running agents only at xhigh reasoning scored poorly (53.9%) due to timeouts compared to 63.6% at high reasoning, while a 'reasoning sandwich' approach achieved 66.5%.

## Concept (2)

### ATOM-SOURCE-20260217-016-0002
**Lines**: 9-11
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.60

> Harness Engineering involves building tooling around a model to optimize goals like task performance, token efficiency, and latency, by making design decisions about the system prompt, tool choice, and execution flow.

### ATOM-SOURCE-20260217-016-0011
**Lines**: 54-54
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> The purpose of a harness engineer is to prepare and deliver context to agents so they can autonomously complete work.

## Framework (2)

### ATOM-SOURCE-20260217-016-0005
**Lines**: 33-35
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.60

> Key 'knobs' for optimizing an agent harness include the System Prompt, Tools, and Middleware (hooks around model and tool calls).

### ATOM-SOURCE-20260217-016-0018
**Lines**: 76-77
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.60

> A 'reasoning sandwich' heuristic for compute allocation involves using xhigh reasoning for planning and understanding (first 25% of budget), high reasoning for building and iterating (middle 50%), and xhigh reasoning for final verification (last 25%).

## Praxis Hook (4)

### ATOM-SOURCE-20260217-016-0003
**Lines**: 14-17
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> To improve agents, use traces (e.g., LangChain Traces) to understand agent failure modes at scale by observing inputs and outputs in text space, which then informs improvement loops.

### ATOM-SOURCE-20260217-016-0006
**Lines**: 40-43
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> A 'Trace Analyzer Skill' can be used to iteratively improve an agent's harness by: 1) fetching experiment traces, 2) spawning parallel error analysis agents to synthesize findings, and 3) aggregating feedback to make targeted harness changes.

### ATOM-SOURCE-20260217-016-0008
**Lines**: 47-51
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> To improve agent performance in environments where time is a constraint, inject time budget warnings to encourage agents to finish work and shift to verification, as agents are typically poor at time estimation.

### ATOM-SOURCE-20260217-016-0013
**Lines**: 59-61
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.60

> Implement a LoopDetectionMiddleware that tracks per-file edit counts via tool call hooks and adds context like '…consider reconsidering your approach' after N edits to the same file to help agents recover from 'doom loops'.
