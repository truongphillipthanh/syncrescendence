# Claude Code optimization architecture for Syncrescendence

**MCP-enabled multi-Claude orchestration can eliminate most manual Principal relay bottlenecks**, but direct Oracle→Claude Code communication requires shared-state intermediaries—GitHub MCP, claude-flow's ReasoningBank, or filesystem-based coordination—rather than native Claude-to-Claude messaging. The architecture recommended here uses GitHub as the single source of truth, git worktrees for conflict-free parallel execution across 3 Claude Pro accounts, and a layered memory hierarchy that separates committed team knowledge (CLAUDE.md) from ephemeral session context.

The core friction in your current workflow—manual Principal relay between Oracle threads and Claude Code instances—can be reduced **60-80%** through automation pipelines that leverage Claude Code's headless mode (`-p` flag), MCP servers for GitHub operations, and slash commands that encode your Oracle synthesis patterns into repeatable workflows. The remaining 20-40% requiring human oversight covers security-critical commits, architectural decisions, and production deployments.

---

## CLAUDE.md specification for knowledge management systems

Claude Code reads CLAUDE.md files in a **hierarchical priority order**: Enterprise policy (`/Library/Application Support/ClaudeCode/CLAUDE.md` on macOS), Project memory (`./CLAUDE.md`), User memory (`~/.claude/CLAUDE.md`), and Project-local overrides (`./CLAUDE.local.md`, auto-gitignored). Files at each directory level are loaded recursively upward to the filesystem root, with **subdirectory CLAUDE.md files loaded on-demand** when Claude accesses those paths.

The extended thinking triggers work exclusively in Claude Code CLI (not claude.ai web or API): `"think"` allocates ~4,000 tokens, `"megathink"` allocates ~10,000 tokens, and **`"ultrathink"` allocates the maximum ~31,999 tokens**. These keywords must appear naturally in your prompts—Claude Code's JavaScript parses them from prompt text. Custom slash commands live in `.claude/commands/` with `.md` files supporting YAML frontmatter for `allowed-tools`, `description`, and argument placeholders (`$ARGUMENTS`, `$1`, `$2`).

The import syntax `@path/to/file` allows CLAUDE.md to reference external documentation without bloating the base context. Maximum recursion depth is 5 hops. For your 7-directory structure, use progressive disclosure—reference but don't embed the full content of each directory's specialized documentation.

### Complete CLAUDE.md template for Syncrescendence

```markdown
# Syncrescendence Knowledge Management System

## Constitutional Rules
1. NEVER modify files in 00-ORCHESTRATION without explicit Principal approval
2. All ledger updates must use atomic write patterns (temp file → validation → rename)
3. Verify processing claims before marking tasks complete—use subagents when uncertain
4. When working across multiple directories, read CLAUDE.md in each before modifying
5. Commit frequently with semantic prefixes: feat:, fix:, docs:, chore:, refactor:

## Architecture Overview
Syncrescendence operates as a multi-Claude coordination system with:
- 3 parallel Claude Pro accounts executing A/B streams
- Oracle synthesis sessions coordinating strategic direction
- GitHub repository as single source of truth

See @docs/architecture.md for system design
See @docs/processing-workflows.md for standard operations

## Directory Structure
- `00-ORCHESTRATION/` - Strategic coordination, Oracle directives (PROTECTED)
- `01-FOUNDATIONS/` - Core schemas, taxonomies, constitutional documents
- `02-INTAKE/` - Raw source ingestion, pending processing
- `03-PROCESSING/` - Active transformation pipelines
- `04-CANON/` - Verified, immutable reference knowledge
- `05-OPERATIONAL/` - Working state, ledgers, indexes (mutable)
- `06-EXEMPLA/` - Templates, patterns, examples

## Critical Commands
```bash
make verify              # Run all validation checks
make process-queue       # Process pending intake items
make update-ledgers      # Sync CSV ledgers with validation
make sync                # Pull latest, rebase, push
```

## Processing Patterns
- Source intake: @docs/processing/intake-workflow.md
- Ledger updates: @docs/processing/ledger-protocol.md
- Canon promotion: @docs/processing/canonicalization.md

## Verification Requirements (MANDATORY before completing any task)
1. Run `make lint` - code style validation
2. Run `make test` - unit test suite
3. Run `make validate-schemas` - JSON/CSV schema compliance
4. Confirm no uncommitted changes to 00-ORCHESTRATION

## Anti-Patterns to AVOID
- Modifying ledger CSVs without atomic write wrapper
- Committing directly to main branch without PR
- Running ultrathink for simple lookup tasks (cost inefficient)
- Skipping verification steps to "save time"
- Storing secrets or API keys in any committed file

## Session Management
- Use /compact before context fills; summarize key decisions
- Maintain active session notes in 05-OPERATIONAL/session-state/
- Name sessions descriptively for later resumption

## Multi-Claude Coordination
- Each account operates in dedicated git worktree
- Write exclusively to assigned zones per coordination.yaml
- Shared files use append-only patterns
- Conflicts resolved via PR integration on develop branch
```

