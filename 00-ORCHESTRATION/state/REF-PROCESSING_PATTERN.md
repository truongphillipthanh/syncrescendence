# Source Processing Pattern
## Repeatable Methodology for Source-to-Synthesis Cycle

**Version**: 1.0.0
**Created**: 2026-01-01
**Authority**: Oracle9
**Demonstrated**: DIRECTIVE-033B

---

## Overview

This pattern transforms raw sources into CANON-integrated insights through a complete processing cycle.

---

## The Pattern

```
┌─────────────────────────────────────────────────────────────┐
│                    RAW SOURCE                               │
│           (SOURCES/raw/.../filename.md)                     │
└──────────────────────────┬──────────────────────────────────┘
                           │
                    ┌──────▼──────┐
                    │   TRIAGE    │
                    │ (if not     │
                    │  already    │
                    │  triaged)   │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  PROCESS    │
                    │ - Apply     │
                    │   function  │
                    │ - Add       │
                    │   frontmatter│
                    │ - Extract   │
                    │   insights  │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  INTEGRATE  │
                    │ - Identify  │
                    │   CANON     │
                    │   targets   │
                    │ - Add       │
                    │   citations │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │   UPDATE    │
                    │ - sources.csv│
                    │ - frontmatter│
                    │   status    │
                    └──────┬──────┘
                           │
┌─────────────────────────▼───────────────────────────────────┐
│                  INTEGRATED SOURCE                          │
│         (SOURCES/processed/SOURCE-YYYYMMDD-xxx.md)          │
└─────────────────────────────────────────────────────────────┘
```

---

## Step 1: Triage (if needed)

If source is not already triaged in sources.csv:

1. Apply TRIAGE_PROTOCOL.md
2. Assign signal_tier
3. If paradigm or strategic: proceed to processing
4. If tactical: archive metadata only
5. If noise: skip or prune

---

## Step 2: Process

### 2.1 Select Function

Based on PROCESSING_ROUTING.md:

| Platform + Format | Function |
|-------------------|----------|
| youtube + interview | transcribe_interview |
| youtube + panel | transcribe_panel |
| youtube + solo_presentation | transcribe_youtube |
| x + thread | text_native (minimal processing) |
| substack + article | readize |

### 2.2 Create Processed File

Output file naming: `SOURCE-YYYYMMDD-platform-format-creator-guest.md`

Location: `SOURCES/processed/`

### 2.3 Complete Frontmatter

Required fields:
```yaml
---
id: SOURCE-YYYYMMDD-NNN
platform: youtube|x|substack|arxiv|...
format: interview|panel|solo_presentation|thread|...
cadence: daily|weekly|periodic|arrhythmic|evergreen
value_modality: dialogue_primary|audio_primary|visual_primary|text_native|...
signal_tier: paradigm|strategic|tactical|noise
status: processed
chain: intelligence|information|insight|expertise|knowledge|wisdom
topics: [list, of, tags]
creator: Creator Name
guest: Guest Name (if applicable)
title: "Full Title"
url: https://...
date_published: YYYY-MM-DD
date_processed: YYYY-MM-DD
date_integrated: null (until integrated)
processing_function: transcribe_interview|readize|...
integrated_into: []
synopsis: |
  2-3 sentence summary of source and its value.
key_insights:
  - "Quotable insight 1"
  - "Quotable insight 2"
  - ...
visual_notes: |
  Assessment of value_modality. What's lost in transcript?
---
```

### 2.4 Extract Key Insights

For each source:
- **Synopsis**: 2-3 sentences capturing who, what, why it matters
- **Key Insights**: 5-10 quotable points, direct quotes when paradigm-shifting
- **Integration Candidates**: Which CANON documents could benefit

---

## Step 3: Integrate

### 3.1 Identify Target CANON Documents

Match source to CANON by:
- Chain alignment (e.g., intelligence chain sources → CANON-30xxx)
- Topic relevance (e.g., bitter_lesson → CANON with 18 lenses)
- Validation/enhancement potential

