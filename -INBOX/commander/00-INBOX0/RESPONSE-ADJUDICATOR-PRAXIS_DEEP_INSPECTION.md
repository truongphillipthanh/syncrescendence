---
agent: adjudicator
council: DC-203
topic: DC-203 Praxis Deep Inspection — final RESULT (36-file praxis/05-SIGMA audit, per-file verdicts + recommendations)
status: unprocessed
collected: 2026-02-23
---

# RESULT — Adjudicator Deep Inspection (DC-203)

Inspection scope: `praxis/05-SIGMA/` (36 entries including `.DS_Store`).
Baseline verification: target safe-point commit `65dc5e6d` exists, and `git diff 65dc5e6d..HEAD -- AGENTS.md CLAUDE.md praxis/05-SIGMA` returned no differences.

## Section 1: Per-File Verdict Table

| # | File | Verdict | Confidence | Evidence |
|---|------|---------|------------|----------|
| 1 | `mechanics/MECH-context_compaction_strategies.md` | HIGH-SIGNAL | MEDIUM | `rg` shows broken cross-ref `[[SYNTHESIS-claude_code_architecture]]`; core guidance still operationally useful. |
| 2 | `mechanics/MECH-git_worktree_coordination.md` | STALE | HIGH | References `verify-zone.sh`, `consolidate-ledgers.sh`, `ledgers/tasks-*.csv`, `coordination.yaml`; these are absent via `find/ls`. |
| 3 | `mechanics/MECH-headless_mode_automation.md` | HIGH-SIGNAL | MEDIUM | Headless pattern remains valid; cross-ref to missing `SYNTHESIS-claude_code_architecture`. |
| 4 | `mechanics/MECH-hooks_lifecycle_automation.md` | HIGH-SIGNAL | MEDIUM | Hook lifecycle concepts valid, but local path reality differs (`orchestration/scripts/*` missing; `orchestration/00-ORCHESTRATION/scripts/*` exists). |
| 5 | `mechanics/MECH-mcp_server_patterns.md` | HIGH-SIGNAL | MEDIUM | Valuable architecture, but both synthesis links (`SYNTHESIS-agents_mcp_foundations`, `SYNTHESIS-cross_platform_patterns`) are missing. |
| 6 | `mechanics/MECH-prompt_engineering_patterns.md` | HIGH-SIGNAL | MEDIUM | Practical pattern doc, but references missing `MECH-extended_thinking_triggers` and missing synthesis doc. |
| 7 | `mechanics/MECH-skill_system_architecture.md` | HIGH-SIGNAL | MEDIUM | Skill pattern matches current `.claude/skills/` usage; synthesis cross-ref target missing. |
| 8 | `mechanics/MECH-source_anneal_pipeline.md` | STALE | HIGH | File self-labels as blueprint; many referenced scripts/paths missing (`sources/_scripts/ingest.py`, `anneal.py`, token files). |
| 9 | `mechanics/MECH-subagent_delegation.md` | HIGH-SIGNAL | MEDIUM | Core mechanism still useful; links to missing `SYNTHESIS-agents_mcp_foundations`. |
| 10 | `mechanics/MECH-task_orchestration.md` | HIGH-SIGNAL | MEDIUM | Task decomposition remains relevant; dependent synthesis link missing. |
| 11 | `mechanics/MECH-youtube_ingestion_pipeline.md` | SUPERSEDED-BY:`mechanics/MECH-source_anneal_pipeline.md` | HIGH | File header explicitly states “STATUS: SUPERSEDED” and names successor document. |
| 12 | `practice/PRAC-auteur_content_strategy.md` | HIGH-SIGNAL | LOW | High-value content strategy, but largely external/theoretical and weakly coupled to current repo operations. |
| 13 | `practice/PRAC-blitzkrieg_worktree_isolation.md` | STALE | HIGH | Uses legacy `orchestration/scripts/setup-worktrees.sh` path and dead `sources/research/*` references. |
| 14 | `practice/PRAC-cowork_desktop_integration.md` | HIGH-SIGNAL | MEDIUM | Useful practice doc; one core cross-ref target (`SYNTHESIS-agents_mcp_foundations`) is missing. |
| 15 | `practice/PRAC-ledger_management_patterns.md` | ORPHANED | HIGH | Core entities (`ledgers/tasks-*.csv`, `validate-ledger.sh`, `consolidate-ledgers.sh`) do not exist in current repo. |
| 16 | `practice/PRAC-multi_account_coordination.md` | STALE | HIGH | Workflow depends on missing `orchestration/oracle_contexts/handoffs/`; synthesis cross-ref missing. |
| 17 | `practice/PRAC-multi_methodology_framework.md` | STALE | MEDIUM | External tool stack mappings are not verifiable in-repo; canon mappings are partial and mixed. |
| 18 | `practice/PRAC-ontology_queries.md` | STALE | HIGH | Claims “10/79” extended-frontmatter coverage; current check shows `78/162` CANON files with `operational_status`. |
| 19 | `practice/PRAC-operational_wisdom_compendium.md` | CANONICAL | HIGH | Matches AGENTS: `watch_dispatch.sh` deprecated; `auto_ingest_loop.sh` sole dispatch system. |
| 20 | `practice/PRAC-oracle_to_executor_handoff.md` | ORPHANED | HIGH | Handoff target path `orchestration/oracle_contexts/handoffs/` is absent. |
| 21 | `practice/PRAC-parallel_claude_orchestration.md` | HIGH-SIGNAL | MEDIUM | Parallelism guidance still useful; synthesis cross-ref target missing. |
| 22 | `practice/PRAC-ralph_pattern_execution.md` | HIGH-SIGNAL | MEDIUM | Core “fresh context loop” pattern still useful; referenced synthesis target missing. |
| 23 | `practice/PRAC-semantic_compression_workflow.md` | HIGH-SIGNAL | HIGH | SN workflow remains actionable; path drift on `orchestration/scripts/*` (actual under `00-ORCHESTRATION`). |
| 24 | `practice/PRAC-subagent_delegation_guide.md` | ORPHANED | HIGH | Points to missing `sources/research/MECH-subagent_delegation.md`; model row for Adjudicator (Sonnet) diverges from AGENTS registry. |
| 25 | `syntheses/SYNTHESIS-codex-cli.md` | STALE | MEDIUM | Useful synthesis but source citations like `claude-openai.md`, `chatgpt-openai.md` are missing from repo. |
| 26 | `syntheses/SYNTHESIS-gemini-cli.md` | STALE | HIGH | Dated `2025-07-15` with explicit unresolved CLI gaps; major currency delta vs Feb 2026 operations. |
| 27 | `syntheses/SYNTHESIS-openclaw-v2.md` | HIGH-SIGNAL | MEDIUM | Retains strong strategic/security signal; includes time-bound action items and version-specific claims. |
| 28 | `syntheses/SYNTHESIS-openclaw.md` | SUPERSEDED-BY:`syntheses/SYNTHESIS-openclaw-v2.md` | HIGH | v2 header explicitly declares this file as prior version. |
| 29 | `syntheses/SYNTHESIS-platform_topology_jan2026.md` | STALE | HIGH | Snapshot is Jan 2026; AGENTS operational registry is Feb 2026 and fleet/platform state has shifted. |
| 30 | `EXEMPLA-APHORISMS.md` | CANONICAL | HIGH | Aphorisms align with AGENTS constitutional semantics (`distill content`, `protect orchestration infra`). |
| 31 | `EXEMPLA-PROVERBS.md` | HIGH-SIGNAL | MEDIUM | Wisdom content valuable, but cited source `claudes-proposal.md` is missing. |
| 32 | `EXEMPLA-README.md` | STALE | HIGH | Describes `06-EXEMPLA/` subtree and templates not present in current `praxis/05-SIGMA` layout. |
| 33 | `EXEMPLA-TALE-ajna2-lobotomy.md` | CANONICAL | MEDIUM | Historical cautionary tale remains coherent with current platform-role doctrine. |
| 34 | `README.md` | STALE | HIGH | Claims 5 mechanics/6 practice + removed syntheses; actual tree has 11 mechanics, 13 practice, 5 syntheses. |
| 35 | `REF-CLAUDE_CODE_OPERATIONS_MANUAL.md` | HIGH-SIGNAL | MEDIUM | Strong operations manual, but Claude-centric assumptions are broader than current multi-agent/multi-platform reality. |
| 36 | `.DS_Store` | ORPHANED | HIGH | Binary macOS artifact; non-knowledge file in operational corpus. |

