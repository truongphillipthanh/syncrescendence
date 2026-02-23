# ARCH-SCAFFOLD_ELUCIDATION.md
## What the Scaffold Is, What It Contains, and What It's For

**Version**: 1.0.0
**Created**: 2026-02-22
**Authority**: Sovereign + Oracle consensus
**Purpose**: Complete elucidation of the non-CANON directories for cross-platform sensing (Grok, Oracle, all agents)

---

## The Two-Layer Architecture

Syncrescendence separates **doctrine** (canon) from **operations** (everything else). The CANON is the immutable knowledge corpus — 81 files organized by celestial tier (cosmic/core/lattice/planetary/lunar/asteroid) across Six Chains (Intelligence → Information → Insight → Expertise → Knowledge → Wisdom). It is the "what we believe and have proven."

The **scaffold** is everything else — the factory that metabolizes raw intellectual feed into canonical knowledge and operational capability. The scaffold is where the work happens. CANON is where the results live.

**Critical insight**: The scaffold currently captures ~12% of the convergence vision operationally. This is correct build order (factory before product), but the inflection point for product-facing scaffold injection is NOW — during the Abstraction Phase window (~85% LM maturity, 12-24 months remaining).

---

## Scaffold Directory Map

### orchestration/ — The Nervous System

**Purpose**: Strategic coordination, automation, state management, and the full decision/execution audit trail.

**Three layers**:

| Layer | Path | What Lives Here | File Count |
|-------|------|-----------------|------------|
| **State** | `state/` | Live operational brain — architecture decisions (ARCH-*), dynamic state (DYN-*), references (REF-*), implementation records (impl/) | ~80 files + subdirs |
| **Scripts** | `scripts/` | Automation engine — ingest, dispatch, ontology, health, verification, SN codec, launchd plists | ~90 files |
| **Archive** | `archive/` | Historical record — resolved decisions, old dispatches, graduated state files | ~80 files |

**Key state files for live sensing**:
- `DYN-SYSTEM_STATE.json` — machine-readable constellation snapshot
- `DYN-TASKS.csv`, `DYN-PROJECTS.csv`, `DYN-FUNCTIONS.csv` — structured ledgers
- `DYN-MODELS.csv`, `DYN-API_PRICING.csv` — model intelligence (STALE — needs live ledger)
- `DYN-GLOBAL_LEDGER.md` — cross-session work record
- `DYN-DEFERRED_COMMITMENTS.md` — open promises (86% deferred loss rate historically)
- `ARCH-INTENTION_COMPASS.md` (v3.3.0) — 21+ Council sessions of Sovereign intentions
- `ontology.db` — SQLite (1484 rows, 43 tables, 340 strategic relationships)

**Key implementation subdirs**:
- `impl/clarescence/` — ~40 deep analysis documents, the decision + execution trail
- `impl/kinetic/` — automation binding layer (action types, agent bindings, model capabilities)
- `impl/sensing/` — audit templates (corpus staleness, ecosystem health, frontier scan)
- `impl/tooling/` — tool decision records

### engine/ — The Operational Reference Library

**Purpose**: Everything an agent needs to understand HOW to operate — reference docs, function definitions, prompts, avatars, model profiles.

**Prefix taxonomy** (135 files total):

| Prefix | Count | What It Is |
|--------|-------|------------|
| REF- | 32 | Canonical operational specifications (Rosetta Stone, Fleet Handbook, Stack Teleology, Clarescence Runbook, Memory Architecture, etc.) |
| FUNC- | 28 | Processing operations — XML/MD verb definitions (absorb, amalgamate, amplify, anneal, coalesce, compile, consolidate, harmonize, reforge, translate) + transcription suite (youtube, interview, x_thread, medium, panel, website) + content transforms (readize, listenize, audize, integrate) |
| PROMPT- | 18 | Canonical prompts per AI platform (Claude, ChatGPT, Gemini, Grok) + handoff/memory prompts |
| AVATAR- | 8 | Per-AI persona configurations (each avatar = role + characteristic cognition + constraints) |
| MODEL- | 7 | Model profiles as YAML (Claude 4 Sonnet, Claude 4.1 Opus, Claude 4.5 Opus, Gemini 2.5 Pro, GPT-5, Grok 4) + MODEL-INDEX.md |
| IIC- | 6 | Interlocutor Identity Configurations — 5 account personas + shared protocols |
| DYN- | 7 | Dynamic operational data (accounts, platforms, roles CSVs; constellation config JSON; coordination YAML; IIC registry; ticker feed) |
| CAP- | 5 | Capability YAML definitions |
| QUEUE- | 7 | Processing backlogs |
| TOOL- | 4 | Tool definitions |
| SURVEY- | 2 | AI ecosystem surveys |

