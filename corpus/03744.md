# Extraction: SOURCE-20260207-013

**Source**: `SOURCE-20260207-x-article-rjs-shaping_0_1_with_claude_code.md`
**Atoms extracted**: 20
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (2)

### ATOM-SOURCE-20260207-013-0010
**Lines**: 91-94
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> A timezone library that is local and correctly handles DST rules eliminates the need to fetch timezone data from the internet on every load, as the data is accurate by design.

### ATOM-SOURCE-20260207-013-0020
**Lines**: 229-234
**Context**: anecdote / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.70

> Following a structured design process with an LLM, even for simple applications, provides a deeper understanding of the system's workings and rationale, facilitating future improvements and changes.

## Concept (6)

### ATOM-SOURCE-20260207-013-0002
**Lines**: 31-35
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.60

> The 'shaping skill' in Claude Code involves separating problem and solution to allow for iterative development, using terms like 'solution A' for different potential approaches.

### ATOM-SOURCE-20260207-013-0004
**Lines**: 54-64
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> In the context of Claude Code's shaping skill, 'R' refers to requirements, which are ideally general enough to apply to any solution, while 'A' refers to a specific solution shape, comprising high-level 'moving parts' or mechanics.

### ATOM-SOURCE-20260207-013-0006
**Lines**: 69-72
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> A 'fit check' in the shaping terminology used with Claude Code is a comparison between requirements (R) and a proposed solution shape (A) to identify what is solved, unsolved, known, and unknown.

### ATOM-SOURCE-20260207-013-0007
**Lines**: 69-72
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.70, epistemic_stability=0.90

> A 'spike' is an engineering term referring to an investigation into a question to gather concrete information about possibilities and implementation methods.

### ATOM-SOURCE-20260207-013-0015
**Lines**: 159-162
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.00, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.50

> A 'breadboard' is a technical diagram that combines UI and code into a single circuit-like representation, useful for visualizing and slicing larger projects into vertical slices.

### ATOM-SOURCE-20260207-013-0017
**Lines**: 185-185
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.70

> In the context of system design, 'affordances' refer to either UI affordances (actions a user can take) or code affordances (actions the system can perform).

## Framework (2)

### ATOM-SOURCE-20260207-013-0013
**Lines**: 137-140
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.60

> A concrete shape 'A' for an application can be broken down into parts such as: TUI shell, mechanism using zoneinfo, hour table builder, default config, LLM input handler with tool definitions, and tool executor with validation.

### ATOM-SOURCE-20260207-013-0018
**Lines**: 185-189
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> A system's wiring can be formally defined as a table of 'wire' relationships between the IDs of its affordances, enabling an LLM to slice the system by defining a slice as a subset of affordances while maintaining wiring integrity.

## Praxis Hook (10)

### ATOM-SOURCE-20260207-013-0001
**Lines**: 4-29
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To shape and build a small project from 0-1 using Claude Code, start by describing your vision in a new blank directory, then explicitly ask Claude to use its 'shaping skill' to capture requirements and separate problem from solution, using terminology like 'solution A' to allow for iteration.

### ATOM-SOURCE-20260207-013-0003
**Lines**: 43-64
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> When using Claude Code for project shaping, after the initial prompt, review the generated `shaping.md` document which includes a problem/outcome frame, extracted requirements (R), and an initial solution shape (A) with flagged unknowns.

### ATOM-SOURCE-20260207-013-0005
**Lines**: 66-72
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> To check the fit between requirements (R) and a solution shape (A) in Claude Code, use the shorthand 'show me R x A' to get a fit check table that indicates solved and unsolved parts, providing a jumping-off point for further iteration.

### ATOM-SOURCE-20260207-013-0008
**Lines**: 77-81
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> To understand a solution shape (A) better in Claude Code, you can 'rotate the fit check' by asking 'show me A x R', which displays all parts of A against all R, often with commentary suggesting next steps.

### ATOM-SOURCE-20260207-013-0009
**Lines**: 78-80
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> When conducting a 'spike' investigation, the findings should be documented as a separate markdown file for reference and inspection.

### ATOM-SOURCE-20260207-013-0011
**Lines**: 109-111
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> The primary rule of spiking is to ensure it's not a yes-or-no question; a spike should aim to gather objective information for decision-making.

### ATOM-SOURCE-20260207-013-0012
**Lines**: 130-130
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.00, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.60

> For V1 of a project, prioritizing an LLM-only approach can simplify the implementation.

### ATOM-SOURCE-20260207-013-0014
**Lines**: 152-157
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> In larger or more complex projects, it is important to create 'vertical slices' (subsets of the project with both backend and frontend) to allow for demoing and verification of direction, avoiding churn and interdependent decisions.

### ATOM-SOURCE-20260207-013-0016
**Lines**: 164-167
**Context**: method / evidence
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.60

> A CLI tool named `beam` can be used to find Mermaid code in a Markdown file and project it to a local TLDraw instance, allowing for hot-reloading and visual inspection of diagrams generated by an LLM.

### ATOM-SOURCE-20260207-013-0019
**Lines**: 218-221
**Context**: method / evidence
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.60

> When an LLM-generated application crashes, instruct the LLM to run the app itself and interact with it to verify functionality across various test cases (e.g., "add brazil", "feb 12", "paris feb 18").
