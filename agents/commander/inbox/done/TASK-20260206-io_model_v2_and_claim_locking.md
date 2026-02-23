# TASK-20260206-io_model_v2_and_claim_locking

**From**: Psyche
**To**: Commander
**Issued**: 2026-02-06
**Priority**: P0
**Status**: COMPLETE

---

## Objective

Amend the IO model so it supports “always-on, low-micromanagement” operation without duplicate consumers, while preserving -OUTGOING’s narrow purpose.

This task is a companion to:
- `TASK-20260206-outgoing-bypass-question.md`

---

## Sovereign Clarification (authoritative)

**A) Agent→Agent = -INBOX (direct delivery)**
- Ajna results for Psyche → write to `-INBOX/psyche/` (not -OUTGOING)
- Psyche tasks for Ajna → write to `-INBOX/ajna/`

**B) Agent→Web = -OUTGOING (PROMPT-* only)**
We will standardize web-relay prompt naming as:
- `-OUTGOING/PROMPT-ORACLE-*.md` (Grok)
- `-OUTGOING/PROMPT-AUGUR-*.md` (Perplexity)
- `-OUTGOING/PROMPT-VIZIER-*.md` (Claude Web)
- `-OUTGOING/PROMPT-VANGUARD-*.md` (ChatGPT Web)
- `-OUTGOING/PROMPT-DIVINER-*.md` (Gemini Web)

This is the official answer to “why not bypass -OUTGOING altogether?”
- We *do* bypass it for agent→agent.
- We *keep* it for web relay.

**C) Global Ledger = both task lifecycle + Sovereign decisions**
We want a global ledger layer that reduces Phillip’s double-relay burden.
Track:
- dispatch/claim/complete events
- **DecisionAtoms** and (when present) **IntentionLink** references

---

## Required decisions + implementation

### 1) IO Model v2 docs (P0)
Update docs to reflect the clarified IO model:
- `-INBOX/README.md`
- `-OUTGOING/README.md`

### 2) Add claim-locking to prevent duplicate processing (P0)

Update `00-ORCHESTRATION/scripts/watch_dispatch.sh` claim step to be atomic.

Recommended mechanism:
- watcher atomically renames the file when claiming:
  - `TASK-xxxx.md` → `TASK-xxxx.md.claimed-by-{agent}-{hostname}`
- only the claimer proceeds
- on completion:
  - rename to `.complete` (or restore name and mark Status: COMPLETE)

### 3) Add global ledger (P0)
Create:
- `00-ORCHESTRATION/state/DYN-GLOBAL_LEDGER.md` (append-only)

Create script:
- `00-ORCHESTRATION/scripts/append_ledger.sh`

Integrate ledger append in:
- `00-ORCHESTRATION/scripts/dispatch.sh` (on dispatch)
- `watch_dispatch.sh` (on claim + on completion)

Ledger entry schema (suggested):
- timestamp (ISO)
- event: DISPATCH|CLAIM|COMPLETE|DECISION
- from/to
- task id
- fingerprint
- commit hash (if any)
- DecisionAtom (optional)
- IntentionLink (optional)

### 4) Add triage script for self-inbox (P1)

Add `00-ORCHESTRATION/scripts/triage_inbox.sh <agent>`
- lists PENDING/IN_PROGRESS
- highlights stale IN_PROGRESS > N minutes

### 5) Re-home legacy non-PROMPT artifacts in -OUTGOING (P1)

`-OUTGOING/` currently contains non-PROMPT artifacts:
- `20260202-corpus-survey/…`
- `forensic-audit-type-theory/…`

Option 1 (recommended): move to `04-SOURCES/research/` or `00-ORCHESTRATION/archive/` and leave stub notes.
Option 2: explicitly exempt these as “REPORT-*” artifacts in README.

---

## Expected Output

1) A commit implementing IO Model v2 docs + claim-locking + global ledger (or a staged patch plan if you want Sovereign approval first).
2) A short result note indicating:
   - where ledger lives
   - how DecisionAtoms are captured
   - how -OUTGOING is now constrained to PROMPT-* web relay
