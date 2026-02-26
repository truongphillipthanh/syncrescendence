#!/usr/bin/env python3
"""lattice_annealer.py - pre-promotion lattice coherence gate (CC35 Section 2)."""

from __future__ import annotations

import argparse
import datetime as dt
import fcntl
import json
import math
import os
import re
import tempfile
import time
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "1.0.0"
DIM_KEYS = (
    "cognitive",
    "semiotic",
    "psychological",
    "phenomenological",
    "volitional",
    "embodied",
    "behavioral",
    "characterological",
    "aesthetic",
    "linguistic",
    "social",
    "spiritual",
    "temporal",
    "environmental",
)
NDIM = len(DIM_KEYS)

# Core integrative axes for hypervolume scoring
CORE_AXES = ("cognitive", "semiotic", "psychological", "volitional", "social")

LEGACY_DIM_KEYS = (
    "mode_of_access",
    "content_domain",
    "transformative_depth",
    "social_distribution",
    "practical_application",
)
LEGACY_DIM_MAP = {
    "mode_of_access": "behavioral",
    "content_domain": "cognitive",
    "transformative_depth": "volitional",
    "social_distribution": "social",
    "practical_application": "behavioral",
}


def map_legacy_dim(v: dict[str, float]) -> dict[str, float]:
    """Map legacy 5-dim vector to 14-dim, zero-filling unmapped."""
    out = {k: 0.0 for k in DIM_KEYS}
    for old_key, new_key in LEGACY_DIM_MAP.items():
        if old_key in v:
            out[new_key] = max(out[new_key], float(v[old_key]))
    return out

STATE_REL = "orchestration/00-ORCHESTRATION/state"
LOCK_DIR_REL = f"{STATE_REL}/locks"
INDEX_REL = f"{STATE_REL}/DYN-LATTICE_INDEX.json"
HEALTH_REL = f"{STATE_REL}/DYN-LATTICE_HEALTH.json"
ANNEAL_LOG_REL = f"{STATE_REL}/DYN-LATTICE_ANNEAL_LOG.jsonl"
REPAIR_QUEUE_REL = f"{STATE_REL}/DYN-LATTICE_REPAIR_QUEUE.jsonl"
REBUILD_QUEUE_REL = f"{STATE_REL}/DYN-LATTICE_REBUILD_QUEUE.jsonl"

GATE_V1_REL = "canon/01-CANON/CANON-ONTOLOGY-GATE_v1.md"
ROSETTA_REL = "engine/02-ENGINE/REF-ROSETTA_STONE.md"
SN_DIR_REL = "canon/01-CANON/sn"

LOCK_ORDER = ("LOCK_LATTICE_INDEX", "LOCK_LATTICE_HEALTH", "LOCK_ANNEAL_LOG")
LOCK_TIMEOUT = 5.0
INDEX_STALE_SEC = 24 * 3600
TOP_K = 5


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")


def clamp(lo: float, hi: float, x: float) -> float:
    return max(lo, min(hi, x))


def fnum(v: Any, d: float = 0.0) -> float:
    try:
        return float(v)
    except (TypeError, ValueError):
        return d


def resolve(repo_root: Path, p: str) -> Path:
    path = Path(p)
    return path if path.is_absolute() else (repo_root / path).resolve()


def parse_iso(s: str) -> dt.datetime:
    t = s.strip()
    if t.endswith("Z"):
        t = t[:-1] + "+00:00"
    return dt.datetime.fromisoformat(t)


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json_atomic(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(data, fh, ensure_ascii=True, indent=2, sort_keys=True)
            fh.write("\n")
        os.replace(tmp, path)
    except Exception:
        try:
            os.unlink(tmp)
        except Exception:
            pass
        raise


def append_jsonl(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, ensure_ascii=True, sort_keys=True) + "\n")


def pid_alive(pid: int) -> bool:
    if pid <= 0:
        return False
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def parse_lock_pid(text: str) -> int | None:
    line = (text.splitlines() or [""])[0].strip()
    return int(line) if line.isdigit() else None


