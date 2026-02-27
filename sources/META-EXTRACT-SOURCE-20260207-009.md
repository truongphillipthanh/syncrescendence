# Extraction: SOURCE-20260207-009

**Source**: `SOURCE-20260207-x-article-jasonzhou1993-how_to_install_and_use_claude_code_agent_teams_reverse_engineered.md`
**Atoms extracted**: 20
**Categories**: analogy, claim, concept, framework, praxis_hook, prediction

---

## Analogy (1)

### ATOM-SOURCE-20260207-009-0018
**Lines**: 355-356
**Context**: anecdote / evidence
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.30, actionability=0.60, epistemic_stability=0.60

> Agent teammates can be used to investigate different hypotheses and engage in a 'scientific debate' to disprove each other's theories, similar to how human scientists might collaborate to reach a consensus.

## Claim (5)

### ATOM-SOURCE-20260207-009-0001
**Lines**: 7-7
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.10, epistemic_stability=0.90

> Claude Code has released a significant update to its agent system called "Agent Teams."

### ATOM-SOURCE-20260207-009-0005
**Lines**: 59-62
**Context**: anecdote / claim
**Tension**: novelty=0.30, consensus_pressure=0.40, contradiction_load=0.00, speculation_risk=0.30, actionability=0.70, epistemic_stability=0.60

> Agent Teams are most effective when all agents' work can be viewed in parallel, ideally using tools like tmux or iTerm2 on macOS.

### ATOM-SOURCE-20260207-009-0015
**Lines**: 307-310
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.90

> Messages sent via the `sendMessage` tool are stored in `.claude/teams/<team_id>/inbox/` for each agent and are injected as new user messages into the recipient agent's conversation history.

### ATOM-SOURCE-20260207-009-0017
**Lines**: 350-351
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.50, epistemic_stability=0.70

> Agent Teams offer a more sophisticated communication channel and context sharing compared to sub-agents, opening up new possibilities for agentic tasks.

### ATOM-SOURCE-20260207-009-0019
**Lines**: 359-360
**Context**: consensus / limitation
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.80

> Using agent teams results in higher token consumption and slower speed compared to sub-agents, indicating a trade-off between sophistication and resource usage.

## Concept (4)

### ATOM-SOURCE-20260207-009-0002
**Lines**: 9-11
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Agent Teams represent a fundamentally different execution model from the old task + sub-agent model, allowing 3–5 independent Claude Code instances to collaborate, share context, exchange messages, and coordinate via a shared task system.

### ATOM-SOURCE-20260207-009-0007
**Lines**: 87-91
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.10, epistemic_stability=0.90

> The old Claude Code model involved a main agent calling a task tool, which spun up an isolated sub-agent that worked independently, terminated its session, and returned only a summary to the main agent.

### ATOM-SOURCE-20260207-009-0008
**Lines**: 94-97
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Agent Teams introduce shared task lists, inter-agent messaging and communication, and explicit lifecycle control (startup, shutdown), enabled by new internal tools.

### ATOM-SOURCE-20260207-009-0012
**Lines**: 222-222
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> A 'teammate' agent is distinguished from a 'sub-agent' by the inclusion of 'name' and 'team_name' parameters when spawned, enabling it to join a team and communicate with other agents.

## Framework (4)

### ATOM-SOURCE-20260207-009-0009
**Lines**: 102-122
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> The `TeamCreate` tool initiates an Agent Team by creating a new team folder under `.claude/teams/`, establishing the team's scaffolding before any agents are assigned. It requires a `team_name`, `description`, and `agent_type` (e.g., "researcher", "test-runner").

### ATOM-SOURCE-20260207-009-0010
**Lines**: 124-149
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> The `TaskCreate` tool is used to create new to-do items, with each task stored as a JSON file under `.claude/tasks/team-id`. It tracks Task ID, Description, Status (pending, in_progress, complete, deleted), Owner, and Dependencies (blocks, blocked_by). Tasks can be delegated by the team-lead or self-claimed by agent team members.

### ATOM-SOURCE-20260207-009-0011
**Lines**: 151-160
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> The `Task` tool, which activates agents, has been upgraded for Agent Teams with new parameters `name` (for the spawned agent's identity) and `team_name` (to join a team), which differentiate it from simple sub-agent subprocesses.

### ATOM-SOURCE-20260207-009-0014
**Lines**: 299-305
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> The `sendMessage` tool facilitates communication within agent teams, supporting direct messages (agent to agent), broadcast messages (agent to all teammates), and specific message types like `shutdown_request`, `shutdown_response`, and `plan_approval_response`.

## Praxis Hook (5)

### ATOM-SOURCE-20260207-009-0003
**Lines**: 29-40
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To enable Agent Teams, update Claude Code to the latest version, then add `"CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"` to the `env` section of your `~/.claude/settings.json` file and restart your terminal.

### ATOM-SOURCE-20260207-009-0004
**Lines**: 45-52
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.00, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> Agent Teams are activated by explicitly instructing Claude Code to create an agent team in your prompt, for example: "Create an agent team to explore this from different angles: one teammate on UX, one on technical architecture, one playing devil's advocate."

### ATOM-SOURCE-20260207-009-0006
**Lines**: 66-77
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To set up iTerm2 for Agent Teams, install iTerm2, enable Python API in Settings → General → Magic, restart iTerm2, and then launch Claude Code with `claude --teammate-mode tmux` to open separate panes for the team lead and each agent teammate.

### ATOM-SOURCE-20260207-009-0013
**Lines**: 226-226
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Agents are expected to use the `taskUpdate` tool to claim tasks, update their status (pending, in_progress, complete, deleted), modify task details (subject, description, activeForm, owner, metadata), and manage task dependencies (addBlocks, addBlockedBy).

### ATOM-SOURCE-20260207-009-0016
**Lines**: 314-315
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> A team-lead agent can send a `shutdown_request` to a teammate agent, which then sends a `shutdown_response` to confirm, likely using a `postToolCall` hook to automatically terminate the agent session.

## Prediction (1)

### ATOM-SOURCE-20260207-009-0020
**Lines**: 363-363
**Context**: speculation / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.20, speculation_risk=0.80, actionability=0.30, epistemic_stability=0.30

> Agent teams, combined with a 'ralph loop' (presumably a feedback or iterative process), could enable the structuring of extremely long-running agentic tasks.
