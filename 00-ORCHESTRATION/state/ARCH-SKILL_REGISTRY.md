# Skill Registry — Syncrescendence Constellation
## ARCH-SKILL_REGISTRY.md

**Document Type**: ARCHITECTURE (Living Document)
**Last Updated**: 2026-02-12 (registry created)
**Last Verified**: 2026-02-15 (Commander formalization gap closure)
**Source**: Skills Architecture Overhaul — BLITZKRIEG Phase 1

---

## Purpose
Centralized manifest of all skills available to the Syncrescendence constellation.
Every skill — canonical, project, or workspace — is registered here with provenance,
security status, bifurcation (agent vs sovereign), pipeline stage assignments,
and wiring state.

## Anti-Shelfware Rule
Every skill with Status=active MUST have a non-empty `Wired To` field (hook, chain,
agent-loop, or slash-command). Skills with empty wiring after 30-day review → Status=dormant.

## Bifurcation Schema
- **agent**: Used in automation/agent-loops, always loaded
- **sovereign**: Slash commands invoked by the Sovereign, heuristically minimal
- **both**: Available to both agents and Sovereign

## Consolidation Groups
Skills with overlapping functionality are tagged with a consolidation group ID.
Consolidation reduces 264 → ~196 effective skills through mode-parameterized wrappers.

---

## Statistics
| Category | Count | Active | Dormant | Quarantined |
|----------|-------|--------|---------|-------------|
| Syncrescendence Project | 18 | 18 | 0 | 0 |
| CEK (Context Engineering Kit) | 62 | 62 | 0 | 0 |
| AI Research | 83 | ~40 | ~43 | 0 |
| Trail of Bits Security | 32 | ~26 | ~6 | 0 |
| Trail of Bits Blockchain | 6 | 0 | 0 | 6 |
| Vibeship/Community Utility | 63 | 19 | 44 | 0 |
| **TOTAL** | **264** | **194** | **64** | **6** |

### Installation Verification (2026-02-15)

**MBA Claude Code project-level skills** (`.claude/skills/`): 34 installed
- 18 Syncrescendence project skills (all present)
- 16 canonical skills promoted to project level: brainstorming, commit-work, dispatching-parallel-agents, google-ai-mode-skill, last30days, lastday, lastweek, memory-systems, mermaid-diagrams, planning-with-files, session-handoff, skill-judge, subagent-driven-development, systematic-debugging, tmux, web-to-markdown, verification-before-completion

**MBA Claude Code user-level skills** (`~/.claude/skills/`): 35 installed (34 symlinks to project + 1 standalone: `mba-commander-init`)

**Skill sync pipeline**: `com.syncrescendence.skill-sync` launchd agent active on MBA with WatchPaths trigger and 5-second debounce.

**DEC-C3 hard gates (enacted 2026-02-13)**: triage, claresce, execute, verification-before-completion, update_universal_ledger are wired into CLAUDE.md as mandatory stage gates per Ajna strategic assessment.

**Anti-shelfware rule**: DEFINED in this document but NOT ENFORCED as automated lint. No cadenced sweep verifies the 30-day dormancy rule.

**Security audit status**: Adjudicator completed 230-skill audit (2026-02-12): 0 quarantine, 119 flagged (false-positive heavy -- URLs + credential refs in skill text), 111 cleared. Full 264-skill security audit per meta-clarescence recommendation: NOT DONE.

---

# 1. Syncrescendence Project Skills (18)

All skills in this section: `source=project`, `provenance=syncrescendence`, `security=vetted`.

| Name | Source | Provenance | Status | Bifurcation | Tier | Pipeline Stages | Platform Deps | Consolidation Group | Agents | Wired To | Security | Description |
|------|--------|------------|--------|-------------|------|-----------------|---------------|---------------------|--------|----------|----------|-------------|
| audize | project | syncrescendence | active | both | T1-operational | ingest, transform | ffmpeg | MEDIA-INGEST | Commander, Ajna | slash-command | vetted | Audio transcription and processing pipeline |
| blitzkrieg_teams | project | syncrescendence | active | agent | T0-strategic | plan, dispatch | git, gh | — | Commander | agent-loop | vetted | Multi-agent blitzkrieg team coordination |
| claresce | project | syncrescendence | active | both | T0-strategic | plan, clarify | — | — | Commander, Ajna | slash-command, agent-loop | vetted | Clarescence facilitation — structured clarification sessions |
| execute | project | syncrescendence | active | agent | T0-strategic | execute | git, bash | EXEC | Commander, Psyche | agent-loop | vetted | Core execution orchestrator for task dispatch |
| find-skills | project | syncrescendence | active | both | T1-operational | lookup | — | SKILL-LOOKUP | all | slash-command | vetted | Project-local skill discovery (overrides canonical) |
| integrate | project | syncrescendence | active | agent | T1-operational | integrate, verify | git, gh | — | Psyche, Commander | agent-loop | vetted | Integration pipeline for merging agent work products |
| intentions | project | syncrescendence | active | both | T0-strategic | plan, prioritize | — | — | Commander, Ajna | slash-command, agent-loop | vetted | Intention stack management and compass alignment |
| listenize | project | syncrescendence | active | both | T1-operational | ingest, transform | ffmpeg | MEDIA-INGEST | Commander, Ajna | slash-command | vetted | Audio listening and extraction pipeline |
| method_kaizen | project | syncrescendence | active | both | T1-operational | review, improve | — | KAIZEN | Commander, Adjudicator | slash-command | vetted | Continuous method improvement via kaizen cycles |
| pedigree | project | syncrescendence | active | agent | T1-operational | audit, trace | git | — | Adjudicator, Cartographer | agent-loop | vetted | Provenance tracking and lineage auditing |
| plan | project | syncrescendence | active | both | T0-strategic | plan | git, gh | PLAN | Commander | slash-command, agent-loop | vetted | Project-level planning orchestrator |
| readize | project | syncrescendence | active | both | T1-operational | ingest, transform | — | MEDIA-INGEST | Commander, Ajna | slash-command | vetted | Reading ingestion and summarization pipeline |
| reviewtrospective | project | syncrescendence | active | both | T1-operational | review, reflect | — | REVIEW | Adjudicator, Commander | slash-command | vetted | Retrospective review and lessons-learned extraction |
| transcribe_interview | project | syncrescendence | active | both | T1-operational | ingest, transform | ffmpeg | MEDIA-INGEST | Commander, Ajna | slash-command | vetted | Interview transcription with speaker diarization |
| transcribe_youtube | project | syncrescendence | active | both | T1-operational | ingest, transform | yt-dlp, ffmpeg | MEDIA-INGEST | Commander, Ajna | slash-command | vetted | YouTube video transcription pipeline |
| triage | project | syncrescendence | active | both | T0-strategic | triage, prioritize | — | — | Commander, Adjudicator | slash-command, agent-loop | vetted | Incoming work item triage and routing |
| update_agent_memory | project | syncrescendence | active | agent | T1-operational | memory, persist | — | MEMORY | all | agent-loop | vetted | Agent memory update and consolidation |
| update_universal_ledger | project | syncrescendence | active | agent | T1-operational | audit, persist | — | — | Commander, Cartographer | agent-loop | vetted | Universal ledger synchronization |

---

# 2. CEK Skills — Context Engineering Kit (62)

All skills in this section: `source=canonical`, `provenance=cek`, `security=vetted`.

## 2.1 CEK — Analysis (8)

| Name | Source | Provenance | Status | Bifurcation | Tier | Pipeline Stages | Platform Deps | Consolidation Group | Agents | Wired To | Security | Description |
|------|--------|------------|--------|-------------|------|-----------------|---------------|---------------------|--------|----------|----------|-------------|
| cek-analyse | canonical | cek | active | both | T1-operational | analyse | — | CEK-ANALYSIS | Commander, Adjudicator | slash-command, agent-loop | vetted | General-purpose analysis framework |
| cek-analyse-problem | canonical | cek | active | both | T1-operational | analyse | — | CEK-ANALYSIS | Commander, Adjudicator | slash-command, agent-loop | vetted | Structured problem analysis with decomposition |
| cek-analyze-issue | canonical | cek | active | both | T1-operational | analyse | gh | CEK-ANALYSIS | Commander, Adjudicator | slash-command, agent-loop | vetted | GitHub issue analysis and categorization |
| cek-cause-and-effect | canonical | cek | active | both | T1-operational | analyse | — | CEK-ANALYSIS | Commander, Adjudicator | slash-command, agent-loop | vetted | Cause-and-effect chain analysis (Ishikawa) |
| cek-kaizen | canonical | cek | active | both | T1-operational | analyse, improve | — | KAIZEN | Commander, Adjudicator | slash-command, agent-loop | vetted | Continuous improvement via kaizen methodology |
| cek-why | canonical | cek | active | both | T1-operational | analyse | — | CEK-ANALYSIS | Commander, Adjudicator | slash-command, agent-loop | vetted | Five Whys root cause interrogation |
| cek-root-cause-tracing | canonical | cek | active | both | T1-operational | analyse | — | CEK-ANALYSIS | Commander, Adjudicator | slash-command, agent-loop | vetted | Root cause tracing with evidence chains |
| cek-plan-do-check-act | canonical | cek | active | both | T1-operational | analyse, execute | — | CEK-ANALYSIS | Commander, Adjudicator | slash-command, agent-loop | vetted | PDCA cycle implementation |

