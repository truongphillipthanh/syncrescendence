#!/usr/bin/env python3
"""Render effective harness capability registry from base + external overrides."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_BASE = REPO_ROOT / "orchestration" / "state" / "HARNESS-CAPABILITY-REGISTRY-CC79.json"
DEFAULT_OVERRIDES = (
    REPO_ROOT / "orchestration" / "state" / "HARNESS-CAPABILITY-REGISTRY-CC79-EXTERNAL-OVERRIDES.json"
)
DEFAULT_EFFECTIVE_JSON = (
    REPO_ROOT / "orchestration" / "state" / "HARNESS-CAPABILITY-REGISTRY-CC79-EFFECTIVE.json"
)
DEFAULT_EFFECTIVE_MD = (
    REPO_ROOT / "orchestration" / "state" / "impl" / "HARNESS-CAPABILITY-REGISTRY-CC79-EFFECTIVE.md"
)
DEFAULT_PROMOTION_MD = (
    REPO_ROOT / "orchestration" / "state" / "impl" / "HARNESS-PROMOTION-CANDIDATES-CC79-EFFECTIVE.md"
)


def load_json(path: Path) -> list[dict[str, object]]:
    return json.loads(path.read_text(encoding="utf-8"))


def key_for(record: dict[str, object]) -> tuple[str, str]:
    return (
        str(record.get("harness", "")).strip(),
        str(record.get("command", "")).strip(),
    )


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def render_registry_md(
    *,
    records: list[dict[str, object]],
    overrides_applied: list[dict[str, object]],
    out_path: Path,
) -> None:
    tier_counts: dict[str, int] = {}
    status_counts: dict[str, int] = {}
    for row in records:
        tier = str(row.get("tier", ""))
        status = str(row.get("status", ""))
        tier_counts[tier] = tier_counts.get(tier, 0) + 1
        status_counts[status] = status_counts.get(status, 0) + 1

    lines = [
        "# Harness Capability Registry CC79 Effective",
        "",
        "**Class**: effective capability registry",
        "**Method**: base registry with external override precedence",
        "",
        "## Counts",
        "",
        f"- records: {len(records)}",
        f"- overrides applied: {len(overrides_applied)}",
        f"- T0: {tier_counts.get('T0', 0)}",
        f"- T1: {tier_counts.get('T1', 0)}",
        f"- T2: {tier_counts.get('T2', 0)}",
        f"- T3: {tier_counts.get('T3', 0)}",
        "",
        "## Status Distribution",
        "",
    ]
    for status in sorted(status_counts):
        lines.append(f"- `{status}`: {status_counts[status]}")
    lines.extend(["", "## Applied Overrides", ""])
    if not overrides_applied:
        lines.append("- none")
    else:
        for row in sorted(overrides_applied, key=lambda r: (str(r.get("harness", "")), str(r.get("command", "")))):
            lines.append(
                f"- `{row.get('harness')}` | `{row.get('command')}` -> `{row.get('status')}` `{row.get('tier')}`"
            )

    lines.extend(["", "## Effective Registry", "", "| Harness | Tier | Status | Command | Source | Detail |", "|---|---|---|---|---|---|"])
    for row in sorted(records, key=lambda r: (str(r.get("harness", "")), str(r.get("tier", "")), str(r.get("status", "")), str(r.get("command", "")))):
        harness = str(row.get("harness", "")).replace("|", "\\|")
        tier = str(row.get("tier", "")).replace("|", "\\|")
        status = str(row.get("status", "")).replace("|", "\\|")
        command = str(row.get("command", "")).replace("|", "\\|")
        source = str(row.get("source", row.get("source_file", ""))).replace("|", "\\|")
        detail = str(row.get("detail", "")).replace("|", "\\|")
        lines.append(f"| {harness} | {tier} | {status} | `{command}` | `{source}` | {detail} |")

    write_text(out_path, "\n".join(lines).rstrip() + "\n")


def render_promotion_md(*, records: list[dict[str, object]], out_path: Path) -> None:
    primary_bin = {
        "aider": "aider ",
        "claude_code": "claude ",
        "codex": "codex ",
        "gemini_cli": "gemini ",
        "openclaw": "openclaw ",
        "opencode": "opencode ",
        "openhands": "openhands ",
    }
    grouped: dict[str, list[str]] = {}
    for row in records:
        harness = str(row.get("harness", ""))
        command = str(row.get("command", ""))
        tier = str(row.get("tier", ""))
        status = str(row.get("status", ""))
        if tier not in ("T0", "T1"):
            continue
        if status != "probe_pass":
            continue
        prefix = primary_bin.get(harness)
        if prefix and not command.startswith(prefix):
            continue
        grouped.setdefault(harness, [])
        if command not in grouped[harness]:
            grouped[harness].append(command)

    lines = [
        "# Harness Promotion Candidates CC79 Effective",
        "",
        "**Class**: promotion queue",
        "**Rule**: effective registry only; `T0/T1` + `probe_pass` required",
        "",
    ]
    for harness in sorted(primary_bin.keys()):
        lines.extend([f"## {harness}", ""])
        commands = sorted(grouped.get(harness, []))
        if not commands:
            lines.append("- no command-level candidates")
            lines.append("")
            continue
        lines.append("### Candidate Claims")
        lines.append("")
        for command in commands:
            lines.append(f"- `{command}`")
        lines.extend(
            [
                "",
                "### Promotion Rule",
                "",
                "- add playbook atom first",
                "- promote operator only if command is deterministic and non-interactive",
                "",
            ]
        )

    write_text(out_path, "\n".join(lines).rstrip() + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", type=Path, default=DEFAULT_BASE)
    parser.add_argument("--overrides", type=Path, default=DEFAULT_OVERRIDES)
    parser.add_argument("--effective-json", type=Path, default=DEFAULT_EFFECTIVE_JSON)
    parser.add_argument("--effective-md", type=Path, default=DEFAULT_EFFECTIVE_MD)
    parser.add_argument("--promotion-md", type=Path, default=DEFAULT_PROMOTION_MD)
    args = parser.parse_args()

    base_rows = load_json(args.base)
    override_rows = load_json(args.overrides)

    keyed: dict[tuple[str, str], dict[str, object]] = {}
    for row in base_rows:
        row_copy = dict(row)
        row_copy["source"] = row_copy.get("source_file", "base_registry")
        keyed[key_for(row_copy)] = row_copy

    applied: list[dict[str, object]] = []
    for override in override_rows:
        k = key_for(override)
        if k in keyed:
            row = dict(keyed[k])
            row["status"] = override.get("status", row.get("status"))
            row["tier"] = override.get("tier", row.get("tier"))
            row["detail"] = override.get("detail", row.get("detail"))
            row["source"] = override.get("source", "external_override")
            keyed[k] = row
        else:
            keyed[k] = {
                "harness": override.get("harness"),
                "command": override.get("command"),
                "status": override.get("status"),
                "tier": override.get("tier"),
                "detail": override.get("detail"),
                "source": override.get("source", "external_override"),
            }
        applied.append(dict(override))

    effective_rows = sorted(
        keyed.values(),
        key=lambda r: (str(r.get("harness", "")), str(r.get("command", ""))),
    )

    write_text(args.effective_json, json.dumps(effective_rows, indent=2, ensure_ascii=True) + "\n")
    render_registry_md(records=effective_rows, overrides_applied=applied, out_path=args.effective_md)
    render_promotion_md(records=effective_rows, out_path=args.promotion_md)

    print(args.effective_json)
    print(args.effective_md)
    print(args.promotion_md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