def acquire_lock(lock_dir: Path, name: str, timeout: float = LOCK_TIMEOUT):
    lock_dir.mkdir(parents=True, exist_ok=True)
    path = lock_dir / f"{name}.lock"
    deadline = time.monotonic() + timeout
    while time.monotonic() <= deadline:
        fh = path.open("a+", encoding="utf-8")
        try:
            fcntl.flock(fh.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            fh.seek(0)
            fh.truncate()
            fh.write(f"{os.getpid()}\n{now_iso()}\n")
            fh.flush()
            return fh
        except BlockingIOError:
            fh.seek(0)
            pid = parse_lock_pid(fh.read())
            fh.close()
            if pid is not None and not pid_alive(pid):
                try:
                    path.unlink(missing_ok=True)
                except Exception:
                    pass
            time.sleep(0.05)
    raise RuntimeError(f"LOCK_TIMEOUT:{name}")


def acquire_locks(lock_dir: Path):
    held = []
    try:
        for name in LOCK_ORDER:
            held.append(acquire_lock(lock_dir, name))
        return held
    except Exception:
        for fh in reversed(held):
            try:
                fcntl.flock(fh.fileno(), fcntl.LOCK_UN)
                fh.close()
            except Exception:
                pass
        raise


def release_locks(held) -> None:
    for fh in reversed(held):
        try:
            fcntl.flock(fh.fileno(), fcntl.LOCK_UN)
        except Exception:
            pass
        try:
            fh.close()
        except Exception:
            pass


def vec_list(v: Any) -> list[float]:
    if isinstance(v, list):
        if len(v) == 5:
            # Legacy 5-dim list — map to 14-dim via positional legacy keys
            legacy = {LEGACY_DIM_KEYS[i]: clamp(0.0, 1.0, fnum(v[i])) for i in range(5)}
            mapped = map_legacy_dim(legacy)
            return [mapped[k] for k in DIM_KEYS]
        if len(v) != NDIM:
            raise ValueError(f"dimension_vector list must be length {NDIM} (or 5 for legacy)")
        return [clamp(0.0, 1.0, fnum(x)) for x in v]
    if isinstance(v, dict):
        # Detect legacy 5-dim dict
        if set(v.keys()) <= set(LEGACY_DIM_KEYS) and not set(v.keys()) & set(DIM_KEYS):
            mapped = map_legacy_dim(v)
            return [clamp(0.0, 1.0, fnum(mapped[k])) for k in DIM_KEYS]
        return [clamp(0.0, 1.0, fnum(v.get(k, 0.0))) for k in DIM_KEYS]
    raise ValueError("dimension_vector must be list/object")


def vec_dict(v: list[float]) -> dict[str, float]:
    return {DIM_KEYS[i]: round(v[i], 6) for i in range(NDIM)}


def is_zero(v: list[float]) -> bool:
    return all(abs(x) <= 1e-9 for x in v)


def parse_candidate(raw: dict[str, Any]) -> tuple[dict[str, Any], list[str], int]:
    errs: list[str] = []
    iteration = 0
    for key in ("iteration_count", "iteration", "anneal_iteration"):
        if key in raw:
            try:
                iteration = max(0, int(raw[key]))
                break
            except (TypeError, ValueError):
                pass
    md = raw.get("metadata") if isinstance(raw.get("metadata"), dict) else {}
    if "iteration_count" in md and iteration == 0:
        try:
            iteration = max(0, int(md["iteration_count"]))
        except (TypeError, ValueError):
            pass

    def need(obj: dict[str, Any], key: str, path: str):
        if key not in obj:
            errs.append(path)
            return None
        return obj[key]

    atom_id = need(raw, "atom_id", "atom_id")
    src = need(raw, "source_atom_ids", "source_atom_ids")
    content = need(raw, "content", "content")
    md = need(raw, "metadata", "metadata") or {}
    terms = need(raw, "rosetta_terms", "rosetta_terms")
    dim = need(raw, "dimension_vector", "dimension_vector")
    pedges = need(raw, "proposed_edges", "proposed_edges") or {}

    for f in ("origin_hash", "axiom_alignment_score", "terminal_domain", "matched_intention", "drift_score"):
        if not isinstance(md, dict) or f not in md:
            errs.append(f"metadata.{f}")

    cids = pedges.get("canonical_node_ids") if isinstance(pedges, dict) else None
    if not isinstance(cids, list):
        errs.append("proposed_edges.canonical_node_ids")
        cids = []

    if not isinstance(atom_id, str) or not atom_id.strip():
        errs.append("atom_id:type")
    if not isinstance(src, list) or not all(isinstance(x, str) and x for x in src):
        errs.append("source_atom_ids:type")
    if not isinstance(content, str) or not content.strip():
        errs.append("content:type")
    if not isinstance(terms, list) or not all(isinstance(x, str) for x in terms):
        errs.append("rosetta_terms:type")

    try:
        dim_v = vec_list(dim)
    except Exception:
        errs.append("dimension_vector:type")
        dim_v = [0.0] * NDIM

    if errs:
        return {}, sorted(set(errs)), iteration

    c = {
        "atom_id": atom_id.strip(),
        "source_atom_ids": list(src),
        "content": content,
        "metadata": {
            "origin_hash": str(md["origin_hash"]),
            "axiom_alignment_score": clamp(0.0, 1.0, fnum(md["axiom_alignment_score"])),
            "terminal_domain": str(md["terminal_domain"]),
            "matched_intention": str(md["matched_intention"]),
            "drift_score": clamp(0.0, 1.0, fnum(md["drift_score"])),
        },
        "rosetta_terms": sorted({x.strip().lower() for x in terms if x.strip()}),
        "dimension_vector": dim_v,
        "proposed_edges": {"canonical_node_ids": [str(x).strip() for x in cids if str(x).strip()]},
    }
    return c, [], iteration


def gate_constraints(repo_root: Path) -> tuple[float, float]:
    text = (repo_root / GATE_V1_REL).read_text(encoding="utf-8")
    drift = 0.10
    align = 0.85
    m = re.search(r"drift_score:\s*<\s*([0-9.]+)\s*required", text, re.I)
    if m:
        drift = fnum(m.group(1), 0.10)
    m = re.search(r"Similarity\([^)]*\)\s*>\s*([0-9.]+)", text, re.I)
    if m:
        align = fnum(m.group(1), 0.85)
    return drift, align


def rosetta_lexicon(repo_root: Path) -> list[str]:
    text = (repo_root / ROSETTA_REL).read_text(encoding="utf-8")
    terms: set[str] = set()
    for m in re.finditer(r"^\|\s*\d+\s*\|\s*([^|]+?)\s*\|", text, re.M):
        for p in re.split(r"[/>,;()]+", m.group(1)):
            t = re.sub(r"\s+", " ", p).strip().lower()
            if len(t) >= 3:
                terms.add(t)
    return sorted(terms)


def sn_map(repo_root: Path) -> dict[str, dict[str, Any]]:
    root = repo_root / SN_DIR_REL
    if not root.is_dir():
        raise FileNotFoundError(root)
    out = {}
    for p in sorted(root.glob("*.md")):
        m = re.search(r"CANON-\d{5}", p.name)
        if not m:
            continue
        out[m.group(0)] = {"path": p, "text": p.read_text(encoding="utf-8")}
    return out


def terms_in_text(text: str, lex: list[str]) -> list[str]:
    low = text.lower()
    return sorted({t for t in lex if t in low})


def infer_dim(text: str) -> dict[str, float]:
    low = text.lower()
    buckets = {
        "cognitive": ("reason", "logic", "inference", "analysis", "cognition", "abstraction", "model"),
        "semiotic": ("sign", "symbol", "meaning", "reference", "interpret", "semantic", "signal"),
        "psychological": ("emotion", "motivation", "perception", "awareness", "attention", "memory", "affect"),
        "phenomenological": ("experience", "consciousness", "qualia", "intentionality", "presence"),
        "volitional": ("will", "choice", "decision", "agency", "autonomy", "intention", "commitment"),
        "embodied": ("body", "gesture", "sensation", "movement", "proprioception", "somatic"),
        "behavioral": ("action", "habit", "pattern", "response", "conduct", "practice", "routine"),
        "characterological": ("virtue", "integrity", "character", "identity", "disposition", "temperament"),
        "aesthetic": ("beauty", "elegance", "harmony", "form", "design", "style", "composition"),
        "linguistic": ("language", "grammar", "syntax", "discourse", "narrative", "rhetoric"),
        "social": ("agent", "team", "coordination", "collective", "community", "collaborate"),
        "spiritual": ("transcendence", "sacred", "wisdom", "contemplation", "unity", "purpose", "soul"),
        "temporal": ("time", "duration", "rhythm", "cycle", "epoch", "sequence", "history"),
        "environmental": ("ecology", "context", "habitat", "landscape", "system", "network", "infrastructure"),
    }
    out = {}
    for k, words in buckets.items():
        score = sum(len(re.findall(rf"\b{re.escape(w)}\b", low)) for w in words)
        out[k] = round(clamp(0.0, 1.0, score / 8.0), 6)
    return out


def build_index(repo_root: Path, index_path: Path, lex: list[str]) -> dict[str, Any]:
    smap = sn_map(repo_root)
    nodes = []
    for nid in sorted(smap):
        text = smap[nid]["text"]
        p = smap[nid]["path"]
        title = (re.search(r"^#\s+(.+)$", text, re.M) or re.match(r"^$", "")).group(1) if re.search(r"^#\s+(.+)$", text, re.M) else nid
        fname = p.name.lower()
        tier = "unknown"
        for t in ("cosmos", "core", "lattice", "chain", "planetary", "lunar", "satellite"):
            if t in fname:
                tier = t
                break
        nodes.append(
            {
                "node_id": nid,
                "file": p.relative_to(repo_root).as_posix(),
                "title": title.strip(),
                "tier": tier,
                "rosetta_terms": terms_in_text(text, lex),
                "dimension_vector": infer_dim(text),
                "adjacency": sorted({x for x in re.findall(r"CANON-\d{5}", text) if x != nid}),
                "retired": bool(re.search(r"\b(retired|deprecated|tombstone)\b", text, re.I)),
            }
        )
    payload = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": now_iso(),
        "node_count": len(nodes),
        "nodes": nodes,
    }
    write_json_atomic(index_path, payload)
    return payload


