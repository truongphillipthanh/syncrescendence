# MECH-source_anneal_pipeline

**Type:** Mechanism
**Domain:** Knowledge Infrastructure
**Status:** Blueprint (post-manual-anneal, pre-automation)
**Created:** 2026-02-21
**Author:** Commander (COO)
**Derived From:** The Great Source Anneal operation record (`04-SOURCES/_meta/ANNEAL_OPERATION_RECORD.md`)

---

## Purpose

This mechanism defines a repeatable, automated pipeline for ingesting, deduplicating, normalizing, enriching, and indexing source materials into the Syncrescendence flat Obsidian-native knowledge corpus. It codifies the lessons learned from the manual Source Anneal operation and subsequent Watch Later drain into infrastructure that handles both bulk imports and continuous incremental additions.

**Corpus stats (as of 2026-02-22):** 1,773 SOURCE files. Growth breakdown:
- Original anneal: 1,131 files across 3 pools reduced to 627 unified sources
- Watch Later drain (2026-02-19): 1,158 YouTube videos processed, 1,148 successfully ingested as SOURCE-*.md (10 failed transcript fetch, metadata-only fallback). This single operation nearly tripled the corpus.

---

## Pipeline Architecture

```
   [Watch Folders]
        |
   STAGE 1: INGEST
        |
   STAGE 2: CENSUS
        |
   STAGE 3: NORMALIZE
        |
   STAGE 4: ENRICH
        |
   STAGE 5: INDEX
        |
   STAGE 6: STAGE
        |
   [NotebookLM / Obsidian]
```

Each stage is **idempotent** -- re-running a stage on already-processed files produces no change and no corruption. Each stage writes a manifest of its actions to `04-SOURCES/_meta/` for auditability.

---

## Stage 1: INGEST

### Function
Watch designated folders for new source files. Auto-detect file type and source platform. Apply naming convention immediately on ingest.

### Input Sources
- `~/Desktop/research/` -- X bookmark exports (primary intake)
- `~/Downloads/*.md` -- Manual drops
- Clipboard capture (future: browser extension or bookmarklet)
- X API bookmark export (future)
- YouTube Watch Later playlist (OPERATIONAL — OAuth2 connected, Ingest Queue playlist created, yt-dlp drain script built and executed)

### Detection Logic

```python
def detect_platform(filepath, content, frontmatter):
    """Platform detection priority chain."""
    # 1. Frontmatter explicit
    if frontmatter.get('platform'):
        return frontmatter['platform']
    # 2. URL pattern
    url = frontmatter.get('url', '') or extract_url_from_body(content)
    if 'x.com/' in url or 'twitter.com/' in url:
        return 'x'
    if 'youtube.com/' in url or 'youtu.be/' in url:
        return 'youtube'
    if 'medium.com/' in url:
        return 'medium'
    if 'substack.com/' in url:
        return 'substack'
    if 'arxiv.org/' in url:
        return 'arxiv'
    # 3. Filename pattern
    if '-x_article-' in filepath or '-x_thread-' in filepath:
        return 'x'
    if '-youtube_video-' in filepath or '-youtube-' in filepath:
        return 'youtube'
    # 4. Content heuristics
    if content.startswith('RT @') or '(@' in content[:200]:
        return 'x'
    return 'unknown'
```

### Format Detection

```python
def detect_format(platform, filepath, content, frontmatter):
    """Format detection from platform + content signals."""
    if frontmatter.get('format'):
        return frontmatter['format']
    if platform == 'x':
        if 'thread' in filepath.lower() or content.count('\n\n') > 10:
            return 'thread'
        return 'article'
    if platform == 'youtube':
        if 'interview' in filepath.lower():
            return 'interview'
        if 'lecture' in filepath.lower():
            return 'lecture'
        if 'panel' in filepath.lower():
            return 'panel'
        return 'video'
    return 'article'  # default
```

### Actions
1. Copy file to `04-SOURCES/_staging/` (temporary holding area)
2. Detect platform and format
3. Extract or infer date, creator, title slug
4. Rename to `SOURCE-{YYYYMMDD}-{platform}-{format}-{creator}-{title_slug}.md`
5. Inject minimal frontmatter skeleton if missing
6. Move to `04-SOURCES/` root
7. Log action to `_meta/INGEST_LOG.md`

### Implementation
- **Mechanism:** `fswatch` on macOS (or `launchd` periodic polling every 60s)
- **Script:** `04-SOURCES/_scripts/ingest.py` (or `ingest.sh` for bash)
- **Trigger:** File creation in watch folders
- **Idempotency:** Skip files already present in `04-SOURCES/` (match by URL or filename)

---

## Stage 2: CENSUS

### Function
Check newly ingested files against the existing corpus for duplicates. Generate a census delta report.

### Deduplication Priority Chain

```
1. URL match (primary)     — exact match on normalized url field
2. Filename fuzzy match    — Levenshtein distance < 0.2 on title_slug component
3. Content hash (tertiary) — SHA-256 of body text (frontmatter excluded)
```

### URL Normalization

```python
def normalize_url(url):
    """Normalize URL for dedup matching."""
    url = url.strip().rstrip('/')
    url = url.replace('http://', 'https://')
    url = url.replace('twitter.com/', 'x.com/')
    # Remove tracking params
    url = re.sub(r'[?&](utm_\w+|ref|s|t)=[^&]*', '', url)
    url = url.rstrip('?&')
    return url
```

### URL Index (SQLite)

```sql
CREATE TABLE source_index (
    url           TEXT PRIMARY KEY,
    filename      TEXT NOT NULL,
    platform      TEXT,
    format        TEXT,
    creator       TEXT,
    date_published TEXT,
    date_ingested TEXT DEFAULT (datetime('now')),
    content_hash  TEXT,
    file_size     INTEGER
);

CREATE INDEX idx_filename ON source_index(filename);
CREATE INDEX idx_creator ON source_index(creator);
CREATE INDEX idx_platform ON source_index(platform);
```

### Actions
1. For each new file: extract URL, compute content hash
2. Query source_index for URL match
3. If match: log as duplicate, skip (or compare size/quality and replace if better)
4. If no match: insert into index, proceed to Stage 3
5. Generate `_meta/CENSUS_DELTA_YYYYMMDD.md`

### Winner Selection (on duplicate detection)

```
Priority: Existing corpus file > New file (existing wins by default)
Exception: New file wins if:
  - Existing file has no frontmatter and new file does
  - New file is >20% larger (richer content capture)
  - New file has URL and existing does not
Decision logged to _meta/DEDUP_LOG.md
```

---

## Stage 3: NORMALIZE

### Function
Apply the canonical naming convention and ensure complete frontmatter on every file.

### Naming Convention

```
SOURCE-{YYYYMMDD}-{platform}-{format}-{creator}-{title_slug}.md
```