## 2.2 CEK — Planning (3)

| Name | Source | Provenance | Status | Bifurcation | Tier | Pipeline Stages | Platform Deps | Consolidation Group | Agents | Wired To | Security | Description |
|------|--------|------------|--------|-------------|------|-----------------|---------------|---------------------|--------|----------|----------|-------------|
| cek-plan | canonical | cek | active | agent | T0-strategic | plan | gh, git | PLAN | Commander | agent-loop | vetted | Strategic planning with GitHub integration |
| cek-add-task | canonical | cek | active | both | T1-operational | plan, dispatch | bash | — | Commander | slash-command, agent-loop | vetted | Task creation and backlog insertion |
| cek-software-architecture | canonical | cek | active | both | T1-operational | plan, design | — | — | Psyche, Commander | slash-command | vetted | Software architecture design and documentation |

## 2.3 CEK — Review (8)

| Name | Source | Provenance | Status | Bifurcation | Tier | Pipeline Stages | Platform Deps | Consolidation Group | Agents | Wired To | Security | Description |
|------|--------|------------|--------|-------------|------|-----------------|---------------|---------------------|--------|----------|----------|-------------|
| cek-agent-evaluation | canonical | cek | active | agent | T1-operational | review, evaluate | — | CEK-REVIEW | Adjudicator, Commander | agent-loop | vetted | Agent output quality evaluation |
| cek-attach-review-to-pr | canonical | cek | active | agent | T1-operational | review, publish | gh | CEK-REVIEW | Adjudicator, Commander | agent-loop | vetted | Attach structured review comments to GitHub PR |
| cek-critique | canonical | cek | active | agent | T1-operational | review | — | CEK-REVIEW | Adjudicator, Commander | agent-loop | vetted | Structured critique framework |
| cek-judge | canonical | cek | active | agent | T1-operational | review, evaluate | — | CEK-REVIEW | Adjudicator, Commander | agent-loop | vetted | Quality judgment with rubric scoring |
| cek-judge-with-debate | canonical | cek | active | agent | T1-operational | review, evaluate | — | CEK-REVIEW | Adjudicator, Commander | agent-loop | vetted | Adversarial debate-based judgment |
| cek-reflect | canonical | cek | active | both | T1-operational | review, reflect | — | CEK-REVIEW | Adjudicator, Commander | slash-command, agent-loop | vetted | Structured self-reflection protocol |
| cek-review-local-changes | canonical | cek | active | agent | T1-operational | review | git | CEK-REVIEW | Adjudicator, Commander | agent-loop | vetted | Review uncommitted local changes for quality |
| cek-review-pr | canonical | cek | active | agent | T1-operational | review | gh, git | CEK-REVIEW | Adjudicator, Commander | agent-loop | vetted | Full pull request review pipeline |

## 2.4 CEK — Git Worktrees (5)

| Name | Source | Provenance | Status | Bifurcation | Tier | Pipeline Stages | Platform Deps | Consolidation Group | Agents | Wired To | Security | Description |
|------|--------|------------|--------|-------------|------|-----------------|---------------|---------------------|--------|----------|----------|-------------|
| cek-compare-worktrees | canonical | cek | active | both | T2-sprint | compare, review | git | CEK-WORKTREE | Psyche, Commander | slash-command | vetted | Diff comparison across git worktrees |
| cek-create-worktree | canonical | cek | active | both | T2-sprint | execute | git | CEK-WORKTREE | Psyche, Commander | slash-command | vetted | Create and configure a new git worktree |
| cek-merge-worktree | canonical | cek | active | both | T2-sprint | integrate | git | CEK-WORKTREE | Psyche, Commander | slash-command | vetted | Merge worktree branch back to main |
| cek-worktrees | canonical | cek | active | both | T2-sprint | manage | git | CEK-WORKTREE | Psyche, Commander | slash-command | vetted | List and manage active git worktrees |
| cek-notes | canonical | cek | active | both | T2-sprint | annotate | git | CEK-WORKTREE | Psyche, Commander | slash-command | vetted | Git notes management for metadata annotation |

## 2.5 CEK — Reasoning (4)

| Name | Source | Provenance | Status | Bifurcation | Tier | Pipeline Stages | Platform Deps | Consolidation Group | Agents | Wired To | Security | Description |
|------|--------|------------|--------|-------------|------|-----------------|---------------|---------------------|--------|----------|----------|-------------|
| cek-context-engineering | canonical | cek | active | both | T0-strategic | reason, design | — | CEK-REASONING | all | slash-command, agent-loop | vetted | Context engineering methodology and patterns |
| cek-thought-based-reasoning | canonical | cek | active | both | T1-operational | reason | — | CEK-REASONING | all | slash-command, agent-loop | vetted | Chain-of-thought structured reasoning |
| cek-tree-of-thoughts | canonical | cek | active | agent | T1-operational | reason | — | CEK-REASONING | all | agent-loop | vetted | Tree-of-thoughts branching exploration |
| cek-prompt-engineering | canonical | cek | active | both | T1-operational | reason, design | — | CEK-REASONING | all | slash-command, agent-loop | vetted | Prompt engineering best practices and patterns |

## 2.6 CEK — Execution (15)

| Name | Source | Provenance | Status | Bifurcation | Tier | Pipeline Stages | Platform Deps | Consolidation Group | Agents | Wired To | Security | Description |
|------|--------|------------|--------|-------------|------|-----------------|---------------|---------------------|--------|----------|----------|-------------|
| cek-commit | canonical | cek | active | both | T2-sprint | commit | git | CEK-GIT-OPS | Commander, Psyche | slash-command, agent-loop | vetted | Structured git commit with conventional format |
| cek-create-pr | canonical | cek | active | both | T2-sprint | publish | gh | CEK-GIT-OPS | Commander, Psyche | slash-command, agent-loop | vetted | Create pull request with structured description |
| cek-create-hook | canonical | cek | active | both | T2-sprint | execute, configure | — | — | Commander, Psyche | slash-command | vetted | Create git hooks or automation hooks |
| cek-do-and-judge | canonical | cek | active | agent | T1-operational | execute, review | — | CEK-EXEC | Commander, Psyche | agent-loop | vetted | Execute then self-evaluate output quality |
| cek-do-competitively | canonical | cek | active | agent | T1-operational | execute, evaluate | — | CEK-EXEC | Commander, Psyche | agent-loop | vetted | Parallel competitive execution with best-pick |
| cek-do-in-parallel | canonical | cek | active | agent | T1-operational | execute | — | CEK-EXEC | Commander, Psyche | agent-loop | vetted | Fan-out parallel task execution |
| cek-do-in-steps | canonical | cek | active | agent | T0-strategic | execute | — | CEK-EXEC | Commander, Psyche | agent-loop | vetted | Sequential step-by-step execution |
| cek-fix-tests | canonical | cek | active | agent | T1-operational | execute, fix | — | CEK-TDD | Commander, Psyche | agent-loop | vetted | Automated test failure diagnosis and fix |
| cek-implement | canonical | cek | active | agent | T0-strategic | execute | — | EXEC | Commander, Psyche | agent-loop | vetted | Core implementation skill — code generation |
| cek-launch-sub-agent | canonical | cek | active | agent | T1-operational | dispatch | — | CEK-MULTI-AGENT | Commander, Psyche | agent-loop | vetted | Sub-agent spawning and lifecycle management |
| cek-load-issues | canonical | cek | active | both | T2-sprint | ingest | gh | — | Commander, Psyche | slash-command, agent-loop | vetted | Load GitHub issues into working context |
| cek-subagent-driven-development | canonical | cek | active | agent | T1-operational | execute, dispatch | — | CEK-MULTI-AGENT | Commander, Psyche | agent-loop | vetted | Development via orchestrated sub-agents |
| cek-test-driven-development | canonical | cek | active | both | T1-operational | execute, test | — | CEK-TDD | Commander, Psyche | slash-command, agent-loop | vetted | TDD red-green-refactor cycle |
| cek-write-tests | canonical | cek | active | agent | T1-operational | test | git | CEK-TDD | Commander, Psyche | agent-loop | vetted | Automated test generation |
| cek-update-docs | canonical | cek | active | agent | T1-operational | document | git | — | Commander, Psyche | agent-loop | vetted | Documentation update and synchronization |

## 2.7 CEK — Meta (12)

