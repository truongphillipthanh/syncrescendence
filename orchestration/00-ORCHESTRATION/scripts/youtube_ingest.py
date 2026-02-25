#!/usr/bin/env python3
"""
YouTube Stateless Ingest Pipeline for Syncrescendence.

Authenticates via OAuth2, polls Liked Videos (and optionally a named playlist),
transcribes each video, generates SOURCE-*.md files, and optionally removes
videos from the playlist after successful ingest.

Usage:
  python youtube_ingest.py
  python youtube_ingest.py --clear-after-ingest
  python youtube_ingest.py --playlist PLxxxxxx --max-results 50
  python youtube_ingest.py --dry-run
"""
from config import *

import argparse
import json
import logging
import os
import re
import sqlite3
import sys
import unicodedata
from datetime import datetime
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build as build_youtube

try:
    from youtube_transcript_api import YouTubeTranscriptApi
    HAS_TRANSCRIPT_API = True
except ImportError:
    HAS_TRANSCRIPT_API = False

# ---------------------------------------------------------------------------
# Paths & defaults
# ---------------------------------------------------------------------------

SYNCRESCENDENCE_DIR = Path(os.environ.get(
    "SYNCRESCENDENCE_CONFIG_DIR",
    Path.home() / ".syncrescendence"
))

DEFAULT_TOKEN_PATH = SYNCRESCENDENCE_DIR / "youtube_token.json"

DEFAULT_SOURCES_DIR = Path(os.environ.get(
    "SYNCRESCENDENCE_SOURCES_DIR",
    Path(__file__).resolve().parent.parent.parent / "sources"
))

INGEST_QUEUE_ID_PATH = SYNCRESCENDENCE_DIR / "ingest_queue_playlist_id.txt"

SCOPES = [
    "https://www.googleapis.com/auth/youtube.readonly",
    "https://www.googleapis.com/auth/youtube",
]

LOG_FORMAT = "%(asctime)s [%(levelname)s] %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
log = logging.getLogger("youtube_ingest")

# ---------------------------------------------------------------------------
# Auth
# ---------------------------------------------------------------------------

def get_authenticated_service(token_path: Path):
    """Load saved OAuth2 token and return an authenticated YouTube service."""
    if not token_path.exists():
        log.error("Token not found at %s. Run youtube_oauth_setup.py first.", token_path)
        sys.exit(1)

    creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)

    if creds.expired and creds.refresh_token:
        log.info("Refreshing expired token...")
        creds.refresh(Request())
        # Persist refreshed token
        token_data = {
            "token": creds.token,
            "refresh_token": creds.refresh_token,
            "token_uri": creds.token_uri,
            "client_id": creds.client_id,
            "client_secret": creds.client_secret,
            "scopes": list(creds.scopes) if creds.scopes else None,
        }
        token_path.write_text(json.dumps(token_data, indent=2))
        os.chmod(token_path, 0o600)

    if not creds.valid:
        log.error("Token invalid and cannot be refreshed. Re-run youtube_oauth_setup.py.")
        sys.exit(1)

    return build_youtube("youtube", "v3", credentials=creds)

# ---------------------------------------------------------------------------
# URL Index (dedup gate)
# ---------------------------------------------------------------------------

def _sqlite_db_path(sources_dir: Path) -> Path:
    return sources_dir / "_meta" / "source_index.db"


def _sqlite_url_set(sources_dir: Path) -> set[str] | None:
    """Load all URLs from SQLite index, or None if DB doesn't exist."""
    db = _sqlite_db_path(sources_dir)
    if not db.exists():
        return None
    try:
        conn = sqlite3.connect(str(db))
        conn.execute("PRAGMA journal_mode=WAL")
        urls = {r[0] for r in conn.execute("SELECT url FROM source_index").fetchall()}
        conn.close()
        return urls
    except Exception:
        return None


def _sqlite_insert(sources_dir: Path, url: str, filename: str = "", **kwargs):
    """Insert a URL into the SQLite index (upsert)."""
    db = _sqlite_db_path(sources_dir)
    if not db.exists():
        return
    try:
        conn = sqlite3.connect(str(db))
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
             "youtube_ingest"),
        )
        conn.commit()
        conn.close()
    except Exception:
        pass


def load_url_index(sources_dir: Path) -> set[str]:
    """Load known URLs — SQLite first, flat file fallback."""
    db_urls = _sqlite_url_set(sources_dir)
    if db_urls is not None:
        return db_urls
    index_path = sources_dir / "_meta" / "URL_INDEX.txt"
    if not index_path.exists():
        return set()
    return {line.strip() for line in index_path.read_text().splitlines() if line.strip()}


def append_to_url_index(sources_dir: Path, url: str, filename: str = "", **kwargs):
    """Append URL to both flat file and SQLite."""
    index_path = sources_dir / "_meta" / "URL_INDEX.txt"
    index_path.parent.mkdir(exist_ok=True)
    with open(index_path, "a") as f:
        f.write(url + "\n")
    _sqlite_insert(sources_dir, url, filename=filename, **kwargs)

