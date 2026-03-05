# OPEN-QUESTIONS

**Project:** Syncrescendence Account Centralization — CC82
**Prepared:** 2026-03-05
**Status:** UNRESOLVED — these items block or materially impact cutover execution

---

## Overview

This document captures all unresolved questions and blocking unknowns that the operator team must resolve before or during the migration ceremony. Items are ordered by severity and urgency. Each item includes a description of the blocking condition, the impact if unresolved, and a recommended resolution path.

---

## OQ-001 — Slack App Inventory (BLOCKING for Wave 2)

**Description:** The full inventory of Slack apps created under `truongphillipthanh@icloud.com` has not been completed. Without this inventory, it is not possible to determine how many apps need to be recreated, which integrations will be disrupted, and what the total token rotation surface is.

**Impact if Unresolved:** Wave 2 (Slack App Ownership) cannot be executed. Downstream integrations that rely on Slack app tokens will break if apps are deactivated without a migration plan in place.

**Recommended Resolution:** The operator assigned to this track must log in to [api.slack.com/apps](https://api.slack.com/apps) as `truongphillipthanh@icloud.com` and export the complete list of apps. For each app, document: the app name, app ID, OAuth scopes, whether it uses token rotation, and all downstream consumers of its tokens. This inventory should be completed before Wave 2 is scheduled.

---

## OQ-002 — Discord Developer Team Ownership Lead Time (BLOCKING for Wave 2)

**Description:** The Discord developer team ownership transfer process requires a formal support request and dual-party consent within 30 days, with a total process duration of 30–60 days. [^1] This is the longest-lead-time item in the entire migration.

**Impact if Unresolved:** If this process is not initiated immediately, it will be the critical path item that delays the completion of the full migration. Any hard deadline for the migration must account for this 30–60 day window.

**Recommended Resolution:** Initiate the Discord Developer Support transfer request at [https://dis.gd/developer-support/teams-and-ownership](https://dis.gd/developer-support/teams-and-ownership) immediately, before any other wave is executed. Collect the App ID, Team ID, and new owner's User ID in advance. Ensure the `syncrescendence@gmail.com` Discord account is ready to respond to the consent request promptly.

---

## OQ-003 — Discord App Verification Loss (RISK for Wave 2)

**Description:** If the Syncrescendence Discord developer team owns any verified applications, those applications will lose their verified status during the ownership transfer process. The new owner must reapply for verification after the transfer. [^1]

**Impact if Unresolved:** Verified apps may have elevated API rate limits, access to privileged intents (e.g., Message Content Intent), or trust indicators visible to users. Loss of verification could disrupt bot functionality or user trust during the re-verification period.

**Recommended Resolution:** Determine whether any Discord apps are currently verified. If so, prepare the re-verification documentation (identity verification via Stripe Identity) in advance. Plan the transfer to occur during a low-traffic period. Communicate any expected disruption to users in advance.

---

## OQ-004 — Notion Private Content Inventory (RISK for Wave 4)

**Description:** Notion accounts can contain private pages and databases that are not shared with any workspace. If the `truongphillipthanh@icloud.com` Notion account is deprovisioned or its email is changed, private content owned by that account may become inaccessible if not properly handled.

**Impact if Unresolved:** Private Notion content could be lost or become inaccessible if the account migration is not handled carefully.

**Recommended Resolution:** Before executing the Notion email change, the operator must audit all private pages and databases under `truongphillipthanh@icloud.com`. Any content that needs to be preserved should be moved to a shared workspace or explicitly shared with `syncrescendence@gmail.com` before the email change is executed. The recommended migration path (changing the email on the existing account rather than creating a new account) preserves all content, but this must be verified.

---

## OQ-005 — Cloudflare Registrar Inter-Account Transfer Process (RISK for Wave 1)

**Description:** If any Syncrescendence domains are registered through Cloudflare Registrar (as opposed to a third-party registrar), the domain migration process is different from the standard nameserver-update flow. Cloudflare Registrar domains require a separate inter-account domain registration transfer process that involves both the source and destination accounts confirming the transfer. [^2]

**Impact if Unresolved:** Attempting to use the standard nameserver-update flow for a Cloudflare Registrar domain will fail. The domain will remain associated with the legacy account.

**Recommended Resolution:** Confirm whether any Syncrescendence domains are registered through Cloudflare Registrar. If so, refer to the Cloudflare Registrar inter-account transfer documentation and follow that process instead of the standard zone migration flow.

---

## OQ-006 — Airtable Enterprise Plan Requirement (RISK for Wave 4)

**Description:** The Airtable admin panel workspace ownership transfer feature (which allows bulk workspace ownership transfer) is only available on the **Enterprise plan**. [^3] If Syncrescendence is on a lower-tier Airtable plan, workspace ownership transfer must be performed on a per-base basis, which may be significantly more time-consuming.

**Impact if Unresolved:** If not on Enterprise, the operator team must manually transfer ownership of each base individually, which could be a significant manual burden depending on the number of bases.

**Recommended Resolution:** Confirm the current Airtable plan tier. If not on Enterprise, enumerate all bases and plan for per-base ownership transfer. Evaluate whether a temporary upgrade to Enterprise is warranted to simplify the migration.

---

## OQ-007 — Basecamp Primary Owner Transfer Self-Service Path (RISK for Wave 4)

**Description:** Basecamp's documentation for transferring primary account ownership is not as clearly documented as other platforms. The self-service path for designating a new primary account owner may require contacting Basecamp support.

**Impact if Unresolved:** The operator team may encounter an unexpected manual step or support ticket process when attempting to transfer Basecamp account ownership.

**Recommended Resolution:** Before scheduling the Basecamp migration, contact Basecamp support to confirm the exact process for transferring primary account ownership from `truongphillipthanh@icloud.com` to `syncrescendence@gmail.com`. Document the confirmed process before execution.

---

## OQ-008 — API Key and Secret Rotation Scope (CROSS-CUTTING)

**Description:** While this runbook explicitly does not handle credentials, a comprehensive migration must account for the rotation of all API keys, OAuth tokens, bot tokens, and other secrets that are currently associated with `truongphillipthanh@icloud.com` across all platforms. The scope of this rotation has not been inventoried.

**Impact if Unresolved:** After ownership transfer, secrets associated with the legacy account may continue to function temporarily but will eventually expire or be revoked, causing silent failures in production systems.

**Recommended Resolution:** As a parallel workstream to this migration, the operator team should conduct a full secrets audit across all platforms and CI/CD systems. Identify every secret tied to `truongphillipthanh@icloud.com`, document all downstream consumers, and plan a coordinated rotation after each ownership transfer is complete. This workstream should be tracked in the CC81 tracker as a separate but dependent item.

---

## OQ-009 — Two-Factor Authentication on Legacy Account (PRECONDITION)

**Description:** Several platforms (including GitHub and Slack) require the current owner to authenticate with their password or 2FA device to confirm ownership transfers. If `truongphillipthanh@icloud.com` has lost access to their 2FA device or recovery codes, the ownership transfer process may be blocked.

**Impact if Unresolved:** Ownership transfers on platforms that require password/2FA confirmation cannot be completed without resolving the authentication issue first.

**Recommended Resolution:** Before scheduling any migration wave, confirm that `truongphillipthanh@icloud.com` has active access to their account on each platform, including 2FA. If access is lost on any platform, initiate the platform's account recovery process before the migration ceremony.

---

## References

[^1]: [How to Transfer Ownership of a Developer Team — Discord Developer Support](https://support-dev.discord.com/hc/en-us/articles/34905402845591-How-to-Transfer-Ownership-of-a-Developer-Team)
[^2]: [Move a domain between Cloudflare accounts — Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/manage-domains/move-domain/)
[^3]: [Transferring Airtable workspace, base, and interface ownership — Airtable Support](https://support.airtable.com/docs/transferring-airtable-workspace-base-and-interface-ownership)
