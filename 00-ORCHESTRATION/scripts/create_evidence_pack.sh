#!/usr/bin/env bash
#
# create_evidence_pack.sh - Create clean evidence pack exports
#
# Ensures exports are free from:
#   - __MACOSX resource fork directories
#   - .DS_Store metadata files
#   - Forbidden root artifacts (OUTGOING/, outgoing/)
#
# Usage:
#   ./create_evidence_pack.sh <source_directory> [output_name]
#
# Examples:
#   ./create_evidence_pack.sh -OUTGOING/20260119-drift_cleanup drift_cleanup
#   ./create_evidence_pack.sh -OUTGOING/20260118-blitzkrieg
#
# The script will:
#   1. Create a clean zip without macOS resource forks
#   2. Exclude .DS_Store files automatically
#   3. Validate the archive for contamination
#   4. Report any Constitutional Rule #4 violations
#
# Exit codes:
#   0 - Success
#   1 - Invalid arguments
#   2 - Source directory not found
#   3 - Zip creation failed
#   4 - Contamination detected in output
#   5 - Forbidden patterns detected

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Repository root (script location relative)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Print usage
usage() {
    cat << 'EOF'
Usage: create_evidence_pack.sh <source_directory> [output_name]

Creates a clean zip archive free from macOS contamination.

Arguments:
  source_directory  Directory to pack (relative to repo root or absolute)
  output_name       Output filename without .zip extension (optional)
                    Defaults to basename of source_directory

Options:
  -h, --help        Show this help message
  -v, --verify-only Check existing archive for contamination
  -o, --output-dir  Directory for output zip (default: same as source parent)

Examples:
  ./create_evidence_pack.sh -OUTGOING/20260119-drift_cleanup drift_cleanup
  ./create_evidence_pack.sh -OUTGOING/20260118-blitzkrieg
  ./create_evidence_pack.sh --verify-only existing_archive.zip

EOF
}

# Log functions
log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Verify archive for contamination
verify_archive() {
    local archive="$1"
    local contamination_found=0

    log_info "Verifying archive: $archive"

    # Check for __MACOSX
    if unzip -l "$archive" 2>/dev/null | grep -qE "__MACOSX"; then
        log_error "__MACOSX resource forks detected!"
        unzip -l "$archive" | grep "__MACOSX" | head -10
        contamination_found=1
    fi

    # Check for .DS_Store
    if unzip -l "$archive" 2>/dev/null | grep -qE "\.DS_Store"; then
        log_error ".DS_Store files detected!"
        unzip -l "$archive" | grep "\.DS_Store" | head -10
        contamination_found=1
    fi

    # Check for forbidden patterns (Constitutional Rule #4)
    # Forbidden: OUTGOING/ or outgoing/ (without leading dash)
    if unzip -l "$archive" 2>/dev/null | grep -qE "(^|/)OUTGOING/|(^|/)outgoing/"; then
        log_error "Forbidden pattern detected: OUTGOING/ or outgoing/ (violates Constitutional Rule #4)"
        unzip -l "$archive" | grep -E "(^|/)OUTGOING/|(^|/)outgoing/" | head -10
        contamination_found=1
    fi

    # Check for AppleDouble files (._*)
    if unzip -l "$archive" 2>/dev/null | grep -qE "/\._[^/]+$"; then
        log_error "AppleDouble resource fork files detected!"
        unzip -l "$archive" | grep -E "/\._[^/]+" | head -10
        contamination_found=1
    fi

    if [ $contamination_found -eq 0 ]; then
        log_info "Archive is clean - no contamination detected"
        return 0
    else
        return 4
    fi
}

