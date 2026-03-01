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

## Cross-References

- **Triage Protocol**: See `TRIAGE_PROTOCOL.md` for qualification procedures
- **Processing Routing**: See `PROCESSING_ROUTING.md` for function selection
- **Four Systems**: See `FOUR_SYSTEMS.md` for operational modes
- **ORACLE9 Context**: See `ORACLE9_CONTEXT_v2.md` for architectural decisions

---

## Schema Evolution

This schema will evolve through use. Additions:
1. New platform values as sources expand
2. New format values for edge cases
3. New topic vocabulary as domains emerge
4. Refinements based on processing experience

Changes require Oracle approval and 18-lens evaluation.
