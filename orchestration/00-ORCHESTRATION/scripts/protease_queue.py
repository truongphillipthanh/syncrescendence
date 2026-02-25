#!/usr/bin/env python3
"""protease_queue.py — Protease Protocol Phase 1: Queue Builder.

Reads atom clustering output and intention compass, generates a prioritized
"chewing queue" of atoms for Sovereign review.

Input:
  - DYN-ATOM_SCORE_AUDIT.jsonl   (per-atom 6D scores + band)
  - DYN-ATOM_INDEX.jsonl          (atom metadata + integration_status)
  - DYN-ATOM_CLUSTER_MANIFEST.jsonl (cluster assignments + previews)
  - ARCH-INTENTION_COMPASS.md     (active intentions)

Output:
  - DYN-PROTEASE_QUEUE.jsonl  (machine-readable queue)
  - DYN-PROTEASE_QUEUE.md     (human-readable, grouped by intention)
"""

import argparse
import json
import os
import re
import sys
import tempfile
from collections import defaultdict
from pathlib import Path


# ---------------------------------------------------------------------------
# Path constants (relative to repo root)
# ---------------------------------------------------------------------------
SCORE_AUDIT_REL = "sources/04-SOURCES/_meta/DYN-ATOM_SCORE_AUDIT.jsonl"
ATOM_INDEX_REL = "sources/04-SOURCES/_meta/DYN-ATOM_INDEX.jsonl"
CLUSTER_MANIFEST_REL = "sources/04-SOURCES/_meta/DYN-ATOM_CLUSTER_MANIFEST.jsonl"
INTENTION_COMPASS_REL = "orchestration/00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md"
OUTPUT_DIR_REL = "orchestration/00-ORCHESTRATION/state"
QUEUE_JSONL = "DYN-PROTEASE_QUEUE.jsonl"
QUEUE_MD = "DYN-PROTEASE_QUEUE.md"