---

## Custom slash command specifications

The four requested commands encode your Oracle-directed workflows into repeatable, automated operations. Each command file goes in `.claude/commands/project/` for the `/project:` namespace.

### `/project:process-source` command

```markdown
---
name: process-source
description: Process a source document from intake through canonicalization
allowed-tools: Read, Write, Edit, Bash(python:*), Bash(make:*), Glob, Grep
---
# Process Source Document

Process the source document: $ARGUMENTS

## Workflow
1. **Locate source**: Find the document in 02-INTAKE/ using Glob
2. **Read metadata**: Extract bibliographic information, dates, provenance
3. **Schema validation**: Run `make validate-schema -- "$1"` to check structure
4. **Content extraction**: Parse key concepts, entities, relationships
5. **Cross-reference check**: Search 04-CANON/ for related existing entries
6. **Transform**: Apply processing templates from 06-EXEMPLA/templates/
7. **Stage**: Move processed output to 03-PROCESSING/staged/
8. **Update ledgers**: Add entry to sources.csv and processing_log.csv
9. **Verification**: Run `make verify` to confirm all checks pass

## Output
- Processed document in 03-PROCESSING/staged/
- Updated sources.csv with new entry
- Processing log entry with timestamp and status

IMPORTANT: Do not promote to 04-CANON without explicit Principal approval.
```

### `/project:update-ledgers` command

```markdown
---
name: update-ledgers
description: Safely update CSV ledgers with atomic writes and validation
allowed-tools: Read, Write, Bash(python:*), Bash(make:*)
---
# Update Ledgers Safely

Update the specified ledger with: $ARGUMENTS

## Safety Protocol
1. **Backup**: Create timestamped backup in 05-OPERATIONAL/ledgers/.backups/
2. **Lock check**: Verify no .lock file exists for target ledger
3. **Create lock**: Touch .lock file with current timestamp
4. **Load existing**: Read current CSV into memory
5. **Apply changes**: Add/modify rows per instruction
6. **Validate schema**: Run Python validator against ledger schema
7. **Atomic write**: Write to temp file, validate, rename to final
8. **Update indexes**: Regenerate any dependent index files
9. **Release lock**: Remove .lock file
10. **Verify**: Run `make validate-ledgers` to confirm integrity

## Error Recovery
If any step fails:
- Do NOT proceed to subsequent steps
- Report the failure point clearly
- Keep backup intact for manual recovery
- Remove lock file to prevent deadlock

## Supported Ledgers
- tasks.csv: Task tracking (id, title, status, assignee, created, updated)
- projects.csv: Project registry (id, name, phase, priority, dependencies)
- sources.csv: Source documents (id, title, author, date, path, status)
```

### `/project:verify` command

```markdown
---
name: verify
description: Run comprehensive verification across the knowledge base
allowed-tools: Bash(make:*), Bash(python:*), Read, Grep
---
# Comprehensive Verification

Run all verification checks for the knowledge base.

## Verification Suite
1. **Lint**: `make lint` - Code style and formatting
2. **Types**: `make typecheck` - Python type validation
3. **Schemas**: `make validate-schemas` - JSON/YAML schema compliance
4. **Ledgers**: `make validate-ledgers` - CSV integrity and cross-references
5. **Links**: `make check-links` - Internal reference validation
6. **Git status**: Confirm working tree is clean or list uncommitted changes
7. **Tests**: `make test` - Run unit test suite

## Output Report
Generate verification report in format:
```
=== Verification Report ===
Timestamp: [ISO-8601]
Lint:      [PASS/FAIL] [details if fail]
Types:     [PASS/FAIL] [details if fail]
Schemas:   [PASS/FAIL] [details if fail]
Ledgers:   [PASS/FAIL] [details if fail]
Links:     [PASS/FAIL] [details if fail]
Git:       [CLEAN/DIRTY] [list if dirty]
Tests:     [PASS/FAIL] [X/Y passed]
=== Overall: [PASS/FAIL] ===
```

If all checks pass, report ready for commit/push.
If any fail, list specific failures with remediation suggestions.
```

