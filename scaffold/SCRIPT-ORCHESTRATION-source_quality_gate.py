#!/usr/bin/env python3
"""DC-208-6 Source Quality Gate — main runner.

Evaluates extracted knowledge atoms against 4+1 quality gates:
  1. Coverage: key insights mapped to canon
  2. Graph density: bidirectional relations from source atoms
  3. Praxis linkage: test artifacts linked
  4. Logical consistency: contradiction score <= threshold
  5. Surprise x Precision: alert scoring for novel high-value atoms

Usage:
    python3 source_quality_gate.py --extract-jsonl EXTRACT-*.jsonl \\
        [--canon-dir canon/] [--praxis-dir praxis/] \\
        [--graph-state DYN-KNOWLEDGE_GRAPH.json] \\
        [--out-dir sources/04-SOURCES/_meta] [--verbose]
"""
from __future__ import annotations
from config import *

import argparse
import glob
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")

from source_quality_metrics import (
    AtomMetrics,
    batch_encode_atoms,
    evaluate_atom,
    load_canon_embeddings,
    load_praxis_cache,
)


def load_atoms(jsonl_paths: list[str]) -> list[dict]:
    """Load atoms from one or more JSONL files.

    Args:
        jsonl_paths: List of file paths (supports glob patterns).

    Returns:
        List of atom dicts parsed from all files.
    """
    atoms: list[dict] = []
    expanded: list[str] = []
    for pattern in jsonl_paths:
        matches = sorted(glob.glob(pattern))
        if not matches:
            print(f"WARNING: no files matched pattern '{pattern}'", file=sys.stderr)
        expanded.extend(matches)

    for path in expanded:
        with open(path) as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    atom = json.loads(line)
                    if "atom_id" not in atom or "content" not in atom:
                        print(f"WARNING: {path}:{lineno} missing atom_id/content, skipping",
                              file=sys.stderr)
                        continue
                    atom["_source_file"] = path
                    atoms.append(atom)
                except json.JSONDecodeError as e:
                    print(f"WARNING: {path}:{lineno} JSON error: {e}", file=sys.stderr)
    return atoms


def load_graph_state(path: str | None) -> dict | None:
    """Load graph state JSON if available."""
    if path is None:
        return None
    p = Path(path)
    if not p.exists():
        print(f"INFO: graph state file not found: {path}", file=sys.stderr)
        return None
    try:
        return json.loads(p.read_text())
    except (json.JSONDecodeError, OSError) as e:
        print(f"WARNING: could not load graph state: {e}", file=sys.stderr)
        return None


def load_triage(meta_dir: Path) -> dict | None:
    """Load source triage scores if available."""
    triage_path = meta_dir / "DYN-SOURCE_TRIAGE.json"
    if not triage_path.exists():
        return None
    try:
        return json.loads(triage_path.read_text())
    except (json.JSONDecodeError, OSError):
        return None


def write_results_jsonl(results: list[AtomMetrics], out_path: Path) -> None:
    """Write per-atom gate results as JSONL."""
    with open(out_path, "w") as f:
        for m in results:
            f.write(json.dumps(m.to_dict(), default=str) + "\n")


