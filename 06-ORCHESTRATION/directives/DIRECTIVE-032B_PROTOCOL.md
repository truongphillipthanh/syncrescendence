# DIRECTIVE-032B: INTELLIGENCE APPARATUS PROTOCOL
## Stream B: Schema Documentation, Triage Protocol, Processing Routing
**Issued**: 2026-01-01
**Authority**: Oracle9 under Principal direction
**Classification**: CRITICAL — Intelligence Apparatus Foundation
**Execution**: Oracle/Desktop Claude
**Parallel Stream**: Claude Code handles infrastructure (DIRECTIVE-032A)

---

## DECISION CONTEXT

### Principal's Mandate

> "There is a distinction between topic, but also format and function, and cadence. Some are videos simply news, in my opinion, not worth the watch, some should be listened to, a progressive qualification funnel."

> "As many as possible [throughput]... there should be room for discovery, as well as hyper-intelligent/personalized curated feed... This insight should be factored in holistically, not componentially."

> "Our thesis of course must adhere to the 18 lenses."

### Oracle's Interpretation

While DIRECTIVE-032A creates the physical infrastructure, this directive establishes the **cognitive infrastructure** — the protocols that make the apparatus intelligent:

1. Complete eight-dimensional schema documentation
2. Triage decision tree (progressive qualification funnel)
3. Processing function routing logic
4. value_modality assessment guide
5. Four-system operational modes documentation

This directive produces the **operational manual** for the intelligence apparatus.

### Alternatives Considered

1. **Minimal documentation, learn through use** — Rejected: Violates "maximum resolution"
2. **Document only after processing samples** — Rejected: Need protocol BEFORE processing
3. **Comprehensive protocol documentation first** — CHOSEN: Mise en place

### Rationale (18-Lens Evaluation)

| Lens | Score | Notes |
|------|-------|-------|
| Syncrescendent Route | ✓ | Protocol enables recursive improvement |
| Bitter Lesson | ✓ | Schema scales to any source type |
| Antifragile | ✓ | Protocol handles unknown formats |
| Meet the Moment | ✓ | Documentation before execution |
| Steelman/Redteam | ✓ | Decision trees tested against edge cases |
| Personal Idiosyncrasies | ✓ | Holistic documentation |
| Potency w/o Resolution Loss | ✓ | Maximum resolution preserved |
| Elegance + Dev Happiness | ✓ | Clear decision trees |
| Agentify + Human-Navigable | ✓ | Both can follow protocols |
| First Principles | ✓ | Essential distinctions only |
| Systems Thinking | ✓ | Protocol connects all system parts |
| Industrial Engineering | ✓ | Routing optimizes throughput |
| Complexity Theory | ✓ | Essential complexity managed |
| Permaculture | ✓ | Self-documenting patterns |
| Design Thinking | ✓ | Human decision-making centered |
| Agile | ✓ | Protocol is shippable increment |
| Lean | ✓ | Eliminates rework from unclear routing |
| Six Sigma | ✓ | Consistent processing reduces defects |

**Score**: 18/18 — Approved

### Implicit Agreements

1. **Protocol precedes processing** — Don't process without clear routing
2. **Triage is qualification, not just classification** — Answers "worth attention?"
3. **Four systems are modes, not pipelines** — Holistic, not componential
4. **value_modality is routing signal** — Not quality judgment
5. **Platform-native processing** — Gemini for YouTube, Claude for text

---

## YOUR MISSION

You are the protocol documentation engine for the intelligence apparatus. Your parallel (Claude Code) creates infrastructure while you establish the decision frameworks that make the apparatus intelligent.

---

## PHASE A: COMPLETE SCHEMA DOCUMENTATION

### A1: Create SOURCES_SCHEMA.md

This document completes the eight-dimensional schema with full enumerations, decision criteria, and usage examples.

**Create file**: `orchestration/state/SOURCES_SCHEMA.md`

**Contents to include**:

