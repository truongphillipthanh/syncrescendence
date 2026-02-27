#!/usr/bin/env python3
"""fusion_operator.py — Semantic compression via merged reason class (CC38 Spec 4).

Consumes N lower-order canon axioms, produces 1 hyper-dense successor,
tombstones merged members, queues dependents for reanneal.

Called by protease_promote.py post-promotion, or standalone via --force-fusion.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "1.0.0"
STATE_REL = "orchestration/00-ORCHESTRATION/state"
FUSION_LEDGER_REL = f"{STATE_REL}/DYN-FUSION_LEDGER.jsonl"
APOPTOSIS_LEDGER_REL = f"{STATE_REL}/DYN-APOPTOSIS_LEDGER.jsonl"
REANNEAL_QUEUE_REL = f"{STATE_REL}/DYN-REANNEAL_QUEUE.jsonl"
LATTICE_INDEX_REL = f"{STATE_REL}/DYN-LATTICE_INDEX.json"
PROMOTION_METRICS_REL = f"{STATE_REL}/DYN-PROMOTION_METRICS.jsonl"

DEFAULT_TRIGGER_THRESHOLD = 5
DEFAULT_MAX_FUSIONS_PER_RUN = 3
DEFAULT_MIN_CLUSTER_SIZE = 2
DEFAULT_MIN_MERGE_QUALITY = 0.4


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return rows


def append_jsonl(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=True, sort_keys=True) + "\n")


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def write_json_atomic(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    tmp.rename(path)


def count_tokens(text: str) -> int:
    """Rough token count: whitespace-delimited words."""
    return len(text.split())


def cosine_similarity(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    ma = math.sqrt(sum(x * x for x in a)) or 1e-9
    mb = math.sqrt(sum(x * x for x in b)) or 1e-9
    return dot / (ma * mb)


def jaccard(a: set, b: set) -> float:
    if not a and not b:
        return 0.0
    return len(a & b) / len(a | b)


# ---------------------------------------------------------------------------
# Cluster detection
# ---------------------------------------------------------------------------

def build_clusters(
    axioms: list[dict],
    min_quality: float = DEFAULT_MIN_MERGE_QUALITY,
    min_size: int = DEFAULT_MIN_CLUSTER_SIZE,
) -> list[list[dict]]:
    """Find merge-eligible clusters from axiom list.

    Uses Rosetta term overlap + dimension vector similarity to identify
    semantically overlapping axioms that could fuse.
    """
    n = len(axioms)
    if n < min_size:
        return []

    # Pairwise similarity matrix
    sim = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            ti = set(axioms[i].get("rosetta_terms", []))
            tj = set(axioms[j].get("rosetta_terms", []))
            jac = jaccard(ti, tj)

            di = axioms[i].get("dimension_vector") or {}
            dj = axioms[j].get("dimension_vector") or {}
            dim_keys = sorted(set(di.keys()) | set(dj.keys()))
            vi = [float(di.get(k, 0.0)) for k in dim_keys]
            vj = [float(dj.get(k, 0.0)) for k in dim_keys]
            cos = cosine_similarity(vi, vj) if dim_keys else 0.0

            sim[i][j] = sim[j][i] = 0.5 * jac + 0.5 * max(0.0, cos)

    # Greedy single-linkage clustering
    assigned = [False] * n
    clusters: list[list[int]] = []
    for i in range(n):
        if assigned[i]:
            continue
        cluster = [i]
        assigned[i] = True
        for j in range(i + 1, n):
            if assigned[j]:
                continue
            if any(sim[j][k] >= min_quality for k in cluster):
                cluster.append(j)
                assigned[j] = True
        if len(cluster) >= min_size:
            clusters.append(cluster)

    return [[axioms[i] for i in c] for c in clusters]


# ---------------------------------------------------------------------------
# Fusion execution
# ---------------------------------------------------------------------------

def fuse_cluster(cluster: list[dict]) -> tuple[dict, list[dict], float]:
    """Fuse a cluster of axioms into one successor + tombstones.

    Returns (successor, tombstones, binding_energy).
    """
    # Generate successor ID from first member
    base_id = cluster[0].get("node_id", cluster[0].get("atom_id", "FUSED"))
    successor_id = f"FUSED-{base_id}-{len(cluster)}"

    # Merge content
    contents = [a.get("content", "") for a in cluster]
    total_tokens = sum(count_tokens(c) for c in contents)

    # Merge Rosetta terms (union)
    all_terms = set()
    for a in cluster:
        all_terms.update(a.get("rosetta_terms", []))

    # Average dimension vectors
    dim_keys = list((cluster[0].get("dimension_vector") or {}).keys())
    if dim_keys:
        avg_vec = {}
        for k in dim_keys:
            vals = [float(a.get("dimension_vector", {}).get(k, 0.0)) for a in cluster]
            avg_vec[k] = round(sum(vals) / len(vals), 6)
    else:
        avg_vec = {}

    # Merge adjacency (union minus merged members)
    member_ids = {a.get("node_id", a.get("atom_id", "")) for a in cluster}
    all_adj = set()
    for a in cluster:
        all_adj.update(a.get("adjacency", []))
    all_adj -= member_ids

    # Successor content: condensed summary (not full concatenation — that's the point of fusion)
    # In production, an LLM would generate the compressed axiom.
    # Mechanically, we produce a structured fusion stub for human/LLM rewrite.
    successor_content = (
        f"# {successor_id}\n\n"
        f"**Fusion of {len(cluster)} axioms**: {', '.join(sorted(member_ids))}.\n\n"
        f"**Unified Rosetta terms**: {', '.join(sorted(all_terms))}.\n\n"
        f"**Lineage**: This axiom condenses {total_tokens} tokens of source material "
        f"into a single canonical entry. Rewrite pending.\n"
    )
    successor_tokens = count_tokens(successor_content)

    successor = {
        "node_id": successor_id,
        "atom_id": successor_id,
        "content": successor_content,
        "rosetta_terms": sorted(all_terms),
        "dimension_vector": avg_vec,
        "adjacency": sorted(all_adj),
        "source_atom_ids": sorted(member_ids),
        "tier": "axiom",
        "retired": False,
        "fusion_generation": max(a.get("fusion_generation", 0) for a in cluster) + 1,
    }

    # Tombstones
    tombstones = []
    for a in cluster:
        tombstones.append({
            "node_id": a.get("node_id", a.get("atom_id", "")),
            "reason_class": "merged",
            "successor_ids": [successor_id],
            "redirect_to": successor_id,
            "tombstoned_at": now_iso(),
            "original_content_tokens": count_tokens(a.get("content", "")),
        })

    # Binding energy
    binding_energy = (total_tokens - successor_tokens) / total_tokens if total_tokens > 0 else 0.0

    return successor, tombstones, binding_energy


# ---------------------------------------------------------------------------
# Main execution
# ---------------------------------------------------------------------------

def run_fusion(
    repo_root: Path,
    force: bool = False,
    dry_run: bool = False,
    max_fusions: int = DEFAULT_MAX_FUSIONS_PER_RUN,
    trigger_threshold: int = DEFAULT_TRIGGER_THRESHOLD,
) -> dict[str, Any]:
    """Execute fusion pass. Returns summary dict."""

    ledger_path = repo_root / FUSION_LEDGER_REL
    apoptosis_path = repo_root / APOPTOSIS_LEDGER_REL
    lattice_path = repo_root / LATTICE_INDEX_REL
    reanneal_path = repo_root / REANNEAL_QUEUE_REL
    metrics_path = repo_root / PROMOTION_METRICS_REL

    # Count promotions since last fusion
    fusion_entries = load_jsonl(ledger_path)
    last_fusion_at = None
    for e in reversed(fusion_entries):
        if e.get("event") == "fusion_complete":
            last_fusion_at = e.get("timestamp")
            break

    metrics = load_jsonl(metrics_path)
    promotions_since = 0
    for m in metrics:
        ts = m.get("generated_at", m.get("timestamp", ""))
        if last_fusion_at and ts <= last_fusion_at:
            continue
        promotions_since += m.get("axioms_promoted", m.get("blocks_promoted", 0))

    if not force and promotions_since < trigger_threshold:
        return {
            "status": "SKIPPED",
            "reason": f"Only {promotions_since} promotions since last fusion (threshold: {trigger_threshold})",
            "fusions": 0,
        }

    # Load lattice index for axiom data
    lattice = load_json(lattice_path)
    nodes = lattice.get("nodes", [])
    if isinstance(nodes, dict):
        nodes = [{"node_id": k, **v} for k, v in nodes.items()]

    # Filter to non-retired axioms
    live = [n for n in nodes if not n.get("retired", False)]

    clusters = build_clusters(live)
    if not clusters:
        return {
            "status": "NO_CLUSTERS",
            "reason": "No eligible merge clusters found",
            "fusions": 0,
        }

    # Execute fusions up to limit
    results = []
    for cluster in clusters[:max_fusions]:
        successor, tombstones, energy = fuse_cluster(cluster)

        if energy <= 0:
            results.append({"cluster": [a.get("node_id") for a in cluster], "skipped": "negative_energy"})
            continue

        if dry_run:
            results.append({
                "successor_id": successor["node_id"],
                "merged": [t["node_id"] for t in tombstones],
                "binding_energy": round(energy, 4),
                "dry_run": True,
            })
            continue

        # Write tombstones to apoptosis ledger
        for t in tombstones:
            append_jsonl(apoptosis_path, t)

        # Queue dependents for reanneal
        member_ids = {t["node_id"] for t in tombstones}
        for n in nodes:
            adj = set(n.get("adjacency", []))
            if adj & member_ids and n.get("node_id") not in member_ids:
                append_jsonl(reanneal_path, {
                    "atom_id": n["node_id"],
                    "reason": "dependency_merged",
                    "successor_redirect": successor["node_id"],
                    "queued_at": now_iso(),
                })

        # Record fusion event
        append_jsonl(ledger_path, {
            "event": "fusion_complete",
            "timestamp": now_iso(),
            "successor_id": successor["node_id"],
            "merged_ids": [t["node_id"] for t in tombstones],
            "binding_energy": round(energy, 4),
            "tokens_before": sum(t["original_content_tokens"] for t in tombstones),
            "tokens_after": count_tokens(successor["content"]),
        })

        # Update lattice index: append successor, retire merged members
        lattice = load_json(lattice_path)
        idx_nodes = lattice.get("nodes", [])
        if isinstance(idx_nodes, dict):
            idx_nodes = [{"node_id": k, **v} for k, v in idx_nodes.items()]
        for n in idx_nodes:
            if n.get("node_id") in member_ids:
                n["retired"] = True
                n["redirect_to"] = successor["node_id"]
        idx_nodes.append(successor)
        lattice["nodes"] = idx_nodes
        write_json_atomic(lattice_path, lattice)

        results.append({
            "successor_id": successor["node_id"],
            "merged": [t["node_id"] for t in tombstones],
            "binding_energy": round(energy, 4),
        })

    return {
        "status": "COMPLETE",
        "fusions": len([r for r in results if "successor_id" in r]),
        "results": results,
    }


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------

def self_test() -> int:
    import tempfile as tf

    cases = []

    def rec(cid: str, ok: bool, detail: str = ""):
        cases.append({"id": cid, "status": "PASS" if ok else "FAIL", "detail": detail})

    with tf.TemporaryDirectory(prefix="fusion-selftest-") as td:
        root = Path(td)
        (root / STATE_REL).mkdir(parents=True, exist_ok=True)

        # Build a lattice index with 5 similar axioms
        nodes = []
        for i in range(5):
            nodes.append({
                "node_id": f"CANON-{10001 + i:05d}",
                "content": f"Ontology coherence protocol variant {i} for lattice integration.",
                "rosetta_terms": ["ontology", "coherence", "lattice", "protocol"],
                "dimension_vector": {
                    "cognitive": 0.8, "semiotic": 0.7, "psychological": 0.2,
                    "phenomenological": 0.1, "volitional": 0.5, "embodied": 0.1,
                    "behavioral": 0.7, "characterological": 0.1, "aesthetic": 0.2,
                    "linguistic": 0.3, "social": 0.6, "spiritual": 0.1,
                    "temporal": 0.2, "environmental": 0.4,
                },
                "adjacency": [f"CANON-{10001 + ((i + 1) % 5):05d}"],
                "retired": False,
            })
        write_json_atomic(root / LATTICE_INDEX_REL, {
            "schema_version": "1.0.0",
            "nodes": nodes,
        })

        # Fake enough promotions
        metrics_path = root / PROMOTION_METRICS_REL
        for i in range(5):
            append_jsonl(metrics_path, {
                "generated_at": now_iso(),
                "axioms_promoted": 1,
            })

        # Test 1: 5 redundant axioms → fusion
        r1 = run_fusion(root, force=True)
        rec("FUS-T01", r1["fusions"] >= 1 and r1["status"] == "COMPLETE",
            json.dumps(r1, sort_keys=True))

        # Check tombstones written
        apop = load_jsonl(root / APOPTOSIS_LEDGER_REL)
        rec("FUS-T01b", len(apop) >= 4 and all(t["reason_class"] == "merged" for t in apop),
            f"tombstones={len(apop)}")

        # Check binding energy > 0
        ledger = load_jsonl(root / FUSION_LEDGER_REL)
        energy_ok = any(e.get("binding_energy", 0) > 0 for e in ledger)
        rec("FUS-T01c", energy_ok, f"ledger_entries={len(ledger)}")

        # Check lattice index has successor node and merged members retired
        lat = load_json(root / LATTICE_INDEX_REL)
        lat_nodes = lat.get("nodes", [])
        successor_in_index = any(n.get("node_id", "").startswith("FUSED-") for n in lat_nodes)
        rec("FUS-T01d", successor_in_index, "successor_node_in_lattice_index")
        retired_members = [n for n in lat_nodes if n.get("retired") and n.get("redirect_to", "").startswith("FUSED-")]
        rec("FUS-T01e", len(retired_members) >= 4, f"retired_members={len(retired_members)}")

    with tf.TemporaryDirectory(prefix="fusion-selftest-t2-") as td:
        root = Path(td)
        (root / STATE_REL).mkdir(parents=True, exist_ok=True)
        write_json_atomic(root / LATTICE_INDEX_REL, {"schema_version": "1.0.0", "nodes": []})

        # Test 2: below trigger threshold → skip
        r2 = run_fusion(root, force=False)
        rec("FUS-T02", r2["status"] == "SKIPPED", json.dumps(r2, sort_keys=True))

    with tf.TemporaryDirectory(prefix="fusion-selftest-t3-") as td:
        root = Path(td)
        (root / STATE_REL).mkdir(parents=True, exist_ok=True)

        # Test 3: dry run produces no side effects
        nodes3 = []
        for i in range(5):
            nodes3.append({
                "node_id": f"CANON-{20001 + i:05d}",
                "content": f"Test axiom {i} for dry run.",
                "rosetta_terms": ["test", "axiom"],
                "dimension_vector": {"cognitive": 0.8, "semiotic": 0.7},
                "adjacency": [],
                "retired": False,
            })
        write_json_atomic(root / LATTICE_INDEX_REL, {"schema_version": "1.0.0", "nodes": nodes3})
        r3 = run_fusion(root, force=True, dry_run=True)
        apop3 = load_jsonl(root / APOPTOSIS_LEDGER_REL)
        rec("FUS-T03", len(apop3) == 0, f"dry_run_tombstones={len(apop3)}")

    passed = sum(1 for c in cases if c["status"] == "PASS")
    failed = len(cases) - passed
    print(json.dumps({
        "self_test": "PASS" if failed == 0 else "FAIL",
        "passed": passed,
        "failed": failed,
        "cases": cases,
    }, indent=2))
    return 1 if failed else 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Fusion Operator — semantic compression via merged reason class")
    parser.add_argument("--repo-root", type=Path, required="--self-test" not in sys.argv)
    parser.add_argument("--force-fusion", action="store_true", help="Force fusion regardless of trigger threshold")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be fused without writing")
    parser.add_argument("--max-fusions", type=int, default=DEFAULT_MAX_FUSIONS_PER_RUN)
    parser.add_argument("--trigger-threshold", type=int, default=DEFAULT_TRIGGER_THRESHOLD)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        sys.exit(self_test())

    result = run_fusion(
        repo_root=args.repo_root,
        force=args.force_fusion,
        dry_run=args.dry_run,
        max_fusions=args.max_fusions,
        trigger_threshold=args.trigger_threshold,
    )
    print(json.dumps(result, indent=2))
    if result["status"] == "COMPLETE" and result["fusions"] > 0:
        print(f"\nFusion complete: {result['fusions']} cluster(s) processed.")
    elif result["status"] == "SKIPPED":
        print(f"\n{result['reason']}")
    elif result["status"] == "NO_CLUSTERS":
        print("\nNo eligible merge clusters found.")


if __name__ == "__main__":
    main()
