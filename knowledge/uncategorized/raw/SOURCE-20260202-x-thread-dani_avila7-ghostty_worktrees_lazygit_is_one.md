---
url: https://x.com/dani_avila7/status/2018453309808390226
author: "Daniel San (@dani_avila7)"
captured_date: 2026-02-14
id: SOURCE-20260202-010
original_filename: "20260202-x_thread-ghostty_worktrees_lazygit_is_one-@dani_avila7.md"
status: triaged
platform: x
format: thread
creator: dani_avila7
signal_tier: tactical
topics:
  - developer-tools
  - workflow
  - git
teleology: extract
notebooklm_category: coding-tools
aliases:
  - "Daniel San - Ghostty worktrees lazygit combo"
synopsis: "Brief thread praising the Ghostty + Git Worktrees + Lazygit combination as a developer experience unlock, with Claude Code worktree commands visible in the setup. Teases a forthcoming detailed article on the workflow."
key_insights:
  - "Ghostty + Git Worktrees + Lazygit is emerging as a preferred terminal-native developer workflow for AI-assisted coding with Claude Code."
  - "Git worktrees enable parallel branch work that complements AI agent workflows where multiple tasks run simultaneously."
  - "The DX improvements in Ghostty are specifically tuned for the kind of terminal-heavy workflows that AI coding agents require."
---
# Ghostty + Worktrees + Lazygit Thread

Ghostty + Worktrees + Lazygit is one of those combos you try once, and you're never going back

And somehow, every new feature @mitchellh ships feels perfectly tuned for better DX

I'm preparing an article about this... stay tuned

(Description: Claude Code terminal window showing git worktrees configuration with multiple branches listed, including .cloude/commands directory, worktree-check.md, worktree-cleanup.md, worktree-deliver.md, and worktree-init.md. The left panel shows commit information with timestamps and author details. The right panel displays configuration logs and metadata including feature reorganization notes for footer sections and npm package links. Various commit SHAs are visible (5d05a756, 625902f3, ca3c98bd, 8e28fd10, etc.) with associated features and improvements.)

---

**In reply to Anu — the NPC (@anu_realm) - Feb 2:**

Anu: "Hate worktrees - good for simple front end sites. But running a backend server with database and a frontend server in multiple worktrees... is just too much to handle."

---

True. As soon as the setup gets more complex, you start needing full environments per branch, and worktrees alone don't really solve that.

You can mitigate it with containers or per-worktree bootstrapping, but at that point you're essentially creating isolated instances anyway