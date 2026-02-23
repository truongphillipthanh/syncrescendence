---
url: https://www.dbreunig.com/2026/02/10/system-prompts-define-the-agent-as-much-as-the-model.html
title: How System Prompts Define Agent Behavior
domain: dbreunig.com
author: D. Breunig with Srihari Sriraman
published_date: 2026-02-10
captured_date: 2026-02-20
content_type: article
id: SOURCE-20260210-001
original_filename: 20260210-website-how_system_prompts_define_agent--dbreunig.md
status: triaged
platform: website
format: article
creator: dbreunig
signal_tier: strategic
topics:
  - ai-agents
  - prompting
  - context-management
  - cursor
  - codex
  - gemini
  - architecture
teleology: synthesize
notebooklm_category: ai-agents
aliases:
  - "How System Prompts Define Agent Behavior"
synopsis: "How System Prompts Define Agent Behavior **Tags:** AI, AGENTS, SYSTEM PROMPTS, CONTEXT, COLLABORATION, CONTEXT ENGINEERING This post was co-authored with [Srihari Sriraman]( --- Coding agents are fascinating to study. They help us build software in a new way, while themselves exemplifying a novel approach to architecting and implementing software."
key_insights:
  - "They help us build software in a new way, while themselves exemplifying a novel approach to architecting and implementing software."
  - "A critical part of this harness is the system prompt, the baseline instructions for the application."
  - "The system prompt is always present, defining a core set of behaviors, strategies, and tone."
