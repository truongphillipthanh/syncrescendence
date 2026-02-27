# Subagent Configurability in Codex Launch Thread
**Hell yeah! Subagent Configurability in Codex will launch tomorrow!**
Create, define, and launch custom agents with your model / reasoning level of choice with a simple edit to config file.
> Plan with one model
> Orchestrate with another
> Execute (with Spark!?)
TY @OpenAIDevs
## Embedded Code Configuration
(Description: A Zed code editor screenshot showing a TOML configuration file for Codex agents. The file is titled "agents_config.toml" and was edited 10 hours ago by jif-oai. The content includes:)
```toml
version = 1
# Default role used when spawn_agent is called without agent_type.
[agent.main]
model = "gpt-5.3-codex"
reasoning_effort = "medium"
read_only = false    # true restricts the agent to read-only sandbox policy
[agents.explorer]
# Override a built-in role by reusing its name. The description is provided to the parent model so that it can decide
# which `agent_type` to use
description = "Fast codebase explorer for investigation tasks."
model = "gpt-5.3-codex-spark"
reasoning_effort = "medium"
read_only = true
[agents.planner]
# A custom role example.
description = "Planning-focused agent that produces execution plans."
model = "gpt-5.1-codex"
reasoning_effort = "high"
read_only = false    # Fallback to false when not defined.
# Optional path to extra role-specific instructions. These instructions will be added as DEVELOPER instructions
# to the context.
instructions_file = "~/.codex/agents/planner.md"
[agents.tester]
# Another custom role with a different profile.
description = "Testing-focused agent for validation and regression checks."
model = "gpt-5.1-codex-shift"
reasoning_effort = "low"
```
(Description: The editor window includes collaborative features and shows a comment "If you think this is a good design, this can land early this week" with reaction indicators.)
---
**Post Details:**
- Posted: 12:12 PM · Feb 16, 2026
- Engagement: 36 replies, 37 reposts, 358 likes, 197 bookmarks, 58.1K views