## Section 2: Reality Check (MECH-* and PRAC-* files only)

### mechanics/MECH-context_compaction_strategies.md
- **Claims verified**: `.claude/settings.json` exists.
- **Claims falsified**: Cross-reference `[[SYNTHESIS-claude_code_architecture]]` has no target.
- **Scripts referenced**: `settings.json` -> exists as `.claude/settings.json`.
- **Agents referenced**: None explicit -> N/A.
- **Hooks referenced**: None explicit -> N/A.

### mechanics/MECH-git_worktree_coordination.md
- **Claims verified**: Git worktree mechanism itself is available (`git worktree`).
- **Claims falsified**: `verify-zone.sh`, `consolidate-ledgers.sh`, `coordination.yaml`, `ledgers/tasks-*.csv` not found.
- **Scripts referenced**: `verify-zone.sh`, `consolidate-ledgers.sh` -> missing.
- **Agents referenced**: Generic Gemini mention only -> no AGENTS conflict.
- **Hooks referenced**: Mentions pre-commit hook generically -> no concrete repo hook verified.

### mechanics/MECH-headless_mode_automation.md
- **Claims verified**: Headless automation framing is internally coherent.
- **Claims falsified**: `[[SYNTHESIS-claude_code_architecture]]` missing.
- **Scripts referenced**: `triage_agent.sh`, `process_files.sh`, `nightly_audit.sh`, `deploy.sh` -> missing (example-only).
- **Agents referenced**: Claude generic -> no fleet mismatch.
- **Hooks referenced**: Only cross-ref to hooks mechanism; no direct hook file claims.

