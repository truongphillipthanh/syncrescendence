#!/usr/bin/env python3
"""Probe Acumen Google-surface identity binding against canonical account."""

from __future__ import annotations

import argparse
import json
import subprocess
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


def utc_now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def run_command(command: list[str], timeout: float = 5.0) -> tuple[int | None, str, str, bool]:
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False,
            timeout=timeout,
        )
        return result.returncode, result.stdout, result.stderr, False
    except subprocess.TimeoutExpired as exc:
        return None, exc.stdout or "", exc.stderr or "", True


def active_gcloud_account() -> dict[str, Any]:
    code, stdout, stderr, timed_out = run_command(["gcloud", "auth", "list", "--format=json"], timeout=8.0)
    if timed_out:
        return {"available": True, "timed_out": True}
    if code != 0:
        return {"available": False, "error": (stderr or stdout).strip() or None}
    rows = json.loads(stdout or "[]")
    active = next((item for item in rows if item.get("status") == "ACTIVE"), None)
    return {
        "available": True,
        "active_account": active.get("account") if active else None,
        "accounts": [item.get("account") for item in rows],
    }


def keychain_value(service: str, account: str) -> dict[str, Any]:
    code, stdout, stderr, timed_out = run_command(
        ["security", "find-generic-password", "-s", service, "-a", account, "-w"],
        timeout=3.0,
    )
    if timed_out:
        return {"present": False, "timed_out": True}
    if code != 0:
        return {"present": False, "error": (stderr or stdout).strip() or None}
    return {"present": True, "value": stdout.strip()}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--binding", default="orchestration/state/ACUMEN-IDENTITY-BINDING-CC87.json")
    parser.add_argument("--output", default="orchestration/state/ACUMEN-IDENTITY-STATUS.json")
    parser.add_argument("--strict", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    binding_path = Path(args.binding).expanduser().resolve()
    binding = json.loads(binding_path.read_text(encoding="utf-8"))
    canonical = binding["google_surfaces"]["canonical_identity"]

    gcloud = active_gcloud_account()
    keychain = keychain_value("syncrescendence", "gcloud-account")

    mismatches: list[str] = []
    if gcloud.get("available") and gcloud.get("active_account"):
        if gcloud["active_account"] != canonical:
            mismatches.append(
                f"gcloud active account mismatch: {gcloud['active_account']} != {canonical}"
            )
    if keychain.get("present"):
        if keychain["value"] != canonical:
            mismatches.append(
                f"keychain gcloud-account mismatch: {keychain['value']} != {canonical}"
            )

    status = {
        "captured_at": utc_now(),
        "binding_file": str(binding_path),
        "canonical_identity": canonical,
        "gcloud": gcloud,
        "keychain": {
            "present": keychain.get("present", False),
            "matches_canonical": keychain.get("value") == canonical if keychain.get("present") else None,
        },
        "mismatches": mismatches,
        "ok": len(mismatches) == 0,
    }

    output_path = Path(args.output).expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(status, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(output_path)
    if mismatches:
        for item in mismatches:
            print(f"- {item}")
    if args.strict and mismatches:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
