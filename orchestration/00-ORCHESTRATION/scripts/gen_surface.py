#!/usr/bin/env python3
"""Generate static ontology surface markdown for Obsidian."""
import sqlite3
import datetime

DB_PATH = "/Users/home/.syncrescendence/ontology.db"
OUT_PATH = "/Users/home/Desktop/syncrescendence/orchestration/state/SURFACE-ONTOLOGY_DASHBOARD.md"

db = sqlite3.connect(DB_PATH)
meta = dict(db.execute("SELECT key, value FROM _meta").fetchall())
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

lines = []
lines.append("---")
lines.append("id: SURFACE-ONTOLOGY")
lines.append("name: Ontology Strategic Dashboard")
lines.append("type: surface")
lines.append(f"generated: {now}")
lines.append(f"schema_version: {meta.get('schema_version', '?')}")
lines.append("operational_status: operational")
lines.append("---")
lines.append("")
lines.append("# Ontology Strategic Dashboard")
lines.append(f"> Auto-generated {now} from `ontology_query.py dashboard`")
lines.append(f"> Schema v{meta.get('schema_version', '?')} | 2015 build rows | 1174 queryable")
lines.append("")

# Commitments
lines.append("## Commitments")
lines.append("")
lines.append("| Code | Name | Stakeholder | Status | Intent |")
lines.append("|------|------|-------------|--------|--------|")
for r in db.execute("SELECT code, name, stakeholder, status, intention_link FROM commitments ORDER BY code"):
    lines.append(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} |")
lines.append("")

# Goals
lines.append("## Goals")
lines.append("")
lines.append("| Code | Name | Status |")
lines.append("|------|------|--------|")
for r in db.execute("SELECT code, name, status FROM goals ORDER BY code"):
    lines.append(f"| {r[0]} | {r[1]} | {r[2]} |")
lines.append("")

# Risk matrix
lines.append("## Risk Matrix")
lines.append("")
lines.append("| Code | Category | Probability | Impact | Risk |")
lines.append("|------|----------|-------------|--------|------|")
for r in db.execute("""SELECT code, category, probability, impact, name FROM risks
    ORDER BY CASE impact WHEN 'catastrophic' THEN 0 WHEN 'critical' THEN 1 WHEN 'high' THEN 2 WHEN 'medium' THEN 3 ELSE 4 END, code"""):
    lines.append(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} |")
lines.append("")

# Resource economics
lines.append("## Resource Economics")
lines.append("")
lines.append("| Category | Items | Monthly |")
lines.append("|----------|-------|---------|")
for r in db.execute("SELECT category, COUNT(*), SUM(monthly_cost) FROM resources GROUP BY category ORDER BY SUM(monthly_cost) DESC"):
    lines.append(f"| {r[0]} | {r[1]} | ${r[2]:.0f} |")
total = db.execute("SELECT SUM(monthly_cost) FROM resources").fetchone()[0]
lines.append(f"| **TOTAL** | **25** | **${total:.0f}** |")
lines.append("")

# Environments
lines.append("## Environments")
lines.append("")
lines.append("| Code | Name | Machine | Agent |")
lines.append("|------|------|---------|-------|")
for r in db.execute("SELECT code, name, machine, primary_agent FROM environments ORDER BY code"):
    lines.append(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} |")
lines.append("")

# Relationships (top 15)
lines.append("## Strategic Relationships (by strength)")
lines.append("")
lines.append("| Entity A | Relationship | Entity B | Strength |")
lines.append("|----------|-------------|----------|----------|")
for r in db.execute("SELECT entity_a, relationship_type, entity_b, strength FROM strategic_relationships ORDER BY strength DESC LIMIT 15"):
    lines.append(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} |")
lines.append("")
lines.append("*30 total relationships. Run `python3 ontology_query.py relationships` for full list.*")
lines.append("")

# Agent bindings
lines.append("## Constellation Bindings")
lines.append("")
lines.append("| Agent | Bindings | |")
lines.append("|-------|----------|---|")
for r in db.execute("SELECT agent_code, COUNT(*) FROM agent_bindings GROUP BY agent_code ORDER BY COUNT(*) DESC"):
    bar = "█" * (r[1] // 2)
    lines.append(f"| {r[0]} | {r[1]} | {bar} |")
lines.append("")

# Verb governance
lines.append("## Verb Governance")
lines.append("")
lines.append("| Category | Verbs | Sovereign-Gated |")
lines.append("|----------|-------|-----------------|")
for r in db.execute("SELECT category, COUNT(*), SUM(CASE WHEN requires_approval=1 THEN 1 ELSE 0 END) FROM governed_verbs GROUP BY category ORDER BY category"):
    gated = str(int(r[2])) if r[2] > 0 else "—"
    lines.append(f"| {r[0]} | {r[1]} | {gated} |")
lines.append("")

# Footer
lines.append("---")
lines.append("")
lines.append("*Regenerate: `python3 orchestration/scripts/ontology_query.py dashboard`*")
lines.append(f"*Full DB: `~/.syncrescendence/ontology.db` (v{meta.get('schema_version', '?')}, 43 tables)*")

output = "\n".join(lines)
with open(OUT_PATH, "w") as f:
    f.write(output)
print(f"Written {len(lines)} lines to {OUT_PATH}")

db.close()
