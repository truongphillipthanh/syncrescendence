#!/usr/bin/env python3
"""
memory_compaction.py — Weekly journal compaction, entity dedup, conflict detection.

DC-142: Memory compaction job for the Syncrescendence constellation.

Usage:
    memory_compaction.py compact journals [--agent <name>] [--dry-run]
    memory_compaction.py compact entities [--agent <name>] [--auto-merge]
    memory_compaction.py compact conflicts
    memory_compaction.py compact all [--dry-run]
"""
from config import *

import argparse
import json
import os
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

AGENTS = ["commander", "psyche", "ajna", "adjudicator", "cartographer"]


def find_repo_root() -> Path:
    """Walk up from script location to find repo root (contains AGENTS.md)."""
    p = Path(__file__).resolve().parent
    for _ in range(10):
        if (p / "AGENTS.md").exists():
            return p
        p = p.parent
    sys.exit("ERROR: Cannot find repo root (no AGENTS.md found)")


REPO = find_repo_root()


def agent_memory(agent: str) -> Path:
    return REPO / "agents" / agent / "memory"


def iso_week(ts_str: str) -> str:
    """Return YYYY-WNN from an ISO timestamp string."""
    dt = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
    year, week, _ = dt.isocalendar()
    return f"{year}-W{week:02d}"


def current_week() -> str:
    now = datetime.now(timezone.utc)
    year, week, _ = now.isocalendar()
    return f"{year}-W{week:02d}"


# ---------------------------------------------------------------------------
# Journal Compaction
# ---------------------------------------------------------------------------

def load_compaction_state(agent: str) -> dict:
    state_file = agent_memory(agent) / "sync" / "compaction_state.json"
    if state_file.exists():
        return json.loads(state_file.read_text())
    return {"compacted_weeks": [], "last_run": None}


def save_compaction_state(agent: str, state: dict):
    state_file = agent_memory(agent) / "sync" / "compaction_state.json"
    state_file.parent.mkdir(parents=True, exist_ok=True)
    state_file.write_text(json.dumps(state, indent=2) + "\n")


