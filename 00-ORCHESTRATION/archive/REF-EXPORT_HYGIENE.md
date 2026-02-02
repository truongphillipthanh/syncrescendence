---
id: export-hygiene-protocol
kind: protocol
scope: repo
target: exports
owner: C3
version: 1.0.0
created: 2026-01-19
---

# REF-EXPORT_HYGIENE

## Purpose

Ensure evidence pack exports are free from contamination that could compromise archive integrity, cause confusion when unpacked on other platforms, or violate Constitutional rules.

## Contamination Types

### 1. macOS Resource Forks (`__MACOSX/`)

**Problem**: When creating zip archives on macOS using Finder or `zip` without special flags, the OS includes AppleDouble resource forks in a hidden `__MACOSX/` directory.

**Impact**:
- Confuses recipients on Linux/Windows
- Increases archive size unnecessarily
- Exposes internal macOS metadata

**Prevention**:
```bash
# Use COPYFILE_DISABLE environment variable
COPYFILE_DISABLE=1 zip -r archive.zip folder/

# Or use -X flag
zip -rX archive.zip folder/
```

### 2. Finder Metadata (`.DS_Store`)

**Problem**: macOS creates `.DS_Store` files in every directory to store Finder view settings (icon positions, sort order, etc.).

**Impact**:
- Leaks personal preferences
- Clutters recipient's systems
- May contain sensitive path information

**Prevention**:
```bash
# Exclude during zip creation
zip -r archive.zip folder/ -x "*.DS_Store" -x "*/.DS_Store"
```

### 3. AppleDouble Files (`._*`)

**Problem**: When files are copied to non-HFS+ volumes (FAT32, network shares), macOS creates companion `._filename` files to store extended attributes.

**Impact**:
- Doubles apparent file count
- Confuses file processing scripts
- May contain hidden metadata

**Prevention**:
```bash
zip -r archive.zip folder/ -x "*/._*" -x "._*"
```

### 4. Forbidden Root Artifacts (Constitutional Rule #4)

**Problem**: Exports must not include paths that violate Constitutional rules, specifically `OUTGOING/` or `outgoing/` (without leading dash).

**Impact**:
- Constitutional violation
- Structural confusion
- May indicate improper file organization

**Prevention**:
- Only pack from `-OUTGOING/` (with leading dash)
- Script validates source paths before packing

## The Solution

### Script-Based Workflow

Use `create_evidence_pack.sh` for all evidence pack exports:

```bash
# From repo root
./00-ORCHESTRATION/scripts/create_evidence_pack.sh -OUTGOING/20260119-drift_cleanup

# With custom output name
./00-ORCHESTRATION/scripts/create_evidence_pack.sh -OUTGOING/20260119-drift_cleanup drift_cleanup

# Verify existing archive
./00-ORCHESTRATION/scripts/create_evidence_pack.sh --verify-only existing.zip
```

### Makefile Integration

```bash
# Create pack
make pack SRC=-OUTGOING/20260119-drift_cleanup

# With custom name
make pack SRC=-OUTGOING/20260119-drift_cleanup NAME=drift_cleanup

# Verify existing archive
make pack-verify ARCHIVE=existing.zip
```

### Manual Workflow (Reference)

If you must create archives manually:

```bash
# Defense-in-depth approach (recommended)
cd /path/to/parent
COPYFILE_DISABLE=1 zip -rX output.zip directory/ \
    -x "*.DS_Store" \
    -x "*/.DS_Store" \
    -x "__MACOSX/*" \
    -x "*/__MACOSX/*" \
    -x "*/._*" \
    -x "._*"

# Post-creation verification
unzip -l output.zip | grep -E '__MACOSX|\.DS_Store|/\._'
```

## Verification Protocol

Before sharing any evidence pack:

### 1. Run Automated Verification

```bash
make pack-verify ARCHIVE=path/to/archive.zip
# or
./00-ORCHESTRATION/scripts/create_evidence_pack.sh --verify-only archive.zip
```

### 2. Manual Spot Check

```bash
# List contents and grep for contamination
unzip -l archive.zip | grep -E '__MACOSX|\.DS_Store|/\._'

# Should return nothing if clean
```

### 3. Test Extraction

```bash
# Extract to temp directory and inspect
mkdir -p /tmp/test_extract
unzip archive.zip -d /tmp/test_extract
find /tmp/test_extract -name "__MACOSX" -o -name ".DS_Store" -o -name "._*"
rm -rf /tmp/test_extract
```

## Remediation

If contamination is detected in an existing archive:

```bash
# Remove contamination in place
zip -d contaminated.zip "__MACOSX/*" "*.DS_Store" "*/.DS_Store" "*/._*"

# Or recreate from source
rm contaminated.zip
make pack SRC=original_directory NAME=clean_archive
```

## Exit Codes

The `create_evidence_pack.sh` script uses these exit codes:

| Code | Meaning |
|------|---------|
| 0 | Success - clean archive created |
| 1 | Invalid arguments |
| 2 | Source directory not found |
| 3 | Zip creation failed |
| 4 | Contamination detected in output |
| 5 | Forbidden patterns detected in source |

## Integration with Blitzkrieg

When finalizing Blitzkrieg passes, use the pack workflow:

```bash
# After blitzkrieg_finalize.sh creates the evidence directory
make pack SRC=-OUTGOING/20260119-blitzkrieg NAME=BLITZ_20260119_final
```

## Anti-Patterns

**Do Not**:
- Use Finder's "Compress" option (creates __MACOSX)
- Use plain `zip -r` without exclusions
- Skip verification before sharing
- Pack from `OUTGOING/` (without leading dash)
- Assume cleanliness without verification

## See Also

- `00-ORCHESTRATION/scripts/create_evidence_pack.sh` - Implementation
- `Makefile` - `pack` and `pack-verify` targets
- `REF-REPO_VALIDATION_PROTOCOL.md` - Related validation procedures
- `CLAUDE.md` - Constitutional Rule #4 (sanctioned exceptions)
