# EXOCORTEX-SUITE-CUTOVER

**Project:** Syncrescendence Account Centralization — CC82
**Scope:** Notion, Coda, Confluence, Jira, Linear, ClickUp, Basecamp, Airtable
**Prepared:** 2026-03-05

---

## Overview

This document provides the detailed cutover procedure for the exocortex suite — the knowledge management, project management, and collaborative intelligence platforms that form the Syncrescendence operational brain. Each platform section follows the structure: **Preconditions → Owner Mutation → Post-Verification → Rollback**.

These migrations are generally lower-risk than the infrastructure and communication layers (Waves 1–3) and can be executed in parallel with each other. However, they should be executed after Wave 3 (Google Workspace) is complete, as some platforms may use Google SSO tied to the legacy account.

---

## 1. Notion

Notion's recommended migration path for account ownership transfer is to change the email address on the existing account, rather than creating a new account and migrating content. This preserves all workspace memberships, page ownership, and database access without requiring any content migration. [^1]

**Preconditions**

Confirm that `syncrescendence@gmail.com` is not already associated with an existing Notion account. If it is, that account must be deleted or its email changed to a different address first to free up the target email. Audit all private pages and databases under `truongphillipthanh@icloud.com` and ensure all content that needs to be preserved is either in a shared workspace or explicitly shared with another account before proceeding (see OQ-004).

**Owner Mutation Step**

1. Log in to Notion as `truongphillipthanh@icloud.com`.
2. Navigate to **Settings → My Account**.
3. Under **Account security**, click **Change email**.
4. Enter `syncrescendence@gmail.com` as the new email address.
5. Click **Send verification code**. A code will be sent to `syncrescendence@gmail.com`.
6. Enter the verification code to confirm the change. [^1]

**Post-Verification Step**

Log out and log back in to Notion using `syncrescendence@gmail.com`. Confirm that all workspaces, pages, and databases previously accessible under `truongphillipthanh@icloud.com` are still accessible. Confirm that the account is listed as the workspace owner in **Settings → Members**.

**Rollback Step**

Repeat the email change process to revert to `truongphillipthanh@icloud.com`.

---

## 2. Coda

Coda supports per-document ownership transfer. Workspace-level ownership may require admin panel access or support contact.

**Preconditions**

Confirm that `syncrescendence@gmail.com` has a Coda account and is a **Doc Maker** in the destination workspace. [^2] Enumerate all docs owned by `truongphillipthanh@icloud.com` that need to be transferred.

**Owner Mutation Step — Per-Document Transfer**

For each doc owned by `truongphillipthanh@icloud.com`:

1. Open the doc in Coda.
2. Click the **Share** button in the top right.
3. Locate `syncrescendence@gmail.com` in the collaborators list (add as a Doc Maker if not present).
4. Click the role dropdown next to `syncrescendence@gmail.com` and select **Make Owner**. [^2]
5. Confirm the ownership change in the dialog box.

**Owner Mutation Step — Workspace Offboarding**

If `truongphillipthanh@icloud.com` is being removed from the workspace, use Coda's workspace offboarding feature to reassign ownership of all their docs to `syncrescendence@gmail.com` in bulk. Navigate to **Workspace Settings → Members**, locate the legacy account, and use the **Remove member** flow, which includes an option to reassign all owned docs. [^3]

**Post-Verification Step**

Confirm that `syncrescendence@gmail.com` is listed as the owner of all transferred docs. Verify that all doc functionality, automations, and integrations are intact.

**Rollback Step**

Repeat the Make Owner process to revert doc ownership to `truongphillipthanh@icloud.com`.

---

## 3. Confluence and Jira (Atlassian)

Confluence and Jira are managed under a single Atlassian organization. Transferring organization admin rights covers both products simultaneously.

**Preconditions**