### `/project:blitzkrieg` command

```markdown
---
name: blitzkrieg
description: Rapid parallel processing of multiple intake items
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---
# Blitzkrieg Processing Mode

Ultrathink about the optimal parallel processing strategy, then execute rapid processing of pending intake items.

## Pre-flight
1. Count items in 02-INTAKE/pending/
2. Assess complexity distribution (simple/medium/complex)
3. Check current context capacity - if >60% full, use /compact first
4. Verify all ledgers are unlocked

## Execution Strategy
For batch of items: $ARGUMENTS (or all pending if not specified)

### Phase 1: Triage (5 minutes max)
- Categorize all items by type and complexity
- Identify dependencies between items
- Flag any requiring special handling

### Phase 2: Parallel Processing
- Process simple items first (build momentum)
- Group related items for batch context efficiency
- Use subagents for independent verification

### Phase 3: Ledger Consolidation
- Batch all ledger updates (single atomic operation per ledger)
- Validate cross-references
- Update processing_log.csv with batch entry

### Phase 4: Verification
- Run /project:verify
- Report items successfully processed vs. failures
- Stage failures for manual review

## Constraints
- Maximum 10 items per blitzkrieg session
- Stop immediately if any critical validation fails
- Document any assumptions made during rapid processing

## Output
Summary report with:
- Items processed: X/Y
- Processing time: Z minutes
- Items requiring follow-up: [list]
- Next recommended action
```

---

## MCP server configuration for macOS

The MCP architecture enables Claude to interact with external tools and services. For Syncrescendence's multi-account coordination, three MCP servers are essential: GitHub (repository operations), claude-flow (multi-agent swarm orchestration), and optionally Zilliz context (semantic code search for large corpora).

**Important deprecation notice**: The npm package `@modelcontextprotocol/server-github` is deprecated as of April 2025. Development moved to `github/github-mcp-server`, GitHub's official Go-based implementation with **24.5k stars and 31 releases** as of January 2026.

### Recommended MCP configuration for macOS

Create or update `~/.claude/.mcp.json` (user scope) or `.mcp.json` in project root (project scope):

```json
{
  "mcpServers": {
    "github": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-e", "GITHUB_PERSONAL_ACCESS_TOKEN",
        "-e", "GITHUB_TOOLSETS=repos,issues,pull_requests,actions",
        "ghcr.io/github/github-mcp-server"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_PAT}"
      }
    },
    "claude-flow": {
      "command": "npx",
      "args": ["claude-flow@alpha", "mcp", "start"]
    },
    "filesystem": {
      "command": "npx",
      "args": [
        "-y", "@modelcontextprotocol/server-filesystem",
        "/Users/YOUR_USERNAME/syncrescendence",
        "/Users/YOUR_USERNAME/syncrescendence-canon"
      ]
    }
  }
}
```

### GitHub MCP server capabilities

The official GitHub MCP server provides **40+ tools** across toolsets. Enable specific toolsets via the `GITHUB_TOOLSETS` environment variable:

| Toolset | Key Tools | Use Case |
|---------|-----------|----------|
| `repos` | create_branch, push_files, search_code | Repository management |
| `issues` | create_issue, list_issues, add_comment | Task tracking |
| `pull_requests` | create_pull_request, merge, get_diff | Code integration |
| `actions` | run_workflow, get_job_logs, cancel_run | CI/CD automation |

For security, use `GITHUB_READ_ONLY=1` on Claude instances that shouldn't modify repository state.

### claude-flow for multi-agent coordination

claude-flow (v2.7.0-alpha, 11k GitHub stars) provides multi-agent swarm orchestration with **100+ MCP tools and 64 specialized agents**. Critical capabilities:

- **ReasoningBank**: SQLite-based persistent memory (`~/.swarm/memory.db`) with hash-based embeddings requiring no API keys, achieving 2-3ms query latency
- **Swarm topologies**: Hierarchical (Queen-led), Mesh (peer-to-peer), Star (central coordinator), Adaptive (dynamic)
- **Memory commands**: `memory store`, `memory query`, `memory vector-search` for cross-session context

