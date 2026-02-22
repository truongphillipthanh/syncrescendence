---
id: SOURCE-20260131-x-thread-bcherny-im_boris_and_i_created_claude
platform: x
format: thread
creator: bcherny
title: im boris and i created claude
status: triaged
original_filename: "20260131-x_thread-im_boris_and_i_created_claude-@bcherny.md"
url: https://x.com/bcherny/status/2017742741636321619
author: "Boris Cherny (@bcherny)"
captured_date: 2026-01-31
signal_tier: paradigm
topics:
  - claude-code
  - developer-tools
  - best-practices
teleology: extract
notebooklm_category: claude-code
aliases:
  - "Boris Cherny - Claude Code tips from the team"
synopsis: "Claude Code creator Boris Cherny shares tips sourced directly from the Claude Code team at Anthropic. Top tip: spin up 3-5 git worktrees running parallel Claude sessions — the single biggest productivity unlock. Emphasizes there's no one right way to use Claude Code."
key_insights:
  - "Running 3-5 parallel Claude Code sessions in git worktrees is the single biggest productivity unlock, and the top tip from the Claude Code team at Anthropic."
  - "The Claude Code team itself uses multiple approaches (git checkouts vs worktrees) — there is no single 'correct' workflow."
  - "These are insider tips from the team that built and uses Claude Code daily, making them higher-signal than community advice."
---
# Claude Code Tips & Tricks - From the Team

I'm Boris and I created Claude Code. I wanted to quickly share a few tips for using Claude Code, sourced directly from the Claude Code team. The way the team uses Claude is different than how I use it. Remember: there is no one right way to use Claude Code -- everyones' setup is different. You should experiment to see what works for you!

---

## 1. Do more in parallel

Spin up 3–5 git worktrees at once, each running its own Claude session in parallel. It's the single biggest productivity unlock, and the top tip from the team. Personally, I use multiple git checkouts, but most of the Claude Code team prefers worktrees --

(Description: Code snippet showing git commands:
```bash
$ git worktree add .claude/worktrees/my-worktree origin/main

$ cd .claude/worktrees/my-worktree 5G claude
```

Claude Code v2.1.29 - Opus 4.5 • Claude Enterprise - /.claude/worktrees/my-worktree)

---

## 2. Start every complex task in plan mode

Pour your energy into the plan so Claude can 1-shot the implementation.

(Description: Screenshot showing Claude Code interface with a plan mode visible with command syntax and interface elements)

---

## 3. Invest in your CLAUDE.md

After every correction, end with: "Update your CLAUDE.md so you don't make that mistake again." Claude is eerily good at writing rules for itself. Ruthlessly edit your CLAUDE.md over time. Keep iterating

(Description: Code box showing CLAUDE.md memory file structure:
```
Memory files · /memory
├ ~/.claude/CLAUDE.md: 76 tokens
└ CLAUDE.md: 4k tokens
```
)

---

## 4. Create your own skills and commit them to git. Reuse across every project.

Tips from the team:
- If you do something more than once a day, turn it into a skill or command
- Build a /techdebt slash command and run it at the end of every session to find and kill duplicated code

(Reference: Extend Claude with skills - Claude Code Docs - code.claude.com)

---

## 5. Claude fixes most bugs by itself. Here's how we do it:

Enable the Slack MCP, then paste a Slack bug thread into Claude and just say "fix". Zero context switching required.

Or, just say "Go fix the failing CI tests". Don't micromanage how.

Point Claude at docker logs to

(Description: Terminal output showing Claude Code interface with Slack MCP search tool:
```
slack - search_public (MCP)(query: "in:C07VBSH...")

Tool use
slack - search_public(query: "in:C07VBSH...")
Searches for messages in public Slack channels

'slack_search_public' does NOT generally require user consent to use 'slack_search_private' unless the task requires DMs, or group messages...
```
)

---

## 6. Level up your prompting

a. Challenge Claude. Say "Grill me on these changes and don't make a PR until I pass your test". Make Claude be your reviewer. Or, say "Prove to me this works" and have Claude diff behavior between main and your feature branch

b. After a mediocre

(Description: Extended prompt example showing interaction mode with feedback loops)

---

## 7. Terminal & Environment Setup

The team loves Ghostty! Multiple people like its synchronized rendering, 24-bit color, and proper unicode support.

For easier Claude-juggling, use /statusline to customize your status bar to always show context usage and current git branch. Many of us also color-code and name our terminal tabs, sometimes using tmux — one tab per task/worktree.

Use voice dictation. You speak 3x faster than you type, and your prompts get way more detailed as a result. (hit fn x2 on macOS)

More tips: https://code.claude.com/docs/en/terminal-config…

(Description: Terminal interface screenshot showing Claude Code editor with status line displaying context usage and git branch information - window showing "edit REPL.tsx to..." prompt and shortcuts)

---

## 8. Use subagents

a. Append "use subagents" to any request where you want Claude to throw more compute at the problem

b. Offload individual tasks to subagents to keep your main agent's context window clean and focused

c. Route permission requests to Opus 4.5 via a hook — let it

(Description: Extended code example showing subagent usage pattern:
```
use 5 subagents to explore the codebase

- I'll launch 5 explore agents in parallel to
- Running 5 Explore agents... (ctrl+o to expand
  - Explore entry points and startup · 10
    └ Bash: Find CLI or main entry files
  - Explore React components structure · 12
    └ Bash: ls -la /Users/boris/code/claude
  - Explore tools implementation · 14 tools
    └ Bash: Find tool implementation files
  - Explore state management · 13 tool uses
    └ Search: **/screens/REPL.tsx
  - Explore testing infrastructure · 13 tools
    └ Search: test/mocks/*/*.ts
ctrl+b to run in background
```
)

---

## 9. Use Claude for data & analytics

Ask Claude Code to use the "bq" CLI to pull and analyze metrics on the fly. We have a BigQuery skill checked into the codebase, and everyone on the team uses it for analytics queries directly in Claude Code. Personally, I haven't written a line of SQL in 6+ months.

This works for any database that has a CLI, MCP, or API.

(End with expanded content about analytics capabilities and CLI tools)

---

## 10. Learning with Claude

A few tips from the team to use Claude Code for learning:

a. Enable the "Explanatory" or "Learning" output style in /config to have Claude explain the "why" behind its changes

b. Have Claude generate a visual HTML presentation explaining unfamiliar code. It makes surprisingly good slides!

c. Ask Claude to draw ASCII diagrams of new protocols and codebases to help you understand them

d. Build a spaced-repetition learning skill: you explain your understanding, Claude asks follow-ups to fill gaps, stores the result

---

## 11. Hope these tips are helpful! What do you want to hear about next?

---

**Engagement Metrics:**
- Replies: 850
- Reposts: 6.2K
- Likes: 49K
- Bookmarks: 100K
- Views: 8.1M