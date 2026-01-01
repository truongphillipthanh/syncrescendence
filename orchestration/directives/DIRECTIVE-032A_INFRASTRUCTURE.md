# DIRECTIVE-032A: INTELLIGENCE APPARATUS INFRASTRUCTURE
## Stream A: Directory Structure, Archive Extraction, Schema Installation
**Issued**: 2026-01-01
**Authority**: Oracle9 under Principal direction
**Classification**: CRITICAL — Intelligence Apparatus Foundation
**Execution**: Claude Code (Desktop)
**Parallel Stream**: Oracle/Desktop handles protocol documentation (DIRECTIVE-032B)

---

## DECISION CONTEXT

### Principal's Mandate

> "Before we jump the gun and ingest, let's mise en place an MVP intelligence apparatus first, knowing that the ingestion of this new material will only strengthen our thesis."

> "I bet this is perfect fodder for the flat hierarchy, alias, frontmatter/metadata, filenaming approach, as I mentioned to Oracle 8."

> "This needs to generalize. I do believe there needs to be an architecture that would be the agentified spiritual successor to DEVONThink/Zotero."

### Oracle's Interpretation

Oracle9's mission is activating the Information Chain as functional apparatus. Before processing 468 transcripts, infrastructure must exist:
1. SOURCES/ directory structure following CANON/ pattern
2. Archive extracted to raw/ staging area
3. Schema documentation installed
4. Orphan files at repository root triaged
5. Skeletal aliases created for human navigation

This directive establishes the **physical substrate** for the intelligence apparatus.

### Alternatives Considered

1. **Process transcripts directly into CANON** — Rejected: Sources are INPUT, not OUTPUT
2. **Create complex folder hierarchy** — Rejected: Violates flat principle
3. **Defer infrastructure, triage manually** — Rejected: Principal mandated "mise en place"
4. **Flat + naming + metadata + aliases** — CHOSEN: Proven pattern from CANON/

### Rationale (18-Lens Evaluation)

| Lens | Score | Notes |
|------|-------|-------|
| Syncrescendent Route | ✓ | Sources feed CANON recursively |
| Bitter Lesson | ✓ | Schema scales to any source type |
| Antifragile | ✓ | New source types strengthen taxonomy |
| Meet the Moment | ✓ | Infrastructure before processing |
| Steelman/Redteam | ✓ | Pattern proven with CANON/ |
| Personal Idiosyncrasies | ✓ | Holistic architecture before detail |
| Potency w/o Resolution Loss | ✓ | Full metadata, no compression |
| Elegance + Dev Happiness | ✓ | Predictable patterns |
| Agentify + Human-Navigable | ✓ | 2 decisions to any source |
| First Principles | ✓ | External intelligence IS Information Chain input |
| Systems Thinking | ✓ | SOURCES → QUEUE → CANON flow |
| Industrial Engineering | ✓ | Pipeline before throughput |
| Complexity Theory | ✓ | Essential structure only |
| Permaculture | ✓ | Self-maintaining pattern |
| Design Thinking | ✓ | Human navigation via aliases |
| Agile | ✓ | Shippable increment |
| Lean | ✓ | No premature processing |
| Six Sigma | ✓ | Consistent structure reduces defects |

**Score**: 18/18 — Approved

### Implicit Agreements

1. **SOURCES/ is INPUT tier** — Not CANON (authored synthesis) or QUEUE (pending work)
2. **Flat + naming + metadata + aliases** — Three-pillar pattern from CANON/
3. **Raw vs processed** — Two states, one directory each
4. **Aliases skeletal now** — Expand as schema stabilizes
5. **Orphans must be filed** — Repository root should be clean

---

## MANDATORY FIRST STEP: COMPREHENSIVE SURVEY

**Before ANY execution, run these commands and document output:**

```bash
# Survey repository root for orphans
ls -la | grep -v "^d" | grep -v ".git"

# Check if SOURCES/ already exists
ls -la SOURCES/ 2>/dev/null || echo "SOURCES/ does not exist"

# Check current aliases structure
ls -la aliases/ 2>/dev/null || echo "aliases/ does not exist"

# Survey orchestration state
ls orchestration/state/

# Count files in transcript archive (if accessible)
unzip -l /path/to/transcripts.zip | grep -c "\.md$\|\.txt$"

# Check for existing source-like files
find . -name "SOURCE-*.md" 2>/dev/null | head -10
```

**Document findings before proceeding.**

---

## PHASE A: ORPHAN TRIAGE (5 minutes)

### A1: Identify Orphans at Repository Root