**For Oracle→Claude Code communication**: Store tasks in ReasoningBank namespaces. Oracle writes directives to a shared namespace; Claude Code instances poll for pending tasks.

```bash
# Oracle instance stores directive
npx claude-flow@alpha memory store task_001 \
  "Process intake batch 2026-01-08" \
  --namespace orchestration --reasoningbank

# Claude Code instance queries for work
npx claude-flow@alpha memory query "task" \
  --namespace orchestration --reasoningbank
```

### Key limitation

**MCP does NOT enable direct Claude-to-Claude communication.** It's a client-server protocol connecting Claude to external tools, not an inter-agent messaging system. Coordination requires shared state via GitHub, filesystem, or ReasoningBank.

---

## Automation pipeline prioritized roadmap

The following roadmap sequences automation investments by **impact-to-effort ratio**, starting with high-impact, low-effort patterns before tackling complex orchestration.

### Phase 1: Foundation automation (Weeks 1-2, effort: Low)

| Task | Implementation | Expected Impact |
|------|----------------|-----------------|
| Headless mode wrappers | Shell scripts using `claude -p` with JSON output | 40% reduction in repetitive prompts |
| Pre-commit hooks | `pre-commit` framework with lint, type-check, schema validation | Eliminates broken commits |
| Session naming | `claude --continue` with descriptive session names | Faster context resumption |
| Git commit automation | `safe_commit_push()` function with protected branch guards | Reduced manual git operations |

**Deliverables**: `scripts/claude-wrapper.sh`, `.pre-commit-config.yaml`, `.claude/commands/` directory with initial commands.

### Phase 2: Ledger and validation automation (Weeks 3-4, effort: Medium)

| Task | Implementation | Expected Impact |
|------|----------------|-----------------|
| Atomic CSV updates | Python module with temp file→validate→rename pattern | Zero data corruption risk |
| Ledger schema enforcement | Pandera/Pydantic validators in pre-commit | Catch invalid entries before commit |
| Makefile standardization | Targets for verify, process, sync, update-ledgers | Consistent operations interface |
| Backup automation | Timestamped backups with 30-day retention | Safe rollback capability |

**Deliverables**: `tools/km_tools/processors/ledger.py`, `canon/schemas/ledger-schemas.json`, `Makefile` with documented targets.

### Phase 3: Multi-Claude coordination (Weeks 5-8, effort: High)

| Task | Implementation | Expected Impact |
|------|----------------|-----------------|
| Git worktree setup | Per-account worktrees with dedicated branches | Conflict-free parallel execution |
| MCP server deployment | GitHub + claude-flow + filesystem servers | Automated repository operations |
| Zone-based ownership | `coordination.yaml` defining write zones per account | Eliminate merge conflicts |
| ReasoningBank integration | Shared memory namespace for Oracle directives | 60% reduction in Principal relay |

**Deliverables**: `scripts/setup-worktrees.sh`, `config/coordination.yaml`, MCP configuration files, claude-flow initialization.

### Phase 4: Advanced orchestration (Weeks 9-12, effort: Very High)

| Task | Implementation | Expected Impact |
|------|----------------|-----------------|
| GitHub Actions CI/CD | Validation workflows, merge automation, doc generation | Automated quality gates |
| SQLite migration | Parallel CSV+SQLite with `user_version` pragma | Query performance, atomic transactions |
| Custom MCP server | TypeScript server for domain-specific operations | Codified Oracle patterns |
| Blitzkrieg mode | Parallel processing with subagent verification | 3x throughput on bulk operations |

**Deliverables**: `.github/workflows/*.yml`, `migrations/` directory with versioned schemas, custom MCP server package.

### Human oversight boundaries

**Fully automatable** (no approval required): Code formatting, linting, test execution, documentation generation, ledger backups, dependency updates with validation gates.

**Requires human oversight**: Security-critical code, architectural decisions, production deployments, git push to protected branches (main/master), external API integrations with cost implications, file deletions.

---

## Repository evolution from CSV to RDBMS

The migration from CSV-based ledgers to SQLite follows a **parallel operation strategy** that maintains backwards compatibility throughout the transition.

### Phase 1: Schema formalization (Weeks 1-2)

Define JSON Schema for each CSV, implement Pandera validators, and establish baseline data quality metrics.

