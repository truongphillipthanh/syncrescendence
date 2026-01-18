#!/usr/bin/env bash
set -euo pipefail

APPROVAL_FILE="APPLY_DEFRAG_APPROVAL.txt"

if [[ ! -f "$APPROVAL_FILE" ]] || ! rg -q "I_APPROVE_DEFRAG_APPLY" "$APPROVAL_FILE"; then
  echo "APPLY not armed. This script is preview-only."
  exit 1
fi

echo "PREVIEW: git status --porcelain"
echo "PREVIEW: git rev-parse HEAD"
echo "PREVIEW: git checkout <pre-defrag-commit> -- ."
echo "PREVIEW: rerun post-apply verification script"
