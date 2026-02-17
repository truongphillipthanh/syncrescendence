#!/usr/bin/env python3
"""Ontology acceptance tests and metrics — IMPL-C-0015 (SYN-22).

Runs a comprehensive verification suite against ontology.db:
  1. Schema integrity (tables, FK constraints, _meta)
  2. Command matrix (all 21 ontology_query.py commands)
  3. Coverage metrics (populated vs empty tables, NULL rates)
  4. Duplicate detection (unique constraint violations)
  5. Query latency benchmarks

Usage:
    python3 ontology_verify.py           # Full suite
    python3 ontology_verify.py --quick   # Schema + commands only
    python3 ontology_verify.py --json    # JSON output for CI

Exit codes: 0 = PASS, 1 = FAIL, 2 = WARN (non-blocking issues)
"""

import sqlite3
import subprocess
import sys
import time
import json
import os

DB_PATH = os.path.expanduser("~/.syncrescendence/ontology.db")
QUERY_SCRIPT = os.path.join(os.path.dirname(__file__), "ontology_query.py")

# Expected schema version and minimum thresholds
EXPECTED_SCHEMA = "1.3.0"
MIN_TABLES = 40
MIN_TOTAL_ROWS = 1000
MIN_STRATEGIC_RECORDS = 100
MAX_NULL_RATE = 0.3  # 30% NULL rate triggers warning

# All 21 commands that must succeed
COMMANDS = [
    "stats", "layers", "apps", "search ontology", "primitives",
    "apparatus", "projects", "tasks", "sources", "actions",
    "agent-bindings", "workflows", "commitments", "goals", "risks",
    "resources", "relationships", "environments", "verbs", "dashboard",
    "sql SELECT 1"
]

results = {"pass": 0, "fail": 0, "warn": 0, "tests": []}


def record(name, status, detail=""):
    results["tests"].append({"name": name, "status": status, "detail": detail})
    results[status] += 1
    icon = {"pass": "+", "fail": "FAIL", "warn": "WARN"}[status]
    if not json_mode:
        print(f"  [{icon}] {name}" + (f" — {detail}" if detail else ""))


def test_schema_integrity():
    """Verify schema version, table count, FK constraints."""
    if not json_mode:
        print("\n=== Schema Integrity ===")

    db = sqlite3.connect(DB_PATH)

    # Schema version
    try:
        ver = db.execute("SELECT value FROM _meta WHERE key='schema_version'").fetchone()[0]
        if ver == EXPECTED_SCHEMA:
            record("schema_version", "pass", f"v{ver}")
        else:
            record("schema_version", "warn", f"v{ver} (expected {EXPECTED_SCHEMA})")
    except Exception as e:
        record("schema_version", "fail", str(e))

    # Table count
    tables = db.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'").fetchone()[0]
    if tables >= MIN_TABLES:
        record("table_count", "pass", f"{tables} tables")
    else:
        record("table_count", "fail", f"{tables} tables (minimum {MIN_TABLES})")

    # Integrity check
    integrity = db.execute("PRAGMA integrity_check").fetchone()[0]
    if integrity == "ok":
        record("integrity_check", "pass")
    else:
        record("integrity_check", "fail", integrity)

    # Foreign key check
    fk_violations = db.execute("PRAGMA foreign_key_check").fetchall()
    if len(fk_violations) == 0:
        record("foreign_key_check", "pass", "0 violations")
    else:
        record("foreign_key_check", "fail", f"{len(fk_violations)} FK violations")

    db.close()


def test_command_matrix():
    """Run all 21 ontology_query.py commands and verify they exit 0."""
    if not json_mode:
        print("\n=== Command Matrix (21 commands) ===")

    for cmd in COMMANDS:
        args = cmd.split()
        start = time.time()
        try:
            result = subprocess.run(
                ["python3", QUERY_SCRIPT] + args,
                capture_output=True, text=True, timeout=30
            )
            elapsed = time.time() - start
            if result.returncode == 0:
                record(f"cmd:{args[0]}", "pass", f"{elapsed:.2f}s")
            else:
                record(f"cmd:{args[0]}", "fail", f"exit {result.returncode}: {result.stderr[:100]}")
        except subprocess.TimeoutExpired:
            record(f"cmd:{args[0]}", "fail", "timeout (30s)")
        except Exception as e:
            record(f"cmd:{args[0]}", "fail", str(e))


