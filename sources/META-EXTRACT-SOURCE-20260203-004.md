# Extraction: SOURCE-20260203-004

**Source**: `SOURCE-20260203-internal-research-diviner-response_openclaw_deep_research.md`
**Atoms extracted**: 69
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (24)

### ATOM-SOURCE-20260203-004-0001
**Lines**: 4-7
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.30, epistemic_stability=0.70

> The OpenClaw platform is an autonomous agent runtime environment that shifts from ephemeral, cloud-hosted chat interfaces to a persistent, local-first, event-driven architecture.

### ATOM-SOURCE-20260203-004-0003
**Lines**: 10-12
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.40, epistemic_stability=0.70

> OpenClaw's architecture supports long-running, multi-turn workflows, autonomous background processing, and complex multi-agent topologies on a single host.

### ATOM-SOURCE-20260203-004-0005
**Lines**: 17-20
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> The Gateway binds to a local control plane (defaulting to WebSocket on 127.0.0.1:18789) and provides a unified API for local UIs and remote control interfaces.

### ATOM-SOURCE-20260203-004-0006
**Lines**: 20-24
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.40, epistemic_stability=0.60

> OpenClaw's design decouples the agent's cognitive runtime (LLM inference) from the I/O layer, allowing it to persist across UI restarts and handle asynchronous events like cron jobs or webhooks.

### ATOM-SOURCE-20260203-004-0009
**Lines**: 35-39
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.40, epistemic_stability=0.70

> OpenClaw's interaction model is fundamentally Event-Driven, where the Gateway normalizes signals from various sources (messages, temporal events, hardware interrupts) into a standard event format and routes them deterministically to the appropriate Agent Runtime.

### ATOM-SOURCE-20260203-004-0010
**Lines**: 39-43
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.40, epistemic_stability=0.60

> The routing logic in OpenClaw is crucial for its multi-agent capabilities, enabling a single inbound communication channel (e.g., a WhatsApp phone number) to serve multiple distinct agent personalities based on the sender's identity.

### ATOM-SOURCE-20260203-004-0011
**Lines**: 47-51
**Context**: consensus / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.70

> OpenClaw replaces unstructured shell-script 'skills' with typed, first-class tools that offer structured inputs, outputs, and validation, enhancing reliability and security by allowing the Gateway to enforce strict schema validation.

### ATOM-SOURCE-20260203-004-0013
**Lines**: 60-60
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> The `exec` tool supports both synchronous execution for immediate feedback and asynchronous execution for long-running tasks.

### ATOM-SOURCE-20260203-004-0014
**Lines**: 61-62
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Access to the `exec` tool is heavily gated by the tool restriction chain due to its security implications as the primary vector for system modification.

### ATOM-SOURCE-20260203-004-0015
**Lines**: 62-64
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> The `elevated` parameter in the `exec` tool allows an agent to request host-level access, bypassing sandbox constraints, if global and agent-specific policies permit.

### ATOM-SOURCE-20260203-004-0017
**Lines**: 79-81
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.80

> The `process` tool maintains a registry of backgrounded processes and allows agents to attach to them to read logs, send input to stdin, or terminate them.

### ATOM-SOURCE-20260203-004-0019
**Lines**: 82-83
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.80

> The `log` action of the `process` tool supports pagination via offset and limit to prevent context window overflow when reading large build logs.

### ATOM-SOURCE-20260203-004-0022
**Lines**: 100-102
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> The Gateway enforces strict session binding for message tool calls, constraining them to the target of the active session to prevent accidental or malicious broadcasting of private responses to different channels or users.

### ATOM-SOURCE-20260203-004-0031
**Lines**: 145-146
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> Session data in OpenClaw is strictly isolated per agent to prevent context contamination, stored at `~/.openclaw/agents/<agentId>/sessions/`.

### ATOM-SOURCE-20260203-004-0033
**Lines**: 162-162
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> The `sessions_spawn` tool in OpenClaw instantiates a full Agent Runtime context, not merely calling another model, when invoked.

