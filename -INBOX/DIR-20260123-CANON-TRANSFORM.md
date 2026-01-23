# DIRECTIVE: CANON Transformation + Directory Rename + Offload
## DIR-20260123-CANON-TRANSFORM

**Date**: 2026-01-23
**From**: Claude Web (INTERPRETER)
**To**: Claude Code (EXECUTOR)
**Phase**: Semantic Compression Execution
**Depends On**: 
- DIR-20260123-INFRASTRUCTURE-STABILIZATION ✅
- DIR-20260123-SEMANTIC-CASCADE ✅
- Principal approves directory renames (PENDING)
- Principal sets up rclone (PENDING)

---

## CONTEXT

Two directives complete. SN infrastructure ready. This directive executes the actual transformation work:
1. Rename directories to reflect true ontology
2. Execute transcript offload (requires rclone)
3. Begin CANON → SN conversion (16 monoliths first)

**Conditional Execution**: Some lanes require Principal action first. Execute what's unblocked immediately; queue the rest.

---

## LANE A: Directory Rename (Requires Principal Approval)

### Wait Condition
```bash
# Principal must confirm this rename set before execution
# Signal: Create file .rename-approved in repo root
```

### Execution (Once Approved)

```bash
#!/bin/bash
# Directory Rename Script
# Preserves git history via git mv

set -e  # Exit on error

echo "=== Directory Rename Execution ==="

# 1. Rename 02-OPERATIONAL → 02-ENGINE
git mv 02-OPERATIONAL 02-ENGINE
echo "✓ 02-OPERATIONAL → 02-ENGINE"

# 2. Rename 05-ARCHIVE → 05-MEMORY
git mv 05-ARCHIVE 05-MEMORY
echo "✓ 05-ARCHIVE → 05-MEMORY"

# 3. Update all references
echo "Updating references..."

# Find and replace in all .md files
find . -name "*.md" -type f -exec sed -i '' \
    -e 's|02-OPERATIONAL|02-ENGINE|g' \
    -e 's|05-ARCHIVE|05-MEMORY|g' \
    {} \;

# Find and replace in all .yaml files
find . -name "*.yaml" -type f -exec sed -i '' \
    -e 's|02-OPERATIONAL|02-ENGINE|g' \
    -e 's|05-ARCHIVE|05-MEMORY|g' \
    {} \;

# Find and replace in all .py files
find . -name "*.py" -type f -exec sed -i '' \
    -e 's|02-OPERATIONAL|02-ENGINE|g' \
    -e 's|05-ARCHIVE|05-MEMORY|g' \
    {} \;

# Find and replace in shell scripts
find . -name "*.sh" -type f -exec sed -i '' \
    -e 's|02-OPERATIONAL|02-ENGINE|g' \
    -e 's|05-ARCHIVE|05-MEMORY|g' \
    {} \;

# 4. Update CLAUDE.md directory map
sed -i '' \
    -e 's|02-OPERATIONAL.*Executable components|02-ENGINE/ — Executable components|g' \
    -e 's|05-ARCHIVE.*Historical artifacts|05-MEMORY/ — Short-term memory, staging|g' \
    CLAUDE.md

# 5. Verify no orphaned references
echo "Checking for orphaned references..."
orphans_operational=$(grep -r "02-OPERATIONAL" --include="*.md" . 2>/dev/null | wc -l)
orphans_archive=$(grep -r "05-ARCHIVE" --include="*.md" . 2>/dev/null | wc -l)

if [ "$orphans_operational" -gt 0 ] || [ "$orphans_archive" -gt 0 ]; then
    echo "⚠ Found orphaned references:"
    grep -r "02-OPERATIONAL" --include="*.md" . 2>/dev/null || true
    grep -r "05-ARCHIVE" --include="*.md" . 2>/dev/null || true
    echo "Manual review required."
else
    echo "✓ No orphaned references"
fi

# 6. Commit
git add -A
git commit -m "refactor: rename directories to reflect true ontology

- 02-OPERATIONAL → 02-ENGINE (it's what makes things run)
- 05-ARCHIVE → 05-MEMORY (short-term, not permanent archive)
- Updated all references across corpus"

echo "=== Directory Rename Complete ==="
```

### Post-Rename Verification

```bash
# Verify structure
ls -la | grep -E "^d"
# Expected:
# 00-ORCHESTRATION/
# 01-CANON/
# 02-ENGINE/
# 03-QUEUE/
# 04-SOURCES/
# 05-MEMORY/
# 06-EXEMPLA/

# Verify no broken references
grep -r "02-OPERATIONAL" --include="*.md" . | wc -l  # Should be 0
grep -r "05-ARCHIVE" --include="*.md" . | wc -l      # Should be 0
```

---

## LANE B: Transcript Offload (Requires rclone)

