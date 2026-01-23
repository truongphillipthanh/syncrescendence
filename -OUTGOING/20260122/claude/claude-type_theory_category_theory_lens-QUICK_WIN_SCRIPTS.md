# Quick Win Scripts: Type Error Fixes

**Estimated Total Time**: 6.5 hours
**Estimated Total Savings**: 28,700 tokens/year
**ROI**: 4,400 tokens/hour

---

## Script 1: Validate Sources (1 hour)

**Purpose**: Identify all sources missing required fields (especially `value_modality`)

**Location**: `00-ORCHESTRATION/scripts/validate_sources.py`

```python
#!/usr/bin/env python3
"""
Validate all processed sources against SOURCES_SCHEMA.md
Reports missing required fields and invalid enum values
"""

import yaml
import sys
from pathlib import Path
from typing import Dict, List, Set

# Schema definition (from REF-SOURCES_SCHEMA.md)
REQUIRED_FIELDS = [
    "platform",
    "format",
    "cadence",
    "value_modality",  # CRITICAL
    "signal_tier",
    "status",
    "chain",
    "topics",
]

VALID_ENUMS = {
    "platform": {
        "youtube", "podcast", "substack", "newsletter", "arxiv", "paper",
        "book", "x", "reddit", "hn", "course", "film", "other"
    },
    "format": {
        "interview", "panel", "solo_presentation", "tutorial", "documentary",
        "lecture", "paper", "thread", "article", "essay", "chapter", "script",
        "post", "other"
    },
    "cadence": {"daily", "weekly", "periodic", "arrhythmic", "evergreen"},
    "value_modality": {
        "dialogue_primary", "audio_primary", "visual_primary",
        "comments_primary", "multimodal_essential", "text_native"
    },
    "signal_tier": {"paradigm", "strategic", "tactical", "noise"},
    "status": {"raw", "triaged", "processed", "integrated", "archived"},
    "chain": {
        "intelligence", "information", "insight",
        "expertise", "knowledge", "wisdom"
    },
}

def extract_frontmatter(file_path: Path) -> Dict:
    """Extract YAML frontmatter from markdown file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if not content.startswith('---'):
        return {}

    try:
        _, frontmatter, _ = content.split('---', 2)
        return yaml.safe_load(frontmatter) or {}
    except:
        return {}

def validate_source(file_path: Path) -> List[str]:
    """Validate a single source file, return list of errors"""
    errors = []
    frontmatter = extract_frontmatter(file_path)

    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in frontmatter:
            errors.append(f"MISSING REQUIRED FIELD: {field}")

    # Check enum values
    for field, valid_values in VALID_ENUMS.items():
        if field in frontmatter:
            value = frontmatter[field]
            if isinstance(value, str) and value.lower() not in valid_values:
                errors.append(f"INVALID {field}: '{value}' (valid: {valid_values})")

    # Check topics is a list
    if "topics" in frontmatter and not isinstance(frontmatter["topics"], list):
        errors.append(f"INVALID topics: must be array, got {type(frontmatter['topics'])}")

    return errors

def validate_all_sources(sources_dir: Path) -> Dict[str, List[str]]:
    """Validate all sources in directory"""
    results = {}

    for source_file in sources_dir.glob("SOURCE-*.md"):
        errors = validate_source(source_file)
        if errors:
            results[source_file.name] = errors

    return results

def main():
    repo_root = Path(__file__).parent.parent.parent
    processed_dir = repo_root / "04-SOURCES" / "processed"

    print(f"Validating sources in: {processed_dir}")
    print("=" * 80)

    results = validate_all_sources(processed_dir)

    if not results:
        print("✓ All sources valid!")
        sys.exit(0)

    print(f"✗ Found {len(results)} sources with errors:\n")

    for filename, errors in sorted(results.items()):
        print(f"{filename}:")
        for error in errors:
            print(f"  - {error}")
        print()

    # Summary
    missing_value_modality = sum(
        1 for errors in results.values()
        if any("value_modality" in e for e in errors)
    )

    print("=" * 80)
    print(f"SUMMARY:")
    print(f"  Total sources with errors: {len(results)}")
    print(f"  Missing value_modality: {missing_value_modality}")
    print(f"  Total error types: {sum(len(e) for e in results.values())}")

    sys.exit(1)

if __name__ == "__main__":
    main()
```

