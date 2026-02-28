#!/usr/bin/env python3
"""Canon Compiler — 5-stage pipeline (CC49 ratified V-2).

Stage 1: PARSE    — Extract frontmatter + body structure → IR (JSON)
Stage 2: VALIDATE — S-1 schema enforcement + cross-file coherence
Stage 3: GRAPH    — Build dependency DAG, detect cycles, emit Mermaid
Stage 4: COMPRESS — Generate Syncrescript v2 structural skeleton + metrics
Stage 5: EMIT     — Render views: Scripture (human), Config (agent), Graph, Ledger

The compiler IS the immune system (T-6 ratified).
Validation = circulating antibodies. S-1 frontmatter = MHC.

Usage:
    python3 corpus/canon_compiler.py parse              # Stage 1 only → IR to stdout
    python3 corpus/canon_compiler.py validate            # Stages 1+2
    python3 corpus/canon_compiler.py compile             # All implemented stages
    python3 corpus/canon_compiler.py parse --out ir.json # Write IR to file
    python3 corpus/canon_compiler.py validate --json     # JSON output
    python3 corpus/canon_compiler.py validate --strict   # Warnings = errors
"""

import sys
import os
import re
import yaml
import json
import argparse
from pathlib import Path
from datetime import date, datetime

CANON_DIR = Path(__file__).parent.parent / "canon"
MUTAGENIC_DIR = Path(__file__).parent.parent / "corpus" / "mutagenic"

# ============================================================
# S-1 SCHEMA (Ratified CC49)
# ============================================================

VALID_TIERS = {"cosmos", "core", "lattice", "chain", "archive", "immune"}
VALID_CHAINS = {None, "null", "intelligence", "information", "insight", "expertise", "knowledge", "wisdom"}
VALID_CELESTIAL_TYPES = {"root", "planetary", "ring", "lunar", "comet", "asteroid", "satellite", "policy", "meta"}
VALID_VOLATILITY_BANDS = {"permanent", "stable", "moderate", "dynamic"}
VALID_REFRESH_CADENCES = {None, "null", "", "annual", "semi-annual", "quarterly", "monthly"}
VALID_STATUSES = {"canonical", "draft", "deprecated", "archived", "demoted"}
VALID_OP_STATUSES = {"operational", "partial", "theoretical", "pilot"}
VALID_ELEMENTS = {None, "null", "", "fire", "water", "earth", "air", "quintessence"}
VALID_OODA_PHASES = {None, "null", "", "observe", "orient", "decide", "act", "sharpen"}
VALID_LAYERS = {None, "null", "", "lattice", "chain", "cosmos"}
VALID_DEV_STATUSES = {None, "null", "", "active", "stable", "dormant"}

REQUIRED_FIELDS = [
    "id", "canonical_name", "tier", "celestial_type",
    "volatility_band", "status", "operational_status",
    "version", "created", "updated"
]

RECOMMENDED_FIELDS = [
    "parent", "requires", "siblings", "synthesizes",
    "refresh_cadence", "last_verified", "element", "ooda_phase",
    "volatile_sections", "title", "chain"
]

# Volatility consistency rules
VOLATILITY_RULES = {
    ("permanent", "monthly"): "Permanent content with monthly refresh — contradiction",
    ("permanent", "quarterly"): "Permanent content with quarterly refresh — too frequent",
    ("dynamic", "annual"): "Dynamic content with annual refresh — too slow",
    ("dynamic", None): "Dynamic content with no refresh cadence — will go stale",
    ("dynamic", ""): "Dynamic content with no refresh cadence — will go stale",
    ("dynamic", "null"): "Dynamic content with no refresh cadence — will go stale",
}


# ============================================================
# STAGE 1: PARSE — Extract intermediate representation
# ============================================================

def parse_canon_file(filepath):
    """Parse a single canon file into intermediate representation."""
    text = filepath.read_text(encoding="utf-8")
    ir = {
        "source_path": str(filepath),
        "filename": filepath.name,
        "frontmatter": None,
        "has_frontmatter": False,
        "body": {
            "headings": [],
            "line_count": 0,
            "word_count": 0,
            "has_version_inline": False,
            "inline_versions": [],
            "sections": [],
        },
        "parse_errors": [],
    }

    # Extract frontmatter
    match = re.match(r"^---\s*\n(.*?\n)---\s*\n", text, re.DOTALL)
    if match:
        try:
            fm = yaml.safe_load(match.group(1))
            if isinstance(fm, dict):
                ir["frontmatter"] = fm
                ir["has_frontmatter"] = True
            else:
                ir["parse_errors"].append("Frontmatter parsed but not a dict")
        except yaml.YAMLError as e:
            ir["parse_errors"].append(f"YAML parse error: {e}")
        body_text = text[match.end():]
    else:
        ir["parse_errors"].append("No YAML frontmatter found")
        body_text = text

    # Parse body structure
    lines = body_text.split("\n")
    ir["body"]["line_count"] = len(lines)
    ir["body"]["word_count"] = len(body_text.split())

    # Extract headings
    for i, line in enumerate(lines):
        heading_match = re.match(r"^(#{1,6})\s+(.+)", line)
        if heading_match:
            ir["body"]["headings"].append({
                "level": len(heading_match.group(1)),
                "text": heading_match.group(2).strip(),
                "line": i + 1,
            })

    # Check for inline version declarations
    version_matches = re.findall(r"\*\*Version\*\*:\s*(\d+\.\d+\.\d+)", body_text)
    if version_matches:
        ir["body"]["has_version_inline"] = True
        ir["body"]["inline_versions"] = version_matches

    # Extract sections (H2-level blocks)
    current_section = None
    for heading in ir["body"]["headings"]:
        if heading["level"] <= 2:
            if current_section:
                ir["body"]["sections"].append(current_section)
            current_section = {"title": heading["text"], "line": heading["line"]}
    if current_section:
        ir["body"]["sections"].append(current_section)

    return ir


