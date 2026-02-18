#!/usr/bin/env bash
#
# ingest_chatgpt_container.sh
#
# Shell wrapper for ChatGPT container ingestion utility.
# Reads from stdin and files content into -INBOX/-OUTGOING.
#
# Usage:
#   cat pasted_response.txt | ./ingest_chatgpt_container.sh --date YYYYMMDD --slug <slug>
#   pbpaste | ./ingest_chatgpt_container.sh --date 20260118 --slug phoenix
#   ./ingest_chatgpt_container.sh --date 20260118 --slug phoenix --input response.txt
#
# Options:
#   --date YYYYMMDD   Date for filing (required)
#   --slug <slug>     Slug identifier (required)
#   --input, -i       Read from file instead of stdin
#   --force, -f       Overwrite existing files without suffix
#   --dry-run, -n     Preview changes without writing
#   --help, -h        Show this help message
#

set -euo pipefail

# Get repo root
REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || dirname "$(dirname "$(dirname "$(realpath "$0")")")")"
SCRIPT_DIR="${REPO_ROOT}/00-ORCHESTRATION/scripts"
PYTHON_SCRIPT="${SCRIPT_DIR}/ingest_chatgpt_container.py"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

log() { echo -e "${GREEN}[INFO]${NC} $*"; }
warn() { echo -e "${YELLOW}[WARN]${NC} $*"; }
error() { echo -e "${RED}[ERROR]${NC} $*" >&2; }

usage() {
    cat <<EOF
Usage: $(basename "$0") --date YYYYMMDD --slug <slug> [OPTIONS]

Ingest ChatGPT container response and file into repo structure.

Required:
  --date YYYYMMDD   Date for filing (e.g., 20260118)
  --slug <slug>     Slug identifier for this ingestion

Options:
  --input, -i FILE  Read from file instead of stdin
  --force, -f       Overwrite existing files without adding suffix
  --dry-run, -n     Show what would be done without making changes
  --help, -h        Show this help message

Examples:
  cat response.txt | $(basename "$0") --date 20260118 --slug phoenix
  pbpaste | $(basename "$0") --date 20260118 --slug phoenix
  $(basename "$0") --date 20260118 --slug phoenix --input response.txt --dry-run

Output Structure:
  -INBOX/<DATE>-audizer/<slug>.txt                              (Audizable)
  -OUTGOING/<DATE>-blitzkrieg-<slug>/01_context/context.md      (Context)
  -OUTGOING/<DATE>-blitzkrieg-<slug>/02_pedigree/pedigree.md    (Pedigree)
  -OUTGOING/<DATE>-blitzkrieg-<slug>/04_directives/*.md         (Directives)
  -OUTGOING/<DATE>-blitzkrieg-<slug>/06_return_to_webapp/merged_return_packet.md (Readable)
EOF
}

# Check Python script exists
if [[ ! -f "${PYTHON_SCRIPT}" ]]; then
    error "Python script not found: ${PYTHON_SCRIPT}"
    exit 1
fi

# Parse arguments
DATE=""
SLUG=""
INPUT=""
FORCE=""
DRY_RUN=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --date)
            DATE="$2"
            shift 2
            ;;
        --slug)
            SLUG="$2"
            shift 2
            ;;
        --input|-i)
            INPUT="$2"
            shift 2
            ;;
        --force|-f)
            FORCE="--force"
            shift
            ;;
        --dry-run|-n)
            DRY_RUN="--dry-run"
            shift
            ;;
        --help|-h)
            usage
            exit 0
            ;;
        *)
            error "Unknown option: $1"
            usage
            exit 1
            ;;
    esac
done

# Validate required arguments
if [[ -z "${DATE}" ]]; then
    error "Missing required argument: --date"
    usage
    exit 1
fi

if [[ -z "${SLUG}" ]]; then
    error "Missing required argument: --slug"
    usage
    exit 1
fi

# Build command
CMD=(python3 "${PYTHON_SCRIPT}" --date "${DATE}" --slug "${SLUG}")

if [[ -n "${INPUT}" ]]; then
    CMD+=(--input "${INPUT}")
fi

if [[ -n "${FORCE}" ]]; then
    CMD+=(--force)
fi

if [[ -n "${DRY_RUN}" ]]; then
    CMD+=(--dry-run)
fi

# Execute
log "Ingesting ChatGPT container: date=${DATE}, slug=${SLUG}"
cd "${REPO_ROOT}"
"${CMD[@]}"
