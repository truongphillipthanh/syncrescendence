# Extraction: SOURCE-20260207-007

**Source**: `SOURCE-20260207-x-article-fr0gger_-shield_md_a_security_standard_for_openclaw_and_ai_agents.md`
**Atoms extracted**: 39
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (9)

### ATOM-SOURCE-20260207-007-0001
**Lines**: 20-22
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.70

> OpenClaw's simplicity and chat app integration have led to its online popularity, but also exposed security risks.

### ATOM-SOURCE-20260207-007-0002
**Lines**: 24-26
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> An agent exposed to the internet without proper security can be accessed by an attacker, granting them access to the connected machine.

### ATOM-SOURCE-20260207-007-0003
**Lines**: 26-27
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Malicious skills, compromised or backdoored packages, and prompt injection are high risks for AI agents.

### ATOM-SOURCE-20260207-007-0005
**Lines**: 36-37
**Context**: consensus / limitation
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.60

> The existing Security.md file is used for reporting vulnerabilities, not for the security policy of an agent.

### ATOM-SOURCE-20260207-007-0023
**Lines**: 182-182
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> If multiple threats match, `block` overrides `require_approval`, which overrides `log`.

### ATOM-SOURCE-20260207-007-0034
**Lines**: 226-230
**Context**: consensus / limitation
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> Shield v0 has limitations including susceptibility to prompt injection, potential for threat logic summarization or leakage by the model, non-deterministic compliance across runs and models, and context window limits constraining feed size and rule complexity.

### ATOM-SOURCE-20260207-007-0035
**Lines**: 232-232
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> Shield v0 should be considered early guardrails to reduce accidental risk, not a security boundary, due to its limitations.

### ATOM-SOURCE-20260207-007-0038
**Lines**: 244-245
**Context**: consensus / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> Shield is a new approach to improve agent security through dynamic policy logic, aiming for a common, simple, readable, customizable, and evolving structure for security rules.

### ATOM-SOURCE-20260207-007-0039
**Lines**: 245-245
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> Despite its limitations and potential for bypass, Shield contributes to stronger agent security.

## Concept (5)

### ATOM-SOURCE-20260207-007-0004
**Lines**: 29-32
**Context**: method / evidence
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.50

> MoltThreat is the first human-curated threat intelligence database specifically for AI agents, which updates a local Security.md file with threat detections.

### ATOM-SOURCE-20260207-007-0006
**Lines**: 39-41
**Context**: hypothesis / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.30, actionability=0.70, epistemic_stability=0.40

> SHIELD.md is a proposed standard for AI agent security policies, addressing the need to secure agents with a new approach.

### ATOM-SOURCE-20260207-007-0008
**Lines**: 64-66
**Context**: hypothesis / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.30, actionability=0.70, epistemic_stability=0.40

> SHIELD.md is a Markdown file that follows a specific format, containing an evolvable security policy to provide security guidelines to an agent.

### ATOM-SOURCE-20260207-007-0009
**Lines**: 68-70
**Context**: hypothesis / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.30, actionability=0.70, epistemic_stability=0.40

> Shield v0 is a context-loaded security policy for AI agents, structured like a skill, that defines how an agent should react to detected threats without redefining its role.

### ATOM-SOURCE-20260207-007-0033
**Lines**: 222-224
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.20, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> Shield v0 is a policy guideline that needs to be explicitly specified to an agent through `SOUL.md`, `AGENTS.md`, and `MEMORY.md` files to enforce its policies, as it does not provide hard enforcement.

## Framework (5)

### ATOM-SOURCE-20260207-007-0007
**Lines**: 46-60
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.70

> OpenClaw agents rely on multiple Markdown files, each with a specific role: AGENTS.md (agent structure), HEARTBEAT.md (planned tasks), IDENTITY.md (agent role/scope), MEMORY.md (durable facts/decisions), SOUL.md (personality/boundaries), TOOLS.md (available tools/rules), USER.md (human operator), and SKILL.md (extends capabilities).

### ATOM-SOURCE-20260207-007-0011
**Lines**: 102-110
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.50

> The scope of SHIELD.md policy applies to: prompt (incoming/generated instructions), skill.install (adding skills), skill.execute (running skills), tool.call (calling tools), network.egress (outbound network requests), secrets.read (accessing sensitive data), and mcp (connecting to MCP servers).

### ATOM-SOURCE-20260207-007-0012
**Lines**: 112-126
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.50

> SHIELD.md defines threat categories including: prompt (injection), tool (abusive usage), mcp (malicious servers), memory (access/exfiltration), supply_chain (malicious dependencies), vulnerability (exploitation), fraud (scams), policy_bypass (evasion), anomaly (suspicious behavior), and skill (unsafe logic).

### ATOM-SOURCE-20260207-007-0015
**Lines**: 137-145
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.50

> The Decision block format includes: action (log|require_approval|block), scope (event type), threat_id, fingerprint, matched_on (e.g., skill.name, domain), match_value, and a short reason.

### ATOM-SOURCE-20260207-007-0022
**Lines**: 178-183
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.50