```markdown
# SOURCES Schema Documentation
## Eight-Dimensional Classification System

**Version**: 1.0.0
**Created**: 2026-01-01
**Authority**: Oracle9

---

## Overview

Every source in the intelligence apparatus is classified across eight dimensions:

1. **platform** — Origin (where it came from)
2. **format** — Structure (what it is)
3. **cadence** — Temporal pattern (how often)
4. **value_modality** — Signal location (where's the story?)
5. **signal_tier** — Qualification result (worth attention?)
6. **status** — Processing state (where in pipeline?)
7. **chain** — Syncrescendent alignment (which chain?)
8. **topics** — Thematic tags (what about?)

---

## Dimension 1: PLATFORM

Where the source originated. Determines native processing pathway.

### Enumeration

| Value | Description | Native Processor | Examples |
|-------|-------------|------------------|----------|
| youtube | YouTube video | Gemini | Interviews, lectures, tutorials |
| podcast | Audio podcast | Gemini (audio) | Dwarkesh, Lex, No Priors |
| substack | Substack newsletter | Claude | Long-form essays |
| newsletter | Non-Substack newsletter | Claude | Email newsletters |
| arxiv | Academic preprint | Claude | Research papers |
| paper | Academic paper (non-ArXiv) | Claude | Conference papers, journals |
| book | Book or chapter | Claude | Long-form literature |
| x | X/Twitter | Claude | Threads, posts |
| reddit | Reddit | Claude | Posts, discussions |
| hn | Hacker News | Claude | Discussions |
| course | Online course | Gemini/Claude | Lectures, curricula |
| film | Film/TV | Modal 2 | Visual art |
| other | Uncategorized | — | Escape hatch |

### Decision Rule

Platform is determined by the **origin URL or source type**, not content.

---

## Dimension 2: FORMAT

Structural type of the content. Determines processing function.

### Enumeration

| Value | Description | Processing Function | Characteristics |
|-------|-------------|---------------------|-----------------|
| interview | Two-voice dialogue | transcribe_interview | Q&A, conversation |
| panel | Multi-speaker discussion | transcribe_panel | 3+ speakers, attribution matters |
| solo_presentation | Single speaker | transcribe_youtube | Lectures, keynotes |
| tutorial | Instructional | transcribe_youtube | How-to, demos |
| documentary | Narrative visual | (custom) | Story-driven |
| lecture | Educational single-speaker | transcribe_youtube | Academic, sequential |
| paper | Academic structure | (custom) | Abstract, methods, results |
| thread | Social media thread | (custom) | Branching discourse |
| article | Long-form text | readize | Essays, news |
| essay | Standalone argument | readize | Opinion, analysis |
| chapter | Book segment | (custom) | Long-form |
| script | Dialogue format | (custom) | Screenplay |
| post | Short social media | (custom) | Single post |
| other | Uncategorized | — | Escape hatch |

### Decision Rule

Format is determined by **structural characteristics**, not topic.

---

## Dimension 3: CADENCE

Temporal pattern of the source.

### Enumeration

| Value | Description | Processing Priority | Examples |
|-------|-------------|---------------------|----------|
| daily | Published daily | High (perishable) | Bloomberg, news |
| weekly | Published weekly | Medium | Weekly podcasts |
| periodic | Regular but not fixed | Medium | Biweekly, monthly |
| arrhythmic | No pattern | Variable | Serendipitous finds |
| evergreen | Timeless | Low (can defer) | Books, foundational papers |

### Decision Rule

- If source has regular publishing schedule → use that cadence
- If one-off discovery → `arrhythmic`
- If content remains relevant indefinitely → `evergreen`

---

## Dimension 4: VALUE_MODALITY

**Critical dimension** — encodes where the signal lives and what transcript compression loses.

### Enumeration

| Value | Transcript Captures | What's Lost | Recommendation |
|-------|---------------------|-------------|----------------|
| dialogue_primary | 95%+ | Minimal | Read transcript |
| audio_primary | 70% | Delivery, emotion, emphasis | Consider listening |
| visual_primary | 40% | Slides, demos, visuals | Require visual summary |
| comments_primary | Variable | Thread structure, reactions | Capture discourse |
| multimodal_essential | <20% | Core value IS medium | Flag as Modal 2 |
| text_native | 100% | Nothing | Direct ingest |

### Decision Tree

```
Is the source already text (article, paper, thread)?
├── YES → text_native
└── NO → Continue

