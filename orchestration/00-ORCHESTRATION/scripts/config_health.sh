#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_SH="$SCRIPT_DIR/config.sh"
OUTPUT_FORMAT="md"
STRICT_MODE=0
HARDCODED_ROOT="/Users/system/""syncrescendence"

usage() {
  cat <<'USAGE'
Usage: config_health.sh [--json|--md] [--strict]

Options:
  --json    Emit JSON report
  --md      Emit Markdown report (default)
  --strict  Promote optional checks to failures
USAGE
}

for arg in "$@"; do
  case "$arg" in
    --json) OUTPUT_FORMAT="json" ;;
    --md) OUTPUT_FORMAT="md" ;;
    --strict) STRICT_MODE=1 ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown arg: $arg" >&2
      usage >&2
      exit 2
      ;;
  esac
done

CHECKS_TSV="$(mktemp -t config_health_checks.XXXXXX)"
cleanup() {
  rm -f "$CHECKS_TSV"
}
trap cleanup EXIT

sanitize() {
  printf '%s' "$1" | tr '\t\r\n' ' ' | sed 's/[[:space:]]\+/ /g; s/^ //; s/ $//'
}

add_check() {
  local check_id="$1"
  local status="$2"
  local required="$3"
  local message="$4"
  local detail="${5:-}"
  printf '%s\t%s\t%s\t%s\t%s\n' \
    "$(sanitize "$check_id")" \
    "$(sanitize "$status")" \
    "$(sanitize "$required")" \
    "$(sanitize "$message")" \
    "$(sanitize "$detail")" \
    >> "$CHECKS_TSV"
}

optional_status() {
  if [[ "$STRICT_MODE" == "1" ]]; then
    printf 'FAIL'
  else
    printf 'WARN'
  fi
}

if [[ ! -f "$CONFIG_SH" ]]; then
  echo "Missing config.sh: $CONFIG_SH" >&2
  exit 2
fi

if bash -n "$CONFIG_SH" >/dev/null 2>&1; then
  add_check "CONFIG_SH_SYNTAX" "PASS" "true" "config.sh syntax is valid"
else
  add_check "CONFIG_SH_SYNTAX" "FAIL" "true" "config.sh has syntax errors" "run: bash -n $CONFIG_SH"
fi

if source_err="$(bash -c "source \"$CONFIG_SH\" >/dev/null" 2>&1)"; then
  add_check "CONFIG_SH_SOURCEABLE" "PASS" "true" "config.sh sources cleanly"
else
  add_check "CONFIG_SH_SOURCEABLE" "FAIL" "true" "config.sh failed to source" "$source_err"
fi

# shellcheck source=/dev/null
source "$CONFIG_SH"

if preflight_err="$(bash -c "source \"$CONFIG_SH\"; sync_config_preflight config_health.sh >/dev/null" 2>&1)"; then
  add_check "CONFIG_PREFLIGHT" "PASS" "true" "sync_config_preflight passes"
else
  add_check "CONFIG_PREFLIGHT" "FAIL" "true" "sync_config_preflight failed" "$preflight_err"
fi

required_env_vars=("SYNCRESCENDENCE_ROOT" "HOME" "USER")
for var_name in "${required_env_vars[@]}"; do
  if [[ -n "${!var_name-}" ]]; then
    add_check "ENV_${var_name}" "PASS" "true" "required env var is set: $var_name"
  else
    add_check "ENV_${var_name}" "FAIL" "true" "required env var missing: $var_name" "export $var_name=<value>"
  fi
done

optional_env_vars=(
  "SSH_MINI"
  "SSH_AIR"
  "GRAPHITI_ENDPOINT"
)
for var_name in "${optional_env_vars[@]}"; do
  if [[ -n "${!var_name-}" ]]; then
    add_check "ENV_${var_name}" "PASS" "false" "optional env var is set: $var_name"
  else
    add_check "ENV_${var_name}" "$(optional_status)" "false" "optional env var missing: $var_name" "set in launchd/env for neural-bridge routing"
  fi
done

