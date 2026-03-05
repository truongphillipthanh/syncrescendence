# CC82 Exocortex Account Centralization Execution Plan v1

**Date**: 2026-03-04  
**Status**: active  
**Class**: execution plan

## Objective

Move operational ownership of the exocortex and control-plane surfaces from legacy account-1 ownership (`truongphillipthanh@icloud.com`) to:

`syncrescendence@gmail.com`

without service interruption, data loss, or irreversible lockout.

## Operating Assumptions

1. Owner/billing mutations are human-confirmed operations.
2. Commander can automate evidence capture, checklist generation, and tracker updates.
3. Manus can generate and refine migration procedures but cannot perform tenant owner mutations directly.
4. Legacy account remains break-glass until each surface reaches post-cutover verification.

## Wave Schedule (execution order)

## Wave 0: Security + Snapshot Gate

Preconditions:
- target account MFA and recovery methods validated
- break-glass access validated
- token/integration inventory frozen

Actions:
1. Run phase-0 gates in [CC81-PHASE0-GATE-CHECKLIST.md](/Users/system/syncrescendence/orchestration/state/impl/CC81-PHASE0-GATE-CHECKLIST.md).
2. Capture snapshot receipts for all target surfaces.
3. Mark tracker and ledger rows as `snapshot_done`.

Rollback:
- no ownership mutation has occurred yet; rollback is immediate by aborting wave.

## Wave 1: Code + Edge Control Plane

Surfaces:
- GitHub
- Cloudflare/domain
- GCP IAM/project owner state

Mutation pattern per surface:
1. Add `syncrescendence@gmail.com` as top-tier admin/owner.
2. Verify owner-only action from target account.
3. Keep legacy owner active during stabilization window.

Rollback pattern:
1. Reassert legacy owner as primary.
2. Revert billing/contact owner metadata.
3. Validate CI/deploy path and DNS authority before closing rollback window.

## Wave 2: Operator Bus Cutover

Surfaces:
- Slack
- Discord

Mutation pattern per surface:
1. Promote target account to owner/admin equivalent.
2. Transfer app/bot ownership or maintainership.
3. Rotate app/bot tokens and webhook secrets to target-account-controlled vault.
4. Rebind automations and verify runtime message flow.

Rollback pattern:
1. Temporarily restore legacy app credentials.
2. Restore legacy owner/admin privileges if target-account execution fails.
3. Keep channel/service continuity before retrying mutation.

## Wave 3: Exocortex SaaS Surfaces

Surfaces:
- Notion
- Coda
- Confluence
- Jira
- Linear
- ClickUp
- Basecamp
- Airtable

Mutation pattern per surface:
1. Grant target account equivalent owner/admin role.
2. Validate owner-only function and API/integration posture.
3. Rotate service tokens/personal access tokens away from legacy account.

Rollback pattern:
1. Reinstate legacy account as active owner/admin.
2. Revert integration tokens if necessary.
3. Re-run post-change access checks.

## Wave 4: Legacy Primacy Decommission

Preconditions:
- all previous waves verified
- all integrations running under target-account authority
- explicit executive approval recorded

Actions:
1. Demote legacy account to break-glass only.
2. Revoke stale legacy-bound tokens.
3. Publish final receipt package for cutover closure.

Rollback:
- reopen legacy owner/admin where platform supports reversible demotion.

## Surface Execution Matrix

| Surface | Mutation executor | Automation support | Status |
|---|---|---|---|
| GitHub | human | commander/manus checklist + evidence automation | queued |
| Cloudflare | human | commander evidence automation | queued |
| GCP | human | commander cli verification | queued |
| Slack | human | commander/manus checklist + token rotation plan | queued |
| Discord | human | commander/manus checklist + token rotation plan | queued |
| Notion | human | manus checklist | queued |
| Coda | human | manus checklist | queued |
| Confluence/Jira | human | manus checklist | queued |
| Linear | human | commander/manus checklist | queued |
| ClickUp | human | manus checklist | queued |
| Basecamp | human | manus checklist | queued |
| Airtable | human | commander/manus checklist | queued |

## Required Human Action Windows

1. Tenant logins with `syncrescendence@gmail.com`.
2. Owner-role acceptance/confirmation flows in each platform UI.
3. Billing/contact owner confirmation where API coverage is incomplete.
4. Slack/Discord app token regeneration after ownership changes.

## Evidence Artifacts

1. Tracker:
   - [IDENTITY-CUTOVER-TRACKER-CC81.json](/Users/system/syncrescendence/orchestration/state/IDENTITY-CUTOVER-TRACKER-CC81.json)
2. Machine-readable surface ledger:
   - [EXOCORTEX-CENTRALIZATION-LEDGER-CC82.json](/Users/system/syncrescendence/orchestration/state/EXOCORTEX-CENTRALIZATION-LEDGER-CC82.json)
3. Dispatch log:
   - [LOG-CC82-wake-loop-and-centralization-dispatch.md](/Users/system/syncrescendence/communications/logs/LOG-CC82-wake-loop-and-centralization-dispatch.md)

## Blocking Conditions

1. Missing snapshot evidence for any surface.
2. Missing target-account owner/admin role in a platform.
3. Unverified token rotation for Slack/Discord/automation paths.
4. Any rollback path not explicitly documented before mutation.

## Active Blocking Questions (from Manus CC82)

1. Slack app inventory is incomplete; cannot safely execute Slack app/token migration without full dependency map.
2. Discord developer-team ownership transfer has long lead time (30-60 days); this is the critical-path item and should be initiated immediately.
3. Cloudflare registrar flow may differ if domains are registered directly in Cloudflare Registrar.
4. Secrets rotation scope across integrations is still incomplete and must run as a parallel workstream.
