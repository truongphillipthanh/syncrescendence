# Extraction: SOURCE-20260220-001

**Source**: `SOURCE-20260220-x-article-ashpreetbedi-the_5_levels_of_agentic_software.md`
**Atoms extracted**: 28
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (14)

### ATOM-SOURCE-20260220-001-0004
**Lines**: 20-20
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.80

> Tools transform an LLM into an Agent by enabling it to perform actions.

### ATOM-SOURCE-20260220-001-0005
**Lines**: 20-21
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> For a coding agent, essential tools include the ability to read files, write files, and run shell commands.

### ATOM-SOURCE-20260220-001-0006
**Lines**: 43-44
**Context**: consensus / limitation
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> A Level 1 agent (Agent with tools) is stateless, meaning each run starts without memory of previous sessions or project conventions, and its knowledge is limited to the current context.

### ATOM-SOURCE-20260220-001-0007
**Lines**: 46-46
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.70

> Level 2 agents address the statelessness of Level 1 by incorporating session storage and domain knowledge.

### ATOM-SOURCE-20260220-001-0008
**Lines**: 49-54
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> Session storage enables an agent to include recent chat history in its context window and provides a record of agent actions for auditing and analysis.

### ATOM-SOURCE-20260220-001-0009
**Lines**: 57-61
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> Knowledge integration provides agents with access to project-relevant information outside the codebase, such as architecture specs, design decisions, and meeting notes.

### ATOM-SOURCE-20260220-001-0010
**Lines**: 63-67
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.70

> A significant amount of valuable context for coding agents exists outside the codebase, including team discussions and past decisions.

### ATOM-SOURCE-20260220-001-0012
**Lines**: 106-106
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> Level 2 agents are suitable when an agent needs to adhere to standards it wasn't trained on or when multi-turn conversations are expected, making it a 'sweet spot' for most internal tools.

### ATOM-SOURCE-20260220-001-0013
**Lines**: 108-109
**Context**: consensus / claim
**Tension**: novelty=0.50, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.60

> The transition from Level 2 to Level 3 in agentic software is crucial because Level 3 agents learn rules from experience, unlike Level 2 agents which only follow given rules.

### ATOM-SOURCE-20260220-001-0014
**Lines**: 110-110
**Context**: consensus / claim
**Tension**: novelty=0.50, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.60

> A Level 3 agent (Agent with memory and learning) improves its performance over time, meaning later interactions are better than earlier ones.

### ATOM-SOURCE-20260220-001-0017
**Lines**: 130-132
**Context**: consensus / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.30, actionability=0.70, epistemic_stability=0.50

> Level 3 agents incorporate a 'Learning Machine' that enables them to decide what information to remember (e.g., coding patterns, mistakes, user preferences) and store it in a separate knowledge base for future sessions.

### ATOM-SOURCE-20260220-001-0018
**Lines**: 133-134
**Context**: consensus / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.30, actionability=0.70, epistemic_stability=0.50

> Level 3 agents also feature 'Agentic Memory,' allowing them to build a user profile over time, including preferred coding styles, frameworks, and explanation preferences.

### ATOM-SOURCE-20260220-001-0021
**Lines**: 174-176
**Context**: limitation / limitation
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.40, speculation_risk=0.60, actionability=0.20, epistemic_stability=0.50

> Multi-agent teams are powerful but unpredictable because the team leader, an LLM, makes delegation decisions that can sometimes be ineffective.

### ATOM-SOURCE-20260220-001-0027
**Lines**: 217-219
**Context**: consensus / counterevidence
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.30, speculation_risk=0.20, actionability=0.30, epistemic_stability=0.60

> Many teams prematurely adopt multi-agent architectures (Level 4) due to their impressive demos, leading to months of debugging coordination failures that a simpler single-agent approach could have avoided.

## Concept (1)

### ATOM-SOURCE-20260220-001-0003
**Lines**: 20-20
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> An agent without tools is merely an LLM capable of reasoning but unable to perform actions.

## Framework (3)

### ATOM-SOURCE-20260220-001-0002
**Lines**: 9-14
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> Agentic software can be categorized into five architectural levels: Agent with tools, Agent with storage and knowledge, Agent with memory and learning, Multi-agent teams, and Production systems.

### ATOM-SOURCE-20260220-001-0020
**Lines**: 145-146
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.60

> Level 4 of agentic system design involves splitting responsibilities across specialized agents coordinated by a team leader, allowing for multiple perspectives and decomposition of tasks into specialist roles.

### ATOM-SOURCE-20260220-001-0024
**Lines**: 184-185
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.60

> Level 5 of agentic system design involves transitioning Levels 1-4 into a production service by upgrading to production databases (e.g., PostgreSQL + PgVector), adding tracing for observability, and exposing the system as an API via a wrapper like AgentOS.

## Praxis Hook (10)

### ATOM-SOURCE-20260220-001-0001
**Lines**: 7-7
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To build agentic software, start simple, progressively add capabilities, and verify behavior at each step.

### ATOM-SOURCE-20260220-001-0011
**Lines**: 96-98
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> To provide knowledge to an agent, insert documents (text, PDF, URLs) into a knowledge base, which the agent then searches for relevant chunks to add to its context (Agentic RAG).

### ATOM-SOURCE-20260220-001-0015
**Lines**: 118-122
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> To enable an agent to learn and adapt to user preferences over time, provide it with `save_learning` and `search_learnings` tools. The agent can then decide what information (e.g., coding patterns, mistakes, user preferences) is worth remembering and store it in a separate knowledge base for future sessions.

### ATOM-SOURCE-20260220-001-0016
**Lines**: 123-125
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.60

> To build a user profile for an agent, enable 'Agentic Memory' so it can track and adapt to user preferences like coding style, preferred frameworks, and explanation styles over time.

### ATOM-SOURCE-20260220-001-0019
**Lines**: 140-142
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> Use Level 3 agentic learning when the agent serves the same users repeatedly and needs to improve over time, such as in personal coding assistants, team tools with shared learnings, or contexts where adapting to specific user preferences is important.

### ATOM-SOURCE-20260220-001-0022
**Lines**: 176-177
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> For production systems requiring reliability, prefer explicit workflows over dynamic multi-agent teams to avoid coordination failures.

### ATOM-SOURCE-20260220-001-0023
**Lines**: 179-181
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> Use Level 4 multi-agent teams when multiple perspectives are needed (e.g., code review), tasks naturally decompose into specialist roles, or in human-supervised interactive tools where a human can oversee the team's output.

### ATOM-SOURCE-20260220-001-0025
**Lines**: 210-211
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> Use Level 5 when an agent leaves development, requiring support for multiple users, uptime requirements, and the ability to debug production issues.

### ATOM-SOURCE-20260220-001-0026
**Lines**: 214-216
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> When building agentic systems, start at Level 1 by creating the simplest agent that can solve the problem, then incrementally add capabilities only when a missing feature is clearly identified.

### ATOM-SOURCE-20260220-001-0028
**Lines**: 220-221
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> View agentic system levels as a hierarchy of capability, and only pay the cost of increased complexity when simpler approaches have demonstrably failed.
