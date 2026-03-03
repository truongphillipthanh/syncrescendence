#!/usr/bin/env python3
"""Copy an archived artifact into the canonical shell with a provenance receipt."""

from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime, UTC
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
RECEIPTS = REPO_ROOT / "pedigree" / "rehousing-receipts"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--dest-rel", required=True, help="Path relative to repo root")
    parser.add_argument("--reason", required=True)
    parser.add_argument("--label", required=True)
    args = parser.parse_args()

    source = Path(args.source).expanduser().resolve()
    if not source.is_file():
        raise SystemExit(f"source file not found: {source}")

    dest = (REPO_ROOT / args.dest_rel).resolve()
    if REPO_ROOT not in dest.parents and dest != REPO_ROOT:
        raise SystemExit("destination must remain inside the canonical repo")
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, dest)

    RECEIPTS.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    receipt_path = RECEIPTS / f"{args.label}-{stamp}.json"
    receipt = {
        "label": args.label,
        "source": str(source),
        "destination": str(dest),
        "dest_rel": args.dest_rel,
        "reason": args.reason,
        "timestamp_utc": stamp,
    }
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n")
    print(dest)
    print(receipt_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