def hydrate_index(repo_root: Path, idx: dict[str, Any], lex: list[str]) -> dict[str, Any]:
    smap = sn_map(repo_root)
    out = []
    for n in idx.get("nodes", []):
        if not isinstance(n, dict):
            continue
        nid = str(n.get("node_id", "")).strip()
        if not nid:
            continue
        text = smap[nid]["text"] if nid in smap else ""
        terms = n.get("rosetta_terms", []) if isinstance(n.get("rosetta_terms"), list) else []
        terms = [str(x).strip().lower() for x in terms if str(x).strip()]
        if not terms and text:
            terms = terms_in_text(text, lex)
        try:
            v = vec_list(n.get("dimension_vector", {}))
        except Exception:
            v = [0.0] * NDIM
        if is_zero(v) and text:
            v = vec_list(infer_dim(text))
        adj = n.get("adjacency", []) if isinstance(n.get("adjacency"), list) else []
        adj = [str(x).strip() for x in adj if str(x).strip()]
        if not adj and text:
            adj = sorted({x for x in re.findall(r"CANON-\d{5}", text) if x != nid})
        out.append(
            {
                **n,
                "node_id": nid,
                "rosetta_terms": sorted(set(terms)),
                "dimension_vector": vec_dict(v),
                "adjacency": sorted(set(adj)),
                "retired": bool(n.get("retired", False)),
            }
        )
    return {
        "schema_version": str(idx.get("schema_version", SCHEMA_VERSION)),
        "generated_at": str(idx.get("generated_at", "")),
        "node_count": len(out),
        "nodes": out,
    }