def write_alerts_md(results: list[AtomMetrics], out_path: Path,
                    total_atoms: int) -> None:
    """Write human-readable alert summary as Markdown."""
    critical = [m for m in results if m.alert_band == "CRITICAL"]
    review = [m for m in results if m.alert_band == "REVIEW"]
    ignore_count = total_atoms - len(critical) - len(review)

    # Gate summary
    gate_names = ["coverage", "graph_density", "praxis", "consistency"]
    gate_pass = {g: 0 for g in gate_names}
    gate_fail = {g: 0 for g in gate_names}
    gate_skip = {g: 0 for g in gate_names}
    for m in results:
        for g in gate_names:
            status = m.gates.get(g, "")
            if status.startswith("PASS"):
                gate_pass[g] += 1
            elif status.startswith("FAIL"):
                gate_fail[g] += 1
            elif status.startswith("SKIPPED"):
                gate_skip[g] += 1

    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines = [
        f"# Quality Gate Results",
        f"",
        f"**Generated**: {ts}",
        f"**Total atoms evaluated**: {total_atoms}",
        f"",
        f"## Gate Summary",
        f"",
        f"| Gate | Pass | Fail | Skipped |",
        f"|------|------|------|---------|",
    ]
    for g in gate_names:
        lines.append(f"| {g} | {gate_pass[g]} | {gate_fail[g]} | {gate_skip[g]} |")

    lines += [
        f"",
        f"## Alert Distribution",
        f"",
        f"| Band | Count |",
        f"|------|-------|",
        f"| CRITICAL | {len(critical)} |",
        f"| REVIEW | {len(review)} |",
        f"| IGNORE | {ignore_count} |",
        f"",
    ]

    if critical:
        lines.append("## CRITICAL Alerts")
        lines.append("")
        for m in sorted(critical, key=lambda x: -x.alert_score):
            lines.append(f"### {m.atom_id} (score: {m.alert_score:.3f})")
            lines.append(f"- Surprise: {m.surprise:.3f} (novelty={m.novelty:.3f}, "
                         f"belief_violation={m.belief_violation:.3f})")
            lines.append(f"- Precision: {m.precision:.3f} (evidence={m.evidence_coverage:.3f}, "
                         f"reliability={m.source_reliability:.3f}, "
                         f"cross_source={m.cross_source_support:.3f}, "
                         f"falsifiability={m.falsifiability_score:.3f})")
            lines.append(f"- Gates: {m.gates}")
            lines.append("")

    if review:
        lines.append("## REVIEW Alerts")
        lines.append("")
        for m in sorted(review, key=lambda x: -x.alert_score)[:20]:
            lines.append(f"- **{m.atom_id}** — score: {m.alert_score:.3f} "
                         f"(surprise={m.surprise:.3f}, precision={m.precision:.3f})")
        if len(review) > 20:
            lines.append(f"- ... and {len(review) - 20} more")
        lines.append("")

    out_path.write_text("\n".join(lines) + "\n")


def run_quality_gate(
    extract_patterns: list[str],
    canon_dir: str = "canon/",
    praxis_dir: str | None = "praxis/",
    graph_state_path: str | None = None,
    out_dir: str = "sources/04-SOURCES/_meta",
    coverage_threshold: float = 0.45,
    graph_density_threshold: int = 8,
    praxis_threshold: int = 2,
    consistency_threshold: float = 0.12,
    verbose: bool = False,
) -> list[AtomMetrics]:
    """Run the full quality gate pipeline.

    Args:
        extract_patterns: Glob patterns for EXTRACT JSONL files.
        canon_dir: Path to canon directory for embeddings.
        praxis_dir: Path to praxis directory (None to skip Gate 3).
        graph_state_path: Path to knowledge graph JSON (None to skip Gate 2).
        out_dir: Output directory for results files.
        coverage_threshold: Cosine sim threshold for Gate 1.
        graph_density_threshold: Min relations for Gate 2.
        praxis_threshold: Min praxis links for Gate 3.
        consistency_threshold: Max contradiction score for Gate 4.
        verbose: Print per-atom progress.

    Returns:
        List of AtomMetrics for all evaluated atoms.
    """
    # Load inputs
    atoms = load_atoms(extract_patterns)
    if not atoms:
        print("ERROR: no atoms loaded from extract files", file=sys.stderr)
        return []

    print(f"Loaded {len(atoms)} atoms from extract files", flush=True)

    canon_path = Path(canon_dir)
    if not canon_path.exists():
        print(f"WARNING: canon dir not found: {canon_dir}", file=sys.stderr)

    print("Loading canon embeddings...")
    canon_embs, canon_texts = load_canon_embeddings(canon_path)
    print(f"  {len(canon_texts)} canon paragraphs embedded", flush=True)

    graph_state = load_graph_state(graph_state_path)
    praxis_path = Path(praxis_dir) if praxis_dir else None
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    triage = load_triage(out_path)

    # Pre-load praxis files into memory once (avoids N*M disk reads)
    print("Loading praxis cache...", flush=True)
    praxis_cache = load_praxis_cache(praxis_path)
    if praxis_cache is not None:
        print(f"  {len(praxis_cache)} praxis files cached in memory", flush=True)
    else:
        print("  praxis cache skipped (no praxis dir)", flush=True)

    # Batch-encode all atom contents (single pass, huge speedup vs per-atom)
    print("Batch-encoding atom embeddings...", flush=True)
    atom_embs = batch_encode_atoms(atoms)
    print(f"  Encoded {atom_embs.shape[0]} atoms ({atom_embs.shape[1]}d)", flush=True)

    # Evaluate each atom
    results: list[AtomMetrics] = []
    for i, atom in enumerate(atoms):
        if verbose and (i % 1000 == 0 or i == len(atoms) - 1):
            print(f"  [{i+1}/{len(atoms)}] {atom['atom_id']}", flush=True)
        m = evaluate_atom(
            atom, canon_embs, canon_texts, graph_state, praxis_path,
            triage, atoms,
            coverage_threshold=coverage_threshold,
            graph_density_threshold=graph_density_threshold,
            praxis_threshold=praxis_threshold,
            consistency_threshold=consistency_threshold,
            praxis_cache=praxis_cache,
            atom_emb=atom_embs[i],
            all_atom_embs=atom_embs,
            atom_index=i,
        )
        results.append(m)

    # Write outputs
    jsonl_out = out_path / "DYN-QUALITY_GATE_RESULTS.jsonl"
    write_results_jsonl(results, jsonl_out)
    print(f"Wrote {len(results)} results to {jsonl_out}")

    alerts_out = out_path / "DYN-QUALITY_ALERTS.md"
    write_alerts_md(results, alerts_out, len(atoms))
    print(f"Wrote alerts summary to {alerts_out}")

    # Print summary
    bands = {"CRITICAL": 0, "REVIEW": 0, "IGNORE": 0}
    for m in results:
        bands[m.alert_band] = bands.get(m.alert_band, 0) + 1
    print(f"\nAlert distribution: {bands}")

    return results