def stage_parse(canon_dir=CANON_DIR):
    """Stage 1: Parse all canon files into IR."""
    ir_collection = {
        "stage": "parse",
        "timestamp": datetime.now().isoformat(),
        "canon_dir": str(canon_dir),
        "file_count": 0,
        "parse_errors": 0,
        "files": [],
        "id_index": {},  # id → index for cross-ref
    }

    canon_files = sorted(canon_dir.glob("*.md"))
    for i, f in enumerate(canon_files):
        file_ir = parse_canon_file(f)
        ir_collection["files"].append(file_ir)
        ir_collection["file_count"] += 1
        if file_ir["parse_errors"]:
            ir_collection["parse_errors"] += len(file_ir["parse_errors"])

        # Build ID index
        if file_ir["frontmatter"] and "id" in file_ir["frontmatter"]:
            ir_collection["id_index"][str(file_ir["frontmatter"]["id"])] = i

    return ir_collection


# ============================================================
# UTILITIES
# ============================================================

def _extract_refs(fm, field):
    """Extract reference IDs from a frontmatter field."""
    refs = fm.get(field)
    if refs is None:
        return []
    if isinstance(refs, str):
        refs = [refs]
    if not isinstance(refs, list):
        refs = [refs]
    return [str(r).strip() for r in refs if str(r).strip() and str(r).strip() != "null"]


# ============================================================
# STAGE 2: VALIDATE — S-1 schema enforcement
# ============================================================

def validate_file_ir(file_ir, all_ids, strict=False):
    """Validate a single file's IR against S-1 schema."""
    issues = []
    fm = file_ir["frontmatter"]

    if fm is None:
        issues.append(("ERROR", "No valid frontmatter"))
        return issues

    # Required fields
    for field in REQUIRED_FIELDS:
        val = fm.get(field)
        if val is None or (isinstance(val, str) and val.strip() == ""):
            issues.append(("ERROR", f"Missing required field: {field}"))

    # Enum validations
    def check_enum(field, valid_set, level="ERROR"):
        val = fm.get(field)
        if val is not None and str(val).lower() not in {str(v).lower() if v else str(v) for v in valid_set}:
            issues.append((level, f"Invalid {field}: {val}"))

    check_enum("tier", VALID_TIERS)
    check_enum("chain", VALID_CHAINS)
    check_enum("celestial_type", VALID_CELESTIAL_TYPES)
    check_enum("volatility_band", VALID_VOLATILITY_BANDS)
    check_enum("refresh_cadence", VALID_REFRESH_CADENCES, "WARN")
    check_enum("status", VALID_STATUSES)
    check_enum("operational_status", VALID_OP_STATUSES)
    check_enum("element", VALID_ELEMENTS, "WARN")
    check_enum("ooda_phase", VALID_OODA_PHASES, "WARN")
    check_enum("layer", VALID_LAYERS, "WARN")
    check_enum("developmental_status", VALID_DEV_STATUSES, "WARN")

    # Recommended fields
    for field in RECOMMENDED_FIELDS:
        if field not in fm:
            issues.append(("WARN", f"Missing recommended field: {field}"))

    # Cross-reference validation
    for ref_field in ("requires", "siblings", "synthesizes", "parent"):
        refs = fm.get(ref_field)
        if refs is None:
            continue
        if isinstance(refs, str):
            refs = [refs]
        if not isinstance(refs, list):
            refs = [refs]
        for ref in refs:
            ref_str = str(ref).strip()
            if ref_str and ref_str != "null" and ref_str not in all_ids:
                issues.append(("WARN", f"{ref_field} → unknown id: {ref_str}"))

    # Version consistency
    yaml_ver = str(fm.get("version", ""))
    for inline_ver in file_ir["body"].get("inline_versions", []):
        if inline_ver != yaml_ver:
            issues.append(("WARN", f"Body version ({inline_ver}) ≠ YAML ({yaml_ver})"))

    # Volatility consistency
    vb = str(fm.get("volatility_band", "")).lower()
    rc = fm.get("refresh_cadence")
    rc_str = str(rc).lower() if rc else None
    key = (vb, rc_str)
    if key in VOLATILITY_RULES:
        issues.append(("WARN", VOLATILITY_RULES[key]))

    return issues


