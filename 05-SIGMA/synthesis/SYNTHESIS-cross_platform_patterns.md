# Cross-Platform Orchestration Patterns: Canonical Reference

**Version**: 1.0.0 | **Stream**: C | **Purpose**: Unify multi-platform patterns

---

## Executive Frame

The Chorus Architecture leverages multiple platforms contributing from genuine strengths—not draconian role relegation but authentic collaboration. Claude proposes architectural solutions. ChatGPT builds implementation details. Gemini provides interdisciplinary synthesis with 1M token context. Grok contributes practitioner wisdom and colloquial insight.

The Oracle-Executor pattern solves a fundamental problem: web apps hold strategic context that CLI cannot see. The solution is **context-as-code**—structured handoff documents, CLAUDE.md hierarchies, and repository-based state that survives session death. Memory lives in files, not conversations.

---

## TERM Blocks: Core Concepts

```
TERM ChorusArchitecture:
sutra: "Each platform's characteristic cognition compounds—synergy, not role rigidity"
gloss: Multi-platform orchestration that leverages genuine strengths. Claude for
       architectural proposals, ChatGPT for implementation pragmatism, Gemini
       for massive-context synthesis, Grok for colloquial wisdom. Not forcing
       platforms into artificial roles—recognizing authentic capabilities.
spec:
    type: TERM
    platforms:
        claude: "Architectural proposals, safety consciousness, explicit reasoning"
        chatgpt: "Implementation pragmatism, code-first, immediate actionability"
        gemini: "1M context synthesis, interdisciplinary connections, theoretical framing"
        grok: "Practitioner patterns, community wisdom, colloquial voice"
    anti_pattern: "Treating any platform as inferior"
    principle: "Present problems to strengths, synthesize across perspectives"
end
```

```
TERM OracleExecutorPattern:
sutra: "Web app reasons, CLI executes—file-based bridges survive context death"
gloss: Strategic reasoning happens in web apps (Oracle). Execution happens in CLI
       (Executor). The visibility gap is bridged by structured handoff documents
       in the repository. These persist when conversations die. Memory-as-files
       rather than memory-as-state.
spec:
    type: TERM
    oracle:
        location: web app
        function: strategic reasoning
        output: handoff documents, decisions, constraints
    executor:
        location: CLI
        function: tool execution
        input: handoff documents, CLAUDE.md
    bridge: repository files
    key_insight: "Context-as-code persists; conversation context dies"
    handoff_location: "00-ORCHESTRATION/oracle_contexts/handoffs/"
end
```

```
TERM ContextAsCode:
sutra: "CLAUDE.md is persistent behavioral constitution—every mistake becomes a rule"
gloss: LLMs are stateless between sessions. CLAUDE.md serves as persistent memory
       that survives session death, context compaction, and account switches.
       Hierarchical loading enables granular context engineering. Version control
       creates institutional knowledge that compounds over time.
spec:
    type: TERM
    hierarchy:
        1: Enterprise (~/.../CLAUDE.md)
        2: Project root (./CLAUDE.md)
        3: Project rules (.claude/rules/*.md)
        4: User global (~/.claude/CLAUDE.md)
        5: Project local (./CLAUDE.local.md, gitignored)
    loading: "Automatic at session start, survives compaction"
    import_syntax: "@path/to/file (max 5 hops)"
    compounding: "Every error → add rule → system improves forever"
    size_limit: "50-200 lines root; extended in .claude/rules/"
end
```

```
TERM MemoryAsFiles:
sutra: "State in repository survives what conversation cannot—plan.md beats memory"
gloss: Production practitioners evolved from treating web app memory as primary
       context to treating repository files as authoritative source. Any Claude
       instance with repo access has equivalent strategic context. Account rate
       limits, session death, context compaction—all survivable with file-based state.
spec:
    type: TERM
    repository_structure:
        ".claude/": "Configuration and context"
        "context/": "Architecture decisions, handoffs"
        "commands/": "Custom slash commands"
    portability: "Account 2 clones repo, has equivalent context"
    durability: "Survives session death, rate limits, compaction"
    anti_pattern: "Relying on web app memory as primary"
end
```