| Component | Rules |
|-----------|-------|
| `YYYYMMDD` | From frontmatter `date_published`, `captured_date`, or Snowflake ID. `undated` if unknown. |
| `platform` | x, youtube, website, medium, substack, arxiv, podcast, internal, unknown |
| `format` | article, thread, interview, lecture, essay, tutorial, announcement, video, transcript, research, panel |
| `creator` | Lowercase handle without @, or lastname for non-X. `unknown` if unresolvable. |
| `title_slug` | First 6-8 meaningful words, lowercase, underscores. Max 80 chars. |

### Twitter Snowflake Date Extraction

```python
def snowflake_to_date(tweet_id: int) -> str:
    """Extract creation date from Twitter Snowflake ID.

    Twitter Snowflake: top 42 bits = ms since Twitter epoch (1288834974657).
    """
    twitter_epoch_ms = 1288834974657
    timestamp_ms = (tweet_id >> 22) + twitter_epoch_ms
    dt = datetime.utcfromtimestamp(timestamp_ms / 1000)
    return dt.strftime('%Y-%m-%d')

def extract_tweet_id(url: str) -> int:
    """Extract tweet ID from X/Twitter URL."""
    match = re.search(r'/status/(\d+)', url)
    if match:
        return int(match.group(1))
    return None
```

### Frontmatter Template

```yaml
---
id: SOURCE-{YYYYMMDD}-{NNN}
original_filename: "{pre-rename path}"
status: triaged
platform: x
format: article
creator: handle
title: ""
url: https://...
date_published: YYYY-MM-DD
captured_date: YYYY-MM-DD
author: "Display Name (@handle)"
signal_tier: ""
topics: []
synopsis: ""
key_insights: []
teleology: ""
notebooklm_category: ""
aliases: []
---
```

### Actions
1. Parse existing frontmatter
2. Fill missing fields from filename, URL, and content analysis
3. Rename file if not already in canonical format
4. Preserve `original_filename` in frontmatter
5. Validate YAML syntax
6. Log to `_meta/NORMALIZE_LOG.md`

### Idempotency
- Check if file already starts with `SOURCE-` prefix
- Check if all required frontmatter fields are present
- Skip files that are already fully normalized

---

## Stage 4: ENRICH

### Function
AI-powered metadata generation for every source file. Read content, generate synopsis, topics, teleology, signal_tier, notebooklm_category, aliases, and title (for X files).

### Enrichment Prompt Template

```
You are enriching a source file for a knowledge management system.

Read the following source content and generate:
1. synopsis: 2-3 sentence summary of what this content says and why it matters
2. key_insights: Top 3 actionable or paradigm-shifting takeaways (bullet points)
3. topics: Array of 3-7 topic tags (lowercase, use existing taxonomy when possible)
4. teleology: One of: extract, implement, strategize, synthesize, contextualize, inspire, reference
5. signal_tier: One of: paradigm (field-shifting), strategic (informs major decisions), tactical (useful technique), noise (low value)
6. notebooklm_category: One of the configured notebook categories
7. aliases: 2-3 short reference names for this source
8. title: (X platform only) Synthetic title from first meaningful sentence

Respond in YAML format only.
```

### Batch Processing

```python
BATCH_SIZE = 25
MAX_CONCURRENT = 4
MODEL = "claude-sonnet-4-6"  # cost-effective for enrichment
RETRY_MAX = 3
RETRY_DELAY = 30  # seconds

async def enrich_batch(files: list[Path]):
    """Process a batch of files through AI enrichment."""
    tasks = []
    for f in files:
        content = f.read_text()
        frontmatter = parse_frontmatter(content)

        # Skip if already enriched
        if frontmatter.get('synopsis') and frontmatter.get('teleology'):
            continue

        tasks.append(enrich_single(f, content, frontmatter))

    results = await asyncio.gather(*tasks, return_exceptions=True)

    for f, result in zip(files, results):
        if isinstance(result, Exception):
            update_frontmatter(f, {'status': 'enrich_failed'})
            log_error(f, result)
        else:
            update_frontmatter(f, result)
```

### Field Protection
- If a field already has a non-empty value, do NOT overwrite (respect pre-existing curated data)
- Exception: `status` field is always updated to `processed` on successful enrichment
- The 34 files with pre-existing `signal_tier` values (from legacy processing) are validated, not overwritten

### Rate Limiting
- Claude API: respect per-minute token limits
- Batch size of 25 files fits comfortably in a single context window summary
- 4 concurrent batches = ~100 files in flight
- Full corpus (1,773 files) completes in ~18 batches = ~45 minutes at 4x parallelism

---

## Stage 5: INDEX

### Function
Regenerate MOC (Map of Content) files from enriched metadata. Update master tracking CSV.

### MOC Types

| MOC File | Grouping Key | Sort |
|----------|-------------|------|
| MOC-by-topic.md | `topics` array (one entry per unique tag) | Alphabetical |
| MOC-by-creator.md | `creator` field | Post count descending |
| MOC-by-teleology.md | `teleology` field | Category then date |
| MOC-by-platform.md | `platform` field | Count descending |
| MOC-by-signal-tier.md | `signal_tier` field | paradigm first |
| MOC-chronological.md | `date_published` | Newest first |
| MOC-notebooklm.md | `notebooklm_category` | Category then date |

### MOC Template

```markdown
# MOC: By {Dimension}

> Auto-generated from SOURCE-*.md frontmatter.
> Last updated: {timestamp}
> Total sources: {count}

## {Group Name} ({count})

- [[SOURCE-20260203-x-article-tempoimmaterial-subagents_when_and_how_to_use_them|Subagents: When and How to Use Them]]
- [[SOURCE-20260205-x-article-jainarvind-how_do_you_build_a_context_graph|How Do You Build a Context Graph]]
...
```

### DYN-SOURCES.csv

```csv
id,filename,platform,format,creator,date_published,signal_tier,teleology,notebooklm_category,url,status
SOURCE-20260203-001,SOURCE-20260203-x-article-tempoimmaterial-subagents_when_and_how_to_use_them.md,x,article,tempoimmaterial,2026-02-03,strategic,implement,agents-orchestration,https://x.com/...,processed
```

### Actions
1. Scan all `SOURCE-*.md` files, parse frontmatter
2. Build in-memory index grouped by each MOC dimension
3. Write MOC files to `04-SOURCES/_index/`
4. Write `DYN-SOURCES.csv` to `04-SOURCES/_meta/`
5. Write `SCHEMA.md` documenting all field values and their frequencies

---

## Stage 6: STAGE

### Function
Map enriched sources to NotebookLM notebooks by category. Generate upload manifest.

### NotebookLM Category Mapping

