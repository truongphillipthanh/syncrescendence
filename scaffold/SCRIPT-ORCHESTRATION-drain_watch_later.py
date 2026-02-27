#!/usr/bin/env python3
"""
Watch Later Bootstrap Drain — yt-dlp + YouTube Data API + youtube-transcript-api

Drains YouTube Watch Later playlist via yt-dlp (browser cookie extraction),
fetches metadata via YouTube Data API, fetches transcripts, and generates
SOURCE-*.md files compatible with the Syncrescendence ingest pipeline.

REQUIREMENTS:
  - yt-dlp (in venv at ~/.syncrescendence/venv/)
  - youtube-transcript-api >= 1.0 (same venv)
  - requests (same venv)
  - YouTube Data API key (hardcoded or via --api-key)

IMPORTANT — BROWSER MUST BE CLOSED:
  yt-dlp --cookies-from-browser reads the browser's cookie database directly.
  Chrome (and most browsers) lock this file while running. You MUST quit Chrome
  (or whichever browser you specify) before running this script. If the script
  hangs at the "Extracting Watch Later" step, this is almost certainly why.

  Alternative: export cookies to a Netscape-format file and use --cookies-file.
    yt-dlp --cookies-from-browser chrome --cookies cookies.txt "https://example.com"
  Then re-run with: --cookies-file cookies.txt

Usage:
  python drain_watch_later.py
  python drain_watch_later.py --dry-run
  python drain_watch_later.py --cookies-from-browser firefox
  python drain_watch_later.py --cookies-file ~/cookies.txt
  python drain_watch_later.py --remove-after
"""
from config import *

import argparse
import json
import logging
import os
import re
import sqlite3
import subprocess
import sys
import unicodedata
from datetime import datetime
from pathlib import Path

LOG_FORMAT = "%(asctime)s [%(levelname)s] %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
log = logging.getLogger("drain_watch_later")

# ---------------------------------------------------------------------------
# Defaults
# ---------------------------------------------------------------------------

VENV_DIR = Path.home() / ".syncrescendence" / "venv"
YT_DLP = VENV_DIR / "bin" / "yt-dlp"

REPO_DIR = Path(__file__).resolve().parent.parent.parent
SOURCES_DIR = REPO_DIR / "sources"
URL_INDEX_PATH = SOURCES_DIR / "_meta" / "URL_INDEX.txt"

YOUTUBE_API_KEY = "AIzaSyCOnSjn4inSv3BRip0Gaum4d-j-AqCqgR0"
WATCH_LATER_URL = "https://www.youtube.com/playlist?list=WL"

# ---------------------------------------------------------------------------
# URL Index (dedup gate)
# ---------------------------------------------------------------------------

SOURCE_INDEX_DB = SOURCES_DIR / "_meta" / "source_index.db"


def _sqlite_url_set() -> set | None:
    """Load all URLs from SQLite index, or None if DB doesn't exist."""
    if not SOURCE_INDEX_DB.exists():
        return None
    try:
        conn = sqlite3.connect(str(SOURCE_INDEX_DB))
        conn.execute("PRAGMA journal_mode=WAL")
        urls = {r[0] for r in conn.execute("SELECT url FROM source_index").fetchall()}
        conn.close()
        return urls
    except Exception:
        return None


def _sqlite_insert(url: str, filename: str = "", **kwargs):
    """Insert a URL into the SQLite index (upsert)."""
    if not SOURCE_INDEX_DB.exists():
        return
    try:
        conn = sqlite3.connect(str(SOURCE_INDEX_DB))
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute(
            """INSERT INTO source_index (url, filename, platform, format, creator, date_published, ingest_source)
               VALUES (?, ?, ?, ?, ?, ?, ?)
               ON CONFLICT(url) DO UPDATE SET filename=excluded.filename""",
            (url, filename,
             kwargs.get("platform", "youtube"),
             kwargs.get("format"),
             kwargs.get("creator"),
             kwargs.get("date_published"),
             "drain_watch_later"),
        )
        conn.commit()
        conn.close()
    except Exception:
        pass


