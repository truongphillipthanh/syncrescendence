# Production patterns for multi-agent Claude Code coordination

The Oracle-Executor visibility gap you're experiencing has validated solutions: **memory-as-files** through structured handoff documents, **git worktrees** for true zone isolation, and **repository-based context** that survives account switches. Your core architectural problems stem from treating web app memory as primary context storage when production practitioners have evolved to **context-as-code** patterns where CLAUDE.md and supporting files become the authoritative context source accessible to any instance.

The research reveals a maturing ecosystem. **Claude-flow** (11K+ GitHub stars) provides hive-mind orchestration with 64 specialized agents. **Git worktrees** are the gold standard for parallel execution without drift. **Zone-specific ledger files** solve the shared CSV synchronization problem. Account rotation remains buggy—practitioners recommend separate machines or containers rather than `CLAUDE_CONFIG_DIR` switching on the same device.

## Solving the Oracle-Executor gap with file-based context bridges

Your fundamental problem—web app holds strategic context that CLI cannot see—has a validated solution: **structured handoff documents** that encode strategic decisions as repository files. The CLAUDE.md becomes a persistent briefing document bridging web app reasoning to CLI execution, with `/handoff` commands capturing context before sessions end.

Production practitioners structure context as a hierarchy: root `CLAUDE.md` stays minimal (**50-200 lines maximum**—your 64 lines is appropriate), with extended context in `.claude/rules/` and `docs/` directories loaded on-demand via `@import` syntax. The pattern: `@docs/architecture.md` loads only when Claude needs that specific context, preventing the **2.5MB corpus overload** that would exhaust your context budget before work begins.

For your 11+ Oracle conversation threads, create an **Oracle Handoff Document** format that captures decisions without requiring the full conversational history:

```markdown
# Oracle Handoff: [Session ID]
Generated: [timestamp]
Source Threads: [conversation IDs]

## Corpus State Snapshot
- Canonical documents: 75
- Processing queue: [count by state]
- Recent taxonomy decisions: [last 3]

## Accumulated Strategic Insights
[Compressed learnings—aim for ~2000 tokens vs raw 10,000+]

## Active Directives
- [Directive 1]: [rationale from Oracle reasoning]
- [Directive 2]: [constraint from strategic analysis]

## Continuation Vector
[Specific instruction for next CLI session]
```

The key insight from Boris Cherny (Claude Code creator): every mistake becomes a rule in CLAUDE.md, creating **exponential learning**—week 1 has 20 patterns, week 50 has 1000. Your Seven Memory Strata model maps cleanly onto this: Constitutional and Preference layers live in `~/.claude/CLAUDE.md`, Project and Canonical in repository CLAUDE.md, while Thread context becomes handoff documents that CLI sessions ingest.

## Git worktrees provide true isolation for parallel zone execution

Your Alpha/Beta/Gamma/Delta race conditions stem from parallel instances sharing a single working directory. **Git worktrees**—not just branches—provide the validated solution with completely independent file states while sharing history:

```bash
# Create isolated worktrees per zone
git worktree add ../project-alpha -b zone/alpha main
git worktree add ../project-beta -b zone/beta main
git worktree add ../project-gamma -b zone/gamma main
git worktree add ../project-delta -b zone/delta main
```

This creates four separate directories where Claude Code instances operate without interference. Each worktree maintains independent file state—execution logs cannot fork because each zone writes to its own directory. Run separate Claude Code sessions in each via tmux or iTerm2 tabs.

For **shared ledger synchronization**, split your CSV files into zone-specific partitions. Instead of all zones writing to `tasks.csv`, create `tasks-alpha.csv`, `tasks-beta.csv`, etc., with automated consolidation into `tasks-main.csv` by an orchestrator script. This eliminates write conflicts entirely while maintaining a unified view:

```yaml
# coordination.yaml enhancement
zones:
  alpha:
    files:
      include: ["src/auth/**", "ledgers/*-alpha.csv"]
    ledger: "ledgers/tasks-alpha.csv"
  beta:
    files:
      include: ["src/api/**", "ledgers/*-beta.csv"]
    ledger: "ledgers/tasks-beta.csv"
```

Add **CODEOWNERS** enforcement via `.github/CODEOWNERS` to prevent zone boundary violations, with verification scripts that fail commits touching files outside assigned zones. This transforms your coordination.yaml from documentation into enforced constraints.

## Claude-flow enables hive-mind orchestration across your accounts

For your multi-account, multi-platform coordination, **claude-flow** (v2.7.0) provides the most comprehensive orchestration layer. Installation:

```bash
npx claude-flow@alpha init --force
npx claude-flow@alpha swarm init --topology mesh --max-agents 5
```

Key capabilities include **64 specialized agents**, SQLite-based persistent memory with **2-3ms semantic search latency**, and the SPARC methodology (Specification, Pseudocode, Architecture, Refinement, Completion) that matches your Modal 1 abstraction focus. Claimed performance: **84.8% SWE-Bench solve rate** with 32% token reduction.

