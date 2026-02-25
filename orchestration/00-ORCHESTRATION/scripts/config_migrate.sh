#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
INVENTORY_PATH="$REPO_ROOT/-INBOX/commander/00-INBOX0/RESULT-CODEX-CONFIG-CENTRALIZATION.md"
MODE="dry-run"

usage() {
  cat <<'EOF'
Usage: config_migrate.sh [--dry-run|--apply]

Modes:
  --dry-run   Show proposed unified diffs (default)
  --apply     Write changes to disk
EOF
}

for arg in "$@"; do
  case "$arg" in
    --dry-run) MODE="dry-run" ;;
    --apply) MODE="apply" ;;
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

if [[ ! -f "$INVENTORY_PATH" ]]; then
  echo "Inventory missing: $INVENTORY_PATH" >&2
  exit 2
fi

echo "[config-migrate] repo: $REPO_ROOT"
echo "[config-migrate] inventory: $INVENTORY_PATH"
echo "[config-migrate] mode: $MODE"

python3 - "$MODE" "$INVENTORY_PATH" "$SCRIPT_DIR" <<'PY'
import difflib
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

mode, inventory_path, scripts_dir = sys.argv[1:4]
inventory = Path(inventory_path)
scripts = Path(scripts_dir)

row_re = re.compile(r"^\|\s*`([^`]+)`\s*\|\s*`([^`]+)`\s*\|")
mappings: list[tuple[str, str]] = []  # (literal, variable)
for raw in inventory.read_text(errors="replace").splitlines():
    m = row_re.match(raw.strip())
    if m:
        var, literal = m.group(1).strip(), m.group(2).strip()
        mappings.append((literal, var))

if not mappings:
    print("[config-migrate] ERROR: no mappings parsed from inventory", file=sys.stderr)
    sys.exit(2)

# Longest literal first to avoid partial shadowing.
mappings.sort(key=lambda x: len(x[0]), reverse=True)

BASH_SOURCE_LINE = 'source "$(dirname "${BASH_SOURCE}")/config.sh"'


# ---------------------------------------------------------------------------
# Transform helpers
# ---------------------------------------------------------------------------

def has_bash_shebang(text: str) -> bool:
    first = text.splitlines()[0] if text.splitlines() else ""
    return first.startswith("#!") and "bash" in first


def inject_bash_source(text: str) -> tuple[str, bool]:
    lines = text.splitlines(keepends=True)
    cleaned = []
    removed = False
    for line in lines:
        if re.match(r"^\s*source\s+.*config\.sh.*$", line):
            removed = True
            continue
        cleaned.append(line)
    lines = cleaned

    insert_idx = 1 if lines and lines[0].startswith("#!") else 0
    while insert_idx < len(lines) and lines[insert_idx].strip() == "":
        lines.pop(insert_idx)

    inject = BASH_SOURCE_LINE + "\n"
    if insert_idx < len(lines) and lines[insert_idx].strip() != "":
        inject += "\n"

    lines.insert(insert_idx, inject)
    updated = "".join(lines)
    return updated, (updated != text or removed)


def _bash_rel_expr(var_name: str) -> str:
    return "${" + var_name + "#$REPO_ROOT/}"


def replace_bash_paths(text: str) -> tuple[str, int]:
    changed = 0
    out = text

    for literal, var in mappings:
        before = out

        # Canonical absolute patterns built from REPO_ROOT.
        out = out.replace(f"${{REPO_ROOT}}/{literal}", f"${{{var}}}")
        out = out.replace(f"$REPO_ROOT/{literal}", f"${var}")

        # Relative literal in double-quoted strings can be represented as
        # a path relative to repo root using config variables.
        out = out.replace(f'"{literal}', '"' + _bash_rel_expr(var))

        if out != before:
            changed += 1

    return out, changed


def _find_docstring_end(lines: list[str], start: int) -> int:
    line = lines[start].lstrip()
    if not (line.startswith('"""') or line.startswith("'''")):
        return start

    quote = '"""' if line.startswith('"""') else "'''"
    # Single-line docstring
    if line.count(quote) >= 2 and len(line) > 6:
        return start + 1

    i = start + 1
    while i < len(lines):
        if quote in lines[i]:
            return i + 1
        i += 1
    return start + 1


