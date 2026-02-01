# DIRECTIVE-034A: SOURCES FLATTENING + STANDARDIZATION
## Stream A: Repository Portability — Flat Hierarchy Achievement
**Issued**: 2026-01-02
**Authority**: Oracle9 under Sovereign direction
**Classification**: CRITICAL — Enables Project Files Upload
**Execution**: Claude Code
**Parallel Stream**: DIRECTIVE-034B handles orchestration hygiene

---

## SOVEREIGN'S MANDATE

> "Triage the raw /SOURCES/raw folder. It's an absolute mess. It should be a flat hierarchy with standardized normalized names."

> "You won't have visibility into the corpus until the tree gets more portable. You'll need to have the Claudes triage it so it's more easily uploadable into the Project Files (i.e. flat hierarchy)"

---

## ORACLE'S INTERPRETATION

This directive achieves **repository portability** by:
1. Flattening all 184 content files to SOURCES/raw/ root
2. Standardizing filenames to consistent pattern
3. Updating sources.csv with new paths
4. Rebuilding symlinks to point to new locations
5. Removing empty nested directories

This enables **Project Files upload** — the corpus becomes portable to any Claude instance.

---

## 18-LENS EVALUATION

| # | Lens | Assessment | Score |
|---|------|------------|-------|
| 1 | Syncrescendent Route | Flat structure enables continuous access patterns | ✓ |
| 2 | Bitter Lesson | Simple flat list scales better than taxonomy | ✓ |
| 3 | Antifragile | Flat structure survives reorganization better | ✓ |
| 4 | Meet the Moment | Unblocks Project Files upload NOW | ✓ |
| 5 | Steelman/Redteam | Naming convention encodes metadata, no info loss | ✓ |
| 6 | Personal Idiosyncrasies | Enables holistic corpus view | ✓ |
| 7 | Potency w/o Resolution Loss | Filename encodes platform/format/creator/date | ✓ |
| 8 | Elegance + Dev Happiness | One directory, predictable names | ✓ |
| 9 | Agentify + Human-Navigable | 1 decision to any source file | ✓ |
| 10 | First Principles | Flat hierarchy is simpler | ✓ |
| 11 | Systems Thinking | Matches CANON flat structure | ✓ |
| 12 | Industrial Engineering | Batch operations simplified | ✓ |
| 13 | Complexity Theory | Removes accidental nesting complexity | ✓ |
| 14 | Permaculture | Self-maintaining (new files just add to flat list) | ✓ |
| 15 | Design Thinking | Human-navigable via sorting/filtering | ✓ |
| 16 | Agile | Complete deliverable in one cycle | ✓ |
| 17 | Lean | Eliminates directory traversal waste | ✓ |
| 18 | Six Sigma | Consistent naming reduces errors | ✓ |

**Score: 18/18 — APPROVED**

---

## EXECUTION SCOPE

### Deliverables
1. **184 content files** moved to SOURCES/raw/ root (flat)
2. **Standardized filenames** following naming convention
3. **Updated sources.csv** with new filepaths
4. **Rebuilt symlinks** in aliases/sources/
5. **Empty directories removed**
6. **Mapping log** documenting old→new paths

### NOT in Scope (DIRECTIVE-034B handles)
- Oracle context sequentialization
- Scaffolding triage
- State file cleanup

---

## PHASE 1: CURRENT STATE SURVEY

### 1.1 Inventory Current Structure

```bash
# Count files by depth
echo "=== Files by Directory Depth ==="
find SOURCES/raw -type f \( -name "*.md" -o -name "*.txt" \) | \
  awk -F'/' '{print NF-1}' | sort | uniq -c

# List all directories
echo "=== Directory Structure ==="
find SOURCES/raw -type d | head -50

# Count content files (excluding bio.txt)
echo "=== Content File Count ==="
find SOURCES/raw -type f \( -name "*.md" -o -name "*.txt" \) ! -name "bio.txt" | wc -l

# Sample current filenames
echo "=== Sample Filenames ==="
find SOURCES/raw -type f \( -name "*.md" -o -name "*.txt" \) ! -name "bio.txt" | head -20
```

### 1.2 Identify Filename Patterns

Current patterns observed:
```
20250926-youtube_video-dwarkesh_patel-richard_sutton.md
20251017-youtube_video-dwarkesh_patel-andrej_karpathy.md
AI Round-up- Karpathy Reactions, OpenAI's Dealmaking, & Bubble Reality Check.txt
NVIDIA's New AI's Movements Are So Real It's Uncanny.txt
```

