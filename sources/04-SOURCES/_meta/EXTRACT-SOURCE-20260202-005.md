# Extraction: SOURCE-20260202-005

**Source**: `SOURCE-20260202-x-article-rahulsood-i_run_a_fleet_of_ai_agents_from_a_mac_mini_heres_how_i_keep_them_from_going_rogue.md`
**Atoms extracted**: 10
**Categories**: claim, praxis_hook

---

## Claim (1)

### ATOM-SOURCE-20260202-005-0007
**Lines**: 49-50
**Context**: anecdote / evidence
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.30, actionability=0.80, epistemic_stability=0.60

> Using workspace files for AI agents allows for rapid onboarding of new agents, enabling them to understand their job comprehensively and immediately.

## Praxis Hook (9)

### ATOM-SOURCE-20260202-005-0001
**Lines**: 12-15
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> To manage multiple AI agents securely and in sync, use a primary 'Chief of Staff' agent (e.g., on Claude) to oversee subordinate agents (e.g., on Gemini Flash).

### ATOM-SOURCE-20260202-005-0002
**Lines**: 18-20
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> Isolate AI agents by running them as separate macOS users on distinct ports with their own configurations, workspaces, and permissions, even if they share a common codebase.

### ATOM-SOURCE-20260202-005-0003
**Lines**: 25-30
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.30, actionability=0.90, epistemic_stability=0.80

> Implement a daily cron job for a primary AI agent to pull the latest code commits, diff changes, audit for security vulnerabilities (obfuscated code, suspicious network calls, credential changes, new postinstall scripts, exfiltration patterns), and generate a security assessment with a SAFE/CAUTION/BLOCK recommendation.

### ATOM-SOURCE-20260202-005-0004
**Lines**: 31-33
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.80

> Require human approval for a primary AI agent to pull, build, and restart subordinate agents after a security assessment, ensuring human-in-the-loop security updates.

### ATOM-SOURCE-20260202-005-0005
**Lines**: 38-43
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.80

> Use dedicated workspace files (e.g., SOUL.md for personality/role, MEMORY.md for long-term memory, STRATEGY.md for playbooks, HEARTBEAT.md for periodic tasks) as persistent memory for AI agents.

### ATOM-SOURCE-20260202-005-0006
**Lines**: 45-47
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Delegate the writing and maintenance of subordinate agents' workspace files (e.g., strategy docs, heartbeats) to the primary agent, allowing for centralized configuration and updates.

### ATOM-SOURCE-20260202-005-0008
**Lines**: 53-56
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.80

> Grant a primary AI agent scoped sudo permissions, allowing it to run specific commands (e.g., kill, su, launchctl, cp, chown) without a password for managing subordinate agents, but restrict it from system-wide installations or configuration modifications.

### ATOM-SOURCE-20260202-005-0009
**Lines**: 58-59
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> Configure subordinate AI agents with zero sudo permissions, limiting their operations strictly to their own home directories.

### ATOM-SOURCE-20260202-005-0010
**Lines**: 62-64
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> For Telegram integration, lock the primary AI agent to a specific group chat ID, process messages only from an allowlist of user IDs, and make it respond only to @mentions.