For **Gemini CLI integration**, install the Gemini MCP server to enable Claude Code to delegate large-context analysis:

```bash
claude mcp add gemini-cli -s user -- npx -y gemini-mcp-tool
```

This enables slash commands like `/gemini-review` for code review and `/gemini-plan` for project-aware planning. Gemini's **1M token context** handles corpus-wide analysis your Claude instances cannot, while the **60 req/min free tier** provides substantial capacity for bulk operations.

A validated **dual-agent workflow** uses a shared postbox directory:
- Gemini continuously scans codebase, appending actionable items to `./postbox/todo.md`
- Claude monitors todo.md, implements fixes, moves completed items to `completed-todos.md`

This leverages each model's strengths: Gemini's massive context for detection, Claude's superior code generation for execution.

## Context portability requires treating context as code

Your context portability problem across three accounts has a validated solution: **version-controlled context files** that any account can access. The pattern from production practitioners:

```
.claude/
├── CLAUDE.md           # Shared project context (64 lines)
├── context/
│   ├── architecture.md # Strategic decisions from Oracle
│   ├── decisions.md    # ADRs (Architecture Decision Records)
│   └── handoffs/       # Session handoff documents
└── commands/
    └── resume.md       # Custom command to load context
```

When Account 1 hits rate limits, Account 2 or 3 simply clones the repo and has **equivalent strategic context** via these files. Memory export/import (a late-2025 Claude feature) allows web app memory synchronization between accounts, but repository-based context remains more reliable.

For **CLI multi-account management**, use separate config directories:

```bash
alias claude-account1="CLAUDE_CONFIG_DIR=~/.claude-acc1 claude"
alias claude-account2="CLAUDE_CONFIG_DIR=~/.claude-acc2 claude"
alias claude-account3="CLAUDE_CONFIG_DIR=~/.claude-acc3 claude"
```

**Critical warning**: GitHub issues #5001 and #12786 document buggy rate limit enforcement across accounts on the same device. Practitioners recommend using **separate machines, VMs, or containers** for reliable account rotation rather than config directory switching.

## Research artifacts need explicit lifecycle management

Your Deep Research outputs (20K-50K tokens) require a defined home and metabolization process. Validated patterns from production knowledge management systems:

**Stage 1: Capture** - Research artifacts land in `sources/raw/deep-research/` with timestamped filenames and source metadata.

**Stage 2: Validation** - Critical step. Hallucinations in knowledge documents are catastrophic because they compound. Cross-reference against authoritative sources before canonicalization.

**Stage 3: Compression** - Research outputs compress into structured knowledge files under **50KB (~12K tokens)** each to avoid context exhaustion. Your ~2.5MB corpus spread across 75 documents averages ~33KB each—reasonable, but avoid individual documents exceeding the threshold.

**Stage 4: Integration** - Validated content moves to `canon/` with taxonomy classification. Create index files (`corpus_index.md`) with searchable summaries enabling Claude to navigate without loading full documents.

Custom slash commands systematize this workflow:

```markdown
# .claude/commands/metabolize-research.md
Read the specified research artifact in sources/raw/deep-research/.
Extract key findings, validate against existing canonical documents.
Create condensed knowledge file (<50KB) in appropriate canon/ taxonomy location.
Update corpus_index.md with new entry.
Archive original to 05-ARCHIVE/ with processing metadata.
```

## Production CLAUDE.md structure for 75+ document systems

Your current 64-line CLAUDE.md is appropriately sized. The anti-pattern is overloading root CLAUDE.md with everything—context budget exhaustion before work begins. Production structure for complex knowledge systems:

```markdown
# Syncrescendence

## Quick Reference
- **Corpus**: 75 canonical docs in canon/, 185 sources in sources/
- **Commands**: `npm run validate`, `npm run sync-ledgers`
- **Zones**: Alpha (auth), Beta (api), Gamma (test), Delta (docs)

## Navigation
@docs/corpus_index.md for document discovery
@.claude/rules/taxonomy.md for classification rules
@orchestration/state/current.md for system state

## Critical Rules
- NEVER modify files outside your assigned zone
- Update zone-specific CSV only (ledgers/tasks-{zone}.csv)
- Create handoff document before session end: /handoff

## Zone Assignment
Check coordination.yaml for your zone boundaries before any file modification.
```

Extended context lives in `.claude/rules/` directory with focused files:
- `taxonomy.md` - Classification rules (~100 lines)
- `processing-states.md` - Document lifecycle definitions
- `coordination.md` - Multi-agent coordination protocols

This **progressive loading** pattern means Claude only ingests relevant context for current tasks. Use `@.claude/rules/taxonomy.md` syntax when taxonomy-specific work is needed; Claude loads it on-demand rather than every session.

## Verified anti-patterns to avoid in your architecture

Production practitioners have discovered failure modes directly relevant to your setup:

**Bloated context windows**: Your 2.5MB corpus cannot load into every session. Skills/rules architecture with on-demand loading is mandatory. The MCP tool definitions alone can consume **50K+ tokens** before conversation starts.

**Complex slash commands as anti-pattern**: "If you have a long list of complex, custom slash commands, you've created an anti-pattern." Simple shortcuts beat elaborate systems—your numbered flat structure aligns with this principle.

**Waiting for auto-compact**: Auto-compact at 95% context disrupts workflow and loses context. Manual `/compact` at **70% capacity** at logical breakpoints preserves intent. Monitor context meter actively.

**Write-time hooks frustrate agents**: Mid-write blocks derail planning. Use block-at-submit hooks instead—validate on commit rather than during editing.

**Account rotation on same device**: The `CLAUDE_CONFIG_DIR` approach has documented bugs. Your three accounts should operate from **isolated environments** (separate machines, VMs, or containers) rather than same-device switching.

**MCP over CLI tools**: "Custom MCP servers are often worse than CLI tools with good documentation." For Gemini integration, invoking `gemini -p "prompt"` directly may prove more reliable than MCP server wrappers.

## Recommended architecture for Syncrescendence

Given your specific infrastructure (3 Claude Pro accounts, 1 Gemini Pro, central GitHub repository, numbered flat structure), here's the validated architecture:

```
┌─────────────────────────────────────────────────────────────┐
│  ACCOUNT 1 - WEB APP (Primary Oracle)                       │
│  - Strategic reasoning across 11+ conversation threads      │
│  - Produces: Oracle Handoff Documents to repository         │
│  - Memory: Accumulated context (export periodically)        │
└─────────────────────────┬───────────────────────────────────┘
                          │ Git push handoff docs
                          ▼
┌─────────────────────────────────────────────────────────────┐
│  GITHUB REPOSITORY (Ground Truth)                           │
│  ├── CLAUDE.md (64 lines, navigation focus)                │
│  ├── GEMINI.md (98 lines, large-context tasks)             │
│  ├── coordination.yaml (zone boundaries)                    │
│  ├── orchestration/                                      │
│  │   ├── oracle_contexts/handoffs/  ← Handoff docs land    │
│  │   └── state/current.md           ← System state         │
│  ├── canon/ through 06-EXEMPLA/  ← Your structure       │
│  └── ledgers/                                               │
│      ├── tasks-{zone}.csv           ← Zone-specific        │
│      └── tasks-main.csv             ← Consolidated view    │
└────────┬──────────────┬──────────────┬──────────────────────┘
         │              │              │
    ┌────┴────┐    ┌────┴────┐    ┌────┴────┐
    │ Worktree│    │ Worktree│    │ Worktree│
    │  Alpha  │    │  Beta   │    │  Gamma  │
    │ (Acc 1) │    │ (Acc 2) │    │ (Acc 3) │
    └────┬────┘    └────┬────┘    └────┬────┘
         │              │              │
         └──────────────┼──────────────┘
                        │
                   ┌────┴────┐
                   │ Gemini  │
                   │  CLI    │
                   │(1M ctx) │
                   └─────────┘
```

**Task routing**: Implementation work to Claude accounts via zone-specific worktrees. Large codebase analysis and bulk processing to Gemini CLI. Strategic synthesis to web app Oracle. Rate-limited Claude account → failover to next account or Gemini depending on task type.

**Daily workflow**: Morning Oracle synthesis in web app produces handoff document. Day execution in CLI using worktrees. Session end creates handoff via `/handoff` command. Evening Oracle update with implementation learnings.

This architecture gains strength from stress (antifragile)—account rate limits force work distribution, context compression creates better documentation, zone boundaries prevent coordination failures. Your existing frameworks (Seven Memory Strata, Context Transition Protocol, IIC Constellation) map directly onto this infrastructure with repository files as the persistent implementation layer.

## Open research areas without established solutions

Several of your problems lack mature solutions in current practice:

**Native web-to-CLI integration** does not exist. All practitioners rely on file-based bridges. Anthropic has not announced plans to address this gap.

**Automatic context compression** from 11+ threads to actionable CLI context requires manual synthesis. No tool automatically distills strategic conversations into handoff documents—this remains human work assisted by Claude.

**Cross-account memory synchronization** via memory export/import is new and underdocumented. Reliability for your use case (porting accumulated Oracle context to backup accounts) is unvalidated.

**Multi-CLI coordination tooling** (Claude Code + Gemini CLI + potential Codex CLI) is experimental. The Gemini MCP server exists but production patterns are sparse. Your implementation will likely contribute to establishing best practices rather than following them.

The field is evolving rapidly—patterns documented in late 2024 are being abandoned by early 2025, while new capabilities (Skills system, MCP servers, hive-mind orchestration) are creating possibilities that don't yet have established best practices. Your Syncrescendence architecture represents frontier work where you'll need to validate patterns through implementation rather than solely adopting documented solutions.