### ATOM-SOURCE-20260203-004-0035
**Lines**: 169-172
**Context**: anecdote / evidence
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.30, epistemic_stability=0.70

> A critical flaw in earlier versions of OpenClaw, known as the "Herbert Yang" issue, involved `agentId` and `model` overrides in `sessions_spawn` failing to propagate routing context correctly, leading to "malformed tool calls" or 400 errors from providers like OpenRouter.

### ATOM-SOURCE-20260203-004-0037
**Lines**: 172-175
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> Release 2026.2.2 of OpenClaw, attributed to @justinhuangcode, fixed the "Herbert Yang" issue by ensuring that `accountId` and binding contexts are correctly inherited by the embedded run, allowing sub-agents to utilize the correct provider credentials and routing identities.

### ATOM-SOURCE-20260203-004-0039
**Lines**: 178-178
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> OpenClaw implements aggressive hygiene protocols to manage the finite context window of LLMs.

### ATOM-SOURCE-20260203-004-0047
**Lines**: 215-215
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> OpenClaw adheres to the AgentSkills specification, a standardized format for portable agent capabilities that allows skills to be shared, versioned, and gated.

### ATOM-SOURCE-20260203-004-0053
**Lines**: 265-265
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> OpenClaw's configuration file (`openclaw.json`) supports complex multi-agent setups through the `agents.list` array.

### ATOM-SOURCE-20260203-004-0057
**Lines**: 309-309
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> OpenClaw implements a defense-in-depth security model, which is critical for a system that allows LLMs to execute shell commands.

### ATOM-SOURCE-20260203-004-0060
**Lines**: 319-320
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> OpenClaw employs a defense-in-depth security model, which is crucial for a system that permits LLMs to execute shell commands.

### ATOM-SOURCE-20260203-004-0063
**Lines**: 342-348
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> OpenClaw's sandboxing strategy is built on Docker and offers three modes: 'off' (tools run on host, high risk/power), 'non-main' (only main session on host, groups/cron in sandbox), and 'all' (everything runs in sandbox).

### ATOM-SOURCE-20260203-004-0064
**Lines**: 349-352
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> OpenClaw's sandboxing strategy offers three scopes: 'session' (fresh container per session, most secure but slower), 'agent' (persistent container per agent), and 'shared' (single container shared by multiple agents).

## Concept (15)

### ATOM-SOURCE-20260203-004-0002
**Lines**: 7-10
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.40, epistemic_stability=0.60

> OpenClaw operates as a continuous daemon, called the Gateway, which maintains a persistent event loop, unlike traditional Request-Response models where an agent is dormant until queried.

### ATOM-SOURCE-20260203-004-0004
**Lines**: 14-17
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> The Gateway is an always-on process at the core of the OpenClaw system, functioning as its central nervous system, responsible for protocol multiplexing, session state management, token accounting, and agent loop orchestration.

### ATOM-SOURCE-20260203-004-0007
**Lines**: 26-29
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.40, epistemic_stability=0.60

> Agents in OpenClaw are logical units of cognition, each with a distinct identity, workspace, session store, and configuration profile, architecturally isolated with their own memory banks and permission scopes.

### ATOM-SOURCE-20260203-004-0008
**Lines**: 29-33
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.40, epistemic_stability=0.60

> Nodes in OpenClaw are paired devices (iOS/Android endpoints, secondary desktop clients) that form a distributed hardware mesh, extending the agent's sensory and actuation range by exposing their hardware capabilities to the Gateway.

### ATOM-SOURCE-20260203-004-0012
**Lines**: 56-58
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> The `exec` tool is the foundational primitive for system interaction in OpenClaw, allowing agents to execute shell commands within configured environments (host OS or Dockerized sandbox).

### ATOM-SOURCE-20260203-004-0016
**Lines**: 75-77
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.80

> The `process` tool in OpenClaw manages the lifecycle of commands initiated by the `exec` tool, allowing agents to monitor complex builds or servers asynchronously.

