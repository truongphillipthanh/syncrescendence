#!/usr/bin/env python3
"""
Batch transcribe YouTube SOURCE files missing transcript content.

Usage:
    python3 batch_transcribe.py [--max N] [--dry-run] [--delay SECS]

Gracefully handles IP bans by stopping early and reporting progress.
Idempotent: skips files that already have a ## Transcript section.
Updates has_transcript frontmatter field on success.
"""

import argparse
import glob
import os
import re
import sys
import time

SOURCES_DIR = "/Users/system/Desktop/syncrescendence/04-SOURCES"
PATTERN = os.path.join(SOURCES_DIR, "SOURCE-*youtube*.md")
MARKER_FILE = os.path.join(SOURCES_DIR, "_meta", ".transcribed_files.txt")


def extract_url(content):
    """Extract YouTube URL from frontmatter."""
    m = re.search(r'url:\s*"?(https?://(?:www\.)?youtube\.com/watch\?v=([^"&\s]+))', content)
    if m:
        return m.group(1), m.group(2)
    m = re.search(r'url:\s*"?(https?://youtu\.be/([^"&\s]+))', content)
    if m:
        return m.group(1), m.group(2)
    return None, None


def has_transcript(content):
    """Check if file already has a ## Transcript section."""
    return "## Transcript" in content


def update_has_transcript_field(content):
    """Set has_transcript: yes in frontmatter."""
    return re.sub(r'^(has_transcript:)\s*\S+', r'\1 yes', content, count=1, flags=re.MULTILINE)


def load_done_set():
    """Load set of already-transcribed filenames for resume."""
    if os.path.exists(MARKER_FILE):
        with open(MARKER_FILE) as f:
            return set(line.strip() for line in f if line.strip())
    return set()


def mark_done(filename):
    os.makedirs(os.path.dirname(MARKER_FILE), exist_ok=True)
    with open(MARKER_FILE, "a") as f:
        f.write(filename + "\n")


def main():
    parser = argparse.ArgumentParser(description="Batch transcribe YouTube SOURCE files")
    parser.add_argument("--max", type=int, default=0, help="Max files to process (0=all)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done")
    parser.add_argument("--delay", type=float, default=1.0, help="Delay between requests (seconds)")
    args = parser.parse_args()

    from youtube_transcript_api import YouTubeTranscriptApi
    from youtube_transcript_api._errors import IpBlocked

    api = YouTubeTranscriptApi()
    done_set = load_done_set()
    files = sorted(glob.glob(PATTERN))

    # Build candidate list
    candidates = []
    already = 0
    no_url = 0
    for filepath in files:
        basename = os.path.basename(filepath)
        if basename in done_set:
            already += 1
            continue
        with open(filepath, "r", errors="replace") as f:
            content = f.read()
        if has_transcript(content):
            already += 1
            mark_done(basename)
            continue
        _, video_id = extract_url(content)
        if not video_id:
            no_url += 1
            continue
        candidates.append((filepath, basename, video_id))

    total_yt = len(files)
    to_process = candidates[:args.max] if args.max > 0 else candidates

    print(f"YouTube SOURCE files: {total_yt}")
    print(f"Already transcribed:  {already}")
    print(f"No URL:               {no_url}")
    print(f"Candidates:           {len(candidates)}")
    print(f"Processing:           {len(to_process)}")
    print()

    if args.dry_run:
        for _, basename, vid in to_process[:20]:
            print(f"  DRY RUN: {basename} ({vid})")
        if len(to_process) > 20:
            print(f"  ... and {len(to_process) - 20} more")
        return

    transcribed = 0
    failed = 0
    ip_blocked = False

    for i, (filepath, basename, video_id) in enumerate(to_process):
        print(f"[{i+1}/{len(to_process)}] {basename} ({video_id})...", end=" ", flush=True)

        try:
            transcript = api.fetch(video_id)
            text = "\n".join(s.text for s in transcript.snippets)

            if not text.strip():
                print("EMPTY")
                failed += 1
                continue

            # Read current content, append transcript, update frontmatter
            with open(filepath, "r", errors="replace") as f:
                content = f.read()

            content = update_has_transcript_field(content)
            content += f"\n\n## Transcript\n\n{text}\n"

            with open(filepath, "w") as f:
                f.write(content)

            mark_done(basename)
            transcribed += 1
            print(f"OK ({len(text)} chars)")
            time.sleep(args.delay)

        except IpBlocked:
            print("IP BLOCKED — stopping early")
            ip_blocked = True
            break

        except Exception as e:
            err = str(e)[:120]
            print(f"FAIL: {err}")
            failed += 1
            time.sleep(args.delay)

        if (i + 1) % 25 == 0:
            print(f"  Progress: {i+1}/{len(to_process)} | transcribed: {transcribed} | failed: {failed}")

    print(f"\nDone. Transcribed: {transcribed}, Failed: {failed}, IP blocked: {ip_blocked}")
    print(f"Remaining: {len(candidates) - transcribed - failed}")

    # Write report
    report_path = os.path.join(SOURCES_DIR, "_meta", "TRANSCRIPTION_REPORT.md")
    with open(report_path, "w") as f:
        f.write("# YouTube Transcript Batch Report\n\n")
        f.write(f"**Date**: {time.strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"**Script**: `batch_transcribe.py`\n\n")
        f.write(f"| Metric | Count |\n|--------|-------|\n")
        f.write(f"| Total YouTube SOURCE files | {total_yt} |\n")
        f.write(f"| Already transcribed | {already + transcribed} |\n")
        f.write(f"| No URL | {no_url} |\n")
        f.write(f"| Remaining | {len(candidates) - transcribed - failed} |\n")
        f.write(f"| Failed this run | {failed} |\n")
        f.write(f"| IP blocked | {'yes' if ip_blocked else 'no'} |\n")
    print(f"Report: {report_path}")


if __name__ == "__main__":
    main()