### mechanics/MECH-hooks_lifecycle_automation.md
- **Claims verified**: `.claude/settings.json` contains a hooks block; CLAUDE table declares 5 active hooks.
- **Claims falsified**: `.claude/hooks/` directory absent; plugin-specific workflow (`hookify`) not present in repo.
- **Scripts referenced**: Formatting/typecheck examples (`black`, `prettier`, `tsc`) -> not repo-bound.
- **Agents referenced**: None explicit -> N/A.
- **Hooks referenced**: PreToolUse/PostToolUse/PreCompact/Stop/UserPromptSubmit; aligns conceptually with CLAUDE hook events, but configured script paths drift.

### mechanics/MECH-mcp_server_patterns.md
- **Claims verified**: MCP architectural framing is coherent.
- **Claims falsified**: `[[SYNTHESIS-agents_mcp_foundations]]` and `[[SYNTHESIS-cross_platform_patterns]]` missing.
- **Scripts referenced**: `mcp.json`, `.mcp.json`, `managed-mcp.json` -> missing in current repo.
- **Agents referenced**: Claude/Gemini references -> both platforms present in AGENTS.
- **Hooks referenced**: None.

### mechanics/MECH-prompt_engineering_patterns.md
- **Claims verified**: `[[PRAC-oracle_to_executor_handoff]]` target exists.
- **Claims falsified**: `[[SYNTHESIS-agents_mcp_foundations]]` and `[[MECH-extended_thinking_triggers]]` missing.
- **Scripts referenced**: `context.json` examples -> missing (example-only).
- **Agents referenced**: Generic GPT/Claude references -> no direct AGENTS mismatch.
- **Hooks referenced**: None.

### mechanics/MECH-skill_system_architecture.md
- **Claims verified**: `.claude/skills/` exists; SKILL.md architecture is used in repo skill corpus.
- **Claims falsified**: `[[SYNTHESIS-claude_code_architecture]]` missing.
- **Scripts referenced**: none concrete.
- **Agents referenced**: None explicit.
- **Hooks referenced**: Mentions hooks in skill frontmatter conceptually; no direct mismatch found.

### mechanics/MECH-source_anneal_pipeline.md
- **Claims verified**: `DYN-SOURCES.csv` exists (`sources/04-SOURCES/DYN-SOURCES.csv`); `youtube_ingest.py` exists under `orchestration/00-ORCHESTRATION/scripts/`.
- **Claims falsified**: Multiple referenced scripts/paths absent (`sources/_scripts/ingest.py`, `anneal.py`, token files, several `_meta/*` flows); references `praxis/syntheses/*` path that omits `05-SIGMA` layer.
- **Scripts referenced**: `youtube_ingest.py` -> exists; `ingest.py`, `ingest.sh`, `x_ingest.py`, `anneal.py`, `manual_drop_watcher.sh` -> missing.
- **Agents referenced**: Commander/Adjudicator/Ajna -> roles/models align with AGENTS registry.
- **Hooks referenced**: Mentions post-commit hook behavior; not verified as active hook.

### mechanics/MECH-subagent_delegation.md
- **Claims verified**: Cross-refs to `MECH-skill_system_architecture` and `MECH-task_orchestration` resolve.
- **Claims falsified**: `[[SYNTHESIS-agents_mcp_foundations]]` missing.
- **Scripts referenced**: none concrete.
- **Agents referenced**: Built-in subagent archetypes (bash/explore/plan) -> not constellation-role conflict.
- **Hooks referenced**: None.

### mechanics/MECH-task_orchestration.md
- **Claims verified**: `.claude/settings.json` exists.
- **Claims falsified**: `[[SYNTHESIS-claude_code_architecture]]` missing; `.claude/tasks/my-project/*.json` examples not present.
- **Scripts referenced**: task JSON examples -> missing (example-only).
- **Agents referenced**: Generic task owners only -> no AGENTS mismatch.
- **Hooks referenced**: None.

