# Extraction: SOURCE-20260216-005

**Source**: `SOURCE-20260216-x-article-dabit3-the_self_healing_pr.md`
**Atoms extracted**: 6
**Categories**: claim, framework, praxis_hook

---

## Claim (3)

### ATOM-SOURCE-20260216-005-0001
**Lines**: 6-6
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> Agents generate Pull Requests (PRs) faster than human teams can review them.

### ATOM-SOURCE-20260216-005-0004
**Lines**: 17-19
**Context**: consensus / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.00, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> The autofix system works with any bot that leaves comments on GitHub PRs, including linters, test runners, security scanners, SonarQube, Codacy, and Devin Review.

### ATOM-SOURCE-20260216-005-0006
**Lines**: 24-25
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Lint failure comments are always processed by Devin regardless of allowlist settings because they are common mechanical fixes and least likely to cause loops.

## Framework (1)

### ATOM-SOURCE-20260216-005-0003
**Lines**: 15-16
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.00, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> The autofix process involves a loop: Devin writes code → a review bot comments → Devin reads the comment → Devin pushes a fix → CI runs again → if something else is flagged, the loop continues.

## Praxis Hook (2)

### ATOM-SOURCE-20260216-005-0002
**Lines**: 13-14
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.00, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> @cognition has implemented an "autofix" system using @DevinAI where Devin reads incoming review comments from bots on a PR and pushes a fix to the same PR.

### ATOM-SOURCE-20260216-005-0005
**Lines**: 22-23
**Context**: method / limitation
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.00, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> To prevent infinite loops, Devin ignores all bot comments by default, requiring specific bots to be added to an allowlist for processing.
