#!/usr/bin/env python3
"""DC-208-1: Source triage pipeline for the Syncrescendence mining system.

Reads DYN-SOURCES.csv + source file frontmatter, scores each source by
target density, embedding centrality, lineage potential, and domain priority,
then emits ranked triage JSON, a dependency DAG, and a Mermaid sidecar.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import logging
import os
import random
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Optional

import yaml

# ---------------------------------------------------------------------------
# Optional heavy imports — degrade gracefully
# ---------------------------------------------------------------------------

try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False

try:
    from sentence_transformers import SentenceTransformer
    HAS_SBERT = True
except ImportError:
    HAS_SBERT = False

try:
    import networkx as nx
    HAS_NX = True
except ImportError:
    HAS_NX = False

log = logging.getLogger("source_triage")

# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class SourceRecord:
    source_id: str
    filename: str
    filepath: str = ""
    signal_tier: str = ""
    status: str = ""
    topics: list[str] = field(default_factory=list)
    integration_targets: list[str] = field(default_factory=list)
    key_insights: list[str] = field(default_factory=list)
    synopsis: str = ""
    title: str = ""
    published_date: str = ""
    transcript_chars: int = 0
    chain: str = ""
    creator: str = ""
    platform: str = ""
    format: str = ""
    teleology: str = ""
    has_transcript: str = ""
    parse_error: bool = False
    _mtime_hash: str = ""


@dataclass
class ScoreBreakdown:
    source_id: str
    total: float = 0.0
    target_density: float = 0.0
    centrality: float = 0.0
    lineage: float = 0.0
    domain_priority: float = 0.0
    wildfire_promoted: bool = False


@dataclass
class DagEdge:
    from_source_id: str
    to_source_id: str
    edge_type: str
    confidence: float


# ---------------------------------------------------------------------------
# Config loader
# ---------------------------------------------------------------------------

def load_config(path: Optional[str]) -> dict:
    defaults = {
        "scoring": {
            "weights": {"target_density": 0.45, "centrality": 0.25, "lineage": 0.20, "domain_priority": 0.10},
            "domain_priority_map": {"paradigm": 1.0, "strategic": 0.8, "tactical": 0.5, "noise": 0.1},
            "domain_priority_default": 0.3,
        },
        "wildfire": {"pct": 0.05, "min_topic_diversity": 2},
        "embedding": {
            "model": "all-MiniLM-L6-v2",
            "fallback_model": "text-embedding-3-small",
            "fields": ["title", "key_insights", "synopsis"],
            "field_separator": " | ",
        },
        "scanning": {"thread_count": 8, "head_bytes": 4096},
        "cache": {"enabled": True, "filename_suffix": "_CACHE.json"},
        "output": {"top_k": 50, "mermaid_max_nodes": 80, "mermaid_max_edges": 200},
    }
    if path and Path(path).exists():
        with open(path) as f:
            user = yaml.safe_load(f) or {}
        _deep_merge(defaults, user)
    return defaults


def _deep_merge(base: dict, overlay: dict) -> None:
    for k, v in overlay.items():
        if k in base and isinstance(base[k], dict) and isinstance(v, dict):
            _deep_merge(base[k], v)
        else:
            base[k] = v


# ---------------------------------------------------------------------------
# CSV loading
# ---------------------------------------------------------------------------

def load_dyn_sources_csv(path: str) -> list[SourceRecord]:
    records: list[SourceRecord] = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            topics_raw = row.get("topics", "")
            topics = [t.strip() for t in topics_raw.split(",") if t.strip()] if topics_raw else []
            integrated_raw = row.get("integrated_into", "")
            targets = [t.strip() for t in integrated_raw.split(",") if t.strip()] if integrated_raw else []

            rec = SourceRecord(
                source_id=row.get("id", "").strip(),
                filename=row.get("filename", "").strip(),
                filepath=row.get("filepath", "").strip(),
                signal_tier=row.get("signal_tier", "").strip(),
                status=row.get("status", "").strip(),
                topics=topics,
                integration_targets=targets,
                title=row.get("title", "").strip(),
                published_date=row.get("date_published", "").strip(),
                chain=row.get("chain", "").strip(),
                creator=row.get("creator", "").strip(),
                platform=row.get("platform", "").strip(),
                format=row.get("format", "").strip(),
            )
            if rec.source_id:
                records.append(rec)
    log.info("Loaded %d records from CSV", len(records))
    return records


# ---------------------------------------------------------------------------
# Frontmatter scanning
# ---------------------------------------------------------------------------

_YAML_FENCE = re.compile(r"^---\s*$", re.MULTILINE)
# For files that start with key: value without --- fence
_BARE_YAML_KEY = re.compile(r"^[a-z_]+:\s", re.MULTILINE)


def _extract_yaml_block(text: str) -> Optional[str]:
    """Extract the first YAML block from text. Handles both fenced (---) and bare frontmatter."""
    fences = list(_YAML_FENCE.finditer(text))
    if len(fences) >= 2:
        return text[fences[0].end():fences[1].start()]

    # Bare frontmatter: file starts with yaml-like keys without --- fence
    # (33 files start with has_transcript: yes)
    if _BARE_YAML_KEY.match(text):
        lines = text.split("\n")
        yaml_lines = []
        for line in lines:
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                break
            # Stop if we hit markdown content
            if stripped.startswith("# ") and not stripped.startswith("#  "):
                break
            yaml_lines.append(line)
        if yaml_lines:
            return "\n".join(yaml_lines)

    # Try finding --- deeper in the first 4KB
    if fences:
        # Single fence found — look for end of block by next fence or EOF
        start = fences[0].end()
        # Scan for second fence after the first
        rest = text[start:]
        m = _YAML_FENCE.search(rest)
        if m:
            return rest[:m.start()]

    return None


def _parse_source_frontmatter(filepath: Path, head_bytes: int) -> dict[str, Any]:
    result: dict[str, Any] = {"_parse_error": False, "_mtime_hash": ""}
    try:
        stat = filepath.stat()
        result["_mtime_hash"] = hashlib.md5(
            f"{filepath.name}:{stat.st_mtime_ns}:{stat.st_size}".encode()
        ).hexdigest()

        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            head = f.read(head_bytes)

        yaml_block = _extract_yaml_block(head)
        if not yaml_block:
            result["_parse_error"] = True
            return result

        parsed = yaml.safe_load(yaml_block)
        if isinstance(parsed, dict):
            result.update(parsed)
        else:
            result["_parse_error"] = True
    except Exception as exc:
        log.warning("Frontmatter parse error for %s: %s", filepath, exc)
        result["_parse_error"] = True
    return result


def scan_source_frontmatter(
    source_dir: str,
    records: list[SourceRecord],
    config: dict,
    cache: dict[str, dict],
) -> dict[str, dict]:
    """Scan source files with ThreadPoolExecutor, enrich records in-place, return new cache."""
    head_bytes = config["scanning"]["head_bytes"]
    thread_count = config["scanning"]["thread_count"]
    source_path = Path(source_dir)
    new_cache: dict[str, dict] = {}

    # Build lookup: source_id -> record
    id_to_rec = {r.source_id: r for r in records}

    # Collect files to scan
    md_files = list(source_path.glob("SOURCE-*.md"))
    log.info("Found %d SOURCE-*.md files to scan", len(md_files))

    # Map filename -> filepath for matching
    fname_to_path: dict[str, Path] = {}
    for p in md_files:
        fname_to_path[p.name] = p

    # Also index by source_id extracted from frontmatter (second pass enrichment)
    results: dict[str, dict] = {}

    def _scan_one(fpath: Path) -> tuple[str, dict]:
        # Check cache by mtime hash
        stat = fpath.stat()
        mtime_hash = hashlib.md5(
            f"{fpath.name}:{stat.st_mtime_ns}:{stat.st_size}".encode()
        ).hexdigest()
        cached = cache.get(fpath.name)
        if cached and cached.get("_mtime_hash") == mtime_hash:
            return fpath.name, cached
        return fpath.name, _parse_source_frontmatter(fpath, head_bytes)

    with ThreadPoolExecutor(max_workers=thread_count) as pool:
        futures = {pool.submit(_scan_one, fp): fp for fp in md_files}
        for fut in as_completed(futures):
            fname, fm = fut.result()
            results[fname] = fm
            new_cache[fname] = fm

    # Enrich records from frontmatter
    parse_errors = 0
    for rec in records:
        # Try matching by filename
        fm = results.get(rec.filename)
        if not fm:
            # Try matching by source_id pattern in filename
            for fname, fdata in results.items():
                if fdata.get("id") == rec.source_id:
                    fm = fdata
                    break
        if not fm:
            continue

        if fm.get("_parse_error"):
            rec.parse_error = True
            parse_errors += 1
            continue

        rec._mtime_hash = fm.get("_mtime_hash", "")
        rec.synopsis = fm.get("synopsis", "") or rec.synopsis
        rec.teleology = fm.get("teleology", "") or rec.teleology
        rec.has_transcript = str(fm.get("has_transcript", "")) or rec.has_transcript

        fm_insights = fm.get("key_insights")
        if isinstance(fm_insights, list) and fm_insights:
            rec.key_insights = [str(i) for i in fm_insights if i]

        fm_topics = fm.get("topics")
        if isinstance(fm_topics, list) and fm_topics:
            rec.topics = [str(t) for t in fm_topics if t]

        fm_targets = fm.get("integrated_into")
        if isinstance(fm_targets, list) and fm_targets:
            rec.integration_targets = [str(t) for t in fm_targets if t]

        if not rec.signal_tier:
            rec.signal_tier = fm.get("signal_tier", "") or ""

        if not rec.title:
            rec.title = fm.get("title", "") or ""

    log.info("Frontmatter enrichment complete. Parse errors: %d", parse_errors)
    return new_cache


# ---------------------------------------------------------------------------
# Embedding centrality
# ---------------------------------------------------------------------------

def _build_embedding_text(rec: SourceRecord, emb_config: dict) -> str:
    sep = emb_config.get("field_separator", " | ")
    parts = []
    for f in emb_config.get("fields", ["title", "key_insights", "synopsis"]):
        val = getattr(rec, f, None)
        if val is None:
            continue
        if isinstance(val, list):
            parts.append("; ".join(str(v) for v in val if v))
        elif val:
            parts.append(str(val))
    return sep.join(parts)


def compute_embedding_centrality(
    records: list[SourceRecord], config: dict
) -> dict[str, float]:
    emb_config = config["embedding"]
    texts = [_build_embedding_text(r, emb_config) for r in records]
    ids = [r.source_id for r in records]

    if not any(t.strip() for t in texts):
        log.warning("No text content for embeddings; centrality will be zero")
        return {sid: 0.0 for sid in ids}

    embeddings = None

    if HAS_SBERT and HAS_NUMPY:
        model_name = emb_config["model"]
        try:
            log.info("Loading sentence-transformers model: %s", model_name)
            model = SentenceTransformer(model_name)
            embeddings = model.encode(texts, show_progress_bar=False, normalize_embeddings=True)
            embeddings = np.array(embeddings)
        except Exception as exc:
            log.warning("sentence-transformers failed (%s), trying fallback", exc)
            embeddings = None

    if embeddings is None and HAS_NUMPY:
        # Fallback: OpenAI text-embedding-3-small
        api_key = os.environ.get("OPENAI_API_KEY")
        if api_key:
            try:
                embeddings = _openai_embed(texts, emb_config["fallback_model"], api_key)
            except Exception as exc:
                log.warning("OpenAI embedding fallback failed: %s", exc)

    if embeddings is None:
        # Last resort: TF-IDF-like cosine via bag-of-words
        log.warning("No embedding model available; using bag-of-words centrality proxy")
        return _bow_centrality(texts, ids)

    # Cosine similarity matrix (embeddings already L2-normalized if sbert)
    norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
    norms = np.where(norms == 0, 1, norms)
    normed = embeddings / norms
    sim_matrix = normed @ normed.T

    # Centrality = mean similarity to all others (excluding self)
    n = len(ids)
    centralities: dict[str, float] = {}
    for i, sid in enumerate(ids):
        if n <= 1:
            centralities[sid] = 1.0
        else:
            row_sum = float(sim_matrix[i].sum()) - float(sim_matrix[i, i])
            centralities[sid] = row_sum / (n - 1)

    # Normalize to [0, 1]
    if centralities:
        cmin = min(centralities.values())
        cmax = max(centralities.values())
        span = cmax - cmin if cmax > cmin else 1.0
        centralities = {k: (v - cmin) / span for k, v in centralities.items()}

    return centralities


def _openai_embed(texts: list[str], model: str, api_key: str):
    """Minimal OpenAI embeddings call without the openai SDK."""
    import urllib.request

    # Batch in groups of 100
    all_embeddings = []
    for i in range(0, len(texts), 100):
        batch = texts[i:i + 100]
        payload = json.dumps({"input": batch, "model": model}).encode()
        req = urllib.request.Request(
            "https://api.openai.com/v1/embeddings",
            data=payload,
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read())
        sorted_data = sorted(data["data"], key=lambda x: x["index"])
        all_embeddings.extend([d["embedding"] for d in sorted_data])

    import numpy as np
    return np.array(all_embeddings)


def _bow_centrality(texts: list[str], ids: list[str]) -> dict[str, float]:
    """Bag-of-words Jaccard centrality as last-resort fallback."""
    tokenized = []
    for t in texts:
        tokens = set(re.findall(r"[a-z0-9]+", t.lower()))
        tokenized.append(tokens)

    n = len(ids)
    centralities: dict[str, float] = {}
    for i, sid in enumerate(ids):
        if n <= 1:
            centralities[sid] = 1.0
            continue
        total = 0.0
        for j in range(n):
            if i == j:
                continue
            union = tokenized[i] | tokenized[j]
            if union:
                total += len(tokenized[i] & tokenized[j]) / len(union)
        centralities[sid] = total / (n - 1)

    if centralities:
        cmin = min(centralities.values())
        cmax = max(centralities.values())
        span = cmax - cmin if cmax > cmin else 1.0
        centralities = {k: (v - cmin) / span for k, v in centralities.items()}

    return centralities


# ---------------------------------------------------------------------------
# Lineage potential
# ---------------------------------------------------------------------------

def compute_lineage_potential(records: list[SourceRecord]) -> dict[str, float]:
    """Score lineage potential based on integration targets, insights density, and chain membership."""
    scores: dict[str, float] = {}
    max_targets = max((len(r.integration_targets) for r in records), default=1) or 1
    max_insights = max((len(r.key_insights) for r in records), default=1) or 1

    for rec in records:
        target_score = len(rec.integration_targets) / max_targets
        insight_score = len(rec.key_insights) / max_insights
        chain_bonus = 0.15 if rec.chain and rec.chain.lower() not in ("", "null", "none") else 0.0
        transcript_bonus = 0.10 if rec.has_transcript in ("yes", "true", "True", "1") else 0.0
        scores[rec.source_id] = min(1.0, target_score * 0.4 + insight_score * 0.35 + chain_bonus + transcript_bonus)

    return scores


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

def score_source(
    rec: SourceRecord,
    weights: dict[str, float],
    domain_map: dict[str, float],
    domain_default: float,
    centrality: float,
    lineage: float,
) -> ScoreBreakdown:
    # Target density: normalized count of integration targets
    # (absolute count; normalized later across all records)
    td_raw = len(rec.integration_targets)

    dp = domain_map.get(rec.signal_tier.lower(), domain_default) if rec.signal_tier else domain_default

    return ScoreBreakdown(
        source_id=rec.source_id,
        target_density=td_raw,  # will be normalized
        centrality=centrality,
        lineage=lineage,
        domain_priority=dp,
    )


def score_all(
    records: list[SourceRecord],
    centralities: dict[str, float],
    lineages: dict[str, float],
    config: dict,
) -> list[ScoreBreakdown]:
    w = config["scoring"]["weights"]
    dmap = config["scoring"]["domain_priority_map"]
    ddef = config["scoring"]["domain_priority_default"]

    scores = []
    for rec in records:
        sb = score_source(
            rec, w, dmap, ddef,
            centralities.get(rec.source_id, 0.0),
            lineages.get(rec.source_id, 0.0),
        )
        scores.append(sb)

    # Normalize target_density across all records
    max_td = max((s.target_density for s in scores), default=1) or 1
    for s in scores:
        s.target_density = s.target_density / max_td

    # Compute totals
    for s in scores:
        s.total = (
            w["target_density"] * s.target_density
            + w["centrality"] * s.centrality
            + w["lineage"] * s.lineage
            + w["domain_priority"] * s.domain_priority
        )

    scores.sort(key=lambda s: s.total, reverse=True)
    return scores


# ---------------------------------------------------------------------------
# Wildfire promotion
# ---------------------------------------------------------------------------

def apply_wildfire(
    scores: list[ScoreBreakdown],
    records: list[SourceRecord],
    top_k: int,
    wildfire_pct: float,
    min_topic_diversity: int,
) -> list[ScoreBreakdown]:
    """Randomly elevate lowest-ranked sources with a topic-diversity constraint."""
    if wildfire_pct <= 0 or top_k <= 0:
        return scores

    n_wildfire = max(1, int(top_k * wildfire_pct))
    if len(scores) <= top_k:
        return scores

    id_to_rec = {r.source_id: r for r in records}

    # Topics already covered by top-k
    top_ids = {s.source_id for s in scores[:top_k]}
    covered_topics: set[str] = set()
    for sid in top_ids:
        rec = id_to_rec.get(sid)
        if rec:
            covered_topics.update(t.lower() for t in rec.topics)

    # Candidates: everything outside top-k
    candidates = scores[top_k:]
    random.shuffle(candidates)

    promoted: list[ScoreBreakdown] = []
    for cand in candidates:
        if len(promoted) >= n_wildfire:
            break
        rec = id_to_rec.get(cand.source_id)
        if not rec:
            continue
        new_topics = {t.lower() for t in rec.topics} - covered_topics
        if len(new_topics) >= min_topic_diversity or len(promoted) == 0:
            cand.wildfire_promoted = True
            promoted.append(cand)
            covered_topics.update(new_topics)

    # If we didn't get enough with diversity constraint, fill remainder
    if len(promoted) < n_wildfire:
        for cand in candidates:
            if cand.wildfire_promoted:
                continue
            if len(promoted) >= n_wildfire:
                break
            cand.wildfire_promoted = True
            promoted.append(cand)

    # Insert wildfire picks at end of top-k
    top_section = scores[:top_k]
    remaining = [s for s in scores[top_k:] if not s.wildfire_promoted]
    result = top_section + promoted + remaining
    return result


# ---------------------------------------------------------------------------
# Dependency DAG
# ---------------------------------------------------------------------------

def build_dependency_dag(
    records: list[SourceRecord],
) -> tuple[list[dict], list[DagEdge]]:
    """Build DAG edges from chain membership, shared topics, and integration targets."""
    id_to_rec = {r.source_id: r for r in records}
    edges: list[DagEdge] = []
    seen: set[tuple[str, str, str]] = set()

    # Chain-based edges: sources in the same chain form a sequence by published_date
    chain_groups: dict[str, list[SourceRecord]] = {}
    for rec in records:
        c = rec.chain.strip().lower() if rec.chain else ""
        if c and c not in ("null", "none", ""):
            chain_groups.setdefault(c, []).append(rec)

    for chain_name, members in chain_groups.items():
        # Sort by published_date
        dated = sorted(members, key=lambda r: r.published_date or "0000")
        for i in range(len(dated) - 1):
            key = (dated[i].source_id, dated[i + 1].source_id, "chain_sequence")
            if key not in seen:
                seen.add(key)
                edges.append(DagEdge(
                    from_source_id=dated[i].source_id,
                    to_source_id=dated[i + 1].source_id,
                    edge_type="chain_sequence",
                    confidence=0.9,
                ))

    # Integration target edges: if source A lists target X, and source B's filename
    # contains X, then A -> B (A feeds into B)
    target_index: dict[str, list[str]] = {}  # target_string -> [source_ids that mention it]
    for rec in records:
        for t in rec.integration_targets:
            target_index.setdefault(t.strip().lower(), []).append(rec.source_id)

    # Topic co-occurrence edges (high overlap = dependency signal)
    topic_index: dict[str, list[str]] = {}
    for rec in records:
        for t in rec.topics:
            topic_index.setdefault(t.strip().lower(), []).append(rec.source_id)

    for topic, sids in topic_index.items():
        if len(sids) < 2 or len(sids) > 20:
            continue
        for i in range(len(sids)):
            for j in range(i + 1, len(sids)):
                a, b = sids[i], sids[j]
                # Direction: earlier published -> later published
                ra, rb = id_to_rec.get(a), id_to_rec.get(b)
                if not ra or not rb:
                    continue
                da = ra.published_date or "9999"
                db = rb.published_date or "9999"
                if da <= db:
                    src, dst = a, b
                else:
                    src, dst = b, a
                key = (src, dst, "topic_overlap")
                if key not in seen:
                    seen.add(key)
                    # Confidence based on topic specificity
                    confidence = min(0.7, 1.0 / len(sids))
                    edges.append(DagEdge(
                        from_source_id=src,
                        to_source_id=dst,
                        edge_type="topic_overlap",
                        confidence=round(confidence, 3),
                    ))

    nodes = [{"id": r.source_id, "title": r.title, "signal_tier": r.signal_tier} for r in records]
    return nodes, edges


# ---------------------------------------------------------------------------
# Persistence
# ---------------------------------------------------------------------------

def persist_triage_outputs(
    scores: list[ScoreBreakdown],
    records: list[SourceRecord],
    nodes: list[dict],
    edges: list[DagEdge],
    cache: dict[str, dict],
    out_prefix: str,
    config: dict,
    top_k: int,
) -> None:
    id_to_rec = {r.source_id: r for r in records}

    # --- Triage JSON ---
    triage_path = f"{out_prefix}_TRIAGE.json"
    triage_records = []
    for rank, sb in enumerate(scores[:top_k], 1):
        rec = id_to_rec.get(sb.source_id)
        entry = asdict(sb)
        entry["rank"] = rank
        if rec:
            entry["filename"] = rec.filename
            entry["title"] = rec.title
            entry["signal_tier"] = rec.signal_tier
            entry["topics"] = rec.topics
            entry["parse_error"] = rec.parse_error
        entry["total"] = round(entry["total"], 4)
        entry["target_density"] = round(entry["target_density"], 4)
        entry["centrality"] = round(entry["centrality"], 4)
        entry["lineage"] = round(entry["lineage"], 4)
        entry["domain_priority"] = round(entry["domain_priority"], 4)
        triage_records.append(entry)

    triage_output = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "total_sources": len(records),
        "top_k": top_k,
        "wildfire_promoted": sum(1 for s in scores[:top_k] if s.wildfire_promoted),
        "records": triage_records,
    }
    _write_json(triage_path, triage_output)
    log.info("Wrote triage: %s (%d records)", triage_path, len(triage_records))

    # --- DAG JSON ---
    dag_path = f"{out_prefix}_DEPENDENCY_DAG.json"
    dag_output = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "node_count": len(nodes),
        "edge_count": len(edges),
        "nodes": nodes,
        "edges": [asdict(e) for e in edges],
    }
    _write_json(dag_path, dag_output)
    log.info("Wrote DAG: %s (%d nodes, %d edges)", dag_path, len(nodes), len(edges))

    # --- Mermaid sidecar ---
    mmd_path = f"{out_prefix}_DEPENDENCY_DAG.mmd"
    max_nodes = config["output"]["mermaid_max_nodes"]
    max_edges = config["output"]["mermaid_max_edges"]
    _write_mermaid(mmd_path, nodes, edges, scores, top_k, max_nodes, max_edges)
    log.info("Wrote Mermaid: %s", mmd_path)

    # --- Cache ---
    if config["cache"]["enabled"]:
        cache_path = f"{out_prefix}{config['cache']['filename_suffix']}"
        _write_json(cache_path, cache)
        log.info("Wrote cache: %s", cache_path)


class _SafeEncoder(json.JSONEncoder):
    def default(self, obj):
        import datetime
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        return super().default(obj)


def _write_json(path: str, data: Any) -> None:
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False, cls=_SafeEncoder)
        f.write("\n")
    os.replace(tmp, path)


def _write_mermaid(
    path: str,
    nodes: list[dict],
    edges: list[DagEdge],
    scores: list[ScoreBreakdown],
    top_k: int,
    max_nodes: int,
    max_edges: int,
) -> None:
    # Only include top-k nodes in mermaid for readability
    top_ids = {s.source_id for s in scores[:min(top_k, max_nodes)]}
    score_map = {s.source_id: s for s in scores}

    lines = ["flowchart LR"]

    # Node definitions
    for node in nodes:
        nid = node["id"]
        if nid not in top_ids:
            continue
        safe_id = _mermaid_id(nid)
        label = (node.get("title") or nid)[:50].replace('"', "'")
        tier = node.get("signal_tier", "")
        sb = score_map.get(nid)
        suffix = ""
        if sb and sb.wildfire_promoted:
            suffix = " 🔥"
        lines.append(f'    {safe_id}["{label}{suffix}"]')
        if tier == "paradigm":
            lines.append(f"    style {safe_id} fill:#e6ffe6,stroke:#2d8632")
        elif tier == "strategic":
            lines.append(f"    style {safe_id} fill:#e6f0ff,stroke:#2d5086")
        elif tier == "noise":
            lines.append(f"    style {safe_id} fill:#ffe6e6,stroke:#862d2d")

    # Edges (limited)
    edge_count = 0
    for e in edges:
        if edge_count >= max_edges:
            break
        if e.from_source_id in top_ids and e.to_source_id in top_ids:
            src = _mermaid_id(e.from_source_id)
            dst = _mermaid_id(e.to_source_id)
            label = e.edge_type[:12]
            lines.append(f"    {src} -->|{label}| {dst}")
            edge_count += 1

    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    os.replace(tmp, path)


def _mermaid_id(source_id: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_]", "_", source_id)


# ---------------------------------------------------------------------------
# Cache loading
# ---------------------------------------------------------------------------

def load_cache(out_prefix: str, config: dict) -> dict[str, dict]:
    if not config["cache"]["enabled"]:
        return {}
    cache_path = f"{out_prefix}{config['cache']['filename_suffix']}"
    if Path(cache_path).exists():
        try:
            with open(cache_path, encoding="utf-8") as f:
                return json.load(f)
        except Exception as exc:
            log.warning("Failed to load cache: %s", exc)
    return {}


# ---------------------------------------------------------------------------
# Mode filters
# ---------------------------------------------------------------------------

def apply_mode_filter(records: list[SourceRecord], mode: str) -> list[SourceRecord]:
    """Filter records based on triage mode."""
    if mode == "all":
        return records
    if mode == "paradigm":
        return [r for r in records if r.signal_tier.lower() in ("paradigm", "strategic", "")]
    if mode == "tactical":
        return [r for r in records if r.signal_tier.lower() in ("tactical", "paradigm", "strategic", "")]
    if mode == "unprocessed":
        return [r for r in records if r.status.lower() in ("raw", "triaged", "")]
    log.warning("Unknown mode '%s', using all records", mode)
    return records


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="DC-208-1: Source triage pipeline for Syncrescendence mining.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--csv", required=True, help="Path to DYN-SOURCES.csv")
    p.add_argument("--sources-dir", required=True, help="Path to sources/04-SOURCES directory")
    p.add_argument("--config", default=None, help="Path to source_triage_config.yaml")
    p.add_argument("--mode", default="paradigm", choices=["all", "paradigm", "tactical", "unprocessed"],
                    help="Triage mode filter (default: paradigm)")
    p.add_argument("--top-k", type=int, default=None, help="Override top-k from config")
    p.add_argument("--wildfire-pct", type=float, default=None, help="Override wildfire percentage")
    p.add_argument("--out-prefix", required=True, help="Output file prefix (e.g., sources/04-SOURCES/_meta/DYN-SOURCE)")
    p.add_argument("--seed", type=int, default=None, help="Random seed for reproducibility")
    p.add_argument("--no-cache", action="store_true", help="Disable frontmatter cache")
    p.add_argument("--no-embeddings", action="store_true", help="Skip embedding computation (use BoW fallback)")
    p.add_argument("-v", "--verbose", action="store_true", help="Debug logging")
    return p


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )

    # Auto-discover config beside the script if not specified
    if not args.config:
        script_dir = Path(__file__).parent
        default_config = script_dir / "source_triage_config.yaml"
        if default_config.exists():
            args.config = str(default_config)

    config = load_config(args.config)

    if args.no_cache:
        config["cache"]["enabled"] = False
    if args.top_k is not None:
        config["output"]["top_k"] = args.top_k
    if args.wildfire_pct is not None:
        config["wildfire"]["pct"] = args.wildfire_pct
    if args.seed is not None:
        random.seed(args.seed)

    top_k = config["output"]["top_k"]
    wildfire_pct = config["wildfire"]["pct"]
    min_topic_div = config["wildfire"]["min_topic_diversity"]

    # Validate paths
    csv_path = Path(args.csv)
    if not csv_path.exists():
        log.error("CSV not found: %s", csv_path)
        return 1
    sources_dir = Path(args.sources_dir)
    if not sources_dir.is_dir():
        log.error("Sources directory not found: %s", sources_dir)
        return 1

    # Ensure output directory exists
    out_dir = Path(args.out_prefix).parent
    out_dir.mkdir(parents=True, exist_ok=True)

    # --- Pipeline ---

    log.info("=== Source Triage Pipeline (DC-208-1) ===")
    log.info("Mode: %s | top-k: %d | wildfire: %.0f%%", args.mode, top_k, wildfire_pct * 100)

    # 1. Load CSV
    all_records = load_dyn_sources_csv(str(csv_path))
    if not all_records:
        log.error("No records loaded from CSV")
        return 1

    # 2. Scan frontmatter
    cache = load_cache(args.out_prefix, config)
    new_cache = scan_source_frontmatter(str(sources_dir), all_records, config, cache)

    # 3. Mode filter
    records = apply_mode_filter(all_records, args.mode)
    log.info("After mode filter: %d / %d records", len(records), len(all_records))

    if not records:
        log.warning("No records after filtering; writing empty outputs")
        records = all_records  # fallback to all

    # 4. Embedding centrality
    if args.no_embeddings:
        centralities = _bow_centrality(
            [_build_embedding_text(r, config["embedding"]) for r in records],
            [r.source_id for r in records],
        )
    else:
        centralities = compute_embedding_centrality(records, config)

    # 5. Lineage potential
    lineages = compute_lineage_potential(records)

    # 6. Score
    scores = score_all(records, centralities, lineages, config)

    # 7. Wildfire
    scores = apply_wildfire(scores, records, top_k, wildfire_pct, min_topic_div)

    # 8. DAG
    nodes, edges = build_dependency_dag(records)

    # 9. Persist
    persist_triage_outputs(scores, records, nodes, edges, new_cache, args.out_prefix, config, top_k)

    log.info("=== Pipeline complete ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
