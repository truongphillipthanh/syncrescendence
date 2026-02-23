Here's a coherent, self-healing scaffold toolchain that treats the git-tracked filesystem as sovereign truth, and treats every other layer (launchd, generated configs, graph indices) as derived and regenerable. Everything below assumes repo root contains `orchestration/ canon/ engine/ sources/ agents/` plus a sigma-equivalent directory (default `sigma/`, overridable).

I'm giving you three scripts that work together:

* `scripts/scaffold_validate.sh` — authoritative structural integrity check, JSON output by default (machine-parseable), strict enough for pre-commit/CI.
* `scripts/scaffold_heal.sh` — safe auto-repair (mkdirs, INIT templates, unambiguous link fixes), and an "attention report" for anything requiring human judgment.
* `scripts/scaffold_rename.sh` — one-time migration (git mv + reference rewrite + launchd plist rewrite + report).

These scripts are designed to be boring under failure: if optional tooling is missing (`rg`, `jq`), they degrade to POSIX-ish equivalents, while still producing a deterministic PASS/FAIL signal.

---

## 1) `scripts/scaffold_validate.sh`

Default output is JSON. Exit code `0` on PASS, `1` on FAIL.

```bash
#!/usr/bin/env bash
# scripts/scaffold_validate.sh
set -euo pipefail

# ---- config ---------------------------------------------------------------
SIGMA_DIR_DEFAULT="sigma"                         # sigma-equivalent dir name (rename script can change)
SIGMA_DIR="${SIGMA_DIR:-$SIGMA_DIR_DEFAULT}"      # override via env SIGMA_DIR

# Top-level directories required
REQUIRED_TOP_DIRS=( "orchestration" "canon" "engine" "sources" "agents" )

# Allowed top-level entries (dirs or files) besides REQUIRED_TOP_DIRS + SIGMA_DIR
ALLOWED_TOP_LEVEL=(
  ".git" ".github" ".claude" ".vscode"
  "scripts" "templates" "reports" "docs"
  "Makefile" "README.md" "AGENTS.md" "CLAUDE.md" "LICENSE"
  ".gitignore" ".gitattributes"
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
    add_vio "MISSING_DIR" "$SIGMA_DIR" 1 "Sigma-equivalent directory missing (set SIGMA_DIR or create sigma/)."
  fi
fi

# Orphaned top-level entries (anything not in allowlist)
# Build allow set = REQUIRED_TOP_DIRS + SIGMA_DIR + ALLOWED_TOP_LEVEL
declare -A ALLOW
for x in "${REQUIRED_TOP_DIRS[@]}"; do ALLOW["$x"]=1; done
ALLOW["$SIGMA_DIR"]=1
for x in "${ALLOWED_TOP_LEVEL[@]}"; do ALLOW["$x"]=1; done

while IFS= read -r entry; do
  [[ -z "$entry" ]] && continue
  # ignore . and ..
  [[ "$entry" == "." || "$entry" == ".." ]] && continue
  if [[ -z "${ALLOW[$entry]+x}" ]]; then
    add_vio "ORPHAN_TOPLEVEL" "$entry" 0 "Top-level entry is not sanctioned; move it into an approved directory."
  fi
done < <(find . -mindepth 1 -maxdepth 1 -printf "%P\n" 2>/dev/null || find . -mindepth 1 -maxdepth 1 -print | sed 's|^\./||')

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
  # Read first ~30 lines for Cadence:
  cadence="$(sed -n '1,30p' "$f" | grep -E '^[Cc]adence:' | head -n1 | awk -F: '{print tolower($2)}' | tr -d '[:space:]' || true)"
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
  echo "$head30" | grep -Eq '^[Vv]ersion:\s*' || add_vio "ARCH_MISSING_VERSION" "$f" 0 "ARCH file missing 'Version:' header in first 30 lines."
  echo "$head30" | grep -Eq '^([Dd]ate|[Uu]pdated):\s*[0-9]{4}-[0-9]{2}-[0-9]{2}' || add_vio "ARCH_MISSING_DATE" "$f" 0 "ARCH file missing 'Date:' or 'Updated:' header (YYYY-MM-DD) in first 30 lines."
done < <(find . -type f -name 'ARCH-*' -print 2>/dev/null | sed 's|^\./||')

# Broken markdown cross-references (local links)
if have python3; then
  python3 - <<'PY' "$ROOT" "$VIO_TMP"
import os, re, sys

root = sys.argv
vio_path = sys.argv

# Markdown link patterns:
# - standard: ](path)
# - wikilinks: [[path]]
md_files = []
for dirpath, dirnames, filenames in os.walk(root):
    # skip .git
    if "/.git/" in dirpath or dirpath.endswith("/.git"):
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
    p = p.strip().split("#", 1).strip()
    p = p.split("?", 1).strip()
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
root, status, vio = sys.argv, sys.argv, sys.argv
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
```