---
# How System Prompts Define Agent Behavior
**Tags:** AI, AGENTS, SYSTEM PROMPTS, CONTEXT, COLLABORATION, CONTEXT ENGINEERING
This post was co-authored with [Srihari Sriraman](https://blog.nilenso.com/blog/2026/02/10/how-system-prompts-define-agent-behaviiour/)
---
Coding agents are fascinating to study. They help us build software in a new way, while themselves exemplifying a novel approach to architecting and implementing software. At their core is an AI model, but wrapped around it is a mix of code, tools, and prompts: the harness.
A critical part of this harness is the system prompt, the baseline instructions for the application. This context is present in every call to the model, no matter what skills, tools, or instructions are loaded. The system prompt is always present, defining a core set of behaviors, strategies, and tone.
Once you start analyzing agent design and behavior, a question emerges: how much does the system prompt actually determine an agent's effectiveness? We take for granted that the model is the most important component of any agent, but how much can a system prompt contribute? Could a great system prompt paired with a mediocre model challenge a mediocre prompt paired with a frontier model?
To find out, we obtained and analyzed system prompts from six different coding agents. We clustered them semantically, comparing where their instructions diverged and where they converged. Then we swapped system prompts between agents and observed how behavior changed.
**System prompts matter far more than most assume. A given model sets the theoretical ceiling of an agent's performance, but the system prompt determines whether this peak is reached.**
---
## The Variety of System Prompts
To understand the range of system prompts, we looked at six CLI coding agents: Claude Code, Cursor, Gemini CLI, Codex CLI, OpenHands, and Kimi CLI. Each performs the same basic function: given a task they gather information, understands the code base, writes code, tracks their progress, and runs commands. But despite these similarities, the system prompts are **quite** different.
### Try It Out
Explore the above figures interactively in [context viewer](https://nilenso.github.io/context-viewer/g/960d42ad-314c-44cf-8594-4b009ef528a1/comparison?sidebar=0&panel=0&sortBy=category&sortDir=asc&import=https://raw.githubusercontent.com/nilenso/long-prompts-analysis/refs/heads/main/context-viewer-exports/system-prompts-simpler.json).
(Image: Waffle chart comparisons of 6 coding agent system prompts. A breakdown showing token distribution across multiple categories including Code Style, Environment Details, Personality & Steering, Tool Descriptions & Instructions, and Workflow Guidance for six different coding agents.)
---
We're analyzing [exfiltrated system prompts](https://github.com/asgeirtj/system_prompts_leaks), which we clean up and [host here](https://github.com/nilenso/long-prompts-analysis/tree/main/data/prompts/filtered)[^1]. Each of these is fed into [context-viewer](https://github.com/nilenso/context-viewer), a tool Srihari developed that chunks contexts in semantic components for exploration and analysis.
Looking at the above visualizations, there is plenty of variety. Claude, Codex, Gemini, and OpenHands roughly prioritize the same instructions, but vary their distributions. Further, prompts for Claude Code and OpenHands both are less than half the length of prompts in Codex and Gemini.
Cursor's and Kimi's prompts are dramatically different. Here we're looking at Cursor's prompt that's paired with GPT-5 ([Cursor uses slightly different prompts when hooked to different models](https://www.adiasg.com/blog/comparing-cursors-prompts-across-models)), and it spends over a third of its tokens on personality and steering instructions. Kimi CLI, meanwhile, contains zero workflow guidance, barely hints at personality instructions, and is the shortest prompt by far.
Given the similar interfaces of these apps, we're left wondering: why are their system prompts so different?
There's two main reasons the system prompts vary: **model calibration** and **user experience**.
Each model has its own quirks, rough edges, and baseline behaviors. If the goal is to produce a measured, helpful TUI coding assistant, each system prompt will have to deal with and adjust for unique aspects of the underlying model to achieve this goal. This **model calibration** reins in problematic behavior.
System prompts also vary because they specify slightly different **user experience**. Sure, they're all text-only, terminal interfaces that explore and manipulate code. But some are more talkative, more autonomous, more direct, or require more detailed instructions. System prompts define this UX and, as we'll see later, we can make a coding agent "feel" like a different agent just by swapping out the system prompt.
We can get a glimpse of these two functions together by looking at how a given system prompt changes over time, especially as new versions of models arrive. For example:
### Try It Out
Explore the above figures interactively in [context viewer](https://nilenso.github.io/context-viewer/g/b179a05f-2bd4-4012-83ab-42a0cb1e79fd/comparison?sidebar=0&panel=0&legend=compact&sortBy=category&sortDir=asc&cols=5&import=https://raw.githubusercontent.com/nilenso/long-prompts-analysis/refs/heads/main/context-viewer-exports/claude-prompt-evolution-export-simpler.json). Or, [check out Codex's system prompt evolution in similar detail](https://nilenso.github.io/context-viewer/g/56b68fb5-7221-4c04-807e-b590f138c1fe/comparison?sidebar=0&panel=0&view=tokens-absolute&legend=compact&sortBy=category&sortDir=asc&cols=10&spr=4&import=https://raw.githubusercontent.com/nilenso/long-prompts-analysis/refs/heads/main/context-viewer-exports/codex-prompt-evolution-export-only-codex.json).
(Image: Claude Code System Prompt Evolution chart showing token count by category over time. A stacked bar chart tracking changes across multiple versions (Opus 4 through Opus 4.5/4.6 and Haiku 4.3/4.5) with color-coded categories: Code Style, Environment Details, Personality & Steering, Tool Descriptions & Instructions, and Workflow Guidance.)
---
Note how the system prompt isn't stable, nor growing in a straight line. It bounces around a bit, as the Claude Code team tweaks the prompt to both adjust new behaviors and smooth over the quirks of new models. Though the trend is a march upward, as the coding agent matures.
If you want to dive further into Claude Code's prompt history, Mario Zechner has [an excellent site](https://cchistory.mariozechner.at) where he highlights the exact changes from version to version.
### Go Deeper
Sometimes instructions are just…**weird**. Srihari [cataloged some of the odder instructions he found while exploring coding agent system prompts](https://blog.nilenso.com/blog/2026/02/12/weird-system-prompt-artefacts/).
---
## The Common Jobs of a Coding Agent System Prompt
While these prompts vary from tool to tool, there are many commonalities that each prompt features. There is clear evidence that these teams are [fighting the weights](https://www.dbreunig.com/2025/11/11/don-t-fight-the-weights.html): they use repeated instructions, all-caps admonishments, and stern warnings to adjust common behaviors. This shared effort suggests common patterns in their training datasets, which each has to mitigate.
For example, there are **many** notes about how these agents should use comments in their code. Cursor specifies that the model should, "not add comments for trivial or obvious code." Claude states there should be no added comments, "unless the user asks you to." Codex takes the same stance. Gemini instructions the model to, "Add code comments sparingly… NEVER talk to the user through comments."
These consistent, repeated instructions are warranted. They fight against examples of conversation in code comments, present in countless codebases and Github repo. This behavior goes deep: we've even seen that [Opus 4.5 will reason in code comments if you turn off thinking](https://x.com/aidenybai/status/1993901129210712129).
System prompts also repeatedly specify that tool calls should be parallel whenever possible. Claude should, "maximize use of parallel tool calls where possible." Cursor is sternly told, "CRITICAL INSTRUCTION: involve all relevant tools concurrently… DEFAULT TO PARALLEL." Kimi adopts all-caps as well, stating, "you are HIGHLY RECOMMENDED to make [tool calls] in parallel."
This likley reflects the face that most post-training reasoning and agentic examples are **serial** in nature. This is perhaps easier to debug and a bit of delay when synthesizing these datasets isn't a hinderence. However, in real world situations, users certainly appreciate the speed, so system prompts need to override this training.
Both of these examples of **fighting the weights** demonstrate how system prompts are used to smooth over the quirks of each model (which they pick up during training) and improve the user experience in an agentic coding application.
Much of what these prompts specify is shared; common adjustments, common desired behaviors, and common UX. But their differences notably affect application behavior.
### Go Deeper
Srihari looked at more examples of fighting the weights to understand [how system prompts reveal model biases](https://blog.nilenso.com/blog/2026/02/12/how-system-prompts-reveal-model-biases/).
---
## Do the Prompts Change the Agent?
Helpfully, [OpenCode](https://opencode.ai) [allows users to specify custom system prompts](https://opencode.ai/docs/modes/#prompt). With this feature, we can drop in prompts from Kimi, Gemini, Codex and more, removing and swapping instructions to measure their contribution.
We gave SWE-Bench Pro test questions to two applications: two agents running the OpenCode harness, calling Opus 4.5, but with one one using the Claude Code system prompt and the other armed with Codex's instructions.
Time and time again, the agent workflows diverged immediately. For example:
| Step | Codex Prompt | Claude Prompt |
|------|--------------|---------------|
| 1 | Read prompt + Glob README (parallel) | Read prompt file (wrong path) |
| 2 | Read README | pwd && ls (recovery) |
| 3 | Read 3 files in parallel | Read README |
| 4 | Read hostblock.py | Run tests first (diagnostic) |
| 5 | Create 3-item todo | Read test files |
| 6 | Document all test cases | Read source files |
| 7 | Implement (passes) | Create 2-item todo |
| 8 | — | Implement (2 failures) |
| 9 | — | Fix (1 failure) |
| 10 | — | Fix (passes) |
(Image: Workflow comparison table. A side-by-side comparison showing how Codex and Claude prompts direct different approaches to solving the same task. Codex takes a methodical, documentation-first approach while Claude adopts an iterative, test-driven strategy.)
---
The Codex prompt produced a methodical, documentation-first approach: understand fully, then implement once. The Claude prompt produced an iterative approach: try something, see what breaks, fix it.
This pattern remains consistent over many SWE Bench problems. If we average the contexts for each model and system prompt pair, we get the following:
(Image: SWE-bench Context Composition by Agent chart showing average tokens per task. Four heatmap visualizations comparing Opus Claude Code Prompt, Opus Codex CLI Prompt, GPT Claude Code Prompt, and GPT Codex CLI Prompt. Each shows different patterns with categories: Explore, Analyze, Understand, Plan, Implement, Verify, Complete. Color-coded squares represent token allocation across these stages.)
---
### Try It Out
Explore the above figures interactively in [context viewer](https://nilenso.github.io/context-viewer/g/67175678-6244-45bc-b022-238b72f8e646/comparison?sidebar=0&panel=0&legend=compact&sortBy=category&sortDir=asc&cols=5&import=https://raw.githubusercontent.com/nilenso/long-prompts-analysis/refs/heads/main/context-viewer-exports/swapping-prompts-swe-tasks.json).
---
All prompt-model combinations correctly answered this subset of SWE Bench Pro questions. But **how** they succeeded was rather different. The system prompts shaped the workflows.
### Go Deeper
Srihari explored [Codex CLI and Claude Code autonomy](https://blog.nilenso.com/blog/2026/02/12/codex-cli-vs-claude-code-on-autonomy/), and how the system prompt may shape their behavior.
---
## System Prompts Deserve More Attention
Last week, when Opus 4.6 and Codex 5.3 landed, people began putting them through the paces, trying to decide which would be their daily driver. Many tout the capabilities of one option over another, but just as often are complaints about approach, tone, or other discretionary choices. Further, it seems **every** week brings discussion of a new coding harness, especially for managing swarms of agents.
There is markedly less discussion about the system prompts that define the behaviors of these agents[^2]. System prompts define the UX and smooth over the rough edges of models. They're given to the model with **every** instruction, yet we prefer to talk Opus vs. GPT-5.3 or Gastown vs. Pi.
**Context engineering starts with the system prompt.**
---
## Notes
[^1]: Exfiltrated system prompts represent versions of the system prompt for a given session. It's not 100% canonical, as many AI harnesses assemble system prompts from multiple snippets, given the task at hand. But given the consistent manner with which we can extract these prompts, and comparing them with [public examples](https://github.com/openai/codex/blob/d452bb3ae5b5e0f715bba3a44d7d30a51b5f28ae/codex-rs/core/prompt.md), we feel they are sufficiently representative for this analysis.
[^2]: Though you can use Mario's [system prompt diff tool to explore the changes accompanying Opus 4.6's release](https://cchistory.mariozechner.at/?from=2.1.31&to=2.1.34).
---
**Copyright:** 2026, [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/), [Contact](https://dbreunig.com/contact.html)