def is_stale(idx: dict[str, Any]) -> bool:
    try:
        g = str(idx.get("generated_at", "")).strip()
        if not g:
            return True
        age = dt.datetime.now(dt.timezone.utc) - parse_iso(g)
        return age.total_seconds() > INDEX_STALE_SEC
    except Exception:
        return True


def cos(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    return 0.0 if na == 0.0 or nb == 0.0 else dot / (na * nb)


def wj(a: dict[str, float], b: dict[str, float]) -> float:
    ks = set(a) | set(b)
    if not ks:
        return 0.0
    inter = sum(min(a.get(k, 0.0), b.get(k, 0.0)) for k in ks)
    uni = sum(max(a.get(k, 0.0), b.get(k, 0.0)) for k in ks)
    return 0.0 if uni <= 0 else inter / uni


def top_neighbors(candidate: dict[str, Any], nodes: list[dict[str, Any]], k: int = TOP_K) -> list[dict[str, Any]]:
    live = [n for n in nodes if not bool(n.get("retired", False))]
    byid = {str(n.get("node_id")): n for n in live}
    got, seen = [], set()
    for nid in candidate["proposed_edges"]["canonical_node_ids"]:
        if nid in byid and nid not in seen:
            got.append(byid[nid])
            seen.add(nid)
            if len(got) >= k:
                return got
    cv = candidate["dimension_vector"]
    scored = []
    for n in live:
        nid = str(n.get("node_id"))
        if nid in seen:
            continue
        try:
            nv = vec_list(n.get("dimension_vector", {}))
        except Exception:
            nv = [0.0] * NDIM
        scored.append((cos(cv, nv), n))
    scored.sort(key=lambda x: x[0], reverse=True)
    for _, n in scored:
        got.append(n)
        if len(got) >= k:
            break
    return got


def score(candidate: dict[str, Any], idx: dict[str, Any]) -> dict[str, Any]:
    nodes = idx.get("nodes", [])
    neigh = top_neighbors(candidate, nodes, TOP_K)

    cterms = {t: 1.0 for t in candidate["rosetta_terms"]}
    nterms: dict[str, float] = {}
    for i, n in enumerate(neigh):
        w = 1.0 / (i + 1)
        for t in n.get("rosetta_terms", []):
            ts = str(t).strip().lower()
            if ts:
                nterms[ts] = nterms.get(ts, 0.0) + w
    s_ro = wj(cterms, nterms)

    if neigh:
        ws = [1.0 / (i + 1) for i in range(len(neigh))]
        cen = [0.0] * NDIM
        den = sum(ws)
        for i, n in enumerate(neigh):
            try:
                nv = vec_list(n.get("dimension_vector", {}))
            except Exception:
                nv = [0.0] * NDIM
            for j in range(NDIM):
                cen[j] += nv[j] * ws[i]
        cen = [x / den for x in cen] if den > 0 else cen
        cos_align = clamp(0.0, 1.0, (cos(candidate["dimension_vector"], cen) + 1.0) / 2.0)
        # Hypervolume scoring on core integrative axes
        eps = 1e-6
        cv = vec_list(candidate.get("dimension_vector_raw", candidate["dimension_vector"]))
        core_vals = [max(eps, cv[DIM_KEYS.index(ax)]) for ax in CORE_AXES]
        hypervolume = math.prod(core_vals) ** (1.0 / len(core_vals))
        s_dim = clamp(0.0, 1.0, 0.7 * cos_align + 0.3 * hypervolume)
    else:
        s_dim = 0.0

    live_ids = {str(n.get("node_id")) for n in nodes if not bool(n.get("retired", False))}
    links = sum(1 for nid in candidate["proposed_edges"]["canonical_node_ids"] if nid in live_ids)
    s_back = clamp(0.0, 1.0, links / 4.0)

    coh = clamp(0.0, 1.0, 0.4 * s_ro + 0.4 * s_dim + 0.2 * s_back)
    rec_edges = [str(n.get("node_id")) for n in neigh if str(n.get("node_id")) not in candidate["proposed_edges"]["canonical_node_ids"]][:5]
    return {
        "rosetta_overlap_score": round(s_ro, 6),
        "dimension_alignment_score": round(s_dim, 6),
        "backlink_score": round(s_back, 6),
        "coherence_score": round(coh, 6),
        "links_to_live_nodes": links,
        "top_neighbor_ids": [str(n.get("node_id")) for n in neigh],
        "neighbor_term_weights": nterms,
        "recommended_edges": rec_edges,
    }


def health_default() -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at": now_iso(),
        "global_coherence": 0.70,
        "global_drift": 0.0,
        "fragmentation_index": 0.0,
        "sample_count": 0,
        "last_candidate_id": None,
        "last_decision": None,
    }


def health_load(path: Path) -> tuple[dict[str, Any], list[str]]:
    if not path.exists():
        return health_default(), ["MISSING_LATTICE_HEALTH"]
    try:
        d = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(d, dict):
            raise ValueError("not object")
    except Exception:
        return health_default(), ["INVALID_LATTICE_HEALTH", "MISSING_LATTICE_HEALTH"]
    base = health_default()
    base.update(d)
    base["global_coherence"] = clamp(0.0, 1.0, fnum(base.get("global_coherence"), 0.70))
    base["global_drift"] = clamp(0.0, 1.0, fnum(base.get("global_drift"), 0.0))
    base["fragmentation_index"] = clamp(0.0, 1.0, fnum(base.get("fragmentation_index"), 0.0))
    base["sample_count"] = max(0, int(fnum(base.get("sample_count"), 0)))
    return base, []