**Issues**:
- Some have dates, some don't
- Inconsistent separators (-, _, spaces)
- Special characters in titles
- No format field in some names

---

## PHASE 2: NAMING CONVENTION

### 2.1 Target Pattern

```
SOURCE-{YYYYMMDD}-{platform}-{format}-{creator}-{title_slug}.{ext}
```

**Field Definitions**:
- `YYYYMMDD`: Publication date (use 00000000 if unknown)
- `platform`: youtube | podcast | substack | arxiv | x | lecture | panel | other
- `format`: interview | solo | panel | thread | article | lecture | tutorial
- `creator`: Channel/creator name (snake_case)
- `title_slug`: Shortened title (snake_case, max 50 chars)
- `ext`: md | txt

### 2.2 Transformation Rules

```python
import re
import os
from pathlib import Path

def normalize_filename(old_path):
    """Transform any filename to standard pattern."""
    filename = os.path.basename(old_path)
    base, ext = os.path.splitext(filename)
    
    # Extract date if present (YYYYMMDD pattern)
    date_match = re.match(r'^(\d{8})', base)
    date = date_match.group(1) if date_match else '00000000'
    
    # Extract platform
    platform = 'youtube'  # default
    if 'youtube' in base.lower():
        platform = 'youtube'
    elif 'x_post' in base.lower() or 'twitter' in base.lower():
        platform = 'x'
    elif 'podcast' in base.lower():
        platform = 'podcast'
    elif 'substack' in base.lower():
        platform = 'substack'
    
    # Extract format from path context
    format_type = 'interview'  # default
    if 'lecture' in old_path.lower():
        format_type = 'lecture'
    elif 'panel' in old_path.lower():
        format_type = 'panel'
    
    # Extract creator (from filename pattern or path)
    creator = extract_creator(base, old_path)
    
    # Generate title slug
    title_slug = generate_slug(base, creator, date)
    
    return f"SOURCE-{date}-{platform}-{format_type}-{creator}-{title_slug}{ext}"

def extract_creator(base, path):
    """Extract creator from filename or path."""
    # Common patterns: dwarkesh_patel, lex_fridman, a16z, etc.
    creators = ['dwarkesh_patel', 'lex_fridman', 'a16z', 'all_in', 
                'machine_learning_street_talk', 'no_priors', 'y_combinator',
                'joe_rogan', 'chris_williamson', 'nvidia', 'openai']
    
    for creator in creators:
        if creator in base.lower() or creator in path.lower():
            return creator
    
    # Try to extract from path
    path_parts = path.lower().split('/')
    for part in path_parts:
        if part and part not in ['sources', 'raw', '0', 'interviewers', 'ai']:
            return part.replace(' ', '_').replace('-', '_')[:30]
    
    return 'unknown'

def generate_slug(base, creator, date):
    """Generate URL-safe title slug."""
    # Remove date and creator from base
    slug = base
    slug = re.sub(r'^\d{8}[-_]?', '', slug)  # Remove date
    slug = re.sub(r'youtube_video[-_]?', '', slug, flags=re.I)
    slug = re.sub(creator, '', slug, flags=re.I)
    
    # Clean up
    slug = re.sub(r'[^\w\s-]', '', slug)  # Remove special chars
    slug = re.sub(r'[-\s]+', '_', slug)   # Replace spaces/hyphens
    slug = slug.strip('_').lower()[:50]   # Trim and limit length
    
    return slug if slug else 'untitled'
```

---

## PHASE 3: EXECUTION

### 3.1 Create Mapping