Based on Oracle8 handoff, expected orphans:
- `ORACLE_CONTEXT.md`
- `ORACLE_CONTEXT_v2.md`
- `ORACLE8_STATUS_REPORT.md`

### A2: File Orphans

```bash
# Move Oracle state files to orchestration/state/
mv ORACLE_CONTEXT.md orchestration/state/
mv ORACLE_CONTEXT_v2.md orchestration/state/
mv ORACLE8_STATUS_REPORT.md orchestration/state/

# Move Gemini conversation to scaffolding (working document)
# If present at root:
mv Gemini_conversation.md orchestration/scaffolding/ 2>/dev/null

# Verify root is clean
ls | grep -v "^CANON$\|^OPERATIONAL$\|^QUEUE$\|^ARCHIVE$\|^EXEMPLA$\|^aliases$\|^orchestration$\|^SOURCES$\|^README\|^\.git"
```

### A3: Verification

```bash
# Root should contain only:
# - CANON/, OPERATIONAL/, QUEUE/, ARCHIVE/, EXEMPLA/, aliases/, orchestration/, SOURCES/
# - README.md, .gitignore, .obsidian/, .git/
ls -la | head -20
```

---

## PHASE B: SOURCES/ DIRECTORY CREATION (10 minutes)

### B1: Create Directory Structure

```bash
# Create SOURCES/ with subdirectories
mkdir -p SOURCES/raw
mkdir -p SOURCES/processed

# Create README.md
cat > SOURCES/README.md << 'EOF'
# SOURCES Directory

External intelligence input layer for the Syncrescendent apparatus.

## Structure

```
SOURCES/
├── raw/           # Unprocessed source files
├── processed/     # Clean, frontmatter-tagged sources (FLAT)
├── index.md       # Master manifest
└── README.md      # This file
```

## Relationship to Other Tiers

- **SOURCES** = External intelligence INPUT (not authored by Principal)
- **CANON** = Authored synthesis OUTPUT
- **QUEUE** = Pending work items

## Naming Convention

```
SOURCE-{YYYYMMDD}-{platform}-{format}-{creator}-{title_slug}.md
```

## Processing Flow

```
raw/ → triage → processed/ → integration → CANON/
```

## See Also

- `SOURCES/index.md` — Master manifest
- `orchestration/state/ORACLE9_CONTEXT.md` — Full schema documentation
EOF

# Create index.md template
cat > SOURCES/index.md << 'EOF'
# SOURCES Index

Master manifest of external intelligence sources.

**Last Updated**: 2026-01-01
**Total Sources**: 0 processed, ~468 raw (pending triage)

---

## By Signal Tier

### Paradigm (Must Engage)
<!-- Sources with signal_tier: paradigm -->

### Strategic (Queue for Synthesis)
<!-- Sources with signal_tier: strategic -->

### Tactical (Archive Reference)
<!-- Sources with signal_tier: tactical -->

---

## By Platform

### YouTube
<!-- platform: youtube -->

### Podcast
<!-- platform: podcast -->

### Substack
<!-- platform: substack -->

### ArXiv
<!-- platform: arxiv -->

### X/Twitter
<!-- platform: x -->

---

## By Chain

### Intelligence
<!-- chain: intelligence -->

### Information
<!-- chain: information -->

### Insight
<!-- chain: insight -->

---

## Processing Queue

| Source | Status | Assigned To | Notes |
|--------|--------|-------------|-------|
| (pending triage) | raw | — | — |

---

## Integration Log

| Source | Integrated Into | Date | Notes |
|--------|-----------------|------|-------|
| — | — | — | — |

EOF

# Verify creation
ls -la SOURCES/
```

---

## PHASE C: ARCHIVE EXTRACTION (15 minutes)

### C1: Locate and Extract Archive

**Note**: The archive path depends on how Principal provides it. Adjust as needed.

```bash
# If archive is at repository root or known location:
unzip transcripts.zip -d SOURCES/raw/

# Or if provided via upload:
# cp /path/to/transcripts.zip SOURCES/
# cd SOURCES/ && unzip transcripts.zip -d raw/

# Remove macOS artifacts
find SOURCES/raw -name "__MACOSX" -type d -exec rm -rf {} + 2>/dev/null
find SOURCES/raw -name ".DS_Store" -delete 2>/dev/null
find SOURCES/raw -name "._*" -delete 2>/dev/null
```

### C2: Survey Extracted Contents

```bash
# Count files by extension
find SOURCES/raw -name "*.md" | wc -l
find SOURCES/raw -name "*.txt" | wc -l

# List top-level structure
ls -la SOURCES/raw/transcripts/

# List subdirectories
find SOURCES/raw -type d | head -20

# Sample file names
find SOURCES/raw -name "*.md" | head -20
```

