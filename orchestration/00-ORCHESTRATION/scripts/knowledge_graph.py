#!/usr/bin/env python3
"""
knowledge_graph.py — DC-148 Local Knowledge Graph with Fuzzy Repair

Extracts entities and relationships from repo markdown files (MEMORY.md,
ARCH-*, DYN-*, AGENTS.md, etc.), stores them in a local SQLite graph,
and provides fuzzy duplicate detection + merge capabilities.

Usage:
    python3 knowledge_graph.py ingest [--repo-root PATH]
    python3 knowledge_graph.py query <entity>
    python3 knowledge_graph.py neighbors <entity> [--depth N]
    python3 knowledge_graph.py stats
    python3 knowledge_graph.py repair [--auto-merge] [--threshold N]
    python3 knowledge_graph.py export [--format jsonl|dot]

DB: orchestration/00-ORCHESTRATION/state/knowledge_graph.db
Deps: stdlib only (sqlite3, re, json, pathlib, argparse, collections, difflib)
"""

import argparse
import collections
import json
import os
import re
import sqlite3
import sys
from difflib import SequenceMatcher
from pathlib import Path

# ── Configuration ──────────────────────────────────────────────────────

REPO_ROOT_DEFAULT = Path(__file__).resolve().parent.parent.parent.parent
DB_PATH_DEFAULT = Path(__file__).resolve().parent.parent / "state" / "knowledge_graph.db"

AGENTS = ["commander", "psyche", "ajna", "adjudicator", "cartographer", "sovereign"]

# File patterns to scan (relative globs from repo root)
SCAN_PATTERNS = [
    "agents/*/memory/MEMORY.md",
    "agents/*/INIT.md",
    "orchestration/**/ARCH-*.md",
    "orchestration/**/DYN-*.md",
    "engine/**/REF-*.md",
    "engine/**/FUNC-*.md",
    "engine/**/PROMPT-*.md",
    "canon/**/*.md",
    "praxis/**/*.md",
    "AGENTS.md",
    "CLAUDE.md",
    "README.md",
]

# Entity type patterns — (regex, entity_type)
ENTITY_PATTERNS = [
    # Agents (case-insensitive)
    (re.compile(r'\b(Commander|Psyche|Ajna|Adjudicator|Cartographer|Sovereign)\b'), "agent"),
    # Systems / services
    (re.compile(r'\b(Graphiti|Neo4j|Qdrant|Docker|SQLite|tmux|launchd|OpenClaw|Obsidian)\b'), "system"),
    # Architectural concepts
    (re.compile(r'\b(Neural Bridge|AjnaPsyche Archon|Auto-Ingest|memsync|constellation|knowledge graph)\b', re.I), "concept"),
    # Machines
    (re.compile(r'\b(Mac mini|MacBook Air|MBA|Mac ?mini)\b', re.I), "machine"),
    # File references — backtick-quoted paths or markdown links to .md/.py/.sh/.yaml
    (re.compile(r'`([A-Za-z0-9_/.-]+\.(?:md|py|sh|yaml|csv|json|db))`'), "file"),
    # Markdown links to local files
    (re.compile(r'\[([^\]]+)\]\(([^)]+\.(?:md|py|sh))\)'), "file_link"),
    # DC-NNN directives
    (re.compile(r'\b(DC-\d{3,4}[A-Z]?)\b'), "directive"),
    # DEC-XX decisions
    (re.compile(r'\b(DEC-[A-Z]\d+)\b'), "decision"),
    # INT-NNNN incidents
    (re.compile(r'\b(INT-\d{4})\b'), "incident"),
    # CANON-NNNNN references
    (re.compile(r'\b(CANON-\d{5})\b'), "canon_ref"),
    # Model names
    (re.compile(r'\b(GPT-5\.\d[\w-]*|Opus 4\.\d|Sonnet 4\.\d|Haiku 4\.\d|'
                r'Gemini (?:Flash|Pro) \d\.\d|Grok \d[\w.]*|Kimi K\d\.\d)\b'), "model"),
]

