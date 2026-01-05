# ORACLE9 CONTEXT
## Intelligence Apparatus Architecture & Transcript Ingestion
**Prepared by**: Oracle8 → Oracle9 Handoff
**Date**: 2026-01-01
**Status**: Constitutional — Include with ALL Oracle9 directives

---

## PURPOSE

> "You have to WITH EVERY DIRECTIVE HAVE THEM ENCODE WHAT WE GO OVER. ALWAYS."
> — Principal, Oracle7

> "This needs to generalize. I do believe there needs to be an architecture that would be the agentified spiritual successor to DEVONThink/Zotero."
> — Principal, Oracle9 initialization

This document captures Oracle9 scope, decisions, and context. **INCLUDE WITH EVERY DIRECTIVE.**

---

## SECTION 1: ORACLE9 MISSION

### The Teleological Frame

Oracle9 is **not administrative filing**. It is the activation of the Information Chain as functional apparatus.

**What we're building**: The agentified spiritual successor to DEVONThink/Zotero — a Personal Autonomous Intelligence Apparatus that:
- Ingests multi-platform, multi-modal content
- Qualifies through progressive triage funnel
- Processes via format-appropriate functions
- Integrates into CANON synthesis
- Maintains compression-awareness (what transcripts lose)

**What we're NOT building**: A note-taking system, a podcast archive, a content management system.

### Source Material Scope

The apparatus must accommodate (now and future):

| Domain | Examples | Modal | Compression Challenge |
|--------|----------|-------|----------------------|
| Video | YouTube, courses, lectures | 1-2 | Visual layer often essential |
| Audio | Podcasts, interviews | 1 | Delivery sometimes carries signal |
| Text-Native | Substack, articles, newsletters | 1 | Cleanest ingestion |
| Academic | ArXiv, papers, books | 1 | Citation network matters |
| Social | X threads, Reddit, HN | 1 | Comments often ARE the story |
| Literature | Books, scripture, essays | 1 | Long-form, chapter handling |
| Visual Art | Film, design, graphics | 2 | Cannot reduce to text |
| Courses | Curricula, sequential lectures | 1-2 | Order matters |

### The Immediate Corpus

**transcripts.zip**: 468 files representing 2+ years of curated primary sources
- AGI/ML interviews (Dwarkesh, Lex, etc.)
- Anthropology, biology, physics
- Physical AI, VFX, visual tools
- Industry leaders, philosophy of technology

**This is the first test case, not the design constraint.**

---

## SECTION 2: ARCHITECTURAL DECISIONS

### Decision 9.1: Eight-Dimensional Source Schema

**Principal's Words**:
> "I think this is a good exercise in type/category theory, taxonomizing the teleologies of these pieces... There is a distinction between topic, but also format and function, and cadence."

**Oracle's Interpretation**: Eight dimensions capture essential distinctions without over-taxonomizing:

1. **PLATFORM** — Where it came from (youtube, podcast, substack, arxiv, x, book, etc.)
2. **FORMAT** — Structural type (interview, panel, paper, thread, lecture, etc.)
3. **CADENCE** — Temporal pattern (daily, weekly, periodic, arrhythmic, evergreen)
4. **VALUE_MODALITY** — Where's the signal? (dialogue_primary, visual_primary, audio_primary, comments_primary, multimodal_essential, text_native)
5. **SIGNAL_TIER** — Qualification result (paradigm, strategic, tactical, noise)
6. **PROCESSING_STATUS** — State machine (raw, triaged, processed, integrated, archived)
7. **CHAIN_ALIGNMENT** — Which Syncrescendent chain served
8. **TOPIC_TAGS** — Thematic tags (free-form but curated)

**Alternatives Considered**:
1. Folder hierarchy by topic — Rejected: Violated flat principle, multi-topic sources problematic
2. Minimal metadata — Rejected: Insufficient for intelligent routing
3. Comprehensive eight-dimension schema — CHOSEN

**18-Lens Score**: 16/18 pass

---

### Decision 9.2: Value Modality as Compression Acknowledgment

**Principal's Words**:
> "There is quite a bit of compression via transcript alone. There is no capture/translation/interpretation of the audio/visual layers, more crucial in some pieces than others."

**Oracle's Interpretation**: The `value_modality` field explicitly acknowledges what transcripts lose:

| Value Modality | Transcript Captures | What's Lost | Recommendation |
|----------------|---------------------|-------------|----------------|
| dialogue_primary | 95%+ | Minimal | Full transcript sufficient |
| audio_primary | 70% | Delivery, emotion | Consider audio consumption |
| visual_primary | 40% | Slides, demos | Require visual summary layer |
| comments_primary | Variable | Thread structure | Capture discourse separately |
| multimodal_essential | <20% | Core value IS medium | Flag as Modal 2 dependency |
| text_native | 100% | Nothing | Direct ingest |

This is NOT a quality judgment — it's a routing signal for appropriate processing.

---

### Decision 9.3: Platform-Native Processing Allocation

**Principal's Words**:
> "This specific YouTube workflow might be best delegated to Gemini, or maybe Chrome, as it is its native platform."

