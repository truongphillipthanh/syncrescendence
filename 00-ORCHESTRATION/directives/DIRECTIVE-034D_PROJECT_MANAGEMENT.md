# DIRECTIVE-034B: PROJECT MANAGEMENT SYSTEM + TRANSCRIPT NAMING + QUEUE RECONCILIATION
## Stream B: Operational Infrastructure Restoration
**Issued**: 2026-01-02
**Authority**: Oracle9 under Sovereign direction
**Classification**: CRITICAL — Establishing Visibility and Control Infrastructure
**Execution**: Claude Code
**Parallel Stream**: DIRECTIVE-034A handles Forensic Recovery + Narratives

---

## SOVEREIGN'S MANDATE

> "Phase B: Create an agentified Agile/Scrum/Kanban with flexibility for waterfall and PRINCE2, and whatever other methodology. Apply the 18 lenses to create the spiritual successor to the Project Management System."

> "Phase C: Replace SOURCE with TRANSCRIPT, and yes, apply standard"

> "Phase D: Absolutely needs reconciling. This SHOULD have informed the trajectory."

---

## ORACLE'S INTERPRETATION

This directive establishes **operational control infrastructure** by:

1. **Project Management System** — Agentified methodology-agnostic tracking with burndown visibility
2. **Transcript Naming Correction** — Apply Sovereign's standard, not invented convention
3. **QUEUE Reconciliation** — Map pending work to roadmap, establish inbox zero tracking

These are **not separate tasks** but interconnected infrastructure that enables trajectory visibility.

---

## 18-LENS EVALUATION (APPLIED TO PROJECT MANAGEMENT DESIGN)

| # | Lens | Design Implication | Score |
|---|------|-------------------|-------|
| 1 | Syncrescendent Route | Continuous tracking across Oracle sessions | ✓ |
| 2 | Bitter Lesson | Simple structure that scales with complexity | ✓ |
| 3 | Antifragile | Methodology-agnostic (survives process changes) | ✓ |
| 4 | Meet the Moment | Provides visibility NOW while enabling future automation | ✓ |
| 5 | Steelman/Redteam | Supports multiple methodologies (Agile, Waterfall, PRINCE2) | ✓ |
| 6 | Personal Idiosyncrasies | Globe-before-trees visibility (holistic → tactical) | ✓ |
| 7 | Potency w/o Resolution Loss | Maximum tracking with minimal overhead | ✓ |
| 8 | Elegance + Dev Happiness | CSV/structured format for both human and agent access | ✓ |
| 9 | Agentify + Human-Navigable | Agents can read/update, humans can review | ✓ |
| 10 | First Principles | Track: What, Status, Blocked-by, Owner, Due | ✓ |
| 11 | Systems Thinking | Connects QUEUE to Roadmap to Oracle Arc | ✓ |
| 12 | Industrial Engineering | Enables throughput measurement (velocity) | ✓ |
| 13 | Complexity Theory | Essential tracking only, no ceremonial overhead | ✓ |
| 14 | Permaculture | Self-maintaining (agents update as they work) | ✓ |
| 15 | Design Thinking | Sovereign can see progress at a glance | ✓ |
| 16 | Agile | Supports sprints, backlogs, velocity | ✓ |
| 17 | Lean | Eliminates invisible work-in-progress | ✓ |
| 18 | Six Sigma | Tracks defects/blockers for process improvement | ✓ |

**Score: 18/18 — DESIGN APPROVED**

---

## PHASE 1: PROJECT MANAGEMENT SYSTEM

### 1.1 Design Principles (18-Lens Derived)

```
┌─────────────────────────────────────────────────────────────────────┐
│                    SYNCRESCENDENT PROJECT MANAGEMENT                 │
│                                                                      │
│  METHODOLOGY-AGNOSTIC: Works with Agile, Waterfall, PRINCE2, Hybrid │
│  AGENT-NATIVE: CSV/structured format for programmatic access        │
│  HUMAN-READABLE: Markdown views for Sovereign review                │
│  HOLISTIC-FIRST: Globe view before tree details                     │
│  CONTINUOUS: Updates persist across Oracle sessions                 │
└─────────────────────────────────────────────────────────────────────┘
```