```yaml
notebooks:
  agents-orchestration:
    description: "Multi-agent systems, swarms, orchestration patterns"
    topics_include: [agents, orchestration, multi-agent, swarm, delegation]
  ai-engineering:
    description: "AI/ML engineering, architecture, roadmaps"
    topics_include: [ai-engineering, ml, architecture, roadmap]
  claude-code:
    description: "Claude Code usage, skills, configuration, patterns"
    topics_include: [claude-code, skills, claude-md, subagents]
  coding-tools-platforms:
    description: "Developer tools, IDEs, coding platforms"
    topics_include: [codex, gemini, tools, platforms, ide]
  philosophy-paradigm:
    description: "Deep paradigm content, consciousness, intelligence theory"
    topics_include: [philosophy, paradigm, consciousness, intelligence]
  career-growth:
    description: "Career strategy, personal development, economic positioning"
    topics_include: [career, growth, strategy, economics]
  vibe-coding-design:
    description: "Vibe coding, design, creative tools"
    topics_include: [vibe-coding, design, creative, ux]
  prompt-engineering:
    description: "Prompt engineering, skills craft"
    topics_include: [prompts, prompt-engineering, skills]
  ai-creative-media:
    description: "AI in video, VFX, creative media"
    topics_include: [video, vfx, creative-media, 3d]
  syncrescendence:
    description: "Internal system knowledge, convergence strategy"
    topics_include: [syncrescendence, convergence, internal]
```

### Upload Manifest

```markdown
# NotebookLM Upload Manifest
Generated: {timestamp}

## agents-orchestration (23 sources)
1. SOURCE-20260131-x-article-pbteja1998-the_complete_guide_to_building_mission_control.md
2. SOURCE-20260203-x-article-tempoimmaterial-subagents_when_and_how_to_use_them.md
...

## claude-code (142 sources)
1. SOURCE-20260109-x-article-chasing_next-how_to_set_up_claude_code_in_15_minutes.md
...
```

### Actions
1. Read `notebooklm_category` from each file's frontmatter
2. Group files by category
3. Generate upload manifest with file counts and paths
4. Flag files with empty `notebooklm_category` for manual assignment

---

## Key Design Decisions

### URL as Primary Key
Every source's URL is the deduplication anchor. A source without a URL requires manual classification. The URL index (SQLite) is the single source of truth for "has this been ingested before?"

### Idempotent Stages
Each stage can be re-run without corruption:
- Census does not mutate files
- Normalize checks for existing `SOURCE-` prefix before renaming
- Enrich only fills empty fields, never overwrites populated ones
- Index is fully regenerated from current frontmatter state

### Incremental Operation
The pipeline handles both bulk anneal (first run, ~1000 files) and incremental additions (ongoing, 1-10 files at a time). The same stages execute; only the file count changes.

### Twitter Snowflake Date Extraction
Built-in for any X/Twitter URL. Extract tweet_id from URL, compute `(id >> 22) + 1288834974657` for epoch milliseconds, convert to date. This is a zero-cost date recovery method that the manual anneal proved recovers dates for 100% of X files with URLs.

### Flat Over Hierarchical
Physical structure is flat (one directory). Organization is virtual:
- Frontmatter metadata = the database
- Naming convention = human-scannable sort order
- MOC files = virtual hierarchies
- Tags and aliases = cross-cutting access paths

---

## API Integration Points

### X/Twitter API (Read-Only)
- **Bookmark export**: Periodic export of user bookmarks to markdown files
- **Tweet content fetch**: Given a tweet URL, fetch full text, thread expansion, media URLs
- **Date recovery**: Snowflake ID extraction (no API needed -- pure math)
- **Authentication**: OAuth 2.0 Bearer token (read-only scope)
- **Rate limit**: 500 requests / 15 min (basic tier)

### YouTube Data API
- **Video search**: Search by channel + title to recover URLs for files missing them
- **Metadata fetch**: Title, description, publish date, channel name, duration
- **Transcript fetch**: Via `youtube-transcript-api` v1.x Python package (no API key needed). API surface: `api.fetch()` returns transcript, `transcript.snippets` for segment access. (Note: pre-1.0 `YouTubeTranscriptApi.get_transcript()` is deprecated.)
- **Authentication**: OAuth2 connected (user context for playlist access including Watch Later)
- **Ingest Queue**: Dedicated YouTube playlist created as the staging inbox for automated drain
- **Drain script**: yt-dlp-based batch extraction script built and proven at scale (1,158 videos)
- **Rate limit**: 10,000 units/day (search = 100 units each)

### Gemini Multimodal (Target Processing Engine)
- **Role**: Primary enrichment engine for YouTube content (per CANON-25200 task routing: "YouTube processing → Gemini, Native 263 tok/sec multimodal")
- **Capability**: Native YouTube URL processing — visual + audio analysis, not just captions. Captures diagrams, code on screen, visual demos that transcript-only misses.
- **Hosting target**: GCP Cloud Functions for serverless execution
- **Cost advantage**: Significantly cheaper than Claude for bulk video processing at scale
- **Reference**: `05-SIGMA/syntheses/SYNTHESIS-gemini-cli.md` (Colab-to-Claude bridge pattern), `05-SIGMA/syntheses/SYNTHESIS-platform_topology_jan2026.md` (token economics)

### Claude API
- **Enrichment pass**: Synopsis, topics, teleology, signal_tier generation
- **Model**: `claude-sonnet-4-6` for cost-effective batch enrichment
- **Rate limit**: Respect per-minute token limits; batch size 25 files
- **Cost estimate**: ~$0.02-0.05 per file (average 2K tokens in, 500 tokens out)

### NotebookLM
- **Current**: Manual upload via web UI based on staging manifest
- **Future**: API integration when NotebookLM API becomes available
- **Workaround**: Generate notebook-specific markdown bundles that can be drag-dropped

---

## Implementation Priority

| Priority | Component | Effort | Dependency | Status |
|----------|-----------|--------|------------|--------|
| 1 | URL index (SQLite) | 2 hours | None -- foundational for all dedup | PLANNED |
| 2 | Normalize script (Python) | 4 hours | URL index | PLANNED |
| 3 | Ingest watcher (fswatch/launchd) | 2 hours | Normalize script | PLANNED |
| 4 | Enrich batching (Python + Claude API) | 6 hours | Normalize script | PLANNED |
| 5 | MOC generator (Python) | 3 hours | Enrich batching | PLANNED |
| 6 | X API integration | 4 hours | URL index | PLANNED |
| 7 | YouTube OAuth2 + playlist access | 3 hours | URL index | **DONE** (OAuth2 connected, Ingest Queue playlist created) |
| 8 | YouTube yt-dlp drain script | 2 hours | YouTube OAuth2 | **DONE** (1,158 videos drained) |
| 9 | YouTube transcript API (v1.x) | 2 hours | YouTube drain | **DONE** (1,148 transcripts fetched) |
| 10 | NotebookLM staging | 2 hours | MOC generator | PLANNED |
| 11 | Gemini multimodal enrichment | 4 hours | GCP Cloud Functions | PLANNED |

