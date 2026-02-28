#!/usr/bin/env python3
"""Build SQLite URL dedup index from SOURCE-*.md frontmatter.

Creates/rebuilds source_index.db with WAL mode, also writes URL_INDEX.txt
for backward compatibility.
"""
from config import *

import hashlib
import os
import re
import sqlite3
import sys
from pathlib import Path

SOURCES_DIR = Path(__file__).resolve().parents[2] / "sources"
META_DIR = SOURCES_DIR / "_meta"
DB_PATH = META_DIR / "source_index.db"
URL_INDEX_PATH = META_DIR / "URL_INDEX.txt"

SCHEMA = """
CREATE TABLE IF NOT EXISTS source_index (
    url TEXT PRIMARY KEY,
    filename TEXT NOT NULL,
    platform TEXT,
    format TEXT,
    creator TEXT,
    date_published TEXT,
    date_ingested TEXT DEFAULT (datetime('now')),
    content_hash TEXT,
    file_size INTEGER,
    ingest_source TEXT,
    save_cleared INTEGER DEFAULT 0,
    ingest_cycle TEXT
);
CREATE INDEX IF NOT EXISTS idx_filename ON source_index(filename);
CREATE INDEX IF NOT EXISTS idx_creator ON source_index(creator);
CREATE INDEX IF NOT EXISTS idx_platform ON source_index(platform);
CREATE INDEX IF NOT EXISTS idx_ingest_source ON source_index(ingest_source);
CREATE INDEX IF NOT EXISTS idx_save_cleared ON source_index(save_cleared);
"""

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)


def parse_yaml_frontmatter(text: str) -> dict:
    """Minimal YAML frontmatter parser (no pyyaml dependency)."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    result = {}
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("-"):
            continue
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        if val:
            result[key] = val
    return result


def content_hash(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:16]


def build_index():
    META_DIR.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA journal_mode=WAL")
    conn.executescript(SCHEMA)

    source_files = sorted(SOURCES_DIR.glob("SOURCE-*.md"))
    urls_seen = []
    inserted = 0
    skipped_no_url = 0

    for fp in source_files:
        raw = fp.read_bytes()
        text = raw.decode("utf-8", errors="replace")
        fm = parse_yaml_frontmatter(text)
        url = fm.get("url")
        if not url:
            skipped_no_url += 1
            continue

        urls_seen.append(url)
        conn.execute(
            """INSERT INTO source_index
               (url, filename, platform, format, creator, date_published,
                content_hash, file_size, ingest_source)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
               ON CONFLICT(url) DO UPDATE SET
                 filename=excluded.filename,
                 platform=excluded.platform,
                 format=excluded.format,
                 creator=excluded.creator,
                 date_published=excluded.date_published,
                 content_hash=excluded.content_hash,
                 file_size=excluded.file_size
            """,
            (
                url,
                fp.name,
                fm.get("platform"),
                fm.get("format"),
                fm.get("creator"),
                fm.get("date_published"),
                content_hash(raw),
                len(raw),
                "build_url_index_sqlite",
            ),
        )
        inserted += 1

    conn.commit()

    # Backward compat: write URL_INDEX.txt
    URL_INDEX_PATH.write_text("\n".join(urls_seen) + "\n" if urls_seen else "")

    # Stats
    row_count = conn.execute("SELECT COUNT(*) FROM source_index").fetchone()[0]
    platform_stats = conn.execute(
        "SELECT platform, COUNT(*) FROM source_index GROUP BY platform ORDER BY COUNT(*) DESC"
    ).fetchall()
    creator_count = conn.execute(
        "SELECT COUNT(DISTINCT creator) FROM source_index"
    ).fetchone()[0]

    conn.close()

    print(f"=== Source Index Build Complete ===")
    print(f"SOURCE-*.md files scanned : {len(source_files)}")
    print(f"URLs indexed (upserted)   : {inserted}")
    print(f"Skipped (no URL)          : {skipped_no_url}")
    print(f"Total rows in DB          : {row_count}")
    print(f"Distinct creators         : {creator_count}")
    print(f"URL_INDEX.txt lines       : {len(urls_seen)}")
    print(f"DB path                   : {DB_PATH}")
    print(f"\nPlatform breakdown:")
    for plat, cnt in platform_stats:
        print(f"  {plat or '(none)':<20} {cnt}")


if __name__ == "__main__":
    build_index()