required_dirs=(
  "$ORCHESTRATION_DIR"
  "$CANON_DIR"
  "$ENGINE_DIR"
  "$SOURCES_DIR"
  "$PRAXIS_DIR"
  "$AGENTS_DIR"
)
for dir_path in "${required_dirs[@]}"; do
  if [[ -d "$dir_path" ]]; then
    add_check "DIR_$(basename "$dir_path")" "PASS" "true" "required directory exists" "$dir_path"
  else
    add_check "DIR_$(basename "$dir_path")" "FAIL" "true" "required directory missing" "$dir_path"
  fi
done

optional_dirs=(
  "$SOVEREIGN_DIR"
  "$COLLAB_DIR"
  "$INBOX_DIR"
  "$ARCHIVE_DIR"
  "$TEMPLATES_DIR"
)
for dir_path in "${optional_dirs[@]}"; do
  if [[ -d "$dir_path" ]]; then
    add_check "DIR_$(basename "$dir_path")" "PASS" "false" "optional directory exists" "$dir_path"
  else
    add_check "DIR_$(basename "$dir_path")" "$(optional_status)" "false" "optional directory missing" "$dir_path"
  fi
done

required_files=(
  "$STATE_DIR/DYN-DEFERRED_COMMITMENTS.md"
  "$STATE_DIR/ARCH-INTENTION_COMPASS.md"
)
for file_path in "${required_files[@]}"; do
  if [[ -f "$file_path" ]]; then
    add_check "FILE_$(basename "$file_path")" "PASS" "true" "required state file exists" "$file_path"
  else
    add_check "FILE_$(basename "$file_path")" "FAIL" "true" "required state file missing" "$file_path"
  fi
done

if python_out="$(python3 - "$SCRIPT_DIR" "$STRICT_MODE" <<'PY'
import sys

script_dir = sys.argv[1]
strict = sys.argv[2] == "1"
sys.path.insert(0, script_dir)

try:
    from config import ConfigError, validate_config
except Exception as exc:  # pragma: no cover - shell wrapper handles formatting
    print(f"IMPORT_ERROR\t{exc}")
    sys.exit(2)

try:
    violations = validate_config(strict=strict)
except ConfigError as exc:
    print("CRITICAL\t" + str(exc).replace("\n", " | "))
    sys.exit(2)

if violations:
    for item in violations:
        print("VIOLATION\t" + item)
    sys.exit(1)

print("PASS\tconfig.py validate_config passed")
PY
)"; then
  add_check "CONFIG_PY_VALIDATE" "PASS" "true" "config.py validate_config passed" "$python_out"
else
  python_rc=$?
  if [[ "$python_rc" == "1" ]]; then
    add_check "CONFIG_PY_VALIDATE" "$(optional_status)" "false" "config.py optional violations" "$python_out"
  else
    add_check "CONFIG_PY_VALIDATE" "FAIL" "true" "config.py critical validation failed" "$python_out"
  fi
fi

hardcoded_scan="$(python3 - "$REPO_ROOT" "$ORCHESTRATION_DIR/scripts" <<'PY'
from pathlib import Path
import re
import sys

repo_root = Path(sys.argv[1])
scripts_dir = Path(sys.argv[2])
needle = "/Users/system/" + "syncrescendence"
active_files: list[Path] = []

scan_roots = [scripts_dir]
agents_root = repo_root / "agents"
if agents_root.exists():
    scan_roots.append(agents_root)

include_ext = {".sh", ".py"}
active_re = re.compile(r"sync_config_preflight\b")
active_names = {
    "config.sh",
    "config.py",
    "config_health.sh",
    "config_migrate.sh",
    "scaffold_validate.sh",
}

for root in scan_roots:
    if not root.exists():
        continue
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in include_ext:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if path.name in active_names or active_re.search(text):
            active_files.append(path)

hits: list[str] = []
for path in active_files:
    try:
        lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    except OSError:
        continue
    for idx, line in enumerate(lines, start=1):
        if needle in line:
            rel = path.relative_to(repo_root)
            hits.append(f"{rel}:{idx}:{line.strip()}")