### C3: Document Archive Structure

Create inventory in execution log showing:
- Total file count
- Directory structure
- File naming patterns observed
- Any anomalies

---

## PHASE D: SKELETAL ALIASES (10 minutes)

### D1: Create Alias Structure

```bash
# Create aliases/sources/ structure
mkdir -p aliases/sources/by-platform/youtube
mkdir -p aliases/sources/by-platform/podcast
mkdir -p aliases/sources/by-platform/substack
mkdir -p aliases/sources/by-platform/arxiv
mkdir -p aliases/sources/by-platform/x

mkdir -p aliases/sources/by-tier/paradigm
mkdir -p aliases/sources/by-tier/strategic
mkdir -p aliases/sources/by-tier/tactical

mkdir -p aliases/sources/by-chain/intelligence
mkdir -p aliases/sources/by-chain/information
mkdir -p aliases/sources/by-chain/insight
mkdir -p aliases/sources/by-chain/expertise
mkdir -p aliases/sources/by-chain/knowledge
mkdir -p aliases/sources/by-chain/wisdom

# Create README in aliases/sources/
cat > aliases/sources/README.md << 'EOF'
# Source Aliases

Symlink navigation layer for SOURCES/.

## Structure

```
aliases/sources/
├── by-platform/    # youtube, podcast, substack, arxiv, x
├── by-tier/        # paradigm, strategic, tactical
└── by-chain/       # intelligence, information, insight, etc.
```

## Usage

These directories contain symlinks to files in `SOURCES/processed/`.
Symlinks are created during processing based on frontmatter metadata.

## Creating Symlinks

```bash
# Example: Link a source to platform alias
ln -s ../../../SOURCES/processed/SOURCE-20251017-youtube-interview-dwarkesh_patel-andrej_karpathy.md aliases/sources/by-platform/youtube/

# Example: Link same source to tier alias
ln -s ../../../SOURCES/processed/SOURCE-20251017-youtube-interview-dwarkesh_patel-andrej_karpathy.md aliases/sources/by-tier/paradigm/
```

## Note

Aliases are populated incrementally as sources are processed.
Initial structure is skeletal; expands through use.
EOF

# Verify structure
find aliases/sources -type d
```

---

## PHASE E: SCHEMA DOCUMENTATION INSTALLATION (5 minutes)

### E1: Install Oracle9 Context

```bash
# Copy ORACLE9_CONTEXT.md to orchestration/state/
# (This file is provided separately by Oracle)
cp ORACLE9_CONTEXT.md orchestration/state/

# Verify
ls orchestration/state/ | grep ORACLE
```

### E2: Create Frontmatter Template

```bash
cat > SOURCES/FRONTMATTER_TEMPLATE.md << 'EOF'
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
EOF

# Verify
ls SOURCES/ | grep TEMPLATE
```

---

## PHASE F: VERIFICATION (10 minutes)

### F1: Structure Verification

```bash
# Verify SOURCES/ structure
echo "=== SOURCES/ Structure ==="
find SOURCES -type d | sort

# Verify aliases/sources/ structure
echo "=== aliases/sources/ Structure ==="
find aliases/sources -type d | sort

# Verify raw extraction
echo "=== Raw Contents ==="
find SOURCES/raw -type f -name "*.md" | wc -l
find SOURCES/raw -type f -name "*.txt" | wc -l

# Verify orchestration state
echo "=== orchestration/state/ ==="
ls orchestration/state/

# Verify repository root clean
echo "=== Repository Root ==="
ls | grep -v "^CANON$\|^OPERATIONAL$\|^QUEUE$\|^ARCHIVE$\|^EXEMPLA$\|^aliases$\|^orchestration$\|^SOURCES$\|^README\|^\.git"
```

### F2: Documentation Verification

```bash
# Verify key files exist
test -f SOURCES/README.md && echo "✓ SOURCES/README.md" || echo "✗ SOURCES/README.md"
test -f SOURCES/index.md && echo "✓ SOURCES/index.md" || echo "✗ SOURCES/index.md"
test -f SOURCES/FRONTMATTER_TEMPLATE.md && echo "✓ SOURCES/FRONTMATTER_TEMPLATE.md" || echo "✗ SOURCES/FRONTMATTER_TEMPLATE.md"
test -f aliases/sources/README.md && echo "✓ aliases/sources/README.md" || echo "✗ aliases/sources/README.md"
test -f orchestration/state/ORACLE9_CONTEXT.md && echo "✓ orchestration/state/ORACLE9_CONTEXT.md" || echo "✗ orchestration/state/ORACLE9_CONTEXT.md"
```

