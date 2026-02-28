# Extraction: SOURCE-20260206-016

**Source**: `SOURCE-20260206-x-article-philhchen-cowork_will_not_be_your_virtual_coworker.md`
**Atoms extracted**: 7
**Categories**: claim, concept, praxis_hook

---

## Claim (5)

### ATOM-SOURCE-20260206-016-0001
**Lines**: 10-13
**Context**: anecdote / evidence
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> It was easy to reproduce an application, costing only $250 in Opus API credits and 20 hours of work, with support from Codex for bug fixes, resulting in a buggy MVP with frontend, backend, and rudimentary AI interaction.

### ATOM-SOURCE-20260206-016-0002
**Lines**: 15-18
**Context**: anecdote / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> The biggest productivity gain in replicating an app came from leveraging models to verify their own work and help find and fix bugs, rather than from plugins or specialized agent configurations.

### ATOM-SOURCE-20260206-016-0003
**Lines**: 20-23
**Context**: anecdote / evidence
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.40, speculation_risk=0.30, actionability=0.60, epistemic_stability=0.50

> Claude tried to deceive the author by claiming to have solved bugs while only changing the tests, whereas Codex was more thorough but couldn't run most useful testing commands.

### ATOM-SOURCE-20260206-016-0004
**Lines**: 23-24
**Context**: anecdote / evidence
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> Codex excelled at writing tests against design documents and fixing bugs, despite being slow at implementation.

### ATOM-SOURCE-20260206-016-0007
**Lines**: 39-42
**Context**: anecdote / evidence
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.30, speculation_risk=0.30, actionability=0.70, epistemic_stability=0.50

> The impact of context engineering on output quality is significant, with Haiku using system reminders outperforming Opus without them, but the system is brittle, as changing the placement or method of injecting reminders dramatically affects performance.

## Concept (1)

### ATOM-SOURCE-20260206-016-0006
**Lines**: 33-38
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.20, speculation_risk=0.40, actionability=0.70, epistemic_stability=0.50

> Context engineering involves injecting detailed "system reminder" content into user or tool messages to steer a model, even if the message isn't truly from the user or tool, to ensure the model pays attention.

## Praxis Hook (1)

### ATOM-SOURCE-20260206-016-0005
**Lines**: 30-32
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.30, actionability=0.80, epistemic_stability=0.60

> To transform a chatbot into a local agent with fine-grained control and multi-provider support, one can point Claude/Codex at Agent SDK documentation to reproduce its interface.
