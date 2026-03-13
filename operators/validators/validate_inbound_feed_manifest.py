#!/usr/bin/env python3
"""Validate Acumen inbound feed manifest files."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MANIFEST_DIR = REPO_ROOT / "runtime" / "acumen" / "inbound-feed-manifests"
MANIFEST_SCHEMA_VERSION = "acumen.inbound-feed.manifest/v1"

ALLOWED_IDENTITY_STATUS = {"confirmed", "unconfirmed", "blocked", "ambiguous"}
ALLOWED_AMBIGUITY_STATUS = {"none", "identity_ambiguous", "session_ambiguous"}
ALLOWED_TARGET_STATUS = {"resolved", "unresolved", "ambiguous"}
REQUIRED_MANIFEST_FIELDS = {
    "manifest_id",
    "schema_version",
    "capture_account",
    "claimed_chain",
    "platform",
    "capture_started_at",
    "capture_completed_at",
    "identity_status",
    "identity_evidence",
    "ambiguity_status",
    "entry_count",
    "entries",
    "raw_capture_refs",
    "notes",
}
PLATFORM_REQUIRED_IDENTIFIERS = {
    "youtube": {"channel_id"},
    "x": {"user_id"},
}


def repo_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def resolve_repo_path(raw_value: str | None) -> Path | None:
    if raw_value is None or not str(raw_value).strip():
        return None
    candidate = Path(str(raw_value)).expanduser()
    if candidate.is_absolute():
        return candidate.resolve()
    return (REPO_ROOT / candidate).resolve()


def load_json_object(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"{repo_rel(path)} must be a JSON object")
    return payload


def normalize_platform(value: Any) -> str:
    return str(value or "").strip().lower()


def choose_display_name(entry: dict[str, Any]) -> str:
    for key in ("display_name", "name", "title"):
        value = str(entry.get(key, "")).strip()
        if value:
            return value
    return ""


def choose_profile_url(entry: dict[str, Any]) -> str:
    for key in ("profile_url", "target_url", "channel_url", "url"):
        value = str(entry.get(key, "")).strip()
        if value:
            return value
    return ""


def normalized_identifier_map(raw_value: Any) -> dict[str, str]:
    if not isinstance(raw_value, dict):
        return {}
    normalized: dict[str, str] = {}
    for key, value in raw_value.items():
        key_text = str(key).strip()
        value_text = str(value).strip()
        if key_text and value_text:
            normalized[key_text] = value_text
    return normalized


def required_identifiers_for(
    manifest: dict[str, Any],
    entry: dict[str, Any],
    platform: str,
) -> list[str]:
    required = set(PLATFORM_REQUIRED_IDENTIFIERS.get(platform, set()))

    manifest_requirements = manifest.get("stable_identifier_requirements")
    if isinstance(manifest_requirements, dict):
        for key in ("*", platform):
            values = manifest_requirements.get(key)
            if isinstance(values, list):
                required.update(str(item).strip() for item in values if str(item).strip())

    entry_requirements = entry.get("required_stable_identifiers")
    if isinstance(entry_requirements, list):
        required.update(str(item).strip() for item in entry_requirements if str(item).strip())

    return sorted(required)


def entry_duplicate_key(
    *,
    platform: str,
    identifiers: dict[str, str],
    required_identifiers: list[str],
    profile_url: str,
    display_name: str,
) -> str:
    if required_identifiers:
        resolved_values = [identifiers.get(key, "").strip() for key in required_identifiers]
        if all(resolved_values):
            return f"{platform}|required|{'|'.join(f'{key}={identifiers[key]}' for key in required_identifiers)}"
    if identifiers:
        parts = [f"{key}={value}" for key, value in sorted(identifiers.items())]
        return f"{platform}|stable|{'|'.join(parts)}"
    if profile_url:
        return f"{platform}|url|{profile_url.lower()}"
    return f"{platform}|name|{display_name.casefold()}"


def classify_stable_identifier_status(required_identifiers: list[str], identifiers: dict[str, str]) -> str:
    if not required_identifiers:
        return "not_required"
    if all(identifiers.get(key, "").strip() for key in required_identifiers):
        return "resolved"
    return "missing_required"


def assess_manifest(payload: dict[str, Any], *, source_path: Path | None = None) -> dict[str, Any]:
    manifest_id = str(payload.get("manifest_id", "<missing>")).strip() or "<missing>"
    manifest_platform = normalize_platform(payload.get("platform"))
    manifest_errors: list[str] = []

    missing_fields = sorted(REQUIRED_MANIFEST_FIELDS - set(payload.keys()))
    if missing_fields:
        manifest_errors.append(f"{manifest_id}: missing required fields {missing_fields}")

    schema_version = str(payload.get("schema_version", "")).strip()
    if schema_version and schema_version != MANIFEST_SCHEMA_VERSION:
        manifest_errors.append(
            f"{manifest_id}: schema_version must be {MANIFEST_SCHEMA_VERSION!r}, got {schema_version!r}"
        )

    identity_status = str(payload.get("identity_status", "")).strip()
    if identity_status and identity_status not in ALLOWED_IDENTITY_STATUS:
        manifest_errors.append(f"{manifest_id}: identity_status {identity_status!r} is not supported")
    if identity_status != "confirmed":
        manifest_errors.append(f"{manifest_id}: identity_status must be 'confirmed'")

    ambiguity_status = str(payload.get("ambiguity_status", "")).strip()
    if ambiguity_status and ambiguity_status not in ALLOWED_AMBIGUITY_STATUS:
        manifest_errors.append(f"{manifest_id}: ambiguity_status {ambiguity_status!r} is not supported")
    if ambiguity_status != "none":
        manifest_errors.append(f"{manifest_id}: ambiguity_status must be 'none'")

    identity_evidence = payload.get("identity_evidence")
    if not isinstance(identity_evidence, list) or not identity_evidence:
        manifest_errors.append(f"{manifest_id}: identity_evidence must be a non-empty list")

    raw_capture_refs = payload.get("raw_capture_refs")
    lineage_errors: list[str] = []
    raw_capture_paths: list[str] = []
    raw_capture_ref_count = 0
    if not isinstance(raw_capture_refs, list) or not raw_capture_refs:
        lineage_errors.append(f"{manifest_id}: raw_capture_refs must be a non-empty list")
    else:
        kinds_seen: set[str] = set()
        for index, ref in enumerate(raw_capture_refs, start=1):
            raw_capture_ref_count += 1
            scope = f"{manifest_id}: raw_capture_refs[{index}]"
            if not isinstance(ref, dict):
                lineage_errors.append(f"{scope} must be an object")
                continue
            kind = str(ref.get("kind", "")).strip()
            raw_path_value = str(ref.get("path", "")).strip()
            if not kind:
                lineage_errors.append(f"{scope} missing kind")
            if not raw_path_value:
                lineage_errors.append(f"{scope} missing path")
                continue
            resolved_path = resolve_repo_path(raw_path_value)
            if resolved_path is None:
                lineage_errors.append(f"{scope} path could not be resolved")
                continue
            try:
                raw_capture_paths.append(repo_rel(resolved_path))
            except Exception:
                raw_capture_paths.append(str(resolved_path))
            if not resolved_path.exists():
                lineage_errors.append(f"{scope} missing referenced artifact {repo_rel(resolved_path)}")
            elif not repo_rel(resolved_path).startswith("knowledge/feedstock/"):
                lineage_errors.append(
                    f"{scope} must point into knowledge/feedstock/, got {repo_rel(resolved_path)}"
                )
            if kind:
                kinds_seen.add(kind)
        if "capture_artifact" not in kinds_seen:
            lineage_errors.append(f"{manifest_id}: raw_capture_refs must include a capture_artifact")
        if "staging_receipt" not in kinds_seen:
            lineage_errors.append(f"{manifest_id}: raw_capture_refs must include a staging_receipt")
    manifest_errors.extend(lineage_errors)

    entries = payload.get("entries")
    entry_count = payload.get("entry_count")
    if not isinstance(entries, list):
        manifest_errors.append(f"{manifest_id}: entries must be a list")
        entries = []
    if not isinstance(entry_count, int):
        manifest_errors.append(f"{manifest_id}: entry_count must be an integer")
    elif entry_count != len(entries):
        manifest_errors.append(
            f"{manifest_id}: entry_count={entry_count} does not match actual entries={len(entries)}"
        )

    entry_assessments: list[dict[str, Any]] = []
    seen_entry_ids: set[str] = set()
    seen_duplicate_keys: dict[str, str] = {}
    entry_errors_all: list[str] = []

    for index, entry in enumerate(entries, start=1):
        entry_errors: list[str] = []
        if not isinstance(entry, dict):
            entry_errors.append("entry must be an object")
            entry_assessments.append(
                {
                    "entry_index": index,
                    "entry_id": f"entry-{index}",
                    "platform": manifest_platform,
                    "display_name": "",
                    "profile_url": "",
                    "registry_seed": None,
                    "stable_identifiers": {},
                    "required_stable_identifiers": [],
                    "stable_identifier_status": "missing_required",
                    "target_status": "unresolved",
                    "duplicate_key": f"{manifest_platform}|entry-{index}",
                    "current_registry_compatible": False,
                    "errors": entry_errors,
                }
            )
            entry_errors_all.extend(f"{manifest_id}: entries[{index}]: {message}" for message in entry_errors)
            continue

        entry_id = str(entry.get("entry_id", "")).strip() or f"entry-{index}"
        if entry_id in seen_entry_ids:
            entry_errors.append("duplicate entry_id within manifest")
        seen_entry_ids.add(entry_id)

        entry_platform = normalize_platform(entry.get("platform") or manifest_platform)
        if not entry_platform:
            entry_errors.append("platform is required either on the manifest or the entry")

        target_status = str(entry.get("target_status", "resolved")).strip()
        if target_status not in ALLOWED_TARGET_STATUS:
            entry_errors.append(f"target_status {target_status!r} is not supported")
        elif target_status == "ambiguous":
            entry_errors.append("target resolution is ambiguous")

        stable_identifiers = normalized_identifier_map(entry.get("stable_identifiers"))
        required_stable_identifiers = required_identifiers_for(payload, entry, entry_platform)
        missing_required = [
            key for key in required_stable_identifiers if not stable_identifiers.get(key, "").strip()
        ]
        if missing_required:
            entry_errors.append(f"missing required stable identifiers {missing_required}")

        display_name = choose_display_name(entry)
        profile_url = choose_profile_url(entry)
        duplicate_key = entry_duplicate_key(
            platform=entry_platform or manifest_platform or "unknown",
            identifiers=stable_identifiers,
            required_identifiers=required_stable_identifiers,
            profile_url=profile_url,
            display_name=display_name or entry_id,
        )
        previous_entry_id = seen_duplicate_keys.get(duplicate_key)
        if previous_entry_id is not None:
            entry_errors.append(f"duplicate entry target within manifest (matches {previous_entry_id})")
        else:
            seen_duplicate_keys[duplicate_key] = entry_id

        stable_identifier_status = classify_stable_identifier_status(
            required_stable_identifiers,
            stable_identifiers,
        )
        current_registry_compatible = bool(
            entry_platform == "youtube" and stable_identifiers.get("channel_id", "").strip() and display_name
        )

        assessment = {
            "entry_index": index,
            "entry_id": entry_id,
            "platform": entry_platform,
            "display_name": display_name,
            "profile_url": profile_url,
            "registry_seed": entry.get("registry_seed") if isinstance(entry.get("registry_seed"), dict) else None,
            "stable_identifiers": stable_identifiers,
            "required_stable_identifiers": required_stable_identifiers,
            "stable_identifier_status": stable_identifier_status,
            "target_status": target_status,
            "duplicate_key": duplicate_key,
            "current_registry_compatible": current_registry_compatible,
            "errors": entry_errors,
        }
        entry_assessments.append(assessment)
        entry_errors_all.extend(f"{manifest_id}: {entry_id}: {message}" for message in entry_errors)

    errors = manifest_errors + entry_errors_all

    return {
        "manifest_id": manifest_id,
        "source_path": repo_rel(source_path) if source_path is not None else None,
        "schema_version": schema_version,
        "capture_account": str(payload.get("capture_account", "")).strip(),
        "claimed_chain": str(payload.get("claimed_chain", "")).strip(),
        "platform": manifest_platform,
        "capture_started_at": str(payload.get("capture_started_at", "")).strip(),
        "capture_completed_at": str(payload.get("capture_completed_at", "")).strip(),
        "registry_seed_defaults": (
            payload.get("registry_seed_defaults")
            if isinstance(payload.get("registry_seed_defaults"), dict)
            else None
        ),
        "identity_status": identity_status,
        "ambiguity_status": ambiguity_status,
        "entry_count": len(entries),
        "raw_capture_ref_count": raw_capture_ref_count,
        "raw_capture_paths": raw_capture_paths,
        "manifest_errors": manifest_errors,
        "lineage_errors": lineage_errors,
        "identity_blocked": identity_status != "confirmed" or ambiguity_status != "none",
        "errors": errors,
        "entry_assessments": entry_assessments,
        "valid": not errors,
    }


def assess_manifest_path(path: Path) -> dict[str, Any]:
    try:
        payload = load_json_object(path)
    except Exception as exc:
        manifest_id = path.stem
        return {
            "manifest_id": manifest_id,
            "source_path": repo_rel(path),
            "schema_version": None,
            "capture_account": "",
            "claimed_chain": "",
            "platform": "",
            "capture_started_at": "",
            "capture_completed_at": "",
            "identity_status": "",
            "ambiguity_status": "",
            "entry_count": 0,
            "raw_capture_ref_count": 0,
            "raw_capture_paths": [],
            "manifest_errors": [str(exc)],
            "lineage_errors": [str(exc)],
            "identity_blocked": True,
            "errors": [f"{manifest_id}: {exc}"],
            "entry_assessments": [],
            "valid": False,
        }
    return assess_manifest(payload, source_path=path)


def discover_manifest_paths(
    *,
    manifest_paths: list[str] | None = None,
    manifest_dir: str | Path | None = None,
) -> list[Path]:
    explicit_paths = [Path(item).expanduser().resolve() for item in (manifest_paths or []) if str(item).strip()]
    if explicit_paths:
        return sorted(dict.fromkeys(explicit_paths))

    if manifest_dir is None:
        candidate_dir = DEFAULT_MANIFEST_DIR
    else:
        candidate_dir = Path(manifest_dir).expanduser().resolve()
    if not candidate_dir.exists():
        return []
    return sorted(path.resolve() for path in candidate_dir.glob("*.json") if path.is_file())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", action="append", dest="manifests", default=[])
    parser.add_argument("--manifest-dir", default=str(DEFAULT_MANIFEST_DIR))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest_paths = discover_manifest_paths(
        manifest_paths=args.manifests,
        manifest_dir=args.manifest_dir,
    )

    assessments = [assess_manifest_path(path) for path in manifest_paths]
    errors = [message for assessment in assessments for message in assessment["errors"]]

    if errors:
        print("inbound_manifests=invalid")
        print(f"manifests={len(manifest_paths)}")
        for message in errors:
            print(f"- {message}")
        return 1

    print("inbound_manifests=valid")
    print(f"manifests={len(manifest_paths)}")
    print(f"entries={sum(assessment['entry_count'] for assessment in assessments)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
