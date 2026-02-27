# Extraction: SOURCE-20260207-016

**Source**: `SOURCE-20260207-x-article-voxyz_ai-the_full_tutorial_6_ai_agents_that_run_a_company_how_i_built_them_from_scratch.md`
**Atoms extracted**: 65
**Categories**: analogy, claim, concept, framework, praxis_hook

---

## Analogy (1)

### ATOM-SOURCE-20260207-016-0022
**Lines**: 280-282
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.00, actionability=0.60, epistemic_stability=0.90

> In a multi-agent system, the VPS is like an employee doing the work, Vercel is like the boss issuing directives, and Supabase is like the company's shared documentation that everyone reads from and writes to.

## Claim (9)

### ATOM-SOURCE-20260207-016-0002
**Lines**: 24-24
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> A functional AI agent system can be built using Next.js, Supabase, and a Virtual Private Server (VPS), with a monthly cost of $8 fixed plus LLM usage.

### ATOM-SOURCE-20260207-016-0003
**Lines**: 26-27
**Context**: consensus / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> An AI agent system can be implemented without relying on OpenAI Assistants API, LangChain, or AutoGPT, instead using PostgreSQL, Node.js workers, and a rule engine.

### ATOM-SOURCE-20260207-016-0020
**Lines**: 266-269
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> Using a queue for agent reactions, rather than immediate execution, allows reactions to pass through the same proposal gates (quota checks, auto-approve, cap gates) as other tasks, and facilitates inspection and debugging.

### ATOM-SOURCE-20260207-016-0023
**Lines**: 289-295
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> Conversations are crucial for emergent intelligence in multi-agent systems, facilitating information synchronization, emergent decision-making, serving as a source for lessons learned, and enhancing user engagement through dynamic interactions.

### ATOM-SOURCE-20260207-016-0026
**Lines**: 319-320
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> Differing viewpoints among AI agents are crucial for valuable conversations.

### ATOM-SOURCE-20260207-016-0031
**Lines**: 408-410
**Context**: anecdote / evidence
**Tension**: novelty=0.30, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.60

> Weighted randomness in speaker selection makes AI agent conversations feel more real, allowing agents with good relationships to riff off each other while still enabling unexpected participants.

### ATOM-SOURCE-20260207-016-0035
**Lines**: 462-464
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.60, actionability=0.50, epistemic_stability=0.80

> AI agents without memory will repeatedly make the same mistakes or suggestions, such as suggesting more weekend posts despite previous low engagement.

### ATOM-SOURCE-20260207-016-0056
**Lines**: 725-726
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.60, actionability=0.30, epistemic_stability=0.90

> An agent without enough experience will propose generic, surface-level ideas.

### ATOM-SOURCE-20260207-016-0064
**Lines**: 802-808
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.20, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Rule-driven systems for deriving agent personality modifiers are deterministic, cost-effective (zero additional LLM calls), and debuggable, unlike LLM-based approaches which can hallucinate or be difficult to trace.

## Concept (5)

### ATOM-SOURCE-20260207-016-0007
**Lines**: 56-58
**Context**: consensus / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.70

> A 'Proposal' in an AI agent system is an agent's request, such as a social media agent wanting to post a tweet, which the system then reviews for approval or rejection.

### ATOM-SOURCE-20260207-016-0012
**Lines**: 120-122
**Context**: consensus / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> A 'Heartbeat' in an AI agent system is a periodic function (e.g., every 5 minutes) that checks and processes critical system components like triggers, reaction queues, insights, outcomes, and recovers stuck tasks or conversations.

### ATOM-SOURCE-20260207-016-0045
**Lines**: 599-603
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> Agent memory is structured knowledge distilled from experience, distinct from chat history, with each memory having a type, confidence score, and tags for efficient retrieval.

### ATOM-SOURCE-20260207-016-0053
**Lines**: 695-699
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.80

> An "Initiative" in an agent system refers to agents proactively proposing actions or ideas, in contrast to working reactively based on triggers, analogous to senior employees proposing plans versus junior employees waiting for assignments.

### ATOM-SOURCE-20260207-016-0059
**Lines**: 753-759
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.80

> Voice Evolution for agents means their speaking style changes to reflect accumulated experience, similar to how a human's communication style adapts based on their work experience (e.g., data analysts lead with numbers, customer service becomes more patient).

## Framework (12)

### ATOM-SOURCE-20260207-016-0005
**Lines**: 37-41
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> The core data model for an AI agent system consists of four tables forming a closed loop: `ops_mission_proposals` (agent ideas), `ops_missions` (approved tasks), `ops_mission_steps` (concrete execution steps), and `ops_agent_events` (event stream triggering new ideas).

