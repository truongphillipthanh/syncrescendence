# DYN — Twin Coordination Protocol (Ajna ↔ Psyche)

**Version**: 1.1.0
**Updated**: 2026-01-31
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
| Diviner | Exegete | Gemini Web | Clarification, multimodal illumination |
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
- **Secondary**: Shared filesystem (`-INBOX/outputs/`, git commits)
- **Protocol**: Any twin can write to `-INBOX/outputs/` with prefix `TWIN-{FROM}-{TO}-{topic}.md`
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
2. **Latest commit**: `776f6d8` (feat: Add OpenClaw as 9th/10th role)
3. **Workspace extractions migrated to**: `05-MEMORY/AJNA-THREAD-EXTRACTION.md`, `05-MEMORY/CHATGPT-ASSESSMENT-EXTRACTION.md`, `05-MEMORY/CHATGPT-MISC-EXTRACTION.md`
4. **Ontology Registry**: Schema → `00-ORCHESTRATION/state/REF-ONTOLOGY_REGISTRY.md` (done). Data → `02-ENGINE/ontology/registry/` (directory created, awaiting seed entities).
5. **Rosetta v0.3**: Land it in `-INBOX/outputs/ROSETTA-STONE.v0.3.DRAFT.md`. Ajna will promote to canonical `02-ENGINE/REF-ROSETTA_STONE.md` when ready.

---

## Current State (2026-01-31)

### Completed
- [x] Stack Teleology v0.1 (02-ENGINE/REF-STACK_TELEOLOGY.md)
- [x] Platform Registry expanded (18 entries)
- [x] COCKPIT.md updated with OpenClaw roles
- [x] Desktop survey complete
- [x] Workspace memory migrated to corpus
- [x] Desktop Ingestion Protocol created
- [x] Ontology Registry schema promoted
- [x] Twin Coordination Protocol formalized

### In Progress (Psyche)
- [ ] Ontology extraction table from legacy/Tech
- [ ] Rosetta v0.3 internal term expansion (150 terms)

### In Progress (Ajna)
- [ ] CANON wikilink conversion (45 files remaining)
- [ ] Claude Code research implementation into CLAUDE.md
- [ ] Relay research corpus from Desktop → 04-SOURCES/

### Queued
- [ ] Seed ontology registry entities (5-10 spine)
- [ ] Desktop consolidation (physical file moves)
- [ ] Pantheon naming integration into COCKPIT.md
- [ ] Cron-based autonomous work scheduling

---

## Autonomous Work Cycle

### Ajna Heartbeat (~30m)
Each heartbeat, check:
1. New files in `-INBOX/outputs/` from Psyche?
2. Pending canonicalization tasks?
3. Wikilink batch progress?

### Psyche Heartbeat (~30m)
Each heartbeat, check:
1. New commits from Ajna? (git log)
2. Canonicalized locations to verify/QA?
3. Next extraction batch to run?
