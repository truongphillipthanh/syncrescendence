#!/usr/bin/env python3
"""Build a minimal derivative Acumen telemetry report over the admitted inbound system."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

try:
    from .evidence_family import (
        REPO_ROOT,
        TRAINING_LEDGER_PATH,
        TRIAGE_LEDGER_PATH,
        load_jsonl,
        repo_rel,
        scan_forbidden_content,
        utc_now,
    )
except ImportError:
    OPS_DIR = Path(__file__).resolve().parents[1]
    if str(OPS_DIR) not in sys.path:
        sys.path.insert(0, str(OPS_DIR))
    from evidence_family import (  # type: ignore[no-redef]
        REPO_ROOT,
        TRAINING_LEDGER_PATH,
        TRIAGE_LEDGER_PATH,
        load_jsonl,
        repo_rel,
        scan_forbidden_content,
        utc_now,
    )


CONTRACT_PATH = REPO_ROOT / "orchestration" / "state" / "impl" / "ACUMEN-TELEMETRY-FAMILY-CONTRACT-v1.md"
PIPELINE_STATUS_PATH = REPO_ROOT / "orchestration" / "state" / "ACUMEN-PIPELINE-STATUS.json"
EVIDENCE_REPORT_PATH = REPO_ROOT / "orchestration" / "state" / "ACUMEN-TRIAGE-EVIDENCE-REPORT.json"
BRIDGE_PATH = REPO_ROOT / "orchestration" / "state" / "ACUMEN-AUGUR-VERIFICATION-BRIDGE.json"
BRIDGE_REPORT_PATH = REPO_ROOT / "orchestration" / "state" / "ACUMEN-AUGUR-VERIFICATION-BRIDGE-REPORT.json"
LIVE_BATCH_PROOF_STATUS_PATH = REPO_ROOT / "orchestration" / "state" / "ACUMEN-LIVE-BATCH-PROOF-STATUS.json"
LIVE_BATCH_PROOF_REPORT_PATH = REPO_ROOT / "orchestration" / "state" / "ACUMEN-LIVE-BATCH-PROOF-REPORT.json"
REGISTRY_PATH = REPO_ROOT / "runtime" / "acumen" / "registry.json"
POLL_STATUS_PATH = REPO_ROOT / "runtime" / "acumen" / "poll-status.json"
TRIAGE_STATUS_PATH = REPO_ROOT / "runtime" / "acumen" / "triage-status.json"
DEFAULT_OUTPUT_JSON = REPO_ROOT / "orchestration" / "state" / "ACUMEN-TELEMETRY-REPORT.json"
DEFAULT_OUTPUT_MD = REPO_ROOT / "orchestration" / "state" / "ACUMEN-TELEMETRY-REPORT.md"

ELIGIBLE_DECISIONS = {"Promote", "Flag-for-Primary"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-json", default=str(DEFAULT_OUTPUT_JSON))
    parser.add_argument("--output-md", default=str(DEFAULT_OUTPUT_MD))
    return parser.parse_args()


def load_json_object(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise SystemExit(f"{repo_rel(path)} must be a JSON object")
    return payload


def _repo_source(path: Path | str) -> str:
    if isinstance(path, Path):
        return repo_rel(path)
    candidate = Path(str(path))
    if candidate.is_absolute():
        return repo_rel(candidate.resolve())
    return str(path)


def datum(label: str, value: Any, *sources: Path | str, reason: str | None = None) -> dict[str, Any]:
    unique_sources: list[str] = []
    for source in sources:
        rendered = _repo_source(source)
        if rendered not in unique_sources:
            unique_sources.append(rendered)
    payload: dict[str, Any] = {
        "label": label,
        "value": value,
        "sources": unique_sources,
    }
    if reason is not None:
        payload["reason"] = reason
    return payload


def observed(value: Any, *sources: Path | str, reason: str | None = None) -> dict[str, Any]:
    return datum("observed", value, *sources, reason=reason)


def estimated(value: Any, *sources: Path | str, reason: str | None = None) -> dict[str, Any]:
    return datum("estimated", value, *sources, reason=reason)


def unavailable(*sources: Path | str, reason: str) -> dict[str, Any]:
    return datum("unavailable", None, *sources, reason=reason)


def safe_ratio(numerator: int, denominator: int) -> float | None:
    if denominator <= 0:
        return None
    return round(numerator / denominator, 4)


def build_report() -> dict[str, Any]:
    registry = load_json_object(REGISTRY_PATH)
    poll_status = load_json_object(POLL_STATUS_PATH)
    triage_status = load_json_object(TRIAGE_STATUS_PATH)
    pipeline_status = load_json_object(PIPELINE_STATUS_PATH)
    evidence_report = load_json_object(EVIDENCE_REPORT_PATH)
    bridge = load_json_object(BRIDGE_PATH)
    bridge_report = load_json_object(BRIDGE_REPORT_PATH)
    live_batch_proof_status = load_json_object(LIVE_BATCH_PROOF_STATUS_PATH)
    live_batch_proof_report = load_json_object(LIVE_BATCH_PROOF_REPORT_PATH)
    triage_events = load_jsonl(TRIAGE_LEDGER_PATH)
    training_events = load_jsonl(TRAINING_LEDGER_PATH)

    registry_channels = registry.get("channels", [])
    if not isinstance(registry_channels, list):
        raise SystemExit(f"{repo_rel(REGISTRY_PATH)}: channels must be a list")
    admitted_channel_ids = {
        str(channel.get("channel_id", "")).strip()
        for channel in registry_channels
        if isinstance(channel, dict) and str(channel.get("channel_id", "")).strip()
    }
    admitted_channel_names = [
        str(channel.get("name", "unknown"))
        for channel in registry_channels
        if isinstance(channel, dict)
    ]

    poll_channels = poll_status.get("channels", [])
    if not isinstance(poll_channels, list):
        raise SystemExit(f"{repo_rel(POLL_STATUS_PATH)}: channels must be a list")
    channels_in_registry_seen = sum(
        1
        for channel in poll_channels
        if isinstance(channel, dict) and str(channel.get("channel_id", "")).strip() in admitted_channel_ids
    )
    poll_channel_lines = []
    for channel in poll_channels:
        if not isinstance(channel, dict):
            continue
        poll_channel_lines.append(
            "{channel_id}:{name}:status={status}:mode={mode}:new={new_items}".format(
                channel_id=channel.get("channel_id", "unknown"),
                name=channel.get("channel_name", "unknown"),
                status=channel.get("status", "unknown"),
                mode=channel.get("source_mode", "unknown"),
                new_items=channel.get("new_items", "unknown"),
            )
        )

    triage_counter = Counter()
    promotion_eligible_events = 0
    for event in triage_events:
        record = event.get("decision_record", {})
        if not isinstance(record, dict):
            continue
        decision = str(record.get("decision", "")).strip()
        if not decision:
            continue
        triage_counter[decision] += 1
        if decision in ELIGIBLE_DECISIONS:
            promotion_eligible_events += 1

    training_provider_counter = Counter()
    training_model_counter = Counter()
    for event in training_events:
        record = event.get("training_record", {})
        if not isinstance(record, dict):
            continue
        provider = str(record.get("provider", "")).strip()
        model = str(record.get("model", "")).strip()
        if provider:
            training_provider_counter[provider] += 1
        if model:
            training_model_counter[model] += 1

    bridge_counts = bridge.get("counts", {})
    if not isinstance(bridge_counts, dict):
        bridge_counts = {}

    proof_gate = live_batch_proof_status.get("latest_proof_gate", {})
    if not isinstance(proof_gate, dict):
        proof_gate = {}

    report: dict[str, Any] = {
        "schema_version": observed("acumen.telemetry.report/v1", CONTRACT_PATH),
        "generated_at": observed(utc_now(), CONTRACT_PATH),
        "contract_path": observed(repo_rel(CONTRACT_PATH), CONTRACT_PATH),
        "derivative_boundary": observed(
            "Telemetry is derivative of admitted registry, poll, triage, evidence, bridge, and proof surfaces only.",
            CONTRACT_PATH,
            REGISTRY_PATH,
            POLL_STATUS_PATH,
            TRIAGE_STATUS_PATH,
            PIPELINE_STATUS_PATH,
            EVIDENCE_REPORT_PATH,
            BRIDGE_PATH,
            LIVE_BATCH_PROOF_STATUS_PATH,
        ),
        "receipt": observed(
            (
                "A real admitted inbound system is observable, but only at the current registry-backed Acumen intake layer. "
                "The broader admitted inbound system is still incomplete, so this family stays minimal and marks "
                "five-account constellation telemetry unavailable instead of fabricating authority."
            ),
            CONTRACT_PATH,
            REGISTRY_PATH,
            POLL_STATUS_PATH,
            TRIAGE_STATUS_PATH,
            PIPELINE_STATUS_PATH,
        ),
        "admitted_inbound_system": observed(
            {
                "system_kind": observed("registry_backed_acumen_youtube_intake", REGISTRY_PATH, POLL_STATUS_PATH),
                "real_system_observed": observed(
                    bool(admitted_channel_ids and channels_in_registry_seen > 0),
                    REGISTRY_PATH,
                    POLL_STATUS_PATH,
                ),
                "completeness": observed(
                    "minimal_registry_only",
                    REGISTRY_PATH,
                    POLL_STATUS_PATH,
                    TRIAGE_STATUS_PATH,
                    reason="Registry admission and traversal exist, but broader constellation admission is not part of this observed family.",
                ),
                "pipeline_profile": observed(
                    pipeline_status.get("execution_profile"),
                    PIPELINE_STATUS_PATH,
                ),
                "poll_mode": observed(
                    poll_status.get("mode"),
                    POLL_STATUS_PATH,
                ),
                "triage_mode": observed(
                    triage_status.get("mode"),
                    TRIAGE_STATUS_PATH,
                ),
                "broader_constellation_telemetry": unavailable(
                    CONTRACT_PATH,
                    reason="The five-account constellation/import spine is not part of the admitted observed input set for this report.",
                ),
            },
            CONTRACT_PATH,
            REGISTRY_PATH,
            POLL_STATUS_PATH,
            TRIAGE_STATUS_PATH,
            PIPELINE_STATUS_PATH,
        ),
        "registry_surface": observed(
            {
                "channels_total": observed(len(admitted_channel_ids), REGISTRY_PATH),
                "channel_names": observed(admitted_channel_names, REGISTRY_PATH),
                "generated_at": observed(registry.get("generated_at"), REGISTRY_PATH),
                "seed_source": observed(registry.get("source_seed"), REGISTRY_PATH),
            },
            REGISTRY_PATH,
        ),
        "poll_surface": observed(
            {
                "captured_at": observed(poll_status.get("captured_at"), POLL_STATUS_PATH),
                "channels_total": observed(poll_status.get("channels_total"), POLL_STATUS_PATH),
                "channels_in_registry_seen": observed(channels_in_registry_seen, REGISTRY_PATH, POLL_STATUS_PATH),
                "new_uploads": observed(poll_status.get("new_uploads"), POLL_STATUS_PATH),
                "failures": observed(poll_status.get("failures"), POLL_STATUS_PATH),
                "channel_status_lines": observed(poll_channel_lines, POLL_STATUS_PATH),
                "live_upstream_counts": unavailable(
                    POLL_STATUS_PATH,
                    reason="The committed poll snapshot is fixture-backed, so upstream live discovery counts are not directly observed here.",
                )
                if poll_status.get("mode") != "live"
                else observed(poll_status.get("new_uploads"), POLL_STATUS_PATH),
            },
            POLL_STATUS_PATH,
            REGISTRY_PATH,
        ),
        "triage_surface": observed(
            {
                "current_batch_processed": observed(triage_status.get("processed"), TRIAGE_STATUS_PATH),
                "current_batch_training_records": observed(triage_status.get("training_records"), TRIAGE_STATUS_PATH),
                "current_batch_skipped_existing": observed(triage_status.get("skipped_existing"), TRIAGE_STATUS_PATH),
                "current_batch_failures": observed(triage_status.get("failures"), TRIAGE_STATUS_PATH),
                "cumulative_triage_events": observed(len(triage_events), TRIAGE_LEDGER_PATH, EVIDENCE_REPORT_PATH),
                "cumulative_training_events": observed(len(training_events), TRAINING_LEDGER_PATH, EVIDENCE_REPORT_PATH),
                "decision_mix": observed(
                    [f"{decision}={count}" for decision, count in sorted(triage_counter.items())],
                    TRIAGE_LEDGER_PATH,
                ),
                "promotion_eligible_events": observed(promotion_eligible_events, TRIAGE_LEDGER_PATH),
                "promotion_eligible_ratio": observed(
                    safe_ratio(promotion_eligible_events, len(triage_events)),
                    TRIAGE_LEDGER_PATH,
                ),
                "evidence_status": observed(evidence_report.get("status"), EVIDENCE_REPORT_PATH),
                "evidence_findings": observed(len(evidence_report.get("findings", [])), EVIDENCE_REPORT_PATH),
            },
            TRIAGE_STATUS_PATH,
            TRIAGE_LEDGER_PATH,
            TRAINING_LEDGER_PATH,
            EVIDENCE_REPORT_PATH,
        ),
        "verification_ready_surface": observed(
            {
                "eligible_items_total": observed(bridge_counts.get("eligible_items_total"), BRIDGE_PATH),
                "selected_batch_items": observed(bridge_counts.get("selected_batch_items"), BRIDGE_PATH),
                "awaiting_response": observed(bridge_counts.get("awaiting_response"), BRIDGE_PATH),
                "dossiers_written": observed(bridge_counts.get("dossiers_written"), BRIDGE_PATH),
                "augur_packets_written": observed(bridge_counts.get("augur_packets_written"), BRIDGE_PATH),
                "verification_ready_ratio": observed(
                    safe_ratio(
                        int(bridge_counts.get("augur_packets_written") or 0),
                        int(bridge_counts.get("eligible_items_total") or 0),
                    ),
                    BRIDGE_PATH,
                ),
                "bridge_validation_ok": observed(bridge_report.get("ok"), BRIDGE_REPORT_PATH),
                "bridge_validation_findings": observed(len(bridge_report.get("findings", [])), BRIDGE_REPORT_PATH),
                "verification_complete_ratio": unavailable(
                    BRIDGE_PATH,
                    BRIDGE_REPORT_PATH,
                    reason="No ingested verification return is present in the current bridge state.",
                ),
            },
            BRIDGE_PATH,
            BRIDGE_REPORT_PATH,
        ),
        "cost_and_proof_surface": observed(
            {
                "provider_mix": observed(
                    [f"{provider}={count}" for provider, count in sorted(training_provider_counter.items())],
                    TRAINING_LEDGER_PATH,
                ),
                "model_mix": observed(
                    [f"{model}={count}" for model, count in sorted(training_model_counter.items())],
                    TRAINING_LEDGER_PATH,
                ),
                "gemini_calls_used": observed(
                    triage_status.get("external_dependencies", {}).get("gemini_api", {}).get("calls_used"),
                    TRIAGE_STATUS_PATH,
                ),
                "estimated_cost_usd": estimated(
                    triage_status.get("external_dependencies", {}).get("gemini_api", {}).get("estimated_cost_usd"),
                    TRIAGE_STATUS_PATH,
                    reason="The current cost surface is explicitly estimated, not provider-billed truth.",
                ),
                "estimated_cost_per_call_usd": estimated(
                    triage_status.get("external_dependencies", {}).get("gemini_api", {}).get("estimated_cost_per_call_usd"),
                    TRIAGE_STATUS_PATH,
                    reason="The current cost surface is explicitly estimated, not provider-billed truth.",
                ),
                "observed_provider_billing_usd": unavailable(
                    TRIAGE_STATUS_PATH,
                    LIVE_BATCH_PROOF_STATUS_PATH,
                    reason="No committed live provider billing evidence exists in the admitted observed system.",
                ),
                "live_batch_proof_present": observed(
                    live_batch_proof_status.get("live_proof_present"),
                    LIVE_BATCH_PROOF_STATUS_PATH,
                    LIVE_BATCH_PROOF_REPORT_PATH,
                ),
                "latest_proof_outcome": observed(
                    live_batch_proof_status.get("latest_outcome"),
                    LIVE_BATCH_PROOF_STATUS_PATH,
                ),
                "latest_failure_domain": observed(
                    live_batch_proof_status.get("latest_failure_domain"),
                    LIVE_BATCH_PROOF_STATUS_PATH,
                ),
                "latest_failure_code": observed(
                    live_batch_proof_status.get("latest_failure_code"),
                    LIVE_BATCH_PROOF_STATUS_PATH,
                ),
                "proof_gate_reason_code": observed(
                    proof_gate.get("reason_code"),
                    LIVE_BATCH_PROOF_STATUS_PATH,
                ),
                "proof_validator_findings": observed(
                    len(live_batch_proof_report.get("findings", [])),
                    LIVE_BATCH_PROOF_REPORT_PATH,
                ),
            },
            TRIAGE_STATUS_PATH,
            TRAINING_LEDGER_PATH,
            LIVE_BATCH_PROOF_STATUS_PATH,
            LIVE_BATCH_PROOF_REPORT_PATH,
        ),
        "five_account_constellation_surface": unavailable(
            CONTRACT_PATH,
            reason=(
                "Unavailable by design in this report. The family only observes the current registry-backed Acumen intake; "
                "five-account constellation/import telemetry remains outside the admitted observed boundary."
            ),
        ),
    }

    findings = scan_forbidden_content(report, scope="telemetry_report")
    if findings:
        raise SystemExit("; ".join(findings))
    return report


def summarize(datum_payload: dict[str, Any]) -> tuple[str, str, str | None]:
    label = str(datum_payload.get("label", "unknown"))
    value = datum_payload.get("value")
    reason = datum_payload.get("reason")
    if value is None:
        value_text = "n/a"
    elif isinstance(value, list):
        value_text = ", ".join(str(item) for item in value) if value else "[]"
    else:
        value_text = str(value)
    return label, value_text, str(reason) if reason is not None else None


def render_section(lines: list[str], heading: str, section: dict[str, Any]) -> None:
    lines.extend([f"## {heading}", ""])
    section_value = section.get("value", {})
    if not isinstance(section_value, dict):
        label, value_text, reason = summarize(section)
        lines.append(f"- `{heading}`: {label} | `{value_text}`")
        if reason:
            lines.append(f"  - {reason}")
        lines.append("")
        return
    for key, datum_payload in section_value.items():
        if not isinstance(datum_payload, dict):
            continue
        label, value_text, reason = summarize(datum_payload)
        label_text = key.replace("_", " ")
        lines.append(f"- `{label_text}`: {label} | `{value_text}`")
        if reason:
            lines.append(f"  - {reason}")
    lines.append("")


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# Acumen Telemetry Report",
        "",
        f"- Generated at: `{report['generated_at']['value']}`",
        f"- Contract: `{report['contract_path']['value']}`",
        f"- Receipt: {report['receipt']['value']}",
        "",
    ]
    render_section(lines, "Admitted Inbound System", report["admitted_inbound_system"])
    render_section(lines, "Registry Surface", report["registry_surface"])
    render_section(lines, "Poll Surface", report["poll_surface"])
    render_section(lines, "Triage Surface", report["triage_surface"])
    render_section(lines, "Verification-Ready Surface", report["verification_ready_surface"])
    render_section(lines, "Cost And Proof Surface", report["cost_and_proof_surface"])
    label, _, reason = summarize(report["five_account_constellation_surface"])
    lines.extend(
        [
            "## Five-Account Constellation Surface",
            "",
            f"- `constellation telemetry`: {label} | `n/a`",
            f"  - {reason}",
            "",
            "## Derivative Boundary",
            "",
            f"- {report['derivative_boundary']['value']}",
            "- No telemetry ledger is created by this family.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    output_json = Path(args.output_json).expanduser().resolve()
    output_md = Path(args.output_md).expanduser().resolve()

    report = build_report()
    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_md.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    output_md.write_text(render_markdown(report).rstrip() + "\n", encoding="utf-8")

    print(repo_rel(output_json))
    print(repo_rel(output_md))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