### 3.2 Integration Method

| Method | When to Use |
|--------|-------------|
| **CITATION** | Add source reference, paraphrase insight |
| **ENHANCEMENT** | Expand existing section with new detail |
| **VALIDATION** | Confirm existing thesis with external evidence |
| **CHALLENGE** | Note tension/contradiction for resolution |

### 3.3 Add Integration

In target CANON document:
1. Find relevant section
2. Add insight with SOURCE-YYYYMMDD-NNN reference
3. Update CANON version history if substantive

---

## Step 4: Update Records

### 4.1 Update sources.csv

Change:
- `status`: triaged → integrated
- `date_processed`: YYYY-MM-DD
- `date_integrated`: YYYY-MM-DD
- `integrated_into`: [[CANON-00004-EVOLUTION-cosmos]],[[CANON-30400-AGENTIC_ARCHITECTURE-comet-INTELLIGENCE]],...
- `notes`: Brief processing note

### 4.2 Update Source Frontmatter

Change:
- `status`: processed → integrated
- `date_integrated`: YYYY-MM-DD
- `integrated_into`: [[[CANON-00004-EVOLUTION-cosmos]], [[CANON-30400-AGENTIC_ARCHITECTURE-comet-INTELLIGENCE]]]

---

## Quality Checklist

Before marking complete:

- [ ] Processed file exists in SOURCES/processed/
- [ ] Frontmatter has all required fields
- [ ] Synopsis captures essence (2-3 sentences)
- [ ] Key insights are quotable (5-10 points)
- [ ] Integration adds value (not redundant)
- [ ] Source reference included in CANON
- [ ] sources.csv updated
- [ ] Status changed to 'integrated'

---

## Example: Complete Cycle

**Source**: Dwarkesh Patel - Richard Sutton interview (2025-09-26)

**Step 1**: Already triaged as paradigm by DIRECTIVE-033A

**Step 2**: Process
- Apply transcribe_interview (already clean, add frontmatter)
- Create `SOURCES/processed/SOURCE-20250926-youtube-interview-dwarkesh_patel-richard_sutton.md`
- Extract synopsis: "Richard Sutton challenges LLM paradigm, argues for experiential learning..."
- Extract key insights: 8 quotable points on Bitter Lesson, world models, succession

**Step 3**: Integrate
- Target 1: CANON-00004-EVOLUTION (Bitter Lesson validation)
- Target 2: CANON-30400-AGENTIC_ARCHITECTURE (RL limitations, agent timelines)
- Method: VALIDATION for Bitter Lesson, ENHANCEMENT for agent architecture

**Step 4**: Update
- sources.csv: SOURCE-20250926-057 → status=integrated, integrated_into=[[CANON-00004-EVOLUTION-cosmos]],[[CANON-30400-AGENTIC_ARCHITECTURE-comet-INTELLIGENCE]]
- Frontmatter: status=integrated, integrated_into=[[[CANON-00004-EVOLUTION-cosmos]], [[CANON-30400-AGENTIC_ARCHITECTURE-comet-INTELLIGENCE]]]

---

## Anti-Patterns

**Don't**:
- Process without triage (wasted effort on noise)
- Skip frontmatter (loses metadata)
- Add redundant integrations (CANON bloat)
- Forget to update sources.csv (tracking lost)
- Mark integrated without actual CANON changes (false records)

---

## Batch Processing

For multiple paradigm sources:

1. Process all sources first (create processed/ files)
2. Then integrate in batches by target CANON document
3. Update sources.csv in single pass at end
4. Commit with descriptive message listing all sources and integrations

---

## Cross-References

- **SOURCES_SCHEMA.md**: Full dimension specifications
- **TRIAGE_PROTOCOL.md**: How to assign signal_tier
- **PROCESSING_ROUTING.md**: Which function to apply
- **FOUR_SYSTEMS.md**: Which operational mode applies