def load_url_index() -> set:
    db_urls = _sqlite_url_set()
    if db_urls is not None:
        return db_urls
    # Fallback to flat file
    if not URL_INDEX_PATH.exists():
        return set()
    return {line.strip() for line in URL_INDEX_PATH.read_text().splitlines() if line.strip()}


def append_to_url_index(url: str, filename: str = "", **kwargs):
    URL_INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(URL_INDEX_PATH, "a") as f:
        f.write(url + "\n")
    _sqlite_insert(url, filename=filename, **kwargs)

# ---------------------------------------------------------------------------
# yt-dlp Watch Later extraction
# ---------------------------------------------------------------------------

def extract_watch_later(cookies_from_browser: str = "chrome",
                        cookies_file: str = None) -> list:
    """Use yt-dlp --flat-playlist to get video entries from Watch Later."""
    cmd = [str(YT_DLP)]

    if cookies_file:
        cmd += ["--cookies", cookies_file]
    else:
        cmd += ["--cookies-from-browser", cookies_from_browser]

    cmd += ["--flat-playlist", "-j", WATCH_LATER_URL]

    log.info("Running: %s", " ".join(cmd))
    log.info("(If this hangs, quit your browser — it locks the cookie DB)")

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)

    if result.returncode != 0:
        log.error("yt-dlp failed (exit %d):\n%s", result.returncode, result.stderr)
        sys.exit(1)

    entries = []
    for line in result.stdout.strip().splitlines():
        if line.strip():
            try:
                entries.append(json.loads(line))
            except json.JSONDecodeError:
                log.warning("Skipping unparseable line: %s", line[:100])
    return entries

# ---------------------------------------------------------------------------
# YouTube Data API metadata
# ---------------------------------------------------------------------------

def fetch_video_metadata(video_id: str, api_key: str) -> dict | None:
    """Fetch video snippet + contentDetails via YouTube Data API v3."""
    import requests
    url = "https://www.googleapis.com/youtube/v3/videos"
    params = {
        "part": "snippet,contentDetails,statistics",
        "id": video_id,
        "key": api_key,
    }
    try:
        resp = requests.get(url, params=params, timeout=15)
        resp.raise_for_status()
        items = resp.json().get("items", [])
        return items[0] if items else None
    except Exception as e:
        log.warning("API metadata fetch failed for %s: %s", video_id, e)
        return None

# ---------------------------------------------------------------------------
# Transcript
# ---------------------------------------------------------------------------

def fetch_transcript(video_id: str) -> str | None:
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id)
        return "\n".join(s.text for s in transcript.snippets)
    except ImportError:
        log.warning("youtube-transcript-api not installed. Skipping transcript.")
        return None
    except Exception as e:
        log.warning("Transcript unavailable for %s: %s", video_id, e)
        return None

# ---------------------------------------------------------------------------
# Filename & frontmatter (mirrors youtube_ingest.py)
# ---------------------------------------------------------------------------

def slugify(text: str, max_len: int = 60) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = text.strip("_")
    if len(text) > max_len:
        text = text[:max_len].rstrip("_")
    return text


def classify_format(title: str, description: str) -> str:
    lower = (title + " " + description).lower()
    if any(w in lower for w in ["interview", "conversation with", "talks to", "sits down with"]):
        return "interview"
    if any(w in lower for w in ["lecture", "talk at", "keynote", "presentation"]):
        return "lecture"
    if any(w in lower for w in ["panel", "roundtable", "discussion"]):
        return "panel"
    if any(w in lower for w in ["tutorial", "how to", "walkthrough"]):
        return "tutorial"
    return "lecture"