### 1.2 Core Data Structure

Create `orchestration/state/projects.csv`:

```csv
id,name,type,status,priority,owner,blocked_by,oracle_scope,modal,due_date,created,updated,notes
PROJ-001,Transcript Ingestion,initiative,in_progress,P1,Oracle9,null,9,modal1,2026-01-15,2026-01-01,2026-01-02,Pattern proven; 43 paradigm sources pending
PROJ-002,IIC Configuration,initiative,blocked,P1,Oracle10,PROJ-001,10,modal1,2026-02-01,2025-12-29,2026-01-02,Requires enriched corpus
PROJ-003,Tooling Stack,initiative,blocked,P2,Oracle11,PROJ-002,11,modal1,null,2025-12-29,2026-01-02,GPT-5.2/Grok/MCP/Skills/Notion/Airtable
PROJ-004,Automation,initiative,blocked,P2,Oracle12,PROJ-003,12,modal1,null,2025-12-29,2026-01-02,Agentification of processes
PROJ-005,Branding,initiative,blocked,P3,Oracle13,PROJ-002,13,modal1,null,2025-12-29,2026-01-02,Business side elucidation
PROJ-006,Ontology Project,initiative,blocked,P1,Oracle14,PROJ-003,14,modal1,null,2025-12-29,2026-01-02,Palantir-like operational infrastructure
PROJ-007,Curriculum,initiative,blocked,P3,Oracle15,PROJ-006,15,modal1,null,2025-12-29,2026-01-02,Teaching Syncrescendence
PROJ-008,Tech Lunar Canonization,initiative,not_started,P2,TBD,null,TBD,modal1,null,2025-12-30,2026-01-02,306K specs to CANON-30xxx
PROJ-009,Modal 2 Preparation,initiative,not_started,P3,TBD,null,TBD,modal2,null,2025-12-29,2026-01-02,3D/VFX/Video synthesis runway
```

### 1.3 Task Tracking Structure

Create `orchestration/state/tasks.csv`:

```csv
id,project_id,name,type,status,priority,owner,blocked_by,estimate_hrs,actual_hrs,created,updated,notes
TASK-001,PROJ-001,Flatten SOURCES/raw,task,not_started,P1,Claude_Code,null,2,null,2026-01-02,2026-01-02,Apply correct naming standard
TASK-002,PROJ-001,Rename transcripts to standard,task,not_started,P1,Claude_Code,TASK-001,3,null,2026-01-02,2026-01-02,{YYYYMMDD}-{platform_format}-{channel}-{guest/title}
TASK-003,PROJ-001,Process remaining 43 paradigm sources,task,not_started,P1,Claude_Code,TASK-002,20,null,2026-01-02,2026-01-02,Batch processing
TASK-004,PROJ-001,Process 44 strategic sources,task,not_started,P2,Claude_Code,TASK-003,15,null,2026-01-02,2026-01-02,Secondary priority
TASK-005,null,Restore macroscopic narratives,task,in_progress,P1,Claude_Code,null,4,null,2026-01-02,2026-01-02,DIRECTIVE-034A
TASK-006,null,Git archaeology for Coherence,task,in_progress,P1,Claude_Code,null,2,null,2026-01-02,2026-01-02,DIRECTIVE-034A
TASK-007,null,Create project management system,task,in_progress,P1,Claude_Code,null,3,null,2026-01-02,2026-01-02,DIRECTIVE-034B
TASK-008,null,Reconcile QUEUE with roadmap,task,not_started,P1,Claude_Code,TASK-007,2,null,2026-01-02,2026-01-02,DIRECTIVE-034B
```

### 1.4 Sprint/Iteration Tracking

Create `orchestration/state/sprints.csv`:

```csv
id,name,start_date,end_date,status,goal,velocity_planned,velocity_actual,notes
SPRINT-001,Oracle9-Alpha,2026-01-01,2026-01-07,in_progress,Establish ingestion pattern + restore lost content,40,null,First sprint with project tracking
```

### 1.5 Burndown Tracking

Create `orchestration/state/burndown.csv`:

