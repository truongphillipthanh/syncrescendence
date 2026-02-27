---
id: arch-rosetta_normalization_audit
kind: architecture
scope: orchestration
target: state
---

# Rosetta Stone Normalization Audit (DC-302)

**Version**: 1.0.0
**Updated**: 2026-02-24
**Authority**: Commander (Opus 4.6)
**Source**: REF-ROSETTA_STONE.md v2.7.0 (311 entries)
**Method**: Automated grep of all `*.md` files, excluding `sources/` raw feed and `-SOVEREIGN/CONFIG-SANDBOX`

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| DEPRECATED terms in Rosetta Stone | 10 |
| DEPRECATED terms with active usage (outside Rosetta/sources) | 8 |
| Total files with deprecated term usage | ~65 (deduplicated) |
| Orphan terms found (used but not in Rosetta) | 3 |
| ALIGNED/ADAPTED spot-check failures | 1 |

**Overall assessment**: Deprecated terminology is widespread in operational docs, archive, and engine. The highest-impact contamination is "Oracle" (used as session label in 50+ files), "Oracle-Executor" (11 active files), and "Chain Matrix / Tri-Helix" (21 files). Most deprecated usage is in archive and historical clarescence files, but several live operational files (state/, engine/, praxis/) need remediation.

---

## Per-Term Findings

### DEPRECATED Terms

#### 1. Wells vs Rivers (Rosetta #3)
- **Replacement**: "ephemeral vs durable"
- **Files using deprecated term** (excluding sources/, Rosetta itself):
  - `engine/02-ENGINE/REF-FLEET_COMMANDERS_HANDBOOK.md`
- **Severity**: LOW (1 active file)
- **Action**: Replace in Fleet Commander's Handbook

#### 2. Oracle-Executor (Rosetta #6)
- **Replacement**: "Plan/Implementation"; "Oracle" now exclusively = Grok
- **Files using deprecated term** (excluding sources/, Rosetta itself, CONFIG-SANDBOX):
  - `orchestration/00-ORCHESTRATION/state/ARCH-ONTOLOGY_ANNEALMENT_v2.md`
  - `orchestration/00-ORCHESTRATION/archive/ARCH-ONTOLOGY_ANNEALMENT_v2.md`
  - `orchestration/00-ORCHESTRATION/archive/PRAC-oracle_to_executor_handoff.md`
  - `agents/commander/inbox/done/RESULT-ADJUDICATOR-DC203-PRAXIS_DEEP_INSPECTION.md`
  - `agents/commander/inbox/active/RESULT-ADJUDICATOR-DC203-PRAXIS_DEEP_INSPECTION.md`
  - `-INBOX/commander/00-INBOX0/RESPONSE-ADJUDICATOR-PRAXIS_DEEP_INSPECTION.md`
  - `orchestration/00-ORCHESTRATION/state/impl/.scratch/SOURCES-DIGEST-RESEARCH.md`
  - `orchestration/00-ORCHESTRATION/state/impl/.scratch/VERIFY-C-gaps_metachar_scaffold.md`
  - `orchestration/00-ORCHESTRATION/state/impl/.scratch/VERIFY-D-clarescence.md`
- **Severity**: MEDIUM (9 files; 1 in active state/, rest in archive/scratch/inbox)
- **Action**: Update ARCH-ONTOLOGY_ANNEALMENT_v2.md (state copy). Archive/inbox files are historical artifacts; no remediation needed.

#### 3. IMEP (Rosetta #13)
- **Replacement**: Hook responses / execution logs
- **Files using deprecated term** (excluding sources/, Rosetta itself):
  - `orchestration/00-ORCHESTRATION/archive/ARCH-ORACLE_GENEALOGY.md`
  - `orchestration/00-ORCHESTRATION/archive/ARCH-EXECUTION_HISTORY.md`
  - `engine/02-ENGINE/PROTO-ChatGPT-Onboarding.md`
  - `engine/02-ENGINE/PROTO-Gemini-Onboarding.md`
  - `engine/02-ENGINE/REF-PROMPT_REGISTRY.md`
  - `engine/02-ENGINE/REF-STATION_PROMPTS_REGISTRY.md`
  - `orchestration/00-ORCHESTRATION/archive/outgoing-2026-02/RESULT-commander-20260206-three_inbox_tasks.md`
  - `orchestration/00-ORCHESTRATION/archive/sovereign-resolved/SOVEREIGN-008-CANON_31150_TERMINOLOGY.md`
  - `agents/commander/inbox/done/TASK-20260206-sovereign008-approval.md`