def health_update(prev: dict[str, Any], c: dict[str, Any], s: dict[str, Any], decision: str) -> dict[str, Any]:
    a = 0.20
    out = dict(prev)
    out["global_coherence"] = round(clamp(0.0, 1.0, (1 - a) * fnum(prev.get("global_coherence"), 0.70) + a * fnum(s["coherence_score"])), 6)
    out["global_drift"] = round(clamp(0.0, 1.0, (1 - a) * fnum(prev.get("global_drift"), 0.0) + a * fnum(c["metadata"]["drift_score"])), 6)
    frag = clamp(0.0, 1.0, 1.0 - fnum(s["backlink_score"]))
    out["fragmentation_index"] = round(clamp(0.0, 1.0, (1 - a) * fnum(prev.get("fragmentation_index"), 0.0) + a * frag), 6)
    out["sample_count"] = int(fnum(prev.get("sample_count"), 0)) + 1
    out["last_candidate_id"] = c["atom_id"]
    out["last_decision"] = decision
    out["generated_at"] = now_iso()
    out["schema_version"] = SCHEMA_VERSION
    return out


def threshold(global_coherence: float) -> tuple[float, bool]:
    raw = 0.70 + 0.25 * (global_coherence - 0.70)
    req = clamp(0.60, 0.78, raw)
    return round(req, 6), abs(req - raw) > 1e-9


def repair_prompt(c: dict[str, Any], s: dict[str, Any], req: float, it: int, max_it: int) -> str:
    cterms = set(c["rosetta_terms"])
    wterms = sorted(s["neighbor_term_weights"].items(), key=lambda x: x[1], reverse=True)
    miss = [t for t, _ in wterms if t not in cterms][:6]
    extra = [t for t in cterms if t not in dict(wterms)][:6]
    invalid = [e for e in c["proposed_edges"]["canonical_node_ids"] if e not in s["top_neighbor_ids"]][:6]
    lines = [
        f"Anneal adjustment request for atom {c['atom_id']}.",
        f"Current coherence={s['coherence_score']:.4f}; required>={req:.4f}.",
        f"Iteration {it + 1} of {max_it}.",
        "",
    ]
    if miss:
        lines += ["Add or strengthen these Rosetta terms:", ", ".join(miss), ""]
    else:
        lines += ["Improve Rosetta overlap with nearest lattice neighbors.", ""]
    if extra:
        lines += ["De-emphasize low-signal terms:", ", ".join(extra), ""]
    if invalid:
        lines += ["Review low-relevance edges:", ", ".join(invalid), ""]
    if s["recommended_edges"]:
        lines += ["Suggested canonical edges:", ", ".join(s["recommended_edges"][:4]), ""]
    lines.append("Resubmit updated candidate JSON with incremented iteration_count.")
    return "\n".join(lines)


def output(decision: str, reasons: list[str], it: int, coh: float, req: float, prompt: str | None) -> dict[str, Any]:
    return {
        "decision": decision,
        "justification": {
            "reason_codes": sorted(set(reasons)),
            "iteration_count": it,
            "coherence_score": round(coh, 6),
            "required_threshold": round(req, 6),
        },
        "repair_prompt": prompt,
    }