> Supported conditions for `recommendation_agent` include: `skill name equals <value>`, `skill name contains <value>`, `outbound request to <domain>`, `outbound request to <url_prefix>`, `secrets read path equals <value>`, and `file path equals <value>`.

## Praxis Hook (20)

### ATOM-SOURCE-20260207-007-0010
**Lines**: 76-84
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.30, actionability=0.90, epistemic_stability=0.40

> SHIELD.md operates by: 1. An event (skill install, tool call, etc.) occurs. 2. Shield evaluates the event against active threats. 3. The strongest match wins based on decision priority (block > require_approval > log). 4. A Decision block is emitted before execution, stating the action and matched threat context.

### ATOM-SOURCE-20260207-007-0013
**Lines**: 128-132
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.50

> Every threat match in SHIELD.md must result in exactly one action: `log`, `require_approval`, or `block`.

### ATOM-SOURCE-20260207-007-0014
**Lines**: 134-135
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.50

> Before any skill install/execution, tool call, MCP interaction, network request, or secret access, an agent must output a Decision block and stop.

### ATOM-SOURCE-20260207-007-0016
**Lines**: 147-149
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.50

> SHIELD.md default behavior: if no match is found, `action = log`; if uncertainty exists, `action = require_approval`.

### ATOM-SOURCE-20260207-007-0017
**Lines**: 153-156
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.50

> A threat is eligible for matching only if `revoked is false`, `revoked_at is null`, and `current time is before expires_at`.

### ATOM-SOURCE-20260207-007-0018
**Lines**: 159-161
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.50

> If `threat.confidence >= 0.85`, treat it as enforceable; if `threat.confidence < 0.85`, set `action = require_approval` unless `threat.action is block` and `severity is critical`.

### ATOM-SOURCE-20260207-007-0019
**Lines**: 164-168
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.50

> Threat matching logic uses: 1. `threat.category` and event scope alignment. 2. `threat.recommendation_agent` conditions (primary). 3. Fallback string matches in title and description (secondary, only for explicit exact values).

### ATOM-SOURCE-20260207-007-0020
**Lines**: 173-176
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.50

> The `recommendation_agent` mini syntax supports directives like `BLOCK: <condition>`, `APPROVE: <condition>` (maps to `require_approval`), and `LOG: <condition>`.

### ATOM-SOURCE-20260207-007-0021
**Lines**: 177-180
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To implement security policies, map threat actions: `BLOCK` to `action = block`, `APPROVE` to `action = require_approval`, and `LOG` to `action = log`.

### ATOM-SOURCE-20260207-007-0024
**Lines**: 186-191
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> If `action = block`, the system must immediately stop, not call tools, not perform network access, not read secrets, and not install or execute skills.

### ATOM-SOURCE-20260207-007-0025
**Lines**: 195-199
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.50

> If `action = block`, the agent must not call tools, perform network access, read secrets, install/execute skills, and must stop immediately after the block response.

### ATOM-SOURCE-20260207-007-0026
**Lines**: 195-195
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> When `action = block`, respond exactly with: `Blocked. Threat matched: <threat_id>. Match: <matched_on>=<match_value>.` and then stop.

### ATOM-SOURCE-20260207-007-0027
**Lines**: 196-196
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> When `action = require_approval`, ask one yes or no question and then stop.

### ATOM-SOURCE-20260207-007-0028
**Lines**: 197-197
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> When `action = log`, continue normally.

### ATOM-SOURCE-20260207-007-0029
**Lines**: 201-205
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.50

> Required behavior for SHIELD.md: if `action = block`, respond with `Blocked. Threat matched: <threat_id>. Match: <matched_on>=<match_value>.` and stop; if `action = require_approval`, ask a yes/no question and stop; if `action = log`, continue normally.

### ATOM-SOURCE-20260207-007-0030
**Lines**: 201-204
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To avoid context overflow, only include active threats required for the current task, prefer threats with `action = block` and `severity = critical` or `high`, and cap active threats loaded in context to 25 entries.

### ATOM-SOURCE-20260207-007-0031
**Lines**: 207-208
**Context**: method / limitation
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.50

> To avoid context overflow, SHIELD.md limits active threats loaded in context to 25 entries, preferring those with `action = block` and `severity = critical` or `high`, and avoiding long descriptions unless required for matching.

### ATOM-SOURCE-20260207-007-0032
**Lines**: 209-216
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> When compressing active threats, each entry must retain only fields required for matching and decision: `id`, `fingerprint`, `category`, `severity`, `confidence`, `action`, `title` (short), `recommendation_agent`, `expires_at`, and `revoked`.

### ATOM-SOURCE-20260207-007-0036
**Lines**: 236-237
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To use Shield, create a `SHIELD.md` file at the root of your agent and specify its use through `SOUL.md`, `AGENTS.md`, and `MEMORY.md` to enforce the policy.

### ATOM-SOURCE-20260207-007-0037
**Lines**: 239-240
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> A good starting point for populating `SHIELD.md` is to leverage MoltThreats and follow its structure to add security measures.
