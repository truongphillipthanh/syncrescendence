# I want to learn how to use Claude CoWork.
(Description: Illustration showing a person seated at a desk with a laptop, surrounded by workflow icons including calendar, spreadsheet, documents, email, gear/settings, magnifying glass, email envelope, chart, and a prominent "Claude CoWork" badge in the upper right corner. Multiple red arrows point outward from the central figure, symbolizing distributed task automation and multi-directional workflow execution.)
## Overview
There's two types of AI users.
**Type A:** Use AI as their google search.
**Type B:** Use AI as an agentic workforce.
The same AI. Completely different life and outcomes.
You just need to know how to use Claude CoWork with sonnet + opus, you don't need OpenClaw, you don't need a expensive set up, you don't need to waste tokens, you just need to know this:
---
## What the f*ck is CoWork?
**Standard Claude** gives you advice.
**CoWork** executes the task.
### Here's the difference in practice:
**Standard Claude:** "Here's how you'd organise those invoices."
**CoWork:** "I've sorted your invoices by date, pulled vendor names and amounts into a spreadsheet, and flagged three duplicates. Want me to delete them?"
That's not a chatbot. That's a desktop agent.
It runs on Claude Opus 4.6, with a 1-million-token context window - large enough to process entire projects in a single pass. File access, browser control, and app integrations all in one interface.
---
## Before you start:
No workarounds on these if you want to use Claude CoWork (no, I'm not being paid to write this for these billion dollar nerds, I'm just excited to use tech that legit changes my day-to-day life)...
**Subscription:** Claude Pro ($20/mo), Team, or Enterprise (go pro and see if you really need a more expensive version in the future).
**Platform:** macOS (available Jan 2026) or Windows x64 (available since Feb 10, 2026, lfg you window bros).
**App:** Claude Desktop only. The browser version of Claude does not run CoWork.
---
## Setup: 10 mins
1. Go to claude dot com/download. Install the Desktop App.
2. Open it. Three tabs at the top: Chat, CoWork, Code. Click CoWork.
3. For web access, install **Claude in Chrome** from the Chrome Web Store. Without it, Claude is blind to anything browser-based. With it, it becomes a full web agent.
Sixty seconds of installation unlocks every web automation in this guide.
---
## Level 1: File management (start here)
CoWork runs in a virtual machine. Claude cannot access files outside the folder you explicitly unlock.
Click the Folder icon. Select a folder. That's the boundary.
### Three tasks that prove the concept immediately:
- **The Cleanup** - "Organise my Downloads folder. Group files by type: Images, PDFs, Installers. Create named folders." A 200-file folder that takes 45 minutes manually runs in under four.
- **The Renamer** - "Rename every screenshot in this folder based on what's in the image." Claude reads each image before naming it. No guessing.
- **The Data Analyst** - "Scan this folder of invoices. Build a CSV with Date, Vendor, and Amount for each one." Structured output from a messy folder, no manual entry.
(Description: Dense grid of desktop file and folder icons in various colors (blue, yellow, orange, gray), representing a cluttered desktop with hundreds of mixed file types. The image conveys visual chaos and disorganization.)
I hope your desktop doesn't look like this lmfao.
Built-in deletion protection means Claude asks for confirmation before removing anything. No silent wipeouts.
---
## Level 2: Web agent
Install the Chrome extension and CoWork gains web access.
It opens a dedicated browser instantly which is visually distinct from your normal tabs and operates it like a human. Scrolls, clicks, reads, reports back.
### Three use cases worth running today:
- **Deep Research** - "Go to X and Y. Pull the top 3 AI agent stories. Summarise into a memo." Two hours of tab-switching, done in one prompt.
- **Competitor Intel** - "Go to [URL]. Screenshot their pricing page. Summarise their feature set into a comparison table."
- **Sentiment Analysis** - "Find the latest video on this YouTube channel. Read the comments. Give me the overall sentiment."
For sites you use daily - Gmail, your CRM - choose "allow always." Removes the permission prompt every time.
---
## Level 3: Connectors
CoWork talks to external apps through MCP (Model Context Protocol). Think of it as a live bridge between Claude and your data.
**One-click connections via Settings > Connectors:** Google Drive, Gmail, Google Calendar.
### Here's what that makes possible in a single prompt:
> "Check my calendar for my next free slot. Pull my last email from John to see what we needed to discuss. Draft a meeting invite."
One prompt. Three apps. Zero tab-switching.
(Description: Interface mockup showing a settings panel with toggles for "CoinGecko," "Claude in Chrome," and "office-addin," all enabled. Additional options include "Connectors," "Add plugins," "Tool access" dropdown menu. Below are task suggestions: "Let's knock something off your list," "Optimize my week," "Organize my screenshots," and "Find insights in files.")
For tools not listed like Notion, Slack, Salesforce search "[App Name] MCP server." Advanced users edit a config.json file in Desktop settings. Non-technical users should look for Community Skills that package these connections automatically.
---
## Level 4: Skills
A Skill is a saved, repeatable workflow.
You stop prompting from scratch every time. You teach Claude a process once, and it executes on command.
### Using existing Skills:
Go to Settings > Capabilities > Add Skill. Upload a .zip from sites like **smithy.ai**. Done. Skills like "SEO Blog Writer" or "Resume Tailor" are ready to run immediately.
### Building your own:
Run the task manually once. Refine until the output is exactly right. Then ask:
> "Create a Skill from this session so I can repeat it later."
Claude generates a skill file. Save it. Next time: "Run the [Name] Skill on this file."
You can build a skill for your weekly content workflow: transcript in, X post and newsletter intro out. Runs in 90 seconds every Monday.
(Description: Interaction modal showing the text "Yo bitch, create a skill from this session so I can repeat it later. (the yo bitch bit is a joke, don't actually use this bc when AGI comes you're soooooo fucked)" with controls: dropdown menu "Work in a folder," plus icon, "Haiku 4.5" selector, and "Let's go" button with arrow.)
---
## Level 5: Expert tekkerz (tactics for my USA bros)
### Parallel Processing
Open multiple CoWork tabs. Assign research in Tab 1, file sorting in Tab 2, email drafting in Tab 3.
You manage. It executes. All simultaneously.
### Plan Mode
For complex tasks, ask Claude to write a plan first. Review it. Then say "Proceed."
This protects your usage quota and catches errors before they compound.
### Self-Verification
Add to any prompt: *"After you finish, verify the output and flag anything missed."*
Forces a second pass. Catches mistakes before you see them.
### Project Integration
Pull your Claude Projects, brand voice docs, style guides, business context, directly into CoWork. Click + > Include Project.
CoWork now executes tasks using your specific knowledge base, not generic assumptions.
---
## What co-work can't do yet:
**No cross-session memory.** Start a new window and it doesn't remember the last one. Save context into a file or a Skill if you need continuity.
**Requires the Desktop App to stay open.** Close it, the task stops.
**Quota burns faster than regular chat.** CoWork thinks in multiple steps. Heavy users should consider the Max tiers (5x or 20x capacity).
**It can still make mistakes.** Misclicks in browsers happen. Misread files happen. Always review the output.
---
## What should you try today?
- Install Claude Desktop and the Claude in Chrome extension
- Create a folder called Claude_Playground with a mix of dummy files
- Ask CoWork to rename and organise those files
- Connect Gmail and Google Calendar via Settings > Connectors
- Build one Skill for a task you repeat weekly and hate doing
That's the foundation. Everything else is just adding tools to a system that already works.
---
## Here's what matters most:
1. **CoWork acts - it doesn't advise.** The gap between "Claude told me how" and "Claude did it" is the gap between a tool and a workflow.
2. **Skills are the multiplier.** One hour building a Skill saves that hour every single week it runs.
3. **Start with files, then browser, then connectors.** Each level compounds the one before it.
The next move is simple: create your Claude_Playground folder and give CoWork its first real task today. Go play init.
---
## Community Question
Which level are you starting with, file management, browser automation, or connectors? Drop a comment.
Genuinely curious where people are finding the most leverage.
---
## Closing Note
**PSSSSST...** The users treating CoWork as a chatbot and the users running it as an agent are both paying the same $20. The difference is entirely in what they know. Now you know.
---
**Engagement:** 20 replies, 91 reposts, 1K likes, 2.6K bookmarks, 142K views
**Posted:** 7:23 AM · Feb 18, 2026