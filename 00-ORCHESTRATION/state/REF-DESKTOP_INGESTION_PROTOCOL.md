# REF — Desktop Ingestion Protocol

**Date**: 2026-01-31
**Authors**: Ajna (Opus 4.5) + Psyche (GPT-5.2)
**Purpose**: Canonical routing rules for all Desktop materials into syncrescendence

## Canonical Root
`~/Desktop/syncrescendence/` — this is ground truth. No mirrors.

## Routing Rules

| Source | Destination | Method |
|--------|------------|--------|
| Desktop/todos/* | Backlog items → DYN-BACKLOG.md | Extract actionable items, archive originals in 05-MEMORY/ |
| Desktop/claude-code-disruption-research/* | 04-SOURCES/research/ | Move wholesale, preserve directory structure |
| Desktop/building upon previous research.../* | 04-SOURCES/research/ajna9-fodder/ | Move wholesale |
| Desktop/configuration_layers/* | 02-ENGINE/configs/ | Formalize into skills/configs |
| Desktop/legacy/Coherence/* | 05-MEMORY/legacy/coherence/ | Archive with provenance |
| Desktop/legacy/Tech/* | Extract → 02-ENGINE/ontology/registry/ | Via ontology extraction pipeline |
| Desktop/legacy/Transcendence/* | 05-MEMORY/legacy/transcendence/ | Archive with provenance |
| Desktop/legacy/scaffold/* | Triage: metabolized → 05-MEMORY/, unmetabolized → 03-QUEUE/ | File-by-file assessment |
| Desktop/x_articles/* | 03-QUEUE/feedcraft/ | Pending read + metabolization |
| Desktop/zip/* | 05-MEMORY/snapshots/ | Historical reference only |
| Desktop loose files | File by type (see below) | |

## Loose File Routing
- `dns-gemini*.md` → 04-SOURCES/explainers/
- `my inputs*.md` → 05-MEMORY/ (process archaeology)
- `slackbot.md` → DELETE (tokens in config, sensitive)
- `TREE.md` → DELETE (macOS bookmark artifact)
- `*.jpg`, `*.png` → 02-ENGINE/avatars/ or DELETE if screenshots

## Completion Criteria
Desktop should contain ONLY:
- `/syncrescendence` (the repo)
- Nothing else

All other materials metabolized into the corpus structure.