### mechanics/MECH-youtube_ingestion_pipeline.md
- **Claims verified**: Explicit superseded marker and successor pointer are present; `youtube_ingest.py` exists (00-ORCHESTRATION path).
- **Claims falsified**: Historical output path assumptions (`sources/research/youtube/`) not reflected in current tree.
- **Scripts referenced**: `youtube_ingest.py` -> exists; `playlist_manifest.json` -> missing local artifact.
- **Agents referenced**: Ajna/Psyche mentions align with AGENTS roles.
- **Hooks referenced**: None.

### practice/PRAC-auteur_content_strategy.md
- **Claims verified**: None repo-specific.
- **Claims falsified**: None directly falsifiable against repo structure.
- **Scripts referenced**: None.
- **Agents referenced**: None.
- **Hooks referenced**: None.

### practice/PRAC-blitzkrieg_worktree_isolation.md
- **Claims verified**: `dispatch.sh` exists; `setup-worktrees.sh` exists under `orchestration/00-ORCHESTRATION/scripts/`.
- **Claims falsified**: File references legacy path `orchestration/scripts/setup-worktrees.sh`; `sources/research/MECH-git_worktree_coordination.md` and `sources/research/PRAC-parallel_claude_orchestration.md` missing.
- **Scripts referenced**: `dispatch.sh` -> exists; `orchestration/scripts/setup-worktrees.sh` -> path drift (`00-ORCHESTRATION` actual).
- **Agents referenced**: Commander/Adjudicator/Cartographer/Psyche/Ajna -> roles match AGENTS mapping.
- **Hooks referenced**: None.

### practice/PRAC-cowork_desktop_integration.md
- **Claims verified**: Cross-refs to `MECH-subagent_delegation` and `MECH-skill_system_architecture` resolve.
- **Claims falsified**: `[[SYNTHESIS-agents_mcp_foundations]]` missing.
- **Scripts referenced**: None.
- **Agents referenced**: Claude generic only.
- **Hooks referenced**: None.

### practice/PRAC-ledger_management_patterns.md
- **Claims verified**: Cross-refs to `MECH-git_worktree_coordination` and `PRAC-oracle_to_executor_handoff` resolve.
- **Claims falsified**: Core ledger artifacts and scripts missing (`ledgers/tasks-*.csv`, `validate-ledger.sh`, `consolidate-ledgers.sh`); synthesis cross-ref missing.
- **Scripts referenced**: `validate-ledger.sh`, `consolidate-ledgers.sh` -> missing.
- **Agents referenced**: None.
- **Hooks referenced**: Mentions pre-commit pattern only; no concrete current hook binding.

### practice/PRAC-multi_account_coordination.md
- **Claims verified**: Cross-refs to `MECH-git_worktree_coordination` and `PRAC-oracle_to_executor_handoff` resolve.
- **Claims falsified**: Uses missing path `orchestration/oracle_contexts/handoffs/`; synthesis cross-ref missing.
- **Scripts referenced**: None concrete.
- **Agents referenced**: Gemini routing mention aligns with AGENTS Cartographer role.
- **Hooks referenced**: None.

### practice/PRAC-multi_methodology_framework.md
- **Claims verified**: `DYN-PROJECTS.csv`, `DYN-BACKLOG.md`, `DYN-EXECUTION_STAGING.md` exist under `orchestration/00-ORCHESTRATION/state/`.
- **Claims falsified**: External-system integration claims (Jira/Trello/TeamGantt/ClickUp coupling) not verifiable from repo state.
- **Scripts referenced**: None.
- **Agents referenced**: Commander/Adjudicator/Cartographer references align with AGENTS roles.
- **Hooks referenced**: Generic statement “hooks enforce some” not contradicted.

### practice/PRAC-ontology_queries.md
- **Claims verified**: CANON corpus exists and Dataview query syntax is structurally coherent.
- **Claims falsified**: Coverage statement `10/79` is outdated; repo now has `162` CANON files and `78` with `operational_status`.
- **Scripts referenced**: None.
- **Agents referenced**: Commander authority mention does not contradict AGENTS role mapping.
- **Hooks referenced**: None.

### practice/PRAC-operational_wisdom_compendium.md
- **Claims verified**: AGENTS confirms `watch_dispatch.sh` deprecation (2026-02-17) and sole-dispatch `auto_ingest_loop.sh`; agent role/model summaries mostly align.
- **Claims falsified**: `git_sync.sh` referenced but not found in repo.
- **Scripts referenced**: `auto_ingest_loop.sh` -> exists; `watch_dispatch.sh` -> exists (deprecated); `git_sync.sh` -> missing.
- **Agents referenced**: Commander/Psyche/Adjudicator/Cartographer/Ajna -> match AGENTS fleet and roles.
- **Hooks referenced**: None explicit.

