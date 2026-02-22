---
id: SOURCE-20260127-x-thread-bcherny-in_case_its_not_clear
platform: x
format: thread
creator: bcherny
title: in case its not clear
status: triaged
original_filename: "20260127-x_thread-in_case_its_not_clear-@bcherny.md"
url: https://x.com/bcherny/status/2016339448863355206
author: "Boris Cherny (@bcherny)"
captured_date: 2026-02-04
signal_tier: tactical
topics:
  - claude-code
  - developer-tools
  - best-practices
teleology: extract
notebooklm_category: claude-code
aliases:
  - "Boris Cherny - CLAUDE.md loading behavior"
synopsis: "Boris Cherny (creator of Claude Code) clarifies CLAUDE.md file loading behavior: ancestor files load automatically at startup while descendant files load lazily only when Claude reads/writes files in that folder. Designed for monorepos. Also shows how to disable CLAUDE.md loading with CLAUDE_CODE_DISABLE_CLAUDE_MDS=1."
key_insights:
  - "Ancestor CLAUDE.md files load into context automatically on startup; descendant CLAUDE.md files load lazily only when Claude accesses files in their directory — effectively acting as specialized skills."
  - "This lazy loading design was intentional for monorepos and large repos to avoid context bloat."
  - "CLAUDE_CODE_DISABLE_CLAUDE_MDS=1 environment variable disables all CLAUDE.md loading entirely."
---
# Claude Code: CLAUDE.md Loading Behavior

**@bcherny · Jan 27, 2026**

In case it's not clear in the docs:

- **Ancestor** `CLAUDE.md`'s are loaded into context automatically on startup
- **Descendent** `CLAUDE.md`'s are loaded *lazily* only when Claude reads/writes files in a folder the `CLAUDE.md` is in. Think of it as a special kind of skill.

We designed it this way for monorepos and other big repos, tends to work pretty well in practice.

---

**@bcherny · Jan 27, 2026**
```
CLAUDE_CODE_DISABLE_CLAUDE_MDS=1 claude
```