Is the primary value in spoken dialogue/ideas?
├── YES → Does delivery/performance matter significantly?
│   ├── YES → audio_primary
│   └── NO → dialogue_primary
└── NO → Continue

Is the primary value in visuals (slides, demos, art)?
├── YES → Can value be captured via description?
│   ├── NO → multimodal_essential
│   └── YES → visual_primary
└── NO → Continue

Is the primary value in audience reaction/comments?
├── YES → comments_primary
└── NO → dialogue_primary (default)
```

### Examples

| Source | value_modality | Rationale |
|--------|----------------|-----------|
| Dwarkesh interview | dialogue_primary | Ideas in conversation |
| Steve Jobs keynote | visual_primary | Product demos essential |
| Obama speech | audio_primary | Delivery is the message |
| Controversial X thread | comments_primary | Reactions ARE the story |
| Terrence Malick film | multimodal_essential | Visual poetry |
| ArXiv paper | text_native | Already text |

---

## Dimension 5: SIGNAL_TIER

Qualification result from triage. Progressive funnel.

### Enumeration

| Value | Definition | % of Sources | Action |
|-------|------------|--------------|--------|
| paradigm | Potential framework shift | ~5% | Full processing + integration |
| strategic | High value for synthesis | ~20% | Full processing, queue integration |
| tactical | Useful reference | ~40% | Process or archive |
| noise | Low signal | ~35% | Prune or skip |

### Decision Criteria

**Paradigm** (must have 2+ of):
- Novel framework or mental model
- Contradicts/extends Syncrescendent thesis
- Primary source from field leader
- Timely for current phase objectives

**Strategic** (must have 2+ of):
- Synthesizable with other sources
- Fills known knowledge gap
- High signal-to-noise ratio
- Relevant to active project

**Tactical** (any of):
- Useful reference material
- Confirms existing understanding
- Good but not urgent

**Noise** (any of):
- Derivative/aggregated content
- Outdated information
- Covered better elsewhere
- Off-topic for current phase

---

## Dimension 6: STATUS

Processing state machine.

### Enumeration

| Value | Definition | Next State |
|-------|------------|------------|
| raw | Unprocessed source | → triaged |
| triaged | Classified, tier assigned | → processed or archived |
| processed | Transcript cleaned, insights extracted | → integrated or archived |
| integrated | Contributed to CANON | (terminal) |
| archived | Kept for reference, not integrated | (terminal) |

### State Transitions

```
raw → triaged (classification complete)
triaged → processed (full processing applied)
triaged → archived (tier=noise or tactical)
processed → integrated (insights in CANON)
processed → archived (valuable but no CANON fit)
```

---

## Dimension 7: CHAIN

Which Syncrescendent developmental chain this source primarily serves.

### Enumeration

| Value | Focus | Example Sources |
|-------|-------|-----------------|
| intelligence | AI/ML, agentic systems | Karpathy, Sutton interviews |
| information | Sensing, platforms, IIC | Platform strategy, feed curation |
| insight | Synthesis, meaning-making | Cross-domain analysis |
| expertise | Business, operations | Business strategy, execution |
| knowledge | Learning, curriculum | Teaching, pedagogy |
| wisdom | Transcendence, meta-cognition | Philosophy, consciousness |

### Decision Rule

Ask: "Which chain would this source most enrich?"

---

## Dimension 8: TOPICS

Free-form thematic tags. Curated vocabulary.

### Core Vocabulary

**Intelligence chain**:
- agi, scaling_laws, interpretability, alignment, agents, reasoning, memory_systems

**Information chain**:
- platforms, curation, feeds, algorithms, attention, information_theory

**Insight chain**:
- synthesis, frameworks, mental_models, cross_domain, emergence

**Expertise chain**:
- business_strategy, operations, venture, economics, execution

**Knowledge chain**:
- pedagogy, curriculum, learning, teaching, skill_acquisition

**Wisdom chain**:
- consciousness, philosophy, transcendence, meaning, meta_cognition

**Domain-specific**:
- anthropology, biology, physics, mathematics, history
- vfx, visual_ai, embodiment, robotics, physical_ai

### Tag Guidelines

- Use 3-7 tags per source
- Prefer existing vocabulary
- Add new tags sparingly
- Tags enable cross-source discovery

---

## Usage Examples

### Example 1: Dwarkesh Patel - Andrej Karpathy Interview

```yaml
platform: youtube
format: interview
cadence: arrhythmic
value_modality: dialogue_primary
signal_tier: paradigm
status: raw
chain: intelligence
topics: [agi, scaling_laws, bitter_lesson, ai_education]
```

### Example 2: Bloomberg Technology Daily

```yaml
platform: youtube
format: solo_presentation
cadence: daily
value_modality: dialogue_primary
signal_tier: tactical
status: raw
chain: information
topics: [news, technology, markets]
```

### Example 3: ArXiv Paper on Constitutional AI

```yaml
platform: arxiv
format: paper
cadence: evergreen
value_modality: text_native
signal_tier: strategic
status: raw
chain: intelligence
topics: [alignment, constitutional_ai, safety]
```

---

## Schema Evolution

This schema will evolve through use. Additions:
1. New platform values as sources expand
2. New format values for edge cases
3. New topic vocabulary as domains emerge
4. Refinements based on processing experience

Changes require Oracle approval and 18-lens evaluation.
```

