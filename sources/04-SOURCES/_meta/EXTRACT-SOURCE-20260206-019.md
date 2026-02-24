# Extraction: SOURCE-20260206-019

**Source**: `SOURCE-20260206-x-article-shpigford-token_efficiency_in_openclaw_let_scripts_do_the_heavy_lifting.md`
**Atoms extracted**: 31
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (6)

### ATOM-SOURCE-20260206-019-0002
**Lines**: 10-14
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> AI agents checking for work frequently (e.g., every few minutes) burn tokens and incur real costs even when no work is found, due to context loading and decision-making.

### ATOM-SOURCE-20260206-019-0003
**Lines**: 18-25
**Context**: anecdote / evidence
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> The author's 'Swarm dispatcher' alone burned $10-20 by checking empty queues over 260+ sessions, with each 'queue empty' response costing $0.01-0.07 in tokens.

### ATOM-SOURCE-20260206-019-0005
**Lines**: 34-36
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> Every OpenClaw heartbeat is a full model invocation, incurring costs for context loading, reasoning, and tool calls, even if the outcome is 'nothing happening'.

### ATOM-SOURCE-20260206-019-0007
**Lines**: 50-51
**Context**: anecdote / evidence
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> Using a cheaper model like Haiku for browser tasks can be 5x cheaper than using a premium model like Opus for identical work ($0.03 vs. $0.15+ per task).

### ATOM-SOURCE-20260206-019-0022
**Lines**: 154-157
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> Batched checks that benefit from shared context are a valid use case for heartbeats in agent systems, such as checking email, calendar, and weather simultaneously to correlate information.

### ATOM-SOURCE-20260206-019-0025
**Lines**: 164-170
**Context**: anecdote / evidence
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.30, epistemic_stability=0.70

> Migrating to a specific pattern (not fully detailed in this excerpt) resulted in significant cost reductions and efficiency improvements for an agent system, including reducing swarm empty-queue checks from $10-20 to $0, browser task costs from $0.15+ to $0.03, and auth check frequency by 12x.

## Concept (3)

### ATOM-SOURCE-20260206-019-0004
**Lines**: 30-33
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.90

> OpenClaw's 'heartbeat' system is a periodic poll (default every 30 minutes) that wakes an agent to check configured tasks (e.g., emails, calendar, printer status) listed in a HEARTBEAT.md file.

### ATOM-SOURCE-20260206-019-0023
**Lines**: 158-161
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> The AI agent's HEARTBEAT.md should be reserved for batched checks that benefit from shared context (e.g., correlating email, calendar, and weather for an outdoor meeting), while independent checks should be handled by cron jobs.

### ATOM-SOURCE-20260206-019-0031
**Lines**: 182-182
**Context**: hypothesis / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.40, speculation_risk=0.30, actionability=0.40, epistemic_stability=0.50

> An AI assistant should be viewed as a 'thinker' rather than a 'cron daemon,' implying its primary role is judgment and complex reasoning, not routine, deterministic tasks.

## Framework (3)

### ATOM-SOURCE-20260206-019-0006
**Lines**: 40-45
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> A core philosophy for token efficiency is: 'Models are expensive thinkers. Scripts are free doers.' Deterministic logic ('if X, then Y') should be handled by scripts, while models should only engage for ambiguity, human-readable formatting, or complex edge cases.

### ATOM-SOURCE-20260206-019-0008
**Lines**: 53-60
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> A three-tier model strategy for AI agents involves using: Premium models (e.g., Opus) for main conversation and complex decisions; Workhorse models (e.g., Sonnet 4.5) for research, writing, and analysis; and Cheap models (e.g., Haiku 4.5) for browser automation and mechanical tasks.

### ATOM-SOURCE-20260206-019-0011
**Lines**: 74-81
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> The 'Cron + Script Pattern' for token efficiency involves a cron job firing a script that handles all deterministic logic, only calling the AI model if there's something to report, thereby reducing token burn compared to a model-centric heartbeat approach.

## Praxis Hook (19)

