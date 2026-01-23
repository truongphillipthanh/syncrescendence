# DIRECTIVE-041B: MCP CONFIGURATION + COORDINATION ARCHITECTURE
## Stream B — Automation Infrastructure (Permaculture Lens)

**Issued**: 2026-01-08
**Stream**: B (Claude 3)
**Priority**: P0 — CRITICAL
**Estimated Duration**: 90-120 minutes
**Parallel**: DIRECTIVE-041A executing simultaneously on Claude 2
**Project**: PROJ-011 (Automation Infrastructure)

---

## PREAMBLE

You are Claude 3, executing Stream B of Blitzkrieg 41. You have received this directive alongside ORACLE10_CONTEXT_v3.md. **READ THE CONTEXT FIRST.**

**Your mandate**: Configure MCP servers, create coordination architecture for multi-Claude execution, and build automation scripts to address the Permaculture lens failure (system not self-sustaining).

**Critical understanding**: This infrastructure enables the system to operate with minimal Principal intervention. Every automation reduces relay friction exponentially.

---

## PHASE 1: MCP CONFIGURATION (30 minutes)

### 1.1 Create Config Directory
```bash
mkdir -p config
```

### 1.2 Create MCP Configuration Documentation

Create `config/MCP_SETUP.md`:

```markdown
# MCP (Model Context Protocol) Configuration

## Overview
MCP enables Claude to interact with external services (GitHub, filesystem, databases) through a standardized protocol. This configuration supports multi-Claude coordination for Syncrescendence.

## Prerequisites
- Docker installed (for GitHub MCP server)
- Node.js 18+ (for local MCP servers)
- GitHub Personal Access Token with repo scope

## Server Configuration

### GitHub MCP Server
The official GitHub MCP server enables repository operations without manual git commands.

**Installation**:
```bash
# Pull the official image
docker pull ghcr.io/github/github-mcp-server

# Or use npx (requires Node.js)
npx @anthropic/github-mcp-server
```

**Configuration** (add to `~/.claude/.mcp.json`):
```json
{
  "mcpServers": {
    "github": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-e", "GITHUB_PERSONAL_ACCESS_TOKEN",
        "-e", "GITHUB_TOOLSETS=repos,issues,pull_requests",
        "ghcr.io/github/github-mcp-server"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_PAT}"
      }
    }
  }
}
```

**Available Toolsets**:
- `repos` - Repository management, file operations, branch creation
- `issues` - Issue creation, listing, commenting
- `pull_requests` - PR creation, review, merge
- `actions` - Workflow triggers, job logs

### Filesystem MCP Server
For direct filesystem operations across allowed paths.

**Configuration**:
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y", "@modelcontextprotocol/server-filesystem",
        "/Users/YOUR_USERNAME/syncrescendence",
        "/Users/YOUR_USERNAME/syncrescendence-alpha",
        "/Users/YOUR_USERNAME/syncrescendence-beta",
        "/Users/YOUR_USERNAME/syncrescendence-gamma"
      ]
    }
  }
}
```

## Security Notes
- Never commit tokens to repository
- Use environment variables for secrets
- Restrict toolsets to minimum required
- Use `GITHUB_READ_ONLY=1` for read-only instances

## Verification
```bash
# Test GitHub MCP
docker run -i --rm -e GITHUB_PERSONAL_ACCESS_TOKEN ghcr.io/github/github-mcp-server

# Check available tools
npx @anthropic/mcp-client list-tools
```
```

### 1.3 Create MCP JSON Template

Create `config/mcp.json.template`:

```json
{
  "mcpServers": {
    "github": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-e", "GITHUB_PERSONAL_ACCESS_TOKEN",
        "-e", "GITHUB_TOOLSETS=repos,issues,pull_requests",
        "ghcr.io/github/github-mcp-server"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_PAT}"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": [
        "-y", "@modelcontextprotocol/server-filesystem",
        "${SYNCRESCENDENCE_ROOT}",
        "${SYNCRESCENDENCE_ROOT}-alpha",
        "${SYNCRESCENDENCE_ROOT}-beta", 
        "${SYNCRESCENDENCE_ROOT}-gamma"
      ]
    }
  }
}
```

### 1.4 Verification
```bash
cat config/MCP_SETUP.md | head -40
cat config/mcp.json.template
```

---

## PHASE 2: COORDINATION ARCHITECTURE (30 minutes)

### 2.1 Create Coordination Configuration

Create `config/coordination.yaml`:

```yaml
# Syncrescendence Multi-Claude Coordination
# Defines zone ownership and conflict prevention

