#!/usr/bin/env python3
"""Validate Acumen Feed Registry contract."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from registry_contract import policy_findings, policy_view, validate_registry


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
    policy_issues: list[str] = []
    policy_bound_channels = 0
    for channel in channels:
        policy = policy_view(channel)
        if policy["policy_fields_present"]:
            policy_bound_channels += 1
        policy_issues.extend(policy_findings(channel, require_explicit=args.strict))

    print("registry=valid")
    print(f"channels={len(channels)}")
    print(f"policy_bound_channels={policy_bound_channels}")

    if args.strict and policy_issues:
        print("strict_policy=invalid")
        for item in policy_issues:
            print(f"- {item}")
        return 2

    if policy_issues:
        print("policy_warnings=yes")
        for item in policy_issues:
            print(f"- {item}")

    if args.strict:
        for channel in channels:
            if channel.get("signal_density") == "low" and channel.get("priority_band") == "Tier 1":
                print("strict_policy=invalid")
                print(
                    "- low-density channel is still Tier 1 "
                    f"({channel.get('channel_id')}, {channel.get('name')})"
                )
                return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
