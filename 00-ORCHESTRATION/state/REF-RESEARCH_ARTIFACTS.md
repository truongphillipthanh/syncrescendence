# Research Artifact Protocol

## Purpose
Handle deep research outputs systematically to prevent root pollution and ensure knowledge preservation.

## Artifact Types

### Type 1: Deep Research Reports
- **Source**: Claude Desktop "Research" feature, extended analysis
- **Characteristics**: 20K-100K+ tokens, structured reports, comprehensive
- **Example**: `claude_code_optimization_architecture.md`

### Type 2: Oracle Session Outputs
- **Source**: Oracle thread synthesis, strategic analysis
- **Characteristics**: 5K-20K tokens, context-specific
- **Example**: `ORACLE10_CONTEXT_v*.md`

### Type 3: Execution Artifacts
- **Source**: Claude Code execution, temporary files
- **Characteristics**: Variable size, often superseded
- **Example**: Directive files dropped at root

## Disposition Decision Tree

```
Is this a deep research report (Type 1)?
├─ YES: Does it contain unique value not in CANON?
│   ├─ YES: Archive as RESEARCH-{date}-{topic}.md in 05-ARCHIVE/
│   └─ NO: Distill into relevant CANON, delete original
└─ NO: Is this an Oracle context (Type 2)?
    ├─ YES: Move to 00-ORCHESTRATION/oracle_contexts/
    └─ NO: Is this a directive/execution artifact (Type 3)?
        ├─ YES: Move to appropriate 00-ORCHESTRATION/ subdirectory
        └─ NO: Evaluate case-by-case, default to 05-ARCHIVE/
```

## Naming Convention

### Research Archives
`RESEARCH-{YYYYMMDD}-{topic_slug}.md`

Examples:
- `RESEARCH-20260108-claude_code_optimization.md`
- `RESEARCH-20260115-mcp_architecture_analysis.md`

### Distillation Candidates
If research report value can be compressed into CANON:
1. Extract key insights
2. Add to relevant CANON document (e.g., CANON-30340-IMPLEMENTATION_PATTERNS)
3. Delete or archive original (append `-DISTILLED` suffix if archiving)

## Root Cleanup Script

See `00-ORCHESTRATION/scripts/cleanup_root.sh` for automated enforcement.

## Acceptable Root Files

The following files are permitted at repository root:
- `CLAUDE.md` — Constitutional rules (required)
- `Makefile` — Build automation
- `README.md` — Repository documentation (if created)
- `.gitignore` — Git configuration

All other `.md` files must be relocated per the disposition tree.

## Periodic Maintenance

Run weekly or before each Oracle session:
```bash
./00-ORCHESTRATION/scripts/cleanup_root.sh
make verify
```
