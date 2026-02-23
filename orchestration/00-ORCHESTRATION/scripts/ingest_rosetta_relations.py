#!/usr/bin/env python3
"""
ingest_rosetta_relations.py — Parse ARCH-ROSETTA_ONTOLOGY_BRIDGE.md
and ingest 200+ typed relations into the ontology SQLite database.

Targets the strategic_relationships table with schema:
  (code, entity_a, entity_a_type, entity_b, entity_b_type,
   relationship_type, strength, context, notes)

Usage:
    python3 ingest_rosetta_relations.py [--db-path PATH] [--bridge-path PATH] [--dry-run]
"""

import os
import re
import sqlite3
import sys
from pathlib import Path

DEFAULT_DB_PATH = os.environ.get(
    "ONTOLOGY_DB",
    os.path.expanduser("~/Desktop/syncrescendence/orchestration/state/ontology.db"),
)
DEFAULT_BRIDGE_PATH = os.path.expanduser(
    "~/Desktop/syncrescendence/orchestration/state/ARCH-ROSETTA_ONTOLOGY_BRIDGE.md"
)

# Entity type code mapping (Bridge codes → lowercase for DB consistency)
TYPE_MAP = {
    "CON": "concept",
    "CAP": "capability",
    "TOOL": "tool",
    "AGT": "agent",
    "WF": "workflow",
    "ART": "artifact",
    "PROTO": "protocol",
    "NOT": "notation",
    "MET": "metric",
    "STR": "structure",
}

# Default strength by relation type (higher = stronger coupling)
STRENGTH_DEFAULTS = {
    "governed_by": 9,
    "part_of": 8,
    "contains": 8,
    "uses": 7,
    "provides": 8,
    "enables": 7,
    "produces": 7,
    "evaluates": 6,
    "alias_of": 5,
    "replaces": 6,
    "requires": 8,
    "maps_to": 6,
    "governs": 9,
    "connects": 6,
    "models": 6,
    "tracks": 6,
    "from": 5,
    "encodes": 7,
    "supports": 7,
    "threatens": 7,
    "mitigates": 7,
    "resolves": 8,
    "drives": 8,
    "implements": 9,
    "contributes_to": 6,
    "blocks": 9,
    "constrains": 7,
    "invalidates": 9,
    "hosts": 9,
    "unblocks": 7,
    "aspires_to": 5,
}


def parse_expanded_relations(bridge_path: str) -> list[dict]:
    """Parse the EXPANDED RELATION TABLE sections from the bridge document."""
    with open(bridge_path, "r") as f:
        content = f.read()

    # Find the EXPANDED RELATION TABLE section
    marker = "## EXPANDED RELATION TABLE"
    idx = content.find(marker)
    if idx == -1:
        print(f"ERROR: Could not find '{marker}' in {bridge_path}")
        sys.exit(1)

    # Extract from marker to next ## or end
    section = content[idx:]
    # Cut at the next major section that isn't a ### subsection
    next_h2 = re.search(r'\n## [^#]', section[len(marker):])
    if next_h2:
        section = section[:len(marker) + next_h2.start()]

    relations = []

    # Parse markdown tables: | From | Relation | To | Evidence |
    # Each table row looks like:
    #   | CANON (STR) | governed_by | Five Invariants (CON) | CANON-00003, CLAUDE.md |
    table_row_re = re.compile(
        r'^\|\s*(.+?)\s*\|\s*(\w+)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|$',
        re.MULTILINE,
    )

    for match in table_row_re.finditer(section):
        from_col = match.group(1).strip()
        relation = match.group(2).strip()
        to_col = match.group(3).strip()
        evidence = match.group(4).strip()

        # Skip header rows
        if from_col in ("From", "---", "------") or relation in ("Relation", "---"):
            continue
        if from_col.startswith("-") or to_col.startswith("-"):
            continue

        # Parse entity: "Name (TYPE)" or just "Name"
        entity_a, type_a = parse_entity(from_col)
        entity_b, type_b = parse_entity(to_col)

        if not entity_a or not entity_b:
            continue

        relations.append({
            "entity_a": entity_a,
            "entity_a_type": type_a,
            "entity_b": entity_b,
            "entity_b_type": type_b,
            "relationship_type": relation,
            "evidence": evidence,
        })

    return relations


def parse_entity_relations(bridge_path: str) -> list[dict]:
    """Parse inline relations from the ENTITY CLASSIFICATION tables.

    These tables have format:
    | # | Term | Entity Type | Relations |
    | 19 | CANON | STR | `governed_by` Five Invariants; `part_of` Repository |
    """
    with open(bridge_path, "r") as f:
        content = f.read()

    # Find ENTITY CLASSIFICATION section
    marker = "## ENTITY CLASSIFICATION"
    end_marker = "## KEY RELATION CLUSTERS"
    idx = content.find(marker)
    end_idx = content.find(end_marker)
    if idx == -1:
        return []

    section = content[idx:end_idx] if end_idx != -1 else content[idx:]
    relations = []

    # Parse rows: | # | Term | Entity Type | Relations |
    row_re = re.compile(
        r'^\|\s*(\d+\w*)\s*\|\s*(.+?)\s*\|\s*(\w+)\s*\|\s*(.+?)\s*\|$',
        re.MULTILINE,
    )

    for match in row_re.finditer(section):
        term = match.group(2).strip()
        entity_type = match.group(3).strip()
        relations_col = match.group(4).strip()

        # Parse inline relations: `relation_type` Target; `relation_type` Target
        inline_re = re.compile(r'`(\w+)`\s+([^;`]+)')
        for rel_match in inline_re.finditer(relations_col):
            rel_type = rel_match.group(1).strip()
            target = rel_match.group(2).strip().rstrip(';').strip()

            # Skip very generic targets
            if not target or target in ("—", "neutral"):
                continue

            relations.append({
                "entity_a": term,
                "entity_a_type": TYPE_MAP.get(entity_type, entity_type.lower()),
                "entity_b": target,
                "entity_b_type": "unknown",  # Will be resolved if found in expanded table
                "relationship_type": rel_type,
                "evidence": f"Rosetta entity classification",
            })

    return relations