---

## 2) `scripts/scaffold_heal.sh`

This script only performs repairs that are unambiguously safe. Everything else is reported as "needs human attention."

* Creates missing directories (top-level, agent office structure).
* Generates missing `INIT.md` from a template.
* Fixes broken markdown links only when the target can be resolved unambiguously by basename within the repo.
* Never deletes anything.
* Never "updates" stale DYN files; it flags them.

```bash
#!/usr/bin/env bash
# scripts/scaffold_heal.sh
set -euo pipefail

SIGMA_DIR_DEFAULT="sigma"
SIGMA_DIR="${SIGMA_DIR:-$SIGMA_DIR_DEFAULT}"

die() { echo "ERROR: $*" >&2; exit 2; }
have() { command -v "$1" >/dev/null 2>&1; }
repo_root() { git rev-parse --show-toplevel 2>/dev/null || die "Not in a git repo."; }

ROOT="$(repo_root)"
cd "$ROOT"

[[ -x "scripts/scaffold_validate.sh" ]] || die "scripts/scaffold_validate.sh not found or not executable."
have python3 || die "python3 required for scaffold_heal."

VAL_JSON="$(mktemp -t scaffold_val.XXXXXX.json)"
HEAL_JSON="$(mktemp -t scaffold_heal.XXXXXX.json)"
ATTN_MD="reports/scaffold_heal_attention_$(date +%Y%m%d-%H%M%S).md"
mkdir -p reports

# Run validate
if scripts/scaffold_validate.sh --json >"$VAL_JSON"; then
  # nothing to heal
  python3 - <<'PY' "$ROOT"
import json, sys, datetime
print(json.dumps({
  "status":"PASS",
  "timestamp": datetime.datetime.utcnow().replace(microsecond=0).isoformat()+"Z",
  "repo_root": sys.argv,
  "healed": [],
  "needs_human_attention": []
}, indent=2))
PY
  exit 0
fi

# Extract violations
python3 - <<'PY' "$VAL_JSON" "$HEAL_JSON" "$ATTN_MD" "$SIGMA_DIR"
import json, os, sys, datetime, pathlib, re

val_path, out_path, attn_path, sigma_dir = sys.argv, sys.argv, sys.argv, sys.argv
data = json.load(open(val_path, "r", encoding="utf-8"))
root = data["repo_root"]
violations = data.get("violations", [])

healed = []
attn = []

def mkdirp(rel):
    p = os.path.join(root, rel)
    os.makedirs(p, exist_ok=True)
    healed.append({"action":"mkdir", "path":rel})

def write_init(agent_rel):
    # agent_rel like agents/Commander
    init_rel = os.path.join(agent_rel, "INIT.md")
    init_abs = os.path.join(root, init_rel)
    if os.path.exists(init_abs):
        return
    agent = os.path.basename(agent_rel.rstrip("/"))
    template = f"""# {agent} — INIT
Version: 0.1.0
Date: {datetime.date.today().isoformat()}

Agent: {agent}
Office: {agent_rel}
Mandate: (fill)
Interfaces: inbox/ outbox/ scratchpad/ memory/
Cadence: (fill)

## Operating Notes
- This file is authoritative for local office invariants.
"""
    os.makedirs(os.path.dirname(init_abs), exist_ok=True)
    with open(init_abs, "w", encoding="utf-8") as f:
        f.write(template)
    healed.append({"action":"write_template", "path":init_rel})

def find_unique_by_basename(basename):
    # Search tracked files first, then whole repo if needed
    matches = []
    for dirpath, dirnames, filenames in os.walk(root):
        if "/.git/" in dirpath or dirpath.endswith("/.git"):
            continue
        for fn in filenames:
            if fn == basename:
                matches.append(os.path.join(dirpath, fn))
    # unique?
    if len(matches) == 1:
        return matches
    return None

def fix_md_links():
    # For each .md file, fix broken local links when target basename uniquely resolves.
    link_pat = re.compile(r"\]\(([^)]+)\)")
    wik_pat  = re.compile(r"\[\[([^\]]+)\]\]")

    def is_local(p):
        p = p.strip()
        if not p: return False
        if p.startswith("#"): return False
        if re.match(r"^(https?:|mailto:|tel:)", p, re.I): return False
        return True

    def normalize_target(p):
        p = p.strip().split("#",1).split("?",1).strip()
        return p

    for dirpath, dirnames, filenames in os.walk(root):
        if "/.git/" in dirpath or dirpath.endswith("/.git"):
            continue
        for fn in filenames:
            if not fn.lower().endswith(".md"):
                continue
            fp = os.path.join(dirpath, fn)
            rel_fp = os.path.relpath(fp, root)
            txt = open(fp, "r", encoding="utf-8", errors="ignore").read()

            def fix_one(raw):
                if not is_local(raw):
                    return None
                tgt = normalize_target(raw)
                if not tgt:
                    return None
                # Resolve current target
                if tgt.startswith("/"):
                    abs_tgt = os.path.join(root, tgt.lstrip("/"))
                else:
                    abs_tgt = os.path.normpath(os.path.join(os.path.dirname(fp), tgt))
                if os.path.exists(abs_tgt):
                    return None

                base = os.path.basename(tgt)
                resolved = find_unique_by_basename(base)
                if not resolved:
                    return None

                # Compute new relative path
                new_rel = os.path.relpath(resolved, os.path.dirname(fp))
                new_rel = new_rel.replace(os.sep, "/")
                # Preserve anchor if present
                anchor = ""
                if "#" in raw:
                    anchor = "#" + raw.split("#",1)
                return (raw, new_rel + anchor)

            changed = False

            # standard links
            for raw in set(link_pat.findall(txt)):
                repl = fix_one(raw)
                if repl:
                    a,b = repl
                    txt = txt.replace(f"]({a})", f"]({b})")
                    healed.append({"action":"fix_link", "file":rel_fp, "from":a, "to":b})
                    changed = True

            # wikilinks
            for raw in set(wik_pat.findall(txt)):
                repl = fix_one(raw)
                if repl:
                    a,b = repl
                    txt = txt.replace(f"[[{a}]]", f"[[{b}]]")
                    healed.append({"action":"fix_wikilink", "file":rel_fp, "from":a, "to":b})
                    changed = True

            if changed:
                with open(fp, "w", encoding="utf-8") as f:
                    f.write(txt)

# Safe repairs based on fixable violations
for v in violations:
    code = v["code"]
    path = v["path"]
    fixable = v.get("fixable", False)
    if not fixable:
        continue

    if code == "MISSING_DIR":
        mkdirp(path)
    elif code == "MISSING_INIT":
        # path is agents/<agent>/INIT.md
        agent_rel = str(pathlib.Path(path).parent).replace("\\","/")
        write_init(agent_rel)

# Opportunistic link repair (safe only when unambiguous)
fix_md_links()

# Human attention: stale DYN files + any non-fixable violations
for v in violations:
    if v["code"] in ("DYN_STALE","DYN_MISSING_CADENCE","DYN_UNKNOWN_CADENCE"):
        attn.append(v)
    elif not v.get("fixable", False):
        attn.append(v)

# Write attention report
lines = []
lines.append("# scaffold_heal — human attention")
lines.append("")
lines.append(f"- timestamp: {datetime.datetime.utcnow().replace(microsecond=0).isoformat()}Z")
lines.append(f"- violations_needing_attention: {len(attn)}")
lines.append("")
for v in attn:
    lines.append(f"- [{v['code']}] ({v['path']}) — {v['message']}")
os.makedirs(os.path.dirname(os.path.join(root, attn_path)), exist_ok=True)
open(os.path.join(root, attn_path), "w", encoding="utf-8").write("\n".join(lines) + "\n")

# Emit heal report JSON
out = {
  "status": "HEALED_WITH_REMAINDERS" if attn else "HEALED_CLEAN",
  "timestamp": datetime.datetime.utcnow().replace(microsecond=0).isoformat()+"Z",
  "repo_root": root,
  "healed": healed,
  "needs_human_attention": attn,
  "attention_report": attn_path.replace("\\","/")
}
json.dump(out, open(out_path, "w", encoding="utf-8"), indent=2)
print(json.dumps(out, indent=2))
PY

# Re-run validate for final pass/fail signal
echo
echo "Re-validating after heal..."
if scripts/scaffold_validate.sh --json >/dev/null; then
  exit 0
else
  echo "Validation still failing. See: $ATTN_MD" >&2
  exit 1
fi
```

