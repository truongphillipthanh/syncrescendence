# Extraction: SOURCE-20260109-001

**Source**: `SOURCE-20260109-web-article-mikaela_grace_jeremy_hadfield_rodrigo_olivares_jiri_de_jongh-demystifying_evals_for_ai_agents.md`
**Atoms extracted**: 64
**Categories**: analogy, claim, concept, framework, praxis_hook

---

## Analogy (1)

### ATOM-SOURCE-20260109-001-0058
**Lines**: 317-319
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Like the Swiss Cheese Model from safety engineering, no single evaluation method catches every issue; combining multiple methods ensures failures that slip through one layer are caught by another.

## Claim (26)

### ATOM-SOURCE-20260109-001-0001
**Lines**: 5-6
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.70

> The capabilities that make AI agents useful, such as autonomy, intelligence, and flexibility, also make them difficult to evaluate.

### ATOM-SOURCE-20260109-001-0007
**Lines**: 33-34
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.70

> Agent evaluations are complex because agents use tools across many turns, modifying state and adapting, which can lead to mistakes propagating and compounding.

### ATOM-SOURCE-20260109-001-0013
**Lines**: 50-54
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.80

> Teams with established evaluation systems (evals) can adopt new, more powerful AI models in days, while those without evals may take weeks due to extensive testing requirements.

### ATOM-SOURCE-20260109-001-0015
**Lines**: 54-57
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> Evals provide baselines and regression tests for metrics like latency, token usage, cost per task, and error rates on a static bank of tasks.

### ATOM-SOURCE-20260109-001-0016
**Lines**: 57-59
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.20, actionability=0.50, epistemic_stability=0.70

> Evals can serve as a high-bandwidth communication channel between product and research teams by defining metrics for researchers to optimize.

### ATOM-SOURCE-20260109-001-0026
**Lines**: 130-132
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> Effective evaluations for modern coding agents typically use well-specified tasks, stable test environments, and thorough tests for the generated code.

### ATOM-SOURCE-20260109-001-0027
**Lines**: 134-136
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.90

> Deterministic graders are suitable for coding agents because software evaluation is generally straightforward, focusing on whether code runs and tests pass.

### ATOM-SOURCE-20260109-001-0028
**Lines**: 137-141
**Context**: anecdote / evidence
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> SWE-bench Verified evaluates coding agents by having them fix GitHub issues from Python repositories, passing only if failing tests are fixed without breaking existing ones.

### ATOM-SOURCE-20260109-001-0029
**Lines**: 141-143
**Context**: anecdote / evidence
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> Terminal-Bench evaluates coding agents by testing end-to-end technical tasks, such as building a Linux kernel or training an ML model.

### ATOM-SOURCE-20260109-001-0032
**Lines**: 158-164
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> Unlike coding agents, where unit tests provide binary pass/fail signals, the quality of research agent output is judged relative to the specific task, as what constitutes 'comprehensive,' 'well-sourced,' or 'correct' varies by context (e.g., market scan vs. scientific report).

### ATOM-SOURCE-20260109-001-0033
**Lines**: 166-170
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.20, speculation_risk=0.20, actionability=0.20, epistemic_stability=0.70

> Evaluating research agents presents unique challenges, including expert disagreement on synthesis comprehensiveness, constantly shifting ground truth due to changing reference content, and increased potential for errors in longer, open-ended outputs.

### ATOM-SOURCE-20260109-001-0035
**Lines**: 177-180
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.80

