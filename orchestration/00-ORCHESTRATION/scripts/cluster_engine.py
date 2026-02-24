#!/usr/bin/env python3
"""DC-208-3 Cluster Engine — hybrid HDBSCAN + constrained K-means.

Clusters extracted knowledge atoms from EXTRACT-*.jsonl files using
embedding-based similarity. Supports three dependency tiers:

  Tier 1 (full):   sentence-transformers + HDBSCAN
  Tier 2 (mid):    sklearn TF-IDF + KMeans (elbow method)
  Tier 3 (stdlib): bag-of-words cosine + simple centroid clustering

Usage:
    cluster_engine.py --extract-dir sources/04-SOURCES/_meta/ \\
        --out-dir sources/04-SOURCES/_meta/ \\
        [--min-cluster-size 5] [--max-clusters 50] \\
        [--method auto|hdbscan|kmeans|simple] [--verbose]
"""
from __future__ import annotations

import argparse
import glob
import json
import math
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")

# ---------------------------------------------------------------------------
# Dependency detection
# ---------------------------------------------------------------------------

HAS_NUMPY = False
HAS_SKLEARN = False
HAS_HDBSCAN = False
HAS_SENTENCE_TRANSFORMERS = False

try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    pass

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.cluster import KMeans as SklearnKMeans
    from sklearn.metrics import silhouette_score
    HAS_SKLEARN = True
except ImportError:
    pass

try:
    import hdbscan as hdbscan_lib
    HAS_HDBSCAN = True
except ImportError:
    pass

try:
    from sentence_transformers import SentenceTransformer
    HAS_SENTENCE_TRANSFORMERS = True
except ImportError:
    pass


def log(msg: str, verbose: bool = True) -> None:
    """Print timestamped log message to stderr."""
    if verbose:
        ts = datetime.now(timezone.utc).strftime("%H:%M:%S")
        print(f"[cluster_engine {ts}] {msg}", file=sys.stderr)


# ===================================================================
# 1. ATOM LOADING
# ===================================================================

