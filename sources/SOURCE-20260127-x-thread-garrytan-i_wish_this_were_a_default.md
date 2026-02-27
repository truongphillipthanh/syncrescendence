---
id: SOURCE-20260127-x-thread-garrytan-i_wish_this_were_a_default
platform: x
format: thread
creator: garrytan
title: i wish this were a default
status: triaged
original_filename: "20260127-x_thread-i_wish_this_were_a_default-@garrytan.md"
url: https://x.com/garrytan/status/2016339446975889735
author: "Garry Tan (@garrytan)"
captured_date: 2026-01-27
signal_tier: tactical
topics:
  - claude-code
  - developer-tools
teleology: extract
notebooklm_category: claude-code
aliases:
  - "Garry Tan - Claude Code verbose mode"
synopsis: "Y Combinator's Garry Tan shares how to enable verbose mode in Claude Code to see full bash outputs instead of truncated summaries, plus how to increase the max output length via environment variable."
key_insights:
  - "Run 'claude config set -g verbose true' to globally enable full command output display in Claude Code."
  - "Set BASH_MAX_OUTPUT_LENGTH=50000 environment variable to prevent output truncation."
  - "Claude Code defaults to hiding log details, which frustrates power users who want full visibility into agent operations."
---
# X Thread: Claude Code Verbose Mode Request

I wish this were a default setting. This is Claude Code, not Claude Cowork. I wanna see all the logs, don't hide them from me!

(Description: Screenshot of Claude documentation or terminal interface showing configuration instructions for verbose mode)

---

## Enable Verbose Mode

Run this to see full bash outputs:
```bash
claude config set -g verbose true
```

This globally enables showing complete command output instead of the truncated summaries.

**stackoverflow**

## Increase Output Length

You can also set the environment variable to prevent truncation:
```bash
export BASH_MAX_OUTPUT_LENGTH=50000
```

Or add it to your shell config. **stackoverflow**

---

**Engagement Metrics (Jan 27, 2026, 6:36 PM)**
- Views: 61K
- Replies: 55
- Reposts: 8
- Likes: 322
- Bookmarks: 180