def inject_python_import(text: str) -> tuple[str, bool]:
    lines = text.splitlines(keepends=True)
    removed = False
    cleaned = []
    for line in lines:
        if re.match(r"^\s*from\s+config\s+import\s+\*\s*$", line):
            removed = True
            continue
        cleaned.append(line)
    lines = cleaned

    idx = 0

    if idx < len(lines) and lines[idx].startswith("#!"):
        idx += 1

    if idx < len(lines) and re.match(r"^#.*coding[:=]", lines[idx]):
        idx += 1

    # Skip blank lines before possible module docstring.
    while idx < len(lines) and lines[idx].strip() == "":
        idx += 1

    if idx < len(lines):
        stripped = lines[idx].lstrip()
        if stripped.startswith('"""') or stripped.startswith("'''"):
            idx = _find_docstring_end(lines, idx)

    # __future__ imports must stay at the beginning of the module body.
    # Skip comments/blank lines while scanning this prologue region.
    scan = idx
    saw_future = False
    while scan < len(lines):
        stripped = lines[scan].strip()
        if stripped == "" or lines[scan].lstrip().startswith("#"):
            scan += 1
            continue
        if re.match(r"^\s*from\s+__future__\s+import\s+", lines[scan]):
            saw_future = True
            scan += 1
            continue
        break
    if saw_future:
        idx = scan

    while idx > 0 and lines[idx - 1].strip() == "":
        lines.pop(idx - 1)
        idx -= 1

    while idx < len(lines) and lines[idx].strip() == "":
        lines.pop(idx)

    inject = "from config import *\n"
    if idx < len(lines) and lines[idx].strip() != "":
        inject += "\n"

    lines.insert(idx, inject)
    updated = "".join(lines)
    return updated, (updated != text or removed)


def replace_python_paths(text: str) -> tuple[str, int]:
    changed = 0
    out = text

    # Common local hardcoded root in existing scripts.
    out2 = re.sub(r"Path\(['\"]/Users/system/syncrescendence['\"]\)", "REPO_ROOT", out)
    if out2 != out:
        changed += 1
        out = out2

    for literal, var in mappings:
        # Replace REPO_ROOT / "literal[/suffix]" with VAR[/suffix]
        patt = re.compile(
            rf"REPO_ROOT\s*/\s*([\"']){re.escape(literal)}(?P<rest>/[^\"']*)?\1"
        )

        def _repl(match: re.Match[str]) -> str:
            rest = match.group("rest") or ""
            if not rest:
                return var
            return f'{var} / "{rest.lstrip("/")}"'

        newer = patt.sub(_repl, out)
        if newer != out:
            changed += 1
            out = newer

    return out, changed


# ---------------------------------------------------------------------------
# File loop
# ---------------------------------------------------------------------------

skip_reason = Counter()
changed_files: list[Path] = []
unchanged_files: list[Path] = []

for path in sorted(scripts.iterdir()):
    if not path.is_file():
        continue

    suffix = path.suffix.lower()

    # Scope: scripts only, skip prose.
    if suffix == ".md":
        skip_reason["markdown"] += 1
        continue

    if path.name in {"config.sh", "config.py", "config_migrate.sh"}:
        skip_reason["config-core"] += 1
        continue

    if suffix not in {".sh", ".py"}:
        skip_reason["non-script"] += 1
        continue

    original = path.read_text(errors="replace")
    updated = original
    local_changes = 0

    if suffix == ".sh":
        if not has_bash_shebang(original):
            skip_reason["non-bash-shebang"] += 1
            continue
        updated, did_inject = inject_bash_source(updated)
        if did_inject:
            local_changes += 1
        updated, c = replace_bash_paths(updated)
        local_changes += c
    else:
        updated, did_inject = inject_python_import(updated)
        if did_inject:
            local_changes += 1
        updated, c = replace_python_paths(updated)
        local_changes += c

    if updated == original:
        unchanged_files.append(path)
        continue

    changed_files.append(path)

    if mode == "dry-run":
        diff = difflib.unified_diff(
            original.splitlines(),
            updated.splitlines(),
            fromfile=str(path),
            tofile=str(path),
            lineterm="",
        )
        print("\n".join(diff))
        print()
    else:
        path.write_text(updated)

print("[config-migrate] summary")
print(f"  mapped literals: {len(mappings)}")
print(f"  migrated: {len(changed_files)}")
print(f"  unchanged: {len(unchanged_files)}")
print(f"  skipped: {sum(skip_reason.values())}")
if skip_reason:
    for reason in sorted(skip_reason):
        print(f"    - {reason}: {skip_reason[reason]}")
if changed_files:
    print("  migrated files:")
    for p in changed_files:
        print(f"    - {p}")

# Post-migration gate (always run).
validate = scripts / "scaffold_validate.sh"
print("[config-migrate] running scaffold_validate.sh --json")
res = subprocess.run([str(validate), "--json"], text=True, capture_output=True)
if res.stdout:
    print(res.stdout.rstrip())
if res.stderr:
    print(res.stderr.rstrip(), file=sys.stderr)
if res.returncode != 0:
    print(f"[config-migrate] gate FAILED (exit={res.returncode})", file=sys.stderr)
    sys.exit(res.returncode)
print("[config-migrate] gate PASSED")
PY