coordination:
  version: "1.0"
  updated: "2026-01-08"
  
  # Account definitions
  accounts:
    alpha:
      name: "Claude Instance Alpha"
      role: "Primary executor"
      worktree: "../syncrescendence-alpha"
      branch_prefix: "alpha/"
      
    beta:
      name: "Claude Instance Beta"
      role: "Parallel executor"
      worktree: "../syncrescendence-beta"
      branch_prefix: "beta/"
      
    gamma:
      name: "Claude Instance Gamma"
      role: "Verification/overflow"
      worktree: "../syncrescendence-gamma"
      branch_prefix: "gamma/"
      
    oracle:
      name: "Oracle Thread"
      role: "Strategic synthesis (Claude Desktop)"
      worktree: null
      branch_prefix: null
      notes: "Read-only access via GitHub connector"

  # Zone ownership (exclusive write access)
  zones:
    alpha:
      writable:
        - "04-SOURCES/processed/a-*"
        - "00-ORCHESTRATION/execution_logs/*-A.md"
      description: "Stream A processing and logging"
      
    beta:
      writable:
        - "04-SOURCES/processed/b-*"
        - "00-ORCHESTRATION/execution_logs/*-B.md"
      description: "Stream B processing and logging"
      
    gamma:
      writable:
        - "04-SOURCES/processed/c-*"
        - "00-ORCHESTRATION/execution_logs/*-C.md"
      description: "Stream C processing and logging"
      
    shared:
      writable:
        - "00-ORCHESTRATION/state/*.csv"
        - "04-SOURCES/sources.csv"
      pattern: "append_only"
      description: "Ledgers use append-only pattern with row-level locking"

  # Protected zones (require Principal approval)
  protected:
    - "01-CANON/"
    - "00-ORCHESTRATION/oracle_contexts/"
    - "CLAUDE.md"
    - "config/coordination.yaml"

  # Conflict resolution
  conflict_resolution:
    strategy: "branch_per_instance"
    merge_target: "develop"
    merge_method: "rebase"
    notes: |
      Each instance works in isolated branch.
      PRs merge to develop branch.
      Main branch updated only after verification.

  # Communication patterns
  communication:
    oracle_to_code:
      method: "directive_files"
      location: "00-ORCHESTRATION/directives/"
      pattern: "DIRECTIVE-{number}{stream}.md"
      
    code_to_oracle:
      method: "execution_logs"
      location: "00-ORCHESTRATION/execution_logs/"
      pattern: "EXECUTION_LOG-{date}-{directive}.md"
      
    inter_instance:
      method: "git_branches"
      notes: "No direct communication; coordinate via shared repository"
```

### 2.2 Create Worktree Setup Script

Create `00-ORCHESTRATION/scripts/setup-worktrees.sh`:

```bash
#!/bin/zsh
# setup-worktrees.sh
# Create git worktrees for multi-Claude coordination

set -e

REPO_ROOT=$(git rev-parse --show-toplevel)
PARENT_DIR=$(dirname "$REPO_ROOT")

echo "=== Syncrescendence Worktree Setup ==="
echo "Repository: $REPO_ROOT"
echo "Parent: $PARENT_DIR"
echo ""

# Ensure we're on develop branch
git checkout develop 2>/dev/null || git checkout -b develop

# Create worktrees
echo "Creating worktrees..."

if [ ! -d "$PARENT_DIR/syncrescendence-alpha" ]; then
    git worktree add "$PARENT_DIR/syncrescendence-alpha" -b alpha/work
    echo "  Created: syncrescendence-alpha"
else
    echo "  Exists: syncrescendence-alpha"
fi

