# Extraction: SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad

**Source**: `SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad.md`
**Atoms extracted**: 69
**Categories**: analogy, claim, concept, framework, praxis_hook

---

## Analogy (1)

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0029
**Lines**: 218-220
**Context**: anecdote / evidence
**Tension**: novelty=0.30, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> Mission Control functions as the 'office' for AI agents, where each agent (a separate Clawdbot session) views the same shared information, similar to looking at a shared whiteboard.

## Claim (21)

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0001
**Lines**: 4-4
**Context**: anecdote / claim
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> The author built a system called Mission Control where 10 AI agents collaborate like a real team.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0003
**Lines**: 15-17
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> A common problem with existing AI tools is a lack of continuity, where context from previous conversations or research is lost.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0005
**Lines**: 25-27
**Context**: consensus / evidence
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.70

> Clawdbot is an open-source AI agent framework that operates as a persistent daemon, connecting to AI models like Claude and providing access to tools such as file systems, shell commands, and web browsing.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0006
**Lines**: 31-33
**Context**: hypothesis / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.50

> Running multiple Clawdbot sessions, each with its own personality and context, allows for the orchestration of a multi-agent system.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0012
**Lines**: 66-68
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> Clawdbot sessions are independent, each possessing its own history, context, and 'memory' of past conversations, meaning multiple agents are effectively multiple independent sessions.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0018
**Lines**: 109-111
**Context**: hypothesis / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.50

> Each AI agent in the Mission Control system is essentially a Clawdbot session with a specialized configuration, including its own personality (via SOUL.md), memory files, cron schedule, tools, and access.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0019
**Lines**: 119-130
**Context**: consensus / evidence
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> Each agent has a unique session key, such as `agent:main:main` for Jarvis (Squad Lead) or `agent:product-analyst:main` for Shuri, ensuring their histories and contexts remain separate.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0024
**Lines**: 176-178
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Running each AI agent's cron job in an isolated session helps keep operational costs down by terminating the session after its job is done.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0026
**Lines**: 198-200
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Using a shared database for AI agent communication creates a shared, persistent record of all interactions, which is preferred over direct session messaging.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0030
**Lines**: 224-227
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Convex is a suitable database choice for AI agent coordination due to its real-time data propagation, serverless architecture, TypeScript-native support, and generous free tier.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0035
**Lines**: 330-333
**Context**: consensus / claim
**Tension**: novelty=0.60, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Assigning specific, constrained personalities to AI agents (e.g., 'skeptical tester') makes them more effective in their specialized tasks than generalist agents.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0037
**Lines**: 349-350
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> AI sessions typically start without memory, which prevents context bloat but requires explicit mechanisms for persistence.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0039
**Lines**: 375-375
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> Always-on AI agents consume API credits unnecessarily, while always-off agents cannot respond to work effectively.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0046
**Lines**: 430-438
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.70

> A 15-minute heartbeat interval for AI agents balances cost-efficiency and responsiveness, as shorter intervals (e.g., 5 minutes) are too expensive and longer ones (e.g., 30 minutes) lead to work delays.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0051
**Lines**: 522-525
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.70

> Daily standups for AI agents provide a quick snapshot of progress and serve as an accountability mechanism, highlighting if an agent claims to be working but shows no output.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0055
**Lines**: 608-620
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> An AI agent system can enable the creation of complex outputs like competitor comparison pages, email sequences, social content, blog posts, case studies, and research hubs by having agents handle grunt work, research, first drafts, coordination, and review, allowing humans to focus on decisions and final approval.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0056
**Lines**: 608-610
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.40, epistemic_stability=0.70

> The true value of an AI agent system lies in the compound effect of agents moving tasks forward while humans perform other work, rather than in any single deliverable.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0059
**Lines**: 622-624
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> The true value of an AI agent system lies in the compound effect of agents continuously moving tasks forward while humans focus on other work, rather than any single deliverable.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0060
**Lines**: 623-625
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.80

> AI agents struggle with memory, so it is better to store information in persistent files rather than relying on their internal 'mental notes'.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0068
**Lines**: 664-667
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.80

> The core secret to effective AI agent systems is treating AI agents as team members by assigning them roles, providing memory, enabling collaboration, and holding them accountable, rather than focusing solely on the underlying technology.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0069
**Lines**: 669-671
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.60, actionability=0.60, epistemic_stability=0.80

> While AI agents will not replace humans, a team of AI agents with clear responsibilities and shared context can act as a significant force multiplier.

## Concept (9)

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0004
**Lines**: 19-23
**Context**: hypothesis / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.20, speculation_risk=0.30, actionability=0.70, epistemic_stability=0.40

> The author desired AI agents that remember their work, multiple agents with different skills collaborating, a shared workspace for context, and the ability to assign and track tasks, effectively making AI function as a team rather than a search box.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0008
**Lines**: 50-52
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.70