```
TERM GeminiIntegration:
sutra: "1M tokens for corpus analysis, 60 req/min free—Claude executes what Gemini discovers"
gloss: Gemini's massive context handles codebase-wide analysis Claude cannot.
       Dual-agent workflow: Gemini continuously scans, appends actionable items
       to postbox/todo.md; Claude monitors, implements, moves completed.
       Each model's strength leveraged.
spec:
    type: TERM
    gemini_strengths:
        context: "1M tokens (vs 200K Claude)"
        rate: "60 req/min free tier"
        use_for: "Corpus-wide analysis, bulk detection"
    claude_strengths:
        execution: "Superior code generation"
        tools: "Full agentic harness"
        use_for: "Implementation, file operations"
    workflow:
        gemini: "Scan codebase → append to postbox/todo.md"
        claude: "Monitor todo.md → implement → move to completed"
    integration: "claude mcp add gemini-cli -s user -- npx -y gemini-mcp-tool"
end
```

```
TERM WorktreeIsolation:
sutra: "Same .git history, independent working trees—parallel agents without race conditions"
gloss: Git worktrees provide true isolation for parallel zone execution. Each
       worktree is separate directory with independent file state sharing git
       history. Execution logs cannot fork because each zone writes to own
       directory. The gold standard for multi-agent coordination.
spec:
    type: TERM
    setup: "git worktree add ../project-alpha -b zone/alpha main"
    isolation: "Completely independent file states"
    sharing: "Same .git history across all worktrees"
    benefit: "No race conditions, no file locks"
    pattern: "One worktree per zone, one Claude instance per worktree"
    merge_strategy: "Infrequent merges at natural breakpoints"
end
```

```
TERM ZoneOwnership:
sutra: "Alpha edits src/auth/*, Beta edits src/api/*—boundaries prevent conflicts"
gloss: Parallel agents must not edit same files simultaneously. Zone ownership
       assigns orthogonal file boundaries. coordination.yaml defines boundaries.
       CODEOWNERS enforces via commit verification. Zone-specific ledgers
       eliminate shared CSV conflicts.
spec:
    type: TERM
    definition: "coordination.yaml with zone boundaries"
    enforcement: ".github/CODEOWNERS + verification scripts"
    pattern:
        alpha: ["src/auth/**", "ledgers/*-alpha.csv"]
        beta: ["src/api/**", "ledgers/*-beta.csv"]
        gamma: ["src/test/**", "ledgers/*-gamma.csv"]
    ledger_strategy: "Zone-specific CSVs, consolidation script for main view"
end
```

---

## The Chorus Procedure

```
PROC ChorusProcedure:
    context: "Problem requiring multi-perspective synthesis"

    1: "Present problem to Claude for architectural proposal"
        - Explicit reasoning chains
        - Safety considerations
        - Structural options

    2: "Have ChatGPT build implementation details"
        - Pragmatic code patterns
        - Immediate actionability
        - Error handling

    3: "Gather Gemini for interdisciplinary insights"
        - Corpus-wide context
        - Theoretical framing
        - Novel connections

    4: "Collect Grok for practitioner wisdom"
        - Community patterns
        - Colloquial framing
        - War stories

    5: "Synthesize across perspectives"
        - Not averaging—integrating
        - Preserve unique angles
        - Resolve contradictions explicitly

    anti_pattern: "Asking same question to all, taking first answer"
    principle: "Leverage strengths, don't enforce roles"
end
```

---

## The Oracle-Executor Handoff

```
PROC OracleExecutorHandoff:
    context: "11+ Oracle web app threads → CLI execution"

    1: "Oracle synthesizes strategic decisions"
        - Review conversation threads
        - Extract decisions (not conversation)
        - Identify constraints and rationale

    2: "Create handoff document"
        - Template in 00-ORCHESTRATION/oracle_contexts/handoffs/
        - Aim for ~2000 tokens (vs raw 10,000+)
        - Include continuation vector

    3: "Commit to repository"
        - Executor can git pull to receive
        - Version controlled for audit
        - Survives session death

    4: "Executor loads context"
        - Reads handoff + CLAUDE.md
        - Has equivalent strategic context
        - Executes with full authority

    5: "Executor creates return handoff"
        - Implementation learnings
        - New constraints discovered
        - Before session ends: /handoff command

    timing: "Before context death, before rate limit"
    bridge: "Repository files, not memory export"
end
```

### Handoff Document Template

```markdown
# Oracle Handoff: [Session ID]
Generated: [timestamp]
Source Threads: [conversation IDs]

## Corpus State Snapshot
- Canonical documents: [count]
- Processing queue: [count by state]
- Recent taxonomy decisions: [last 3]

## Accumulated Strategic Insights
[Compressed learnings—~2000 tokens vs raw 10,000+]

## Active Directives
- [Directive 1]: [rationale from Oracle reasoning]
- [Directive 2]: [constraint from strategic analysis]

## Continuation Vector
[Specific instruction for next CLI session]
```