def stage_validate(ir_collection, strict=False):
    """Stage 2: Validate all files in IR collection."""
    all_ids = set(ir_collection["id_index"].keys())

    validation = {
        "stage": "validate",
        "timestamp": datetime.now().isoformat(),
        "total_files": ir_collection["file_count"],
        "clean_files": 0,
        "total_errors": 0,
        "total_warnings": 0,
        "orphans": [],
        "results": {},
    }

    # Validate each file
    for file_ir in ir_collection["files"]:
        issues = validate_file_ir(file_ir, all_ids, strict)
        errors = [i for i in issues if i[0] == "ERROR"]
        warns = [i for i in issues if i[0] == "WARN"]
        validation["total_errors"] += len(errors)
        validation["total_warnings"] += len(warns)
        if not issues:
            validation["clean_files"] += 1
        if issues:
            validation["results"][file_ir["filename"]] = [
                {"level": l, "message": m} for l, m in issues
            ]

    # Orphan detection
    referenced_ids = set()
    for file_ir in ir_collection["files"]:
        fm = file_ir["frontmatter"]
        if not fm:
            continue
        for ref_field in ("requires", "siblings", "synthesizes", "parent"):
            refs = fm.get(ref_field)
            if refs is None:
                continue
            if isinstance(refs, str):
                refs = [refs]
            if not isinstance(refs, list):
                refs = [refs]
            for ref in refs:
                ref_str = str(ref).strip()
                if ref_str and ref_str != "null":
                    referenced_ids.add(ref_str)

    # Files with a valid parent are positionally anchored, not orphaned
    parented_ids = set()
    for file_ir in ir_collection["files"]:
        fm = file_ir["frontmatter"]
        if fm:
            parent_refs = _extract_refs(fm, "parent") if "parent" in fm else []
            for p in parent_refs:
                if p in all_ids:
                    parented_ids.add(str(fm.get("id", "")))

    for file_ir in ir_collection["files"]:
        fm = file_ir["frontmatter"]
        if fm and "id" in fm:
            fid = str(fm["id"])
            if fid not in referenced_ids and fid != "CANON-00000" and fid not in parented_ids:
                validation["orphans"].append(fid)

    # Heatmap summary
    heatmap = {"green": 0, "yellow": 0, "red": 0, "grey": 0}
    for file_ir in ir_collection["files"]:
        fm = file_ir["frontmatter"]
        if not fm:
            heatmap["grey"] += 1
            continue
        tier = str(fm.get("tier", "")).lower()
        vb = str(fm.get("volatility_band", "")).lower()
        if tier == "immune":
            heatmap["grey"] += 1
        elif vb == "dynamic" and tier in ("cosmos", "core", "lattice"):
            heatmap["red"] += 1
        elif vb == "moderate" and tier in ("cosmos", "core"):
            heatmap["yellow"] += 1
        else:
            heatmap["green"] += 1
    validation["heatmap"] = heatmap

    return validation


# ============================================================
# STAGE 3: GRAPH — Dependency DAG, cycle detection, Mermaid
# ============================================================

def _detect_cycles(adjacency):
    """Detect cycles via DFS. Returns list of cycles found."""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {n: WHITE for n in adjacency}
    parent_map = {}
    cycles = []

    def dfs(u, path):
        color[u] = GRAY
        for v in adjacency.get(u, []):
            if v not in color:
                continue
            if color[v] == GRAY:
                # Found cycle — extract it
                cycle_start = path.index(v)
                cycles.append(path[cycle_start:] + [v])
            elif color[v] == WHITE:
                dfs(v, path + [v])
        color[u] = BLACK

    for node in adjacency:
        if color[node] == WHITE:
            dfs(node, [node])

    return cycles


def _topo_sort(adjacency, all_nodes):
    """Topological sort via Kahn's algorithm. Returns (sorted_list, has_cycle)."""
    in_degree = {n: 0 for n in all_nodes}
    for u in adjacency:
        for v in adjacency[u]:
            if v in in_degree:
                in_degree[v] += 1

    queue = sorted([n for n in all_nodes if in_degree[n] == 0])
    result = []
    while queue:
        node = queue.pop(0)
        result.append(node)
        for v in sorted(adjacency.get(node, [])):
            if v in in_degree:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

    return result, len(result) != len(all_nodes)


def _compute_depths(adjacency, all_nodes):
    """Compute max depth from roots for each node using BFS."""
    in_degree = {n: 0 for n in all_nodes}
    for u in adjacency:
        for v in adjacency.get(u, []):
            if v in in_degree:
                in_degree[v] += 1

    depths = {n: 0 for n in all_nodes if in_degree[n] == 0}
    queue = list(depths.keys())
    visited = set()

    while queue:
        node = queue.pop(0)
        if node in visited:
            continue
        visited.add(node)
        for v in adjacency.get(node, []):
            if v in all_nodes:
                new_d = depths[node] + 1
                if v not in depths or new_d > depths[v]:
                    depths[v] = new_d
                if v not in visited:
                    queue.append(v)

    # Assign depth 0 to any unvisited nodes (in cycles)
    for n in all_nodes:
        if n not in depths:
            depths[n] = 0

    return depths