```csv
date,sprint_id,total_points,completed_points,remaining_points,ideal_remaining
2026-01-01,SPRINT-001,40,0,40,40
2026-01-02,SPRINT-001,40,8,32,34
```

### 1.6 Human-Readable Dashboard

Create `orchestration/state/DASHBOARD.md`:

```markdown
# SYNCRESCENDENT DASHBOARD
## Project Management Overview
**Generated**: [AUTO-UPDATE TIMESTAMP]
**Current Sprint**: SPRINT-001 (Oracle9-Alpha)

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

### Initiative Status

| ID | Initiative | Status | Owner | Blocked By |
|----|------------|--------|-------|------------|
| PROJ-001 | Transcript Ingestion | 🔄 In Progress | Oracle9 | — |
| PROJ-002 | IIC Configuration | 🚫 Blocked | Oracle10 | PROJ-001 |
| PROJ-003 | Tooling Stack | 🚫 Blocked | Oracle11 | PROJ-002 |
| PROJ-006 | Ontology Project | 🚫 Blocked | Oracle14 | PROJ-003 |

### Current Sprint Burndown

```
Points Remaining
40 │ ▓
35 │ ▓ ▓
30 │ ▓ ▓ ░
25 │ ▓ ▓ ░ ░
20 │ ▓ ▓ ░ ░ ░
15 │ ▓ ▓ ░ ░ ░ ░
10 │ ▓ ▓ ░ ░ ░ ░ ░
 5 │ ▓ ▓ ░ ░ ░ ░ ░ ░
 0 └──────────────────────
     1  2  3  4  5  6  7  (Day)
   ▓ = Actual  ░ = Ideal
```

### QUEUE Status (Inbox Zero Tracking)

| Queue | Items | Status |
|-------|-------|--------|
| QUEUE/pending/ | [COUNT] | [STATUS] |
| QUEUE/modal1/ | [COUNT] | [STATUS] |
| QUEUE/modal2/ | [COUNT] | [STATUS] |

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

## UPDATE PROTOCOL

Agents MUST update after every directive:
1. Update task status in tasks.csv
2. Update burndown in burndown.csv
3. Regenerate DASHBOARD.md
4. Commit changes to orchestration/state/
```

### 1.7 Update Script

Create `orchestration/scripts/update_dashboard.py`:

```python
#!/usr/bin/env python3
"""
Regenerate DASHBOARD.md from CSV data sources.
Run after any task/project/sprint updates.
"""

import csv
from datetime import datetime
from pathlib import Path

STATE_DIR = Path('orchestration/state')

def load_csv(filename):
    with open(STATE_DIR / filename, 'r') as f:
        return list(csv.DictReader(f))

def count_by_status(tasks):
    counts = {}
    for t in tasks:
        status = t['status']
        counts[status] = counts.get(status, 0) + 1
    return counts

def generate_dashboard():
    projects = load_csv('projects.csv')
    tasks = load_csv('tasks.csv')
    sprints = load_csv('sprints.csv')
    burndown = load_csv('burndown.csv')
    
    # Calculate metrics
    task_counts = count_by_status(tasks)
    current_sprint = [s for s in sprints if s['status'] == 'in_progress'][0] if sprints else None
    
    # Generate markdown
    dashboard = f"""# SYNCRESCENDENT DASHBOARD
## Project Management Overview
**Generated**: {datetime.now().isoformat()}
**Current Sprint**: {current_sprint['name'] if current_sprint else 'None'}

---

## Initiative Status

| ID | Initiative | Status | Owner | Blocked By |
|----|------------|--------|-------|------------|
"""
    
    for p in projects:
        status_icon = {'in_progress': '🔄', 'blocked': '🚫', 'not_started': '⏸️', 'done': '✅'}.get(p['status'], '❓')
        dashboard += f"| {p['id']} | {p['name']} | {status_icon} {p['status'].replace('_', ' ').title()} | {p['owner']} | {p['blocked_by'] or '—'} |\n"
    
    dashboard += f"""
---

## Task Summary

- Not Started: {task_counts.get('not_started', 0)}
- In Progress: {task_counts.get('in_progress', 0)}
- Done: {task_counts.get('done', 0)}
- Blocked: {task_counts.get('blocked', 0)}

---

*Dashboard auto-generated. Update CSVs and re-run to refresh.*
"""
    
    with open(STATE_DIR / 'DASHBOARD.md', 'w') as f:
        f.write(dashboard)
    
    print(f"Dashboard updated: {STATE_DIR / 'DASHBOARD.md'}")

if __name__ == '__main__':
    generate_dashboard()
```

