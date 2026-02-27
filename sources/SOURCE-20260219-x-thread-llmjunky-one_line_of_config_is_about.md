---
url: https://x.com/LLMJunky/status/2024647077586731351
author: am.will
handle: LLMJunky
published_date: February 19, 2026
captured_date: February 21, 2026
post_count: 2
id: SOURCE-20260219-023
original_filename: "20260219-x_thread-one_line_of_config_is_about-@LLMJunky.md"
status: triaged
platform: x
format: thread
creator: llmjunky
signal_tier: tactical
topics:
  - prompting
  - testing
  - codex
  - openai
  - multi-agent
  - token-management
teleology: reference
notebooklm_category: coding-tools
aliases:
  - "Agent Teams Coming to Codex"
synopsis: "Agent Teams Coming to Codex One line of config is about to change how you Codex Update 0.105.0 will bring configurable multi-agent depth. Your agents can now spawn agents that spawn agents. Max agent depth used to be hard-coded to 1 level deep. Root agent spawns a researcher. Researcher spawns a frontend agent, a backend agent, a tester, and code reviewer. All running in parallel."
key_insights:
  - "Agent Teams Coming to Codex One line of config is about to change how you Codex Update 0.105.0 will bring configurable multi-agent depth."
  - "Your agents can now spawn agents that spawn agents."
  - "Max agent depth used to be hard-coded to 1 level deep."
---
# Agent Teams Coming to Codex
One line of config is about to change how you Codex
Update 0.105.0 will bring configurable multi-agent depth. Your agents can now spawn agents that spawn agents.
Max agent depth used to be hard-coded to 1 level deep. Not anymore.
Root agent spawns a researcher. Researcher spawns a frontend agent, a backend agent, a tester, and code reviewer. All running in parallel.
The catch? It will annihilate your token budget. If you're one of those who struggles to use all the tokens on your Pro account, problem solved lol.
But beware: a single prompt could spiral into dozens of parallel model calls if setup irresponsibly.
But with the right scaffolding? Agent teams that divide work, delegate subtasks, and coordinate across branches.
Things are getting rather interesting, wouldn't you agree?
Instructions in ze comments. 👇
(Description: A technical diagram showing "Agent Teams Coming to Codex" with a central "ORCHESTRATOR AGENT" node connected to multiple "Subagent" nodes in a network topology, rendered with glowing blue and orange cyberpunk-style visuals and interconnecting paths)
---
## Post 2
To test early:
```
npm i -g @openai/codex@0.105.0-alpha.6
```
In config:
```
[agents]
max_threads = 12
max_depth = 2
```
(Description: Code snippet showing configuration syntax with comments explaining:
- "Tag: day 2x rate limits until April 2nd"
- Discussion of first-level subagents, nested agent spawning, token limits
- Agent spawned configuration with call, call_sku65315x8234231234, result status: pending [set], prompt: Reply exactly: N-2
- Waiting for agents section with call_sku165hx2x3hx8h849, nested async calls, parallel async-task completion timeouts
- Mail templates with call_sku52hx2x8hx34hx949, Constraints to email task completion
- First-level: N-1, Second-level: N-2
- "Try tests for glitches"
- "npm i | codex online ~ -m -i split -m -w -cmd -exit")
---