#!/usr/bin/env python3
"""Canon S-1 Frontmatter Migration — Batch upgrade to ratified schema (CC49).

Reads existing frontmatter, infers new S-1 fields, and writes upgraded YAML.
Splits `depends_on` into `requires`/`siblings`/`synthesizes` with heuristics,
flagging ambiguous cases for sovereign review.

Usage:
    python3 corpus/canon_frontmatter_migrate.py --dry-run   # default, report only
    python3 corpus/canon_frontmatter_migrate.py --execute    # write changes
    python3 corpus/canon_frontmatter_migrate.py --review     # show sovereign review queue
"""

import sys
import os
import re
import yaml
import json
import argparse
import copy
from pathlib import Path
from datetime import date

CANON_DIR = Path(__file__).parent.parent / "canon"

# === Inference Maps ===

# ID range → chain mapping
CHAIN_MAP = {
    range(30000, 31000): "intelligence",
    range(31000, 32000): "information",
    range(32000, 33000): "insight",
    range(33000, 34000): "expertise",
    range(34000, 35000): "knowledge",
    range(35000, 36000): "wisdom",
}

# Existing type → celestial_type mapping
TYPE_TO_CELESTIAL = {
    "cosmos": "root",
    "core": "planetary",
    "lattice": "planetary",
    "planetary": "planetary",
    "ring": "ring",
    "lunar": "lunar",
    "comet": "comet",
    "asteroid": "asteroid",
    "satellite": "satellite",
    "policy": "policy",
    "meta": "meta",
}

# Celestial type → volatility band
CELESTIAL_TO_VOLATILITY = {
    "root": "permanent",
    "planetary": "stable",
    "ring": "stable",
    "lunar": "moderate",
    "comet": "dynamic",
    "asteroid": "dynamic",
    "satellite": "moderate",
    "policy": "stable",
    "meta": "moderate",
}

# Volatility → refresh cadence
VOLATILITY_TO_REFRESH = {
    "permanent": "annual",
    "stable": "semi-annual",
    "moderate": "quarterly",
    "dynamic": "monthly",
}

# ID range → tier (overrides for non-chain files)
TIER_MAP_OVERRIDES = {
    range(0, 100): "cosmos",
    range(10000, 12000): "core",
    range(20000, 26000): "lattice",
    range(99000, 100000): "archive",
}

# Chain root IDs (these are chain-level, not their children)
CHAIN_ROOTS = {30000, 31000, 32000, 33000, 34000, 35000}

# Element mapping by chain
CHAIN_TO_ELEMENT = {
    "intelligence": "quintessence",
    "information": "air",
    "insight": "water",
    "expertise": "fire",
    "knowledge": "earth",
    "wisdom": "quintessence",
}

# OODA mapping by chain
CHAIN_TO_OODA = {
    "information": "observe",
    "insight": "orient",
    "expertise": "decide",
    "knowledge": "act",
    "wisdom": "sharpen",
    "intelligence": None,
}


def parse_frontmatter(filepath):
    """Extract YAML frontmatter and body from a markdown file."""
    text = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?\n)---\s*\n", text, re.DOTALL)
    if not match:
        return None, text, text
    try:
        fm = yaml.safe_load(match.group(1))
        body = text[match.end():]
        return fm if isinstance(fm, dict) else None, body, text
    except yaml.YAMLError:
        return None, text, text


def extract_id_num(canon_id):
    """Extract numeric part from CANON-XXXXX id."""
    if not canon_id:
        return None
    m = re.search(r"(\d{4,5})", str(canon_id))
    return int(m.group(1)) if m else None


def infer_chain(id_num):
    """Infer chain from ID number."""
    if id_num is None:
        return None
    for r, chain in CHAIN_MAP.items():
        if id_num in r:
            return chain
    return None


