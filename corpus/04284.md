# Extraction: SOURCE-20260218-009

**Source**: `SOURCE-20260218-x-article-jordymaui-youve_set_up_openclaw_now_what_why_skills_beat_agents_and_save_you_thousands_in_fees.md`
**Atoms extracted**: 16
**Categories**: analogy, claim, concept, praxis_hook

---

## Analogy (1)

### ATOM-SOURCE-20260218-009-0004
**Lines**: 26-30
**Context**: consensus / evidence
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.40, epistemic_stability=0.60

> Learning new skills or referencing a manual is analogous to how skills work for an agent: the brain remains the same, knowledge carries over, and the agent gains more capabilities without changing its core identity.

## Claim (6)

### ATOM-SOURCE-20260218-009-0001
**Lines**: 10-12
**Context**: anecdote / evidence
**Tension**: novelty=0.10, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Agents forgot what other agents were doing, context got lost between handoffs, and managing agents consumed more time than actual work.

### ATOM-SOURCE-20260218-009-0005
**Lines**: 42-45
**Context**: anecdote / evidence
**Tension**: novelty=0.20, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> Multi-agent setups often lead to agents not sharing context or memory, acting as 'separate brains in separate rooms shouting through walls'.

### ATOM-SOURCE-20260218-009-0006
**Lines**: 46-51
**Context**: anecdote / evidence
**Tension**: novelty=0.20, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> Introducing a 'coordinator' agent in a multi-agent system burns tokens by relaying messages, loses nuance in handoffs, and complicates debugging when issues arise.

### ATOM-SOURCE-20260218-009-0008
**Lines**: 52-54
**Context**: anecdote / evidence
**Tension**: novelty=0.10, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> The author's experience with 8 agents and multiple API keys resulted in hundreds of dollars in token costs and output worse than one decent agent with the right setup.

### ATOM-SOURCE-20260218-009-0011
**Lines**: 62-68
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.20, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> Multi-agent setups incur significantly higher costs due to token consumption for context loading, personality files, and memory retrieval for each agent, whereas a single-agent setup with skills loads context only once, resulting in substantial savings.

### ATOM-SOURCE-20260218-009-0015
**Lines**: 91-94
**Context**: anecdote / evidence
**Tension**: novelty=0.30, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.60

> A single OpenClaw agent named Larry, equipped with a social media skill, achieved 8 million TikTok views in a week and earned $4,000 in 24 hours by automating content creation, scheduling, and posting.

## Concept (2)

### ATOM-SOURCE-20260218-009-0002
**Lines**: 20-22
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.70

> An agent is a separate brain with its own memory, context window, and personality, akin to hiring a new employee unfamiliar with the company.

### ATOM-SOURCE-20260218-009-0003
**Lines**: 23-25
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.70

> A skill is a set of instructions an existing agent can follow, adding new capabilities to the same brain, memory, and context.

## Praxis Hook (7)

### ATOM-SOURCE-20260218-009-0007
**Lines**: 50-53
**Context**: method / evidence
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> For heavy, isolated research tasks that shouldn't clog the main conversation, spawn a sub-agent that performs the work, reports back, and then terminates. OpenClaw supports this by allowing the main agent to initiate background tasks that run in isolation and announce results upon completion.

### ATOM-SOURCE-20260218-009-0009
**Lines**: 54-56
**Context**: method / evidence
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> Utilize different AI models for specific jobs, such as using a cheaper model like Sonnet for data grinding or pure scraping tasks, while reserving a more capable main agent for complex interactions.

### ATOM-SOURCE-20260218-009-0010
**Lines**: 57-58
**Context**: method / evidence
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> For shared work environments where multiple people interact with an agent, use a separate agent with its own permissions to manage interactions effectively.

### ATOM-SOURCE-20260218-009-0012
**Lines**: 72-73
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To add a skill in OpenClaw, create a folder within your workspace's skills directory and place a SKILL.md file inside it, containing instructions for your agent.

### ATOM-SOURCE-20260218-009-0013
**Lines**: 76-83
**Context**: method / evidence
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To create an 'Email skill' for an agent, provide specific instructions in the SKILL.md file, such as keeping emails short (3-5 sentences), starting with the recipient's name, signing off with just your name, matching formality, avoiding phrases like 'just following up,' and not using mdashes.

### ATOM-SOURCE-20260218-009-0014
**Lines**: 85-86
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.60, actionability=0.90, epistemic_stability=0.80

> Install community skills from ClawHub by simply asking your agent to 'install the [name] skill,' and the agent will handle the rest.

### ATOM-SOURCE-20260218-009-0016
**Lines**: 100-105
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> The recommended setup for AI agents involves one main agent with a defined personality and context files, skills for every repeating task, channels mapped to specific skills, sub-agents only for heavy background tasks, and memory files for continuity and long-term recall.
