# DIRECTIVE-033A: COMPREHENSIVE TRIAGE + STRUCTURED INDEX
## Stream A: Complete Source Cataloging and Ontology Seed
**Issued**: 2026-01-01
**Authority**: Oracle9 under Sovereign direction
**Classification**: CRITICAL — Intelligence Apparatus Completion
**Execution**: Claude Code
**Parallel Stream**: DIRECTIVE-033B handles paradigm processing + CANON integration

---

## SOVEREIGN'S MANDATE

> "These directives are way too narrow in scope. Get more done when issuing these tasks... Have the Claudes stage, evaluate and compare against the criteria and execute."

> "It might be time to introduce structured file formats. This appears to be the bridge towards codifying the mechanics into the codebase... whether it's simple csv, or rdbms."

> "What would a superintelligent forward deployed systems designer/architect/engineer create?"

---

## ORACLE'S INTERPRETATION

This directive completes the **triage layer** of Oracle9 in a single comprehensive cycle:
1. Survey all 234 raw sources
2. Create sources.csv as structured index (ontology seed)
3. Batch-triage with full eight-dimensional classification
4. Populate alias symlinks for navigation
5. Establish the pattern for ongoing cataloging

This is NOT incremental staging. This is **complete execution** of the triage apparatus.

---

## 18-LENS EVALUATION

| # | Lens | Assessment | Score |
|---|------|------------|-------|
| 1 | Syncrescendent Route | sources.csv enables recursive discovery across chains | ✓ |
| 2 | Bitter Lesson | Structured data scales to 10,000+ sources | ✓ |
| 3 | Antifragile | Schema handles unknown source types via 'other' escape | ✓ |
| 4 | Meet the Moment | CSV immediately useful, prepares for database | ✓ |
| 5 | Steelman/Redteam | CSV is universal—no vendor lock-in, any tool reads it | ✓ |
| 6 | Personal Idiosyncrasies | Holistic view via sorting/filtering | ✓ |
| 7 | Potency w/o Resolution Loss | CSV index + markdown files = full resolution | ✓ |
| 8 | Elegance + Dev Happiness | One file, all metadata, simple format | ✓ |
| 9 | Agentify + Human-Navigable | CSV for agents, aliases for humans | ✓ |
| 10 | First Principles | Index is essential for 234 items | ✓ |
| 11 | Systems Thinking | Connects triage→routing→processing→integration | ✓ |
| 12 | Industrial Engineering | Enables batch operations, eliminates manual tracking | ✓ |
| 13 | Complexity Theory | Essential structure only—8 dimensions, no more | ✓ |
| 14 | Permaculture | New entries follow same pattern, self-maintaining | ✓ |
| 15 | Design Thinking | Solves real navigation/discovery problem | ✓ |
| 16 | Agile | Complete deliverable in one cycle | ✓ |
| 17 | Lean | Eliminates relay waste, manual status tracking | ✓ |
| 18 | Six Sigma | Consistent schema reduces classification errors | ✓ |

**Score: 18/18 — APPROVED**

---

## EXECUTION SCOPE

### Deliverables
1. **sources.csv** — Complete structured index of all 234 sources
2. **Alias symlinks** — Populated by-tier/ and by-chain/ directories
3. **Triage report** — Summary statistics and notable findings
4. **Updated SOURCES/index.md** — Reflects cataloged state

### NOT in Scope (DIRECTIVE-033B handles)
- Full transcript processing
- CANON integration
- Frontmatter addition to processed files

---

## PHASE 1: SURVEY AND SCHEMA CREATION

### 1.1 Complete File Inventory

```bash
# Generate complete file listing with paths
find SOURCES/raw -type f \( -name "*.md" -o -name "*.txt" \) > /tmp/source_inventory.txt

# Count by directory
echo "=== Distribution by Directory ==="
find SOURCES/raw -type f \( -name "*.md" -o -name "*.txt" \) | sed 's|/[^/]*$||' | sort | uniq -c | sort -rn

# Count by extension
echo "=== Distribution by Extension ==="
find SOURCES/raw -type f -name "*.md" | wc -l
find SOURCES/raw -type f -name "*.txt" | wc -l

# Sample filenames for pattern recognition
echo "=== Sample Filenames ==="
find SOURCES/raw -type f -name "*.md" | head -20
```

### 1.2 Create sources.csv with Headers

