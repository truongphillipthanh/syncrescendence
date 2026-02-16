# PRAC: Cowork Desktop Integration

**Scope**: Folder permissions, skill loading, VM architecture, non-developer bridge

---

## What Is Cowork

Claude Code for non-developers. Same powerful agent architecture, GUI interface. No terminal required.

**Access**: Claude Max ($100-200/mo), macOS Desktop app, Windows coming.

**Core shift**: Don't treat as ChatGPT with folder access. Cowork is a worker. Describe outcome, step away, come back to finished files.

---

## Folder Access Strategy

### Start Narrow

```
Claude-Work/
├── inbox/           ← Drop files here for Claude to process
├── processed/       ← Claude moves finished work here
├── outputs/         ← Claude creates new files here
└── reference/       ← Files Claude should read but not modify
```

Tell Claude this structure in first prompt:
```
The inbox folder contains files to process. Move them to processed
when done. Create any new files in outputs. The reference folder
is read-only—don't modify those files.
```

### Don't Point at Entire Documents

- Create dedicated work folder
- Move files you want processed into it
- Keep backups of anything important
- Be explicit about deletions

---

## Prompting for Cowork

### Define "Done"

**Vague**: "Create an expense report"
**Actionable**: "Create an Excel spreadsheet with columns for date, vendor, amount, and category, sorted by date, with a sum total at the bottom"

### Include Constraints

- "Don't delete any files, just move them"
- "Keep original filenames but add date prefix"
- "Only process files from the last 90 days"

### Specify Context

- Does Claude know your naming conventions?
- Your folder structure preferences?
- The difference between work and personal?

---

## Built-in Skills

Cowork produces actual files, not text to copy:

| Skill | Output | Capabilities |
|-------|--------|--------------|
| **Excel** | .xlsx | Formulas, formatting, multiple sheets, charts |
| **PowerPoint** | .pptx | Real slides with layouts |
| **Word** | .docx | Headings, TOC, tables |
| **PDF** | .pdf | Form filling, assembly |

---

## Custom Skills

Package specific workflows as skill files:

```markdown
# style-guide.md

## Report Format
- Use Calibri 11pt for body
- Headers in bold
- Tables with alternating row colors
- Executive summary first page

## Terminology
- Use "customers" not "clients"
- Use "platform" not "system"
```

Then prompt: "Read the style-guide.md file and follow it for all documents you create."

---

## Sub-Agent Patterns

Cowork inherits Claude Code's sub-agent capability:

```
Spin up sub-agents to research each of these four vendors
independently. For each one, find pricing, customer reviews,
and integration capabilities. Then synthesize into a comparison.
```

For large document sets:
```
I have 50 customer interview transcripts. Use sub-agents to
process them in parallel. Extract key themes, notable quotes,
and feature requests. Synthesize into a single insights report.
```

---

## Connectors

Cowork integrates with external services:
- Google Drive
- Slack
- Asana
- Notion
- SharePoint
- Teams
- Zendesk
- Canva

**Example workflow**:
```
Pull the Q4 numbers from our Google Drive finance folder,
combine with the notes in my local /q4-planning folder,
and create a summary presentation.
```

---

## Browser Access (Chrome Extension)

With Claude in Chrome enabled:

```
Visit the pricing pages for [competitors]. Extract their
pricing tiers, features per tier, and any listed customer
logos. Create a comparison spreadsheet.
```

**Safety**: Limit to trusted sites. Prompt injection risks exist.

---

## Task Queuing

Unlike regular chat, queue multiple tasks:

```
I have receipt screenshots in /receipts. First, organize them
by month into subfolders. Then create an expense spreadsheet
with all the data. Finally, create a one-page summary for my
accountant showing totals by category. Put all outputs in /outputs.
```

One session, three tasks, less usage consumed.

**Note**: Desktop app must remain open while tasks run.

---

## Usage Management

Cowork consumes more than regular chat:
- Batch related work
- Use regular chat for quick questions
- Check Settings > Usage for patterns

---

## Safety Checklist

**Before first session**:
- [ ] Create dedicated work folder
- [ ] Back up important files
- [ ] Decide what Claude cannot delete

**Every session**:
- [ ] Explicit constraints in prompt
- [ ] Avoid sensitive files in work folder
- [ ] Limit browser to trusted sites

---

## Cross-References

- [[SYNTHESIS-agents_mcp_foundations]] → Agent fundamentals
- [[MECH-subagent_delegation]] → Sub-agent patterns
- [[MECH-skill_system_architecture]] → Custom skills
