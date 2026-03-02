#!/usr/bin/env python3
"""Render harness-specific config artifacts from the repo source files."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def machine_index(machine_dir: Path) -> dict[str, dict]:
    index: dict[str, dict] = {}
    for path in sorted(machine_dir.glob("*.json")):
        data = load_json(path)
        data["_source"] = path.name
        for hostname in data.get("hostnames", []):
            index[hostname.lower()] = data
    return index


def render_target(repo_root: Path, harnesses: dict[str, dict], target: dict) -> tuple[str, str]:
    harness = harnesses[target["harness"]]
    parts = [repo_root / "AGENTS.md"]
    parts.extend(repo_root / source for source in harness.get("extension_sources", []))
    rendered = []
    for path in parts:
        rendered.append(path.read_text(encoding="utf-8").rstrip())
    return harness["generated_filename"], "\n\n".join(rendered).rstrip() + "\n"


def build_manifest(
    repo_root: Path,
    output_dir: Path,
    targets: list[dict],
    harnesses: dict[str, dict],
    machine: dict | None,
    hostname: str,
) -> dict:
    items = []
    root_outputs = machine.get("root_outputs", {}) if machine else {}
    openclaw_workspaces = machine.get("openclaw_workspaces", {}) if machine else {}
    for target in targets:
        harness = harnesses[target["harness"]]
        filename = harness["generated_filename"]
        relative_output = Path(target["agent"]) / filename
        item = {
            "agent": target["agent"],
            "harness": target["harness"],
            "generated": str(relative_output),
            "root_sync": bool(harness.get("root_sync")),
        }
        if target["agent"] in root_outputs:
            item["root_output"] = root_outputs[target["agent"]]
        if target["agent"] in openclaw_workspaces:
            item["openclaw_workspace"] = openclaw_workspaces[target["agent"]]
        items.append(item)
    return {
        "generated_at_host": hostname,
        "machine_manifest": machine.get("_source") if machine else None,
        "repo_root": str(repo_root),
        "outputs_root": str(output_dir),
        "targets": items,
    }


def write_root_outputs(output_dir: Path, manifest: dict):
    for item in manifest["targets"]:
        root_output = item.get("root_output")
        if not root_output:
            continue
        source = output_dir / item["generated"]
        target = Path(root_output)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="AGENTS.md")
    parser.add_argument("--harness-dir", default="harness")
    parser.add_argument("--machine-dir", default="machine")
    parser.add_argument("--output-dir", default="configs")
    parser.add_argument("--machine", required=True)
    parser.add_argument("--sync-root", action="store_true")
    args = parser.parse_args()

    repo_root = Path(args.source).resolve().parent
    harness_dir = repo_root / args.harness_dir
    machine_dir = repo_root / args.machine_dir
    output_dir = repo_root / args.output_dir

    harnesses = {
        path.stem: load_json(path)
        for path in sorted(harness_dir.glob("*.json"))
        if path.name != "targets.json"
    }
    targets = load_json(harness_dir / "targets.json")
    hostname = slugify(args.machine)
    machine = machine_index(machine_dir).get(hostname)

    for target in targets:
        filename, rendered = render_target(repo_root, harnesses, target)
        destination = output_dir / target["agent"] / filename
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(rendered, encoding="utf-8")

    manifest = build_manifest(repo_root, output_dir, targets, harnesses, machine, hostname)
    (output_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    if args.sync_root:
        write_root_outputs(output_dir, manifest)

    print(f"Rendered {len(targets)} targets for {hostname} into {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
