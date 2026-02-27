# TASK: Annealment v2 Verification & Gap Patching — MBA Reinit

**Status**: DONE
**Priority**: P0
**Reply-To**: commander
**CC**: commander
**Created**: 2026-02-17
**Authority**: Sovereign directive (Session 20)
**Machine**: MBA (m4-macbook-air)

---

## Directive

You are Commander (Opus) reinitializing on the MBA to complete the Unified Corpus Annealment v2. The synthesis document has been written but needs verification — confirm no details were missed, patch any sensing gaps, and ensure the document is a faithful triangulation of all sources.

**Enter /plan mode first.** Explore before executing.

---

## What Was Done (Mac mini session, 2026-02-17)

### Phase 1: Canon Digest Completion (4 of 5 digests existed from prior session)
Previous session (Session 20a) produced 4 digests but CANON indexer failed at 264K tokens. This session split canon into 5 shards via parallel Sonnet agents:

| Shard | File | Lines | Range |
|-------|------|-------|-------|
| canon-0x | `ANNEAL-DIGEST-CANON-0X.md` | 319 | CANON-00000–09999 (18 files) |
| canon-1x2x | `ANNEAL-DIGEST-CANON-1X2X.md` | 307 | CANON-10000–29999 (13 files) |
| canon-30 | `ANNEAL-DIGEST-CANON-30.md` | 209 | CANON-30000–30999 (15 files) |
| canon-31 | `ANNEAL-DIGEST-CANON-31.md` | 236 | CANON-31000–31999 (26 files) |
| canon-32-35 | `ANNEAL-DIGEST-CANON-32-35.md` | 387 | CANON-32000–35999 (20 files) |

All at: `orchestration/state/impl/.scratch/`

Note: canon-30+31 combined (56 files) overflowed Sonnet's context. Had to split into two separate agents.

### Phase 2: Convergence Synthesis
One Sonnet agent read ALL inputs and produced the final document:

**Output**: `orchestration/state/ARCH-ONTOLOGY_ANNEALMENT_v2.md`
- 765 lines, 50KB
- Committed as `bb0446d`

### Inputs to Convergence Agent
The agent read these 14 source groups:

**Digests (pre-distilled, in `.scratch/`):**
1. ANNEAL-DIGEST-CANON-0X.md (319 lines)
2. ANNEAL-DIGEST-CANON-1X2X.md (307 lines)
3. ANNEAL-DIGEST-CANON-30.md (209 lines)
4. ANNEAL-DIGEST-CANON-31.md (236 lines)
5. ANNEAL-DIGEST-CANON-32-35.md (387 lines)
6. ANNEAL-DIGEST-GAPS.md (412 lines) — from prior session
7. ANNEAL-DIGEST-METACHAR.md (307 lines) — from prior session
8. ANNEAL-DIGEST-SCAFFOLD.md (381 lines) — from prior session
9. ANNEAL-DIGEST-CLARESCENCE.md (581 lines) — at `impl/clarescence/.scratch/` (wrong path, known)

**Raw sources (read directly by convergence agent):**
10. ARCH-ONTOLOGY_ANNEALMENT_v1.md (605 lines)
11. syncrescendence_convergence.md (~600 lines)
12. syncrescendent_convergence_aligned.md (~600 lines)
13. new_ontology_metacharacterization/ (5 files: prompt + claude/chatgpt/gemini/grok)
14. new_ontology_metacharacterization_2/ (5 files: prompt + claude/chatgpt/gemini/grok)

### V2 Section Structure
```
## 1. Ontological Core — entity types, orbital classes, six chains, Cognitive Palace, Modal Sequence
## 2. Canon Taxonomy — chains, hierarchies, thematic clusters, numbering schema
## 3. Reconception: Palantir-Inspired Ontology — semantic+kinetic+dynamic layers, sovereign stack
## 4. Scaffold State — five-tier tasks, constellation agents, MCP/tools, memory, automation
## 5. Strategic Convergence — tri-helical strategy, Alchemizing Catalyst, modal timeline
## 6. Clarescence Synthesis — recurring themes, resolved tensions, persistent gaps
## 7. Gap Analysis — missing, contradictory, aspirational vs. operational
## 8. Delta from v1 — new concepts, retired concepts, structural shifts
## Appendix: Key File Paths Referenced
```

---

## Known Risks & Issues

### 1. Convergence Agent Hit Rate Limits Twice
The convergence agent was rate-limited mid-read on the first attempt, then resumed. On resume, it had all source material in context but the write was a single monolithic Write call. Risk: the agent may have lost fidelity on sources read early in context (metachar raw files especially) due to context distance.

### 2. No Intermediate Inbox Digest
Per the plan, raw inbox sources (metachar LLM outputs + convergence docs) should have been pre-digested before feeding to the convergence agent. This step was SKIPPED — the convergence agent read them raw alongside digests. Total input was ~6K+ lines, which is above the 3K-line-per-agent budget established this session.

**SEARED LESSON**: Every input to a final synthesis agent must be pre-distilled. Raw → Digest → Synthesis is mandatory pipeline. See `memory/context-engineering.md`.