def run_once(
    repo_root: Path,
    candidate_json: Path,
    lattice_index: Path,
    max_iterations: int,
    mode: str,
    write_state: bool = True,
) -> tuple[dict[str, Any], int]:
    reasons, trace = [], ["INGESTED"]

    try:
        raw = read_json(candidate_json)
    except FileNotFoundError:
        return output("REJECT", ["CANDIDATE_MISSING", "ERROR_FATAL"], 0, 0.0, 0.70, None), 2
    except Exception:
        return output("REJECT", ["CANDIDATE_INVALID", "ERROR_FATAL"], 0, 0.0, 0.70, None), 2

    cand, errs, it = parse_candidate(raw if isinstance(raw, dict) else {})
    it = min(max(it, 0), max_iterations)
    if errs:
        return output("REJECT", ["V1_FIELD_MISSING", "CANDIDATE_INVALID"], it, 0.0, 0.70, None), 2

    if mode == "reanneal":
        reasons.append("REANNEAL_MODE")

    try:
        drift_limit, align_min = gate_constraints(repo_root)
        lex = rosetta_lexicon(repo_root)
    except FileNotFoundError as e:
        code = "MISSING_GATE_V1" if str(repo_root / GATE_V1_REL) in str(e) else "MISSING_ROSETTA"
        return output("REJECT", [code, "ERROR_FATAL"], it, 0.0, 0.70, None), 2
    except Exception:
        return output("REJECT", ["REFERENCE_READ_FAILED", "ERROR_FATAL"], it, 0.0, 0.70, None), 2

    held = []
    if write_state:
        try:
            held = acquire_locks(repo_root / LOCK_DIR_REL)
        except Exception:
            return output("REJECT", ["LOCK_TIMEOUT", "ERROR_FATAL"], it, 0.0, 0.70, None), 2

    try:
        health, hr = health_load(repo_root / HEALTH_REL)
        reasons += hr
        req, clamped = threshold(fnum(health.get("global_coherence"), 0.70))
        if clamped:
            reasons.append("THRESHOLD_CLAMPED")

        if not lattice_index.exists():
            reasons += ["INDEX_MISSING", "ERROR_FATAL"]
            trace.append("ERROR_FATAL")
            if write_state:
                append_jsonl(
                    repo_root / REBUILD_QUEUE_REL,
                    {
                        "schema_version": SCHEMA_VERSION,
                        "generated_at": now_iso(),
                        "reason": "INDEX_MISSING",
                        "candidate_atom_id": cand["atom_id"],
                        "mode": mode,
                        "index_path": lattice_index.as_posix(),
                    },
                )
            out = output("REJECT", reasons, it, 0.0, req, None)
            if write_state:
                append_jsonl(
                    repo_root / ANNEAL_LOG_REL,
                    {
                        "schema_version": SCHEMA_VERSION,
                        "generated_at": now_iso(),
                        "state_trace": trace,
                        "decision": out["decision"],
                        "candidate_atom_id": cand["atom_id"],
                        "reason_codes": out["justification"]["reason_codes"],
                        "mode": mode,
                    },
                )
            return out, 2

        try:
            idx = read_json(lattice_index)
            if not isinstance(idx.get("nodes"), list):
                raise ValueError("bad index")
        except Exception:
            return output("REJECT", ["INDEX_INVALID", "ERROR_FATAL"], it, 0.0, req, None), 2

        if is_stale(idx):
            reasons.append("INDEX_STALE")
            try:
                idx = build_index(repo_root, lattice_index, lex)
                reasons.append("INDEX_STALE_REBUILT")
            except Exception:
                reasons += ["INDEX_REBUILD_FAILED", "ERROR_FATAL"]
                trace.append("ERROR_FATAL")
                if write_state:
                    append_jsonl(
                        repo_root / REBUILD_QUEUE_REL,
                        {
                            "schema_version": SCHEMA_VERSION,
                            "generated_at": now_iso(),
                            "reason": "INDEX_REBUILD_FAILED",
                            "candidate_atom_id": cand["atom_id"],
                            "mode": mode,
                            "index_path": lattice_index.as_posix(),
                        },
                    )
                    append_jsonl(
                        repo_root / ANNEAL_LOG_REL,
                        {
                            "schema_version": SCHEMA_VERSION,
                            "generated_at": now_iso(),
                            "state_trace": trace,
                            "decision": "REJECT",
                            "candidate_atom_id": cand["atom_id"],
                            "reason_codes": sorted(set(reasons)),
                            "mode": mode,
                        },
                    )
                return output("REJECT", reasons, it, 0.0, req, None), 2

        idx = hydrate_index(repo_root, idx, lex)
        trace.append("INDEX_READY")

        hard = False
        if cand["metadata"]["drift_score"] > drift_limit:
            hard = True
            reasons.append("HARD_REJECT_DRIFT")
        if cand["metadata"]["axiom_alignment_score"] < align_min:
            hard = True
            reasons.append("HARD_REJECT_ALIGNMENT")

        s = score(cand, idx)
        coh = fnum(s["coherence_score"])
        trace.append("SCORED")

        prompt = None
        if hard:
            decision = "REJECT"
            trace.append("REJECTED")
        elif coh >= req:
            decision = "PROMOTE"
            trace.append("ACCEPTED")
        elif it < max_iterations:
            decision = "ADJUST"
            reasons.append("COHERENCE_BELOW_THRESHOLD")
            trace.append("ADJUST_REQUESTED")
            prompt = repair_prompt(cand, s, req, it, max_iterations)
        else:
            decision = "REJECT"
            reasons += ["COHERENCE_BELOW_THRESHOLD", "MAX_ITERATIONS_EXCEEDED"]
            trace.append("REJECTED")

        out = output(decision, reasons, it, coh, req, prompt)

        if write_state:
            write_json_atomic(repo_root / HEALTH_REL, health_update(health, cand, s, decision))
            if decision == "ADJUST":
                append_jsonl(
                    repo_root / REPAIR_QUEUE_REL,
                    {
                        "schema_version": SCHEMA_VERSION,
                        "generated_at": now_iso(),
                        "candidate_atom_id": cand["atom_id"],
                        "iteration_count": it,
                        "next_iteration": min(it + 1, max_iterations),
                        "coherence_score": coh,
                        "required_threshold": req,
                        "repair_prompt": prompt,
                        "mode": mode,
                    },
                )
            append_jsonl(
                repo_root / ANNEAL_LOG_REL,
                {
                    "schema_version": SCHEMA_VERSION,
                    "generated_at": now_iso(),
                    "mode": mode,
                    "state_trace": trace,
                    "decision": decision,
                    "candidate_atom_id": cand["atom_id"],
                    "source_atom_ids": cand["source_atom_ids"],
                    "reason_codes": out["justification"]["reason_codes"],
                    "iteration_count": it,
                    "required_threshold": req,
                    "scores": {
                        "rosetta_overlap_score": s["rosetta_overlap_score"],
                        "dimension_alignment_score": s["dimension_alignment_score"],
                        "backlink_score": s["backlink_score"],
                        "coherence_score": s["coherence_score"],
                        "links_to_live_nodes": s["links_to_live_nodes"],
                        "top_neighbor_ids": s["top_neighbor_ids"],
                    },
                    "index_generated_at": idx.get("generated_at"),
                    "index_node_count": idx.get("node_count"),
                },
            )

        return out, 0
    finally:
        if write_state:
            release_locks(held)


