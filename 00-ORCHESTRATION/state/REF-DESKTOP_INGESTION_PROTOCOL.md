# REF — Desktop Ingestion Protocol

**Date**: 2026-01-31
**Authors**: Ajna (Opus 4.5) + Psyche (GPT-5.2)
**Purpose**: Canonical routing rules for all Desktop materials into syncrescendence

## Canonical Root
`~/Desktop/syncrescendence/` — this is ground truth. No mirrors.

## Routing Rules

| Source | Destination | Method |
|--------|------------|--------|
| Desktop/todos/* | Backlog items → DYN-BACKLOG.md | Extract actionable items, archive originals in 05-SIGMA/ |
| Desktop/claude-code-disruption-research/* | 04-SOURCES/research/ | Move wholesale, preserve directory structure |
| Desktop/building upon previous research.../* | 04-SOURCES/research/ajna9-fodder/ | Move wholesale |
| Desktop/configuration_layers/* | 02-ENGINE/ | Formalize into skills/configs |
| Desktop/legacy/Coherence/* | 05-SIGMA/ | Archive with MEMORY- prefix |
| Desktop/legacy/Tech/* | Extract → 02-ENGINE/ | Via ontology extraction pipeline |
| Desktop/legacy/Transcendence/* | 05-SIGMA/ | Archive with MEMORY- prefix |
| Desktop/legacy/scaffold/* | Triage: metabolized → 05-SIGMA/, unmetabolized → 02-ENGINE/QUEUE-* | File-by-file assessment |
| Desktop/x_articles/* | 02-ENGINE/QUEUE-feedcraft | Pending read + metabolization |
| Desktop/zip/* | 05-SIGMA/ | Historical reference with MEMORY- prefix |
| Desktop loose files | File by type (see below) | |

## Loose File Routing
- `dns-gemini*.md` → 04-SOURCES/explainers/
- `my inputs*.md` → 05-SIGMA/ with MEMORY- prefix (process archaeology)
- `slackbot.md` → DELETE (tokens in config, sensitive)
- `TREE.md` → DELETE (macOS bookmark artifact)
- `*.jpg`, `*.png` → 02-ENGINE/avatars/ or DELETE if screenshots

## Completion Criteria
Desktop should contain ONLY:
- `/syncrescendence` (the repo)
- Nothing else

All other materials metabolized into the corpus structure.