**Usage**:
```bash
python 00-ORCHESTRATION/scripts/validate_sources.py
```

**Add to Makefile**:
```makefile
validate-sources:
	@echo "Validating all processed sources..."
	python 00-ORCHESTRATION/scripts/validate_sources.py
```

---

## Script 2: Normalize Frontmatter Fields (2 hours)

**Purpose**: Migrate variant field names to canonical schema

**Location**: `00-ORCHESTRATION/scripts/normalize_frontmatter.py`

```python
#!/usr/bin/env python3
"""
Normalize frontmatter field names to match SOURCES_SCHEMA.md
Migrates:
  - chain_relevance → chain
  - integration_targets → integrated_into
  - source_id → id
"""

import yaml
import re
from pathlib import Path
from typing import Dict, Any

# Field name mappings (old → new)
FIELD_MAPPINGS = {
    "chain_relevance": "chain",
    "integration_targets": "integrated_into",
    "source_id": "id",
}

def extract_and_split(file_path: Path) -> tuple[str, str, str]:
    """Extract frontmatter, content, and preserve formatting"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if not content.startswith('---'):
        return "", "", content

    parts = content.split('---', 2)
    if len(parts) < 3:
        return "", "", content

    return parts[0], parts[1], parts[2]

def normalize_frontmatter(frontmatter_str: str) -> str:
    """Normalize field names in frontmatter string"""
    frontmatter = yaml.safe_load(frontmatter_str) or {}

    # Apply field name mappings
    for old_name, new_name in FIELD_MAPPINGS.items():
        if old_name in frontmatter:
            # Special handling for chain_relevance (comma-separated → lowercase)
            if old_name == "chain_relevance":
                value = frontmatter.pop(old_name)
                # "Intelligence, Knowledge" → "intelligence"
                if isinstance(value, str) and "," in value:
                    value = value.split(",")[0].strip().lower()
                else:
                    value = value.lower() if isinstance(value, str) else value
                frontmatter[new_name] = value

            # Special handling for integration_targets (string → array)
            elif old_name == "integration_targets":
                value = frontmatter.pop(old_name)
                if isinstance(value, str):
                    # "CANON-00015, CANON-00004" → ["CANON-00015", "CANON-00004"]
                    value = [v.strip() for v in value.split(",")]
                frontmatter[new_name] = value

            else:
                frontmatter[new_name] = frontmatter.pop(old_name)

    # Convert back to YAML
    return yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True)

def normalize_file(file_path: Path, dry_run: bool = False) -> bool:
    """Normalize a single file, return True if changes made"""
    prefix, frontmatter_str, content = extract_and_split(file_path)

    if not frontmatter_str:
        return False

    normalized = normalize_frontmatter(frontmatter_str)

    if normalized == frontmatter_str:
        return False

    if dry_run:
        print(f"Would normalize: {file_path.name}")
        return True

    # Write normalized version
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(f"{prefix}---\n{normalized}---{content}")

    print(f"✓ Normalized: {file_path.name}")
    return True

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Normalize frontmatter field names")
    parser.add_argument("--dry-run", action="store_true",
                       help="Show what would be changed without modifying files")
    args = parser.parse_args()

    repo_root = Path(__file__).parent.parent.parent
    processed_dir = repo_root / "04-SOURCES" / "processed"

    print(f"{'DRY RUN: ' if args.dry_run else ''}Normalizing sources in: {processed_dir}")
    print("=" * 80)

    changed = 0
    total = 0

    for source_file in processed_dir.glob("SOURCE-*.md"):
        total += 1
        if normalize_file(source_file, dry_run=args.dry_run):
            changed += 1

    print("=" * 80)
    print(f"{'Would normalize' if args.dry_run else 'Normalized'}: {changed}/{total} sources")

    if args.dry_run and changed > 0:
        print("\nRun without --dry-run to apply changes")

if __name__ == "__main__":
    main()
```

