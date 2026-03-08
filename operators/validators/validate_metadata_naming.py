#!/usr/bin/env python3
"""Report on communications-lane naming and lightweight metadata compliance."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
STATE_DIR = REPO_ROOT / "orchestration" / "state"
JSON_OUT = STATE_DIR / "COMMUNICATIONS-NAMING-REPORT.json"
MD_OUT = STATE_DIR / "COMMUNICATIONS-NAMING-REPORT.md"

RULES = {
    "prompts": {
        "pattern": re.compile(r"^(PACKET|PROMPT)-.+\.md$"),
        "content_tokens": ["## ", "**Priority**", "**Target"],
    },
    "responses": {
        "pattern": re.compile(r"^RESPONSE-.+\.md$"),
        "content_tokens": ["# ", "**Observed**", "**Response ID**", "**Date**"],
    },
    "handoffs": {
        "pattern": re.compile(r"^HANDOFF-.+\.md$"),
        "content_tokens": ["**Handoff ID**", "## Next Moves"],
    },
    "dispatches": {
        "pattern": re.compile(r"^(DISPATCH-.+|README)\.md$"),
        "content_tokens": ["# ", "**Date**", "**Dispatch"],
    },
    "logs": {
        "pattern": re.compile(r"^(LOG-.+|README)\.md$"),
        "content_tokens": ["# ", "**Date**", "## "],
    },
    "retros": {
        "pattern": re.compile(r"^(RETRO-.+|README)\.md$"),
        "content_tokens": ["# ", "## "],
    },
    "assessments": {
        "pattern": re.compile(r"^(ASSESSMENT-TEMPLATE|COMMUNICATIONS-MIGRATION-.+|.+ASSESSMENT.*)\.md$"),
        "content_tokens": ["# ", "## Verdict", "## What Is Strong", "## Adoptable Conclusions"],
    },
}


@dataclass
class Finding:
    level: str
    lane: str
    path: str
    note: str


def scan_lane(lane: str, config: dict[str, object]) -> list[Finding]:
    findings: list[Finding] = []
    lane_dir = REPO_ROOT / "communications" / lane
    if not lane_dir.exists():
        findings.append(Finding("error", lane, str(lane_dir.relative_to(REPO_ROOT)), "communications sublane missing"))
        return findings

    for path in sorted(lane_dir.glob("*.md")):
        rel = str(path.relative_to(REPO_ROOT))
        if not config["pattern"].match(path.name):
            findings.append(Finding("warning", lane, rel, "filename does not match lane naming convention"))
        text = path.read_text(encoding="utf-8")
        if not any(token in text for token in config["content_tokens"]):
            findings.append(Finding("warning", lane, rel, "file lacks expected lane metadata markers"))
    return findings


def render_markdown(findings: list[Finding]) -> str:
    lines = [
        "# Communications Naming Report",
        "",
        "Report-only scan for successor-shell communications naming and metadata drift.",
        "",
    ]
    by_lane: dict[str, list[Finding]] = {}
    for finding in findings:
        by_lane.setdefault(finding.lane, []).append(finding)
    for lane in sorted(RULES):
        lines.append(f"## {lane}")
        lines.append("")
        items = by_lane.get(lane, [])
        if not items:
            lines.append("- clean")
            lines.append("")
            continue
        for item in items:
            lines.append(f"- `{item.level}` `{item.path}`: {item.note}")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true", help="Fail on warnings.")
    args = parser.parse_args()

    findings: list[Finding] = []
    for lane, config in RULES.items():
        findings.extend(scan_lane(lane, config))

    JSON_OUT.write_text(json.dumps([asdict(item) for item in findings], indent=2) + "\n", encoding="utf-8")
    MD_OUT.write_text(render_markdown(findings), encoding="utf-8")

    errors = [item for item in findings if item.level == "error"]
    warnings = [item for item in findings if item.level == "warning"]

    if errors:
        for item in errors:
            print(f"ERROR: {item.path}: {item.note}")
        return 1
    if warnings and args.strict:
        for item in warnings:
            print(f"WARNING: {item.path}: {item.note}")
        return 1

    print(f"Communications naming scan completed with {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
