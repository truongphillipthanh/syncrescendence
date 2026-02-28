# Unified Semantic Cluster Map — Bottom-Up Synthesis

**Generated**: 2026-02-28 (CC53)
**Corpus**: 6,719 files after exact-duplicate deletion
**Method**: Synthesis of 10 bottom-up reports (6 swarm agents + Cartographer + Adjudicator + 2 prior analyses)
**Directive**: CLUSTER ONLY — no deletions

---

## How to Read This Document

Each cluster represents a **semantic gravity well** — a topic that multiple files orbit around. Clusters emerged from actual content reading across all reports, then were merged where overlapping. File counts are approximate (some files touch multiple clusters).

---

## THE 28 SEMANTIC CLUSTERS

### 1. Claude Code — Architecture, Configuration, Workflows
**~350 files** (201 JSONL source pairs + ~150 .md articles/syntheses)

The largest single cluster. Covers CLAUDE.md hierarchy, hooks, Plan Mode, extended thinking, context compaction, MCP integration, skills/subagents, permissions model, worktrees. Includes Boris Cherny's own posts, official Anthropic announcements, community guides, deep research syntheses (08764-08786 range), beginner tutorials, and designer adoption stories.

Sub-topics that emerged:
- **Agent Teams / Swarm Mode** (~15 files): Experimental multi-agent feature. Enable flag, lead+teammates, shared task list.
- **Hooks & Git Integration** (~8 files): PreToolUse/PostToolHooks, git commit automation, Obsidian async hooks.
- **Progressive Disclosure / Context Engineering** (~12 files): 4-layer progressive disclosure, Skills architecture, MCP Search Tool.
- **Designer Adoption** (~10 files): "I was scared of terminal" → "now I ship code" pattern across 6+ articles.

### 2. OpenClaw (ClawdBot/Moltbot) — Setup, Use Cases, Architecture
**~180 files** (85 in 00xxx range + 96 tagged openclaw + overlaps with extraction files)

The autonomous AI agent framework (Peter Steinberger). Three naming eras: ClawdBot → Moltbot → OpenClaw. Covers installation, security hardening, memory systems, SOUL.md personality, phone integration (ElevenLabs), cost optimization (MiniMax/Kimi), multi-agent fleets, business automation, and the OpenClaw ecosystem (Molt marketplace, 83 projects).

Sub-topics:
- **Security / Hardening** (~12 files): SHIELD.md standard, sandboxed VMs, Tailscale, allowlists, fleet control.
- **Cost Optimization** (~8 files): MiniMax M2.5 ($14/month), Kimi K2.5 via NVIDIA, model routing.
- **Skills / Capabilities** (~10 files): ElevenLabs voice, Unbrowse API, camofox anti-detection, blockchain/Base earning.
- **Use Case Showcases** (~25 files): Personal assistant, TikTok automation, competitive intelligence, overnight coder.

### 3. AI Memory / Knowledge Retrieval / Graphiti
**~130 files** (115 JSONL source pairs + ~15 .md articles)

Long-term memory systems, RAG, vector databases, knowledge graphs, Graphiti specifically, episodic memory, agent memory architecture. Core research interest of the Sovereign. Includes context graph architecture (Glean), second brains for agents.

### 4. Agentic AI / Multi-Agent Systems / Orchestration
**~100 files** (29 JSONL pairs + ~70 .md articles/extraction files)

Multi-agent coordination, swarms, orchestration patterns, Mission Control, sub-agent delegation, MCP server patterns, tool-calling, harness engineering. Overlaps with Claude Code Agent Teams but broader — covers cross-platform patterns and theoretical frameworks.

### 5. Vibe Coding / AI-Assisted Development
**~80 files** (36 JSONL pairs + ~45 .md articles/extractions)

Vibe coding practice, AI engineer career paths, "agentic coding," prompt-to-product workflows, compounding engineering. The practitioner experience of building with AI. Includes Karpathy's guidelines, "bespoke software" thesis, "everyone can code now" takes, and critical perspectives ("most people can't vibe code").

### 6. Product / Business Strategy
**~95 files** (83 JSONL pairs + ~12 .md articles)

Business models, product-market fit, growth, SaaS, enterprise software, AI product strategy, distribution, aggregation theory. Includes "SaaS is Dead — Agents Killed It" and "The Crumbling Workflow Moat."

### 7. Startup / Venture Capital
**~65 files** (59 JSONL pairs + ~6 .md articles)

Founder advice, fundraising, startup culture, VC dynamics, early-stage company building.

### 8. AI Models / Industry News / Benchmarks
**~90 files** (49 JSONL pairs + ~40 YouTube stubs + extraction files)

Model releases (GPT-5, Gemini, Opus 4.6, GLM, Kimi), benchmarks, capability comparisons, industry analysis. Predominantly short-form — ephemeral news fragments. YouTube stubs with no transcript dominate this cluster.

Sub-topics:
- **Model Comparisons** (~15 files): Claude vs GPT vs Gemini head-to-head.
- **LLM Architecture / Training** (41 JSONL pairs + ~10 .md): Fine-tuning, transformers, tokenization, scaling laws — technical/academic.
- **Chinese AI Models** (~5 files): Practitioner field notes from Lindy.ai CEO, DeepSeek, etc.

