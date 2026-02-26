#!/usr/bin/env python3
"""candidate_adapter.py — Bridge protease_promote output to lattice_annealer input.

Adapter contract: orchestration/00-ORCHESTRATION/state/ARCH-CANDIDATE_ADAPTER_CONTRACT.yaml
"""

import argparse
import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Dimension keyword maps
# ---------------------------------------------------------------------------

DIMENSION_KEYWORDS = {
    "mode_of_access": ["access", "interface", "api", "tool", "platform"],
    "content_domain": ["knowledge", "ontology", "canon", "axiom", "theory"],
    "transformative_depth": ["transform", "change", "evolve", "refactor", "restructure"],
    "social_distribution": ["collaborate", "team", "agent", "constellation", "dispatch"],
    "practical_application": ["implement", "build", "deploy", "execute", "run"],
}


def load_rosetta_terms(repo_root: Path) -> list[str]:
    """Extract Internal Term column from REF-ROSETTA_STONE.md."""
    rosetta_path = repo_root / "engine" / "02-ENGINE" / "REF-ROSETTA_STONE.md"
    try:
        text = rosetta_path.read_text(encoding="utf-8")
    except OSError:
        return []
    terms: list[str] = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cols = [c.strip() for c in line.split("|")]
        # cols[0] is empty before first pipe; cols[1]=#, cols[2]=Internal Term
        if len(cols) < 3:
            continue
        num_field = cols[1]
        if not num_field or num_field == "#" or num_field == "---":
            continue
        try:
            int(num_field)
        except ValueError:
            continue
        terms.append(cols[2])
    return terms


def match_rosetta(content: str, terms: list[str]) -> list[str]:
    """Return rosetta terms found in content (case-insensitive substring)."""
    lower = content.lower()
    return [t for t in terms if t.lower() in lower]


def compute_dimension_vector(content: str) -> dict[str, float]:
    """Heuristic dimension scoring from keyword counts, normalized to [0,1]."""
    lower = content.lower()
    vec: dict[str, float] = {}
    for dim, keywords in DIMENSION_KEYWORDS.items():
        count = sum(lower.count(kw) for kw in keywords)
        vec[dim] = min(count / 3.0, 1.0)
    return vec


def load_lattice_index(repo_root: Path) -> dict:
    """Load DYN-LATTICE_INDEX.json, return {} on failure."""
    path = repo_root / "orchestration" / "00-ORCHESTRATION" / "state" / "DYN-LATTICE_INDEX.json"
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def find_canon_refs(content: str, lattice_index: dict) -> list[str]:
    """Extract CANON-NNNNN references from content + title matches from lattice index."""
    refs = list(set(re.findall(r"CANON-\d{5}", content)))
    # Check lattice index entries for title matches
    if isinstance(lattice_index, dict):
        nodes = lattice_index.get("nodes", lattice_index)
        if isinstance(nodes, list):
            for node in nodes:
                title = node.get("title", "")
                node_id = node.get("id", "")
                if title and title.lower() in content.lower() and node_id and node_id not in refs:
                    refs.append(node_id)
        elif isinstance(nodes, dict):
            for node_id, meta in nodes.items():
                title = meta.get("title", "") if isinstance(meta, dict) else ""
                if title and title.lower() in content.lower() and node_id not in refs:
                    refs.append(node_id)
    return refs


def adapt(atom: dict, repo_root: Path) -> dict:
    """Transform protease_promote output to lattice_annealer input."""
    rosetta_terms = load_rosetta_terms(repo_root)
    lattice_index = load_lattice_index(repo_root)
    content = atom.get("content", "")

    return {
        "atom_id": atom["atom_id"],
        "source_atom_ids": list(atom.get("source_atom_ids") or [atom["atom_id"]]),
        "content": content,
        "metadata": {
            "origin_hash": atom.get("origin_hash", ""),
            "axiom_alignment_score": atom.get("axiom_alignment_score", 0.0),
            "terminal_domain": atom.get("terminal_domain", ""),
            "matched_intention": atom.get("matched_intention", ""),
            "drift_score": atom.get("drift_score", 0.0),
        },
        "rosetta_terms": match_rosetta(content, rosetta_terms),
        "dimension_vector": compute_dimension_vector(content),
        "proposed_edges": {
            "canonical_node_ids": find_canon_refs(content, lattice_index),
        },
    }


def self_test() -> None:
    """Run with synthetic fixture, verify output schema."""
    fixture = {
        "atom_id": "AX99",
        "source_file": "sources/raw/test.md",
        "content": "Constitutional AI requires ontology access and team collaboration to deploy CANON-00016.",
        "origin_hash": "deadbeef",
        "axiom_alignment_score": 0.88,
        "terminal_domain": "CON",
        "matched_intention": "INT-0001",
        "drift_score": 0.02,
    }
    result = adapt(fixture, Path("/nonexistent"))
    required = {"atom_id", "source_atom_ids", "content", "metadata", "rosetta_terms",
                "dimension_vector", "proposed_edges"}
    assert required <= set(result.keys()), f"Missing keys: {required - set(result.keys())}"
    assert isinstance(result["source_atom_ids"], list)
    assert isinstance(result["rosetta_terms"], list)
    assert set(result["dimension_vector"].keys()) == set(DIMENSION_KEYWORDS.keys())
    assert all(0.0 <= v <= 1.0 for v in result["dimension_vector"].values())
    assert "CANON-00016" in result["proposed_edges"]["canonical_node_ids"]
    print("self-test PASSED")
    print(json.dumps(result, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Bridge protease_promote output to lattice_annealer input schema.")
    parser.add_argument("--repo-root", type=Path, required="--self-test" not in sys.argv,
                        help="Repository root path")
    parser.add_argument("--input-json", type=Path, help="Input JSON from protease_promote")
    parser.add_argument("--output-json", type=Path, help="Output JSON for lattice_annealer")
    parser.add_argument("--self-test", action="store_true", help="Run synthetic self-test")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        return

    if not args.input_json or not args.output_json:
        parser.error("--input-json and --output-json are required")

    atom = json.loads(args.input_json.read_text(encoding="utf-8"))
    result = adapt(atom, args.repo_root)
    args.output_json.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Adapted {atom['atom_id']} → {args.output_json}")


if __name__ == "__main__":
    main()