def stage_graph(ir_collection):
    """Stage 3: Build dependency DAG from IR, detect cycles, compute metrics."""
    # Build adjacency: parent→child, requires edges
    adjacency = {}  # node → [nodes it points to]
    reverse_adj = {}  # node → [nodes that point to it]
    all_nodes = set()
    node_meta = {}  # id → {tier, celestial_type, volatility_band, filename}
    edge_list = []  # (source, target, edge_type)

    for file_ir in ir_collection["files"]:
        fm = file_ir["frontmatter"]
        if not fm or "id" not in fm:
            continue
        fid = str(fm["id"])
        all_nodes.add(fid)
        adjacency.setdefault(fid, [])
        reverse_adj.setdefault(fid, [])
        node_meta[fid] = {
            "tier": str(fm.get("tier", "")),
            "celestial_type": str(fm.get("celestial_type", "")),
            "volatility_band": str(fm.get("volatility_band", "")),
            "filename": file_ir["filename"],
        }

        # Parent → child (parent points to this node)
        for parent_id in _extract_refs(fm, "parent"):
            if parent_id == fid:
                continue  # Skip self-refs
            if parent_id in ir_collection["id_index"] or parent_id in all_nodes:
                adjacency.setdefault(parent_id, [])
                if fid not in adjacency[parent_id]:
                    adjacency[parent_id].append(fid)
                reverse_adj.setdefault(fid, [])
                if parent_id not in reverse_adj[fid]:
                    reverse_adj[fid].append(parent_id)
                edge_list.append((parent_id, fid, "parent"))

        # Requires: this node depends on required nodes (required → this)
        for req_id in _extract_refs(fm, "requires"):
            adjacency.setdefault(req_id, [])
            if fid not in adjacency[req_id]:
                adjacency[req_id].append(fid)
            if req_id not in reverse_adj.setdefault(fid, []):
                reverse_adj[fid].append(req_id)
            edge_list.append((req_id, fid, "requires"))

        # Siblings: bidirectional (model as undirected)
        for sib_id in _extract_refs(fm, "siblings"):
            edge_list.append((fid, sib_id, "sibling"))

        # Synthesizes: this node synthesizes others (others → this)
        for syn_id in _extract_refs(fm, "synthesizes"):
            edge_list.append((syn_id, fid, "synthesizes"))

    # Cycle detection
    cycles = _detect_cycles(adjacency)

    # Topological sort
    topo_order, has_cycle = _topo_sort(adjacency, all_nodes)

    # Depth computation
    depths = _compute_depths(adjacency, all_nodes)
    max_depth = max(depths.values()) if depths else 0

    # Roots and leaves
    roots = sorted([n for n in all_nodes if not reverse_adj.get(n)])
    leaves = sorted([n for n in all_nodes if not adjacency.get(n, [])])

    # Tier distribution
    tier_counts = {}
    for nid, meta in node_meta.items():
        t = meta["tier"]
        tier_counts[t] = tier_counts.get(t, 0) + 1

    # Depth layers
    depth_layers = {}
    for nid, d in depths.items():
        depth_layers.setdefault(d, [])
        depth_layers[d].append(nid)

    # Connected components (undirected)
    visited = set()
    components = []
    undirected = {n: set() for n in all_nodes}
    for src, tgt, _ in edge_list:
        if src in all_nodes and tgt in all_nodes:
            undirected[src].add(tgt)
            undirected[tgt].add(src)

    def bfs_component(start):
        comp = set()
        queue = [start]
        while queue:
            n = queue.pop(0)
            if n in comp:
                continue
            comp.add(n)
            for nb in undirected.get(n, []):
                if nb not in comp:
                    queue.append(nb)
        return comp

    for n in sorted(all_nodes):
        if n not in visited:
            comp = bfs_component(n)
            visited |= comp
            components.append(sorted(comp))

    # Generate Mermaid
    mermaid_lines = ["graph TD"]

    # Style classes by tier
    mermaid_lines.append("    classDef cosmos fill:#FFD700,stroke:#B8860B,color:#000")
    mermaid_lines.append("    classDef core fill:#FF6347,stroke:#B22222,color:#fff")
    mermaid_lines.append("    classDef lattice fill:#4682B4,stroke:#2F4F4F,color:#fff")
    mermaid_lines.append("    classDef chain fill:#32CD32,stroke:#228B22,color:#000")
    mermaid_lines.append("    classDef archive fill:#808080,stroke:#696969,color:#fff")
    mermaid_lines.append("    classDef immune fill:#DA70D6,stroke:#8B008B,color:#000")
    mermaid_lines.append("")

    # Nodes
    def mermaid_id(canon_id):
        return canon_id.replace("-", "_")

    for nid in sorted(all_nodes):
        mid = mermaid_id(nid)
        short = nid.replace("CANON-", "")
        meta = node_meta.get(nid, {})
        tier = meta.get("tier", "")
        mermaid_lines.append(f"    {mid}[\"{short}\"]:::{tier}")

    mermaid_lines.append("")

    # Edges (deduplicated)
    seen_edges = set()
    for src, tgt, etype in edge_list:
        if src not in all_nodes or tgt not in all_nodes:
            continue
        key = (src, tgt, etype)
        if key in seen_edges:
            continue
        seen_edges.add(key)
        msrc = mermaid_id(src)
        mtgt = mermaid_id(tgt)
        if etype == "parent":
            mermaid_lines.append(f"    {msrc} --> {mtgt}")
        elif etype == "requires":
            mermaid_lines.append(f"    {msrc} -.-> {mtgt}")
        elif etype == "sibling":
            mermaid_lines.append(f"    {msrc} <--> {mtgt}")
        elif etype == "synthesizes":
            mermaid_lines.append(f"    {msrc} ==> {mtgt}")

    mermaid_text = "\n".join(mermaid_lines)

    return {
        "stage": "graph",
        "timestamp": datetime.now().isoformat(),
        "node_count": len(all_nodes),
        "edge_count": len(seen_edges),
        "max_depth": max_depth,
        "depth_layers": {str(k): sorted(v) for k, v in sorted(depth_layers.items())},
        "roots": roots,
        "leaves": leaves,
        "root_count": len(roots),
        "leaf_count": len(leaves),
        "cycles": cycles,
        "has_cycle": len(cycles) > 0,
        "topo_order": topo_order,
        "connected_components": len(components),
        "component_sizes": [len(c) for c in components],
        "tier_distribution": tier_counts,
        "mermaid": mermaid_text,
    }


def format_graph_text(graph_result):
    """Human-readable graph report."""
    lines = []
    lines.append("Canon Compiler — Graph Report (Stage 3)")
    lines.append("=" * 60)
    lines.append(f"Nodes:             {graph_result['node_count']}")
    lines.append(f"Edges:             {graph_result['edge_count']}")
    lines.append(f"Max depth:         {graph_result['max_depth']}")
    lines.append(f"Roots:             {graph_result['root_count']}")
    lines.append(f"Leaves:            {graph_result['leaf_count']}")
    lines.append(f"Components:        {graph_result['connected_components']}")
    lines.append(f"Cycles:            {len(graph_result['cycles'])}")

    lines.append(f"\nTier distribution:")
    for tier, count in sorted(graph_result["tier_distribution"].items()):
        lines.append(f"  {tier:12s}: {count}")

    lines.append(f"\nDepth layers:")
    for depth, nodes in sorted(graph_result["depth_layers"].items()):
        lines.append(f"  Depth {depth}: {len(nodes)} nodes")

    if graph_result["cycles"]:
        lines.append(f"\n✗ CYCLES DETECTED ({len(graph_result['cycles'])}):")
        for cycle in graph_result["cycles"]:
            lines.append(f"  {' → '.join(cycle)}")
    else:
        lines.append(f"\n✓ No cycles. DAG is valid.")

    lines.append(f"\nRoots: {', '.join(graph_result['roots'])}")
    lines.append(f"Leaves: {', '.join(graph_result['leaves'])}")

    return "\n".join(lines)


