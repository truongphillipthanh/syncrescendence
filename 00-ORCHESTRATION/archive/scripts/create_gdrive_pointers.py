#!/usr/bin/env python3
"""
Create pointer documents for files offloaded to Google Drive
Replaces local .txt files with .gdrive-pointer.md files
"""

import os
import sys
from pathlib import Path
from datetime import datetime

def create_pointer(local_path: Path, gdrive_path: str):
    """Create a pointer document for an offloaded file"""

    # Get file info
    file_size = local_path.stat().st_size if local_path.exists() else 0
    file_name = local_path.name

    # Create pointer content
    pointer_content = f"""# Google Drive Pointer

**Original file**: {file_name}
**Offloaded to**: Google Drive
**Path**: `{gdrive_path}`
**Original size**: {file_size:,} bytes
**Offloaded**: {datetime.now().strftime('%Y-%m-%d')}

## Access

View in Google Drive:
```
rclone cat "{gdrive_path}"
```

Download locally:
```
rclone copy "{gdrive_path}" ./
```

---

**Note**: Raw transcript offloaded to Google Drive to reduce local repository size.
Processed version may exist in `04-SOURCES/processed/`.
"""

    # Write pointer file
    pointer_path = local_path.with_suffix('.gdrive-pointer.md')
    with open(pointer_path, 'w', encoding='utf-8') as f:
        f.write(pointer_content)

    return pointer_path

def main():
    source_dir = Path('04-SOURCES/raw')
    gdrive_base = 'gdrive:syncrescendence/04-SOURCES-raw-transcripts'

    txt_files = list(source_dir.glob('*.txt'))
    print(f"Found {len(txt_files)} .txt files to convert to pointers")

    for txt_file in txt_files:
        gdrive_path = f"{gdrive_base}/{txt_file.name}"
        pointer_path = create_pointer(txt_file, gdrive_path)
        print(f"  Created: {pointer_path.name}")

        # Remove original .txt file
        txt_file.unlink()

    print(f"\n✓ Created {len(txt_files)} pointer documents")
    print(f"✓ Removed {len(txt_files)} local .txt files")

if __name__ == '__main__':
    main()
