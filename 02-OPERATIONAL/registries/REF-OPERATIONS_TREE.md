---
id: operations-tree
kind: registry
scope: repo
target: repo
owner: Deviser
---

# Operations Tree: What Lives Where

Quick reference for 02-OPERATIONAL directory structure.

Last updated: 2026-01-18

## Directory Map

```
02-OPERATIONAL/
├── prompts/                    # Executable prompts by system
│   ├── chatgpt/               # ChatGPT-specific prompts
│   │   ├── PROMPT-CHATGPT-PROJECT_INSTRUCTIONS-DEVISER.md
│   │   ├── PROMPT-CHATGPT-GLOBAL_MEMORY_REGISTRATION.md
│   │   └── PROMPT-CHATGPT-PROJECT_MEMORY_ANCHOR-SYNCRESCENDENCE.md
│   ├── canonical/             # Cross-platform canonical prompts
│   ├── profiles/              # Model profile YAML specs
│   └── unified/               # Full unified prompts per platform
│
├── specs/                      # REF-* protocol documents
│   ├── REF-AUDIZER_PROTOCOL.md
│   └── REF-CHATGPT_MEMORY_POLICY.md
│
├── registries/                 # Indexes and lookup tables
│   ├── REF-OPERATIONS_ARTIFACT_TAXONOMY.md
│   ├── REF-OPERATIONS_TREE.md (this file)
│   └── REF-PROMPT_REGISTRY.md
│
├── scripts/                    # Automation scripts
│   ├── ops_lint.sh            # Frontmatter linter
│   ├── rename_canon.sh
│   └── validate_frontmatter.sh
│
├── functions/                  # Processing functions
├── models/                     # Model configurations
├── memory/                     # Memory management
├── queues/                     # Queue definitions
├── surveys/                    # Survey templates
└── templates/                  # Document templates
```

## Naming Conventions

| Prefix | Meaning | Location |
|--------|---------|----------|
| PROMPT-* | Executable prompt | prompts/ |
| REF-* | Stable protocol/spec | specs/ or registries/ |
| SCHEMA-* | Structured schema | schemas/ |
| CMD-* | Command definition | commands/ |
| MODEL_PROFILE-* | Model capability profile | prompts/profiles/ |

## Required Frontmatter

All PROMPT-* and REF-* files must have YAML frontmatter with:
- `id`: unique identifier
- `kind`: artifact type
- `scope`: global | project | repo
- `target`: chatgpt | claude_code | gemini | cli | repo

## See Also

- REF-OPERATIONS_ARTIFACT_TAXONOMY.md - Full naming/frontmatter protocol
- REF-PROMPT_REGISTRY.md - Complete prompt index