---

## PHASE 2: TRANSCRIPT NAMING CORRECTION

### 2.1 Sovereign's Standard

```
{YYYYMMDD}-{platform_format}-{full_channel_name}-{guest(if interview)}/{title(if not interview)}-{episode#}.txt
```

**Key distinctions**:
- `.txt` = Raw transcript (URL, Title, Date, More Info, Transcript with timestamps)
- `.md` = Processed transcript (cleaned, frontmatter)
- Use `TRANSCRIPT` not `SOURCE` as prefix consideration is NONE (just the date)

### 2.2 Platform_Format Values

| Value | Description |
|-------|-------------|
| `youtube_video` | Standard YouTube video (most interviews) |
| `youtube_lecture` | Educational/conference presentation |
| `youtube_panel` | Multi-person discussion |
| `youtube_tutorial` | How-to/instructional content |
| `podcast_interview` | Audio podcast interview |
| `podcast_solo` | Solo podcast episode |
| `x_thread` | Twitter/X thread |
| `substack_article` | Newsletter article |
| `arxiv_paper` | Academic paper |

### 2.3 Transformation Mapping

```python
# OLD (wrong):
# SOURCE-00000000-youtube-interview-dwarkesh_sutton-dwarkesh_sutton.md
# SOURCE-20250926-youtube-interview-dwarkesh_patel-richard_sutton.md

# NEW (correct):
# 20250926-youtube_video-dwarkesh_patel-richard_sutton.txt  (raw)
# 20250926-youtube_video-dwarkesh_patel-richard_sutton.md   (processed)
```

### 2.4 Execution Script

```bash
#!/bin/bash
# rename_transcripts.sh
# Apply Sovereign's naming standard to SOURCES/raw/

cd SOURCES/raw

# Create mapping file
echo "old_name,new_name" > ../rename_mapping.csv

for file in SOURCE-*; do
    if [[ -f "$file" ]]; then
        # Extract components from current name
        # SOURCE-{date}-{platform}-{format}-{creator}-{slug}.{ext}
        
        # Parse the filename
        base="${file%.*}"
        ext="${file##*.}"
        
        # Remove SOURCE- prefix
        without_prefix="${base#SOURCE-}"
        
        # Extract date (first 8 chars or 00000000)
        date="${without_prefix:0:8}"
        rest="${without_prefix:9}"
        
        # Parse remaining components
        # This is complex because the old format was inconsistent
        # We'll need to handle case-by-case
        
        # For now, create a simpler transformation:
        # Remove SOURCE- prefix, keep rest, fix platform_format
        
        # Replace "youtube-interview" with "youtube_video"
        new_name=$(echo "$without_prefix" | sed 's/youtube-interview/youtube_video/g' | sed 's/youtube-lecture/youtube_lecture/g' | sed 's/youtube-tutorial/youtube_tutorial/g')
        
        # Rename
        if [[ "$file" != "$new_name.$ext" ]]; then
            echo "$file,$new_name.$ext" >> ../rename_mapping.csv
            mv "$file" "$new_name.$ext"
            echo "Renamed: $file -> $new_name.$ext"
        fi
    fi
done

echo "Rename complete. Mapping saved to ../rename_mapping.csv"
```

### 2.5 Python Implementation (More Robust)

