---
canon_id: "CANON-3004"
title: "Memory Architecture"
slug: "memory-architecture"
tier: 3
tier_name: "chain"
chain: 0
chain_name: "universal"
celestial_type: "comet"
element: null
parent: null
children: []
heritage:
  - "CANON-25000-MEMORY_ARCH-lattice"
  - "CANON-30430-MEMORY_SYSTEMS-asteroid-INTELLIGENCE"
antithesis: "Every session that starts from zero is a session that wastes its first hour rediscovering what the previous session already knew."
depends_on: []
weight: 1.0
status: "canonical"
authority_status: not-live-authority
cautionary_status: partial
cautionary_reason:
  - superseded_doctrine
  - mixed_reuse_risk
pedigree_preservation: "Rehoused witness copy with custody metadata; source body preserved below."
source_tributary: syncrescendence_pre_schematic_design
source_path: neocanon/CANON-3004-MEMORY_ARCHITECTURE.md
source_filesystem_path: /Users/system/Desktop/syncrescendence_pre_schematic_design/neocanon/CANON-3004-MEMORY_ARCHITECTURE.md
source_body_sha256: 4d07a35326d5520623c9890541e37098d0d5b5ff72f33c8889c53fd644bea5b8
preserved_candidate_id: tdc-memory-architecture-neo-0004
merge_family_id: mf-memory-architecture-v1
preserved_at_utc: "2026-03-06T23:54:30Z"
preserved_by: codex_parallel_session
content_integrity: normalized-copy
version: "1.0.0"
epistemic_status: {}
knowledge_base: []
date_created: "2026-03-04"
date_modified: "2026-03-04"
sovereign_ratified: true
volatility: "annual"
---
# CANON-3004: MEMORY ARCHITECTURE
## Universal Protocol for Cognitive Persistence

> Memory is the substrate upon which persistent identity coheres.

For AI-augmented cognition, memory determines whether each interaction builds upon accumulated understanding or begins anew in isolation. This document establishes the systematic framework for maintaining cognitive continuity across sessions, threads, platforms, and accounts.

---

## PART I: THE MEMORY SOVEREIGNTY PRINCIPLE

The practitioner owns their memory. Not the platform. Not the model provider. Not the API.

This is an architectural requirement. Platforms change pricing, deprecate features, alter memory behavior without notice. Any memory architecture that depends entirely on platform-native features is a memory architecture that can be erased by a terms-of-service update.

The sovereign file system -- your disk, your git repo, your backups -- is the canonical memory layer, following what Vannevar Bush envisioned in his 1945 "memex" proposal: a personal, extensible, owner-controlled knowledge store. Platform-native memory is a convenience cache, useful but not authoritative.

---

## PART II: THE SEVEN MEMORY STRATA

Every AI platform implements some subset of these strata. Understanding the universal architecture enables strategic configuration regardless of which platform you use.

### Stratum 1: Constitutional Memory

The platform's immutable identity layer. System prompts, safety constraints, fundamental behavioral parameters. You cannot change this. It constrains everything above it.

### Stratum 2: Preference Memory

User-specified behavioral calibrations that persist across sessions. Claude's User Preferences. ChatGPT's Custom Instructions. Gemini's Saved Info.

Practitioner control: full. User-authored, user-editable. Keep minimal -- reserve complexity for project-level configuration.

### Stratum 3: Accumulated Memory

System-generated inferences from conversation history. Claude's Basal Memory. ChatGPT's Memory feature. Gemini's personalization.

Practitioner control: partial. The system infers; you curate. Audit regularly -- accumulated memory drifts toward stale generalizations.

### Stratum 4: Project/Space Memory

Scoped context for specific work domains. Claude Projects. ChatGPT Projects. Custom GPTs.

This is the most architecturally significant layer. Project isolation prevents cross-contamination between cognitive domains. Without isolation, consulting work bleeds into framework development bleeds into personal reflection.

### Stratum 5: Canonical Knowledge (RAG)

Retrieved knowledge from uploaded documents or connected knowledge bases. Project files. Uploaded PDFs. Connected repositories.

This is where The Codex meets the AI. Canonical documents uploaded to project context become retrievable knowledge. The quality of this layer depends entirely on the quality of what you upload.

### Stratum 6: Thread Context

The conversation itself. Working memory of the immediate interaction. Ephemeral by nature. Lost when the thread closes.

Critical limitation: thread context functions as the scratchpad, the ephemeral working surface. The filing cabinet lives elsewhere.

### Stratum 7: Tool-Extended Memory

External access capabilities. File system read/write. Git integration. API calls. MCP servers. CLI tools with full system access.

This is where sovereignty lives. Tool-extended memory through file system access provides cross-platform coordination (same files accessible to multiple CLI tools), git-based versioning (time travel through memory states), and sovereign storage (your disk, your control).