def iso_duration_to_human(duration: str) -> str:
    match = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", duration or "")
    if not match:
        return duration or "unknown"
    h, m, s = (int(x) if x else 0 for x in match.groups())
    parts = []
    if h: parts.append(f"{h}h")
    if m: parts.append(f"{m}m")
    if s: parts.append(f"{s}s")
    return " ".join(parts) or "0s"


def generate_source_file(video_id: str, snippet: dict, content_details: dict,
                         transcript: str | None, seq: int) -> Path:
    title = snippet.get("title", "Untitled")
    channel = snippet.get("channelTitle", "unknown")
    published = snippet.get("publishedAt", "")[:10]
    description = snippet.get("description", "")
    duration = iso_duration_to_human(content_details.get("duration", ""))
    url = f"https://www.youtube.com/watch?v={video_id}"

    date_str = published.replace("-", "") if published else datetime.now().strftime("%Y%m%d")
    fmt = classify_format(title, description)
    creator_slug = slugify(channel, max_len=30)
    title_slug = slugify(title, max_len=60)

    filename = f"SOURCE-{date_str}-youtube-{fmt}-{creator_slug}-{title_slug}.md"
    filepath = SOURCES_DIR / filename

    if filepath.exists():
        filename = f"SOURCE-{date_str}-youtube-{fmt}-{creator_slug}-{title_slug}_{seq}.md"
        filepath = SOURCES_DIR / filename

    today = datetime.now().strftime("%Y-%m-%d")
    source_id = f"SOURCE-{date_str}-{seq:03d}"

    body = transcript if transcript else description
    body_label = "Transcript" if transcript else "Description (no transcript available)"
    has_transcript = "yes" if transcript else "no"

    frontmatter = f"""---
id: {source_id}
platform: youtube
format: {fmt}
cadence: evergreen
value_modality: {"dialogue_primary" if fmt in ("interview", "panel") else "audio_primary"}
signal_tier: null
status: raw
chain: null
topics: []
creator: "{channel}"
guest: null
title: "{title}"
url: "{url}"
date_published: {published or "null"}
date_processed: {today}
date_integrated: null
processing_function: transcribe_youtube
integrated_into: []
duration: "{duration}"
has_transcript: {has_transcript}
synopsis: null
key_insights: []
visual_notes: null
---"""

    content = f"""{frontmatter}

# {title}

**Channel**: {channel}
**Published**: {published or "unknown"}
**Duration**: {duration}
**URL**: {url}

## {body_label}

{body}
"""
    filepath.write_text(content, encoding="utf-8")
    return filepath

# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def run(args):
    known_urls = load_url_index()
    log.info("Loaded %d known URLs from dedup index", len(known_urls))

    # Extract Watch Later via yt-dlp or load from pre-dumped JSONL
    if args.jsonl_dump:
        log.info("Loading pre-dumped JSONL from %s", args.jsonl_dump)
        entries = []
        with open(args.jsonl_dump) as f:
            for line in f:
                if line.strip():
                    try:
                        entries.append(json.loads(line))
                    except json.JSONDecodeError:
                        pass
    else:
        entries = extract_watch_later(
            cookies_from_browser=args.cookies_from_browser,
            cookies_file=args.cookies_file,
        )
    total = len(entries)
    log.info("Watch Later contains %d videos", total)

    if total == 0:
        log.info("Nothing to drain.")
        return

    ingested = 0
    skipped = 0
    failed = 0

    for seq, entry in enumerate(entries, start=1):
        video_id = entry.get("id") or entry.get("url", "").split("?v=")[-1]
        if not video_id:
            log.warning("No video ID in entry: %s", json.dumps(entry)[:200])
            failed += 1
            continue

        url = f"https://www.youtube.com/watch?v={video_id}"
        yt_dlp_title = entry.get("title", "?")

        if url in known_urls:
            log.info("SKIP [%d/%d] (indexed): %s -- %s", seq, total, video_id, yt_dlp_title)
            skipped += 1
            continue

        if args.dry_run:
            log.info("DRY-RUN [%d/%d] would ingest: %s -- %s", seq, total, video_id, yt_dlp_title)
            ingested += 1
            continue

        log.info("INGEST [%d/%d]: %s -- %s", seq, total, video_id, yt_dlp_title)

        # Fetch full metadata from YouTube Data API
        meta = fetch_video_metadata(video_id, args.api_key)
        if not meta:
            # Fallback: use yt-dlp metadata (less structured but functional)
            log.warning("API metadata unavailable, using yt-dlp data for %s", video_id)
            snippet = {
                "title": yt_dlp_title,
                "channelTitle": entry.get("channel", entry.get("uploader", "unknown")),
                "publishedAt": entry.get("upload_date", ""),
                "description": entry.get("description", ""),
            }
            # Convert upload_date YYYYMMDD -> YYYY-MM-DD
            ud = snippet["publishedAt"]
            if ud and len(ud) == 8 and ud.isdigit():
                snippet["publishedAt"] = f"{ud[:4]}-{ud[4:6]}-{ud[6:8]}"

            dur_secs = entry.get("duration")
            if dur_secs and isinstance(dur_secs, (int, float)):
                h, rem = divmod(int(dur_secs), 3600)
                m, s = divmod(rem, 60)
                content_details = {"duration": f"PT{h}H{m}M{s}S"}
            else:
                content_details = {"duration": ""}
        else:
            snippet = meta["snippet"]
            content_details = meta["contentDetails"]

        # Transcript
        transcript = fetch_transcript(video_id)

        # Generate SOURCE file
        try:
            filepath = generate_source_file(video_id, snippet, content_details, transcript, seq)
            log.info("  -> %s", filepath.name)
        except Exception as e:
            log.error("  FAILED to write SOURCE for %s: %s", video_id, e)
            failed += 1
            continue

        # Update dedup index
        append_to_url_index(url)
        known_urls.add(url)
        ingested += 1

        # Remove from Watch Later (if requested)
        if args.remove_after:
            log.warning(
                "  --remove-after: yt-dlp does NOT support removing videos from playlists. "
                "YouTube Data API deprecated Watch Later (WL) playlist mutation in 2016. "
                "Manual removal required."
            )

    # Summary
    log.info("=" * 60)
    log.info("DRAIN COMPLETE")
    log.info("  Total in Watch Later: %d", total)
    log.info("  Already indexed (skipped): %d", skipped)
    log.info("  Newly ingested: %d", ingested)
    log.info("  Failed: %d", failed)
    log.info("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Drain YouTube Watch Later via yt-dlp + Data API + transcripts"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="List what would be ingested without writing files",
    )
    parser.add_argument(
        "--cookies-from-browser", default="chrome",
        help="Browser for yt-dlp cookie extraction (default: chrome). BROWSER MUST BE CLOSED.",
    )
    parser.add_argument(
        "--cookies-file", default=None,
        help="Path to Netscape-format cookies file (alternative to --cookies-from-browser)",
    )
    parser.add_argument(
        "--jsonl-dump", default=None,
        help="Path to pre-dumped JSONL file from yt-dlp --flat-playlist -j (skips extraction)",
    )
    parser.add_argument(
        "--api-key", default=YOUTUBE_API_KEY,
        help="YouTube Data API key (default: built-in key)",
    )
    parser.add_argument(
        "--remove-after", action="store_true",
        help="Attempt to remove videos from Watch Later after ingest. "
             "NOTE: Not supported by yt-dlp or YouTube API for WL. Logged as warning.",
    )
    parser.add_argument(
        "--sources-dir", type=Path, default=None,
        help=f"Override sources directory (default: {SOURCES_DIR})",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="Enable debug logging",
    )
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    if args.sources_dir:
        import drain_watch_later as _self
        _self.SOURCES_DIR = args.sources_dir
        _self.URL_INDEX_PATH = args.sources_dir / "_meta" / "URL_INDEX.txt"

    run(args)


if __name__ == "__main__":
    main()