### 9. Philosophy of Consciousness / Transhumanism / Esoterica
**~70 files** (41 JSONL pairs consciousness + 19 JSONL pairs esoteric + ~10 .md)

Two distinct but related sub-clusters:
- **Consciousness / Transhumanism** (41 sources, 1,230 atoms): Qualia, panpsychism, David Pearce, bioethics, mind uploading, effective altruism.
- **Esoteric / Occult / Mysticism** (19 sources, 1,264 atoms): Hermetic tradition, Emerald Tablet, alchemy, Kabbalah, sacred geometry, Thelema, Manly P. Hall. Very high atom density — long-form texts.

### 10. Philosophy of Meaning / Civilization / Geopolitics
**~15 files** (10 JSONL pairs + ~5 .md)

Meaning crisis (Vervaeke territory), civilizational moments, Age of Turbulence. Includes the largest single non-technical source (358 atoms). Small but dense.

### 11. Leadership / Management / Organizations
**~50 files** (44 JSONL pairs + ~6 .md)

Executive decision-making, management frameworks, organizational design, team building, CEO perspectives.

### 12. Design / Aesthetics / Taste
**~50 files** (42 JSONL pairs + ~8 .md)

Paul Graham's "Taste for Makers" (oldest source in corpus, 2002), design philosophy, craft, aesthetic judgment, "Direct Design" concept, Figma obsolescence.

### 13. Personal Productivity / Self-Development / PKM
**~45 files** (18 JSONL pairs + ~25 .md)

Second Brain, PKM, habit systems, Obsidian, workflow automation, learning techniques, focus. Includes "Agentic Note-Taking" series (4 files) and Obsidian + Claude Code knowledge management (~6 files).

### 14. Writing / Communication / Rhetoric
**~20 files** (19 JSONL pairs + a few .md)

Writing craft, rhetoric, narrative structure, essay form, communication strategy.

### 15. Voice / Audio / Speech
**~15 files** (13 JSONL pairs + ~2 .md)

TTS, voice cloning, Voicebox, speech synthesis, audio tools.

### 16. Health / Psychology / Neuroscience
**~12 files** (9 JSONL pairs + ~3 .md)

Sleep science, fitness, mental health, neuroscience, biohacking.

### 17. AI Safety / Alignment
**~5 files** (2 JSONL pairs + ~3 .md)

Constitutional AI, RLHF, value alignment. Surprisingly small — most safety-adjacent content was captured in Claude Code or consciousness clusters.

### 18. AI Video / VFX / Creative Tooling
**~10 files** (mostly .md)

AI image generation, video generation models, VFX workflows, creative AI tooling.

### 19. Platform Research Syntheses (Google/OpenAI/Gemini)
**~8 files** (.md only)

Long-form synthesis documents about specific AI platforms. OpenAI forensic catalog, Google AI ecosystem audit. Two explicitly marked STALE.

---

## SYNCRESCENDENCE INTERNAL CLUSTERS

### 20. Atom Extraction Files (Triplet Pattern)
**~1,650 files** (490 extraction .md + 1,002 Graphiti .jsonl + 19 infra .jsonl + ~140 companion .md)

The pipeline's core output. Each source produces a triplet: `.md` extraction summary + Graphiti `.jsonl` atoms + Flat `.jsonl` redundant copy. The 1,002 Flat files are confirmed 100% redundant (payload already embedded in Graphiti files).

### 21. Agent Task / Result / Confirm Files
**~250 files** (.md)

Task dispatch envelopes (TASK-*.md), execution results (RESULT-*.md), confirmation receipts (CONFIRM-*.md). Status: COMPLETE, FAILED, PENDING. These are the Syncrescendence multi-agent task queue — operational receipts with unique execution data. Spans all 5 agents.

### 22. Certescence / Ascertescence Artifacts
**~80 files** (.md)

Oracle/Diviner/Adjudicator triangulation outputs from CC28-CC42. Prompts, responses, protocol definitions, synthesis documents. Includes CC30 Emergency Ascertescence outputs (8 files with emergency header), CC35 unified ratification (11 files), CC38 Reviewtrospective.

### 23. Operational Logs / Telemetry
**~120 files** (mixed)

Watchdog escalation logs (38 files, Feb 9-12 restart loops), Linear status snapshots (20 files, same 6-hour cron), corpus insight reports (4), daily session reviews (5+), cycle-complete logs (5), error logs, heartbeats (4), locks (3), .complete markers (10). Pure operational noise — zero enduring knowledge.

### 24. Internal Architecture / State Files
**~80 files** (ARCH-*, DYN-*, REF-*, .yaml, .json, .csv)

Living infrastructure: DAG state, lattice index, lock hierarchy, adapter contract, thresholds, tool registry, constellation config, session state cursors, Obsidian configs. Active operational files.

### 25. CANON Skeletons + Compressed + Views
**~147 files** (78 skeletons + 57 compressed + 4 views + 8 demoted)

