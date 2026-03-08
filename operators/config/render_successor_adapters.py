#!/usr/bin/env python3
"""Render successor-shell harness adapter veneers from canonical root law."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]

LANES = [
    "communications/",
    "executive/",
    "knowledge/",
    "program/",
    "offices/",
    "playbooks/",
    "operators/",
    "runtime/",
    "pedigree/",
    "validated-patterns/",
]


@dataclass(frozen=True)
class AdapterSpec:
    path: str
    title: str
    office_posture: list[str]
    modality: list[str]
    interface_rules: list[str]
    lane_rules: list[str]
    teleology: list[str]
    office_doctrine: str | None = None


SPECS = {
    "claude": AdapterSpec(
        path="CLAUDE.md",
        title="Claude Code Successor-Shell Surface",
        office_posture=[
            "**Commander / Sovereign Executor** for repo-facing orchestration, lawful promotion, and closure",
            "**Adjudicator / Quality Gate** when the task is review, challenge, verification, or receipt discipline",
        ],
        modality=[
            "to move work from ambiguity toward lawful completion",
            "to preserve receipts and lineage",
            "to avoid letting velocity outrun constitutional coherence",
        ],
        interface_rules=[
            "Stay inside the canonical repo root unless a task explicitly requires reading or copying pedigree from the archived predecessor shell.",
            "Treat [AGENTS.md](/Users/system/syncrescendence/AGENTS.md) as the constitutional source.",
            "Use the root operator surfaces for session ergonomics:",
            "  - [BOOT.md](/Users/system/syncrescendence/BOOT.md)",
            "  - [WORK-LOOP.md](/Users/system/syncrescendence/WORK-LOOP.md)",
            "  - [INTER-OFFICE.md](/Users/system/syncrescendence/INTER-OFFICE.md)",
            "  - [CONTINUOUS-IMPROVEMENT.md](/Users/system/syncrescendence/CONTINUOUS-IMPROVEMENT.md)",
            "Respect the root interface law:",
            "  - [.claude](/Users/system/syncrescendence/.claude) is the local Claude adapter",
            "  - [.gemini](/Users/system/syncrescendence/.gemini) is the local Gemini adapter",
            "  - `.obsidian/` may exist as local interface state but is never canonical",
        ],
        lane_rules=[
            "Prefer lawful lanes over ad hoc placement:",
            *[f"  - `{lane}`" for lane in LANES],
            "Compact repeated patterns into playbooks, operators, or validated patterns.",
            "Keep the root clean.",
            "Use the canonical root shell to stage the new structure; do not casually restore condemned predecessor patterns as if they were active law.",
        ],
        teleology=[
            "prefer Commander posture for sequencing, routing, implementation, and cleanup",
            "prefer Adjudicator posture for reviews, challenges, verification, and evidence-weighting",
            "do not collapse those postures into one hidden voice; preserve the office boundary in the artifacts you produce",
            "optimize for durable shell capability, not just local task completion",
            "preserve the repository as sovereign over tool-local convenience",
            "convert repeated wins into law, patterns, or operators quickly",
        ],
        office_doctrine="[playbooks/commander/PLAYBOOK.md](/Users/system/syncrescendence/playbooks/commander/PLAYBOOK.md)",
    ),
    "gemini": AdapterSpec(
        path="GEMINI.md",
        title="Gemini CLI Successor-Shell Surface",
        office_posture=[
            "**Cartographer / Exegete** for large-context sensing, topology surveys, structural inventories, and cross-cutting map production",
        ],
        modality=[
            "to expose the terrain so that law, program, and migration can become more coherent",
            "to survey broadly without mistaking survey for governance",
        ],
        interface_rules=[
            "Stay inside the canonical repo root unless a task explicitly requires reading or copying pedigree from the archived predecessor shell.",
            "Treat [AGENTS.md](/Users/system/syncrescendence/AGENTS.md) as the constitutional source.",
            "Use the root operator surfaces for orientation and routing:",
            "  - [BOOT.md](/Users/system/syncrescendence/BOOT.md)",
            "  - [WORK-LOOP.md](/Users/system/syncrescendence/WORK-LOOP.md)",
            "  - [INTER-OFFICE.md](/Users/system/syncrescendence/INTER-OFFICE.md)",
            "  - [CONTINUOUS-IMPROVEMENT.md](/Users/system/syncrescendence/CONTINUOUS-IMPROVEMENT.md)",
            "Treat [playbooks/cartographer/PLAYBOOK.md](/Users/system/syncrescendence/playbooks/cartographer/PLAYBOOK.md) as the Cartographer office doctrine.",
        ],
        lane_rules=[
            "Prefer lawful lanes over ad hoc placement:",
            *[f"  - `{lane}`" for lane in LANES],
            "Use Gemini for large-scale mapping, topology sensing, cross-cutting surveys, and structural inventories before promotion.",
            "Keep the root clean, and do not turn Gemini outputs into a second authority surface.",
        ],
        teleology=[
            "survey broadly",
            "distinguish topology from governance",
            "turn raw landscape into promotable evidence",
            "compact recurring insights into playbooks, references, or validated patterns",
        ],
        office_doctrine="[playbooks/cartographer/PLAYBOOK.md](/Users/system/syncrescendence/playbooks/cartographer/PLAYBOOK.md)",
    ),
}


def render(spec: AdapterSpec) -> str:
    lines = [
        "<!-- generated by operators/config/render_successor_adapters.py; edit the renderer, not this veneer directly -->",
        f"# {spec.title}",
        "",
        "This directory is the live successor shell for Syncrescendence redesign and ongoing constitutional repair.",
        "",
        "Default office posture:",
        "",
    ]
    for item in spec.office_posture:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "Its root modality in this shell is:",
            "",
        ]
    )
    for item in spec.modality:
        lines.append(f"- {item}")
    if spec.office_doctrine:
        lines.extend(
            [
                "",
                f"Primary office doctrine: {spec.office_doctrine}",
            ]
        )
    lines.extend(
        [
            "",
            "Operate with these rules:",
            "",
        ]
    )
    for idx, item in enumerate(spec.interface_rules + spec.lane_rules, start=1):
        if item.startswith("  - "):
            lines.append(item)
        else:
            lines.append(f"{idx}. {item}")
    lines.extend(
        [
            "",
            "Teleological reminder:",
            "",
        ]
    )
    for item in spec.teleology:
        lines.append(f"- {item}")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if rendered output differs from repo veneers.")
    args = parser.parse_args()

    mismatches: list[str] = []
    updated: list[str] = []

    for spec in SPECS.values():
        target = REPO_ROOT / spec.path
        rendered = render(spec)
        current = target.read_text(encoding="utf-8") if target.exists() else None
        if current != rendered:
            if args.check:
                mismatches.append(spec.path)
            else:
                target.write_text(rendered, encoding="utf-8")
                updated.append(spec.path)

    if args.check and mismatches:
        for path in mismatches:
            print(f"MISMATCH: {path} is out of sync with successor-shell adapter renderer")
        return 1

    if args.check:
        print("Successor-shell adapter veneers are in sync.")
    elif updated:
        print(f"Rendered {' '.join(updated)}")
    else:
        print("No adapter veneer changes required.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
