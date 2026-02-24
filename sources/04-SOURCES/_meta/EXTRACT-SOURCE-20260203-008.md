# Extraction: SOURCE-20260203-008

**Source**: `SOURCE-20260203-internal-research-vanguard-response_openclaw_deep_research.md`
**Atoms extracted**: 53
**Categories**: claim, framework, praxis_hook

---

## Claim (8)

### ATOM-SOURCE-20260203-008-0008
**Lines**: 12-13
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.90

> Running tools in Docker sandboxes and using strict allowlists is strongly recommended when processing untrusted content in OpenClaw.

### ATOM-SOURCE-20260203-008-0009
**Lines**: 26-26
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> Sandboxing isolates file operations and limits prompt injection risks.

### ATOM-SOURCE-20260203-008-0028
**Lines**: 60-61
**Context**: anecdote / evidence
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> OpenClaw currently runs 24/7 on a static Mac mini, uses persistent file memory for conversations, and has multiple agents/skills set up for different tasks.

### ATOM-SOURCE-20260203-008-0029
**Lines**: 61-62
**Context**: anecdote / evidence
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Watcher scripts and a Slack protocol for coordination align with OpenClaw's multi-agent architecture, where each role has its own workspace.

### ATOM-SOURCE-20260203-008-0030
**Lines**: 64-64
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> Key security practices like sandboxing, allowlists, and authentication are missing in the current OpenClaw setup, as is a Brave API for search.

### ATOM-SOURCE-20260203-008-0031
**Lines**: 65-66
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> A disciplined skill governance process is needed for OpenClaw, as demonstrated by the "ClawHavoc" incident which showed the danger of unvetted skills.

### ATOM-SOURCE-20260203-008-0051
**Lines**: 168-169
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> Brave Search offers 2,000 free queries per month, with subsequent queries charged at $5 per 1,000 requests (up to 20 million queries) under the Base AI plan.

### ATOM-SOURCE-20260203-008-0052
**Lines**: 169-170
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.20, actionability=0.30, epistemic_stability=0.80

> Typical RAG usage, involving a few searches per task, is expected to remain within Brave Search's free query tier.

## Framework (1)

### ATOM-SOURCE-20260203-008-0035
**Lines**: 83-88
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> The "divide and conquer" strategy for AI orchestration involves using an orchestrator to spawn subtasks to different models based on their cost and capability (e.g., expensive models for refined input, cheap models for grunt work), then synthesizing the results.

## Praxis Hook (44)

### ATOM-SOURCE-20260203-008-0001
**Lines**: 3-5
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> To secure OpenClaw, bind the gateway to localhost only (`gateway.bind: "loopback"`), use the built-in gateway token, and lock down channels with allowlists or pairing.

### ATOM-SOURCE-20260203-008-0002
**Lines**: 5-6
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Use OpenClaw pairing or Slack/iMessage DM allowlists to ensure only authorized users can trigger the agent.

### ATOM-SOURCE-20260203-008-0003
**Lines**: 6-7
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Inspect and pin all plugins/skills before enabling them, treating npm-based plugins as untrusted code.

### ATOM-SOURCE-20260203-008-0004
**Lines**: 7-8
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Set workspace file permissions (e.g., `~/.openclaw/openclaw.json` to 600) and configure a firewall to block unwanted ports.

### ATOM-SOURCE-20260203-008-0005
**Lines**: 8-9
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Verify that the gateway is not exposed on `0.0.0.0` and use VPN/Tailscale for any remote access.

### ATOM-SOURCE-20260203-008-0006
**Lines**: 9-10
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Run an `openclaw security audit` to catch misconfigurations and require human approval for risky actions.

### ATOM-SOURCE-20260203-008-0007
**Lines**: 12-15
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Enable sandboxing and tool limits in OpenClaw by setting `agents.defaults.sandbox.mode="all"` with `workspaceAccess: "ro"` for agents that run tools, and deny dangerous tools (e.g., `exec`, `browser`, `process`) to non-owner agents.

### ATOM-SOURCE-20260203-008-0010
**Lines**: 27-28
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> Use the latest instruction-tuned models (e.g., Claude Opus 4.5, GPT-5.2) for any agent with tool access; weaker models (Sonnet, Haiku) should only process trusted input or run in a locked-down mode.

