#!/usr/bin/env python3
"""Render Ajna's staged exocortex access program from the surface + teleology registries."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_REGISTRY = REPO_ROOT / "orchestration" / "state" / "EXOCORTEX-SURFACE-REGISTRY-CC90.json"
DEFAULT_TELEOLOGY = REPO_ROOT / "orchestration" / "state" / "EXOCORTEX-TELEOLOGY-REGISTRY-CC90.json"
DEFAULT_OUTPUT_JSON = REPO_ROOT / "orchestration" / "state" / "AJNA-EXOCORTEX-ACCESS-PROGRAM-CC93.json"
DEFAULT_OUTPUT_MD = REPO_ROOT / "orchestration" / "state" / "impl" / "AJNA-EXOCORTEX-ACCESS-PROGRAM-CC93.md"

LIVE_RUNTIME_SURFACES = {"slack_surface", "discord_surface"}


def utc_now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def access_strategy(access_model: str, auth_parent: str | None) -> str:
    if auth_parent:
        return "parent_auth_then_surface"
    if access_model == "web":
        return "browser_only"
    if access_model == "web_api":
        return "browser_then_api"
    if access_model == "web_api_cli":
        return "browser_then_api_cli"
    if access_model == "api":
        return "api_first"
    if access_model == "cli":
        return "cli_first"
    return "hybrid_manual"


def ajna_role(access_model: str, modality: str) -> str:
    if modality == "headless":
        return "secondary_to_cli_or_automation"
    if access_model == "web":
        return "primary_browser_operator"
    if "web" in access_model:
        return "primary_auth_and_browser_operator"
    if modality == "agentified":
        return "runtime_surface_operator"
    return "shared_operator"


def wave_for(slug: str, priority: str, access_model: str, modality: str) -> str:
    if slug in LIVE_RUNTIME_SURFACES:
        return "wave0_live_runtime"
    if priority == "P1" and ("web" in access_model or modality in {"agentified", "hybrid"}):
        return "wave1_priority_hubs"
    if priority == "P1":
        return "wave1_priority_hubs"
    if priority == "P2":
        return "wave2_secondary_systems"
    return "wave3_long_tail"


def sort_key(item: dict[str, Any]) -> tuple[str, str]:
    return (item["wave"], item["slug"])


def render_program(registry: dict[str, Any], teleology: dict[str, Any]) -> dict[str, Any]:
    teleology_by_slug = {
        row["slug"]: row
        for row in teleology.get("surfaces", [])
        if isinstance(row, dict) and isinstance(row.get("slug"), str)
    }
    program_surfaces: list[dict[str, Any]] = []

    for surface in registry.get("surfaces", []):
        if not isinstance(surface, dict):
            continue
        slug = surface.get("slug")
        if not isinstance(slug, str):
            continue
        teleology_row = teleology_by_slug.get(slug, {})
        access_model = str(surface.get("access_model", "unknown"))
        priority = str(teleology_row.get("integration_priority", "P3"))
        modality = str(teleology_row.get("default_modality", "hybrid"))
        auth_parent = surface.get("auth_parent_surface")
        record = {
            "slug": slug,
            "service": surface.get("service"),
            "class": surface.get("class"),
            "owner_identity": surface.get("owner_identity"),
            "workspace_namespace": surface.get("workspace_namespace"),
            "status": surface.get("status"),
            "auth_parent_surface": auth_parent,
            "teleology_epithet": teleology_row.get("epithet"),
            "proper_role": teleology_row.get("proper_role"),
            "anti_role": teleology_row.get("anti_role"),
            "default_modality": modality,
            "integration_priority": priority,
            "access_model": access_model,
            "access_strategy": access_strategy(access_model, auth_parent if isinstance(auth_parent, str) else None),
            "ajna_role": ajna_role(access_model, modality),
            "wave": wave_for(slug, priority, access_model, modality),
        }
        program_surfaces.append(record)

    program_surfaces.sort(key=sort_key)
    wave_counts = Counter(item["wave"] for item in program_surfaces)
    strategy_counts = Counter(item["access_strategy"] for item in program_surfaces)

    return {
        "generated_at": utc_now(),
        "status": "active",
        "version": "cc93",
        "office": "ajna",
        "designated_browser": {
            "browser_family": "vivaldi",
            "openclaw_profile": "vivaldi",
            "executable_path": "/Applications/Vivaldi.app/Contents/MacOS/Vivaldi",
            "driver": "extension",
            "note": "Ajna is pinned to Vivaldi by explicit OpenClaw config, not system-default browser detection.",
        },
        "mission": "Give Ajna broad exocortex reach while keeping repo truth, least-privilege credentials, and staged onboarding discipline intact.",
        "live_runtime_surfaces": sorted(LIVE_RUNTIME_SURFACES),
        "counts": {
            "surface_count": len(program_surfaces),
            "wave_counts": dict(sorted(wave_counts.items())),
            "strategy_counts": dict(sorted(strategy_counts.items())),
        },
        "waves": {
            "wave0_live_runtime": "already-live operator bus and runtime comms surfaces",
            "wave1_priority_hubs": "identity roots, work hubs, intelligence hubs, and operational P1 rails",
            "wave2_secondary_systems": "secondary but still operationally meaningful surfaces",
            "wave3_long_tail": "lower-priority or highly manual surfaces that should not block the control plane",
        },
        "surfaces": program_surfaces,
    }


def render_markdown(program: dict[str, Any]) -> str:
    lines = [
        "# Ajna Exocortex Access Program — CC93",
        "",
        f"- Generated: `{program['generated_at']}`",
        "- Office: `ajna`",
        f"- Designated browser: `{program['designated_browser']['browser_family']}` via OpenClaw profile `{program['designated_browser']['openclaw_profile']}`",
        f"- Mission: {program['mission']}",
        "",
        "## Design Law",
        "",
        "- Ajna is the browser-first exocortex operator, not the constitutional authority.",
        "- Repo artifacts remain ratified truth; exocortex surfaces are execution, sensing, and relay surfaces.",
        "- Access expansion must be staged by wave, not improvised tab sprawl.",
        "- Parent-auth children must never be treated as independent identity roots.",
        "",
        "## Counts",
        "",
    ]
    for key, value in sorted(program["counts"].items()):
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(["", "## Waves", ""])
    grouped: dict[str, list[dict[str, Any]]] = {}
    for item in program["surfaces"]:
        grouped.setdefault(item["wave"], []).append(item)
    for wave, description in program["waves"].items():
        lines.append(f"### {wave}")
        lines.append("")
        lines.append(f"- {description}")
        for item in grouped.get(wave, []):
            parent = f" parent=`{item['auth_parent_surface']}`" if item.get("auth_parent_surface") else ""
            lines.append(
                f"- `{item['slug']}`: `{item['service']}` | strategy=`{item['access_strategy']}` | role=`{item['ajna_role']}` | priority=`{item['integration_priority']}`{parent}"
            )
        lines.append("")
    lines.extend(
        [
            "## Operational Reading",
            "",
            "- `browser_only` and `browser_then_api` surfaces are Ajna-primary.",
            "- `browser_then_api_cli` surfaces are shared: Ajna handles login/browser auth, terminal harnesses consume stable CLI/API afterwards.",
            "- `secondary_to_cli_or_automation` surfaces should still be visible to Ajna, but they should not distort role boundaries or make Ajna the new backend.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", default=str(DEFAULT_REGISTRY))
    parser.add_argument("--teleology", default=str(DEFAULT_TELEOLOGY))
    parser.add_argument("--output-json", default=str(DEFAULT_OUTPUT_JSON))
    parser.add_argument("--output-md", default=str(DEFAULT_OUTPUT_MD))
    args = parser.parse_args()

    registry = load_json(Path(args.registry).expanduser().resolve())
    teleology = load_json(Path(args.teleology).expanduser().resolve())
    program = render_program(registry, teleology)

    output_json = Path(args.output_json).expanduser().resolve()
    output_md = Path(args.output_md).expanduser().resolve()
    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_md.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(json.dumps(program, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    output_md.write_text(render_markdown(program) + "\n", encoding="utf-8")
    print(f"Wrote {output_json}")
    print(f"Wrote {output_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
