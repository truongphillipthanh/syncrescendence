# Extraction: SOURCE-20260218-011

**Source**: `SOURCE-20260218-x-article-llmjunky-codex_multi_agent_playbook_part_1_setup_guide.md`
**Atoms extracted**: 23
**Categories**: claim, concept, framework, praxis_hook, prediction

---

## Claim (8)

### ATOM-SOURCE-20260218-011-0001
**Lines**: 5-7
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Codex subagents, now called "multi agents," can be customized beyond the three built-in roles.

### ATOM-SOURCE-20260218-011-0003
**Lines**: 19-20
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> Codex update 0.102.0 introduced a new configuration setup for subagents, officially named "multi agents" by OpenAI.

### ATOM-SOURCE-20260218-011-0004
**Lines**: 21-22
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.70

> OpenAI implemented custom multi-agent roles into Codex due to community support and open issues on GitHub.

### ATOM-SOURCE-20260218-011-0008
**Lines**: 56-57
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Multi-agent configurations are defined through Codex's native config.toml and the new /agents/role_config.toml files.

### ATOM-SOURCE-20260218-011-0009
**Lines**: 62-64
**Context**: anecdote / claim
**Tension**: novelty=0.40, consensus_pressure=0.30, contradiction_load=0.00, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.50

> The documentation for Codex does not mention that the cap preventing more than six parallel agents can be configured to allow 'n' number of threads.

### ATOM-SOURCE-20260218-011-0012
**Lines**: 85-86
**Context**: consensus / limitation
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> Adding too many threads for parallel agents in Codex can lead to 429 errors, requiring a reduction in the number of parallel threads.

### ATOM-SOURCE-20260218-011-0018
**Lines**: 122-122
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> You can call skills from subagents and subagents from skills.

### ATOM-SOURCE-20260218-011-0022
**Lines**: 156-162
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> A curated list of 25 custom agent roles is available on GitHub, including roles such as 'api_designer', 'backend_architect', 'bug_bounty_hunter', 'code_reviewer', 'data_pipeline_architect', 'design_system_lead', 'devops_engineer', 'frontend_architect', 'infrastructure_architect', 'ml_engineer', 'mobile_architect', 'performance_optimizer', 'product_analyst', 'qa_engineer', 'requirements_analyst', 'schema_designer', 'security_auditor', 'shell_expert', 'skill_author', 'sre_engineer', 'start_up_cto', 'storage_architect', 'tech_writer', 'tester_creative', and 'infrastructure_automation'.

## Concept (1)

### ATOM-SOURCE-20260218-011-0005
**Lines**: 26-27
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> Custom Multi-Agent Roles are user-defined subagents in Codex, typically designed for repeatable tasks, in contrast to the three native roles: default, explorer, and worker.

## Framework (2)

### ATOM-SOURCE-20260218-011-0006
**Lines**: 31-36
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> The three base multi-agent roles in Codex are: Default agent (no defined role, inherits parent's model/reasoning), Explorer agent (runs on 5.1-Codex-Mini, designed for exploration), and Worker agent (implements tasks, fixes/runs tests, refactors code, inherits parent's model/reasoning).

### ATOM-SOURCE-20260218-011-0007
**Lines**: 44-55
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Multi-agent roles in Codex can be configured with: defined model and reasoning level, global or project scope, user-defined system prompt (developer_instructions), user-defined description, per-role permissions (read-only, read/write), customizable features (memory, shell access), user-defined MCP Servers and ChatGPT Apps, and customizable verbosity and personality.

## Praxis Hook (11)

### ATOM-SOURCE-20260218-011-0002
**Lines**: 8-9
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Users can create custom multi-agent roles with their own models, reasoning levels, permissions, and system prompts in Codex.

### ATOM-SOURCE-20260218-011-0010
**Lines**: 72-75
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Codex config files are hierarchical, loading first from the global ~/.codex directory, with additional config files at the project level able to supplement or override global settings.

### ATOM-SOURCE-20260218-011-0011
**Lines**: 81-83
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To increase the default number of parallel agents Codex can launch, define `max_threads` in your global config.toml under the `[agents]` section, for example: `[agents] max_threads = 12`.

### ATOM-SOURCE-20260218-011-0013
**Lines**: 87-99
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To define a custom agent in Codex, add an entry to your config.toml file (global or project root/subfolders) with a `role description` and a `config_file` path, such as `[agents.security_auditor] description = "Finds auth, injection, and secrets risks." config_file = "agents/security_auditor.toml"`.

### ATOM-SOURCE-20260218-011-0014
**Lines**: 88-93
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> When defining requirements, clarify the user goal and business outcome, surface assumptions and unknowns explicitly, define scope boundaries to prevent implementation drift, present concrete tradeoffs with recommendations, and produce acceptance criteria that engineers and QA can execute directly.

### ATOM-SOURCE-20260218-011-0015
**Lines**: 94-103
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Operating rules for requirements definition include: not jumping to implementation details before clarifying product intent, stating assumptions and proposing 1-2 viable interpretations if requirements are ambiguous, preferring concise decision-ready output, calling out risks, dependencies, and sequencing constraints early, separating must-have requirements from nice-to-have enhancements, including non-goals to prevent scope creep, and proposing minimum instrumentation needed to decide if data is missing.

### ATOM-SOURCE-20260218-011-0016
**Lines**: 102-106
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.60, actionability=0.90, epistemic_stability=0.70

> For custom role definitions in Codex, create an `/agents/` folder within your `.codex` directory (global or project) and define granular configurations in files like `.codex/agents/your-role_config.toml`, where omitted values will be inherited from the parent.

### ATOM-SOURCE-20260218-011-0017
**Lines**: 109-114
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> A custom agent's configuration file (e.g., `.codex/agents/your-role_config.toml`) can specify: `model`, `model_reasoning_effort`, `model_reasoning_summary`, `model_verbosity`, `personality`, `developer_instructions`, `sandbox_mode`, `network_access`, `writable_roots`, `web_search`, `memory_tool`, `shell_tool`, and `mcp_servers`.

### ATOM-SOURCE-20260218-011-0019
**Lines**: 124-135
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> To configure a subagent, define its description and a config file path in the main config.toml, then specify its model, reasoning effort, reasoning summary, and developer instructions in its dedicated config file (e.g., `frontend_arch.toml`).

### ATOM-SOURCE-20260218-011-0020
**Lines**: 138-139
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> To ensure subagents follow a structured output, add a structured output template to the `developer_instructions`.

### ATOM-SOURCE-20260218-011-0021
**Lines**: 150-153
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> To call an agent, use natural language prompts like "Use Sparky to implement plan.md. Work in a loop until all tasks are complete." Explicitly naming the agent in the prompt ensures it is called.

## Prediction (1)

### ATOM-SOURCE-20260218-011-0023
**Lines**: 165-166
**Context**: speculation / claim
**Tension**: novelty=0.10, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.60, actionability=0.70, epistemic_stability=0.70

> The next installment of the Subagent Masterclass will cover when to use subagents vs. the main session, orchestration strategies for parallel implementation with Spark, how to structure plan files for subagent execution, and prompt patterns for best results from custom roles.