def compact_journals(agent: str, dry_run: bool = False) -> dict:
    """Compact completed weeks of journal JSONL into weekly digest files."""
    journal_dir = agent_memory(agent) / "journal"
    if not journal_dir.exists():
        return {"agent": agent, "status": "no_journal_dir", "weeks": []}

    state = load_compaction_state(agent)
    already_done = set(state.get("compacted_weeks", []))
    cur_week = current_week()

    # Collect all entries grouped by week
    weeks: dict[str, list[dict]] = defaultdict(list)
    jsonl_files = sorted(journal_dir.glob("*.jsonl"))

    for jf in jsonl_files:
        for line_num, line in enumerate(jf.read_text().splitlines(), 1):
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            ts = record.get("ts", "")
            if not ts:
                continue
            wk = iso_week(ts)
            record["_source_file"] = jf.name
            record["_source_line"] = line_num
            weeks[wk].append(record)

    # Process completed weeks only
    results = []
    for wk in sorted(weeks.keys()):
        if wk == cur_week:
            continue  # never compact current week
        if wk in already_done:
            continue

        entries = weeks[wk]
        digest_dir = journal_dir / "digest"
        digest_file = digest_dir / f"WEEK-{wk}.md"

        if dry_run:
            results.append({"week": wk, "entries": len(entries), "action": "would_compact"})
            continue

        digest_dir.mkdir(parents=True, exist_ok=True)

        # Build digest markdown
        lines = [
            f"# Weekly Journal Digest: {wk}",
            f"**Agent**: {agent}",
            f"**Entries**: {len(entries)}",
            f"**Compacted**: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}",
            "",
            "---",
            "",
        ]

        # Group by kind
        by_kind: dict[str, list[dict]] = defaultdict(list)
        for e in entries:
            by_kind[e.get("kind", "unknown")].append(e)

        for kind in sorted(by_kind.keys()):
            lines.append(f"## {kind.title()} ({len(by_kind[kind])})")
            lines.append("")
            for e in by_kind[kind]:
                ts_short = e.get("ts", "?")[:19]
                text = e.get("text", "(no text)")
                git_ref = e.get("refs", {}).get("git", "")
                ref_str = f" `{git_ref}`" if git_ref else ""
                lines.append(f"- **{ts_short}**{ref_str}: {text}")
            lines.append("")

        # UUID list for traceability
        lines.append("## Absorbed UUIDs")
        lines.append("")
        for e in entries:
            lines.append(f"- `{e.get('uuid', '?')}`")
        lines.append("")

        digest_file.write_text("\n".join(lines))
        already_done.add(wk)
        results.append({"week": wk, "entries": len(entries), "action": "compacted", "file": str(digest_file.relative_to(REPO))})

    # Save state
    if not dry_run:
        state["compacted_weeks"] = sorted(already_done)
        state["last_run"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        save_compaction_state(agent, state)

    return {"agent": agent, "status": "ok", "current_week": cur_week, "weeks": results}


# ---------------------------------------------------------------------------
# Entity Dedup
# ---------------------------------------------------------------------------

def normalize_entity_name(filename: str) -> str:
    """Strip .md, lowercase, collapse whitespace/hyphens/underscores."""
    name = filename.replace(".md", "")
    name = name.lower().replace("-", " ").replace("_", " ")
    return " ".join(name.split())


def compact_entities(agent: str, auto_merge: bool = False) -> dict:
    """Detect near-duplicate entity files within an agent's memory."""
    ent_dir = agent_memory(agent) / "entities"
    if not ent_dir.exists() or not any(ent_dir.glob("*.md")):
        return {"agent": agent, "status": "no_entities", "count": 0, "duplicates": []}

    files = sorted(ent_dir.glob("*.md"))
    # Group by normalized name
    groups: dict[str, list[Path]] = defaultdict(list)
    for f in files:
        groups[normalize_entity_name(f.name)].append(f)

    duplicates = []
    merged = 0
    for norm_name, paths in groups.items():
        if len(paths) < 2:
            continue

        # Check if content differs or only case differs
        contents = [p.read_text() for p in paths]
        names = [p.name for p in paths]
        content_identical = all(c == contents[0] for c in contents)
        case_only = len(set(n.lower() for n in names)) == 1

        dup_entry = {
            "normalized": norm_name,
            "files": names,
            "case_only_diff": case_only,
            "content_identical": content_identical,
        }

        if auto_merge and case_only and content_identical:
            # Keep the first file, remove others
            for p in paths[1:]:
                p.unlink()
            dup_entry["action"] = "auto_merged"
            merged += 1
        elif auto_merge and case_only and not content_identical:
            # Merge: concatenate into first file
            combined = contents[0]
            for extra in contents[1:]:
                # Only add lines not already present
                existing = set(combined.splitlines())
                for line in extra.splitlines():
                    if line not in existing:
                        combined += "\n" + line
                        existing.add(line)
            paths[0].write_text(combined)
            for p in paths[1:]:
                p.unlink()
            dup_entry["action"] = "auto_merged_content"
            merged += 1
        else:
            dup_entry["action"] = "flagged_for_review"

        duplicates.append(dup_entry)

    return {
        "agent": agent,
        "status": "ok",
        "count": len(files),
        "duplicates": duplicates,
        "auto_merged": merged,
    }


# ---------------------------------------------------------------------------
# Conflict Detection (Cross-Agent)
# ---------------------------------------------------------------------------

def detect_conflicts() -> dict:
    """Compare entity files across agents for conflicts and redundancies."""
    # Build entity index: norm_name -> [(agent, filename, content)]
    entity_index: dict[str, list[tuple[str, str, str]]] = defaultdict(list)

    for agent in AGENTS:
        ent_dir = agent_memory(agent) / "entities"
        if not ent_dir.exists():
            continue
        for f in ent_dir.glob("*.md"):
            norm = normalize_entity_name(f.name)
            entity_index[norm].append((agent, f.name, f.read_text()))

    conflicts = []
    redundants = []
    agent_counts = {}

    for agent in AGENTS:
        ent_dir = agent_memory(agent) / "entities"
        count = len(list(ent_dir.glob("*.md"))) if ent_dir.exists() else 0
        agent_counts[agent] = count

    for norm_name, entries in entity_index.items():
        if len(entries) < 2:
            continue

        agents_involved = [e[0] for e in entries]
        # Check if same agent appears multiple times (intra-agent dup, handled by entity dedup)
        if len(set(agents_involved)) < 2:
            continue

        contents = [e[2] for e in entries]
        content_identical = all(c == contents[0] for c in contents)

        if content_identical:
            redundants.append({
                "entity": norm_name,
                "agents": agents_involved,
                "files": [e[1] for e in entries],
                "type": "REDUNDANT",
            })
        else:
            # Extract differing lines for the report
            conflict_detail = []
            for agent_name, fname, content in entries:
                # First 5 non-empty lines as preview
                preview_lines = [l for l in content.splitlines() if l.strip()][:5]
                conflict_detail.append({
                    "agent": agent_name,
                    "file": fname,
                    "preview": preview_lines,
                })
            conflicts.append({
                "entity": norm_name,
                "agents": agents_involved,
                "type": "CONFLICT",
                "detail": conflict_detail,
            })

    return {
        "status": "ok",
        "agent_entity_counts": agent_counts,
        "conflicts": conflicts,
        "redundants": redundants,
        "total_cross_agent_entities": len([k for k, v in entity_index.items() if len(set(e[0] for e in v)) > 1]),
    }


# ---------------------------------------------------------------------------
# Report Formatting
# ---------------------------------------------------------------------------

def print_journal_report(results: list[dict]):
    print("\n=== Journal Compaction Report ===\n")
    for r in results:
        agent = r["agent"]
        status = r["status"]
        if status != "ok":
            print(f"  {agent}: {status}")
            continue
        weeks = r.get("weeks", [])
        if not weeks:
            print(f"  {agent}: nothing to compact (current week: {r.get('current_week', '?')})")
        else:
            print(f"  {agent}:")
            for w in weeks:
                action = w["action"]
                print(f"    {w['week']}: {w['entries']} entries — {action}")
                if "file" in w:
                    print(f"      → {w['file']}")
    print()


def print_entity_report(results: list[dict]):
    print("\n=== Entity Dedup Report ===\n")
    for r in results:
        agent = r["agent"]
        count = r.get("count", 0)
        dups = r.get("duplicates", [])
        merged = r.get("auto_merged", 0)
        print(f"  {agent}: {count} entities, {len(dups)} duplicate groups, {merged} auto-merged")
        for d in dups:
            files = ", ".join(d["files"])
            print(f"    [{d['action']}] {d['normalized']}: {files}")
    print()


def print_conflict_report(result: dict):
    print("\n=== Cross-Agent Conflict Report ===\n")
    counts = result.get("agent_entity_counts", {})
    for agent, count in counts.items():
        print(f"  {agent}: {count} entities")
    print()

    conflicts = result.get("conflicts", [])
    redundants = result.get("redundants", [])

    if conflicts:
        print(f"  CONFLICTS ({len(conflicts)}):")
        for c in conflicts:
            agents = ", ".join(c["agents"])
            print(f"    ⚠ {c['entity']} — agents: {agents}")
            for d in c.get("detail", []):
                print(f"      [{d['agent']}] {d['file']}:")
                for line in d.get("preview", [])[:3]:
                    print(f"        {line}")
        print()

    if redundants:
        print(f"  REDUNDANT ({len(redundants)}):")
        for r in redundants:
            agents = ", ".join(r["agents"])
            print(f"    = {r['entity']} — agents: {agents}")
        print()

    if not conflicts and not redundants:
        print("  No cross-agent conflicts or redundancies detected.")
        print()

    total = result.get("total_cross_agent_entities", 0)
    print(f"  Total entities shared across agents: {total}")
    print()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def resolve_agents(agent_arg: str | None) -> list[str]:
    if agent_arg:
        if agent_arg not in AGENTS:
            sys.exit(f"ERROR: Unknown agent '{agent_arg}'. Valid: {', '.join(AGENTS)}")
        return [agent_arg]
    return AGENTS


def main():
    parser = argparse.ArgumentParser(
        description="Memory compaction: journal digests, entity dedup, conflict detection."
    )
    sub = parser.add_subparsers(dest="command")

    # compact subcommand
    compact_parser = sub.add_parser("compact", help="Run compaction operations")
    compact_sub = compact_parser.add_subparsers(dest="target")

    # compact journals
    j_parser = compact_sub.add_parser("journals", help="Compact journal JSONL into weekly digests")
    j_parser.add_argument("--agent", type=str, default=None, help="Single agent name")
    j_parser.add_argument("--dry-run", action="store_true", help="Report without writing")

    # compact entities
    e_parser = compact_sub.add_parser("entities", help="Detect and merge duplicate entities")
    e_parser.add_argument("--agent", type=str, default=None, help="Single agent name")
    e_parser.add_argument("--auto-merge", action="store_true", help="Auto-merge safe duplicates")

    # compact conflicts
    compact_sub.add_parser("conflicts", help="Cross-agent conflict detection")

    # compact all
    a_parser = compact_sub.add_parser("all", help="Run all compaction operations")
    a_parser.add_argument("--agent", type=str, default=None, help="Single agent name")
    a_parser.add_argument("--dry-run", action="store_true", help="Report without writing")

    args = parser.parse_args()

    if args.command != "compact" or not args.target:
        parser.print_help()
        sys.exit(1)

    if args.target == "journals":
        agents = resolve_agents(args.agent)
        results = [compact_journals(a, dry_run=args.dry_run) for a in agents]
        print_journal_report(results)

    elif args.target == "entities":
        agents = resolve_agents(args.agent)
        results = [compact_entities(a, auto_merge=args.auto_merge) for a in agents]
        print_entity_report(results)

    elif args.target == "conflicts":
        result = detect_conflicts()
        print_conflict_report(result)

    elif args.target == "all":
        agents = resolve_agents(getattr(args, "agent", None))
        dry_run = getattr(args, "dry_run", False)

        j_results = [compact_journals(a, dry_run=dry_run) for a in agents]
        print_journal_report(j_results)

        e_results = [compact_entities(a, auto_merge=False) for a in agents]
        print_entity_report(e_results)

        c_result = detect_conflicts()
        print_conflict_report(c_result)


if __name__ == "__main__":
    main()