---

## 3) `scripts/scaffold_rename.sh` (one-time numbered → semantic migration)

This script:

* Requires clean git status.
* `git mv` old directories → new directories.
* Rewrites internal references across tracked + untracked (non-ignored) text files.
* Rewrites launchd plist templates inside the repo.
* Produces a before/after count report in `reports/`.
* Runs `scaffold_validate.sh` at the end.

It also handles `praxis` → your chosen name via `--sigma-name <dir>`.

```bash
#!/usr/bin/env bash
# scripts/scaffold_rename.sh
set -euo pipefail

die() { echo "ERROR: $*" >&2; exit 2; }
have() { command -v "$1" >/dev/null 2>&1; }
repo_root() { git rev-parse --show-toplevel 2>/dev/null || die "Not in a git repo."; }

SIGMA_NAME="sigma"
while [[ $# -gt 0 ]]; do
  case "$1" in
    --sigma-name) SIGMA_NAME="${2:-}"; shift 2 ;;
    *) die "Unknown arg: $1" ;;
  esac
done
[[ -n "$SIGMA_NAME" ]] || die "--sigma-name requires a value."

ROOT="$(repo_root)"
cd "$ROOT"

have python3 || die "python3 required for reference rewrite."
have git || die "git required."

# Clean working tree required
git diff --quiet || die "Working tree dirty. Commit or stash before rename."
git diff --cached --quiet || die "Index dirty. Commit or stash before rename."

mkdir -p reports
REPORT="reports/scaffold_rename_report_$(date +%Y%m%d-%H%M%S).md"

# Map old → new
declare -A MAP
MAP["orchestration"]="orchestration"
MAP["canon"]="canon"
MAP["engine"]="engine"
MAP["sources"]="sources"
MAP["praxis"]="$SIGMA_NAME"

count_refs() {
  local needle="$1"
  if have rg; then
    rg -n --no-heading -S "$needle" . | wc -l | tr -d '[:space:]'
  else
    grep -RIn "$needle" . 2>/dev/null | wc -l | tr -d '[:space:]'
  fi
}

{
  echo "# scaffold_rename report"
  echo
  echo "- timestamp: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "- repo_root: $ROOT"
  echo "- sigma_name: $SIGMA_NAME"
  echo
  echo "## before reference counts"
  for old in "${!MAP[@]}"; do
    echo "- $old: $(count_refs "$old")"
  done
} >"$REPORT"

# Perform git mv operations
for old in "${!MAP[@]}"; do
  new="${MAP[$old]}"
  if [[ -d "$old" ]]; then
    if [[ -e "$new" ]]; then
      die "Target path already exists: $new (cannot mv $old)."
    fi
    git mv "$old" "$new"
  fi
done

# Rewrite references in text files (tracked + untracked non-ignored)
python3 - <<'PY' "$ROOT" "$REPORT"
import os, sys, subprocess, pathlib

root = sys.argv
report = sys.argv

# same mapping as bash (hardcoded here to avoid fragile cross-process export)
# NOTE: keep this in sync with MAP above
mapping = {
  "orchestration": "orchestration",
  "canon": "canon",
  "engine": "engine",
  "sources": "sources",
  "praxis": None,   # will be filled from git mv result: look for any dir in root that was just created and contains prior content
}

# Determine sigma target by checking which of known targets exists besides defaults
# We'll infer it by scanning for a directory that is neither standard nor numbered.
# More reliable: read it from the report line "sigma_name: ..."
sigma_name = None
with open(report, "r", encoding="utf-8") as f:
    for line in f:
        if line.startswith("- sigma_name:"):
            sigma_name = line.split(":",1).strip()
            break
if not sigma_name:
    sigma_name = "sigma"
mapping["praxis"] = sigma_name

# Files to edit: tracked + untracked (non-ignored)
def git_lines(args):
    out = subprocess.check_output(["git"] + args, cwd=root, text=True)
    return [ln.strip() for ln in out.splitlines() if ln.strip()]

tracked = set(git_lines(["ls-files"]))
untracked = set(git_lines(["ls-files","-co","--exclude-standard"]))
paths = sorted(tracked | untracked)

def is_text_file(p: pathlib.Path) -> bool:
    # quick heuristic by extension + utf-8 decodability
    ext = p.suffix.lower()
    if ext in {".png",".jpg",".jpeg",".gif",".webp",".pdf",".zip",".gz",".tgz",".bz2",".7z",".dmg",".pkg",".a",".o",".so",".dylib",".exe"}:
        return False
    try:
        data = p.read_bytes()
    except Exception:
        return False
    # reject obvious binary
    if b"\x00" in data[:4096]:
        return False
    try:
        data.decode("utf-8")
        return True
    except Exception:
        return False

edits = 0
for rel in paths:
    abs_p = pathlib.Path(root) / rel
    if not abs_p.exists() or not abs_p.is_file():
        continue
    if not is_text_file(abs_p):
        continue
    txt = abs_p.read_text(encoding="utf-8", errors="ignore")
    orig = txt
    for old, new in mapping.items():
        # Replace both "OLD/" and "OLD" occurrences (path-safe approach)
        txt = txt.replace(old + "/", new + "/")
        txt = txt.replace(old, new)
    if txt != orig:
        abs_p.write_text(txt, encoding="utf-8")
        edits += 1

with open(report, "a", encoding="utf-8") as f:
    f.write("\n## reference rewrite\n")
    f.write(f"- edited_files: {edits}\n")
PY

# Update launchd plists in repo if present (they're already covered by rewrite; this is just an explicit audit point)
{
  echo
  echo "## after reference counts"
  for old in "${!MAP[@]}"; do
    echo "- $old: $(count_refs "$old")"
  done
  echo
  echo "## git status"
  git status --porcelain=v1
} >>"$REPORT"

echo "Rename completed. Report: $REPORT"

# Run validation
SIGMA_DIR="$SIGMA_NAME" scripts/scaffold_validate.sh --json >/dev/null || {
  echo "Post-rename validation failed. See report: $REPORT" >&2
  exit 1
}

echo "Post-rename validation PASS."
```

