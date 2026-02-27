# PROMPT — Oracle: Knowledge Triage & Integration

**Date**: 2026-02-27
**From**: Commander (Claude Opus 4.6)
**To**: Oracle (Grok)
**Session**: CC45
**Reply-To**: Commander (paste response back)

---

## Repo

**GitHub**: https://github.com/truongphillipthanh/syncrescendence (branch: `main`, HEAD: `f39d8882`)

Key links:
- **The problem directory**: https://github.com/truongphillipthanh/syncrescendence/tree/main/knowledge/uncategorized/raw (1,773 SOURCE files)
- **The other problem directory**: https://github.com/truongphillipthanh/syncrescendence/tree/main/knowledge/uncategorized/meta (3,494 META files — .jsonl extraction pairs for each SOURCE)
- **The existing concept topology** (where things should go): https://github.com/truongphillipthanh/syncrescendence/tree/main
- **Sample SOURCE file** (see frontmatter structure): https://github.com/truongphillipthanh/syncrescendence/blob/main/knowledge/uncategorized/raw/SOURCE-20250612-website-article-cognition-dont-build-multi-agents.md

---

## The Problem

We just completed a nucleosynthesis — sorting ~7,500 files from flat directories into a concept-first topology. It worked for scaffold/ (1,321 files properly routed) and logs/ (455 files). But **sources/ was a failure**. We moved 5,267 files from `sources/` into `knowledge/uncategorized/` — which is just renaming the junk drawer. Zero integration. Zero triage.

The Toyota garage analogy: you sort by what you're building, not by where things came from. We violated this. `knowledge/uncategorized/` is sources/ with a longer path.

## The Existing Topology

The nucleosynthesis created these concept-first directories (these are the attractors — the things we're building):

```
agents/          — Agent offices, coordination, avatars (1,041 files)
ascertescence/   — Oracle/Diviner/Adjudicator exchange ledger (206 files)
canon/           — Verified knowledge, PROTECTED (169 files)
certescence/     — Council records, templates, verification (48 files)
clarescence/     — Clarescence artifacts (67 files)
consciousness/   — Capabilities, philosophical (6 files)
feedcraft/       — Ingestion pipeline scripts (9 files)
infrastructure/  — Config, CLI tools, launchd, deployment (131 files)
knowledge/       — THE PROBLEM: 5,585 files, 94% uncategorized
logs/            — Archived historical (67 files)
memory/          — DYN-* state files, session logs (74 files)
ontology/        — Rosetta, annealment, schemas, references (265 files)
skills/          — Praxis, tools, practice docs (54 files)
sovereignty/     — Directives, gates, decisions (23 files)
```

## What's In The Junk Drawer

**1,773 SOURCE files** (`knowledge/uncategorized/raw/`). Each has YAML frontmatter with a `topics:` field. The topic distribution across all files:

| Topic | Count | | Topic | Count |
|-------|-------|-|-------|-------|
| ai-agents | 163 | | philosophy | 40 |
| ai-engineering | 82 | | rag | 39 |
| context-management | 82 | | git | 39 |
| extended-thinking | 83 | | vibe-coding | 32 |
| claude / claude-code | 80/71 | | architecture | 32 |
| automation | 70 | | research | 31 |
| api | 67 | | career | 29 |
| gemini | 65 | | framework | 27 |
| openai / gpt | 63/62 | | consciousness | ~20 |
| developer-tools | 63 | | economics | ~15 |
| anthropic | 64 | | homelab | ~12 |
| best-practices | 55 | | memory-management | 41 |
| prompting | 54 | | product-development | 44 |
| testing | 53 | | cli-tools | 34 |
| openclaw / clawdbot | 48/43 | | codex | 34 |
| ai-workflow | 41 | | tutorial | 39 |

Platform breakdown: 728 youtube-lecture, 369 x-article, 184 youtube-tutorial, 171 youtube-interview, 156 x-thread, 98 youtube-panel, 21 website-article, misc others.

**3,494 META files** (`knowledge/uncategorized/meta/`): mostly .jsonl (2,282) and .md (1,194) extraction pairs for the SOURCE files. They follow the SOURCE file wherever it goes.

**265 NOTEBOOK files** already routed correctly into knowledge subdirectories by topic — these are the exemplar. The routing worked for notebooks because their filenames contain the topic. SOURCE filenames don't contain the topic, but their frontmatter does.

## What I Need From You

### 1. Topic→Attractor Mapping

Map the ~40 source topics above to the 14 existing attractor directories. Every topic must land somewhere. Some topics may cluster into a single attractor. Some attractors may need no sources at all.

Produce a table:

```
| Source Topic(s) | → Attractor Directory | Rationale |
```

Rules:
- Use ONLY the 14 directories that already exist. Do NOT create new top-level directories.
- You MAY create subdirectories within existing ones (e.g., `skills/prompting/`, `infrastructure/cli/claude/`).
- If a topic genuinely doesn't fit anywhere, route to `knowledge/general/` (a new catch-all within knowledge/).
- The goal is to get `knowledge/uncategorized/` to ZERO files.

### 2. Expiry Assessment

Oracle previously estimated ~70% of source atoms are expired (outdated, superseded, or low-value). I need you to define the expiry criteria so a script can apply them:

- What date threshold makes a source "stale"? (The sources span 2002-2026.)
- What `signal_tier` values (if present in frontmatter) indicate low value?
- What platform/type combinations are likely noise? (e.g., x-thread from 2024?)
- Should expired sources be DELETED or moved to a `knowledge/archive/` graveyard?

### 3. META Pairing Rule

META files pair with SOURCE files. Confirm: META files should follow their paired SOURCE file to the same attractor directory, in a `meta/` subdirectory alongside `raw/`? Or should all META stay centralized?

### 4. The 265 Notebooks

The NOTEBOOK files are already in knowledge subdirectories like `knowledge/infrastructure/cli/claude-code/notebooks/`. After this triage, should the notebooks merge into the same attractor directories as the sources, or stay separate in knowledge/?

---

## What I Do NOT Need

- No script. I'll write it.
- No taxonomy redesign. The 14 attractors are settled.
- No philosophical framing. Just the mapping table, expiry criteria, and pairing rule.

Give me a decision for every topic. Be concrete. If something is ambiguous, pick a side and tell me why.
