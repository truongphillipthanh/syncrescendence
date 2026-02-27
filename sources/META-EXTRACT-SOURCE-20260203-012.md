# Extraction: SOURCE-20260203-012

**Source**: `SOURCE-20260203-x-article-andrey__hq-what_lives_inside_openclaw.md`
**Atoms extracted**: 14
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (4)

### ATOM-SOURCE-20260203-012-0002
**Lines**: 18-22
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.70

> Every serious agent system currently shipping, including custom GPTs, Claude's project files, and Cursor's rules configurations, has converged on using text (markdown) files on disk as the source of truth for agent behavior.

### ATOM-SOURCE-20260203-012-0004
**Lines**: 35-40
**Context**: anecdote / evidence
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.20, speculation_risk=0.20, actionability=0.50, epistemic_stability=0.60

> The default SOUL.md in OpenClaw is generic and can lead to unsatisfactory, impersonal interactions because it's not tailored to the user's specific communication preferences or values.

### ATOM-SOURCE-20260203-012-0008
**Lines**: 61-65
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> Logging every component of a conversation with an agent leads to increased token consumption and degraded response quality due to noise making relevant information harder to identify.

### ATOM-SOURCE-20260203-012-0012
**Lines**: 88-93
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> The 'Heartbeat' system requires intelligence from core files (like USER.md and SOUL.md) to be useful; for example, an 'urgent emails' check needs USER.md to define 'urgency', and 'calendar event reminders' need SOUL.md to define timing and format.

## Concept (3)

### ATOM-SOURCE-20260203-012-0003
**Lines**: 29-33
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> SOUL.md defines an agent's personality, including its tone, response prioritization, and communication boundaries, by being read at the beginning of every session.

### ATOM-SOURCE-20260203-012-0011
**Lines**: 82-86
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> The 'Heartbeat' system in an agent is a scheduled interval where the agent independently wakes up, checks a list of monitored items, and decides if anything warrants communication, functionally differentiating it from a simple chatbot.

### ATOM-SOURCE-20260203-012-0014
**Lines**: 101-101
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> The 'Cron' system handles tasks requiring precise timing (e.g., scheduled news checks), differing from the 'Heartbeat' system which focuses on proactive awareness checking at periodic intervals.

## Framework (1)

### ATOM-SOURCE-20260203-012-0010
**Lines**: 75-80
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> OpenClaw agents utilize a 'Heartbeat' system for scheduled, independent checks of monitored items, prompting the agent to reach out if warranted, and a 'Cron' system for tasks requiring precise timing.

## Praxis Hook (6)

### ATOM-SOURCE-20260203-012-0001
**Lines**: 10-12
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To effectively set up OpenClaw (Moltbot), understand that the entire setup is rooted in three main files: SOUL.md, USER.md, and MEMORY.md.

### ATOM-SOURCE-20260203-012-0005
**Lines**: 43-48
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> The first half of SOUL.md should define communication preferences with specificity, including how the agent opens conversations, presents research, handles uncertainty, and whether it should push back on requests.

### ATOM-SOURCE-20260203-012-0006
**Lines**: 50-56
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.60

> Include negative constraints in SOUL.md to eliminate unwanted behaviors like corporate pleasantries or repetitive stylistic patterns, as these small annoyances can lead to users abandoning AI tools.

### ATOM-SOURCE-20260203-012-0007
**Lines**: 50-59
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.60

> To manage agent memory effectively and avoid excessive token usage, implement a scoring system for conversations to log only important topics, even if they don't lead to immediate execution.

### ATOM-SOURCE-20260203-012-0009
**Lines**: 69-73
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Alternatively, explicitly instruct the agent to log specific information into its memory (e.g., "log this into your memory.md file") to save time compared to manual copying and pasting.

### ATOM-SOURCE-20260203-012-0013
**Lines**: 95-99
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> To optimize an agent's 'Heartbeat' system, iterate to find the right balance: use a deliberately narrow checklist focused on specific event categories and set intervals that match working patterns to avoid excessive notifications.
