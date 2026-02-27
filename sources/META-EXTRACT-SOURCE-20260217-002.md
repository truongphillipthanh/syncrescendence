# Extraction: SOURCE-20260217-002

**Source**: `SOURCE-20260217-x-article-ashpreetbedi-the_programming_language_for_agentic_software.md`
**Atoms extracted**: 14
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (6)

### ATOM-SOURCE-20260217-002-0001
**Lines**: 4-7
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.10, epistemic_stability=0.90

> Every era of computing develops its own programming language, with each new language emerging because the previous generation could no longer clearly express the new abstraction.

### ATOM-SOURCE-20260217-002-0002
**Lines**: 8-8
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.20, actionability=0.10, epistemic_stability=0.80

> We are currently in the agentic era of computing.

### ATOM-SOURCE-20260217-002-0004
**Lines**: 12-12
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.10, epistemic_stability=0.90

> When the fundamental contract of software changes, the programming language used for it must also change.

### ATOM-SOURCE-20260217-002-0008
**Lines**: 40-42
**Context**: consensus / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.20, epistemic_stability=0.70

> Agentic software breaks the traditional software contract of 'Same input, same output' because its execution is dynamic.

### ATOM-SOURCE-20260217-002-0009
**Lines**: 44-46
**Context**: hypothesis / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.30, actionability=0.20, epistemic_stability=0.60

> Agentic software requires a new programming language that natively expresses dynamic execution and incorporates at least three new core capabilities: a new interaction model, a new governance model, and a new trust model.

### ATOM-SOURCE-20260217-002-0014
**Lines**: 84-87
**Context**: consensus / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.20, epistemic_stability=0.70

> The agentic era introduces a new abstraction: systems that reason, remember, and decide at runtime, which necessitates a change in programming language because the contract, primitives, and execution model have all changed.

## Concept (5)

### ATOM-SOURCE-20260217-002-0003
**Lines**: 9-11
**Context**: hypothesis / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.30, actionability=0.20, epistemic_stability=0.60

> In the agentic era, software is characterized by reasoning over context, calling tools, learning from past runs, and making decisions at runtime, rather than merely executing instructions.

### ATOM-SOURCE-20260217-002-0007
**Lines**: 34-37
**Context**: hypothesis / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.30, actionability=0.20, epistemic_stability=0.60

> Agents are a new form of program where the path between input and output is not predetermined, as an agent reasons over context, chooses tools dynamically, looks up data, retrieves memory, and decides its path at runtime.

### ATOM-SOURCE-20260217-002-0010
**Lines**: 47-51
**Context**: hypothesis / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.40, actionability=0.30, epistemic_stability=0.50

> The new interaction model for agentic software involves streaming reasoning, tool calls, intermediate results, and real-time pivots, where the execution path can change mid-run, and streaming and iteration are first-class behaviors.

### ATOM-SOURCE-20260217-002-0011
**Lines**: 52-58
**Context**: hypothesis / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.40, actionability=0.30, epistemic_stability=0.50

> The new governance model for agentic software requires that decision-making authority be part of the agent definition itself, distinguishing between low-risk actions (e.g., summarizing text) and high-risk actions (e.g., issuing refunds) that may require user approval or higher authority.

### ATOM-SOURCE-20260217-002-0012
**Lines**: 59-63
**Context**: hypothesis / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.40, actionability=0.30, epistemic_stability=0.50

> The new trust model for agentic software must be engineered differently due to probabilistic reasoning in execution paths, necessitating guardrails, evaluation, logging, and post-response checks built into the runtime semantics.

## Framework (2)

### ATOM-SOURCE-20260217-002-0005
**Lines**: 15-19
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.10, epistemic_stability=0.90

> A programming language is fundamentally composed of three elements: primitives for thinking and building, an engine to execute those primitives, and a runtime that governs memory, I/O, permissions, and external interaction.

### ATOM-SOURCE-20260217-002-0006
**Lines**: 24-30
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.50

> For agentic systems, Agno provides agents, teams, workflows, memory, knowledge, tools, guardrails, and approval flows as primitives; an engine that runs model calls, tool execution, and context management; and AgentOS as a production runtime enforcing streaming, authentication, session isolation, monitoring, and background execution.

## Praxis Hook (1)

### ATOM-SOURCE-20260217-002-0013
**Lines**: 66-80
**Context**: method / evidence
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> Agno allows defining an agent (Gcode) with explicit configurations for knowledge (searchable long-term memory), learning (agent-extracted learnings), tools (sandboxed operations), memory (user preferences), and historical context (past runs), which are treated as first-class primitives and built-in capabilities.