# ============================================================
# STAGE 4: COMPRESS — Syncrescript v2 structural skeleton
# ============================================================

# SN v2 block types mapped from heading/content patterns
SN_BLOCK_TYPES = {
    "definition": "TERM",    # Defines a concept
    "normative": "NORM",     # Establishes a standard/rule
    "procedural": "PROC",    # Steps/process
    "passage": "PASS",       # Expository/teaching content
}

# Greek letter prefix for CANON IDs in SN notation
SN_PREFIX = "Κ"


def _classify_section(heading_text):
    """Classify a section heading into SN block type."""
    h = heading_text.lower()
    proc_signals = ["how", "step", "process", "procedure", "protocol", "workflow", "guide", "usage"]
    norm_signals = ["rule", "principle", "invariant", "constraint", "requirement", "must", "standard", "law"]
    term_signals = ["definition", "what is", "overview", "concept", "glossary", "terminology"]

    for s in proc_signals:
        if s in h:
            return "PROC"
    for s in norm_signals:
        if s in h:
            return "NORM"
    for s in term_signals:
        if s in h:
            return "TERM"
    return "PASS"


def _compress_id(canon_id):
    """Compress CANON-XXXXX to Κ-XXXXX."""
    return canon_id.replace("CANON-", f"{SN_PREFIX}-")


def _make_block_name(heading_text):
    """Convert heading text to PascalCase block name."""
    words = re.sub(r'[^a-zA-Z0-9\s]', '', heading_text).split()
    return "".join(w.capitalize() for w in words[:4])


def compress_file_ir(file_ir, graph_result=None):
    """Compress a single file IR into Syncrescript v2 skeleton."""
    fm = file_ir["frontmatter"]
    if not fm:
        return None

    fid = str(fm.get("id", ""))
    body = file_ir["body"]
    headings = body.get("headings", [])
    sections = body.get("sections", [])

    # SN v2 header (lossless structural data)
    sn_header = {
        "id": f"[[{fid}]]",
        "name": fm.get("canonical_name", fm.get("title", fid)),
        "tier": fm.get("tier", ""),
        "chain": fm.get("chain"),
        "celestial_type": fm.get("celestial_type", ""),
        "volatility_band": fm.get("volatility_band", ""),
        "sn_version": "2.0",
        "parent": fm.get("parent"),
        "requires": fm.get("requires", []),
        "siblings": fm.get("siblings", []),
        "synthesizes": fm.get("synthesizes", []),
        "entities": fm.get("entities_defined", []),
        "original_words": body.get("word_count", 0),
        "original_lines": body.get("line_count", 0),
    }

    # Remove null/empty values
    sn_header = {k: v for k, v in sn_header.items()
                 if v is not None and v != [] and v != "" and v != "null"}

    # Generate SN blocks from sections
    blocks = []
    for heading in headings:
        if heading["level"] > 3:
            continue  # Skip deep headings
        block_type = _classify_section(heading["text"])
        block_name = _make_block_name(heading["text"])
        if not block_name:
            continue
        blocks.append({
            "type": block_type,
            "name": block_name,
            "source_heading": heading["text"],
            "level": heading["level"],
            "line": heading["line"],
        })

    # Compute compression metrics
    # SN skeleton word count estimate (header + block stubs)
    sn_lines = []
    sn_lines.append("---")
    for k, v in sn_header.items():
        sn_lines.append(f"{k}: {v}")
    sn_lines.append("---")
    sn_lines.append("")
    sn_lines.append(f"# {_compress_id(fid)}: {sn_header.get('name', fid)} (SN)")
    sn_lines.append("")

    for block in blocks:
        indent = "    "
        sn_lines.append(f"{block['type']} {block['name']}:")
        sn_lines.append(f'{indent}sutra: "← compress {block["source_heading"]}"')
        sn_lines.append(f"{indent}gloss:")
        sn_lines.append(f"{indent}    ← semantic compression required")
        sn_lines.append("end")
        sn_lines.append("")

    sn_text = "\n".join(sn_lines)
    sn_words = len(sn_text.split())
    original_words = body.get("word_count", 1) or 1

    return {
        "id": fid,
        "sn_header": sn_header,
        "blocks": blocks,
        "sn_text": sn_text,
        "metrics": {
            "original_words": original_words,
            "skeleton_words": sn_words,
            "block_count": len(blocks),
            "compression_potential": round(1 - (sn_words / original_words), 2) if original_words > sn_words else 0,
        },
    }