### ATOM-SOURCE-20260203-008-0011
**Lines**: 30-30
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Obtain a Brave Search API key and add it to the OpenClaw configuration to address the lack of a web search API.

### ATOM-SOURCE-20260203-008-0012
**Lines**: 31-32
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.90

> Consider running the OpenClaw gateway in a Docker container or VM for isolation, noting that the DigitalOcean 1-Click deploy uses container isolation and a hardened firewall.

### ATOM-SOURCE-20260203-008-0013
**Lines**: 32-33
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Audit and remove any unnecessary or suspicious ClawdHub skills, as the community has reported "hundreds of malicious skills" (e.g., the "ClawHavoc" campaign).

### ATOM-SOURCE-20260203-008-0014
**Lines**: 34-35
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Update all skills/plugins to exact versions (no `*`), run static scans, disable auto-updates of skills, and periodically run `openclaw security audit`.

### ATOM-SOURCE-20260203-008-0015
**Lines**: 35-36
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Apply prompt-guard measures by requiring confirmation for any tool execution and logging all actions.

### ATOM-SOURCE-20260203-008-0016
**Lines**: 39-40
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Enable access controls by enforcing pairing/allowlist for DMs and mention-trigger in groups.

### ATOM-SOURCE-20260203-008-0017
**Lines**: 40-41
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Lock OpenClaw configuration by setting file permissions, using a gateway auth token, enabling minimal mDNS mode, and ensuring no open ports.

### ATOM-SOURCE-20260203-008-0018
**Lines**: 42-42
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Install a Brave key and configure `web_search` in OpenClaw.

### ATOM-SOURCE-20260203-008-0019
**Lines**: 43-44
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Vet OpenClaw skills by removing any that ask to paste shell commands or install packages, and audit existing ones for external prerequisites.

### ATOM-SOURCE-20260203-008-0020
**Lines**: 45-45
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Set the sandbox default in OpenClaw by adding `agents.defaults.sandbox` and testing critical skills in isolation.

### ATOM-SOURCE-20260203-008-0021
**Lines**: 46-46
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Pin plugin versions in OpenClaw by using explicit `@version` in `extensions.allowlist` and reviewing their code.

### ATOM-SOURCE-20260203-008-0022
**Lines**: 49-50
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.90

> Move OpenClaw to a managed or containerized deployment (e.g., Ubuntu VM with Docker) to gain OS-level isolation.

### ATOM-SOURCE-20260203-008-0023
**Lines**: 50-50
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Use tools like Tailscale instead of LAN bind for remote access to OpenClaw.

### ATOM-SOURCE-20260203-008-0024
**Lines**: 51-52
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> Formalize separate agent identities for each role in OpenClaw and maintain per-agent config directories and memory.

### ATOM-SOURCE-20260203-008-0025
**Lines**: 53-54
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> Upgrade OpenClaw from raw text logs to structured DB or vector memory, ensuring logs are on append-only storage and rotated.

### ATOM-SOURCE-20260203-008-0026
**Lines**: 55-56
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Establish a skill governance policy for OpenClaw, including periodic audits, least-privilege checks, and an approval process for new skills.

### ATOM-SOURCE-20260203-008-0027
**Lines**: 57-58
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> Implement a model usage policy in OpenClaw to track token consumption per agent/model, adjust prompts for conciseness, and use fallbacks and throttling.

### ATOM-SOURCE-20260203-008-0032
**Lines**: 69-71
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> In OpenClaw, define agent roles and model fallbacks by declaring separate agents or default models in `openclaw.json`, using the Models CLI config to set primary/fallback chains.

### ATOM-SOURCE-20260203-008-0033
**Lines**: 77-81
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> To optimize token usage and cost, offload bulk processing, summarization, or list-making tasks to cheaper, smaller models like Sonnet, Haiku, or DeepSeek, wrapping them in a sandbox for verification due to potential error-proneness.

### ATOM-SOURCE-20260203-008-0034
**Lines**: 80-81
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Use `sessions_spawn` for parallelizable sub-tasks and concurrency in OpenClaw, as it runs sub-agents asynchronously and is ideal for background research or analysis.

### ATOM-SOURCE-20260203-008-0036
**Lines**: 90-93
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> Implement a "Council" multi-perspective pattern by having a lead agent (e.g., Ajna) pose the same problem to multiple sub-agents ("advisors"), aggregate their answers, and then synthesize a consensus or select the best parts.