### Wait Condition
```bash
# Principal must have rclone configured
# Test: rclone lsd gdrive: should list Google Drive contents
```

### Execution (Once rclone Ready)

```bash
#!/bin/bash
# Transcript Offload Script
# Moves raw transcripts to Google Drive, keeps pointers

set -e

GDRIVE_REMOTE="gdrive"  # Adjust if different
GDRIVE_PATH="Syncrescendence/corpus-offload"

echo "=== Transcript Offload Execution ==="

# 1. Create Google Drive structure
echo "Creating Google Drive directories..."
rclone mkdir "$GDRIVE_REMOTE:$GDRIVE_PATH/raw-transcripts"
rclone mkdir "$GDRIVE_REMOTE:$GDRIVE_PATH/youtube-queue"

# 2. Identify raw transcripts in 04-SOURCES
echo "Identifying raw transcripts..."
find 04-SOURCES -name "*.txt" -type f > /tmp/raw_transcript_list.txt
RAW_COUNT=$(wc -l < /tmp/raw_transcript_list.txt)
echo "Found $RAW_COUNT raw transcripts"

# 3. Upload to Google Drive
echo "Uploading to Google Drive..."
while read -r file; do
    rclone copy "$file" "$GDRIVE_REMOTE:$GDRIVE_PATH/raw-transcripts/" --progress
done < /tmp/raw_transcript_list.txt

# 4. Verify upload
UPLOADED=$(rclone ls "$GDRIVE_REMOTE:$GDRIVE_PATH/raw-transcripts/" | wc -l)
echo "Uploaded: $UPLOADED files"

if [ "$UPLOADED" -ne "$RAW_COUNT" ]; then
    echo "⚠ Upload count mismatch! Expected $RAW_COUNT, got $UPLOADED"
    echo "Manual verification required before deletion."
    exit 1
fi

# 5. Remove from repo (after verification)
echo "Removing from local repo..."
while read -r file; do
    git rm "$file"
done < /tmp/raw_transcript_list.txt

# 6. Create pointer document
cat > 04-SOURCES/OFFLOADED_TRANSCRIPTS.md << EOF
# Offloaded Transcripts

**Date**: $(date +%Y-%m-%d)
**Location**: Google Drive > Syncrescendence > corpus-offload > raw-transcripts
**Count**: $RAW_COUNT files

## Retrieval

\`\`\`bash
# Download all
rclone copy $GDRIVE_REMOTE:$GDRIVE_PATH/raw-transcripts/ ./04-SOURCES/raw/

# Download specific file
rclone copy "$GDRIVE_REMOTE:$GDRIVE_PATH/raw-transcripts/filename.txt" ./
\`\`\`

## Manifest

See \`/tmp/raw_transcript_list.txt\` or query Google Drive:
\`\`\`bash
rclone ls $GDRIVE_REMOTE:$GDRIVE_PATH/raw-transcripts/
\`\`\`
EOF

# 7. Handle 03-QUEUE YouTube transcripts (if any)
if [ -d "03-QUEUE" ] && [ "$(find 03-QUEUE -name "*.txt" -type f | wc -l)" -gt 0 ]; then
    echo "Uploading 03-QUEUE transcripts..."
    find 03-QUEUE -name "*.txt" -type f -exec rclone copy {} "$GDRIVE_REMOTE:$GDRIVE_PATH/youtube-queue/" \;
    find 03-QUEUE -name "*.txt" -type f -exec git rm {} \;
    
    cat > 03-QUEUE/OFFLOADED_YOUTUBE.md << EOF
# Offloaded YouTube Transcripts

**Date**: $(date +%Y-%m-%d)
**Location**: Google Drive > Syncrescendence > corpus-offload > youtube-queue

## Note
Raw YouTube transcripts offloaded. High-signal content should be processed
through IIC pipeline and integrated, not stored here.
EOF
fi

# 8. Commit
git add -A
git commit -m "chore: offload raw transcripts to Google Drive

- $RAW_COUNT raw .txt files moved to Google Drive
- Created pointer documents for retrieval
- Space freed: ~4MB estimated"

echo "=== Transcript Offload Complete ==="
echo "Space freed: approximately 4MB"
```

---

## LANE C: CANON SN Conversion (Monoliths First)

### Methodology

Use the SN conversion template and encode/decode tools to transform CANON documents.

**Priority Order** (by word count, descending):
1. CANON-00007-EVALUATION-cosmos.md (34,829 words)
2. CANON-00011-ARTIFACT_PROTOCOL-cosmos.md (25,142 words)
3. CANON-00004-EVOLUTION-cosmos.md (23,457 words)
4. CANON-00005-SYNCRESCENDENCE-cosmos.md
5. CANON-00012-MODAL_SEQUENCE-cosmos.md
6. ... (remaining 11 monoliths)

### Conversion Script