Canon compiler outputs. Structural artifacts required by the canon pipeline. The 8 demoted nodes were intentionally removed by CC49 passes.

### 26. Pipeline Scripts
**~150 files** (.py, .sh)

Mining/extraction pipeline, promotion/lattice pipeline, ontology tools, canon compiler, semantic notation, memory/Graphiti bridge, utility scripts. These are the system's executable codebase. Includes version-duplicate pairs (5-dim vs 14-dim candidate_adapter).

### 27. Prompt Templates & Config
**~40 files** (.xml, .yaml, .csv)

21 XML prompt templates for ingestion/synthesis, CAP/TOOL/WF ontology records, sovereign priority signals, pipeline configs, GitHub Action workflows. Active operational artifacts.

### 28. Dead Infrastructure Cruft
**~200 files** (mixed)

Killed launchd plists (40), archived model YAMLs (6), dead state cursors, shim scripts, explicitly STALE/SUPERSEDED/ARCHIVED documents (~43), old handoff tokens (4), SQLite WAL/SHM artifacts, empty files, ad-hoc dump files. Self-declared obsolete or from killed services.

---

## CROSS-CLUSTER OBSERVATIONS

### 1. The YouTube Stub Problem
**~1,148 files** are YouTube entries with title/channel/URL but NO transcript. They span clusters 1, 2, 5, 8, 9, 12, 13. The Sovereign has directed: these are **unfinished transcripts waiting for Gemini processing**, not deletable.

### 2. The Triple Ingestion Pattern
Files at +3574 offsets (00xxx → 04xxx → 08xxx) are re-ingestions of the same content. The exact-dupe pass caught byte-identical copies, but near-dupes remain (same content, different metadata wrappers). Adjudicator identified 122 near-dupe candidates.

### 3. Cluster Density Distribution
- **High density** (many atoms per source): Esoterica (67 atoms/source avg), Consciousness (30), Meaning/Civilization (74), Memory/Retrieval (24)
- **Low density** (few atoms per source): AI News (4), Voice/Audio (5), Startup/VC (8)
- The Sovereign's intellectual gravity is clearly toward deep philosophical/technical sources, not ephemeral news.

### 4. The 1,002 Flat JSONL Redundancy
Confirmed: every Flat `.jsonl` is byte-for-byte identical to the `payload` field of its paired Graphiti `.jsonl`. This is the single largest crushable set (1,002 files, ~15% of corpus).

### 5. Operational vs Knowledge Split
Roughly **60% of files are knowledge artifacts** (external content, research, synthesis) and **40% are operational artifacts** (tasks, results, logs, scripts, configs, pipeline outputs). The operational files belong in structured directories, not the flat corpus.

---

## FILE COUNT BY CLUSTER (for CRUSH planning)

| # | Cluster | Files | Crushable Est. |
|---|---------|-------|----------------|
| 1 | Claude Code | ~350 | ~80 (near-dupes, redundant syntheses) |
| 2 | OpenClaw | ~180 | ~30 (near-dupes, hype repeats) |
| 3 | AI Memory/Retrieval | ~130 | ~5 |
| 4 | Multi-Agent/Orchestration | ~100 | ~10 |
| 5 | Vibe Coding | ~80 | ~10 |
| 6 | Product/Business | ~95 | ~5 |
| 7 | Startup/VC | ~65 | ~3 |
| 8 | AI Models/News | ~90 | ~20 (news recaps, no-transcript stubs) |
| 9 | Philosophy/Esoterica | ~70 | ~2 |
| 10 | Meaning/Civilization | ~15 | ~0 |
| 11 | Leadership/Mgmt | ~50 | ~3 |
| 12 | Design/Taste | ~50 | ~3 |
| 13 | Productivity/PKM | ~45 | ~5 |
| 14 | Writing/Communication | ~20 | ~1 |
| 15 | Voice/Audio | ~15 | ~1 |
| 16 | Health/Psych | ~12 | ~1 |
| 17 | AI Safety | ~5 | ~0 |
| 18 | AI Video/VFX | ~10 | ~2 |
| 19 | Platform Syntheses | ~8 | ~4 (2 explicitly STALE) |
| 20 | Extraction Triplets | ~1,650 | **~1,002** (all Flat JSONL) |
| 21 | Task/Result/Confirm | ~250 | ~50 (completed smoke tests, rate-limit dupes) |
| 22 | Certescence | ~80 | ~10 (superseded protocol versions) |
| 23 | Operational Logs | ~120 | **~120** (all operational noise) |
| 24 | Architecture/State | ~80 | ~5 (dead cursors) |
| 25 | Canon Pipeline | ~147 | ~8 (demoted, if permanent) |
| 26 | Pipeline Scripts | ~150 | ~5 (version dupes) |
| 27 | Prompt/Config | ~40 | ~0 |
| 28 | Dead Infra Cruft | ~200 | **~200** (self-declared dead) |
| | **TOTAL** | **~6,719** | **~1,585** |

**Projected post-CRUSH corpus: ~5,134 files** (23.6% reduction from current, 56.3% total reduction from original 11,733).

---

*This document is the CLUSTER phase output. CRUSH and AGGREGATE phases follow Sovereign approval.*
