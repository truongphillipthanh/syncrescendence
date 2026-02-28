# Source Frontmatter Template

Copy this template when creating processed sources.

```yaml
---
id: SOURCE-{YYYYMMDD}-{NNN}
platform: youtube | podcast | substack | arxiv | x | book | course | newsletter
format: interview | panel | solo_presentation | paper | thread | article | lecture | essay
cadence: daily | weekly | periodic | arrhythmic | evergreen
value_modality: dialogue_primary | visual_primary | audio_primary | comments_primary | multimodal_essential | text_native
signal_tier: paradigm | strategic | tactical | noise
status: raw | triaged | processed | integrated | archived
chain: intelligence | information | insight | expertise | knowledge | wisdom
topics: [tag1, tag2, tag3]
creator: Creator Name
guest: Guest Name (if applicable)
title: "Full Title"
url: https://...
date_published: YYYY-MM-DD
date_processed: YYYY-MM-DD
date_integrated: null | YYYY-MM-DD
processing_function: transcribe_youtube | transcribe_interview | transcribe_panel | readize | custom
integrated_into: [] | [CANON-XXXXX, CANON-YYYYY]
synopsis: |
  2-3 sentence summary of content and significance.
key_insights:
  - Insight 1
  - Insight 2
  - Insight 3
visual_notes: |
  Assessment of what transcript captures vs. misses.
  Note if visual layer is essential (slides, demos, etc.)
---
```

## Field Definitions

### platform
Where the source originated. Determines native processing pathway.

### format
Structural type. Determines which processing function applies.

### cadence
Temporal pattern. From Gemini conversation's periodic vs. arrhythmic distinction.

### value_modality
**Critical field** — encodes what transcript captures vs. loses:
- `dialogue_primary`: Transcript captures 95%+. Standard interviews.
- `visual_primary`: Transcript captures ~40%. Slides/demos essential.
- `audio_primary`: Transcript captures ~70%. Delivery matters.
- `comments_primary`: Comments ARE the story. X threads, Reddit.
- `multimodal_essential`: Cannot reduce to text. Film, visual art.
- `text_native`: Already optimal format. Articles, papers.

### signal_tier
Triage result. Progressive qualification funnel:
- `paradigm`: Must engage deeply. Potential framework shift. ~5% of sources.
- `strategic`: High value, queue for synthesis. ~20% of sources.
- `tactical`: Useful reference, archive. ~40% of sources.
- `noise`: Low signal, prune. ~35% of sources.

### status
Processing state machine:
- `raw`: Unprocessed source material
- `triaged`: Classified, qualified, routed
- `processed`: Transcript cleaned, insights extracted
- `integrated`: Contributed to CANON document(s)
- `archived`: Processed but not integrated, kept for reference

### chain
Which Syncrescendent developmental chain this source primarily serves.

### processing_function
Which function from OPERATIONAL/functions/ was used.
