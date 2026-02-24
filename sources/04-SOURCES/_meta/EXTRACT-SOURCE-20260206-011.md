# Extraction: SOURCE-20260206-011

**Source**: `SOURCE-20260206-x-article-jordanlyall-how_i_set_up_openclaw_clawdbot_without_giving_it_the_keys_to_my_life.md`
**Atoms extracted**: 27
**Categories**: claim, praxis_hook, prediction

---

## Claim (5)

### ATOM-SOURCE-20260206-011-0002
**Lines**: 48-66
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.20, actionability=0.30, epistemic_stability=0.70

> Many OpenClaw guides neglect security, leading to issues like automated spam tactics, users granting agents bank access without guardrails, and agents wiping inboxes due to prompt injection attacks.

### ATOM-SOURCE-20260206-011-0014
**Lines**: 191-195
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> Phase 1 of an AI agent project, including Claude API with 30-min heartbeat, free Tailscale, and basic Twitter/X API, is estimated to cost $130-200 per month.

### ATOM-SOURCE-20260206-011-0024
**Lines**: 228-228
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> The goal of AI agent security is intentionality, not paranoia, due to the inherent power of such systems.

### ATOM-SOURCE-20260206-011-0025
**Lines**: 230-231
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> Individuals in high-profile spaces like crypto are already targets and should avoid creating new attack vectors with unsecured AI agents.

### ATOM-SOURCE-20260206-011-0027
**Lines**: 249-253
**Context**: speculation / claim
**Tension**: novelty=0.40, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.80, actionability=0.30, epistemic_stability=0.30

> Future plans for AI agents include restaurant reservation checking, price monitoring, market monitoring, and a second agent for a different domain, but only after the foundation is proven solid.

## Praxis Hook (21)

### ATOM-SOURCE-20260206-011-0001
**Lines**: 10-10
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To safely experiment with OpenClaw, use a dedicated machine, Tailscale for network access (no public ports), an allowlist for commands, read-only tokens for external services, and a one-way data flow for integrations.

### ATOM-SOURCE-20260206-011-0004
**Lines**: 102-125
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To harden a machine for an AI agent, create a non-admin user account for the agent, enable and configure a firewall (e.g., macOS built-in with stealth mode), harden SSH (keys only, no root, limit attempts, specific user), use Tailscale for private network access, and disable all unnecessary services (e.g., Remote Management, Screen Sharing, File Sharing, AirDrop).

### ATOM-SOURCE-20260206-011-0005
**Lines**: 129-146
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> When installing OpenClaw, secure API keys by locking file permissions and rotating keys monthly, restrict bot access to only the owner's user ID (e.g., Telegram), enable sandbox mode for risky operations, and configure a command allowlist to limit the shell commands the agent can execute.

### ATOM-SOURCE-20260206-011-0006
**Lines**: 150-159
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> When configuring an AI agent, define its identity and constraints in a SOUL file, explicitly listing what the agent does and, crucially, what it does not do (e.g., no posting, no financial transactions, no modifying files outside its workspace).

### ATOM-SOURCE-20260206-011-0007
**Lines**: 156-157
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Before deploying an AI agent, run a security audit command and fix all flagged issues.

### ATOM-SOURCE-20260206-011-0008
**Lines**: 159-164
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Test AI agent network access by attempting to reach the machine with Tailscale off, SSH from outside the tailnet, and sending messages from an unauthorized Telegram account.

### ATOM-SOURCE-20260206-011-0009
**Lines**: 168-171
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To integrate an AI agent with existing systems securely, use a one-way data flow where the agent writes to an inbox folder, and other tools process that inbox, preventing bidirectional sync, corruption, or drift.

### ATOM-SOURCE-20260206-011-0010
**Lines**: 175-177
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Before deploying an AI agent, run a security audit command and fix all flagged issues, then test network access (e.g., try reaching the machine with Tailscale off, try SSH from outside the tailnet) and bot access (e.g., send messages from different accounts) to verify security measures.

### ATOM-SOURCE-20260206-011-0011
**Lines**: 175-176
**Context**: anecdote / evidence
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> Enable Tailscale SSH for remote access before traveling to prevent being locked out of an AI agent system.

### ATOM-SOURCE-20260206-011-0012
**Lines**: 182-182
**Context**: anecdote / evidence
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> To prevent AI agent context overflow, implement periodic session resets, memory pruning, or maximum context limits.

### ATOM-SOURCE-20260206-011-0013
**Lines**: 188-188
**Context**: anecdote / evidence
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> Use cheaper AI models for heartbeat checks and reserve more expensive models for actual work to manage API rate limits.

### ATOM-SOURCE-20260206-011-0015
**Lines**: 200-200
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Implement a kill switch to immediately stop an AI agent gateway, either directly or via Tailscale SSH.

### ATOM-SOURCE-20260206-011-0016
**Lines**: 203-208
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> In case of suspected AI agent compromise: stop the gateway, revoke all API tokens, review logs, change Telegram bot token, audit modified files, and do not restart until the cause is understood.

### ATOM-SOURCE-20260206-011-0017
**Lines**: 212-212
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> When starting with AI agents, begin in a read-only mode without posting, outreach, or financial access to ensure safe operation.

### ATOM-SOURCE-20260206-011-0018
**Lines**: 214-214
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Limit initial AI agent deployments to one agent and one channel to manage complexity.

### ATOM-SOURCE-20260206-011-0019
**Lines**: 216-216
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Use Tailscale and avoid public ports for AI agents to ensure network security.

### ATOM-SOURCE-20260206-011-0020
**Lines**: 218-219
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Implement a command allowlist instead of open shell access for AI agents, as prompt injection resistance is not perfect.

### ATOM-SOURCE-20260206-011-0021
**Lines**: 221-221
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Scope every API token for AI agents, granting read-only access where possible and documenting each token's capabilities.

### ATOM-SOURCE-20260206-011-0022
**Lines**: 223-223
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Enable remote access, such as Tailscale SSH, for AI agents before it becomes critically needed.

### ATOM-SOURCE-20260206-011-0023
**Lines**: 225-226
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Set a gate for AI agent expansion, such as two weeks of stable operation without security issues, before adding new capabilities.

### ATOM-SOURCE-20260206-011-0026
**Lines**: 235-236
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> Copying this guide into a Claude Code context can help with AI-assisted setup of AI agents, adapting commands and catching mistakes.

## Prediction (1)

### ATOM-SOURCE-20260206-011-0003
**Lines**: 68-72
**Context**: speculation / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.80, actionability=0.20, epistemic_stability=0.60

> Attackers are already using AI to craft more convincing phishing attempts, and the ability to inject instructions directly into an AI agent's context poses a significant threat, especially for individuals in crypto, fintech, or other high-target spaces.