```python
#!/usr/bin/env python3
"""
rename_transcripts.py
Apply Sovereign's naming standard to SOURCES/raw/
"""

import os
import re
import csv
from pathlib import Path

SOURCES_RAW = Path('SOURCES/raw')
MAPPING_FILE = Path('SOURCES/rename_mapping.csv')

def parse_old_name(filename):
    """Parse the old SOURCE-* naming convention."""
    base = filename.rsplit('.', 1)[0]
    ext = filename.rsplit('.', 1)[1] if '.' in filename else ''
    
    # Remove SOURCE- prefix
    if base.startswith('SOURCE-'):
        base = base[7:]  # len('SOURCE-') = 7
    
    # Extract date (first 8 digits or 00000000)
    date_match = re.match(r'^(\d{8})-', base)
    if date_match:
        date = date_match.group(1)
        rest = base[9:]  # Skip date and hyphen
    else:
        date = '00000000'
        rest = base
    
    return date, rest, ext

def transform_to_new_standard(date, rest, ext):
    """Transform to Sovereign's standard."""
    # Replace platform-format with platform_format
    rest = rest.replace('youtube-interview', 'youtube_video')
    rest = rest.replace('youtube-lecture', 'youtube_lecture')
    rest = rest.replace('youtube-tutorial', 'youtube_tutorial')
    rest = rest.replace('youtube-panel', 'youtube_panel')
    rest = rest.replace('x-thread', 'x_thread')
    rest = rest.replace('podcast-interview', 'podcast_interview')
    
    # Construct new name
    new_name = f"{date}-{rest}.{ext}"
    
    return new_name

def main():
    mapping = []
    
    for filepath in SOURCES_RAW.iterdir():
        if filepath.is_file() and filepath.name.startswith('SOURCE-'):
            old_name = filepath.name
            date, rest, ext = parse_old_name(old_name)
            new_name = transform_to_new_standard(date, rest, ext)
            
            if old_name != new_name:
                new_path = filepath.parent / new_name
                
                # Check for conflicts
                if new_path.exists():
                    print(f"CONFLICT: {new_name} already exists, skipping {old_name}")
                    continue
                
                # Rename
                filepath.rename(new_path)
                mapping.append({'old_name': old_name, 'new_name': new_name})
                print(f"Renamed: {old_name} -> {new_name}")
    
    # Save mapping
    with open(MAPPING_FILE, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['old_name', 'new_name'])
        writer.writeheader()
        writer.writerows(mapping)
    
    print(f"\nRenamed {len(mapping)} files. Mapping saved to {MAPPING_FILE}")

if __name__ == '__main__':
    main()
```

### 2.6 Update sources.csv

After renaming, update sources.csv to reflect new filenames:

```python
#!/usr/bin/env python3
"""
update_sources_csv.py
Update sources.csv with new filenames after rename
"""

import csv
from pathlib import Path

SOURCES_CSV = Path('SOURCES/sources.csv')
RENAME_MAPPING = Path('SOURCES/rename_mapping.csv')

def main():
    # Load rename mapping
    mapping = {}
    with open(RENAME_MAPPING, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            old = row['old_name']
            new = row['new_name']
            mapping[old] = new
    
    # Update sources.csv
    rows = []
    with open(SOURCES_CSV, 'r') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            old_filename = row.get('filename', '')
            if old_filename in mapping:
                row['filename'] = mapping[old_filename]
                # Update filepath too
                old_path = row.get('filepath', '')
                if old_path:
                    row['filepath'] = old_path.replace(old_filename, mapping[old_filename])
            rows.append(row)
    
    # Write back
    with open(SOURCES_CSV, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Updated {len(mapping)} entries in sources.csv")

if __name__ == '__main__':
    main()
```

---

## PHASE 3: QUEUE RECONCILIATION

### 3.1 Audit QUEUE Contents

```bash
# Inventory QUEUE structure
echo "=== QUEUE Structure ==="
find QUEUE -type f -name "*.md" | head -30

# Count by directory
echo "=== Counts by Directory ==="
echo "modal1: $(find QUEUE/modal1 -type f | wc -l)"
echo "modal2: $(find QUEUE/modal2 -type f | wc -l)"
echo "pending: $(find QUEUE/pending -type f | wc -l)"

# Show file sizes
echo "=== File Sizes ==="
find QUEUE -type f -name "*.md" -exec wc -c {} \; | sort -rn | head -20
```

### 3.2 Map QUEUE to Roadmap

Create `orchestration/state/QUEUE_ROADMAP_MAPPING.md`:

```markdown
# QUEUE → ROADMAP MAPPING
## Reconciliation of Pending Work with Oracle Arc

**Audit Date**: 2026-01-02

---

## QUEUE/modal1/ (Current Capability Work)

| File | Size | Maps To | Oracle Scope | Status |
|------|------|---------|--------------|--------|
| AI_ECOSYSTEM_SURVEY.md | [SIZE] | PROJ-003 (Tooling Stack) | Oracle11 | Waiting |
| CONTENT_PROCESSING_QUEUE.md | [SIZE] | PROJ-001 (Transcript Ingestion) | Oracle9 | Active |
| QUICK_WINS.md | [SIZE] | [ASSESS] | [ASSESS] | [ASSESS] |
| YOUTUBE_PROCESSING_BACKLOG.md | [SIZE] | PROJ-001 (Transcript Ingestion) | Oracle9 | Active |

**Assessment**: [SUMMARY]

---

## QUEUE/modal2/ (Future Visual/Simulation Work)

| File | Size | Maps To | Oracle Scope | Status |
|------|------|---------|--------------|--------|
| AI_3D_VFX.md | [SIZE] | PROJ-009 (Modal 2 Prep) | Future | Parking lot |
| AI_Academic_Research.md | [SIZE] | [ASSESS] | [ASSESS] | [ASSESS] |
| AI_Image_Generators.md | [SIZE] | PROJ-009 (Modal 2 Prep) | Future | Parking lot |
| AI_Workflows_in_Video_and_VFX.md | [SIZE] | PROJ-009 (Modal 2 Prep) | Future | Parking lot |
| Physical_AI.md | [SIZE] | PROJ-009 (Modal 2 Prep) | Future | Parking lot |
| QUEUE-36200-SCREENPLAY_ORCHESTRATION.md | [SIZE] | PROJ-009 (Modal 2 Prep) | Future | Parking lot |
| The_Next_Wave_in_AI_Video_and_VFX.md | [SIZE] | PROJ-009 (Modal 2 Prep) | Future | Parking lot |

**Assessment**: Modal 2 content is correctly parked. Will activate when Modal 2 approaches.

---

## QUEUE/pending/ (Inbox - Should Be Zero)

| File | Size | Action | Destination |
|------|------|--------|-------------|
| operational_engine.md | [SIZE] | [TRIAGE] | [DESTINATION] |
| operational_engine.md.NOTE | [SIZE] | [TRIAGE] | [DESTINATION] |

**Assessment**: Inbox should be zero. These need immediate triage.

---

## Inbox Zero Status

- **Current pending items**: [COUNT]
- **Target**: 0
- **Action required**: Triage all pending items to modal1/, modal2/, or DELETE

---

## Recommendations

1. [Based on audit findings]
2. [Based on audit findings]
3. [Based on audit findings]
```

### 3.3 Triage Pending Items

```bash
# Examine pending items
cat QUEUE/pending/operational_engine.md | head -100
cat QUEUE/pending/operational_engine.md.NOTE 2>/dev/null

# Decision for each:
# If modal1 work → mv to QUEUE/modal1/
# If modal2 work → mv to QUEUE/modal2/
# If superseded → DELETE
# If needs processing → Leave in pending with note
```

### 3.4 Connect QUEUE to Project Management

Add QUEUE items to tasks.csv:

```csv
# Add to tasks.csv
TASK-009,null,Triage QUEUE/pending items,task,not_started,P1,Claude_Code,null,1,null,2026-01-02,2026-01-02,Achieve inbox zero
TASK-010,PROJ-001,Review CONTENT_PROCESSING_QUEUE.md,task,not_started,P2,Claude_Code,null,1,null,2026-01-02,2026-01-02,May have overlapping info with sources.csv
TASK-011,PROJ-001,Review YOUTUBE_PROCESSING_BACKLOG.md,task,not_started,P2,Claude_Code,null,1,null,2026-01-02,2026-01-02,May have additional sources not in SOURCES/raw
```

---

## PHASE 4: VERIFICATION AND COMMIT

### 4.1 Verification Commands

```bash
# Verify project management files created
ls -la orchestration/state/*.csv
ls -la orchestration/state/DASHBOARD.md

# Verify transcript renames
ls SOURCES/raw/ | grep -v "^SOURCE-" | head -20  # Should show renamed files
ls SOURCES/raw/ | grep "^SOURCE-" | wc -l  # Should be 0

# Verify sources.csv updated
head -5 SOURCES/sources.csv

# Verify QUEUE mapping created
cat orchestration/state/QUEUE_ROADMAP_MAPPING.md

# Verify inbox status
find QUEUE/pending -type f | wc -l  # Target: 0
```