### practice/PRAC-oracle_to_executor_handoff.md
- **Claims verified**: Cross-refs to `MECH-git_worktree_coordination` and `PRAC-ledger_management_patterns` resolve.
- **Claims falsified**: Operational path `orchestration/oracle_contexts/handoffs/` does not exist.
- **Scripts referenced**: None.
- **Agents referenced**: Oracle/Executor pattern (abstract) -> no direct role conflict.
- **Hooks referenced**: None.

### practice/PRAC-parallel_claude_orchestration.md
- **Claims verified**: Cross-refs to `MECH-task_orchestration` and `PRAC-ralph_pattern_execution` resolve.
- **Claims falsified**: `[[SYNTHESIS-claude_code_architecture]]` target missing.
- **Scripts referenced**: Example task files (`task-001-*.md`, etc.) not present.
- **Agents referenced**: Claude generic only.
- **Hooks referenced**: None.

### practice/PRAC-ralph_pattern_execution.md
- **Claims verified**: Cross-refs to `MECH-context_compaction_strategies` and `MECH-headless_mode_automation` resolve.
- **Claims falsified**: `[[SYNTHESIS-claude_code_architecture]]` missing; `ralph.sh` not present.
- **Scripts referenced**: `ralph.sh` -> missing (pattern scaffold only).
- **Agents referenced**: Claude generic.
- **Hooks referenced**: None.

### practice/PRAC-semantic_compression_workflow.md
- **Claims verified**: Referenced SN assets exist under `orchestration/00-ORCHESTRATION/scripts/`.
- **Claims falsified**: Uses legacy `orchestration/scripts/*` path and missing synthesis target; placeholder `[[FileName]]` unresolved.
- **Scripts referenced**: `orchestration/scripts/sn_symbols.yaml`, `orchestration/scripts/SN_BLOCK_TEMPLATES.md` -> path drift (actual under `00-ORCHESTRATION`).
- **Agents referenced**: Claude/ChatGPT/Gemini comparative framing does not conflict with AGENTS.
- **Hooks referenced**: None.

### practice/PRAC-subagent_delegation_guide.md
- **Claims verified**: `dispatch.sh` exists (00-ORCHESTRATION); references to `PRAC-blitzkrieg_worktree_isolation.md` and `PRAC-ralph_pattern_execution.md` resolve.
- **Claims falsified**: `sources/research/MECH-subagent_delegation.md` missing; Adjudicator row says “Sonnet,” while AGENTS operational registry lists `GPT-5.2/5.3 codex`.
- **Scripts referenced**: `dispatch.sh` -> exists.
- **Agents referenced**: Adjudicator/Cartographer/Psyche -> roles match; Adjudicator model string outdated.
- **Hooks referenced**: None.

## Section 3: Synthesis Currency (SYNTHESIS-* files only)

### syntheses/SYNTHESIS-codex-cli.md
- **Platform described**: Codex CLI ecosystem snapshot (dated 2026-02-01), centered on GPT-5.2-Codex and cloud/local execution patterns.
- **Current platform state**: AGENTS Operational Registry lists Adjudicator as Codex CLI with `GPT-5.2/5.3 codex`, tmux dispatch on Mac mini.
- **Delta**: Core role alignment holds, but several cited source artifacts are absent and some comparative claims are now time-bound.
- **Verdict**: OUTDATED-MINOR

### syntheses/SYNTHESIS-gemini-cli.md
- **Platform described**: Gemini CLI + Google AI ecosystem synthesis dated 2025-07-15 with explicit “critical gap” notes.
- **Current platform state**: AGENTS Operational Registry lists Cartographer as `gemini-2.5-pro` headless (`gemini -p -y -o text`) on Mac mini.
- **Delta**: Document predates current constellation state by ~7 months and flags unresolved CLI mechanics; major currency drift.
- **Verdict**: OUTDATED-MAJOR

### syntheses/SYNTHESIS-openclaw-v2.md
- **Platform described**: OpenClaw deep research v2 (2026-02-03) with security and multi-agent operating guidance.
- **Current platform state**: AGENTS Operational Registry uses OpenClaw for Psyche (`GPT-5.3-codex`) and Ajna (`Kimi K2.5`).
- **Delta**: Still aligned at architectural level; some urgent actions/version callouts are now temporal.
- **Verdict**: OUTDATED-MINOR

### syntheses/SYNTHESIS-openclaw.md
- **Platform described**: OpenClaw v1 synthesis (2026-02-02).
- **Current platform state**: OpenClaw remains active for Psyche/Ajna per AGENTS, but v2 document is declared successor.
- **Delta**: Coverage superseded by v2’s expanded, newer synthesis.
- **Verdict**: OUTDATED-MAJOR

