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
TOLERANCE_DOC = STATE_DIR / "COMMUNICATIONS-NAMING-TOLERANCES-v1.md"

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


@dataclass(frozen=True)
class Tolerance:
    lane: str
    path: str
    note: str
    rationale: str


TOLERANCES = [
    Tolerance(
        lane="prompts",
        path="communications/prompts/COWORK-PERPLEXITY-PROTOTYPE-PROMPT.md",
        note="filename does not match lane naming convention",
        rationale="intentional cowork lineage artifact name",
    ),
    Tolerance(
        lane="prompts",
        path="communications/prompts/PACKET-GROK-cc79-harness-aider.md",
        note="file lacks expected lane metadata markers",
        rationale="preserved raw-lineage harness packet",
    ),
    Tolerance(
        lane="prompts",
        path="communications/prompts/PACKET-GROK-cc79-harness-claude_code.md",
        note="file lacks expected lane metadata markers",
        rationale="preserved raw-lineage harness packet",
    ),
    Tolerance(
        lane="prompts",
        path="communications/prompts/PACKET-GROK-cc79-harness-codex.md",
        note="file lacks expected lane metadata markers",
        rationale="preserved raw-lineage harness packet",
    ),
    Tolerance(
        lane="prompts",
        path="communications/prompts/PACKET-GROK-cc79-harness-gemini_cli.md",
        note="file lacks expected lane metadata markers",
        rationale="preserved raw-lineage harness packet",
    ),
    Tolerance(
        lane="prompts",
        path="communications/prompts/PACKET-GROK-cc79-harness-openclaw.md",
        note="file lacks expected lane metadata markers",
        rationale="preserved raw-lineage harness packet",
    ),
    Tolerance(
        lane="prompts",
        path="communications/prompts/PACKET-GROK-cc79-harness-opencode.md",
        note="file lacks expected lane metadata markers",
        rationale="preserved raw-lineage harness packet",
    ),
    Tolerance(
        lane="prompts",
        path="communications/prompts/PACKET-GROK-cc79-harness-openhands.md",
        note="file lacks expected lane metadata markers",
        rationale="preserved raw-lineage harness packet",
    ),
    Tolerance(
        lane="responses",
        path="communications/responses/RESPONSE-GROK-cc79-harness-aider-raw.md",
        note="file lacks expected lane metadata markers",
        rationale="preserved raw response artifact",
    ),
    Tolerance(
        lane="responses",
        path="communications/responses/RESPONSE-GROK-cc79-harness-claude_code-raw.md",
        note="file lacks expected lane metadata markers",
        rationale="preserved raw response artifact",
    ),
    Tolerance(
        lane="responses",
        path="communications/responses/RESPONSE-GROK-cc79-harness-openhands-raw.md",
        note="file lacks expected lane metadata markers",
        rationale="preserved raw response artifact",
    ),
]
TOLERANCE_LOOKUP = {(item.path, item.note): item for item in TOLERANCES}


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


def split_tolerated(findings: list[Finding]) -> tuple[list[Finding], list[Tolerance]]:
    active: list[Finding] = []
    tolerated: list[Tolerance] = []
    for finding in findings:
        tolerance = TOLERANCE_LOOKUP.get((finding.path, finding.note))
        if tolerance:
            tolerated.append(tolerance)
        else:
            active.append(finding)
    return active, tolerated


def render_markdown(findings: list[Finding], tolerated: list[Tolerance]) -> str:
    lines = [
        "# Communications Naming Report",
        "",
        "Report-only scan for successor-shell communications naming and metadata drift.",
        "",
        "Active debt remains visible below; bounded naming tolerances are listed separately.",
        "",
        f"- active findings: `{len(findings)}`",
        f"- explicit tolerances: `{len(tolerated)}`",
        f"- tolerance source: [{TOLERANCE_DOC.name}]({TOLERANCE_DOC})",
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
    lines.append("## explicit tolerances")
    lines.append("")
    if not tolerated:
        lines.append("- none")
        lines.append("")
        return "\n".join(lines)

    tolerated_by_lane: dict[str, list[Tolerance]] = {}
    for item in tolerated:
        tolerated_by_lane.setdefault(item.lane, []).append(item)
    for lane in sorted(tolerated_by_lane):
        lines.append(f"### {lane}")
        lines.append("")
        for item in tolerated_by_lane[lane]:
            lines.append(f"- `{item.path}`: {item.note} ({item.rationale})")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true", help="Fail on warnings.")
    args = parser.parse_args()

    findings: list[Finding] = []
    for lane, config in RULES.items():
        findings.extend(scan_lane(lane, config))

    active_findings, tolerated_findings = split_tolerated(findings)

    JSON_OUT.write_text(json.dumps([asdict(item) for item in active_findings], indent=2) + "\n", encoding="utf-8")
    MD_OUT.write_text(render_markdown(active_findings, tolerated_findings), encoding="utf-8")

    errors = [item for item in active_findings if item.level == "error"]
    warnings = [item for item in active_findings if item.level == "warning"]

    if errors:
        for item in errors:
            print(f"ERROR: {item.path}: {item.note}")
        return 1
    if warnings and args.strict:
        for item in warnings:
            print(f"WARNING: {item.path}: {item.note}")
        return 1

    print(
        "Communications naming scan completed with "
        f"{len(warnings)} active warning(s) and {len(tolerated_findings)} tolerated finding(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