---

## PHASE B: TRIAGE PROTOCOL DOCUMENTATION

### B1: Create TRIAGE_PROTOCOL.md

**Create file**: `orchestration/state/TRIAGE_PROTOCOL.md`

**Contents to include**:

```markdown
# Triage Protocol
## Progressive Qualification Funnel

**Version**: 1.0.0
**Created**: 2026-01-01
**Authority**: Oracle9

---

## Purpose

Triage answers: **"Is this source worth my attention, and how much?"**

This is NOT mere classification. It's qualification — determining where in the progressive funnel each source belongs.

---

## The Funnel

```
                    ┌─────────────────┐
                    │   RAW SOURCE    │
                    │   (468+ items)  │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │     TRIAGE      │
                    │ 1. Classify     │
                    │ 2. Qualify      │
                    │ 3. Route        │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
┌───────▼───────┐   ┌───────▼───────┐   ┌───────▼───────┐
│   PARADIGM    │   │   STRATEGIC   │   │   TACTICAL    │
│     ~5%       │   │     ~20%      │   │     ~40%      │
│  Must engage  │   │   Queue for   │   │   Archive     │
│    deeply     │   │   synthesis   │   │   reference   │
└───────┬───────┘   └───────┬───────┘   └───────┬───────┘
        │                   │                   │
        │           ┌───────▼───────┐           │
        │           │    NOISE      │           │
        │           │     ~35%      │           │
        │           │    Prune      │           │
        │           └───────────────┘           │
        │                                       │