def test_coverage_metrics():
    """Measure data coverage: populated tables, NULL rates, row counts."""
    if not json_mode:
        print("\n=== Coverage Metrics ===")

    db = sqlite3.connect(DB_PATH)

    # Total rows
    tables = [r[0] for r in db.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' AND name != '_meta'"
    ).fetchall()]

    total_rows = 0
    empty_tables = []
    for t in tables:
        try:
            count = db.execute(f"SELECT COUNT(*) FROM [{t}]").fetchone()[0]
            total_rows += count
            if count == 0:
                empty_tables.append(t)
        except Exception:
            pass

    if total_rows >= MIN_TOTAL_ROWS:
        record("total_rows", "pass", f"{total_rows} rows across {len(tables)} tables")
    else:
        record("total_rows", "fail", f"{total_rows} rows (minimum {MIN_TOTAL_ROWS})")

    # Empty tables
    if len(empty_tables) == 0:
        record("empty_tables", "pass", "all tables populated")
    elif len(empty_tables) <= 5:
        record("empty_tables", "warn", f"{len(empty_tables)} empty: {', '.join(empty_tables[:5])}")
    else:
        record("empty_tables", "warn", f"{len(empty_tables)} empty tables")

    # Strategic records
    strategic_tables = ["commitments", "goals", "risks", "resources",
                        "environments", "governed_verbs", "strategic_relationships"]
    strategic_count = 0
    for t in strategic_tables:
        try:
            strategic_count += db.execute(f"SELECT COUNT(*) FROM [{t}]").fetchone()[0]
        except Exception:
            pass

    if strategic_count >= MIN_STRATEGIC_RECORDS:
        record("strategic_records", "pass", f"{strategic_count} records")
    else:
        record("strategic_records", "fail", f"{strategic_count} (minimum {MIN_STRATEGIC_RECORDS})")

    # NULL rate on key columns
    null_checks = [
        ("apps", "name"), ("apps", "slug"),
        ("models", "name"), ("models", "api_name"),
        ("commitments", "name"), ("goals", "name"), ("risks", "name"),
    ]
    for table, col in null_checks:
        try:
            total = db.execute(f"SELECT COUNT(*) FROM [{table}]").fetchone()[0]
            if total == 0:
                continue
            nulls = db.execute(f"SELECT COUNT(*) FROM [{table}] WHERE [{col}] IS NULL OR [{col}] = ''").fetchone()[0]
            rate = nulls / total
            if rate == 0:
                record(f"null:{table}.{col}", "pass", "0%")
            elif rate <= MAX_NULL_RATE:
                record(f"null:{table}.{col}", "warn", f"{rate:.0%} NULL ({nulls}/{total})")
            else:
                record(f"null:{table}.{col}", "fail", f"{rate:.0%} NULL ({nulls}/{total})")
        except Exception:
            pass

    db.close()


def test_duplicates():
    """Check for duplicate entries in key unique-constrained columns."""
    if not json_mode:
        print("\n=== Duplicate Detection ===")

    db = sqlite3.connect(DB_PATH)

    unique_checks = [
        ("apps", "slug"), ("models", "api_name"),
        ("commitments", "code"), ("goals", "code"), ("risks", "code"),
        ("resources", "code"), ("environments", "code"),
    ]

    for table, col in unique_checks:
        try:
            dupes = db.execute(f"""
                SELECT [{col}], COUNT(*) FROM [{table}]
                WHERE [{col}] IS NOT NULL AND [{col}] != ''
                GROUP BY [{col}] HAVING COUNT(*) > 1
            """).fetchall()
            if len(dupes) == 0:
                record(f"unique:{table}.{col}", "pass")
            else:
                detail = ", ".join(f"{d[0]}({d[1]})" for d in dupes[:3])
                record(f"unique:{table}.{col}", "fail", f"{len(dupes)} duplicates: {detail}")
        except Exception:
            pass

    db.close()


def test_latency():
    """Benchmark key query latencies."""
    if not json_mode:
        print("\n=== Query Latency ===")

    db = sqlite3.connect(DB_PATH)

    benchmarks = [
        ("full_text_search", "SELECT * FROM apps WHERE name LIKE '%claude%'"),
        ("strategic_join", """
            SELECT c.code, c.name, sr.relationship_type, sr.entity_b
            FROM commitments c
            LEFT JOIN strategic_relationships sr ON sr.entity_a = c.code
        """),
        ("risk_matrix", "SELECT * FROM risks ORDER BY probability, impact"),
        ("agent_bindings", "SELECT agent_code, COUNT(*) FROM agent_bindings GROUP BY agent_code"),
        ("dashboard_meta", "SELECT key, value FROM _meta"),
    ]

    for name, sql in benchmarks:
        start = time.time()
        try:
            rows = db.execute(sql).fetchall()
            elapsed = (time.time() - start) * 1000  # ms
            if elapsed < 100:
                record(f"latency:{name}", "pass", f"{elapsed:.1f}ms ({len(rows)} rows)")
            elif elapsed < 500:
                record(f"latency:{name}", "warn", f"{elapsed:.1f}ms ({len(rows)} rows)")
            else:
                record(f"latency:{name}", "fail", f"{elapsed:.1f}ms (>500ms threshold)")
        except Exception as e:
            record(f"latency:{name}", "fail", str(e))

    db.close()


def print_summary():
    total = results["pass"] + results["fail"] + results["warn"]
    if json_mode:
        print(json.dumps({
            "total": total,
            "pass": results["pass"],
            "fail": results["fail"],
            "warn": results["warn"],
            "verdict": "FAIL" if results["fail"] > 0 else ("WARN" if results["warn"] > 0 else "PASS"),
            "tests": results["tests"]
        }, indent=2))
    else:
        print(f"\n{'='*50}")
        print(f"ONTOLOGY VERIFICATION REPORT")
        print(f"{'='*50}")
        print(f"  Total:  {total}")
        print(f"  Pass:   {results['pass']}")
        print(f"  Fail:   {results['fail']}")
        print(f"  Warn:   {results['warn']}")
        verdict = "FAIL" if results["fail"] > 0 else ("WARN" if results["warn"] > 0 else "PASS")
        print(f"  Verdict: {verdict}")
        print(f"{'='*50}")


if __name__ == "__main__":
    json_mode = "--json" in sys.argv
    quick_mode = "--quick" in sys.argv

    if not os.path.exists(DB_PATH):
        print(f"ERROR: Database not found at {DB_PATH}")
        sys.exit(1)

    if not json_mode:
        print("ONTOLOGY VERIFICATION SUITE")
        print(f"Database: {DB_PATH}")

    test_schema_integrity()
    test_command_matrix()

    if not quick_mode:
        test_coverage_metrics()
        test_duplicates()
        test_latency()

    print_summary()

    if results["fail"] > 0:
        sys.exit(1)
    elif results["warn"] > 0:
        sys.exit(2)
    else:
        sys.exit(0)