def stage_compress(ir_collection, graph_result=None, output_dir=None):
    """Stage 4: Generate Syncrescript v2 structural skeletons."""
    results = {
        "stage": "compress",
        "timestamp": datetime.now().isoformat(),
        "file_count": 0,
        "total_original_words": 0,
        "total_skeleton_words": 0,
        "total_blocks": 0,
        "files": [],
        "skeletons_written": 0,
    }

    for file_ir in ir_collection["files"]:
        compressed = compress_file_ir(file_ir, graph_result)
        if not compressed:
            continue

        results["file_count"] += 1
        results["total_original_words"] += compressed["metrics"]["original_words"]
        results["total_skeleton_words"] += compressed["metrics"]["skeleton_words"]
        results["total_blocks"] += compressed["metrics"]["block_count"]
        results["files"].append({
            "id": compressed["id"],
            "blocks": compressed["metrics"]["block_count"],
            "original_words": compressed["metrics"]["original_words"],
            "skeleton_words": compressed["metrics"]["skeleton_words"],
        })

        # Write skeleton files if output dir specified
        if output_dir:
            out_path = output_dir / f"{compressed['id']}.sn.md"
            out_path.write_text(compressed["sn_text"], encoding="utf-8")
            results["skeletons_written"] += 1

    # Aggregate metrics
    if results["total_original_words"] > 0:
        results["skeleton_ratio"] = round(
            results["total_skeleton_words"] / results["total_original_words"], 3
        )
        results["avg_blocks_per_file"] = round(
            results["total_blocks"] / max(results["file_count"], 1), 1
        )

    return results


def format_compress_text(compress_result):
    """Human-readable compression report."""
    lines = []
    lines.append("Canon Compiler — Compression Report (Stage 4)")
    lines.append("=" * 60)
    lines.append(f"Files processed:   {compress_result['file_count']}")
    lines.append(f"Total blocks:      {compress_result['total_blocks']}")
    lines.append(f"Avg blocks/file:   {compress_result.get('avg_blocks_per_file', 0)}")
    lines.append(f"Original words:    {compress_result['total_original_words']:,}")
    lines.append(f"Skeleton words:    {compress_result['total_skeleton_words']:,}")
    lines.append(f"Skeleton ratio:    {compress_result.get('skeleton_ratio', 0):.1%}")
    lines.append(f"Skeletons written: {compress_result['skeletons_written']}")

    if compress_result["skeletons_written"] > 0:
        lines.append(f"\n✓ SN v2 skeletons emitted. Semantic compression pending (V-4 PoC).")
    else:
        lines.append(f"\nℹ Dry run — use --sn-out <dir> to write skeleton files.")

    # Top 10 largest files
    sorted_files = sorted(compress_result["files"], key=lambda f: f["original_words"], reverse=True)
    lines.append(f"\nLargest files (compression priority):")
    for f in sorted_files[:10]:
        lines.append(f"  {f['id']:40s}  {f['original_words']:>6,} words  {f['blocks']:>3} blocks")

    return "\n".join(lines)


# ============================================================
# STAGE 5: EMIT — Render views
# ============================================================

def emit_scripture_view(ir_collection, graph_result, output_path):
    """Scripture View: Human-readable canon overview.

    A single document that a human can read to understand the entire canon
    at a glance — hierarchy, relationships, key entities, health status.
    """
    lines = []
    lines.append("# Canon Scripture — Living Overview")
    lines.append(f"> Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} by Canon Compiler")
    lines.append(f"> 78 files | {graph_result['node_count']} nodes | {graph_result['edge_count']} edges | Max depth {graph_result['max_depth']}")
    lines.append("")

    # Build id→ir lookup
    id_lookup = {}
    for file_ir in ir_collection["files"]:
        fm = file_ir["frontmatter"]
        if fm and "id" in fm:
            id_lookup[str(fm["id"])] = (fm, file_ir)

    # Organize by tier
    tier_order = ["cosmos", "core", "lattice", "chain", "immune", "archive"]
    tier_labels = {
        "cosmos": "COSMOS — Universal Laws",
        "core": "CORE — Structural Primitives",
        "lattice": "LATTICE — Operational Architecture",
        "chain": "CHAIN — Developmental Pathways",
        "immune": "IMMUNE — System Integrity",
        "archive": "ARCHIVE — Historical Record",
    }

    by_tier = {}
    for fid, (fm, file_ir) in id_lookup.items():
        tier = str(fm.get("tier", "")).lower()
        by_tier.setdefault(tier, []).append((fid, fm, file_ir))

    for tier in tier_order:
        items = by_tier.get(tier, [])
        if not items:
            continue
        lines.append(f"## {tier_labels.get(tier, tier.upper())}")
        lines.append("")

        # Sort by ID
        for fid, fm, file_ir in sorted(items, key=lambda x: x[0]):
            name = fm.get("canonical_name", fm.get("title", fid))
            vb = fm.get("volatility_band", "")
            ct = fm.get("celestial_type", "")
            parent = fm.get("parent", "")
            words = file_ir["body"].get("word_count", 0)
            entities = fm.get("entities_defined", [])

            # Volatility indicator
            vb_icon = {"permanent": "●", "stable": "◐", "moderate": "◑", "dynamic": "○"}.get(vb, "?")

            line = f"- **{fid}** — {name} `{ct}` {vb_icon}"
            if parent and str(parent) != "null" and str(parent) != fid:
                line += f" ← {parent}"
            line += f" ({words:,} words)"
            lines.append(line)

            # Key entities
            if entities:
                ent_str = ", ".join(str(e) for e in entities[:5])
                if len(entities) > 5:
                    ent_str += f" +{len(entities)-5} more"
                lines.append(f"  Entities: {ent_str}")

        lines.append("")

    # Legend
    lines.append("---")
    lines.append("**Volatility**: ● permanent | ◐ stable | ◑ moderate | ○ dynamic")
    lines.append("")

    text = "\n".join(lines)
    Path(output_path).write_text(text, encoding="utf-8")
    return len(lines)


