# Extraction: SOURCE-20260206-021

**Source**: `SOURCE-20260206-x-article-tomcrawshaw01-how_to_install_and_use_claude_code_agent_teams_complete_guide.md`
**Atoms extracted**: 21
**Categories**: analogy, claim, concept, praxis_hook

---

## Analogy (2)

### ATOM-SOURCE-20260206-021-0003
**Lines**: 22-24
**Context**: anecdote / evidence
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.70

> Agent teams are like going from a single freelancer doing everything solo to a project manager who brings a full crew and delegates tasks.

### ATOM-SOURCE-20260206-021-0005
**Lines**: 51-53
**Context**: anecdote / evidence
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.70

> Sub-agents are like sending an assistant to get an answer, while agent teams are like putting a group of specialists in a room to work through a problem collaboratively.

## Claim (3)

### ATOM-SOURCE-20260206-021-0001
**Lines**: 10-12
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> Anthropic has natively integrated multi-agent orchestration, previously developed by the OpenClaw community, into Claude Code, calling it "agent teams."

### ATOM-SOURCE-20260206-021-0006
**Lines**: 54-59
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.80

> Agent teams are beneficial for complex, multi-part work benefiting from collaboration, while sub-agents are better for focused tasks where inter-worker communication is not needed and token cost is a concern.

### ATOM-SOURCE-20260206-021-0007
**Lines**: 62-64
**Context**: consensus / limitation
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> Agent teams add coordination overhead and consume significantly more tokens than single sessions, making them unsuitable for all tasks.

## Concept (2)

### ATOM-SOURCE-20260206-021-0002
**Lines**: 17-20
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> Agent teams in Claude Code involve a lead agent breaking a task into pieces and delegating them to multiple independent teammates who coordinate, share context, and work in parallel.

### ATOM-SOURCE-20260206-021-0004
**Lines**: 44-49
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> Unlike sub-agents which report back to a main agent, agent teams consist of fully independent Claude Code sessions (teammates) with their own context windows, able to communicate directly, share findings, and self-coordinate through a shared task list.

## Praxis Hook (14)

### ATOM-SOURCE-20260206-021-0008
**Lines**: 66-73
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Agent teams are effective for tasks requiring parallel exploration, such as research and review, building new features with separate modules, debugging competing hypotheses, and cross-layer work (e.g., frontend, backend, testing).

### ATOM-SOURCE-20260206-021-0009
**Lines**: 75-77
**Context**: method / limitation
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> Agent teams are not suitable for sequential tasks, same-file edits (due to overwrites), or simple tasks where coordination overhead outweighs the benefits.

### ATOM-SOURCE-20260206-021-0010
**Lines**: 79-84
**Context**: method / claim
**Tension**: novelty=0.00, consensus_pressure=0.90, contradiction_load=0.00, speculation_risk=0.00, actionability=0.90, epistemic_stability=0.90

> To enable agent teams in Claude Code, add `"env": { "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1" }` to your settings.json file or set it as an environment variable.

### ATOM-SOURCE-20260206-021-0011
**Lines**: 86-89
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.20, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To create an AI agent team, specify the number of teammates and the AI model to use, for example: "Create a team with 4 teammates to refactor these modules in parallel. Use Sonnet for each teammate."

### ATOM-SOURCE-20260206-021-0012
**Lines**: 89-94
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.80

> To start an agent team, describe the desired outcome in plain language and specify clear, independent roles for each teammate, or explicitly state the number of teammates and the model to use.

### ATOM-SOURCE-20260206-021-0013
**Lines**: 98-101
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.20, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Interact directly with individual AI teammates by selecting them (Shift+Up/Down in in-process mode, clicking their pane in split-pane mode) and typing.

### ATOM-SOURCE-20260206-021-0014
**Lines**: 103-107
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.30, contradiction_load=0.00, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Toggle 'delegate mode' (Shift+Tab) for the lead AI agent to restrict it to coordination-only tasks like spawning teammates, assigning tasks, sending messages, and managing the task list, preventing it from doing the work itself.

### ATOM-SOURCE-20260206-021-0015
**Lines**: 109-112
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.20, contradiction_load=0.00, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Manage task assignments by allowing teammates to self-claim unassigned tasks or by explicitly telling the lead AI which task to assign to which teammate.

### ATOM-SOURCE-20260206-021-0016
**Lines**: 114-118
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.20, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To shut down an AI teammate, ask the lead to send a shutdown request; to clean up all shared team resources after all teammates are shut down, tell the lead to clean up.

### ATOM-SOURCE-20260206-021-0017
**Lines**: 124-128
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.30, contradiction_load=0.00, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Provide detailed spawn prompts to AI teammates, including specific context they need, as they do not inherit the lead's conversation history but automatically load project context from CLAUDE.md and MCP servers.

### ATOM-SOURCE-20260206-021-0018
**Lines**: 130-133
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.40, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.60

> Size AI agent tasks to be self-contained units that produce a clear deliverable (e.g., a function, test file, or review) to balance coordination overhead and the risk of wasted effort from long, unchecked work.

### ATOM-SOURCE-20260206-021-0019
**Lines**: 135-137
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.20, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Assign different files to each AI teammate to prevent overwrites and ensure efficient parallel work.

### ATOM-SOURCE-20260206-021-0020
**Lines**: 139-142
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.40, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.60

> For new users of AI agent teams, start with research and review tasks (e.g., reviewing a PR from different angles or investigating a bug with competing theories) before attempting parallel implementation to understand the value of parallel work without complex coordination.

### ATOM-SOURCE-20260206-021-0021
**Lines**: 144-145
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.20, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Regularly check in on AI agent teams to prevent wasted effort, especially if a teammate pursues an unproductive path.
