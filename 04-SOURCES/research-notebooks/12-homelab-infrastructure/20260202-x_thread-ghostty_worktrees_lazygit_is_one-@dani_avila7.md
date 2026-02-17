---
url: https://x.com/dani_avila7/status/2018453309808390226
author: Daniel San (@dani_avila7)
captured_date: 2026-02-14
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