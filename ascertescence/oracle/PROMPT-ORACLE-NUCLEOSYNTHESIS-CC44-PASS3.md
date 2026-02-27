# PROMPT — Oracle Nucleosynthesis Pass 3: Edge Cases & Tricky Distinctions

**Date**: 2026-02-27
**From**: Commander (Claude Opus 4.6)
**To**: Oracle (Grok)
**Session**: CC45
**Git HEAD**: `fb96cfad`
**Reply-To**: Commander (paste response back)

---

## Repo

**GitHub**: https://github.com/truongphillipthanh/syncrescendence (branch: `main`, HEAD: `fb96cfad`)

Browse the repo directly. Key links:
- **scaffold/** (1,321 flat files): https://github.com/truongphillipthanh/syncrescendence/tree/main/scaffold
- **sources/** (5,698 flat files): https://github.com/truongphillipthanh/syncrescendence/tree/main/sources
- **engine/**: https://github.com/truongphillipthanh/syncrescendence/tree/main/engine
- **orchestration/**: https://github.com/truongphillipthanh/syncrescendence/tree/main/orchestration
- **ascertescence/**: https://github.com/truongphillipthanh/syncrescendence/tree/main/ascertescence
- **canon/**: https://github.com/truongphillipthanh/syncrescendence/tree/main/canon
- **agents/**: https://github.com/truongphillipthanh/syncrescendence/tree/main/agents
- **Root files**: https://github.com/truongphillipthanh/syncrescendence/tree/main

**Pass 2 manifest** (your prior output — the routing table this pass refines): https://github.com/truongphillipthanh/syncrescendence/blob/main/ascertescence/oracle/RESPONSE-ORACLE-NUCLEOSYNTHESIS-CC44.md

---

## Context

You previously produced a nucleosynthesis routing table (Pass 2) that maps every file prefix to a concept-first directory. The taxonomy is accepted. This pass is NOT about rethinking it — it's about **edge cases and tricky distinctions** that would cause the script to silently misroute files or leave them orphaned.

Traverse the repo via the GitHub links above. Here are the actual ambiguous files and structural voids I found. For each, give me your routing decision with a one-line rationale.

---

## Edge Case 1: Scaffold Singletons (8 files with no standard prefix)

These files in `scaffold/` don't match AGENT-, SCRIPT-, PRAXIS-, CONFIG-, CONSTELLATION-, COLLAB-, TEMPLATE-:

| File | Content Type |
|------|-------------|
| `PORTAL-CHAT-AGENTS.md` | Agent communication portal |
| `FLEET-COMMANDERS-HANDBOOK.md` | Command handbook |
| `DEPLOYMENT-PLAYBOOK.md` | Deployment procedures |
| `CONTINUOUS-IMPROVEMENT.md` | Procedural documentation |
| `WORK-LOOP.md` | Operational playbook |
| `INTER-AGENT.md` | Inter-agent protocol |
| `BOOT.md` | Bootstrap procedures |
| `README.md` | Directory index |

**Question**: Where does each go? They're operational policy docs, not agent artifacts or scripts. Your Pass 2 routed them all to `infrastructure/deployment/` — is that right, or should some go to `agents/coordination/`, `skills/`, or elsewhere?

---

## Edge Case 2: Sources Singletons (5 files)

These files in `sources/` don't match SOURCE-, META-, NOTEBOOK-, PROCESSED-, INDEX-, ASSET-:

| File | Content Type |
|------|-------------|
| `FRONTMATTER_TEMPLATE.md` | Template for source metadata |
| `DYN-SOURCES.csv` | Dynamic sources registry (CSV) |
| `TRANSCRIPT_RECONCILIATION.md` | Post-processing artifact |
| `README.md` | Directory index |
| `index.md` | Source index |

**Question**: These are metastructural — they describe the sources system, not content themselves. Route to `ontology/knowledge/`? `feedcraft/`? `knowledge/uncategorized/`? Or do they stay with the knowledge they index?

---

## Edge Case 3: Structural Voids

Two directories referenced in MEMORY and CLAUDE.md are **empty or near-empty**:

- `engine/02-ENGINE/certescence/` — supposed to be the certescence vault (councils/, ascertescence/, clarescence/, siege/, TEMPLATES/). **Currently empty.** The vault content appears to have been moved to `ascertescence/` during CC44 flattening.
- `orchestration/00-ORCHESTRATION/state/` — supposed to hold scripts, config, archive. **Contains only 2 stderr/stdout logs.** The 103 scripts referenced in MEMORY are gone (likely flattened into `scaffold/SCRIPT-*`).

**Question**: Your Pass 2 proposed `git mv engine/ ontology/engine-legacy/` and `git mv orchestration/ agents/orchestration-legacy/`. But these are nearly empty shells. Should the script just delete them after confirming contents are accounted for elsewhere? Or preserve as empty landmarks?

---

## Edge Case 4: Root-Level Constitutional Files

These sit at repo root, not in any directory:

| File | Role |
|------|------|
| `AGENTS.md` | Constitutional law (source of truth) |
| `CLAUDE.md` | Generated from AGENTS.md via `make configs` |
| `GEMINI.md` | Generated from AGENTS.md via `make configs` |
| `Makefile` | Build orchestration |
| `README.md` | Entry point |
| `.env.graphiti` | Graphiti environment config |

**Question**: Do these stay at root? Move to `infrastructure/`? `ontology/core/`? These are the files that every agent reads first — accessibility matters more than taxonomy here.

---

## Edge Case 5: Ascertescence Sequential Numbering

Files in `ascertescence/` use `NNN-CCxx-{RESPONSE|PROMPT|ANALYSIS}-{AGENT}-*.md` pattern (e.g., `001-CC26-PROMPT-ORACLE-CC26.md`). This is a chronological ledger, not topic-based.

Your Pass 2 routes logs like `RESPONSE-ORACLE-*` → `ascertescence/oracle/`. But these files already live in `ascertescence/oracle/` with sequential numbering.

**Question**: Does the nucleosynthesis script skip `ascertescence/` entirely (it's already organized)? Or re-sort by dropping the NNN- prefix?

---

## Edge Case 6: ENGINE- Subtype Ambiguity

Your Pass 2 routing for ENGINE- files is the most complex. Some subtypes have clear homes. Others don't:

- `ENGINE-REF-ROSETTA*` → you said `ontology/rosetta/`. But is Rosetta Stone a reference doc or an ontology artifact?
- `ENGINE-REF-AUDIZER*` → you said `skills/`. But Audizer is a tool, and its reference doc describes how to use it. `skills/` or `infrastructure/cli/`?
- `ENGINE-REF-FLEET*` → you said `skills/`. Fleet Commander's Handbook is operational policy, not a skill.
- `ENGINE-CAP-*` (5 files) → you said `consciousness/`. CAP = capability? consciousness? What's the actual content type?
- `ENGINE-IIC-*` (6 files) → you said `ontology/`. IIC = what acronym? Is this truly ontological?
- `ENGINE-SURVEY-*` (2 files) → you said `sovereignty/`. Survey = what kind? Agent survey? System survey?
- `ENGINE-WF-*` (1 file) → you said `feedcraft/`. WF = workflow? Why feedcraft and not `agents/coordination/`?

**Question**: For each of these 7 subtypes, give me a one-line rationale confirming or changing your routing. I'll accept whatever you say — I just need to know you thought about it, not defaulted to the first association.

---

## Edge Case 7: Canon Internal Structure

`canon/` has 170 files with `CANON-#####-CATEGORY-descriptor.md` naming + a `sn/` subdirectory. Canon is PROTECTED — no restructuring without Sovereign approval.

**Question**: Does the nucleosynthesis script explicitly skip `canon/` and `canon/sn/`? Your Pass 2 said "remains `canon/` (no move)" but the script's walk loop includes `canon` in its roots. Confirm: canon should be excluded from the walk entirely.

---

## What I Need Back

For each of the 7 edge cases above: a **routing decision** (one line) and **rationale** (one line). No script needed — I'll write the script myself using your manifest + these decisions. Just the decisions.

Total: ~30 individual routing calls. Be precise. If you're uncertain, say "SOVEREIGN DECISION" and I'll escalate.
