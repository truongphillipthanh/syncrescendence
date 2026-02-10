#!/usr/bin/env python3
"""
ontology_query.py — Navigation interface for the Syncrescendence Ontology DB
Implements the 7 navigation patterns from CANON-30300.

Usage:
    python3 ontology_query.py search "markdown editor"
    python3 ontology_query.py layers
    python3 ontology_query.py apps [--layer L5] [--status active]
    python3 ontology_query.py primitives [CODE]
    python3 ontology_query.py apparatus [CODE]
    python3 ontology_query.py projects [--status active]
    python3 ontology_query.py tasks [--status done] [--project PROJ-001]
    python3 ontology_query.py sources [--chain intelligence]
    python3 ontology_query.py stats
    python3 ontology_query.py sql "SELECT ..."
"""

import os
import sqlite3
import sys
import textwrap

DB_PATH = os.environ.get(
    "ONTOLOGY_DB",
    os.path.expanduser("~/.syncrescendence/ontology.db"),
)


def get_conn():
    if not os.path.exists(DB_PATH):
        print(f"Database not found: {DB_PATH}")
        print("Run build_ontology_db.py first.")
        sys.exit(1)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def cmd_stats(args):
    """Show database statistics."""
    conn = get_conn()
    cur = conn.cursor()

    print("=== ONTOLOGY SUBSTRATE — STATISTICS ===\n")

    sections = {
        "Bedrock": ["layers", "object_types", "commercial_seams", "modalities", "lifecycle_states", "deployment_contexts"],
        "Settlements": ["apps", "models", "api_pricing"],
        "Intelligence": ["primitives", "apparatus", "usage_contexts"],
        "Operational": ["projects", "tasks", "accounts", "platforms", "platform_roles", "sources"],
    }

    grand = 0
    for section, tables in sections.items():
        print(f"  {section}:")
        subtotal = 0
        for t in tables:
            cur.execute(f"SELECT COUNT(*) FROM {t}")
            c = cur.fetchone()[0]
            subtotal += c
            print(f"    {t:28s} {c:>6d}")
        print(f"    {'SUBTOTAL':28s} {subtotal:>6d}")
        grand += subtotal
        print()

    print(f"  {'GRAND TOTAL':30s} {grand:>6d}")

    # Meta
    cur.execute("SELECT key, value FROM _meta ORDER BY key")
    print("\n  Metadata:")
    for row in cur.fetchall():
        print(f"    {row['key']:28s} {row['value']}")

    conn.close()


def cmd_layers(args):
    """List all ASA layers."""
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT code, name, domain, description FROM layers ORDER BY sequence_order")
    print(f"{'Code':<6} {'Name':<28} {'Domain':<12} Description")
    print("-" * 80)
    for row in cur.fetchall():
        print(f"{row['code']:<6} {row['name']:<28} {row['domain']:<12} {row['description'][:40]}")
    conn.close()


def cmd_apps(args):
    """List apps with optional filters."""
    conn = get_conn()
    cur = conn.cursor()

    query = """
        SELECT a.name, a.slug, a.description, a.stage,
               l.code as layer_code, l.name as layer_name,
               ot.asa_code, ls.code as lifecycle
        FROM apps a
        LEFT JOIN layers l ON a.layer_id = l.id
        LEFT JOIN object_types ot ON a.object_type_id = ot.id
        LEFT JOIN lifecycle_states ls ON a.lifecycle_state_id = ls.id
        WHERE 1=1
    """
    params = []

    if "--layer" in args:
        idx = args.index("--layer")
        if idx + 1 < len(args):
            query += " AND l.code = ?"
            params.append(args[idx + 1])

    if "--status" in args:
        idx = args.index("--status")
        if idx + 1 < len(args):
            query += " AND ls.code = ?"
            params.append(args[idx + 1])

    query += " ORDER BY a.name"
    cur.execute(query, params)
    rows = cur.fetchall()

    print(f"{'Name':<35} {'Type':<8} {'Lifecycle':<12} {'Stage':<12} Description")
    print("-" * 100)
    for row in rows:
        desc = (row["description"] or "")[:30]
        print(f"{row['name']:<35} {(row['asa_code'] or '-'):<8} {(row['lifecycle'] or '-'):<12} {(row['stage'] or '-'):<12} {desc}")

    print(f"\n{len(rows)} apps found.")
    conn.close()