**Oracle's Interpretation**: Use models in their native strength domain:

| Platform | Optimal Processor | Rationale |
|----------|-------------------|-----------|
| YouTube | Gemini | Native platform, video upload, visual analysis |
| Podcasts | Gemini (audio) | Audio transcription, speaker diarization |
| Substack/Articles | Claude | Text synthesis, already in text form |
| X Threads | Claude | Thread reconstruction, discourse analysis |
| ArXiv/Papers | Claude | Academic synthesis, citation handling |
| Books | Claude | Long-form synthesis, chapter handling |

**Implication**: YouTube processing is NOT Claude Code's primary task. Claude Code handles: infrastructure, schema, routing, integration. Gemini handles: YouTube transcription + visual layer capture.

---

### Decision 9.4: Flat + Naming + Aliases (Three Pillars)

**Principal's Words**:
> "I bet this is perfect fodder for the flat hierarchy, alias, frontmatter/metadata, filenaming approach, as I mentioned to Oracle 8."

**Oracle's Interpretation**: SOURCES/ follows CANON/ pattern:

1. **Flat Storage**: All processed sources at SOURCES/processed/ level
2. **Naming Convention**: `SOURCE-{YYYYMMDD}-{platform}-{format}-{creator}-{title_slug}.md`
3. **Frontmatter Metadata**: Full eight-dimension schema in YAML
4. **Aliases**: Symlink views by platform, tier, chain, topic

**18-Lens Evaluation of Aliases Timing**:
- 15/18 lenses say "create during Oracle9"
- 3 lenses say "start minimal, expand as schema stabilizes"
- **VERDICT**: Create skeletal aliases (by-platform, by-tier) during Oracle9. Expand post-stabilization.

---

### Decision 9.5: Four-System Intelligence Architecture

**Source**: Gemini conversation (2025-06-17)

**Principal's Words**:
> "As many as possible [throughput]... there should be room for discovery, as well as hyper-intelligent/personalized curated feed... This insight should be factored in holistically, not componentially."

**Oracle's Interpretation**: The Gemini conversation's four-system architecture maps to Syncrescendence:

| Gemini System | IIC Equivalent | Function |
|---------------|----------------|----------|
| Automatic-Push | Daily Intelligence Brief | Scheduled monitoring |
| Curation-Push | Serendipitous Encounters | Mobile save-to-queue |
| On-Demand-Pull | Active Research | Query-driven deep dives |
| Triage & Qualification | Priority Band | Gatekeeper ("worth attention?") |

**Critical Insight**: This is NOT four separate pipelines. It's one apparatus with four operational modes. The throughput question becomes: what mode serves which source type?

---

### Decision 9.6: Progressive Qualification Funnel

**Principal's Words** (via Gemini conversation):
> "Is this source worth my attention?" ... "The dialogue is the story" / "The comments are the story" / "The visuals are the story" / "The delivery is the story"

**Oracle's Interpretation**: Triage produces routing, not just ranking:

```
RAW SOURCE (468+ items)
        ↓
    TRIAGE
    ├── Classify format
    ├── Assess value_modality
    └── Assign signal_tier
        ↓
    ┌─────────────────┬─────────────────┬─────────────────┐
    ↓                 ↓                 ↓                 ↓
PARADIGM         STRATEGIC         TACTICAL          NOISE
(~5%)            (~20%)            (~40%)            (~35%)
Must engage      Queue for         Archive           Prune
deeply           synthesis         reference
    ↓                 ↓                 ↓
PROCESS          PROCESS           METADATA
Full transcript  Qualified brief   Only
+ integration
```

---

## SECTION 3: DIRECTORY STRUCTURE

### SOURCES/ Architecture

```
SOURCES/
├── raw/                    # Unprocessed source files (transcripts.zip contents)
├── processed/              # Clean, frontmatter-tagged sources (FLAT)
├── index.md                # Master manifest
└── README.md               # Protocol documentation

aliases/sources/            # Human navigation layer
├── by-platform/
│   ├── youtube/           → symlinks to relevant sources
│   ├── podcast/
│   ├── substack/
│   └── arxiv/
├── by-tier/
│   ├── paradigm/          → highest-priority sources
│   ├── strategic/
│   └── tactical/
└── by-chain/
    ├── intelligence/
    ├── information/
    └── insight/
```

### Naming Convention

```
SOURCE-{YYYYMMDD}-{platform}-{format}-{creator}-{title_slug}.md
```

**Examples**:
```
SOURCE-20251017-youtube-interview-dwarkesh_patel-andrej_karpathy.md
SOURCE-20250312-youtube-interview-dwarkesh_patel-joseph_henrich.md
SOURCE-20251031-x-thread-karpathy-bitter_lesson_response.md
SOURCE-20251020-arxiv-paper-anthropic-constitutional_ai.md
```

### Frontmatter Schema

