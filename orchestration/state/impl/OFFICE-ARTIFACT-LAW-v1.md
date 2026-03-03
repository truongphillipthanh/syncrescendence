# Office Artifact Law v1

## Purpose

Define the lawful local artifact classes that live inside offices before federal promotion.

This law is derived primarily from the predecessor commander office, where the strongest recurring local forms were:

- dispatch envelopes
- receipts
- results
- confirms
- alerts
- briefings
- execution logs

## Local Classes

### 1. Dispatch Envelope

Purpose:
- send actionable work from one office to another
- carry task identity, objective lock, receipt expectation, and return condition

Default local home:
- `outbox/dispatches/`

### 2. Receipt

Purpose:
- acknowledge claimed or completed execution with machine-readable operating metadata
- preserve who claimed the work, when, exit status, and return expectations

Default local home:
- `outbox/receipts/`

### 3. Result

Purpose:
- hold the substantive return from the work itself
- preserve findings, implementation result, synthesis, or inspection output

Default local home:
- `outbox/results/`

### 4. Confirm

Purpose:
- close the loop from the executing office back to the origin office
- confirm completion status and point to the result path

Default local home:
- receiving office `inbox/done/` or `inbox/active/` until resolved

### 5. Briefing

Purpose:
- provide high-priority orientation or executive read-in to an office

Default local home:
- receiving office `inbox/pending/` or executive briefings lane after promotion

### 6. Alert

Purpose:
- report urgent failure, degradation, or health risk

Default local home:
- receiving office `inbox/active/` or `inbox/done/` depending on handling state

### 7. Exec Log

Purpose:
- store raw mechanical trace, stdout/stderr, or unshaped execution detail

Default local home:
- `platform/logs/`

Exec logs are evidence, not verdicts.
They must not substitute for receipts or results.

## Promotion Law

These office-local classes promote when:

- a dispatch becomes durable prompt/packet lineage
- a result has federal communications value
- a confirm becomes part of a handoff or executive/program decision trail
- an alert affects federal runtime, executive, or program truth
- repeated local forms should harden into validated patterns or templates

## Anti-Patterns

Forbidden:

1. storing results only as raw logs
2. omitting receipt metadata while claiming completion
3. mixing confirm and result into one shapeless note when traceability matters
4. treating office-local dispatches as if they were already federal prompts
5. allowing local artifact names to drift until routing becomes guesswork
