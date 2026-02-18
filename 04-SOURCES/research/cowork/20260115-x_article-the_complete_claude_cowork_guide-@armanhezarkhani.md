---
url: https://x.com/armanhezarkhani/status/2011818455922553106/
author: Arman Hezarkhani (@ArmanHezarkhani)
captured_date: 2026-01-15
---

# The Complete Claude Cowork Guide

(Description: Cover image with coral/orange rounded square icon containing a white lightning bolt symbol, paired with serif typography reading "The Complete Claude Cowork Guide" and subtitle "Cowork: Claude Code for the rest of your work")

At Tenex, we've been using Claude Code since its release—for coding and non-coding tasks alike. But we always found it hard to get our clients onboarded. The terminal scares people. The name scares people. Claude Cowork might be the answer to that problem.

Here's a beginner's playbook containing everything I've learned after putting Cowork through its paces on real knowledge work.

## What Is Cowork?

Cowork is Claude Code for the rest of your work. Same powerful agent architecture, wrapped in an interface that doesn't require you to touch a terminal.

You give Claude access to a folder on your computer. Claude can then read, edit, and create files in that folder—organizing downloads, building spreadsheets from receipts, drafting reports from scattered notes, and more. It plans, executes, and loops you in along the way.

Anthropic built the entire thing in about ten days. Using Claude Code.

Claude Max subscribers ($100 or $200/month) can use it now in the macOS Desktop app. Everyone else can join the waitlist. Windows support is coming.

To get started, download the Claude Desktop app, click "Cowork" in the sidebar, and grant access to a folder.

## The Mental Shift

The biggest mistake people make with Cowork is treating it like ChatGPT with folder access. Ask a question, get an answer, copy-paste the output manually into a document.

That's not what this is.

Cowork is a worker. You describe an outcome and step away. It plans, executes, organizes files, creates spreadsheets with real formulas, drafts reports, and synthesizes research—all while you do something else.

As Anthropic puts it: "It feels much less like a back-and-forth and much more like leaving messages for a coworker."

If you keep treating it like a chat interface, you'll get 10% of the value.

## Write Better Prompts

The quality of your output is directly proportional to the quality of your input. The people who get terrible results are the ones who type "organize my files" and expect magic.

Before you delegate anything, answer these questions in your prompt:

### What does "done" look like?

If you can't picture the finished state, neither can Claude. "Create an expense report" is vague. "Create an Excel spreadsheet with columns for date, vendor, amount, and category, sorted by date, with a sum total at the bottom" is actionable.

### What context does Claude need?

Does it know your naming conventions? Your folder structure preferences? The difference between work and personal documents? Tell it.

### What constraints matter?

"Don't delete any files, just move them." "Keep the original filenames but add a date prefix." "Only process files from the last 90 days." Claude can't read your mind about limits you haven't stated.

### Prompt Templates You Can Steal

**For file organization:**
Organize all files in this folder. Group them into subfolders by [project/client/file type]. Rename each file using the format YYYY-MM-DD-descriptive-name. Do not delete anything. Create a summary document listing what you moved and where.

**For research synthesis:**
Read all the documents in this folder. Create a single report that synthesizes the key findings. Include direct quotes where relevant, with the source file name. Flag any contradictions between sources. End with a list of questions that remain unanswered.

**For document creation:**
Create a [PowerPoint/Word doc/Excel spreadsheet] based on the files in this folder. Use [specific structure or template description]. The audience is [who]. The goal is [what you want them to understand or do after reading].

**For data extraction:**
I have [X] screenshots of [receipts/invoices/forms] in this folder. Extract the data into an Excel spreadsheet with columns for [list columns]. Sort by [column]. Add a total row at the bottom. Flag any images that were unclear or couldn't be processed.

## Folder Access Strategy

In Cowork, you designate specific folders Claude can access. This is where the power comes from—and where the responsibility lands on you.

### Start with a dedicated work folder.

Don't point Claude at your entire Documents folder on day one. Create a "Claude-Work" folder, move the files you want processed into it, and give Claude access to that.

### Keep backups of anything important.

Claude can take destructive actions like deleting files. While Claude only deletes if instructed, there's always a chance of misinterpretation. If a file matters, back it up first.

### Be explicit about deletions.

If you want Claude to delete duplicates, say "delete duplicates." If you don't want anything deleted, say "do not delete any files under any circumstances—only move or rename them."

### Folder Setup I Recommend
```
Claude-Work/
├── inbox/           ← Drop files here for Claude to process
├── processed/       ← Claude moves finished work here
├── outputs/         ← Claude creates new files here
└── reference/       ← Files Claude should read but not modify
```

Tell Claude about this structure in your first prompt: "The inbox folder contains files to process. Move them to processed when done. Create any new files in outputs. The reference folder is read-only—don't modify those files."

## Sub-Agents for Complex Work