| Name | Source | Provenance | Status | Bifurcation | Tier | Pipeline Stages | Platform Deps | Consolidation Group | Agents | Wired To | Security | Description |
|------|--------|------------|--------|-------------|------|-----------------|---------------|---------------------|--------|----------|----------|-------------|
| cek-add-typescript-best-practices | canonical | cek | active | sovereign | T2-sprint | configure | — | — | Psyche | slash-command | vetted | Add TypeScript best practices to project config |
| cek-apply-anthropic-skill-best-practices | canonical | cek | active | both | T1-operational | meta | — | CEK-META | all | slash-command | vetted | Apply Anthropic skill authoring standards |
| cek-build-mcp | canonical | cek | active | both | T2-sprint | execute | python, node | — | Psyche, Commander | slash-command | vetted | Build MCP server implementation |
| cek-create-agent | canonical | cek | active | both | T1-operational | meta | — | CEK-META | Commander | slash-command | vetted | Create new agent definition and configuration |
| cek-create-command | canonical | cek | active | both | T1-operational | meta | — | CEK-META | Commander | slash-command | vetted | Create new CLI command definition |
| cek-create-skill | canonical | cek | active | both | T1-operational | meta | — | CEK-META | Commander | slash-command | vetted | Create new skill definition from template |
| cek-create-workflow-command | canonical | cek | active | both | T1-operational | meta | — | CEK-META | Commander | slash-command | vetted | Create workflow command with chained steps |
| cek-memorize | canonical | cek | active | both | T1-operational | memory, persist | — | MEMORY | all | slash-command, agent-loop | vetted | Commit insight or fact to persistent memory |
| cek-multi-agent-patterns | canonical | cek | active | both | T0-strategic | design | — | CEK-MULTI-AGENT | Commander | slash-command | vetted | Multi-agent coordination pattern library |
| cek-test-prompt | canonical | cek | active | agent | T1-operational | test | — | CEK-META | Commander | agent-loop | vetted | Test and validate prompt templates |
| cek-test-skill | canonical | cek | active | agent | T1-operational | test | — | CEK-META | Commander | agent-loop | vetted | Test and validate skill definitions |
| cek-write-concisely | canonical | cek | active | both | T2-sprint | transform | — | — | all | slash-command | vetted | Concise writing style enforcement |

## 2.8 CEK — Brainstorm (2)

| Name | Source | Provenance | Status | Bifurcation | Tier | Pipeline Stages | Platform Deps | Consolidation Group | Agents | Wired To | Security | Description |
|------|--------|------------|--------|-------------|------|-----------------|---------------|---------------------|--------|----------|----------|-------------|
| cek-brainstorm | canonical | cek | active | both | T1-operational | ideate | — | CEK-BRAINSTORM | all | slash-command | vetted | Structured brainstorming with diverge/converge |
| cek-create-ideas | canonical | cek | active | agent | T1-operational | ideate | — | CEK-BRAINSTORM | all | agent-loop | vetted | Automated idea generation and clustering |

## 2.9 CEK — Setup (5)

| Name | Source | Provenance | Status | Bifurcation | Tier | Pipeline Stages | Platform Deps | Consolidation Group | Agents | Wired To | Security | Description |
|------|--------|------------|--------|-------------|------|-----------------|---------------|---------------------|--------|----------|----------|-------------|
| cek-setup-arxiv-mcp | canonical | cek | active | sovereign | T3-session | configure | docker | CEK-SETUP | Psyche | slash-command | unvetted | Setup arXiv MCP server for paper retrieval |
| cek-setup-code-formating | canonical | cek | active | sovereign | T3-session | configure | — | CEK-SETUP | Psyche | slash-command | vetted | Setup code formatting tools (prettier, etc.) |
| cek-setup-codemap-cli | canonical | cek | active | sovereign | T3-session | configure | homebrew | CEK-SETUP | Psyche | slash-command | unvetted | Setup codemap CLI for codebase visualization |
| cek-setup-context7-mcp | canonical | cek | active | sovereign | T3-session | configure | — | CEK-SETUP | Psyche | slash-command | unvetted | Setup Context7 MCP server |
| cek-setup-serena-mcp | canonical | cek | active | sovereign | T3-session | configure | — | CEK-SETUP | Psyche | slash-command | unvetted | Setup Serena MCP server for code navigation |

---

# 3. AI Research Skills (83)

All skills in this section: `source=canonical`, `provenance=ai-research`.

## 3.1 ML/Training (18)

| Name | Source | Provenance | Status | Bifurcation | Tier | Pipeline Stages | Platform Deps | Consolidation Group | Agents | Wired To | Security | Description |
|------|--------|------------|--------|-------------|------|-----------------|---------------|---------------------|--------|----------|----------|-------------|
| fine-tuning-llms | canonical | ai-research | active | both | T1-operational | train | GPU, python | ML-FINETUNE | Psyche, Ajna | slash-command | vetted | General LLM fine-tuning methodology |
| llama-factory | canonical | ai-research | active | both | T1-operational | train | GPU, python | ML-FINETUNE | Psyche, Ajna | slash-command | vetted | LLaMA-Factory unified fine-tuning framework |
| lora-fine-tuning | canonical | ai-research | active | both | T1-operational | train | GPU, python | ML-FINETUNE | Psyche, Ajna | slash-command | vetted | LoRA parameter-efficient fine-tuning |
| peft | canonical | ai-research | active | both | T1-operational | train | GPU, python | ML-FINETUNE | Psyche, Ajna | slash-command | vetted | HuggingFace PEFT library methods |
| qlora-fine-tuning | canonical | ai-research | active | both | T1-operational | train | GPU, python | ML-FINETUNE | Psyche, Ajna | slash-command | vetted | QLoRA quantized fine-tuning |
| trl-fine-tuning | canonical | ai-research | active | both | T1-operational | train | GPU, python | ML-FINETUNE | Psyche, Ajna | slash-command | vetted | TRL (Transformer Reinforcement Learning) |
| unsloth | canonical | ai-research | active | both | T1-operational | train | GPU, python | ML-FINETUNE | Psyche, Ajna | slash-command | vetted | Unsloth 2x faster fine-tuning |
| axolotl | canonical | ai-research | active | both | T1-operational | train | GPU, python | ML-FINETUNE | Psyche, Ajna | slash-command | vetted | Axolotl streamlined fine-tuning |
| reward-modeling | canonical | ai-research | active | both | T1-operational | train | GPU, python | ML-RLHF | Psyche, Ajna | slash-command | vetted | Reward model training for RLHF |
| rlhf-training | canonical | ai-research | active | both | T1-operational | train | GPU, python | ML-RLHF | Psyche, Ajna | slash-command | vetted | RLHF training pipeline |
| dpo-training | canonical | ai-research | active | both | T1-operational | train | GPU, python | ML-RLHF | Psyche, Ajna | slash-command | vetted | Direct Preference Optimization training |
| verl | canonical | ai-research | active | both | T1-operational | train | GPU, python | ML-RLHF | Psyche, Ajna | slash-command | vetted | VERL scalable RL training framework |
| open-rlhf | canonical | ai-research | active | both | T1-operational | train | GPU, python | ML-RLHF | Psyche, Ajna | slash-command | vetted | Open-source RLHF training toolkit |
| slime | canonical | ai-research | active | both | T2-sprint | train | GPU, python | ML-RL | Psyche, Ajna | slash-command | vetted | SLIME RL environment integration |
| miles-rl | canonical | ai-research | active | both | T2-sprint | train | GPU, python | ML-RL | Psyche, Ajna | slash-command | vetted | MILES reinforcement learning framework |
| torchforge | canonical | ai-research | active | both | T2-sprint | train | GPU, python | — | Psyche, Ajna | slash-command | vetted | TorchForge training utility library |
| pretraining-llms | canonical | ai-research | active | both | T0-strategic | train | GPU, python | — | Psyche, Ajna | slash-command | vetted | LLM pretraining from scratch methodology |
| data-preprocessing | canonical | ai-research | active | both | T1-operational | ingest, transform | python | — | Psyche, Ajna | slash-command | vetted | Training data preprocessing and curation |

## 3.2 Quantization (7)

| Name | Source | Provenance | Status | Bifurcation | Tier | Pipeline Stages | Platform Deps | Consolidation Group | Agents | Wired To | Security | Description |
|------|--------|------------|--------|-------------|------|-----------------|---------------|---------------------|--------|----------|----------|-------------|
| awq-quantization | canonical | ai-research | active | both | T1-operational | optimize | GPU, python | ML-QUANT | Psyche, Ajna | slash-command | vetted | AWQ activation-aware weight quantization |
| gguf | canonical | ai-research | active | both | T1-operational | optimize, export | python | ML-QUANT | Psyche, Ajna | slash-command | vetted | GGUF model format conversion |
| gptq-quantization | canonical | ai-research | active | both | T1-operational | optimize | GPU, python | ML-QUANT | Psyche, Ajna | slash-command | vetted | GPTQ post-training quantization |
| hqq-quantization | canonical | ai-research | active | both | T1-operational | optimize | GPU, python | ML-QUANT | Psyche, Ajna | slash-command | vetted | HQQ half-quadratic quantization |
| quantizing-models-bitsandbytes | canonical | ai-research | active | both | T1-operational | optimize | GPU, python | ML-QUANT | Psyche, Ajna | slash-command | vetted | bitsandbytes 4/8-bit quantization |
| model-merging | canonical | ai-research | active | both | T1-operational | optimize | GPU, python | ML-MODEL-OPS | Psyche, Ajna | slash-command | vetted | Model merging techniques (SLERP, TIES, DARE) |
| model-pruning | canonical | ai-research | active | both | T1-operational | optimize | GPU, python | ML-MODEL-OPS | Psyche, Ajna | slash-command | vetted | Model pruning and sparsification |

## 3.3 Inference/Serving (8)

