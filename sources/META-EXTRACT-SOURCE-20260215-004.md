# Extraction: SOURCE-20260215-004

**Source**: `SOURCE-20260215-x-article-austin_hurwitz-the_ultimate_openclaw_setup_point_your_agent_here.md`
**Atoms extracted**: 39
**Categories**: claim, framework, praxis_hook

---

## Claim (5)

### ATOM-SOURCE-20260215-004-0004
**Lines**: 81-82
**Context**: consensus / claim
**Tension**: novelty=0.50, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Giving an AI clear permission boundaries, specifying what it can do autonomously versus what requires approval, is a key insight for effective agent deployment.

### ATOM-SOURCE-20260215-004-0006
**Lines**: 95-95
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> OpenClaw loads an AI agent's personality entirely from files, eliminating the need for code changes.

### ATOM-SOURCE-20260215-004-0037
**Lines**: 334-336
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> The breakthrough in autonomous builders is the 'harness' (persistence, memory, clear operating instructions) rather than solely the AI model itself.

### ATOM-SOURCE-20260215-004-0038
**Lines**: 338-338
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> Permission boundaries are more critical than personality tuning for AI agents, requiring clear rules on autonomous actions versus those needing approval.

### ATOM-SOURCE-20260215-004-0039
**Lines**: 339-339
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> File-based memory is a simple and effective approach for AI agents, using daily logs for raw events, `MEMORY.md` for curated context, and `active-tasks.md` for crash recovery.

## Framework (2)

### ATOM-SOURCE-20260215-004-0002
**Lines**: 30-44
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> An OpenClaw AI agent's workspace structure includes core files like `AGENTS.md` (operating instructions), `SOUL.md` (personality), `USER.md` (developer info), `IDENTITY.md` (AI's role), `TOOLS.md` (local environment notes), `HEARTBEAT.md` (self-check checklist), `MEMORY.md` (long-term memory), and directories for `memory/` (daily logs), `outputs/` (generated artifacts), and `skills/` (custom skill definitions).

### ATOM-SOURCE-20260215-004-0018
**Lines**: 228-237
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> The Factory.ai 5-level model for agent readiness includes: Level 1 (Functional), Level 2 (Documented), Level 3 (Standardized), Level 4 (Optimized), and Level 5 (Autonomous).

## Praxis Hook (32)

### ATOM-SOURCE-20260215-004-0001
**Lines**: 10-44
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> To deploy a persistent AI agent with memory, automation, and integrations, use OpenClaw (an open-source AI assistant framework) and configure a workspace directory with specific files for operating instructions (`AGENTS.md`), personality (`SOUL.md`), user information (`USER.md`), identity (`IDENTITY.md`), tool notes (`TOOLS.md`), self-check checklists (`HEARTBEAT.md`), and long-term memory (`MEMORY.md`), alongside directories for daily logs (`memory/`), generated artifacts (`outputs/`), and custom skills (`skills/`).

### ATOM-SOURCE-20260215-004-0003
**Lines**: 48-80
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> To configure an AI agent's operating manual (`AGENTS.md`), include sections for "First Run" (e.g., follow `BOOTSTRAP.md` then delete it), "Crash Recovery" (e.g., read `memory/active-tasks.md` first and resume autonomously), "Every Session" (e.g., read `active-tasks.md`, `SOUL.md`, `USER.md`, and recent daily logs), "Safety" (e.g., don't exfiltrate data, ask before destructive commands, prefer recoverable actions), and "Autonomous Building" (e.g., read/write/execute code, commit to git, run tests, ask for review before merging).

### ATOM-SOURCE-20260215-004-0005
**Lines**: 85-94
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> To define an AI agent's working style (`SOUL.md`), specify traits like being genuinely helpful, resourceful before asking, earning trust through competence, shipping working code, and testing work before claiming completion.

### ATOM-SOURCE-20260215-004-0007
**Lines**: 98-113
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> To provide an AI agent with environment notes (`TOOLS.md`), document credential storage (e.g., env vars, never raw API keys), project structure (e.g., main repo path, language, package manager, test runner), and common commands (e.g., build, test, dev server).

### ATOM-SOURCE-20260215-004-0008
**Lines**: 118-129
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> To enable crash recovery for an AI agent, maintain an `active-tasks.md` file that the agent reads first on restart to autonomously resume in-progress work, blocked tasks, and recently completed items.

### ATOM-SOURCE-20260215-004-0009
**Lines**: 132-143
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> To provide an AI agent with memory, log every significant event, decision, and code change into daily log files (`memory/YYYY-MM-DD.md`).

### ATOM-SOURCE-20260215-004-0010
**Lines**: 146-158
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> To prevent an AI agent from repeating mistakes, document every error once in a `lessons.md` file, categorized by type (e.g., Code, Process, Tools), so future sessions can learn from them.

### ATOM-SOURCE-20260215-004-0011
**Lines**: 161-174
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> To enable an AI agent to perform regular self-checks, configure a `self-review.md` file that the agent critiques every few hours, asking questions like: Am I stuck? Have I waited too long for human input? Did I make loggable mistakes? Are there stale tasks? Is my context bloated?

### ATOM-SOURCE-20260215-004-0012
**Lines**: 164-179
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Design skills for AI agents with explicit routing guidance, including 'When to Use' and 'When NOT to Use' conditions, to prevent misfires.