### ATOM-SOURCE-20260203-008-0037
**Lines**: 100-101
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> To optimize token usage, use cheaper models like Sonnet/Haiku for low-stakes drafts and reserve more expensive models like Opus/GPT-5.2 for final outputs.

### ATOM-SOURCE-20260203-008-0038
**Lines**: 104-106
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> To manage costs and ensure continuity, implement a fallback mechanism where an agent like Ajna can switch from GPT-5.2 to Claude (and vice versa) if one hits rate limits, without losing context.

### ATOM-SOURCE-20260203-008-0039
**Lines**: 105-115
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> To orchestrate complex questions, an agent like Ajna (Opus 4.5) can spawn sub-agents for specific tasks: Psyche (GPT-5.2) for drafting answers/reasoning, Gemini for web search, and DeepSeek for large-scale data crunching.

### ATOM-SOURCE-20260203-008-0040
**Lines**: 106-108
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Leverage OpenAI's plus plan for free compute by offloading as much as possible to ChatGPT-5.2, as its flat fee covers unlimited chat, effectively providing 'no marginal tokens' for now.

### ATOM-SOURCE-20260203-008-0041
**Lines**: 108-110
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> Use Claude Max ($100) for specialized tasks that GPT-5.2 cannot handle or for improved tool-safety, as Claude Opus is effective at resisting prompt hacks.

### ATOM-SOURCE-20260203-008-0042
**Lines**: 120-126
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Use `sessions_spawn` for one-way, non-blocking parallel delegation of tasks to sub-agents, and `sessions_send` for two-way dialogues between agents, which automatically handles multiple rounds of back-and-forth up to a configurable limit.

### ATOM-SOURCE-20260203-008-0043
**Lines**: 129-133
**Context**: method / limitation
**Tension**: novelty=0.40, consensus_pressure=0.30, contradiction_load=0.20, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.50

> To avoid a bug where `agentId` in `sessions_spawn` silently ignores the model override, do not combine `agentId` and `model` parameters, or spawn without specifying `agentId` and then assign the model.

### ATOM-SOURCE-20260203-008-0044
**Lines**: 133-135
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Monitor `runTimeoutSeconds` for subtask hangs and inspect "Status: error" replies from sub-agents to diagnose failures.

### ATOM-SOURCE-20260203-008-0045
**Lines**: 135-137
**Context**: method / limitation
**Tension**: novelty=0.30, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.60

> Limit agent-to-agent turns using `agent.wait` or `agentToAgent.maxPingPongTurns` to prevent deep loops and excessive token usage when using `sessions_send`.

### ATOM-SOURCE-20260203-008-0046
**Lines**: 137-139
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Ensure proper context isolation for agents by using separate `agentDir` or enabling sandbox mode to prevent one agent from accessing another's workspace.

### ATOM-SOURCE-20260203-008-0047
**Lines**: 142-144
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> To manage costs, consolidate contexts, cap output lengths, use cheaper models when acceptable, and track token usage (available in Ajna's announce lines).

### ATOM-SOURCE-20260203-008-0048
**Lines**: 144-146
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Prioritize using paid models with flat fees like GPT-5.2 (ChatGPT+) and Claude Max, falling back to Claude Pro or lower tiers only if necessary, to optimize cost.

### ATOM-SOURCE-20260203-008-0049
**Lines**: 146-148
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> If budget constraints arise, temporarily disable the most expensive agent (e.g., GPT-5.2 spawn) or reduce tokens in prompts.

### ATOM-SOURCE-20260203-008-0050
**Lines**: 152-166
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To set up Brave Search API for OpenClaw, create an account at Brave Search API, select the "Data for Search" plan, generate a subscription token, and add the API key to your OpenClaw config (e.g., `openclaw.json`) or as a `BRAVE_API_KEY` environment variable.

### ATOM-SOURCE-20260203-008-0053
**Lines**: 172-175
**Context**: method / limitation
**Tension**: novelty=0.40, consensus_pressure=0.30, contradiction_load=0.30, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> Use Brave Search judiciously, despite OpenClaw's endorsement, due to Brave's official policy discouraging "AI inference"; consider enabling other search tools as a fallback if Brave becomes restricted.