### ATOM-SOURCE-20260206-019-0001
**Lines**: 1-4
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To reduce token costs in AI agents, move deterministic logic from AI model invocations to 'dumb scripts' and use 'smart triggers' to only invoke the model when ambiguity or reporting is required.

### ATOM-SOURCE-20260206-019-0009
**Lines**: 62-64
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> The main AI session should orchestrate tasks rather than execute them directly; spawn sub-agents with appropriate models (e.g., Haiku for browser work, Sonnet for research) for specific tasks.

### ATOM-SOURCE-20260206-019-0010
**Lines**: 66-67
**Context**: method / limitation
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Always verify the model actually applied, as incorrect model names (e.g., `claude-3-5-haiku` instead of `claude-haiku-4-5`) can cause silent fallback to more expensive models.

### ATOM-SOURCE-20260206-019-0012
**Lines**: 86-89
**Context**: method / evidence
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> To save $10-20, replace an AI agent's cron job checking a dispatch queue every 2 minutes with native code that only invokes the model when work exists.

### ATOM-SOURCE-20260206-019-0013
**Lines**: 92-95
**Context**: method / evidence
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> To reduce model invocations from ~50/day to ~3, use a bash script to monitor printer status and only output (and thus invoke the model) if something has changed.

### ATOM-SOURCE-20260206-019-0014
**Lines**: 98-101
**Context**: method / evidence
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> To achieve a 12x reduction in invocations, replace an AI model checking API token validity during every heartbeat with a 6-hour cron job running a script that returns an exit code, only waking the model on failure.

### ATOM-SOURCE-20260206-019-0015
**Lines**: 104-107
**Context**: method / evidence
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> Achieve a 5x cost reduction and isolate 168k tokens by using a Haiku sub-agent for browser automation instead of a premium model like Opus.

### ATOM-SOURCE-20260206-019-0016
**Lines**: 112-117
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Write scripts that output nothing on success; configure cron jobs to only send output to the AI model if the script produces it, indicating a non-OK result.

### ATOM-SOURCE-20260206-019-0017
**Lines**: 120-121
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Set `delivery: "none"` by default for most cron jobs, having the agent explicitly send messages only when warranted, to avoid unnecessary notifications.

### ATOM-SOURCE-20260206-019-0018
**Lines**: 124-130
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Pre-format data (e.g., tables, summaries) within scripts so the AI model's job becomes 'send this' rather than 'understand this data and present it nicely'.

### ATOM-SOURCE-20260206-019-0019
**Lines**: 133-134
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Run every cron job in `sessionTarget: "isolated"` to keep the main AI session context clean and prevent scheduled tasks from polluting conversation history.

### ATOM-SOURCE-20260206-019-0020
**Lines**: 137-142
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Explicitly set the model in cron job payloads (e.g., `"model": "anthropic/claude-haiku-4-5"`) to match the task's complexity and cost requirements.

### ATOM-SOURCE-20260206-019-0021
**Lines**: 147-150
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Move routine, independent tasks (like backup sync or dispatch queue checks) from the AI agent's heartbeat to cron jobs, using cheaper models and silent reporting unless failure occurs.

### ATOM-SOURCE-20260206-019-0024
**Lines**: 159-159
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> For independent checks in an agent system, use cron jobs instead of heartbeats.

### ATOM-SOURCE-20260206-019-0026
**Lines**: 176-176
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> Use scripts for logic and models for judgment; if a task can be handled by an if statement, avoid using tokens on a model.

### ATOM-SOURCE-20260206-019-0027
**Lines**: 177-177
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> Tier your models by cost and capability: use Haiku for labor ($0.017/turn), Sonnet for craft, and Opus for conversation ($0.089/turn).

### ATOM-SOURCE-20260206-019-0028
**Lines**: 178-178
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> Keep models silent by default, only invoking them when there is something specific to communicate.

### ATOM-SOURCE-20260206-019-0029
**Lines**: 179-179
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> Ensure scheduled work runs in isolated sessions to prevent it from polluting the main context of an agent system.

### ATOM-SOURCE-20260206-019-0030
**Lines**: 180-180
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> Verify model names carefully, as a typo can silently cause a fallback to more expensive default models.
