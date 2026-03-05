# CC86 Owner Cutover Kit v1

**Date**: 2026-03-04  
**Status**: active  
**Class**: execution kit

## WAVE1_CONTROL_PLANE_KIT

### GitHub

Prechecks:

1. `syncrescendence@gmail.com` has accepted org invitation and 2FA enabled.
2. Current owner account can still access organization settings and billing.
3. Branch protection and Actions secrets inventory snapshot captured.

Promotion:

1. Org Settings -> People -> invite `syncrescendence@gmail.com` as owner.
2. Verify target owner can open: org settings, billing, Actions secrets, branch protection.
3. Transfer primary ownership authority to target owner.

Owner-only verification probes:

1. Create and delete a temporary org-level secret.
2. Change and restore a repo default setting (non-destructive).
3. Confirm owner can manage team permissions.

Rollback:

1. Re-promote legacy account to owner.
2. Revert owner transfer if any integration breaks.

Token/integration rotation scope:

1. rotate GH app/webhook secrets used by Slack/Discord/automation.
2. reauthorize `gh` CLI on control-plane account.

Evidence artifacts:

1. pointer note with timestamp + actor + setting screens touched.
2. owner verification checklist completion note.

Failure signatures and recovery:

1. missing billing access -> regrant owner and recheck org billing role.
2. Actions/webhook failures -> rotate app/webhook secret immediately and replay test event.

### Cloudflare

Prechecks:

1. target account invited to account with super-admin eligibility.
2. zone export pointer recorded.
3. API token inventory pointer recorded.

Promotion:

1. Account members -> grant `syncrescendence@gmail.com` super administrator.
2. Confirm target can access account settings, zone DNS, tunnels, tokens.

Owner-only verification probes:

1. create and delete a temporary DNS TXT record.
2. create and revoke a test-scoped API token.
3. verify tunnel management page access.

Rollback:

1. keep legacy super-admin active through stabilization window.
2. if outage occurs, legacy account restores prior zone/token state.

Token/integration rotation scope:

1. rotate cloudflared/wrangler tokens.
2. update any API tokens tied to legacy owner.

Evidence artifacts:

1. pointer note to member-role screen before/after.
2. DNS/token verification receipt.

Failure signatures and recovery:

1. DNS drift or stale cache -> restore record snapshot and purge cache.
2. tunnel auth failure -> reissue token and restart tunnel service.

### GCP / Google Cloud IAM

Prechecks:

1. project list exported.
2. IAM policy snapshot captured for each project/folder.
3. billing account access confirmed for target account.

Promotion:

1. grant `syncrescendence@gmail.com` owner (or equivalent admin) on org/folder/projects.
2. grant billing admin where required.
3. verify target account can view IAM, APIs, billing, service accounts.

Owner-only verification probes:

1. create and delete a temporary service account.
2. enable and disable a non-critical API on test project.
3. run IAM policy read/write check in console.

Rollback:

1. keep legacy owner roles until post-wave verification complete.
2. restore previous IAM bindings from snapshot if permission regressions appear.

Token/integration rotation scope:

1. rotate service-account keys and user OAuth tokens tied to legacy account.
2. refresh gcloud auth on operator machines with target identity.

Evidence artifacts:

1. per-project IAM change receipt.
2. billing-admin verification note.

Failure signatures and recovery:

1. permission denied on core project -> re-add legacy owner and diff IAM bindings.
2. billing lockout -> restore prior billing admin immediately.

## WAVE2_OPERATOR_BUS_KIT

### Slack

Prechecks:

1. workspace plan supports ownership transfer path in current tier.
2. app ownership and bot token inventory captured.
3. target account present in workspace with required role.

Promotion:

1. promote target to admin/owner.
2. if supported, transfer primary ownership.
3. rebind app ownership to target account where applicable.

Owner-only verification probes:

1. manage app settings and token regeneration.
2. modify and restore workspace-level policy setting.
3. confirm event subscription and socket mode controls.

Rollback:

1. legacy owner remains active during verification window.
2. if automation breaks, reassign app owner back temporarily and rotate tokens.

Token/integration rotation scope:

1. rotate bot token + app token.
2. update OpenClaw/channel secrets and callback endpoints.

Evidence artifacts:

1. workspace role transition pointer.
2. token rotation receipt (pointer only).

Failure signatures and recovery:

1. app disconnect/events failing -> rollback app owner, regenerate tokens, replay event probe.
2. ownership transfer blocked by plan -> hold wave and keep dual-admin mode.

### Discord

Prechecks:

1. target account added to server with admin rights.
2. developer application ownership path confirmed.
3. bot permissions and intents snapshot captured.

Promotion:

1. transfer server ownership to target account.
2. transfer developer team/app ownership if applicable.
3. confirm target can manage bot, intents, and webhooks.

Owner-only verification probes:

1. edit and restore server setting requiring owner-level privileges.
2. regenerate bot token and confirm controlled redeploy.

Rollback:

1. keep legacy owner in admin role until bot/runtime verified stable.
2. if failure, reverse ownership transfer and reissue token.

Token/integration rotation scope:

1. rotate bot token.
2. update runtime secrets and validate probe.

Evidence artifacts:

1. server ownership transition pointer.
2. bot token rotation receipt (pointer only).

Failure signatures and recovery:

1. bot offline/intents mismatch -> restore prior token/config and recheck gateway intents.
2. ownership transfer delay in team app -> hold cutover and keep dual-admin.

## MUTATION_ORDER_AND_HOLDS

1. GitHub -> hold for verification.
2. Cloudflare -> hold for DNS/tunnel verification.
3. GCP IAM -> hold for IAM/billing verification.
4. Slack -> hold for app/token verification.
5. Discord -> final wave hold.

Hold rule:

1. no next platform until current platform has:
   - owner-only probe pass
   - rollback test pass
   - evidence artifact filed

## SOVEREIGN_OPERATOR_CHECKLIST

1. Confirm MFA and recovery on target + break-glass identities.
2. Capture snapshots before every platform mutation.
3. Execute Wave 1 in order with holds.
4. Execute Wave 2 in order with holds.
5. Rotate tokens only after owner transfer verifies.
6. Keep legacy owner privileged until full wave verification completes.
7. Publish final cutover receipt with platform-by-platform evidence pointers.

## RISKS_AND_FAILURE_SIGNATURES

1. Hidden integration ownership coupling:
   - signature: owner transfer succeeds but automation fails within minutes.
   - action: immediate token/app ownership rollback on affected surface.
2. Billing authority drift:
   - signature: admin access present but invoices or plan controls blocked.
   - action: restore billing admin on prior owner, then recut with dual-admin validation.
3. Identity lockout:
   - signature: target owner loses console access due MFA/recovery mismatch.
   - action: use break-glass account, suspend further mutations, repair recovery chain first.
4. Multi-platform blast radius:
   - signature: concurrent failures across channels after parallel mutations.
   - action: stop all waves, roll back latest platform only, resume one-at-a-time sequencing.