```yaml
---
id: SOURCE-20251017-001
platform: youtube
format: interview
cadence: arrhythmic
value_modality: dialogue_primary
signal_tier: paradigm
status: processed
chain: intelligence
topics: [agi, scaling_laws, bitter_lesson]
creator: Dwarkesh Patel
guest: Andrej Karpathy
title: "Andrej Karpathy - AI, Software, and the Future"
url: https://youtube.com/...
date_published: 2025-10-17
date_processed: 2026-01-02
date_integrated: null
processing_function: transcribe_interview
integrated_into: []
synopsis: |
  [2-3 sentence summary]
key_insights:
  - [Insight 1]
  - [Insight 2]
visual_notes: |
  [Assessment of what transcript captures/misses]
---
```

---

## SECTION 4: PROCESSING FUNCTION ROUTING

| Format | Function | Notes |
|--------|----------|-------|
| YouTube solo | transcribe_youtube | Removes ads, previews, filler |
| YouTube interview | transcribe_interview | Preserves dialogue dynamics |
| YouTube panel | transcribe_panel | Speaker attribution |
| Podcast | transcribe_interview | Same as interview |
| Article/Substack | readize | Already text, optimize structure |
| X thread | (custom) | Thread reconstruction |
| ArXiv paper | (custom) | Academic structure preservation |
| Book chapter | (custom) | Long-form handling |

**Note**: Functions exist for transcript types. Article, thread, paper functions need development.

---

## SECTION 5: ORACLE ARC POSITION

| Oracle | Phase | Accomplishment | Current |
|--------|-------|----------------|---------|
| 0-3 | Foundation | IIC, cosmology, vocabulary | |
| 4 | Defrag | 79% reduction, 9 lenses | |
| 5 | Recovery | Orchestration restored | |
| 6 | Semantic | 18 lenses, bifurcation | |
| 7 | Ground Truth | Verification protocols | |
| 8 | Annealment | Mechanical + semantic + temporal | |
| **9** | **Ingestion** | **Intelligence apparatus architecture** | **← HERE** |
| 10 | IIC Config | Platform configurations | Next |

---

## SECTION 6: PARALLELIZATION STRATEGY

### Stream A: Infrastructure (Claude Code)
**DIRECTIVE-032A**: Create directory structure, extract archive, install schema

### Stream B: Protocol Documentation (Oracle/Desktop)
**DIRECTIVE-032B**: Complete schema documentation, triage protocol, routing logic

### Stream C: Sample Processing (After A+B)
**DIRECTIVE-033**: Triage + process sample batch (5-10 paradigm-tier sources)

### Stream D: Integration Protocol (After C)
**DIRECTIVE-034**: CANON integration demonstration

---

## SECTION 7: IMPLICIT AGREEMENTS

1. **YouTube processing delegated to Gemini** — Claude handles routing, not transcription
2. **value_modality is routing signal** — Not quality judgment
3. **Throughput target: "as many as possible"** — But with progressive qualification
4. **Schema will evolve** — Start minimal, expand through use
5. **This is MVP** — Full automation (Gemini RPA, n8n) is future work
6. **Holistic, not componential** — Four systems are modes, not pipelines

---

## SECTION 8: 18 EVALUATIVE LENSES (Reference)

| # | Lens | Question |
|---|------|----------|
| 1 | Syncrescendent Route | Continuous, cyclic, recursive? |
| 2 | Bitter Lesson | General-method, large-context-ready? |
| 3 | Antifragile | Gains from disorder? |
| 4 | Meet the Moment | Timely + future-positioned? |
| 5 | Steelman & Redteam | Survives strongest attack? |
| 6 | Personal Idiosyncrasies | Honors macroscopic-holistic cognition? |
| 7 | Potency w/o Resolution Loss | Maximum compression, full fidelity? |
| 8 | Elegance + Dev Happiness | Minimal surface, predictable patterns? |
| 9 | Agentify + Human-Navigable | 2 decisions to any file? |
| 10 | First Principles | Does it need to exist? |
| 11 | Systems Thinking | Parts relate to whole? |
| 12 | Industrial Engineering | Throughput optimization? |
| 13 | Complexity Theory | Essential vs accidental? |
| 14 | Permaculture | Self-sustaining? |
| 15 | Design Thinking | Human-centered? |
| 16 | Agile | Shippable increments? |
| 17 | Lean | Waste elimination? |
| 18 | Six Sigma | Defect reduction? |

**Threshold**: 12/18 must pass for approval.

---

## SECTION 9: PROTOCOL DOCUMENTATION

Oracle9 protocol documentation is maintained in four companion documents:

| Document | Purpose | Location |
|----------|---------|----------|
| SOURCES_SCHEMA.md | Eight-dimensional classification system | orchestration/state/ |
| TRIAGE_PROTOCOL.md | Progressive qualification funnel | orchestration/state/ |
| PROCESSING_ROUTING.md | Function selection logic | orchestration/state/ |
| FOUR_SYSTEMS.md | Operational modes documentation | orchestration/state/ |

These documents provide the operational manual for the intelligence apparatus.

---

## VERSION HISTORY

- v1.0.0 (2026-01-01): Initial creation from Oracle9 initialization session
- v1.1.0 (2026-01-01): Added Section 9 referencing protocol documentation (DIRECTIVE-032B)

---

**THIS DOCUMENT MUST ACCOMPANY EVERY ORACLE9 DIRECTIVE.**