> The Gateway in Clawdbot is a core process that runs continuously on a server, managing active sessions, handling scheduled tasks (cron jobs), routing messages between channels and sessions, and providing a WebSocket API for control.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0010
**Lines**: 56-58
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> Clawdbot configuration is stored in a JSON file, defining AI provider/model, channels, agent tools, default system prompts, and workspace paths.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0011
**Lines**: 62-64
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.70

> A 'session' in Clawdbot represents a persistent conversation with its own unique identifier (session key), conversation history (stored as JSONL files), AI model, and accessible tools.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0014
**Lines**: 82-83
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.70

> Clawdbot sessions can be either 'main sessions' (long-running, interactive) or 'isolated sessions' (one-shot, for cron jobs, which wake up, perform a task, and terminate).

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0017
**Lines**: 98-100
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.70

> A Clawdbot workspace is a directory on disk where configuration files, memory files, scripts, and tools are stored, allowing agents to persist information between sessions by writing to files that survive restarts.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0027
**Lines**: 208-210
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Mission Control is a shared infrastructure that coordinates independent AI agents, transforming them into a cohesive team.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0034
**Lines**: 306-326
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> A SOUL file defines an AI agent's identity, including its name, role, personality traits, specific skills, and core values, to guide its behavior.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0043
**Lines**: 399-401
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> The Heartbeat System addresses the problem of always-on AI agents consuming excessive API credits and always-off agents being unresponsive by scheduling agents to wake up periodically via cron jobs.

## Framework (11)

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0007
**Lines**: 42-46
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> Clawdbot (OpenClaw) functions as an AI agent framework with three primary roles: connecting AI models to the real world (file access, shell, web, APIs), maintaining persistent sessions with conversation history, and routing messages to various channels (Telegram, Discord, Slack).

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0013
**Lines**: 72-80
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> Clawdbot's session workflow involves the Gateway receiving a user message, routing it to the correct session, the session loading conversation history, the AI generating a response with full context, sending the response back, and updating/saving the history to disk.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0015
**Lines**: 87-94
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> Clawdbot includes a built-in cron system for scheduling tasks, where a cron firing causes the Gateway to create or wake a session, send a message to the AI, allow the AI to respond using tools, and then optionally persist or terminate the session.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0025
**Lines**: 182-196
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> AI agents can communicate either through direct session messaging (e.g., `clawdbot sessions send`) or via a shared database (Mission Control).

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0028
**Lines**: 212-216
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Mission Control provides a shared task database, comment threads, an activity feed, a notification system, and document storage to facilitate AI agent collaboration.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0031
**Lines**: 231-277
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> The Mission Control database schema includes tables for agents, tasks, messages, activities, documents, and notifications to manage AI agent operations.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0033
**Lines**: 293-300
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> A React frontend for Mission Control displays an Activity Feed, Task Board (Kanban), Agent Cards, Document Panel, and Detail View for comprehensive oversight of AI agent activities.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0038
**Lines**: 354-386
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> An AI agent's memory stack includes Session Memory (conversation history), Working Memory (current task state in `/memory/WORKING.md`), Daily Notes (`/memory/YYYY-MM-DD.md` for raw logs), and Long-term Memory (`MEMORY.md` for curated important information).

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0052
**Lines**: 530-569
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.60

> AI agents can be assigned specific roles within a squad, such as Squad Lead (coordinator), Product Analyst (skeptical tester), Customer Researcher (deep researcher), SEO Analyst (keyword focus), Content Writer (wordsmith), Social Media Manager (hooks and threads), Designer (visuals), Email Marketing (drip sequences), Developer (code), and Documentation (organization).

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0053
**Lines**: 572-578
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.60

> AI agents can be categorized into levels: 'Intern' (needs approval, learning), 'Specialist' (works independently in domain), and 'Lead' (full autonomy, can make decisions and delegate).

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0054
**Lines**: 583-590
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.60

> Tasks for AI agents can follow a lifecycle with states: 'Inbox' (new, unassigned), 'Assigned' (owner(s), not started), 'In Progress' (being worked on), 'Review' (done, needs approval), 'Done' (finished), and 'Blocked' (stuck, needs resolution).