# ---------------------------------------------------------------------------
# Playlist fetching
# ---------------------------------------------------------------------------

def fetch_playlist_items(youtube, playlist_id: str, max_results: int = 200) -> list[dict]:
    """Fetch all items from a playlist, paginated."""
    items = []
    page_token = None

    while len(items) < max_results:
        request = youtube.playlistItems().list(
            part="snippet,contentDetails",
            playlistId=playlist_id,
            maxResults=min(50, max_results - len(items)),
            pageToken=page_token,
        )
        response = request.execute()
        items.extend(response.get("items", []))
        page_token = response.get("nextPageToken")
        if not page_token:
            break

    return items[:max_results]


def get_video_details(youtube, video_id: str) -> dict | None:
    """Fetch full video metadata."""
    response = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=video_id,
    ).execute()
    items = response.get("items", [])
    return items[0] if items else None

# ---------------------------------------------------------------------------
# Transcript
# ---------------------------------------------------------------------------

def fetch_transcript(video_id: str) -> str | None:
    """Attempt to get transcript via youtube-transcript-api v1.x."""
    if not HAS_TRANSCRIPT_API:
        log.warning("youtube-transcript-api not installed. Skipping transcript.")
        return None
    try:
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id)
        return "\n".join(s.text for s in transcript.snippets)
    except Exception as e:
        log.warning("Transcript unavailable for %s: %s", video_id, e)
        return None

# ---------------------------------------------------------------------------
# Filename & frontmatter generation
# ---------------------------------------------------------------------------

def slugify(text: str, max_len: int = 60) -> str:
    """Convert text to a filesystem-safe slug."""
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = text.strip("_")
    if len(text) > max_len:
        text = text[:max_len].rstrip("_")
    return text


def classify_format(title: str, description: str, channel: str) -> str:
    """Heuristic format classification."""
    lower_title = (title + " " + description).lower()
    if any(w in lower_title for w in ["interview", "conversation with", "talks to", "sits down with"]):
        return "interview"
    if any(w in lower_title for w in ["lecture", "talk at", "keynote", "presentation"]):
        return "lecture"
    if any(w in lower_title for w in ["panel", "roundtable", "discussion"]):
        return "panel"
    if any(w in lower_title for w in ["tutorial", "how to", "walkthrough"]):
        return "tutorial"
    return "lecture"


def iso_duration_to_human(duration: str) -> str:
    """Convert ISO 8601 duration (PT1H2M3S) to human-readable."""
    match = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", duration or "")
    if not match:
        return duration or "unknown"
    h, m, s = (int(x) if x else 0 for x in match.groups())
    parts = []
    if h:
        parts.append(f"{h}h")
    if m:
        parts.append(f"{m}m")
    if s:
        parts.append(f"{s}s")
    return " ".join(parts) or "0s"


def generate_source_file(
    video_id: str,
    snippet: dict,
    content_details: dict,
    transcript: str | None,
    sources_dir: Path,
    seq: int,
) -> Path:
    """Generate a SOURCE-*.md file and return its path."""
    title = snippet.get("title", "Untitled")
    channel = snippet.get("channelTitle", "unknown")
    published = snippet.get("publishedAt", "")[:10]  # YYYY-MM-DD
    description = snippet.get("description", "")
    duration = iso_duration_to_human(content_details.get("duration", ""))
    url = f"https://www.youtube.com/watch?v={video_id}"

    date_str = published.replace("-", "") if published else datetime.now().strftime("%Y%m%d")
    fmt = classify_format(title, description, channel)
    creator_slug = slugify(channel, max_len=30)
    title_slug = slugify(title, max_len=60)

    filename = f"SOURCE-{date_str}-youtube-{fmt}-{creator_slug}-{title_slug}.md"
    filepath = sources_dir / filename

    # Prevent collision
    if filepath.exists():
        filename = f"SOURCE-{date_str}-youtube-{fmt}-{creator_slug}-{title_slug}_{seq}.md"
        filepath = sources_dir / filename

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
# Playlist removal
# ---------------------------------------------------------------------------

def remove_from_playlist(youtube, playlist_item_id: str):
    """Remove a video from a playlist by its playlistItem ID."""
    youtube.playlistItems().delete(id=playlist_item_id).execute()

# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def run_ingest(
    youtube,
    playlist_id: str,
    sources_dir: Path,
    clear_after: bool,
    dry_run: bool,
    max_results: int,
):
    """Core ingest loop."""
    known_urls = load_url_index(sources_dir)
    log.info("Loaded %d known URLs from index", len(known_urls))

    log.info("Fetching playlist %s (max %d)...", playlist_id, max_results)
    try:
        items = fetch_playlist_items(youtube, playlist_id, max_results)
    except Exception as e:
        log.error("Failed to fetch playlist %s: %s", playlist_id, e)
        if "watchLater" in str(e).lower() or "WL" == playlist_id:
            log.error(
                "Watch Later (WL) is deprecated in the YouTube API. "
                "Use a named playlist ID instead, or use Liked Videos (LL)."
            )
        return

    log.info("Found %d items in playlist", len(items))

    ingested = 0
    skipped = 0
    failed = 0

    for seq, item in enumerate(items, start=1):
        video_id = item["contentDetails"]["videoId"]
        playlist_item_id = item["id"]
        url = f"https://www.youtube.com/watch?v={video_id}"
        title = item["snippet"].get("title", "?")

        if url in known_urls:
            log.info("SKIP (already indexed): %s — %s", video_id, title)
            skipped += 1
            continue

        if dry_run:
            log.info("DRY-RUN would ingest: %s — %s", video_id, title)
            ingested += 1
            continue

        log.info("Processing: %s — %s", video_id, title)

        # Get full metadata
        details = get_video_details(youtube, video_id)
        if not details:
            log.warning("Could not fetch details for %s, skipping", video_id)
            failed += 1
            continue

        # Transcript
        transcript = fetch_transcript(video_id)

        # Generate SOURCE file
        try:
            filepath = generate_source_file(
                video_id,
                details["snippet"],
                details["contentDetails"],
                transcript,
                sources_dir,
                seq,
            )
            log.info("Created: %s", filepath.name)
        except Exception as e:
            log.error("Failed to write SOURCE for %s: %s", video_id, e)
            failed += 1
            continue

        # Update index
        append_to_url_index(sources_dir, url)
        known_urls.add(url)
        ingested += 1

        # Remove from playlist
        if clear_after:
            try:
                remove_from_playlist(youtube, playlist_item_id)
                log.info("Removed from playlist: %s", video_id)
            except Exception as e:
                log.warning("Failed to remove %s from playlist: %s", video_id, e)

    log.info("Done. Ingested=%d, Skipped=%d, Failed=%d", ingested, skipped, failed)


def main():
    parser = argparse.ArgumentParser(
        description="YouTube stateless ingest pipeline for Syncrescendence"
    )
    parser.add_argument(
        "--token-path", type=Path, default=DEFAULT_TOKEN_PATH,
        help=f"OAuth2 token path (default: {DEFAULT_TOKEN_PATH})",
    )
    parser.add_argument(
        "--sources-dir", type=Path, default=DEFAULT_SOURCES_DIR,
        help=f"sources directory (default: {DEFAULT_SOURCES_DIR})",
    )
    parser.add_argument(
        "--playlist", type=str, default="LL",
        help="Playlist ID to ingest (default: LL = Liked Videos). "
             "WL (Watch Later) is deprecated; use a named playlist ID instead.",
    )
    parser.add_argument(
        "--ingest-queue", action="store_true",
        help="Use Ingest Queue playlist as primary (reads ID from "
             f"{INGEST_QUEUE_ID_PATH}). Implies --clear-after-ingest.",
    )
    parser.add_argument(
        "--additional-playlists", nargs="*", default=[],
        help="Additional playlist IDs to also ingest from.",
    )
    parser.add_argument(
        "--max-results", type=int, default=200,
        help="Max videos to fetch per playlist (default: 200)",
    )
    parser.add_argument(
        "--clear-after-ingest", action="store_true",
        help="Remove videos from playlist after successful ingest",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="List what would be ingested without writing files",
    )
    parser.add_argument(
        "--rebuild-index", action="store_true",
        help="Rebuild URL_INDEX.txt before ingesting (runs build_url_index)",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="Enable debug logging",
    )
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Resolve --ingest-queue: override playlist and enable clear-after
    if args.ingest_queue or (not args.ingest_queue and INGEST_QUEUE_ID_PATH.exists()):
        iq_id = INGEST_QUEUE_ID_PATH.read_text().strip() if INGEST_QUEUE_ID_PATH.exists() else ""
        if iq_id:
            log.info("Using Ingest Queue playlist: %s", iq_id)
            args.playlist = iq_id
            args.clear_after_ingest = True
        elif args.ingest_queue:
            log.error("--ingest-queue specified but %s not found. Run create_ingest_queue.py first.", INGEST_QUEUE_ID_PATH)
            sys.exit(1)

    # Optionally rebuild index first
    if args.rebuild_index:
        log.info("Rebuilding URL index...")
        from build_url_index import build_index
        urls = build_index(args.sources_dir)
        index_path = args.sources_dir / "_meta" / "URL_INDEX.txt"
        index_path.parent.mkdir(exist_ok=True)
        index_path.write_text("\n".join(urls) + "\n" if urls else "")
        log.info("Rebuilt index: %d URLs", len(urls))

    youtube = get_authenticated_service(args.token_path)

    # Process primary playlist
    all_playlists = [args.playlist] + args.additional_playlists
    for pl_id in all_playlists:
        log.info("=== Ingesting playlist: %s ===", pl_id)
        run_ingest(
            youtube,
            playlist_id=pl_id,
            sources_dir=args.sources_dir,
            clear_after=args.clear_after_ingest,
            dry_run=args.dry_run,
            max_results=args.max_results,
        )


if __name__ == "__main__":
    main()