# Relationship patterns — (regex, relation_type, src_group, dst_group)
RELATIONSHIP_PATTERNS = [
    # "X dispatches to Y" / "dispatch to Y"
    (re.compile(r'(?:dispatch(?:es|ed)?|send(?:s)?)\s+(?:to|→)\s+\*?\*?(\w+)\*?\*?', re.I),
     "dispatches_to", None, 1),
    # "X runs on Y" / "X on Mac mini"
    (re.compile(r'\b(\w+)\s+(?:runs? on|on|lives? on)\s+(Mac\s*mini|MacBook Air|MBA)', re.I),
     "runs_on", 1, 2),
    # "X uses Y" / "X via Y"
    (re.compile(r'\b(\w+)\s+(?:uses?|via|through)\s+(\w+)', re.I),
     "uses", 1, 2),
    # Cross-reference links: `path/to/file.md`
    (re.compile(r'`([A-Za-z0-9_/.-]+\.(?:md|py|sh))`'), "references", None, 1),
]

# ── Database ───────────────────────────────────────────────────────────

SCHEMA = """
CREATE TABLE IF NOT EXISTS entities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    source_file TEXT,
    metadata_json TEXT DEFAULT '{}',
    merged_into INTEGER DEFAULT NULL,
    UNIQUE(name, type)
);

CREATE TABLE IF NOT EXISTS edges (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    src_id INTEGER NOT NULL REFERENCES entities(id),
    dst_id INTEGER NOT NULL REFERENCES entities(id),
    relation TEXT NOT NULL,
    weight REAL DEFAULT 1.0,
    source_file TEXT,
    UNIQUE(src_id, dst_id, relation)
);

CREATE INDEX IF NOT EXISTS idx_entity_name ON entities(name);
CREATE INDEX IF NOT EXISTS idx_entity_type ON entities(type);
CREATE INDEX IF NOT EXISTS idx_edge_src ON edges(src_id);
CREATE INDEX IF NOT EXISTS idx_edge_dst ON edges(dst_id);
"""


