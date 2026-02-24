# Extraction: SOURCE-20260219-009

**Source**: `SOURCE-20260219-x-article-minchoi-measuring_ai_agent_autonomy_framework.md`
**Atoms extracted**: 18
**Categories**: claim, concept, framework

---

## Claim (16)

### ATOM-SOURCE-20260219-009-0001
**Lines**: 4-6
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Anthropic has published a framework for measuring AI agent autonomy, which assesses how independently an AI can plan, use tools, recover from mistakes, and complete tasks end-to-end.

### ATOM-SOURCE-20260219-009-0003
**Lines**: 30-31
**Context**: consensus / evidence
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> The 99.9th percentile 'work time' for Claude Code, representing how long it works before stopping, nearly doubled from under 25 minutes to over 45 minutes in approximately three months (September 2025 to January 2026).

### ATOM-SOURCE-20260219-009-0004
**Lines**: 40-40
**Context**: consensus / evidence
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Experienced users of Claude Code (40%+) auto-approve full sessions at a higher rate than new users (~20%).

### ATOM-SOURCE-20260219-009-0005
**Lines**: 41-42
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.30, epistemic_stability=0.70

> As users gain experience with Claude Code, their oversight shifts from approving every step to monitoring and intervening only when necessary, despite an increase in interruptions.

### ATOM-SOURCE-20260219-009-0006
**Lines**: 51-52
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.30, epistemic_stability=0.70

> On complex tasks, Claude Code initiates pauses for clarification more than twice as often as humans interrupt it, indicating agent-initiated oversight.

### ATOM-SOURCE-20260219-009-0007
**Lines**: 56-60
**Context**: consensus / evidence
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> The primary reasons Claude stops itself are to present choices (35%), gather diagnostic information (21%), clarify vague requests (13%), request missing credentials (12%), or seek approval/confirmation (11%).

### ATOM-SOURCE-20260219-009-0009
**Lines**: 63-67
**Context**: consensus / evidence
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> The main reasons humans interrupt Claude are to provide missing context/corrections (32%), due to Claude being slow/hanging (17%), having received enough help (7%), wanting to take the next step themselves (7%), or to change requirements mid-task (5%).

### ATOM-SOURCE-20260219-009-0010
**Lines**: 63-63
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> The majority of AI agent tasks currently cluster in lower-risk quadrants, as shown in a scatter plot titled "What is the risk-autonomy tradeoff in practice?" which plots Mean autonomy score against Mean risk score.

### ATOM-SOURCE-20260219-009-0011
**Lines**: 67-67
**Context**: consensus / evidence
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.20, actionability=0.10, epistemic_stability=0.70

> Tasks identified as "Unclear and unsafe tasks (e.g., banking ops in Cyber)" are located in the top-left quadrant of the risk-autonomy tradeoff plot, indicating lower autonomy and higher risk.

### ATOM-SOURCE-20260219-009-0012
**Lines**: 68-68
**Context**: consensus / evidence
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.20, actionability=0.10, epistemic_stability=0.70

> Tasks described as "Perfect agents - Narrow tasks with high safety guardrails" are found in the bottom-right quadrant, signifying higher autonomy and lower risk.

### ATOM-SOURCE-20260219-009-0013
**Lines**: 69-69
**Context**: consensus / evidence
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.20, actionability=0.10, epistemic_stability=0.70

> Tasks experiencing "Performance issues - Struggling on docs/PDFs/real-world messiness" are situated in the lower-left quadrant, indicating lower autonomy and lower risk.

### ATOM-SOURCE-20260219-009-0014
**Lines**: 70-70
**Context**: consensus / evidence
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.20, actionability=0.10, epistemic_stability=0.70

> An "Autonomy breakthrough - Steady growth in short, well-defined tasks like debugging" is observed in the bottom-right quadrant, representing higher autonomy and lower risk.

### ATOM-SOURCE-20260219-009-0015
**Lines**: 75-75
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.20, actionability=0.10, epistemic_stability=0.70

> The top-right quadrant (higher autonomy, higher risk) of the risk-autonomy tradeoff plot is sparsely populated but not empty, suggesting that some AI agent tasks operate in this challenging space.

### ATOM-SOURCE-20260219-009-0016
**Lines**: 76-77
**Context**: method / evidence
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.20, actionability=0.10, epistemic_stability=0.70

> The data on AI agent risk and autonomy is based on Claude-generated classifications of individual tool calls made via Anthropic's public API, validated against internal data where possible.

### ATOM-SOURCE-20260219-009-0017
**Lines**: 78-79
**Context**: method / limitation
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.20, actionability=0.10, epistemic_stability=0.70

> The analysis of AI agent risk and autonomy excludes task clusters that do not meet aggregation minimums for unique tool calls or customers.

### ATOM-SOURCE-20260219-009-0018
**Lines**: 79-79
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.20, actionability=0.10, epistemic_stability=0.70

> The data for the risk-autonomy tradeoff analysis is based on a sample of 998,481 tool calls on Anthropic's public API.

## Concept (1)

### ATOM-SOURCE-20260219-009-0002
**Lines**: 20-20
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.70

> An AI agent is defined as a model combined with tools that enable it to take actions.

## Framework (1)

### ATOM-SOURCE-20260219-009-0008
**Lines**: 60-65
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.30, epistemic_stability=0.60

> AI agent tasks can be categorized into four quadrants based on their mean autonomy and mean risk scores: lower autonomy/lower risk, higher autonomy/lower risk, lower autonomy/higher risk, and higher autonomy/higher risk.
