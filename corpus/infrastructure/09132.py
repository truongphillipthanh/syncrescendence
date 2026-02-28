#!/usr/bin/env python3
"""
Atom Integration Pipeline — CC26 Adjudicator Task 1A
Clusters extracted atoms, scores against Sovereign priorities, outputs ranked manifest.

Usage:
    python3 atom_cluster.py --repo-root /Users/system/syncrescendence --top-n 200
    python3 atom_cluster.py --repo-root /Users/system/syncrescendence --top-n 10 --sample 500

Dependencies (all pre-installed):
    - sentence-transformers (all-MiniLM-L6-v2)
    - scikit-learn (KMeans, TfidfVectorizer, silhouette)
    - numpy, PyYAML
"""
from config import *

import os
os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")

import argparse
import glob
import json
import math
import re
import sys
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import yaml

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
WEIGHTS = {
    "confidence": 0.24,
    "recency": 0.16,
    "sovereign_overlap": 0.22,
    "actionability": 0.16,
    "foundational": 0.12,
    "uniqueness": 0.10,
}

ACTIONABILITY_MAP = {
    "praxis_hook": 1.0,
    "framework": 0.85,
    "method": 0.85,
    "claim": 0.45,
    "evidence": 0.45,
    "concept": 0.25,
}
ACTIONABILITY_DEFAULT = 0.25

BAND_THRESHOLDS = {
    "auto_promote_candidate": 0.78,  # default; overridden by --auto-promote-percentile
    "sovereign_review": 0.58,
}

TODAY = datetime.now(timezone.utc)

# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_atoms(meta_dir: str, sample: int | None = None) -> list[dict]:
    """Load atoms from EXTRACT-*.jsonl files (excluding *.bridge.jsonl)."""
    pattern = os.path.join(meta_dir, "EXTRACT-*.jsonl")
    files = sorted(f for f in glob.glob(pattern) if not f.endswith(".bridge.jsonl"))
    atoms = []
    for fpath in files:
        with open(fpath, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                    atoms.append(obj)
                except json.JSONDecodeError:
                    continue
    print(f"[load] {len(atoms)} atoms from {len(files)} files")
    if sample and sample < len(atoms):
        rng = np.random.default_rng(42)
        indices = rng.choice(len(atoms), size=sample, replace=False)
        atoms = [atoms[i] for i in sorted(indices)]
        print(f"[load] sampled down to {len(atoms)}")
    return atoms


def load_quality_scores(meta_dir: str) -> dict[str, dict]:
    """Load quality gate results keyed by atom_id."""
    path = os.path.join(meta_dir, "DYN-QUALITY_GATE_RESULTS.jsonl")
    qmap = {}
    if not os.path.exists(path):
        print("[load] No quality gate file found, using defaults")
        return qmap
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                aid = obj.get("atom_id", "")
                if aid:
                    qmap[aid] = obj
            except json.JSONDecodeError:
                continue
    print(f"[load] {len(qmap)} quality gate entries")
    return qmap


def load_sovereign_priorities(state_dir: str) -> set[str]:
    """Load priority terms from REF-SOVEREIGN_PRIORITY_SIGNALS.yaml."""
    path = os.path.join(state_dir, "REF-SOVEREIGN_PRIORITY_SIGNALS.yaml")
    terms = set()
    if not os.path.exists(path):
        print("[load] No sovereign priority signals file found")
        return terms
    with open(path, "r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    if not data or "priority_terms" not in data:
        return terms
    for category, term_list in data["priority_terms"].items():
        if isinstance(term_list, list):
            for t in term_list:
                # Normalize: lowercase, split multi-word into individual tokens too
                t_lower = str(t).lower().strip()
                terms.add(t_lower)
                for word in t_lower.split():
                    if len(word) > 2:
                        terms.add(word)
    print(f"[load] {len(terms)} sovereign priority terms")
    return terms


# ---------------------------------------------------------------------------
# Embedding
# ---------------------------------------------------------------------------

def build_embeddings(texts: list[str]) -> np.ndarray:
    """Build embeddings. Primary: sentence-transformers. Fallback: TF-IDF."""
    try:
        from sentence_transformers import SentenceTransformer
        print("[embed] Using sentence-transformers/all-MiniLM-L6-v2")
        model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        embeddings = model.encode(texts, show_progress_bar=True, batch_size=256)
        return np.array(embeddings, dtype=np.float32)
    except Exception as e:
        print(f"[embed] sentence-transformers failed ({e}), falling back to TF-IDF")

    from sklearn.feature_extraction.text import TfidfVectorizer
    vec = TfidfVectorizer(max_features=8000, ngram_range=(1, 2))
    mat = vec.fit_transform(texts)
    return mat.toarray().astype(np.float32)


# ---------------------------------------------------------------------------
# Clustering
# ---------------------------------------------------------------------------

def cluster_atoms(embeddings: np.ndarray) -> np.ndarray:
    """Cluster embeddings. Primary: HDBSCAN. Fallback: KMeans with silhouette."""
    n = embeddings.shape[0]

    # Try HDBSCAN
    try:
        import hdbscan
        print("[cluster] Using HDBSCAN")
        clusterer = hdbscan.HDBSCAN(min_cluster_size=5, min_samples=2)
        labels = clusterer.fit_predict(embeddings)
        n_clusters = len(set(labels) - {-1})
        n_noise = int((labels == -1).sum())
        print(f"[cluster] HDBSCAN: {n_clusters} clusters, {n_noise} noise points")
        return labels
    except ImportError:
        pass

    # Fallback: KMeans with silhouette
    from sklearn.cluster import KMeans
    from sklearn.metrics import silhouette_score

    print("[cluster] Using KMeans with silhouette selection")

    # Determine k range
    k_min = max(10, n // 200)
    k_max = min(200, n // 3)
    if k_max <= k_min:
        k_max = k_min + 10

    # Coarse search: step by 10
    candidates = list(range(k_min, k_max + 1, max(1, (k_max - k_min) // 15)))
    if candidates[-1] != k_max:
        candidates.append(k_max)

    best_k, best_score = k_min, -1.0
    for k in candidates:
        km = KMeans(n_clusters=k, n_init=3, max_iter=100, random_state=42)
        labs = km.fit_predict(embeddings)
        # Sample for silhouette if large
        if n > 5000:
            idx = np.random.default_rng(42).choice(n, 5000, replace=False)
            sc = silhouette_score(embeddings[idx], labs[idx])
        else:
            sc = silhouette_score(embeddings, labs)
        if sc > best_score:
            best_score = sc
            best_k = k
        print(f"  k={k}: silhouette={sc:.4f}")

    print(f"[cluster] Best k={best_k} (silhouette={best_score:.4f})")
    km = KMeans(n_clusters=best_k, n_init=10, max_iter=300, random_state=42)
    labels = km.fit_predict(embeddings)
    return labels


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

def parse_date_from_source_id(source_id: str) -> datetime | None:
    """Extract date from source_id like SOURCE-20250124-684."""
    m = re.search(r"(\d{8})", source_id or "")
    if m:
        try:
            return datetime.strptime(m.group(1), "%Y%m%d").replace(tzinfo=timezone.utc)
        except ValueError:
            pass
    return None


def compute_recency(atom: dict) -> float:
    """exp(-days/365) from source date."""
    dt = parse_date_from_source_id(atom.get("source_id", ""))
    if dt is None:
        return 0.3  # default for undated
    days = (TODAY - dt).days
    if days < 0:
        days = 0
    return math.exp(-days / 365.0)


def tokenize(text: str) -> set[str]:
    """Simple word tokenization for Jaccard."""
    return set(re.findall(r"[a-z]{3,}", text.lower()))


def compute_sovereign_overlap(atom: dict, priority_terms: set[str]) -> float:
    """Jaccard of atom terms vs sovereign priority terms."""
    content = atom.get("content", "")
    category = atom.get("category", "")
    atom_tokens = tokenize(content + " " + category)
    if not atom_tokens or not priority_terms:
        return 0.0
    intersection = atom_tokens & priority_terms
    union = atom_tokens | priority_terms
    return len(intersection) / len(union) if union else 0.0


def compute_actionability(atom: dict) -> float:
    """Rule-based by category."""
    cat = atom.get("category", "").lower()
    return ACTIONABILITY_MAP.get(cat, ACTIONABILITY_DEFAULT)


def compute_foundational(atom: dict, quality: dict | None) -> float:
    """Foundational score: concept/framework bonus, cross_source_support, paradigm signals."""
    score = 0.0
    cat = atom.get("category", "").lower()
    if cat in ("concept", "framework"):
        score += 0.45

    # cross_source_support from quality gate
    css = 0.0
    if quality:
        css = quality.get("cross_source_support", 0.0)
    if css >= 0.3:
        score += 0.25

    # paradigm / strategic signal detection
    content = atom.get("content", "").lower()
    paradigm_signals = ["paradigm", "strategic", "foundational", "architectural",
                        "constitutional", "invariant", "axiom", "principle"]
    if any(s in content for s in paradigm_signals):
        score += 0.30

    return min(score, 1.0)


def compute_confidence(atom: dict, quality: dict | None) -> float:
    """Confidence from atom, quality gate, or default."""
    # Check atom-level confidence
    conf = atom.get("confidence")
    if conf is not None:
        return float(conf)
    # Check quality gate
    if quality:
        cs = quality.get("consistency_score")
        if cs is not None:
            return float(cs)
    return 0.55


def score_atoms(atoms: list[dict], quality_map: dict[str, dict],
                priority_terms: set[str], embeddings: np.ndarray) -> list[dict]:
    """Score each atom with the weighted rubric. Returns list of score dicts."""

    # Pre-compute pairwise max cosine sim for uniqueness
    # For efficiency, use batch cosine sim
    print("[score] Computing uniqueness (max cosine similarity)...")
    norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    normed = embeddings / norms

    # For large N, compute in chunks to avoid memory blowup
    n = len(atoms)
    max_sims = np.zeros(n, dtype=np.float32)

    chunk_size = 500
    for i in range(0, n, chunk_size):
        end = min(i + chunk_size, n)
        sims = normed[i:end] @ normed.T  # (chunk, n)
        # Zero out self-similarity
        for j in range(end - i):
            sims[j, i + j] = -1.0
        max_sims[i:end] = sims.max(axis=1)

    print("[score] Scoring atoms...")
    results = []
    for idx, atom in enumerate(atoms):
        aid = atom.get("atom_id", f"UNKNOWN-{idx}")
        quality = quality_map.get(aid)

        conf = compute_confidence(atom, quality)
        rec = compute_recency(atom)
        sov = compute_sovereign_overlap(atom, priority_terms)
        act = compute_actionability(atom)
        fnd = compute_foundational(atom, quality)
        uniq = 1.0 - max(0.0, float(max_sims[idx]))

        weighted = (
            WEIGHTS["confidence"] * conf
            + WEIGHTS["recency"] * rec
            + WEIGHTS["sovereign_overlap"] * sov
            + WEIGHTS["actionability"] * act
            + WEIGHTS["foundational"] * fnd
            + WEIGHTS["uniqueness"] * uniq
        )

        # Band
        if weighted >= BAND_THRESHOLDS["auto_promote_candidate"]:
            band = "auto_promote_candidate"
        elif weighted >= BAND_THRESHOLDS["sovereign_review"]:
            band = "sovereign_review"
        else:
            band = "archive_candidate"

        results.append({
            "atom_id": aid,
            "source_id": atom.get("source_id", ""),
            "category": atom.get("category", ""),
            "score": round(weighted, 6),
            "band": band,
            "components": {
                "confidence": round(conf, 4),
                "recency": round(rec, 4),
                "sovereign_overlap": round(sov, 4),
                "actionability": round(act, 4),
                "foundational": round(fnd, 4),
                "uniqueness": round(uniq, 4),
            },
            "content_preview": atom.get("content", "")[:120],
        })

    return results


# ---------------------------------------------------------------------------
# Cluster aggregation + output
# ---------------------------------------------------------------------------

def aggregate_clusters(atom_scores: list[dict], labels: np.ndarray,
                       atoms: list[dict], top_n: int,
                       auto_promote_threshold: float | None = None) -> list[dict]:
    """Aggregate atom scores to cluster level, rank, return top N."""
    ap_thresh = auto_promote_threshold or BAND_THRESHOLDS["auto_promote_candidate"]
    cluster_map = defaultdict(list)
    for idx, label in enumerate(labels):
        cid = int(label)
        cluster_map[cid].append(idx)

    clusters = []
    for cid, indices in cluster_map.items():
        scores_in = [atom_scores[i]["score"] for i in indices]
        mean_score = float(np.mean(scores_in))
        max_score = float(np.max(scores_in))

        # Band by mean
        if mean_score >= ap_thresh:
            band = "auto_promote_candidate"
        elif mean_score >= BAND_THRESHOLDS["sovereign_review"]:
            band = "sovereign_review"
        else:
            band = "archive_candidate"

        # Category distribution
        cats = Counter(atom_scores[i]["category"] for i in indices)

        # Representative atom: highest scoring
        best_idx = indices[int(np.argmax(scores_in))]

        clusters.append({
            "cluster_id": cid,
            "size": len(indices),
            "mean_score": round(mean_score, 6),
            "max_score": round(max_score, 6),
            "band": band,
            "category_distribution": dict(cats.most_common()),
            "representative_atom": atom_scores[best_idx]["atom_id"],
            "representative_preview": atom_scores[best_idx]["content_preview"],
            "atom_ids": [atom_scores[i]["atom_id"] for i in indices],
        })

    # Sort by mean_score descending
    clusters.sort(key=lambda c: c["mean_score"], reverse=True)

    # Assign rank
    for rank, c in enumerate(clusters, 1):
        c["rank"] = rank

    return clusters[:top_n]


def write_outputs(clusters: list[dict], atom_scores: list[dict],
                  atoms: list[dict], meta_dir: str):
    """Write all 4 output files."""

    # 1. Cluster manifest
    manifest_path = os.path.join(meta_dir, "DYN-ATOM_CLUSTER_MANIFEST.jsonl")
    with open(manifest_path, "w", encoding="utf-8") as fh:
        for c in clusters:
            fh.write(json.dumps(c, ensure_ascii=False) + "\n")
    print(f"[output] {manifest_path} ({len(clusters)} clusters)")

    # 2. Score audit
    audit_path = os.path.join(meta_dir, "DYN-ATOM_SCORE_AUDIT.jsonl")
    with open(audit_path, "w", encoding="utf-8") as fh:
        for s in atom_scores:
            fh.write(json.dumps(s, ensure_ascii=False) + "\n")
    print(f"[output] {audit_path} ({len(atom_scores)} atoms)")

    # 3. Atom index with lifecycle fields
    index_path = os.path.join(meta_dir, "DYN-ATOM_INDEX.jsonl")
    # Build cluster lookup
    atom_to_cluster = {}
    for c in clusters:
        for aid in c["atom_ids"]:
            atom_to_cluster[aid] = c["cluster_id"]

    score_lookup = {s["atom_id"]: s for s in atom_scores}
    with open(index_path, "w", encoding="utf-8") as fh:
        for atom in atoms:
            aid = atom.get("atom_id", "")
            sc = score_lookup.get(aid, {})
            entry = {
                "atom_id": aid,
                "source_id": atom.get("source_id", ""),
                "category": atom.get("category", ""),
                "score": sc.get("score", 0.0),
                "band": sc.get("band", "unscored"),
                "cluster_id": atom_to_cluster.get(aid, -1),
                "integration_status": "pending",
                "integrated_at": None,
                "review_notes": None,
            }
            fh.write(json.dumps(entry, ensure_ascii=False) + "\n")
    print(f"[output] {index_path} ({len(atoms)} atoms)")

    # 4. Human-readable summary
    summary_path = os.path.join(meta_dir, "DYN-ATOM_CLUSTER_SUMMARY.md")
    band_counts = Counter(c["band"] for c in clusters)
    atom_band_counts = Counter(s["band"] for s in atom_scores)

    with open(summary_path, "w", encoding="utf-8") as fh:
        fh.write("# Atom Cluster Summary\n")
        fh.write(f"**Generated**: {TODAY.strftime('%Y-%m-%d %H:%M UTC')}\n")
        fh.write(f"**Cadence**: on-change\n\n")
        fh.write(f"## Overview\n")
        fh.write(f"- **Total atoms scored**: {len(atom_scores)}\n")
        fh.write(f"- **Clusters produced**: {len(clusters)}\n")
        fh.write(f"- **Weights**: {WEIGHTS}\n\n")

        fh.write(f"## Atom Band Distribution\n")
        fh.write(f"| Band | Count | % |\n|------|-------|---|\n")
        for band in ["auto_promote_candidate", "sovereign_review", "archive_candidate"]:
            cnt = atom_band_counts.get(band, 0)
            pct = cnt / len(atom_scores) * 100 if atom_scores else 0
            fh.write(f"| {band} | {cnt} | {pct:.1f}% |\n")

        fh.write(f"\n## Cluster Band Distribution\n")
        fh.write(f"| Band | Clusters |\n|------|----------|\n")
        for band in ["auto_promote_candidate", "sovereign_review", "archive_candidate"]:
            fh.write(f"| {band} | {band_counts.get(band, 0)} |\n")

        fh.write(f"\n## Top 20 Clusters\n\n")
        for c in clusters[:20]:
            fh.write(f"### Rank {c['rank']} — Cluster {c['cluster_id']} "
                      f"(score={c['mean_score']:.4f}, {c['band']}, {c['size']} atoms)\n")
            fh.write(f"- **Categories**: {c['category_distribution']}\n")
            fh.write(f"- **Representative**: `{c['representative_atom']}`\n")
            fh.write(f"- **Preview**: {c['representative_preview']}\n\n")

    print(f"[output] {summary_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Atom Integration Pipeline")
    parser.add_argument("--repo-root", required=True, help="Path to syncrescendence repo")
    parser.add_argument("--top-n", type=int, default=200, help="Top N clusters to output")
    parser.add_argument("--sample", type=int, default=None,
                        help="Sample N atoms for faster testing")
    parser.add_argument("--auto-promote-percentile", type=float, default=3.0,
                        help="Top N%% of atoms become auto_promote_candidate (default: 3)")
    args = parser.parse_args()

    repo = args.repo_root
    meta_dir = os.path.join(repo, "sources", "04-SOURCES", "_meta")
    state_dir = os.path.join(repo, "orchestration", "00-ORCHESTRATION", "state")

    if not os.path.isdir(meta_dir):
        print(f"ERROR: meta_dir not found: {meta_dir}", file=sys.stderr)
        sys.exit(1)

    t0 = time.time()

    # 1. Load data
    atoms = load_atoms(meta_dir, sample=args.sample)
    if not atoms:
        print("ERROR: No atoms loaded", file=sys.stderr)
        sys.exit(1)

    quality_map = load_quality_scores(meta_dir)
    priority_terms = load_sovereign_priorities(state_dir)

    # 2. Build embeddings
    texts = [a.get("content", "") for a in atoms]
    embeddings = build_embeddings(texts)

    # 3. Cluster
    labels = cluster_atoms(embeddings)

    # 4. Score
    atom_scores = score_atoms(atoms, quality_map, priority_terms, embeddings)

    # 4b. Recalculate auto_promote threshold from percentile
    if args.auto_promote_percentile > 0:
        all_scores = sorted([s["score"] for s in atom_scores], reverse=True)
        cutoff_idx = max(1, int(len(all_scores) * args.auto_promote_percentile / 100.0))
        percentile_threshold = all_scores[min(cutoff_idx - 1, len(all_scores) - 1)]
        print(f"[threshold] auto_promote percentile={args.auto_promote_percentile}% "
              f"→ threshold={percentile_threshold:.4f} (top {cutoff_idx} atoms)")
        # Re-band atoms using percentile threshold
        for s in atom_scores:
            if s["score"] >= percentile_threshold:
                s["band"] = "auto_promote_candidate"
            elif s["score"] >= BAND_THRESHOLDS["sovereign_review"]:
                s["band"] = "sovereign_review"
            else:
                s["band"] = "archive_candidate"
    else:
        percentile_threshold = None

    # 5. Aggregate + rank
    clusters = aggregate_clusters(atom_scores, labels, atoms, args.top_n,
                                  auto_promote_threshold=percentile_threshold)

    # 6. Write outputs
    write_outputs(clusters, atom_scores, atoms, meta_dir)

    elapsed = time.time() - t0
    print(f"\n[done] Pipeline complete in {elapsed:.1f}s")
    print(f"  Atoms: {len(atoms)}")
    print(f"  Clusters: {len(clusters)}")

    # Quick stats
    bands = Counter(s["band"] for s in atom_scores)
    for b in ["auto_promote_candidate", "sovereign_review", "archive_candidate"]:
        print(f"  {b}: {bands.get(b, 0)}")


if __name__ == "__main__":
    main()