class KnowledgeGraph:
    """Local SQLite-backed knowledge graph with fuzzy repair."""

    def __init__(self, db_path: Path):
        self.db_path = db_path
        db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(db_path))
        self.conn.execute("PRAGMA journal_mode=WAL")
        self.conn.execute("PRAGMA foreign_keys=ON")
        self.conn.executescript(SCHEMA)
        self.conn.commit()

    def close(self):
        self.conn.close()

    # ── Entity CRUD ────────────────────────────────────────────────

    def upsert_entity(self, name: str, etype: str, source_file: str = None,
                      metadata: dict = None) -> int:
        """Insert or update entity, return its id."""
        meta_json = json.dumps(metadata or {})
        cur = self.conn.execute(
            "INSERT INTO entities (name, type, source_file, metadata_json) "
            "VALUES (?, ?, ?, ?) "
            "ON CONFLICT(name, type) DO UPDATE SET "
            "source_file = COALESCE(excluded.source_file, source_file), "
            "metadata_json = excluded.metadata_json",
            (name, etype, source_file, meta_json),
        )
        self.conn.commit()
        row = self.conn.execute(
            "SELECT id FROM entities WHERE name=? AND type=?", (name, etype)
        ).fetchone()
        return row[0]

    def upsert_edge(self, src_id: int, dst_id: int, relation: str,
                    weight: float = 1.0, source_file: str = None):
        """Insert or bump weight on edge."""
        self.conn.execute(
            "INSERT INTO edges (src_id, dst_id, relation, weight, source_file) "
            "VALUES (?, ?, ?, ?, ?) "
            "ON CONFLICT(src_id, dst_id, relation) DO UPDATE SET "
            "weight = weight + excluded.weight",
            (src_id, dst_id, relation, weight, source_file),
        )
        self.conn.commit()

    def get_entity(self, name: str, etype: str = None):
        """Look up entity by name (and optional type). Returns (id, name, type, source)."""
        if etype:
            return self.conn.execute(
                "SELECT id, name, type, source_file FROM entities "
                "WHERE name=? AND type=? AND merged_into IS NULL", (name, etype)
            ).fetchone()
        return self.conn.execute(
            "SELECT id, name, type, source_file FROM entities "
            "WHERE name=? AND merged_into IS NULL", (name,)
        ).fetchone()

    def search_entities(self, pattern: str):
        """Fuzzy search entities by LIKE pattern."""
        return self.conn.execute(
            "SELECT id, name, type, source_file FROM entities "
            "WHERE name LIKE ? AND merged_into IS NULL ORDER BY type, name",
            (f"%{pattern}%",)
        ).fetchall()

    # ── Ingestion ──────────────────────────────────────────────────

    def ingest_file(self, filepath: Path, repo_root: Path):
        """Extract entities and relationships from a single markdown file."""
        try:
            text = filepath.read_text(encoding="utf-8", errors="replace")
        except (OSError, UnicodeDecodeError):
            return 0, 0

        rel_path = str(filepath.relative_to(repo_root))
        entity_count = 0
        edge_count = 0

        # The source file itself is an entity
        file_id = self.upsert_entity(rel_path, "file", rel_path)
        entity_count += 1

        # Extract entities
        found_entities = {}  # (name, type) -> id
        for pattern, etype in ENTITY_PATTERNS:
            for match in pattern.finditer(text):
                if etype == "file_link":
                    # Group 2 is the path, group 1 is the label
                    name = match.group(2)
                    actual_type = "file"
                else:
                    name = match.group(1)
                    actual_type = etype

                # Normalize
                name = name.strip()
                if not name or len(name) < 2:
                    continue

                key = (name, actual_type)
                if key not in found_entities:
                    eid = self.upsert_entity(name, actual_type, rel_path)
                    found_entities[key] = eid
                    entity_count += 1
                    # Edge: this file mentions this entity
                    self.upsert_edge(file_id, eid, "mentions", 1.0, rel_path)
                    edge_count += 1

        # Extract explicit relationships from table rows and structured patterns
        for pattern, relation, src_grp, dst_grp in RELATIONSHIP_PATTERNS:
            for match in pattern.finditer(text):
                if src_grp is not None and dst_grp is not None:
                    src_name = match.group(src_grp).strip()
                    dst_name = match.group(dst_grp).strip()
                    if len(src_name) < 2 or len(dst_name) < 2:
                        continue
                    src_ent = self._resolve_entity(src_name)
                    dst_ent = self._resolve_entity(dst_name)
                    if src_ent and dst_ent:
                        self.upsert_edge(src_ent, dst_ent, relation, 1.0, rel_path)
                        edge_count += 1
                elif dst_grp is not None:
                    # Source is the file itself
                    dst_name = match.group(dst_grp).strip()
                    if len(dst_name) < 2:
                        continue
                    dst_ent = self._resolve_entity(dst_name)
                    if dst_ent:
                        self.upsert_edge(file_id, dst_ent, relation, 1.0, rel_path)
                        edge_count += 1

        return entity_count, edge_count

    def _resolve_entity(self, name: str):
        """Find entity id by name (any type), or return None."""
        row = self.conn.execute(
            "SELECT id FROM entities WHERE name=? AND merged_into IS NULL", (name,)
        ).fetchone()
        return row[0] if row else None

    def ingest_repo(self, repo_root: Path):
        """Scan repo for markdown files matching SCAN_PATTERNS and ingest all."""
        total_entities = 0
        total_edges = 0
        files_scanned = 0

        for pattern in SCAN_PATTERNS:
            for filepath in sorted(repo_root.glob(pattern)):
                if not filepath.is_file():
                    continue
                ne, nedge = self.ingest_file(filepath, repo_root)
                total_entities += ne
                total_edges += nedge
                files_scanned += 1

        return files_scanned, total_entities, total_edges

    # ── Query ──────────────────────────────────────────────────────

    def query_entity(self, name: str):
        """Return entity info + all edges (in and out)."""
        entities = self.search_entities(name)
        if not entities:
            return None

        results = []
        for eid, ename, etype, esrc in entities:
            outgoing = self.conn.execute(
                "SELECT e.relation, e.weight, t.name, t.type, e.source_file "
                "FROM edges e JOIN entities t ON e.dst_id=t.id "
                "WHERE e.src_id=? ORDER BY e.weight DESC", (eid,)
            ).fetchall()
            incoming = self.conn.execute(
                "SELECT e.relation, e.weight, s.name, s.type, e.source_file "
                "FROM edges e JOIN entities s ON e.src_id=s.id "
                "WHERE e.dst_id=? ORDER BY e.weight DESC", (eid,)
            ).fetchall()
            results.append({
                "id": eid, "name": ename, "type": etype, "source": esrc,
                "outgoing": [{"relation": r, "weight": w, "target": n,
                              "target_type": t, "source_file": sf}
                             for r, w, n, t, sf in outgoing],
                "incoming": [{"relation": r, "weight": w, "source": n,
                              "source_type": t, "source_file": sf}
                             for r, w, n, t, sf in incoming],
            })
        return results

    def neighbors(self, name: str, depth: int = 1):
        """BFS from entity to depth N, return subgraph."""
        start_entities = self.search_entities(name)
        if not start_entities:
            return {"nodes": [], "edges": []}

        visited = set()
        queue = collections.deque()
        nodes = {}
        edges_out = []

        for eid, ename, etype, esrc in start_entities:
            queue.append((eid, 0))
            nodes[eid] = {"id": eid, "name": ename, "type": etype, "depth": 0}

        while queue:
            node_id, d = queue.popleft()
            if node_id in visited:
                continue
            visited.add(node_id)

            if d >= depth:
                continue

            # Outgoing
            for row in self.conn.execute(
                "SELECT e.dst_id, e.relation, e.weight, t.name, t.type "
                "FROM edges e JOIN entities t ON e.dst_id=t.id "
                "WHERE e.src_id=? AND t.merged_into IS NULL", (node_id,)
            ).fetchall():
                did, rel, w, dn, dt = row
                edges_out.append({"src": node_id, "dst": did, "relation": rel, "weight": w})
                if did not in nodes:
                    nodes[did] = {"id": did, "name": dn, "type": dt, "depth": d + 1}
                    queue.append((did, d + 1))

            # Incoming
            for row in self.conn.execute(
                "SELECT e.src_id, e.relation, e.weight, s.name, s.type "
                "FROM edges e JOIN entities s ON e.src_id=s.id "
                "WHERE e.dst_id=? AND s.merged_into IS NULL", (node_id,)
            ).fetchall():
                sid, rel, w, sn, st = row
                edges_out.append({"src": sid, "dst": node_id, "relation": rel, "weight": w})
                if sid not in nodes:
                    nodes[sid] = {"id": sid, "name": sn, "type": st, "depth": d + 1}
                    queue.append((sid, d + 1))

        return {"nodes": list(nodes.values()), "edges": edges_out}

    def stats(self):
        """Return counts by entity type and edge relation."""
        entity_counts = self.conn.execute(
            "SELECT type, COUNT(*) FROM entities WHERE merged_into IS NULL "
            "GROUP BY type ORDER BY COUNT(*) DESC"
        ).fetchall()
        edge_counts = self.conn.execute(
            "SELECT relation, COUNT(*), SUM(weight) FROM edges "
            "GROUP BY relation ORDER BY COUNT(*) DESC"
        ).fetchall()
        total_ent = self.conn.execute(
            "SELECT COUNT(*) FROM entities WHERE merged_into IS NULL"
        ).fetchone()[0]
        total_edge = self.conn.execute("SELECT COUNT(*) FROM edges").fetchone()[0]
        return {
            "total_entities": total_ent,
            "total_edges": total_edge,
            "entities_by_type": {t: c for t, c in entity_counts},
            "edges_by_relation": {r: {"count": c, "total_weight": w}
                                  for r, c, w in edge_counts},
        }

    # ── Fuzzy Repair ───────────────────────────────────────────────

    def find_duplicates(self, threshold: float = 0.85):
        """Find near-duplicate entity pairs using normalized string similarity."""
        entities = self.conn.execute(
            "SELECT id, name, type FROM entities WHERE merged_into IS NULL "
            "ORDER BY type, name"
        ).fetchall()

        duplicates = []
        # Group by type for efficiency
        by_type = collections.defaultdict(list)
        for eid, name, etype in entities:
            by_type[etype].append((eid, name))

        for etype, ents in by_type.items():
            n = len(ents)
            for i in range(n):
                for j in range(i + 1, n):
                    id_a, name_a = ents[i]
                    id_b, name_b = ents[j]

                    # Quick check: identical after normalization
                    norm_a = _normalize(name_a)
                    norm_b = _normalize(name_b)

                    if norm_a == norm_b:
                        sim = 1.0
                    else:
                        sim = SequenceMatcher(None, norm_a, norm_b).ratio()

                    if sim >= threshold:
                        case_only = name_a.lower() == name_b.lower()
                        duplicates.append({
                            "id_a": id_a, "name_a": name_a,
                            "id_b": id_b, "name_b": name_b,
                            "type": etype, "similarity": round(sim, 3),
                            "case_only": case_only,
                        })

        return sorted(duplicates, key=lambda d: -d["similarity"])

    def merge_entities(self, keep_id: int, remove_id: int):
        """Merge remove_id into keep_id: redirect all edges, mark as merged."""
        # Redirect outgoing edges
        self.conn.execute(
            "UPDATE OR IGNORE edges SET src_id=? WHERE src_id=?",
            (keep_id, remove_id)
        )
        # Redirect incoming edges
        self.conn.execute(
            "UPDATE OR IGNORE edges SET dst_id=? WHERE dst_id=?",
            (keep_id, remove_id)
        )
        # Delete orphaned edges (conflicts from UNIQUE constraint)
        self.conn.execute("DELETE FROM edges WHERE src_id=?", (remove_id,))
        self.conn.execute("DELETE FROM edges WHERE dst_id=?", (remove_id,))
        # Mark entity as merged
        self.conn.execute(
            "UPDATE entities SET merged_into=? WHERE id=?", (keep_id, remove_id)
        )
        self.conn.commit()

    def auto_merge_safe(self):
        """Auto-merge case-only duplicates (safe merges). Returns count."""
        dupes = self.find_duplicates(threshold=0.85)
        merged = 0
        for d in dupes:
            if d["case_only"]:
                # Keep the one with more conventional casing (capitalized)
                keep = d["id_a"] if d["name_a"][0].isupper() else d["id_b"]
                remove = d["id_b"] if keep == d["id_a"] else d["id_a"]
                self.merge_entities(keep, remove)
                merged += 1
                print(f"  Merged: '{d['name_b']}' -> '{d['name_a']}' ({d['type']})")
        return merged

    # ── Export ──────────────────────────────────────────────────────

    def export_jsonl(self, out=sys.stdout):
        """Export all entities and edges as JSONL."""
        for row in self.conn.execute(
            "SELECT id, name, type, source_file, metadata_json "
            "FROM entities WHERE merged_into IS NULL"
        ):
            eid, name, etype, src, meta = row
            out.write(json.dumps({
                "kind": "entity", "id": eid, "name": name,
                "type": etype, "source_file": src,
                "metadata": json.loads(meta),
            }) + "\n")
        for row in self.conn.execute(
            "SELECT src_id, dst_id, relation, weight, source_file FROM edges"
        ):
            sid, did, rel, w, src = row
            out.write(json.dumps({
                "kind": "edge", "src_id": sid, "dst_id": did,
                "relation": rel, "weight": w, "source_file": src,
            }) + "\n")

    def export_dot(self, out=sys.stdout):
        """Export graph in DOT format for Graphviz."""
        out.write("digraph knowledge_graph {\n")
        out.write("  rankdir=LR;\n")
        out.write("  node [shape=box, fontsize=10];\n")
        type_colors = {
            "agent": "lightblue", "system": "lightyellow", "concept": "lightgreen",
            "file": "lightgray", "directive": "orange", "machine": "pink",
            "model": "lavender", "decision": "wheat", "incident": "salmon",
        }
        for eid, name, etype in self.conn.execute(
            "SELECT id, name, type FROM entities WHERE merged_into IS NULL"
        ):
            color = type_colors.get(etype, "white")
            label = name.replace('"', '\\"')
            out.write(f'  n{eid} [label="{label}\\n({etype})" '
                      f'style=filled fillcolor="{color}"];\n')
        for sid, did, rel, w in self.conn.execute(
            "SELECT src_id, dst_id, relation, weight FROM edges"
        ):
            out.write(f'  n{sid} -> n{did} [label="{rel}" '
                      f'penwidth={max(0.5, min(w, 5.0))}];\n')
        out.write("}\n")


