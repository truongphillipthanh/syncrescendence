#!/usr/bin/env python3
"""
rename_transcripts.py
Apply Principal's naming standard to SOURCES/raw/

Principal's Standard:
{YYYYMMDD}-{platform_format}-{full_channel_name}-{guest(if interview)}/{title(if not interview)}.{ext}

Platform format values use underscores: youtube_video, youtube_lecture, podcast_interview, etc.
"""

import os
import re
import csv
from pathlib import Path

# Determine paths
SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent.parent
SOURCES_RAW = REPO_ROOT / 'SOURCES' / 'raw'
SOURCES_DIR = REPO_ROOT / 'SOURCES'
MAPPING_FILE = SOURCES_DIR / 'rename_mapping.csv'
SOURCES_CSV = SOURCES_DIR / 'sources.csv'

def parse_old_name(filename):
    """Parse the old SOURCE-* naming convention."""
    if '.' in filename:
        base = filename.rsplit('.', 1)[0]
        ext = filename.rsplit('.', 1)[1]
    else:
        base = filename
        ext = ''

    # Remove SOURCE- prefix
    if base.startswith('SOURCE-'):
        base = base[7:]  # len('SOURCE-') = 7

    # Extract date (first 8 digits or 00000000)
    date_match = re.match(r'^(\d{8})-(.+)$', base)
    if date_match:
        date = date_match.group(1)
        rest = date_match.group(2)
    else:
        date = '00000000'
        rest = base

    return date, rest, ext

def transform_to_new_standard(date, rest, ext):
    """Transform to Principal's standard using underscores for platform_format."""
    # Replace platform-format (hyphen) with platform_format (underscore)
    transformations = [
        ('youtube-interview', 'youtube_video'),
        ('youtube-lecture', 'youtube_lecture'),
        ('youtube-tutorial', 'youtube_tutorial'),
        ('youtube-panel', 'youtube_panel'),
        ('youtube-solo', 'youtube_solo'),
        ('x-thread', 'x_thread'),
        ('podcast-interview', 'podcast_interview'),
        ('podcast-solo', 'podcast_solo'),
        ('substack-article', 'substack_article'),
        ('arxiv-paper', 'arxiv_paper'),
    ]

    for old, new in transformations:
        rest = rest.replace(old, new)

    # Construct new name
    new_name = f"{date}-{rest}.{ext}"

    return new_name

def update_sources_csv(mapping):
    """Update sources.csv with new filenames."""
    if not SOURCES_CSV.exists() or not mapping:
        return 0

    # Load existing CSV
    rows = []
    fieldnames = None
    with open(SOURCES_CSV, 'r') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            rows.append(row)

    # Create mapping dict
    name_map = {m['old_name']: m['new_name'] for m in mapping}

    # Update rows
    updated_count = 0
    for row in rows:
        old_filename = row.get('filename', '')
        if old_filename in name_map:
            row['filename'] = name_map[old_filename]
            # Update filepath too
            old_path = row.get('filepath', '')
            if old_path:
                row['filepath'] = old_path.replace(old_filename, name_map[old_filename])
            updated_count += 1

    # Write back
    with open(SOURCES_CSV, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return updated_count

def main():
    mapping = []
    skipped = []
    errors = []

    print(f"Scanning: {SOURCES_RAW}")
    print("-" * 60)

    for filepath in sorted(SOURCES_RAW.iterdir()):
        if not filepath.is_file():
            continue
        if filepath.name.startswith('.'):
            continue
        if not filepath.name.startswith('SOURCE-'):
            skipped.append(filepath.name)
            continue

        old_name = filepath.name
        date, rest, ext = parse_old_name(old_name)
        new_name = transform_to_new_standard(date, rest, ext)

        if old_name == new_name:
            skipped.append(old_name)
            continue

        new_path = filepath.parent / new_name

        # Check for conflicts
        if new_path.exists():
            errors.append(f"CONFLICT: {new_name} already exists, skipping {old_name}")
            continue

        try:
            # Rename
            filepath.rename(new_path)
            mapping.append({'old_name': old_name, 'new_name': new_name})
            print(f"✓ {old_name[:50]}...")
            print(f"  → {new_name[:50]}...")
        except Exception as e:
            errors.append(f"ERROR renaming {old_name}: {e}")

    # Save mapping
    if mapping:
        with open(MAPPING_FILE, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['old_name', 'new_name'])
            writer.writeheader()
            writer.writerows(mapping)

    print("-" * 60)
    print(f"Renamed: {len(mapping)} files")
    print(f"Skipped: {len(skipped)} files (no change needed or not SOURCE-*)")
    if errors:
        print(f"Errors: {len(errors)}")
        for e in errors:
            print(f"  {e}")

    print(f"\nMapping saved to: {MAPPING_FILE}")

    # Update sources.csv
    if mapping:
        updated = update_sources_csv(mapping)
        print(f"Updated {updated} entries in sources.csv")

    return len(mapping)

if __name__ == '__main__':
    main()