### ATOM-SOURCE-20260207-016-0015
**Lines**: 153-189
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Trigger rules define conditions under which an agent proposal is created, specifying the trigger event, conditions, target agent, and cooldown period. They come in two flavors: reactive triggers (responding to past events like `tweet_high_engagement` or `mission_failed`) and proactive triggers (agents initiating work on a schedule, like `proactive_scan_signals` or `proactive_draft_tweet`).

### ATOM-SOURCE-20260207-016-0018
**Lines**: 224-254
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> The reaction matrix defines how agents respond to each other's actions. It's a JSON policy specifying patterns with `source` agent, event `tags`, `target` agent, reaction `type`, `probability` of reaction, and a `cooldown` period.

### ATOM-SOURCE-20260207-016-0021
**Lines**: 273-278
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> A multi-agent system can be structured into three layers: a VPS (agents' brain + hands for thinking and executing tasks), Vercel (agents' process manager for approving proposals, evaluating triggers, and health monitoring), and Supabase (agents' shared memory, serving as the single source of truth for all state and data).

### ATOM-SOURCE-20260207-016-0027
**Lines**: 326-343
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> Agent personas can be defined with a display name, tone (e.g., 'direct, results-oriented'), a quirk (e.g., 'Always asks for deadlines'), and a systemDirective (a prompt for the AI describing its personality and speaking style).

### ATOM-SOURCE-20260207-016-0029
**Lines**: 353-376
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Three essential conversation formats for AI agents are: Standup (4-6 agents, 6-12 turns, coordinator speaks first, purpose: align priorities), Debate (2-3 agents, 6-10 turns, temperature 0.8 for creativity/conflict, purpose: resolve disagreements), and Watercooler (2-3 agents, 2-5 turns, temperature 0.9 for casualness, purpose: generate insights from informal chat).

### ATOM-SOURCE-20260207-016-0032
**Lines**: 412-422
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> An AI agent daily schedule can be designed with 24 time slots, assigning different conversation formats (e.g., Morning Standup, Afternoon Deep-dive, Evening Watercooler) and probabilities (40%-100%) to each slot to create a natural rhythm.

### ATOM-SOURCE-20260207-016-0036
**Lines**: 466-475
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> Five types of memory for AI agents include: insight (discovery, e.g., 'Users prefer tweets with data'), pattern (pattern recognition, e.g., 'Weekend posts get 30% less engagement'), and strategy (strategy summary, e.g., 'Teaser before main post works better').

### ATOM-SOURCE-20260207-016-0037
**Lines**: 470-479
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.70

> There are 5 types of agent memory: insight (discovery), pattern (pattern recognition), strategy (strategy summary), preference (preference record), and lesson (lesson learned from failure).

### ATOM-SOURCE-20260207-016-0046
**Lines**: 610-620
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> An affinity system for agents tracks relationships between pairs of agents with an affinity value (0.10-0.95), total interactions, positive interactions, negative interactions, and a drift log.

### ATOM-SOURCE-20260207-016-0048
**Lines**: 626-634
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> An agent system can be initialized with 6 agents and 15 pairwise relationships, each having an initial affinity and a backstory, with deliberate low-affinity pairs to generate interesting conversations.

### ATOM-SOURCE-20260207-016-0052
**Lines**: 673-689
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> Agent affinity affects system behavior by influencing speaker selection (higher affinity, more likely to respond), conflict resolution (low-affinity pairs are automatically paired for conflict resolution), mentor pairing (high affinity + experience gap leads to mentoring conversations), and conversation tone (prompt's interaction type adjusts based on affinity, e.g., high tension leads to 'challenge' or 'critical', low tension to 'supportive' or 'agreement').

## Praxis Hook (38)

### ATOM-SOURCE-20260207-016-0001
**Lines**: 9-10
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> To build an AI agent system, you don't need to know how to code; you just need to know how to interact with an AI coding assistant.

### ATOM-SOURCE-20260207-016-0004
**Lines**: 29-29
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> To start an AI agent system, begin with three agents: a coordinator, an executor, and an observer, to establish a fully working loop.

### ATOM-SOURCE-20260207-016-0006
**Lines**: 53-53
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> To create database tables for an AI agent system, provide table definitions to an AI coding assistant and ask it to generate Supabase SQL migrations.

### ATOM-SOURCE-20260207-016-0008
**Lines**: 62-64
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.80

> Implement a single proposal intake pipeline as the sole entry point for all proposals in an AI agent system, regardless of their origin (agent initiative, automatic trigger, or another agent's reaction), to ensure consistent approval processes.

### ATOM-SOURCE-20260207-016-0009
**Lines**: 68-70
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.80

> Before inserting a proposal, check 'Cap Gates' (e.g., daily limits, quotas) and reject the proposal immediately if limits are met, preventing tasks from piling up in the queue.

### ATOM-SOURCE-20260207-016-0010
**Lines**: 96-96
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> Log rejected proposals for audit trails instead of silently dropping them.

### ATOM-SOURCE-20260207-016-0011
**Lines**: 99-100
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.80

> Store quotas and feature flags in an `ops_policy` table with a key-value (JSONB) structure, rather than hardcoding them, to allow for dynamic adjustments without redeployment.

### ATOM-SOURCE-20260207-016-0013
**Lines**: 142-149
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.00, speculation_risk=0.60, actionability=0.90, epistemic_stability=0.90

> To schedule tasks on a Linux system, use crontab. The `*/5 * * * *` syntax means the command will run every 5 minutes. For Vercel deployments, use its built-in cron functionality instead of crontab.

### ATOM-SOURCE-20260207-016-0014
**Lines**: 149-149
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.80

> Implement a system heartbeat where each step is wrapped in a try-catch block to prevent one failing component from taking down the entire system.

### ATOM-SOURCE-20260207-016-0016
**Lines**: 210-213
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.00, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> Proactive triggers can incorporate randomness to simulate natural behavior, including a skip probability (e.g., 10-15% chance of not firing), topic rotation, and jitter (e.g., 25-45 minute random delay) to prevent simultaneous firing.

### ATOM-SOURCE-20260207-016-0017
**Lines**: 215-220
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> When evaluating triggers, prioritize checking cooldowns (cheap) before calling potentially expensive checker functions. Implement a budget (e.g., 4 seconds) for the evaluator; if the budget is exceeded, remaining rules should wait for the next heartbeat to prevent serverless function timeouts.

### ATOM-SOURCE-20260207-016-0019
**Lines**: 256-264
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To manage agent-to-agent reactions: 1) Log agent actions as events with tags. 2) Use an event hook to check the reaction matrix for matching patterns. 3) If a pattern matches and passes probability/cooldown checks, add the reaction to a queue. 4) Process the reaction queue during the next heartbeat to create proposals, ensuring reactions go through standard safety gates like quota checks.