```python
# canon/schemas/ledger_schemas.py
from pandera import DataFrameSchema, Column, Check
import pandera as pa

tasks_schema = DataFrameSchema({
    "id": Column(str, Check.str_matches(r"^TSK-\d{6}$")),
    "title": Column(str, Check.str_length(min_value=5, max_value=200)),
    "status": Column(str, Check.isin(["pending", "active", "completed", "blocked"])),
    "assignee": Column(str, nullable=True),
    "created": Column(pa.DateTime),
    "updated": Column(pa.DateTime),
})
```

### Phase 2: Dual-write implementation (Weeks 3-4)

Every CSV update simultaneously writes to SQLite. Use SQLite's `user_version` pragma for schema versioning.

```sql
-- migrations/0001_initial_schema.sql
PRAGMA user_version = 1;

CREATE TABLE tasks (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('pending','active','completed','blocked')),
    assignee TEXT,
    created TEXT NOT NULL,
    updated TEXT NOT NULL
);

CREATE INDEX idx_tasks_status ON tasks(status);
CREATE INDEX idx_tasks_assignee ON tasks(assignee);
```

### Phase 3: Read migration (Weeks 5-6)

Route read operations through a unified interface that checks SQLite first, falls back to CSV.

```python
class LedgerProcessor:
    def __init__(self, source_path: Path):
        self.source = source_path
        self.use_sqlite = source_path.suffix == '.db'
    
    def query(self, filters: dict = None):
        if self.use_sqlite:
            return self._query_sqlite(filters)
        return self._query_csv(filters)
```

### Phase 4: Write migration (Weeks 7-8)

Switch primary writes to SQLite, generate CSV exports for backwards compatibility with any external tools.

### Phase 5: CSV deprecation (Weeks 9-12)

Remove CSV write paths, keep CSV export as read-only snapshot capability. Final directory structure:

```
05-OPERATIONAL/
├── ledgers/
│   ├── knowledge.db          # Primary SQLite database
│   ├── exports/               # CSV snapshots (generated)
│   │   ├── tasks.csv
│   │   ├── projects.csv
│   │   └── sources.csv
│   └── migrations/
│       ├── 0001_initial.sql
│       ├── 0002_add_indexes.sql
│       └── runner.py
```

### Migration tooling

```bash
# Run pending migrations
km-migrate --db 05-OPERATIONAL/ledgers/knowledge.db

# Export to CSV for compatibility
km-export --format csv --output exports/

# Validate database integrity
km-validate --check-referential --check-constraints
```

---

## Multi-account synchronization architecture

For 3 Claude Pro accounts operating in parallel, the recommended architecture uses **GitHub as the single source of truth** with git worktrees providing isolated working directories per account.

### Layer hierarchy for Syncrescendence

```
┌─────────────────────────────────────────────────────────────┐
│          TRUTH HIERARCHY (Highest to Lowest)                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. GitHub Repository (ground truth)                        │
│     ├── Source code, schemas, canonical documents           │
│     ├── CLAUDE.md (committed, team-shared)                  │
│     └── .claude/settings.json (shared configuration)        │
│                                                             │
│  2. Local Clone (per-account worktree)                      │
│     ├── Working directory with isolated branch              │
│     ├── CLAUDE.local.md (gitignored, personal overrides)    │
│     └── .claude/settings.local.json (personal settings)     │
│                                                             │
│  3. Claude Project Context (if using Claude Desktop)        │
│     ├── Project Knowledge files (200K+ token capacity)      │
│     └── Custom Instructions                                 │
│                                                             │
│  4. Session Memory (ephemeral)                              │
│     ├── Current conversation context                        │
│     └── # shortcut additions via /memory                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Conflict prevention via zone ownership

Create `config/coordination.yaml` defining exclusive write zones:

```yaml
coordination:
  accounts:
    account_1:
      name: "Claude Instance Alpha"
      worktree: "../syncrescendence-alpha"
      branch_prefix: "alpha/"
      writable:
        - 02-INTAKE/queue-a/
        - 03-PROCESSING/stream-a/
        - 05-OPERATIONAL/ledgers/stream-a/
      
    account_2:
      name: "Claude Instance Beta"
      worktree: "../syncrescendence-beta"
      branch_prefix: "beta/"
      writable:
        - 02-INTAKE/queue-b/
        - 03-PROCESSING/stream-b/
        - 05-OPERATIONAL/ledgers/stream-b/
    
    account_3:
      name: "Claude Instance Gamma"
      worktree: "../syncrescendence-gamma"
      branch_prefix: "gamma/"
      writable:
        - 02-INTAKE/queue-c/
        - 03-PROCESSING/stream-c/
        - 05-OPERATIONAL/ledgers/stream-c/

  shared_append_only:
    - 05-OPERATIONAL/audit.log
    - 05-OPERATIONAL/processing_log.csv

  protected:
    - 00-ORCHESTRATION/
    - 04-CANON/
