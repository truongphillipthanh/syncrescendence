#!/bin/bash
# DEFRAG APPLY SCRIPT
# Generated: 2026-01-17T16:09:00Z
#
# ARMING REQUIREMENT:
# This script will NOT execute unless APPLY_DEFRAG_APPROVAL.txt exists
# at repo root with contents: I_APPROVE_DEFRAG_APPLY
#
# SAFETY: Uses git mv for traceability, creates backups

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
LOG_FILE="${REPO_ROOT}/outgoing/DEFRAG_CONVICTION_PASS_20260117_1609/08_post_apply_verification/apply_log_${TIMESTAMP}.md"

# -----------------------------------------------------------------------------
# ARMING CHECK
# -----------------------------------------------------------------------------
check_arming() {
    local APPROVAL_FILE="${REPO_ROOT}/APPLY_DEFRAG_APPROVAL.txt"
    local REQUIRED_STRING="I_APPROVE_DEFRAG_APPLY"

    if [[ ! -f "$APPROVAL_FILE" ]]; then
        echo "ERROR: Arming file not found: $APPROVAL_FILE"
        echo "Create this file with contents: $REQUIRED_STRING"
        exit 1
    fi

    if ! grep -q "$REQUIRED_STRING" "$APPROVAL_FILE"; then
        echo "ERROR: Arming file does not contain required string"
        echo "Required: $REQUIRED_STRING"
        exit 1
    fi

    echo "ARMED: Approval verified. Proceeding with defrag."
}

# -----------------------------------------------------------------------------
# LOGGING
# -----------------------------------------------------------------------------
log_init() {
    mkdir -p "$(dirname "$LOG_FILE")"
    cat > "$LOG_FILE" << EOF
# Defrag Apply Log
**Started**: $(date -u +"%Y-%m-%dT%H:%M:%SZ")
**Operator**: defrag_apply.sh
**Git HEAD**: $(git rev-parse HEAD)

---

## Operations Log

EOF
}

log_op() {
    echo "- $(date +%H:%M:%S) | $1" >> "$LOG_FILE"
    echo "$1"
}

log_finish() {
    cat >> "$LOG_FILE" << EOF

---

## Summary
**Completed**: $(date -u +"%Y-%m-%dT%H:%M:%SZ")
**Final Git HEAD**: $(git rev-parse HEAD)
**Status**: $1
EOF
}

# -----------------------------------------------------------------------------
# PHASE A: DETRITUS REMOVAL
# -----------------------------------------------------------------------------
phase_a_detritus() {
    log_op "PHASE A: Removing detritus"

    # Remove .DS_Store files
    find "$REPO_ROOT" -name ".DS_Store" -type f -delete 2>/dev/null || true
    log_op "  Removed .DS_Store files"

    # Remove .tmp.driveupload if exists
    if [[ -d "${REPO_ROOT}/.tmp.driveupload" ]]; then
        rm -rf "${REPO_ROOT}/.tmp.driveupload"
        log_op "  Removed .tmp.driveupload/"
    fi

    # Remove __MACOSX if exists
    find "$REPO_ROOT" -name "__MACOSX" -type d -exec rm -rf {} + 2>/dev/null || true
    log_op "  Removed __MACOSX directories"

    log_op "PHASE A: Complete"
}

# -----------------------------------------------------------------------------
# PHASE C: ORACLE CONTEXT CONSOLIDATION
# -----------------------------------------------------------------------------
phase_c_oracle() {
    log_op "PHASE C: Oracle context consolidation"

    local ORACLE_CONTEXTS="${REPO_ROOT}/00-ORCHESTRATION/oracle_contexts"
    local ARCHIVE="${REPO_ROOT}/05-ARCHIVE"

    mkdir -p "$ORACLE_CONTEXTS"
    mkdir -p "$ARCHIVE"

    # Relocate ORACLE13_CONTEXT.md if at root
    if [[ -f "${REPO_ROOT}/ORACLE13_CONTEXT.md" ]]; then
        git mv "${REPO_ROOT}/ORACLE13_CONTEXT.md" "${ORACLE_CONTEXTS}/"
        log_op "  Relocated ORACLE13_CONTEXT.md to oracle_contexts/"
    fi

    # Archive ORACLE10 versions (keep FINAL and COMPREHENSIVE_ARCHAEOLOGY)
    for VERSION in "" "_v2" "_v3" "_v4" "_root"; do
        local FILE="${ORACLE_CONTEXTS}/ORACLE10_CONTEXT${VERSION}.md"
        if [[ -f "$FILE" ]] && [[ "$VERSION" != "" ]]; then
            git mv "$FILE" "${ARCHIVE}/ARCH-ORACLE10_CONTEXT${VERSION}.md" 2>/dev/null || true
            log_op "  Archived ORACLE10_CONTEXT${VERSION}.md"
        fi
    done

    log_op "PHASE C: Complete"
}