```bash
cat > SOURCES/sources.csv << 'EOF'
id,filename,filepath,platform,format,cadence,value_modality,signal_tier,status,chain,topics,creator,guest,title,date_published,date_processed,date_integrated,integrated_into,notes
EOF
```

**Column Definitions** (from SOURCES_SCHEMA.md):
- `id`: SOURCE-YYYYMMDD-NNN format
- `filename`: Current filename
- `filepath`: Relative path from SOURCES/
- `platform`: youtube|podcast|substack|arxiv|x|book|course|newsletter|other
- `format`: interview|panel|solo_presentation|paper|thread|article|lecture|tutorial|other
- `cadence`: daily|weekly|periodic|arrhythmic|evergreen
- `value_modality`: dialogue_primary|visual_primary|audio_primary|comments_primary|multimodal_essential|text_native
- `signal_tier`: paradigm|strategic|tactical|noise
- `status`: raw|triaged|processed|integrated|archived
- `chain`: intelligence|information|insight|expertise|knowledge|wisdom
- `topics`: Comma-separated tags (quoted if contains commas)
- `creator`: Primary creator/channel
- `guest`: Guest if interview format
- `title`: Content title
- `date_published`: YYYY-MM-DD
- `date_processed`: YYYY-MM-DD or empty
- `date_integrated`: YYYY-MM-DD or empty
- `integrated_into`: CANON IDs or empty
- `notes`: Any relevant notes

---

## PHASE 2: BATCH TRIAGE

### 2.1 Triage Protocol (from TRIAGE_PROTOCOL.md)

For each source file:

**Quick Scan (5 sec)**:
- Filename pattern → platform, date, creator
- Directory location → topic hint
- Extension → .md may be pre-processed, .txt is raw

**Classification (30 sec)**:
- platform: Extract from filename (youtube_video, podcast, etc.)
- format: Infer from creator/title (Dwarkesh = interview, etc.)
- cadence: Most are arrhythmic (serendipitous finds)

**value_modality (15 sec)**:
- Standard interviews → dialogue_primary
- Keynotes/tutorials → visual_primary (flag for later)
- Text sources → text_native

**signal_tier (30 sec)**:
- AGI/ folder → likely paradigm or strategic
- Daily news → likely tactical or noise
- Known high-value creators (Dwarkesh, Lex, Karpathy) → paradigm

**chain (10 sec)**:
- AGI content → intelligence
- Anthropology → wisdom or insight
- Physical AI → intelligence
- Biology → knowledge or wisdom

### 2.2 Batch Processing Strategy

**Pass 1: High-Priority Directories** (AGI/, Anthropology/, Physical AI/)
- These are Sovereign's pre-categorized high-value
- Likely paradigm or strategic tier
- Process first, populate CSV

**Pass 2: Categorized Sources** (0/interviewers/, 0/lecture/, etc.)
- Sovereign's organization provides routing hints
- 0/interviewers/holistic/ = paradigm interviews
- 0/daily/ = tactical or noise

**Pass 3: Uncategorized** (transcripts/, loose files)
- Require individual assessment
- May contain duplicates of categorized

**Pass 4: Verification**
- Check for duplicates (same content, different locations)
- Validate tier assignments
- Ensure all 234 files cataloged

### 2.3 Triage Execution

For each file, append row to sources.csv:

```bash
# Example row generation (will be done programmatically)
echo 'SOURCE-20250926-001,20250926-youtube_video-dwarkesh_patel-richard_sutton.md,raw/AGI/20250926-youtube_video-dwarkesh_patel-richard_sutton.md,youtube,interview,arrhythmic,dialogue_primary,paradigm,triaged,intelligence,"agi,scaling_laws,bitter_lesson,reinforcement_learning",Dwarkesh Patel,Richard Sutton,Richard Sutton Interview,2025-09-26,,,,' >> SOURCES/sources.csv
```

