# Subcategory Schema Proposal — CC58

**Date**: 2026-02-28
**Author**: Commander (synthesis of Oracle CC58 + Cartographer CC58-v2)
**Status**: DRAFT — awaiting Sovereign approval
**Git HEAD**: `f906c6b3`

---

## Architecture Decision: Ranganathan Faceted Index

**Subcategories will be implemented as INDEX FILES, not filesystem changes.**

Each of the 5 large folders gets a `SUBCATEGORY-INDEX.md` file at its root. Files do not move. Filenames do not change. The index maps numeric IDs to semantic sub-themes.

**Why this wins** (Cartographer analysis, Commander-validated):
- **Flat Principle compliant** — no nesting, no new directories
- **Zero file I/O** — no git-history bloat from mass renames/moves
- **Poly-hierarchical** — a liminal file can appear in multiple sub-theme sections and be cross-referenced from another folder's index
- **Progressive tightening** — reclassifying a file means editing one line in an index, not moving a file
- **Numeric IDs preserved** — the decoupling of physical identity from semantic classification is a feature, not a bug

**Format per index file:**

```markdown
# Subcategory Index — [folder-name]

## [Sub-theme Name]
Brief description of what this sub-theme covers.

Files: 00029, 00091, 00112, 00118, ...

## [Sub-theme Name]
...

## Cross-References
Files in OTHER folders that are thematically relevant to sub-themes here:
- ai-capability-futures/00162 → relevant to [sub-theme] (scaling mechanics)
- ...
```

---

## Formation Principles (Cartographer-derived)

1. **Threshold of Distinction**: A sub-theme is only justified if its semantic distance from peer sub-themes exceeds its internal variance. If two proposed sub-themes need a paragraph to distinguish, they are one sub-theme.

2. **Asymmetric Density**: Sub-themes follow semantic gravity, not numerical symmetry. A dominant sub-theme with 30% of files and a niche sub-theme with 5% are both valid. Don't force equal distribution.

3. **No type-based sub-themes**: "Extraction Artifacts," "YouTube Interviews," "Pipeline Outputs" are constitutionally forbidden at every granularity level. An extraction about training is ABOUT TRAINING.

4. **Target range**: 5-8 sub-themes per folder (Oracle empirical + Cartographer cognitive load analysis). Enough variety to navigate, few enough to scan.

---

## Proposed Sub-Themes by Folder

### ai-models (880 files) — 6 sub-themes

| Sub-theme | Description | Est. % |
|-----------|-------------|--------|
| **Mathematical Foundations** | Linear algebra, calculus, optimization theory underpinning ML | ~12% |
| **Frontier Model Releases** | Announcements, launches, competitive analysis (GPT, Gemini, Claude, Llama releases) | ~25% |
| **Training & Scaling** | RLHF, data mixing, pre-training methodology, scaling laws as engineering (how to train) | ~18% |
| **Benchmarks & Evaluation** | Arena Hard, MMLU, HumanEval, comparative model performance | ~15% |
| **Architecture & Efficiency** | Transformer variants, Mamba/SSM, tokenization, context extension, inference optimization | ~10% |
| **Fine-Tuning & Adaptation** | LoRA, QLoRA, domain adaptation, instruction tuning, tool interfaces | ~10% |

**Absorbed from Oracle's type-based sub-theme 7**: Extraction artifacts about model topics are redistributed into the sub-theme matching their content (e.g., an extraction about GPT-4o → Frontier Model Releases).

**Unaccounted ~10%**: Files that don't cleanly fit will be classified during index construction. May reveal a 7th sub-theme or distribute across existing ones.

### multi-agent-systems (761 files) — 6 sub-themes

| Sub-theme | Description | Est. % |
|-----------|-------------|--------|
| **External MAS Research** | Academic/industry multi-agent theory, debate frameworks, swarm intelligence, coordination protocols | ~28% |
| **Syncrescendence Operations** | Internal operational artifacts: dispatch confirms, clarescence records, scaffold docs, session state | ~25% |
| **Orchestration Patterns** | Fault-tolerant consensus, task decomposition, fleet dispatch patterns (general, not tool-specific) | ~15% |
| **MCP & Protocol Engineering** | Model Context Protocol patterns, tool-calling interfaces, permission scoping, harness design | ~12% |
| **Sub-Agent Delegation** | Skills registries, delegation graphs, parent-child agent routing, compound task mechanics | ~10% |
| **Architecture & Frameworks** | Production frameworks, scaffold design, state management patterns for multi-agent systems | ~10% |

**Migration candidates** (Oracle-identified): ~12 pure infrastructure scripts → infrastructure folder. ~8 ClawdBot-specific fleet records → openclaw.

### claude-code (577 files) — 6 sub-themes

