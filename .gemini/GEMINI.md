# Syncrescendence Vault Context

## Structure
This is a 693+ file Obsidian vault and Git repository containing:
- `00-ORCHESTRATION/` — Strategic coordination (state/, scripts/, archive/)
- `01-CANON/` — 79 canonical knowledge artifacts with standardized frontmatter (PROTECTED)
- `02-ENGINE/` — Functions, prompts, avatars, model profiles, queue items
- `04-SOURCES/` — Source documents (raw/, processed/, research/)
- `05-SIGMA/` — Operational knowledge corpus + memory + exempla
- `-INBOX/` — Filesystem kanban for agent task dispatch (per-agent subfolders)
- `-OUTGOING/` — CLI to WebApp prompt staging
- `-SOVEREIGN/` — Async decision queue from CLI agents to Sovereign

## Key Files
- `IMPLEMENTATION-MAP.md` at `00-ORCHESTRATION/state/IMPLEMENTATION-MAP.md` — 100+ sprint-level tasks
- `COCKPIT.md` — Constellation avatar/role assignments (authoritative)
- `ARCH-INTENTION_COMPASS.md` — Active strategic intentions
- `ARCH-CONSTELLATION_AGENT_LOOPS.md` — 7-phase agent loop architecture
- `REF-ROSETTA_STONE.md` at `02-ENGINE/` — 209+ term glossary

## Conventions
- All files are Markdown (.md), not Org-mode
- Frontmatter uses YAML format with `---` delimiters
- File naming: UPPERCASE-KEBAB for system files, lowercase-kebab for content
- Prefix conventions: ARCH- (architecture), DYN- (dynamic state), REF- (reference), CANON- (canonical)
- Git commits use semantic prefixes: feat:, fix:, docs:, chore:, refactor:, research:, intel:

## Research Priorities
- When surveying, always count files and report coverage percentages
- When analyzing, cross-reference with CANON frontmatter tags
- When mapping, produce Mermaid diagrams where appropriate
- Flag any files without proper frontmatter as potential drift

## Infrastructure
- Neo4j (Graphiti KG): bolt://localhost:7687 (user: neo4j)
- Qdrant: localhost:6333
- Chroma: localhost:8765
- OpenClaw Gateway: localhost:18789
