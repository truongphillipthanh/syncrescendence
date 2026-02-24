#!/usr/bin/env bash
# orchestration/00-ORCHESTRATION/scripts/scaffold_validate.sh
set -euo pipefail

# ---- config ---------------------------------------------------------------
SIGMA_DIR_DEFAULT="praxis"                         # sigma-equivalent dir name
SIGMA_DIR="${SIGMA_DIR:-$SIGMA_DIR_DEFAULT}"      # override via env SIGMA_DIR

# Top-level directories required
REQUIRED_TOP_DIRS=( "orchestration" "canon" "engine" "sources" "agents" )

# Allowed top-level entries (dirs or files) besides REQUIRED_TOP_DIRS + SIGMA_DIR
ALLOWED_TOP_LEVEL=(
  ".git" ".github" ".claude" ".vscode" ".cursor" ".gemini" ".windsurf"
  ".obsidian" ".agents" ".agent" ".constellation" ".DS_Store"
  "scripts" "templates" "reports" "docs"
  "Makefile" "README.md" "AGENTS.md" "CLAUDE.md" "LICENSE"
  ".gitignore" ".gitattributes"
  "BOOT.md" "CLAUDE-EXT.md" "GEMINI.md" "GEMINI-EXT.md" "GROK-EXT.md"
  "OPENCLAW-EXT.md" "INTER-AGENT.md" "WORK-LOOP.md"
  "CONTINUOUS-IMPROVEMENT.md" "ACTIVE-TASKS.md"
  "-INBOX" "-OUTBOX" "-SOVEREIGN"
  "collab" "memory" "openclaw" "sovereign"
  "com.syncrescendence.ingest.plist" "com.syncrescendence.weekly.plist"
  "task_plan.md" "findings.md" "progress.md"
  "Makefile 2"
)

# Agent office required structure
AGENT_REQUIRED_DIRS=(
  "inbox/pending" "inbox/active" "inbox/done" "inbox/failed" "inbox/blocked"
  "outbox" "scratchpad" "memory"
)
AGENT_REQUIRED_FILES=( "INIT.md" )

# Flat principle applies here (no subdirectories allowed beneath these)
FLAT_DIR_GLOBS_DEFAULT=(
  "agents/*/inbox/pending"
  "agents/*/inbox/active"
  "agents/*/inbox/done"
  "agents/*/inbox/failed"
  "agents/*/inbox/blocked"
)
# Override with newline-separated globs in env var SCAFFOLD_FLAT_DIRS
# Example: export SCAFFOLD_FLAT_DIRS=$'agents/*/inbox/pending\nagents/*/outbox'
SCAFFOLD_FLAT_DIRS="${SCAFFOLD_FLAT_DIRS:-}"

# DYN cadence allowances (seconds). Buffer included.
CADENCE_DAILY=$((2*24*3600))
CADENCE_WEEKLY=$((9*24*3600))
CADENCE_MONTHLY=$((40*24*3600))
CADENCE_QUARTERLY=$((110*24*3600))
CADENCE_YEARLY=$((400*24*3600))

OUTPUT_FORMAT="${OUTPUT_FORMAT:-json}"  # json | md
# --------------------------------------------------------------------------

die() { echo "ERROR: $*" >&2; exit 2; }

have() { command -v "$1" >/dev/null 2>&1; }

repo_root() {
  git rev-parse --show-toplevel 2>/dev/null || die "Not in a git repo."
}

mtime_epoch() {
  # macOS: stat -f %m ; Linux: stat -c %Y
  local p="$1"
  if stat -f %m "$p" >/dev/null 2>&1; then stat -f %m "$p"; else stat -c %Y "$p"; fi
}

now_epoch() { date +%s; }

# violations TSV: code \t path \t fixable(0/1) \t message
VIO_TMP="$(mktemp -t scaffold_vio.XXXXXX)"
cleanup() { rm -f "$VIO_TMP"; }
trap cleanup EXIT

