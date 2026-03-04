#!/usr/bin/env python3
"""Run deterministic smoke checks for currently promoted harness atoms."""

from __future__ import annotations

import argparse
import json
import subprocess
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_JSON = REPO_ROOT / "orchestration" / "state" / "HARNESS-PROMOTED-ATOMS-SMOKE.json"
DEFAULT_MD = REPO_ROOT / "orchestration" / "state" / "impl" / "HARNESS-PROMOTED-ATOMS-SMOKE.md"


@dataclass
class Probe:
    harness: str
    claim_command: str
    probe_command: list[str]
    expected_substring: str
    note: str


@dataclass
class ProbeResult:
    harness: str
    claim_command: str
    probe_command: str
    exit_code: int | None
    timed_out: bool
    pass_status: bool
    expected_substring: str
    observed_excerpt: str
    note: str


PROBES: list[Probe] = [
    Probe(
        harness="codex",
        claim_command="codex --help",
        probe_command=["codex", "--help"],
        expected_substring="Codex CLI",
        note="direct promoted atom",
    ),
    Probe(
        harness="codex",
        claim_command="codex apply --help",
        probe_command=["codex", "apply", "--help"],
        expected_substring="Usage: codex apply",
        note="direct promoted atom",
    ),
    Probe(
        harness="opencode",
        claim_command="opencode serve",
        probe_command=["opencode", "serve", "--help"],
        expected_substring="opencode serve",
        note="safe help-form probe for long-running serve command",
    ),
]


def run_probe(probe: Probe, timeout: float) -> ProbeResult:
    try:
        proc = subprocess.run(
            probe.probe_command,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
        output = (proc.stdout or "") + ("\n" + proc.stderr if proc.stderr else "")
        excerpt = "\n".join(output.strip().splitlines()[:12]).strip()
        passed = proc.returncode == 0 and probe.expected_substring in output
        return ProbeResult(
            harness=probe.harness,
            claim_command=probe.claim_command,
            probe_command=" ".join(probe.probe_command),
            exit_code=proc.returncode,
            timed_out=False,
            pass_status=passed,
            expected_substring=probe.expected_substring,
            observed_excerpt=excerpt,
            note=probe.note,
        )
    except subprocess.TimeoutExpired as exc:
        output = (exc.stdout or "") + ("\n" + exc.stderr if exc.stderr else "")
        excerpt = "\n".join(output.strip().splitlines()[:12]).strip()
        return ProbeResult(
            harness=probe.harness,
            claim_command=probe.claim_command,
            probe_command=" ".join(probe.probe_command),
            exit_code=None,
            timed_out=True,
            pass_status=False,
            expected_substring=probe.expected_substring,
            observed_excerpt=excerpt,
            note=probe.note,
        )


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def render_md(results: list[ProbeResult], out_path: Path) -> None:
    now = datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    passed = sum(1 for row in results if row.pass_status)
    failed = len(results) - passed
    lines = [
        "# Harness Promoted Atoms Smoke",
        "",
        f"**Generated**: {now}",
        "**Class**: promoted atom smoke verification",
        "",
        "## Summary",
        "",
        f"- probes: {len(results)}",
        f"- passed: {passed}",
        f"- failed: {failed}",
        "",
        "## Results",
        "",
        "| Harness | Claim Command | Probe Command | Exit | Pass | Note |",
        "|---|---|---|---:|---|---|",
    ]
    for row in results:
        exit_value = "timeout" if row.timed_out else str(row.exit_code)
        pass_value = "yes" if row.pass_status else "no"
        lines.append(
            "| "
            f"{row.harness} | `{row.claim_command}` | `{row.probe_command}` | {exit_value} | {pass_value} | {row.note} |"
        )
        lines.append("")
        lines.append(f"Expected: `{row.expected_substring}`")
        if row.observed_excerpt:
            lines.append("")
            lines.append("Observed excerpt:")
            lines.append("```text")
            lines.append(row.observed_excerpt)
            lines.append("```")
        lines.append("")

    write_text(out_path, "\n".join(lines).rstrip() + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--timeout", type=float, default=4.0)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    results = [run_probe(probe, args.timeout) for probe in PROBES]
    payload = {
        "generated_at": datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "probe_count": len(results),
        "pass_count": sum(1 for row in results if row.pass_status),
        "fail_count": sum(1 for row in results if not row.pass_status),
        "results": [asdict(row) for row in results],
    }

    write_text(args.json_out, json.dumps(payload, indent=2, ensure_ascii=True) + "\n")
    render_md(results, args.md_out)
    print(args.json_out)
    print(args.md_out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
