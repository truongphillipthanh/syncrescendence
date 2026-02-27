---
url: https://x.com/nicopreme/status/2023495040258261460
author: "Nico Bailon (@nicopreme)"
captured_date: 2026-02-20
id: SOURCE-20260216-025
original_filename: "20260216-x_thread-created_an_agent_skill_called-@nicopreme.md"
status: triaged
platform: x
format: thread
creator: nicopreme
signal_tier: tactical
topics: [claude-code, developer-tools, ai-agents]
teleology: reference
notebooklm_category: claude-code
aliases: ["nicopreme - Visual Explainer agent skill"]
synopsis: "An agent skill called Visual Explainer that renders complex explanations as rich HTML pages instead of terminal text. Includes reference templates, CSS pattern library, and slash commands. Reduces cognitive debt by making agent output visually digestible with code reviews, architecture diagrams, and state flows."
key_insights:
  - "Terminal text walls create cognitive debt - rich HTML output with consistent CSS makes complex explanations digestible"
  - "Skill includes reference templates and CSS pattern library so output stays consistently well-designed"
  - "Complements code review workflows: findings rendered as structured visual documents with file references"
---
# Visual Explainer Agent Skill
Created an agent skill called **"Visual Explainer"** + set of complementary slash commands aimed to reduce my cognitive debt so the agent can explain complex things as rich HTML pages. The skill includes reference templates and a CSS pattern library so output stays consistently well-designed. Much easier for me to digest than squinting at walls of terminal text.
[github.com/nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer)
---
## Embedded Code Review Document
(Description: A comprehensive code review document displayed in a terminal-style interface with syntax highlighting, showing multiple findings and recommendations. The document contains several sections organized by topic:)
### Content Overview
**CONTENTS**
1. Summary
2. KPIs
3. Architecture
4. Before / After
5. State Flow
6. File Map
7. Code Review
8. Decisions
9. Re-entry
### Code Review Findings
**Rather than swapping abort handlers at each phase transition** (which had real scoping bugs in earlier plan drafts), a single `closeCurator()` listener registered once handles all phases. The search loop checks `cancelled`, curate-window timers are cleared by `krisen`, and the server is closed by `closeCurator()`. Each phase reuses existing cleanup mechanisms without requiring dedicated short logic.
```
index.ts:586-588
```
---
**stale-cancel guard in openCuratorBrowser**
After `await startCuratorServer()`, the code checks `pendingCurate == ps` before assigning `activeCurator`. If something cancelled the pending curate during the await (session close, new curate search), the server handle is closed immediately instead of leaked. This was identified as a bug during plan review (round 3) and correctly implemented.
```
index.ts:416-419
```
---
**resolveProvider extraction removes real duplication**
The provider fallback logic (auto → perplexity → gemini → fallback) was previously inlined in three places. Now `resolveProvider(requested, available)` is a single function called by the curate path and `/websearch` command. The non-curate path still uses provider strings (see Ugly section), but the duplication is reduced from three to one.
```
index.ts:61-78
```
---
**None found**
No bugs, regressions, or logic errors identified. All edge cases traced (signal-already-aborted, mid-await cancellation, timer/Ctrl+S race, double-cancel idempotency, server handle leak paths). Each resolves correctly through the `cancelled` flag and `closeCurator()` convergence.
---
**index.ts at 1,377 lines is getting heavy**
The file registers 2 shortcuts, 3 tools, 2 commands, and 5 event handlers. `buildSearchReturn`, `openCuratorBrowser`, `filterByQueryIndices`, and the entire curate execute path live inside the `export default` closure because they need `ps`, `activeCurator`, and each other. This coupling makes abstraction hard. The file doesn't need splitting today, but future features should land in adjacent modules where possible.
```
index.ts:1-1377
```
---
**No tests for any of the curate machinery**
The curate lifecycle (PendingCurate state machine, timer interaction, Ctrl+S phases, openCuratorBrowser stale-cancel guard, finish/cancel idempotency) is entirely untested. The plan review caught 14 issues across 5 rounds, several of which were bugs that would have been caught in day one testing. This coupling makes extraction hard; the File doesn't need splitting today, but future features should land in adjacent modules where possible.