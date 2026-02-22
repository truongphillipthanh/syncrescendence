#!/usr/bin/env python3
"""Batch transcribe YouTube SOURCE files missing transcript content."""

import glob
import os
import re
import sys
import time

from youtube_transcript_api import YouTubeTranscriptApi

SOURCES_DIR = "/Users/system/Desktop/syncrescendence/04-SOURCES"
PATTERN = os.path.join(SOURCES_DIR, "SOURCE-*youtube*.md")

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

def get_body_after_frontmatter(content):
    """Get body content after YAML frontmatter."""
    parts = content.split("---", 2)
    if len(parts) >= 3:
        return parts[2]
    return ""

def main():
    files = sorted(glob.glob(PATTERN))

    stats = {
        "total": len(files),
        "no_url": 0,
        "already_has_transcript": 0,
        "newly_transcribed": 0,
        "failed": [],
        "skipped_files": [],
        "transcribed_files": [],
    }

    api = YouTubeTranscriptApi()

    for filepath in files:
        basename = os.path.basename(filepath)
        with open(filepath, "r") as f:
            content = f.read()

        url, video_id = extract_url(content)
        if not video_id:
            stats["no_url"] += 1
            stats["skipped_files"].append((basename, "no URL"))
            continue

        if has_transcript(content):
            stats["already_has_transcript"] += 1
            stats["skipped_files"].append((basename, "already has transcript"))
            continue

        # Only skip if already has a ## Transcript section
        # (existing analysis/summaries are fine to keep alongside transcript)

        # Fetch transcript
        print(f"Fetching: {basename} ({video_id})...")
        try:
            transcript = api.fetch(video_id)
            text = "\n".join(s.text for s in transcript.snippets)

            if not text.strip():
                stats["failed"].append((basename, "empty transcript"))
                continue

            # Append transcript to file
            transcript_section = f"\n\n## Transcript\n\n{text}\n"
            with open(filepath, "a") as f:
                f.write(transcript_section)

            stats["newly_transcribed"] += 1
            stats["transcribed_files"].append(basename)
            print(f"  OK ({len(text)} chars)")

            # Small delay to avoid rate limits
            time.sleep(0.5)

        except Exception as e:
            err = str(e)[:200]
            stats["failed"].append((basename, err))
            print(f"  FAILED: {err}")

    # Print summary
    print("\n" + "=" * 60)
    print("TRANSCRIPTION SUMMARY")
    print("=" * 60)
    print(f"Total YouTube files:      {stats['total']}")
    print(f"No URL found:             {stats['no_url']}")
    print(f"Already has transcript:   {stats['already_has_transcript']}")
    print(f"Newly transcribed:        {stats['newly_transcribed']}")
    print(f"Failed:                   {len(stats['failed'])}")

    if stats["failed"]:
        print("\nFailed files:")
        for name, err in stats["failed"]:
            print(f"  - {name}: {err}")

    if stats["transcribed_files"]:
        print("\nNewly transcribed:")
        for name in stats["transcribed_files"]:
            print(f"  + {name}")

    # Write report
    report_path = os.path.join(SOURCES_DIR, "_meta", "TRANSCRIPTION_REPORT.md")
    with open(report_path, "w") as f:
        f.write("# YouTube Transcript Batch Report\n\n")
        f.write(f"**Date**: {time.strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"**Script**: `00-ORCHESTRATION/scripts/batch_transcribe.py`\n\n")
        f.write("## Summary\n\n")
        f.write(f"| Metric | Count |\n|--------|-------|\n")
        f.write(f"| Total YouTube SOURCE files | {stats['total']} |\n")
        f.write(f"| No URL in frontmatter | {stats['no_url']} |\n")
        f.write(f"| Already has transcript | {stats['already_has_transcript']} |\n")
        f.write(f"| Newly transcribed | {stats['newly_transcribed']} |\n")
        f.write(f"| Failed | {len(stats['failed'])} |\n\n")

        if stats["transcribed_files"]:
            f.write("## Newly Transcribed\n\n")
            for name in stats["transcribed_files"]:
                f.write(f"- `{name}`\n")
            f.write("\n")

        if stats["failed"]:
            f.write("## Failed\n\n")
            for name, err in stats["failed"]:
                f.write(f"- `{name}`: {err}\n")
            f.write("\n")

        if stats["skipped_files"]:
            f.write("## Skipped\n\n")
            for name, reason in stats["skipped_files"]:
                f.write(f"- `{name}`: {reason}\n")
            f.write("\n")

    print(f"\nReport written to: {report_path}")

if __name__ == "__main__":
    main()
