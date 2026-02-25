#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE}")/config.sh"
set -euo pipefail
sync_config_preflight "$(basename "${BASH_SOURCE[0]}")"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODE="dry-run"
VERIFY=0
LEGACY_INVENTORY_PATH="$REPO_ROOT/-INBOX/commander/00-INBOX0/RESULT-CODEX-CONFIG-CENTRALIZATION.md"

usage() {
  cat <<'USAGE'
Usage: config_migrate.sh [--dry-run|--apply] [--verify]

Modes:
  --dry-run   Show proposed unified diffs (default)
  --apply     Write changes to disk

Options:
  --verify    After migration, run bash -n on .sh files and py_compile on .py files
USAGE
}

for arg in "$@"; do
  case "$arg" in
    --dry-run) MODE="dry-run" ;;
    --apply) MODE="apply" ;;
    --verify) VERIFY=1 ;;
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

echo "[config-migrate] repo: $REPO_ROOT"
echo "[config-migrate] scripts_dir: $SCRIPT_DIR"
echo "[config-migrate] mode: $MODE"
echo "[config-migrate] verify: $VERIFY"
if [[ -f "$LEGACY_INVENTORY_PATH" ]]; then
  echo "[config-migrate] legacy inventory: $LEGACY_INVENTORY_PATH"
else
  echo "[config-migrate] legacy inventory: missing (continuing with dynamic inventory)"
fi

python3 - "$MODE" "$VERIFY" "$REPO_ROOT" "$SCRIPT_DIR" "$LEGACY_INVENTORY_PATH" <<'PY'
import difflib
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

mode, verify, repo_root_raw, scripts_dir_raw, legacy_inventory_path = sys.argv[1:6]
verify = verify == "1"
repo_root = Path(repo_root_raw)
scripts_dir = Path(scripts_dir_raw)
legacy_inventory = Path(legacy_inventory_path)
hardcoded_root = "/Users/system/" + "syncrescendence"

# ---------------------------------------------------------------------------
# Mapping inventory (optional legacy + dynamic baseline)
# ---------------------------------------------------------------------------
row_re = re.compile(r"^\|\s*`([^`]+)`\s*\|\s*`([^`]+)`\s*\|")
mappings: list[tuple[str, str]] = []
if legacy_inventory.is_file():
    for raw in legacy_inventory.read_text(errors="replace").splitlines():
        m = row_re.match(raw.strip())
        if m:
            var, literal = m.group(1).strip(), m.group(2).strip()
            mappings.append((literal, var))

# Longest literal first to avoid partial shadowing.
mappings.sort(key=lambda x: len(x[0]), reverse=True)

# ---------------------------------------------------------------------------
# Dynamic hardcoded-path inventory (required by CC28)
# ---------------------------------------------------------------------------

def gather_scan_roots(root: Path) -> list[Path]:
    scan_roots: list[Path] = []
    candidates = [
        root / "orchestration" / "scripts",
        root / "orchestration" / "00-ORCHESTRATION" / "scripts",
    ]
    for candidate in candidates:
        if candidate.exists():
            scan_roots.append(candidate)

    agents_root = root / "agents"
    if agents_root.exists():
        for child in sorted(agents_root.iterdir()):
            if child.is_dir():
                scan_roots.append(child)
    return scan_roots


