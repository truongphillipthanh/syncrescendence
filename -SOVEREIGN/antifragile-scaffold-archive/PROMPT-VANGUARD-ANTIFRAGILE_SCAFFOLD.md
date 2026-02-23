# PROMPT-VANGUARD-ANTIFRAGILE_SCAFFOLD.md
## Vanguard Engineering: Self-Healing Scaffold Implementation
**Priority**: P0 — Sovereign directive
**Target Platform**: ChatGPT (Vanguard) — meticulous engineering
**Reply-To**: Commander | **CC**: Ajna
**Date**: 2026-02-22

---

## Directive

Vanguard, ENGINEERING mission. We are restructuring our multi-agent repo scaffold. Oracle is running recon on naming and antifragile patterns. Your job: engineer the self-healing and validation systems.

### Context
- 5 agents (Commander/Claude, Psyche/GPT, Ajna/Kimi, Adjudicator/Codex, Cartographer/Gemini)
- 2 machines (MacBook Air + Mac mini) connected via SSH neural bridge
- Git-tracked filesystem is ground truth
- Renaming: `orchestration` → `orchestration`, `canon` → `canon`, `engine` → `engine`, `sources` → `sources`, `praxis` → TBD
- Makefile generates platform-specific configs from single-source AGENTS.md
- launchd services run auto_ingest, watchdog, weekly eval

### What We Need Engineered

#### 1. `scripts/scaffold_validate.sh` — Structural Integrity Check
A script that validates the entire scaffold structure. Run on every commit (pre-commit hook or CI). Must check:
- All required directories exist (orchestration/, canon/, engine/, sources/, sigma-equivalent/, agents/)
- All agent offices have required structure (INIT.md, inbox/{pending,active,done,failed,blocked}, outbox/, scratchpad/, memory/)
- No orphaned files outside sanctioned locations
- No subdirectories where flat principle applies
- All DYN-* files have been updated within their stated cadence
- All ARCH-* files have version + date headers
- No broken cross-references (file links that point to moved/deleted files)
- Makefile `configs` target succeeds

Output: PASS/FAIL + specific violations. Machine-parseable (JSON or structured markdown).

#### 2. `scripts/scaffold_heal.sh` — Auto-Repair
When validation finds issues, auto-repair what's safe:
- Create missing directories (agent offices)
- Generate missing INIT.md from template
- Flag stale DYN-* files for review (don't auto-update — just alert)
- Fix broken cross-references where the target is unambiguous (file was renamed, not deleted)

Output: what was healed + what needs human attention.

#### 3. `scripts/scaffold_rename.sh` — One-Time Migration
The rename from numbered to semantic directories:
- Handles git mv (preserves history)
- Updates ALL internal references (grep + sed across all .md, .sh, .py, .yaml, .json, Makefile)
- Updates launchd plists
- Updates CLAUDE.md, AGENTS.md, README.md
- Updates .claude/ project paths
- Updates ssh/scp paths in dispatch scripts
- Produces a verification report: before/after reference counts

#### 4. Agent Office Scaling Pattern
Spec for adding agent 6-20:
- What's the minimum to create a new agent? (directory + INIT.md + inbox structure?)
- How does dispatch.sh handle new agents? (auto-discovery from agents/ dir?)
- How does auto_ingest handle new agents? (parameterized, not hardcoded?)
- How does Makefile handle new agents? (wildcard patterns?)

### Output Format
Engineer-grade. Shell scripts with comments. Config snippets. Exact commands. No hand-waving.