`syncrescendence@gmail.com` must have an Atlassian account and be a managed user within the organization. The current organization admin must be logged in to [admin.atlassian.com](https://admin.atlassian.com).

**Owner Mutation Step**

1. Log in to [admin.atlassian.com](https://admin.atlassian.com) as `truongphillipthanh@icloud.com`.
2. Select the organization. Navigate to **Directory → Users**.
3. Search for and select the `syncrescendence@gmail.com` user to open their profile.
4. Click the more actions menu (•••) and select **Assign org admin role**. [^4]
5. Log in as `syncrescendence@gmail.com` and confirm organization admin access.
6. Optionally, remove the org admin role from `truongphillipthanh@icloud.com` via the same interface.

> **If the current admin is unavailable:** Contact Atlassian Support to initiate a role transfer process. The current admin will be contacted for approval; if there is no response within three days, the role transfer can proceed after identity verification. [^4]

**Post-Verification Step**

Log in as `syncrescendence@gmail.com` and confirm full access to all Jira projects and Confluence spaces via the Atlassian Admin console. Verify billing access and subscription management.

**Rollback Step**

Assign the org admin role back to `truongphillipthanh@icloud.com` using the same process.

---

## 4. Linear

**Preconditions**

`syncrescendence@gmail.com` must be a member of the Linear workspace. The current workspace owner must be logged in.

**Owner Mutation Step**

1. Log in to Linear as `truongphillipthanh@icloud.com`.
2. Navigate to **Settings → Members**.
3. Locate `syncrescendence@gmail.com` in the member list (invite if not present).
4. Click the role dropdown next to the account and select **Workspace Owner**. [^5]
5. Confirm the transfer. The previous owner's role will be downgraded to Admin.

**Post-Verification Step**

Log in as `syncrescendence@gmail.com` and confirm Workspace Owner access, including the ability to manage billing, settings, and all teams.

**Rollback Step**

Transfer workspace ownership back to `truongphillipthanh@icloud.com` from the Settings → Members panel.

---

## 5. ClickUp

**Preconditions**

`syncrescendence@gmail.com` must be a member of the ClickUp workspace. The current workspace owner must be logged in.

**Owner Mutation Step**

1. Log in to ClickUp as `truongphillipthanh@icloud.com`.
2. Navigate to **Settings → People**.
3. Locate `syncrescendence@gmail.com` in the member list (invite if not present).
4. Click the role dropdown next to the account and select **Transfer Ownership**. [^6]
5. Confirm the transfer. The previous owner becomes an Admin.

**Post-Verification Step**

Log in as `syncrescendence@gmail.com` and confirm Workspace Owner access, including billing and workspace settings.

**Rollback Step**

Transfer workspace ownership back to `truongphillipthanh@icloud.com` using the same Settings → People flow.

---

## 6. Basecamp

**Preconditions**

`syncrescendence@gmail.com` must have a Basecamp account. The current account owner must be logged in. Contact Basecamp support in advance to confirm the exact self-service path for primary account owner transfer (see OQ-007).

**Owner Mutation Step**

1. Log in to Basecamp as `truongphillipthanh@icloud.com`.
2. Navigate to **Account Settings → Administrators**.
3. Add `syncrescendence@gmail.com` as an Administrator.
4. Follow the confirmed process from Basecamp support to designate `syncrescendence@gmail.com` as the primary account owner. This may involve a support-mediated transfer.

**Post-Verification Step**

Log in as `syncrescendence@gmail.com` and confirm full account owner access, including billing and the ability to manage all projects and users.

**Rollback Step**

Revert the account owner designation back to `truongphillipthanh@icloud.com` via the same process or via Basecamp support.

---

## 7. Airtable

**Preconditions**

`syncrescendence@gmail.com` must have an Airtable account and be a member of the workspace. Confirm the current Airtable plan tier (see OQ-006). If on Enterprise, the admin panel workspace ownership transfer is available. If not on Enterprise, per-base ownership transfer is required.

**Owner Mutation Step — Enterprise Plan (Workspace)**

1. Log in to Airtable as the Enterprise admin.
2. Navigate to the **Admin Panel → Workspaces tab**.
3. Locate the Syncrescendence workspace and use the ownership transfer option to assign `syncrescendence@gmail.com` as the new workspace owner. [^7]

**Owner Mutation Step — All Plans (Per-Base)**

For each base owned by `truongphillipthanh@icloud.com`:

1. Open the base in Airtable.
2. Navigate to **Share → Collaborators**.
3. Locate `syncrescendence@gmail.com` (add as a Creator if not present).
4. Use the ownership transfer option to assign `syncrescendence@gmail.com` as the new base owner.

**Post-Verification Step**

Confirm that `syncrescendence@gmail.com` is listed as the owner of all workspaces and bases. Verify that all automations, interfaces, and integrations are intact.

**Rollback Step**

Repeat the ownership transfer process to revert to `truongphillipthanh@icloud.com`.

---

## References

[^1]: [Account settings & preferences — Notion Help Center](https://www.notion.com/help/account-settings)
[^2]: [Change ownership of your Coda doc — Coda Help](https://help.coda.io/hc/en-us/articles/39555803168013-Change-ownership-of-your-Coda-doc)
[^3]: [Remove workspace members and manage their docs — Coda Help](https://help.coda.io/hc/en-us/articles/39555830839053-Remove-workspace-members-and-manage-their-docs)
[^4]: [Give users admin permissions — Atlassian Support](https://support.atlassian.com/user-management/docs/give-users-admin-permissions/)
[^5]: [Members and roles — Linear Docs](https://linear.app/docs/members-roles)
[^6]: [Transfer Workspace ownership — ClickUp Help](https://help.clickup.com/hc/en-us/articles/6310482663063-Transfer-Workspace-ownership)
[^7]: [Transferring Airtable workspace, base, and interface ownership — Airtable Support](https://support.airtable.com/docs/transferring-airtable-workspace-base-and-interface-ownership)
