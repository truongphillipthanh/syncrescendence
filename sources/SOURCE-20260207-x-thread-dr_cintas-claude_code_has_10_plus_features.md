---
url: https://x.com/dr_cintas/status/2020201275040641385
author: "Alvaro Cintas (@dr_cintas)"
captured_date: 2026-02-14
id: SOURCE-20260207-017
original_filename: "20260207-x_thread-claude_code_has_10_plus_features-@dr_cintas.md"
status: triaged
platform: x
format: thread
creator: dr_cintas
signal_tier: tactical
topics: [claude-code, developer-tools, tutorial, reference]
teleology: reference
notebooklm_category: claude-code
aliases: ["Alvaro Cintas - Claude Code Hidden Features"]
synopsis: "Repository overview explaining 10+ Claude Code features most users never touch: Skills, Subagents, Memory, Hooks, and MCP servers. Covers when to use each feature and how to set them up properly."
key_insights: ["Most Claude Code users only use basic chat and miss Skills, Subagents, Memory, Hooks, and MCP servers entirely", "Each feature has specific use cases — understanding when to use each one prevents overcomplication", "A single reference repo can serve as the setup guide for all advanced Claude Code features"]
---
# Claude Code: 10+ Hidden Features Explained

Claude Code has 10+ features most people never touch.

**Skills. Subagents. Memory. Hooks. MCP servers.**

This repo explains when to use each one, and how to set them up properly.

**100% Open Source.**

(Description: A GitHub repository preview card for "claude-code-best-practice" with the tagline "practice makes claude perfect", showing 345 stars. Below the card are two embedded tweets from Boris Cherry (@bcherry) discussing Claude Code setup, with the right tweet emphasizing "There is no one correct way to use Claude Code" and noting that different setups work differently for different people.)

## CONCEPTS

**Note:** Custom slash commands have been merged into skills. Files in `.claude/commands/` still work, but skills (`.claude/skills/`) are recommended as they support additional features like supporting files, invocation control, and subagent execution.

- **Skills** - Reusable knowledge, workflows, and slash commands that Claude can load on-demand or you invoke with `/skill-name`

- **Subagents** - Isolated execution contexts that run their own loops and return summarized results

- **Memory** - Persistent context via CLAUDE.md files and `@path` imports that Claude sees every session

- **Rules** - Modular topic-specific instructions in `.claude/rules/x.md` with optional path-scoping via frontmatter

- **Hooks** - Deterministic scripts that run outside the agentic loop on specific events

- **MCP Servers** - Model Context Protocol connections to external tools, databases, and APIs

- **Plugins** - Distributable packages that bundle skills, subagents, hooks, and MCP servers

- **Marketplaces** - Host and discover plugin collections

- **Settings** - Hierarchical configuration system for Claude Code behavior

- **Permissions** - Fine-grained access control for tools and operations

---

## Follow-up Post

**Repo:** [github.com/shanraisshan/claude-code-best-practice](https://t.co/jJraK58Kko)

Follow [@dr_cintas](https://x.com/dr_cintas) for more AI content.

And if you want more practical AI gems and use cases, join my free newsletter with daily tutorials and latest news in AI: [simplifyingai.co](https://t.co/khyHDesFCf)

(Description: Another preview of the "claude-code-best-practice" repository showing the same GitHub card with 1k stars badge and the brown pixelated mascot icon)