| Name | Source | Provenance | Status | Bifurcation | Tier | Pipeline Stages | Platform Deps | Consolidation Group | Agents | Wired To | Security | Description |
|------|--------|------------|--------|-------------|------|-----------------|---------------|---------------------|--------|----------|----------|-------------|
| serving-llms-vllm | canonical | ai-research | active | both | T1-operational | serve | GPU, python | ML-SERVE | Psyche | slash-command | vetted | vLLM high-throughput LLM serving |
| sglang | canonical | ai-research | active | both | T1-operational | serve | GPU, python | ML-SERVE | Psyche | slash-command | vetted | SGLang structured generation serving |
| llama-cpp | canonical | ai-research | active | both | T1-operational | serve | C++, cmake | ML-SERVE | Psyche | slash-command | vetted | llama.cpp CPU/GPU inference engine |
| tensorrt-llm | canonical | ai-research | active | both | T1-operational | serve | GPU, CUDA | ML-SERVE | Psyche | slash-command | vetted | TensorRT-LLM optimized NVIDIA inference |
| speculative-decoding | canonical | ai-research | active | both | T1-operational | serve | GPU, python | ML-SERVE | Psyche | slash-command | vetted | Speculative decoding acceleration |
| optimizing-attention-flash | canonical | ai-research | active | both | T1-operational | optimize | GPU, CUDA | ML-ATTENTION | Psyche | slash-command | vetted | FlashAttention and memory-efficient attention |
| long-context | canonical | ai-research | active | both | T1-operational | serve | GPU, python | ML-ATTENTION | Psyche | slash-command | vetted | Long context window techniques (RoPE, ALiBi) |
| outlines | canonical | ai-research | active | both | T1-operational | serve | python | — | Psyche | slash-command | vetted | Outlines structured generation / constrained decoding |

## 3.4 Framework/Agent (7)

| Name | Source | Provenance | Status | Bifurcation | Tier | Pipeline Stages | Platform Deps | Consolidation Group | Agents | Wired To | Security | Description |
|------|--------|------------|--------|-------------|------|-----------------|---------------|---------------------|--------|----------|----------|-------------|
| langchain | canonical | ai-research | active | both | T1-operational | orchestrate | python | ML-FRAMEWORK | Psyche, Commander | slash-command | vetted | LangChain LLM application framework |
| llamaindex | canonical | ai-research | active | both | T1-operational | orchestrate | python | ML-FRAMEWORK | Psyche, Commander | slash-command | vetted | LlamaIndex RAG and data framework |
| dspy | canonical | ai-research | active | both | T1-operational | orchestrate | python | ML-FRAMEWORK | Psyche, Commander | slash-command | vetted | DSPy programmatic prompt optimization |
| instructor | canonical | ai-research | active | both | T1-operational | orchestrate | python | ML-FRAMEWORK | Psyche, Commander | slash-command | vetted | Instructor structured output extraction |
| guidance | canonical | ai-research | active | both | T1-operational | orchestrate | python | ML-FRAMEWORK | Psyche, Commander | slash-command | vetted | Guidance constrained generation framework |
| crewai-multi-agent | canonical | ai-research | active | both | T1-operational | orchestrate | python | ML-MULTI-AGENT | Commander | slash-command | vetted | CrewAI multi-agent orchestration |
| autogpt-agents | canonical | ai-research | active | both | T1-operational | orchestrate | python | ML-MULTI-AGENT | Commander | slash-command | vetted | AutoGPT autonomous agent patterns |

## 3.5 Vision/Audio/Multimodal (7)

| Name | Source | Provenance | Status | Bifurcation | Tier | Pipeline Stages | Platform Deps | Consolidation Group | Agents | Wired To | Security | Description |
|------|--------|------------|--------|-------------|------|-----------------|---------------|---------------------|--------|----------|----------|-------------|
| clip | canonical | ai-research | dormant | both | T2-sprint | inference | GPU, python | ML-VISION | Ajna | — | vetted | CLIP vision-language embedding model |
| llava | canonical | ai-research | dormant | both | T2-sprint | inference | GPU, python | ML-VISION | Ajna | — | vetted | LLaVA visual instruction tuning |
| blip-2-vision-language | canonical | ai-research | dormant | both | T2-sprint | inference | GPU, python | ML-VISION | Ajna | — | vetted | BLIP-2 vision-language pretraining |
| segment-anything-model | canonical | ai-research | dormant | both | T2-sprint | inference | GPU, python | ML-VISION | Ajna | — | vetted | SAM image segmentation foundation model |
| whisper | canonical | ai-research | dormant | both | T2-sprint | inference | GPU, python | ML-AUDIO | Ajna | — | vetted | OpenAI Whisper speech recognition |
| audiocraft-audio-generation | canonical | ai-research | dormant | both | T2-sprint | inference | GPU, python | ML-AUDIO | Ajna | — | vetted | AudioCraft music and audio generation |
| stable-diffusion-image-generation | canonical | ai-research | dormant | both | T2-sprint | inference | GPU, python | ML-VISION | Ajna | — | vetted | Stable Diffusion image generation |

## 3.6 Vector/Memory (7)

| Name | Source | Provenance | Status | Bifurcation | Tier | Pipeline Stages | Platform Deps | Consolidation Group | Agents | Wired To | Security | Description |
|------|--------|------------|--------|-------------|------|-----------------|---------------|---------------------|--------|----------|----------|-------------|
| chroma | canonical | ai-research | active | both | T1-operational | store, retrieve | python | ML-VECTOR | Psyche, Cartographer | slash-command | vetted | ChromaDB vector store |
| faiss | canonical | ai-research | active | both | T1-operational | store, retrieve | python | ML-VECTOR | Psyche, Cartographer | slash-command | vetted | FAISS similarity search library |
| pinecone | canonical | ai-research | active | both | T1-operational | store, retrieve | python | ML-VECTOR | Psyche, Cartographer | slash-command | vetted | Pinecone managed vector database |
| qdrant-vector-search | canonical | ai-research | active | both | T1-operational | store, retrieve | python | ML-VECTOR | Psyche, Cartographer | slash-command | vetted | Qdrant vector search engine |
| sentence-transformers | canonical | ai-research | active | both | T1-operational | embed | python | ML-EMBED | Psyche, Ajna | slash-command | vetted | Sentence-Transformers embedding models |
| sentencepiece | canonical | ai-research | active | both | T1-operational | tokenize | python | ML-TOKENIZE | Psyche | slash-command | vetted | SentencePiece tokenizer library |
| huggingface-tokenizers | canonical | ai-research | active | both | T1-operational | tokenize | python | ML-TOKENIZE | Psyche | slash-command | vetted | HuggingFace Tokenizers fast library |

## 3.7 Architecture (4)

| Name | Source | Provenance | Status | Bifurcation | Tier | Pipeline Stages | Platform Deps | Consolidation Group | Agents | Wired To | Security | Description |
|------|--------|------------|--------|-------------|------|-----------------|---------------|---------------------|--------|----------|----------|-------------|
| mamba-architecture | canonical | ai-research | dormant | both | T1-operational | research | GPU, python | ML-ARCH | Ajna | — | vetted | Mamba state space model architecture |
| rwkv-architecture | canonical | ai-research | dormant | both | T1-operational | research | GPU, python | ML-ARCH | Ajna | — | vetted | RWKV linear attention architecture |
| nanogpt | canonical | ai-research | dormant | both | T2-sprint | research, train | GPU, python | ML-ARCH | Ajna | — | vetted | NanoGPT minimal GPT implementation |
| implementing-llms-litgpt | canonical | ai-research | dormant | both | T1-operational | research, train | GPU, python | ML-ARCH | Ajna | — | vetted | LitGPT LLM implementation framework |

## 3.8 Observability (5)

| Name | Source | Provenance | Status | Bifurcation | Tier | Pipeline Stages | Platform Deps | Consolidation Group | Agents | Wired To | Security | Description |
|------|--------|------------|--------|-------------|------|-----------------|---------------|---------------------|--------|----------|----------|-------------|
| mlflow | canonical | ai-research | dormant | both | T2-sprint | observe, track | python | ML-OBSERVE | Psyche | — | vetted | MLflow experiment tracking and model registry |
| weights-and-biases | canonical | ai-research | dormant | both | T2-sprint | observe, track | python | ML-OBSERVE | Psyche | — | vetted | Weights & Biases experiment tracking |
| tensorboard | canonical | ai-research | dormant | both | T2-sprint | observe, visualize | python | ML-OBSERVE | Psyche | — | vetted | TensorBoard training visualization |
| phoenix-observability | canonical | ai-research | dormant | both | T2-sprint | observe, trace | python | ML-OBSERVE | Psyche | — | vetted | Phoenix LLM observability platform |
| langsmith-observability | canonical | ai-research | dormant | both | T2-sprint | observe, trace | python | ML-OBSERVE | Psyche | — | vetted | LangSmith LLM tracing and evaluation |

## 3.9 Cloud/Compute (9)