When a task has independent parts, Claude can spin up multiple workers to tackle them simultaneously and synthesize the results. This is massive for research and analysis—instead of working sequentially, it parallelizes.

You don't have to explicitly request sub-agents. Claude spins them up when appropriate. But knowing the capability exists helps you frame requests that benefit from it.

### When to Explicitly Request Sub-Agents

**Vendor or competitor analysis:**
"Spin up sub-agents to research each of these four vendors independently. For each one, find pricing, customer reviews, and integration capabilities. Then synthesize into a comparison."

**Multi-perspective analysis:**
"Analyze this decision using three sub-agents: one focused on financial impact, one on customer experience, one on operational risk. Synthesize their findings into a recommendation."

**Large document sets:**
"I have 50 customer interview transcripts. Use sub-agents to process them in parallel. Extract key themes, notable quotes, and feature requests. Synthesize into a single insights report."

## Skills Turn Claude Into a File Creator

Skills are specialized instruction sets that Claude loads for particular types of work. Cowork comes bundled with skills for creating professional documents—Excel spreadsheets, PowerPoint presentations, Word documents, PDFs.

This matters because Cowork produces actual files, not just text you have to copy somewhere.

When you ask Claude to create an expense spreadsheet, you get an Excel file with working formulas, proper formatting, and multiple tabs if needed. Not a CSV that requires cleanup. Not markdown you have to paste into Excel. A real .xlsx file.

### What Each Skill Does Well

**Excel (.xlsx):**
Financial models, data analysis, trackers, dashboards with formulas. Claude handles SUM, VLOOKUP, conditional formatting, multiple sheets, and charts.

**PowerPoint (.pptx):**
Presentations from raw notes, meeting summaries turned into decks, pitch materials. Claude creates real slides with layouts, not bullet points for you to format.

**Word (.docx):**
Reports, proposals, documentation. Proper headings, tables of contents, formatted tables.

**PDF:**
Form filling, document assembly, standardized outputs.

### Creating Custom Skills

If you have specific workflows—a particular report format, a standard template, a brand style guide—you can package those instructions as a skill. Claude loads them automatically when relevant.

To create a custom skill, put a markdown file in your work folder that describes:
- The format and structure you want
- Specific language or terminology to use
- Examples of good output
- Common mistakes to avoid

Then tell Claude: "Read the style-guide.md file in this folder and follow it for all documents you create."

## Connectors Pull From Your Tools

Cowork integrates with Anthropic's existing connectors—tools that link Claude to external services like Google Drive, Slack, Asana, Notion, SharePoint, Teams, Zendesk, Canva, and more.

If you're constantly copying information from one system to paste into Claude, there's probably a connector that can do it automatically. Check Settings > Connectors to see what's available.

### High-Value Connector Workflows

**Google Drive + Local Files:**
"Pull the Q4 numbers from our Google Drive finance folder, combine with the notes in my local /q4-planning folder, and create a summary presentation."

**Asana/Notion + Document Creation:**
"Check our Asana project for all open tasks, then create a status report document grouped by assignee with due dates highlighted."

**Slack + Research:**
"Search our #product-feedback Slack channel for messages mentioning 'onboarding' from the last 30 days. Summarize the feedback themes and create a recommendations doc."

## Browser Access With Chrome

If you enable the Claude in Chrome extension, Cowork gains browser access. Claude can complete tasks that require navigating websites—web research, form filling, data extraction from online sources.

### Browser Workflows That Work Well

**Competitive research:**
"Visit the pricing pages for [list of competitors]. Extract their pricing tiers, features per tier, and any listed customer logos. Create a comparison spreadsheet."

**Public data gathering:**
"Find the latest SEC 10-K filings for these three companies. Extract revenue, operating expenses, and headcount for the last three years. Create a comparison table."

**Content research:**
"Search for the top 10 articles about [topic] published in the last month. Summarize each one's main argument and create a research brief."

### Browser Safety Precautions

Browser access introduces prompt injection risks. If Claude navigates to a malicious site, hidden instructions could try to alter its behavior. Anthropic has defenses, but agent safety is still evolving.

Limit browser access to trusted sites. Don't send Claude to random URLs from unknown sources. If you're researching competitors, stick to their official sites.

## Queue Tasks and Walk Away

Unlike regular Claude chat, you don't have to wait for one response before giving the next instruction. Queue up tasks and let Claude work through them.

Start a task, add another to the queue, step away, come back to finished work.

The sidebar shows progress—what steps are unfolding, what tools are in use, what outputs are being created. Monitor if you want, or check in later.

**Important:** The Claude Desktop app must remain open while tasks are running. If you close the app or your computer goes to sleep, the session ends.

### Batching Strategy

**Instead of:**
- "Organize my receipts" → wait → done
- "Create expense report" → wait → done
- "Summarize for my accountant" → wait → done