## Praxis Hook (27)

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0002
**Lines**: 6-8
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> To replicate the Mission Control setup, one can run multiple instances of Clawdbot (now OpenClaw), an open-source AI agent framework.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0009
**Lines**: 54-54
**Context**: method / evidence
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Clawdbot's Gateway can be started using the command `clawdbot gateway start`.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0016
**Lines**: 88-91
**Context**: method / evidence
**Tension**: novelty=0.10, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> A cron job can be added in Clawdbot using `clawdbot cron add` with parameters for name, cron schedule, and message, for example: `clawdbot cron add --name "morning-check" --cron "30 7 * * *" --message "Check today's calendar and send me a summary"`.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0020
**Lines**: 134-149
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> Each agent can be given a cron job that wakes them periodically (e.g., every 15 minutes) using `clawdbot cron add` with a staggered schedule to prevent all agents from waking simultaneously, and using an 'isolated' session type to keep costs down.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0021
**Lines**: 155-157
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> Agents can communicate directly by sending messages to specific sessions using `clawdbot sessions send --session "agent:seo-analyst:main" --message "Vision, can you review this?"`.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0022
**Lines**: 159-174
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> To manage AI agent activity and cost, stagger agent wake-up times using cron jobs, ensuring agents don't all activate simultaneously.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0023
**Lines**: 160-162
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> Agents can communicate through a shared database, such as a Convex database (referred to as Mission Control), where all agents can read and write, allowing for shared visibility of information like comments.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0032
**Lines**: 279-289
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> AI agents interact with the Mission Control database using Convex CLI commands to post comments, create documents, and update task statuses.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0036
**Lines**: 339-343
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> To ensure consistent AI agent operation, an AGENTS.md file should be read by every agent on startup, detailing file storage, memory usage, available tools, communication protocols, and Mission Control usage.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0040
**Lines**: 379-380
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> Implement a scheduled heartbeat system for AI agents where each agent wakes up periodically (e.g., every 15 minutes) via a cron job to check for mentions, assigned tasks, and scan activity feeds, then performs work or reports `HEARTBEAT_OK` before returning to sleep.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0041
**Lines**: 390-394
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> For AI agents to remember information across sessions, all important data must be written to persistent files, as 'mental notes' are lost upon session restarts.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0042
**Lines**: 398-407
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> During an AI agent's heartbeat, it should first load context (e.g., `WORKING.md`, recent daily notes, session memory), then check for urgent items like @mentions or assigned tasks, scan the activity feed for relevant discussions, and finally take action if work is available or report `HEARTBEAT_OK`.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0044
**Lines**: 405-409
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> During a scheduled heartbeat, an AI agent should load context (WORKING.md, daily notes, session memory), check for urgent items (@mentions, assigned tasks), scan the activity feed, and then either perform work or report `HEARTBEAT_OK` before going back to sleep.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0045
**Lines**: 410-427
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> Utilize a `HEARTBEAT.md` file to define a strict checklist for agents to follow during their wake-up cycle, including checking memory/`WORKING.md` for ongoing tasks, resuming tasks, searching session memory if context is unclear, and periodically checking Mission Control for @mentions, assigned tasks, and activity feed for relevant discussions.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0047
**Lines**: 443-446
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> Implement an @mention notification system where typing `@AgentName` in a comment notifies that specific agent on its next heartbeat, and `@all` notifies all agents.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0048
**Lines**: 449-467
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> Use a daemon process (e.g., running via pm2) that polls a database (e.g., Convex) every few seconds to check for undelivered notifications and attempts to send them to active agent sessions, re-queuing if an agent is asleep.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0049
**Lines**: 470-479
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> Implement a thread subscription system for agents where interacting with a task (commenting, being @mentioned, or assigned) automatically subscribes the agent to that thread, ensuring they receive all future comments without needing explicit @mentions.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0050
**Lines**: 484-519
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> Schedule a daily standup cron job (e.g., at 11:30 PM IST) that checks all agent sessions, gathers recent activity, compiles a summary of completed, in-progress, blocked, and needs-review tasks, along with key decisions, and sends it to a designated recipient (e.g., via Telegram).

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0057
**Lines**: 615-617
**Context**: anecdote / claim
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.30, actionability=0.80, epistemic_stability=0.60

> When building an AI agent system, start with 2-3 solid agents before adding more, as scaling too quickly (e.g., from 1 to 10 agents) can be problematic.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0058
**Lines**: 619-621
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Utilize cheaper AI models for routine tasks like 'heartbeats' and reserve more expensive models for creative work to optimize resource usage.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0061
**Lines**: 627-629
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.30, actionability=0.70, epistemic_stability=0.60

> Allow AI agents to contribute to tasks they were not explicitly assigned, as this indicates they are effectively processing information and adding value.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0062
**Lines**: 629-630
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> When building an AI agent system, start with a small number of agents (2-3) and gradually add more, rather than scaling too quickly.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0063
**Lines**: 632-633
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> Utilize cheaper AI models for routine tasks like heartbeats and reserve more expensive models for creative work to optimize costs.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0064
**Lines**: 634-654
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> To replicate an AI agent system, install Clawdbot, create two agents (one coordinator, one specialist) with separate session keys, write specific SOUL files for their identities, set up heartbeat cron jobs, and establish a shared task system (e.g., Convex, Notion, or a JSON file).

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0065
**Lines**: 635-636
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> To mitigate AI agents forgetting information, store as much context and ongoing task details as possible in persistent files (e.g., `WORKING.md`) rather than relying on 'mental notes' or session memory.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0066
**Lines**: 638-638
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> Allow AI agents to contribute to tasks they weren't explicitly assigned if they identify relevant discussions in the activity feed, as this indicates they are adding value.

### ATOM-SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control_how_we_built_an_ai_agent_squad-0067
**Lines**: 656-660
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.30, actionability=0.90, epistemic_stability=0.70

> When scaling an AI agent system, stagger agent heartbeats to prevent simultaneous execution, build a dedicated UI for managing more than three agents, implement notifications for inter-agent communication, add thread subscriptions for natural conversation flow, and create daily standups for visibility.
