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
    python3 ontology_query.py relationships [--type supports]
    python3 ontology_query.py environments [--machine mac-mini]
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
        "Kinetic": ["action_types", "app_actions", "agent_bindings", "workflow_templates", "workflow_steps"],
        "Strategic": ["commitments", "goals", "risks", "strategic_relationships", "resources", "environments", "governed_verbs"],
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


def cmd_actions(args):
    """List action types with optional category filter."""
    conn = get_conn()
    cur = conn.cursor()

    query = """
        SELECT at.code, at.name, at.category, r.code as parent_role,
               at.automation_level, at.write_back_capable, at.requires_approval
        FROM action_types at
        LEFT JOIN roles r ON at.parent_role_id = r.id
        WHERE 1=1
    """
    params = []

    if "--category" in args:
        idx = args.index("--category")
        if idx + 1 < len(args):
            query += " AND at.category = ?"
            params.append(args[idx + 1])

    query += " ORDER BY at.category, at.code"
    cur.execute(query, params)
    rows = cur.fetchall()

    print(f"{'Code':<25} {'Name':<25} {'Category':<12} {'Role':<12} {'Auto':<12} WB  Appr")
    print("-" * 100)
    for row in rows:
        wb = "Y" if row["write_back_capable"] else "N"
        appr = "Y" if row["requires_approval"] else "N"
        print(f"{row['code']:<25} {row['name']:<25} {row['category']:<12} {(row['parent_role'] or '-'):<12} {(row['automation_level'] or '-'):<12} {wb:<4}{appr}")

    print(f"\n{len(rows)} action types.")
    conn.close()


def cmd_agent_bindings(args):
    """List agent bindings with optional agent filter."""
    conn = get_conn()
    cur = conn.cursor()

    query = """
        SELECT ab.agent_code, a.slug as app_slug, at.code as action_code,
               ab.binding_strength, ab.invocation_method, ab.frequency, ab.notes
        FROM agent_bindings ab
        JOIN apps a ON ab.app_id = a.id
        JOIN action_types at ON ab.action_type_id = at.id
        WHERE 1=1
    """
    params = []

    if "--agent" in args:
        idx = args.index("--agent")
        if idx + 1 < len(args):
            query += " AND ab.agent_code = ?"
            params.append(args[idx + 1])

    query += " ORDER BY ab.agent_code, ab.binding_strength, a.slug"
    cur.execute(query, params)
    rows = cur.fetchall()

    print(f"{'Agent':<14} {'App':<20} {'Action':<22} {'Strength':<12} {'Method':<10} {'Freq':<10}")
    print("-" * 95)
    for row in rows:
        print(f"{row['agent_code']:<14} {row['app_slug']:<20} {row['action_code']:<22} {row['binding_strength']:<12} {row['invocation_method']:<10} {row['frequency']:<10}")

    print(f"\n{len(rows)} bindings.")
    conn.close()


def cmd_workflows(args):
    """List workflow templates and optionally show steps."""
    conn = get_conn()
    cur = conn.cursor()

    if args:
        # Show specific workflow with steps
        code = args[0]
        cur.execute("""
            SELECT wt.code, wt.name, wt.description, wt.use_frequency,
                   wt.average_duration_minutes, ap.code as apparatus_code
            FROM workflow_templates wt
            LEFT JOIN apparatus ap ON wt.apparatus_id = ap.id
            WHERE wt.code = ?
        """, (code,))
        wf = cur.fetchone()
        if not wf:
            print(f"Workflow '{code}' not found.")
            conn.close()
            return

        print(f"Workflow: {wf['name']} ({wf['code']})")
        print(f"  Description: {wf['description']}")
        print(f"  Apparatus: {wf['apparatus_code'] or 'none'}")
        print(f"  Frequency: {wf['use_frequency']}")
        print(f"  Avg Duration: {wf['average_duration_minutes']} min")
        print(f"\n  Steps:")
        print(f"  {'#':<4} {'App':<18} {'Description':<45} {'Duration':<8}")
        print(f"  {'-'*80}")

        cur.execute("""
            SELECT ws.step_number, a.slug as app_slug, ws.action_description,
                   ws.average_duration_minutes, ws.notes
            FROM workflow_steps ws
            JOIN apps a ON ws.app_id = a.id
            WHERE ws.workflow_id = (SELECT id FROM workflow_templates WHERE code = ?)
            ORDER BY ws.step_number
        """, (code,))
        for step in cur.fetchall():
            print(f"  {step['step_number']:<4} {step['app_slug']:<18} {step['action_description'][:44]:<45} {step['average_duration_minutes'] or '-':>4} min")
    else:
        # List all workflows
        cur.execute("""
            SELECT wt.code, wt.name, wt.use_frequency, wt.average_duration_minutes,
                   ap.code as apparatus_code,
                   (SELECT COUNT(*) FROM workflow_steps ws WHERE ws.workflow_id = wt.id) as step_count
            FROM workflow_templates wt
            LEFT JOIN apparatus ap ON wt.apparatus_id = ap.id
            ORDER BY wt.code
        """)
        rows = cur.fetchall()
        print(f"{'Code':<20} {'Name':<30} {'Apparatus':<22} {'Freq':<10} {'Steps':>5} {'Min':>5}")
        print("-" * 95)
        for row in rows:
            print(f"{row['code']:<20} {row['name']:<30} {(row['apparatus_code'] or '-'):<22} {row['use_frequency']:<10} {row['step_count']:>5} {row['average_duration_minutes'] or '-':>5}")

        print(f"\n{len(rows)} workflows. Use 'workflows <code>' for details.")
    conn.close()