### syntheses/SYNTHESIS-platform_topology_jan2026.md
- **Platform described**: January 2026 multi-platform capability snapshot (Gemini 3/GPT-5.2/Grok 4.1 etc.).
- **Current platform state**: February 2026 AGENTS registry reflects updated operational fleet and routing norms.
- **Delta**: Time-bound market/platform assumptions and rates are snapshot-specific and stale against current operational reference.
- **Verdict**: OUTDATED-MAJOR

## Section 4: Supersession Chain

| Superseded File | Superseded By | Evidence |
|---|---|---|
| `mechanics/MECH-youtube_ingestion_pipeline.md` | `mechanics/MECH-source_anneal_pipeline.md` | Explicit “STATUS: SUPERSEDED” banner with named replacement. |
| `syntheses/SYNTHESIS-openclaw.md` | `syntheses/SYNTHESIS-openclaw-v2.md` | v2 header includes “Prior Version: SYNTHESIS-openclaw.md”. |

OVERLAP findings:
- `OVERLAP: mechanics/MECH-git_worktree_coordination.md + practice/PRAC-blitzkrieg_worktree_isolation.md + practice/PRAC-parallel_claude_orchestration.md`
- `OVERLAP: mechanics/MECH-subagent_delegation.md + practice/PRAC-subagent_delegation_guide.md`
- `OVERLAP: mechanics/MECH-context_compaction_strategies.md + practice/PRAC-ralph_pattern_execution.md`

## Section 5: Cross-Reference Coherence

### 5A. Wiki-Link Cross-References (extracted)