add_vio() {
  local code="$1" path="$2" fixable="$3" msg="$4"
  printf "%s\t%s\t%s\t%s\n" "$code" "$path" "$fixable" "$msg" >> "$VIO_TMP"
}

# ---- argument parsing ------------------------------------------------------
for arg in "${@:-}"; do
  case "$arg" in
    --json) OUTPUT_FORMAT="json" ;;
    --md)   OUTPUT_FORMAT="md" ;;
    *) die "Unknown arg: $arg" ;;
  esac
done

ROOT="$(repo_root)"
cd "$ROOT"

# ---- checks ----------------------------------------------------------------

# Required top-level dirs
for d in "${REQUIRED_TOP_DIRS[@]}"; do
  [[ -d "$d" ]] || add_vio "MISSING_DIR" "$d" 1 "Required top-level directory missing."
done

# Sigma-equivalent dir
if [[ -d "$SIGMA_DIR" ]]; then
  :
else
  # tolerate sigma-* if SIGMA_DIR doesn't exist
  if compgen -G "sigma*" >/dev/null 2>&1; then
    :
  else
    add_vio "MISSING_DIR" "$SIGMA_DIR" 1 "Sigma-equivalent directory missing (set SIGMA_DIR or create $SIGMA_DIR/)."
  fi
fi

# Orphaned top-level entries (anything not in allowlist)
# Build allow set = REQUIRED_TOP_DIRS + SIGMA_DIR + ALLOWED_TOP_LEVEL
# Using a flat list + loop instead of associative array (bash 3 compat)
ALLOW_LIST=()
for x in "${REQUIRED_TOP_DIRS[@]}"; do ALLOW_LIST+=("$x"); done
ALLOW_LIST+=("$SIGMA_DIR")
for x in "${ALLOWED_TOP_LEVEL[@]}"; do ALLOW_LIST+=("$x"); done

_in_allow() {
  local needle="$1"
  for item in "${ALLOW_LIST[@]}"; do
    [[ "$item" == "$needle" ]] && return 0
  done
  return 1
}

while IFS= read -r entry; do
  [[ -z "$entry" ]] && continue
  # ignore . and ..
  [[ "$entry" == "." || "$entry" == ".." ]] && continue
  if ! _in_allow "$entry"; then
    add_vio "ORPHAN_TOPLEVEL" "$entry" 0 "Top-level entry is not sanctioned; move it into an approved directory."
  fi
done < <(find . -mindepth 1 -maxdepth 1 -print | sed 's|^\./||')