**Total estimated: ~34 hours. ~7 hours DONE (YouTube pipeline foundation), ~27 hours remaining.**

Priority 1-3 enable continuous operation. Priority 4-5 enable full enrichment. Priority 7-9 (YouTube foundation) are COMPLETE — the Watch Later drain proved the pipeline at scale. Priority 6 and 10 are quality-of-life improvements. Priority 11 (Gemini) is the target enrichment engine upgrade.

---

## Configuration

```yaml
anneal:
  source_dir: "04-SOURCES/"
  meta_dir: "04-SOURCES/_meta/"
  index_dir: "04-SOURCES/_index/"
  assets_dir: "04-SOURCES/_assets/"
  staging_dir: "04-SOURCES/_staging/"
  scripts_dir: "04-SOURCES/_scripts/"

  watch_dirs:
    - "~/Desktop/research/"
    - "~/Downloads/*.md"

  naming:
    pattern: "SOURCE-{date}-{platform}-{format}-{creator}-{title_slug}.md"
    date_format: "YYYYMMDD"
    undated_label: "undated"
    title_slug_max_words: 8
    title_slug_max_chars: 80

  dedup:
    primary: url
    secondary: filename_fuzzy
    tertiary: content_hash
    fuzzy_threshold: 0.2  # Levenshtein ratio
    winner_priority: [existing, pool_a, pool_b_processed, pool_b_research, pool_c]

  enrich:
    batch_size: 25
    max_concurrent: 4
    model: "claude-sonnet-4-6"
    retry_max: 3
    retry_delay_seconds: 30
    fields:
      - synopsis
      - key_insights
      - topics
      - teleology
      - signal_tier
      - notebooklm_category
      - aliases
      - title  # X platform only
    protect_existing: true  # never overwrite non-empty fields

  index:
    moc_types:
      - topic
      - creator
      - teleology
      - platform
      - signal_tier
      - chronological
      - notebooklm
    csv_output: "DYN-SOURCES.csv"

  platforms:
    known: [x, youtube, website, medium, substack, arxiv, podcast, internal, aihero, huggingface]
    url_patterns:
      x: ["x.com/", "twitter.com/"]
      youtube: ["youtube.com/", "youtu.be/"]
      medium: ["medium.com/"]
      substack: [".substack.com/"]
      arxiv: ["arxiv.org/"]

  teleology:
    values:
      extract: "Mine for specific techniques, configs, code snippets"
      implement: "Step-by-step guide to build something"
      strategize: "Informs high-level decisions, market positioning"
      synthesize: "Connects ideas across domains, meta-analysis"
      contextualize: "Provides background, history, framing"
      inspire: "Creative fuel, vision, motivation"
      reference: "Lookup material, specs, documentation"

  signal_tier:
    values:
      paradigm: "Field-shifting, changes how you think about the domain"
      strategic: "Informs major decisions, important but not paradigm-breaking"
      tactical: "Useful technique or tool, narrow applicability"
      noise: "Low value, keep for completeness but deprioritize"
```

---

## Error Handling

| Scenario | Action | Log |
|----------|--------|-----|
| Duplicate URL detected | Skip file, log to DEDUP_LOG.md | WARNING |
| Missing frontmatter entirely | Create skeleton from filename parsing | INFO |
| Enrichment API failure | Retry 3x with 30s delay, then mark `status: enrich_failed` | ERROR |
| File move collision (same filename exists) | Keep larger file, log decision | WARNING |
| Invalid YAML in frontmatter | Attempt repair (close unclosed quotes, fix indentation), log | ERROR |
| URL normalization failure | Store raw URL, flag for manual review | WARNING |
| Snowflake ID parse failure | Leave date as `undated`, log | WARNING |
| Watch folder inaccessible | Alert via health check, retry on next poll | CRITICAL |
| SQLite index corruption | Rebuild from filesystem scan of all SOURCE-*.md | CRITICAL |

### Recovery Procedures

**Full re-census (index rebuild):**
```bash
python anneal.py rebuild-index
# Scans all SOURCE-*.md, parses frontmatter, rebuilds SQLite index from scratch
# Safe to run anytime -- idempotent
```

**Re-enrich specific files:**
```bash
python anneal.py enrich --force --files "SOURCE-20260203-*.md"
# --force flag overrides protect_existing for targeted re-enrichment
```

**Dry-run any stage:**
```bash
python anneal.py normalize --dry-run
# Shows what would be renamed/modified without making changes
```

---

## Monitoring

### Health Checks
- Source count: `ls 04-SOURCES/SOURCE-*.md | wc -l` (should only increase)
- Index integrity: `python anneal.py check-index` (URL index matches filesystem)
- Enrichment coverage: `grep -l 'synopsis: ""' 04-SOURCES/SOURCE-*.md | wc -l` (should decrease over time)
- Stale staging: `ls 04-SOURCES/_staging/` (should be empty between runs)

### Metrics to Track
- Total source count (monotonically increasing)
- Enrichment coverage % (synopsis, teleology, signal_tier, notebooklm_category)
- URL coverage % (target: 95%+)
- Date coverage % (target: 95%+)
- Creator coverage % (target: 98%+)
- Duplicate detection rate per ingest batch
- Enrichment cost per file (tokens, dollars)

---

## Relationship to Constellation Infrastructure

This pipeline integrates with the existing Syncrescendence constellation:

- **Ingest watcher** runs as a launchd service on the MacBook Air (Ajna's machine, where X bookmark exports land)
- **Enrichment batching** can be dispatched as TASK files to Commander or Adjudicator via the auto-ingest system
- **Index regeneration** triggers on git commit of enriched files (post-commit hook)
- **Health metrics** feed into `DYN-CONSTELLATION_HEALTH.md` via the watchdog
- **URL index (SQLite)** stored at `04-SOURCES/_meta/source_index.db` (gitignored binary, like ontology.db)

---

---

## Stateless Inbox Zero Pipeline

### Design Philosophy

The user's save action is the ONLY manual step in the entire pipeline. One tap -- bookmark, like, watch later -- and everything downstream is automated. The save queue becomes stateless: the user never needs to "process" their saves. They accumulate, get auto-ingested, and auto-cleared.

```
SAVE (1 tap) → POLL → INGEST → ENRICH → INDEX → CLEAR SAVE
```

This inverts the traditional "collect then process" pattern. There is no backlog. There is no guilt queue. The system treats every save as a dispatch signal, not a storage event. The save slot is always empty by the next poll cycle.

**Core invariant:** If it was saved, it was ingested. If it was ingested, the save was cleared. The user's bookmark/like list is always near-zero.

---

### YouTube Pipeline

```
Like / Watch Later → youtube_ingest.py (6h poll) → transcript → SOURCE-*.md → Unlike / Remove
```

#### Authentication
- OAuth2 (user context) via `google-auth-oauthlib`
- Scopes: `youtube.readonly`, `youtube.force-ssl` (for playlist modification / unlike)
- Token stored at `~/.syncrescendence/youtube_token.json` (gitignored)
- Refresh token auto-renews; alert user only on revocation

#### Transcript Acquisition
- Primary: `youtube-transcript-api` Python package (free, no API quota consumed)
- Supports manual captions, auto-generated captions, and community captions
- Language priority: `en` > `en-US` > first available
- Fallback: if no transcript available, capture description + metadata only, set `status: transcript_unavailable`
- Transcript is cleaned (remove `[Music]`, `[Applause]` artifacts, normalize whitespace) before storage

#### Format Detection

```python
def detect_youtube_format(metadata: dict, transcript: str) -> str:
    """Classify video format from metadata and transcript signals."""
    title_lower = metadata.get('title', '').lower()
    description = metadata.get('description', '')
    duration_sec = metadata.get('duration_seconds', 0)
    channel_name = metadata.get('channel', '')

    # Interview: 2+ speakers indicated in title/description
    interview_signals = ['interview', 'conversation with', 'talks to',
                         'sits down with', 'in conversation', 'ep.', 'episode']
    if any(s in title_lower for s in interview_signals):
        return 'interview'

    # Panel: 3+ speakers, typically conferences
    panel_signals = ['panel', 'roundtable', 'discussion with', 'debate']
    if any(s in title_lower for s in panel_signals):
        return 'panel'

    # Lecture: single speaker, educational, >20min
    lecture_signals = ['lecture', 'talk at', 'keynote', 'masterclass', 'course']
    if any(s in title_lower for s in lecture_signals) or duration_sec > 2400:
        return 'lecture'

    # Tutorial: step-by-step, how-to
    tutorial_signals = ['tutorial', 'how to', 'step by step', 'guide',
                        'walkthrough', 'build a', 'create a']
    if any(s in title_lower for s in tutorial_signals):
        return 'tutorial'

    return 'video'  # default
```

#### Metadata via YouTube Data API
- `videos.list` for: title, channel, publishedAt, duration, description, tags, viewCount
- Quota cost: 1 unit per `videos.list` call (well within 10,000 units/day)
- Channel name normalized to lowercase slug for `creator` field

#### Clear-After-Ingest
- Liked videos: `videos.rate(id=VIDEO_ID, rating='none')` (removes like)
- Watch Later: `playlistItems.delete(id=PLAYLIST_ITEM_ID)` (removes from playlist)
- Clear only AFTER successful SOURCE-*.md write AND URL index insertion (two-phase commit)

#### Poll Cycle (6 hours)

```python
async def youtube_poll_cycle():
    """Single poll cycle for YouTube inbox zero."""
    # 1. Fetch current likes + watch later
    liked = fetch_liked_videos(max_results=50)
    watch_later = fetch_watch_later(max_results=50)
    candidates = deduplicate(liked + watch_later)

    # 2. Filter already-ingested
    new = [v for v in candidates if not url_index_contains(v['url'])]

    # 3. Ingest each
    for video in new:
        try:
            metadata = fetch_video_metadata(video['id'])
            transcript = fetch_transcript(video['id'])
            fmt = detect_youtube_format(metadata, transcript)

            source_file = generate_source_file(
                platform='youtube',
                format=fmt,
                creator=metadata['channel_slug'],
                date=metadata['published_at'],
                title=metadata['title'],
                content=transcript or metadata['description'],
                metadata=metadata
            )

            write_source_file(source_file)
            url_index_insert(video['url'], source_file.filename)

            # 4. Clear save (two-phase: only after confirmed write)
            if video in liked:
                remove_like(video['id'])
            if video in watch_later:
                remove_from_watch_later(video['playlist_item_id'])

            log_ingest('youtube', video['url'], source_file.filename, 'success')
        except TranscriptUnavailable:
            # Still ingest metadata, mark status
            source_file = generate_source_file(
                platform='youtube', format=fmt,
                creator=metadata['channel_slug'],
                date=metadata['published_at'],
                title=metadata['title'],
                content=metadata['description'],
                metadata=metadata,
                status='transcript_unavailable'
            )
            write_source_file(source_file)
            url_index_insert(video['url'], source_file.filename)
            remove_like_or_watch_later(video)
            log_ingest('youtube', video['url'], source_file.filename, 'transcript_unavailable')
        except Exception as e:
            log_ingest('youtube', video['url'], None, f'failed: {e}')
            # Do NOT clear save on failure -- retry next cycle
```

---

### X/Twitter Pipeline -- Two Tiers

X access is tiered by cost. Both tiers produce identical SOURCE-*.md output; they differ only in automation level and frequency.

#### Tier 1: Free (Manual Periodic)

```
X Bookmarks Export (monthly) → parse JSON → SOURCE-*.md → manual unbookmark
```

**Workflow:**
1. User downloads data archive from X Settings > "Your Account" > "Download an archive of your data" (monthly cadence)
2. Script watches `~/Downloads/` for `twitter-*.zip` or `x-*.zip` files
3. Extracts `data/bookmarks.json` (or `data/like.js` for liked tweets)
4. Parses each bookmark into SOURCE-*.md with full frontmatter
5. Deduplicates against URL index before writing
6. User manually clears bookmarks in X app (or keeps them -- no auto-clear at free tier)

```python
def parse_x_archive_bookmarks(archive_path: Path) -> list[dict]:
    """Parse bookmarks from X data archive ZIP."""
    import zipfile, json

    with zipfile.ZipFile(archive_path) as zf:
        # X archives use window.YTD.bookmark.part0 = [...]
        bookmark_files = [f for f in zf.namelist()
                          if 'bookmark' in f.lower() and f.endswith('.js')]
        bookmarks = []
        for bf in bookmark_files:
            raw = zf.read(bf).decode('utf-8')
            # Strip JS variable assignment prefix
            json_str = raw[raw.index('['):]
            entries = json.loads(json_str)
            for entry in entries:
                tweet = entry.get('tweet', entry)
                bookmarks.append({
                    'tweet_id': tweet['id'],
                    'text': tweet.get('full_text', tweet.get('text', '')),
                    'url': f"https://x.com/i/status/{tweet['id']}",
                    'created_at': tweet.get('created_at', ''),
                    'user': tweet.get('user', {}).get('screen_name', 'unknown'),
                    'user_display': tweet.get('user', {}).get('name', ''),
                    'media': extract_media_urls(tweet),
                    'quoted_tweet': extract_quoted(tweet),
                })
        return bookmarks
```

**Archive watch integration:**
- fswatch on `~/Downloads/` for `*.zip` matching `twitter-*` or `x-*`
- Auto-triggers extraction pipeline
- Processed archive moved to `04-SOURCES/_meta/archives/` for provenance

#### Tier 2: Automated ($100/mo X Basic API)

```
Bookmark → poll API (1h) → capture tweet → SOURCE-*.md → auto-unbookmark
```

**Authentication:**
- OAuth2 User Context (required for bookmark read/write)
- Scopes: `bookmark.read`, `bookmark.write`, `tweet.read`, `users.read`
- Token stored at `~/.syncrescendence/x_token.json` (gitignored)

**API Endpoints:**
- Fetch bookmarks: `GET /2/users/:id/bookmarks` (expansions: `author_id`, `referenced_tweets`)
- Remove bookmark: `DELETE /2/users/:id/bookmarks/:tweet_id`
- Rate limits: 180 requests / 15 min (bookmarks read), 50 requests / 15 min (bookmark delete)

**Capture depth:**
- Tweet text (full, not truncated)
- Media URLs (images, video thumbnails)
- Thread context: if tweet is part of a thread, fetch full thread via conversation_id
- Quoted tweets: recursively capture quoted tweet content
- Author metadata: handle, display name, bio snippet

**Poll Cycle (1 hour):**

```python
async def x_poll_cycle():
    """Single poll cycle for X/Twitter inbox zero (Tier 2)."""
    bookmarks = fetch_bookmarks(max_results=100)
    new = [b for b in bookmarks if not url_index_contains(b['url'])]

    for tweet in new:
        try:
            # Expand thread if applicable
            if tweet.get('conversation_id') and tweet['conversation_id'] != tweet['id']:
                thread = fetch_thread(tweet['conversation_id'])
                content = format_thread(thread)
                fmt = 'thread'
            else:
                content = tweet['text']
                fmt = 'article' if len(tweet['text']) > 800 else 'article'

            date = snowflake_to_date(int(tweet['id']))

            source_file = generate_source_file(
                platform='x',
                format=fmt,
                creator=tweet['author_handle'],
                date=date,
                title=synthesize_title(content[:500]),
                content=content,
                metadata={
                    'url': tweet['url'],
                    'author': f"{tweet['author_name']} (@{tweet['author_handle']})",
                    'media': tweet.get('media', []),
                    'quoted_tweet_url': tweet.get('quoted_url'),
                }
            )

            write_source_file(source_file)
            url_index_insert(tweet['url'], source_file.filename)

            # Clear bookmark (two-phase)
            remove_bookmark(tweet['id'])
            log_ingest('x', tweet['url'], source_file.filename, 'success')
        except Exception as e:
            log_ingest('x', tweet['url'], None, f'failed: {e}')
```

**Snowflake date extraction** reuses the existing `snowflake_to_date()` function from Stage 3 (Normalize). Zero API calls needed for date recovery.

---

### Manual Drop Pipeline

```
Drop .md into ~/Desktop/research/ → fswatch → normalize → SOURCE-*.md → delete original
```

**Mechanism:**
- `fswatch` monitors configured watch directories for new `.md` files
- On detection: copy to `_staging/`, run through Stage 1 (Ingest) → Stage 2 (Census) → Stage 3 (Normalize)
- Platform and format auto-classified from content (URL patterns, structural heuristics)
- Original file deleted from watch directory after successful ingest to `04-SOURCES/`
- Debounce: 5-second delay after file creation before processing (handles partial writes)

```bash
#!/bin/bash
# manual_drop_watcher.sh -- fswatch monitor for manual drops
WATCH_DIRS=("$HOME/Desktop/research" "$HOME/Downloads")
INGEST_SCRIPT="$SYNCRESCENDENCE_ROOT/04-SOURCES/_scripts/ingest.py"

fswatch -0 --event Created "${WATCH_DIRS[@]}" | while IFS= read -r -d '' file; do
    # Only process .md files
    [[ "$file" != *.md ]] && continue

    # Debounce: wait for file to finish writing
    sleep 5

    # Skip if file was already moved/deleted
    [[ ! -f "$file" ]] && continue

    echo "[$(date)] Ingesting manual drop: $file"
    python3 "$INGEST_SCRIPT" --source "$file" --clear-after-ingest

    if [[ $? -eq 0 ]]; then
        echo "[$(date)] Success. Original deleted."
    else
        echo "[$(date)] FAILED. Original preserved at: $file"
    fi
done
```

**launchd integration:**
- Runs as a launchd user agent on the MBA (Ajna's machine, where research drops land)
- Plist: `~/Library/LaunchAgents/com.syncrescendence.manual-drop-watcher.plist`
- Restarts on failure, logs to `~/Desktop/desktop/running_logs/manual_drop_watcher.log`

---

### Web Capture Pipeline (Future)

```
Browser extension → clip to watch folder → normalize → SOURCE-*.md
```

**Planned implementation:**
- MarkDownload browser extension (or similar) configured to save clips to `~/Desktop/research/`
- Extension captures: page title, URL, selected text or full article, publication date
- Saved as `.md` with basic frontmatter (title, url, date)
- Picked up by the Manual Drop Pipeline's fswatch monitor -- no separate infrastructure needed
- The web capture pipeline is a UX wrapper around manual drops, not a new pipeline

**Future enhancements:**
- Custom browser extension with platform-specific extractors (Medium, Substack, arXiv)
- Readability-mode extraction (strip nav, ads, sidebars) before saving
- Auto-tag from URL domain (substack.com → platform: substack)

---

### Shared Infrastructure

#### URL Index (`04-SOURCES/_meta/source_index.db` -- SQLite)

The URL index is the deduplication backbone for ALL input channels. Every pipeline checks it before processing. This is the same SQLite database defined in Stage 2 (Census), extended with inbox-zero-specific fields:

```sql
-- Extends existing source_index table with inbox_zero tracking
ALTER TABLE source_index ADD COLUMN ingest_source TEXT;
  -- Values: 'youtube_like', 'youtube_watch_later', 'x_bookmark_api',
  --         'x_archive', 'manual_drop', 'web_capture'

ALTER TABLE source_index ADD COLUMN save_cleared INTEGER DEFAULT 0;
  -- 0 = save still exists on platform, 1 = successfully cleared

ALTER TABLE source_index ADD COLUMN ingest_cycle TEXT;
  -- ISO timestamp of the poll cycle that ingested this URL

CREATE INDEX idx_ingest_source ON source_index(ingest_source);
CREATE INDEX idx_save_cleared ON source_index(save_cleared);
```

**Concurrency:** SQLite WAL mode enabled for safe concurrent reads from multiple poll cycles. Write serialization is automatic (SQLite handles this). Each pipeline opens its own connection; no shared connection pool needed.

```python
import sqlite3

def get_db_connection(db_path: str) -> sqlite3.Connection:
    """Get a WAL-mode SQLite connection for the URL index."""
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA busy_timeout=5000")
    conn.row_factory = sqlite3.Row
    return conn
```

#### Enrichment Queue

New SOURCE-*.md files land with `status: raw` (or `status: transcript_unavailable` for YouTube fallbacks). The enrichment daemon processes them on a 2-hour cycle:

1. Scan `04-SOURCES/SOURCE-*.md` for files with `status: raw` or `status: transcript_unavailable`
2. Batch into groups of 25 (respecting the existing Stage 4 batch configuration)
3. Run Claude API enrichment: synopsis, topics, teleology, signal_tier, notebooklm_category, aliases
4. Update frontmatter `status` to `enriched` on success, `enrich_failed` on failure
5. Log batch results to `_meta/ENRICHMENT_LOG.md`
6. Trigger MOC rebuild on batch completion

```python
async def enrichment_cycle():
    """Single enrichment cycle -- finds raw files and enriches them."""
    source_dir = Path('04-SOURCES/')
    raw_files = []

    for f in source_dir.glob('SOURCE-*.md'):
        fm = parse_frontmatter(f.read_text())
        if fm.get('status') in ('raw', 'transcript_unavailable'):
            raw_files.append(f)

    if not raw_files:
        log('enrichment', 'No raw files to process.')
        return

    log('enrichment', f'Found {len(raw_files)} files to enrich.')

    # Process in batches
    for i in range(0, len(raw_files), BATCH_SIZE):
        batch = raw_files[i:i + BATCH_SIZE]
        await enrich_batch(batch)  # Uses existing Stage 4 enrich_batch()

    # Trigger MOC rebuild
    rebuild_mocs()
    log('enrichment', f'Cycle complete. {len(raw_files)} files processed.')
```

#### MOC Auto-Rebuild

After any enrichment batch completes, all MOC files are regenerated:

- Uses the existing Stage 5 (Index) logic
- Incremental mode: compare current MOC content hash against regenerated content; skip write if unchanged
- Full rebuild is fast enough at <1000 files (~2 seconds) that incremental optimization is optional
- Rebuild also regenerates `DYN-SOURCES.csv` for external tooling

---

### Polling Schedule

| Pipeline | Frequency | Method | Machine |
|----------|-----------|--------|---------|
| YouTube Likes/Watch Later | Every 6 hours | launchd | MBA (Ajna) |
| X Bookmarks (Tier 2) | Every 1 hour | launchd | MBA (Ajna) |
| X Bookmarks (Tier 1) | Monthly manual | User triggers archive download | MBA (Ajna) |
| Manual drops | Real-time | fswatch | MBA (Ajna) |
| Enrichment | Every 2 hours | launchd | MBA (Ajna) |
| MOC rebuild | After enrichment | Chained (subprocess) | MBA (Ajna) |

All pipelines run on the MBA because that is where:
- Browser sessions live (X bookmarks, YouTube likes originate here)
- Research files are dropped (Desktop, Downloads)
- Ajna (CSO) orchestrates strategic intake

**launchd plists** (all under `~/Library/LaunchAgents/`):

| Plist | Schedule |
|-------|----------|
| `com.syncrescendence.youtube-ingest.plist` | `StartInterval: 21600` (6h) |
| `com.syncrescendence.x-ingest.plist` | `StartInterval: 3600` (1h) |
| `com.syncrescendence.manual-drop-watcher.plist` | `KeepAlive: true` (persistent fswatch) |
| `com.syncrescendence.enrichment.plist` | `StartInterval: 7200` (2h) |

Each plist must include `EnvironmentVariables` for `SYNCRESCENDENCE_ROOT`, `PATH`, and API token paths. Do NOT rely on `~/.zshrc` -- launchd does not source it.

---

### Configuration

Extends the existing `anneal` configuration block:

```yaml
inbox_zero:
  youtube:
    enabled: true
    poll_interval_hours: 6
    clear_after_ingest: true
    token_path: "~/.syncrescendence/youtube_token.json"
    transcript_fallback: "description_only"
    sources:
      - "liked_videos"
      - "watch_later"
    max_per_cycle: 50
    transcript_cleanup:
      strip_artifacts: true   # Remove [Music], [Applause], etc.
      normalize_whitespace: true
      min_transcript_length: 100  # chars; below this, treat as unavailable

  twitter:
    tier: "free"  # "free" or "basic_api"
    poll_interval_hours: 1  # only used when tier=basic_api
    clear_after_ingest: true
    token_path: "~/.syncrescendence/x_token.json"
    archive_watch_path: "~/Downloads/"
    archive_patterns:
      - "twitter-*.zip"
      - "x-*.zip"
    max_per_cycle: 100
    capture_threads: true   # Expand threads via conversation_id
    capture_quoted: true    # Include quoted tweet content

  manual:
    watch_dirs:
      - "~/Desktop/research/"
      - "~/Downloads/"
    watch_extensions:
      - ".md"
    debounce_seconds: 5
    clear_after_ingest: true

  web_capture:
    enabled: false  # Future: enable when browser extension configured
    watch_dir: "~/Desktop/research/"
    extension: "markdownload"

  enrichment:
    enabled: true
    poll_interval_hours: 2
    model: "claude-sonnet-4-6"
    batch_size: 25
    max_concurrent: 4
    api_key_path: "~/.syncrescendence/anthropic_key.txt"
    retry_max: 3
    retry_delay_seconds: 30
    trigger_moc_rebuild: true

  logging:
    ingest_log: "04-SOURCES/_meta/INGEST_LOG.md"
    enrichment_log: "04-SOURCES/_meta/ENRICHMENT_LOG.md"
    error_log: "04-SOURCES/_meta/INBOX_ZERO_ERRORS.md"
```

---

### Error Recovery

| Failure Mode | Response | Retry Strategy | User Alert |
|-------------|----------|----------------|------------|
| Transcript unavailable | Ingest with description only, set `status: transcript_unavailable` | No retry (permanent state) | None |
| Transcript fetch failed | Mark `status: transcript_failed` | Retry next cycle (transient) | After 3 consecutive failures |
| Enrichment failed | Mark `status: enrich_failed` | Exponential backoff: 2h, 4h, 8h, then manual | After 3 retries |
| Duplicate URL | Skip silently | N/A | Logged to `_meta/INGEST_LOG.md` |
| API rate limit hit | Pause current cycle, resume next scheduled cycle | Automatic (launchd reschedules) | None |
| OAuth token expired | Pause pipeline, write alert to `-SOVEREIGN/` | No retry until re-auth | Immediate (blocks pipeline) |
| YouTube API quota exhausted | Pause YouTube pipeline for 24h | Auto-resume next day | Logged |
| X API error (5xx) | Retry with exponential backoff within current cycle | 3 retries, then defer to next cycle | After 3 consecutive cycle failures |
| SQLite index corruption | Rebuild from filesystem scan (`anneal.py rebuild-index`) | Automatic detection via integrity check | Immediate |
| fswatch crash | launchd auto-restarts (KeepAlive: true) | Automatic | Logged to running_logs |
| Network connectivity loss | All API pipelines skip cycle, manual drops unaffected | Next cycle retry | None (transient) |

**Two-phase commit protocol for clear-after-ingest:**

```python
def safe_ingest_and_clear(item, platform_clear_fn):
    """Ensures save is only cleared after confirmed ingest."""
    # Phase 1: Write source file + index entry
    source_file = generate_and_write_source(item)
    url_index_insert(item['url'], source_file.filename)

    # Phase 2: Verify write succeeded
    if not source_file.path.exists():
        raise IngestError(f"Source file not found after write: {source_file.path}")
    if not url_index_contains(item['url']):
        raise IngestError(f"URL not in index after insert: {item['url']}")

    # Phase 3: Clear save on platform (only after verified write)
    try:
        platform_clear_fn(item)
        url_index_update(item['url'], save_cleared=1)
    except Exception as e:
        # Save NOT cleared -- will be re-processed next cycle
        # but URL index prevents duplicate SOURCE file creation
        log_error(f"Clear failed for {item['url']}: {e}. Will retry next cycle.")
```

This guarantees: no SOURCE file is lost (phase 1 persists before phase 3), no save is cleared without a persisted SOURCE file, and duplicate processing is idempotent (URL index prevents double-writes).

---

### Operational Metrics

Track these to validate inbox-zero health:

| Metric | Target | Check |
|--------|--------|-------|
| YouTube likes pending | < 5 at any time | `youtube_ingest.py --status` |
| X bookmarks pending (Tier 2) | < 10 at any time | `x_ingest.py --status` |
| Files with `status: raw` | < 25 (one enrichment batch) | `grep -l 'status: raw' 04-SOURCES/SOURCE-*.md \| wc -l` |
| Files with `status: enrich_failed` | 0 (after retry cycles) | `grep -l 'status: enrich_failed' 04-SOURCES/SOURCE-*.md \| wc -l` |
| Ingest errors per week | < 5 | `_meta/INBOX_ZERO_ERRORS.md` tail |
| URL index integrity | 100% match to filesystem | `anneal.py check-index` |
| Mean time from save to enriched | < 8 hours | Computed from `date_ingested` vs enrichment timestamp |

---

### Implementation Priority (Inbox Zero Specific)

| Priority | Component | Effort | Dependency |
|----------|-----------|--------|------------|
| IZ-1 | YouTube OAuth2 setup + token storage | 2 hours | None |
| IZ-2 | `youtube_ingest.py` (poll + transcript + clear) | 6 hours | IZ-1, existing URL index |
| IZ-3 | YouTube launchd plist | 1 hour | IZ-2 |
| IZ-4 | X archive parser (Tier 1 free) | 3 hours | Existing URL index |
| IZ-5 | Manual drop fswatch watcher + launchd plist | 2 hours | Existing ingest.py |
| IZ-6 | Enrichment daemon + launchd plist | 3 hours | Existing enrich batch |
| IZ-7 | MOC auto-rebuild chaining | 1 hour | IZ-6, existing MOC generator |
| IZ-8 | X API integration (Tier 2, when/if subscribed) | 4 hours | IZ-4 patterns |
| IZ-9 | Web capture extension config | 1 hour | IZ-5 (reuses fswatch) |
| IZ-10 | Operational dashboard (`--status` flags) | 2 hours | IZ-2, IZ-4, IZ-6 |

**Total estimated implementation: ~25 hours.**

IZ-1 through IZ-3 deliver the highest-value pipeline (YouTube) end-to-end. IZ-4 and IZ-5 cover the two free intake channels. IZ-6 and IZ-7 close the enrichment loop. IZ-8 and IZ-9 are quality-of-life upgrades gated on cost decisions (X API) or tooling maturity (browser extensions).

---

## Cloud Offload Roadmap (GCP)

The pipeline progresses from fully local to fully cloud-hosted in three phases. Each phase is independently operational — no phase requires the next to function.

### Phase 1: LOCAL (CURRENT)

The current operational state. All processing runs on the MBA via launchd services.

- **Polling/ingest**: launchd periodic jobs on MBA (Ajna's machine)
- **Transcript fetch**: `youtube-transcript-api` v1.x (`api.fetch()` / `transcript.snippets`)
- **Storage**: Flat SOURCE-*.md files in `04-SOURCES/`, flat file dedup by filename
- **Enrichment**: Claude subagent enrichment via Anthropic API
- **Scheduling**: launchd plists (`StartInterval`, `KeepAlive`)
- **Proven at scale**: 1,158 YouTube videos drained in a single batch operation

### Phase 2: HYBRID (NEXT)

Local polling remains, but storage and enrichment shift to cloud-native tools.

- **SQLite URL index** replacing flat file dedup (schema already designed in Stage 2 Census)
- **Gemini Flash API** for enrichment — cheaper than Claude for bulk processing, multimodal capable (per CANON-25200 task routing and `SYNTHESIS-platform_topology_jan2026.md` token economics)
- **Google Drive as staging area** — files land in Drive, sync to local via Google Drive for Desktop, then git commit
- **Still local polling** via launchd — minimizes infrastructure change while gaining cloud enrichment cost savings
- **Key migration**: enrichment model switch from `claude-sonnet-4-6` to Gemini Flash for cost-effective batch runs; Claude reserved for high-signal paradigm-tier sources

### Phase 3: FULLY OFFLOADED (TARGET)

Zero local dependencies except `git pull`. The MBA becomes a thin client that reads the repo.

- **GCP Cloud Functions / Cloud Run** for all polling + ingest jobs (replaces launchd entirely)
- **Gemini native YouTube URL processing** — visual + audio multimodal analysis, not just captions. Captures code on screen, diagrams, visual demos. 263 tok/sec native multimodal (per CANON-25200)
- **Vertex AI RAG Engine** for embeddings + semantic search over the SOURCE corpus
- **Cloud Storage** for SOURCE-*.md staging → automated `git push` to repo via Cloud Build trigger
- **Cloud Scheduler** replacing launchd cron-style polling (identical semantics, zero local dependency)
- **Colab-to-Claude bridge** pattern (per `SYNTHESIS-gemini-cli.md`) for hybrid enrichment: Gemini bulk pass → Claude deep pass on flagged sources
- **Zero local dependencies** except `git pull` to consume the enriched corpus

### Reference Documents

| Document | Relevance |
|----------|-----------|
| `01-CANON/sn/CANON-25200` | Task routing decision: "YouTube processing → Gemini" |
| `05-SIGMA/syntheses/SYNTHESIS-gemini-cli.md` | Colab-to-Claude bridge pattern for hybrid enrichment |
| `05-SIGMA/syntheses/SYNTHESIS-platform_topology_jan2026.md` | Token economics and cost comparison across models |

---

*This mechanism document is the automation blueprint for the Source Anneal pipeline. It should be updated as implementation progresses and operational lessons accumulate.*