```

### Worktree setup script

```bash
#!/bin/zsh
# scripts/setup-worktrees.sh

REPO_ROOT=$(git rev-parse --show-toplevel)

# Create worktrees for each Claude instance
git worktree add ../syncrescendence-alpha -b alpha/work
git worktree add ../syncrescendence-beta -b beta/work  
git worktree add ../syncrescendence-gamma -b gamma/work

# Copy local config to each worktree
for dir in alpha beta gamma; do
  cp .claude/settings.local.json.template \
     ../syncrescendence-$dir/.claude/settings.local.json
done

echo "Worktrees created. Each Claude instance should cd to its assigned directory."
```

### Critical limitation

**Claude Pro accounts cannot share Projects**—they're fully isolated. Team/Enterprise plans support project sharing with "Can view" and "Can edit" permissions. For Pro accounts, synchronization must flow through Git commits, not Claude's native project features.

---

## Friction reduction implementation patterns

The highest-impact friction reductions target **permission prompt fatigue**, **context loss between sessions**, and **verification overhead**.

### Permission allowlisting

Add to `.claude/settings.json` to reduce approval prompts for safe operations:

```json
{
  "permissions": {
    "allow": [
      "Edit",
      "Read",
      "Glob",
      "Grep",
      "Bash(npm run:*)",
      "Bash(make:*)",
      "Bash(python -m:*)",
      "Bash(git status:*)",
      "Bash(git diff:*)",
      "Bash(git add:*)",
      "Bash(git commit:*)"
    ],
    "deny": [
      "Bash(rm -rf:*)",
      "Bash(git push --force:*)",
      "Bash(git checkout main:*)"
    ]
  }
}
```

### Context preservation protocol

Before ending any session:

1. Run `/compact` with explicit summary instructions
2. Update `05-OPERATIONAL/session-state/current.md` with decisions made
3. Prompt: "What problems did you overcome that you wish you'd known ahead of time?"
4. Store learnings in `05-OPERATIONAL/session-state/learnings.md`

### Verification hooks

Configure automatic quality gates in `.claude/settings.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write(*.py)",
        "hooks": [
          {"type": "command", "command": "python -m black \"$file\""},
          {"type": "command", "command": "python -m ruff check \"$file\" --fix"}
        ]
      },
      {
        "matcher": "Write(*.csv)",
        "hooks": [
          {"type": "command", "command": "python scripts/validate_csv.py \"$file\""}
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash(git push:*)",
        "hooks": [
          {"type": "command", "command": "make verify"}
        ]
      }
    ]
  }
}
```

### Template interaction conversions

| Repetitive Interaction | Convert To |
|----------------------|------------|
| "Read all files related to X first" | `/project:gather-context X` |
| "Update the task ledger with..." | `/project:update-ledgers tasks.csv ...` |
| "Run all verification checks" | `/project:verify` |
| "Process everything in intake" | `/project:blitzkrieg` |
| "Review this code for security" | `/project:security-review` |

---

## Summary and next steps

Syncrescendence's optimization path follows a clear sequence: **establish CLAUDE.md and slash commands first** (Week 1), **deploy MCP servers and worktree isolation** (Weeks 2-4), **implement automation pipelines with validation hooks** (Weeks 5-8), and **migrate ledgers to SQLite with CI/CD integration** (Weeks 9-12).

The critical architectural decisions are:

1. **GitHub remains the single source of truth**—all persistent state commits to the repository
2. **Git worktrees eliminate merge conflicts**—each Claude instance operates in isolated branches
3. **Zone-based ownership prevents contention**—coordination.yaml defines exclusive write territories
4. **MCP servers enable automation**—GitHub operations, semantic search, and swarm coordination without manual relay
5. **Slash commands codify Oracle patterns**—repeatable workflows replace ad-hoc prompting

The remaining human oversight requirements (security review, architectural decisions, production deployments) cannot be automated safely, but represent only 20-40% of current Principal relay burden. The 60-80% reduction in manual coordination overhead comes from the combination of structured CLAUDE.md context, automated verification hooks, and MCP-enabled repository operations.