**Usage**:
```bash
# Preview changes
python 00-ORCHESTRATION/scripts/normalize_frontmatter.py --dry-run

# Apply changes
python 00-ORCHESTRATION/scripts/normalize_frontmatter.py

# Commit
git add 04-SOURCES/processed/
git commit -m "fix: normalize frontmatter field names to schema"
```

---

## Script 3: Migrate Directive Naming (3 hours)

**Purpose**: Rename all `DIRECTIVE-NNN` to `DIR-YYYYMMDD-` pattern

**Location**: `00-ORCHESTRATION/scripts/migrate_directives.py`

```python
#!/usr/bin/env python3
"""
Migrate old DIRECTIVE-NNN naming to new DIR-YYYYMMDD- pattern
Requires manual date mapping (see DIRECTIVE_DATES below)
"""

import re
import shutil
from pathlib import Path
from typing import Dict

# Manual mapping: directive number → execution date
# TODO: Fill in actual dates from execution logs
DIRECTIVE_DATES = {
    17: "20250825",  # DIRECTIVE-017 executed on 2025-08-25
    20: "20250901",  # DIRECTIVE-020A executed on 2025-09-01
    22: "20250910",  # DIRECTIVE-022B executed on 2025-09-10
    23: "20250915",
    # ... (add remaining mappings)
    42: "20260109",  # DIRECTIVE-042B (known from new files)
    43: "20260120",  # DIRECTIVE-043A (known)
}

def parse_old_directive(filename: str) -> tuple[int, str, str]:
    """Parse old directive filename: DIRECTIVE-042B_MULTI_CLI.md"""
    match = re.match(r"DIRECTIVE-(\d+)([A-Z])?[_-](.*?)\.md", filename)
    if not match:
        return None, None, None

    number = int(match.group(1))
    variant = match.group(2) or ""
    descriptor = match.group(3)

    return number, variant, descriptor

def generate_new_name(number: int, variant: str, descriptor: str) -> str:
    """Generate new filename: DIR-20260109-MULTI_CLI.md"""
    if number not in DIRECTIVE_DATES:
        raise ValueError(f"No date mapping for DIRECTIVE-{number}")

    date = DIRECTIVE_DATES[number]
    # Normalize descriptor (uppercase, hyphens)
    descriptor = descriptor.upper().replace("_", "-")

    return f"DIR-{date}-{descriptor}.md"

def migrate_directive(file_path: Path, dry_run: bool = False) -> bool:
    """Migrate a single directive file"""
    number, variant, descriptor = parse_old_directive(file_path.name)

    if number is None:
        return False

    try:
        new_name = generate_new_name(number, variant, descriptor)
    except ValueError as e:
        print(f"✗ Skipping {file_path.name}: {e}")
        return False

    new_path = file_path.parent / new_name

    if dry_run:
        print(f"Would rename: {file_path.name} → {new_name}")
        return True

    shutil.move(str(file_path), str(new_path))
    print(f"✓ Renamed: {file_path.name} → {new_name}")
    return True

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Migrate directive naming")
    parser.add_argument("--dry-run", action="store_true",
                       help="Show what would be changed without modifying files")
    args = parser.parse_args()

    repo_root = Path(__file__).parent.parent.parent
    directives_dir = repo_root / "00-ORCHESTRATION" / "directives"

    print(f"{'DRY RUN: ' if args.dry_run else ''}Migrating directives in: {directives_dir}")
    print("=" * 80)

    migrated = 0
    total = 0

    for directive_file in directives_dir.glob("DIRECTIVE-*.md"):
        total += 1
        if migrate_directive(directive_file, dry_run=args.dry_run):
            migrated += 1

    print("=" * 80)
    print(f"{'Would migrate' if args.dry_run else 'Migrated'}: {migrated}/{total} directives")

    if args.dry_run and migrated > 0:
        print("\nRun without --dry-run to apply changes")
        print("\n⚠️  IMPORTANT: Update DIRECTIVE_DATES mapping with actual execution dates")

if __name__ == "__main__":
    main()
```