> For research tasks with objectively correct answers (e.g., Company X's Q3 revenue), exact match evaluation works, while LLMs can flag unsupported claims, identify coverage gaps, and verify open-ended synthesis for coherence and completeness.

### ATOM-SOURCE-20260109-001-0038
**Lines**: 189-192
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.80

> Evaluating computer use agents requires running them in real or sandboxed environments to interact with software applications and verifying that they achieve the intended outcome.

### ATOM-SOURCE-20260109-001-0039
**Lines**: 198-201
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> Browser use agents require a balance between token efficiency and latency: DOM-based interactions are fast but token-intensive, while screenshot-based interactions are slower but more token-efficient.

### ATOM-SOURCE-20260109-001-0040
**Lines**: 207-208
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> Agent behavior varies between runs, making evaluation results harder to interpret due to non-determinism.

### ATOM-SOURCE-20260109-001-0044
**Lines**: 222-223
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> Pass@k and Pass^k diverge as the number of trials increases; they are identical at k=1 but tell opposite stories by k=10, with Pass@k approaching 100% and Pass^k falling to 0%.

### ATOM-SOURCE-20260109-001-0046
**Lines**: 237-240
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.70

> A 0% pass rate across many trials for frontier models often signals a broken task or ambiguous specification, rather than an incapable agent.

### ATOM-SOURCE-20260109-001-0049
**Lines**: 247-249
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.70

> One-sided evaluations, such as only testing if an agent searches when it should, can lead to agents over-optimizing for that behavior (e.g., searching for almost everything).

### ATOM-SOURCE-20260109-001-0051
**Lines**: 260-265
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.70

> Unnecessary shared state between evaluation runs (e.g., leftover files, cached data) can cause correlated failures due to infrastructure flakiness rather than agent performance, or artificially inflate performance (e.g., by allowing agents to examine git history from previous trials).

### ATOM-SOURCE-20260109-001-0054
**Lines**: 279-280
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> For AI product teams, owning and iterating on evaluations should be as routine as maintaining unit tests.

### ATOM-SOURCE-20260109-001-0056
**Lines**: 294-296
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> Automated evaluations can be run against an agent in thousands of tasks without deploying to production or affecting real users, but they are only one method for understanding agent performance.

### ATOM-SOURCE-20260109-001-0059
**Lines**: 318-319
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Promptfoo is a lightweight, flexible, and open-source framework that uses declarative YAML configuration for prompt testing, offering assertion types from string matching to LLM-as-judge rubrics.

### ATOM-SOURCE-20260109-001-0061
**Lines**: 321-322
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Braintrust is a platform that integrates offline evaluation with production observability and experiment tracking, suitable for teams needing both development iteration and production quality monitoring.

### ATOM-SOURCE-20260109-001-0062
**Lines**: 322-323
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Braintrust's `autoevals` library includes pre-built scorers for common dimensions like factuality and relevance.

### ATOM-SOURCE-20260109-001-0063
**Lines**: 325-325
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> LangSmith provides tracing, offline and online evaluations, and dataset management, with strong integration into the LangChain ecosystem.

### ATOM-SOURCE-20260109-001-0064
**Lines**: 327-327
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Langfuse offers capabilities similar to LangSmith as a self-hosted open-source alternative for teams with data residency requirements.

## Concept (21)

### ATOM-SOURCE-20260109-001-0003
**Lines**: 22-23
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> An 'evaluation' (eval) is a test for an AI system that involves providing an AI with an input and then applying grading logic to its output to measure success.

### ATOM-SOURCE-20260109-001-0004
**Lines**: 23-24
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> Automated evals are evaluations that can be run during development without real users.

### ATOM-SOURCE-20260109-001-0005
**Lines**: 26-27
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> Single-turn evaluations involve a prompt, a response, and grading logic, and were the primary method for earlier LLMs.

### ATOM-SOURCE-20260109-001-0006
**Lines**: 27-28
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.70

> Multi-turn evaluations have become increasingly common as AI capabilities have advanced.

### ATOM-SOURCE-20260109-001-0008
**Lines**: 40-40
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> A 'task' (also known as a problem or test case) is a single test with defined inputs and success criteria.

### ATOM-SOURCE-20260109-001-0009
**Lines**: 41-42
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> A 'trial' is each attempt at a task, with multiple trials run to produce more consistent results due to model output variability.

### ATOM-SOURCE-20260109-001-0010
**Lines**: 43-44
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> A 'grader' is logic that scores an aspect of an agent's performance, with a task potentially having multiple graders, each containing multiple assertions (checks).

### ATOM-SOURCE-20260109-001-0011
**Lines**: 45-47
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> A 'transcript' (also called a trace or trajectory) is the complete record of a trial, including outputs, tool calls, reasoning, intermediate results, and any other interactions.

### ATOM-SOURCE-20260109-001-0012
**Lines**: 48-50
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> The 'outcome' is the final state in the environment at the end of a trial, which may differ from the agent's stated output.

### ATOM-SOURCE-20260109-001-0014
**Lines**: 51-53
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> An 'evaluation harness' is the infrastructure that runs evals end-to-end, providing instructions and tools, running tasks concurrently, recording steps, grading outputs, and aggregating results.

### ATOM-SOURCE-20260109-001-0017
**Lines**: 65-69
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> AI agents can be categorized into types such as coding agents, research agents, computer use agents, and conversational agents, all of which can be evaluated using similar techniques.

### ATOM-SOURCE-20260109-001-0019
**Lines**: 81-87
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.90

> Code-based graders are fast, cheap, objective, reproducible, easy to debug, and verify specific conditions, but are brittle to valid variations and limited for subjective tasks.

### ATOM-SOURCE-20260109-001-0020
**Lines**: 92-98
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.20, actionability=0.50, epistemic_stability=0.80

> Model-based graders are flexible, scalable, capture nuance, and handle open-ended or freeform output, but are non-deterministic, more expensive than code-based graders, and require calibration with human graders for accuracy.

### ATOM-SOURCE-20260109-001-0021
**Lines**: 103-109
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.90

> Human graders provide gold standard quality, match expert user judgment, and are used to calibrate model-based graders, but are expensive, slow, and often require access to human experts at scale.

### ATOM-SOURCE-20260109-001-0022
**Lines**: 114-116
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.90

> Capability or "quality" evals assess what an agent can do well, starting with a low pass rate on challenging tasks to encourage improvement.

### ATOM-SOURCE-20260109-001-0023
**Lines**: 118-121
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.90

> Regression evals ensure an agent maintains its past performance, aiming for a nearly 100% pass rate to detect any backsliding or issues caused by changes.

### ATOM-SOURCE-20260109-001-0025
**Lines**: 129-130
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.90

> Coding agents write, test, and debug code, navigate codebases, and run commands, similar to human developers.

### ATOM-SOURCE-20260109-001-0031
**Lines**: 156-158
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> Research agents are AI systems designed to gather, synthesize, and analyze information to produce outputs such as answers or reports.

### ATOM-SOURCE-20260109-001-0037
**Lines**: 186-189
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> Computer use agents are AI systems that interact with software through human-like interfaces (screenshots, mouse clicks, keyboard input, scrolling) rather than APIs or code, enabling them to use any application with a graphical user interface (GUI).

### ATOM-SOURCE-20260109-001-0041
**Lines**: 213-214
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> Pass@k measures the likelihood that an agent achieves at least one correct solution within k attempts, with the score increasing as k rises.

### ATOM-SOURCE-20260109-001-0042
**Lines**: 218-220
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> Pass^k measures the probability that all k trials succeed, with the score decreasing as k increases due to the harder bar of consistent success.

## Framework (2)

### ATOM-SOURCE-20260109-001-0018
**Lines**: 73-76
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> Agent evaluations typically combine three types of graders: code-based, model-based, and human, each evaluating portions of the transcript or outcome, with the choice of grader being essential for effective evaluation design.

### ATOM-SOURCE-20260109-001-0057
**Lines**: 296-298
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> A complete picture of AI agent performance includes automated evals, production monitoring, user feedback, A/B testing, manual transcript review, and systematic human evaluation.

## Praxis Hook (14)

### ATOM-SOURCE-20260109-001-0002
**Lines**: 12-15
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> Good evaluations help teams ship AI agents more confidently by making problems and behavioral changes visible before they affect users, preventing reactive loops where issues are only caught in production.

### ATOM-SOURCE-20260109-001-0024
**Lines**: 124-126
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> After an agent is launched and optimized, capability evals with high pass rates can be converted into a continuous regression suite to monitor for drift.

### ATOM-SOURCE-20260109-001-0030
**Lines**: 145-150
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> Beyond pass-or-fail tests for coding task outcomes, it is useful to grade the transcript using heuristics-based code quality rules or model-based graders with rubrics to assess agent behaviors like tool calls or user interaction.

### ATOM-SOURCE-20260109-001-0034
**Lines**: 173-177
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> A strategy for building research agent evaluations is to combine grader types, using groundedness checks for source support, coverage checks for essential facts, and source quality checks for authoritativeness.

### ATOM-SOURCE-20260109-001-0036
**Lines**: 182-184
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> LLM-based rubrics for grading research agents should be frequently calibrated against expert human judgment due to the subjective nature of research quality.

### ATOM-SOURCE-20260109-001-0043
**Lines**: 218-224
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To create effective test cases for AI agents, begin by converting existing manual checks, common user tasks, and reported bugs into automated tests, prioritizing based on user impact.

### ATOM-SOURCE-20260109-001-0045
**Lines**: 226-230
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> When designing tasks for AI agent evaluation, ensure they are unambiguous: two domain experts should independently reach the same pass/fail verdict, and the task should be solvable by an agent following instructions correctly.

### ATOM-SOURCE-20260109-001-0047
**Lines**: 242-244
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> For each evaluation task, create a reference solution (a known-working output) to prove solvability and verify grader configuration.

### ATOM-SOURCE-20260109-001-0048
**Lines**: 246-249
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Build balanced problem sets that test both when a behavior should occur and when it shouldn't, to avoid one-sided optimization and class-imbalanced evaluations.

### ATOM-SOURCE-20260109-001-0050
**Lines**: 258-262
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Ensure the AI agent in the evaluation harness functions similarly to the production agent, and isolate each trial with a clean environment to prevent noise from shared state or infrastructure flakiness.

### ATOM-SOURCE-20260109-001-0052
**Lines**: 265-268
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Do not take evaluation scores at face value until someone investigates the details of the evaluation and reviews transcripts, as issues like unfair grading or ambiguous tasks can invalidate results.

### ATOM-SOURCE-20260109-001-0053
**Lines**: 274-277
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> Establish dedicated evaluation teams to own core infrastructure, while domain experts and product teams contribute most evaluation tasks and run the evaluations themselves to maintain a healthy evaluation suite long-term.

### ATOM-SOURCE-20260109-001-0055
**Lines**: 285-287
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Practice eval-driven development: build evaluations to define planned capabilities before agents can fulfill them, then iterate until the agent performs well.

### ATOM-SOURCE-20260109-001-0060
**Lines**: 321-322
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> The most effective teams combine automated evaluations for fast iteration, production monitoring for ground truth, and periodic human review for calibration.
