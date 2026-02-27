---
url: https://x.com/Letta_AI/status/2022082571988058536
author: "Letta (@Letta_AI)"
captured_date: 2026-02-14
id: SOURCE-20260212-015
original_filename: "20260212-x_thread-introducing_context_repositories_git-tracked_files-@Letta_AI.md"
status: triaged
platform: x
format: thread
creator: letta_ai
signal_tier: tactical
topics:
  - prompting
  - context-management
  - git
  - memory-management
  - codex
  - rag
  - token-management
teleology: reference
notebooklm_category: ai-engineering
aliases:
  - "Introducing Context Repositories"
synopsis: "Introducing Context Repositories **@Letta_AI • Feb 12, 2026 • 2:57 PM** Introducing Context Repositories: git-tracked files for storing agent context Agents can now write scripts and spawn memory subagents to programmatically restructure prior context and learn in token-space."
key_insights:
  - "Note that Claude Code doesn't support progressive memory disclosure (outside of claude\\.md), unlike Letta Code."
  - "--- **@Letta_AI • Feb 12, 2026** --- **@Letta_AI • Feb 12, 2026** (Reply to @bensenescu) Not yet, but we'll turn it on by default soon 👾 ---."
  - "Explores introducing context repositories."
---
# Introducing Context Repositories

**@Letta_AI • Feb 12, 2026 • 2:57 PM**

Introducing Context Repositories: git-tracked files for storing agent context

Agents can now write scripts and spawn memory subagents to programmatically restructure prior context and learn in token-space.

(Description: Technical circuit board diagram schematic with interconnected nodes and pathways, labeled "Introducing Context Repositories: Git-based memory for Coding Agents | Letta")

---

**@Letta_AI • Feb 12, 2026**

We've added built-in skills & subagents leveraging Context Repositories for Letta Code's memory:

- `/init` (learn from old CC/Codex sessions)
- reflection (learn from recent history)
- defragmentation (reorganize and restructure memory over time)

View memories with `/memory`

(Description: Video interface showing "Memo | Letta Code" window with file tree navigation on left side displaying memory structure including system/, prefixes/, communication.md, workflow.md, context.md, identity.md, persona/, behavior.md, role.md, project/, gotchas.md, overview.md, history/, and memory/ folders. Right panel shows "View your agent's memory" with descriptions and Claude Code History Analysis output including source references and session examination data. Status bar shows "... 220 more (enter to view)" with navigation prompt and editor mode indicator. Video timestamp: 0:07)

---

**@Letta_AI • Feb 12, 2026**

To enable Context Repositories in Letta Code, run `/memfs enable`

[GitHub - letta-ai/letta-code: The memory-first coding agent](https://github.com/letta-ai/letta-code)

---

**@Letta_AI • Feb 12, 2026**

If your expect your agent to run forever, it needs memory defragmentation

(Description: Windows "Disk Defragmenter" utility interface showing:
- Volume: C:\\ (currently selected, highlighted in blue)
- CANON_DC (E:), FAT
- Session Status: "Defragmenting..." in progress
- File System: NTFS for C:\\, FAT for CANON_DC
- Capacity: 37.21 GB for C:\\, 15 MB for CANON_DC
- Free Space: 24.09 GB for C:\\, 2 MB for CANON_DC
- % Free Space: 64% for C:\\, 14% for CANON_DC

Two comparative visualizations showing:
- "Estimated disk usage before defragmentation:" - fragmented colored bar pattern (red, blue, purple, green segments)
- "Estimated disk usage after defragmentation:" - optimized colored bar pattern (more consolidated red and blue sections with green free space)

Legend showing: Fragmented files (red), Contiguous files (blue), Unmovable files (green), Free space (white)

Status bar at bottom: "(C:) Defragmenting... 3%. Moving File MathematicsTemp13037.xbl"
With progress indicator)

---

**@Letta_AI • Feb 12, 2026** (Reply to @NoahGreenSnow)

No native integration yet - but you can have a Letta Code agent ingest all your Claude Code history into a context repository (which Claude Code can then read).

Note that Claude Code doesn't support progressive memory disclosure (outside of claude\\.md), unlike Letta Code.

---

**@Letta_AI • Feb 12, 2026**

(Description: Illustration depicting two human head profiles in profile view, rendered in translucent blue with visible brain structures shown in white and red neural network patterns. A glowing red/pink energy beam or connection extends between the two heads from the brain regions, suggesting data transfer or neural communication between minds.)

---

**@Letta_AI • Feb 12, 2026** (Reply to @bensenescu)

Not yet, but we'll turn it on by default soon 👾

---