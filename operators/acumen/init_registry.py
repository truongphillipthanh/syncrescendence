#!/usr/bin/env python3
"""Initialize or merge an Acumen Feed Registry from seed channel metadata."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from registry_contract import default_channel, utc_now, validate_registry


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def index_by_channel_id(channels: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    table: dict[str, dict[str, Any]] = {}
    for channel in channels:
        table[str(channel["channel_id"])] = channel
    return table


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", required=True, help="JSON list of channel seeds.")
    parser.add_argument("--output", default="runtime/acumen/registry.json")
    parser.add_argument("--merge", action="store_true", help="Merge with existing output if present.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    seed_path = Path(args.seed).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()

    seed_rows = load_json(seed_path)
    if not isinstance(seed_rows, list):
        raise SystemExit("seed must be a JSON array")
    normalized = [default_channel(row) for row in seed_rows]

    channels = normalized
    if args.merge and output_path.exists():
        current = load_json(output_path)
        current_channels = current.get("channels", [])
        merged = index_by_channel_id(current_channels)
        for row in normalized:
            merged[str(row["channel_id"])] = row
        channels = sorted(merged.values(), key=lambda item: item["name"].lower())

    registry = {
        "generated_at": utc_now(),
        "source_seed": str(seed_path),
        "channels": channels,
    }
    errors = validate_registry(registry)
    if errors:
        raise SystemExit("registry validation failed:\n- " + "\n- ".join(errors))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(registry, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(output_path)
    print(f"channels={len(channels)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
