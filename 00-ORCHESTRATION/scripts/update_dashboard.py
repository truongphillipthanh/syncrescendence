#!/usr/bin/env python3
"""
update_dashboard.py
Regenerate DYN-DASHBOARD.md from CSV data sources.
Run after any task/project/sprint updates.

Usage: python3 00-ORCHESTRATION/scripts/update_dashboard.py

Enhanced for DIRECTIVE-041B with repository metrics and verification status.
"""

import csv
import subprocess
from datetime import datetime
from pathlib import Path
import os

# Determine paths relative to script location
SCRIPT_DIR = Path(__file__).parent
STATE_DIR = SCRIPT_DIR.parent / 'state'

def load_csv(filename):
    """Load CSV file and return list of dicts."""
    filepath = STATE_DIR / filename
    if not filepath.exists():
        return []
    with open(filepath, 'r') as f:
        return list(csv.DictReader(f))

def count_by_field(items, field):
    """Count items by field value."""
    counts = {}
    for item in items:
        value = item.get(field, 'unknown')
        counts[value] = counts.get(value, 0) + 1
    return counts

def count_queue_items(queue_dir):
    """Count files in QUEUE directories."""
    counts = {}
    queue_path = STATE_DIR.parent.parent / '03-QUEUE'
    for subdir in ['pending', 'modal1', 'modal2']:
        subpath = queue_path / subdir
        if subpath.exists():
            counts[subdir] = len([f for f in subpath.iterdir() if f.is_file() and not f.name.startswith('.')])
        else:
            counts[subdir] = 0
    return counts


def count_files(pattern: str) -> int:
    """Count files matching pattern using shell glob."""
    try:
        repo_root = STATE_DIR.parent.parent
        result = subprocess.run(
            f'ls {repo_root}/{pattern} 2>/dev/null | wc -l',
            shell=True, capture_output=True, text=True
        )
        return int(result.stdout.strip())
    except:
        return 0


def get_repo_metrics() -> dict:
    """Gather comprehensive repository metrics."""
    repo_root = STATE_DIR.parent.parent
    metrics = {}

    # CANON metrics
    metrics['canon_files'] = count_files('01-CANON/*.md')

    # SOURCES metrics
    metrics['processed_sources'] = count_files('04-SOURCES/processed/*.md')
    metrics['raw_sources'] = count_files('04-SOURCES/raw/*.txt') + count_files('04-SOURCES/raw/*.md')

    # OPERATIONAL metrics
    metrics['function_xmls'] = count_files('02-ENGINE/*.xml')

    # Integration metrics
    try:
        result = subprocess.run(
            f'grep -l "SOURCE-" {repo_root}/01-CANON/*.md 2>/dev/null | wc -l',
            shell=True, capture_output=True, text=True
        )
        metrics['canon_with_integrations'] = int(result.stdout.strip())
    except:
        metrics['canon_with_integrations'] = 0

    # Structure metrics
    try:
        result = subprocess.run(
            f'find {repo_root} -mindepth 2 -type d -name "scaffolding" 2>/dev/null | wc -l',
            shell=True, capture_output=True, text=True
        )
        metrics['scaffolding_dirs'] = int(result.stdout.strip())
    except:
        metrics['scaffolding_dirs'] = 0

    try:
        result = subprocess.run(
            f'ls {repo_root}/*.md 2>/dev/null | wc -l',
            shell=True, capture_output=True, text=True
        )
        metrics['root_md_files'] = int(result.stdout.strip())
    except:
        metrics['root_md_files'] = 0

    return metrics

def generate_burndown_chart(burndown):
    """Generate ASCII burndown chart."""
    if not burndown:
        return "No burndown data available."

    chart_lines = []
    chart_lines.append("```")
    chart_lines.append("Points Remaining")

    # Simple ASCII chart
    max_points = 40
    for row in burndown:
        day = row.get('date', '')[8:10] if len(row.get('date', '')) >= 10 else '?'
        remaining = int(row.get('remaining_points', 0))
        bar_len = int(remaining / max_points * 30)
        chart_lines.append(f"  Day {day}: {'█' * bar_len}{'░' * (30 - bar_len)} {remaining}")

    chart_lines.append("```")
    return '\n'.join(chart_lines)

