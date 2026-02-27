#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE}")/config.sh"

# orchestration/00-ORCHESTRATION/scripts/scaffold_heal.sh
set -euo pipefail

SIGMA_DIR_DEFAULT="praxis"
SIGMA_DIR="${SIGMA_DIR:-$SIGMA_DIR_DEFAULT}"

die() { echo "ERROR: $*" >&2; exit 2; }
have() { command -v "$1" >/dev/null 2>&1; }
repo_root() { git rev-parse --show-toplevel 2>/dev/null || die "Not in a git repo."; }

ROOT="$(repo_root)"
cd "$ROOT"

VALIDATE_SCRIPT="${ORCHESTRATION_DIR#$REPO_ROOT/}/scripts/scaffold_validate.sh"

[[ -x "$VALIDATE_SCRIPT" ]] || die "$VALIDATE_SCRIPT not found or not executable."
have python3 || die "python3 required for scaffold_heal."

VAL_JSON="$(mktemp -t scaffold_val.XXXXXX.json)"
HEAL_JSON="$(mktemp -t scaffold_heal.XXXXXX.json)"
ATTN_MD="reports/scaffold_heal_attention_$(date +%Y%m%d-%H%M%S).md"
mkdir -p reports

# Run validate
if "$VALIDATE_SCRIPT" --json >"$VAL_JSON"; then
  # nothing to heal
  python3 - <<'PY' "$ROOT"
import json, sys, datetime
print(json.dumps({
  "status":"PASS",
  "timestamp": datetime.datetime.utcnow().replace(microsecond=0).isoformat()+"Z",
  "repo_root": sys.argv[1],
  "healed": [],
  "needs_human_attention": []
}, indent=2))
PY
  exit 0
fi

# Extract violations
python3 - <<'PY' "$VAL_JSON" "$HEAL_JSON" "$ATTN_MD" "$SIGMA_DIR"
import json, os, sys, datetime, pathlib, re

val_path, out_path, attn_path, sigma_dir = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
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
        return matches[0]
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
        p = p.strip().split("#", 1)[0].split("?", 1)[0].strip()
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
                    anchor = "#" + raw.split("#", 1)[1]
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
if "$VALIDATE_SCRIPT" --json >/dev/null; then
  exit 0
else
  echo "Validation still failing. See: $ATTN_MD" >&2
  exit 1
fi