# ── Helpers ────────────────────────────────────────────────────────────

def _normalize(s: str) -> str:
    """Normalize entity name for comparison: lowercase, strip punctuation, collapse spaces."""
    s = s.lower().strip()
    s = re.sub(r'[_\-./]+', ' ', s)
    s = re.sub(r'\s+', ' ', s)
    # Remove common suffixes that don't change identity
    s = re.sub(r'\s*(agent|system|service|daemon|script)\s*$', '', s)
    return s.strip()


# ── CLI ────────────────────────────────────────────────────────────────

def cmd_ingest(args, kg: KnowledgeGraph):
    repo = Path(args.repo_root).resolve()
    print(f"Scanning {repo} ...")
    files, ents, edges = kg.ingest_repo(repo)
    print(f"Done: {files} files scanned, {ents} entity upserts, {edges} edge upserts")
    s = kg.stats()
    print(f"Graph now: {s['total_entities']} entities, {s['total_edges']} edges")


def cmd_query(args, kg: KnowledgeGraph):
    results = kg.query_entity(args.entity)
    if not results:
        print(f"No entity matching '{args.entity}'")
        return
    for r in results:
        print(f"\n{'='*60}")
        print(f"  {r['name']} ({r['type']}) [id={r['id']}]")
        print(f"  Source: {r['source']}")
        if r['outgoing']:
            print(f"  Outgoing ({len(r['outgoing'])}):")
            for e in r['outgoing'][:20]:
                print(f"    --{e['relation']}--> {e['target']} ({e['target_type']}) "
                      f"[w={e['weight']}]")
            if len(r['outgoing']) > 20:
                print(f"    ... and {len(r['outgoing'])-20} more")
        if r['incoming']:
            print(f"  Incoming ({len(r['incoming'])}):")
            for e in r['incoming'][:20]:
                print(f"    <--{e['relation']}-- {e['source']} ({e['source_type']}) "
                      f"[w={e['weight']}]")
            if len(r['incoming']) > 20:
                print(f"    ... and {len(r['incoming'])-20} more")