| Name | Source | Provenance | Status | Bifurcation | Tier | Pipeline Stages | Platform Deps | Consolidation Group | Agents | Wired To | Security | Description |
|------|--------|------------|--------|-------------|------|-----------------|---------------|---------------------|--------|----------|----------|-------------|
| lambda-labs-gpu-cloud | canonical | ai-research | active | both | T1-operational | provision | — | ML-CLOUD | Psyche | slash-command | vetted | Lambda Labs GPU cloud provisioning |
| modal-serverless-gpu | canonical | ai-research | active | both | T1-operational | provision, serve | python | ML-CLOUD | Psyche | slash-command | vetted | Modal serverless GPU compute |
| skypilot-multi-cloud-orchestration | canonical | ai-research | active | both | T1-operational | provision | python | ML-CLOUD | Psyche | slash-command | vetted | SkyPilot multi-cloud GPU orchestration |
| ray-data | canonical | ai-research | active | both | T1-operational | transform | python | ML-RAY | Psyche | slash-command | vetted | Ray Data distributed data processing |
| ray-train | canonical | ai-research | active | both | T1-operational | train | python | ML-RAY | Psyche | slash-command | vetted | Ray Train distributed training |
| pytorch-fsdp2 | canonical | ai-research | active | both | T1-operational | train | GPU, python | ML-DISTRIBUTED | Psyche | slash-command | vetted | PyTorch FSDP2 fully sharded data parallel |
| pytorch-lightning | canonical | ai-research | active | both | T1-operational | train | GPU, python | ML-DISTRIBUTED | Psyche | slash-command | vetted | PyTorch Lightning training framework |
| deepspeed | canonical | ai-research | active | both | T1-operational | train | GPU, python | ML-DISTRIBUTED | Psyche | slash-command | vetted | DeepSpeed distributed training optimization |
| huggingface-accelerate | canonical | ai-research | active | both | T1-operational | train | GPU, python | ML-DISTRIBUTED | Psyche | slash-command | vetted | HuggingFace Accelerate multi-GPU training |

## 3.10 Safety/Guardrails (5)

| Name | Source | Provenance | Status | Bifurcation | Tier | Pipeline Stages | Platform Deps | Consolidation Group | Agents | Wired To | Security | Description |
|------|--------|------------|--------|-------------|------|-----------------|---------------|---------------------|--------|----------|----------|-------------|
| llamaguard | canonical | ai-research | active | both | T1-operational | guard | GPU, python | ML-SAFETY | Adjudicator, Psyche | slash-command | vetted | LlamaGuard content safety classification |
| nemo-guardrails | canonical | ai-research | active | both | T1-operational | guard | python | ML-SAFETY | Adjudicator, Psyche | slash-command | vetted | NeMo Guardrails programmable safety rails |
| prompt-guard | canonical | ai-research | active | both | T1-operational | guard | python | ML-SAFETY | Adjudicator, Psyche | slash-command | vetted | Prompt injection and jailbreak detection |
| nemo-curator | canonical | ai-research | active | both | T1-operational | curate | GPU, python | ML-DATA-QUALITY | Psyche, Ajna | slash-command | vetted | NeMo Curator data quality pipeline |
| nemo-evaluator-sdk | canonical | ai-research | active | both | T1-operational | evaluate | python | ML-DATA-QUALITY | Psyche, Ajna | slash-command | vetted | NeMo Evaluator SDK model assessment |

## 3.11 Evaluation (2)

| Name | Source | Provenance | Status | Bifurcation | Tier | Pipeline Stages | Platform Deps | Consolidation Group | Agents | Wired To | Security | Description |
|------|--------|------------|--------|-------------|------|-----------------|---------------|---------------------|--------|----------|----------|-------------|
| evaluating-llms-harness | canonical | ai-research | active | both | T1-operational | evaluate | GPU, python | ML-EVAL | Adjudicator, Psyche | slash-command | vetted | lm-evaluation-harness benchmark suite |
| evaluating-code-models | canonical | ai-research | active | both | T1-operational | evaluate | GPU, python | ML-EVAL | Adjudicator, Psyche | slash-command | vetted | Code model evaluation (HumanEval, MBPP) |

## 3.12 Interpretability (3)

| Name | Source | Provenance | Status | Bifurcation | Tier | Pipeline Stages | Platform Deps | Consolidation Group | Agents | Wired To | Security | Description |
|------|--------|------------|--------|-------------|------|-----------------|---------------|---------------------|--------|----------|----------|-------------|
| transformer-lens-interpretability | canonical | ai-research | dormant | both | T2-sprint | research | GPU, python | ML-INTERP | Ajna | — | vetted | TransformerLens mechanistic interpretability |
| nnsight-remote-interpretability | canonical | ai-research | dormant | both | T2-sprint | research | GPU, python | ML-INTERP | Ajna | — | vetted | nnsight remote model interpretability |
| pyvene-interventions | canonical | ai-research | dormant | both | T2-sprint | research | GPU, python | ML-INTERP | Ajna | — | vetted | pyvene causal intervention framework |

## 3.13 ML Writing (1)

| Name | Source | Provenance | Status | Bifurcation | Tier | Pipeline Stages | Platform Deps | Consolidation Group | Agents | Wired To | Security | Description |
|------|--------|------------|--------|-------------|------|-----------------|---------------|---------------------|--------|----------|----------|-------------|
| ml-paper-writing | canonical | ai-research | dormant | both | T2-sprint | document | LaTeX | — | Ajna | — | vetted | ML research paper writing and formatting |

---

# 4. Trail of Bits Security Skills (32)

All skills in this section: `source=canonical`, `provenance=trail-of-bits`, `security=vetted`.

## 4.1 Security/Fuzzing (25)

| Name | Source | Provenance | Status | Bifurcation | Tier | Pipeline Stages | Platform Deps | Consolidation Group | Agents | Wired To | Security | Description |
|------|--------|------------|--------|-------------|------|-----------------|---------------|---------------------|--------|----------|----------|-------------|
| address-sanitizer | canonical | trail-of-bits | active | both | T1-operational | test, sanitize | C/C++ compiler | TOB-SANITIZE | Adjudicator | slash-command | vetted | AddressSanitizer memory error detection |
| aflpp | canonical | trail-of-bits | active | both | T1-operational | fuzz | C/C++ compiler | TOB-FUZZ | Adjudicator | slash-command | vetted | AFL++ coverage-guided fuzzer |
| atheris | canonical | trail-of-bits | active | both | T1-operational | fuzz | python | TOB-FUZZ | Adjudicator | slash-command | vetted | Atheris Python fuzzing engine |
| cargo-fuzz | canonical | trail-of-bits | active | both | T1-operational | fuzz | rust, cargo | TOB-FUZZ | Adjudicator | slash-command | vetted | cargo-fuzz Rust fuzzing framework |
| codeql | canonical | trail-of-bits | active | both | T1-operational | analyse, scan | codeql-cli | TOB-SAST | Adjudicator | slash-command | vetted | CodeQL semantic code analysis |
| coverage-analysis | canonical | trail-of-bits | active | both | T1-operational | analyse | — | TOB-COVERAGE | Adjudicator | slash-command | vetted | Code coverage analysis and gap detection |
| constant-time-analysis | canonical | trail-of-bits | active | both | T1-operational | analyse | — | TOB-CRYPTO | Adjudicator | slash-command | vetted | Constant-time cryptographic code analysis |
| constant-time-testing | canonical | trail-of-bits | active | both | T1-operational | test | — | TOB-CRYPTO | Adjudicator | slash-command | vetted | Constant-time implementation testing |
| fuzzing-dictionary | canonical | trail-of-bits | active | both | T1-operational | fuzz | — | TOB-FUZZ | Adjudicator | slash-command | vetted | Fuzzing dictionary generation |
| fuzzing-obstacles | canonical | trail-of-bits | active | both | T1-operational | analyse | — | TOB-FUZZ | Adjudicator | slash-command | vetted | Identify and overcome fuzzing obstacles |
| harness-writing | canonical | trail-of-bits | active | both | T1-operational | fuzz | — | TOB-FUZZ | Adjudicator | slash-command | vetted | Fuzz harness authoring and design |
| insecure-defaults | canonical | trail-of-bits | active | both | T1-operational | audit | — | TOB-AUDIT | Adjudicator | slash-command | vetted | Insecure default configuration detection |
| libafl | canonical | trail-of-bits | active | both | T1-operational | fuzz | rust | TOB-FUZZ | Adjudicator | slash-command | vetted | LibAFL modular fuzzing framework |
| libfuzzer | canonical | trail-of-bits | active | both | T1-operational | fuzz | C/C++ compiler | TOB-FUZZ | Adjudicator | slash-command | vetted | libFuzzer in-process fuzzing engine |
| ossfuzz | canonical | trail-of-bits | active | both | T1-operational | fuzz | docker | TOB-FUZZ | Adjudicator | slash-command | vetted | OSS-Fuzz continuous fuzzing integration |
| ruzzy | canonical | trail-of-bits | active | both | T1-operational | fuzz | ruby | TOB-FUZZ | Adjudicator | slash-command | vetted | Ruzzy Ruby fuzzing engine |
| semgrep | canonical | trail-of-bits | active | both | T1-operational | scan | python | TOB-SAST | Adjudicator | slash-command | vetted | Semgrep static analysis rule engine |
| semgrep-rule-creator | canonical | trail-of-bits | active | both | T1-operational | create | python | TOB-SAST | Adjudicator | slash-command | vetted | Custom Semgrep rule authoring |
| semgrep-rule-variant-creator | canonical | trail-of-bits | active | both | T1-operational | create | python | TOB-SAST | Adjudicator | slash-command | vetted | Semgrep rule variant generation |
| property-based-testing | canonical | trail-of-bits | active | both | T1-operational | test | — | TOB-TEST | Adjudicator | slash-command | vetted | Property-based testing (Hypothesis, QuickCheck) |
| variant-analysis | canonical | trail-of-bits | active | both | T1-operational | analyse | — | TOB-SAST | Adjudicator | slash-command | vetted | Vulnerability variant analysis |
| wycheproof | canonical | trail-of-bits | active | both | T1-operational | test | — | TOB-CRYPTO | Adjudicator | slash-command | vetted | Wycheproof cryptographic test vectors |
| yara-rule-authoring | canonical | trail-of-bits | active | both | T1-operational | create | — | TOB-DETECT | Adjudicator | slash-command | vetted | YARA malware detection rule authoring |
| sarif-parsing | canonical | trail-of-bits | active | both | T1-operational | parse | — | TOB-REPORT | Adjudicator | slash-command | vetted | SARIF static analysis results parsing |
| dwarf-expert | canonical | trail-of-bits | active | both | T1-operational | analyse | — | TOB-BINARY | Adjudicator | slash-command | vetted | DWARF debug info analysis expert |

