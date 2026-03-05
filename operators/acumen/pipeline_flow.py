#!/usr/bin/env python3
"""Lightweight Acumen pipeline flow scaffold (sequential with optional Prefect import)."""

from __future__ import annotations

import argparse
import json
from datetime import UTC, datetime
from pathlib import Path
import subprocess

from build_dawn_brief import main as dawn_brief_main  # noqa: F401  # imported for lane linkage


def utc_now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", required=True)
    parser.add_argument("--queue", required=True, help="JSONL queue of triage decisions for compile stage.")
    parser.add_argument("--out", required=True, help="Output directory for compiled artifacts.")
    parser.add_argument("--status-json", default="orchestration/state/ACUMEN-PIPELINE-STATUS.json")
    parser.add_argument("--identity-binding", default="orchestration/state/ACUMEN-IDENTITY-BINDING-CC87.json")
    parser.add_argument("--strict-identity", action="store_true")
    return parser.parse_args()


def write_status(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_sequential(args: argparse.Namespace) -> dict:
    registry = Path(args.registry).expanduser().resolve()
    queue = Path(args.queue).expanduser().resolve()
    out = Path(args.out).expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)

    binding_path = Path(args.identity_binding).expanduser().resolve()
    binding = json.loads(binding_path.read_text(encoding="utf-8"))
    canonical = binding["google_surfaces"]["canonical_identity"]
    identity_status_path = Path(args.status_json).expanduser().resolve().parent / "ACUMEN-IDENTITY-STATUS.json"
    identity_probe = subprocess.run(
        [
            "python3",
            str(Path(__file__).resolve().parent / "identity_binding_probe.py"),
            "--binding",
            str(binding_path),
            "--output",
            str(identity_status_path),
        ]
        + (["--strict"] if args.strict_identity else []),
        capture_output=True,
        text=True,
        check=False,
    )
    identity_ok = False
    if identity_status_path.exists():
        try:
            identity_payload = json.loads(identity_status_path.read_text(encoding="utf-8"))
            identity_ok = bool(identity_payload.get("ok"))
        except Exception:
            identity_ok = False

    dawn_brief = out / f"DAWN-BRIEF-{datetime.now(UTC).strftime('%Y%m%d')}.md"
    cmd = [
        "python3",
        str(Path(__file__).resolve().parent / "build_dawn_brief.py"),
        "--input-jsonl",
        str(queue),
        "--output",
        str(dawn_brief),
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    return {
        "captured_at": utc_now(),
        "mode": "sequential",
        "registry_exists": registry.exists(),
        "queue_exists": queue.exists(),
        "canonical_identity": canonical,
        "identity_probe_success": identity_ok,
        "identity_probe_stdout": (identity_probe.stdout or "").strip()[:1200],
        "identity_probe_stderr": (identity_probe.stderr or "").strip()[:1200],
        "dawn_brief_path": str(dawn_brief),
        "dawn_brief_success": proc.returncode == 0,
        "stderr": (proc.stderr or "").strip()[:1200],
        "stdout": (proc.stdout or "").strip()[:1200],
    }


def main() -> int:
    args = parse_args()
    status = run_sequential(args)
    status_path = Path(args.status_json).expanduser().resolve()
    write_status(status_path, status)
    print(status_path)
    if not status["dawn_brief_success"]:
        return 1
    if args.strict_identity and not status["identity_probe_success"]:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