def cmd_neighbors(args, kg: KnowledgeGraph):
    subgraph = kg.neighbors(args.entity, depth=args.depth)
    if not subgraph["nodes"]:
        print(f"No entity matching '{args.entity}'")
        return
    print(f"Subgraph around '{args.entity}' (depth={args.depth}):")
    print(f"  {len(subgraph['nodes'])} nodes, {len(subgraph['edges'])} edges")
    print()
    by_depth = collections.defaultdict(list)
    for n in subgraph["nodes"]:
        by_depth[n["depth"]].append(n)
    for d in sorted(by_depth.keys()):
        print(f"  Depth {d}:")
        for n in sorted(by_depth[d], key=lambda x: x["name"]):
            print(f"    {n['name']} ({n['type']})")


def cmd_stats(args, kg: KnowledgeGraph):
    s = kg.stats()
    print(f"Knowledge Graph: {s['total_entities']} entities, {s['total_edges']} edges")
    print(f"\nEntities by type:")
    for t, c in sorted(s["entities_by_type"].items(), key=lambda x: -x[1]):
        print(f"  {t:20s} {c:5d}")
    print(f"\nEdges by relation:")
    for r, info in sorted(s["edges_by_relation"].items(), key=lambda x: -x[1]["count"]):
        print(f"  {r:20s} {info['count']:5d} (total weight: {info['total_weight']:.0f})")