def emit_config_view(ir_collection, graph_result, output_path):
    """Config View: Machine-readable canon manifest for agent consumption.

    JSON document containing all structural data an agent needs to navigate
    and reason about the canon without reading individual files.
    """
    config = {
        "canon_config_version": "2.0",
        "generated": datetime.now().isoformat(),
        "stats": {
            "file_count": ir_collection["file_count"],
            "node_count": graph_result["node_count"],
            "edge_count": graph_result["edge_count"],
            "max_depth": graph_result["max_depth"],
            "components": graph_result["connected_components"],
            "has_cycles": graph_result["has_cycle"],
        },
        "tier_distribution": graph_result["tier_distribution"],
        "roots": graph_result["roots"],
        "leaves": graph_result["leaves"],
        "topo_order": graph_result["topo_order"],
        "files": {},
    }

    for file_ir in ir_collection["files"]:
        fm = file_ir["frontmatter"]
        if not fm or "id" not in fm:
            continue
        fid = str(fm["id"])
        config["files"][fid] = {
            "name": fm.get("canonical_name", fm.get("title", fid)),
            "tier": fm.get("tier"),
            "chain": fm.get("chain"),
            "celestial_type": fm.get("celestial_type"),
            "volatility_band": fm.get("volatility_band"),
            "parent": fm.get("parent"),
            "requires": fm.get("requires", []) or [],
            "siblings": fm.get("siblings", []) or [],
            "synthesizes": fm.get("synthesizes", []) or [],
            "entities": fm.get("entities_defined", []) or [],
            "status": fm.get("status"),
            "operational_status": fm.get("operational_status"),
            "word_count": file_ir["body"].get("word_count", 0),
            "filename": file_ir["filename"],
        }

    text = json.dumps(config, indent=2, default=str)
    Path(output_path).write_text(text, encoding="utf-8")
    return len(config["files"])


def emit_ledger_view(ir_collection, graph_result, output_path):
    """Ledger View: Compact status tracking table."""
    lines = []
    lines.append("# Canon Ledger")
    lines.append(f"> Generated {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")
    lines.append("| ID | Name | Tier | Volatility | Status | Words | Entities |")
    lines.append("|---|---|---|---|---|---|---|")

    for file_ir in sorted(ir_collection["files"], key=lambda f: str(f.get("frontmatter", {}).get("id", ""))):
        fm = file_ir["frontmatter"]
        if not fm or "id" not in fm:
            continue
        fid = str(fm["id"])
        name = str(fm.get("canonical_name", fm.get("title", "")))[:35]
        tier = fm.get("tier", "")
        vb = fm.get("volatility_band", "")
        status = fm.get("operational_status", "")
        words = file_ir["body"].get("word_count", 0)
        ent_count = len(fm.get("entities_defined", []) or [])
        lines.append(f"| {fid} | {name} | {tier} | {vb} | {status} | {words:,} | {ent_count} |")

    lines.append("")
    text = "\n".join(lines)
    Path(output_path).write_text(text, encoding="utf-8")
    return len(lines) - 4  # header lines