### Stratum Interaction Pattern

```
Request arrives
      |
      v
Stratum 1: Constitutional   -- Immutable identity loaded
Stratum 2: Preferences      -- User calibrations applied
Stratum 3: Accumulated      -- Relevant memories retrieved
Stratum 4: Project          -- Scoped context activated
Stratum 5: Canonical        -- RAG retrieval if relevant
Stratum 6: Thread           -- Conversation history
Stratum 7: Tool-Extended    -- External access if needed
      |
      v
Response generated
```

Earlier strata constrain later strata. Constitutional memory bounds what preferences can modify. Project context shapes what canonical knowledge is retrieved. Understanding The Cascade enables strategic configuration.

---

## PART III: THE CLI-FOYER ARCHITECTURE

The convergent signal from frontier practitioners is unambiguous: serious AI-augmented cognition happens in the CLI. CLI tools provide full system access, unconstrained by conversational modality.

### Why CLI Is Primary

1. **File system access**: Read/write to the sovereign memory layer
2. **Tool execution**: Run arbitrary code, scripts, processes
3. **Version control**: Git integration for memory versioning
4. **Cross-platform**: Multiple CLI tools can access same workspace
5. **Scriptability**: Automation of cognitive workflows

### The Foyer Pattern

The CLI serves as a foyer -- the coordination space where multiple AI systems can access shared context:

```
              SOVEREIGN FILE SYSTEM
    ┌─────────────────────────────────────┐
    │  ~/syncrescendence/                 │
    │  ├── corpus/     (raw knowledge)    │
    │  ├── neocorpus/  (compendium)       │
    │  ├── canon/      (authority)        │
    │  └── memory/     (operational)      │
    └──────┬──────────┬──────────┬────────┘
           v          v          v
    Claude Code   Gemini CLI   Codex CLI
           └──────────┼──────────┘
                      v
               Human Operator
```

### The CLAUDE.md Hierarchy

Claude Code loads context from a hierarchy of configuration files:

1. **Enterprise level**: Organization-wide standards
2. **User level**: `~/.claude/CLAUDE.md` -- personal defaults
3. **Project level**: `./CLAUDE.md` -- project-specific context
4. **Directory level**: Nested CLAUDE.md files for subsystem context

Create CLAUDE.md files that inject appropriate corpus context and behavioral calibrations for each working context.

### Cross-Platform Memory Coordination

When multiple CLI tools access the same workspace:

**Shared state**: file system contents, git history, output artifacts.
**Isolated state**: each tool's conversation history, internal reasoning, platform-specific memory.

**Coordination protocol**: Use files as the communication medium. Timestamp and attribute file changes. Use git commits as synchronization points. Human operator resolves conflicts.

---

## PART IV: THE DISTILLATION PROTOCOL

### The Problem of Accumulation

Without principled distillation -- what cognitive science since Endel Tulving has called the encoding-retrieval trade-off -- memory systems face two failure modes:
1. **Unbounded growth**: Everything saved, nothing forgotten -- retrieval degradation
2. **Premature loss**: Important insights not captured -- reinvention overhead

### The Distillation Cascade

```
FLUID (Thread) --> OPERATIONAL (Memory) --> CANONICAL (Corpus) --> ETERNAL (Constitution)
     |                    |                       |                      |
     | Thread ends        | Pattern emerges       | Principle proven     |
     | Insight captured   | Worth preserving      | Framework stable     |
     v                    v                       v                      v
  Culmination         Memory edit            Corpus update          Constitution
   document           or context file        (new/revised doc)      revision (rare)
```

### Thread Culmination Protocol

When a thread reaches natural conclusion or length limit:

1. **Trajectory Summary**: How the conversation evolved
2. **Key Insights**: Novel understanding generated
3. **Unresolved Questions**: What remains open
4. **Continuation Context**: Minimum viable context for resumption
5. **Canonical Candidates**: Insights worthy of corpus integration

### Corpus Update Protocol

When operational insights warrant canonical status:

**Graduation criteria**: insight stable across multiple applications, represents genuine framework evolution, fills identified gap, aligns with constitutional principles.

**Update process**: draft document, verify placement, update cross-references, version increment, git commit, propagate to relevant projects.

### The Forgetting Protocol

Principled forgetting prevents accumulation pathology.

**Decay candidates**: task-specific context after completion, superseded drafts after final version, exploratory threads that led nowhere, operational details after pattern extraction.

**Preservation triggers** (override decay): referenced by canonical documents, part of active project context, explicitly marked for retention, contains unreplicated insights.

**Implementation**: thread context decays automatically. Memory edits reviewed monthly. Context files archived after project completion. Corpus documents versioned rather than deleted.

---