```python
#!/usr/bin/env python3
"""
CANON SN Converter
Transforms CANON documents to Semantic Notation format
"""

import sys
import re
from pathlib import Path

# Load tools
sys.path.insert(0, str(Path(__file__).parent))
from sn_encode import load_glossary, encode_text

def extract_sections(content: str) -> list:
    """Extract markdown sections as conversion units"""
    sections = []
    current_section = {"level": 0, "title": "Root", "content": ""}
    
    for line in content.split('\n'):
        if line.startswith('#'):
            if current_section["content"].strip():
                sections.append(current_section)
            level = len(re.match(r'^#+', line).group())
            title = line.lstrip('#').strip()
            current_section = {"level": level, "title": title, "content": ""}
        else:
            current_section["content"] += line + "\n"
    
    if current_section["content"].strip():
        sections.append(current_section)
    
    return sections

def generate_sutra(title: str, content: str) -> str:
    """Generate one-line sutra from section"""
    # Take first sentence, compress
    first_sentence = content.split('.')[0].strip()
    if len(first_sentence) > 100:
        first_sentence = first_sentence[:97] + "..."
    return first_sentence

def section_to_block(section: dict, glossary: dict) -> str:
    """Convert a section to SN block"""
    title = section["title"]
    content = section["content"].strip()
    
    if not content:
        return ""
    
    # Determine block type
    block_type = "TERM"  # Default
    if any(word in title.lower() for word in ["must", "should", "rule", "constraint", "principle"]):
        block_type = "NORM"
    elif any(word in title.lower() for word in ["process", "procedure", "protocol", "workflow"]):
        block_type = "PROC"
    
    # Generate sutra
    sutra = generate_sutra(title, content)
    
    # Encode content
    encoded_content = encode_text(content, glossary)
    
    # Build block
    block = f"""{block_type} {title.replace(' ', '')}:
    sutra: "{sutra}"
    gloss:
        {encoded_content[:500]}{"..." if len(encoded_content) > 500 else ""}
end
"""
    return block

def convert_canon_file(input_path: Path, output_path: Path):
    """Convert a CANON file to SN format"""
    glossary = load_glossary()
    
    with open(input_path) as f:
        content = f.read()
    
    # Extract frontmatter if present
    frontmatter = ""
    if content.startswith("---"):
        end_idx = content.find("---", 3)
        if end_idx > 0:
            frontmatter = content[:end_idx+3]
            content = content[end_idx+3:]
    
    # Extract sections
    sections = extract_sections(content)
    
    # Convert each section
    blocks = []
    for section in sections:
        block = section_to_block(section, glossary)
        if block:
            blocks.append(block)
    
    # Assemble output
    output = frontmatter + "\n\n# SN Format (Converted)\n\n"
    output += "\n\n".join(blocks)
    
    # Write output
    with open(output_path, 'w') as f:
        f.write(output)
    
    # Calculate compression
    original_size = len(content)
    converted_size = len(output)
    compression = (1 - converted_size / original_size) * 100
    
    print(f"Converted: {input_path.name}")
    print(f"  Original: {original_size:,} chars")
    print(f"  Converted: {converted_size:,} chars")
    print(f"  Compression: {compression:.1f}%")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: convert_canon.py <input.md> [output.md]")
        sys.exit(1)
    
    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else input_path.with_suffix('.sn.md')
    
    convert_canon_file(input_path, output_path)
```

### Execution Plan

```bash
# 1. Create conversion script
cat > 00-ORCHESTRATION/scripts/convert_canon.py << 'EOF'
[script content above]
EOF
chmod +x 00-ORCHESTRATION/scripts/convert_canon.py

# 2. Create SN output directory
mkdir -p 01-CANON/sn-converted

# 3. Convert monoliths (one at a time, with review)
for file in $(head -16 00-ORCHESTRATION/state/ARCH-CANON_AUDIT_MANIFEST.md | tail -16 | awk '{print $2}'); do
    echo "Converting: $file"
    python3 00-ORCHESTRATION/scripts/convert_canon.py "01-CANON/$file" "01-CANON/sn-converted/$file"
    
    # Pause for review
    echo "Review 01-CANON/sn-converted/$file before continuing"
    read -p "Press Enter to continue, Ctrl+C to abort..."
done

# 4. After review, replace originals (optional)
# Only if Principal approves after reviewing conversions
```

### Verification

```bash
# Round-trip test
python3 00-ORCHESTRATION/scripts/sn_encode.py 01-CANON/CANON-00002.md > /tmp/encoded.md
python3 00-ORCHESTRATION/scripts/sn_decode.py /tmp/encoded.md > /tmp/decoded.md
diff 01-CANON/CANON-00002.md /tmp/decoded.md

# Compression metrics
for file in 01-CANON/sn-converted/*.md; do
    original="01-CANON/$(basename $file)"
    orig_size=$(wc -c < "$original")
    conv_size=$(wc -c < "$file")
    echo "$(basename $file): $orig_size → $conv_size ($(( 100 - conv_size * 100 / orig_size ))% reduction)"
done
```

