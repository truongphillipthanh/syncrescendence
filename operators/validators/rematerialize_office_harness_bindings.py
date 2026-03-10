#!/usr/bin/env python3
"""Rematerialize effective office-harness bindings from the append-only ledger."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
AGENTS_PATH = REPO_ROOT / "AGENTS.md"
LEDGER_PATH = REPO_ROOT / "orchestration" / "state" / "registry" / "office-harness-binding-ledger.jsonl"
OUT_PATH = REPO_ROOT / "orchestration" / "state" / "registry" / "office-harness-bindings.effective.json"
LEDGER_SCHEMA_VERSION = "office-harness-binding-ledger-event/v1"
ALLOWED_EVENT_TYPES = {"binding_seeded", "binding_rebound"}


@dataclass(frozen=True)
class OfficeDefinition:
    office_id: str


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_section(text: str, heading: str) -> str:
    marker = f"## {heading}"
    start = text.find(marker)
    if start == -1:
        raise ValueError(f"missing section {heading!r} in AGENTS.md")
    remainder = text[start + len(marker) :]
    next_heading = remainder.find("\n## ")
    if next_heading == -1:
        return remainder.strip()
    return remainder[:next_heading].strip()


def parse_federal_offices(agents_text: str) -> list[OfficeDefinition]:
    section = extract_section(agents_text, "Federal Offices")
    offices: list[OfficeDefinition] = []
    for line in section.splitlines():
        line = line.strip()
        if not line.startswith("- `") or "`" not in line[3:]:
            continue
        office_title = line.split("`", 2)[1]
        offices.append(OfficeDefinition(office_id=office_title.lower()))
    if not offices:
        raise ValueError("no federal offices parsed from AGENTS.md")
    return offices


def parse_timestamp(value: Any, *, scope: str, errors: list[str]) -> datetime | None:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{scope} must be a non-empty timestamp string")
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        errors.append(f"{scope} must be ISO-8601 UTC, found {value!r}")
        return None


def require_string(mapping: dict[str, Any], key: str, *, scope: str, errors: list[str]) -> str | None:
    value = mapping.get(key)
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{scope}.{key} must be a non-empty string")
        return None
    return value.strip()


def require_optional_string(mapping: dict[str, Any], key: str, *, scope: str, errors: list[str]) -> str | None:
    value = mapping.get(key)
    if value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{scope}.{key} must be a string or null")
        return None
    return value.strip()


def require_positive_int(mapping: dict[str, Any], key: str, *, scope: str, errors: list[str]) -> int | None:
    value = mapping.get(key)
    if not isinstance(value, int) or value < 1:
        errors.append(f"{scope}.{key} must be a positive integer")
        return None
    return value


def require_mapping(mapping: dict[str, Any], key: str, *, scope: str, errors: list[str]) -> dict[str, Any] | None:
    value = mapping.get(key)
    if not isinstance(value, dict):
        errors.append(f"{scope}.{key} must be a JSON object")
        return None
    return value


def load_events(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise ValueError(f"ledger file missing: {path}")
    events: list[dict[str, Any]] = []
    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw_line.strip()
        if not line:
            continue
        try:
            parsed = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"ledger:{line_number} invalid JSON: {exc}") from exc
        if not isinstance(parsed, dict):
            raise ValueError(f"ledger:{line_number} must be a JSON object")
        events.append(parsed)
    return events


def rematerialize(events: list[dict[str, Any]], office_order: dict[str, int]) -> list[dict[str, Any]]:
    errors: list[str] = []
    latest: dict[str, tuple[int, datetime, str, dict[str, Any]]] = {}
    seen_versions: set[tuple[str, int]] = set()

    for line_number, event in enumerate(events, start=1):
        scope = f"ledger:{line_number}"
        schema_version = require_string(event, "schema_version", scope=scope, errors=errors)
        event_id = require_string(event, "event_id", scope=scope, errors=errors)
        event_type = require_string(event, "event_type", scope=scope, errors=errors)
        occurred_at = parse_timestamp(event.get("occurred_at"), scope=f"{scope}.occurred_at", errors=errors)
        require_string(event, "actor", scope=scope, errors=errors)
        office_id = require_string(event, "office_id", scope=scope, errors=errors)
        office_binding_version = require_positive_int(event, "office_binding_version", scope=scope, errors=errors)
        metadata_path = require_string(event, "metadata_path", scope=scope, errors=errors)
        binding_state_before = require_optional_string(event, "binding_state_before", scope=scope, errors=errors)
        binding_state_after = require_string(event, "binding_state_after", scope=scope, errors=errors)
        ratification_pointer = require_string(event, "ratification_pointer", scope=scope, errors=errors)
        ratified_by_artifact_path = require_string(event, "ratified_by_artifact_path", scope=scope, errors=errors)
        ratified_by_artifact_id = require_string(event, "ratified_by_artifact_id", scope=scope, errors=errors)
        ratified_at = require_string(event, "ratified_at", scope=scope, errors=errors)
        effective_record = require_mapping(event, "effective_record", scope=scope, errors=errors)

        if schema_version and schema_version != LEDGER_SCHEMA_VERSION:
            errors.append(
                f"{scope}.schema_version must be {LEDGER_SCHEMA_VERSION!r}, found {schema_version!r}"
            )
        if event_type and event_type not in ALLOWED_EVENT_TYPES:
            errors.append(f"{scope}.event_type must be one of {sorted(ALLOWED_EVENT_TYPES)!r}")

        if effective_record is None or office_id is None or office_binding_version is None:
            continue

        record_office_id = require_string(effective_record, "office_id", scope=f"{scope}.effective_record", errors=errors)
        record_metadata_path = require_string(
            effective_record,
            "metadata_path",
            scope=f"{scope}.effective_record",
            errors=errors,
        )
        record_binding_state = require_string(
            effective_record,
            "binding_state",
            scope=f"{scope}.effective_record",
            errors=errors,
        )
        record_pointer = require_string(
            effective_record,
            "ratification_pointer",
            scope=f"{scope}.effective_record",
            errors=errors,
        )
        record_artifact_path = require_string(
            effective_record,
            "ratified_by_artifact_path",
            scope=f"{scope}.effective_record",
            errors=errors,
        )
        record_artifact_id = require_string(
            effective_record,
            "ratified_by_artifact_id",
            scope=f"{scope}.effective_record",
            errors=errors,
        )
        record_ratifed_at = require_string(
            effective_record,
            "ratified_at",
            scope=f"{scope}.effective_record",
            errors=errors,
        )

        if office_id and record_office_id and office_id != record_office_id:
            errors.append(
                f"{scope}.effective_record.office_id {record_office_id!r} does not match event office_id {office_id!r}"
            )
        if metadata_path and record_metadata_path and metadata_path != record_metadata_path:
            errors.append(
                f"{scope}.effective_record.metadata_path {record_metadata_path!r} does not match event metadata_path {metadata_path!r}"
            )
        if binding_state_after and record_binding_state and binding_state_after != record_binding_state:
            errors.append(
                f"{scope}.effective_record.binding_state {record_binding_state!r} does not match event binding_state_after {binding_state_after!r}"
            )
        if ratification_pointer and record_pointer and ratification_pointer != record_pointer:
            errors.append(
                f"{scope}.effective_record.ratification_pointer {record_pointer!r} does not match event ratification_pointer {ratification_pointer!r}"
            )
        if ratified_by_artifact_path and record_artifact_path and ratified_by_artifact_path != record_artifact_path:
            errors.append(
                f"{scope}.effective_record.ratified_by_artifact_path does not match the event"
            )
        if ratified_by_artifact_id and record_artifact_id and ratified_by_artifact_id != record_artifact_id:
            errors.append(
                f"{scope}.effective_record.ratified_by_artifact_id does not match the event"
            )
        if ratified_at and record_ratifed_at and ratified_at != record_ratifed_at:
            errors.append(f"{scope}.effective_record.ratified_at does not match the event")

        version_key = (office_id, office_binding_version)
        if version_key in seen_versions:
            errors.append(
                f"{scope} duplicates office_binding_version {office_binding_version} for office {office_id!r}"
            )
            continue
        seen_versions.add(version_key)

        if occurred_at is None or event_id is None:
            continue

        current = latest.get(office_id)
        candidate = (office_binding_version, occurred_at, event_id, effective_record)
        if current is None or candidate[:3] > current[:3]:
            latest[office_id] = candidate

    if errors:
        raise ValueError("\n".join(errors))

    return [
        latest[office_id][3]
        for office_id in sorted(
            latest,
            key=lambda value: (office_order.get(value, len(office_order)), value),
        )
    ]


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ledger", type=Path, default=LEDGER_PATH)
    parser.add_argument("--out", type=Path, default=OUT_PATH)
    args = parser.parse_args()

    offices = parse_federal_offices(read_text(AGENTS_PATH))
    office_order = {office.office_id: index for index, office in enumerate(offices)}
    records = rematerialize(load_events(args.ledger), office_order)
    write_json(args.out, records)

    print(args.out)
    print(f"records={len(records)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