# Agent office checks
if [[ -d "agents" ]]; then
  shopt -s nullglob
  for agent_dir in agents/*; do
    [[ -d "$agent_dir" ]] || continue
    agent="$(basename "$agent_dir")"

    # Required files
    for f in "${AGENT_REQUIRED_FILES[@]}"; do
      [[ -f "$agent_dir/$f" ]] || add_vio "MISSING_INIT" "$agent_dir/$f" 1 "Agent office missing required file."
    done

    # Required dirs
    for sub in "${AGENT_REQUIRED_DIRS[@]}"; do
      [[ -d "$agent_dir/$sub" ]] || add_vio "MISSING_DIR" "$agent_dir/$sub" 1 "Agent office missing required directory."
    done
  done
  shopt -u nullglob
fi

# Flat principle: no subdirectories under inbox states (and any extra globs provided)
FLAT_DIR_GLOBS=("${FLAT_DIR_GLOBS_DEFAULT[@]}")
if [[ -n "$SCAFFOLD_FLAT_DIRS" ]]; then
  while IFS= read -r line; do
    [[ -n "$line" ]] && FLAT_DIR_GLOBS+=("$line")
  done <<< "$SCAFFOLD_FLAT_DIRS"
fi

for g in "${FLAT_DIR_GLOBS[@]}"; do
  shopt -s nullglob
  for dir in $g; do
    [[ -d "$dir" ]] || continue
    # find immediate subdirectories
    while IFS= read -r subd; do
      [[ -z "$subd" ]] && continue
      add_vio "FLAT_VIOLATION" "$subd" 0 "Subdirectory found where flat principle applies."
    done < <(find "$dir" -mindepth 1 -maxdepth 1 -type d -print 2>/dev/null)
  done
  shopt -u nullglob
done

# DYN-* cadence checks
NOW="$(now_epoch)"
while IFS= read -r f; do
  [[ -f "$f" ]] || continue
  # Skip pipeline artifacts, archived sandboxes, and non-text DYN files
  case "$f" in
    *sources/04-SOURCES/_meta/*|*-SOVEREIGN/CONFIG-SANDBOX*|*.json|*.csv|*.jsonl|*.yaml|*.mmd) continue ;;
  esac
  # Read first ~30 lines for Cadence:
  cadence="$(sed -n '1,30p' "$f" | grep -iE '^\*{0,2}[Cc]adence\*{0,2}:|^[Uu]pdate [Cc]adence:' | head -n1 | sed 's/.*[Cc]adence[*]*:[[:space:]]*//' | tr -d '[:space:]*' | tr '[:upper:]' '[:lower:]' || true)"
  if [[ -z "$cadence" ]]; then
    add_vio "DYN_MISSING_CADENCE" "$f" 0 "DYN file missing 'Cadence:' header in first 30 lines."
    continue
  fi

  max_age=""
  case "$cadence" in
    daily)     max_age="$CADENCE_DAILY" ;;
    weekly)    max_age="$CADENCE_WEEKLY" ;;
    monthly)   max_age="$CADENCE_MONTHLY" ;;
    quarterly) max_age="$CADENCE_QUARTERLY" ;;
    yearly|annual) max_age="$CADENCE_YEARLY" ;;
    on-change|adhoc|ad-hoc) max_age="" ;;  # no staleness enforcement
    *) add_vio "DYN_UNKNOWN_CADENCE" "$f" 0 "Unknown cadence '$cadence'." ;;
  esac

  if [[ -n "$max_age" ]]; then
    mt="$(mtime_epoch "$f")"
    age=$((NOW - mt))
    if (( age > max_age )); then
      add_vio "DYN_STALE" "$f" 0 "DYN file stale for cadence '$cadence' (age ${age}s > ${max_age}s)."
    fi
  fi
done < <(find . -type f -name 'DYN-*' -print 2>/dev/null | sed 's|^\./||')

# ARCH-* header checks: Version + Date/Updated in first 30 lines
while IFS= read -r f; do
  [[ -f "$f" ]] || continue
  head30="$(sed -n '1,30p' "$f")"
  echo "$head30" | grep -Eq '^\*{0,2}[Vv]ersion\*{0,2}:\s*' || add_vio "ARCH_MISSING_VERSION" "$f" 0 "ARCH file missing 'Version:' header in first 30 lines."
  echo "$head30" | grep -Eq '^\*{0,2}([Dd]ate|[Uu]pdated|[Ll]ast [Uu]pdated)\*{0,2}:\s*[0-9]{4}-[0-9]{2}-[0-9]{2}' || add_vio "ARCH_MISSING_DATE" "$f" 0 "ARCH file missing 'Date:' or 'Updated:' header (YYYY-MM-DD) in first 30 lines."
done < <(find . -type f -name 'ARCH-*' -print 2>/dev/null | sed 's|^\./||')

# Broken markdown cross-references (local links)
if have python3; then
  python3 - <<'PY' "$ROOT" "$VIO_TMP"
import os, re, sys

root = sys.argv[1]
vio_path = sys.argv[2]

# Markdown link patterns:
# - standard: ](path)
# - wikilinks: [[path]]
md_files = []
for dirpath, dirnames, filenames in os.walk(root):
    # skip .git and sources/ (raw extraction content contains markdown-like syntax)
    if "/.git/" in dirpath or dirpath.endswith("/.git"):
        continue
    if "/sources/" in dirpath or dirpath.endswith("/sources"):
        continue
    if "/-SOVEREIGN/" in dirpath:
        continue
    for fn in filenames:
        if fn.lower().endswith(".md"):
            md_files.append(os.path.join(dirpath, fn))