┌───────▼───────────────────────────────────────▼───────┐
│                    ROUTING                            │
│  - value_modality determines consumption mode         │
│  - format determines processing function              │
│  - chain determines integration target                │
└───────────────────────────────────────────────────────┘
```

---

## Triage Steps

### Step 1: Quick Scan (30 seconds)

Without deep reading:
- Who created this?
- What's the title/topic?
- When was it published?
- What format is it?
- What's my gut reaction?

### Step 2: Classification (1 minute)

Assign values for:
- `platform` (obvious from source)
- `format` (obvious from structure)
- `cadence` (is this a regular publication?)

### Step 3: value_modality Assessment (1 minute)

Ask: "Where's the story?"

Use the decision tree:
- Text source? → `text_native`
- Ideas in dialogue? → `dialogue_primary` or `audio_primary`
- Visuals essential? → `visual_primary` or `multimodal_essential`
- Comments matter? → `comments_primary`

### Step 4: Signal Tier Qualification (2 minutes)

**Paradigm criteria** (need 2+):
- [ ] Novel framework or mental model
- [ ] Contradicts/extends Syncrescendent thesis
- [ ] Primary source from field leader
- [ ] Timely for current phase objectives

**Strategic criteria** (need 2+):
- [ ] Synthesizable with other sources
- [ ] Fills known knowledge gap
- [ ] High signal-to-noise ratio
- [ ] Relevant to active project

**Tactical criteria** (any):
- [ ] Useful reference material
- [ ] Confirms existing understanding
- [ ] Good but not urgent

**Noise criteria** (any):
- [ ] Derivative/aggregated content
- [ ] Outdated information
- [ ] Covered better elsewhere
- [ ] Off-topic for current phase

### Step 5: Chain Assignment (30 seconds)

Ask: "Which chain would this most enrich?"

### Step 6: Topic Tagging (1 minute)

Assign 3-7 tags from curated vocabulary.

### Step 7: Record in Frontmatter

Create or update frontmatter with all assignments.

---

## Batch Triage Protocol

For processing large batches (50+ sources):

### Pass 1: Rapid Sort (5 sec/item)
- Scan title, creator, thumbnail
- Quick gut check: Paradigm? Strategic? Tactical? Noise?
- Create four piles

### Pass 2: Paradigm Validation (2 min/item)
- Confirm paradigm assignments
- Demote false positives to strategic

### Pass 3: Classification (1 min/item)
- Complete full eight-dimension classification
- Focus on paradigm + strategic items

### Pass 4: Tactical Decision (15 sec/item)
- Archive immediately or defer processing?
- Most tactical items: archive metadata only

### Pass 5: Noise Pruning (5 sec/item)
- Confirm noise assignments
- Delete or ignore entirely

---

## Triage Questions Cheat Sheet

| Question | Determines |
|----------|------------|
| Where did this come from? | platform |
| What structure does it have? | format |
| How often does this appear? | cadence |
| Where's the signal? | value_modality |
| Is this worth attention? | signal_tier |
| What state is it in? | status |
| Which chain does it serve? | chain |
| What's it about? | topics |

---

## Triage Outputs

After triage, each source has:
1. Complete frontmatter with all dimensions
2. Clear routing (process now, queue, archive, prune)
3. Consumption recommendation (read, listen, watch, skip)

---

## Anti-Patterns

**Don't**:
- Triage without time limit (analysis paralysis)
- Upgrade everything to paradigm (tier inflation)
- Skip value_modality (critical for routing)
- Over-tag (noise in taxonomy)
- Triage one-by-one for large batches (use batch protocol)

---

## Integration with Four Systems

| Triage Result | System | Action |
|---------------|--------|--------|
| paradigm + dialogue_primary | Curation-Push | Full processing, immediate |
| paradigm + visual_primary | On-Demand-Pull | Requires Gemini visual processing |
| strategic + text_native | Automatic-Push | Queue for synthesis window |
| tactical + any | Archive | Metadata only, defer processing |
| noise + any | Prune | Delete or ignore |
```

---

## PHASE C: PROCESSING ROUTING DOCUMENTATION

### C1: Create PROCESSING_ROUTING.md

**Create file**: `orchestration/state/PROCESSING_ROUTING.md`

**Contents to include**:

```markdown
# Processing Routing
## Function Selection Based on Source Characteristics

**Version**: 1.0.0
**Created**: 2026-01-01
**Authority**: Oracle9

---

## Routing Logic

Processing function selection depends on:
1. **platform** — Determines native processor (Gemini vs Claude)
2. **format** — Determines structural handling
3. **value_modality** — Determines compression approach

---

## Primary Routing Table

| Platform | Format | Function | Processor |
|----------|--------|----------|-----------|
| youtube | interview | transcribe_interview | Gemini |
| youtube | panel | transcribe_panel | Gemini |
| youtube | solo_presentation | transcribe_youtube | Gemini |
| youtube | tutorial | transcribe_youtube | Gemini |
| youtube | lecture | transcribe_youtube | Gemini |
| podcast | interview | transcribe_interview | Gemini |
| podcast | panel | transcribe_panel | Gemini |
| podcast | solo | transcribe_youtube | Gemini |
| substack | article | readize | Claude |
| substack | essay | readize | Claude |
| newsletter | article | readize | Claude |
| arxiv | paper | (academic_process) | Claude |
| paper | paper | (academic_process) | Claude |
| book | chapter | (chapter_process) | Claude |
| x | thread | (thread_process) | Claude |
| reddit | post | (thread_process) | Claude |
| film | — | (defer to Modal 2) | — |

**Note**: Functions in parentheses are planned but not yet implemented.

---

## value_modality Modifiers

| value_modality | Additional Processing |
|----------------|----------------------|
| dialogue_primary | Standard processing sufficient |
| audio_primary | Note: consider audio consumption |
| visual_primary | Require Gemini visual summary |
| comments_primary | Capture discourse separately |
| multimodal_essential | Defer to Modal 2 / partial only |
| text_native | Direct processing |

---

## Processor Allocation

### Gemini Handles:
- All YouTube processing (native platform)
- All podcast/audio processing (audio transcription)
- Visual summary generation for visual_primary sources
- Speaker diarization for panels

### Claude Handles:
- All text-native sources (articles, papers, threads)
- Synthesis and integration
- Routing decisions
- Infrastructure and orchestration

### Why This Split?

1. **Native capability**: Gemini can directly process YouTube URLs
2. **Multi-modal**: Gemini can see video frames, read slides
3. **Cost efficiency**: Gemini subscription is flat-rate for native content
4. **Quality**: Claude excels at text synthesis and integration

---

## Function Specifications

### transcribe_youtube
**Input**: YouTube video URL or transcript
**Output**: Clean essay with ads/previews removed
**Location**: `OPERATIONAL/functions/transcribe_youtube.xml`

### transcribe_interview
**Input**: Interview transcript
**Output**: Multi-voice narrative, commercials removed
**Location**: `OPERATIONAL/functions/transcribe_interview.xml`

### transcribe_panel
**Input**: Panel discussion transcript
**Output**: Thematic extraction with speaker attribution
**Location**: `OPERATIONAL/functions/transcribe_panel.xml`

### readize
**Input**: Any text
**Output**: Read-optimized crystalline prose
**Location**: `OPERATIONAL/functions/readize.xml`

### integrate
**Input**: Multiple sources
**Output**: Unified synthesis
**Location**: `OPERATIONAL/functions/integrate.xml`

---

## Processing Workflow

```
1. Source arrives in SOURCES/raw/
        ↓
2. Triage assigns dimensions
        ↓
3. Routing selects function based on:
   - platform → processor
   - format → function
   - value_modality → modifiers
        ↓
4. Execute function
        ↓
5. Output to SOURCES/processed/
        ↓
6. Update status: processed
        ↓
7. Queue for integration (if paradigm/strategic)
```

---

## Edge Cases

### YouTube with essential visuals
- Platform: youtube
- value_modality: visual_primary
- **Action**: Standard transcription + Gemini visual summary

### Podcast that's actually a video
- Platform: podcast (original format)
- **Action**: Process as audio-primary, note video version exists

### X thread with embedded YouTube
- Platform: x (primary)
- **Action**: Process thread as primary, note video separately

### Academic paper with code
- Platform: arxiv
- **Action**: Process paper, code in separate artifact

---

## Future Functions (Planned)

| Function | For | Status |
|----------|-----|--------|
| academic_process | ArXiv, papers | Planned |
| chapter_process | Books | Planned |
| thread_process | X, Reddit | Planned |
| visual_summary | Visual-primary | Planned (Gemini) |
```

---

## PHASE D: FOUR-SYSTEM DOCUMENTATION