def mk_fixture_repo(root: Path) -> tuple[Path, Path, Path]:
    (root / SN_DIR_REL).mkdir(parents=True, exist_ok=True)
    (root / "engine/02-ENGINE").mkdir(parents=True, exist_ok=True)
    (root / STATE_REL).mkdir(parents=True, exist_ok=True)

    (root / GATE_V1_REL).write_text("# gate\n- drift_score: <0.1 required\nSimilarity(atom, term) > 0.85\n", encoding="utf-8")
    (root / ROSETTA_REL).write_text(
        "\n".join(
            [
                "# rosetta",
                "| # | Internal Term | Status | Community Equivalent | Action |",
                "|---|---|---|---|---|",
                "| 1 | triumvirate | UNIQUE | x | x |",
                "| 2 | coherence | ALIGNED | x | x |",
                "| 3 | lattice | ALIGNED | x | x |",
                "| 4 | ontology | ALIGNED | x | x |",
                "| 5 | protocol | ALIGNED | x | x |",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    (root / f"{SN_DIR_REL}/CANON-10001-ALPHA-lattice.md").write_text(
        "# Alpha\nTriumvirate coherence lattice protocol.\nSee CANON-10002.\n", encoding="utf-8"
    )
    (root / f"{SN_DIR_REL}/CANON-10002-BETA-lattice.md").write_text(
        "# Beta\nOntology lattice coherence and execution protocol.\nSee CANON-10001.\n", encoding="utf-8"
    )
    (root / f"{SN_DIR_REL}/CANON-10003-GAMMA-lattice.md").write_text("# Gamma\nIndependent archive note.\n", encoding="utf-8")

    idx = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": now_iso(),
        "node_count": 3,
        "nodes": [
            {
                "node_id": "CANON-10001",
                "file": f"{SN_DIR_REL}/CANON-10001-ALPHA-lattice.md",
                "title": "Alpha",
                "tier": "lattice",
                "rosetta_terms": ["triumvirate", "coherence", "lattice", "protocol"],
                "dimension_vector": {
                    "cognitive": 0.8, "semiotic": 0.7, "psychological": 0.3,
                    "phenomenological": 0.2, "volitional": 0.6, "embodied": 0.1,
                    "behavioral": 0.9, "characterological": 0.1, "aesthetic": 0.2,
                    "linguistic": 0.4, "social": 0.7, "spiritual": 0.1,
                    "temporal": 0.3, "environmental": 0.5,
                },
                "adjacency": ["CANON-10002"],
                "retired": False,
            },
            {
                "node_id": "CANON-10002",
                "file": f"{SN_DIR_REL}/CANON-10002-BETA-lattice.md",
                "title": "Beta",
                "tier": "lattice",
                "rosetta_terms": ["ontology", "coherence", "lattice", "protocol"],
                "dimension_vector": {
                    "cognitive": 0.9, "semiotic": 0.75, "psychological": 0.25,
                    "phenomenological": 0.15, "volitional": 0.7, "embodied": 0.1,
                    "behavioral": 0.85, "characterological": 0.15, "aesthetic": 0.3,
                    "linguistic": 0.35, "social": 0.6, "spiritual": 0.1,
                    "temporal": 0.25, "environmental": 0.55,
                },
                "adjacency": ["CANON-10001"],
                "retired": False,
            },
            {
                "node_id": "CANON-10003",
                "file": f"{SN_DIR_REL}/CANON-10003-GAMMA-lattice.md",
                "title": "Gamma",
                "tier": "lattice",
                "rosetta_terms": ["archive"],
                "dimension_vector": {
                    "cognitive": 0.1, "semiotic": 0.1, "psychological": 0.1,
                    "phenomenological": 0.1, "volitional": 0.1, "embodied": 0.1,
                    "behavioral": 0.1, "characterological": 0.1, "aesthetic": 0.1,
                    "linguistic": 0.1, "social": 0.1, "spiritual": 0.1,
                    "temporal": 0.1, "environmental": 0.1,
                },
                "adjacency": [],
                "retired": False,
            },
        ],
    }
    idx_path = root / INDEX_REL
    write_json_atomic(idx_path, idx)
    write_json_atomic(root / HEALTH_REL, health_default())
    return idx_path, root / HEALTH_REL, root / "candidate.json"


def cand_base() -> dict[str, Any]:
    return {
        "atom_id": "ATOM-TEST-001",
        "source_atom_ids": ["SRC-1"],
        "content": "Triumvirate coherence lattice protocol for ontology execution.",
        "metadata": {
            "origin_hash": "abc123",
            "axiom_alignment_score": 0.92,
            "terminal_domain": "STR",
            "matched_intention": "INT-1000",
            "drift_score": 0.04,
        },
        "rosetta_terms": ["triumvirate", "coherence", "lattice", "protocol", "ontology"],
        "dimension_vector": {
            "cognitive": 0.86, "semiotic": 0.72, "psychological": 0.30,
            "phenomenological": 0.20, "volitional": 0.64, "embodied": 0.10,
            "behavioral": 0.84, "characterological": 0.15, "aesthetic": 0.25,
            "linguistic": 0.40, "social": 0.71, "spiritual": 0.10,
            "temporal": 0.30, "environmental": 0.50,
        },
        "proposed_edges": {"canonical_node_ids": ["CANON-10001", "CANON-10002"]},
    }


def write_candidate(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")


def self_test(_: Path) -> int:
    cases = []

    def rec(cid: str, name: str, ok: bool, detail: str = ""):
        cases.append({"id": cid, "name": name, "status": "PASS" if ok else "FAIL", "details": detail})

    with tempfile.TemporaryDirectory(prefix="lattice-annealer-selftest-") as td:
        root = Path(td)
        idx_path, health_path, cpath = mk_fixture_repo(root)

        c1 = cand_base()
        write_candidate(cpath, c1)
        o1, rc1 = run_once(root, cpath, idx_path, 3, "gate", write_state=True)
        rec("LAN-T01", "promote_on_first_pass", o1["decision"] == "PROMOTE" and o1["justification"]["iteration_count"] == 0 and rc1 == 0, json.dumps(o1, sort_keys=True))

        c2w = cand_base()
        c2w["atom_id"] = "ATOM-TEST-002"
        c2w["rosetta_terms"] = ["agile", "scrum"]
        c2w["dimension_vector"] = [0.1] * NDIM
        c2w["proposed_edges"] = {"canonical_node_ids": []}
        c2w["iteration_count"] = 0
        write_candidate(cpath, c2w)
        o2a, _ = run_once(root, cpath, idx_path, 3, "gate", write_state=True)
        c2s = cand_base()
        c2s["atom_id"] = "ATOM-TEST-002"
        c2s["iteration_count"] = 1
        write_candidate(cpath, c2s)
        o2b, _ = run_once(root, cpath, idx_path, 3, "gate", write_state=True)
        rec("LAN-T02", "adjust_then_promote", o2a["decision"] == "ADJUST" and o2b["decision"] == "PROMOTE" and o2b["justification"]["iteration_count"] == 1, json.dumps({"first": o2a, "second": o2b}, sort_keys=True))

        c3 = cand_base()
        c3["atom_id"] = "ATOM-TEST-003"
        c3["rosetta_terms"] = ["noise"]
        c3["dimension_vector"] = [0.0] * NDIM
        c3["proposed_edges"] = {"canonical_node_ids": []}
        c3["iteration_count"] = 3
        write_candidate(cpath, c3)
        o3, _ = run_once(root, cpath, idx_path, 3, "gate", write_state=True)
        rec("LAN-T03", "reject_after_3_iterations", o3["decision"] == "REJECT" and "MAX_ITERATIONS_EXCEEDED" in set(o3["justification"]["reason_codes"]), json.dumps(o3, sort_keys=True))

        c4 = cand_base()
        c4["atom_id"] = "ATOM-TEST-004"
        c4["metadata"]["drift_score"] = 0.12
        write_candidate(cpath, c4)
        o4, _ = run_once(root, cpath, idx_path, 3, "gate", write_state=True)
        rec("LAN-T04", "hard_reject_on_drift", o4["decision"] == "REJECT" and "HARD_REJECT_DRIFT" in set(o4["justification"]["reason_codes"]) and o4["repair_prompt"] is None, json.dumps(o4, sort_keys=True))

        t50, _ = threshold(0.50)
        t00, _ = threshold(0.00)
        t100, _ = threshold(1.00)
        rec(
            "LAN-T05",
            "dynamic_threshold_relaxes_with_low_global_coherence",
            t50 == 0.65 and t00 == 0.60 and t100 == 0.775,
            json.dumps(
                {
                    "global_coherence_0_50": t50,
                    "global_coherence_0_00": t00,
                    "global_coherence_1_00": t100,
                },
                sort_keys=True,
            ),
        )

    passed = sum(1 for c in cases if c["status"] == "PASS")
    failed = len(cases) - passed
    print(
        json.dumps(
            {
                "self_test": "PASS" if failed == 0 else "FAIL",
                "schema_version": SCHEMA_VERSION,
                "generated_at": now_iso(),
                "passed": passed,
                "failed": failed,
                "cases": cases,
            },
            ensure_ascii=True,
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if failed == 0 else 1


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Lattice annealer gate for candidate canon promotions.")
    p.add_argument("--repo-root", required=True)
    p.add_argument("--candidate-json")
    p.add_argument("--lattice-index", default=INDEX_REL)
    p.add_argument("--max-iterations", type=int, default=3)
    p.add_argument("--mode", choices=("gate", "reanneal"), default="gate")
    p.add_argument("--self-test", action="store_true")
    return p.parse_args()


def main() -> int:
    a = parse_args()
    repo_root = Path(a.repo_root).resolve()
    if not repo_root.exists():
        print(f"ERROR: repo root does not exist: {repo_root}")
        return 2

    if a.self_test:
        return self_test(repo_root)

    if not a.candidate_json:
        print("ERROR: --candidate-json is required unless --self-test is set")
        return 2

    max_it = max(1, min(3, int(a.max_iterations)))
    cpath = resolve(repo_root, a.candidate_json)
    ipath = resolve(repo_root, a.lattice_index)

    try:
        out, code = run_once(repo_root, cpath, ipath, max_it, a.mode, write_state=True)
    except Exception as e:
        out, code = output("REJECT", ["UNHANDLED_EXCEPTION", "ERROR_FATAL"], 0, 0.0, 0.70, None), 2
        out["justification"]["error"] = str(e)

    print(json.dumps(out, ensure_ascii=True, indent=2, sort_keys=True))
    if "ERROR_FATAL" in set(out["justification"]["reason_codes"]):
        return 2
    return code


if __name__ == "__main__":
    raise SystemExit(main())
