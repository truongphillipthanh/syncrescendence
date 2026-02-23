> **STATUS: SUPERSEDED** — This research document was written 2026-02-02 before the Source Anneal operation.
> The authoritative pipeline architecture is now in `MECH-source_anneal_pipeline.md`.
> Retained for historical reference only.

# YouTube Ingestion Pipeline Architecture Research

**Date:** 2026-02-02
**Type:** Research Synthesis
**Purpose:** Map the optimal pipeline for ingesting 942 Watch Later videos into the Syncrescendence knowledge system
**Sources:** Web research, tool documentation, cost modeling (2025-2026)

---

## 1. Key Finding: "Antigravity" Is Not a YouTube Tool

"Antigravity" is Google's AI-powered agentic IDE announced November 2025 alongside Gemini 3. It is a software development tool (competitor to Cursor, Windsurf, Replit Agent), not a YouTube ingestion tool. It has no relevance to the YouTube pipeline use case.

**Implication:** The YouTube pipeline must be built from component tools, not from a single product.

---

## 2. Recommended Architecture: 4-Stage Pipeline

```
Stage 1: EXPORT         Stage 2: TRANSCRIBE       Stage 3: PROCESS         Stage 4: KNOWLEDGE BASE
────────────────       ────────────────────       ─────────────────       ──────────────────────
YouTube Watch Later    yt-dlp transcript          Gemini Flash-Lite       Obsidian vault
→ Export playlist      extraction (free)          API batch processing    structured markdown
  metadata                                        (~$10 for 942 vids)    with backlinks
```

### Stage 1: Export — Get Video Metadata

**Tool:** YouTube Data API v3 or yt-dlp `--flat-playlist`

- Extract: video ID, title, channel, duration, description, upload date
- Export format: JSON or CSV
- Cost: Free (API quota or yt-dlp)
- Output: `playlist_manifest.json` with 942 entries

### Stage 2: Transcribe — Extract Text From Videos

**Primary Tool:** yt-dlp with `--write-auto-sub --sub-lang en --skip-download`

- Extracts YouTube's auto-generated captions (available for ~95% of English videos)
- No audio download needed — pure metadata extraction
- Cost: Free
- Throughput: ~10 videos/second (metadata only)
- Output: `.vtt` or `.srt` files per video

**Fallback:** For videos without captions:
- Download audio with yt-dlp → Whisper (local) or Gemini API transcription
- Affects ~5% of videos (estimated 47 of 942)

### Stage 3: Process — AI-Powered Knowledge Extraction

**Primary Tool:** Gemini 2.0 Flash-Lite API

- Input: Transcript text + video metadata
- Processing: Extract key concepts, arguments, quotes, actionable insights
- Cost model:
  - Average transcript: ~5,000 tokens input
  - Flash-Lite pricing: $0.075/M input, $0.30/M output
  - Per video: ~$0.001 input + ~$0.0003 output ≈ $0.0013
  - **942 videos: ~$1.22**
  - With prompt overhead and retries: **~$5-10 total**

**Alternative:** Gemini API with native YouTube URL support
- Can process YouTube URLs directly (no yt-dlp needed for transcription)
- Higher cost: ~$14 for 942 videos (uses full video context)
- Advantage: Captures visual information, not just audio

**Processing Prompt Structure:**
```
Given this video transcript and metadata, extract:
1. Core thesis/argument (1-2 sentences)
2. Key concepts introduced (bullet list)
3. Notable quotes (with approximate timestamps)
4. Actionable insights (what to do differently)
5. Connections to themes: [list of 3-5 Syncrescendence themes]
6. Quality rating: essential / valuable / background / skip
```

### Stage 4: Knowledge Base — Obsidian Integration

**Output format:** One markdown file per video in `sources/research/youtube/`

```markdown
---
source: youtube
video_id: {id}
title: {title}
channel: {channel}
duration: {duration}
quality: {rating}
themes: [{theme_list}]
processed: 2026-02-XX
---

# {title}

## Core Thesis
{extracted_thesis}

## Key Concepts
{bullet_list}

## Notable Quotes
{timestamped_quotes}

## Actionable Insights
{insights}

## Connections
{backlinks_to_canon_or_sigma}
```

---

## 3. Tool Comparison Matrix

| Tool | Role | Cost | Pros | Cons |
|------|------|------|------|------|
| yt-dlp | Transcript extraction | Free | Fast, reliable, no API key needed | No visual analysis |
| YouTube Data API v3 | Metadata export | Free (quota) | Official, structured data | Requires API key setup |
| Gemini Flash-Lite | AI processing | ~$5-10 | Cheapest per-token, fast | Text-only input |
| Gemini 2.0 Flash | AI processing (visual) | ~$14 | Native YouTube URL support | Higher cost |
| Whisper (local) | Fallback transcription | Free (compute) | Works on any audio | Slow, requires GPU |
| Claude API | AI processing | ~$30-50 | Highest quality extraction | Most expensive option |

---

## 4. Implementation Plan

### Phase 1: Setup (one-time)
1. Install yt-dlp: `brew install yt-dlp`
2. Export Watch Later playlist (requires browser cookies or YouTube Takeout)
3. Set up Google AI API key (Account 2 — already have AI Pro)

### Phase 2: Extraction (batch)
1. Run yt-dlp to extract all 942 transcripts
2. Log failures (no captions available)
3. For failures: download audio → Whisper transcription

### Phase 3: Processing (batch)
1. Write Python script: `youtube_ingest.py`
   - Reads transcript + metadata
   - Calls Gemini Flash-Lite API with extraction prompt
   - Writes structured markdown per video
2. Run in batches of 50 (respect rate limits)
3. Estimated total: ~$5-10 API cost

### Phase 4: Integration
1. Import markdown files to Obsidian vault
2. Create index by channel, theme, quality rating
3. Identify high-value videos for deeper CANON integration
4. Dispatch extraction tasks to Ajna/Psyche for CANON-worthy content

---

## 5. Cost Summary

| Approach | Total Cost | Quality | Speed |
|----------|-----------|---------|-------|
| yt-dlp + Flash-Lite (recommended) | ~$5-10 | Good | Fast |
| Gemini native YouTube URL | ~$14 | Better (visual) | Medium |
| yt-dlp + Claude API | ~$30-50 | Best | Slow |
| Full manual review | $0 | Perfect | Very slow |

**Recommendation:** Start with yt-dlp + Flash-Lite for the bulk run (~$5-10). Flag "essential" rated videos for secondary processing via Gemini native URL or Claude API for deeper extraction.

---

## 6. Dependencies

- **Sovereign action needed:** Google AI API key activation on Account 2
- **Sovereign action needed:** YouTube Watch Later export (requires authenticated browser session)
- **Blocks:** None from repo side — script can be written immediately
- **Blocked by:** API key (SOVEREIGN-009 Decision #1 scope)

---

*Research conducted 2026-02-02. Primary sources: yt-dlp documentation, Google AI pricing (Jan 2026), YouTube Data API v3 reference, Gemini API capabilities matrix.*
