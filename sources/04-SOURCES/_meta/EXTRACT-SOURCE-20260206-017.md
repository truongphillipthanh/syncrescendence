# Extraction: SOURCE-20260206-017

**Source**: `SOURCE-20260206-x-article-rahulsood-the_tailscale_illusion_why_your_isolated_agent_isnt.md`
**Atoms extracted**: 21
**Categories**: claim, concept, praxis_hook

---

## Claim (8)

### ATOM-SOURCE-20260206-017-0001
**Lines**: 12-13
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> If an AI agent can reach other machines on a network, then anyone who hacks that agent can also reach those machines.

### ATOM-SOURCE-20260206-017-0002
**Lines**: 13-15
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> A malicious 'skill' (plugin) can compromise an AI agent, allowing an attacker to pivot to everything else on the network.

### ATOM-SOURCE-20260206-017-0003
**Lines**: 15-16
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> Putting an AI agent on its own computer does not prevent compromise if it is still connected to the network.

### ATOM-SOURCE-20260206-017-0006
**Lines**: 28-30
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Compromising an AI agent is disturbingly easy, often requiring only one malicious skill.

### ATOM-SOURCE-20260206-017-0007
**Lines**: 34-47
**Context**: anecdote / evidence
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> A top downloaded skill on a popular AI skill marketplace was found to be malware, which used a 'required dependency' link to deliver an obfuscated payload, download a binary, remove macOS quarantine attributes, and execute, leading to exfiltration of SSH keys and compromise of Tailscale authentication.

### ATOM-SOURCE-20260206-017-0008
**Lines**: 57-58
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> Separating an AI agent onto its own machine does not create a separate network; it remains one hop away from other machines on the tailnet.

### ATOM-SOURCE-20260206-017-0018
**Lines**: 170-171
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> An AI agent is software running on infrastructure with credentials, and should be treated as an attack surface.

### ATOM-SOURCE-20260206-017-0019
**Lines**: 173-174
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> Tailscale is not a security boundary, separate machines do not provide isolation, and the network is not the perimeter.

## Concept (2)

### ATOM-SOURCE-20260206-017-0005
**Lines**: 23-25
**Context**: hypothesis / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.20, speculation_risk=0.20, actionability=0.30, epistemic_stability=0.70

> The 'Tailscale Illusion' refers to the misconception that Tailscale provides isolation between machines, when in fact it primarily connects them.

### ATOM-SOURCE-20260206-017-0020
**Lines**: 176-176
**Context**: hypothesis / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.20, speculation_risk=0.20, actionability=0.30, epistemic_stability=0.70

> The true security perimeter for an AI agent is defined by what the agent is allowed to do.

## Praxis Hook (11)

### ATOM-SOURCE-20260206-017-0004
**Lines**: 16-17
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> To secure AI agents, lock down what the agent can actually do, rather than just where it resides.

### ATOM-SOURCE-20260206-017-0009
**Lines**: 65-72
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Implement tool policies to restrict what an AI agent can execute at the framework level, using an allowlist for commands (e.g., `git`, `npm`, `node`, `pnpm`) and blocking everything else.

### ATOM-SOURCE-20260206-017-0010
**Lines**: 76-81
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Disable gateway access for worker AI agents in their configuration (`gateway: false`) to prevent them from modifying their own config, disabling safety features, or escalating privileges if compromised.

### ATOM-SOURCE-20260206-017-0011
**Lines**: 85-90
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Restrict filesystem write access for AI agents, allowing writes only to specific output directories (e.g., `/workspace/output`) and denying all other writes (`/**`).

### ATOM-SOURCE-20260206-017-0012
**Lines**: 94-107
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Utilize Tailscale ACLs with tags to control network access, for example, allowing orchestrator machines to connect to worker machines on specific ports (e.g., `tag:worker:22`) but denying worker machines from initiating connections to orchestrator machines.

### ATOM-SOURCE-20260206-017-0013
**Lines**: 111-115
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Assign separate, individually revokable credentials (API keys, SSH keys, service accounts) to each AI agent to contain the impact of a compromise.

### ATOM-SOURCE-20260206-017-0014
**Lines**: 121-130
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Identify malicious AI skills by looking for red flags such as external downloads during install, obfuscated code, privilege escalation attempts, persistence mechanisms (e.g., LaunchAgents, cron jobs), and quarantine removal.

### ATOM-SOURCE-20260206-017-0015
**Lines**: 134-139
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Identify good AI skills by looking for green flags such as being self-contained within their directory, using declarative configurations instead of install scripts, having readable plain text code, and being scoped to only touch their own workspace.

### ATOM-SOURCE-20260206-017-0016
**Lines**: 143-147
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> When evaluating an AI skill, perform a 'sniff test' by reading it like an attacker and questioning why certain steps (e.g., installing a binary, requiring network access during setup) are necessary; if unexplained, do not run it.

### ATOM-SOURCE-20260206-017-0017
**Lines**: 160-164
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To secure AI agent infrastructure, sandbox every agent with tool policies, tag and ACL the Tailscale network, review every external skill submission, and design for containment by assuming breach.

### ATOM-SOURCE-20260206-017-0021
**Lines**: 178-179
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Lock down what an AI agent can do to ensure that a malicious skill results only in a failed command, rather than a system compromise.