---

## Research Artifact Lifecycle

```
PROC ResearchMetabolization:
    context: "Deep Research outputs (20K-50K tokens) require processing"

    stage_1_capture:
        location: "04-SOURCES/raw/deep-research/"
        format: "Timestamped filename + source metadata"

    stage_2_validation:
        critical: "Hallucinations compound in knowledge docs"
        action: "Cross-reference against authoritative sources"
        gate: "Human review before canonicalization"

    stage_3_compression:
        target: "<50KB (~12K tokens) per document"
        method: "Extract key findings, discard prose"
        rationale: "Avoid context exhaustion"

    stage_4_integration:
        destination: "01-CANON/ with taxonomy classification"
        index: "corpus_index.md with searchable summaries"
        archive: "Original to 05-ARCHIVE/ with metadata"
end
```

---

## Multi-Account Coordination

```
TERM MultiAccountPattern:
sutra: "Separate machines for accounts, not CLAUDE_CONFIG_DIR—known bugs"
gloss: Running multiple Claude accounts requires isolation. CLAUDE_CONFIG_DIR
       switching on same device has documented bugs (#5001, #12786). Production
       practitioners recommend separate machines, VMs, or containers rather
       than config directory switching.
spec:
    type: TERM
    approaches:
        naive: "CLAUDE_CONFIG_DIR aliases—buggy"
        recommended: "Separate machines/VMs/containers"
    rate_limit_handling: "Failover to next account or Gemini"
    context_portability: "Version-controlled files, not memory export"
    warnings:
        - "GitHub #5001: buggy rate limit enforcement"
        - "GitHub #12786: account collision on same device"
end
```

---

## Recommended Architecture

```
┌─────────────────────────────────────────────────────────────┐
│  ACCOUNT 1 - WEB APP (Primary Oracle)                       │
│  - Strategic reasoning across 11+ conversation threads      │
│  - Produces: Oracle Handoff Documents to repository         │
└─────────────────────────┬───────────────────────────────────┘
                          │ Git push handoff docs
                          ▼
┌─────────────────────────────────────────────────────────────┐
│  GITHUB REPOSITORY (Ground Truth)                           │
│  ├── CLAUDE.md (64 lines, navigation focus)                │
│  ├── GEMINI.md (98 lines, large-context tasks)             │
│  ├── coordination.yaml (zone boundaries)                    │
│  ├── 00-ORCHESTRATION/                                      │
│  │   ├── oracle_contexts/handoffs/                          │
│  │   └── state/current.md                                   │
│  └── ledgers/                                               │
│      ├── tasks-{zone}.csv                                   │
│      └── tasks-main.csv (consolidated)                      │
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

**Task routing**:
- Implementation → Claude accounts via zone-specific worktrees
- Large codebase analysis → Gemini CLI
- Strategic synthesis → Web app Oracle
- Rate-limited account → Failover to next or Gemini

---

## Verified Anti-Patterns

### From Production Practitioners

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| Bloated context windows | 2.5MB corpus exhausts budget before work | Progressive loading, @import syntax |
| Complex slash commands | "Anti-pattern if you have long list" | Simple shortcuts beat elaborate systems |
| Waiting for auto-compact | 95% triggers corruption | Manual /compact at 70% |
| Write-time hooks | Mid-write blocks derail planning | Block-at-submit instead |
| Same-device account rotation | Documented bugs | Separate machines/VMs |
| MCP over CLI tools | Often worse than CLI with good docs | Try CLI first |

---

## Open Research Areas

**No established solutions**:
- Native web-to-CLI integration (file bridges only)
- Automatic context compression from threads to handoff
- Cross-account memory synchronization
- Multi-CLI coordination (Claude + Gemini + Codex)

**Your implementation will contribute to establishing patterns.**

---

## Cross-References

- [[SYNTHESIS-agents_mcp_foundations]] → Agent paradigm, MCP, sub-agents
- [[MECH-git_worktree_coordination]] → Worktree setup details
- [[PRAC-oracle_to_executor_handoff]] → Handoff document templates
- [[PRAC-ledger_management_patterns]] → Zone-specific CSV patterns
- [[PRAC-multi_account_coordination]] → Account isolation details