### ATOM-SOURCE-20260215-004-0013
**Lines**: 177-178
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> To implement autonomous operation for an AI agent, configure "Heartbeats" where OpenClaw sends regular polls, prompting the AI to read `HEARTBEAT.md` and perform quick checks (e.g., stale tasks, self-review due, context size, old outputs) and proactive work (e.g., commit uncommitted work, run tests, update documentation).

### ATOM-SOURCE-20260215-004-0014
**Lines**: 180-186
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Include negative examples ('When NOT to Use') in AI skill routing logic, as this significantly improves accuracy in production evaluations.

### ATOM-SOURCE-20260215-004-0015
**Lines**: 190-204
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Embed templates directly within AI skills rather than in system prompts to save tokens, as they only load when the skill is triggered.

### ATOM-SOURCE-20260215-004-0016
**Lines**: 205-210
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Adopt a default security posture for AI skills: allow skills, use a minimal allowlist for network access per request, and never combine powerful procedures with open internet access.

### ATOM-SOURCE-20260215-004-0017
**Lines**: 215-227
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Implement a `metrics.json` file to track operational health metrics (e.g., sessions, tasks completed, errors, skills used) and update it during self-review to identify improvement opportunities.

### ATOM-SOURCE-20260215-004-0019
**Lines**: 238-238
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Track progress against the Factory.ai 5-level agent readiness model by creating a `READINESS.md` file.

### ATOM-SOURCE-20260215-004-0020
**Lines**: 241-245
**Context**: consensus / claim
**Tension**: novelty=0.00, consensus_pressure=0.90, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=1.00

> Store credentials (e.g., API keys, tokens) as environment variables (e.g., in `~/.zshrc`) and never in plaintext workspace files.

### ATOM-SOURCE-20260215-004-0021
**Lines**: 247-254
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Configure gateways to run on localhost only, without tunnels or port forwarding, and require token authentication for all API calls.

### ATOM-SOURCE-20260215-004-0022
**Lines**: 255-259
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Manually review all AI skills before installation, ensuring they come from trusted sources, checking for suspicious network calls, and running weekly security audits.

### ATOM-SOURCE-20260215-004-0023
**Lines**: 263-264
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> To upgrade OpenClaw, `pkill` the old gateway process and start fresh, as `SIGUSR1` restart only reloads config, not the binary.

### ATOM-SOURCE-20260215-004-0024
**Lines**: 265-266
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.60, actionability=0.80, epistemic_stability=0.70

> Avoid running `pkill -f clawdbot-gateway` from within an AI session, as it will terminate the current connection; restart from outside the session.

### ATOM-SOURCE-20260215-004-0025
**Lines**: 267-268
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.60

> For memory search, consider using local semantic search tools (like qmd) that work offline, as some built-in tools require embedding API keys.

### ATOM-SOURCE-20260215-004-0026
**Lines**: 269-270
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Ensure all information the AI needs to remember is written to a file, as 'mental notes' do not persist across session restarts.

### ATOM-SOURCE-20260215-004-0027
**Lines**: 271-272
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Always run verification before claiming a task is complete, as the agent that builds should not be the same as the agent that reviews.

### ATOM-SOURCE-20260215-004-0028
**Lines**: 273-277
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> When spawning sub-agents, explicitly define their scope, provide clear success criteria, set a timeout, and prevent multiple agents from writing to the same file.

### ATOM-SOURCE-20260215-004-0029
**Lines**: 280-280
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Set `maxConcurrent` limits on agents and subagents to prevent token costs from spiraling out of control.

### ATOM-SOURCE-20260215-004-0030
**Lines**: 281-281
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Move heavy work to cron jobs and ensure heartbeats are quick checks only, as heartbeats can become expensive.

### ATOM-SOURCE-20260215-004-0031
**Lines**: 283-283
**Context**: consensus / claim
**Tension**: novelty=0.00, consensus_pressure=0.90, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=1.00

> Do not store secrets in file-based memory, as it lacks encryption; use environment variables instead.

### ATOM-SOURCE-20260215-004-0032
**Lines**: 284-284
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Audit all code from skill marketplaces before installation, as skills have full system access.

### ATOM-SOURCE-20260215-004-0033
**Lines**: 285-286
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Use context compaction as a default primitive, not an emergency fallback, and checkpoint to memory files before hitting context limits to manage silently growing context.

### ATOM-SOURCE-20260215-004-0034
**Lines**: 309-323
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To set up an OpenClaw workspace, install `openclaw`, configure it, create a workspace directory, and populate it with core files like `AGENTS.md`, `SOUL.md`, `USER.md`, `IDENTITY.md`, `TOOLS.md`, `HEARTBEAT.md`, `MEMORY.md`, and a `memory/` directory.

### ATOM-SOURCE-20260215-004-0035
**Lines**: 324-326
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.90, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=1.00

> Set credentials as environment variables (e.g., `ANTHROPIC_API_KEY`) by adding them to your shell configuration file (e.g., `~/.zshrc`) and sourcing it.

### ATOM-SOURCE-20260215-004-0036
**Lines**: 327-330
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Configure and start the OpenClaw gateway using `openclaw configure` and `openclaw gateway` commands.
