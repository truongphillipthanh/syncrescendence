#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE}")/config.sh"

# repo_integrity_gate.sh - Layer-0 integrity checks for autonomous orchestration
# Fails closed when repository metadata or canonical structure is unsafe.

set -u

REPO_DIR=""
CONTEXT="unspecified"
EMIT_INCIDENT=1
STRICT_FSCK="${SYNCRESCENDENCE_INTEGRITY_STRICT:-0}"
QUIET=0

usage() {
    cat <<'EOF'
Usage: repo_integrity_gate.sh [options]

Options:
  --repo <path>        Repository path (default: git toplevel or cwd)
  --context <name>     Caller context for incident traceability
  --no-incident        Do not emit -SOVEREIGN incident file
  --strict             Run git fsck --full check
  --quiet              Suppress stdout (stderr still used for failures)
  -h, --help           Show this help
EOF
}

log() {
    [ "$QUIET" -eq 1 ] && return 0
    printf '%s\n' "$*"
}

err() {
    printf '%s\n' "$*" >&2
}

while [ "$#" -gt 0 ]; do
    case "$1" in
        --repo)
            REPO_DIR="${2:-}"
            shift 2
            ;;
        --context)
            CONTEXT="${2:-unspecified}"
            shift 2
            ;;
        --no-incident)
            EMIT_INCIDENT=0
            shift
            ;;
        --strict)
            STRICT_FSCK=1
            shift
            ;;
        --quiet)
            QUIET=1
            shift
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            err "Unknown option: $1"
            usage
            exit 2
            ;;
    esac
done

if [ -z "$REPO_DIR" ]; then
    REPO_DIR="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
fi

if [ ! -d "$REPO_DIR/.git" ]; then
    err "INTEGRITY_FAIL: not a git repository: $REPO_DIR"
    exit 1
fi

timestamp_iso="$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
timestamp_slug="$(date '+%Y%m%d-%H%M%S')"

failures_file="$(mktemp)"
trap 'rm -f "$failures_file"' EXIT

record_failure() {
    printf '%s\n' "$*" >> "$failures_file"
}

# Check 1: index lock must not be present for autonomous writes.
if [ -f "$REPO_DIR/.git/index.lock" ]; then
    record_failure "index.lock present at .git/index.lock"
fi

# Check 2: ref namespace must be clean from Finder artifacts and spaced names.
invalid_refs="$(find "$REPO_DIR/.git/refs" "$REPO_DIR/.git/logs/refs" \
    \( -name '.DS_Store' -o -name '* *' \) -print 2>/dev/null || true)"
if [ -n "$invalid_refs" ]; then
    while IFS= read -r p; do
        [ -n "$p" ] && record_failure "invalid ref artifact: ${p#$REPO_DIR/}"
    done <<< "$invalid_refs"
fi

# Check 3: required canonical top-level entries must be tracked by HEAD.
head_tree="$(git -C "$REPO_DIR" ls-tree --name-only HEAD 2>/dev/null || true)"
for required in -INBOX -OUTGOING orchestration; do
    if ! printf '%s\n' "$head_tree" | grep -qx -- "$required"; then
        record_failure "HEAD missing required tracked root: $required"
    fi
done

# Check 4 (optional): full object/ref fsck.
if [ "$STRICT_FSCK" = "1" ]; then
    fsck_out="$(git -C "$REPO_DIR" fsck --full --no-progress 2>&1 || true)"
    while IFS= read -r line; do
        case "$line" in
            error:*)
                record_failure "fsck ${line#error: }"
                ;;
        esac
    done <<< "$fsck_out"
fi

if [ -s "$failures_file" ]; then
    err "INTEGRITY_FAIL: ${CONTEXT}"
    while IFS= read -r line; do
        err "  - $line"
    done < "$failures_file"

    if [ "$EMIT_INCIDENT" -eq 1 ]; then
        sovereign_dir="$REPO_DIR/-SOVEREIGN"
        mkdir -p "$sovereign_dir" 2>/dev/null || true

        # DEDUP: Skip if same context already has an incident from the last 6 hours
        latest_existing="$(ls -1t "$sovereign_dir"/INCIDENT-INTEGRITY-"${CONTEXT}"-*.md 2>/dev/null | head -1)"
        if [ -n "$latest_existing" ]; then
            # Check if latest incident is less than 6 hours old (21600 seconds)
            if [ "$(uname)" = "Darwin" ]; then
                file_epoch="$(stat -f '%m' "$latest_existing")"
            else
                file_epoch="$(stat -c '%Y' "$latest_existing")"
            fi
            now_epoch="$(date +%s)"
            age=$(( now_epoch - file_epoch ))
            if [ "$age" -lt 21600 ]; then
                err "  - dedup: incident for ${CONTEXT} already exists (${age}s old), skipping"
                exit 1
            fi
        fi

        incident_file="$sovereign_dir/INCIDENT-INTEGRITY-${CONTEXT}-${timestamp_slug}.md"
        {
            echo "# INCIDENT-INTEGRITY-${CONTEXT}-${timestamp_slug}"
            echo
            echo "**Kind**: INCIDENT"
            echo "**Domain**: REPOSITORY_INTEGRITY"
            echo "**Context**: ${CONTEXT}"
            echo "**Detected-At**: ${timestamp_iso}"
            echo "**Policy**: FAIL_CLOSED"
            echo
            echo "## Findings"
            while IFS= read -r line; do
                echo "- $line"
            done < "$failures_file"
            echo
            echo "## Required Action"
            echo "Autonomous dispatch/retry must remain frozen until integrity is restored."
            echo "Run manual repair on refs/index and validate with strict integrity gate."
        } > "$incident_file"
        err "  - incident: ${incident_file#$REPO_DIR/}"
    fi

    exit 1
fi

log "INTEGRITY_OK: ${CONTEXT}"
exit 0
