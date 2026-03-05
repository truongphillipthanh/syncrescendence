#!/usr/bin/env python3
"""Validate Acumen Feed Registry contract."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from registry_contract import validate_registry


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", default="runtime/acumen/registry.json")
    parser.add_argument("--strict", action="store_true", help="Fail on warnings and errors.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    path = Path(args.registry).expanduser().resolve()
    if not path.exists():
        raise SystemExit(f"registry missing: {path}")
    payload = json.loads(path.read_text(encoding="utf-8"))

    errors = validate_registry(payload)
    if errors:
        print("registry=invalid")
        for item in errors:
            print(f"- {item}")
        return 1

    channels = payload.get("channels", [])
    print("registry=valid")
    print(f"channels={len(channels)}")
    if args.strict:
        for channel in channels:
            if channel.get("signal_density") == "low" and channel.get("priority_band") == "Tier 1":
                print(
                    "strict_warning: low-density channel is still Tier 1 "
                    f"({channel.get('channel_id')}, {channel.get('name')})"
                )
                return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