---

## Wiring into pre-commit and CI (minimal, strict)

### `.git/hooks/pre-commit` (local)

```bash
#!/usr/bin/env bash
set -euo pipefail
scripts/scaffold_validate.sh --json >/dev/null
```

If you want "heal then validate" behavior locally (still fail if unresolved):

```bash
#!/usr/bin/env bash
set -euo pipefail
scripts/scaffold_validate.sh --json >/dev/null || scripts/scaffold_heal.sh
scripts/scaffold_validate.sh --json >/dev/null
```

### GitHub Actions (if you use it)

A single step running `scripts/scaffold_validate.sh` is enough.

---

## Agent office scaling pattern (agents 6–20)

Minimum to create a new agent:

1. `agents/<AgentID>/INIT.md`
2. `agents/<AgentID>/inbox/{pending,active,done,failed,blocked}/`
3. `agents/<AgentID>/{outbox,scratchpad,memory}/`

You already get this automatically if `scaffold_heal.sh` sees the directory and notices missing structure. The one "manual" act becomes: create `agents/<AgentID>/` directory. Everything else can be healed into existence.

Dispatch auto-discovery (`dispatch.sh` should never hardcode agent names):

```bash
AGENTS=()
for d in "$REPO_ROOT/agents"/*; do
  [[ -d "$d" ]] || continue
  agent="$(basename "$d")"
  AGENTS+=("$agent")
done
```