| Source File | References | Target Exists? | Target Content Matches? |
|---|---|---|---|
| praxis/05-SIGMA/mechanics/MECH-context_compaction_strategies.md | SYNTHESIS-claude_code_architecture | NO | NO |
| praxis/05-SIGMA/mechanics/MECH-context_compaction_strategies.md | MECH-task_orchestration | YES | YES |
| praxis/05-SIGMA/mechanics/MECH-context_compaction_strategies.md | PRAC-ralph_pattern_execution | YES | YES |
| praxis/05-SIGMA/mechanics/MECH-git_worktree_coordination.md | SYNTHESIS-cross_platform_patterns | NO | NO |
| praxis/05-SIGMA/mechanics/MECH-git_worktree_coordination.md | PRAC-parallel_claude_orchestration | YES | YES |
| praxis/05-SIGMA/mechanics/MECH-git_worktree_coordination.md | PRAC-ledger_management_patterns | YES | YES |
| praxis/05-SIGMA/mechanics/MECH-headless_mode_automation.md | SYNTHESIS-claude_code_architecture | NO | NO |
| praxis/05-SIGMA/mechanics/MECH-headless_mode_automation.md | PRAC-ralph_pattern_execution | YES | YES |
| praxis/05-SIGMA/mechanics/MECH-headless_mode_automation.md | MECH-hooks_lifecycle_automation | YES | YES |
| praxis/05-SIGMA/mechanics/MECH-hooks_lifecycle_automation.md | SYNTHESIS-claude_code_architecture | NO | NO |
| praxis/05-SIGMA/mechanics/MECH-hooks_lifecycle_automation.md | MECH-skill_system_architecture | YES | YES |
| praxis/05-SIGMA/mechanics/MECH-hooks_lifecycle_automation.md | PRAC-parallel_claude_orchestration | YES | YES |
| praxis/05-SIGMA/mechanics/MECH-mcp_server_patterns.md | SYNTHESIS-agents_mcp_foundations | NO | NO |
| praxis/05-SIGMA/mechanics/MECH-mcp_server_patterns.md | SYNTHESIS-cross_platform_patterns | NO | NO |
| praxis/05-SIGMA/mechanics/MECH-mcp_server_patterns.md | MECH-subagent_delegation | YES | YES |
| praxis/05-SIGMA/mechanics/MECH-prompt_engineering_patterns.md | SYNTHESIS-agents_mcp_foundations | NO | NO |
| praxis/05-SIGMA/mechanics/MECH-prompt_engineering_patterns.md | MECH-extended_thinking_triggers | NO | NO |
| praxis/05-SIGMA/mechanics/MECH-prompt_engineering_patterns.md | PRAC-oracle_to_executor_handoff | YES | YES |
| praxis/05-SIGMA/mechanics/MECH-skill_system_architecture.md | SYNTHESIS-claude_code_architecture | NO | NO |
| praxis/05-SIGMA/mechanics/MECH-skill_system_architecture.md | MECH-task_orchestration | YES | YES |
| praxis/05-SIGMA/mechanics/MECH-skill_system_architecture.md | PRAC-parallel_claude_orchestration | YES | YES |
| praxis/05-SIGMA/mechanics/MECH-source_anneal_pipeline.md | SOURCE-20260203-x-article-tempoimmaterial-subagents_when_and_how_to_use_them | NO | NO |
| praxis/05-SIGMA/mechanics/MECH-source_anneal_pipeline.md | SOURCE-20260205-x-article-jainarvind-how_do_you_build_a_context_graph | NO | NO |
| praxis/05-SIGMA/mechanics/MECH-subagent_delegation.md | SYNTHESIS-agents_mcp_foundations | NO | NO |
| praxis/05-SIGMA/mechanics/MECH-subagent_delegation.md | MECH-skill_system_architecture | YES | YES |
| praxis/05-SIGMA/mechanics/MECH-subagent_delegation.md | MECH-task_orchestration | YES | YES |
| praxis/05-SIGMA/mechanics/MECH-task_orchestration.md | SYNTHESIS-claude_code_architecture | NO | NO |
| praxis/05-SIGMA/mechanics/MECH-task_orchestration.md | MECH-skill_system_architecture | YES | YES |
| praxis/05-SIGMA/mechanics/MECH-task_orchestration.md | PRAC-parallel_claude_orchestration | YES | YES |
| praxis/05-SIGMA/practice/PRAC-cowork_desktop_integration.md | SYNTHESIS-agents_mcp_foundations | NO | NO |
| praxis/05-SIGMA/practice/PRAC-cowork_desktop_integration.md | MECH-subagent_delegation | YES | YES |
| praxis/05-SIGMA/practice/PRAC-cowork_desktop_integration.md | MECH-skill_system_architecture | YES | YES |
| praxis/05-SIGMA/practice/PRAC-ledger_management_patterns.md | MECH-git_worktree_coordination | YES | YES |
| praxis/05-SIGMA/practice/PRAC-ledger_management_patterns.md | SYNTHESIS-cross_platform_patterns | NO | NO |
| praxis/05-SIGMA/practice/PRAC-ledger_management_patterns.md | PRAC-oracle_to_executor_handoff | YES | YES |
| praxis/05-SIGMA/practice/PRAC-multi_account_coordination.md | SYNTHESIS-cross_platform_patterns | NO | NO |
| praxis/05-SIGMA/practice/PRAC-multi_account_coordination.md | MECH-git_worktree_coordination | YES | YES |
| praxis/05-SIGMA/practice/PRAC-multi_account_coordination.md | PRAC-oracle_to_executor_handoff | YES | YES |
| praxis/05-SIGMA/practice/PRAC-oracle_to_executor_handoff.md | SYNTHESIS-cross_platform_patterns | NO | NO |
| praxis/05-SIGMA/practice/PRAC-oracle_to_executor_handoff.md | MECH-git_worktree_coordination | YES | YES |
| praxis/05-SIGMA/practice/PRAC-oracle_to_executor_handoff.md | PRAC-ledger_management_patterns | YES | YES |
| praxis/05-SIGMA/practice/PRAC-parallel_claude_orchestration.md | SYNTHESIS-claude_code_architecture | NO | NO |
| praxis/05-SIGMA/practice/PRAC-parallel_claude_orchestration.md | MECH-task_orchestration | YES | YES |
| praxis/05-SIGMA/practice/PRAC-parallel_claude_orchestration.md | PRAC-ralph_pattern_execution | YES | YES |
| praxis/05-SIGMA/practice/PRAC-ralph_pattern_execution.md | SYNTHESIS-claude_code_architecture | NO | NO |
| praxis/05-SIGMA/practice/PRAC-ralph_pattern_execution.md | MECH-context_compaction_strategies | YES | YES |
| praxis/05-SIGMA/practice/PRAC-ralph_pattern_execution.md | MECH-headless_mode_automation | YES | YES |
| praxis/05-SIGMA/practice/PRAC-semantic_compression_workflow.md | FileName | NO | NO |
| praxis/05-SIGMA/practice/PRAC-semantic_compression_workflow.md | SYNTHESIS-claude_code_architecture | NO | NO |
| praxis/05-SIGMA/practice/PRAC-semantic_compression_workflow.md | orchestration/scripts/sn_symbols.yaml | YES | STALE |
| praxis/05-SIGMA/practice/PRAC-semantic_compression_workflow.md | orchestration/scripts/SN_BLOCK_TEMPLATES.md | YES | STALE |

### 5B. Non-Wiki Path References (named document mentions)