### ATOM-SOURCE-20260207-016-0024
**Lines**: 290-292
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> To design agent voices, assign each agent a persona including tone, quirks, and signature phrases to make conversations interesting.

### ATOM-SOURCE-20260207-016-0025
**Lines**: 299-300
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.00, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.60

> To make agent conversations engaging, design a distinct 'persona' for each agent, including a specific tone, quirks, and signature phrases.

### ATOM-SOURCE-20260207-016-0028
**Lines**: 347-349
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> To generate a systemDirective for an AI agent, describe the desired personality in one sentence and use an AI coding assistant to expand it into a complete prompt.

### ATOM-SOURCE-20260207-016-0030
**Lines**: 393-406
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> To simulate realistic conversation flow among AI agents, use weighted randomness for speaker selection, where weights are influenced by factors like affinity to the last speaker, recency of speaking, and a random jitter.

### ATOM-SOURCE-20260207-016-0033
**Lines**: 428-435
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> To orchestrate AI agent conversations, a worker polls a queue for tasks, generates dialogue turn by turn using LLM calls, caps each turn at 120 characters to enforce human-like brevity, extracts memories, and fires events for frontend visibility.

### ATOM-SOURCE-20260207-016-0034
**Lines**: 454-458
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> When prototyping an AI roundtable conversation worker, describe desired conversation formats and agent voice descriptions, then instruct an AI coding assistant to build the worker using a specified queue system (e.g., Supabase) and turn-by-turn LLM generation.

### ATOM-SOURCE-20260207-016-0038
**Lines**: 483-494
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To implement agent memory, store memories in a database table (e.g., `ops_agent_memory`) with fields for `agent_id`, `type`, `content`, `confidence`, `tags`, `source_trace_id` (for idempotent deduplication), and `superseded_by` (for versioning).

### ATOM-SOURCE-20260207-016-0039
**Lines**: 500-511
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> Memories can be distilled from conversation history by sending the full conversation to an LLM, instructing it to extract insights, patterns, or lessons in a JSON format.

### ATOM-SOURCE-20260207-016-0040
**Lines**: 513-517
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Implement idempotent deduplication for memories using a `source_trace_id` to prevent duplicate writes, especially when processes run periodically.

### ATOM-SOURCE-20260207-016-0041
**Lines**: 520-524
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> When distilling memories, enforce constraints such as a maximum number of memories per conversation (e.g., 6), a minimum confidence threshold (e.g., 0.55), and a cap on total memories per agent (e.g., 200, overwriting oldest).