### 4.2 Git Commit

```bash
git add -A
git commit -m "DIRECTIVE-034B: Project Management + Transcript Naming + QUEUE Reconciliation

PROJECT MANAGEMENT SYSTEM:
- Created projects.csv (9 initiatives)
- Created tasks.csv (tracking individual tasks)
- Created sprints.csv (iteration tracking)
- Created burndown.csv (velocity measurement)
- Created DASHBOARD.md (human-readable overview)
- Created update_dashboard.py (regeneration script)
- Supports Agile/Scrum/Kanban/Waterfall/PRINCE2

TRANSCRIPT NAMING:
- Renamed SOURCE-* to Sovereign's standard
- Format: {YYYYMMDD}-{platform_format}-{channel}-{guest/title}
- Updated sources.csv with new filenames
- Created rename_mapping.csv for reference

QUEUE RECONCILIATION:
- Created QUEUE_ROADMAP_MAPPING.md
- Mapped QUEUE items to roadmap initiatives
- Triaged pending items toward inbox zero
- Connected QUEUE to project tracking

Oracle9 operational infrastructure: ESTABLISHED."
```

---

## SUCCESS CRITERIA

### Phase 1: Project Management
- [ ] projects.csv created with all initiatives
- [ ] tasks.csv created with current work
- [ ] sprints.csv created with current sprint
- [ ] burndown.csv initialized
- [ ] DASHBOARD.md generates correctly
- [ ] update_dashboard.py functional

### Phase 2: Transcript Naming
- [ ] All SOURCE-* files renamed to Sovereign's standard
- [ ] No files begin with SOURCE- in SOURCES/raw/
- [ ] sources.csv updated with new filenames
- [ ] rename_mapping.csv documents transformations

### Phase 3: QUEUE Reconciliation
- [ ] QUEUE_ROADMAP_MAPPING.md created
- [ ] All QUEUE items mapped to roadmap
- [ ] QUEUE/pending/ at or approaching inbox zero
- [ ] QUEUE items added to tasks.csv

---

## EXECUTION LOG TEMPLATE

Save to: `orchestration/execution_logs/EXECUTION_LOG-2026-01-02-034B.md`

```markdown
# EXECUTION LOG: DIRECTIVE-034B
## Project Management + Transcript Naming + QUEUE Reconciliation

**Executed**: 2026-01-02
**Agent**: Claude Code
**Status**: [COMPLETE/INCOMPLETE]

---

## Phase 1: Project Management System

- projects.csv created: [Y/N] ([N] rows)
- tasks.csv created: [Y/N] ([N] rows)
- sprints.csv created: [Y/N]
- burndown.csv created: [Y/N]
- DASHBOARD.md generated: [Y/N]
- update_dashboard.py functional: [Y/N]

## Phase 2: Transcript Naming

- Files renamed: [N]
- Remaining SOURCE-* files: [N] (target: 0)
- sources.csv updated: [Y/N]
- rename_mapping.csv created: [Y/N]

## Phase 3: QUEUE Reconciliation

- QUEUE_ROADMAP_MAPPING.md created: [Y/N]
- QUEUE/modal1/ items: [N]
- QUEUE/modal2/ items: [N]
- QUEUE/pending/ items: [N] (target: 0)
- Items triaged: [N]

## Issues/Notes

[Any problems encountered]

## Dashboard Preview

[Paste generated DASHBOARD.md content]
```

---

## DELIVERABLES TO /outputs

1. All orchestration/state/*.csv files
2. orchestration/state/DASHBOARD.md
3. orchestration/scripts/update_dashboard.py
4. SOURCES/rename_mapping.csv
5. orchestration/state/QUEUE_ROADMAP_MAPPING.md
6. EXECUTION_LOG-2026-01-02-034B.md

---

**THIS DIRECTIVE ESTABLISHES OPERATIONAL VISIBILITY AND CONTROL.**