---

## LANE D: Obsidian Backlink Execution

### Execute on Full Corpus

```bash
# Run the backlink script created in infrastructure directive
cd /path/to/syncrescendence

# Dry run first
./00-ORCHESTRATION/scripts/add_obsidian_backlinks.sh . --dry-run 2>&1 | head -50

# If clean, execute
./00-ORCHESTRATION/scripts/add_obsidian_backlinks.sh .

# Verify
grep -r "\[\[CANON-" --include="*.md" . | wc -l
# Should show many [[CANON-XXXXX-NAME]] style links

# Commit
git add -A
git commit -m "feat: add Obsidian-style backlinks across corpus"
```

---

## LANE E: Update Entry Points for New Structure

### Update CLAUDE.md

```bash
# Update directory map section
sed -i '' 's/02-OPERATIONAL.*—.*/02-ENGINE\/ — Executable components (functions, prompts, protocols)/g' CLAUDE.md
sed -i '' 's/05-ARCHIVE.*—.*/05-MEMORY\/ — Short-term memory, staging (not permanent archive)/g' CLAUDE.md

# Add SN reference
cat >> CLAUDE.md << 'EOF'

## Semantic Notation

This corpus uses Semantic Notation (SN) for compression.

**Glossary**: `00-ORCHESTRATION/notation/symbols.yaml`
**Encode**: `00-ORCHESTRATION/scripts/sn_encode.py`
**Decode**: `00-ORCHESTRATION/scripts/sn_decode.py`

Key operators: `::` (expands to), `|` (constrained by), `>>` (transforms into)
EOF
```

### Update COCKPIT.md

```bash
# Ensure COCKPIT reflects new directory names
sed -i '' 's/02-OPERATIONAL/02-ENGINE/g' COCKPIT.md
sed -i '' 's/05-ARCHIVE/05-MEMORY/g' COCKPIT.md
```

---

## SUCCESS CRITERIA

### Lane A (Directory Rename)
- [ ] 02-OPERATIONAL renamed to 02-ENGINE
- [ ] 05-ARCHIVE renamed to 05-MEMORY
- [ ] Zero orphaned references to old names
- [ ] Git history preserved

### Lane B (Offload)
- [ ] Raw transcripts uploaded to Google Drive
- [ ] Pointer documents created
- [ ] ~4MB freed from repo
- [ ] Retrieval instructions documented

### Lane C (CANON Conversion)
- [ ] convert_canon.py script created
- [ ] At least 3 monoliths converted to SN
- [ ] Compression metrics documented
- [ ] Round-trip verification passed

### Lane D (Obsidian)
- [ ] Backlinks added across corpus
- [ ] [[CANON-XXXXX-NAME]] format verified
- [ ] No broken links introduced

### Lane E (Entry Points)
- [ ] CLAUDE.md updated with new directories + SN
- [ ] COCKPIT.md updated with new directories

---

## EXECUTION ORDER

```
IF Principal approved renames:
    1. Lane A (rename) — foundation for everything else
    
IF rclone configured:
    2. Lane B (offload) — space recovery
    
UNCONDITIONAL:
    3. Lane C (CANON conversion) — begin with script creation
    4. Lane D (Obsidian backlinks) — enhances navigation
    5. Lane E (entry points) — documentation alignment
```

---

## TIME ESTIMATE

| Lane | Hours | Condition |
|------|-------|-----------|
| A: Directory Rename | 0.5 | Requires approval |
| B: Offload | 0.5 | Requires rclone |
| C: CANON Conversion | 2.0 | Ready now |
| D: Obsidian Backlinks | 0.25 | Ready now |
| E: Entry Points | 0.25 | After A |
| **TOTAL** | **3.5** | — |

---

## DEPENDENCIES

```
Principal Actions Required:
├── Approve directory renames (signal: create .rename-approved)
├── Configure rclone for Google Drive
└── Review first CANON conversions before bulk execution

Claude Code Can Proceed With:
├── Lane C: Create conversion script
├── Lane C: Convert first 3 monoliths (staging)
└── Lane D: Obsidian backlinks (if approved)
```

---

## HANDOFF

```
HANDOFF-20260123-INTERPRETER-TO-EXECUTOR
Directive: DIR-20260123-CANON-TRANSFORM
Phase: Semantic compression execution
Depends: 
  - Infrastructure ✅
  - Semantic Cascade ✅
  - Principal approval for renames (PENDING)
  - rclone setup (PENDING)
Partial execution: Lanes C, D can proceed unconditionally
```

---

**END DIRECTIVE**