| Source File | References | Target Exists? | Target Content Matches? |
|---|---|---|---|
| `praxis/05-SIGMA/README.md` | `CONVERGENCE-METRICS.md` | NO | NO |
| `praxis/05-SIGMA/README.md` | `MECH-extended_thinking_triggers.md` | NO | NO |
| `praxis/05-SIGMA/README.md` | `PRAC-agentic_mastery_framework.md` | NO | NO |
| `praxis/05-SIGMA/README.md` | `EXEMPLA-AJNA-ARCHAEOLOGY.md` | NO | NO |
| `praxis/05-SIGMA/README.md` | `REF-CLAUDE_CODE_UNIFIED_COALESCENCE.md` | NO | NO |
| `praxis/05-SIGMA/README.md` | `MEMORY-AJNA-THREAD-EXTRACTION.md` | NO | NO |
| `praxis/05-SIGMA/README.md` | `MEMORY-CHATGPT-ASSESSMENT-EXTRACTION.md` | NO | NO |
| `praxis/05-SIGMA/EXEMPLA-README.md` | `APHORISMS.md` / `PROVERBS.md` | NO | NO |
| `praxis/05-SIGMA/EXEMPLA-README.md` | `CASE-TEMPLATE.md` / `EXAMPLE-TEMPLATE.md` | NO | NO |
| `praxis/05-SIGMA/EXEMPLA-PROVERBS.md` | `claudes-proposal.md` | NO | NO |
| `praxis/05-SIGMA/syntheses/SYNTHESIS-codex-cli.md` | `AVATAR-CODEX.md` | YES | YES |
| `praxis/05-SIGMA/syntheses/SYNTHESIS-codex-cli.md` | `DYN-RESEARCH_DISPATCH.md` | YES (archive path) | STALE |
| `praxis/05-SIGMA/syntheses/SYNTHESIS-codex-cli.md` | `claude-openai.md`, `chatgpt-openai.md`, `gemini-openai.md`, `grok-openai.md`, `perplexity-openai.md`, `openai_prompt.md` | NO | NO |
| `praxis/05-SIGMA/syntheses/SYNTHESIS-gemini-cli.md` | `GEMINI.md` | YES | YES |
| `praxis/05-SIGMA/syntheses/SYNTHESIS-gemini-cli.md` | `/syncrescendence/GEMINI.md` | NO (absolute path mismatch) | STALE |
| `praxis/05-SIGMA/syntheses/SYNTHESIS-gemini-cli.md` | `claude-google.md`, `chatgpt-google.md`, `gemini-google.md`, `grok-google.md`, `perplexity-google.md`, `google_prompt.md` | YES (`sources/04-SOURCES/research/gemini/`) | STALE |
| `praxis/05-SIGMA/syntheses/SYNTHESIS-openclaw-v2.md` | `SYNTHESIS-openclaw.md` | YES | YES |
| `praxis/05-SIGMA/syntheses/SYNTHESIS-openclaw.md` | `SOUL.md`, `USER.md`, `TOOLS.md`, `MEMORY.md` | Mixed | STALE |
| `practice/PRAC-blitzkrieg_worktree_isolation.md` | `sources/research/MECH-git_worktree_coordination.md` | NO | NO |
| `practice/PRAC-blitzkrieg_worktree_isolation.md` | `sources/research/PRAC-parallel_claude_orchestration.md` | NO | NO |
| `practice/PRAC-subagent_delegation_guide.md` | `sources/research/MECH-subagent_delegation.md` | NO | NO |

## Section 6: Structural Compliance

1. **Sanctioned subdirectories**: `mechanics/`, `practice/`, `syntheses/` exist under `praxis/05-SIGMA`; however sanctioned `exempla/` directory is absent and EXEMPLA files are root-level prefixed files.
2. **Naming prefixes**: Prefixing is mostly compliant (`MECH-`, `PRAC-`, `SYNTHESIS-`, `EXEMPLA-`, `REF-`), with expected non-prefixed docs (`README.md`) and one artifact (`.DS_Store`).
3. **`05-SIGMA/` nesting layer**: AGENTS directory model describes `praxis/{mechanics,practice,syntheses,exempla}` directly; `praxis/05-SIGMA/` is an extra structural layer and should be flagged for Sovereign review.

## Section 7: Executive Summary

- Total files inspected: 36
- CANONICAL: 3
- HIGH-SIGNAL: 16
- STALE: 11
- ORPHANED: 4
- SUPERSEDED: 2

Top 3 action items for Sovereign (ranked by impact):
1. **Resolve broken operational paths**: normalize references from `orchestration/scripts` and `orchestration/oracle_contexts/handoffs` to actual live paths (notably `orchestration/00-ORCHESTRATION/*`).
2. **Repair praxis index/coherence docs**: update `praxis/05-SIGMA/README.md` and `EXEMPLA-README.md` to match current file inventory and structure.
3. **Cull or refresh orphan/stale playbooks**: prioritize `PRAC-ledger_management_patterns.md`, `PRAC-oracle_to_executor_handoff.md`, `PRAC-subagent_delegation_guide.md`, and outdated synthesis snapshots.