**Programmatic approach** (recommended):
```python
import csv
import os
from pathlib import Path

def triage_file(filepath):
    """Extract metadata from filepath and content."""
    filename = os.path.basename(filepath)
    
    # Parse filename pattern: YYYYMMDD-platform-creator-title
    parts = filename.replace('.md', '').replace('.txt', '').split('-')
    
    # Infer metadata
    metadata = {
        'filename': filename,
        'filepath': filepath.replace('SOURCES/', ''),
        'platform': 'youtube' if 'youtube' in filename else 'other',
        'format': 'interview' if any(x in filepath.lower() for x in ['dwarkesh', 'lex', 'interview']) else 'other',
        'cadence': 'arrhythmic',
        'value_modality': 'dialogue_primary',  # Default for interviews
        'signal_tier': 'strategic',  # Default, upgrade paradigm manually
        'status': 'triaged',
        'chain': 'intelligence' if 'AGI' in filepath else 'insight',
        # ... etc
    }
    return metadata

# Process all files
sources = []
for root, dirs, files in os.walk('SOURCES/raw'):
    for file in files:
        if file.endswith(('.md', '.txt')):
            filepath = os.path.join(root, file)
            sources.append(triage_file(filepath))

# Write CSV
with open('SOURCES/sources.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=[...])
    writer.writeheader()
    writer.writerows(sources)
```

---

## PHASE 3: TIER ASSIGNMENT CRITERIA

### Paradigm Tier (target: 10-15 sources)

**Auto-assign paradigm** if:
- Creator is Dwarkesh Patel interviewing AI researchers
- Creator is Lex Fridman interviewing AI/science leaders
- Content is from Andrej Karpathy
- Content is from Richard Sutton
- Content is from Demis Hassabis
- Content explicitly about scaling laws, bitter lesson, AGI timelines

**Known paradigm files** (from AGI/ folder):
```
20250926-youtube_video-dwarkesh_patel-richard_sutton.md
20251017-youtube_video-dwarkesh_patel-andrej_karpathy.md
20250723-youtube_video-lex_fridman-demis_hassabis_475.md
20250522-youtube_video-dwarkesh_patel-sholto_douglas_&_trenton_bricken.md
20250403-youtube_video-dwarkesh_patel-scott_alexander_&_daniel_kokotajlo.md
20251004-youtube_video-dwarkesh_patel-sutton_response.md
```

### Strategic Tier (target: 40-60 sources)

**Auto-assign strategic** if:
- Interview format with domain expert
- Lecture from recognized institution
- Content relevant to active Syncrescendent chains
- High-signal creator (Y Combinator, a16z, etc.)

### Tactical Tier (target: 80-100 sources)

**Auto-assign tactical** if:
- News/daily content
- Aggregated/derivative content
- Good but not urgent

### Noise Tier (target: 60-80 sources)

**Auto-assign noise** if:
- Duplicate of higher-quality source
- Outdated information
- Off-topic for Syncrescendence
- Low signal-to-noise ratio

---

## PHASE 4: ALIAS POPULATION

### 4.1 Create Symlinks for Paradigm Tier

```bash
# For each paradigm source, create symlinks
cd aliases/sources

# Example for Sutton interview
ln -s ../../../SOURCES/raw/AGI/20250926-youtube_video-dwarkesh_patel-richard_sutton.md by-tier/paradigm/
ln -s ../../../SOURCES/raw/AGI/20250926-youtube_video-dwarkesh_patel-richard_sutton.md by-chain/intelligence/
ln -s ../../../SOURCES/raw/AGI/20250926-youtube_video-dwarkesh_patel-richard_sutton.md by-platform/youtube/
```

### 4.2 Batch Symlink Creation

```bash
# Read paradigm entries from CSV and create symlinks
grep ",paradigm," SOURCES/sources.csv | while IFS=, read -r id filename filepath rest; do
    # Create tier symlink
    ln -sf "../../../SOURCES/$filepath" "aliases/sources/by-tier/paradigm/$filename"
done

# Repeat for strategic tier
grep ",strategic," SOURCES/sources.csv | while IFS=, read -r id filename filepath rest; do
    ln -sf "../../../SOURCES/$filepath" "aliases/sources/by-tier/strategic/$filename"
done
```

---

## PHASE 5: INDEX AND REPORTING

### 5.1 Update SOURCES/index.md

Replace template content with actual statistics:

```markdown
# SOURCES Index

**Last Updated**: 2026-01-01 (DIRECTIVE-033A)
**Total Sources**: 234 cataloged

## Summary Statistics

| Tier | Count | % |
|------|-------|---|
| Paradigm | XX | XX% |
| Strategic | XX | XX% |
| Tactical | XX | XX% |
| Noise | XX | XX% |

| Platform | Count |
|----------|-------|
| YouTube | XX |
| Podcast | XX |
| Other | XX |

| Chain | Count |
|-------|-------|
| Intelligence | XX |
| Information | XX |
| Insight | XX |
| ... | ... |

## Paradigm Sources (Highest Priority)

[List all paradigm-tier sources with links]

## See Also

- `sources.csv` — Complete structured index
- `aliases/sources/` — Navigation symlinks
- `orchestration/state/TRIAGE_PROTOCOL.md` — Classification methodology
```