link_pat = re.compile(r"\]\(([^)]+)\)")
wik_pat  = re.compile(r"\[\[([^\]]+)\]\]")

def is_local(p: str) -> bool:
    p = p.strip()
    if not p: return False
    if p.startswith("#"): return False
    if re.match(r"^(https?:|mailto:|tel:)", p, re.I): return False
    return True

def normalize_target(p: str) -> str:
    p = p.strip().split("#", 1)[0].strip()
    p = p.split("?", 1)[0].strip()
    return p

violations = []
for fp in md_files:
    with open(fp, "r", encoding="utf-8", errors="ignore") as f:
        txt = f.read()

    candidates = link_pat.findall(txt) + wik_pat.findall(txt)
    for raw in candidates:
        raw = raw.strip()
        if not is_local(raw):
            continue
        tgt = normalize_target(raw)
        # ignore empty after stripping anchor
        if not tgt:
            continue
        # Absolute-ish paths treated as repo-root relative if they start with /
        if tgt.startswith("/"):
            abs_tgt = os.path.join(root, tgt.lstrip("/"))
        else:
            abs_tgt = os.path.normpath(os.path.join(os.path.dirname(fp), tgt))
        if not os.path.exists(abs_tgt):
            rel_fp = os.path.relpath(fp, root)
            violations.append(("BROKEN_LINK", rel_fp, 0, f"Broken link target: '{raw}'"))

with open(vio_path, "a", encoding="utf-8") as out:
    for code, path, fixable, msg in violations:
        out.write(f"{code}\t{path}\t{fixable}\t{msg}\n")
PY
else
  add_vio "MISSING_DEP" "python3" 0 "python3 not found; broken-link validation skipped."
fi

# Makefile configs target
if [[ -f "Makefile" ]]; then
  if make -s configs >/tmp/scaffold_make_configs.out 2>&1; then
    :
  else
    msg="$(tail -n 40 /tmp/scaffold_make_configs.out | tr '\n' ' ' | sed 's/[[:space:]]\+/ /g')"
    add_vio "MAKE_CONFIGS_FAIL" "Makefile:configs" 0 "Makefile configs target failed: ${msg}"
  fi
fi

# ---- emit results ----------------------------------------------------------
STATUS="PASS"
VCOUNT="$(wc -l < "$VIO_TMP" | tr -d '[:space:]')"
if [[ "$VCOUNT" != "0" ]]; then STATUS="FAIL"; fi

if [[ "$OUTPUT_FORMAT" == "md" ]]; then
  echo "# scaffold_validate"
  echo
  echo "- status: $STATUS"
  echo "- repo_root: $ROOT"
  echo "- violations: $VCOUNT"
  echo
  if [[ "$VCOUNT" != "0" ]]; then
    echo "## violations"
    echo
    while IFS=$'\t' read -r code path fixable msg; do
      echo "- [$code] ($path) fixable=$fixable — $msg"
    done < "$VIO_TMP"
  fi
else
  if ! have python3; then die "python3 required for JSON emission."; fi
  python3 - <<'PY' "$ROOT" "$STATUS" "$VIO_TMP"
import json, sys, datetime
root, status, vio = sys.argv[1], sys.argv[2], sys.argv[3]
violations=[]
with open(vio, "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        line=line.rstrip("\n")
        if not line: continue
        code, path, fixable, msg = line.split("\t", 3)
        violations.append({"code":code, "path":path, "fixable":bool(int(fixable)), "message":msg})
out = {
  "status": status,
  "timestamp": datetime.datetime.utcnow().replace(microsecond=0).isoformat()+"Z",
  "repo_root": root,
  "violations": violations,
  "stats": {"violations": len(violations)}
}
print(json.dumps(out, indent=2, sort_keys=False))
PY
fi

[[ "$STATUS" == "PASS" ]] && exit 0 || exit 1
