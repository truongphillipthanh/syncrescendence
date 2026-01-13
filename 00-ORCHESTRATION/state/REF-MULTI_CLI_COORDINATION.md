# MULTI-CLI COORDINATION PROTOCOL
## Syncrescendence Parallel Execution Framework

**Version**: 1.0.0
**Created**: 2026-01-09
**Authority**: DIRECTIVE-042B
**Status**: Operational

---

## Overview

Syncrescendence operates multiple AI CLI tools in parallel to scale execution capacity beyond single-instance limits. This protocol defines coordination patterns that prevent conflicts while maximizing throughput.

---

## Available CLI Tools

| Tool | Context File | Capability | Context Limit |
|------|--------------|------------|---------------|
| Claude Code | CLAUDE.md | Full agentic execution | 200K tokens |
| Gemini CLI | GEMINI.md | Full agentic execution | 1M tokens |

---

## Zone Ownership

Each CLI instance operates in designated zones to prevent conflicts:

| Instance | Zone | File Pattern | Execution Logs |
|----------|------|--------------|----------------|
| Claude Code Alpha | A | `04-SOURCES/processed/a-*` | `*-A.md` |
| Claude Code Beta | B | `04-SOURCES/processed/b-*` | `*-B.md` |
| Claude Code Gamma | C | `04-SOURCES/processed/c-*` | `*-C.md` |
| Gemini CLI Delta | D | `04-SOURCES/processed/d-*` | `*-D.md` |

**Shared Zones** (append-only, coordinated access):
- `00-ORCHESTRATION/state/*.csv` — Ledger files
- `01-CANON/` — Canonical documents (integration only)
- `00-ORCHESTRATION/logs/` — Execution logs

---

## Parallel Execution Protocol

### Branch Strategy

```
main
├── alpha/directive-XXX
├── beta/directive-XXX
├── gamma/directive-XXX
├── delta/directive-XXX
└── develop (merge target)
```

1. Each instance creates branches with prefix matching its zone
2. Merge to `develop` branch after completion
3. Principal merges `develop` to `main` after verification

### Conflict Prevention

1. **Same Repository**: All CLIs access same git repository
2. **Zone Discipline**: Stay within assigned zone for file creation
3. **Append-Only Ledgers**: CSV updates add rows, never modify existing
4. **Frequent Commits**: Commit early, commit often
5. **Pull Before Push**: Always pull latest before pushing

---

## Ledger Coordination

### CSV Update Protocol

```bash
# 1. Create backup
cp tasks.csv tasks.csv.bak

# 2. Write to temp file
cat tasks.csv > tasks.csv.tmp
echo "new,row,data" >> tasks.csv.tmp

# 3. Validate
csvtool readable tasks.csv.tmp

# 4. Atomic rename
mv tasks.csv.tmp tasks.csv
```

### Row-Level Locking (Conceptual)

- Each instance appends new rows only
- No modification of existing rows without coordination
- Timestamp all additions for conflict resolution

---

## Capability Comparison

| Capability | Claude Code | Gemini CLI |
|------------|-------------|------------|
| File operations | Full | Full |
| Shell execution | Full | Full |
| Web search | WebSearch tool | Google Search |
| MCP servers | Full support | Full support |
| Context window | 200K | 1M |
| Extended thinking | Yes (think/ultrathink) | Yes (native) |
| Headless mode | Yes | Yes (--output-format) |
| Checkpointing | /compact | /chat save |
| Memory commands | N/A | /memory show/refresh |

---

## Communication Between Instances

Instances do NOT communicate directly. Coordination happens via:

1. **Git Repository**: Shared state through commits
2. **Directive Files**: Oracle issues directives with zone assignments
3. **Execution Logs**: Each instance reports completion in logs/
4. **Ledger Files**: Append-only shared state in CSV files
5. **State Files**: Session state in 00-ORCHESTRATION/state/

---

## Workflow: Parallel Directive Execution

### Phase 1: Directive Distribution
```
Oracle creates:
- DIRECTIVE-042A.md (Instance Alpha)
- DIRECTIVE-042B.md (Instance Beta)
- DIRECTIVE-042C.md (Instance Gamma)
- DIRECTIVE-042D.md (Instance Delta)
```

### Phase 2: Parallel Execution
- Each instance processes its directive independently
- Commits to instance-specific branch
- Updates ledgers with new rows only

### Phase 3: Convergence
- Each instance creates execution log
- Principal reviews all logs
- Merge branches to develop
- Final verification and main merge

---

## Best Practices

### Starting a Session

**Claude Code**:
```bash
cd /path/to/syncrescendence
git pull
# CLAUDE.md loads automatically
```

**Gemini CLI**:
```bash
cd /path/to/syncrescendence
git pull
gemini
> /memory show  # Verify GEMINI.md loaded
```

### During Execution

1. **Verify context**: Confirm correct files are loaded
2. **Stay in zone**: Create files only in assigned zone
3. **Commit frequently**: Every significant change
4. **Update ledgers**: Append new rows as tasks complete
5. **Document progress**: Update execution log continuously

### Ending a Session

1. Commit all changes
2. Push to instance branch
3. Create/update execution log
4. Mark directive complete in tasks.csv

---

## Troubleshooting

### Gemini CLI Context Not Loading
```bash
gemini
> /memory refresh
> /memory show
# Verify GEMINI.md appears
```

### Claude Code Context Not Loading
- Verify CLAUDE.md exists at project root
- Check file permissions
- Restart Claude Code session

### Merge Conflicts
1. Pull latest before starting work
2. Commit frequently (smaller changes = smaller conflicts)
3. Stay in assigned zones
4. For ledger conflicts: accept both additions, deduplicate

### Rate Limits (Gemini Free Tier)
- 60 requests/minute, 1,000/day
- Batch operations where possible
- Use headless mode for bulk tasks

---

## Monitoring

### Health Check Commands

```bash
# Verify all context files exist
ls -la CLAUDE.md GEMINI.md

# Check ledger integrity
make verify

# View recent commits by instance
git log --oneline --all | head -20

# Check for uncommitted changes
git status
```

### Metrics to Track
- Tasks completed per instance per day
- Merge conflict rate
- Ledger consistency (via make verify)
- Context loading success rate

---

## Version History

**v1.0.0** (2026-01-09): Initial protocol
- Zone ownership defined
- Branch strategy established
- Ledger coordination protocol
- Capability comparison documented
