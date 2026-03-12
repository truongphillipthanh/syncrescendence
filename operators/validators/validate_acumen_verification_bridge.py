#!/usr/bin/env python3
"""Validate the Acumen promoted-item dossier and Augur bridge artifacts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from operators.acumen.evidence_family import repo_rel, scan_forbidden_content


BRIDGE_SCHEMA_VERSION = "acumen.verification.bridge/v1"
DOSSIER_SCHEMA_VERSION = "acumen.verification.dossier/v1"
ELIGIBLE_DECISIONS = {"Promote", "Flag-for-Primary"}
STATE_DIR = REPO_ROOT / "orchestration" / "state"
DEFAULT_BRIDGE_JSON = STATE_DIR / "ACUMEN-AUGUR-VERIFICATION-BRIDGE.json"
DEFAULT_MD_REPORT = STATE_DIR / "ACUMEN-AUGUR-VERIFICATION-BRIDGE-REPORT.md"
DEFAULT_JSON_REPORT = STATE_DIR / "ACUMEN-AUGUR-VERIFICATION-BRIDGE-REPORT.json"
TIMESTAMP_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")


@dataclass(frozen=True)
class Finding:
    level: str
    scope: str
    message: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bridge-json", default=str(DEFAULT_BRIDGE_JSON))
    parser.add_argument("--output-md", default=str(DEFAULT_MD_REPORT))
    parser.add_argument("--output-json", default=str(DEFAULT_JSON_REPORT))
    return parser.parse_args()


def add_finding(findings: list[Finding], scope: str, message: str, *, level: str = "error") -> None:
    findings.append(Finding(level=level, scope=scope, message=message))


def load_json_object(path: Path, findings: list[Finding], scope: str) -> dict[str, Any] | None:
    if not path.exists():
        add_finding(findings, scope, f"missing file: {repo_rel(path)}")
        return None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        add_finding(findings, scope, f"invalid JSON: {exc}")
        return None
    if not isinstance(payload, dict):
        add_finding(findings, scope, "must be a JSON object")
        return None
    return payload


def resolve_repo_path(raw_value: str | None) -> Path | None:
    if raw_value is None or not str(raw_value).strip():
        return None
    candidate = Path(str(raw_value))
    if candidate.is_absolute():
        resolved = candidate.resolve()
    else:
        resolved = (REPO_ROOT / candidate).resolve()
    try:
        resolved.relative_to(REPO_ROOT)
    except ValueError:
        return None
    return resolved


def require_string(mapping: dict[str, Any], key: str, findings: list[Finding], scope: str) -> str | None:
    value = mapping.get(key)
    if not isinstance(value, str) or not value.strip():
        add_finding(findings, f"{scope}.{key}", "must be a non-empty string")
        return None
    return value.strip()


def require_mapping(mapping: dict[str, Any], key: str, findings: list[Finding], scope: str) -> dict[str, Any] | None:
    value = mapping.get(key)
    if not isinstance(value, dict):
        add_finding(findings, f"{scope}.{key}", "must be a JSON object")
        return None
    return value


def add_forbidden_findings(findings: list[Finding], payload: Any, scope: str) -> None:
    for message in scan_forbidden_content(payload, scope=scope):
        add_finding(findings, scope, message)


def validate_augur_packet(packet_path: Path, dossier_path: Path, response_path: str, findings: list[Finding], scope: str) -> None:
    if not packet_path.exists():
        add_finding(findings, scope, f"missing Augur packet: {repo_rel(packet_path)}")
        return
    if packet_path.suffix.lower() != ".md":
        add_finding(findings, scope, "Augur packet must be markdown")
        return
    body = packet_path.read_text(encoding="utf-8")
    required_snippets = [
        "Packet type: `acumen_verification_bridge`",
        repo_rel(dossier_path),
        response_path,
        "Acumen remains the intake and triage plane.",
        "Augur is downstream verification only.",
        "Drafting mode: `reconnaissance_only`",
    ]
    for snippet in required_snippets:
        if snippet not in body:
            add_finding(findings, scope, f"packet is missing required snippet: {snippet}")


def validate_dossier(dossier: dict[str, Any], dossier_path: Path, findings: list[Finding], scope: str) -> None:
    schema_version = require_string(dossier, "schema_version", findings, scope)
    generated_at = require_string(dossier, "generated_at", findings, scope)
    if schema_version and schema_version != DOSSIER_SCHEMA_VERSION:
        add_finding(findings, f"{scope}.schema_version", f"must equal {DOSSIER_SCHEMA_VERSION!r}")
    if generated_at and not TIMESTAMP_RE.fullmatch(generated_at):
        add_finding(findings, f"{scope}.generated_at", "must be ISO-8601 UTC")

    decision = require_mapping(dossier, "decision_metadata", findings, scope)
    source = require_mapping(dossier, "source_summary", findings, scope)
    source_packet = require_mapping(dossier, "source_packet", findings, scope)
    policy = require_mapping(dossier, "policy", findings, scope)
    paths = require_mapping(dossier, "paths", findings, scope)
    repo_sovereignty = require_mapping(dossier, "repo_sovereignty", findings, scope)

    if decision is not None:
        decision_value = require_string(decision, "decision", findings, f"{scope}.decision_metadata")
        require_string(decision, "triage_event_id", findings, f"{scope}.decision_metadata")
        require_string(decision, "title", findings, f"{scope}.decision_metadata")
        if decision_value and decision_value not in ELIGIBLE_DECISIONS:
            add_finding(findings, f"{scope}.decision_metadata.decision", "must be Promote or Flag-for-Primary")
    if source is not None:
        for key in ("title", "channel_name", "channel_id", "video_id", "input_summary"):
            require_string(source, key, findings, f"{scope}.source_summary")
    if source_packet is not None:
        packet_path_value = require_string(source_packet, "packet_path", findings, f"{scope}.source_packet")
        exists = source_packet.get("exists")
        if not isinstance(exists, bool):
            add_finding(findings, f"{scope}.source_packet.exists", "must be a boolean")
        packet_path = resolve_repo_path(packet_path_value)
        if packet_path is None:
            add_finding(findings, f"{scope}.source_packet.packet_path", "must resolve inside repo")
        elif exists and not packet_path.exists():
            add_finding(findings, f"{scope}.source_packet.packet_path", f"missing packet: {repo_rel(packet_path)}")
    if policy is not None:
        add_forbidden_findings(findings, policy, f"{scope}.policy")
    if repo_sovereignty is not None:
        for key in ("intake_authority", "external_role", "repo_state_rule"):
            require_string(repo_sovereignty, key, findings, f"{scope}.repo_sovereignty")
    if paths is not None:
        dossier_path_value = require_string(paths, "dossier_path", findings, f"{scope}.paths")
        source_packet_path = require_string(paths, "source_packet_path", findings, f"{scope}.paths")
        augur_packet_path_value = require_string(paths, "augur_packet_path", findings, f"{scope}.paths")
        augur_response_path = require_string(paths, "augur_response_path", findings, f"{scope}.paths")
        require_string(paths, "triage_ledger_path", findings, f"{scope}.paths")
        require_string(paths, "training_ledger_path", findings, f"{scope}.paths")

        resolved_dossier = resolve_repo_path(dossier_path_value)
        if resolved_dossier is None or resolved_dossier != dossier_path:
            add_finding(findings, f"{scope}.paths.dossier_path", "must point to the current dossier file")
        if resolve_repo_path(source_packet_path) is None:
            add_finding(findings, f"{scope}.paths.source_packet_path", "must resolve inside repo")
        augur_packet_path = resolve_repo_path(augur_packet_path_value)
        if augur_packet_path is None:
            add_finding(findings, f"{scope}.paths.augur_packet_path", "must resolve inside repo")
        elif augur_response_path is not None:
            validate_augur_packet(augur_packet_path, dossier_path, augur_response_path, findings, f"{scope}.paths.augur_packet_path")

    add_forbidden_findings(findings, dossier, scope)


def render_markdown_report(report: dict[str, Any]) -> str:
    lines = [
        "# Acumen Augur Verification Bridge Report",
        "",
        f"- Bridge JSON: `{report['bridge_json']}`",
        f"- Checked at: `{report['checked_at']}`",
        f"- OK: `{str(report['ok']).lower()}`",
        f"- Items: `{report['items_checked']}`",
        f"- Findings: `{len(report['findings'])}`",
        "",
        "## Findings",
        "",
    ]
    if report["findings"]:
        for finding in report["findings"]:
            lines.append(f"- [{finding['level']}] `{finding['scope']}` {finding['message']}")
    else:
        lines.append("- no findings")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    bridge_path = Path(args.bridge_json).expanduser().resolve()
    output_md = Path(args.output_md).expanduser().resolve()
    output_json = Path(args.output_json).expanduser().resolve()

    findings: list[Finding] = []
    bridge = load_json_object(bridge_path, findings, "bridge")
    items_checked = 0

    if bridge is not None:
        schema_version = require_string(bridge, "schema_version", findings, "bridge")
        generated_at = require_string(bridge, "generated_at", findings, "bridge")
        if schema_version and schema_version != BRIDGE_SCHEMA_VERSION:
            add_finding(findings, "bridge.schema_version", f"must equal {BRIDGE_SCHEMA_VERSION!r}")
        if generated_at and not TIMESTAMP_RE.fullmatch(generated_at):
            add_finding(findings, "bridge.generated_at", "must be ISO-8601 UTC")

        items = bridge.get("items")
        if not isinstance(items, list):
            add_finding(findings, "bridge.items", "must be a list")
            items = []

        for index, item in enumerate(items):
            scope = f"bridge.items[{index}]"
            if not isinstance(item, dict):
                add_finding(findings, scope, "must be an object")
                continue
            decision = require_string(item, "decision", findings, scope)
            dossier_path_value = require_string(item, "dossier_path", findings, scope)
            require_string(item, "augur_packet_path", findings, scope)
            require_string(item, "augur_response_path", findings, scope)
            if decision and decision not in ELIGIBLE_DECISIONS:
                add_finding(findings, f"{scope}.decision", "must be Promote or Flag-for-Primary")
            dossier_path = resolve_repo_path(dossier_path_value)
            if dossier_path is None:
                add_finding(findings, f"{scope}.dossier_path", "must resolve inside repo")
                continue
            dossier = load_json_object(dossier_path, findings, f"{scope}.dossier")
            if dossier is None:
                continue
            items_checked += 1
            validate_dossier(dossier, dossier_path, findings, f"{scope}.dossier")
            add_forbidden_findings(findings, item, scope)

        add_forbidden_findings(findings, bridge, "bridge")

    report = {
        "bridge_json": repo_rel(bridge_path) if bridge_path.exists() else str(bridge_path),
        "checked_at": datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "ok": not any(finding.level == "error" for finding in findings),
        "items_checked": items_checked,
        "findings": [asdict(finding) for finding in findings],
    }
    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    output_md.parent.mkdir(parents=True, exist_ok=True)
    output_md.write_text(render_markdown_report(report), encoding="utf-8")

    print(repo_rel(output_json))
    print(repo_rel(output_md))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