def cmd_commitments(args):
    """List commitments with optional status filter."""
    conn = get_conn()
    cur = conn.cursor()
    query = "SELECT code, name, stakeholder, deadline, status, intention_link FROM commitments WHERE 1=1"
    params = []
    if "--status" in args:
        idx = args.index("--status")
        if idx + 1 < len(args):
            query += " AND status = ?"
            params.append(args[idx + 1])
    query += " ORDER BY code"
    cur.execute(query, params)
    rows = cur.fetchall()
    print(f"{'Code':<10} {'Name':<35} {'Stakeholder':<12} {'Deadline':<12} {'Status':<10} Intent")
    print("-" * 95)
    for row in rows:
        print(f"{row['code']:<10} {row['name'][:34]:<35} {(row['stakeholder'] or '-'):<12} {(row['deadline'] or '-'):<12} {row['status']:<10} {(row['intention_link'] or '-')}")
    print(f"\n{len(rows)} commitments.")
    conn.close()


def cmd_goals(args):
    """List goals with optional status filter."""
    conn = get_conn()
    cur = conn.cursor()
    query = "SELECT code, name, intention_link, status, success_criteria FROM goals WHERE 1=1"
    params = []
    if "--status" in args:
        idx = args.index("--status")
        if idx + 1 < len(args):
            query += " AND status = ?"
            params.append(args[idx + 1])
    query += " ORDER BY code"
    cur.execute(query, params)
    rows = cur.fetchall()
    print(f"{'Code':<10} {'Name':<35} {'Intent':<12} {'Status':<10} Criteria")
    print("-" * 95)
    for row in rows:
        criteria = (row['success_criteria'] or '')[:30]
        print(f"{row['code']:<10} {row['name'][:34]:<35} {(row['intention_link'] or '-'):<12} {row['status']:<10} {criteria}")
    print(f"\n{len(rows)} goals.")
    conn.close()


def cmd_risks(args):
    """List risks with optional category filter."""
    conn = get_conn()
    cur = conn.cursor()
    query = "SELECT code, name, category, probability, impact, status FROM risks WHERE 1=1"
    params = []
    if "--category" in args:
        idx = args.index("--category")
        if idx + 1 < len(args):
            query += " AND category = ?"
            params.append(args[idx + 1])
    query += " ORDER BY code"
    cur.execute(query, params)
    rows = cur.fetchall()
    print(f"{'Code':<10} {'Name':<35} {'Category':<12} {'Prob':<8} {'Impact':<10} Status")
    print("-" * 90)
    for row in rows:
        print(f"{row['code']:<10} {row['name'][:34]:<35} {(row['category'] or '-'):<12} {(row['probability'] or '-'):<8} {(row['impact'] or '-'):<10} {row['status']}")
    print(f"\n{len(rows)} risks.")
    conn.close()