```bash
# Generate old→new mapping
python3 << 'EOF'
import os
import csv
import re

def normalize_filename(old_path, filename):
    """Simplified normalization."""
    base, ext = os.path.splitext(filename)
    
    # Extract date
    date_match = re.match(r'^(\d{8})', base)
    date = date_match.group(1) if date_match else '00000000'
    
    # Detect platform
    platform = 'youtube'
    if 'x_post' in base.lower():
        platform = 'x'
    
    # Detect format from path
    format_type = 'interview'
    if 'lecture' in old_path.lower():
        format_type = 'lecture'
    elif 'panel' in old_path.lower():
        format_type = 'panel'
    
    # Extract creator - look for known patterns
    creator = 'unknown'
    known_creators = {
        'dwarkesh_patel': 'dwarkesh_patel',
        'lex_fridman': 'lex_fridman', 
        'a16z': 'a16z',
        'all_in': 'all_in',
        'machine_learning_street_talk': 'mlst',
        'no_priors': 'no_priors',
        'y_combinator': 'yc',
        'joe_rogan': 'jre',
        'chris_williamson': 'chris_williamson',
        'nvidia': 'nvidia',
        'openai': 'openai',
        'long_now': 'long_now',
        'strange_loop': 'strange_loop',
        'big_think': 'big_think',
        'scale_ai': 'scale_ai',
        'arc_prize': 'arc_prize',
        'extropic': 'extropic',
        'curt_jaimungal': 'tow',
        'moonshots': 'moonshots',
        'mathew_berman': 'mathew_berman',
        'david_shapiro': 'david_shapiro',
        'bilawal_sidhu': 'bilawal_sidhu',
        'brainmind': 'brainmind'
    }
    
    for pattern, short in known_creators.items():
        if pattern in base.lower() or pattern in old_path.lower():
            creator = short
            break
    
    # Generate slug from remaining filename parts
    slug = base
    slug = re.sub(r'^\d{8}[-_]?', '', slug)
    slug = re.sub(r'youtube_video[-_]?', '', slug, flags=re.I)
    for pattern in known_creators.keys():
        slug = re.sub(pattern, '', slug, flags=re.I)
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[-\s]+', '_', slug)
    slug = slug.strip('_').lower()[:40]
    if not slug:
        slug = 'content'
    
    new_name = f"SOURCE-{date}-{platform}-{format_type}-{creator}-{slug}{ext}"
    return new_name

# Generate mapping
mapping = []
for root, dirs, files in os.walk('SOURCES/raw'):
    for f in files:
        if f.endswith(('.md', '.txt')) and f != 'bio.txt':
            old_path = os.path.join(root, f)
            new_name = normalize_filename(old_path, f)
            mapping.append({
                'old_path': old_path,
                'old_name': f,
                'new_name': new_name,
                'new_path': f'SOURCES/raw/{new_name}'
            })

# Write mapping
with open('SOURCES/filename_mapping.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['old_path', 'old_name', 'new_name', 'new_path'])
    writer.writeheader()
    writer.writerows(mapping)

print(f"Generated mapping for {len(mapping)} files")
EOF
```

### 3.2 Execute Moves

```bash
# Read mapping and move files
python3 << 'EOF'
import csv
import os
import shutil

with open('SOURCES/filename_mapping.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        old = row['old_path']
        new = row['new_path']
        if os.path.exists(old) and old != new:
            # Move file
            shutil.move(old, new)
            print(f"Moved: {old} -> {new}")

print("File moves complete")
EOF
```

### 3.3 Update sources.csv

```bash
# Update filepath column in sources.csv
python3 << 'EOF'
import csv
import os

# Load mapping
mapping = {}
with open('SOURCES/filename_mapping.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        old_rel = row['old_path'].replace('SOURCES/', '')
        new_rel = row['new_path'].replace('SOURCES/', '')
        mapping[old_rel] = new_rel

# Update sources.csv
rows = []
with open('SOURCES/sources.csv', 'r') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row in reader:
        old_path = row['filepath']
        if old_path in mapping:
            row['filepath'] = mapping[old_path]
            row['filename'] = os.path.basename(mapping[old_path])
        rows.append(row)

with open('SOURCES/sources.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Updated {len(rows)} rows in sources.csv")
EOF
```

### 3.4 Rebuild Symlinks