**Do this:**
"I have receipt screenshots in /receipts. First, organize them by month into subfolders. Then create an expense spreadsheet with all the data. Finally, create a one-page summary for my accountant showing totals by category and any unusually large expenses. Put all outputs in /outputs."

One session, three tasks, less usage consumed.

## 25 Use Cases That Actually Work

### Financial & Administrative

- Turn 50 receipt photos into a categorized expense spreadsheet with totals
- Extract key dates, amounts, and obligations from a folder of contracts
- Create invoice summaries from scattered PDF invoices
- Build a budget tracker from bank statement exports
- Generate monthly expense reports from raw transaction data

### Research & Analysis

- Synthesize 30 customer interview transcripts into a themes report
- Compare four vendors on pricing, features, and reviews
- Analyze a folder of competitor marketing materials for positioning insights
- Extract and organize highlights from a folder of PDFs you've annotated
- Create a literature review from a folder of research papers

### Content & Documents

- Turn meeting notes into a formatted slide deck
- Create a project brief from scattered planning documents
- Generate a FAQ document from customer support chat logs
- Build a style guide from examples of approved content
- Turn a long report into an executive summary

### File Management

- Organize a chaotic Downloads folder by project and date
- Find and consolidate duplicate files across subfolders
- Rename files in bulk using a consistent naming convention
- Sort photos by date and create organized album folders
- Archive old files while creating an index of what was moved

### Data Processing

- Extract data from screenshots of forms or tables
- Combine multiple CSV files into a single organized spreadsheet
- Clean and standardize messy data exports
- Convert between file formats in bulk
- Extract specific fields from a large set of documents

### Unexpected Uses People Have Found

Anthropic's Boris Cherny shared what users have done with Claude Code (which Cowork inherits): vacation research, building slide decks from scratch, cleaning up email backlogs, cancelling unused subscriptions, recovering wedding photos from a corrupted hard drive, monitoring plant growth with photos, and controlling smart home devices.

The agent is general-purpose. If it can be done with files and web access, try it.

## Usage Management

Cowork consumes significantly more of your allocation than regular chat. Complex, multi-step tasks are compute-intensive.

**Batch related work.** One session with three related tasks beats three separate sessions.

**Use regular chat for simple stuff.** Quick questions don't need Cowork's overhead.

**Check your usage.** Settings > Usage shows where you're spending tokens. Look for patterns—if one type of task burns through allocation fast, find ways to make the prompts more efficient.

## Safety Checklist

Anthropic is very transparent about Cowork's risks. Here's what to actually do about them.

### Before your first session:

- Create a dedicated work folder (don't use Documents or Desktop)
- Back up any important files you'll give Claude access to
- Decide what Claude is NOT allowed to delete

### Every session:

- Be explicit about constraints in your prompt
- Avoid putting sensitive files (credentials, financial docs, personal records) in the work folder
- If using browser access, stick to trusted sites

### If something seems off:

- Stop the task immediately
- Check what files were modified
- Look for signs of prompt injection (Claude doing things you didn't ask for)

## When to Use Cowork vs. Regular Chat

### Use Cowork when:

- The work lives in your files
- You need Claude to create actual documents (Excel, PowerPoint, Word)
- Tasks involve processing lots of files or sources
- You want to queue tasks and walk away
- The work would hit context limits in regular chat

### Use regular chat when:

- You're asking questions or having a discussion
- You don't need file access
- The task is quick and simple
- Usage efficiency matters more than automation

## Current Limitations

Cowork is a research preview. What's not available yet:

- Projects support
- Memory across sessions
- Sharing sessions with others
- Windows (coming soon)
- Cross-device sync

Use the feedback button in the app. Anthropic is actively developing based on what users report.

## Quick Reference

**Access:** Claude Max ($100-200/mo), macOS Desktop app

**Get started:** Download app → Click "Cowork" → Grant folder access

**Best for:** File organization, research synthesis, document creation, multi-step tasks

**Not for:** Quick questions, simple analysis, anything not needing file access

**Key capabilities:** Sub-agents, Skills (xlsx/pptx/docx), Connectors, Chrome browser access

**Safety basics:** Start narrow, backup important files, be explicit about constraints

## TLDR

Cowork is a worker, not a chatbot. Delegate outcomes, step away, come back to finished files.

Write better prompts. Define what "done" looks like, give context, specify constraints.

Start with a dedicated folder. Limit access while learning. Keep backups.

Use sub-agents for complex work. Claude parallelizes automatically.

Skills produce real files. Excel with formulas, PowerPoint presentations, formatted documents.

Connectors extend reach. Google Drive, Slack, Asana, and more.

Browser access adds power and risk. Limit to trusted sites.

Queue tasks and batch related work to save usage.

Safety is your responsibility. Backup files, avoid sensitive data, monitor what Claude does.

The tool is early. Start learning now.