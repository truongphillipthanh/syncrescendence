# DC-204: Coherence Synthesis — Scaffold Tightening Plan

**Synthesized by**: Commander (Claude Opus 4.6)
**Date**: 2026-02-23
**Authority**: Sovereign directive — "tighten the scaffold the correct way"
**Intel Sources**: Oracle DC-201 (642 files), Oracle DC-202 (147 files), Adjudicator DC-203 (36 files), Diviner DC-205 (synthesis), Cartographer DC-202 (baseline, LOW confidence)

---

## Executive Summary

Four independent inspection legs plus one synthesis leg have mapped 825 files across orchestration/, engine/, and praxis/. The scaffold is **functionally sound but constitutionally misaligned**. The system works — dispatch is operational, pipelines are active, no data has been lost — but the declared structure in AGENTS.md v6.0.0 diverges from the actual filesystem in systematic, predictable ways. Three categories of misalignment emerged with HIGH convergence across all inspectors:

1. **Nesting violations** (structural): `00-ORCHESTRATION/`, `02-ENGINE/`, `05-SIGMA/` create unsanctioned intermediate layers
2. **Reference rot** (coherence): AGENTS.md path declarations, praxis wiki-links, and model profiles all point to locations or entities that don't match reality
3. **Underpopulated infrastructure** (maturity): Ledgers are schema-ready but content-sparse; distillation pipeline exists but barely flows; sources are <2% mined

The tightening plan addresses these in priority order, respecting the Phase Gate Rule (no structural changes without scaffold_validate + memory + rollback tested).

---

## Triangulation Convergence Matrix