if [ ! -d "$PARENT_DIR/syncrescendence-beta" ]; then
    git worktree add "$PARENT_DIR/syncrescendence-beta" -b beta/work
    echo "  Created: syncrescendence-beta"
else
    echo "  Exists: syncrescendence-beta"
fi

if [ ! -d "$PARENT_DIR/syncrescendence-gamma" ]; then
    git worktree add "$PARENT_DIR/syncrescendence-gamma" -b gamma/work
    echo "  Created: syncrescendence-gamma"
else
    echo "  Exists: syncrescendence-gamma"
fi

# Copy local settings template to each worktree
echo ""
echo "Copying local settings templates..."
for instance in alpha beta gamma; do
    WORKTREE="$PARENT_DIR/syncrescendence-$instance"
    if [ -d "$WORKTREE" ]; then
        mkdir -p "$WORKTREE/.claude"
        if [ -f "$REPO_ROOT/.claude/settings.local.json.template" ]; then
            cp "$REPO_ROOT/.claude/settings.local.json.template" \
               "$WORKTREE/.claude/settings.local.json"
            # Update instance name in the copy
            sed -i '' "s/\[ALPHA|BETA|GAMMA\]/$instance/g" \
                "$WORKTREE/.claude/settings.local.json"
            echo "  Configured: $instance"
        fi
    fi
done

echo ""
echo "=== Worktree Setup Complete ==="
echo ""
echo "Worktrees created:"
git worktree list
echo ""
echo "Next steps:"
echo "  1. Each Claude instance should cd to its assigned worktree"
echo "  2. Configure .claude/settings.local.json with account-specific settings"
echo "  3. Use branch prefixes for commits (alpha/, beta/, gamma/)"
```

### 2.3 Make Script Executable
```bash
chmod +x 00-ORCHESTRATION/scripts/setup-worktrees.sh
```

### 2.4 Verification
```bash
cat config/coordination.yaml | head -50
cat 00-ORCHESTRATION/scripts/setup-worktrees.sh | head -30
```

---

## PHASE 3: AUTOMATION SCRIPTS (30 minutes)

### 3.1 Create Ledger Sync Script

Create `00-ORCHESTRATION/scripts/sync_ledgers.py`:

```python
#!/usr/bin/env python3
"""
sync_ledgers.py
Atomic ledger synchronization with validation.

Usage:
    python sync_ledgers.py --ledger tasks --action add --data '{"id":"TASK-XXX",...}'
    python sync_ledgers.py --ledger tasks --action update --id TASK-001 --field status --value done
    python sync_ledgers.py --validate
"""

import argparse
import csv
import json
import os
import shutil
from datetime import datetime
from pathlib import Path

# Ledger paths
LEDGERS = {
    'tasks': Path('00-ORCHESTRATION/state/tasks.csv'),
    'projects': Path('00-ORCHESTRATION/state/projects.csv'),
    'sprints': Path('00-ORCHESTRATION/state/sprints.csv'),
    'burndown': Path('00-ORCHESTRATION/state/burndown.csv'),
    'sources': Path('04-SOURCES/sources.csv'),
}

# Required columns per ledger
REQUIRED_COLUMNS = {
    'tasks': ['id', 'project_id', 'name', 'type', 'status', 'priority', 'owner'],
    'projects': ['id', 'name', 'type', 'status', 'priority', 'owner'],
    'sprints': ['id', 'name', 'start_date', 'end_date', 'status'],
    'burndown': ['date', 'sprint_id', 'total_points', 'completed_points'],
    'sources': ['id', 'filename', 'status'],
}


def backup_ledger(ledger_path: Path) -> Path:
    """Create timestamped backup."""
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    backup_path = ledger_path.with_suffix(f'.csv.bak.{timestamp}')
    shutil.copy(ledger_path, backup_path)
    return backup_path


