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

Use the decision tree from `SOURCES_SCHEMA.md`:
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

| Chain | Focus |
|-------|-------|
| intelligence | AI/ML, agentic systems |
| information | Sensing, platforms, IIC |
| insight | Synthesis, meaning-making |
| expertise | Business, operations |
| knowledge | Learning, curriculum |
| wisdom | Transcendence, meta-cognition |

### Step 6: Topic Tagging (1 minute)

Assign 3-7 tags from curated vocabulary (see `SOURCES_SCHEMA.md`).

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

## Consumption Routing Based on value_modality

| value_modality | Recommendation | Processor |
|----------------|----------------|-----------|
| dialogue_primary | Read transcript | Claude |
| audio_primary | Listen to audio | Human |
| visual_primary | Watch video OR request visual summary | Gemini |
| comments_primary | Read discourse thread | Claude |
| multimodal_essential | Full engagement required | Modal 2 |
| text_native | Direct processing | Claude |

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

See `FOUR_SYSTEMS.md` for full operational mode documentation.

---

## Cross-References

- **Sources Schema**: See `SOURCES_SCHEMA.md` for dimension definitions
- **Processing Routing**: See `PROCESSING_ROUTING.md` for function selection
- **Four Systems**: See `FOUR_SYSTEMS.md` for operational modes
- **Backlog**: See `DYN-BACKLOG.md` for project status