def cmd_search(args):
    """Search apps, models, and primitives by keyword."""
    if not args:
        print("Usage: ontology_query.py search <keyword>")
        return

    keyword = " ".join(args)
    conn = get_conn()
    cur = conn.cursor()

    print(f"=== Search: '{keyword}' ===\n")

    # Search apps
    cur.execute(
        "SELECT name, description, stage FROM apps WHERE name LIKE ? OR description LIKE ?",
        (f"%{keyword}%", f"%{keyword}%"),
    )
    apps = cur.fetchall()
    if apps:
        print(f"Apps ({len(apps)}):")
        for a in apps:
            print(f"  - {a['name']}: {(a['description'] or '')[:60]}")
        print()

    # Search primitives
    cur.execute(
        "SELECT code, name, category, description FROM primitives WHERE name LIKE ? OR description LIKE ? OR code LIKE ?",
        (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"),
    )
    prims = cur.fetchall()
    if prims:
        print(f"Primitives ({len(prims)}):")
        for p in prims:
            print(f"  - {p['code']} ({p['category']}): {p['name']}")
        print()

    # Search projects
    cur.execute(
        "SELECT id, name, status, priority FROM projects WHERE name LIKE ? OR notes LIKE ?",
        (f"%{keyword}%", f"%{keyword}%"),
    )
    projs = cur.fetchall()
    if projs:
        print(f"Projects ({len(projs)}):")
        for p in projs:
            print(f"  - {p['id']} [{p['status']}] {p['name']}")
        print()

    # Search sources
    cur.execute(
        "SELECT id, title, platform, chain FROM sources WHERE title LIKE ? OR topics LIKE ?",
        (f"%{keyword}%", f"%{keyword}%"),
    )
    srcs = cur.fetchall()
    if srcs:
        print(f"Sources ({len(srcs)}):")
        for s in srcs:
            print(f"  - {s['id']} [{s['platform']}] {(s['title'] or '')[:60]}")
        print()

    total = len(apps) + len(prims) + len(projs) + len(srcs)
    if total == 0:
        print("No results found.")
    else:
        print(f"Total: {total} results across {sum(1 for x in [apps, prims, projs, srcs] if x)} categories")

    conn.close()


def cmd_primitives(args):
    """List or detail primitives."""
    conn = get_conn()
    cur = conn.cursor()

    if args:
        code = args[0]
        cur.execute("SELECT * FROM primitives WHERE code = ?", (code,))
        row = cur.fetchone()
        if row:
            print(f"Primitive: {row['name']}")
            print(f"  Code: {row['code']}")
            print(f"  Category: {row['category']}")
            print(f"  Description: {row['description']}")
            print(f"  Extractable: {row['extractable']}")
            print(f"  Abstraction: {row['abstraction_level']}")
        else:
            print(f"Primitive '{code}' not found.")
    else:
        cur.execute("SELECT code, name, category, extractable FROM primitives ORDER BY category, code")
        print(f"{'Code':<25} {'Name':<30} {'Category':<15} Extract")
        print("-" * 75)
        for row in cur.fetchall():
            print(f"{row['code']:<25} {row['name']:<30} {row['category']:<15} {'Y' if row['extractable'] else 'N'}")

    conn.close()


def cmd_apparatus(args):
    """List or detail apparatus patterns."""
    conn = get_conn()
    cur = conn.cursor()

    if args:
        code = args[0]
        cur.execute("SELECT * FROM apparatus WHERE code = ?", (code,))
        row = cur.fetchone()
        if row:
            print(f"Apparatus: {row['name']}")
            print(f"  Code: {row['code']}")
            print(f"  Description: {row['description']}")
            print(f"  Emergence: {row['emergence_pattern']}")
            print(f"  Frequency: {row['frequency_score']}/5")
        else:
            print(f"Apparatus '{code}' not found.")
    else:
        cur.execute("SELECT code, name, frequency_score, description FROM apparatus ORDER BY frequency_score DESC")
        print(f"{'Code':<30} {'Name':<35} {'Freq':>4}  Description")
        print("-" * 100)
        for row in cur.fetchall():
            print(f"{row['code']:<30} {row['name']:<35} {row['frequency_score']:>4}  {(row['description'] or '')[:30]}")

    conn.close()


def cmd_projects(args):
    """List projects with optional status filter."""
    conn = get_conn()
    cur = conn.cursor()

    query = "SELECT id, name, status, priority, owner, notes FROM projects WHERE 1=1"
    params = []

    if "--status" in args:
        idx = args.index("--status")
        if idx + 1 < len(args):
            query += " AND status = ?"
            params.append(args[idx + 1])

    query += " ORDER BY id"
    cur.execute(query, params)
    rows = cur.fetchall()

    print(f"{'ID':<18} {'Status':<12} {'Priority':<6} {'Name':<35} Notes")
    print("-" * 110)
    for row in rows:
        notes = (row["notes"] or "")[:40]
        print(f"{row['id']:<18} {(row['status'] or '-'):<12} {(row['priority'] or '-'):<6} {row['name']:<35} {notes}")

    print(f"\n{len(rows)} projects.")
    conn.close()


def cmd_tasks(args):
    """List tasks with optional filters."""
    conn = get_conn()
    cur = conn.cursor()

    query = "SELECT id, project_id, name, status, priority, owner FROM tasks WHERE 1=1"
    params = []

    if "--status" in args:
        idx = args.index("--status")
        if idx + 1 < len(args):
            query += " AND status = ?"
            params.append(args[idx + 1])

    if "--project" in args:
        idx = args.index("--project")
        if idx + 1 < len(args):
            query += " AND project_id = ?"
            params.append(args[idx + 1])

    query += " ORDER BY id"
    cur.execute(query, params)
    rows = cur.fetchall()

    print(f"{'ID':<12} {'Project':<18} {'Status':<12} {'Priority':<6} Name")
    print("-" * 90)
    for row in rows:
        print(f"{row['id']:<12} {(row['project_id'] or '-'):<18} {(row['status'] or '-'):<12} {(row['priority'] or '-'):<6} {row['name'][:40]}")

    print(f"\n{len(rows)} tasks.")
    conn.close()


def cmd_sources(args):
    """List sources with optional chain filter."""
    conn = get_conn()
    cur = conn.cursor()

    query = "SELECT id, title, platform, chain, status, signal_tier FROM sources WHERE 1=1"
    params = []

    if "--chain" in args:
        idx = args.index("--chain")
        if idx + 1 < len(args):
            query += " AND chain = ?"
            params.append(args[idx + 1])

    if "--status" in args:
        idx = args.index("--status")
        if idx + 1 < len(args):
            query += " AND status = ?"
            params.append(args[idx + 1])

    query += " ORDER BY id LIMIT 50"
    cur.execute(query, params)
    rows = cur.fetchall()

    print(f"{'ID':<25} {'Platform':<10} {'Chain':<15} {'Status':<10} Title")
    print("-" * 100)
    for row in rows:
        title = (row["title"] or "")[:40]
        print(f"{row['id']:<25} {(row['platform'] or '-'):<10} {(row['chain'] or '-'):<15} {(row['status'] or '-'):<10} {title}")

    print(f"\n{len(rows)} sources (limited to 50).")
    conn.close()


def cmd_sql(args):
    """Execute raw SQL query."""
    if not args:
        print("Usage: ontology_query.py sql \"SELECT ...\"")
        return

    query = " ".join(args)
    conn = get_conn()
    cur = conn.cursor()

    try:
        cur.execute(query)
        rows = cur.fetchall()
        if rows:
            headers = rows[0].keys()
            print("\t".join(headers))
            print("-" * 80)
            for row in rows:
                print("\t".join(str(row[h]) if row[h] is not None else "NULL" for h in headers))
            print(f"\n{len(rows)} rows.")
        else:
            print("No results.")
    except sqlite3.Error as e:
        print(f"SQL Error: {e}")

    conn.close()


COMMANDS = {
    "stats": cmd_stats,
    "layers": cmd_layers,
    "apps": cmd_apps,
    "search": cmd_search,
    "primitives": cmd_primitives,
    "apparatus": cmd_apparatus,
    "projects": cmd_projects,
    "tasks": cmd_tasks,
    "sources": cmd_sources,
    "sql": cmd_sql,
}


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help", "help"):
        print("Usage: ontology_query.py <command> [args...]")
        print("\nCommands:")
        for name, fn in COMMANDS.items():
            doc = (fn.__doc__ or "").strip().split("\n")[0]
            print(f"  {name:<15} {doc}")
        print(f"\nDatabase: {DB_PATH}")
        return

    cmd = sys.argv[1]
    if cmd not in COMMANDS:
        print(f"Unknown command: {cmd}")
        print(f"Available: {', '.join(COMMANDS.keys())}")
        sys.exit(1)

    COMMANDS[cmd](sys.argv[2:])


if __name__ == "__main__":
    main()