## 4.2 Security Audit (7)

| Name | Source | Provenance | Status | Bifurcation | Tier | Pipeline Stages | Platform Deps | Consolidation Group | Agents | Wired To | Security | Description |
|------|--------|------------|--------|-------------|------|-----------------|---------------|---------------------|--------|----------|----------|-------------|
| audit-context-building | canonical | trail-of-bits | active | both | T1-operational | audit, prepare | — | TOB-AUDIT | Adjudicator | slash-command | vetted | Build audit context from codebase |
| audit-prep-assistant | canonical | trail-of-bits | active | both | T1-operational | audit, prepare | — | TOB-AUDIT | Adjudicator | slash-command | vetted | Audit preparation and scoping assistant |
| threat-modeling | canonical | trail-of-bits | active | both | T1-operational | analyse, design | — | TOB-AUDIT | Adjudicator | slash-command | vetted | STRIDE/PASTA threat modeling |
| secure-workflow-guide | canonical | trail-of-bits | active | both | T1-operational | guide | — | TOB-AUDIT | Adjudicator | slash-command | vetted | Secure development workflow guidance |
| entry-point-analyzer | canonical | trail-of-bits | active | both | T1-operational | analyse | — | TOB-AUDIT | Adjudicator | slash-command | vetted | Application entry point security analysis |
| token-integration-analyzer | canonical | trail-of-bits | active | both | T1-operational | analyse | — | TOB-AUDIT | Adjudicator | slash-command | vetted | Token integration security analysis |
| firebase-apk-scanner | canonical | trail-of-bits | active | both | T1-operational | scan | — | TOB-MOBILE | Adjudicator | slash-command | vetted | Firebase APK security scanning |

---

# 5. Trail of Bits Blockchain Scanners — QUARANTINED (6)

> **QUARANTINE REASON**: Blockchain-specific dependencies. These skills target smart contract
> platforms not currently in the Syncrescendence stack. Retained for reference; activation
> requires explicit Sovereign approval and dependency installation.

| Name | Source | Provenance | Status | Bifurcation | Tier | Pipeline Stages | Platform Deps | Consolidation Group | Agents | Wired To | Security | Description |
|------|--------|------------|--------|-------------|------|-----------------|---------------|---------------------|--------|----------|----------|-------------|
| algorand-vulnerability-scanner | canonical | trail-of-bits | quarantined | both | T2-sprint | scan | algorand-sdk | TOB-BLOCKCHAIN | Adjudicator | — | vetted | Algorand smart contract vulnerability scanner |
| cairo-vulnerability-scanner | canonical | trail-of-bits | quarantined | both | T2-sprint | scan | cairo-lang | TOB-BLOCKCHAIN | Adjudicator | — | vetted | Cairo/StarkNet contract vulnerability scanner |
| cosmos-vulnerability-scanner | canonical | trail-of-bits | quarantined | both | T2-sprint | scan | cosmos-sdk | TOB-BLOCKCHAIN | Adjudicator | — | vetted | Cosmos SDK vulnerability scanner |
| solana-vulnerability-scanner | canonical | trail-of-bits | quarantined | both | T2-sprint | scan | solana-cli | TOB-BLOCKCHAIN | Adjudicator | — | vetted | Solana program vulnerability scanner |
| substrate-vulnerability-scanner | canonical | trail-of-bits | quarantined | both | T2-sprint | scan | substrate | TOB-BLOCKCHAIN | Adjudicator | — | vetted | Substrate/Polkadot vulnerability scanner |
| ton-vulnerability-scanner | canonical | trail-of-bits | quarantined | both | T2-sprint | scan | ton-cli | TOB-BLOCKCHAIN | Adjudicator | — | vetted | TON smart contract vulnerability scanner |

---

# 6. Vibeship/Community Utility Skills (63)

All skills in this section: `source=canonical`, `provenance=vibeship` (unless noted), `security=unvetted` (unless noted).