### F3: Git Commit

```bash
git add -A
git commit -m "DIRECTIVE-032A: Intelligence apparatus infrastructure

- Created SOURCES/ directory (raw/, processed/)
- Extracted transcripts.zip to SOURCES/raw/
- Created skeletal aliases/sources/ structure
- Installed frontmatter schema template
- Filed orphan files to orchestration/state/
- Installed ORACLE9_CONTEXT.md

Oracle9 Phase: Infrastructure Stream"
```

---

## EXECUTION LOG REQUIREMENTS

Save to: `orchestration/execution_logs/EXECUTION_LOG-2026-01-01-032A.md`

**Template:**

```markdown
# EXECUTION LOG: DIRECTIVE-032A
## Intelligence Apparatus Infrastructure

**Executed**: 2026-01-01
**Agent**: Claude Code
**Directive**: DIRECTIVE-032A
**Parallel Stream**: DIRECTIVE-032B (Protocol Documentation)

---

## PRE-EXECUTION SURVEY

### Repository Root Before
[Paste output of ls -la | head -20]

### SOURCES/ Before
[Paste output showing SOURCES/ did not exist]

### aliases/sources/ Before
[Paste output showing aliases/sources/ did not exist]

---

## PHASE-BY-PHASE EXECUTION

### Phase A: Orphan Triage
| Orphan | Destination | Status |
|--------|-------------|--------|
| ORACLE_CONTEXT.md | orchestration/state/ | ✓ |
| ORACLE_CONTEXT_v2.md | orchestration/state/ | ✓ |
| ORACLE8_STATUS_REPORT.md | orchestration/state/ | ✓ |

### Phase B: SOURCES/ Creation
- SOURCES/raw/ created: ✓
- SOURCES/processed/ created: ✓
- SOURCES/README.md created: ✓
- SOURCES/index.md created: ✓

### Phase C: Archive Extraction
- Archive extracted: ✓
- macOS artifacts removed: ✓
- File count: [N] .md, [N] .txt
- Directory structure: [describe]

### Phase D: Aliases
- aliases/sources/by-platform/ created: ✓
- aliases/sources/by-tier/ created: ✓
- aliases/sources/by-chain/ created: ✓
- README.md created: ✓

### Phase E: Schema Installation
- ORACLE9_CONTEXT.md installed: ✓
- FRONTMATTER_TEMPLATE.md created: ✓

### Phase F: Verification
[Paste verification output]

---

## POST-EXECUTION STATE

### SOURCES/ Structure
[tree or find output]

### aliases/sources/ Structure
[tree or find output]

### File Counts
| Location | Count |
|----------|-------|
| SOURCES/raw/*.md | [N] |
| SOURCES/raw/*.txt | [N] |
| SOURCES/processed/ | 0 |

---

## ORACLE DECISIONS ENCODED

- Decision 9.1: Eight-dimensional schema (template installed)
- Decision 9.2: value_modality field (documented in template)
- Decision 9.4: Flat + naming + aliases (structure created)
- Implicit: SOURCES as INPUT tier (README documents)

---

## STATUS

**COMPLETE** / INCOMPLETE / BLOCKED

---

## COORDINATION WITH DIRECTIVE-032B

Provides to 032B:
- SOURCES/ structure exists
- Raw archive extracted
- Frontmatter template available

Awaits from 032B:
- Complete triage protocol
- Processing function routing documentation
- value_modality assessment guide
```

---

## SUCCESS CRITERIA

- [ ] Repository root clean (orphans filed)
- [ ] SOURCES/raw/ exists with extracted archive
- [ ] SOURCES/processed/ exists (empty, ready)
- [ ] SOURCES/README.md documents purpose
- [ ] SOURCES/index.md template created
- [ ] SOURCES/FRONTMATTER_TEMPLATE.md installed
- [ ] aliases/sources/ skeletal structure exists
- [ ] aliases/sources/README.md documents usage
- [ ] orchestration/state/ORACLE9_CONTEXT.md installed
- [ ] Git commit with descriptive message
- [ ] Execution log saved with evidence

---

## ITEMS NOT IN SCOPE (DIRECTIVE-032B HANDLES)

- Complete triage protocol documentation
- Processing function routing logic
- value_modality assessment decision tree
- Integration protocol specification

---

**CRITICAL REMINDER**: 

> "Claudes must ACTUALLY VERIFY filesystem state, not claim 'already clean' without examining."
> — Oracle7

Run ALL verification commands. Document actual output. Do not assume completion.

---

*This directive archived to orchestration/directives/ upon execution.*