### ATOM-SOURCE-20260203-004-0021
**Lines**: 88-92
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> The message tool is a unified abstraction layer for all supported chat protocols (Discord, Slack, WhatsApp, Telegram, Signal, iMessage, MS Teams), allowing the agent to use the same 'send' action regardless of the underlying transport, with the Gateway handling protocol-specific translation.

### ATOM-SOURCE-20260203-004-0023
**Lines**: 108-109
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> Agentic Concurrency is achieved through the `sessions_spawn` tool, which allows an agent to fork execution by spawning a sub-agent to perform a specific task in isolation.

### ATOM-SOURCE-20260203-004-0030
**Lines**: 140-141
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> In OpenClaw, a Session is the fundamental unit of state, representing a continuous thread of conversation and context, and is file-system backed rather than stored as database rows.

### ATOM-SOURCE-20260203-004-0043
**Lines**: 190-190
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> Compaction, distinct from pruning, summarizes older segments of conversation history into persistent memory notes, freeing up tokens in the sliding window without losing semantic content.

### ATOM-SOURCE-20260203-004-0044
**Lines**: 192-192
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> The `sessionTarget` field in an OpenClaw cron job determines the execution context, fundamentally changing how the job executes, either in the `main` session loop or an `isolated` dedicated session.

### ATOM-SOURCE-20260203-004-0050
**Lines**: 250-252
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> The `{baseDir}` variable in OpenClaw skills resolves dynamically based on the skill's location, pointing to the agent's workspace for workspace skills or the global skills directory for shared skills, allowing reliable referencing of local assets or scripts.

### ATOM-SOURCE-20260203-004-0051
**Lines**: 256-257
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> Standalone Skills in OpenClaw are purely declarative (Markdown) and can only instruct the agent on how to use existing tools, without introducing new TypeScript/Node.js runtime logic.

### ATOM-SOURCE-20260203-004-0052
**Lines**: 258-261
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> Plugins in OpenClaw are integrated modules that can register new Tools via a `register` function and facilitate Skills via `openclaw.plugin.json`, required for adding new fundamental capabilities like binary-level interfaces to hardware devices.

### ATOM-SOURCE-20260203-004-0066
**Lines**: 376-382
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> Syncrescendence's memory system is repo-based, relying on a Git repository as the authoritative ground truth, while OpenClaw uses a hybrid approach with durable MEMORY.md, ephemeral daily logs (memory/YYYY-MM-DD.md), and a hybrid SQLite Vector Search + FTS5 index for search.

## Framework (16)

### ATOM-SOURCE-20260203-004-0018
**Lines**: 80-82
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> The browser tool integrates with the agent's multimodal capabilities, allowing it to generate "AI snapshots" (semantic DOM representations optimized for LLM reading) or "Aria snapshots" (accessibility tree dumps).

### ATOM-SOURCE-20260203-004-0020
**Lines**: 83-84
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> The browser tool's action set includes: navigate, click, type, press (keys), hover, drag, fill (forms), screenshot, pdf, upload, and dialog (handle alerts).

### ATOM-SOURCE-20260203-004-0032
**Lines**: 153-159
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.60

> OpenClaw uses a deterministic key generation strategy to map external inputs to internal sessions, including formats for Single-Agent Mode (`agent:main:<mainKey>`), Multi-Agent Mode (`agent:<agentId>:<mainKey>`), Group Chats (`agent:<agentId>:<channel>:group:<id>`), and Sub-Agents (`agent:<agentId>:subagent:<uuid>`).

### ATOM-SOURCE-20260203-004-0034
**Lines**: 164-168
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.60

> When `sessions_spawn` is invoked, it involves forking (generating a unique session key for the sub-agent), context construction (creating a fresh context window), and isolation (sub-agent runs with its own tool permissions, by default unable to spawn further sub-agents).

### ATOM-SOURCE-20260203-004-0036
**Lines**: 169-169
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> OpenClaw's Cron system provides temporal drive, transforming it from a reactive bot into a proactive agent.