| Name | Source | Provenance | Status | Bifurcation | Tier | Pipeline Stages | Platform Deps | Consolidation Group | Agents | Wired To | Security | Description |
|------|--------|------------|--------|-------------|------|-----------------|---------------|---------------------|--------|----------|----------|-------------|
| ask-questions-if-underspecified | canonical | vibeship | active | both | T1-operational | clarify | — | — | all | slash-command | unvetted | Prompt for clarification when input is ambiguous |
| brainstorming | canonical | vibeship | active | both | T1-operational | ideate | — | CEK-BRAINSTORM | all | slash-command | unvetted | General brainstorming facilitation |
| claude-in-chrome-troubleshooting | canonical | vibeship | dormant | sovereign | T3-session | debug | Chrome | — | — | — | unvetted | Claude Chrome extension troubleshooting |
| claudeception | canonical | vibeship | dormant | agent | T2-sprint | execute | — | — | — | — | unvetted | Recursive Claude self-invocation patterns |
| code-maturity-assessor | canonical | vibeship | dormant | both | T2-sprint | evaluate | — | — | Adjudicator | — | unvetted | Codebase maturity level assessment |
| commit-work | canonical | vibeship | active | both | T2-sprint | commit | git | CEK-GIT-OPS | Commander, Psyche | slash-command | unvetted | Simplified git commit workflow |
| conversation-memory | canonical | vibeship | dormant | both | T1-operational | memory | — | MEMORY | all | — | unvetted | Conversation memory persistence |
| cron | canonical | community | dormant | sovereign | T3-session | schedule | crontab | — | — | — | unvetted | Cron job scheduling and management |
| debug-buttercup | canonical | vibeship | dormant | both | T2-sprint | debug | — | — | Psyche | — | unvetted | Buttercup test framework debugging |
| defuddle | canonical | vibeship | dormant | both | T2-sprint | transform | — | — | — | — | unvetted | Content defuddling and clarity transformation |
| devcontainer-setup | canonical | vibeship | dormant | sovereign | T3-session | configure | docker | — | Psyche | — | unvetted | VS Code devcontainer configuration |
| differential-review | canonical | vibeship | dormant | both | T1-operational | review | git | REVIEW | Adjudicator | — | unvetted | Differential code review (changed lines only) |
| dispatching-parallel-agents | canonical | vibeship | active | agent | T1-operational | dispatch | — | CEK-MULTI-AGENT | Commander | agent-loop | unvetted | Fan-out parallel agent dispatch patterns |
| ensue-memory | canonical | vibeship | dormant | both | T1-operational | memory | — | MEMORY | all | — | unvetted | Ensue memory persistence framework |
| evaluating-code-models | canonical | community | dormant | both | T1-operational | evaluate | GPU, python | ML-EVAL | Adjudicator | — | unvetted | Code model evaluation (community variant) |
| executing-plans | canonical | vibeship | active | agent | T0-strategic | execute | — | EXEC | Commander | agent-loop | unvetted | Plan execution orchestration |
| find-skills | canonical | vibeship | active | both | T1-operational | lookup | — | SKILL-LOOKUP | all | slash-command | unvetted | Canonical skill discovery and search |
| finishing-a-development-branch | canonical | vibeship | active | both | T2-sprint | integrate | git, gh | CEK-GIT-OPS | Commander, Psyche | slash-command | unvetted | Branch completion and merge workflow |
| fix-review | canonical | vibeship | dormant | both | T1-operational | fix, review | git | REVIEW | Psyche | — | unvetted | Apply fixes from code review feedback |
| git-cleanup | canonical | vibeship | dormant | sovereign | T3-session | maintain | git | CEK-GIT-OPS | — | — | unvetted | Git repository cleanup (prune, gc) |
| google-ai-mode-skill | canonical | vibeship | dormant | sovereign | T3-session | search | — | — | — | — | unvetted | Google AI mode integration |
| interpreting-culture-index | canonical | vibeship | dormant | both | T2-sprint | analyse | — | — | Ajna | — | unvetted | Culture Index personality assessment interpretation |
| json-canvas | canonical | vibeship | dormant | both | T2-sprint | visualize | obsidian | OBSIDIAN | Cartographer | — | unvetted | JSON Canvas (Obsidian) rendering |
| last30days | canonical | vibeship | dormant | both | T2-sprint | report | git | VB-REPORT | Commander | — | unvetted | Git activity report — last 30 days |
| lastweek | canonical | vibeship | dormant | both | T2-sprint | report | git | VB-REPORT | Commander | — | unvetted | Git activity report — last week |
| lastday | canonical | vibeship | dormant | both | T2-sprint | report | git | VB-REPORT | Commander | — | unvetted | Git activity report — last day |
| long-context | canonical | community | dormant | both | T1-operational | serve | — | ML-ATTENTION | Psyche | — | unvetted | Long context handling patterns (community) |
| memory-systems | canonical | community | dormant | both | T1-operational | memory | — | MEMORY | all | — | unvetted | Memory system architecture patterns |
| mermaid-diagrams | canonical | vibeship | dormant | both | T2-sprint | visualize | — | — | Cartographer | — | unvetted | Mermaid diagram generation |
| obsidian-bases | canonical | vibeship | dormant | sovereign | T3-session | configure | obsidian | OBSIDIAN | Cartographer | — | unvetted | Obsidian Bases plugin configuration |
| obsidian-cli | canonical | vibeship | dormant | sovereign | T3-session | integrate | obsidian | OBSIDIAN | Cartographer | — | unvetted | Obsidian CLI integration |
| obsidian-markdown | canonical | vibeship | dormant | both | T2-sprint | transform | obsidian | OBSIDIAN | Cartographer | — | unvetted | Obsidian-flavored markdown handling |
| pi-planning-with-files | canonical | vibeship | dormant | both | T1-operational | plan | — | PLAN | Commander | — | unvetted | PI planning via file-based coordination |
| planning-with-files | canonical | vibeship | dormant | both | T1-operational | plan | — | PLAN | Commander | — | unvetted | File-based planning methodology |
| prompt-guard | canonical | community | dormant | both | T1-operational | guard | python | ML-SAFETY | Adjudicator | — | unvetted | Prompt guard (community variant) |
| receiving-code-review | canonical | vibeship | active | both | T1-operational | review | — | REVIEW | Psyche, Commander | slash-command | unvetted | Process and act on received code reviews |
| requesting-code-review | canonical | vibeship | active | both | T1-operational | review | gh | REVIEW | Commander, Psyche | slash-command | unvetted | Request code review from agents or Sovereign |
| second-opinion | canonical | vibeship | dormant | both | T1-operational | review | — | CEK-REVIEW | all | — | unvetted | Seek second opinion on a decision |
| session-handoff | canonical | vibeship | active | both | T1-operational | handoff | — | — | all | slash-command | unvetted | Session state handoff between agents |
| skill-judge | canonical | vibeship | dormant | agent | T1-operational | evaluate | — | CEK-META | Adjudicator | — | unvetted | Evaluate skill quality and completeness |
| skillforge | canonical | vibeship | dormant | both | T1-operational | create | — | CEK-META | Commander | — | unvetted | Skill forging and templating toolkit |
| subagent-driven-development | canonical | vibeship | active | agent | T1-operational | execute | — | CEK-MULTI-AGENT | Commander | agent-loop | unvetted | Sub-agent driven development (vibeship variant) |
| systematic-debugging | canonical | vibeship | active | both | T1-operational | debug | — | — | Psyche, Commander | slash-command | unvetted | Systematic debugging methodology |
| test-driven-development | canonical | vibeship | active | both | T1-operational | test, execute | — | CEK-TDD | Psyche, Commander | slash-command | unvetted | TDD workflow (vibeship variant) |
| tmux | canonical | vibeship | active | both | T2-sprint | manage | tmux | — | Commander, Psyche | slash-command | unvetted | Tmux session management |
| threat-modeling | canonical | community | dormant | both | T1-operational | analyse | — | TOB-AUDIT | Adjudicator | — | unvetted | Threat modeling (community variant) |
| using-gh-cli | canonical | vibeship | active | both | T1-operational | integrate | gh | — | all | slash-command | unvetted | GitHub CLI usage patterns and recipes |
| using-git-worktrees | canonical | vibeship | active | both | T2-sprint | manage | git | CEK-WORKTREE | Psyche, Commander | slash-command | unvetted | Git worktree usage patterns |
| using-superpowers | canonical | vibeship | active | both | T1-operational | execute | — | — | all | slash-command | unvetted | Agent superpower invocation patterns |
| verification-before-completion | canonical | vibeship | active | both | T1-operational | verify | — | — | all | slash-command, agent-loop | unvetted | Pre-completion verification checklist |
| web-to-markdown | canonical | vibeship | dormant | both | T2-sprint | transform | — | — | Ajna | — | unvetted | Web page to markdown conversion |
| writing-plans | canonical | vibeship | active | both | T1-operational | plan | — | PLAN | Commander | slash-command | unvetted | Plan document authoring methodology |
| writing-skills | canonical | vibeship | dormant | both | T1-operational | create | — | CEK-META | Commander | — | unvetted | Skill definition authoring guide |
| crewai-multi-agent | canonical | community | dormant | both | T1-operational | orchestrate | python | ML-MULTI-AGENT | Commander | — | unvetted | CrewAI multi-agent (community variant) |
| autogpt-agents | canonical | community | dormant | both | T1-operational | orchestrate | python | ML-MULTI-AGENT | Commander | — | unvetted | AutoGPT agents (community variant) |
| burpsuite-project-parser | canonical | vibeship | dormant | both | T2-sprint | parse | — | TOB-AUDIT | Adjudicator | — | unvetted | BurpSuite project file parser |
| secure-workflow-guide | canonical | vibeship | dormant | both | T1-operational | guide | — | TOB-AUDIT | Adjudicator | — | unvetted | Secure workflow guide (vibeship variant) |
| testing-handbook-generator | canonical | vibeship | dormant | both | T2-sprint | document | — | — | Adjudicator | — | unvetted | Testing handbook generation |
| spec-to-code-compliance | canonical | vibeship | dormant | both | T1-operational | verify | — | — | Adjudicator | — | unvetted | Spec-to-code compliance checking |
| entry-point-analyzer | canonical | vibeship | dormant | both | T1-operational | analyse | — | TOB-AUDIT | Adjudicator | — | unvetted | Entry point analysis (vibeship variant) |
| guidelines-advisor | canonical | vibeship | dormant | both | T1-operational | guide | — | — | Adjudicator | — | unvetted | Coding guidelines advisory |
| audit-context-building | canonical | vibeship | dormant | both | T1-operational | audit | — | TOB-AUDIT | Adjudicator | — | unvetted | Audit context builder (vibeship variant) |
| audit-prep-assistant | canonical | vibeship | dormant | both | T1-operational | audit | — | TOB-AUDIT | Adjudicator | — | unvetted | Audit prep assistant (vibeship variant) |

---

# Appendix A: Consolidation Groups

Consolidation groups identify skills with overlapping functionality that can be merged into
mode-parameterized wrappers, reducing cognitive load and maintenance burden.

