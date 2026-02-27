# Extraction: SOURCE-20260216-018

**Source**: `SOURCE-20260216-x-article-ryancarson-code_factory_how_to_setup_your_repo_so_your_agent_can_auto_write_and_review_100_percent_of_your_code.md`
**Atoms extracted**: 17
**Categories**: claim, framework, praxis_hook

---

## Claim (3)

### ATOM-SOURCE-20260216-018-0003
**Lines**: 79-80
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.80

> Using a single machine-readable contract removes ambiguity and prevents silent drift between scripts, workflow files, and policy documents in a code repository.

### ATOM-SOURCE-20260216-018-0006
**Lines**: 111-112
**Context**: consensus / claim
**Tension**: novelty=0.50, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.80

> Skipping current-head SHA discipline can lead to merging a PR using stale 'clean' evidence.

### ATOM-SOURCE-20260216-018-0017
**Lines**: 187-187
**Context**: consensus / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> Implementing the recommended pattern for repository management allows agents to implement, validate, and be reviewed with deterministic, auditable standards.

## Framework (3)

### ATOM-SOURCE-20260216-018-0002
**Lines**: 47-51
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> A machine-readable contract for code repositories should define risk tiers by path, required checks by tier, documentation drift rules for control-plane changes, and evidence requirements for UI/critical flows.

### ATOM-SOURCE-20260216-018-0013
**Lines**: 167-175
**Context**: anecdote / claim
**Tension**: novelty=0.50, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> Key lessons for running automated code review in PRs include: deterministic ordering (preflight gate before CI fanout), non-negotiable current-head SHA matching, a single canonical writer for review rerun requests, treating vulnerability language and weak-confidence summaries as actionable, auto-resolving bot-only threads only after clean current-head evidence, and using a remediation agent to shorten loop time with strict guardrails.

### ATOM-SOURCE-20260216-018-0015
**Lines**: 178-185
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.30, actionability=0.90, epistemic_stability=0.60

> A general pattern for automated code review involves a `code review agent`, a `remediation agent`, and a `risk policy gate`, which can be implemented with specific tools like Greptile for code review, Codex Action for remediation, and dedicated workflows for reruns, cleanup, and preflight policies.

## Praxis Hook (11)

### ATOM-SOURCE-20260216-018-0001
**Lines**: 18-25
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.30, actionability=0.90, epistemic_stability=0.60

> To set up a repository for automated code writing and review, establish a loop where a coding agent writes code, the repository enforces risk-aware checks before merging, a code review agent validates the PR, evidence (tests, browser, review) is machine-verifiable, and findings are converted into repeatable harness cases.

### ATOM-SOURCE-20260216-018-0004
**Lines**: 83-88
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> To optimize CI, run a `risk-policy-gate` first to verify deterministic policy and review-agent state, and only then initiate `test/build/security` fanout jobs, avoiding wasted CI minutes on PRs blocked by policy or unresolved review findings.

### ATOM-SOURCE-20260216-018-0005
**Lines**: 103-110
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.80

> Enforce current-head SHA discipline by treating review state as valid only when it matches the current PR head commit, waiting for the review check run on `headSha`, ignoring stale summary comments, failing if the latest review run is non-success or times out, and requiring reruns after each synchronize/push.

### ATOM-SOURCE-20260216-018-0007
**Lines**: 115-117
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> To prevent duplicate bot comments and race conditions when multiple workflows request reruns, use exactly one workflow as the canonical rerun requester and deduplicate by a marker plus `sha:<head>`.

### ATOM-SOURCE-20260216-018-0008
**Lines**: 130-139
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.40, actionability=0.90, epistemic_stability=0.60

> Implement an automated remediation loop where, if review findings are actionable, a coding agent reads review context, patches code, runs focused local validation, and pushes a fix commit to the same PR branch, ensuring determinism by pinning the model and effort for reproducibility, skipping stale comments, and never bypassing policy gates.

### ATOM-SOURCE-20260216-018-0009
**Lines**: 142-147
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> After a clean current-head rerun, auto-resolve unresolved threads where all comments are from the review bot, but never auto-resolve human-participated threads, then rerun the policy gate to reflect the new state of required-conversation-resolution.

### ATOM-SOURCE-20260216-018-0010
**Lines**: 150-156
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> For UI or user-flow changes, require evidence manifests and assertions in CI as first-class proof, ensuring that required flows exist, expected entrypoints and account identities are used, and artifacts are fresh and valid.

### ATOM-SOURCE-20260216-018-0011
**Lines**: 161-166
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> To manage code review agents, use a remediation agent (e.g., Codex Action), a canonical rerun workflow (`greptile-rerun.yml`), a stale-thread cleanup workflow (`greptile-auto-resolve-threads.yml`), and a preflight policy workflow (`risk-policy-gate.yml`).

### ATOM-SOURCE-20260216-018-0012
**Lines**: 162-164
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Preserve incident memory and grow long-term coverage by establishing a harness-gap loop where production regressions lead to a harness gap issue, a case is added, and its SLA is tracked.

### ATOM-SOURCE-20260216-018-0014
**Lines**: 167-168
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> When using a different reviewer for code, maintain the same control-plane semantics and only swap integration points.

### ATOM-SOURCE-20260216-018-0016
**Lines**: 179-187
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.30, actionability=0.90, epistemic_stability=0.60

> A recommended pattern for managing a repository with agents involves: 1. Combining risk and merge policies into a single contract. 2. Enforcing a preflight gate before expensive CI runs. 3. Requiring a clean code-review-agent state for the current head SHA. 4. Remediating findings in-branch and rerunning deterministically if they exist. 5. Auto-resolving only bot-only stale threads after a clean rerun. 6. Requiring browser evidence for UI/flow changes. 7. Converting incidents into harness cases and tracking loop SLOs.
