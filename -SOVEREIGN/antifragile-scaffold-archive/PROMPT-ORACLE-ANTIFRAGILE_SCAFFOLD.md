# PROMPT-ORACLE-ANTIFRAGILE_SCAFFOLD.md
## Oracle Recon: Antifragile Multi-Agent Repo Scaffold
**Priority**: P0 — Sovereign directive
**Target Platform**: Grok (Oracle) — sensor + intel + recon
**Reply-To**: Commander | **CC**: Ajna
**Date**: 2026-02-22

---

## Directive

Oracle, RECON mission. We are restructuring our repository scaffold. We need intelligence on two specific questions:

### Question 1: What should "SIGMA" be called?

Our repo has 5 top-level directories. We're renaming from numbered to semantic:
- `orchestration` → `orchestration` (nervous system: state, scripts, archive)
- `canon` → `canon` (verified immutable knowledge)
- `engine` → `engine` (operational tools: refs, funcs, prompts, avatars, models, ledgers)
- `sources` → `sources` (raw intellectual feed: transcripts, research, notebooks)
- `praxis` → **???** (distilled operational wisdom: proven patterns, mechanics, practice, platform syntheses)

SIGMA currently contains:
- `mechanics/` — 11 files: how things work (context compaction, git worktrees, hooks, MCP, subagents, etc.)
- `practice/` — 13 files: how to do things (blitzkrieg isolation, parallel orchestration, ledger management, etc.)
- `syntheses/` — 5 files: platform-specific operational synthesis (OpenClaw, Gemini CLI, Codex CLI)
- `exempla/` — 4 files: aphorisms, proverbs, cautionary tales

**What we need**: Search X and builder communities for how people name their "proven operational wisdom" layer. Is there a consensus term? Options we've considered: `wisdom`, `knowledge`, `playbook`, `doctrine`, `praxis`, `patterns`, `operations`. What resonates with the AI agent builder community? What would a new contributor immediately understand?

### Question 2: Antifragile repo patterns at scale

We're building a scaffold that:
- Currently has 5 agents across 2 machines
- Needs to scale to 10-20 agents without restructuring
- Must be SELF-HEALING (detect drift, missing files, broken refs, auto-repair or alert)
- Must be CONSENSUS-HARDENED (every directory justified by why it exists)
- Must be GROWTH-READY (adding agent 6 is trivial, not a restructuring event)

**What we need**:
1. How do production multi-agent repos handle self-healing? (CI checks? Watchdog scripts? Schema validation?)
2. What naming/structure patterns scale beyond 10 agents?
3. Are there repos that implement "antifragile" principles (get STRONGER from stress, not just resilient)?
4. Obsidian vault compatibility — does semantic naming help or hurt vault discovery?

### Search Vectors
- X: "repo structure" + "multi-agent" + "scale" (last 30 days)
- X: "knowledge base naming" OR "operational wisdom" OR "playbook" (last 30 days)
- GitHub: multi-agent repos with >1000 stars — how do they name their knowledge layer?
- ADR: antifragile software patterns 2025-2026

### Output Format
For naming: top 3 candidates with rationale + your recommendation.
For antifragile: concrete patterns with source URLs.