| Group ID | Skills | Merge Strategy | Target Wrapper |
|----------|--------|----------------|----------------|
| **CEK-ANALYSIS** | cek-analyse, cek-analyse-problem, cek-analyze-issue, cek-cause-and-effect, cek-why, cek-root-cause-tracing, cek-plan-do-check-act | Mode parameter: `--mode={general,problem,issue,causal,5why,trace,pdca}` | `cek-analyse --mode` |
| **CEK-REVIEW** | cek-agent-evaluation, cek-attach-review-to-pr, cek-critique, cek-judge, cek-judge-with-debate, cek-reflect, cek-review-local-changes, cek-review-pr, second-opinion | Mode parameter: `--mode={eval,pr-attach,critique,judge,debate,reflect,local,pr,second}` | `cek-review --mode` |
| **CEK-EXEC** | cek-do-and-judge, cek-do-competitively, cek-do-in-parallel, cek-do-in-steps | Mode parameter: `--mode={judge,compete,parallel,steps}` | `cek-do --mode` |
| **CEK-MULTI-AGENT** | cek-launch-sub-agent, cek-subagent-driven-development, cek-multi-agent-patterns, dispatching-parallel-agents, subagent-driven-development | Merge into single orchestrator with dispatch modes | `agent-orchestrate --mode` |
| **CEK-TDD** | cek-fix-tests, cek-test-driven-development, cek-write-tests, test-driven-development | Mode parameter: `--mode={fix,tdd,generate}` | `cek-test --mode` |
| **CEK-GIT-OPS** | cek-commit, cek-create-pr, commit-work, finishing-a-development-branch, git-cleanup | Mode parameter: `--mode={commit,pr,finish,cleanup}` | `git-ops --mode` |
| **CEK-WORKTREE** | cek-compare-worktrees, cek-create-worktree, cek-merge-worktree, cek-worktrees, cek-notes, using-git-worktrees | Already well-separated; retain individual skills | — |
| **CEK-REASONING** | cek-context-engineering, cek-thought-based-reasoning, cek-tree-of-thoughts, cek-prompt-engineering | Mode parameter: `--mode={context,chain,tree,prompt}` | `cek-reason --mode` |
| **CEK-BRAINSTORM** | cek-brainstorm, cek-create-ideas, brainstorming | Merge ideation skills | `ideate --mode` |
| **CEK-META** | cek-create-agent, cek-create-command, cek-create-skill, cek-create-workflow-command, cek-test-prompt, cek-test-skill, skill-judge, skillforge, writing-skills | Retain; too diverse for single wrapper | — |
| **CEK-SETUP** | cek-setup-arxiv-mcp, cek-setup-code-formating, cek-setup-codemap-cli, cek-setup-context7-mcp, cek-setup-serena-mcp | Mode parameter: `--target={arxiv,format,codemap,context7,serena}` | `cek-setup --target` |
| **KAIZEN** | cek-kaizen, method_kaizen | Merge: project wrapper calls CEK kaizen | `kaizen` |
| **PLAN** | cek-plan, plan, executing-plans, writing-plans, pi-planning-with-files, planning-with-files | Retain cek-plan + project plan; deprecate overlapping vibeship skills | `plan --mode` |
| **EXEC** | cek-implement, execute, executing-plans | Retain cek-implement + project execute | — |
| **REVIEW** | reviewtrospective, differential-review, fix-review, receiving-code-review, requesting-code-review | Retain; different review lifecycle phases | — |
| **MEMORY** | cek-memorize, update_agent_memory, conversation-memory, ensue-memory, memory-systems | Merge into unified memory interface | `memory --mode` |
| **SKILL-LOOKUP** | find-skills (project), find-skills (canonical) | Project overrides canonical | `find-skills` |
| **MEDIA-INGEST** | audize, listenize, readize, transcribe_interview, transcribe_youtube | Retain; distinct media types | — |
| **OBSIDIAN** | json-canvas, obsidian-bases, obsidian-cli, obsidian-markdown | Mode parameter: `--mode={canvas,bases,cli,markdown}` | `obsidian --mode` |
| **VB-REPORT** | last30days, lastweek, lastday | Mode parameter: `--range={30d,7d,1d}` | `git-report --range` |
| **ML-FINETUNE** | fine-tuning-llms, llama-factory, lora-fine-tuning, peft, qlora-fine-tuning, trl-fine-tuning, unsloth, axolotl | Retain; each targets different framework | — |
| **ML-RLHF** | reward-modeling, rlhf-training, dpo-training, verl, open-rlhf | Retain; distinct training paradigms | — |
| **ML-QUANT** | awq-quantization, gguf, gptq-quantization, hqq-quantization, quantizing-models-bitsandbytes | Mode parameter: `--method={awq,gguf,gptq,hqq,bnb}` | `quantize --method` |
| **ML-SERVE** | serving-llms-vllm, sglang, llama-cpp, tensorrt-llm, speculative-decoding | Retain; different serving backends | — |
| **ML-VECTOR** | chroma, faiss, pinecone, qdrant-vector-search | Mode parameter: `--backend={chroma,faiss,pinecone,qdrant}` | `vector-store --backend` |
| **ML-TOKENIZE** | sentencepiece, huggingface-tokenizers | Merge | `tokenize --backend` |
| **ML-FRAMEWORK** | langchain, llamaindex, dspy, instructor, guidance | Retain; different paradigms | — |
| **ML-MULTI-AGENT** | crewai-multi-agent (ai-research), autogpt-agents (ai-research), crewai-multi-agent (community), autogpt-agents (community) | Deduplicate: ai-research canonical, community deprecated | — |
| **ML-VISION** | clip, llava, blip-2-vision-language, segment-anything-model, stable-diffusion-image-generation | Retain; different modalities | — |
| **ML-AUDIO** | whisper, audiocraft-audio-generation | Retain; speech vs generation | — |
| **ML-ARCH** | mamba-architecture, rwkv-architecture, nanogpt, implementing-llms-litgpt | Retain; research reference skills | — |
| **ML-OBSERVE** | mlflow, weights-and-biases, tensorboard, phoenix-observability, langsmith-observability | Mode parameter: `--backend={mlflow,wandb,tb,phoenix,langsmith}` | `observe --backend` |
| **ML-DISTRIBUTED** | pytorch-fsdp2, pytorch-lightning, deepspeed, huggingface-accelerate | Retain; different distributed strategies | — |
| **ML-CLOUD** | lambda-labs-gpu-cloud, modal-serverless-gpu, skypilot-multi-cloud-orchestration | Retain; different providers | — |
| **ML-RAY** | ray-data, ray-train | Merge | `ray --mode={data,train}` |
| **ML-SAFETY** | llamaguard, nemo-guardrails, prompt-guard (ai-research), prompt-guard (community) | Deduplicate prompt-guard; retain distinct tools | — |
| **ML-EVAL** | evaluating-llms-harness, evaluating-code-models, evaluating-code-models (community) | Deduplicate community variant | — |
| **ML-INTERP** | transformer-lens-interpretability, nnsight-remote-interpretability, pyvene-interventions | Retain; different interpretability approaches | — |
| **ML-EMBED** | sentence-transformers | Standalone | — |
| **ML-DATA-QUALITY** | nemo-curator, nemo-evaluator-sdk | Retain | — |
| **ML-MODEL-OPS** | model-merging, model-pruning | Retain; distinct operations | — |
| **ML-ATTENTION** | optimizing-attention-flash, long-context (ai-research), long-context (community) | Deduplicate long-context | — |
| **ML-RL** | slime, miles-rl | Retain | — |
| **TOB-FUZZ** | aflpp, atheris, cargo-fuzz, fuzzing-dictionary, fuzzing-obstacles, harness-writing, libafl, libfuzzer, ossfuzz, ruzzy | Retain; different fuzzers and aspects | — |
| **TOB-SAST** | codeql, semgrep, semgrep-rule-creator, semgrep-rule-variant-creator, variant-analysis | Retain; different SAST engines | — |
| **TOB-CRYPTO** | constant-time-analysis, constant-time-testing, wycheproof | Retain | — |
| **TOB-AUDIT** | audit-context-building (ToB), audit-prep-assistant (ToB), threat-modeling (ToB), secure-workflow-guide (ToB), insecure-defaults, audit-context-building (VB), audit-prep-assistant (VB), threat-modeling (community), secure-workflow-guide (VB), burpsuite-project-parser | Deduplicate: ToB canonical, VB/community deprecated | — |
| **TOB-BLOCKCHAIN** | algorand-, cairo-, cosmos-, solana-, substrate-, ton-vulnerability-scanner | All quarantined; no merge needed | — |
| **TOB-SANITIZE** | address-sanitizer | Standalone | — |
| **TOB-COVERAGE** | coverage-analysis | Standalone | — |
| **TOB-DETECT** | yara-rule-authoring | Standalone | — |
| **TOB-REPORT** | sarif-parsing | Standalone | — |
| **TOB-BINARY** | dwarf-expert | Standalone | — |
| **TOB-MOBILE** | firebase-apk-scanner | Standalone | — |
| **TOB-TEST** | property-based-testing | Standalone | — |

---

# Appendix B: Pre-Identified Merges (Phase 1 Consolidation)

These merges are prioritized for immediate implementation based on highest overlap and
lowest risk.

| Priority | Merge | From | Into | Savings | Risk |
|----------|-------|------|------|---------|------|
| P0 | Analysis consolidation | 7 cek-analyse-* skills | `cek-analyse --mode` | 6 skill files | Low |
| P0 | Execution consolidation | 4 cek-do-* skills | `cek-do --mode` | 3 skill files | Low |
| P1 | Git ops consolidation | cek-commit, cek-create-pr, commit-work, finishing-a-dev-branch | `git-ops --mode` | 3 skill files | Medium |
| P1 | Report consolidation | last30days, lastweek, lastday | `git-report --range` | 2 skill files | Low |
| P1 | Tokenizer merge | sentencepiece, huggingface-tokenizers | `tokenize --backend` | 1 skill file | Low |
| P2 | Memory consolidation | 5 memory-related skills | `memory --mode` | 4 skill files | Medium |
| P2 | Multi-agent consolidation | 5 multi-agent skills | `agent-orchestrate --mode` | 4 skill files | Medium |
| P2 | Quantization wrapper | 5 quant skills | `quantize --method` | 4 skill files | Low |
| P2 | Vector store wrapper | 4 vector store skills | `vector-store --backend` | 3 skill files | Low |
| P3 | Deduplicate community variants | 8 community/vibeship dupes of canonical | Deprecate community copies | 8 skill files | Low |
| P3 | Deduplicate VB audit skills | 5 vibeship audit skill dupes | Deprecate vibeship copies | 5 skill files | Low |
| P3 | Observability wrapper | 5 ML observe skills | `observe --backend` | 4 skill files | Low |
| P3 | Obsidian wrapper | 4 obsidian skills | `obsidian --mode` | 3 skill files | Low |

**Estimated total consolidation**: 246 skills → ~196 effective skills (Phase 1), → ~180 effective skills (Phase 2 with wrappers fully deployed).

---

# Appendix C: Security Posture Summary

| Security Status | Count | Action Required |
|-----------------|-------|-----------------|
| vetted | 197 | None — cleared for production use |
| unvetted | 67 | Require security review before T0/T1 promotion |
| flagged | 0 | — |

**Unvetted skills** are primarily vibeship/community canonical skills. These are safe for
sovereign-invoked slash-command use but MUST NOT be wired into unsupervised agent loops
until vetted. Vetting involves: (1) source code audit, (2) dependency review, (3)
Adjudicator sign-off.

**Quarantined skills** (6 blockchain scanners) require explicit Sovereign approval and
platform-specific dependency installation before reactivation.

---

*End of ARCH-SKILL_REGISTRY.md*