def infer_tier(id_num, existing_type):
    """Infer tier from ID and existing type."""
    if id_num is None:
        return "chain"
    for r, tier in TIER_MAP_OVERRIDES.items():
        if id_num in r:
            return tier
    # Chain files
    if 30000 <= id_num < 36000:
        return "chain"
    return "chain"


def infer_parent(id_num, depends_on):
    """Infer structural parent from ID hierarchy and depends_on."""
    if id_num is None:
        return None
    # For X0000 files, parent is CANON-00000 (schema root)
    if id_num > 0 and id_num % 10000 == 0:
        return "CANON-00000"
    # For XYYY0 files, parent is X0000
    if id_num > 0 and id_num % 1000 == 0:
        base = (id_num // 10000) * 10000
        return f"CANON-{base:05d}"
    # For XYYYZ files, parent is XYY00 or XYYY0
    if id_num > 0 and id_num % 100 == 0:
        base = (id_num // 1000) * 1000
        return f"CANON-{base:05d}"
    if id_num > 0 and id_num % 10 == 0:
        base = (id_num // 100) * 100
        return f"CANON-{base:05d}"
    # Leaf nodes
    base = (id_num // 10) * 10
    return f"CANON-{base:05d}"


def split_depends_on(depends_on, id_num):
    """Split depends_on into requires/siblings/synthesizes with heuristics.

    Heuristic:
    - If dep is a parent/ancestor (shorter ID prefix) → requires
    - If dep is at same level (same prefix length) → siblings
    - If dep is a child/descendant (longer ID prefix) → synthesizes
    - Cross-chain refs → requires (they provide external context)
    - Ambiguous cases → flagged for sovereign review
    """
    if not depends_on:
        return [], [], [], []

    requires = []
    siblings = []
    synthesizes = []
    ambiguous = []

    if isinstance(depends_on, str):
        depends_on = [depends_on]

    my_chain = infer_chain(id_num)
    my_depth = len(str(id_num)) if id_num else 0

    for dep in depends_on:
        dep_num = extract_id_num(dep)
        if dep_num is None:
            ambiguous.append(dep)
            continue

        dep_chain = infer_chain(dep_num)

        # Cross-chain → requires (external dependency)
        if dep_chain and my_chain and dep_chain != my_chain:
            requires.append(str(dep))
            continue

        # Cosmos/core refs from chain files → requires
        if dep_num < 20000 and id_num and id_num >= 20000:
            requires.append(str(dep))
            continue

        # Parent/ancestor detection: dep is a prefix of our ID
        if id_num and dep_num and dep_num < id_num:
            # Is it an ancestor? (e.g., 31000 is ancestor of 31100)
            dep_str = str(dep_num)
            id_str = str(id_num)
            if id_str.startswith(dep_str.rstrip('0')) or dep_num == (id_num // 1000) * 1000 or dep_num == (id_num // 100) * 100:
                requires.append(str(dep))
                continue

        # Child/descendant: dep ID starts with our prefix
        if id_num and dep_num and dep_num > id_num:
            id_prefix = str(id_num).rstrip('0')
            dep_prefix = str(dep_num)
            if dep_prefix.startswith(id_prefix):
                synthesizes.append(str(dep))
                continue

        # Same-level peers
        if id_num and dep_num:
            my_parent = (id_num // 100) * 100
            dep_parent = (dep_num // 100) * 100
            if my_parent == dep_parent and dep_num != id_num:
                siblings.append(str(dep))
                continue

        # Anything else is ambiguous
        ambiguous.append(str(dep))

    return requires, siblings, synthesizes, ambiguous


def derive_canonical_name(fm, filepath):
    """Derive canonical_name from existing name field or filename."""
    if fm.get("name"):
        # Strip common prefixes like "Planetary ", "The ", etc.
        name = fm["name"]
        for prefix in ["Planetary ", "The ", "Ring of "]:
            if name.startswith(prefix):
                name = name[len(prefix):]
        return name
    # Fall back to filename parsing
    fname = filepath.stem
    # Remove CANON-XXXXX- prefix and suffixes
    parts = fname.split("-")
    if len(parts) > 2:
        # Skip "CANON" and the number
        meaningful = [p for p in parts[2:] if p.upper() not in {
            "COSMOS", "CORE", "LATTICE", "CHAIN", "PLANETARY",
            "LUNAR", "COMET", "ASTEROID", "SATELLITE", "RING",
            "INFORMATION", "INSIGHT", "EXPERTISE", "KNOWLEDGE", "WISDOM",
            "INTELLIGENCE", "META"
        }]
        if meaningful:
            return " ".join(p.replace("_", " ").title() for p in meaningful)
    return fname


def build_s1_frontmatter(fm, filepath, all_ids):
    """Build S-1 compliant frontmatter from existing data."""
    new_fm = {}

    canon_id = fm.get("id", "")
    id_num = extract_id_num(canon_id)

    # === IDENTITY ===
    new_fm["id"] = str(canon_id)
    new_fm["canonical_name"] = derive_canonical_name(fm, filepath)
    new_fm["title"] = fm.get("name", fm.get("identity", derive_canonical_name(fm, filepath)))

    # === CLASSIFICATION ===
    existing_type = fm.get("type", "")
    new_fm["tier"] = infer_tier(id_num, existing_type).lower()

    chain = fm.get("chain", "").lower() if fm.get("chain") else infer_chain(id_num)
    new_fm["chain"] = chain

    celestial_type = TYPE_TO_CELESTIAL.get(existing_type.lower(), "lunar") if existing_type else "lunar"
    new_fm["celestial_type"] = celestial_type

    volatility_band = CELESTIAL_TO_VOLATILITY.get(celestial_type, "moderate")
    new_fm["volatility_band"] = volatility_band

    new_fm["refresh_cadence"] = VOLATILITY_TO_REFRESH.get(volatility_band, "quarterly")

    # === RELATIONSHIPS ===
    depends_on = fm.get("depends_on", [])
    parent = infer_parent(id_num, depends_on)
    new_fm["parent"] = parent

    requires, siblings_list, synthesizes, ambiguous = split_depends_on(depends_on, id_num)
    new_fm["requires"] = requires if requires else []
    new_fm["siblings"] = siblings_list if siblings_list else []
    new_fm["synthesizes"] = synthesizes if synthesizes else []

    # === STATUS ===
    new_fm["status"] = fm.get("status", "canonical").lower()
    new_fm["operational_status"] = fm.get("operational_status", "partial").lower()
    new_fm["version"] = str(fm.get("version", "1.0.0"))
    new_fm["created"] = str(fm.get("created", date.today().isoformat()))
    new_fm["updated"] = str(fm.get("updated", date.today().isoformat()))
    new_fm["last_verified"] = str(fm.get("last_verified", ""))

    # === METADATA ===
    new_fm["element"] = CHAIN_TO_ELEMENT.get(chain)
    new_fm["ooda_phase"] = CHAIN_TO_OODA.get(chain)
    new_fm["volatile_sections"] = []

    # Carry forward entities_defined if present
    if fm.get("entities_defined"):
        new_fm["entities_defined"] = fm["entities_defined"]

    return new_fm, ambiguous


def generate_bare_frontmatter(filepath):
    """Generate frontmatter for files that have none."""
    fname = filepath.stem

    # Known bare files with manual mappings
    BARE_MAPPINGS = {
        "apoptosis_protocol": {
            "id": "CANON-APOPTOSIS-PROTOCOL",
            "canonical_name": "Apoptosis Protocol",
            "title": "Apoptosis Protocol — 5:1 Nucleosynthesis Ratio",
            "tier": "immune",
            "chain": None,
            "celestial_type": "policy",
            "volatility_band": "stable",
        },
        "retirement_protocol": {
            "id": "CANON-RETIREMENT-PROTOCOL",
            "canonical_name": "Retirement Protocol",
            "title": "Retirement Protocol — Competitive Exclusion with Enforced Pruning",
            "tier": "immune",
            "chain": None,
            "celestial_type": "policy",
            "volatility_band": "stable",
        },
        "CANON-ONTOLOGY-GATE_v1": {
            "id": "CANON-ONTOLOGY-GATE-V1",
            "canonical_name": "Ontology Gate v1",
            "title": "Runtime Contract — Layer 1 Enforcement",
            "tier": "immune",
            "chain": None,
            "celestial_type": "policy",
            "volatility_band": "moderate",
        },
        "CANON-ONTOLOGY-GATE_v2": {
            "id": "CANON-ONTOLOGY-GATE-V2",
            "canonical_name": "Ontology Gate v2",
            "title": "Runtime Contract — Layer 2 Enforcement",
            "tier": "immune",
            "chain": None,
            "celestial_type": "policy",
            "volatility_band": "moderate",
        },
        "CANON-25500-ARCHITECTURE_RATIONALE-lattice": {
            "id": "CANON-25500",
            "canonical_name": "Architecture Rationale",
            "title": "Architecture Rationale — Complete Reconstruction Guide",
            "tier": "lattice",
            "chain": None,
            "celestial_type": "planetary",
            "volatility_band": "stable",
        },
        "CANON-31150-PLATFORM_CAPABILITY_CATALOG": {
            "id": "CANON-31150",
            "canonical_name": "Platform Capability Catalog",
            "title": "Platform Capability Catalog",
            "tier": "chain",
            "chain": "information",
            "celestial_type": "satellite",
            "volatility_band": "dynamic",
        },
    }

    base = BARE_MAPPINGS.get(fname, {})
    if not base:
        base = {
            "id": fname,
            "canonical_name": fname.replace("_", " ").replace("-", " ").title(),
            "title": fname,
            "tier": "chain",
            "chain": None,
            "celestial_type": "lunar",
            "volatility_band": "moderate",
        }

    fm = {
        **base,
        "refresh_cadence": VOLATILITY_TO_REFRESH.get(base.get("volatility_band", "moderate"), "quarterly"),
        "parent": None,
        "requires": [],
        "siblings": [],
        "synthesizes": [],
        "status": "canonical",
        "operational_status": "operational",
        "version": "1.0.0",
        "created": date.today().isoformat(),
        "updated": date.today().isoformat(),
        "last_verified": "",
        "element": CHAIN_TO_ELEMENT.get(base.get("chain")),
        "ooda_phase": CHAIN_TO_OODA.get(base.get("chain")),
        "volatile_sections": [],
    }
    return fm


def write_migrated_file(filepath, new_fm, body):
    """Write file with new S-1 frontmatter, preserving body."""
    # Custom YAML dump for clean output
    lines = ["---"]

    # Identity block
    lines.append(f"id: {new_fm['id']}")
    lines.append(f"canonical_name: {new_fm['canonical_name']}")
    lines.append(f"title: \"{new_fm['title']}\"")
    lines.append("")

    # Classification block
    lines.append(f"tier: {new_fm['tier']}")
    lines.append(f"chain: {new_fm['chain'] or 'null'}")
    lines.append(f"celestial_type: {new_fm['celestial_type']}")
    lines.append(f"volatility_band: {new_fm['volatility_band']}")
    lines.append(f"refresh_cadence: {new_fm['refresh_cadence'] or 'null'}")
    lines.append("")

    # Relationships
    lines.append(f"parent: {new_fm['parent'] or 'null'}")
    if new_fm.get("requires"):
        lines.append("requires:")
        for r in new_fm["requires"]:
            lines.append(f"  - {r}")
    else:
        lines.append("requires: []")
    if new_fm.get("siblings"):
        lines.append("siblings:")
        for s in new_fm["siblings"]:
            lines.append(f"  - {s}")
    else:
        lines.append("siblings: []")
    if new_fm.get("synthesizes"):
        lines.append("synthesizes:")
        for s in new_fm["synthesizes"]:
            lines.append(f"  - {s}")
    else:
        lines.append("synthesizes: []")
    lines.append("")

    # Status
    lines.append(f"status: {new_fm['status']}")
    lines.append(f"operational_status: {new_fm['operational_status']}")
    lines.append(f"version: {new_fm['version']}")
    lines.append(f"created: {new_fm['created']}")
    lines.append(f"updated: {new_fm['updated']}")
    lines.append(f"last_verified: {new_fm.get('last_verified', '')}")
    lines.append("")

    # Metadata
    lines.append(f"element: {new_fm.get('element') or 'null'}")
    lines.append(f"ooda_phase: {new_fm.get('ooda_phase') or 'null'}")
    if new_fm.get("volatile_sections"):
        lines.append("volatile_sections:")
        for v in new_fm["volatile_sections"]:
            lines.append(f"  - {v}")
    else:
        lines.append("volatile_sections: []")

    # Carry forward entities_defined
    if new_fm.get("entities_defined"):
        lines.append("entities_defined:")
        for e in new_fm["entities_defined"]:
            lines.append(f"  - \"{e}\"")

    lines.append("---")

    content = "\n".join(lines) + "\n" + body.lstrip("\n")
    filepath.write_text(content, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Canon S-1 Frontmatter Migration")
    parser.add_argument("--execute", action="store_true", help="Write changes (default: dry-run)")
    parser.add_argument("--review", action="store_true", help="Show sovereign review queue only")
    parser.add_argument("--dry-run", action="store_true", help="Report only (default)")
    args = parser.parse_args()

    if not CANON_DIR.is_dir():
        print(f"ERROR: Canon directory not found: {CANON_DIR}", file=sys.stderr)
        sys.exit(1)

    canon_files = sorted(CANON_DIR.glob("*.md"))
    all_ids = set()
    for f in canon_files:
        fm, body, _ = parse_frontmatter(f)
        if fm and "id" in fm:
            all_ids.add(str(fm["id"]))

    total_migrated = 0
    total_bare = 0
    review_queue = []

    for filepath in canon_files:
        fm, body, full_text = parse_frontmatter(filepath)

        if fm is None:
            # Bare file — needs frontmatter injection
            total_bare += 1
            new_fm = generate_bare_frontmatter(filepath)
            body = full_text  # entire file is body
            ambiguous = []

            if not args.review:
                print(f"  [BARE] {filepath.name} → injecting S-1 frontmatter")
                if args.execute:
                    write_migrated_file(filepath, new_fm, body)
        else:
            # Existing frontmatter — upgrade to S-1
            new_fm, ambiguous = build_s1_frontmatter(fm, filepath, all_ids)

            if not args.review:
                print(f"  [UPGRADE] {filepath.name}")
                if args.execute:
                    write_migrated_file(filepath, new_fm, body)

        total_migrated += 1

        if ambiguous:
            review_queue.append({
                "file": filepath.name,
                "id": new_fm.get("id", "?"),
                "ambiguous_deps": ambiguous,
                "note": "Cannot determine if these are requires/siblings/synthesizes — sovereign must classify"
            })

    print()
    print(f"{'EXECUTED' if args.execute else 'DRY RUN'}: {total_migrated} files processed, {total_bare} bare files")

    if review_queue:
        print(f"\n{'=' * 60}")
        print(f"SOVEREIGN REVIEW QUEUE ({len(review_queue)} files with ambiguous dependencies)")
        print(f"{'=' * 60}")
        for item in review_queue:
            print(f"\n  {item['file']} ({item['id']}):")
            for dep in item['ambiguous_deps']:
                print(f"    ? {dep} → requires / siblings / synthesizes ?")

    if not args.execute and not args.review:
        print(f"\nRun with --execute to write changes.")


if __name__ == "__main__":
    main()
