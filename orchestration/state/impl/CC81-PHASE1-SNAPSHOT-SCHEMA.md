# CC81 Phase 1 Snapshot Schema

**Date**: 2026-03-04  
**Status**: active  
**Class**: evidence schema

## Purpose

Normalize pre-cutover snapshots so rollback and verification are deterministic.

## Snapshot Requirements (all platforms)

1. Membership and role baseline.
2. Ownership and billing/contact baseline.
3. Integration/app/token pointer inventory.
4. Current access verification for target and legacy identities.
5. Rollback operator identity and rollback window.

## Required JSON Shape

Use:
- [IDENTITY-CUTOVER-EVIDENCE-RECEIPT-TEMPLATE-CC81.json](/Users/system/syncrescendence/orchestration/state/IDENTITY-CUTOVER-EVIDENCE-RECEIPT-TEMPLATE-CC81.json)

Core fields:
- `cutover_id`
- `platform`
- `captured_at`
- `captured_by`
- `target_identity`
- `legacy_identity`
- `baseline.membership_roles`
- `baseline.ownership_billing`
- `baseline.integrations`
- `baseline.access_validation`
- `rollback`
- `evidence_links`

## Platform-Specific Additions

### GitHub

- org members + roles
- teams and repository permissions
- billing contact pointer

### Cloudflare

- super-admin roster
- DNS export pointer
- zone account mapping

### Google Workspace + GCP

- super-admin list
- project IAM owner bindings
- billing account linkage

### Slack + Discord

- owner/admin identities
- app/bot ownership pointers
- integration dependency notes

### Exocortex suite

- workspace owners/admins
- automation/integration pointers
- owner-only action validation pointer

## Gate to Mutation

No ownership mutation is authorized unless snapshot receipt exists for that platform and validates against this schema.