def main() -> None:
    parser = argparse.ArgumentParser(
        description="DC-208-6 Source Quality Gate",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--extract-jsonl", nargs="+", required=True,
        help="EXTRACT JSONL file paths or glob patterns",
    )
    parser.add_argument(
        "--canon-dir", default="canon/",
        help="Canon directory for embeddings (default: canon/)",
    )
    parser.add_argument(
        "--praxis-dir", default="praxis/",
        help="Praxis directory for Gate 3 (default: praxis/)",
    )
    parser.add_argument(
        "--graph-state", default=None,
        help="Knowledge graph JSON for Gate 2 (default: skip)",
    )
    parser.add_argument(
        "--out-dir", default="sources/04-SOURCES/_meta",
        help="Output directory (default: sources/04-SOURCES/_meta)",
    )
    parser.add_argument("--verbose", action="store_true", help="Per-atom progress")
    parser.add_argument(
        "--coverage-threshold", type=float, default=0.45,
        help="Cosine similarity threshold for Gate 1 (default: 0.45)",
    )
    parser.add_argument(
        "--graph-density-threshold", type=int, default=8,
        help="Min relations for Gate 2 (default: 8)",
    )
    parser.add_argument(
        "--praxis-threshold", type=int, default=2,
        help="Min praxis links for Gate 3 (default: 2)",
    )
    parser.add_argument(
        "--consistency-threshold", type=float, default=0.12,
        help="Max contradiction score for Gate 4 (default: 0.12)",
    )

    args = parser.parse_args()

    run_quality_gate(
        extract_patterns=args.extract_jsonl,
        canon_dir=args.canon_dir,
        praxis_dir=args.praxis_dir,
        graph_state_path=args.graph_state,
        out_dir=args.out_dir,
        coverage_threshold=args.coverage_threshold,
        graph_density_threshold=args.graph_density_threshold,
        praxis_threshold=args.praxis_threshold,
        consistency_threshold=args.consistency_threshold,
        verbose=args.verbose,
    )


if __name__ == "__main__":
    main()