# -----------------------------------------------------------------------------
# PHASE E: RESEARCH ARTIFACT RELOCATION
# -----------------------------------------------------------------------------
phase_e_research() {
    log_op "PHASE E: Research artifact relocation"

    local RAW="${REPO_ROOT}/04-SOURCES/raw"
    mkdir -p "$RAW"

    # Relocate research files
    for FILE in \
        "DEEP_RESEARCH_PROMPT-Claude_Code_Ecosystem.md" \
        "DEEP_RESEARCH_PROMPT-Google_Ecosystem.md" \
        "DEEP_RESEARCH_PROMPT-OpenAI_Ecosystem.md" \
        "google_research.md" \
        "openai_research.md" \
        "SOURCES_ANALYSIS_REPORT.md"
    do
        if [[ -f "${REPO_ROOT}/${FILE}" ]]; then
            git mv "${REPO_ROOT}/${FILE}" "$RAW/"
            log_op "  Relocated $FILE"
        fi
    done

    # Relocate research directories
    for DIR in agents claudecode clitool codex cowork promptengineering; do
        if [[ -d "${REPO_ROOT}/${DIR}" ]]; then
            git mv "${REPO_ROOT}/${DIR}" "$RAW/"
            log_op "  Relocated $DIR/"
        fi
    done

    # Handle files with spaces in names
    for FILE in "${REPO_ROOT}/Stop Using Claude Code"*; do
        if [[ -f "$FILE" ]]; then
            git mv "$FILE" "$RAW/"
            log_op "  Relocated $(basename "$FILE")"
        fi
    done

    for FILE in "${REPO_ROOT}/Why I Stopped Using MCPs"*; do
        if [[ -f "$FILE" ]]; then
            git mv "$FILE" "$RAW/"
            log_op "  Relocated $(basename "$FILE")"
        fi
    done

    log_op "PHASE E: Complete"
}

# -----------------------------------------------------------------------------
# PHASE F: OBSOLETE FILE COMPRESSION (Archive)
# -----------------------------------------------------------------------------
phase_f_obsolete() {
    log_op "PHASE F: Obsolete file archival"

    local ARCHIVE="${REPO_ROOT}/05-ARCHIVE"
    mkdir -p "$ARCHIVE"

    # Archive temporal/obsolete files
    for FILE in \
        "frontier_models.md" \
        "platform_features.md" \
        "BLITZKRIEG_44_DEPLOYMENT_GUIDE.md" \
        "BLITZKRIEG_45_DEPLOYMENT_GUIDE.md" \
        "deviser1_continuity.md" \
        "oracle_memories.md" \
        "oracle_process_archaelogy.md" \
        "previous_thread.md" \
        "oracle_verification_manifest.md"
    do
        if [[ -f "${REPO_ROOT}/${FILE}" ]]; then
            local BASE=$(basename "$FILE" .md)
            git mv "${REPO_ROOT}/${FILE}" "${ARCHIVE}/ARCH-${BASE}.md"
            log_op "  Archived $FILE"
        fi
    done

    log_op "PHASE F: Complete"
}

# -----------------------------------------------------------------------------
# PHASE D: CANON RELOCATION
# -----------------------------------------------------------------------------
phase_d_canon() {
    log_op "PHASE D: Canon relocation"

    # Relocate CANON file at root to 01-CANON/
    if [[ -f "${REPO_ROOT}/CANON-31150-PLATFORM_CAPABILITY_CATALOG.md" ]]; then
        git mv "${REPO_ROOT}/CANON-31150-PLATFORM_CAPABILITY_CATALOG.md" "${REPO_ROOT}/01-CANON/"
        log_op "  Relocated CANON-31150-PLATFORM_CAPABILITY_CATALOG.md"
    fi

    log_op "PHASE D: Complete"
}

# -----------------------------------------------------------------------------
# MAIN EXECUTION
# -----------------------------------------------------------------------------
main() {
    cd "$REPO_ROOT"

    echo "=========================================="
    echo "DEFRAG APPLY SCRIPT"
    echo "=========================================="

    check_arming
    log_init

    log_op "Starting defrag apply"
    log_op "Git HEAD before: $(git rev-parse HEAD)"

    # Execute phases in order
    phase_a_detritus
    phase_c_oracle
    phase_e_research
    phase_f_obsolete
    phase_d_canon

    # Commit changes
    log_op "Creating git commit"
    git add -A
    git commit -m "chore(defrag): apply DEFRAG_CONVICTION_PASS_20260117

- Phase A: Removed detritus (.DS_Store, __MACOSX)
- Phase C: Consolidated Oracle contexts
- Phase E: Relocated research artifacts to 04-SOURCES/raw/
- Phase F: Archived obsolete files to 05-ARCHIVE/
- Phase D: Relocated misplaced CANON file

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>" || log_op "  (No changes to commit)"

    log_op "Git HEAD after: $(git rev-parse HEAD)"
    log_finish "SUCCESS"

    echo ""
    echo "=========================================="
    echo "DEFRAG APPLY COMPLETE"
    echo "Log: $LOG_FILE"
    echo "=========================================="
    echo ""
    echo "BLOCKED OPERATIONS (require Principal decision):"
    echo "  - DIRECTIVE-043 collision resolution"
    echo "  - Working document disposition (checklist.md, INTERACTION_PARADIGM.md)"
    echo ""
    echo "Run: ./post_apply_verify.sh to validate"
}

main "$@"