### 3. Canon File Count Discrepancy
Canon survey found 160 .md files. Digest agents report processing: 18 + 13 + 15 + 26 + 20 = 92 unique files. The `sn/` subdirectory contains mirrors (identical content), so agents correctly skipped them. But 160 - 92 = 68 files unaccounted for — likely the sn/ mirrors, but this was never explicitly verified.

### 4. CLARESCENCE Digest Still at Wrong Path
`ANNEAL-DIGEST-CLARESCENCE.md` lives at `impl/clarescence/.scratch/` instead of `impl/.scratch/`. Convergence agent read it from the correct (wrong) path. Should be moved or symlinked for consistency.

### 5. DC-004 Rosetta Stone Terms
The convergence agent flagged ~25 ontological terms resolved in clarescences but never formalized to `REF-ROSETTA_STONE.md`. Target date was 2026-02-18. Until enumerated, the V2 entity taxonomy is incomplete.

---

## Your Objective (MBA Session)

### Primary: Verify Annealment v2 Completeness

1. **Read `ARCH-ONTOLOGY_ANNEALMENT_v2.md`** (765 lines — delegate to Sonnet agent, do NOT read into Opus context)
2. **Cross-reference against each digest** — have a Sonnet agent check: does every major concept from each digest appear in v2? Produce a coverage checklist.
3. **Cross-reference against inbox sources** — specifically the metacharacterization reconception ideas. The 4-model x 2-prompt exercise produced rich material (Palantir ontology primitives, sovereign stack architecture, prosumer analogues, shackle-vs-organ framing). Verify v2 captures the synthesis, not just surface mentions.
4. **Verify canon coverage** — confirm the 92 vs 160 file count (are the remaining 68 all sn/ mirrors?). If any unique files were missed, flag them.

### Secondary: Patch Gaps

5. If verification reveals missing concepts, produce a **PATCH file** at `impl/.scratch/ANNEAL-V2-PATCHES.md` with specific insertions (section, location, content).
6. Apply patches to v2 if warranted. Keep the 800-line ceiling — compress elsewhere if adding.

### Tertiary: Orchestration Improvement

7. **Context limit protocol**: When dispatching Sonnet agents for this verification, enforce the 3K-line budget. If an agent needs to read v2 (765 lines) + a digest (300-400 lines), that's ~1,100 lines — well within budget. Good.
8. If producing a final patched v2, commit as `fix(anneal): v2 verification patches — [description]`.

---

## Context Limit Handling Rules (SEARED this session)

- Opus = orchestrator. <10K token content budget. NEVER reads raw corpus.
- `wc -l` before every Read. >500 lines → delegate to Sonnet.
- Every input to a synthesis agent must be pre-distilled (<400 lines each).
- Max ~3,000 total lines per agent across all reads.
- Canon: max ~30 files or ~60K tokens per shard.
- 30+31 combined (56 files) OVERFLOWS. Split at 30-file boundary.
- NEVER read from directories containing CLAUDE.md (auto-loads ~20K tokens).
- Full rules at: `memory/context-engineering.md`

---

## Key File Paths

| File | Path |
|------|------|
| V2 output | `orchestration/state/ARCH-ONTOLOGY_ANNEALMENT_v2.md` |
| V1 (superseded) | `orchestration/state/ARCH-ONTOLOGY_ANNEALMENT_v1.md` |
| Canon digests | `orchestration/state/impl/.scratch/ANNEAL-DIGEST-CANON-*.md` |
| Other digests | `orchestration/state/impl/.scratch/ANNEAL-DIGEST-{GAPS,METACHAR,SCAFFOLD}.md` |
| Clarescence digest | `orchestration/state/impl/clarescence/.scratch/ANNEAL-DIGEST-CLARESCENCE.md` |
| Task file (this) | `-INBOX/commander/00-INBOX0/TASK-20260217-annealment_v2_verification_reinit.md` |
| Context engineering | `~/.claude/projects/-Users-home/memory/context-engineering.md` |
| Inbox metachar 1 | `-INBOX/commander/new_ontology_metacharacterization/` |
| Inbox metachar 2 | `-INBOX/commander/new_ontology_metacharacterization_2/` |
| Convergence docs | `-INBOX/commander/syncrescendence_convergence.md` (DELETED from inbox post-commit — content in v2) |
| Convergence aligned | `-INBOX/commander/syncrescendent_convergence_aligned.md` (DELETED from inbox post-commit — content in v2) |
| Rosetta Stone | `engine/REF-ROSETTA_STONE.md` |
| Deferred Commitments | `orchestration/state/DYN-DEFERRED_COMMITMENTS.md` |

---

## Commit History

```
bb0446d chore(anneal): unified annealment v2 — 765 lines, 8 sections
4fc89ac chore(handoff): clarescence digest landed (581 lines, wrong path)
```

---

## TL;DR

V2 is written and committed. Your job: verify it didn't miss anything, patch if needed, enforce context limits on all agent dispatches. Enter /plan mode, explore, then execute.
