#!/usr/bin/env python3
"""Strip corpus filenames to sequential numbers. Store mapping in manifest."""

import os
import json
from pathlib import Path

CORPUS = Path(__file__).parent
SKIP = {"strip_filenames.py", "UNDO-NUCLEOSYNTHESIS.sh", "CORPUS-MANIFEST.json",
        ".DS_Store"}
SKIP_DIRS = {"__pycache__", "demoted", "sn_compressed", "sn_skeletons", "views"}

manifest = {}
counter = 0

# Gather all files (top-level only, skip subdirs and special files)
files = sorted(f for f in CORPUS.iterdir()
               if f.is_file() and f.name not in SKIP)

print(f"Files to rename: {len(files)}")

for f in files:
    counter += 1
    ext = f.suffix  # preserve extension
    new_name = f"{counter:05d}{ext}"
    new_path = CORPUS / new_name

    manifest[new_name] = f.name

    f.rename(new_path)

# Write manifest
manifest_path = CORPUS / "CORPUS-MANIFEST.json"
manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False))

print(f"Renamed: {counter}")
print(f"Manifest: {manifest_path}")