# ---------------------------------------------------------------------------
# JSONL helpers
# ---------------------------------------------------------------------------
def load_jsonl(path: Path) -> list[dict]:
    """Load a JSONL file, skipping blank/malformed lines."""
    records = []
    with open(path, "r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as exc:
                print(f"  WARN: {path.name}:{lineno} — skipped malformed JSON: {exc}", file=sys.stderr)
    return records


def atomic_write_jsonl(path: Path, records: list[dict]) -> None:
    """Write JSONL via temp-file-validate-rename pattern."""
    fd, tmp = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            for rec in records:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        # Validate: re-read and parse every line
        with open(tmp, "r", encoding="utf-8") as f:
            for lineno, line in enumerate(f, 1):
                json.loads(line.strip())
        os.replace(tmp, path)
    except Exception:
        os.unlink(tmp)
        raise


# ---------------------------------------------------------------------------
# Intention parsing
# ---------------------------------------------------------------------------
def parse_intentions(md_path: Path) -> list[dict]:
    """Extract active intentions from ARCH-INTENTION_COMPASS.md.

    Returns list of {id, title, keywords} where keywords are lowercase tokens
    extracted from the intention text column.
    """
    text = md_path.read_text(encoding="utf-8")
    intentions = []

    # Match markdown table rows with INT-XXXX IDs
    # Patterns: | INT-XXXX | ... | "text" | status | ... |
    # Also handles INT-PXXX pattern IDs
    row_re = re.compile(
        r"^\|\s*(INT-[A-Z]?\d+)\s*\|[^|]*\|"   # ID column + skip oracle/council column
        r"\s*\"?([^|\"]+?)\"?\s*\|"               # text column (with optional quotes)
        r"\s*(\w+)\s*\|",                          # status column
        re.MULTILINE,
    )

    # Stop words for keyword extraction
    stop_words = {
        "the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
        "have", "has", "had", "do", "does", "did", "will", "would", "could",
        "should", "may", "might", "shall", "can", "need", "must", "ought",
        "to", "of", "in", "for", "on", "with", "at", "by", "from", "as",
        "into", "through", "during", "before", "after", "above", "below",
        "between", "under", "again", "further", "then", "once", "here",
        "there", "when", "where", "why", "how", "all", "both", "each",
        "few", "more", "most", "other", "some", "such", "no", "nor", "not",
        "only", "own", "same", "so", "than", "too", "very", "just", "but",
        "and", "or", "if", "while", "that", "this", "these", "those", "it",
        "its", "they", "them", "their", "we", "our", "you", "your", "what",
        "which", "who", "whom", "up", "out", "about", "over", "every",
    }

    for m in row_re.finditer(text):
        int_id = m.group(1).strip()
        title = m.group(2).strip()
        status = m.group(3).strip().lower().strip("*")

        # Only active intentions
        if status not in ("active",):
            continue

        # Extract keywords: alphanumeric tokens >= 3 chars, not stop words
        raw_tokens = re.findall(r"[a-zA-Z][a-zA-Z0-9_-]{2,}", title.lower())
        keywords = [t for t in raw_tokens if t not in stop_words]

        intentions.append({
            "id": int_id,
            "title": title,
            "keywords": keywords,
        })

    return intentions


# ---------------------------------------------------------------------------
# Intention matching
# ---------------------------------------------------------------------------
def match_intentions(content: str, intentions: list[dict]) -> list[tuple[str, float]]:
    """Match atom content against intentions via keyword overlap.

    Returns list of (INT-ID, score) for intentions with score > 0, sorted desc.
    """
    content_lower = content.lower()
    content_tokens = set(re.findall(r"[a-zA-Z][a-zA-Z0-9_-]{2,}", content_lower))

    matches = []
    for intent in intentions:
        kws = intent["keywords"]
        if not kws:
            continue
        # Hybrid: exact substring match (weight 2) + token overlap (weight 1)
        score = 0.0
        for kw in kws:
            if kw in content_tokens:
                score += 1.0
            elif kw in content_lower:
                score += 0.5
        # Normalize by keyword count to avoid bias toward verbose intentions
        normalized = score / len(kws) if kws else 0.0
        if normalized > 0.0:
            matches.append((intent["id"], normalized))

    matches.sort(key=lambda x: x[1], reverse=True)
    return matches


# ---------------------------------------------------------------------------
# Cluster context fallback
# ---------------------------------------------------------------------------
def build_cluster_context(cluster_manifest: list[dict]) -> dict[int, str]:
    """Map cluster_id → representative_preview for fallback matching."""
    ctx = {}
    for rec in cluster_manifest:
        cid = rec.get("cluster_id")
        preview = rec.get("representative_preview", "")
        if cid is not None:
            ctx[cid] = preview
    return ctx


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------
def build_queue(repo_root: Path, max_atoms: int) -> dict:
    """Build the protease queue. Returns stats dict."""

    score_audit_path = repo_root / SCORE_AUDIT_REL
    atom_index_path = repo_root / ATOM_INDEX_REL
    cluster_manifest_path = repo_root / CLUSTER_MANIFEST_REL
    intention_path = repo_root / INTENTION_COMPASS_REL
    output_dir = repo_root / OUTPUT_DIR_REL

    # Validate inputs exist
    for p in [score_audit_path, atom_index_path, cluster_manifest_path, intention_path]:
        if not p.exists():
            print(f"ERROR: Missing input file: {p}", file=sys.stderr)
            sys.exit(1)

    print("Loading inputs...")
    score_audit = load_jsonl(score_audit_path)
    atom_index = load_jsonl(atom_index_path)
    cluster_manifest = load_jsonl(cluster_manifest_path)

    # Build lookup maps
    score_map = {r["atom_id"]: r for r in score_audit}
    cluster_ctx = build_cluster_context(cluster_manifest)

    # Build cluster_id lookup from atom_index (atom_id → cluster_id)
    cluster_id_map = {r["atom_id"]: r.get("cluster_id") for r in atom_index}

    # Step 1: Filter pending atoms
    pending_atoms = [r for r in atom_index if r.get("integration_status") == "pending"]
    print(f"  Pending atoms: {len(pending_atoms)}")

    # Step 2: Filter to sovereign_review or auto_promote bands (from score audit)
    eligible = []
    for atom in pending_atoms:
        aid = atom["atom_id"]
        audit = score_map.get(aid)
        if not audit:
            continue
        band = audit.get("band", "")
        if band in ("sovereign_review", "auto_promote"):
            eligible.append({
                "atom_id": aid,
                "source_id": atom.get("source_id", ""),
                "score": audit.get("score", 0.0),
                "band": band,
                "cluster_id": atom.get("cluster_id"),
                "content_preview": audit.get("content_preview", ""),
                "category": atom.get("category", ""),
            })

    print(f"  Eligible atoms (sovereign_review + auto_promote): {len(eligible)}")

    if not eligible:
        print("WARNING: No eligible atoms found. Generating empty queue.", file=sys.stderr)

    # Step 3: Parse intentions
    intentions = parse_intentions(intention_path)
    print(f"  Active intentions parsed: {len(intentions)}")

    # Step 4: Match intentions + compute priority score
    queue_records = []
    for atom in eligible:
        content = atom["content_preview"]
        cluster_id = atom.get("cluster_id")

        # Primary: match against atom content
        matches = match_intentions(content, intentions)

        # Fallback: if no matches, try cluster representative preview
        if not matches and cluster_id is not None:
            cluster_preview = cluster_ctx.get(cluster_id, "")
            if cluster_preview:
                matches = match_intentions(cluster_preview, intentions)

        matched_ids = [m[0] for m in matches]
        intent_boost = max((m[1] for m in matches), default=0.0)

        # Priority score: base atom score + intention alignment boost (0–0.3 range)
        priority_score = atom["score"] + (intent_boost * 0.3)

        queue_records.append({
            "atom_id": atom["atom_id"],
            "source_file": atom["source_id"],
            "excerpt": content[:200],
            "matched_intentions": matched_ids,
            "priority_score": round(priority_score, 6),
            "cluster_id": cluster_id,
            "band": atom["band"],
            "status": "queued",
        })

    # Step 5: Sort by priority_score descending, cap at max_atoms
    queue_records.sort(key=lambda r: r["priority_score"], reverse=True)
    queue_records = queue_records[:max_atoms]
    print(f"  Queue size (capped at {max_atoms}): {len(queue_records)}")

    # Step 6: Write JSONL output
    jsonl_path = output_dir / QUEUE_JSONL
    atomic_write_jsonl(jsonl_path, queue_records)
    print(f"  Written: {jsonl_path}")

    # Step 7: Build and write markdown output
    md_path = output_dir / QUEUE_MD
    md_content = build_markdown(queue_records, intentions)
    fd, tmp = tempfile.mkstemp(dir=output_dir, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(md_content)
        os.replace(tmp, md_path)
    except Exception:
        os.unlink(tmp)
        raise
    print(f"  Written: {md_path}")

    # Stats
    band_counts = defaultdict(int)
    intent_counts = defaultdict(int)
    unmatched = 0
    for r in queue_records:
        band_counts[r["band"]] += 1
        if r["matched_intentions"]:
            for iid in r["matched_intentions"]:
                intent_counts[iid] += 1
        else:
            unmatched += 1

    stats = {
        "total": len(queue_records),
        "bands": dict(band_counts),
        "intentions_matched": len(intent_counts),
        "unmatched_atoms": unmatched,
        "top_intentions": sorted(intent_counts.items(), key=lambda x: x[1], reverse=True)[:10],
    }

    print(f"\n  Stats: {stats['total']} atoms, {stats['intentions_matched']} intentions matched, {stats['unmatched_atoms']} unmatched")
    for iid, cnt in stats["top_intentions"]:
        print(f"    {iid}: {cnt} atoms")

    return stats


# ---------------------------------------------------------------------------
# Markdown builder
# ---------------------------------------------------------------------------
def build_markdown(queue_records: list[dict], intentions: list[dict]) -> str:
    """Build human-readable markdown queue grouped by intention."""
    intent_lookup = {i["id"]: i["title"] for i in intentions}

    # Group atoms by intention
    by_intention: dict[str, list[dict]] = defaultdict(list)
    unmatched = []
    for rec in queue_records:
        if rec["matched_intentions"]:
            # File under first (highest-scoring) matched intention
            primary = rec["matched_intentions"][0]
            by_intention[primary].append(rec)
        else:
            unmatched.append(rec)

    # Band counts
    band_counts = defaultdict(int)
    for r in queue_records:
        band_counts[r["band"]] += 1

    lines = []
    lines.append("# Protease Queue — Sovereign Chewing Queue")
    lines.append("")
    lines.append(f"**Generated**: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"**Total atoms**: {len(queue_records)}")
    lines.append(f"**Bands**: {', '.join(f'{b}: {c}' for b, c in sorted(band_counts.items()))}")
    lines.append(f"**Intentions matched**: {len(by_intention)}")
    lines.append(f"**Unmatched atoms**: {len(unmatched)}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Per-intention sections, sorted by atom count desc
    sorted_intents = sorted(by_intention.items(), key=lambda x: len(x[1]), reverse=True)

    for int_id, atoms in sorted_intents:
        title = intent_lookup.get(int_id, "(unknown)")
        lines.append(f"## {int_id}: {title[:100]}")
        lines.append(f"**Atoms**: {len(atoms)}")
        lines.append("")
        for atom in atoms[:20]:  # Cap display per section
            excerpt = atom["excerpt"].replace("\n", " ")[:150]
            lines.append(f"- **{atom['atom_id']}** (score: {atom['priority_score']:.3f}, cluster: {atom['cluster_id']}, band: {atom['band']})")
            lines.append(f"  > {excerpt}")
        if len(atoms) > 20:
            lines.append(f"  ... and {len(atoms) - 20} more atoms")
        lines.append("")

    # Unmatched section
    if unmatched:
        lines.append("## Unmatched (no intention alignment)")
        lines.append(f"**Atoms**: {len(unmatched)}")
        lines.append("")
        for atom in unmatched[:20]:
            excerpt = atom["excerpt"].replace("\n", " ")[:150]
            lines.append(f"- **{atom['atom_id']}** (score: {atom['priority_score']:.3f}, cluster: {atom['cluster_id']}, band: {atom['band']})")
            lines.append(f"  > {excerpt}")
        if len(unmatched) > 20:
            lines.append(f"  ... and {len(unmatched) - 20} more atoms")
        lines.append("")

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Protease Queue Builder — prioritized atom chewing queue")
    parser.add_argument("--repo-root", type=Path, required=True, help="Path to syncrescendence repo root")
    parser.add_argument("--max-atoms", type=int, default=120, help="Maximum atoms in queue (default: 120)")
    args = parser.parse_args()

    if not args.repo_root.is_dir():
        print(f"ERROR: repo-root does not exist: {args.repo_root}", file=sys.stderr)
        sys.exit(1)

    print(f"Protease Queue Builder — repo: {args.repo_root}, max: {args.max_atoms}")
    build_queue(args.repo_root, args.max_atoms)
    print("\nDone.")


if __name__ == "__main__":
    main()
