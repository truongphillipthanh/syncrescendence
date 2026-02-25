#!/usr/bin/env python3
"""Ontology maintenance operations — IMPL-C-0014 (SYN-22).

Scheduled maintenance cadence for keeping the ontology substrate current:
  - refresh: Update model pricing, check for stale records (weekly)
  - audit: Full integrity audit with coverage report (monthly)
  - report: Generate maintenance status report

Usage:
    python3 ontology_maintain.py refresh    # Weekly: stale detection + pricing flags
    python3 ontology_maintain.py audit      # Monthly: full integrity + coverage gaps
    python3 ontology_maintain.py report     # Status report for dashboards
"""
from config import *

import sqlite3
import sys
import os
import datetime

DB_PATH = os.path.expanduser("~/.syncrescendence/ontology.db")


def cmd_refresh():
    """Weekly refresh: detect stale records, flag pricing gaps, check consistency."""
    db = sqlite3.connect(DB_PATH)
    print("=== ONTOLOGY WEEKLY REFRESH ===")
    print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()

    # 1. Models without pricing data
    no_price = db.execute("""
        SELECT m.name, m.api_name FROM models m
        LEFT JOIN api_pricing ap ON ap.model_id = m.id
        WHERE ap.id IS NULL
    """).fetchall()
    if no_price:
        print(f"Models without pricing ({len(no_price)}):")
        for m in no_price:
            print(f"  - {m[0]} ({m[1]})")
    else:
        print("All models have pricing data.")
    print()

    # 2. Apps without layer assignment
    no_layer = db.execute("""
        SELECT name, slug FROM apps WHERE layer_id IS NULL
    """).fetchall()
    if no_layer:
        print(f"Apps without layer assignment ({len(no_layer)}):")
        for a in no_layer[:10]:
            print(f"  - {a[0]} ({a[1]})")
        if len(no_layer) > 10:
            print(f"  ... and {len(no_layer) - 10} more")
    else:
        print("All apps have layer assignments.")
    print()

    # 3. Commitments status check
    active = db.execute("SELECT COUNT(*) FROM commitments WHERE status='active'").fetchone()[0]
    failed = db.execute("SELECT COUNT(*) FROM commitments WHERE status='failed'").fetchone()[0]
    achieved = db.execute("SELECT COUNT(*) FROM commitments WHERE status='achieved'").fetchone()[0]
    print(f"Commitments: {active} active, {achieved} achieved, {failed} failed")

    # 4. Risks needing attention (high probability + high+ impact)
    hot_risks = db.execute("""
        SELECT code, name, probability, impact FROM risks
        WHERE probability IN ('high', 'certain')
        AND impact IN ('high', 'critical', 'catastrophic')
        ORDER BY
            CASE impact WHEN 'catastrophic' THEN 0 WHEN 'critical' THEN 1 WHEN 'high' THEN 2 ELSE 3 END
    """).fetchall()
    if hot_risks:
        print(f"\nHot risks ({len(hot_risks)}):")
        for r in hot_risks:
            print(f"  {r[0]}: {r[1]} ({r[2]}/{r[3]})")
    print()

    # 5. Strategic relationship gaps
    entities_with_no_rels = db.execute("""
        SELECT code FROM commitments WHERE code NOT IN (
            SELECT entity_a FROM strategic_relationships
            UNION SELECT entity_b FROM strategic_relationships
        )
    """).fetchall()
    if entities_with_no_rels:
        print(f"Commitments with no relationships ({len(entities_with_no_rels)}):")
        for e in entities_with_no_rels:
            print(f"  - {e[0]}")

    db.close()
    print("\n[Refresh complete]")


