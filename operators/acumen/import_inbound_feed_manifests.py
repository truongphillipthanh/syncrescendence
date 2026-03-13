#!/usr/bin/env python3
"""Import Acumen inbound feed manifests into a portfolio preview and registry-ready seed rows."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

try:
    from .evidence_family import REPO_ROOT, repo_rel, utc_now
    from .init_registry import index_by_channel_id, load_json
    from .registry_contract import (
        CADENCES,
        CHAIN_ALIGNMENTS,
        DEPTHS,
        GENRES,
        POLISH_LEVELS,
        PRIORITY_BANDS,
        SIGNAL_DENSITIES,
        VISUAL_DEPENDENCY,
        VOICE_NORMALIZATION,
        default_channel,
        validate_registry,
    )
except ImportError:
    OPS_DIR = Path(__file__).resolve().parent
    if str(OPS_DIR) not in sys.path:
        sys.path.insert(0, str(OPS_DIR))
    from evidence_family import REPO_ROOT, repo_rel, utc_now  # type: ignore[no-redef]
    from init_registry import index_by_channel_id, load_json  # type: ignore[no-redef]
    from registry_contract import (  # type: ignore[no-redef]
        CADENCES,
        CHAIN_ALIGNMENTS,
        DEPTHS,
        GENRES,
        POLISH_LEVELS,
        PRIORITY_BANDS,
        SIGNAL_DENSITIES,
        VISUAL_DEPENDENCY,
        VOICE_NORMALIZATION,
        default_channel,
        validate_registry,
    )

VALIDATORS_DIR = Path(__file__).resolve().parents[1] / "validators"
if str(VALIDATORS_DIR) not in sys.path:
    sys.path.insert(0, str(VALIDATORS_DIR))

from validate_inbound_feed_manifest import (  # type: ignore[no-redef]
    DEFAULT_MANIFEST_DIR,
    assess_manifest_path,
    discover_manifest_paths,
)


PORTFOLIO_SCHEMA_VERSION = "acumen.inbound-feed.portfolio/v1"
DEFAULT_PORTFOLIO_JSON = REPO_ROOT / "orchestration" / "state" / "ACUMEN-INBOUND-FEED-PORTFOLIO.json"
DEFAULT_PORTFOLIO_MD = REPO_ROOT / "orchestration" / "state" / "ACUMEN-INBOUND-FEED-PORTFOLIO.md"
DEFAULT_SEED_OUTPUT = REPO_ROOT / "runtime" / "acumen" / "inbound-feed-import-seed.json"
DEFAULT_REGISTRY_JSON = REPO_ROOT / "runtime" / "acumen" / "registry.json"

REQUIRED_MATCH_STATES = [
    "registry_ready",
    "portfolio_only",
    "blocked_identity",
    "ambiguous_target",
    "unresolved_platform_id",
]
MATCH_STATE_ORDER = {
    "registry_ready": 0,
    "portfolio_only": 1,
    "blocked_identity": 2,
    "ambiguous_target": 3,
    "unresolved_platform_id": 4,
    "broken_lineage": 5,
    "duplicate_manifest_entry": 6,
    "invalid_manifest": 7,
}
CURRENT_REGISTRY_SUPPORTED_PLATFORMS = {"youtube"}
ACCOUNT_PRIORITY = {
    "acumen.truongphillipthanh@gmail.com": 0,
    "coherence.truongphillipthanh@gmail.com": 1,
    "efficacy.truongphillipthanh@gmail.com": 2,
    "mastery.truongphillipthanh@gmail.com": 3,
    "transcendence.truongphillipthanh@gmail.com": 4,
}


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_text(path: Path, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body.rstrip() + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", action="append", dest="manifests", default=[])
    parser.add_argument("--manifest-dir", default=str(DEFAULT_MANIFEST_DIR))
    parser.add_argument("--registry", default=str(DEFAULT_REGISTRY_JSON))
    parser.add_argument("--portfolio-json", default=str(DEFAULT_PORTFOLIO_JSON))
    parser.add_argument("--portfolio-md", default=str(DEFAULT_PORTFOLIO_MD))
    parser.add_argument("--seed-output", default=str(DEFAULT_SEED_OUTPUT))
    return parser.parse_args()


def unique_strings(raw_value: Any) -> list[str]:
    if not isinstance(raw_value, list):
        return []
    seen: set[str] = set()
    result: list[str] = []
    for item in raw_value:
        text = str(item).strip()
        if not text or text in seen:
            continue
        seen.add(text)
        result.append(text)
    return result


def choose_allowed(raw_value: Any, allowed: set[str], default: str) -> str:
    text = str(raw_value or "").strip()
    return text if text in allowed else default


def choose_float(raw_value: Any, default: float) -> float:
    try:
        value = float(raw_value)
    except Exception:
        return default
    return value if 0.0 <= value <= 1.0 else default


def manifest_has_generic_errors(assessment: dict[str, Any]) -> bool:
    return bool(assessment["manifest_errors"]) and not assessment["identity_blocked"] and not assessment["lineage_errors"]


def classify_match_state(assessment: dict[str, Any], entry: dict[str, Any]) -> tuple[str, str]:
    if assessment["identity_blocked"]:
        return "blocked_identity", "manifest identity was not confirmed or capture ambiguity remained"
    if assessment["lineage_errors"]:
        return "broken_lineage", "raw capture lineage is incomplete or missing"
    if manifest_has_generic_errors(assessment):
        return "invalid_manifest", "manifest-level validation errors remain unresolved"
    if any("duplicate entry" in message for message in entry["errors"]):
        return "duplicate_manifest_entry", "duplicate entries remain inside the manifest"
    if entry["target_status"] == "ambiguous" or any("ambiguous" in message for message in entry["errors"]):
        return "ambiguous_target", "entry target remains ambiguous"
    if entry["stable_identifier_status"] == "missing_required":
        return "unresolved_platform_id", "required stable identifiers are still missing"
    if entry["errors"]:
        return "portfolio_only", "entry-level validation errors remain unresolved"
    if entry["platform"] not in CURRENT_REGISTRY_SUPPORTED_PLATFORMS:
        return "portfolio_only", "platform is preserved in the portfolio but not yet supported by the live Acumen registry"
    if not entry["display_name"]:
        return "portfolio_only", "entry lacks the display name required for a current Acumen seed row"
    if not entry["current_registry_compatible"]:
        return "portfolio_only", "entry is not yet current-registry-compatible"
    return "registry_ready", "entry resolves to a current-registry-compatible YouTube channel"


def build_seed_row(
    assessment: dict[str, Any],
    entry: dict[str, Any],
) -> dict[str, Any]:
    stable_identifiers = dict(entry["stable_identifiers"])
    seed_defaults = {}
    if isinstance(assessment.get("registry_seed_defaults"), dict):
        seed_defaults.update(assessment["registry_seed_defaults"])
    entry_seed = entry.get("registry_seed")
    if isinstance(entry_seed, dict):
        seed_defaults.update(entry_seed)

    channel_id = stable_identifiers["channel_id"]
    notes = (
        f"Imported from {assessment['manifest_id']} ({assessment['capture_account']}, {assessment['platform']}) "
        "through the inbound-feed portfolio preview. Portfolio and seed remain derivative to Acumen intake sovereignty."
    )
    return {
        "channel_id": channel_id,
        "name": entry["display_name"],
        "genre": choose_allowed(seed_defaults.get("genre"), GENRES, "Commentary"),
        "cadence": choose_allowed(seed_defaults.get("cadence"), CADENCES, "irregular"),
        "default_compression": choose_allowed(
            seed_defaults.get("default_compression"),
            DEPTHS,
            "Precis",
        ),
        "default_polish": choose_allowed(
            seed_defaults.get("default_polish"),
            POLISH_LEVELS,
            "charitable",
        ),
        "signal_density": choose_allowed(
            seed_defaults.get("signal_density"),
            SIGNAL_DENSITIES,
            "medium",
        ),
        "visual_dependency": choose_allowed(
            seed_defaults.get("visual_dependency"),
            VISUAL_DEPENDENCY,
            "low",
        ),
        "voice_normalization": choose_allowed(
            seed_defaults.get("voice_normalization"),
            VOICE_NORMALIZATION,
            "normalize",
        ),
        "domain_tags": unique_strings(seed_defaults.get("domain_tags") or []),
        "chain_alignment": choose_allowed(
            seed_defaults.get("chain_alignment") or assessment.get("claimed_chain"),
            CHAIN_ALIGNMENTS,
            "Information",
        ),
        "resolution_vocabulary": unique_strings(seed_defaults.get("resolution_vocabulary") or []),
        "priority_band": choose_allowed(
            seed_defaults.get("priority_band"),
            PRIORITY_BANDS,
            "Tier 2",
        ),
        "triage_hit_rate": choose_float(seed_defaults.get("triage_hit_rate"), 0.5),
        "notes": notes,
        "source_manifest_id": assessment["manifest_id"],
        "source_manifest_path": assessment["source_path"],
        "capture_account": assessment["capture_account"],
        "claimed_chain": assessment["claimed_chain"],
        "platform": entry["platform"],
        "profile_url": entry["profile_url"],
        "stable_identifiers": stable_identifiers,
        "portfolio_entry_id": entry["portfolio_entry_id"],
        "raw_capture_paths": assessment["raw_capture_paths"],
    }


def seed_candidate_sort_key(candidate: dict[str, Any]) -> tuple[int, str, str, str]:
    return (
        ACCOUNT_PRIORITY.get(candidate["capture_account"], 99),
        str(candidate["capture_completed_at"]),
        str(candidate["manifest_id"]),
        str(candidate["portfolio_entry_id"]),
    )


def render_portfolio_markdown(portfolio: dict[str, Any]) -> str:
    counts = portfolio["counts"]
    lines = [
        "# Acumen Inbound Feed Portfolio",
        "",
        f"- Generated at: `{portfolio['generated_at']}`",
        f"- Source manifest dir: `{portfolio['source_manifest_dir']}`",
        f"- Current registry: `{portfolio['current_registry_path']}`",
        f"- Portfolio JSON: `{portfolio['runtime_surfaces']['portfolio_json']}`",
        f"- Portfolio markdown: `{portfolio['runtime_surfaces']['portfolio_md']}`",
        f"- Seed output: `{portfolio['runtime_surfaces']['seed_output']}`",
        f"- Intake authority: `{portfolio['intake_authority']}`",
        f"- Manifests discovered: `{counts['manifest_count']}`",
        f"- Entries discovered: `{counts['entry_count']}`",
        f"- Valid manifests: `{counts['valid_manifest_count']}`",
        f"- Invalid manifests: `{counts['invalid_manifest_count']}`",
        f"- Registry-ready entries: `{counts['registry_ready']}`",
        f"- Portfolio-only entries: `{counts['portfolio_only']}`",
        f"- Blocked identity entries: `{counts['blocked_identity']}`",
        f"- Ambiguous target entries: `{counts['ambiguous_target']}`",
        f"- Unresolved platform IDs: `{counts['unresolved_platform_id']}`",
        f"- Seed rows emitted: `{counts['seed_row_count']}`",
        "",
        "## Merge Discipline",
        "",
        "- The inbound portfolio is a preview surface only. It does not replace `runtime/acumen/registry.json`.",
        "- Seed rows are emitted only for current-registry-compatible entries and are revalidated through the existing Acumen registry contract before merge.",
        f"- Merge path: `{portfolio['merge_preview']['merge_command']}`",
        f"- Strict validation path: `{portfolio['merge_preview']['strict_validation_command']}`",
        "",
        "## Manifests",
        "",
    ]

    if portfolio["manifests"]:
        for manifest in portfolio["manifests"]:
            lines.append(
                "- "
                f"`{manifest['manifest_id']}` "
                f"account=`{manifest['capture_account'] or 'unknown'}` "
                f"platform=`{manifest['platform'] or 'unknown'}` "
                f"validation=`{manifest['validation_status']}` "
                f"entries=`{manifest['entry_count']}` "
                f"errors=`{len(manifest['validation_errors'])}` "
                f"path=`{manifest['manifest_path']}`"
            )
    else:
        lines.append("- no manifests discovered")

    lines.extend(["", "## Entries", ""])
    if portfolio["entries"]:
        for entry in portfolio["entries"]:
            parts = [
                f"`{entry['portfolio_entry_id']}`",
                f"platform=`{entry['platform'] or 'unknown'}`",
                f"state=`{entry['match_state']}`",
                f"seed_emitted=`{str(entry['seed_emitted']).lower()}`",
            ]
            if entry.get("seed_channel_id"):
                parts.append(f"channel_id=`{entry['seed_channel_id']}`")
            if entry.get("display_name"):
                parts.append(f"name=`{entry['display_name']}`")
            if entry.get("registry_presence"):
                parts.append(f"registry_presence=`{entry['registry_presence']}`")
            if entry.get("seed_suppressed_reason"):
                parts.append(f"seed_note=`{entry['seed_suppressed_reason']}`")
            lines.append("- " + " ".join(parts))
    else:
        lines.append("- no manifest entries discovered")

    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    manifest_dir = Path(args.manifest_dir).expanduser().resolve()
    registry_path = Path(args.registry).expanduser().resolve()
    portfolio_json_path = Path(args.portfolio_json).expanduser().resolve()
    portfolio_md_path = Path(args.portfolio_md).expanduser().resolve()
    seed_output_path = Path(args.seed_output).expanduser().resolve()

    manifest_dir.mkdir(parents=True, exist_ok=True)
    if not registry_path.exists():
        raise SystemExit(f"registry missing: {registry_path}")

    current_registry = load_json(registry_path)
    if not isinstance(current_registry, dict):
        raise SystemExit(f"registry must be a JSON object: {repo_rel(registry_path)}")
    current_registry_errors = validate_registry(current_registry)
    if current_registry_errors:
        raise SystemExit("current registry validation failed:\n- " + "\n- ".join(current_registry_errors))

    manifest_paths = discover_manifest_paths(
        manifest_paths=args.manifests,
        manifest_dir=manifest_dir,
    )
    assessments = [assess_manifest_path(path) for path in manifest_paths]

    current_channels = current_registry.get("channels", [])
    current_index = index_by_channel_id(current_channels)

    match_state_counter: Counter[str] = Counter()
    manifest_records: list[dict[str, Any]] = []
    entry_records: list[dict[str, Any]] = []
    entry_record_by_id: dict[str, dict[str, Any]] = {}
    seed_candidates: dict[str, list[dict[str, Any]]] = defaultdict(list)
    valid_manifest_count = 0
    invalid_manifest_count = 0

    for assessment in assessments:
        manifest_state_counter: Counter[str] = Counter()
        if assessment["valid"]:
            valid_manifest_count += 1
        else:
            invalid_manifest_count += 1

        for entry in assessment["entry_assessments"]:
            portfolio_entry_id = f"{assessment['manifest_id']}::{entry['entry_id']}"
            entry["portfolio_entry_id"] = portfolio_entry_id

            match_state, match_reason = classify_match_state(assessment, entry)
            stable_identifiers = dict(entry["stable_identifiers"])
            seed_channel_id = stable_identifiers.get("channel_id", "").strip()
            already_in_registry = bool(seed_channel_id and seed_channel_id in current_index)

            record = {
                "portfolio_entry_id": portfolio_entry_id,
                "manifest_id": assessment["manifest_id"],
                "manifest_path": assessment["source_path"],
                "capture_account": assessment["capture_account"],
                "claimed_chain": assessment["claimed_chain"],
                "capture_completed_at": assessment["capture_completed_at"],
                "entry_id": entry["entry_id"],
                "platform": entry["platform"],
                "display_name": entry["display_name"],
                "profile_url": entry["profile_url"],
                "match_state": match_state,
                "match_reason": match_reason,
                "validation_errors": entry["errors"],
                "required_stable_identifiers": entry["required_stable_identifiers"],
                "stable_identifiers": stable_identifiers,
                "target_status": entry["target_status"],
                "manifest_validation_status": "valid" if assessment["valid"] else "invalid",
                "manifest_validation_errors": assessment["manifest_errors"],
                "current_registry_compatible": entry["current_registry_compatible"],
                "registry_presence": (
                    "already_registered"
                    if already_in_registry
                    else ("candidate" if seed_channel_id else "not_applicable")
                ),
                "seed_channel_id": seed_channel_id or None,
                "seed_emitted": False,
                "seed_suppressed_reason": None,
            }

            if match_state == "registry_ready":
                if already_in_registry:
                    record["seed_suppressed_reason"] = "channel_id already present in runtime/acumen/registry.json"
                else:
                    seed_row = build_seed_row(assessment, entry)
                    normalized_preview = default_channel(seed_row)
                    preview_errors = validate_registry({"channels": [normalized_preview]})
                    if preview_errors:
                        record["match_state"] = "portfolio_only"
                        record["match_reason"] = "current Acumen registry contract rejected the derived seed row"
                        record["seed_suppressed_reason"] = "; ".join(preview_errors)
                    else:
                        seed_candidates[seed_channel_id].append(
                            {
                                "portfolio_entry_id": portfolio_entry_id,
                                "manifest_id": assessment["manifest_id"],
                                "capture_account": assessment["capture_account"],
                                "capture_completed_at": assessment["capture_completed_at"],
                                "seed_row": seed_row,
                            }
                        )

            entry_record_by_id[portfolio_entry_id] = record
            entry_records.append(record)
            manifest_state_counter[record["match_state"]] += 1
            match_state_counter[record["match_state"]] += 1

        manifest_records.append(
            {
                "manifest_id": assessment["manifest_id"],
                "manifest_path": assessment["source_path"],
                "capture_account": assessment["capture_account"],
                "claimed_chain": assessment["claimed_chain"],
                "platform": assessment["platform"],
                "validation_status": "valid" if assessment["valid"] else "invalid",
                "validation_errors": assessment["errors"],
                "manifest_errors": assessment["manifest_errors"],
                "entry_count": assessment["entry_count"],
                "raw_capture_paths": assessment["raw_capture_paths"],
                "match_state_counts": dict(sorted(manifest_state_counter.items())),
            }
        )

    selected_seed_rows: list[dict[str, Any]] = []
    for channel_id, candidates in sorted(seed_candidates.items()):
        sorted_candidates = sorted(candidates, key=seed_candidate_sort_key)
        canonical = sorted_candidates[0]
        canonical_entry = entry_record_by_id[canonical["portfolio_entry_id"]]
        canonical_entry["seed_emitted"] = True
        source_manifest_ids = sorted({candidate["manifest_id"] for candidate in sorted_candidates})
        source_capture_accounts = sorted({candidate["capture_account"] for candidate in sorted_candidates})
        canonical["seed_row"]["source_manifest_ids"] = source_manifest_ids
        canonical["seed_row"]["source_capture_accounts"] = source_capture_accounts
        canonical["seed_row"]["source_portfolio_entry_ids"] = [
            candidate["portfolio_entry_id"] for candidate in sorted_candidates
        ]
        canonical["seed_row"]["notes"] = (
            f"{canonical['seed_row']['notes']} Sources={','.join(source_manifest_ids)} "
            f"Accounts={','.join(source_capture_accounts)}"
        )
        selected_seed_rows.append(canonical["seed_row"])

        for suppressed in sorted_candidates[1:]:
            suppressed_entry = entry_record_by_id[suppressed["portfolio_entry_id"]]
            suppressed_entry["seed_suppressed_reason"] = (
                f"seed row consolidated under {canonical['portfolio_entry_id']}"
            )

    normalized_seed_rows = [default_channel(row) for row in selected_seed_rows]
    merged_index = index_by_channel_id(current_channels)
    for row in normalized_seed_rows:
        merged_index[str(row["channel_id"])] = row
    merged_registry = {
        "generated_at": utc_now(),
        "source_seed": str(seed_output_path),
        "channels": sorted(merged_index.values(), key=lambda item: str(item.get("name", "")).lower()),
    }
    merged_registry_errors = validate_registry(merged_registry)
    if merged_registry_errors:
        raise SystemExit("registry merge preview invalid:\n- " + "\n- ".join(merged_registry_errors))

    entry_records.sort(
        key=lambda item: (
            MATCH_STATE_ORDER.get(item["match_state"], 99),
            str(item["capture_account"]),
            str(item["platform"]),
            str(item["display_name"]).casefold(),
            str(item["portfolio_entry_id"]),
        )
    )
    manifest_records.sort(key=lambda item: str(item["manifest_id"]).casefold())

    counts = {
        "manifest_count": len(manifest_records),
        "entry_count": len(entry_records),
        "valid_manifest_count": valid_manifest_count,
        "invalid_manifest_count": invalid_manifest_count,
        "seed_row_count": len(selected_seed_rows),
    }
    for state in REQUIRED_MATCH_STATES:
        counts[state] = match_state_counter.get(state, 0)
    for state in sorted(match_state_counter):
        if state not in counts:
            counts[state] = match_state_counter[state]

    portfolio = {
        "schema_version": PORTFOLIO_SCHEMA_VERSION,
        "generated_at": utc_now(),
        "source_manifest_dir": repo_rel(manifest_dir),
        "current_registry_path": repo_rel(registry_path),
        "intake_authority": (
            "Acumen remains the sole shared intake authority; this portfolio and seed are preview surfaces only."
        ),
        "runtime_surfaces": {
            "portfolio_json": repo_rel(portfolio_json_path),
            "portfolio_md": repo_rel(portfolio_md_path),
            "seed_output": repo_rel(seed_output_path),
        },
        "counts": counts,
        "merge_preview": {
            "validated_with_existing_logic": True,
            "existing_registry_channels": len(current_channels),
            "seed_rows_ready": len(selected_seed_rows),
            "merged_registry_channels": len(merged_index),
            "merge_command": (
                "python3 operators/acumen/init_registry.py "
                f"--seed {repo_rel(seed_output_path)} "
                f"--output {repo_rel(registry_path)} --merge"
            ),
            "strict_validation_command": (
                "python3 operators/acumen/validate_registry.py "
                f"--registry {repo_rel(registry_path)} --strict"
            ),
        },
        "manifests": manifest_records,
        "entries": entry_records,
        "seed_rows": selected_seed_rows,
        "manual_boundary": (
            "Browser/session capture, identity confirmation, and stable-ID resolution remain upstream manual work. "
            "This importer only preserves preview state and prepares seed rows for the existing Acumen registry path."
        ),
    }

    write_json(seed_output_path, selected_seed_rows)
    write_json(portfolio_json_path, portfolio)
    write_text(portfolio_md_path, render_portfolio_markdown(portfolio))

    print(repo_rel(portfolio_json_path))
    print(repo_rel(portfolio_md_path))
    print(repo_rel(seed_output_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
