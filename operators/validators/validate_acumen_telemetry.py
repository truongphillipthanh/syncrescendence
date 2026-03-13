#!/usr/bin/env python3
"""Validate the Acumen telemetry report against admitted source artifacts."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from operators.acumen.evidence_family import (  # noqa: E402
    TRAINING_LEDGER_PATH,
    TRIAGE_LEDGER_PATH,
    load_jsonl,
    repo_rel,
    scan_forbidden_content,
)


REPORT_JSON_PATH = REPO_ROOT / "orchestration" / "state" / "ACUMEN-TELEMETRY-REPORT.json"
REGISTRY_PATH = REPO_ROOT / "runtime" / "acumen" / "registry.json"
POLL_STATUS_PATH = REPO_ROOT / "runtime" / "acumen" / "poll-status.json"
TRIAGE_STATUS_PATH = REPO_ROOT / "runtime" / "acumen" / "triage-status.json"
BRIDGE_PATH = REPO_ROOT / "orchestration" / "state" / "ACUMEN-AUGUR-VERIFICATION-BRIDGE.json"
BRIDGE_REPORT_PATH = REPO_ROOT / "orchestration" / "state" / "ACUMEN-AUGUR-VERIFICATION-BRIDGE-REPORT.json"
LIVE_BATCH_PROOF_STATUS_PATH = REPO_ROOT / "orchestration" / "state" / "ACUMEN-LIVE-BATCH-PROOF-STATUS.json"
LIVE_BATCH_PROOF_REPORT_PATH = REPO_ROOT / "orchestration" / "state" / "ACUMEN-LIVE-BATCH-PROOF-REPORT.json"
FORBIDDEN_LEDGER_PATH = REPO_ROOT / "orchestration" / "state" / "registry" / "acumen-telemetry-ledger.jsonl"
ALLOWED_LABELS = {"observed", "estimated", "unavailable"}
ELIGIBLE_DECISIONS = {"Promote", "Flag-for-Primary"}


@dataclass(frozen=True)
class Finding:
    level: str
    scope: str
    message: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report-json", default=str(REPORT_JSON_PATH))
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


def require_datum(payload: Any, findings: list[Finding], scope: str) -> dict[str, Any] | None:
    if not isinstance(payload, dict):
        add_finding(findings, scope, "must be a datum object")
        return None
    label = payload.get("label")
    if label not in ALLOWED_LABELS:
        add_finding(findings, f"{scope}.label", f"must be one of {sorted(ALLOWED_LABELS)}")
    sources = payload.get("sources")
    if not isinstance(sources, list) or not all(isinstance(item, str) and item for item in sources):
        add_finding(findings, f"{scope}.sources", "must be a non-empty list of strings")
    if "value" not in payload:
        add_finding(findings, f"{scope}.value", "must be present")
    reason = payload.get("reason")
    if reason is not None and not isinstance(reason, str):
        add_finding(findings, f"{scope}.reason", "must be a string when present")
    return payload


def validate_nested_datums(payload: dict[str, Any], findings: list[Finding], scope: str) -> None:
    datum_obj = require_datum(payload, findings, scope)
    if datum_obj is None:
        return
    value = datum_obj.get("value")
    if isinstance(value, dict):
        for key, item in value.items():
            validate_nested_datums(item, findings, f"{scope}.value.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            if isinstance(item, dict):
                add_finding(findings, f"{scope}.value[{index}]", "lists must contain scalar items, not nested objects")


def datum_value(report: dict[str, Any], *path: str) -> Any:
    cursor: Any = report
    for part in path:
        if not isinstance(cursor, dict):
            return None
        cursor = cursor.get(part)
    if isinstance(cursor, dict) and "value" in cursor:
        return cursor.get("value")
    return None


def label_value(report: dict[str, Any], *path: str) -> Any:
    cursor: Any = report
    for part in path:
        if not isinstance(cursor, dict):
            return None
        cursor = cursor.get(part)
    if isinstance(cursor, dict) and "label" in cursor:
        return cursor.get("label")
    return None


def validate_counts(report: dict[str, Any], findings: list[Finding]) -> None:
    registry = load_json_object(REGISTRY_PATH, findings, "registry")
    poll_status = load_json_object(POLL_STATUS_PATH, findings, "poll_status")
    triage_status = load_json_object(TRIAGE_STATUS_PATH, findings, "triage_status")
    bridge = load_json_object(BRIDGE_PATH, findings, "bridge")
    bridge_report = load_json_object(BRIDGE_REPORT_PATH, findings, "bridge_report")
    live_batch_proof_status = load_json_object(LIVE_BATCH_PROOF_STATUS_PATH, findings, "live_batch_proof_status")
    live_batch_proof_report = load_json_object(LIVE_BATCH_PROOF_REPORT_PATH, findings, "live_batch_proof_report")
    if any(payload is None for payload in (registry, poll_status, triage_status, bridge, bridge_report, live_batch_proof_status, live_batch_proof_report)):
        return

    triage_events = load_jsonl(TRIAGE_LEDGER_PATH)
    training_events = load_jsonl(TRAINING_LEDGER_PATH)

    registry_channels = registry.get("channels", [])
    poll_channels = poll_status.get("channels", [])
    bridge_counts = bridge.get("counts", {})
    admitted_channel_ids = {
        str(channel.get("channel_id", "")).strip()
        for channel in registry_channels
        if isinstance(channel, dict) and str(channel.get("channel_id", "")).strip()
    }
    channels_in_registry_seen = sum(
        1
        for channel in poll_channels
        if isinstance(channel, dict) and str(channel.get("channel_id", "")).strip() in admitted_channel_ids
    )

    promotion_eligible = 0
    decision_mix: dict[str, int] = {}
    for event in triage_events:
        record = event.get("decision_record", {})
        if not isinstance(record, dict):
            continue
        decision = str(record.get("decision", "")).strip()
        if not decision:
            continue
        decision_mix[decision] = decision_mix.get(decision, 0) + 1
        if decision in ELIGIBLE_DECISIONS:
            promotion_eligible += 1

    expected_mix = [f"{decision}={count}" for decision, count in sorted(decision_mix.items())]
    actual_mix = datum_value(report, "triage_surface", "value", "decision_mix")
    if actual_mix != expected_mix:
        add_finding(findings, "report.triage_surface.value.decision_mix", f"expected {expected_mix!r}, got {actual_mix!r}")

    comparisons = [
        ("registry_surface.channels_total", datum_value(report, "registry_surface", "value", "channels_total"), len(admitted_channel_ids)),
        ("poll_surface.channels_total", datum_value(report, "poll_surface", "value", "channels_total"), poll_status.get("channels_total")),
        ("poll_surface.channels_in_registry_seen", datum_value(report, "poll_surface", "value", "channels_in_registry_seen"), channels_in_registry_seen),
        ("triage_surface.current_batch_processed", datum_value(report, "triage_surface", "value", "current_batch_processed"), triage_status.get("processed")),
        ("triage_surface.current_batch_training_records", datum_value(report, "triage_surface", "value", "current_batch_training_records"), triage_status.get("training_records")),
        ("triage_surface.cumulative_triage_events", datum_value(report, "triage_surface", "value", "cumulative_triage_events"), len(triage_events)),
        ("triage_surface.cumulative_training_events", datum_value(report, "triage_surface", "value", "cumulative_training_events"), len(training_events)),
        ("triage_surface.promotion_eligible_events", datum_value(report, "triage_surface", "value", "promotion_eligible_events"), promotion_eligible),
        ("verification_ready_surface.eligible_items_total", datum_value(report, "verification_ready_surface", "value", "eligible_items_total"), bridge_counts.get("eligible_items_total")),
        ("verification_ready_surface.awaiting_response", datum_value(report, "verification_ready_surface", "value", "awaiting_response"), bridge_counts.get("awaiting_response")),
        ("verification_ready_surface.bridge_validation_ok", datum_value(report, "verification_ready_surface", "value", "bridge_validation_ok"), bridge_report.get("ok")),
        ("cost_and_proof_surface.live_batch_proof_present", datum_value(report, "cost_and_proof_surface", "value", "live_batch_proof_present"), live_batch_proof_status.get("live_proof_present")),
        ("cost_and_proof_surface.latest_proof_outcome", datum_value(report, "cost_and_proof_surface", "value", "latest_proof_outcome"), live_batch_proof_status.get("latest_outcome")),
        ("cost_and_proof_surface.latest_failure_domain", datum_value(report, "cost_and_proof_surface", "value", "latest_failure_domain"), live_batch_proof_status.get("latest_failure_domain")),
        ("cost_and_proof_surface.latest_failure_code", datum_value(report, "cost_and_proof_surface", "value", "latest_failure_code"), live_batch_proof_status.get("latest_failure_code")),
        ("cost_and_proof_surface.proof_validator_findings", datum_value(report, "cost_and_proof_surface", "value", "proof_validator_findings"), len(live_batch_proof_report.get("findings", []))),
    ]
    for scope, actual, expected in comparisons:
        if actual != expected:
            add_finding(findings, f"report.{scope}", f"expected {expected!r}, got {actual!r}")


def main() -> int:
    args = parse_args()
    findings: list[Finding] = []
    report_path = Path(args.report_json).expanduser().resolve()
    report = load_json_object(report_path, findings, "report")
    if report is None:
        for finding in findings:
            print(f"[{finding.level}] {finding.scope}: {finding.message}")
        return 1

    for key, value in report.items():
        validate_nested_datums(value, findings, f"report.{key}")

    if datum_value(report, "schema_version") != "acumen.telemetry.report/v1":
        add_finding(findings, "report.schema_version", "must equal 'acumen.telemetry.report/v1'")

    if label_value(report, "five_account_constellation_surface") != "unavailable":
        add_finding(findings, "report.five_account_constellation_surface.label", "must remain unavailable until broader constellation telemetry is admitted")

    receipt_value = str(datum_value(report, "receipt") or "")
    if "registry-backed Acumen intake layer" not in receipt_value or "five-account constellation telemetry unavailable" not in receipt_value:
        add_finding(findings, "report.receipt.value", "must explicitly state the minimal admitted system boundary and unavailable constellation telemetry")

    if FORBIDDEN_LEDGER_PATH.exists():
        add_finding(findings, "telemetry_ledger", f"forbidden telemetry ledger exists: {repo_rel(FORBIDDEN_LEDGER_PATH)}")

    for message in scan_forbidden_content(report, scope="report"):
        add_finding(findings, "report", message)

    validate_counts(report, findings)

    if findings:
        for finding in findings:
            print(f"[{finding.level}] {finding.scope}: {finding.message}")
        return 1

    print(f"PASS {repo_rel(report_path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