# Main pack function
create_pack() {
    local source_dir="$1"
    local output_name="$2"
    local output_dir="$3"

    # Resolve source directory
    if [[ "$source_dir" != /* ]]; then
        source_dir="$REPO_ROOT/$source_dir"
    fi

    # Verify source exists
    if [ ! -d "$source_dir" ]; then
        log_error "Source directory not found: $source_dir"
        exit 2
    fi

    # Default output name to source basename
    if [ -z "$output_name" ]; then
        output_name="$(basename "$source_dir")"
    fi

    # Ensure .zip extension is not doubled
    output_name="${output_name%.zip}"

    # Default output directory to source parent
    if [ -z "$output_dir" ]; then
        output_dir="$(dirname "$source_dir")"
    fi

    local output_path="$output_dir/${output_name}.zip"

    log_info "Source: $source_dir"
    log_info "Output: $output_path"

    # Pre-flight contamination check on source
    log_info "Checking source for .DS_Store files..."
    local ds_count
    ds_count=$(find "$source_dir" -name ".DS_Store" 2>/dev/null | wc -l | tr -d ' ')
    if [ "$ds_count" -gt 0 ]; then
        log_warn "Found $ds_count .DS_Store files (will be excluded)"
    fi

    # Check for forbidden patterns in source paths
    if find "$source_dir" -type d \( -name "OUTGOING" -o -name "outgoing" \) 2>/dev/null | grep -q .; then
        log_error "Source contains forbidden OUTGOING/ or outgoing/ directories!"
        log_error "This violates Constitutional Rule #4. Please remediate before packing."
        exit 5
    fi

    # Remove existing output if present
    if [ -f "$output_path" ]; then
        log_warn "Removing existing archive: $output_path"
        rm "$output_path"
    fi

    # Create clean zip using COPYFILE_DISABLE to prevent resource fork creation
    # Combined with -X flag and explicit exclusions for defense in depth
    log_info "Creating clean archive..."

    local parent_dir
    parent_dir="$(dirname "$source_dir")"
    local base_name
    base_name="$(basename "$source_dir")"

    (
        cd "$parent_dir" || exit 3
        COPYFILE_DISABLE=1 zip -rX "$output_path" "$base_name" \
            -x "*.DS_Store" \
            -x "*/.DS_Store" \
            -x "__MACOSX/*" \
            -x "*/__MACOSX/*" \
            -x "*/._*" \
            -x "._*"
    )

    if [ $? -ne 0 ]; then
        log_error "Zip creation failed"
        exit 3
    fi

    # Post-creation verification
    log_info "Running post-creation verification..."
    if ! verify_archive "$output_path"; then
        log_error "Verification failed! Archive may be contaminated."
        log_warn "Consider using 'zip -d' to remove contamination manually"
        exit 4
    fi

    # Final stats
    local file_count
    file_count=$(unzip -l "$output_path" | tail -1 | awk '{print $2}')
    local archive_size
    archive_size=$(ls -lh "$output_path" | awk '{print $5}')

    log_info "Pack complete!"
    log_info "  Archive: $output_path"
    log_info "  Size: $archive_size"
    log_info "  Files: $file_count"

    echo ""
    echo "To verify later:"
    echo "  unzip -l \"$output_path\" | grep -E '__MACOSX|\\.DS_Store'"
}

# Parse arguments
VERIFY_ONLY=false
OUTPUT_DIR=""

while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            usage
            exit 0
            ;;
        -v|--verify-only)
            VERIFY_ONLY=true
            shift
            ;;
        -o|--output-dir)
            OUTPUT_DIR="$2"
            shift 2
            ;;
        -OUTGOING/*|-INBOX/*)
            # These are valid directory paths, not options
            break
            ;;
        -*)
            log_error "Unknown option: $1"
            usage
            exit 1
            ;;
        *)
            break
            ;;
    esac
done

# Main execution
if [ "$VERIFY_ONLY" = true ]; then
    if [ $# -lt 1 ]; then
        log_error "Verify mode requires an archive path"
        usage
        exit 1
    fi
    verify_archive "$1"
    exit $?
fi

if [ $# -lt 1 ]; then
    log_error "Source directory required"
    usage
    exit 1
fi

SOURCE_DIR="$1"
OUTPUT_NAME="${2:-}"

create_pack "$SOURCE_DIR" "$OUTPUT_NAME" "$OUTPUT_DIR"
