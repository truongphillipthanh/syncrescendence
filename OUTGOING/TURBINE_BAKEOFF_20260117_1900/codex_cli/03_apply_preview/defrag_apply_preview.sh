#!/usr/bin/env bash
set -euo pipefail

RUN_ID="20260117_1900"
APPROVAL_FILE="APPLY_DEFRAG_APPROVAL.txt"

if [[ ! -f "$APPROVAL_FILE" ]] || ! rg -q "I_APPROVE_DEFRAG_APPLY" "$APPROVAL_FILE"; then
  echo "APPLY not armed. This script is preview-only."
  exit 1
fi

# Decision gates
if [[ -z "${DIRECTIVE_043A_WINNER:-}" || -z "${DIRECTIVE_043B_WINNER:-}" ]]; then
  echo "Missing DIRECTIVE_043A_WINNER and/or DIRECTIVE_043B_WINNER env vars."
  echo "Set DIRECTIVE_043A_WINNER and DIRECTIVE_043B_WINNER before running."
  exit 1
fi

# Phase A: Detritus (preview)
echo "PREVIEW: find . -name '.DS_Store' -delete"
echo "PREVIEW: rm -rf .tmp.driveupload/"

# Phase B: Directives (preview)
echo "PREVIEW: move DIRECTIVE-042A_IIC_FOUNDATION.md -> 00-ORCHESTRATION/directives/DIRECTIVE-042A.md"
echo "PREVIEW: move DIRECTIVE-042B_MULTI_CLI.md -> 00-ORCHESTRATION/directives/DIRECTIVE-042B.md"
echo "PREVIEW: move DIRECTIVE-042C_OPERATIONAL_HYGIENE.md -> 00-ORCHESTRATION/directives/DIRECTIVE-042C.md"
echo "PREVIEW: move DIRECTIVE-042D_GEMINI_VALIDATION.md -> 00-ORCHESTRATION/directives/DIRECTIVE-042D.md"
echo "PREVIEW: move DIRECTIVE-044A.md -> 00-ORCHESTRATION/directives/DIRECTIVE-044A.md"
echo "PREVIEW: move DIRECTIVE-044B.md -> 00-ORCHESTRATION/directives/DIRECTIVE-044B.md"
echo "PREVIEW: move DIRECTIVE-045A.md -> 00-ORCHESTRATION/directives/DIRECTIVE-045A.md"
echo "PREVIEW: move DIRECTIVE-045B.md -> 00-ORCHESTRATION/directives/DIRECTIVE-045B.md"
echo "PREVIEW: move DIRECTIVE-046A.md -> 00-ORCHESTRATION/directives/DIRECTIVE-046A.md"
echo "PREVIEW: move DIRECTIVE-046B.md -> 00-ORCHESTRATION/directives/DIRECTIVE-046B.md"

if [[ "$DIRECTIVE_043A_WINNER" == "CONSTELLATION" ]]; then
  echo "PREVIEW: move DIRECTIVE-043A_CONSTELLATION_ARCHITECTURE.md -> 00-ORCHESTRATION/directives/DIRECTIVE-043A.md"
  echo "PREVIEW: move DIRECTIVE-043A_INFRASTRUCTURE_OPERATIONS.md -> 00-ORCHESTRATION/directives/DIRECTIVE-047A.md"
else
  echo "PREVIEW: move DIRECTIVE-043A_INFRASTRUCTURE_OPERATIONS.md -> 00-ORCHESTRATION/directives/DIRECTIVE-043A.md"
  echo "PREVIEW: move DIRECTIVE-043A_CONSTELLATION_ARCHITECTURE.md -> 00-ORCHESTRATION/directives/DIRECTIVE-047A.md"
fi

if [[ "$DIRECTIVE_043B_WINNER" == "CONTENT" ]]; then
  echo "PREVIEW: move DIRECTIVE-043B_CONTENT_STRATEGY.md -> 00-ORCHESTRATION/directives/DIRECTIVE-043B.md"
  echo "PREVIEW: move DIRECTIVE-043B_OPERATIONAL_HYGIENE.md -> 00-ORCHESTRATION/directives/DIRECTIVE-047B.md"
else
  echo "PREVIEW: move DIRECTIVE-043B_OPERATIONAL_HYGIENE.md -> 00-ORCHESTRATION/directives/DIRECTIVE-043B.md"
  echo "PREVIEW: move DIRECTIVE-043B_CONTENT_STRATEGY.md -> 00-ORCHESTRATION/directives/DIRECTIVE-047B.md"
fi

# Phase C: Oracle contexts (preview)
echo "PREVIEW: move ORACLE13_CONTEXT.md -> 00-ORCHESTRATION/oracle_contexts/ORACLE13_CONTEXT.md"
echo "PREVIEW: move ORACLE12_PEDIGREE.md -> 00-ORCHESTRATION/oracle_contexts/ORACLE12_PEDIGREE.md"
echo "PREVIEW: move ORACLE12_PEDIGREE-045.md -> 00-ORCHESTRATION/oracle_contexts/ORACLE12_PEDIGREE-045.md"
echo "PREVIEW: move ORACLE12_SESSION_DELIVERABLES.md -> 00-ORCHESTRATION/oracle_contexts/ORACLE12_SESSION_DELIVERABLES.md"

# Phase D: Canon (preview)
echo "PREVIEW: move CANON-31150-PLATFORM_CATALOG-lunar-ACUMEN-planetary-INFORMATION.md -> 01-CANON/CANON-31150-PLATFORM_CATALOG.md"

# Phase E: Research artifacts (preview)
echo "PREVIEW: move research prompts and directories to 04-SOURCES/raw/ (see refined plan for full list)"

# Phase F: Symbolic compression + archive (preview)
echo "PREVIEW: create ARCH-* compressions in 05-ARCHIVE/ before removing originals"

# Phase G: Directory consolidation (preview)
echo "PREVIEW: audit system_prompts/ vs 02-OPERATIONAL/prompts/ then merge unique files"

# Phase H: Working documents (preview)
echo "PREVIEW: apply Principal decisions for checklist.md, INTERACTION_PARADIGM.md, rapport_contract.md"

echo "PREVIEW complete for RUN_ID=$RUN_ID"