def stage_emit(ir_collection, graph_result, output_dir):
    """Stage 5: Emit all views."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    results = {
        "stage": "emit",
        "timestamp": datetime.now().isoformat(),
        "views": {},
    }

    # Scripture view
    scripture_path = output_dir / "CANON-SCRIPTURE.md"
    scripture_lines = emit_scripture_view(ir_collection, graph_result, scripture_path)
    results["views"]["scripture"] = {"path": str(scripture_path), "lines": scripture_lines}

    # Config view
    config_path = output_dir / "CANON-CONFIG.json"
    config_files = emit_config_view(ir_collection, graph_result, config_path)
    results["views"]["config"] = {"path": str(config_path), "files": config_files}

    # Graph view (Mermaid — already generated by stage 3, copy to output)
    graph_path = output_dir / "CANON-GRAPH.mmd"
    if graph_result.get("mermaid"):
        graph_path.write_text(graph_result["mermaid"], encoding="utf-8")
        results["views"]["graph"] = {"path": str(graph_path)}

    # Ledger view
    ledger_path = output_dir / "CANON-LEDGER.md"
    ledger_rows = emit_ledger_view(ir_collection, graph_result, ledger_path)
    results["views"]["ledger"] = {"path": str(ledger_path), "rows": ledger_rows}

    return results


def format_emit_text(emit_result):
    """Human-readable emit report."""
    lines = []
    lines.append("Canon Compiler — Emit Report (Stage 5)")
    lines.append("=" * 60)
    for view_name, info in emit_result["views"].items():
        path = info.get("path", "")
        detail = ""
        if "lines" in info:
            detail = f" ({info['lines']} lines)"
        elif "files" in info:
            detail = f" ({info['files']} files)"
        elif "rows" in info:
            detail = f" ({info['rows']} rows)"
        lines.append(f"  {view_name:12s}: {path}{detail}")
    lines.append(f"\n✓ {len(emit_result['views'])} views emitted.")
    return "\n".join(lines)


# ============================================================
# MUTAGENIC ZONE (M-1 ratified CC49)
# ============================================================

def check_mutagenic_zone():
    """Check mutagenic zone — syntax only, no semantic validation."""
    if not MUTAGENIC_DIR.is_dir():
        return None

    results = {
        "zone": str(MUTAGENIC_DIR),
        "files": 0,
        "syntax_errors": 0,
        "details": [],
    }

    for f in sorted(MUTAGENIC_DIR.glob("*.md")):
        results["files"] += 1
        text = f.read_text(encoding="utf-8")
        match = re.match(r"^---\s*\n(.*?\n)---\s*\n", text, re.DOTALL)
        if match:
            try:
                yaml.safe_load(match.group(1))
            except yaml.YAMLError as e:
                results["syntax_errors"] += 1
                results["details"].append({"file": f.name, "error": str(e)})
        # No semantic validation — this is the mutagenic zone

    return results


# ============================================================
# OUTPUT FORMATTERS
# ============================================================

def format_text(validation, ir_collection):
    """Human-readable output."""
    lines = []
    lines.append("Canon Compiler — Validation Report")
    lines.append("=" * 60)
    lines.append(f"Files scanned:    {validation['total_files']}")
    lines.append(f"S-1 compliant:    {validation['clean_files']}")
    lines.append(f"Errors:           {validation['total_errors']}")
    lines.append(f"Warnings:         {validation['total_warnings']}")
    lines.append(f"Orphans:          {len(validation['orphans'])}")

    hm = validation.get("heatmap", {})
    lines.append(f"\nHeatmap: {hm.get('green',0)} green | {hm.get('yellow',0)} yellow | {hm.get('red',0)} red | {hm.get('grey',0)} grey")

    if validation["results"]:
        lines.append("")
        for fname, issues in sorted(validation["results"].items()):
            lines.append(f"  {fname}:")
            for issue in issues:
                marker = "✗" if issue["level"] == "ERROR" else "⚠"
                lines.append(f"    {marker} [{issue['level']}] {issue['message']}")
            lines.append("")

    if validation["orphans"]:
        lines.append("  Orphans (no inbound refs):")
        for o in sorted(validation["orphans"]):
            lines.append(f"    - {o}")
        lines.append("")

    if validation["total_errors"] == 0:
        lines.append("✓ Canon compilation PASSED. No errors.")
    else:
        lines.append(f"✗ Canon compilation FAILED. {validation['total_errors']} errors.")

    return "\n".join(lines)


# ============================================================
# MAIN
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="Canon Compiler (5-stage pipeline)")
    parser.add_argument("stage", nargs="?", default="validate",
                        choices=["parse", "validate", "graph", "compress", "emit", "compile"],
                        help="Which stage(s) to run")
    parser.add_argument("--out", help="Write IR/results to file")
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument("--strict", action="store_true", help="Warnings = errors")
    parser.add_argument("--mermaid", help="Write Mermaid diagram to file (graph/compile stage)")
    parser.add_argument("--sn-out", help="Write SN v2 skeleton files to directory (compress/compile stage)")
    parser.add_argument("--emit-dir", help="Write emitted views to directory (emit/compile stage)",
                        default="corpus/views")
    args = parser.parse_args()

    # Stage 1: Parse
    ir = stage_parse()

    if args.stage == "parse":
        output = json.dumps(ir, indent=2, default=str)
        if args.out:
            Path(args.out).write_text(output)
            print(f"IR written to {args.out} ({ir['file_count']} files)")
        else:
            print(output)
        sys.exit(0)

    # Stage 2: Validate
    validation = stage_validate(ir, strict=args.strict)

    # Check mutagenic zone
    mutagenic = check_mutagenic_zone()
    if mutagenic:
        validation["mutagenic_zone"] = mutagenic

    if args.stage == "validate":
        if args.json:
            output = json.dumps(validation, indent=2, default=str)
            if args.out:
                Path(args.out).write_text(output)
                print(f"Validation written to {args.out}")
            else:
                print(output)
        else:
            print(format_text(validation, ir))
        sys.exit(1 if validation["total_errors"] > 0 else 0)

    # Stage 3: Graph
    graph_result = stage_graph(ir)

    if args.mermaid:
        Path(args.mermaid).write_text(graph_result["mermaid"])
        print(f"Mermaid diagram written to {args.mermaid}")

    if args.stage == "graph":
        if args.json:
            output = json.dumps(graph_result, indent=2, default=str)
            if args.out:
                Path(args.out).write_text(output)
                print(f"Graph written to {args.out}")
            else:
                print(output)
        else:
            print(format_text(validation, ir))
            print()
            print(format_graph_text(graph_result))
        sys.exit(1 if validation["total_errors"] > 0 else 0)

    # Stage 4: Compress
    sn_out_dir = Path(args.sn_out) if args.sn_out else None
    if sn_out_dir:
        sn_out_dir.mkdir(parents=True, exist_ok=True)
    compress_result = stage_compress(ir, graph_result, output_dir=sn_out_dir)

    if args.stage == "compress":
        if args.json:
            output = json.dumps(compress_result, indent=2, default=str)
            if args.out:
                Path(args.out).write_text(output)
                print(f"Compression written to {args.out}")
            else:
                print(output)
        else:
            print(format_text(validation, ir))
            print()
            print(format_compress_text(compress_result))
        sys.exit(1 if validation["total_errors"] > 0 else 0)

    # Stage 5: Emit
    emit_result = stage_emit(ir, graph_result, args.emit_dir)

    if args.stage == "emit":
        if args.json:
            output = json.dumps(emit_result, indent=2, default=str)
            if args.out:
                Path(args.out).write_text(output)
                print(f"Emit results written to {args.out}")
            else:
                print(output)
        else:
            print(format_text(validation, ir))
            print()
            print(format_emit_text(emit_result))
        sys.exit(1 if validation["total_errors"] > 0 else 0)

    # Stage "compile" — all stages
    if args.json:
        combined = {
            "validation": validation, "graph": graph_result,
            "compress": compress_result, "emit": emit_result,
        }
        output = json.dumps(combined, indent=2, default=str)
        if args.out:
            Path(args.out).write_text(output)
            print(f"Compilation written to {args.out}")
        else:
            print(output)
    else:
        print(format_text(validation, ir))
        print()
        print(format_graph_text(graph_result))
        print()
        print(format_compress_text(compress_result))
        print()
        print(format_emit_text(emit_result))

    sys.exit(1 if validation["total_errors"] > 0 else 0)


if __name__ == "__main__":
    main()
