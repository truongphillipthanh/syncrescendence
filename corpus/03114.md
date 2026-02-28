# Extraction: SOURCE-20260126-x-thread-unknown-karpathy_guidelines_for_coding_agents_jiayuan_jy

**Source**: `SOURCE-20260126-x-thread-unknown-karpathy_guidelines_for_coding_agents_jiayuan_jy.md`
**Atoms extracted**: 5
**Categories**: claim, praxis_hook

---

## Claim (1)

### ATOM-SOURCE-20260126-x-thread-unknown-karpathy_guidelines_for_coding_agents_jiayuan_jy-0005
**Lines**: 80-80
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.30, actionability=0.20, epistemic_stability=0.60

> When building or coding becomes a commodity, taste significantly increases in importance.

## Praxis Hook (4)

### ATOM-SOURCE-20260126-x-thread-unknown-karpathy_guidelines_for_coding_agents_jiayuan_jy-0001
**Lines**: 18-29
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> When coding with LLMs, prioritize caution over speed, especially for non-trivial tasks, by explicitly stating assumptions, presenting multiple interpretations, suggesting simpler approaches, and clarifying confusion before implementing.

### ATOM-SOURCE-20260126-x-thread-unknown-karpathy_guidelines_for_coding_agents_jiayuan_jy-0002
**Lines**: 31-42
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> To ensure simplicity in LLM-generated code, adhere to the minimum code required to solve the problem, avoiding unrequested features, single-use abstractions, unrequested flexibility, and error handling for impossible scenarios. If code is overcomplicated, rewrite it.

### ATOM-SOURCE-20260126-x-thread-unknown-karpathy_guidelines_for_coding_agents_jiayuan_jy-0003
**Lines**: 44-58
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> When editing existing code, make only surgical changes: avoid improving adjacent code, refactoring unbroken elements, or deleting pre-existing dead code unless specifically asked. Match existing style and remove only imports/variables/functions that your changes made unused.

### ATOM-SOURCE-20260126-x-thread-unknown-karpathy_guidelines_for_coding_agents_jiayuan_jy-0004
**Lines**: 60-75
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> For goal-driven execution, transform coding tasks into verifiable goals (e.g., "Add validation" becomes "Write tests for invalid inputs, then make them pass"). For multi-step tasks, state a brief plan with verification checks for each step.