def parse_entity(text: str) -> tuple[str, str]:
    """Parse 'Name (TYPE)' into (name, type_lowercase)."""
    # Match "Entity Name (TYPE_CODE)"
    m = re.match(r'^(.+?)\s*\((\w+)\)\s*$', text)
    if m:
        name = m.group(1).strip()
        type_code = m.group(2).strip()
        return name, TYPE_MAP.get(type_code, type_code.lower())

    # No type annotation — return as-is with unknown type
    return text.strip(), "unknown"


def deduplicate(relations: list[dict]) -> list[dict]:
    """Remove duplicate relations based on (entity_a, relation, entity_b)."""
    seen = set()
    unique = []
    for r in relations:
        key = (
            r["entity_a"].lower(),
            r["relationship_type"].lower(),
            r["entity_b"].lower(),
        )
        if key not in seen:
            seen.add(key)
            unique.append(r)
    return unique


def ingest(db_path: str, bridge_path: str, dry_run: bool = False):
    """Main ingestion pipeline."""
    print(f"=== ROSETTA RELATION INGESTION ===\n")
    print(f"  Bridge: {bridge_path}")
    print(f"  DB:     {db_path}")
    print(f"  Mode:   {'DRY RUN' if dry_run else 'LIVE'}\n")

    if not os.path.exists(bridge_path):
        print(f"ERROR: Bridge file not found: {bridge_path}")
        sys.exit(1)

    if not os.path.exists(db_path):
        print(f"ERROR: Database not found: {db_path}")
        print("Run build_ontology_db.py first.")
        sys.exit(1)

    # Parse expanded relation tables (primary source — 200+ relations)
    expanded = parse_expanded_relations(bridge_path)
    print(f"  Parsed {len(expanded)} relations from EXPANDED RELATION TABLE")

    # Parse inline entity relations (secondary source — fills gaps)
    inline = parse_entity_relations(bridge_path)
    print(f"  Parsed {len(inline)} inline relations from ENTITY CLASSIFICATION")

    # Merge and deduplicate (expanded takes priority)
    all_relations = expanded + inline
    unique = deduplicate(all_relations)
    print(f"  After deduplication: {unique.__len__()} unique relations\n")

    if dry_run:
        print("--- DRY RUN: First 20 relations ---")
        for i, r in enumerate(unique[:20]):
            print(f"  {i+1:3d}. {r['entity_a']} ({r['entity_a_type']}) "
                  f"--[{r['relationship_type']}]--> "
                  f"{r['entity_b']} ({r['entity_b_type']})")
        print(f"\n  ... and {len(unique) - 20} more")
        return

    # Connect to DB and find next REL code
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Find max existing REL code
    cur.execute(
        "SELECT code FROM strategic_relationships WHERE code LIKE 'REL-%' ORDER BY code DESC LIMIT 1"
    )
    row = cur.fetchone()
    if row:
        last_num = int(row[0].split("-")[1])
    else:
        last_num = 0

    next_num = last_num + 1
    inserted = 0
    skipped = 0

    for r in unique:
        code = f"REL-{next_num:03d}"
        strength = STRENGTH_DEFAULTS.get(r["relationship_type"], 5)
        context = f"{r['entity_a']} → {r['entity_b']}"

        try:
            cur.execute(
                "INSERT OR IGNORE INTO strategic_relationships "
                "(code, entity_a, entity_a_type, entity_b, entity_b_type, "
                "relationship_type, strength, context, notes) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    code,
                    r["entity_a"],
                    r["entity_a_type"],
                    r["entity_b"],
                    r["entity_b_type"],
                    r["relationship_type"],
                    strength,
                    context,
                    r["evidence"],
                ),
            )
            if cur.rowcount > 0:
                inserted += 1
                next_num += 1
            else:
                skipped += 1
        except sqlite3.IntegrityError as e:
            skipped += 1

    conn.commit()

    # Report
    total = cur.execute("SELECT COUNT(*) FROM strategic_relationships").fetchone()[0]
    conn.close()

    print(f"=== INGESTION COMPLETE ===")
    print(f"  Inserted: {inserted}")
    print(f"  Skipped (duplicates): {skipped}")
    print(f"  Total strategic_relationships: {total}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Ingest Rosetta Bridge relations into ontology DB"
    )
    parser.add_argument("--db-path", default=DEFAULT_DB_PATH)
    parser.add_argument("--bridge-path", default=DEFAULT_BRIDGE_PATH)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    ingest(args.db_path, args.bridge_path, args.dry_run)