| Finding | Oracle DC-201 | Oracle DC-202 | Adjudicator DC-203 | Diviner DC-205 | Convergence |
|---------|:---:|:---:|:---:|:---:|:---:|
| 00-ORCHESTRATION is de-facto canonical | VERIFIED | — | — | — | 1/1 (only Oracle inspected) |
| 02-ENGINE nesting violates Flat Principle | — | VERIFIED | — | — | 2/2 (Oracle + Cartographer) |
| 05-SIGMA nesting unsanctioned | — | — | VERIFIED | — | 1/1 |
| All AGENTS.md path refs broken | VERIFIED | — | — | — | 1/1 |
| Path drift: `orchestration/scripts/*` → `00-ORCHESTRATION/scripts/*` | VERIFIED | — | VERIFIED | — | 2/2 |
| MODEL-PROFILE-* obsolete (2024-era) | — | VERIFIED | — | — | 2/2 (Oracle + Cartographer) |
| Broken wiki-links to 4 missing SYNTHESIS-* | — | — | VERIFIED | — | 1/1 |
| Ledgers in early-population transition | — | VERIFIED | — | — | 1/1 (Oracle refuted Cartographer's "pure seed" claim) |
| Distillation pipeline has active cross-refs | — | VERIFIED | — | — | 1/1 (Oracle refuted "dormant" claim) |
| Dispatch architecture SOUND | VERIFIED | — | — | — | 1/1 |
| Dual-layer reality functional but misaligned | VERIFIED | — | — | VERIFIED (as theory) | 2/2 |
| Sources <2% mined | — | VERIFIED | — | VERIFIED | 2/2 |
| "Heat Death of Context" risk | — | — | — | VERIFIED | 1/1 (novel insight) |
| "Autoimmunity" risk from over-strict validation | — | — | — | VERIFIED | 1/1 (novel insight) |

---

## Tightening Actions (Priority-Ordered)

### T0: Constitutional Alignment (P0 — blocks everything)

These actions reconcile AGENTS.md with filesystem reality. No structural changes to files — only updating the declaration to match what IS.

**T0-1: Update AGENTS.md path declarations**
- Status: All 6 path references in AGENTS.md v6.0.0 point to `orchestration/state/` but files live in `orchestration/00-ORCHESTRATION/state/`
- Action: Update AGENTS.md to declare the actual paths OR sanctify `00-ORCHESTRATION/` as the canonical location
- Evidence: Oracle DC-201 §1.1 — "Complete reference breakage"
- **SOVEREIGN DECISION REQUIRED**: Choose one:
  - (a) Sanctify `00-ORCHESTRATION/` in AGENTS.md (acknowledges reality, minimal disruption)
  - (b) Hoist files from `00-ORCHESTRATION/` to `orchestration/` root (matches current declaration, massive file move)
  - Commander recommendation: **(a)** — the files are settled, the scripts reference the current paths, and moving 462 files risks another INT-2210

**T0-2: Update AGENTS.md directory structure to reflect `02-ENGINE/` and `05-SIGMA/`**
- Status: AGENTS.md declares `engine/` and `praxis/{mechanics,practice,syntheses,exempla}` but reality is `engine/02-ENGINE/` and `praxis/05-SIGMA/{mechanics,practice,syntheses}`
- Action: Same decision pattern as T0-1 — either sanctify the nesting or flatten it
- Evidence: Oracle DC-202 §8, Adjudicator DC-203 §6
- **SOVEREIGN DECISION REQUIRED**: Choose one:
  - (a) Sanctify `02-ENGINE/` and `05-SIGMA/` in AGENTS.md
  - (b) Flatten: hoist all files up one level (147 engine files + 36 praxis files)
  - Commander recommendation: **(b) for engine/, (a) for praxis/** — engine has no subdirs to collide, praxis has sanctioned subdirs that would cause ambiguity if flattened alongside the nesting layer. But this should wait for DC-120 (scaffold_validate.sh) per Phase Gate Rule.

**T0-3: Frontier Model Registry update**
- Status: All 7 MODEL-PROFILE-* files reference 2024-era models (Claude 3 Opus, GPT-4 Turbo, Grok-2)
- Action: Create new profiles for frontier models (Opus 4.5, GPT-5.2/5.3, Gemini Pro 3.1/Flash 3.0, Grok 4.20β), archive old ones
- Evidence: Oracle DC-202 rows 14-20 all STALE/HIGH
- Dependency: None — can execute immediately
- Effort: M

### T1: Reference Repair (P1 — coherence)

**T1-1: Fix AGENTS.md Operational Registry**
- Status: Agent model names in AGENTS.md Operational Registry are stale
- Action: Update to match Frontier Model Registry (from Sovereign's correction this session)
- Effort: S

**T1-2: Repair praxis wiki-links**
- Status: Adjudicator found 4 missing SYNTHESIS-* targets referenced across 12+ praxis files: `SYNTHESIS-claude_code_architecture`, `SYNTHESIS-agents_mcp_foundations`, `SYNTHESIS-cross_platform_patterns`, `MECH-extended_thinking_triggers`
- Action: Either create these files (if the knowledge exists to populate them) or remove the broken wiki-links
- Evidence: Adjudicator DC-203 §5A — 16 broken wiki-link references
- Effort: M (if creating), S (if removing)

**T1-3: Fix praxis path references**
- Status: Multiple praxis docs reference `orchestration/scripts/*` but actual path is `orchestration/00-ORCHESTRATION/scripts/*`
- Action: Search-and-replace path references in praxis/ files (dependent on T0-1 decision)
- Evidence: Adjudicator DC-203 §2 — MECH-hooks_lifecycle_automation, PRAC-blitzkrieg_worktree_isolation, PRAC-semantic_compression_workflow all affected
- Effort: S

**T1-4: Fix praxis README and EXEMPLA-README**
- Status: Both contain incorrect file counts and reference non-existent files
- Action: Regenerate from actual directory listing
- Evidence: Adjudicator DC-203 rows 32, 34 — both STALE/HIGH
- Effort: S

**T1-5: Clean up REF-AGENTS.md duplicate in engine/**
- Status: Dangerous copy of root AGENTS.md inside engine/02-ENGINE/
- Action: Delete — single source of truth must be root AGENTS.md
- Evidence: Oracle DC-202 row 32, Cartographer claim #5 — both VERIFIED
- Effort: S

### T2: Hygiene (P2 — cleanup)

**T2-1: Prefix normalization**
- `README.md` in engine/ → `REF-ENGINE_README.md`
- `gemini-settings.json` → `DYN-GEMINI_SETTINGS.json` or move to orchestration config
- `MCP_SETUP.md` → `REF-MCP_SETUP.md`
- `REF-JIRA_INTEGRATION 2.md` → `REF-JIRA_INTEGRATION.md` (remove space)
- Evidence: Oracle DC-202 rows 25-27, 33

**T2-2: Delete artifacts**
- `.DS_Store` in engine/ and praxis/ — add to `.gitignore`
- `__pycache__/` in orchestration/scripts/ — add to `.gitignore`
- Evidence: Oracle DC-201 §7, DC-202 row 28, Adjudicator DC-203 row 36

**T2-3: Archive or cull orphaned praxis files**
- `PRAC-ledger_management_patterns.md` — ORPHANED (core artifacts don't exist)
- `PRAC-oracle_to_executor_handoff.md` — ORPHANED (handoff path doesn't exist)
- `PRAC-subagent_delegation_guide.md` — ORPHANED (source ref missing, model table stale)
- Action: Move to `orchestration/archive/` with Rule 6 protection
- Evidence: Adjudicator DC-203 rows 15, 20, 24

**T2-4: Resolve praxis content overlaps**
- MECH-git_worktree_coordination + PRAC-blitzkrieg_worktree_isolation + PRAC-parallel_claude_orchestration
- MECH-subagent_delegation + PRAC-subagent_delegation_guide
- MECH-context_compaction_strategies + PRAC-ralph_pattern_execution
- Action: Consolidate each cluster into single authoritative doc
- Evidence: Adjudicator DC-203 §4

**T2-5: Mark superseded files explicitly**
- MECH-youtube_ingestion_pipeline.md → already self-labeled SUPERSEDED
- SYNTHESIS-openclaw.md → superseded by SYNTHESIS-openclaw-v2.md
- Action: Add `STATUS: SUPERSEDED-BY:<successor>` banner to each
- Evidence: Adjudicator DC-203 §4

### T3: Population (P1 — maturity, but separate from tightening)

**T3-1: Ledger population sprint**
- Status: Oracle found ledgers in "early-population transition" — most have 0-1 entries with good schema
- Action: Targeted mining sprint using existing sources/ and praxis/ to populate each ledger with 5+ entries
- Priority: DYN-LEDGER-MODEL_CAPABILITIES (immediately stale), DYN-LEDGER-PROMPTING_CONSENSUS (high operational value), DYN-LEDGER-CONTEXT_ENGINEERING (feeds agent effectiveness)
- Dependency: T0-3 (model registry must be current first)
- Effort: L

**T3-2: Distillation pipeline activation**
- Status: Oracle confirmed active cross-refs but Diviner noted <2% source mining rate
- Action: Select 10 highest-signal source clusters (per Diviner's vein analysis) and run them through FUNC-amalgamate → FUNC-anneal → praxis/
- Effort: XL (ongoing)

---

## Execution Sequence

```
PHASE 2C: TIGHTENING (this session + next)
├── T0-3: Model profiles (no dependency, execute now)
├── T1-5: Delete REF-AGENTS.md duplicate (no dependency)
├── T2-1: Prefix normalization (no dependency)
├── T2-2: Delete artifacts + .gitignore (no dependency)
│
├── [SOVEREIGN DECISION: T0-1, T0-2 — sanctify or flatten?]
│   ├── T1-1: Update AGENTS.md Operational Registry
│   ├── T1-3: Fix praxis path references (depends on T0-1)
│   └── T1-4: Fix praxis READMEs
│
├── T1-2: Repair/create missing SYNTHESIS-* targets
├── T2-3: Archive orphaned praxis files
├── T2-4: Consolidate overlap clusters
├── T2-5: Mark superseded files
│
PHASE 2D: POPULATION (next session)
├── T3-1: Ledger population sprint
└── T3-2: Distillation pipeline activation (first 10 source clusters)
```

---

## Diviner Novel Insights (Integrated)

The Diviner's cross-disciplinary synthesis surfaced three actionable concepts for the tightening:

1. **"Heat Death of Context"**: As canon/ grows, maintenance energy exceeds ingestion energy. The tightening must include a compression/forgetting mechanism. Implication: T2-4 (overlap consolidation) is not just cleanup — it's thermodynamic necessity.

2. **"Autoimmunity"**: Over-strict AGENTS.md enforcement could reject valid but paradigm-shifting inputs. Implication: T0-1/T0-2 should sanctify reality where possible rather than forcing reality to match declaration. The system evolved these nesting patterns for reasons.

3. **"Kata vs Kumite"**: praxis/ risks becoming a museum of "how we thought it would work." Implication: T2-3 (archiving orphaned docs) and T1-2 (fixing broken wiki-links) are higher priority than they appear — stale praxis actively misleads agents.

---

## Verdict Totals (All Legs Combined)

| Verdict | orchestration/ (642) | engine/ (147) | praxis/ (36) | Total |
|---------|:---:|:---:|:---:|:---:|
| CANONICAL | 580 | 92 | 3 | 675 |
| HIGH-SIGNAL | 72 | 28 | 16 | 116 |
| STALE | 4 | 9 | 11 | 24 |
| ORPHANED | 18 | 3 | 4 | 25 |
| OPERATIONAL | 71 | — | — | 71 |
| DEPRECATED | 4 | — | — | 4 |
| SUPERSEDED | 4 | — | 2 | 6 |
| MISCLASSIFIED | — | 15 | — | 15 |
| COMPLIANT | 1 | — | — | 1 |

**825 files inspected. 675 canonical (82%). 24 stale (3%). 25 orphaned (3%). 15 misclassified (2%).**

The scaffold is healthy. The tightening is surgical, not structural.
