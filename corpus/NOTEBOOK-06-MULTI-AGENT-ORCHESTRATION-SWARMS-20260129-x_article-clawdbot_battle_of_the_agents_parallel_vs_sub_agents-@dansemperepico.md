# ClawdBot Battle of the Agents - Parallel vs Sub-Agents

![Description: A futuristic dark command center scene showing a silhouetted figure seated at a curved control panel facing a large curved wall display. The display shows 8 illuminated AI head profiles arranged in an arc - rendered as neon blue, green, and orange holographic busts with digital interfaces and code visible in the background. Additional monitoring panels and technical readouts line the sides of the room, creating an atmosphere of managing multiple AI agents simultaneously.]

There are three hallmark moments in the journey of anyone getting into AI:

1. The first time they use an LLM in a chat interface (like chatGPT or Claude)
2. The first time they use an AI agent (like Claude Code, Claude Cowork, ClawdBot, or Manus)
3. The first time they use multiple AI agents to carry out tasks simultaneously.

Each one of these blew my mind more than the previous.

Today I'm going to talk about running multiple AI agents. This is where things get really interesting and you can get done in 5 minutes what would have taken you 5 hours.

I'll explain what parallel agents and sub-agents are, and how and when to use them, so you can deploy your own roboto army and get hours of your day back.

(commanding an army of robots is awesome)

Plus I'll share a cool way that one of these types of agents can save you when things go wrong with your Clawdbot.

## What are Parallel Agents?

These are agents that run independently of each other, with their own context, memory, personalities, and separate Telegram bots. They can also communicate and share knowledge and memory.

Think of them like having three different employees with different roles that all report directly to you. They can communicate with each other, but it doesn't happen often unless their functions are closely related.

I have three of these. A chief of staff. A chief marketing officer. A health/fitness/nutrition coach.

## What are Sub-Agents?

These are temporary workers spawned and managed by a parallel agent for specific tasks.

For example, when I ask my chief of staff parallel agent, who runs on the powerful but expensive Opus 4.5 model, to do tasks that don't require such a powerful model, I have him spin up sub-agents using cheaper models better suited for the task at hand.

The main agent manages the sub-agent. When the sub-agent finishes, the main agent delivers the result to me.

Sub-agents are disposable. They don't retain memory which is actually a feature since it keeps context windows clean.

Think of it like one of your department heads in your business hiring and managing contractors on a project by project basis.

## When to Use Parallel Agents

### When you need agents across different domains of expertise.

My health coach Greg knows my workout history, body stats, nutrition targets. My chief of staff rupert has a big picture overview of everything in both my business and personal life, while Ogilvy focuses on helping me with marketing.

### You want direct and separate access to your agent with separate chat records

I want to be able to talk to Greg about my training or my food tracking, without it polluting another conversation I'm having with Rupert about the CTO parallel agent he's helping me spin up.

### Redundancy and Back Up

When Rupert helped me spin up my first parallel agent, he broke something with his own telegram bot/agent configuration.

Luckily, Greg who was a new parallel agent at the time, was still operational, so I used Greg to troubleshoot the issue and get Rupert back online.

### Different models for different jobs

Greg runs on sonnet (cheaper, good enough for fitness/health coaching). Rupert runs on Opus 4.5 (expensive but he's handling more complex stuff). Ogilvy runs on Gemini (I like this better for writing)

## When to Use Sub-Agents

### Batch/Grunt work

Today I connected the Things 3 skill to my ClawdBot, and Rupert spawned sub-agents to help organise 40+ tasks. This would have cost a lot of Opus 4.5 tokens which would have been overkill. Plus, while the sub-agent is doing work, you can still use Rupert for something else, or have him spin up more sub-agents.

### Research Tasks

I'm thinking about getting a cybertruck, so I had Rupert spawn sub-agents to research user reviews on Reddit and write me a report.

### Cost savings

Sub-Agents are the most granular way I have found to apply the right model for the right tasks, resulting in lower token usage and less costs.

The best thing about spawning sub-agents is that it leaves the main agent free to still help you with other stuff while the sub-agent works on a task.

Here's a quick decision table you can use to know when to use parallel vs sub-agents

![Description: A dark-themed decision table with two columns - "Situation" and "Use". The table contains seven rows:
1. Different expertise domain | Parallel agent
2. You want direct conversation | Parallel agent
3. Redundancy/backup needed | Parallel agent
4. Batch/repetitive task | Sub-agent
5. Research and report back | Sub-agent
6. Cost-sensitive work | Sub-agent
7. You want one point of contact | Sub-agent]

Tomorrow, I'll be deploying and trying my hand at vibe coding with a CTO parallel agent.

I'll get it to make something cool and report back tomorrow.

---

**Posted:** 11:15 AM · Jan 29, 2026  
**Engagement:** 6 replies · 10 reposts · 80 likes · 252 bookmarks · 50.7K views