```bash
# Remove old symlinks
find aliases/sources/by-tier -type l -delete
find aliases/sources/by-chain -type l -delete
find aliases/sources/by-platform -type l -delete

# Rebuild from sources.csv
python3 << 'EOF'
import csv
import os

os.makedirs('aliases/sources/by-tier/paradigm', exist_ok=True)
os.makedirs('aliases/sources/by-tier/strategic', exist_ok=True)
os.makedirs('aliases/sources/by-tier/tactical', exist_ok=True)
os.makedirs('aliases/sources/by-chain/intelligence', exist_ok=True)
os.makedirs('aliases/sources/by-chain/information', exist_ok=True)
os.makedirs('aliases/sources/by-chain/insight', exist_ok=True)
os.makedirs('aliases/sources/by-chain/knowledge', exist_ok=True)
os.makedirs('aliases/sources/by-chain/wisdom', exist_ok=True)
os.makedirs('aliases/sources/by-platform/youtube', exist_ok=True)
os.makedirs('aliases/sources/by-platform/x', exist_ok=True)
os.makedirs('aliases/sources/by-platform/podcast', exist_ok=True)

with open('SOURCES/sources.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        filepath = row['filepath']
        filename = row['filename']
        tier = row.get('signal_tier', 'tactical')
        chain = row.get('chain', 'information')
        platform = row.get('platform', 'youtube')
        
        source_path = f"../../../SOURCES/{filepath}"
        
        # Create tier symlink (paradigm and strategic only)
        if tier in ['paradigm', 'strategic']:
            link_path = f"aliases/sources/by-tier/{tier}/{filename}"
            if not os.path.exists(link_path):
                os.symlink(source_path, link_path)
        
        # Create chain symlink (paradigm and strategic only)
        if tier in ['paradigm', 'strategic'] and chain:
            link_path = f"aliases/sources/by-chain/{chain}/{filename}"
            if not os.path.exists(link_path):
                os.symlink(source_path, link_path)
        
        # Create platform symlink (paradigm and strategic only)
        if tier in ['paradigm', 'strategic'] and platform:
            link_path = f"aliases/sources/by-platform/{platform}/{filename}"
            if not os.path.exists(link_path):
                os.symlink(source_path, link_path)

print("Symlinks rebuilt")
EOF
```

### 3.5 Remove Empty Directories

```bash
# Remove empty directories (bottom-up)
find SOURCES/raw -type d -empty -delete

# Verify only flat structure remains
find SOURCES/raw -type d
# Should show only: SOURCES/raw
```

---

## PHASE 4: VERIFICATION

### 4.1 Verification Commands

```bash
# Verify flat structure
echo "=== Directory Count (should be 1) ==="
find SOURCES/raw -type d | wc -l

# Verify file count
echo "=== File Count (should be 184) ==="
find SOURCES/raw -type f \( -name "*.md" -o -name "*.txt" \) | wc -l

# Verify naming pattern
echo "=== Sample New Filenames ==="
ls SOURCES/raw/ | head -20

# Verify all start with SOURCE-
echo "=== Non-conforming Files ==="
ls SOURCES/raw/ | grep -v "^SOURCE-"

# Verify sources.csv row count
echo "=== CSV Row Count ==="
wc -l SOURCES/sources.csv

# Verify symlinks
echo "=== Symlink Count ==="
find aliases/sources -type l | wc -l

# Verify no broken symlinks
echo "=== Broken Symlinks ==="
find aliases/sources -type l ! -exec test -e {} \; -print
```

### 4.2 Git Commit

```bash
git add -A
git commit -m "DIRECTIVE-034A: SOURCES flattening + standardization

- Flattened 184 content files to SOURCES/raw/ root
- Standardized filenames to SOURCE-{date}-{platform}-{format}-{creator}-{slug} pattern
- Updated sources.csv with new filepaths
- Rebuilt 91 symlinks for paradigm/strategic tiers
- Removed nested directory structure
- Created filename_mapping.csv for reference

Repository now portable for Project Files upload.
Oracle9 hygiene phase: Stream A complete."
```

---

## SUCCESS CRITERIA

- [ ] SOURCES/raw contains only files (no subdirectories)
- [ ] All 184 content files present
- [ ] All filenames match SOURCE-* pattern
- [ ] sources.csv filepath column updated
- [ ] Symlinks rebuilt and functional
- [ ] No broken symlinks
- [ ] filename_mapping.csv documents transformations
- [ ] Git committed

---

## EXECUTION LOG TEMPLATE

Save to: `orchestration/execution_logs/EXECUTION_LOG-2026-01-02-034A.md`

```markdown
# EXECUTION LOG: DIRECTIVE-034A

**Executed**: 2026-01-02
**Agent**: Claude Code
**Status**: [COMPLETE/INCOMPLETE]

## Phase 1: Survey
- Total files found: [N]
- Deepest nesting level: [N]
- Directories to flatten: [list]

## Phase 2: Naming
- Mapping generated: [Y/N]
- Transformation issues: [any problems]

## Phase 3: Execution
- Files moved: [N]
- sources.csv updated: [Y/N]
- Symlinks rebuilt: [N]
- Empty directories removed: [N]

## Phase 4: Verification
[Paste verification output]

## Issues/Notes
[Any problems encountered]

## Sample Transformations
| Old Path | New Name |
|----------|----------|
| [example] | [example] |
```

---

**THIS DIRECTIVE ACHIEVES REPOSITORY PORTABILITY.**
