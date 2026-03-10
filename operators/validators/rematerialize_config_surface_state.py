#!/usr/bin/env python3
"""Rematerialize config-surface current state from append-only ledger history."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
LEDGER_PATH = REPO_ROOT / "orchestration" / "state" / "registry" / "config-surface-state-ledger.jsonl"
REGISTRY_OUT = REPO_ROOT / "orchestration" / "state" / "registry" / "CONFIG-SURFACE-REGISTRY-v1.json"
MATRIX_OUT = REPO_ROOT / "orchestration" / "state" / "registry" / "CONFIG-SURFACE-PROJECTION-MATRIX-v1.json"

EXPECTED_FAMILY_ID = "config_surface_state"
EXPECTED_REGISTRY_ID = "config-surface-registry-v1"
EXPECTED_MATRIX_ID = "config-surface-projection-matrix-v1"
EXPECTED_REGISTRY_PATH = "orchestration/state/registry/CONFIG-SURFACE-REGISTRY-v1.json"
EXPECTED_MATRIX_PATH = "orchestration/state/registry/CONFIG-SURFACE-PROJECTION-MATRIX-v1.json"
LEDGER_SCHEMA_VERSION = "config-surface-state-ledger-event/v1"
ALLOWED_EVENT_TYPES = {"seed_receipt", "receipt_refresh", "drift_receipt", "supersession_receipt"}
SHA256_RE = re.compile(r"^sha256:[0-9a-f]{64}$")


@dataclass(frozen=True)
class MaterializedConfigState:
    config_state_version: int
    event_id: str
    registry: dict[str, Any]
    projection_matrix: dict[str, Any]


def canonical_json_text(payload: Any) -> str:
    return json.dumps(payload, indent=2, ensure_ascii=True) + "\n"


def canonical_json_bytes(payload: Any) -> bytes:
    return canonical_json_text(payload).encode("utf-8")


def sha256_for_payload(payload: Any) -> str:
    digest = hashlib.sha256()
    digest.update(canonical_json_bytes(payload))
    return f"sha256:{digest.hexdigest()}"


def joint_sha256(registry_sha256: str, matrix_sha256: str) -> str:
    digest = hashlib.sha256()
    digest.update(f"{registry_sha256}\n{matrix_sha256}\n".encode("utf-8"))
    return f"sha256:{digest.hexdigest()}"


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


def rematerialize(events: list[dict[str, Any]]) -> MaterializedConfigState:
    errors: list[str] = []
    latest: tuple[int, datetime, str, dict[str, Any], dict[str, Any]] | None = None
    seen_versions: set[int] = set()

    for line_number, event in enumerate(events, start=1):
        scope = f"ledger:{line_number}"
        event_id = require_string(event, "event_id", scope=scope, errors=errors)
        event_type = require_string(event, "event_type", scope=scope, errors=errors)
        recorded_at = parse_timestamp(event.get("recorded_at"), scope=f"{scope}.recorded_at", errors=errors)
        require_string(event, "actor", scope=scope, errors=errors)
        family_id = require_string(event, "family_id", scope=scope, errors=errors)
        registry_path = require_string(event, "registry_path", scope=scope, errors=errors)
        matrix_path = require_string(event, "projection_matrix_path", scope=scope, errors=errors)
        registry_sha256 = require_string(event, "registry_sha256", scope=scope, errors=errors)
        matrix_sha256 = require_string(event, "projection_matrix_sha256", scope=scope, errors=errors)
        combined_sha256 = require_string(event, "joint_sha256", scope=scope, errors=errors)

        if event_type and event_type not in ALLOWED_EVENT_TYPES:
            errors.append(f"{scope}.event_type must be one of {sorted(ALLOWED_EVENT_TYPES)!r}")
        if family_id and family_id != EXPECTED_FAMILY_ID:
            errors.append(f"{scope}.family_id must be {EXPECTED_FAMILY_ID!r}")
        if registry_path and registry_path != EXPECTED_REGISTRY_PATH:
            errors.append(f"{scope}.registry_path must be {EXPECTED_REGISTRY_PATH!r}")
        if matrix_path and matrix_path != EXPECTED_MATRIX_PATH:
            errors.append(f"{scope}.projection_matrix_path must be {EXPECTED_MATRIX_PATH!r}")
        for field_name, value in (
            ("registry_sha256", registry_sha256),
            ("projection_matrix_sha256", matrix_sha256),
            ("joint_sha256", combined_sha256),
        ):
            if value and not SHA256_RE.fullmatch(value):
                errors.append(f"{scope}.{field_name} must be a sha256:... digest")
        if registry_sha256 and matrix_sha256 and combined_sha256:
            expected_joint = joint_sha256(registry_sha256, matrix_sha256)
            if combined_sha256 != expected_joint:
                errors.append(f"{scope}.joint_sha256 must be derived from registry and matrix digests")

        effective_state = event.get("effective_state")
        if effective_state is None:
            continue
        if not isinstance(effective_state, dict):
            errors.append(f"{scope}.effective_state must be a JSON object when present")
            continue

        schema_version = require_string(event, "schema_version", scope=scope, errors=errors)
        config_state_version = require_positive_int(event, "config_state_version", scope=scope, errors=errors)
        registry = require_mapping(effective_state, "registry", scope=f"{scope}.effective_state", errors=errors)
        projection_matrix = require_mapping(
            effective_state,
            "projection_matrix",
            scope=f"{scope}.effective_state",
            errors=errors,
        )

        if schema_version and schema_version != LEDGER_SCHEMA_VERSION:
            errors.append(f"{scope}.schema_version must be {LEDGER_SCHEMA_VERSION!r}")
        if config_state_version is not None:
            if config_state_version in seen_versions:
                errors.append(f"{scope} duplicates config_state_version {config_state_version}")
                continue
            seen_versions.add(config_state_version)

        if registry is None or projection_matrix is None:
            continue

        registry_id = require_string(registry, "registry_id", scope=f"{scope}.effective_state.registry", errors=errors)
        matrix_id = require_string(
            projection_matrix,
            "matrix_id",
            scope=f"{scope}.effective_state.projection_matrix",
            errors=errors,
        )
        matrix_registry_ref = require_string(
            projection_matrix,
            "registry_ref",
            scope=f"{scope}.effective_state.projection_matrix",
            errors=errors,
        )

        if registry_id and registry_id != EXPECTED_REGISTRY_ID:
            errors.append(f"{scope}.effective_state.registry.registry_id must be {EXPECTED_REGISTRY_ID!r}")
        if matrix_id and matrix_id != EXPECTED_MATRIX_ID:
            errors.append(f"{scope}.effective_state.projection_matrix.matrix_id must be {EXPECTED_MATRIX_ID!r}")
        if matrix_registry_ref and matrix_registry_ref != EXPECTED_REGISTRY_PATH:
            errors.append(
                f"{scope}.effective_state.projection_matrix.registry_ref must be {EXPECTED_REGISTRY_PATH!r}"
            )

        snapshot_registry_sha256 = sha256_for_payload(registry)
        snapshot_matrix_sha256 = sha256_for_payload(projection_matrix)
        snapshot_joint_sha256 = joint_sha256(snapshot_registry_sha256, snapshot_matrix_sha256)

        if registry_sha256 and snapshot_registry_sha256 != registry_sha256:
            errors.append(f"{scope}.registry_sha256 does not match effective_state.registry bytes")
        if matrix_sha256 and snapshot_matrix_sha256 != matrix_sha256:
            errors.append(f"{scope}.projection_matrix_sha256 does not match effective_state.projection_matrix bytes")
        if combined_sha256 and snapshot_joint_sha256 != combined_sha256:
            errors.append(f"{scope}.joint_sha256 does not match effective_state digests")

        if config_state_version is None or recorded_at is None or event_id is None:
            continue

        candidate = (config_state_version, recorded_at, event_id, registry, projection_matrix)
        if latest is None or candidate[:3] > latest[:3]:
            latest = candidate

    if errors:
        raise ValueError("\n".join(errors))
    if latest is None:
        raise ValueError("ledger does not contain a materializable effective_state event")

    return MaterializedConfigState(
        config_state_version=latest[0],
        event_id=latest[2],
        registry=latest[3],
        projection_matrix=latest[4],
    )


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(canonical_json_text(payload), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ledger", type=Path, default=LEDGER_PATH)
    parser.add_argument("--registry-out", type=Path, default=REGISTRY_OUT)
    parser.add_argument("--projection-matrix-out", type=Path, default=MATRIX_OUT)
    args = parser.parse_args()

    state = rematerialize(load_events(args.ledger))
    write_json(args.registry_out, state.registry)
    write_json(args.projection_matrix_out, state.projection_matrix)

    print(args.registry_out)
    print(args.projection_matrix_out)
    print(f"event_id={state.event_id}")
    print(f"config_state_version={state.config_state_version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