**Critical for live ledger**: The MODEL-*.yaml files and DYN-MODELS.csv are the current model intelligence store — but they are STATIC snapshots. The live ledger must replace these with a dynamic, cross-referenced, continuously-updated intelligence surface.

### sources/ — The Intellectual Feed

**Purpose**: Raw and processed source material — the corpus that gets metabolized into CANON and SIGMA.

**Scale**: ~1,788 items total.

| Layer | Path | What Lives Here |
|-------|------|-----------------|
| **Processed** | `processed/` | 42 post-processed YouTube interviews/lectures (Dwarkesh Patel, Blaise Aguera y Arcas, Max Tegmark, Sam Altman, Jensen Huang, etc.) |
| **Research** | `research/` | 44 files/dirs — agent orchestration research, platform feature comparisons, X thread transcriptions, OpenClaw synthesis, prompt engineering |
| **Research Notebooks** | `research-notebooks/` | 14 deep-dive topic notebooks (openclaw, security, memory, notetaking, cowork, multi-agent, economics, vibe-coding, design, AI engineering, homelab, prompt engineering, philosophy) |
| **Index** | `_index/` | 8 Maps of Content (by creator, platform, signal tier, teleology, topic, transcript, chronological, NotebookLM) |
| **Meta** | `_meta/` | Census, dedup manifests, enrichment records, URL indexes, schema — the administrative audit trail |
| **Root** | `.` | 30+ individually named sources (Paul Graham, MIT OCW, hermeticism, consciousness, AI alignment, generative art) |

**Critical for live ledger**: sources contains the RAW OPERATIONAL WISDOM we've manually transcribed — platform comparisons, model capability observations, consensus patterns from the field. This is the untapped mine for the live ledger. The research-notebooks/ especially contain deep synthesis on exactly the domains the ledger needs to track.

### praxis/ — Distilled Operational Knowledge

**Purpose**: The crystallized operational wisdom — patterns proven across multiple sessions, extracted from experience.

| Layer | Path | Count | What Lives Here |
|-------|------|-------|-----------------|
| **Syntheses** | `syntheses/` | 5 | Platform-specific operational synthesis (OpenClaw v1+v2, Gemini CLI, Codex CLI, platform topology Jan 2026) |
| **Mechanics** | `mechanics/` | 11 | How things work (context compaction, git worktrees, headless mode, hooks lifecycle, MCP patterns, prompt engineering, skill system, source anneal pipeline, subagent delegation, task orchestration, youtube ingestion) |
| **Practice** | `practice/` | 13 | How to do things (auteur content, blitzkrieg worktree, cowork desktop, ledger management, multi-account coordination, multi-methodology, ontology queries, operational wisdom compendium, oracle-to-executor handoff, parallel claude orchestration, ralph pattern, semantic compression, subagent delegation) |
| **Exempla** | root | 4 | Aphorisms, proverbs, README, and the cautionary "Ajna Lobotomy" tale |

**Critical insight**: praxis is the OPERATIONAL CONSENSUS layer — the patterns that survived multiple sessions and proved reliable. The live ledger should draw from SIGMA for established patterns and feed BACK into SIGMA when new consensus crystallizes.

---

## The Scaffold as Factory

```
sources (raw feed)
    ↓ [FUNC-* processing verbs]
engine (operational reference)
    ↓ [AVATAR-* + PROMPT-* platform targeting]
orchestration (coordination + dispatch)
    ↓ [agents/ inbox → execution → outbox]
praxis (crystallized wisdom)
    ↓ [anneal + metabolize]
canon (immutable doctrine)
```

Every source enters at sources, gets processed through ENGINE functions, coordinated through ORCHESTRATION, crystallized in SIGMA, and when proven canonical, graduates to CANON.

The live ledger is the MISSING SENSING LAYER that sits across all of these — continuously monitoring external reality (model releases, benchmark results, pricing changes, community consensus shifts) and feeding signals into this pipeline.

---

## What the Scaffold Needs Next

### Immediate (this session)
1. **Live Ledger architecture** — dynamic intelligence surface replacing static MODEL-*.yaml
2. **Grok sensing integration** — Oracle as the closest thing to a live ledger (X firehose + GitHub parsing)
3. **Chat↔CLI bridge** — every platform now has some repo-viewing capability; synapticalizing this

### Near-term (next 2 weeks)
4. **sources mining** — extract operational wisdom from research-notebooks/ into SIGMA
5. **Product-facing scaffold injection** — begin building convergence vision infrastructure (content, curriculum, economics)
6. **Convergence coverage** — move from 12% to 25%+ scaffold coverage of the 28 convergence domains