| Sub-theme | Description | Est. % |
|-----------|-------------|--------|
| **Core Architecture** | CLI internals, Plan Mode mechanics, context compaction, permissions model | ~22% |
| **Extended Thinking & Reasoning** | Thinking traces, reasoning chains, compound engineering patterns | ~18% |
| **MCP & Sub-Agent Integration** | MCP server patterns, sub-agent spawning, tool-calling harness within Claude Code | ~15% |
| **Customization & Skills** | Hooks, custom skills, workflow automation, CLAUDE.md patterns, user extensions | ~15% |
| **Community & Usage Patterns** | Adoption stories, production workflows, community discussion, operational census | ~12% |
| **Security & Isolation** | Worktrees, sandboxing, permission enforcement, multi-user security | ~10% |

**Migration candidates**: ~22 general AI-coding files (no Claude-specific content) → vibe-coding. ~9 operational census/pool reports → multi-agent-systems.

### openclaw (572 files) — 6 sub-themes

| Sub-theme | Description | Est. % |
|-----------|-------------|--------|
| **Installation & Configuration** | Setup guides, plist config, deployment procedures, initial hardening | ~20% |
| **Memory & Personality** | SOUL.md, episodic recall, vector stores, behavioral priors, personality persistence | ~18% |
| **Phone & Multi-Device Fleets** | SMS dispatch, fleet synchronization, marketplace, cross-device agent routing | ~15% |
| **Security & Cost Optimization** | Permission scoping, sandboxing, inference throttling, cost management | ~12% |
| **Operational Tooling** | Watchdog scripts, health monitoring, kanbanized dispatch, operational workflows | ~12% |
| **Ecosystem & Comparative Analysis** | Deep research articles, MiniMax setups, competitive analysis, community discourse | ~13% |

**Migration candidates**: ~18 organizational philosophy files ("Your Company is a Filesystem" etc.) → meaning-civilization or product-business (depends on content — about organizational theory, or about OpenClaw specifically?). ~7 MiniMax-specific model files → ai-models if model-focused.

### ai-capability-futures (448 files) — 6 sub-themes

| Sub-theme | Description | Est. % |
|-----------|-------------|--------|
| **AGI Timelines & Predictions** | Expert forecasts, timeline analyses, when-not-if arguments | ~22% |
| **Scaling Laws & Trajectories** | Chinchilla-optimal, data walls, emergent abilities, phase transitions — the physics of capability growth | ~18% |
| **Agent Evals & Capability Benchmarks** | SWE-bench, GAIA, real-world tool-use assessment, autonomous coding evaluations | ~15% |
| **Market & Investment Analysis** | AI bubble indicators, VC dynamics, valuation analysis, market correction scenarios | ~12% |
| **Democratization & Open Models** | Open-source frontier models, capability distribution, access equity | ~11% |
| **Human-AI Symbiosis** | Second brains, extended mind, personal capability augmentation, daily AI integration | ~12% |

**Migration candidates**: Jordan Peterson lectures (~12 files) → meaning-civilization. Karpathy programming language talks (~8 files) → vibe-coding or ai-models. ~5 OpenClaw second-brain articles → openclaw if product-focused. "Fractal frontier / network state" content — evaluate whether it's futures-oriented (stays) or geopolitics-oriented (→ geopolitics-grand-strategy).

---

## Cross-Affinity Map (Cartographer-derived)

### The Agency Triad
`multi-agent-systems` ↔ `claude-code` ↔ `openclaw` — dissolving boundaries. All three are expressions of "local agentic orchestration." The indexes should heavily cross-reference each other.

### The Cognition Pair
`ai-models` ↔ `ai-capability-futures` — engine vs horizon. Training scaling (how it works) vs capability scaling (what it means). Boundary principle: mechanics = ai-models, trajectory = ai-capability-futures.

### Satellite Affinities
- ai-models ↔ ai-memory-retrieval (RAG architectures are model-adjacent)
- claude-code ↔ vibe-coding (tool vs practice — migration candidates flow this direction)
- ai-capability-futures ↔ geopolitics-grand-strategy (civilizational AI trajectory)
- ai-capability-futures ↔ ai-safety (capability implies risk)
- openclaw ↔ meaning-civilization (organizational philosophy content)

---

## Metacategories (Future — Not Implemented Now)

Cartographer identified 2 natural metacategories. These are noted for future textbook structure, not for immediate action:

1. **Agency**: multi-agent-systems, claude-code, openclaw, vibe-coding
2. **Cognition**: ai-models, ai-capability-futures, ai-memory-retrieval, ai-safety

(Additional metacategories TBD as the remaining 17 folders are analyzed.)

---

## Execution Plan (Pending Sovereign Approval)

1. **Construct 5 index files**: One `SUBCATEGORY-INDEX.md` per target folder. Commander reads files, assigns to sub-themes, builds the index. This is the bulk work.
2. **Process migration candidates**: ~97 files across 5 folders identified for potential relocation. Spot-check content before moving.
3. **Cross-reference construction**: After indexes are built, add cross-reference sections linking liminal files across folders.
4. **Adjudicator verification**: Dispatch spot-check audit — sample files from each sub-theme, verify classification accuracy.

---

*This proposal synthesizes Oracle's content traversal (sub-themes, filenames, evidence) with Cartographer's structural analysis (Ranganathan index, formation principles, affinity matrix). The architecture is Flat Principle compliant, progressively tightenable, and reversible.*
