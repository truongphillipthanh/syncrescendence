---
url: https://x.com/arscontexta/status/2015585363318743071
author: Heinrich (@arscontexta)
captured_date: 2026-01-25
---

# Obsidian & Claude Code 101: Context Engineering

(Description: A stylized illustration showing a Renaissance-era scholar figure examining documents alongside layered computational diagrams. The left side displays file tree structures and YAML frontmatter examples. The center shows marked sections with numbered callouts (①②③④) indicating the progressive disclosure layers. On the right, a bearded figure in period clothing holds documents, symbolizing knowledge work and information architecture.)

## Overview

Vibe note-taking works better if you force Claude Code to be selective about what it reads.

By default Claude reads full files whenever they seem useful for the task.

Use 4 layers to be more selective.

The pattern is called **progressive disclosure**.

## 1. File Tree

A session start hook injects the full file tree before Claude touches anything.
```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "tree -L 3 -a -I '.git|.obsidian' --noreport"
          }
        ]
      }
    ]
  }
}
```

This gives Claude the map before it starts exploring.

Filenames are descriptive so they work as a first impression.

> "queries evolve during search so agents should checkpoint md"

This tells you more than "search notes md".

Just reading the tree already shows what notes are about.

## 2. YAML Descriptions

Every note has a one sentence description in the frontmatter.
```yaml
---
description: Memory retrieval in brains works through spreading activation where neighbors prime each other. Wiki link traversal replicates this, making backlinks function as primes that surface relevant contexts
---

# spreading activation models how agents should traverse
...
```

The description elaborates the title.

If something seems interesting Claude queries it with ripgrep.
```bash
rg "^description:" 01_thinking/*.md
```

## 3. Outline

If a note passes the description filter Claude checks the outline.

Sometimes you only need one section and loading the full file would create noise.
```
grep -n "^#" "01_thinking/knowledge-work.md"
# output:
# 5:# knowledge-work
# 13:## Core Ideas
# 19:## Tensions
# 23:## Gaps
```

Now Claude knows where to look and can read what it needs.

## 4. Full Content

If everything seems relevant for the task Claude loads the full file.

But only for notes that passed all three filters.

Most notes never get here but that's the point.

When Claude has to justify each read it curates better.

## The MCP Parallel

This isn't a new pattern.

MCP tool discovery works the same way.

When you have 50+ tools Claude doesn't load all definitions into context upfront.

Tool specs are available but deferred until Claude actually searches for them.
```plaintext
tool list → tool search → tool references → full definitions
```

Same structure:
```plaintext
file tree → descriptions → outline → full content
```

## Implementation

The whole thing is just:

1. A SessionStart hook that runs `tree`
2. YAML frontmatter with a description field
3. Instructions in claude.md telling Claude to check descriptions before reading

Just a few constraints that force selectivity.

---

**Author:** Heinrich (@arscontexta)  
**Posted:** 4:39 PM · Jan 25, 2026  
**Engagement:** 12 replies, 71 reposts, 731 likes, 1,448 bookmarks, 94,900 views