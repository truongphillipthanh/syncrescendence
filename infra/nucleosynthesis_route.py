#!/usr/bin/env python3
"""Nucleosynthesis routing script — moves corpus files into typed directories.

Usage:
    python3 nucleosynthesis_route.py --dry-run          # report routing decisions
    python3 nucleosynthesis_route.py --audit             # show unrouted files
    python3 nucleosynthesis_route.py --execute           # move files (creates dirs, writes undo script)
    python3 nucleosynthesis_route.py --stats             # summary counts per type

The routing table (routing_table.yaml) is the ONLY input that determines where files go.
This script is deliberately dumb — all intelligence lives in the YAML, not in the code.
"""

import argparse
import os
import shutil
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml")

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent  # corpus/ is one level under repo root
DEFAULT_TABLE = SCRIPT_DIR / "routing_table.yaml"


def load_routing_table(path: Path) -> dict:
    """Load and validate routing_table.yaml."""
    import re

    with open(path) as f:
        table = yaml.safe_load(f)

    if not table or "types" not in table:
        sys.exit(f"Invalid routing table: missing 'types' key in {path}")

    # Compile regex patterns
    for type_name, type_def in table["types"].items():
        compiled = []
        for pattern in type_def.get("patterns", []):
            try:
                compiled.append(re.compile(pattern))
            except re.error as e:
                sys.exit(f"Bad regex in type '{type_name}': {pattern!r} — {e}")
        type_def["_compiled"] = compiled

    return table


def route_file(filename: str, table: dict) -> str | None:
    """Return the type name a file routes to, or None if unrouted."""
    for type_name, type_def in table["types"].items():
        for regex in type_def.get("_compiled", []):
            if regex.search(filename):
                return type_name
    return None


def resolve_target_dir(type_name: str, type_def: dict, table: dict) -> Path:
    """Resolve the target directory for a given type."""
    target = type_def.get("target_dir", type_name)
    base = Path(table.get("target_base", str(REPO_ROOT)))
    return base / target


def run_dry_run(corpus_dir: Path, table: dict):
    """Report routing decisions without moving anything."""
    files = sorted(f for f in os.listdir(corpus_dir) if os.path.isfile(corpus_dir / f))
    routed = 0
    unrouted = 0

    for f in files:
        type_name = route_file(f, table)
        if type_name:
            target = resolve_target_dir(type_name, table["types"][type_name], table)
            print(f"  {type_name:12s} ← {f}")
            routed += 1
        else:
            unrouted += 1

    print(f"\n--- Dry Run Summary ---")
    print(f"Total files:  {len(files)}")
    print(f"Routed:       {routed}")
    print(f"Unrouted:     {unrouted}")


def run_audit(corpus_dir: Path, table: dict):
    """Show files that don't match any routing pattern."""
    files = sorted(f for f in os.listdir(corpus_dir) if os.path.isfile(corpus_dir / f))
    unrouted = []

    for f in files:
        if route_file(f, table) is None:
            unrouted.append(f)

    print(f"Unrouted files: {len(unrouted)} / {len(files)}")
    for f in unrouted:
        print(f"  ? {f}")


def run_stats(corpus_dir: Path, table: dict):
    """Summary counts per type."""
    files = [f for f in os.listdir(corpus_dir) if os.path.isfile(corpus_dir / f)]
    counts: dict[str, int] = {}
    unrouted = 0

    for f in files:
        type_name = route_file(f, table)
        if type_name:
            counts[type_name] = counts.get(type_name, 0) + 1
        else:
            unrouted += 1

    print(f"{'Type':15s} {'Count':>6s} {'%':>6s}")
    print("-" * 30)
    for t in sorted(counts, key=lambda k: -counts[k]):
        pct = 100.0 * counts[t] / len(files)
        print(f"{t:15s} {counts[t]:6d} {pct:5.1f}%")
    print("-" * 30)
    pct = 100.0 * unrouted / len(files) if files else 0
    print(f"{'UNROUTED':15s} {unrouted:6d} {pct:5.1f}%")
    print(f"{'TOTAL':15s} {len(files):6d}")


def run_execute(corpus_dir: Path, table: dict):
    """Move files according to routing table. Creates dirs, writes undo script."""
    files = sorted(f for f in os.listdir(corpus_dir) if os.path.isfile(corpus_dir / f))

    # Create required directories
    for dir_path in table.get("directories", []):
        p = Path(table.get("target_base", str(REPO_ROOT))) / dir_path
        p.mkdir(parents=True, exist_ok=True)

    undo_lines = ["#!/bin/bash", "# Undo script for nucleosynthesis routing", "set -e", ""]
    moved = 0
    collisions = 0
    skipped = 0

    for f in files:
        type_name = route_file(f, table)
        if not type_name:
            skipped += 1
            continue

        src = corpus_dir / f
        target_dir = resolve_target_dir(type_name, table["types"][type_name], table)
        target_dir.mkdir(parents=True, exist_ok=True)
        dst = target_dir / f

        if dst.exists():
            print(f"  COLLISION: {f} → {target_dir} (target exists)")
            collisions += 1
            continue

        shutil.move(str(src), str(dst))
        undo_lines.append(f'mv "{dst}" "{src}"')
        moved += 1

    # Write undo script
    undo_path = corpus_dir / "UNDO-NUCLEOSYNTHESIS.sh"
    with open(undo_path, "w") as out:
        out.write("\n".join(undo_lines) + "\n")
    os.chmod(undo_path, 0o755)

    print(f"\n--- Execution Summary ---")
    print(f"Moved:      {moved}")
    print(f"Collisions: {collisions}")
    print(f"Skipped:    {skipped} (unrouted)")
    print(f"Undo:       {undo_path}")


def main():
    parser = argparse.ArgumentParser(description="Nucleosynthesis corpus routing")
    parser.add_argument("--dry-run", action="store_true", help="Report routing decisions")
    parser.add_argument("--audit", action="store_true", help="Show unrouted files")
    parser.add_argument("--stats", action="store_true", help="Summary counts per type")
    parser.add_argument("--execute", action="store_true", help="Move files (destructive)")
    parser.add_argument("--table", type=Path, default=DEFAULT_TABLE, help="Routing table YAML")
    parser.add_argument("--corpus", type=Path, default=SCRIPT_DIR, help="Corpus directory")
    args = parser.parse_args()

    if not args.table.exists():
        sys.exit(f"Routing table not found: {args.table}\nCreate it first (see routing_table.yaml.example)")

    table = load_routing_table(args.table)

    if args.dry_run:
        run_dry_run(args.corpus, table)
    elif args.audit:
        run_audit(args.corpus, table)
    elif args.stats:
        run_stats(args.corpus, table)
    elif args.execute:
        print("WARNING: This will move files out of corpus/. Ctrl+C to abort.")
        run_execute(args.corpus, table)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