- **Severity**: MEDIUM (9 files; 4 in engine active docs need cleanup)
- **Action**: Remove IMEP references from PROTO-ChatGPT-Onboarding, PROTO-Gemini-Onboarding, REF-PROMPT_REGISTRY, REF-STATION_PROMPTS_REGISTRY

#### 4. Chain Matrix / Tri-Helix (Rosetta #16)
- **Replacement**: IIC framework (#15) for active chain concepts; historical only
- **Files using deprecated term** (excluding sources/, Rosetta itself, CONFIG-SANDBOX):
  - `orchestration/00-ORCHESTRATION/state/ARCH-SOVEREIGNTY_STRATA.md`
  - `orchestration/00-ORCHESTRATION/state/ARCH-ROSETTA_ONTOLOGY_BRIDGE.md`
  - `orchestration/00-ORCHESTRATION/state/ARCH-ONTOLOGY_ANNEALMENT_v2.md`
  - `orchestration/00-ORCHESTRATION/state/impl/clarescence/` (8+ clarescence files)
  - `orchestration/00-ORCHESTRATION/state/impl/.scratch/` (5+ scratch files)
  - `orchestration/00-ORCHESTRATION/archive/` (3 files)
- **Severity**: HIGH (21 files; 3 in active state/ docs)
- **Action**: Update ARCH-SOVEREIGNTY_STRATA.md, ARCH-ROSETTA_ONTOLOGY_BRIDGE.md, ARCH-ONTOLOGY_ANNEALMENT_v2.md to mark Chain Matrix/Tri-Helix references as deprecated inline. Clarescence/scratch files are implementation artifacts; low priority. **WARNING**: Do NOT touch convergence Tri-Helical Strategy (#242) references -- that is a different concept.

#### 5. Blitzkrieg Lane A/B/C (Rosetta #18)
- **Replacement**: Neo-Blitzkrieg full constellation pipeline
- **Files using deprecated term** (excluding sources/, Rosetta itself, CONFIG-SANDBOX):
  - `orchestration/00-ORCHESTRATION/archive/ARCH-DIRECTIVE_COMPENDIUM.md`
  - `praxis/05-SIGMA/practice/PRAC-blitzkrieg_worktree_isolation.md`
  - `engine/02-ENGINE/REF-BLITZKRIEG_PROTOCOL.md`
  - `orchestration/00-ORCHESTRATION/state/impl/CAPABILITY-MATRIX-20260207-twin-swarm-routing.md`
  - `orchestration/00-ORCHESTRATION/state/impl/clarescence/CLARESCENCE-2026-02-08-sovereign-cockpit-architecture.md`
  - `orchestration/00-ORCHESTRATION/state/REF-NEO_BLITZKRIEG_BUILDOUT.md`
  - `engine/02-ENGINE/REF-FLEET_COMMANDERS_HANDBOOK.md`
  - `engine/02-ENGINE/REF-SAAS_INTEGRATION_ARCHITECTURE.md`
  - `.claude/commands/project/blitzkrieg_issue.md`
- **Severity**: HIGH (9 files; 4 in active engine/praxis docs)
- **Action**: Update REF-BLITZKRIEG_PROTOCOL.md, PRAC-blitzkrieg_worktree_isolation.md, REF-FLEET_COMMANDERS_HANDBOOK.md, REF-SAAS_INTEGRATION_ARCHITECTURE.md to reference Neo-Blitzkrieg. The blitzkrieg_issue.md command file also needs updating.

#### 6. Archetype Engineering (Rosetta #79)
- **Replacement**: Reception Calibration (active paradigm)
- **Files using deprecated term** (excluding sources/, Rosetta itself):
  - `orchestration/00-ORCHESTRATION/state/ARCH-ROSETTA_ONTOLOGY_BRIDGE.md`
  - `orchestration/00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md`
  - `orchestration/00-ORCHESTRATION/archive/ARCH-DESIGN_DECISIONS_GENESIS.md`
- **Severity**: MEDIUM (3 files; 2 in active state/)
- **Action**: Update ARCH-ROSETTA_ONTOLOGY_BRIDGE.md and ARCH-INTENTION_COMPASS.md

#### 7. Deviser (Rosetta #95, renamed to Vanguard)
- **Replacement**: Vanguard
- **Files using deprecated term** (excluding sources/, Rosetta itself):
  - `orchestration/00-ORCHESTRATION/state/ARCH-ROSETTA_ONTOLOGY_BRIDGE.md`
  - `orchestration/00-ORCHESTRATION/state/ARCH-ONTOLOGY_ANNEALMENT_v1.md`
  - `orchestration/00-ORCHESTRATION/archive/ARCH-ONTOLOGY_ANNEALMENT_v1.md`
  - `orchestration/00-ORCHESTRATION/archive/ARCH-EXECUTION_HISTORY.md`
  - `orchestration/00-ORCHESTRATION/state/DYN-BACKLOG.md`
  - `canon/01-CANON/CANON-31150-PLATFORM_CAPABILITY_CATALOG.md`
  - `orchestration/00-ORCHESTRATION/archive/outgoing-2026-02/RESULT-commander-20260206-three_inbox_tasks.md`
  - `orchestration/00-ORCHESTRATION/archive/sovereign-resolved/SOVEREIGN-008-CANON_31150_TERMINOLOGY.md`
  - `agents/commander/inbox/done/TASK-20260206-sovereign008-approval.md`
- **Severity**: HIGH (9 files; 3 in active state/ or canon/)
- **Action**: Update DYN-BACKLOG.md, ARCH-ROSETTA_ONTOLOGY_BRIDGE.md, CANON-31150 (requires Sovereign approval for canon/ edits)

#### 8. megathink (Rosetta #159)
- **Replacement**: "think hard"
- **Files using deprecated term** (excluding sources/, Rosetta itself):
  - `orchestration/00-ORCHESTRATION/state/ARCH-ROSETTA_ONTOLOGY_BRIDGE.md`
- **Severity**: LOW (1 active file)
- **Action**: Replace in ARCH-ROSETTA_ONTOLOGY_BRIDGE.md

#### 9. Five-Account Model (Rosetta #160)
- **Replacement**: Historical only (subsumed by IIC framework)
- **Files using deprecated term** (excluding Rosetta itself):
  - `orchestration/00-ORCHESTRATION/state/ARCH-ROSETTA_ONTOLOGY_BRIDGE.md`
- **Severity**: LOW (1 active file)
- **Action**: Mark as historical in ARCH-ROSETTA_ONTOLOGY_BRIDGE.md

#### 10. SN Format (Rosetta #12, renamed to Syncrescript)
- **Not searched** -- low risk since tooling retains `sn_` prefix for backward compatibility. Rosetta migration path already documented.

---

### Orphan Terms (used in active docs but NOT in Rosetta Stone)

#### O1. "Oracle session" / "Oracle N" (historical session numbering)
- **Status**: Rosetta #72 covers "Council (fmr. Oracle Session)" but many files still use "Oracle session" or "Oracle 0-17" numbering
- **Active files with legacy "Oracle session/Oracle N" usage**: 51 files total
  - Key active state files: `ARCH-TASK_TIER_ARCHITECTURE.md`, `ARCH-INTENTION_COMPASS.md`, `DYN-TWIN_COORDINATION_PROTOCOL.md`, `DYN-PEDIGREE_LOG.md`
  - Key engine files: `REF-FLEET_COMMANDERS_HANDBOOK.md`, `REF-STATION_PROMPTS_REGISTRY.md`, `PROTO-Gemini-Onboarding.md`
  - Key canon files: `CANON-25100`, `CANON-25200`, `CANON-25500`
- **Severity**: HIGH -- This is the single largest terminology debt. "Oracle" is ambiguous (historical session label vs. current Grok epithet).
- **Action**: In active docs, replace "Oracle session N" with "Council N" (for N >= 18) or mark as historical lineage (for N < 18). Pedigree logs retain "Oracle 0-17" as lineage markers per Rosetta migration path.

#### O2. "Ring 7" / "Seven Rings" (pre-sigma terminology)
- **Rosetta #5 says migration COMPLETE** but 11 files still use "Ring" terminology
  - `ARCH-NEO_SCAFFOLD.md`, `ARCH-NEO_EXOCORTEX.md`, `ARCH-NEO_CANON_CORE.md` (state + archive copies)
  - `IMPLEMENTATION-MAP.md`
  - Various scratch/heritage files
- **Severity**: MEDIUM (migration declared complete but residual usage remains)
- **Action**: Update active state files. Mark Rosetta #5 migration as PARTIAL until cleaned.

#### O3. "Vanguard" as active agent name
- **Rosetta #119 lists Vanguard as UNIQUE** (ChatGPT Web avatar) but Vanguard was part of the old Neo-Blitzkrieg pipeline and appears in 83 files. The term itself is not deprecated, but its role has shifted -- it appears in pipeline descriptions alongside deprecated concepts (Lane A/B/C).
- **Severity**: LOW -- term is correctly defined in Rosetta; usage is consistent with current definition.
- **Action**: No remediation needed for the term itself, only for co-occurring deprecated pipeline references.

---

### ALIGNED/ADAPTED Spot-Checks

#### S1. Ralph Pattern (Rosetta #17, ALIGNED)
- **Expected**: Consistent usage matching "Ralph Wiggum Pattern"
- **Result**: PASS. Usage in `praxis/05-SIGMA/practice/PRAC-ralph_pattern_execution.md` is consistent. No conflicting definitions found.

#### S2. Chorus/Medley distinction (Rosetta #8, ALIGNED)
- **Expected**: Constellation described as operating in "Medley mode" per Rosetta migration path
- **Result**: PARTIAL FAIL. CLAUDE.md and AGENTS.md do not explicitly state "Medley mode." The Rosetta migration path says to "Update COCKPIT.md to clarify" but this appears incomplete. Active docs still conflate Chorus and Constellation.
- **Action**: Add "operating in Medley mode" clarification to AGENTS.md Enterprise Role Mapping section.

#### S3. Fingerprint / Handoff Token (Rosetta #2, ADAPTED)
- **Expected**: Both terms used correctly per Rosetta definitions
- **Result**: PASS. CLAUDE.md correctly references both concepts. `REF-STATE_FINGERPRINT_PROTOCOL.md` exists in engine.

---

## Prioritized Remediation Plan

### Priority 1 -- HIGH IMPACT (active operational docs)

| # | Term | Files to Fix | Effort |
|---|------|-------------|--------|
| R1 | "Oracle session/Oracle N" in active state + engine | ~15 active files | MEDIUM -- requires careful distinction between historical lineage markers and deprecated usage |
| R2 | Chain Matrix / Tri-Helix in active state | 3 files (ARCH-SOVEREIGNTY_STRATA, ARCH-ROSETTA_ONTOLOGY_BRIDGE, ARCH-ONTOLOGY_ANNEALMENT_v2) | LOW |
| R3 | Blitzkrieg Lane A/B/C in engine + praxis | 4 files (REF-BLITZKRIEG_PROTOCOL, PRAC-blitzkrieg_worktree_isolation, REF-FLEET_COMMANDERS_HANDBOOK, REF-SAAS_INTEGRATION_ARCHITECTURE) | LOW |
| R4 | Deviser in DYN-BACKLOG + CANON-31150 | 2-3 files (CANON edit needs Sovereign approval) | LOW |

### Priority 2 -- MEDIUM IMPACT (consistency + correctness)

| # | Term | Files to Fix | Effort |
|---|------|-------------|--------|
| R5 | Oracle-Executor in state | 1 file (ARCH-ONTOLOGY_ANNEALMENT_v2) | LOW |
| R6 | IMEP in engine protos + registries | 4 files | LOW |
| R7 | Archetype Engineering in state | 2 files | LOW |
| R8 | Ring 7 / Seven Rings residual | 3-4 active state files | LOW |
| R9 | Chorus/Medley distinction in AGENTS.md | 1 file | LOW |

### Priority 3 -- LOW IMPACT (cosmetic / archive)

| # | Term | Files to Fix | Effort |
|---|------|-------------|--------|
| R10 | Wells vs Rivers in Fleet Handbook | 1 file | TRIVIAL |
| R11 | megathink in ontology bridge | 1 file | TRIVIAL |
| R12 | Five-Account Model in ontology bridge | 1 file | TRIVIAL |

### Exclusions (no action needed)

- **Archive files** (`orchestration/00-ORCHESTRATION/archive/`): Historical record; deprecated terms are expected.
- **Source files** (`sources/`): Raw intellectual feed; not normalization targets.
- **Scratch/impl files** (`state/impl/.scratch/`): Working artifacts; will be cleaned during Phase 2C completion.
- **Inbox done/active files**: Task artifacts; historical.
- **Canon files**: Protected zone; changes require Sovereign approval. Flag for R4 (Deviser in CANON-31150) only.
- **CONFIG-SANDBOX**: Excluded per audit scope.
- **Rosetta Stone itself**: Self-referential; deprecated terms are documented there by design.

---

## Estimated Total Remediation Effort

- **Priority 1**: ~2 hours (careful Oracle session disambiguation across 15 files)
- **Priority 2**: ~1 hour (straightforward find-and-replace with context awareness)
- **Priority 3**: ~15 minutes (trivial replacements)
- **Total**: ~3.25 hours of focused normalization work

---

## Next Steps

1. Sovereign approval for CANON-31150 edit (Deviser -> Vanguard)
2. Execute Priority 1 remediation (batch operation with grep verification)
3. Update Rosetta Stone #5 migration status from COMPLETE to PARTIAL
4. Execute Priority 2-3 remediation
5. Run verification grep to confirm zero deprecated terms in active docs
6. Update this audit to v1.1.0 with post-remediation statistics
