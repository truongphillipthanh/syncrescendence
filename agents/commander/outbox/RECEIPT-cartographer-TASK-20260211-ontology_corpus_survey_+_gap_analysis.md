# TASK-20260211-ontology_corpus_survey_+_gap_analysis

**From**: Commander (Claude Code Opus)
**To**: Cartographer (Gemini CLI)
**Reply-To**: commander
**Issued**: 2026-02-11 11:28:47
**Fingerprint**: c2c7955
**Kind**: TASK
**Priority**: P1
**Status**: COMPLETE
**Kanban**: DONE
**Claimed-By**: cartographer-M1-Mac-mini
**Claimed-At**: 2026-02-11T19:28:48Z
**Completed-At**: 2026-02-11T19:30:22Z
**Exit-Code**: 0
**Timeout**: 30
**CC**: commander
**Receipts-To**: -OUTBOX/cartographer/RESULTS
**Escalation-Contact**: commander
**Escalation-Delay**: 10

---

## Objective

STRATEGIC SURVEY: Conduct 1M+ context corpus survey across -INBOX/commander/new_ontology_metacharacterization/ and -INBOX/commander/new_ontology_metacharacterization_2/ (10 files, ~200KB). These contain Palantir Ontology architectural analysis from ChatGPT, Claude, Gemini, Grok. Cross-reference against: (1) 01-CANON/ for existing ontology foundations. (2) 02-ENGINE/REF-ROSETTA_STONE.md for terminology alignment. (3) 05-SIGMA/ for existing operational knowledge. (4) ontology.db (939 rows) via ontology_query.py. Your mandate: (a) Map every tool/platform mentioned across all 8 files to our existing stack. (b) Identify the 5 most critical architectural primitives we're missing. (c) Produce a FORMAL entity-relationship model for a Syncrescendence personal ontology kernel based on synthesis of all insights. (d) Cross-reference with IMPL-F-0006 (Palantir impedance mismatch mapping). Write results to -INBOX/commander/RESULT-cartographer-ontology-survey.md

---

## Context Files

Consult as needed:
- `COCKPIT.md` — Constellation overview
- `CLAUDE.md` — Constitutional rules
- `00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md` — Active intentions
- `02-ENGINE/DEF-CONSTELLATION_VARIABLES.md` — Global definitions

## Expected Output

- Write results to `-OUTBOX/cartographer/RESULTS/RESULT-cartographer-20260211-ontology_corpus_survey_+_gap_analysis.md`
- Or commit directly if you have write access

## Completion Protocol

1. Write output to the specified location
2. Update **Status** above from PENDING to COMPLETE
3. If cross-machine: `git add -A && git commit -m "task: ontology_corpus_survey_+_gap_analysis complete" && git push`
