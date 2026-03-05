#!/usr/bin/env python3
"""Compile Dawn Brief markdown from triage decision records."""

from __future__ import annotations

import argparse
import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


def utc_day() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%d")


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        payload = json.loads(line)
        if isinstance(payload, dict):
            rows.append(payload)
    return rows


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-jsonl", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--date", default=utc_day())
    return parser.parse_args()


def sort_key(item: dict[str, Any]) -> tuple[int, str]:
    band = str(item.get("priority_band", "Tier 3"))
    order = {"Tier 1": 0, "Tier 2": 1, "Tier 3": 2}
    return (order.get(band, 3), str(item.get("channel_name", "")))


def main() -> int:
    args = parse_args()
    path = Path(args.input_jsonl).expanduser().resolve()
    rows = load_jsonl(path)

    promoted = sorted([r for r in rows if r.get("decision") in {"Promote", "Flag-for-Primary"}], key=sort_key)
    compressed = sorted([r for r in rows if r.get("decision") in {"Compress", "Headline"}], key=sort_key)
    flagged = [r for r in rows if r.get("decision") == "Flag-for-Primary"]

    synthesis = "No cross-domain synthesis computed."
    if len(promoted) >= 2:
        a = promoted[0]
        b = promoted[1]
        synthesis = (
            f"{a.get('channel_name','Unknown')} and {b.get('channel_name','Unknown')} converged on "
            f"{a.get('domain_tags','adjacent themes')} with high triage confidence."
        )

    lines = [
        f"# Dawn Brief | {args.date}",
        "",
        "## Synthesis Alert",
        synthesis,
        "",
        "## Tactical Awareness (Promoted)",
    ]
    if not promoted:
        lines.append("- none")
    for item in promoted:
        lines.extend(
            [
                f"**[{item.get('channel_name','Unknown')}] {item.get('title','Untitled')}**",
                str(item.get("abstract", item.get("rationale", ""))).strip(),
                f"*Why promoted: {item.get('rationale','n/a')}*",
                f"*Suggested consumption: {item.get('suggested_consumption','Layer 2 / Digest')}*",
                "",
            ]
        )

    lines.extend(["## Peripheral Radar (Compressed)", ""])
    if not compressed:
        lines.append("- none")
    for item in compressed[:12]:
        lines.append(f"- **[{item.get('channel_name','Unknown')}]** {item.get('title','Untitled')}")

    lines.extend(["", "## Primary Source Flags", ""])
    if not flagged:
        lines.append("- none")
    for item in flagged:
        lines.extend(
            [
                f"- **[{item.get('channel_name','Unknown')}]** {item.get('title','Untitled')}",
                f"  *Why this cannot be compressed: {item.get('primary_flag_reason','n/a')}*",
            ]
        )

    lines.extend(
        [
            "",
            "## Pipeline Health",
            "",
            f"{len(rows)} ingested / {len(compressed)} compressed / {len(promoted)} promoted / {len(flagged)} flagged.",
        ]
    )

    output_path = Path(args.output).expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