Auto-ingest should be parameterized by agent directory discovery the same way, optionally filtered by `--agent <id>`.

Makefile should use wildcards:

```makefile
AGENT_DIRS := $(wildcard agents/*/)
AGENTS := $(patsubst agents/%/,%,$(AGENT_DIRS))

configs:
	@./scripts/generate_configs.sh $(AGENTS)

validate:
	@./scripts/scaffold_validate.sh --json >/dev/null
```

This keeps "agent count changes" inside the filesystem only; your tooling follows the scaffold rather than requiring updates per new agent.

---

## A couple of small invariants that make the scaffold antifragile

1. Every "dynamic" file (`DYN-*`) must declare cadence in the first 30 lines via `Cadence: daily|weekly|monthly|...` so staleness becomes a mechanical property rather than a feeling.

2. Every "architecture" file (`ARCH-*`) must have `Version:` and `Date:`/`Updated:` headers, so "is this current?" is deterministic.

3. Generated caches live under `**/cache/` and are explicitly overwrite-safe. Humans never curate caches; humans curate `MEMORY.md` and `entities/`.

If you want, I can also give you a `scripts/agent_new.sh <AgentID>` that creates the directory and then calls `scaffold_heal.sh`, plus a `launchd` plist template that runs `scaffold_validate.sh` daily and opens a failure report in a predictable location.
