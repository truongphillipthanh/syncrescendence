# TASK: MODEL-INDEX Refresh Template

**Priority**: P1
**Reply-To**: commander
**CC**: commander
**Created**: 2026-02-09

## Objective
Create a cron-ready refresh script that scans frontier AI model releases and updates:
1. `02-ENGINE/REF-MODEL_INDEX.md` — model capabilities, pricing, context windows
2. `02-ENGINE/DYN-PLATFORMS.md` — platform status changes
3. `05-SIGMA/SURVEY-AI_ECOSYSTEM.md` — ecosystem landscape

## Approach
1. Web search for latest model releases from: Anthropic, OpenAI, Google, Meta, Mistral, Alibaba
2. Compare against current MODEL-INDEX entries
3. Flag entries older than 48 hours as STALE
4. Update with new data, add `last_verified: YYYY-MM-DD` timestamp
5. Output a diff summary for Sovereign review

## Deliverables
- [ ] Updated MODEL-INDEX with current data
- [ ] Diff summary of what changed
- [ ] Script template (bash) for future automated runs
- [ ] `last_verified` timestamps on all entries

## Context
Part of the Live Ledger Infrastructure (SYN-31). Data hours old is irrelevant at current model velocity. This is the first step toward self-correcting corpus.