### D1: Create FOUR_SYSTEMS.md

**Create file**: `orchestration/state/FOUR_SYSTEMS.md`

**Contents to include**:

```markdown
# Four-System Intelligence Architecture
## Operational Modes of the Intelligence Apparatus

**Version**: 1.0.0
**Created**: 2026-01-01
**Authority**: Oracle9
**Source**: Gemini conversation (2025-06-17)

---

## Overview

The intelligence apparatus operates in **four modes**, not four pipelines.

These are complementary operational patterns, not separate systems.

---

## System 1: Automatic-Push (Scheduled Monitoring)

### Purpose
Proactively monitor trusted, high-cadence sources and deliver synthesis.

### Characteristics
- **Trigger**: Schedule (daily, weekly)
- **Sources**: Known high-signal, periodic publications
- **Processing**: Automated transcription + synthesis
- **Output**: Daily/weekly intelligence brief

### Example Workflow
```
6:00 AM: Scheduled trigger
  ↓
Poll Feedly RSS for new items from:
  - Bloomberg Technology
  - No Priors podcast
  - Lex Fridman new episodes
  ↓
Download and process new items
  ↓
Generate "State of the Union" brief
  ↓
Deliver to inbox / review queue
```

### IIC Mapping
Maps to **Daily Intelligence Brief** in Acumen IIC architecture.

---

## System 2: Curation-Push (Serendipitous Discovery)

### Purpose
Frictionless save-to-queue from mobile browsing, high-fidelity processing.

### Characteristics
- **Trigger**: User save action (Watch Later, bookmark, etc.)
- **Sources**: Serendipitous finds during browsing
- **Processing**: Multi-modal transcription when queued item processed
- **Output**: Clean source in SOURCES/processed/

### Example Workflow
```
User browsing on phone
  ↓
Sees interesting YouTube video
  ↓
Saves to Watch Later playlist
  ↓
(Later) Agent polls Watch Later
  ↓
Processes via Gemini
  ↓
Deposits in SOURCES/processed/
  ↓
Awaits triage and integration
```

### IIC Mapping
Maps to **Serendipitous Encounters** stream in Acumen IIC.

---

## System 3: On-Demand-Pull (Active Research)

### Purpose
Query-driven deep dives on specific topics.

### Characteristics
- **Trigger**: User research query
- **Sources**: Trans-platform search based on query
- **Processing**: Full synthesis across sources
- **Output**: Research packet / synthesis document

### Example Workflow
```
User: "What's the latest on multimodal reasoning?"
  ↓
Search across:
  - YouTube (relevant videos)
  - ArXiv (recent papers)
  - X (discourse threads)
  ↓
Process and synthesize
  ↓
Deliver research packet
```

### IIC Mapping
Maps to **Active Research** mode in Coherence IIC.

---

## System 4: Triage & Qualification (Gatekeeper)

### Purpose
Pre-filter answering: "Is this worth my attention?"

### Characteristics
- **Trigger**: Any source entering the system
- **Sources**: All sources before processing
- **Processing**: Quick classification + tier assignment
- **Output**: Routing decision

### Critical Questions
- Is the dialogue the story? → Read transcript
- Are the comments the story? → Read discourse
- Are the visuals the story? → Watch video
- Is the delivery the story? → Listen to audio

### Example Workflow
```
New source arrives
  ↓
Quick scan (30 sec)
  ↓
Assign signal_tier:
  - paradigm → full processing
  - strategic → queue processing
  - tactical → archive
  - noise → prune
  ↓
Assign value_modality:
  - dialogue_primary → transcript sufficient
  - visual_primary → watch recommended
  ↓