### 5.2 Generate Triage Report

Create `orchestration/execution_logs/TRIAGE_REPORT-2026-01-01.md`:

```markdown
# Triage Report: DIRECTIVE-033A

## Execution Summary
- Total files processed: 234
- Paradigm tier: XX
- Strategic tier: XX
- Tactical tier: XX
- Noise tier: XX

## Notable Findings
- [Any duplicates identified]
- [Any classification challenges]
- [Recommendations for 033B processing]

## Paradigm Sources for Processing (033B)
1. [filename] — [rationale]
2. ...

## Files Requiring Manual Review
- [Any ambiguous cases]
```

---

## PHASE 6: VERIFICATION AND COMMIT

### 6.1 Verification Commands

```bash
# Verify CSV row count matches file count
wc -l SOURCES/sources.csv  # Should be 235 (234 + header)

# Verify all files cataloged
find SOURCES/raw -type f \( -name "*.md" -o -name "*.txt" \) | wc -l  # Should be 234

# Verify tier distribution
echo "Paradigm:"; grep -c ",paradigm," SOURCES/sources.csv
echo "Strategic:"; grep -c ",strategic," SOURCES/sources.csv
echo "Tactical:"; grep -c ",tactical," SOURCES/sources.csv
echo "Noise:"; grep -c ",noise," SOURCES/sources.csv

# Verify symlinks created
ls aliases/sources/by-tier/paradigm/ | wc -l
ls aliases/sources/by-tier/strategic/ | wc -l

# Verify no broken symlinks
find aliases/sources -type l ! -exec test -e {} \; -print
```

### 6.2 Git Commit

```bash
git add -A
git commit -m "DIRECTIVE-033A: Complete source triage + structured index

- Created sources.csv with 234 entries (ontology seed)
- Tier distribution: XX paradigm, XX strategic, XX tactical, XX noise
- Populated alias symlinks for paradigm/strategic tiers
- Updated SOURCES/index.md with statistics
- Generated triage report

Oracle9 Phase: Triage layer complete. Ready for 033B processing."
```

---

## SUCCESS CRITERIA

- [ ] sources.csv exists with 234 rows + header
- [ ] All files have complete eight-dimension classification
- [ ] Paradigm tier: 10-15 sources identified
- [ ] Strategic tier: 40-60 sources identified
- [ ] Alias symlinks populated for paradigm and strategic
- [ ] SOURCES/index.md updated with statistics
- [ ] Triage report generated
- [ ] No broken symlinks
- [ ] Git committed with descriptive message

---

## COORDINATION WITH DIRECTIVE-033B

**Provides to 033B**:
- sources.csv with paradigm sources identified
- Triage report with processing recommendations
- Alias structure for navigation

**033B will**:
- Process paradigm-tier sources
- Integrate into CANON
- Update sources.csv status to 'processed'/'integrated'

---

## EXECUTION LOG TEMPLATE

Save to: `orchestration/execution_logs/EXECUTION_LOG-2026-01-01-033A.md`

```markdown
# EXECUTION LOG: DIRECTIVE-033A

**Executed**: 2026-01-01
**Agent**: Claude Code
**Status**: [COMPLETE/INCOMPLETE]

## Phase 1: Survey
- Total files found: [N]
- Distribution: [summary]

## Phase 2: Batch Triage
- Files processed: [N]
- Method: [programmatic/manual]
- Time taken: [estimate]

## Phase 3: Tier Assignment
| Tier | Count |
|------|-------|
| Paradigm | [N] |
| Strategic | [N] |
| Tactical | [N] |
| Noise | [N] |

## Phase 4: Aliases
- Paradigm symlinks: [N]
- Strategic symlinks: [N]
- Broken symlinks: [N]

## Phase 5: Reporting
- index.md updated: [Y/N]
- Triage report created: [Y/N]

## Phase 6: Verification
[Paste verification output]

## Paradigm Sources Identified
1. [filename] — [brief rationale]
2. ...

## Issues/Notes
[Any problems encountered]
```

---

**THIS DIRECTIVE COMPLETES THE TRIAGE LAYER OF ORACLE9.**