def script_files_under(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for base in paths:
        for path in base.rglob("*"):
            if not path.is_file():
                continue
            if path.suffix.lower() not in {".sh", ".py"}:
                continue
            files.append(path)
    return sorted(set(files))


def detect_hardcoded_hits(files: list[Path]) -> dict[Path, list[tuple[int, str]]]:
    out: dict[Path, list[tuple[int, str]]] = defaultdict(list)
    for path in files:
        try:
            lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
        except OSError:
            continue
        for idx, line in enumerate(lines, start=1):
            if hardcoded_root in line:
                out[path].append((idx, line.strip()))
    return out


scan_roots = gather_scan_roots(repo_root)
scan_files = script_files_under(scan_roots)
hardcoded_hits = detect_hardcoded_hits(scan_files)

print("[config-migrate] hardcoded-path inventory")
print(f"  roots_scanned: {len(scan_roots)}")
print(f"  scripts_scanned: {len(scan_files)}")
print(f"  files_with_hits: {len(hardcoded_hits)}")

if hardcoded_hits:
    for path in sorted(hardcoded_hits):
        rel = path.relative_to(repo_root)
        lines = hardcoded_hits[path]
        replacement = (
            "source config.sh + use ${REPO_ROOT}/..."
            if path.suffix == ".sh"
            else "from config import * + use REPO_ROOT / ..."
        )
        print(f"  - {rel} (hits={len(lines)})")
        print(f"    proposed: {replacement}")
        for line_no, snippet in lines[:3]:
            print(f"    line {line_no}: {snippet}")

BASH_SOURCE_LINE = 'source "$(dirname "${BASH_SOURCE}")/config.sh"'
BASH_PREFLIGHT_LINE = 'sync_config_preflight "$(basename "${BASH_SOURCE[0]}")"'


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
        if re.match(r"^\s*sync_config_preflight\b.*$", line):
            removed = True
            continue
        cleaned.append(line)
    lines = cleaned

    insert_idx = 1 if lines and lines[0].startswith("#!") else 0
    while insert_idx < len(lines) and lines[insert_idx].strip() == "":
        lines.pop(insert_idx)

    inject = BASH_SOURCE_LINE + "\n" + BASH_PREFLIGHT_LINE + "\n"
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

    root_pattern = hardcoded_root
    replacements = [
        (f'"{root_pattern}', '"${REPO_ROOT}'),
        (f"'{root_pattern}", "'${REPO_ROOT}"),
        (f"{root_pattern}/", "${REPO_ROOT}/"),
        (root_pattern, "${REPO_ROOT}"),
    ]
    for needle, repl in replacements:
        newer = out.replace(needle, repl)
        if newer != out:
            changed += 1
            out = newer

    for literal, var in mappings:
        before = out
        out = out.replace(f"${{REPO_ROOT}}/{literal}", f"${{{var}}}")
        out = out.replace(f"$REPO_ROOT/{literal}", f"${var}")
        out = out.replace(f'"{literal}', '"' + _bash_rel_expr(var))
        if out != before:
            changed += 1

    return out, changed


def _find_docstring_end(lines: list[str], start: int) -> int:
    line = lines[start].lstrip()
    if not (line.startswith('"""') or line.startswith("'''")):
        return start

    quote = '"""' if line.startswith('"""') else "'''"
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

    while idx < len(lines) and lines[idx].strip() == "":
        idx += 1

    if idx < len(lines):
        stripped = lines[idx].lstrip()
        if stripped.startswith('"""') or stripped.startswith("'''"):
            idx = _find_docstring_end(lines, idx)

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

    root_pattern = re.escape(hardcoded_root)
    newer = re.sub(rf"Path\((['\"]){root_pattern}\1\)", "REPO_ROOT", out)
    if newer != out:
        changed += 1
        out = newer

    path_with_rest = re.compile(rf"Path\((['\"]){root_pattern}(?P<rest>/[^\"']*)\1\)")

    def _path_rest_repl(match: re.Match[str]) -> str:
        rest = match.group("rest").lstrip("/")
        return f'REPO_ROOT / "{rest}"'

    newer = path_with_rest.sub(_path_rest_repl, out)
    if newer != out:
        changed += 1
        out = newer

    for literal, var in mappings:
        patt = re.compile(rf"REPO_ROOT\s*/\s*([\"']){re.escape(literal)}(?P<rest>/[^\"']*)?\1")

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
# File loop (migration scope: orchestration/00-ORCHESTRATION/scripts)
# ---------------------------------------------------------------------------
skip_reason = Counter()
changed_files: list[Path] = []
unchanged_files: list[Path] = []

for path in sorted(scripts_dir.iterdir()):
    if not path.is_file():
        continue

    suffix = path.suffix.lower()

    if suffix == ".md":
        skip_reason["markdown"] += 1
        continue

    if path.name in {"config.sh", "config.py", "config_migrate.sh", "config_health.sh"}:
        skip_reason["config-core"] += 1
        continue

    if suffix not in {".sh", ".py"}:
        skip_reason["non-script"] += 1
        continue

    original = path.read_text(errors="replace")
    updated = original

    if suffix == ".sh":
        if not has_bash_shebang(original):
            skip_reason["non-bash-shebang"] += 1
            continue
        updated, _ = inject_bash_source(updated)
        updated, _ = replace_bash_paths(updated)
    else:
        updated, _ = inject_python_import(updated)
        updated, _ = replace_python_paths(updated)

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

# Post-migration scaffold gate (always run).
validate = scripts_dir / "scaffold_validate.sh"
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

# Optional syntax verification for migrated script domains.
if verify:
    verify_roots = gather_scan_roots(repo_root)
    verify_files = script_files_under(verify_roots)
    print("[config-migrate] verify: syntax checks")
    print(f"  files: {len(verify_files)}")

    failures: list[str] = []
    for path in verify_files:
        if path.suffix == ".sh":
            chk = subprocess.run(["bash", "-n", str(path)], text=True, capture_output=True)
            if chk.returncode != 0:
                failures.append(f"bash -n failed: {path}\n{chk.stderr.strip()}")
        elif path.suffix == ".py":
            chk = subprocess.run(["python3", "-m", "py_compile", str(path)], text=True, capture_output=True)
            if chk.returncode != 0:
                failures.append(f"py_compile failed: {path}\n{chk.stderr.strip()}")

    if failures:
        print(f"[config-migrate] verify FAILED: {len(failures)} file(s)", file=sys.stderr)
        for item in failures[:20]:
            print(item, file=sys.stderr)
        sys.exit(1)

    print("[config-migrate] verify PASSED")
PY
