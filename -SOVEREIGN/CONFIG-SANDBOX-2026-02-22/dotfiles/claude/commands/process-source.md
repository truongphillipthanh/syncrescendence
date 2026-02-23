---
name: process-source
description: Process a source document from raw to processed
allowed-tools: Read, Write, Edit, Bash(python:*), Bash(grep:*), Glob
---
# Process Source Document

Process: $ARGUMENTS

## Workflow
1. **Locate**: Find in sources/raw/ using the provided identifier
2. **Read**: Extract full content and metadata
3. **Analyze**: Identify key themes, claims, relevance to chains
4. **Generate**: Create qualified brief with frontmatter
5. **Write**: Save to sources/processed/ with correct naming
6. **Update**: Add entry to sources.csv (status: processed, date_processed: today)
7. **Verify**: Confirm file exists and CSV updated

## Naming Convention
`{YYYYMMDD}-{platform}_{format}-{channel}-{guest_or_title}.md`

## Frontmatter Template
```yaml
---
id: SOURCE-{date}-{platform}-{format}-{channel}-{slug}
title: "{Title}"
date_published: {YYYY-MM-DD}
date_processed: {YYYY-MM-DD}
platform: {youtube|x|substack|arxiv}
format: {video|lecture|panel|thread|article}
creator: "{Channel/Author}"
guest: "{Guest Name if interview}"
signal_tier: {paradigm|strategic|tactical}
chains: [{Intelligence|Information|Insight|Expertise|Knowledge|Wisdom}]
status: processed
---
```

## Output
- Processed file in sources/processed/
- Updated sources.csv entry
- Verification confirmation
