---
url: https://x.com/affaanmustafa/status/2018270130674029037
author: "cogsec (@affaanmustafa)"
captured_date: 2026-02-14
id: SOURCE-20260202-009
original_filename: 20260202-x_thread-guide_tutorials_p1_the_orchestration-affaanmustafa.md
status: triaged
platform: x
format: thread
creator: affaanmustafa
signal_tier: tactical
topics:
  - ai-agents
  - automation
  - developer-tools
  - orchestration
teleology: implement
notebooklm_category: ai-agents
aliases:
  - "cogsec - orchestration workflow tutorial"
synopsis: "Tutorial demonstrating parallel agent orchestration using 6 terminals, 1 orchestrator, and tmux for visual parallel execution. Shows embedded skills in prompts, subagents, and orchestration planning with the ability to watch, edit, and stop individual background processes independently."
key_insights:
  - "Visual tmux-based orchestration provides more degrees of freedom than opaque background task spawning — you can watch, interact with, and stop individual agent processes."
  - "The orchestration pattern combines embedded skills, subagents, and parallelization with verification loops for reliable multi-agent execution."
  - "Presenting agent orchestration as visual terminal multiplexing makes the coordination pattern tangible and debuggable."
---
# Guide Tutorials: P1 - The Orchestration Workflow

**cogsec** @affaanmustafa · Feb 2, 2026

Guide Tutorials : P1 - The Orchestration Workflow

6 terminals. 1 orchestrator. Parallel execution.

**From Shorthand:**
- Embedded skills in prompts
- Subagents
- Orchestration + Planning
- tmux

**From Longform:**
- Parallelization
- Groundwork
- Verification loops

(hidden easter egg)

(Description: Video screenshot showing a multi-monitor setup with six Claude Code terminal windows running in parallel. Each terminal displays code execution with orange status indicators at the top. Green progress bars are visible indicating active processes. The setup demonstrates tmux splitting of multiple terminals for parallel agent orchestration, with the orchestrator managing execution across all instances.)

---

## Reply to @alxfazio

**cogsec** @affaanmustafa · Feb 2

> what's the difference between this and just asking claude to spawn 5 background tasks in parallel

thats literally what I did in the video its all background processes, except its visual as you can watch and edit / stop the output in individual background processes / you can interact with individual processes without the orchestration

more degrees of freedom this way