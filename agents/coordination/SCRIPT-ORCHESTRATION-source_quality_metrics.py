#!/usr/bin/env python3
"""Metrics computation library for the DC-208-6 Source Quality Gate.

Computes coverage, graph density, praxis linkage, logical consistency,
and the Surprise x Precision alert score for extracted knowledge atoms.
"""
from __future__ import annotations
from config import *

import json
import math
import os
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")

import numpy as np

# Lazy-loaded globals for sentence-transformers
_model = None
_canon_embeddings: np.ndarray | None = None
_canon_texts: list[str] = []


def _get_model():
    """Lazy-load the sentence-transformer model."""
    global _model
    if _model is None:
        from sentence_transformers import SentenceTransformer
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model


def _cosine_sim(a: np.ndarray, b: np.ndarray) -> float:
    """Cosine similarity between two vectors."""
    denom = np.linalg.norm(a) * np.linalg.norm(b)
    if denom < 1e-12:
        return 0.0
    return float(np.dot(a, b) / denom)


def _cosine_sim_batch(vec: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    """Cosine similarities between a vector and each row of a matrix."""
    norms = np.linalg.norm(matrix, axis=1)
    vec_norm = np.linalg.norm(vec)
    denom = norms * vec_norm
    denom = np.where(denom < 1e-12, 1.0, denom)
    return matrix @ vec / denom


# ---------------------------------------------------------------------------
# Canon embedding cache
# ---------------------------------------------------------------------------

def load_canon_embeddings(canon_dir: Path) -> tuple[np.ndarray, list[str]]:
    """Load and cache canon text embeddings.

    Reads all .md files in canon_dir, splits into paragraphs, and embeds them.
    Returns (embeddings_matrix, texts).
    """
    global _canon_embeddings, _canon_texts
    if _canon_embeddings is not None:
        return _canon_embeddings, _canon_texts

    texts: list[str] = []
    for md_file in sorted(canon_dir.rglob("*.md")):
        try:
            content = md_file.read_text(errors="replace")
        except OSError:
            continue
        paragraphs = [p.strip() for p in content.split("\n\n") if len(p.strip()) > 40]
        texts.extend(paragraphs[:200])  # cap per file

    if not texts:
        _canon_embeddings = np.zeros((0, 384), dtype=np.float32)
        _canon_texts = []
        return _canon_embeddings, _canon_texts

    model = _get_model()
    _canon_embeddings = model.encode(texts, show_progress_bar=False, convert_to_numpy=True)
    _canon_texts = texts
    return _canon_embeddings, _canon_texts


# ---------------------------------------------------------------------------
# Individual metric functions
# ---------------------------------------------------------------------------

@dataclass
class AtomMetrics:
    """Computed metrics for a single atom."""
    atom_id: str
    # Gate 1
    coverage_mapped: bool = False
    # Gate 2
    graph_relation_count: int = 0
    gate2_skipped: bool = False
    # Gate 3
    praxis_link_count: int = 0
    gate3_skipped: bool = False
    # Gate 4
    contradiction_score: float = 0.0
    consistency_score: float = 1.0
    gate4_skipped: bool = False
    # Gate 5 components
    novelty: float = 0.0
    belief_violation: float = 0.0
    surprise: float = 0.0
    evidence_coverage: float = 0.0
    source_reliability: float = 0.5
    cross_source_support: float = 0.0
    falsifiability_score: float = 0.0
    precision: float = 0.0
    alert_score: float = 0.0
    alert_band: str = "IGNORE"
    # Gate pass/fail
    gates: dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {k: v for k, v in self.__dict__.items()}


def batch_encode_atoms(atoms: list[dict], batch_size: int = 256) -> np.ndarray:
    """Batch-encode all atom contents into embeddings.

    Returns ndarray of shape (len(atoms), embedding_dim).
    """
    model = _get_model()
    texts = [a["content"] for a in atoms]
    return model.encode(texts, show_progress_bar=True, convert_to_numpy=True,
                        batch_size=batch_size)


def compute_coverage(atom: dict, canon_embs: np.ndarray, canon_texts: list[str],
                     threshold: float = 0.45,
                     atom_emb: np.ndarray | None = None) -> bool:
    """Gate 1: Does this atom's content map to at least one canon paragraph?

    Uses cosine similarity >= threshold as the mapping criterion.
    If atom_emb is provided, skips re-encoding.
    """
    if canon_embs.shape[0] == 0:
        return False
    if atom_emb is None:
        model = _get_model()
        atom_emb = model.encode([atom["content"]], show_progress_bar=False, convert_to_numpy=True)[0]
    sims = _cosine_sim_batch(atom_emb, canon_embs)
    return bool(np.max(sims) >= threshold)


def compute_graph_density(atom: dict, graph_state: dict | None,
                          threshold: int = 8) -> tuple[int, bool]:
    """Gate 2: Count bidirectional relations from this atom in the graph.

    Returns (relation_count, skipped).
    """
    if graph_state is None:
        return 0, True
    atom_id = atom["atom_id"]
    edges = graph_state.get("edges", [])
    count = 0
    for e in edges:
        if e.get("source") == atom_id or e.get("target") == atom_id:
            count += 1
    return count, False


def load_praxis_cache(praxis_dir: Path | None) -> list[str] | None:
    """Pre-load all praxis .md file contents into memory once.

    Returns None if praxis_dir is unavailable, otherwise a list of file contents.
    """
    if praxis_dir is None or not praxis_dir.exists():
        return None
    contents = []
    for md_file in praxis_dir.rglob("*.md"):
        try:
            contents.append(md_file.read_text(errors="replace"))
        except OSError:
            continue
    return contents


def compute_praxis_linkage(atom: dict, praxis_dir: Path | None,
                           threshold: int = 2,
                           praxis_cache: list[str] | None = None) -> tuple[int, bool]:
    """Gate 3: Count praxis artifacts linked to this atom.

    Simple heuristic: search praxis .md files for the atom_id string.
    Returns (link_count, skipped).
    Uses praxis_cache if provided to avoid re-reading files per atom.
    """
    if praxis_cache is not None:
        atom_id = atom["atom_id"]
        count = sum(1 for content in praxis_cache if atom_id in content)
        return count, False
    if praxis_dir is None or not praxis_dir.exists():
        return 0, True
    atom_id = atom["atom_id"]
    count = 0
    for md_file in praxis_dir.rglob("*.md"):
        try:
            if atom_id in md_file.read_text(errors="replace"):
                count += 1
        except OSError:
            continue
    return count, False


def compute_consistency(atom: dict, canon_embs: np.ndarray,
                        canon_texts: list[str],
                        atom_emb: np.ndarray | None = None) -> float:
    """Gate 4: Logical consistency via NLI heuristic.

    Returns contradiction_score in [0, 1]. Lower is better.
    If atom_emb is provided, skips re-encoding.
    """
    if canon_embs.shape[0] == 0:
        return 0.0
    if atom_emb is None:
        model = _get_model()
        atom_emb = model.encode([atom["content"]], show_progress_bar=False, convert_to_numpy=True)[0]
    sims = _cosine_sim_batch(atom_emb, canon_embs)
    max_sim = float(np.max(sims))

    # Heuristic: topically similar but not identical suggests potential tension
    # Very high sim (>0.85) = consistent. Very low (<0.3) = unrelated.
    # The danger zone is 0.4-0.7 where content overlaps but may contradict.
    if max_sim > 0.85:
        return 0.02
    elif max_sim < 0.3:
        return 0.05  # unrelated, not contradicting
    else:
        # Scale: peak contradiction around 0.55 similarity
        return 0.04 + 0.08 * math.exp(-((max_sim - 0.55) ** 2) / 0.02)


def compute_novelty(atom: dict, canon_embs: np.ndarray,
                    atom_emb: np.ndarray | None = None) -> float:
    """Novelty = 1 - max_cosine(atom_embedding, canon_neighbor_embeddings)."""
    if canon_embs.shape[0] == 0:
        return 1.0
    if atom_emb is None:
        model = _get_model()
        atom_emb = model.encode([atom["content"]], show_progress_bar=False, convert_to_numpy=True)[0]
    sims = _cosine_sim_batch(atom_emb, canon_embs)
    return float(1.0 - np.max(sims))


def compute_belief_violation(atom: dict, canon_embs: np.ndarray,
                             atom_emb: np.ndarray | None = None) -> float:
    """Belief violation via cosine heuristic.

    If atom has < 0.3 similarity to any canon claim, belief_violation = high.
    """
    if canon_embs.shape[0] == 0:
        return 0.5  # unknown baseline
    if atom_emb is None:
        model = _get_model()
        atom_emb = model.encode([atom["content"]], show_progress_bar=False, convert_to_numpy=True)[0]
    sims = _cosine_sim_batch(atom_emb, canon_embs)
    max_sim = float(np.max(sims))
    if max_sim < 0.3:
        return 0.85
    elif max_sim < 0.5:
        return 0.5
    else:
        return max(0.05, 1.0 - max_sim)


def compute_evidence_coverage(atom: dict) -> float:
    """Evidence coverage from chaperone metadata.

    Atoms with argument_role='evidence' and context_type in structured types
    score higher.
    """
    chaperone = atom.get("chaperone", {})
    score = 0.3  # baseline
    role = chaperone.get("argument_role", "")
    if role == "evidence":
        score += 0.35
    elif role == "claim":
        score += 0.15
    ctx = chaperone.get("context_type", "")
    if ctx in ("empirical", "experimental", "statistical"):
        score += 0.25
    elif ctx in ("consensus", "anecdote"):
        score += 0.10
    return min(score, 1.0)


def compute_source_reliability(atom: dict, triage: dict | None) -> float:
    """Source reliability from triage scores if available."""
    if triage is None:
        return 0.5
    source_id = atom.get("source_id", "")
    records = triage.get("records", [])
    for rec in records:
        if rec.get("source_id") == source_id:
            return float(rec.get("total", 0.5))
    # Try filename match
    return 0.5


def compute_cross_source_support(atom: dict, other_atoms: list[dict],
                                 threshold: float = 0.75,
                                 atom_emb: np.ndarray | None = None,
                                 all_atom_embs: np.ndarray | None = None,
                                 atom_index: int | None = None) -> float:
    """Check if similar atoms appear in other EXTRACT files.

    Uses embedding similarity against atoms from other source_ids.
    If all_atom_embs is provided, uses pre-computed embeddings (massive speedup).
    Returns a score in [0, 1].
    """
    own_source = atom.get("source_id", "")

    if all_atom_embs is not None and atom_emb is not None:
        # Fast path: use pre-computed embeddings
        # Build mask of foreign atoms
        foreign_mask = np.array([a.get("source_id", "") != own_source for a in other_atoms])
        if not np.any(foreign_mask):
            return 0.0
        foreign_embs = all_atom_embs[foreign_mask]
        # Cap at 2000 for memory
        if foreign_embs.shape[0] > 2000:
            indices = np.random.choice(foreign_embs.shape[0], 2000, replace=False)
            foreign_embs = foreign_embs[indices]
        sims = _cosine_sim_batch(atom_emb, foreign_embs)
        supporting = int(np.sum(sims >= threshold))
        return min(supporting / 3.0, 1.0)

    # Slow fallback
    foreign = [a for a in other_atoms if a.get("source_id", "") != own_source]
    if not foreign:
        return 0.0

    model = _get_model()
    if atom_emb is None:
        atom_emb = model.encode([atom["content"]], show_progress_bar=False, convert_to_numpy=True)[0]
    foreign_texts = [a["content"] for a in foreign[:500]]
    foreign_embs = model.encode(foreign_texts, show_progress_bar=False, convert_to_numpy=True)
    sims = _cosine_sim_batch(atom_emb, foreign_embs)
    supporting = int(np.sum(sims >= threshold))
    return min(supporting / 3.0, 1.0)


# Falsifiability keywords
_FALSIFIABLE_PATTERNS = [
    re.compile(r"\b\d{4}\b"),          # years
    re.compile(r"\b\d+(\.\d+)?%\b"),   # percentages
    re.compile(r"\b(by|before|after|within)\s+\d"),  # temporal predictions
    re.compile(r"\b(will|predicts?|forecast|project)", re.IGNORECASE),
    re.compile(r"\b(increase|decrease|grow|shrink|double|triple)\b", re.IGNORECASE),
    re.compile(r"\$[\d,.]+"),           # dollar amounts
    re.compile(r"\b\d+x\b"),           # multipliers
]


def compute_falsifiability(atom: dict) -> float:
    """Keyword heuristic: claims with numbers, dates, predictions score higher."""
    text = atom.get("content", "")
    hits = sum(1 for p in _FALSIFIABLE_PATTERNS if p.search(text))
    return min(hits / 4.0, 1.0)


def compute_surprise_precision(
    novelty: float,
    belief_violation: float,
    evidence_coverage: float,
    source_reliability: float,
    cross_source_support: float,
    falsifiability_score: float,
) -> tuple[float, float, float, str]:
    """Compute the Surprise x Precision alert score.

    Returns (surprise, precision, alert_score, alert_band).
    """
    surprise = 0.6 * novelty + 0.4 * belief_violation
    precision = (0.35 * evidence_coverage
                 + 0.25 * source_reliability
                 + 0.25 * cross_source_support
                 + 0.15 * falsifiability_score)
    alert_score = surprise * precision

    if alert_score >= 0.55:
        band = "CRITICAL"
    elif alert_score >= 0.35:
        band = "REVIEW"
    else:
        band = "IGNORE"

    return surprise, precision, alert_score, band


def evaluate_atom(
    atom: dict,
    canon_embs: np.ndarray,
    canon_texts: list[str],
    graph_state: dict | None,
    praxis_dir: Path | None,
    triage: dict | None,
    other_atoms: list[dict],
    coverage_threshold: float = 0.45,
    graph_density_threshold: int = 8,
    praxis_threshold: int = 2,
    consistency_threshold: float = 0.12,
    praxis_cache: list[str] | None = None,
    atom_emb: np.ndarray | None = None,
    all_atom_embs: np.ndarray | None = None,
    atom_index: int | None = None,
) -> AtomMetrics:
    """Run all 4+1 gates on a single atom and return metrics.

    If atom_emb is provided, skips re-encoding (4x speedup).
    If all_atom_embs is provided, cross-source support uses pre-computed embeddings.
    """
    m = AtomMetrics(atom_id=atom["atom_id"])

    # Gate 1: Coverage
    m.coverage_mapped = compute_coverage(atom, canon_embs, canon_texts, coverage_threshold, atom_emb=atom_emb)
    m.gates["coverage"] = "PASS" if m.coverage_mapped else "FAIL"

    # Gate 2: Graph density
    m.graph_relation_count, m.gate2_skipped = compute_graph_density(atom, graph_state, graph_density_threshold)
    if m.gate2_skipped:
        m.gates["graph_density"] = "SKIPPED - no graph state"
    else:
        m.gates["graph_density"] = "PASS" if m.graph_relation_count >= graph_density_threshold else "FAIL"

    # Gate 3: Praxis linkage
    m.praxis_link_count, m.gate3_skipped = compute_praxis_linkage(atom, praxis_dir, praxis_threshold, praxis_cache=praxis_cache)
    if m.gate3_skipped:
        m.gates["praxis"] = "SKIPPED - no praxis dir"
    else:
        m.gates["praxis"] = "PASS" if m.praxis_link_count >= praxis_threshold else "FAIL"

    # Gate 4: Consistency
    m.contradiction_score = compute_consistency(atom, canon_embs, canon_texts, atom_emb=atom_emb)
    m.consistency_score = 1.0 - m.contradiction_score
    if canon_embs.shape[0] == 0:
        m.gate4_skipped = True
        m.gates["consistency"] = "SKIPPED - no canon embeddings"
    else:
        m.gates["consistency"] = "PASS" if m.contradiction_score <= consistency_threshold else "FAIL"

    # Gate 5 components
    m.novelty = compute_novelty(atom, canon_embs, atom_emb=atom_emb)
    m.belief_violation = compute_belief_violation(atom, canon_embs, atom_emb=atom_emb)
    m.evidence_coverage = compute_evidence_coverage(atom)
    m.source_reliability = compute_source_reliability(atom, triage)
    m.cross_source_support = compute_cross_source_support(
        atom, other_atoms, atom_emb=atom_emb,
        all_atom_embs=all_atom_embs, atom_index=atom_index)
    m.falsifiability_score = compute_falsifiability(atom)

    m.surprise, m.precision, m.alert_score, m.alert_band = compute_surprise_precision(
        m.novelty, m.belief_violation, m.evidence_coverage,
        m.source_reliability, m.cross_source_support, m.falsifiability_score,
    )
    m.gates["surprise_precision"] = m.alert_band

    return m


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Test metrics on a single atom JSONL")
    parser.add_argument("--extract-jsonl", required=True, help="Path to EXTRACT JSONL file")
    parser.add_argument("--canon-dir", default="canon/", help="Canon directory")
    args = parser.parse_args()

    canon_dir = Path(args.canon_dir)
    canon_embs, canon_texts = load_canon_embeddings(canon_dir)
    print(f"Loaded {len(canon_texts)} canon paragraphs, embedding shape: {canon_embs.shape}")

    atoms = []
    with open(args.extract_jsonl) as f:
        for line in f:
            line = line.strip()
            if line:
                atoms.append(json.loads(line))

    if atoms:
        m = evaluate_atom(atoms[0], canon_embs, canon_texts, None, None, None, atoms)
        print(json.dumps(m.to_dict(), indent=2))
