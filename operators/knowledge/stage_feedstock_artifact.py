#!/usr/bin/env python3
"""Stage a new research artifact into the live knowledge feedstock lane."""

from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
INBOX_DIR = REPO_ROOT / "knowledge" / "feedstock" / "inbox"
RECEIPTS_DIR = REPO_ROOT / "knowledge" / "feedstock" / "receipts"


def slugify(value: str) -> str:
    return "-".join(
        piece for piece in "".join(ch.lower() if ch.isalnum() else "-" for ch in value).split("-") if piece
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--label", required=True)
    parser.add_argument("--reason", required=True)
    args = parser.parse_args()

    source = Path(args.source).expanduser().resolve()
    if not source.exists() or not source.is_file():
        raise SystemExit(f"source file not found: {source}")

    stamp = datetime.now(timezone.utc).strftime("%Y%m%d")
    receipt_stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    slug = slugify(source.stem)
    dest_name = f"{stamp}-{slug}{source.suffix.lower()}"

    INBOX_DIR.mkdir(parents=True, exist_ok=True)
    RECEIPTS_DIR.mkdir(parents=True, exist_ok=True)

    destination = INBOX_DIR / dest_name
    if destination.exists():
        raise SystemExit(f"destination already exists: {destination}")

    shutil.copy2(source, destination)

    receipt = {
        "label": args.label,
        "reason": args.reason,
        "source": str(source),
        "destination": str(destination),
        "timestamp": receipt_stamp,
        "mode": "feedstock-stage",
    }
    receipt_path = RECEIPTS_DIR / f"{args.label}-{receipt_stamp}.json"
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n")
    print(destination)
    print(receipt_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
