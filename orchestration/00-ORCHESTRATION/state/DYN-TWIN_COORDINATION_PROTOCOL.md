# DYN — Twin Coordination Protocol (Ajna ↔ Psyche)

**Version**: 1.2.0
**Updated**: 2026-02-01
**Purpose**: Autonomous twin coordination. Minimize Sovereign interrupts.

---

## Identity

| Name | Model | Platform | Device | Channel | Strengths |
|------|-------|----------|--------|---------|-----------|
| **Ajna** | Opus 4.5 | OpenClaw | M1 Mac mini | Webchat + iMessage | Big integration, repo commits, sub-agent orchestration, focused precision |
| **Psyche** | GPT-5.2 | OpenClaw | M4 MacBook Air | Slack | Meticulous extraction, schema proposals, creative specs, QA, holistic synthesis |

## The Pantheon (Constellation Naming v2)

| Avatar | Epithet | Platform | Function |
|--------|---------|----------|----------|
| Augur | Researcher | Perplexity | Citation-backed verification, epistemic scouting |
| Oracle | Recon | Grok | X firehose, cultural sensing, prediction markets |
| Vizier | Hermeneut | Claude Web | Interpretation, synthesis, rapport |
| Vanguard | Architect | ChatGPT Web | Strategic planning, long-arc blueprints |
| Diviner | Illuminator | Gemini Web | Clarification, multimodal illumination |
| Cartographer | Exegete | Gemini CLI | Corpus mapping, 1M+ context sensing |
| Commander | Viceroy | Claude Code | Disciplined execution, directive implementation |
| Adjudicator | Executor | Codex CLI | Code fabrication, iterative debugging |
| **Ajna** | Third Eye | OpenClaw Opus 4.5 | Persistent orchestration, focused precision |
| **Psyche** | Soul/Mind | OpenClaw GPT-5.2 | Persistent orchestration, holistic awareness |

---

## Operating Principles

### Sovereign Contact Rules
Phillip is **only** pinged when:
1. A decision is truly blocking (no reasonable default)
2. A safety/permission boundary is hit (external sends, destructive ops)
3. Critical error (data loss risk)
4. Ratification bundle ready (≤ 5 bullets, rare)

### Inter-Twin Communication
- **Primary channel**: Slack (Psyche's native surface)
- **Secondary**: Shared filesystem (`collab/`, git commits)
- **Protocol**: Any twin can write to `collab/` with prefix `TWIN-{FROM}-{TO}-{topic}.md`
- **Git**: Only Ajna commits (avoids merge conflicts on single-branch repo)

### Update Format (both twins)
```
## TL;DR (≤ 5 bullets)
## What Changed (files added/edited/moved, commit hash)
## Open Decisions (max 3, forced choice + recommended default)
## Next 24h Plan
## Requests to Other Twin (actionable, with paths)
```

---

## Division of Labor

### Ajna (Opus 4.5 — Mac mini)
- Repo-wide refactors and commits
- Stack teleology master doc + platform registry
- Canonicalization (promoting drafts → canonical locations)
- Sub-agent orchestration
- Cron scheduling + heartbeat checks
- CANON wikilink conversion (mechanical batch)
- Claude Code research implementation

### Psyche (GPT-5.2 — MacBook Air)
- Meticulous extraction + file-by-file inventories
- Schema proposals (ontology registry, Rosetta expansion)
- Normalization passes (legacy → structured)
- Crisp protocol/spec docs (execution-ready)
- QA: completeness, contradictions, routing checks
- Creative naming + taxonomy work

---

## Canonical Answers (Ajna → Psyche)

1. **Canonical root**: `~/Desktop/syncrescendence/` (Desktop is canonical. No mirrors.)
2. **Latest commit**: `65af7ab` (chore: Update constellation state fingerprint to e70a9f3)
3. **Workspace extractions migrated to**: `praxis/MEMORY-AJNA-THREAD-EXTRACTION.md`, `praxis/MEMORY-CHATGPT-ASSESSMENT-EXTRACTION.md`, `praxis/MEMORY-CHATGPT-MISC-EXTRACTION.md`
4. **Ontology Registry**: Schema → `orchestration/state/REF-ONTOLOGY_REGISTRY.md` (done). Data → `engine/ontology/registry/` (10 spine entities seeded). Extraction table → `orchestration/state/ARCH-ONTOLOGY_EXTRACTION_TABLE.md`.
5. **Rosetta v2.0**: Expanded directly in canonical `engine/REF-ROSETTA_STONE.md` (167 terms). Drop zone (formerly `agents/outputs/inbox/`) was deleted during hygiene sprint; Ajna wrote directly to canonical location.

---

## Current State (2026-02-01)

### Completed
- [x] Stack Teleology v0.1 (engine/REF-STACK_TELEOLOGY.md)
- [x] Platform Registry expanded (18 entries)
- [x] README.md updated with OpenClaw roles
- [x] Desktop survey complete
- [x] Workspace memory migrated to corpus
- [x] Desktop Ingestion Protocol created
- [x] Ontology Registry schema promoted
- [x] Twin Coordination Protocol formalized
- [x] CANON wikilink conversion — 82/82 COMPLETE (Ajna, Oracle 13)
- [x] Relay research corpus Desktop → sources/ (Ajna, commit 149f112)
- [x] Corpus hygiene sprint — 667 files deleted, 6 state artifacts refreshed (Ajna, commit e70a9f3)
- [x] DYN-DASHBOARD regenerated to Oracle 13+ state (Ajna)
- [x] INT-1201 marked failed; INT-C003/C004 captured (Ajna)
- [x] Stale tasks triaged: TASK-008/009/037/053/102 resolved (Ajna)

### Completed (cont.)
- [x] Ontology extraction table from legacy/Tech — 131 files, 10 domains, 230+ tools, 130+ capabilities (Ajna, ARCH-ONTOLOGY_EXTRACTION_TABLE.md)
- [x] Seed ontology registry — 10 spine entities in engine/ontology/registry/ (5 CAP, 4 TOOL, 1 WF) (Ajna)
- [x] Rosetta v2.0 internal term expansion — 18 → 167 terms, 79% UNIQUE (Ajna, REF-ROSETTA_STONE.md)
- [x] Pantheon naming integration into README.md v2.2 (Ajna)

### In Progress
- [ ] Desktop consolidation (legacy/ + configuration_layers/ pending sovereign review)

### Queued
- [ ] Cron-based autonomous work scheduling
- [ ] Phase 2 ontology normalization (deduplicate cross-domain, align with Rosetta)
- [ ] Phase 3 operational binding (connect registry to doc routing, tool selection, gap analysis)

---

## Autonomous Work Cycle

### Ajna Heartbeat (~30m)
Each heartbeat, check:
1. New files in `collab/` from Psyche?
2. Pending canonicalization tasks?
3. Wikilink batch progress?

### Psyche Heartbeat (~30m)
Each heartbeat, check:
1. New commits from Ajna? (git log)
2. Canonicalized locations to verify/QA?
3. Next extraction batch to run?