def validate_ledger(ledger_name: str) -> tuple[bool, str]:
    """Validate ledger structure and content."""
    path = LEDGERS.get(ledger_name)
    if not path or not path.exists():
        return False, f"Ledger not found: {ledger_name}"
    
    required = REQUIRED_COLUMNS.get(ledger_name, [])
    
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        
        # Check required columns
        missing = [col for col in required if col not in headers]
        if missing:
            return False, f"Missing columns: {missing}"
        
        # Check for malformed rows
        row_count = 0
        for row in reader:
            row_count += 1
            if len(row) != len(headers):
                return False, f"Malformed row {row_count}: column count mismatch"
    
    return True, f"Valid: {row_count} rows"


def atomic_write(ledger_path: Path, rows: list, fieldnames: list) -> bool:
    """Write ledger atomically via temp file."""
    temp_path = ledger_path.with_suffix('.csv.tmp')
    
    try:
        with open(temp_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        
        # Validate temp file
        with open(temp_path, 'r') as f:
            reader = csv.DictReader(f)
            temp_rows = list(reader)
            if len(temp_rows) != len(rows):
                raise ValueError("Row count mismatch after write")
        
        # Atomic rename
        os.replace(temp_path, ledger_path)
        return True
        
    except Exception as e:
        if temp_path.exists():
            temp_path.unlink()
        raise e


def add_row(ledger_name: str, data: dict) -> str:
    """Add row to ledger."""
    path = LEDGERS[ledger_name]
    backup = backup_ledger(path)
    
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)
    
    rows.append(data)
    atomic_write(path, rows, fieldnames)
    
    return f"Added row to {ledger_name}. Backup: {backup.name}"


def update_row(ledger_name: str, row_id: str, field: str, value: str) -> str:
    """Update specific field in row."""
    path = LEDGERS[ledger_name]
    backup = backup_ledger(path)
    
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)
    
    updated = False
    for row in rows:
        if row.get('id') == row_id:
            row[field] = value
            row['updated'] = datetime.now().strftime('%Y-%m-%d')
            updated = True
            break
    
    if not updated:
        return f"Row not found: {row_id}"
    
    atomic_write(path, rows, fieldnames)
    return f"Updated {row_id}.{field} = {value}. Backup: {backup.name}"


def validate_all() -> None:
    """Validate all ledgers."""
    print("=== Ledger Validation ===\n")
    for name in LEDGERS:
        valid, message = validate_ledger(name)
        status = "✓" if valid else "✗"
        print(f"{status} {name}: {message}")


def main():
    parser = argparse.ArgumentParser(description='Ledger synchronization')
    parser.add_argument('--ledger', choices=list(LEDGERS.keys()))
    parser.add_argument('--action', choices=['add', 'update', 'validate'])
    parser.add_argument('--data', help='JSON data for add action')
    parser.add_argument('--id', help='Row ID for update action')
    parser.add_argument('--field', help='Field name for update action')
    parser.add_argument('--value', help='New value for update action')
    parser.add_argument('--validate', action='store_true', help='Validate all ledgers')
    
    args = parser.parse_args()
    
    if args.validate:
        validate_all()
        return
    
    if args.action == 'add':
        data = json.loads(args.data)
        result = add_row(args.ledger, data)
        print(result)
    
    elif args.action == 'update':
        result = update_row(args.ledger, args.id, args.field, args.value)
        print(result)
    
    elif args.action == 'validate':
        valid, message = validate_ledger(args.ledger)
        print(f"{'✓' if valid else '✗'} {message}")


if __name__ == '__main__':
    main()
```

### 3.2 Create Verification Script

Create `00-ORCHESTRATION/scripts/verify_all.sh`:

```bash
#!/bin/zsh
# verify_all.sh
# Comprehensive repository verification

set -e

echo "╔════════════════════════════════════════╗"
echo "║   Syncrescendence Verification Suite   ║"
echo "╚════════════════════════════════════════╝"
echo ""

# Structure verification
echo "┌─ Structure Verification ─────────────────"
echo -n "│ Unexpected subdirectories: "
SUBDIRS=$(find . -mindepth 2 -type d -name "scaffolding" 2>/dev/null | wc -l | tr -d ' ')
if [ "$SUBDIRS" -eq 0 ]; then
    echo "✓ 0"
else
    echo "✗ $SUBDIRS"
fi

