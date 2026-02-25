#!/usr/bin/env python3
"""protease_promote.py — Protease Protocol Phase 2: Promote Sovereign axioms.

Takes Sovereign-rewritten axioms and promotes them into praxis/canon,
updating atom lifecycle status in DYN-ATOM_INDEX.jsonl.

Part of the Protease Protocol (CC28 Adjudicator Spec 1).
"""

import argparse
import json
import os
import re
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

VALID_TRANSITIONS = {
    "pending":          {"queued"},
    "queued":           {"consumed"},
    "consumed":         {"promoted_praxis", "promoted_canon", "rejected"},
    "promoted_praxis":  {"promoted_canon"},
}

QUEUE_REL      = "orchestration/00-ORCHESTRATION/state/DYN-PROTEASE_QUEUE.jsonl"
ATOM_INDEX_REL = "sources/04-SOURCES/_meta/DYN-ATOM_INDEX.jsonl"
METRICS_JSONL  = "orchestration/00-ORCHESTRATION/state/DYN-PROTEASE_METRICS.jsonl"
METRICS_MD     = "orchestration/00-ORCHESTRATION/state/DYN-PROTEASE_METRICS.md"

TARGET_PATHS = {
    "praxis": "praxis/05-SIGMA/practice/PRAC-PROTEASE_AXIOMS.sn.md",
    "canon":  "canon/01-CANON/sn/CANON-PROTEASE_AXIOMS.sn.md",
}

SN_HEADERS = {
    "praxis": "# Protease Axioms — Praxis\n\n> Sovereign-distilled axioms promoted from atom triage.\n\n",
    "canon":  "# Protease Axioms — Canon\n\n> Sovereign-distilled axioms promoted to canonical status.\n\n",
}

# ---------------------------------------------------------------------------
# Axiom parser
# ---------------------------------------------------------------------------

_AXIOM_RE = re.compile(
    r"^##\s+Axiom:\s*(?P<title>.+?)$",
    re.MULTILINE,
)

def parse_axiom_file(path: Path) -> list[dict]:
    """Parse a Sovereign axiom markdown file into structured blocks."""
    text = path.read_text(encoding="utf-8")
    blocks: list[dict] = []
    splits = _AXIOM_RE.split(text)
    # splits: [preamble, title1, body1, title2, body2, ...]
    if len(splits) < 3:
        die(f"No axiom blocks found in {path}")
    for i in range(1, len(splits), 2):
        title = splits[i].strip()
        body = splits[i + 1] if i + 1 < len(splits) else ""
        block = _parse_block(title, body)
        blocks.append(block)
    return blocks


def _parse_block(title: str, body: str) -> dict:
    # Extract blockquote (the axiom text)
    bq_lines = [l.lstrip("> ").strip() for l in body.splitlines() if l.strip().startswith(">")]
    axiom_text = " ".join(bq_lines).strip()

    # Extract metadata fields
    source_ids = _extract_list(body, "source_atom_ids")
    why = _extract_value(body, "why_preserved")
    intention = _extract_value(body, "matched_intention")

    if not source_ids:
        die(f"Axiom '{title}' missing source_atom_ids")
    if not why:
        die(f"Axiom '{title}' missing why_preserved")

    return {
        "title": title,
        "axiom_text": axiom_text,
        "source_atom_ids": source_ids,
        "why_preserved": why,
        "matched_intention": intention or "NONE",
    }


def _extract_list(text: str, field: str) -> list[str]:
    m = re.search(rf"^\s*-\s*{field}:\s*\[(.+?)\]", text, re.MULTILINE)
    if not m:
        return []
    return [s.strip().strip("'\"") for s in m.group(1).split(",")]


def _extract_value(text: str, field: str) -> str:
    m = re.search(rf"^\s*-\s*{field}:\s*(.+)$", text, re.MULTILINE)
    return m.group(1).strip() if m else ""


# ---------------------------------------------------------------------------
# Index I/O (atomic write)
# ---------------------------------------------------------------------------

def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as e:
            die(f"JSONL parse error at {path}:{lineno}: {e}")
    return rows