def load_atoms(extract_dir: str, verbose: bool = False) -> list[dict]:
    """Load atoms from EXTRACT-*.jsonl files (excludes .bridge.jsonl)."""
    pattern = os.path.join(extract_dir, "EXTRACT-*.jsonl")
    all_files = sorted(glob.glob(pattern))
    # Exclude bridge files — those are cross-reference metadata
    jsonl_files = [f for f in all_files if not f.endswith(".bridge.jsonl")]

    atoms: list[dict] = []
    skipped = 0
    for path in jsonl_files:
        with open(path) as fh:
            for lineno, line in enumerate(fh, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    atom = json.loads(line)
                    if "atom_id" not in atom or "content" not in atom:
                        skipped += 1
                        continue
                    atom["_source_file"] = os.path.basename(path)
                    atoms.append(atom)
                except json.JSONDecodeError:
                    skipped += 1

    log(f"Loaded {len(atoms)} atoms from {len(jsonl_files)} files "
        f"({skipped} skipped)", verbose)
    return atoms


# ===================================================================
# 2. EMBEDDING STRATEGIES
# ===================================================================

def _build_text(atom: dict) -> str:
    """Build text representation for embedding from atom fields."""
    parts = []
    if atom.get("category"):
        parts.append(f"[{atom['category']}]")
    parts.append(atom["content"])
    chap = atom.get("chaperone", {})
    if chap.get("context_type"):
        parts.append(f"(context: {chap['context_type']})")
    if chap.get("argument_role"):
        parts.append(f"(role: {chap['argument_role']})")
    return " ".join(parts)


def embed_sentence_transformers(
    atoms: list[dict], verbose: bool = False
) -> "np.ndarray":
    """Tier 1: Embed using sentence-transformers all-MiniLM-L6-v2."""
    log("Embedding with sentence-transformers (all-MiniLM-L6-v2)...", verbose)
    model = SentenceTransformer("all-MiniLM-L6-v2")
    texts = [_build_text(a) for a in atoms]
    embeddings = model.encode(texts, show_progress_bar=verbose, batch_size=64)
    return np.array(embeddings)


def embed_tfidf(atoms: list[dict], verbose: bool = False) -> "np.ndarray":
    """Tier 2: Embed using TF-IDF with sklearn."""
    log("Embedding with TF-IDF (sklearn)...", verbose)
    texts = [_build_text(a) for a in atoms]
    vectorizer = TfidfVectorizer(
        max_features=5000,
        stop_words="english",
        ngram_range=(1, 2),
        min_df=2,
        max_df=0.95,
    )
    matrix = vectorizer.fit_transform(texts)
    return matrix.toarray(), vectorizer


def embed_bow(atoms: list[dict], verbose: bool = False) -> list[dict[str, float]]:
    """Tier 3: Simple bag-of-words with TF normalization (stdlib only)."""
    log("Embedding with bag-of-words (stdlib)...", verbose)
    stop_words = {
        "the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
        "have", "has", "had", "do", "does", "did", "will", "would", "could",
        "should", "may", "might", "shall", "can", "need", "dare", "ought",
        "used", "to", "of", "in", "for", "on", "with", "at", "by", "from",
        "as", "into", "through", "during", "before", "after", "above",
        "below", "between", "out", "off", "over", "under", "again",
        "further", "then", "once", "here", "there", "when", "where", "why",
        "how", "all", "each", "every", "both", "few", "more", "most",
        "other", "some", "such", "no", "nor", "not", "only", "own", "same",
        "so", "than", "too", "very", "just", "because", "but", "and", "or",
        "if", "while", "that", "this", "it", "its", "i", "me", "my", "we",
        "our", "you", "your", "he", "him", "his", "she", "her", "they",
        "them", "their", "what", "which", "who", "whom",
    }

    def tokenize(text: str) -> list[str]:
        return [
            w for w in re.findall(r"[a-z][a-z0-9'-]*", text.lower())
            if w not in stop_words and len(w) > 2
        ]

    # Build document frequency
    texts = [_build_text(a) for a in atoms]
    doc_tokens = [tokenize(t) for t in texts]
    df: Counter = Counter()
    for tokens in doc_tokens:
        for w in set(tokens):
            df[w] += 1

    n_docs = len(atoms)
    # Build vocab from top terms by DF (min_df=2, max_df=95%)
    vocab = sorted([
        w for w, c in df.items()
        if 2 <= c <= int(0.95 * n_docs)
    ], key=lambda w: -df[w])[:3000]
    vocab_idx = {w: i for i, w in enumerate(vocab)}

    vectors: list[dict[str, float]] = []
    for tokens in doc_tokens:
        tf: Counter = Counter(tokens)
        vec: dict[str, float] = {}
        for w, count in tf.items():
            if w in vocab_idx:
                idf = math.log((n_docs + 1) / (df[w] + 1)) + 1
                vec[w] = count * idf
        # L2 normalize
        norm = math.sqrt(sum(v * v for v in vec.values())) or 1.0
        vec = {w: v / norm for w, v in vec.items()}
        vectors.append(vec)

    log(f"BoW vocab size: {len(vocab)}", verbose)
    return vectors


# ===================================================================
# 3. CLUSTERING STRATEGIES
# ===================================================================

def cluster_hdbscan(
    embeddings: "np.ndarray",
    min_cluster_size: int = 5,
    verbose: bool = False,
) -> "np.ndarray":
    """Tier 1: HDBSCAN clustering — finds natural clusters."""
    log(f"Clustering with HDBSCAN (min_cluster_size={min_cluster_size})...",
        verbose)
    clusterer = hdbscan_lib.HDBSCAN(
        min_cluster_size=min_cluster_size,
        min_samples=2,
        metric="euclidean",
        cluster_selection_method="eom",
    )
    labels = clusterer.fit_predict(embeddings)
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise = int(np.sum(labels == -1))
    log(f"HDBSCAN found {n_clusters} clusters, {n_noise} noise points",
        verbose)
    return labels


def _elbow_k(
    embeddings: "np.ndarray",
    max_clusters: int,
    verbose: bool = False,
) -> int:
    """Find optimal K using elbow method (inertia second derivative)."""
    n = embeddings.shape[0]
    k_range = range(2, min(max_clusters + 1, n // 2 + 1, 51))
    if len(list(k_range)) < 2:
        return min(5, n)

    inertias: list[float] = []
    for k in k_range:
        km = SklearnKMeans(n_clusters=k, n_init=5, max_iter=100,
                           random_state=42)
        km.fit(embeddings)
        inertias.append(km.inertia_)

    # Second derivative (acceleration)
    k_list = list(k_range)
    if len(inertias) < 3:
        return k_list[0]

    accels = []
    for i in range(1, len(inertias) - 1):
        accel = inertias[i - 1] - 2 * inertias[i] + inertias[i + 1]
        accels.append(accel)

    best_idx = accels.index(max(accels)) + 1  # +1 because accel starts at i=1
    best_k = k_list[best_idx]
    log(f"Elbow method selected K={best_k}", verbose)
    return best_k


def cluster_kmeans(
    embeddings: "np.ndarray",
    max_clusters: int = 50,
    verbose: bool = False,
) -> "np.ndarray":
    """Tier 2: KMeans with elbow method."""
    n = embeddings.shape[0]
    if n < 4:
        return np.zeros(n, dtype=int)

    k = _elbow_k(embeddings, max_clusters, verbose)
    log(f"Clustering with KMeans (K={k})...", verbose)
    km = SklearnKMeans(n_clusters=k, n_init=10, max_iter=300, random_state=42)
    labels = km.fit_predict(embeddings)

    try:
        score = silhouette_score(embeddings, labels)
        log(f"KMeans silhouette score: {score:.3f}", verbose)
    except Exception:
        pass

    return labels


def _bow_cosine(a: dict[str, float], b: dict[str, float]) -> float:
    """Cosine similarity between two sparse BoW vectors."""
    keys = set(a) & set(b)
    if not keys:
        return 0.0
    dot = sum(a[k] * b[k] for k in keys)
    return dot  # Already L2-normalized


def cluster_simple(
    vectors: list[dict[str, float]],
    max_clusters: int = 50,
    min_cluster_size: int = 5,
    verbose: bool = False,
) -> list[int]:
    """Tier 3: Simple greedy centroid clustering (stdlib only).

    Assigns each atom to the most similar existing centroid (if similarity
    exceeds threshold), otherwise creates a new cluster. Then merges
    clusters below min_cluster_size into nearest neighbor.
    """
    log("Clustering with simple centroid method (stdlib)...", verbose)
    n = len(vectors)
    if n == 0:
        return []

    # Greedy assignment with adaptive threshold
    threshold = 0.25
    clusters: list[list[int]] = []  # cluster -> list of doc indices
    centroids: list[dict[str, float]] = []

    for i, vec in enumerate(vectors):
        if not vec:
            # Empty vector — assign to noise
            best_cluster = -1
        else:
            best_sim = -1.0
            best_cluster = -1
            for ci, centroid in enumerate(centroids):
                sim = _bow_cosine(vec, centroid)
                if sim > best_sim:
                    best_sim = sim
                    best_cluster = ci

            if best_sim < threshold or best_cluster == -1:
                if len(clusters) < max_clusters:
                    # New cluster
                    clusters.append([i])
                    centroids.append(dict(vec))
                    continue
                # Else assign to best even if below threshold

        if best_cluster == -1:
            if not clusters:
                clusters.append([i])
                centroids.append(dict(vec))
            else:
                clusters[0].append(i)
        else:
            clusters[best_cluster].append(i)
            # Update centroid (running average)
            c = centroids[best_cluster]
            size = len(clusters[best_cluster])
            all_keys = set(c) | set(vec)
            for k in all_keys:
                old = c.get(k, 0.0)
                new = vec.get(k, 0.0)
                c[k] = old + (new - old) / size

    # Merge small clusters into nearest
    labels = [0] * n
    final_id = 0
    for ci, members in enumerate(clusters):
        if len(members) < min_cluster_size and len(clusters) > 1:
            # Find nearest other cluster
            best_merge = -1
            best_sim = -1.0
            for cj, _ in enumerate(clusters):
                if cj == ci or len(clusters[cj]) == 0:
                    continue
                sim = _bow_cosine(centroids[ci], centroids[cj])
                if sim > best_sim:
                    best_sim = sim
                    best_merge = cj
            if best_merge >= 0:
                clusters[best_merge].extend(members)
                clusters[ci] = []  # Empty it
                continue

    # Assign final labels
    label_map: dict[int, int] = {}
    next_label = 0
    for ci, members in enumerate(clusters):
        if not members:
            continue
        label_map[ci] = next_label
        next_label += 1
    for ci, members in enumerate(clusters):
        if not members:
            continue
        for idx in members:
            labels[idx] = label_map[ci]

    n_clusters = len([m for m in clusters if m])
    log(f"Simple clustering found {n_clusters} clusters", verbose)
    return labels


# ===================================================================
# 4. CLUSTER LABELING
# ===================================================================

def _extract_top_terms(
    atoms: list[dict],
    labels: list[int] | Any,
    n_terms: int = 8,
) -> dict[int, list[str]]:
    """Extract top TF-IDF-like terms per cluster for labeling."""
    stop_words = {
        "the", "a", "an", "is", "are", "was", "were", "be", "been", "have",
        "has", "had", "do", "does", "did", "will", "would", "could", "should",
        "may", "might", "can", "to", "of", "in", "for", "on", "with", "at",
        "by", "from", "as", "into", "through", "this", "that", "it", "its",
        "and", "or", "but", "not", "no", "so", "if", "than", "too", "very",
        "just", "also", "about", "more", "most", "some", "any", "all", "each",
        "which", "who", "what", "where", "when", "how", "been", "being",
        "there", "here", "they", "them", "their", "our", "your", "his", "her",
        "we", "you", "he", "she", "me", "my", "i",
    }

    def tokenize(text: str) -> list[str]:
        return [
            w for w in re.findall(r"[a-z][a-z0-9'-]*", text.lower())
            if w not in stop_words and len(w) > 2
        ]

    # Global DF
    all_texts = [_build_text(a) for a in atoms]
    n_docs = len(atoms)
    global_df: Counter = Counter()
    for text in all_texts:
        for w in set(tokenize(text)):
            global_df[w] += 1

    # Per-cluster TF
    labels_list = list(labels) if not isinstance(labels, list) else labels
    cluster_ids = sorted(set(labels_list))
    result: dict[int, list[str]] = {}

    for cid in cluster_ids:
        if cid == -1:
            result[-1] = ["(noise)"]
            continue
        indices = [i for i, l in enumerate(labels_list) if l == cid]
        tf: Counter = Counter()
        for idx in indices:
            tf.update(tokenize(all_texts[idx]))

        # Score by TF * IDF
        scored = []
        for w, count in tf.items():
            if global_df[w] < 2:
                continue
            idf = math.log((n_docs + 1) / (global_df[w] + 1)) + 1
            scored.append((w, count * idf))
        scored.sort(key=lambda x: -x[1])
        result[cid] = [w for w, _ in scored[:n_terms]]

    return result


def _generate_cluster_label(terms: list[str]) -> str:
    """Generate a short label from top terms."""
    if not terms or terms == ["(noise)"]:
        return "noise"
    return " / ".join(terms[:3])


# ===================================================================
# 5. OUTPUT
# ===================================================================

def write_cluster_results(
    atoms: list[dict],
    labels: list[int] | Any,
    cluster_terms: dict[int, list[str]],
    out_path: str,
    verbose: bool = False,
) -> None:
    """Write DYN-CLUSTER_RESULTS.jsonl."""
    labels_list = list(labels) if not isinstance(labels, list) else labels
    with open(out_path, "w") as fh:
        for atom, label in zip(atoms, labels_list):
            cid = int(label)
            terms = cluster_terms.get(cid, [])
            record = {
                "atom_id": atom["atom_id"],
                "source_id": atom.get("source_id", ""),
                "category": atom.get("category", ""),
                "content": atom["content"],
                "cluster_id": cid,
                "cluster_label": _generate_cluster_label(terms),
                "cluster_terms": terms[:5],
            }
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")
    log(f"Wrote {len(atoms)} clustered atoms to {out_path}", verbose)


def write_cluster_summary(
    atoms: list[dict],
    labels: list[int] | Any,
    cluster_terms: dict[int, list[str]],
    method_used: str,
    out_path: str,
    verbose: bool = False,
) -> None:
    """Write DYN-CLUSTER_SUMMARY.md — human-readable report."""
    labels_list = list(labels) if not isinstance(labels, list) else labels
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    cluster_sizes: Counter = Counter(labels_list)
    cluster_ids = sorted(set(labels_list))
    n_clusters = len([c for c in cluster_ids if c != -1])
    n_noise = cluster_sizes.get(-1, 0)

    # Category distribution per cluster
    cluster_categories: dict[int, Counter] = defaultdict(Counter)
    cluster_sources: dict[int, set] = defaultdict(set)
    for atom, label in zip(atoms, labels_list):
        cid = int(label)
        cluster_categories[cid][atom.get("category", "unknown")] += 1
        cluster_sources[cid].add(atom.get("source_id", "unknown"))

    lines: list[str] = []
    lines.append("# Cluster Analysis Summary")
    lines.append("")
    lines.append(f"**Generated**: {ts}")
    lines.append(f"**Method**: {method_used}")
    lines.append(f"**Total atoms**: {len(atoms)}")
    lines.append(f"**Clusters**: {n_clusters}")
    if n_noise > 0:
        lines.append(f"**Noise points**: {n_noise}")
    lines.append("")

    # Size distribution
    lines.append("## Size Distribution")
    lines.append("")
    sizes = sorted([cluster_sizes[c] for c in cluster_ids if c != -1],
                   reverse=True)
    if sizes:
        lines.append(f"- **Largest cluster**: {sizes[0]} atoms")
        lines.append(f"- **Smallest cluster**: {sizes[-1]} atoms")
        median_idx = len(sizes) // 2
        lines.append(f"- **Median cluster**: {sizes[median_idx]} atoms")
        lines.append(f"- **Mean cluster**: {sum(sizes) / len(sizes):.1f} atoms")
    lines.append("")

    # Histogram (text)
    lines.append("### Size Histogram")
    lines.append("")
    lines.append("| Size Range | Count |")
    lines.append("|-----------|-------|")
    if sizes:
        bins = [(1, 5), (6, 10), (11, 20), (21, 50), (51, 100), (101, 9999)]
        for lo, hi in bins:
            count = sum(1 for s in sizes if lo <= s <= hi)
            if count > 0:
                label = f"{lo}-{hi}" if hi < 9999 else f"{lo}+"
                lines.append(f"| {label} | {count} |")
    lines.append("")

    # Per-cluster detail
    lines.append("## Cluster Details")
    lines.append("")
    for cid in sorted(cluster_ids):
        if cid == -1:
            continue
        terms = cluster_terms.get(cid, [])
        label = _generate_cluster_label(terms)
        size = cluster_sizes[cid]
        cats = cluster_categories[cid]
        n_sources = len(cluster_sources[cid])

        lines.append(f"### Cluster {cid}: {label}")
        lines.append("")
        lines.append(f"- **Size**: {size} atoms from {n_sources} sources")
        lines.append(f"- **Top terms**: {', '.join(terms[:8])}")
        cat_str = ", ".join(f"{k}={v}" for k, v in cats.most_common(5))
        lines.append(f"- **Categories**: {cat_str}")
        lines.append("")

    # Noise section
    if n_noise > 0:
        lines.append("## Noise Points")
        lines.append("")
        lines.append(f"{n_noise} atoms did not fit any cluster. These may "
                     "represent unique insights or extraction artifacts.")
        noise_cats = cluster_categories.get(-1, Counter())
        if noise_cats:
            cat_str = ", ".join(f"{k}={v}" for k, v in noise_cats.most_common(5))
            lines.append(f"- **Categories**: {cat_str}")
        lines.append("")

    # Dependency tier note
    lines.append("## Method Notes")
    lines.append("")
    lines.append(f"- Clustering method: **{method_used}**")
    if "sentence-transformers" in method_used:
        lines.append("- Embeddings: all-MiniLM-L6-v2 (384-dim dense)")
    elif "tfidf" in method_used.lower():
        lines.append("- Embeddings: TF-IDF (sparse, max 5000 features)")
    else:
        lines.append("- Embeddings: Bag-of-words TF-IDF (stdlib)")
    lines.append("")

    with open(out_path, "w") as fh:
        fh.write("\n".join(lines))
    log(f"Wrote cluster summary to {out_path}", verbose)


# ===================================================================
# 6. METHOD RESOLUTION
# ===================================================================

def resolve_method(requested: str, verbose: bool = False) -> str:
    """Resolve 'auto' to the best available method."""
    if requested == "auto":
        if HAS_HDBSCAN and HAS_SENTENCE_TRANSFORMERS and HAS_NUMPY:
            method = "hdbscan"
        elif HAS_SKLEARN and HAS_NUMPY:
            method = "kmeans"
        else:
            method = "simple"
        log(f"Auto-resolved method: {method}", verbose)
        return method

    if requested == "hdbscan":
        if not HAS_HDBSCAN:
            log("HDBSCAN not available, falling back to kmeans", verbose)
            if HAS_SKLEARN and HAS_NUMPY:
                return "kmeans"
            return "simple"
        if not HAS_NUMPY:
            log("numpy not available, falling back to simple", verbose)
            return "simple"
        return "hdbscan"

    if requested == "kmeans":
        if not HAS_SKLEARN or not HAS_NUMPY:
            log("sklearn/numpy not available, falling back to simple", verbose)
            return "simple"
        return "kmeans"

    return "simple"


def resolve_embedding(method: str, verbose: bool = False) -> str:
    """Determine embedding strategy based on clustering method."""
    if method == "hdbscan" and HAS_SENTENCE_TRANSFORMERS:
        return "sentence-transformers"
    if method in ("hdbscan", "kmeans") and HAS_SKLEARN:
        return "tfidf"
    if method in ("hdbscan", "kmeans") and HAS_SENTENCE_TRANSFORMERS:
        return "sentence-transformers"
    return "bow"


# ===================================================================
# 7. MAIN PIPELINE
# ===================================================================

def run_pipeline(
    extract_dir: str,
    out_dir: str,
    method: str = "auto",
    min_cluster_size: int = 5,
    max_clusters: int = 50,
    verbose: bool = False,
) -> dict[str, Any]:
    """Full clustering pipeline: load -> embed -> cluster -> output."""

    # Load atoms
    atoms = load_atoms(extract_dir, verbose)
    if not atoms:
        log("ERROR: No atoms loaded. Check --extract-dir path.", True)
        return {"status": "error", "reason": "no atoms"}

    if len(atoms) < 3:
        log("WARNING: Too few atoms for meaningful clustering.", True)
        labels = list(range(len(atoms)))
        cluster_terms = {i: [atoms[i].get("category", "atom")]
                        for i in range(len(atoms))}
        method_used = "trivial (< 3 atoms)"
    else:
        # Resolve method
        method = resolve_method(method, verbose)
        embed_strategy = resolve_embedding(method, verbose)
        log(f"Pipeline: embed={embed_strategy}, cluster={method}", verbose)

        # Embed
        vectorizer = None
        if embed_strategy == "sentence-transformers":
            embeddings = embed_sentence_transformers(atoms, verbose)
        elif embed_strategy == "tfidf":
            embeddings, vectorizer = embed_tfidf(atoms, verbose)
        else:
            embeddings = embed_bow(atoms, verbose)

        # Cluster
        if method == "hdbscan":
            if embed_strategy == "sentence-transformers":
                labels = cluster_hdbscan(embeddings, min_cluster_size, verbose)
            else:
                # HDBSCAN on TF-IDF — need numpy array
                labels = cluster_hdbscan(
                    np.array(embeddings) if not isinstance(embeddings, np.ndarray)
                    else embeddings,
                    min_cluster_size, verbose
                )
        elif method == "kmeans":
            emb = (embeddings if isinstance(embeddings, np.ndarray)
                   else np.array(embeddings))
            labels = cluster_kmeans(emb, max_clusters, verbose)
        else:
            # Simple — works with BoW dicts or dense arrays
            if isinstance(embeddings, list) and embeddings and isinstance(embeddings[0], dict):
                labels = cluster_simple(embeddings, max_clusters,
                                       min_cluster_size, verbose)
            elif HAS_NUMPY and isinstance(embeddings, np.ndarray):
                # Convert dense to sparse dicts for simple clustering
                bow_vecs: list[dict[str, float]] = []
                for row in embeddings:
                    vec = {str(i): float(v) for i, v in enumerate(row) if v != 0}
                    bow_vecs.append(vec)
                labels = cluster_simple(bow_vecs, max_clusters,
                                       min_cluster_size, verbose)
            else:
                labels = cluster_simple(embeddings, max_clusters,
                                       min_cluster_size, verbose)

        method_used = f"{method} + {embed_strategy}"

        # Extract top terms for labels
        cluster_terms = _extract_top_terms(atoms, labels)

    # Ensure output directory exists
    os.makedirs(out_dir, exist_ok=True)

    results_path = os.path.join(out_dir, "DYN-CLUSTER_RESULTS.jsonl")
    summary_path = os.path.join(out_dir, "DYN-CLUSTER_SUMMARY.md")

    write_cluster_results(atoms, labels, cluster_terms, results_path, verbose)
    write_cluster_summary(atoms, labels, cluster_terms, method_used,
                          summary_path, verbose)

    labels_list = list(labels) if not isinstance(labels, list) else labels
    n_clusters = len(set(labels_list)) - (1 if -1 in labels_list else 0)

    result = {
        "status": "ok",
        "n_atoms": len(atoms),
        "n_clusters": n_clusters,
        "n_noise": labels_list.count(-1) if -1 in labels_list else 0,
        "method": method_used,
        "results_path": results_path,
        "summary_path": summary_path,
    }
    log(f"Pipeline complete: {json.dumps(result, indent=2)}", verbose)
    return result


# ===================================================================
# 8. CLI
# ===================================================================

def main() -> int:
    parser = argparse.ArgumentParser(
        description="DC-208-3 Cluster Engine — cluster extracted knowledge atoms",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Dependency tiers:
  Tier 1: sentence-transformers + hdbscan (best quality)
  Tier 2: sklearn TF-IDF + KMeans (good quality)
  Tier 3: stdlib bag-of-words + centroid (basic, no deps)

Examples:
  %(prog)s --extract-dir sources/04-SOURCES/_meta/ --out-dir sources/04-SOURCES/_meta/
  %(prog)s --extract-dir sources/04-SOURCES/_meta/ --method kmeans --max-clusters 30
  %(prog)s --extract-dir sources/04-SOURCES/_meta/ --method simple --verbose
        """,
    )
    parser.add_argument(
        "--extract-dir",
        required=True,
        help="Directory containing EXTRACT-*.jsonl files",
    )
    parser.add_argument(
        "--out-dir",
        required=True,
        help="Output directory for results and summary",
    )
    parser.add_argument(
        "--min-cluster-size",
        type=int,
        default=5,
        help="HDBSCAN min_cluster_size (default: 5)",
    )
    parser.add_argument(
        "--max-clusters",
        type=int,
        default=50,
        help="KMeans max clusters for elbow method (default: 50)",
    )
    parser.add_argument(
        "--method",
        choices=["auto", "hdbscan", "kmeans", "simple"],
        default="auto",
        help="Clustering method (default: auto — best available)",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose logging to stderr",
    )
    parser.add_argument(
        "--deps",
        action="store_true",
        help="Print dependency status and exit",
    )

    # Handle --deps before full arg validation
    if "--deps" in sys.argv:
        print(f"numpy:                {HAS_NUMPY}")
        print(f"sklearn:              {HAS_SKLEARN}")
        print(f"hdbscan:              {HAS_HDBSCAN}")
        print(f"sentence-transformers: {HAS_SENTENCE_TRANSFORMERS}")
        best = resolve_method("auto", verbose=False)
        print(f"auto method:          {best}")
        return 0

    args = parser.parse_args()

    if args.deps:
        print(f"numpy:                {HAS_NUMPY}")
        print(f"sklearn:              {HAS_SKLEARN}")
        print(f"hdbscan:              {HAS_HDBSCAN}")
        print(f"sentence-transformers: {HAS_SENTENCE_TRANSFORMERS}")
        best = resolve_method("auto", verbose=False)
        print(f"auto method:          {best}")
        return 0

    result = run_pipeline(
        extract_dir=args.extract_dir,
        out_dir=args.out_dir,
        method=args.method,
        min_cluster_size=args.min_cluster_size,
        max_clusters=args.max_clusters,
        verbose=args.verbose,
    )

    if result["status"] == "error":
        return 1

    # Print summary to stdout
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