echo -n "│ Root .md files: "
ROOT_MD=$(ls *.md 2>/dev/null | wc -l | tr -d ' ')
if [ "$ROOT_MD" -le 2 ]; then  # CLAUDE.md and README.md allowed
    echo "✓ $ROOT_MD"
else
    echo "✗ $ROOT_MD (expected ≤2)"
fi

echo -n "│ Directory count: "
DIR_COUNT=$(ls -d */ 2>/dev/null | wc -l | tr -d ' ')
echo "$DIR_COUNT"
echo "└──────────────────────────────────────────"
echo ""

# Ledger verification
echo "┌─ Ledger Verification ───────────────────"
echo -n "│ tasks.csv: "
if [ -f "00-ORCHESTRATION/state/tasks.csv" ]; then
    TASKS=$(wc -l < 00-ORCHESTRATION/state/tasks.csv | tr -d ' ')
    DONE=$(grep -c ',done,' 00-ORCHESTRATION/state/tasks.csv 2>/dev/null || echo 0)
    echo "✓ $TASKS rows ($DONE done)"
else
    echo "✗ Not found"
fi

echo -n "│ projects.csv: "
if [ -f "00-ORCHESTRATION/state/projects.csv" ]; then
    PROJECTS=$(wc -l < 00-ORCHESTRATION/state/projects.csv | tr -d ' ')
    COMPLETE=$(grep -c ',complete,' 00-ORCHESTRATION/state/projects.csv 2>/dev/null || echo 0)
    echo "✓ $PROJECTS rows ($COMPLETE complete)"
else
    echo "✗ Not found"
fi

echo -n "│ sources.csv: "
if [ -f "04-SOURCES/sources.csv" ]; then
    SOURCES=$(wc -l < 04-SOURCES/sources.csv | tr -d ' ')
    PROCESSED=$(grep -c ',processed,' 04-SOURCES/sources.csv 2>/dev/null || echo 0)
    echo "✓ $SOURCES rows ($PROCESSED processed)"
else
    echo "✗ Not found"
fi
echo "└──────────────────────────────────────────"
echo ""

