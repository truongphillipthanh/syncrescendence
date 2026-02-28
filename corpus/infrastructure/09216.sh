#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE}")/config.sh"

# orchestration/00-ORCHESTRATION/scripts/scaffold_rename.sh
# DC-123: Safe rename utility enforcing naming conventions.
# Usage: scaffold_rename.sh [--dry-run] <old_path> <new_path>
set -euo pipefail

# ---- helpers ---------------------------------------------------------------
die()  { echo "ERROR: $*" >&2; exit 2; }
info() { echo "INFO: $*" >&2; }
have() { command -v "$1" >/dev/null 2>&1; }

repo_root() { git rev-parse --show-toplevel 2>/dev/null || die "Not in a git repo."; }

# ---- args ------------------------------------------------------------------
DRY_RUN=0
POSITIONAL=()
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=1 ;;
    --help|-h)
      echo "Usage: scaffold_rename.sh [--dry-run] <old_path> <new_path>"
      echo ""
      echo "Safely renames a file/directory using git mv, validates naming"
      echo "conventions, and updates all markdown cross-references."
      echo ""
      echo "Options:"
      echo "  --dry-run   Show what would happen without making changes"
      echo "  --help      Show this help"
      exit 0
      ;;
    *) POSITIONAL+=("$arg") ;;
  esac
done

