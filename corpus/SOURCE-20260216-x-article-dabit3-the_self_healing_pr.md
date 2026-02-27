# The Self-Healing PR
(Description: A split-panel illustration showing chaotic scribbled lines on the left side in gray, transitioning to a clean light background on the right. In the center, a red toggle switch labeled "ON" is positioned horizontally with a red circular indicator, suggesting activation or engagement. Below reads "AUTOFIX ENGAGED" in monospace text.)
## Overview
Agents generate PRs faster than teams can review them. Bots catch a lot of the issues - linters, CI, security scanners, review tools.
A human then has to go fix it. Or copy the feedback into a coding agent, wait for the update, check the next review pass and whether it resolved the issue. The review bot already knows what's wrong. The coding agent already knows how to fix things. We were the middleman.
We automated that.
## Autofix
At @cognition, we now autofix incoming review comments with @DevinAI. When a bot comments on a PR, Devin reads the comment and pushes a fix to the same PR.
Devin writes the code → a review bot comments → Devin reads the comment → Devin pushes a fix → CI runs again → if something else is flagged, the loop continues.
This works with any bot that leaves comments on GitHub PRs. Our linter, test runner, security scanner, SonarQube, Codacy, Devin Review. If it posts a comment, Devin can respond to it.
## Loops
The obvious concern: Devin fixes something, the review bot comments again, Devin fixes that, forever.
By default, Devin ignores all bot comments. We opt in to specific bots by adding them to an allowlist.
Lint failure comments are always processed regardless of settings - CI failures are the most common mechanical fix and the least likely to loop.
## What humans review now
A PR that's already been through multiple automated passes. The lint errors, null checks, type mismatches, and CI failures are handled. What's left is logic, architecture, and whether the change should exist at all.
## Closing the loop
A coding agent alone writes code. A review agent alone finds bugs.
Connect them and each pass makes the PR better without anyone manually shuttling context between tools.
The loop runs until the PR is clean. Then a human reviews what's left.
Each piece existed before. The new part is that they talk to each other.
This is available as part of the @DevinAI platform. Try it on your next PR.
---
**Published:** 5:24 PM · February 15, 2026  
**Engagement:** 18 replies, 26 reposts, 319 likes, 523 bookmarks, 95.7K views