def cmd_repair(args, kg: KnowledgeGraph):
    threshold = args.threshold / 100.0
    dupes = kg.find_duplicates(threshold=threshold)
    if not dupes:
        print("No duplicates found above threshold.")
        return

    print(f"Found {len(dupes)} potential duplicate pairs (threshold={threshold:.0%}):\n")

    if args.auto_merge:
        safe = [d for d in dupes if d["case_only"]]
        unsafe = [d for d in dupes if not d["case_only"]]
        if safe:
            print(f"Auto-merging {len(safe)} case-only duplicates:")
            merged = kg.auto_merge_safe()
            print(f"  {merged} merges completed.")
        if unsafe:
            print(f"\n{len(unsafe)} non-trivial duplicates require manual review:")
            for d in unsafe:
                print(f"  [{d['similarity']:.0%}] '{d['name_a']}' vs '{d['name_b']}' "
                      f"({d['type']})")
    else:
        for d in dupes:
            marker = " [SAFE: case-only]" if d["case_only"] else ""
            print(f"  [{d['similarity']:.0%}] '{d['name_a']}' vs '{d['name_b']}' "
                  f"({d['type']}){marker}")
        print(f"\nRun with --auto-merge to auto-fix case-only duplicates.")


def cmd_export(args, kg: KnowledgeGraph):
    fmt = args.format
    if fmt == "jsonl":
        kg.export_jsonl()
    elif fmt == "dot":
        kg.export_dot()
    else:
        print(f"Unknown format: {fmt}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        prog="knowledge_graph",
        description="DC-148 Local Knowledge Graph — entity extraction, "
                    "SQLite storage, fuzzy repair",
    )
    parser.add_argument("--db", default=str(DB_PATH_DEFAULT),
                        help="Path to SQLite database")
    parser.add_argument("--repo-root", default=str(REPO_ROOT_DEFAULT),
                        help="Repository root path")

    sub = parser.add_subparsers(dest="command", required=True)

    # ingest
    sub.add_parser("ingest", help="Scan repo and build/update graph")

    # query
    p_query = sub.add_parser("query", help="Show all relationships for an entity")
    p_query.add_argument("entity", help="Entity name (partial match)")

    # neighbors
    p_nb = sub.add_parser("neighbors", help="BFS neighborhood to depth N")
    p_nb.add_argument("entity", help="Entity name (partial match)")
    p_nb.add_argument("--depth", type=int, default=2, help="BFS depth (default: 2)")

    # stats
    sub.add_parser("stats", help="Entity/edge counts by type")

    # repair
    p_repair = sub.add_parser("repair", help="Fuzzy duplicate detection and repair")
    p_repair.add_argument("--auto-merge", action="store_true",
                          help="Auto-merge safe (case-only) duplicates")
    p_repair.add_argument("--threshold", type=int, default=85,
                          help="Similarity threshold 0-100 (default: 85)")

    # export
    p_export = sub.add_parser("export", help="Export graph as JSONL or DOT")
    p_export.add_argument("--format", choices=["jsonl", "dot"], default="jsonl",
                          help="Output format (default: jsonl)")

    args = parser.parse_args()
    kg = KnowledgeGraph(Path(args.db))

    try:
        {
            "ingest": cmd_ingest,
            "query": cmd_query,
            "neighbors": cmd_neighbors,
            "stats": cmd_stats,
            "repair": cmd_repair,
            "export": cmd_export,
        }[args.command](args, kg)
    finally:
        kg.close()


if __name__ == "__main__":
    main()