def cmd_audit():
    """Monthly audit: comprehensive integrity + coverage analysis."""
    db = sqlite3.connect(DB_PATH)
    print("=== ONTOLOGY MONTHLY AUDIT ===")
    print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()

    # Schema metadata
    meta = dict(db.execute("SELECT key, value FROM _meta").fetchall())
    print(f"Schema: v{meta.get('schema_version', '?')}")
    print(f"Build: {meta.get('build_timestamp', '?')}")
    print()

    # Table-by-table coverage
    tables = db.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' AND name != '_meta' ORDER BY name"
    ).fetchall()

    print(f"{'Table':<30} {'Rows':>6}  {'Status'}")
    print("-" * 50)

    total = 0
    empty_count = 0
    for (t,) in tables:
        try:
            count = db.execute(f"SELECT COUNT(*) FROM [{t}]").fetchone()[0]
            total += count
            status = "OK" if count > 0 else "EMPTY"
            if count == 0:
                empty_count += 1
            print(f"  {t:<28} {count:>6}  {status}")
        except Exception as e:
            print(f"  {t:<28} {'?':>6}  ERROR: {e}")

    print("-" * 50)
    print(f"  {'TOTAL':<28} {total:>6}")
    print(f"  Populated: {len(tables) - empty_count}/{len(tables)} tables")
    print()

    # FK integrity
    fk_violations = db.execute("PRAGMA foreign_key_check").fetchall()
    print(f"FK violations: {len(fk_violations)}")

    # Full integrity
    integrity = db.execute("PRAGMA integrity_check").fetchone()[0]
    print(f"Integrity: {integrity}")
    print()

    # Strategic layer health
    print("=== Strategic Layer Health ===")
    strategic = {
        "commitments": db.execute("SELECT COUNT(*) FROM commitments").fetchone()[0],
        "goals": db.execute("SELECT COUNT(*) FROM goals").fetchone()[0],
        "risks": db.execute("SELECT COUNT(*) FROM risks").fetchone()[0],
        "resources": db.execute("SELECT COUNT(*) FROM resources").fetchone()[0],
        "environments": db.execute("SELECT COUNT(*) FROM environments").fetchone()[0],
        "governed_verbs": db.execute("SELECT COUNT(*) FROM governed_verbs").fetchone()[0],
        "strategic_relationships": db.execute("SELECT COUNT(*) FROM strategic_relationships").fetchone()[0],
    }
    for table, count in strategic.items():
        print(f"  {table}: {count}")
    print(f"  Total strategic: {sum(strategic.values())}")
    print()

    # Coverage gaps
    print("=== Coverage Gaps ===")

    # Goals without linked commitments
    orphan_goals = db.execute("""
        SELECT code, name FROM goals WHERE code NOT IN (
            SELECT entity_b FROM strategic_relationships WHERE relationship_type IN ('supports', 'enables', 'contributes_to', 'implements')
        )
    """).fetchall()
    if orphan_goals:
        print(f"Goals with no supporting commitment ({len(orphan_goals)}):")
        for g in orphan_goals:
            print(f"  - {g[0]}: {g[1]}")

    # Risks without mitigation relationships
    unmitigated = db.execute("""
        SELECT code, name FROM risks WHERE code NOT IN (
            SELECT entity_a FROM strategic_relationships WHERE relationship_type IN ('mitigates', 'resolves')
            UNION SELECT entity_b FROM strategic_relationships WHERE relationship_type IN ('mitigates', 'resolves')
        )
    """).fetchall()
    if unmitigated:
        print(f"\nRisks with no mitigation relationship ({len(unmitigated)}):")
        for r in unmitigated:
            print(f"  - {r[0]}: {r[1]}")

    db.close()
    print("\n[Audit complete]")


def cmd_report():
    """Generate compact status report suitable for dashboards."""
    db = sqlite3.connect(DB_PATH)
    meta = dict(db.execute("SELECT key, value FROM _meta").fetchall())

    tables = db.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' AND name != '_meta'"
    ).fetchall()

    total = 0
    for (t,) in tables:
        try:
            total += db.execute(f"SELECT COUNT(*) FROM [{t}]").fetchone()[0]
        except Exception:
            pass

    strategic = sum([
        db.execute("SELECT COUNT(*) FROM commitments").fetchone()[0],
        db.execute("SELECT COUNT(*) FROM goals").fetchone()[0],
        db.execute("SELECT COUNT(*) FROM risks").fetchone()[0],
        db.execute("SELECT COUNT(*) FROM resources").fetchone()[0],
        db.execute("SELECT COUNT(*) FROM environments").fetchone()[0],
        db.execute("SELECT COUNT(*) FROM governed_verbs").fetchone()[0],
        db.execute("SELECT COUNT(*) FROM strategic_relationships").fetchone()[0],
    ])

    fk = len(db.execute("PRAGMA foreign_key_check").fetchall())
    integrity = db.execute("PRAGMA integrity_check").fetchone()[0]

    print(f"ontology v{meta.get('schema_version', '?')} | "
          f"{len(tables)} tables | "
          f"{total} rows | "
          f"{strategic} strategic | "
          f"FK:{fk} | "
          f"integrity:{integrity}")

    db.close()


COMMANDS = {
    "refresh": cmd_refresh,
    "audit": cmd_audit,
    "report": cmd_report,
}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print("Usage: python3 ontology_maintain.py {refresh|audit|report}")
        print("  refresh  — Weekly: stale detection, pricing flags, consistency")
        print("  audit    — Monthly: full integrity, coverage gaps, health report")
        print("  report   — One-line status for dashboards")
        sys.exit(1)

    COMMANDS[sys.argv[1]]()
