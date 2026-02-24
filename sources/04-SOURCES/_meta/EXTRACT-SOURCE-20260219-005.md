# Extraction: SOURCE-20260219-005

**Source**: `SOURCE-20260219-x-article-dimitrispapail-addition_under_pressure.md`
**Atoms extracted**: 17
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (10)

### ATOM-SOURCE-20260219-005-0001
**Lines**: 2-3
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> Claude Code trained a 6,080-parameter transformer model and Codex trained a 1,644-parameter transformer model, both capable of 10-digit addition.

### ATOM-SOURCE-20260219-005-0003
**Lines**: 22-25
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> The prompt for the AI agents had three objectives in order of priority: 1) at least 99% exact-match accuracy on 10-digit addition, 2) minimize parameter count, and 3) produce a report documenting the process.

### ATOM-SOURCE-20260219-005-0007
**Lines**: 50-51
**Context**: anecdote / evidence
**Tension**: novelty=0.20, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.70

> Claude Code initially used a variable-length format (e.g., '123+45=') which failed for 10-digit problems due to digit alignment issues.

### ATOM-SOURCE-20260219-005-0009
**Lines**: 57-59
**Context**: anecdote / evidence
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.70

> Claude Code observed 'grokking' in the transformer training for 10-digit addition, characterized by a sharp phase transition where the model suddenly learns the algorithm after thousands of steps at near-zero accuracy.

### ATOM-SOURCE-20260219-005-0011
**Lines**: 66-67
**Context**: anecdote / evidence
**Tension**: novelty=0.50, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.70

> Claude Code discovered a sharp parameter phase transition for 10-digit addition: a d=12 model (4,176 params) failed, while a d=16 model (6,080 params) succeeded perfectly.

### ATOM-SOURCE-20260219-005-0012
**Lines**: 66-69
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> In Claude Code's format for addition, computing an output digit requires attending to two separate positions (A's digit and B's digit), whereas with "pair tokens" (where both digits are packed together), one layer suffices.

### ATOM-SOURCE-20260219-005-0013
**Lines**: 67-67
**Context**: anecdote / evidence
**Tension**: novelty=0.50, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.70

> For the 10-digit addition task, Claude Code found that model width (hidden dimension) matters more than depth, with 2 layers being the optimal depth.

### ATOM-SOURCE-20260219-005-0014
**Lines**: 74-76
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> A transformer model for 10-digit addition achieved 99.04% accuracy with 1,644 parameters, using one layer, a hidden dimension of 8, and a feedforward dimension of 12, with a vocabulary of 114 tokens.

### ATOM-SOURCE-20260219-005-0015
**Lines**: 84-86
**Context**: consensus / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.20, speculation_risk=0.20, actionability=0.50, epistemic_stability=0.60

> The parameter count for the addition transformer was reduced by 223x, from 366K to 1,644, by reframing the objective rather than introducing new information about the task.

### ATOM-SOURCE-20260219-005-0017
**Lines**: 95-97
**Context**: anecdote / evidence
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.30, speculation_risk=0.20, actionability=0.40, epistemic_stability=0.50

> Codex achieved its efficiency by using a clever token encoding that optimized for parameter reduction, potentially disregarding an unwritten objective of generality.

## Concept (1)

### ATOM-SOURCE-20260219-005-0016
**Lines**: 92-93
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> There is a tradeoff between generality and optimizing hard for a specific goal in AI model development.

## Framework (1)

### ATOM-SOURCE-20260219-005-0005
**Lines**: 35-40
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> Hard rules for the transformer training task included: generalization to a held-out test set of at least 10k examples, no encoding the answer in the input, no calculators/symbolic solvers at inference time, autoregressive output, and no external resources.

## Praxis Hook (5)

### ATOM-SOURCE-20260219-005-0002
**Lines**: 12-16
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> A research experiment was conducted by prompting AI agents (Claude Code and Codex) to train the smallest possible transformer for 10-digit addition with at least 99% accuracy, without internet access or external resources, and to produce a report.

### ATOM-SOURCE-20260219-005-0004
**Lines**: 28-32
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> AI agents were required to operate autonomously, setting up, running, monitoring experiments, making decisions, justifying them, and writing reports without human feedback.

### ATOM-SOURCE-20260219-005-0006
**Lines**: 44-46
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.60

> AI agents were given the freedom to optimize data format and tokenization programmatically, without specific suggestions like reversing digits or padding.

### ATOM-SOURCE-20260219-005-0008
**Lines**: 51-54
**Context**: method / evidence
**Tension**: novelty=0.50, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Claude Code successfully used zero-padded fixed-length inputs with reversed output (e.g., '0000000123+0000000045=') to ensure carry propagation flows left to right during generation, which immediately worked for 10-digit addition.

### ATOM-SOURCE-20260219-005-0010
**Lines**: 62-64
**Context**: method / evidence
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Claude Code systematically scaled down parameters, starting from 795K, then sweeping from 400K to 100K, 58K to 7K, and 15K to 4K, to find the smallest successful model.