def write_jsonl_atomic(path: Path, rows: list[dict]) -> None:
    """Write JSONL via temp file + atomic rename."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            for row in rows:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
        os.replace(tmp, path)
    except Exception:
        os.unlink(tmp)
        raise


def append_jsonl(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


# ---------------------------------------------------------------------------
# State machine
# ---------------------------------------------------------------------------

def validate_transition(current: str, desired: str, atom_id: str) -> None:
    allowed = VALID_TRANSITIONS.get(current, set())
    if desired not in allowed:
        die(f"Invalid transition for {atom_id}: {current} -> {desired}")


def transition_atoms(index_path: Path, atom_ids: list[str], target_status: str,
                     dry_run: bool) -> int:
    """Transition atoms in index. Returns count of atoms updated."""
    rows = load_jsonl(index_path)
    id_set = set(atom_ids)
    updated = 0
    now = datetime.now(timezone.utc).isoformat()

    for row in rows:
        if row.get("atom_id") in id_set:
            current = row.get("integration_status", "pending")
            # Two-step: first to consumed, then to promoted
            if current == "queued":
                validate_transition("queued", "consumed", row["atom_id"])
                row["integration_status"] = "consumed"
                current = "consumed"
            elif current == "pending":
                # pending -> queued -> consumed (fast-forward for atoms not yet queued)
                row["integration_status"] = "consumed"
                current = "consumed"

            validate_transition(current, target_status, row["atom_id"])
            row["integration_status"] = target_status
            row["integrated_at"] = now
            id_set.discard(row["atom_id"])
            updated += 1

    if id_set:
        print(f"WARNING: {len(id_set)} atom IDs not found in index: {sorted(id_set)[:5]}...",
              file=sys.stderr)

    if not dry_run:
        write_jsonl_atomic(index_path, rows)

    return updated


# ---------------------------------------------------------------------------
# SN file append
# ---------------------------------------------------------------------------

def ensure_sn_file(path: Path, target: str) -> None:
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(SN_HEADERS[target], encoding="utf-8")


def append_axioms_to_sn(path: Path, blocks: list[dict], dry_run: bool) -> str:
    """Append axiom blocks to SN file. Returns the text that would be appended."""
    parts: list[str] = []
    for b in blocks:
        parts.append(f"## Axiom: {b['title']}\n")
        parts.append(f"> {b['axiom_text']}\n")
        parts.append(f"- source_atom_ids: [{', '.join(b['source_atom_ids'])}]")
        parts.append(f"- why_preserved: {b['why_preserved']}")
        parts.append(f"- matched_intention: {b['matched_intention']}")
        parts.append(f"- promoted_at: {datetime.now(timezone.utc).strftime('%Y-%m-%d')}")
        parts.append("")

    text = "\n".join(parts)
    if not dry_run:
        with open(path, "a", encoding="utf-8") as f:
            f.write("\n" + text)
    return text


# ---------------------------------------------------------------------------
# Duplicate detection
# ---------------------------------------------------------------------------

def check_duplicates(sn_path: Path, blocks: list[dict]) -> None:
    """Hard fail if any source_atom_id already appears in the SN file."""
    if not sn_path.exists():
        return
    existing = sn_path.read_text(encoding="utf-8")
    for b in blocks:
        for aid in b["source_atom_ids"]:
            if aid in existing:
                die(f"Duplicate: atom {aid} already promoted in {sn_path.name}. "
                    f"Re-promotion violates state machine.")


# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------

def write_metrics(repo: Path, blocks: list[dict], target: str, atoms_updated: int,
                  dry_run: bool) -> None:
    all_atom_ids = []
    all_intentions = set()
    total_tokens = 0
    for b in blocks:
        all_atom_ids.extend(b["source_atom_ids"])
        if b["matched_intention"] != "NONE":
            all_intentions.add(b["matched_intention"])
        total_tokens += len(b["axiom_text"].split())

    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "atoms_in": len(all_atom_ids),
        "atoms_out": len(blocks),
        "compression_ratio": round(len(all_atom_ids) / max(len(blocks), 1), 2),
        "target_tier": target,
        "intention_coverage": sorted(all_intentions),
        "axiom_token_count": total_tokens,
    }

    metrics_jsonl = repo / METRICS_JSONL
    metrics_md = repo / METRICS_MD

    if not dry_run:
        append_jsonl(metrics_jsonl, record)

    # Rebuild human-readable metrics
    all_records = load_jsonl(metrics_jsonl) if metrics_jsonl.exists() else []
    if not dry_run:
        all_records.append(record)  # include current if not yet on disk
    else:
        all_records = [record]  # dry-run preview

    # Deduplicate (the append above + load may double-count)
    seen_ts = set()
    unique = []
    for r in all_records:
        if r["timestamp"] not in seen_ts:
            seen_ts.add(r["timestamp"])
            unique.append(r)

    md_lines = ["# Protease Metrics\n",
                f"*Last updated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}*\n",
                f"| Timestamp | Atoms In | Axioms Out | Ratio | Tier | Intentions | Tokens |",
                f"|-----------|----------|------------|-------|------|------------|--------|"]
    for r in unique:
        intents = ", ".join(r.get("intention_coverage", []))
        md_lines.append(
            f"| {r['timestamp'][:19]} | {r['atoms_in']} | {r['atoms_out']} | "
            f"{r['compression_ratio']} | {r['target_tier']} | {intents} | {r['axiom_token_count']} |"
        )
    md_lines.append("")

    if not dry_run:
        metrics_md.parent.mkdir(parents=True, exist_ok=True)
        metrics_md.write_text("\n".join(md_lines), encoding="utf-8")

    print(f"Metrics: {record['atoms_in']} atoms -> {record['atoms_out']} axioms "
          f"(ratio {record['compression_ratio']}), {record['axiom_token_count']} tokens, "
          f"tier={target}")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def die(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Protease Promote — promote Sovereign axioms into praxis/canon")
    parser.add_argument("--repo-root", required=True, type=Path,
                        help="Path to syncrescendence repo root")
    parser.add_argument("--axiom-file", required=True, type=Path,
                        help="Path to Sovereign-authored axiom markdown file")
    parser.add_argument("--target", required=True, choices=["praxis", "canon"],
                        help="Destination tier")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview without writing")
    args = parser.parse_args()

    repo = args.repo_root.resolve()
    axiom_path = args.axiom_file.resolve()

    # Validate inputs
    if not repo.is_dir():
        die(f"Repo root not found: {repo}")
    if not axiom_path.is_file():
        die(f"Axiom file not found: {axiom_path}")

    index_path = repo / ATOM_INDEX_REL
    if not index_path.exists():
        die(f"Atom index not found: {index_path}")

    sn_path = repo / TARGET_PATHS[args.target]
    target_status = f"promoted_{args.target}"

    # Parse axioms
    blocks = parse_axiom_file(axiom_path)
    print(f"Parsed {len(blocks)} axiom blocks from {axiom_path.name}")

    # Collect all atom IDs
    all_atom_ids = []
    for b in blocks:
        all_atom_ids.extend(b["source_atom_ids"])
    print(f"Referencing {len(all_atom_ids)} source atoms")

    # Duplicate check
    ensure_sn_file(sn_path, args.target)
    check_duplicates(sn_path, blocks)

    # Transition atoms in index
    updated = transition_atoms(index_path, all_atom_ids, target_status, args.dry_run)
    print(f"{'Would update' if args.dry_run else 'Updated'} {updated} atoms -> {target_status}")

    # Append to SN file
    text = append_axioms_to_sn(sn_path, blocks, args.dry_run)
    if args.dry_run:
        print(f"\n--- DRY RUN: would append to {sn_path.name} ---")
        print(text)
        print("--- END DRY RUN ---")
    else:
        print(f"Appended {len(blocks)} axioms to {sn_path.name}")

    # Write metrics
    write_metrics(repo, blocks, args.target, updated, args.dry_run)

    prefix = "[DRY RUN] " if args.dry_run else ""
    print(f"\n{prefix}Protease promote complete: {len(blocks)} axioms -> {args.target}")


if __name__ == "__main__":
    main()