### ATOM-SOURCE-20260207-016-0042
**Lines**: 529-539
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Agents can learn from outcomes by periodically fetching performance data (e.g., tweet metrics), calculating a baseline (e.g., median engagement rate), and writing 'lesson' memories with varying confidence based on strong or weak performance relative to the baseline.

### ATOM-SOURCE-20260207-016-0043
**Lines**: 549-569
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.30, actionability=0.80, epistemic_stability=0.60

> To ensure memories influence agent behavior without stifling exploration, implement a probabilistic mechanism (e.g., 30% chance) where memories (strategies, lessons) can override or enrich topic selection, while allowing a baseline behavior for the remaining percentage.

### ATOM-SOURCE-20260207-016-0044
**Lines**: 575-580
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Optimize memory queries by using a cache (e.g., `Map<agentId, MemoryEntry[]>`) at the entry point of trigger evaluation, ensuring that an agent's memories are fetched from the database only once per evaluation cycle.

### ATOM-SOURCE-20260207-016-0047
**Lines**: 622-626
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> When storing agent relationships, use a `CHECK(agent_a < agent_b)` constraint on agent IDs to ensure alphabetical ordering and prevent duplicate records for the same pair (e.g., 'analyst-boss' vs. 'boss-analyst').

### ATOM-SOURCE-20260207-016-0049
**Lines**: 634-637
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.30, actionability=0.80, epistemic_stability=0.60

> Deliberately create initial low-affinity pairs between agents to foster more interesting conversations, debates, and conflict resolution, as universally high affinity can lead to boring interactions.

### ATOM-SOURCE-20260207-016-0050
**Lines**: 636-639
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> When setting up agent relationships, deliberately create a few "low affinity" pairs to produce more interesting conversations during debates and conflict resolution, as high affinity among all agents leads to boring interactions.

### ATOM-SOURCE-20260207-016-0051
**Lines**: 643-669
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> Implement a relationship drift mechanism where an LLM call for memory distillation also outputs pairwise relationship drift, with strict rules: max drift ±0.03 per conversation, affinity floor 0.10, affinity ceiling 0.95, and keeping the last 20 drift_log entries.

### ATOM-SOURCE-20260207-016-0054
**Lines**: 701-714
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.60

> To implement an initiative system for agents, separate the lightweight enqueueing process (Heartbeat) from the heavy LLM-based generation process (VPS worker) to avoid Vercel function timeouts and ensure reliability, where Heartbeat identifies agents due for an initiative and enqueues them, and a VPS worker consumes the queue to generate proposals using a cheap and fast LLM.

### ATOM-SOURCE-20260207-016-0055
**Lines**: 716-723
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> To ensure valuable initiative proposals from agents, set enqueue conditions such as a cooldown (max 1 per 4 hours) and prerequisites like having at least 5 high-confidence memories and outcome lessons, ensuring the agent has sufficient "accumulated experience."

### ATOM-SOURCE-20260207-016-0057
**Lines**: 729-745
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> Derive action items from specific conversation formats like standup, war_room, and brainstorm, but not informal chats, by piggybacking on the memory distillation LLM call to generate action items with titles, assigned agents, and step kinds, converting a maximum of 3 action items per day into missions.

### ATOM-SOURCE-20260207-016-0058
**Lines**: 747-749
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Ensure that all steps of the agent initiative process, including agents proposing their own work, go through full proposal-service gates (quota checks, auto-approve, cap gates) to maintain safety mechanisms.

### ATOM-SOURCE-20260207-016-0060
**Lines**: 763-770
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.60

> To implement agent voice evolution, derive personality dynamically from existing memory tables by calculating voice modifiers based on an agent's memory distribution (e.g., lesson count, tags, pattern count) before each conversation, rather than storing a separate personality score.

### ATOM-SOURCE-20260207-016-0061
**Lines**: 773-800
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> To implement dynamic agent personality, use a rule-driven system to derive 'voice modifiers' based on agent statistics, then inject these modifiers into the agent's system prompt before a conversation begins.

### ATOM-SOURCE-20260207-016-0062
**Lines**: 782-786
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.20, speculation_risk=0.60, actionability=0.90, epistemic_stability=0.70

> Use rule-driven logic instead of LLMs for deriving agent voice modifiers because rules are deterministic, cost nothing, and are debuggable, preventing unpredictable results or hallucinations.

### ATOM-SOURCE-20260207-016-0063
**Lines**: 789-794
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> Inject derived voice modifiers into an agent's system prompt before a conversation starts by appending them to the base voice's system directive.

### ATOM-SOURCE-20260207-016-0065
**Lines**: 809-811
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Cache an agent's voice modifiers once per conversation to avoid re-querying them on every turn.
