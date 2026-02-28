# Extraction: SOURCE-20260203-011

**Source**: `SOURCE-20260203-x-article-aidenybai-how_i_made_claude_code_3x_faster.md`
**Atoms extracted**: 14
**Categories**: claim, concept, praxis_hook

---

## Claim (10)

### ATOM-SOURCE-20260203-011-0001
**Lines**: 10-11
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> Coding agents are inefficient at frontend tasks because the process of translating user intent (from UI to prompt to code to UI) is lossy.

### ATOM-SOURCE-20260203-011-0002
**Lines**: 20-23
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.20, speculation_risk=0.20, actionability=0.40, epistemic_stability=0.70

> The search process for coding agents is random and non-deterministic due to language models, leading to variable latency, cost, and performance.

### ATOM-SOURCE-20260203-011-0004
**Lines**: 32-33
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.20, speculation_risk=0.30, actionability=0.30, epistemic_stability=0.60

> Improving coding agents' codebase search capabilities involves significant unsolved research problems, including training better models.

### ATOM-SOURCE-20260203-011-0005
**Lines**: 36-36
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> Reducing the number of translation steps required for coding agents makes the process faster and more accurate, especially as codebase size increases.

### ATOM-SOURCE-20260203-011-0006
**Lines**: 40-42
**Context**: anecdote / evidence
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> Referencing the file path or specific grep-able content significantly speeds up coding agents' ability to find referenced code.

### ATOM-SOURCE-20260203-011-0008
**Lines**: 51-52
**Context**: anecdote / evidence
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> When provided with React Grab's component stack, Claude Code instantly found files and made changes in seconds, demonstrating a significant speed improvement.

### ATOM-SOURCE-20260203-011-0010
**Lines**: 67-70
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> Without React Grab, coding agents must search the codebase, a non-deterministic process that adds latency, increases token consumption, and degrades performance.

### ATOM-SOURCE-20260203-011-0011
**Lines**: 72-75
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> With React Grab, the search phase for coding agents is eliminated because the component stack with exact file paths and line numbers is embedded in the DOM, allowing O(1) time complexity for locating code.

### ATOM-SOURCE-20260203-011-0012
**Lines**: 77-77
**Context**: consensus / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Claude Code becomes approximately 3 times faster when used with React Grab.

### ATOM-SOURCE-20260203-011-0013
**Lines**: 90-90
**Context**: consensus / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> React Grab is most effective for low-entropy adjustments like spacing, layout tweaks, or minor visual changes in UI.

## Concept (1)

### ATOM-SOURCE-20260203-011-0007
**Lines**: 44-46
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> React Grab is a tool that walks up the React component tree from a clicked element, collects component names and source locations (file path + line number), and formats them into a readable stack.

## Praxis Hook (3)

### ATOM-SOURCE-20260203-011-0003
**Lines**: 28-29
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To improve coding agent performance, users can 'prompt better' by adding context and writing longer, more specific prompts.

### ATOM-SOURCE-20260203-011-0009
**Lines**: 55-56
**Context**: method / evidence
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.90

> The shadcn/ui dashboard, a Next.js application, was used as the test codebase for benchmarking React Grab's performance.

### ATOM-SOURCE-20260203-011-0014
**Lines**: 94-95
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> React Grab works with any IDE or coding tool (e.g., Cursor, Claude Code, Copilot, Codex, Zed, Windsurf) by adding extra context to prompts to help agents locate code faster.