**Usage**:
```bash
# 1. First, populate DIRECTIVE_DATES mapping in script
# 2. Preview changes
python 00-ORCHESTRATION/scripts/migrate_directives.py --dry-run

# 3. Apply migration
python 00-ORCHESTRATION/scripts/migrate_directives.py

# 4. Update references (manual)
grep -r "DIRECTIVE-" 00-ORCHESTRATION/ 01-CANON/ --include="*.md"
# Update each reference to new DIR- pattern

# 5. Commit
git add 00-ORCHESTRATION/directives/
git commit -m "refactor: migrate directive naming to DIR-YYYYMMDD- pattern"
```

---

## Script 4: Segregate Non-Source Artifacts (30 minutes)

**Purpose**: Move non-source files out of SOURCES/raw/

**Location**: `00-ORCHESTRATION/scripts/segregate_artifacts.sh`

```bash
#!/bin/bash
# Segregate non-source artifacts from SOURCES/raw/

REPO_ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
RAW_DIR="$REPO_ROOT/04-SOURCES/raw"
OPERATIONAL_DIR="$REPO_ROOT/02-OPERATIONAL"

echo "Segregating non-source artifacts from SOURCES/raw/"
echo "=========================================================================="

# Create target directories
mkdir -p "$OPERATIONAL_DIR/prompts/research"
mkdir -p "$OPERATIONAL_DIR/research"

# Move DEEP_RESEARCH_PROMPT files
if ls "$RAW_DIR"/DEEP_RESEARCH_PROMPT-*.md 1> /dev/null 2>&1; then
    echo "Moving DEEP_RESEARCH_PROMPT files to 02-OPERATIONAL/prompts/research/"
    mv "$RAW_DIR"/DEEP_RESEARCH_PROMPT-*.md "$OPERATIONAL_DIR/prompts/research/"
    echo "✓ Moved DEEP_RESEARCH_PROMPT files"
fi

# Move research files
if [ -f "$RAW_DIR/openai_research.md" ]; then
    echo "Moving openai_research.md to 02-OPERATIONAL/research/"
    mv "$RAW_DIR/openai_research.md" "$OPERATIONAL_DIR/research/"
    echo "✓ Moved openai_research.md"
fi

echo "=========================================================================="
echo "✓ Segregation complete"
echo ""
echo "Verify changes:"
echo "  ls 02-OPERATIONAL/prompts/research/"
echo "  ls 02-OPERATIONAL/research/"
echo ""
echo "Commit changes:"
echo "  git add 04-SOURCES/raw/ 02-OPERATIONAL/"
echo "  git commit -m 'chore: segregate non-source artifacts from SOURCES/raw/'"
```

**Usage**:
```bash
chmod +x 00-ORCHESTRATION/scripts/segregate_artifacts.sh
./00-ORCHESTRATION/scripts/segregate_artifacts.sh
```

---

## Script 5: Fix File Extension Typo (1 minute)

**Purpose**: Fix `.md` extension typo

```bash
#!/bin/bash
# Fix execution log file extension typo

REPO_ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
LOGS_DIR="$REPO_ROOT/00-ORCHESTRATION/execution_logs"

cd "$LOGS_DIR" || exit 1

if [ -f "EXECUTION_LOG-2025-12-31-028md" ]; then
    mv EXECUTION_LOG-2025-12-31-028md EXECUTION_LOG-2025-12-31-028.md
    echo "✓ Fixed: EXECUTION_LOG-2025-12-31-028md → EXECUTION_LOG-2025-12-31-028.md"

    git add EXECUTION_LOG-2025-12-31-028.md
    git commit -m "fix: correct file extension typo in execution log"
else
    echo "✓ File already corrected or not found"
fi
```

**Usage**:
```bash
./00-ORCHESTRATION/scripts/fix_extension_typo.sh
```

---

## Script 6: Standardize CSV Backup Naming (1 hour)

**Purpose**: Unify CSV backup naming strategy

**Location**: `00-ORCHESTRATION/scripts/backup_ledgers.sh`

