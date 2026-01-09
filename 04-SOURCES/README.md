# SOURCES Directory

External intelligence input layer for the Syncrescendent apparatus.

## Pipeline Stages

```
STAGE 1: raw/*.txt     → Raw transcripts (copy-paste, auto-generated)
STAGE 2: raw/*.md      → Formatted (transcribe function applied, content structured)
STAGE 3: processed/    → Qualified (SOURCE- prefix, frontmatter, insights extracted)
STAGE 4: integrated    → CANON absorption confirmed (sources.csv status='integrated')
```

### Stage 1: Ingestion (raw/*.txt)
- Raw transcript files from various sources
- Naming: any format (will be normalized in later stages)
- Content: unformatted, direct captures

### Stage 2: Formatted (raw/*.md)
- `transcribe_[format].xml` function applied
- Proper markdown structure
- May still need SOURCE- prefix normalization
- Ready for qualification assessment

### Stage 3: Qualified (processed/)
- Full `SOURCE-YYYYMMDD-format-venue-subject.md` naming
- Complete frontmatter per FRONTMATTER_TEMPLATE.md
- Key insights extracted
- Ready for CANON integration

### Stage 4: Integrated
- `sources.csv`: status='integrated'
- Insights absorbed into relevant CANON documents
- Source file retained in processed/ for reference

## Directory Structure

```
03-SOURCES/
├── raw/                    # Stages 1-2 (txt = Stage 1, md = Stage 2)
├── processed/              # Stage 3 (integration-ready)
├── sources.csv             # Master tracking file
├── filename_mapping.csv    # Rename history
├── index.md                # Master manifest
├── FRONTMATTER_TEMPLATE.md # Processing template
└── README.md               # This file
```

## Naming Convention

```
SOURCE-{YYYYMMDD}-{format}-{venue}-{subject}.md
```

Examples:
- `SOURCE-20250926-youtube-interview-dwarkesh_patel-richard_sutton.md`
- `SOURCE-20251001-x-thread-andrej_karpathy-sutton_response.md`

## Relationship to Other Tiers

- **SOURCES** = External intelligence INPUT (not authored by Principal)
- **CANON** = Authored synthesis OUTPUT
- **QUEUE** = Pending work items
- **ARCHIVE** = Full research corpora (pre-distillation)

## Processing Functions

See `01-OPERATIONAL/functions/` for:
- `transcribe_youtube.xml` - YouTube video processing
- `transcribe_interview.xml` - Interview format processing
- `transcribe_panel.xml` - Panel discussion processing
- `readize.xml` - Article/document processing

## See Also

- `FRONTMATTER_TEMPLATE.md` — Field definitions and template
- `sources.csv` — Master tracking spreadsheet
- `index.md` — Master manifest