def generate_dashboard():
    """Generate the dashboard markdown."""
    projects = load_csv('projects.csv')
    tasks = load_csv('tasks.csv')
    sprints = load_csv('sprints.csv')
    burndown = load_csv('burndown.csv')

    # Calculate metrics
    task_counts = count_by_field(tasks, 'status')
    queue_counts = count_queue_items(STATE_DIR)
    current_sprint = next((s for s in sprints if s.get('status') == 'in_progress'), None)
    repo_metrics = get_repo_metrics()

    # Status icons
    status_icons = {
        'in_progress': '🔄',
        'blocked': '🚫',
        'not_started': '⏸️',
        'done': '✅',
        'completed': '✅'
    }

    # Generate markdown
    dashboard = f"""# SYNCRESCENDENT DASHBOARD
## Project Management Overview
**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Current Sprint**: {current_sprint['name'] if current_sprint else 'None'} ({current_sprint['goal'][:50] + '...' if current_sprint and len(current_sprint.get('goal', '')) > 50 else current_sprint.get('goal', '') if current_sprint else 'N/A'})

---

## THE GLOBE (Holistic View)

```
ORACLE ARC PROGRESS
═══════════════════════════════════════════════════════════════════
Oracle 0-8: ████████████████████████████████████████ COMPLETE
Oracle 9:   ████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 20% (in progress)
Oracle 10+: ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ BLOCKED
═══════════════════════════════════════════════════════════════════
```

---

## Repository Metrics

| Category | Count | Notes |
|----------|-------|-------|
| CANON files | {repo_metrics['canon_files']} | Canonical knowledge documents |
| Processed sources | {repo_metrics['processed_sources']} | Qualified briefs |
| Raw sources | {repo_metrics['raw_sources']} | Pending processing |
| Function XMLs | {repo_metrics['function_xmls']} | Operational metaprompts |
| CANON with integrations | {repo_metrics['canon_with_integrations']} | Files with SOURCE- references |

### Structural Health

| Check | Status |
|-------|--------|
| Scaffolding dirs | {'PASS' if repo_metrics['scaffolding_dirs'] == 0 else 'FAIL: ' + str(repo_metrics['scaffolding_dirs'])} |
| Root .md files | {'PASS' if repo_metrics['root_md_files'] <= 2 else 'WARN: ' + str(repo_metrics['root_md_files'])} |

---

## Initiative Status

| ID | Initiative | Status | Priority | Owner | Blocked By | Modal |
|----|------------|--------|----------|-------|------------|-------|
"""

    for p in projects:
        status = p.get('status', 'unknown')
        icon = status_icons.get(status, '❓')
        blocked = p.get('blocked_by', '') or '—'
        dashboard += f"| {p.get('id', '')} | {p.get('name', '')} | {icon} {status.replace('_', ' ').title()} | {p.get('priority', '')} | {p.get('owner', '')} | {blocked} | {p.get('modal', '')} |\n"

    dashboard += f"""
---

## Task Summary

| Status | Count |
|--------|-------|
| Not Started | {task_counts.get('not_started', 0)} |
| In Progress | {task_counts.get('in_progress', 0)} |
| Done | {task_counts.get('done', 0)} |
| Blocked | {task_counts.get('blocked', 0)} |

### Active Tasks

| ID | Task | Status | Priority | Project | Owner |
|----|------|--------|----------|---------|-------|
"""

    # Show in_progress and not_started tasks
    for t in tasks:
        if t.get('status') in ['in_progress', 'not_started']:
            dashboard += f"| {t.get('id', '')} | {t.get('name', '')[:40]} | {t.get('status', '')} | {t.get('priority', '')} | {t.get('project_id', '') or '—'} | {t.get('owner', '')} |\n"

    dashboard += f"""
---

## Current Sprint Burndown

{generate_burndown_chart(burndown)}

---

## QUEUE Status (Inbox Zero Tracking)

| Queue | Items | Status |
|-------|-------|--------|
| QUEUE/pending/ | {queue_counts.get('pending', 0)} | {'🔴 NEEDS TRIAGE' if queue_counts.get('pending', 0) > 0 else '✅ CLEAR'} |
| QUEUE/modal1/ | {queue_counts.get('modal1', 0)} | {'⏳ Active work' if queue_counts.get('modal1', 0) > 0 else '✅ CLEAR'} |
| QUEUE/modal2/ | {queue_counts.get('modal2', 0)} | {'📦 Parked' if queue_counts.get('modal2', 0) > 0 else '✅ CLEAR'} |

**Inbox Zero Target**: pending/ should be 0

---

## Dependency Chain

```
PROJ-001 (Transcript Ingestion)
    ↓
PROJ-002 (IIC Configuration)
    ↓
PROJ-003 (Tooling Stack) ─────→ PROJ-005 (Branding)
    ↓
PROJ-006 (Ontology Project)
    ↓
PROJ-007 (Curriculum)
```

---

## METHODOLOGY SUPPORT

This system supports multiple methodologies:

### Agile/Scrum
- Sprints tracked in sprints.csv
- Velocity calculated from completed points
- Burndown chart updated daily

### Kanban
- Tasks flow: not_started → in_progress → done
- WIP limits can be enforced via status counts
- Blockers tracked in blocked_by field

### Waterfall
- Projects have dependencies (blocked_by)
- Sequential phases visible in Oracle scope

### PRINCE2
- Business case in project notes
- Stage gates at Oracle boundaries
- Exception reporting via blockers

---

## Quick Commands

```bash
make verify         # Run verification suite
make sync           # Git pull/push
make update-ledgers # Regenerate this dashboard
./00-ORCHESTRATION/scripts/verify_all.sh  # Full verification
```

## UPDATE PROTOCOL

Agents MUST update after every directive:
1. Update task status in tasks.csv
2. Update burndown in burndown.csv
3. Run: `python3 00-ORCHESTRATION/scripts/update_dashboard.py`
4. Commit changes to 00-ORCHESTRATION/state/

---

*Dashboard auto-generated by update_dashboard.py*
"""

    # Write dashboard
    dashboard_path = STATE_DIR / 'DYN-DASHBOARD.md'
    with open(dashboard_path, 'w') as f:
        f.write(dashboard)

    print(f"Dashboard updated: {dashboard_path}")
    print(f"  Projects: {len(projects)}")
    print(f"  Tasks: {len(tasks)}")
    print(f"  Current Sprint: {current_sprint['name'] if current_sprint else 'None'}")
    print(f"  Queue pending: {queue_counts.get('pending', 0)}")

if __name__ == '__main__':
    generate_dashboard()