Route accordingly
```

### IIC Mapping
Maps to **Priority Band** system in Acumen IIC.

---

## How Systems Interact

```
┌─────────────────────────────────────────────────────────────┐
│                    INCOMING SOURCES                         │
└──────────────────────────┬──────────────────────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
   ┌─────────┐       ┌─────────┐       ┌─────────┐
   │ System  │       │ System  │       │ System  │
   │    1    │       │    2    │       │    3    │
   │ Auto-   │       │ Curation│       │ On-     │
   │ Push    │       │  Push   │       │ Demand  │
   └────┬────┘       └────┬────┘       └────┬────┘
        │                 │                 │
        └────────────────┬┘─────────────────┘
                         │
                         ▼
                  ┌─────────────┐
                  │   System 4   │
                  │   Triage &   │
                  │ Qualification│
                  └──────┬──────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
   ┌─────────┐     ┌─────────┐     ┌─────────┐
   │ PARADIGM│     │STRATEGIC│     │TACTICAL │
   │ Process │     │  Queue  │     │ Archive │
   └─────────┘     └─────────┘     └─────────┘
```

---

## MVP Implementation

For Oracle9 MVP:

| System | Implementation | Status |
|--------|----------------|--------|
| System 1 | Manual batch processing | Manual |
| System 2 | transcripts.zip = accumulated queue | Ready |
| System 3 | On-demand triage + processing | Manual |
| System 4 | Triage protocol documented | Ready |

Future automation:
- Gemini RPA for YouTube processing
- n8n for RSS/Feedly polling
- Scheduled triggers for daily brief

---

## Holistic Not Componential

**Principal's instruction**: 
> "This insight should be factored in holistically, not componentially."

These four systems are **modes of operation**, not separate pipelines.

The same source might:
- Enter via System 2 (saved during browsing)
- Pass through System 4 (triage)
- Get enhanced via System 3 (research query adds context)
- Inform System 1 (becomes part of monitored feeds)

Think of four lenses on the same apparatus, not four machines.
```

---

## PHASE E: VERIFICATION

### E1: Document Checklist

Verify all documents created:

- [ ] `orchestration/state/ORACLE9_CONTEXT.md`
- [ ] `orchestration/state/SOURCES_SCHEMA.md`
- [ ] `orchestration/state/TRIAGE_PROTOCOL.md`
- [ ] `orchestration/state/PROCESSING_ROUTING.md`
- [ ] `orchestration/state/FOUR_SYSTEMS.md`

### E2: Cross-Reference Verification

Verify documents reference each other correctly:
- ORACLE9_CONTEXT references all four protocol documents
- TRIAGE_PROTOCOL references SOURCES_SCHEMA dimensions
- PROCESSING_ROUTING references function locations
- FOUR_SYSTEMS references IIC mappings

### E3: Commit to Repository

```bash
git add -A
git commit -m "DIRECTIVE-032B: Intelligence apparatus protocol documentation

- Created SOURCES_SCHEMA.md (eight-dimension specification)
- Created TRIAGE_PROTOCOL.md (progressive qualification funnel)
- Created PROCESSING_ROUTING.md (function selection logic)
- Created FOUR_SYSTEMS.md (operational modes documentation)
- Cross-referenced with ORACLE9_CONTEXT.md

Oracle9 Phase: Protocol Documentation Stream"
```

---

## EXECUTION LOG REQUIREMENTS

Save to: `orchestration/execution_logs/EXECUTION_LOG-2026-01-01-032B.md`

**Template provided in DIRECTIVE-032A applies.**

---

## SUCCESS CRITERIA

- [ ] ORACLE9_CONTEXT.md complete and installed
- [ ] SOURCES_SCHEMA.md with full eight dimensions
- [ ] TRIAGE_PROTOCOL.md with decision trees
- [ ] PROCESSING_ROUTING.md with function mapping
- [ ] FOUR_SYSTEMS.md with operational modes
- [ ] All documents cross-referenced
- [ ] Git commit with descriptive message
- [ ] Execution log saved with evidence

---

## COORDINATION WITH DIRECTIVE-032A

**Receives from 032A**:
- SOURCES/ directory structure exists
- Raw archive extracted
- Frontmatter template available

**Provides to 032A and future directives**:
- Complete schema documentation
- Triage decision framework
- Processing routing logic
- Four-system operational model

---

*This directive archived to orchestration/directives/ upon execution.*