## PART V: IIC MEMORY INTEGRATION

Each IIC account requires distinct memory configuration aligned with its chain function:

| IIC | Memory Priority | Forgetting Bias | Persistence |
|-----|----------------|-----------------|-------------|
| **Acumen** (Sensing) | Breadth over depth | Aggressive | Only patterns and qualified signals |
| **Coherence** (Synthesis) | Pattern integration | Moderate | Frameworks persist; raw inputs decay |
| **Efficacy** (Operations) | Process knowledge | Low for procedures | Proven procedures become canonical |
| **Mastery** (Curriculum) | Pedagogical structure | Very low | Educational content deliberately stable |
| **Transcendence** (Wisdom) | Meta-patterns | Minimal | Maximum persistence across longest timescales |

### Cross-IIC Synchronization

The corpus itself is the synchronization primitive. All IICs access the same canonical documents.

```
Acumen (sensing) --> Coherence (synthesis) --> Transcendence (integration)
                                                        |
Mastery (teaching) <-- Efficacy (operations) <----------+
```

Each IIC operates within its domain. Cross-IIC learnings captured in thread culmination. Human operator transfers relevant context between accounts. Corpus updates propagate to all IIC projects on next session.

---

## PART VI: PLATFORM-SPECIFIC IMPLEMENTATION

### Claude

| Stratum | Feature | Configuration |
|---------|---------|---------------|
| 1. Constitutional | Base system prompt | Fixed by Anthropic |
| 2. Preferences | User Preferences | Settings > Profile |
| 3. Accumulated | Memory (basal + project) | Auto-generated, user-editable |
| 4. Project | Projects | Create per IIC |
| 5. Canonical | Project Files | Upload corpus documents |
| 6. Thread | Conversation | Current chat |
| 7. Tool-Extended | CLI tools, computer use | Full system access |

Claude-specific: use memory editing to curate accumulated memory. Use conversation search to retrieve past context. Project Files are the primary canonical layer.

### ChatGPT

| Stratum | Feature | Configuration |
|---------|---------|---------------|
| 1. Constitutional | System behaviors | Fixed by OpenAI |
| 2. Preferences | Custom Instructions | Settings > Personalization |
| 3. Accumulated | Memory | Auto-generated, viewable |
| 4. Project | Projects | Create for scoped context |
| 5. Canonical | File uploads | Upload to Project |
| 6. Thread | Conversation | Can continue indefinitely |
| 7. Tool-Extended | Plugins, actions, Code Interpreter | Configure per GPT |

ChatGPT-specific: Custom Instructions limited to 3,000 characters. Memory more opaque than Claude -- audit regularly. Use Project-Only Memory mode for deterministic tasks. Canvas provides persistent workspace artifacts.

### CLI Tools

| Stratum | Feature | Configuration |
|---------|---------|---------------|
| 1. Constitutional | Model defaults | Per-tool config |
| 2. Preferences | Config files | ~/.claude/settings.json |
| 3. Accumulated | Limited | Most CLI tools don't persist |
| 4. Project | CLAUDE.md / AGENTS.md | Project-level context |
| 5. Canonical | File system | Full read access to corpus |
| 6. Thread | Session | Current terminal session |
| 7. Tool-Extended | Full | File system, git, shell, network |

CLI-specific: CLAUDE.md hierarchy is the primary configuration mechanism. File system is the canonical layer -- full sovereignty. Git provides versioning. Session state doesn't persist -- use files for continuity.

---

## PART VII: OPERATIONAL CHECKLISTS

### New Session

- Verify correct account/project context
- Check that relevant corpus documents are accessible
- Review accumulated memory for accuracy
- Inject any required continuation context
- Confirm tool access

### Thread Culmination

- Generate culmination document
- Identify canonical candidates
- Save artifacts to appropriate location
- Update context files if needed
- Git commit if using CLI

### Monthly Memory Hygiene

- Audit accumulated memory for accuracy
- Remove obsolete memory entries
- Archive completed project contexts
- Review forgetting candidates
- Verify corpus integrity

---

## PART VIII: FUTURE EVOLUTION

**Memory Portability**: Standards for cross-platform memory transfer will emerge. Design current architecture to be export-ready.

**MCP Universalization**: As MCP becomes universal, memory servers will enable coordination. Current file-based approach is MCP-compatible.

**Context Window Expansion**: Larger windows reduce retrieval pressure but don't eliminate memory architecture need. Curation remains valuable.

**Agent Autonomy**: As agents operate longer without human intervention, memory architecture becomes more critical for maintaining coherence.

When platform capabilities change: evaluate which stratum is affected, update platform-specific implementation, preserve universal principles, maintain file-based sovereignty as backup, test new features before full integration.

---

*Neocanon entry -- Tier 3, Chain 0 (Universal)*
