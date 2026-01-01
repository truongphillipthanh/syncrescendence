# SOURCES Directory

External intelligence input layer for the Syncrescendent apparatus.

## Structure

```
SOURCES/
├── raw/           # Unprocessed source files
├── processed/     # Clean, frontmatter-tagged sources (FLAT)
├── index.md       # Master manifest
└── README.md      # This file
```

## Relationship to Other Tiers

- **SOURCES** = External intelligence INPUT (not authored by Principal)
- **CANON** = Authored synthesis OUTPUT
- **QUEUE** = Pending work items

## Naming Convention

```
SOURCE-{YYYYMMDD}-{platform}-{format}-{creator}-{title_slug}.md
```

## Processing Flow

```
raw/ → triage → processed/ → integration → CANON/
```

## See Also

- `SOURCES/index.md` — Master manifest
- `orchestration/state/ORACLE9_CONTEXT.md` — Full schema documentation