### ATOM-SOURCE-20260203-004-0038
**Lines**: 173-179
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> A cron job in OpenClaw is defined by a structured object with fields for `name` (human-readable identifier), `schedule` (timing definition), `payload` (execution logic and target), and `sessionTarget` (execution context: main or isolated).

### ATOM-SOURCE-20260203-004-0040
**Lines**: 180-183
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.60

> OpenClaw's session expiration includes a daily reset (sessions roll over at 04:00 AM local time, archiving the previous day's chat) and an idle reset (a new session starts if inactive for a configurable `idleMinutes` duration).

### ATOM-SOURCE-20260203-004-0041
**Lines**: 183-188
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> OpenClaw's cron schedule object supports three modes: `at` for one-shot execution at a specific UTC ISO timestamp (with optional delete-after-run), `every` for recurring intervals (e.g., "30m", "1h"), and `cron` for standard 5-field Unix cron syntax.

### ATOM-SOURCE-20260203-004-0042
**Lines**: 184-189
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.60

> OpenClaw's pruning strategy, executed before every LLM call if `mode: "cache-ttl"` is active, removes verbose `toolResult` messages older than a defined `ttl` (default: 5 minutes), while user and assistant messages are never pruned, and the last `keepLastAssistants` (default: 3) tool results are preserved.

### ATOM-SOURCE-20260203-004-0048
**Lines**: 219-239
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> An OpenClaw Skill is defined by a directory containing a SKILL.md file, which combines YAML Frontmatter metadata (e.g., name, description, user-invocable, disable-model-invocation, command-dispatch, command-tool, and OpenClaw-specific metadata like OS gating, binary dependencies, environment variables, and config keys) with a Markdown instruction body for prompt injection.

### ATOM-SOURCE-20260203-004-0049
**Lines**: 243-248
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> OpenClaw resolves multiple skills with a strict hierarchy from highest to lowest priority: Workspace Skills (per-agent, user-owned), Managed Skills (local overrides shared across agents), and Bundled Skills (shipped with OpenClaw distribution).

### ATOM-SOURCE-20260203-004-0054
**Lines**: 283-290
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> OpenClaw's Gateway uses a deterministic "Most Specific Match Wins" Binding Resolution Order to route inbound messages to the correct agent, prioritizing Peer Match (exact User ID), then Guild/Team Match, Account Match (specific Channel Account), Channel Match (generic wildcard), and finally a Fallback to the default or first agent.

### ATOM-SOURCE-20260203-004-0059
**Lines**: 313-318
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> OpenClaw calculates tool permissions through an 8-layer hierarchy, applying a strict "Deny Wins" logic where if any layer denies a tool, it is blocked regardless of other allowances, starting with the Global Tool Profile (`tools.profile`).

### ATOM-SOURCE-20260203-004-0061
**Lines**: 323-326
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> OpenClaw's security architecture uses an 8-layer Tool Restriction Chain where permissions are calculated by filtering requested tool usage, and the 'Deny Wins' logic means any layer denying a tool blocks it.

### ATOM-SOURCE-20260203-004-0062
**Lines**: 328-339
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> The 8 layers of OpenClaw's Tool Restriction Chain are: Global Tool Profile, Global Provider Profile, Global Policy, Provider Policy, Agent Policy (primary user config), Agent Provider Policy, Sandbox Policy, and Sub-agent Policy.

### ATOM-SOURCE-20260203-004-0065
**Lines**: 357-373
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> The Syncrescendence constellation architecture (CAPTURE → DISPATCH → RETURN) maps to OpenClaw primitives: CAPTURE uses Gateway Event Loop, DISPATCH uses sessions_spawn/Routing, and RETURN uses the Announce Step.

## Praxis Hook (14)

