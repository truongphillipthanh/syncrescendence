#!/usr/bin/env python3
"""
URL Index Builder for Syncrescendence sources corpus.

Scans all SOURCE-*.md files, extracts URLs from frontmatter,
writes to sources/_meta/URL_INDEX.txt (one URL per line).

This is the dedup gate for all ingest pipelines.

Usage:
  python build_url_index.py
  python build_url_index.py --sources-dir /path/to/sources
"""
from config import *

import argparse
import os
import re
from pathlib import Path

DEFAULT_SOURCES_DIR = Path(os.environ.get(
    "SYNCRESCENDENCE_SOURCES_DIR",
    Path(__file__).resolve().parent.parent.parent / "sources"
))


def extract_url_from_frontmatter(filepath: Path) -> str | None:
    """Extract url field from YAML frontmatter of a SOURCE file."""
    try:
        text = filepath.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return None

    # Match YAML frontmatter block
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return None

    frontmatter = match.group(1)
    # Extract url field (handles quoted and unquoted)
    url_match = re.search(r'^url:\s*["\']?(https?://[^\s"\']+)["\']?', frontmatter, re.MULTILINE)
    if url_match:
        return url_match.group(1)
    return None


def build_index(sources_dir: Path) -> list[str]:
    """Scan all SOURCE-*.md files and collect URLs."""
    urls = []
    for f in sorted(sources_dir.glob("SOURCE-*.md")):
        url = extract_url_from_frontmatter(f)
        if url:
            urls.append(url)
    return urls


def main():
    parser = argparse.ArgumentParser(description="Build URL index from SOURCE files")
    parser.add_argument(
        "--sources-dir", type=Path, default=DEFAULT_SOURCES_DIR,
        help=f"Path to sources directory (default: {DEFAULT_SOURCES_DIR})",
    )
    args = parser.parse_args()

    sources_dir = args.sources_dir
    meta_dir = sources_dir / "_meta"
    meta_dir.mkdir(exist_ok=True)

    urls = build_index(sources_dir)
    index_path = meta_dir / "URL_INDEX.txt"
    index_path.write_text("\n".join(urls) + "\n" if urls else "")

    print(f"Indexed {len(urls)} URLs from SOURCE files")
    print(f"Written to {index_path}")


if __name__ == "__main__":
    main()