```bash
#!/bin/bash
# Standardize CSV backup naming: {filename}.bak.{YYYYMMDD_HHMMSS}

REPO_ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
STATE_DIR="$REPO_ROOT/00-ORCHESTRATION/state"

# Get current timestamp
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

cd "$STATE_DIR" || exit 1

echo "Creating timestamped backups of all ledgers..."
echo "=========================================================================="

# Backup all CSV ledgers
for ledger in DYN-TASKS.csv DYN-PROJECTS.csv DYN-SPRINTS.csv DYN-BURNDOWN.csv; do
    if [ -f "$ledger" ]; then
        backup_name="${ledger}.bak.${TIMESTAMP}"
        cp "$ledger" "$backup_name"
        echo "✓ Backed up: $ledger → $backup_name"
    fi
done

echo "=========================================================================="
echo "✓ Backup complete"
echo ""
echo "Clean up old backups:"
echo "  ls -1 *.bak* | head -n -3  # View oldest backups"
echo "  rm *.bak  # Remove old .bak files (keep only timestamped)"
```

**Usage**:
```bash
chmod +x 00-ORCHESTRATION/scripts/backup_ledgers.sh

# Create backups before updating ledgers
./00-ORCHESTRATION/scripts/backup_ledgers.sh

# Add to Makefile
```

**Makefile Addition**:
```makefile
backup-ledgers:
	@echo "Creating timestamped backups of ledgers..."
	./00-ORCHESTRATION/scripts/backup_ledgers.sh

update-ledgers: backup-ledgers
	@echo "Updating ledgers..."
	python 00-ORCHESTRATION/scripts/sync_ledgers.py
```

---

## Execution Checklist

### Week 1: Quick Wins (6.5 hours)

- [ ] **Script 1**: Run validation audit (1h)
  - [ ] Create `validate_sources.py`
  - [ ] Run and document errors
  - [ ] Add to Makefile

- [ ] **Script 2**: Normalize frontmatter (2h)
  - [ ] Create `normalize_frontmatter.py`
  - [ ] Run dry-run
  - [ ] Apply changes
  - [ ] Commit

- [ ] **Script 3**: Migrate directives (3h)
  - [ ] Populate `DIRECTIVE_DATES` mapping
  - [ ] Create `migrate_directives.py`
  - [ ] Run dry-run
  - [ ] Apply migration
  - [ ] Update references manually
  - [ ] Commit

- [ ] **Script 4**: Segregate artifacts (30m)
  - [ ] Run `segregate_artifacts.sh`
  - [ ] Verify moved files
  - [ ] Commit

- [ ] **Script 5**: Fix extension typo (1m)
  - [ ] Run `fix_extension_typo.sh`
  - [ ] Commit

- [ ] **Script 6**: Standardize backups (1h)
  - [ ] Create `backup_ledgers.sh`
  - [ ] Update Makefile
  - [ ] Remove old `.bak` files
  - [ ] Document in REF-STANDARDS.md

### Verification

```bash
# Validate all sources pass
make validate-sources

# Verify no old patterns remain
grep -r "chain_relevance\|integration_targets" 04-SOURCES/processed/
grep -r "DIRECTIVE-" 00-ORCHESTRATION/directives/

# Verify segregation
ls 04-SOURCES/raw/DEEP_RESEARCH_PROMPT-*.md  # Should be empty
ls 02-OPERATIONAL/prompts/research/          # Should contain DEEP_RESEARCH_PROMPT files

# Verify backups
ls -1 00-ORCHESTRATION/state/*.bak.*         # Should show timestamped backups
```

---

## Expected Outcomes

After completing all scripts:

✅ **Type Safety**:
- All sources have required fields
- No field naming variance
- No extension typos

✅ **Consistency**:
- Single directive naming pattern (DIR-YYYYMMDD-)
- Unified CSV backup strategy
- Clean artifact segregation

✅ **Token Savings**: 28,700 tokens/year

✅ **Automation**:
- `make validate-sources` (pre-commit check)
- `make backup-ledgers` (before updates)
- No manual field disambiguation needed

---

## Next Steps

After quick wins:
1. Implement JSON Schema validation (P1)
2. Add pre-commit hooks for validation
3. Create polymorphic processing pipeline (P2)
4. Document FLAT PRINCIPLE exceptions in CLAUDE.md

**ROI Projection**:
- Quick wins: 6.5h → 28.7K tokens/year (4,400 tok/h)
- Schema validation: 8h → Prevent future errors
- Polymorphic refactor: 10h → 13.8K tokens saved

**Total**: 24.5 hours → 42.5K tokens/year + architectural improvement