### ATOM-SOURCE-20260203-004-0024
**Lines**: 111-119
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> The `sessions_spawn` tool takes parameters such as `task` (natural language instruction for the sub-agent), `label` (human-readable tag), `agentId` (target specific agent configuration), `model` (override default model), `runTimeoutSeconds` (hard timeout), and `cleanup` ('keep' or 'delete').

### ATOM-SOURCE-20260203-004-0025
**Lines**: 121-122
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> When `sessions_spawn` is used, it immediately returns a `runId` and `childSessionKey`, and the sub-agent executes asynchronously, with its result injected back into the parent session via an "Announce" step upon completion.

### ATOM-SOURCE-20260203-004-0026
**Lines**: 125-126
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> `sessions_send` enables inter-session communication and supports a `timeoutSeconds` parameter: if greater than 0, it acts as a synchronous RPC call waiting for a reply; if 0, it behaves as a fire-and-forget message.

### ATOM-SOURCE-20260203-004-0027
**Lines**: 127-127
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> `sessions_list` allows agents to discover active contexts, which can be filtered by kind (main, group, cron) or recency.

### ATOM-SOURCE-20260203-004-0028
**Lines**: 130-131
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> The `cron` tool manages the scheduler, allowing agents to self-schedule tasks using `add`, `update`, or `remove` actions, requiring a full job schema.

### ATOM-SOURCE-20260203-004-0029
**Lines**: 132-135
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> The `gateway` tool provides administrative control, including `config.get`, `config.patch` for hot updates, and `restart`, which reboots the Gateway process and requires explicit enablement in `openclaw.json` (`commands.restart: true`) to prevent accidental shutdowns.

### ATOM-SOURCE-20260203-004-0045
**Lines**: 195-201
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To execute an OpenClaw cron job within the primary session loop, set `sessionTarget: main` and use a `systemEvent` payload; this is suitable for tasks requiring awareness of recent user interactions like reminders or daily briefings, and triggers a heartbeat wakeup of the main agent.

### ATOM-SOURCE-20260203-004-0046
**Lines**: 202-210
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To execute an OpenClaw cron job in a dedicated, fresh session with zero context, set `sessionTarget: isolated` and use an `agentTurn` payload; this is ideal for heavy background processing, log scrubbing, or fetching external data without polluting the main context window, and the Gateway proactively spawns the new session immediately.

### ATOM-SOURCE-20260203-004-0055
**Lines**: 293-298
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To implement a "Shared Account" pattern in OpenClaw, where a single channel account serves multiple users, configure peer-specific bindings (e.g., `peer: "+1234..."` to Agent A and `peer: "+5678..."` to Agent B) so the Gateway routes messages to isolated agent instances, ensuring data privacy and context isolation.

### ATOM-SOURCE-20260203-004-0056
**Lines**: 302-305
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To enable direct agent-to-agent communication in OpenClaw, which is disabled by default to prevent loops, configure the `agentToAgent` tool in the allowlist; agents can then use the `message` tool or `sessions_send` to address each other as chat peers.

### ATOM-SOURCE-20260203-004-0058
**Lines**: 310-314
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.10, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To enable direct agent-to-agent communication in OpenClaw, configure the `agentToAgent` tool in the allowlist, then agents can use the `message` tool or `sessions_send` to communicate.

### ATOM-SOURCE-20260203-004-0067
**Lines**: 383-386
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> To integrate Syncrescendence's repo-truth with OpenClaw, bypass OpenClaw's vector store for authoritative data by configuring a skill that instructs the agent to use `exec` to directly grep or read the Syncrescendence repository.

### ATOM-SOURCE-20260203-004-0068
**Lines**: 389-392
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> OpenClaw can orchestrate external CLIs like Gemini or Claude Code by defining a Skill that uses the `exec` tool to run commands (e.g., `exec(command='gemini query "..."')`).

### ATOM-SOURCE-20260203-004-0069
**Lines**: 393-394
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To automate external CLI invocation in OpenClaw, use a cron job with `sessionTarget: "isolated"` to run a script that invokes CLIs, processes output, and reports back using the `message` tool (via curl webhook or `sessions_send`).
