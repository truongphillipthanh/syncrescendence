#!/usr/bin/env python3
"""Generate comparative manifests for archived predecessor shells."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUT = REPO_ROOT / "pedigree" / "archive-manifests"

DISPOSITION_RULES = {
    "communications": {
        "communications": "live-communications",
        "-INBOX": "communications-pedigree",
        "-OUTBOX": "communications-pedigree",
        "-OUTGOING": "communications-pedigree",
        "engine": "communications-pedigree",
        "ascertescence": "communications-pedigree",
        "collab": "communications-pedigree",
    },
    "executive": {
        "executive": "live-executive",
        "-SOVEREIGN": "executive-pedigree",
    },
    "program": {
        "program": "live-program",
        "00-ORCHESTRATION": "program-or-runtime-pedigree",
        "orchestration": "program-or-runtime-pedigree",
    },
    "office-playbook": {
        "offices": "live-office",
        "playbooks": "live-playbook",
        "agents": "office-or-playbook-pedigree",
        "praxis": "playbook-pedigree",
        "openclaw": "playbook-or-runtime-pedigree",
    },
    "knowledge-pedigree": {
        "pedigree": "live-pedigree",
        "canon": "pedigree-or-knowledge-archive",
        "01-CANON": "pedigree-or-knowledge-archive",
        "corpus": "knowledge-archive",
        "neocorpus": "knowledge-reference",
        "sources": "knowledge-feedstock",
        "04-SOURCES": "knowledge-feedstock",
        "05-SIGMA": "playbook-or-knowledge-pedigree",
    },
    "operator-runtime": {
        "operators": "live-operator",
        "validated-patterns": "live-validated-patterns",
        "scripts": "operator-pedigree",
        "runtime": "live-runtime",
        "memory": "runtime-pedigree",
        "machine": "operator-or-runtime-pedigree",
        "harness": "operator-or-playbook-pedigree",
        "configs": "operator-pedigree",
        "CLI-WEB-GAP": "validated-patterns-or-operator-pedigree",
        ".openclaw": "runtime-local-state",
        ".claude": "runtime-local-state",
        ".constellation": "runtime-local-state",
        ".obsidian": "runtime-local-state",
        ".gemini": "runtime-local-state",
        ".env.graphiti": "runtime-local-state",
    },
}

DIRECT_RULES = {
    "README.md": "root-explanation",
    "AGENTS.md": "constitution-pedigree",
    "CLAUDE.md": "constitution-pedigree",
    "GEMINI.md": "constitution-pedigree",
    "Makefile": "operator-pedigree",
}

IGNORE = {".git", ".DS_Store", "__pycache__", ".gitattributes", ".github", ".gitignore", "..bfg-report"}


@dataclass
class EntryRecord:
    name: str
    kind: str
    disposition: str
    rationale: str


def classify(name: str, is_dir: bool) -> tuple[str, str]:
    if name in DIRECT_RULES:
        return DIRECT_RULES[name], "directly mapped by name"

    if name.startswith("neosyncrescendence_root_cutover_snapshot_"):
        return "archive-snapshot", "successor-shell snapshot preserved as cutover provenance"
    if name.startswith("root_offload_tranche_"):
        return "archive-tranche", "offloaded predecessor payload preserved as tranche archive"

    for family, rules in DISPOSITION_RULES.items():
        if name in rules:
            return rules[name], f"{family} family mapping"

    if name in {"02-ENGINE", "engine"}:
        return "communications-pedigree", "engine treated as prompt/spec/response lineage pedigree"

    if is_dir and name.startswith("."):
        return "runtime-local-state", "hidden directory treated as local/runtime state"
    if not is_dir and name.endswith((".md", ".txt")):
        return "pedigree-review", "top-level document requires hermeneutic review before promotion"
    if not is_dir and name.endswith((".py", ".sh", ".sql", ".toml", ".xml", ".json")):
        return "operator-review", "top-level executable or config requires operator-law review"
    return "unclassified", "no rule yet"


def manifest_for(root: Path, label: str) -> dict[str, object]:
    entries = []
    for path in sorted(root.iterdir(), key=lambda p: p.name.lower()):
        if path.name in IGNORE:
            continue
        disposition, rationale = classify(path.name, path.is_dir())
        entries.append(
            EntryRecord(
                name=path.name,
                kind="directory" if path.is_dir() else "file",
                disposition=disposition,
                rationale=rationale,
            )
        )

    summary: dict[str, int] = {}
    for entry in entries:
        summary[entry.disposition] = summary.get(entry.disposition, 0) + 1

    return {
        "label": label,
        "root": str(root),
        "entry_count": len(entries),
        "summary": dict(sorted(summary.items())),
        "entries": [asdict(entry) for entry in entries],
    }


def render_markdown(report: dict[str, object]) -> str:
    lines = [
        f"# Archive Shell Manifest: {report['label']}",
        "",
        f"- root: [{report['root']}]({report['root']})",
        f"- top-level entries: {report['entry_count']}",
        "",
        "## Disposition Summary",
        "",
    ]
    for key, value in report["summary"].items():
        lines.append(f"- `{key}`: {value}")
    lines.extend(["", "## Top-Level Entry Classification", ""])
    for entry in report["entries"]:
        lines.append(
            f"- `{entry['name']}` ({entry['kind']}): `{entry['disposition']}` — {entry['rationale']}"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--label", required=True)
    parser.add_argument("--out-dir", default=str(DEFAULT_OUT))
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    out_dir = Path(args.out_dir).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    report = manifest_for(root, args.label)
    (out_dir / f"{args.label}.json").write_text(json.dumps(report, indent=2) + "\n")
    (out_dir / f"{args.label}.md").write_text(render_markdown(report))
    print(out_dir / f"{args.label}.json")
    print(out_dir / f"{args.label}.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