[[ ${#POSITIONAL[@]} -eq 2 ]] || die "Exactly two positional args required: <old_path> <new_path>"
OLD_PATH="${POSITIONAL[0]}"
NEW_PATH="${POSITIONAL[1]}"

ROOT="$(repo_root)"
cd "$ROOT"

# Normalize to repo-relative paths
OLD_REL="${OLD_PATH#$ROOT/}"
NEW_REL="${NEW_PATH#$ROOT/}"
# Strip leading ./ if present
OLD_REL="${OLD_REL#./}"
NEW_REL="${NEW_REL#./}"

# ---- validate old path exists ----------------------------------------------
[[ -e "$OLD_REL" ]] || die "Source path does not exist: $OLD_REL"

# ---- validate new path does not exist --------------------------------------
[[ ! -e "$NEW_REL" ]] || die "Target path already exists: $NEW_REL"

# ---- naming convention validation ------------------------------------------
# Sanctioned prefixes from REF-NAMING_CONVENTIONS.md
SANCTIONED_PREFIXES=(
  "ARCH-" "DYN-" "REF-" "FUNC-" "PROMPT-" "CANON-" "SOURCE-" "EXTRACT-"
  "AVATAR-" "IIC-" "TEMPLATE-" "MODEL-" "RESPONSE-" "QUEUE-" "SOVEREIGN-"
  "MECH-" "PRAC-" "SYNTHESIS-" "EXEMPLA-" "MOC-" "SCAFF-" "HANDOFF-"
  "DECISION-" "ALERT-" "RECEIPT-"
)

# Prefix-to-directory binding (Section 3 of REF-NAMING_CONVENTIONS.md)
declare -A PREFIX_DIRS
PREFIX_DIRS["ARCH-"]="${ORCHESTRATION_DIR#$REPO_ROOT/}/ orchestration/state/"
PREFIX_DIRS["DYN-"]="${ENGINE_DIR#$REPO_ROOT/}/ orchestration/state/ orchestration/00-ORCHESTRATION/ sources/04-SOURCES/"
PREFIX_DIRS["REF-"]="${ENGINE_DIR#$REPO_ROOT/}/ praxis/05-SIGMA/ sources/04-SOURCES/"
PREFIX_DIRS["FUNC-"]="${ENGINE_DIR#$REPO_ROOT/}/"
PREFIX_DIRS["PROMPT-"]="${ENGINE_DIR#$REPO_ROOT/}/ -SOVEREIGN/"
PREFIX_DIRS["CANON-"]="canon/01-CANON/"
PREFIX_DIRS["SOURCE-"]="sources/04-SOURCES/"
PREFIX_DIRS["EXTRACT-"]="sources/04-SOURCES/"
PREFIX_DIRS["AVATAR-"]="${ENGINE_DIR#$REPO_ROOT/}/"
PREFIX_DIRS["IIC-"]="${ENGINE_DIR#$REPO_ROOT/}/"
PREFIX_DIRS["TEMPLATE-"]="${ENGINE_DIR#$REPO_ROOT/}/ orchestration/00-ORCHESTRATION/templates/"
PREFIX_DIRS["MODEL-"]="${ENGINE_DIR#$REPO_ROOT/}/"
PREFIX_DIRS["RESPONSE-"]="-INBOX/"
PREFIX_DIRS["QUEUE-"]="-SOVEREIGN/"
PREFIX_DIRS["SOVEREIGN-"]="-SOVEREIGN/"
PREFIX_DIRS["MECH-"]="${PRAXIS_DIR#$REPO_ROOT/}/mechanics/"
PREFIX_DIRS["PRAC-"]="${PRAXIS_DIR#$REPO_ROOT/}/practice/"
PREFIX_DIRS["SYNTHESIS-"]="${PRAXIS_DIR#$REPO_ROOT/}/syntheses/"
PREFIX_DIRS["EXEMPLA-"]="${PRAXIS_DIR#$REPO_ROOT/}/"
PREFIX_DIRS["MOC-"]=""  # any directory
PREFIX_DIRS["SCAFF-"]="${ORCHESTRATION_DIR#$REPO_ROOT/}/scripts/"
PREFIX_DIRS["HANDOFF-"]="agents/"
PREFIX_DIRS["DECISION-"]="${ORCHESTRATION_DIR#$REPO_ROOT/}/archive/"
PREFIX_DIRS["ALERT-"]="-SOVEREIGN/"
PREFIX_DIRS["RECEIPT-"]="agents/"

NEW_BASENAME="$(basename "$NEW_REL")"
NEW_DIRNAME="$(dirname "$NEW_REL")/"

WARNINGS=()
ERRORS=()

# Check if new name is a markdown file with a prefix
if [[ "$NEW_BASENAME" == *.md ]]; then
  FOUND_PREFIX=""
  for prefix in "${SANCTIONED_PREFIXES[@]}"; do
    if [[ "$NEW_BASENAME" == ${prefix}* ]]; then
      FOUND_PREFIX="$prefix"
      break
    fi
  done

  # If the file starts with an uppercase letter but has no sanctioned prefix, warn
  if [[ -z "$FOUND_PREFIX" && "$NEW_BASENAME" =~ ^[A-Z] ]]; then
    # Check if it looks like it's trying to use a prefix
    MAYBE_PREFIX="${NEW_BASENAME%%-*}-"
    if [[ "$MAYBE_PREFIX" != "$NEW_BASENAME-" ]]; then
      WARNINGS+=("Unsanctioned prefix detected: '$MAYBE_PREFIX'. See REF-NAMING_CONVENTIONS.md Section 7.3.")
    fi
  fi

  # Validate prefix-directory binding
  if [[ -n "$FOUND_PREFIX" ]]; then
    ALLOWED_DIRS="${PREFIX_DIRS[$FOUND_PREFIX]:-}"
    if [[ -n "$ALLOWED_DIRS" ]]; then
      DIR_OK=0
      for allowed in $ALLOWED_DIRS; do
        if [[ "$NEW_DIRNAME" == ${allowed}* ]]; then
          DIR_OK=1
          break
        fi
      done
      if [[ $DIR_OK -eq 0 ]]; then
        ERRORS+=("Prefix '$FOUND_PREFIX' is not sanctioned in directory '$NEW_DIRNAME'. Allowed: $ALLOWED_DIRS")
      fi
    fi

    # Validate UPPER_SNAKE_CASE after prefix (Section 5)
    NAME_AFTER_PREFIX="${NEW_BASENAME#${FOUND_PREFIX}}"
    NAME_AFTER_PREFIX="${NAME_AFTER_PREFIX%.md}"
    if [[ -n "$NAME_AFTER_PREFIX" ]] && ! echo "$NAME_AFTER_PREFIX" | grep -qE '^[A-Z0-9][A-Z0-9_-]*$'; then
      WARNINGS+=("Prefixed filename should be UPPER_SNAKE_CASE after prefix. Got: '$NAME_AFTER_PREFIX'")
    fi
  fi

  # Scripts should be lowercase_snake_case
elif [[ "$NEW_BASENAME" == *.sh || "$NEW_BASENAME" == *.py ]]; then
  if ! echo "$NEW_BASENAME" | grep -qE '^[a-z0-9][a-z0-9_.-]*$'; then
    WARNINGS+=("Scripts should use lowercase_snake_case. Got: '$NEW_BASENAME'")
  fi
fi

# ---- report errors ---------------------------------------------------------
if [[ ${#ERRORS[@]} -gt 0 ]]; then
  for err in "${ERRORS[@]}"; do
    echo "NAMING ERROR: $err" >&2
  done
  die "Naming convention violations prevent rename. Fix errors or override with caution."
fi

for warn in "${WARNINGS[@]}"; do
  echo "WARNING: $warn" >&2
done

# ---- find cross-references ------------------------------------------------
# Search all markdown files for references to old path
OLD_BASENAME="$(basename "$OLD_REL")"

XREF_FILES=()
if have rg; then
  while IFS= read -r f; do
    [[ -n "$f" ]] && XREF_FILES+=("$f")
  done < <(rg -l --type md -F "$OLD_BASENAME" . 2>/dev/null || true)
  # Also search for path-style references
  while IFS= read -r f; do
    [[ -n "$f" ]] && XREF_FILES+=("$f")
  done < <(rg -l --type md -F "$OLD_REL" . 2>/dev/null || true)
else
  while IFS= read -r f; do
    [[ -n "$f" ]] && XREF_FILES+=("$f")
  done < <(grep -rl --include='*.md' -F "$OLD_BASENAME" . 2>/dev/null || true)
  while IFS= read -r f; do
    [[ -n "$f" ]] && XREF_FILES+=("$f")
  done < <(grep -rl --include='*.md' -F "$OLD_REL" . 2>/dev/null || true)
fi

# Deduplicate
XREF_UNIQUE=()
declare -A SEEN_XREF
for f in "${XREF_FILES[@]}"; do
  f="${f#./}"
  if [[ -z "${SEEN_XREF[$f]+x}" ]]; then
    SEEN_XREF["$f"]=1
    XREF_UNIQUE+=("$f")
  fi
done

# ---- dry-run report -------------------------------------------------------
if [[ $DRY_RUN -eq 1 ]]; then
  info "=== DRY RUN ==="
  info "git mv: $OLD_REL -> $NEW_REL"
  if [[ ${#XREF_UNIQUE[@]} -gt 0 ]]; then
    info "Cross-references to update (${#XREF_UNIQUE[@]} files):"
    for f in "${XREF_UNIQUE[@]}"; do
      info "  - $f"
    done
  else
    info "No cross-references found."
  fi
  if [[ ${#WARNINGS[@]} -gt 0 ]]; then
    info "Warnings: ${#WARNINGS[@]}"
  fi

  # JSON report to stdout
  if have python3; then
    python3 -c "
import json, sys
print(json.dumps({
    'dry_run': True,
    'old_path': sys.argv[1],
    'new_path': sys.argv[2],
    'git_mv': {'from': sys.argv[1], 'to': sys.argv[2]},
    'cross_references': sys.argv[3].split('|') if sys.argv[3] else [],
    'warnings': sys.argv[4].split('|') if sys.argv[4] else [],
    'errors': []
}, indent=2))
" "$OLD_REL" "$NEW_REL" \
  "$(IFS='|'; echo "${XREF_UNIQUE[*]}")" \
  "$(IFS='|'; echo "${WARNINGS[*]}")"
  else
    echo "{\"dry_run\":true,\"old_path\":\"$OLD_REL\",\"new_path\":\"$NEW_REL\"}"
  fi
  exit 0
fi

# ---- execute rename --------------------------------------------------------

# Check if file is git-tracked
IS_TRACKED=0
git ls-files --error-unmatch "$OLD_REL" >/dev/null 2>&1 && IS_TRACKED=1

if [[ $IS_TRACKED -eq 1 ]]; then
  info "Performing git mv: $OLD_REL -> $NEW_REL"
  # Ensure target directory exists
  mkdir -p "$(dirname "$NEW_REL")"
  git mv "$OLD_REL" "$NEW_REL"
else
  info "File not tracked by git; performing plain mv: $OLD_REL -> $NEW_REL"
  mkdir -p "$(dirname "$NEW_REL")"
  mv "$OLD_REL" "$NEW_REL"
fi

# ---- update cross-references ----------------------------------------------
UPDATED_FILES=()
for f in "${XREF_UNIQUE[@]}"; do
  # Skip the file we just moved (use new path)
  [[ "$f" == "$OLD_REL" ]] && f="$NEW_REL"
  [[ -f "$f" ]] || continue

  # macOS sed uses -i '' ; Linux sed uses -i
  if [[ "$(uname)" == "Darwin" ]]; then
    # Replace full path references
    sed -i '' "s|${OLD_REL}|${NEW_REL}|g" "$f"
    # Replace basename references (in links/wikilinks only, to avoid false positives)
    if [[ "$OLD_BASENAME" != "$NEW_BASENAME" ]]; then
      sed -i '' "s|${OLD_BASENAME}|${NEW_BASENAME}|g" "$f"
    fi
  else
    sed -i "s|${OLD_REL}|${NEW_REL}|g" "$f"
    if [[ "$OLD_BASENAME" != "$NEW_BASENAME" ]]; then
      sed -i "s|${OLD_BASENAME}|${NEW_BASENAME}|g" "$f"
    fi
  fi
  UPDATED_FILES+=("$f")
done

# ---- JSON report -----------------------------------------------------------
REPORT_FILE="reports/scaffold_rename_$(date +%Y%m%d-%H%M%S).json"
mkdir -p reports

if have python3; then
  python3 -c "
import json, sys, datetime
updated = sys.argv[5].split('|') if sys.argv[5] else []
warnings = sys.argv[6].split('|') if sys.argv[6] else []
report = {
    'dry_run': False,
    'timestamp': datetime.datetime.utcnow().replace(microsecond=0).isoformat() + 'Z',
    'old_path': sys.argv[1],
    'new_path': sys.argv[2],
    'git_tracked': sys.argv[3] == '1',
    'git_mv': sys.argv[3] == '1',
    'cross_references_updated': updated,
    'cross_references_count': len(updated),
    'warnings': warnings,
    'errors': [],
    'report_file': sys.argv[4]
}
with open(sys.argv[4], 'w') as f:
    json.dump(report, f, indent=2)
print(json.dumps(report, indent=2))
" "$OLD_REL" "$NEW_REL" "$IS_TRACKED" "$REPORT_FILE" \
  "$(IFS='|'; echo "${UPDATED_FILES[*]}")" \
  "$(IFS='|'; echo "${WARNINGS[*]}")"
else
  echo "{\"old_path\":\"$OLD_REL\",\"new_path\":\"$NEW_REL\",\"cross_references_count\":${#UPDATED_FILES[@]}}" | tee "$REPORT_FILE"
fi

info "Rename complete. Report: $REPORT_FILE"
