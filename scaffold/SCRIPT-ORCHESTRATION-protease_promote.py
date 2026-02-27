#!/usr/bin/env python3
"""protease_promote.py — Protease Protocol Phase 2: Promote Sovereign axioms.

Takes Sovereign-rewritten axioms and promotes them into praxis/canon,
updating atom lifecycle status in DYN-ATOM_INDEX.jsonl.

Part of the Protease Protocol (CC28 Adjudicator Spec 1).
"""

import argparse
import fcntl
import json
import os
import re
import subprocess
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
REANNEAL_QUEUE = "orchestration/00-ORCHESTRATION/state/DYN-REANNEAL_QUEUE.jsonl"

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
# Lattice Annealer Gate (v2 — CC37)
# ---------------------------------------------------------------------------

SCRIPTS_DIR = Path(__file__).parent

def run_annealer_gate(block: dict, repo: Path, skip: bool = False) -> dict:
    """Run candidate_adapter + lattice_annealer as pre-promotion gate.

    Returns {"decision": "PROMOTE"|"ADJUST"|"REJECT", "justification": {...}, ...}
    If skip=True, returns synthetic PROMOTE (with warning).
    """
    if skip:
        print("WARNING: --skip-annealer active. CANON-ONTOLOGY-GATE_v2 requires annealer.",
              file=sys.stderr)
        return {"decision": "PROMOTE", "justification": {"reason_codes": ["ANNEALER_SKIPPED"]}}

    adapter_script = SCRIPTS_DIR / "candidate_adapter.py"
    annealer_script = SCRIPTS_DIR / "lattice_annealer.py"

    for script in (adapter_script, annealer_script):
        if not script.exists():
            die(f"Annealer gate: missing {script.name}. Cannot promote without v2 gate.")

    # Build adapter input from block — preserve full lineage per ARCH-CANDIDATE_ADAPTER_CONTRACT
    primary_id = block["source_atom_ids"][0] if block["source_atom_ids"] else block["title"]
    adapter_input = {
        "atom_id": primary_id,
        "source_atom_ids": list(block["source_atom_ids"]),  # full lineage, not just [0]
        "source_file": "",
        "content": block["axiom_text"],
        "origin_hash": "",
        "axiom_alignment_score": 0.9,
        "terminal_domain": "",
        "matched_intention": block.get("matched_intention", "NONE"),
        "drift_score": 0.0,
    }

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f_in:
        json.dump(adapter_input, f_in)
        input_path = f_in.name
    output_path = input_path + ".adapted.json"

    try:
        # Step 1: Adapt
        r = subprocess.run(
            [sys.executable, str(adapter_script),
             "--repo-root", str(repo),
             "--input-json", input_path,
             "--output-json", output_path],
            capture_output=True, text=True, timeout=30)
        if r.returncode != 0:
            die(f"candidate_adapter failed: {r.stderr.strip()}")

        # Step 2: Anneal
        r = subprocess.run(
            [sys.executable, str(annealer_script),
             "--repo-root", str(repo),
             "--candidate-json", output_path,
             "--mode", "gate"],
            capture_output=True, text=True, timeout=60)
        if r.returncode != 0:
            die(f"lattice_annealer failed: stderr={r.stderr.strip()} stdout={r.stdout[:300]}")

        # Parse annealer stdout JSON
        result = json.loads(r.stdout)
        return result

    except subprocess.TimeoutExpired:
        die("Annealer gate timed out")
    except json.JSONDecodeError:
        die(f"Annealer returned invalid JSON: {r.stdout[:200]}")
    finally:
        for p in (input_path, output_path):
            try:
                os.unlink(p)
            except OSError:
                pass


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
    parser.add_argument("--skip-annealer", action="store_true",
                        help="Skip lattice annealer gate (v2 requires it — use only for testing)")
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

    # Acquire LOCK_CANON_PROMOTION for the entire critical section (order 1 per hierarchy)
    lock_dir = repo / "orchestration" / "00-ORCHESTRATION" / "state" / "locks"
    lock_dir.mkdir(parents=True, exist_ok=True)
    canon_lock_path = lock_dir / "LOCK_CANON_PROMOTION.lock"
    canon_lock_fd = None

    if args.target == "canon" and not args.dry_run:
        canon_lock_fd = open(canon_lock_path, "w")
        try:
            fcntl.flock(canon_lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            canon_lock_fd.write(str(os.getpid()))
            canon_lock_fd.flush()
        except OSError:
            canon_lock_fd.close()
            die("LOCK_CANON_PROMOTION held by another process. Concurrent canon promotion blocked.")

    try:
        # Duplicate check
        ensure_sn_file(sn_path, args.target)
        check_duplicates(sn_path, blocks)

        # Lattice Annealer Gate (v2 — mandatory for canon promotion)
        # Per CANON-ONTOLOGY-GATE_v2.md Rules 6/7: ADJUST is iterative (max 3),
        # not an immediate batch abort. Only REJECT hard-blocks an atom.
        quarantined = []
        rejected = []
        promotable_blocks = []
        if args.target == "canon":
            for b in blocks:
                result = run_annealer_gate(b, repo, skip=args.skip_annealer)
                decision = result.get("decision", "REJECT")
                justification = result.get("justification", {})
                if decision == "PROMOTE":
                    print(f"  ANNEAL PASS: {b['title']} (coherence={justification.get('coherence_score', '?')})")
                    promotable_blocks.append(b)
                elif decision == "ADJUST":
                    repair = result.get("repair_prompt", "")
                    iteration = result.get("justification", {}).get("iteration_count", 0)
                    primary_id = b["source_atom_ids"][0] if b["source_atom_ids"] else b["title"]
                    print(f"  ANNEAL ADJUST: {b['title']} — quarantined for reanneal (iteration {iteration + 1}). "
                          f"Repair: {repair[:120]}...", file=sys.stderr)
                    quarantined.append(b["title"])
                    # Queue for reanneal per CC38 Adjudicator contract
                    if not args.skip_annealer and not args.dry_run:
                        reanneal_entry = {
                            "atom_id": primary_id,
                            "source_atom_ids": list(b["source_atom_ids"]),
                            "title": b["title"],
                            "repair_prompt": repair,
                            "iteration_count": iteration + 1,
                            "status": "QUARANTINED_ADJUST_PENDING",
                            "queued_at": datetime.now(timezone.utc).isoformat(),
                        }
                        append_jsonl(repo / REANNEAL_QUEUE, reanneal_entry)
                else:
                    codes = justification.get("reason_codes", [])
                    print(f"  ANNEAL REJECT: {b['title']} — {codes}", file=sys.stderr)
                    rejected.append(b["title"])
            if rejected and not args.skip_annealer:
                die(f"Annealer rejected {len(rejected)} axiom(s): {rejected}. "
                    f"Fix and retry, or use --skip-annealer for testing.")
            blocks = promotable_blocks
        else:
            promotable_blocks = blocks

        # Recollect atom IDs from promotable blocks only (quarantined atoms excluded)
        all_atom_ids = []
        for b in blocks:
            all_atom_ids.extend(b["source_atom_ids"])

        # Transition atoms in index
        updated = transition_atoms(index_path, all_atom_ids, target_status, args.dry_run)
        print(f"{'Would update' if args.dry_run else 'Updated'} {updated} atoms -> {target_status}")

        # Append to SN file (inside lock for canon atomicity)
        text = append_axioms_to_sn(sn_path, blocks, args.dry_run)
        if args.dry_run:
            print(f"\n--- DRY RUN: would append to {sn_path.name} ---")
            print(text)
            print("--- END DRY RUN ---")
        else:
            print(f"Appended {len(blocks)} axioms to {sn_path.name}")

        # Write metrics
        write_metrics(repo, blocks, args.target, updated, args.dry_run)

        # Post-promotion fusion hook (inside LOCK_CANON_PROMOTION)
        try:
            from fusion_operator import run_fusion
            fusion_result = run_fusion(repo, dry_run=args.dry_run)
            if fusion_result.get("fusions", 0) > 0:
                print(f"\nFusion pass: {fusion_result['fusions']} cluster(s) fused.")
            elif fusion_result.get("status") == "SKIPPED":
                print(f"\nFusion skipped: {fusion_result.get('reason', 'below threshold')}")
        except ImportError:
            pass  # fusion_operator not available — non-fatal
        except Exception as e:
            print(f"\nWARNING: Fusion pass failed (non-fatal): {e}", file=sys.stderr)

        prefix = "[DRY RUN] " if args.dry_run else ""
        print(f"\n{prefix}Protease promote complete: {len(blocks)} axioms -> {args.target}")
        if quarantined:
            print(f"\nWARNING: {len(quarantined)} atom(s) quarantined (ADJUST — pending reanneal): "
                  f"{quarantined}", file=sys.stderr)
            print(f"Reanneal queue: {repo / REANNEAL_QUEUE}", file=sys.stderr)
    finally:
        if canon_lock_fd is not None:
            fcntl.flock(canon_lock_fd, fcntl.LOCK_UN)
            canon_lock_fd.close()


if __name__ == "__main__":
    main()