def cmd_resources(args):
    """List resources with optional category filter."""
    conn = get_conn()
    cur = conn.cursor()
    query = "SELECT code, name, category, monthly_cost, status, machine FROM resources WHERE 1=1"
    params = []
    if "--category" in args:
        idx = args.index("--category")
        if idx + 1 < len(args):
            query += " AND category = ?"
            params.append(args[idx + 1])
    query += " ORDER BY code"
    cur.execute(query, params)
    rows = cur.fetchall()
    print(f"{'Code':<10} {'Name':<30} {'Category':<14} {'$/mo':>6} {'Status':<10} Machine")
    print("-" * 85)
    for row in rows:
        cost = f"${row['monthly_cost']:.0f}" if row['monthly_cost'] else "$0"
        print(f"{row['code']:<10} {row['name'][:29]:<30} {(row['category'] or '-'):<14} {cost:>6} {row['status']:<10} {(row['machine'] or '-')}")
    total = sum(r['monthly_cost'] or 0 for r in rows)
    print(f"\n{len(rows)} resources. Total monthly: ${total:.0f}")
    conn.close()


def cmd_relationships(args):
    """List strategic relationships with optional type filter."""
    conn = get_conn()
    cur = conn.cursor()
    query = "SELECT code, entity_a, entity_a_type, relationship_type, entity_b, entity_b_type, strength, context FROM strategic_relationships WHERE 1=1"
    params = []
    if "--type" in args:
        idx = args.index("--type")
        if idx + 1 < len(args):
            query += " AND relationship_type = ?"
            params.append(args[idx + 1])
    query += " ORDER BY strength DESC, code ASC"
    cur.execute(query, params)
    rows = cur.fetchall()
    print(f"{'Code':<10} {'Entity A':<18} {'Type':<12} {'Entity B':<18} {'Str':>4}  Context")
    print("-" * 95)
    for row in rows:
        ctx = (row['context'] or '')[:40]
        print(f"{row['code']:<10} {row['entity_a'][:17]:<18} {row['relationship_type']:<12} {row['entity_b'][:17]:<18} {row['strength'] or '-':>4}  {ctx}")
    print(f"\n{len(rows)} relationships.")
    conn.close()


def cmd_environments(args):
    """List environments with optional machine filter."""
    conn = get_conn()
    cur = conn.cursor()
    query = "SELECT code, name, machine, spatial_context, primary_agent, notes FROM environments WHERE 1=1"
    params = []
    if "--machine" in args:
        idx = args.index("--machine")
        if idx + 1 < len(args):
            query += " AND machine = ?"
            params.append(args[idx + 1])
    query += " ORDER BY code ASC"
    cur.execute(query, params)
    rows = cur.fetchall()
    print(f"{'Code':<10} {'Name':<25} {'Machine':<12} {'Context':<18} {'Agent':<12} Notes")
    print("-" * 100)
    for row in rows:
        notes = (row['notes'] or '')[:40]
        print(f"{row['code']:<10} {row['name'][:24]:<25} {(row['machine'] or '-'):<12} {(row['spatial_context'] or '-')[:17]:<18} {(row['primary_agent'] or '-'):<12} {notes}")
    print(f"\n{len(rows)} environments.")
    conn.close()


def cmd_verbs(args):
    """List governed verbs with optional category filter."""
    conn = get_conn()
    cur = conn.cursor()
    query = "SELECT verb, category, applies_to, requires_approval, advisory_note FROM governed_verbs WHERE 1=1"
    params = []
    if "--category" in args:
        idx = args.index("--category")
        if idx + 1 < len(args):
            query += " AND category = ?"
            params.append(args[idx + 1])
    query += " ORDER BY category, verb"
    cur.execute(query, params)
    rows = cur.fetchall()
    print(f"{'Verb':<18} {'Category':<12} {'Applies To':<16} {'Approval':>8}  Note")
    print("-" * 80)
    for row in rows:
        appr = "YES" if row['requires_approval'] else "no"
        print(f"{row['verb']:<18} {row['category']:<12} {row['applies_to']:<16} {appr:>8}  {(row['advisory_note'] or '')[:25]}")
    print(f"\n{len(rows)} governed verbs (advisory mode).")
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
    "actions": cmd_actions,
    "agent-bindings": cmd_agent_bindings,
    "workflows": cmd_workflows,
    "commitments": cmd_commitments,
    "goals": cmd_goals,
    "risks": cmd_risks,
    "resources": cmd_resources,
    "relationships": cmd_relationships,
    "environments": cmd_environments,
    "verbs": cmd_verbs,
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
