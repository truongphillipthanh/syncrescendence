# Extraction: SOURCE-20250124-website-article-unknown-writing_a_good_claude_md_humanlayer

**Source**: `SOURCE-20250124-website-article-unknown-writing_a_good_claude_md_humanlayer.md`
**Atoms extracted**: 21
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (9)

### ATOM-SOURCE-20250124-website-article-unknown-writing_a_good_claude_md_humanlayer-0002
**Lines**: 14-15
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.20, epistemic_stability=0.80

> Coding agent harnesses, such as Claude Code, typically require explicit management of agents' memory.

### ATOM-SOURCE-20250124-website-article-unknown-writing_a_good_claude_md_humanlayer-0003
**Lines**: 15-17
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.20, epistemic_stability=0.80

> `CLAUDE.md` (or `AGENTS.md`) is the default file included in every conversation with a coding agent.

### ATOM-SOURCE-20250124-website-article-unknown-writing_a_good_claude_md_humanlayer-0005
**Lines**: 47-48
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.10, epistemic_stability=0.70

> Claude often ignores the contents of `CLAUDE.md` files, regardless of the model used.

### ATOM-SOURCE-20250124-website-article-unknown-writing_a_good_claude_md_humanlayer-0006
**Lines**: 51-57
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.00, actionability=0.10, epistemic_stability=0.80

> Claude Code injects a system reminder with `CLAUDE.md` content, instructing the agent to ignore it unless highly relevant to the task.

### ATOM-SOURCE-20250124-website-article-unknown-writing_a_good_claude_md_humanlayer-0007
**Lines**: 60-63
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.10, epistemic_stability=0.70

> Claude is more likely to ignore `CLAUDE.md` instructions if they are not universally applicable to the tasks it is working on.

### ATOM-SOURCE-20250124-website-article-unknown-writing_a_good_claude_md_humanlayer-0008
**Lines**: 66-72
**Context**: speculation / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.00, speculation_risk=0.70, actionability=0.10, epistemic_stability=0.50

> Anthropic likely added the instruction to ignore `CLAUDE.md` content because many users appended 'hotfixes' and non-broadly applicable instructions, and telling Claude to ignore these led to better results.

### ATOM-SOURCE-20250124-website-article-unknown-writing_a_good_claude_md_humanlayer-0009
**Lines**: 83-86
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> An LLM performs better on a task when its context window is filled with focused, relevant information (examples, related files, tool calls, tool results) rather than irrelevant context.

### ATOM-SOURCE-20250124-website-article-unknown-writing_a_good_claude_md_humanlayer-0016
**Lines**: 133-135
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> Code style guidelines and mostly-irrelevant code snippets in an LLM's context window degrade performance, instruction-following, and consume valuable context.

### ATOM-SOURCE-20250124-website-article-unknown-writing_a_good_claude_md_humanlayer-0017
**Lines**: 137-140
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.90

> LLMs are in-context learners, meaning if code follows certain style guidelines, the LLM should tend to follow those patterns without explicit instruction, especially with access to the codebase or documentation.

## Concept (1)

### ATOM-SOURCE-20250124-website-article-unknown-writing_a_good_claude_md_humanlayer-0001
**Lines**: 10-12
**Context**: consensus / claim
**Tension**: novelty=0.00, consensus_pressure=0.90, contradiction_load=0.00, speculation_risk=0.00, actionability=0.10, epistemic_stability=0.90

> LLMs are stateless functions, meaning their weights are fixed during inference and they do not learn over time. Their knowledge of a codebase is limited to the tokens provided in the current input.

## Framework (1)

### ATOM-SOURCE-20250124-website-article-unknown-writing_a_good_claude_md_humanlayer-0013
**Lines**: 105-120
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.00, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> The principle of Progressive Disclosure can be applied to LLM instructions by keeping task-specific instructions in separate, self-descriptive markdown files (e.g., `building_the_project.md`, `running_tests.md`) and having `CLAUDE.md` instruct the LLM to decide which files are relevant to read.

## Praxis Hook (10)

### ATOM-SOURCE-20250124-website-article-unknown-writing_a_good_claude_md_humanlayer-0004
**Lines**: 29-42
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Use `CLAUDE.md` to onboard Claude to your codebase by providing information on 'WHAT' (tech stack, project structure, monorepo details), 'WHY' (project purpose, function of parts), and 'HOW' (execution environment, verification steps like tests, typechecks, compilation).

### ATOM-SOURCE-20250124-website-article-unknown-writing_a_good_claude_md_humanlayer-0010
**Lines**: 87-90
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> When writing `CLAUDE.md`, prioritize fewer instructions, ideally only those universally applicable to the task, as LLMs have limits on instruction following and performance degrades with more instructions.

### ATOM-SOURCE-20250124-website-article-unknown-writing_a_good_claude_md_humanlayer-0011
**Lines**: 88-94
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> Ensure the contents of `CLAUDE.md` are as universally applicable as possible, avoiding task-specific instructions (e.g., how to structure a new database schema) that would distract the model in unrelated contexts.

### ATOM-SOURCE-20250124-website-article-unknown-writing_a_good_claude_md_humanlayer-0012
**Lines**: 96-99
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Keep the `CLAUDE.md` file concise; general consensus suggests less than 300 lines, with shorter being even better, to optimize LLM performance.

### ATOM-SOURCE-20250124-website-article-unknown-writing_a_good_claude_md_humanlayer-0014
**Lines**: 122-124
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.50, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> When using separate instruction files for an LLM, prefer pointers to copies by including `file:line` references instead of code snippets, as snippets can quickly become outdated.

### ATOM-SOURCE-20250124-website-article-unknown-writing_a_good_claude_md_humanlayer-0015
**Lines**: 128-131
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Avoid including code style guidelines in `CLAUDE.md` because LLMs are expensive and slow compared to traditional linters and formatters; always use deterministic tools when possible.

### ATOM-SOURCE-20250124-website-article-unknown-writing_a_good_claude_md_humanlayer-0018
**Lines**: 142-144
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.00, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Set up a Claude Code Stop hook that runs a formatter and linter and presents errors to Claude for fixing, rather than having Claude find formatting issues itself.

### ATOM-SOURCE-20250124-website-article-unknown-writing_a_good_claude_md_humanlayer-0019
**Lines**: 146-148
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Use a linter that can automatically fix issues, and carefully tune its rules for maximum safe auto-fix coverage.

### ATOM-SOURCE-20250124-website-article-unknown-writing_a_good_claude_md_humanlayer-0020
**Lines**: 150-153
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.00, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Create a Slash Command that includes code guidelines and points Claude to changes in version control or `git status` to handle implementation and formatting separately, leading to better results.

### ATOM-SOURCE-20250124-website-article-unknown-writing_a_good_claude_md_humanlayer-0021
**Lines**: 157-164
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.50, contradiction_load=0.00, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.80

> Avoid auto-generating `CLAUDE.md` files, as it is the highest leverage point of the harness and requires careful crafting to define the project's WHY, WHAT, and HOW.
