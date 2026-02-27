---
id: SOURCE-20260125-x-thread-garrytan-i_dont_know_why_this_isnt_just_in_claude
platform: x
format: thread
creator: garrytan
title: i dont know why this isnt just in claude
status: triaged
original_filename: "20260125-x_thread-i_dont_know_why_this_isnt_just_in_claude-@garrytan.md"
url: https://x.com/garrytan/status/2015540619855425959
author: "Garry Tan (@garrytan)"
captured_date: 2026-01-25
signal_tier: tactical
topics: ""
teleology: implement
notebooklm_category: claude-code
aliases: ""
synopsis: ""
key_insights: ""
---
# CLAUDE.md Instructions for Bash Behavior Thread

I don't know why this isn't just in Claude Code's system prompt

(Description: Screenshot showing a CLAUDE.md instructions card with the following content:)
```
CLAUDE.md Instructions for Bash Behavior

Add the following to your project's CLAUDE.md file:

text

# Bash Guidelines

## IMPORTANT: Avoid commands that cause output buffering issues
- DO NOT pipe output through `head`, `tail`, `less`, or `more` when monitoring or checking command output
- DO NOT use `| head -n X` or `| tail -n X` to truncate output - these cause buffering problems
- Instead, let commands complete fully, or use `--max-lines` flags if the command supports them
- For log monitoring, prefer reading files directly rather than piping through filters

## When checking command output:
- Run commands directly without pipes when possible
- If you need to limit output, use command-specific flags (e.g., `git log -n 10` instead of `git log | head -10`)
- Avoid chained pipes that can cause output to buffer indefinitely
```