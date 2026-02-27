# Extraction: SOURCE-20260208-006

**Source**: `SOURCE-20260208-x-article-jumperz-i_built_an_ai_agent_swarm_in_discord_it_works_better_than_anything_ive_tried_full_guide.md`
**Atoms extracted**: 25
**Categories**: claim, framework, praxis_hook, prediction

---

## Claim (5)

### ATOM-SOURCE-20260208-006-0007
**Lines**: 70-71
**Context**: consensus / evidence
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.60, actionability=0.60, epistemic_stability=0.80

> Cheaper AI models are sufficient for tasks like data scraping or writing content that will undergo human review, as the final output is not raw AI generation.

### ATOM-SOURCE-20260208-006-0016
**Lines**: 155-158
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.60

> Specific agents, such as a 'Find' agent, 'Create' agent, and 'Build' agent, can remember specialized knowledge like preferred data sources, writing styles, and tech stacks, leading to automatic knowledge compounding.

### ATOM-SOURCE-20260208-006-0018
**Lines**: 170-173
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> The system operates continuously with heartbeats every 30 minutes, cron jobs for scheduled tasks, and event triggers for real-world reactions, providing users with morning briefs on overnight activities.

### ATOM-SOURCE-20260208-006-0021
**Lines**: 203-209
**Context**: consensus / evidence
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> Discord is an effective platform for AI coordination because its features (channels for workspaces, threading for deep work, permissions for access control, search, unlimited history, and mobile app) eliminate the need to build these functionalities from scratch.

### ATOM-SOURCE-20260208-006-0024
**Lines**: 243-245
**Context**: consensus / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.30, actionability=0.50, epistemic_stability=0.60

> Agent coordination is the fundamental architecture for future AI systems, as models become cheaper and context windows larger, making the orchestration layer crucial for utility.

## Framework (6)

### ATOM-SOURCE-20260208-006-0003
**Lines**: 28-31
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> The AI agent system uses a 'Coordinator' model that reads user tasks, breaks them into sub-tasks, and delegates them to specialized agents without performing the work itself.

### ATOM-SOURCE-20260208-006-0004
**Lines**: 43-50
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> A core team of five specialized AI agents can be used: 'Find' (Research), 'Build' (Implement), 'Track' (Measure), 'Watch' (Observe), and 'Create' (Write), each running as independent, parallel sessions.

### ATOM-SOURCE-20260208-006-0008
**Lines**: 84-92
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Each AI agent should have three dedicated Discord channels: 'Output' for results, 'Logs' for debug information and thought processes, and 'Memory' for persistent knowledge, effectively using Discord channels as a searchable, threaded, and persistent database.

### ATOM-SOURCE-20260208-006-0015
**Lines**: 150-153
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> An agent's memory system consists of two layers: shared team memory (e.g., Discord channels) and private agent memory (e.g., local .md files), allowing agents to retain knowledge and improve over time.

### ATOM-SOURCE-20260208-006-0017
**Lines**: 162-166
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> Agent DNA, or local configuration, is defined by SOUL.md (personality), AGENTS.md (rules), and MEMORY.md (knowledge), and resides on the user's machine, ensuring ownership of the agent's core identity.

### ATOM-SOURCE-20260208-006-0020
**Lines**: 193-196
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> The infrastructure for this system uses Discord for coordination and persistence, and an OpenClaw gateway on the user's machine to connect to AI model providers, leveraging Discord's free and reliable features.

## Praxis Hook (12)

### ATOM-SOURCE-20260208-006-0001
**Lines**: 7-7
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> An AI agent coordination system can be built within a Discord server where agents communicate, split work, and deliver results.

### ATOM-SOURCE-20260208-006-0002
**Lines**: 15-24
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Users can initiate tasks for an AI agent system by typing plain English commands into a designated Discord channel (e.g., #orders), such as "Research the top 10 AI coding tools and write a comparison thread" or "Build a landing page for my new SaaS idea."

### ATOM-SOURCE-20260208-006-0005
**Lines**: 52-55
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.60

> Assigning names to AI agents (e.g., Scout, Max, John, Maya) helps in remembering and referencing them, and allows the coordinator to recognize them more easily.

### ATOM-SOURCE-20260208-006-0006
**Lines**: 67-77
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> To optimize costs, use expensive 'smart models' (e.g., Claude Opus) only for the Coordinator and 'Build' agents, while using cheaper, faster models (e.g., Claude Haiku, Sonnet) for 'Find', 'Track', 'Watch', and 'Create' agents, as their output is often reviewed by humans.

### ATOM-SOURCE-20260208-006-0009
**Lines**: 98-105
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> To scale efficiently, agents can spawn temporary 'intern' workers for specific tasks, which are then dismissed, allowing for workload-based scaling without permanent cost.

### ATOM-SOURCE-20260208-006-0010
**Lines**: 113-124
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Agents should communicate directly with each other in a dedicated channel (e.g., #agent-chat) to report status ('done', 'stuck') or hand off tasks, facilitating faster coordination than routing everything through the central coordinator.

### ATOM-SOURCE-20260208-006-0011
**Lines**: 128-134
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> The Coordinator agent is responsible for synthesizing the raw outputs from multiple agents into a single, polished, human-readable result, connecting dots and cleaning up messy data.

### ATOM-SOURCE-20260208-006-0012
**Lines**: 138-141
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> To monitor agent activity, use a dashboard for daily summaries and a live feed for real-time observation, allowing for high-level overviews or deep dives as needed.

### ATOM-SOURCE-20260208-006-0013
**Lines**: 140-143
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> Implement a dashboard and live feed using Discord channels to provide a high-level overview of daily activity and allow real-time monitoring of agents' work.

### ATOM-SOURCE-20260208-006-0014
**Lines**: 147-149
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> Agents should read their dedicated memory channels upon spawning to retain knowledge from previous runs, enabling them to become 'smarter' over time.

### ATOM-SOURCE-20260208-006-0019
**Lines**: 179-189
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> To enable self-improvement for agents, users can drop links into a designated channel (e.g., #drop-links), which the system then automatically summarizes, extracts takeaways, and archives, making the agents smarter with each input.

### ATOM-SOURCE-20260208-006-0022
**Lines**: 226-234
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To set up the system, users must create a Discord server, obtain a Discord Bot Token, connect Discord to OpenClaw, ensure LLM, OpenClaw, and Discord are linked, name their coordinator, assign the first task, and add more agents as needed, allowing the coordinator to manage subsequent actions.

## Prediction (2)

### ATOM-SOURCE-20260208-006-0023
**Lines**: 238-241
**Context**: speculation / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.20, speculation_risk=0.80, actionability=0.30, epistemic_stability=0.30

> Within two years, every company will run a system similar to this orchestration of one coordinator and a few agents, evolving into swarms of hundreds of agents coordinating in real-time to split complex problems into micro-tasks.

### ATOM-SOURCE-20260208-006-0025
**Lines**: 247-248
**Context**: speculation / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.70, actionability=0.40, epistemic_stability=0.40

> The cost of AI models will continue to decrease, allowing users to run at least five agents on Discord for minimal expense.