# Content verification
echo "┌─ Content Verification ──────────────────"
echo -n "│ CANON files: "
CANON=$(ls 01-CANON/*.md 2>/dev/null | wc -l | tr -d ' ')
echo "$CANON"

echo -n "│ Processed sources: "
PROC_SOURCES=$(ls 04-SOURCES/processed/*.md 2>/dev/null | wc -l | tr -d ' ')
echo "$PROC_SOURCES"

echo -n "│ CANON with integrations: "
INTEGRATIONS=$(grep -l "SOURCE-" 01-CANON/*.md 2>/dev/null | wc -l | tr -d ' ')
echo "$INTEGRATIONS"

echo -n "│ Function XMLs: "
FUNCTIONS=$(ls 02-ENGINE/*.xml 2>/dev/null | wc -l | tr -d ' ')
echo "$FUNCTIONS"
echo "└──────────────────────────────────────────"
echo ""

# Git status
echo "┌─ Git Status ────────────────────────────"
CHANGES=$(git status --short | wc -l | tr -d ' ')
if [ "$CHANGES" -eq 0 ]; then
    echo "│ Working tree: ✓ Clean"
else
    echo "│ Working tree: ⚠ $CHANGES uncommitted changes"
    git status --short | head -10 | sed 's/^/│   /'
fi

BRANCH=$(git branch --show-current)
echo "│ Current branch: $BRANCH"
echo "└──────────────────────────────────────────"
echo ""

# Summary
echo "═══════════════════════════════════════════"
echo "Verification complete: $(date '+%Y-%m-%d %H:%M:%S')"
echo "═══════════════════════════════════════════"
```

### 3.3 Create Tree Generator Enhancement

Update `00-ORCHESTRATION/scripts/update_dashboard.py` to include verification:

```python
#!/usr/bin/env python3
"""
update_dashboard.py
Generate dashboard with current repository state.
"""

import subprocess
from datetime import datetime
from pathlib import Path

STATE_DIR = Path('00-ORCHESTRATION/state')

def count_files(pattern: str) -> int:
    """Count files matching pattern."""
    try:
        result = subprocess.run(
            f'ls {pattern} 2>/dev/null | wc -l',
            shell=True, capture_output=True, text=True
        )
        return int(result.stdout.strip())
    except:
        return 0

def count_csv_rows(path: str) -> int:
    """Count rows in CSV (excluding header)."""
    try:
        result = subprocess.run(
            f'wc -l < {path}',
            shell=True, capture_output=True, text=True
        )
        return max(0, int(result.stdout.strip()) - 1)
    except:
        return 0

def count_csv_status(path: str, status: str) -> int:
    """Count rows with specific status."""
    try:
        result = subprocess.run(
            f"grep -c ',{status},' {path}",
            shell=True, capture_output=True, text=True
        )
        return int(result.stdout.strip())
    except:
        return 0

def generate_dashboard():
    """Generate dashboard markdown."""
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Gather metrics
    canon_files = count_files('01-CANON/*.md')
    processed_sources = count_files('04-SOURCES/processed/*.md')
    raw_sources = count_files('04-SOURCES/raw/*.txt')
    function_xmls = count_files('02-ENGINE/*.xml')
    
    tasks_total = count_csv_rows('00-ORCHESTRATION/state/tasks.csv')
    tasks_done = count_csv_status('00-ORCHESTRATION/state/tasks.csv', 'done')
    
    projects_total = count_csv_rows('00-ORCHESTRATION/state/projects.csv')
    projects_complete = count_csv_status('00-ORCHESTRATION/state/projects.csv', 'complete')
    
    sources_total = count_csv_rows('04-SOURCES/sources.csv')
    sources_processed = count_csv_status('04-SOURCES/sources.csv', 'processed')
    
    dashboard = f"""# Syncrescendence Dashboard

**Generated**: {now}

## Repository Metrics

| Category | Count | Notes |
|----------|-------|-------|
| CANON files | {canon_files} | Canonical knowledge |
| Processed sources | {processed_sources} | Qualified briefs |
| Raw sources | {raw_sources} | Pending processing |
| Function XMLs | {function_xmls} | Operational metaprompts |

## Ledger Status

### Tasks
- Total: {tasks_total}
- Done: {tasks_done}
- Completion: {(tasks_done/tasks_total*100):.1f}% (if tasks_total > 0 else 'N/A')

### Projects
- Total: {projects_total}
- Complete: {projects_complete}

### Sources
- Total: {sources_total}
- Processed: {sources_processed}
- Processing rate: {(sources_processed/sources_total*100):.1f}% (if sources_total > 0 else 'N/A')

## Quick Commands

```bash
make verify         # Run verification suite
make sync           # Git pull/push
make update-ledgers # Ledger status report
make tree           # Regenerate tree
```

---
*Auto-generated. Run `python 00-ORCHESTRATION/scripts/update_dashboard.py` to refresh.*
"""
    
    with open(STATE_DIR / 'DYN-DASHBOARD.md', 'w') as f:
        f.write(dashboard)
    
    print(f"Dashboard updated: {STATE_DIR / 'DYN-DASHBOARD.md'}")


if __name__ == '__main__':
    generate_dashboard()
```

### 3.4 Make Scripts Executable
```bash
chmod +x 00-ORCHESTRATION/scripts/sync_ledgers.py
chmod +x 00-ORCHESTRATION/scripts/verify_all.sh
chmod +x 00-ORCHESTRATION/scripts/update_dashboard.py
```

### 3.5 Verification
```bash
python3 00-ORCHESTRATION/scripts/sync_ledgers.py --validate
./00-ORCHESTRATION/scripts/verify_all.sh
```

---

## PHASE 4: UPDATE LEDGERS (15 minutes)

### 4.1 Add Tasks for Stream B

Add to tasks.csv:
```
TASK-044,PROJ-011,Create MCP configuration,infrastructure,done,P0,Claude_Code_3,null,0.5,{actual},2026-01-08,2026-01-08,MCP_SETUP.md and mcp.json.template
TASK-045,PROJ-011,Create coordination.yaml,infrastructure,done,P0,Claude_Code_3,null,0.5,{actual},2026-01-08,2026-01-08,Multi-Claude zone ownership defined
TASK-046,PROJ-011,Create worktree setup script,infrastructure,done,P0,Claude_Code_3,null,0.25,{actual},2026-01-08,2026-01-08,setup-worktrees.sh
TASK-047,PROJ-011,Create automation scripts,infrastructure,done,P0,Claude_Code_3,null,0.5,{actual},2026-01-08,2026-01-08,sync_ledgers.py verify_all.sh update_dashboard.py
```

### 4.2 Update PROJ-011 Status

If Stream A completed successfully, update PROJ-011 status to `complete`.

### 4.3 Verification
```bash
grep "TASK-04" 00-ORCHESTRATION/state/tasks.csv | wc -l
python3 00-ORCHESTRATION/scripts/sync_ledgers.py --validate
```

---

## PHASE 5: GIT COMMIT + VERIFICATION (10 minutes)

### 5.1 Stage and Commit
```bash
git add config/ 00-ORCHESTRATION/scripts/
git add 00-ORCHESTRATION/state/tasks.csv
git commit -m "feat(PROJ-011): Deploy MCP config, coordination architecture, automation scripts

- Add config/MCP_SETUP.md with server documentation
- Add config/mcp.json.template for MCP configuration
- Add config/coordination.yaml with zone ownership
- Add setup-worktrees.sh for multi-Claude isolation
- Add sync_ledgers.py for atomic CSV operations
- Add verify_all.sh comprehensive verification
- Update update_dashboard.py with metrics

Addresses Permaculture lens failure (18-lens #14).
Part of Blitzkrieg 41, Stream B."
```

### 5.2 Final Verification
```bash
./00-ORCHESTRATION/scripts/verify_all.sh
```

### 5.3 Create Execution Log

Create `00-ORCHESTRATION/execution_logs/EXECUTION_LOG-2026-01-08-041B.md` with:
- All phases completed
- Verification outputs
- Files created/modified
- Task status updates

---

## SUCCESS CRITERIA

Stream B is complete when:
- [ ] `cat config/MCP_SETUP.md` shows MCP documentation
- [ ] `cat config/mcp.json.template` shows server configuration
- [ ] `cat config/coordination.yaml` shows zone ownership
- [ ] `./00-ORCHESTRATION/scripts/setup-worktrees.sh` is executable
- [ ] `python3 00-ORCHESTRATION/scripts/sync_ledgers.py --validate` passes
- [ ] `./00-ORCHESTRATION/scripts/verify_all.sh` runs successfully
- [ ] `grep TASK-04 00-ORCHESTRATION/state/tasks.csv | wc -l` returns 8+ (combined with Stream A)
- [ ] Git commit completed with semantic message
- [ ] Execution log created with verification outputs

---

## ANTI-PATTERNS

**DO NOT**:
- Skip MCP documentation (it's for future Principal reference)
- Create coordination.yaml without zone ownership
- Make scripts without making them executable
- Forget atomic write patterns in sync_ledgers.py
- Claim complete without running verify_all.sh

**DO**:
- Execute each phase completely
- Test scripts after creation
- Use exact paths specified
- Update ledgers atomically
- Include verification outputs in log

---

## PROJ-011 COMPLETION GATE

After both streams complete, verify PROJ-011 success:

```bash
# Stream A deliverables
cat CLAUDE.md | wc -l                        # ~70-80 lines
ls .claude/commands/project/ | wc -l         # 4 files
cat Makefile | grep -c "^[a-z]*:"            # 5+ targets

# Stream B deliverables
cat config/coordination.yaml | wc -l         # ~80+ lines
ls 00-ORCHESTRATION/scripts/*.sh | wc -l     # 2+ scripts
ls 00-ORCHESTRATION/scripts/*.py | wc -l     # 2+ scripts

# Combined verification
./00-ORCHESTRATION/scripts/verify_all.sh
make verify
```

If all pass: Update PROJ-011 to `complete`, PROJ-002 to `in_progress` (now unblocked by automation infrastructure).

---

*Permaculture lens addressed. Self-sustaining patterns established. System can operate with minimal Principal intervention.*