print(f"COUNTS\t{len(active_files)}\t{len(hits)}")
for hit in hits[:25]:
    print(f"HIT\t{hit}")
PY
)"

active_count="0"
hit_count="0"
hit_preview=""
while IFS= read -r line; do
  [[ -z "$line" ]] && continue
  if [[ "$line" == COUNTS$'\t'* ]]; then
    active_count="$(printf '%s' "$line" | cut -f2)"
    hit_count="$(printf '%s' "$line" | cut -f3)"
  elif [[ "$line" == HIT$'\t'* ]]; then
    if [[ -z "$hit_preview" ]]; then
      hit_preview="${line#HIT$'\t'}"
    else
      hit_preview+=" | ${line#HIT$'\t'}"
    fi
  fi
done <<< "$hardcoded_scan"

if [[ "$active_count" == "0" ]]; then
  add_check "HARDCODED_ROOT_SCAN" "$(optional_status)" "false" "no active scripts discovered for hardcoded-path scan" "expected scripts to source config.sh/import config"
elif [[ "$hit_count" == "0" ]]; then
  add_check "HARDCODED_ROOT_SCAN" "PASS" "true" "no hardcoded ${HARDCODED_ROOT} in active scripts" "active_scripts=$active_count"
else
  add_check "HARDCODED_ROOT_SCAN" "FAIL" "true" "hardcoded ${HARDCODED_ROOT} found in active scripts" "hits=$hit_count $hit_preview"
fi

TOTAL="$(wc -l < "$CHECKS_TSV" | tr -d '[:space:]')"
PASS_COUNT="$(awk -F '\t' '$2=="PASS"{c++} END{print c+0}' "$CHECKS_TSV")"
WARN_COUNT="$(awk -F '\t' '$2=="WARN"{c++} END{print c+0}' "$CHECKS_TSV")"
FAIL_COUNT="$(awk -F '\t' '$2=="FAIL"{c++} END{print c+0}' "$CHECKS_TSV")"

STATUS="PASS"
if [[ "$FAIL_COUNT" != "0" ]]; then
  STATUS="FAIL"
fi

if [[ "$OUTPUT_FORMAT" == "json" ]]; then
  python3 - <<'PY' "$CHECKS_TSV" "$STATUS" "$STRICT_MODE" "$REPO_ROOT"
import datetime
import json
import sys

checks_path, status, strict_mode, repo_root = sys.argv[1:5]
checks = []
with open(checks_path, "r", encoding="utf-8", errors="ignore") as handle:
    for raw in handle:
        raw = raw.rstrip("\n")
        if not raw:
            continue
        check_id, item_status, required, message, detail = raw.split("\t", 4)
        checks.append(
            {
                "id": check_id,
                "status": item_status,
                "required": required == "true",
                "message": message,
                "detail": detail,
            }
        )

summary = {
    "total": len(checks),
    "passed": sum(1 for c in checks if c["status"] == "PASS"),
    "warnings": sum(1 for c in checks if c["status"] == "WARN"),
    "failed": sum(1 for c in checks if c["status"] == "FAIL"),
}

report = {
    "status": status,
    "strict": strict_mode == "1",
    "timestamp": datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
    "repo_root": repo_root,
    "summary": summary,
    "checks": checks,
}
print(json.dumps(report, indent=2, sort_keys=False))
PY
else
  echo "# config_health"
  echo
  echo "- status: $STATUS"
  echo "- strict: $STRICT_MODE"
  echo "- repo_root: $REPO_ROOT"
  echo "- total: $TOTAL"
  echo "- passed: $PASS_COUNT"
  echo "- warnings: $WARN_COUNT"
  echo "- failed: $FAIL_COUNT"
  echo
  echo "## checks"
  echo
  while IFS=$'\t' read -r check_id item_status required message detail; do
    line="- [$item_status] $check_id (required=$required): $message"
    if [[ -n "$detail" ]]; then
      line+=" [$detail]"
    fi
    echo "$line"
  done < "$CHECKS_TSV"
fi

[[ "$STATUS" == "PASS" ]] && exit 0 || exit 1
