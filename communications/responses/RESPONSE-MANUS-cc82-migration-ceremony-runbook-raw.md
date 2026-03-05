# MIGRATION-CEREMONY-RUNBOOK

**Project:** Syncrescendence Account Centralization — CC82
**From:** `truongphillipthanh@icloud.com` (legacy surface)
**To:** `syncrescendence@gmail.com` (control plane)
**Prepared:** 2026-03-05
**Status:** READY FOR EXECUTION

---

## Overview

This runbook governs the wave-by-wave transfer of operational ownership across all Syncrescendence platform surfaces. Each wave is designed to be independently executable and reversible. Waves must be executed in order, as later waves may depend on infrastructure established in earlier ones. Each step follows the pattern: **Preconditions → Owner Mutation → Post-Verification → Rollback**.

> **Constraint:** No destructive actions are permitted. No credentials are handled in this runbook. All steps are reversible. Every step references official documentation.

---

## Wave 1 — Core Infrastructure (GitHub + Cloudflare)

Wave 1 establishes the foundational infrastructure layer. GitHub controls source code and CI/CD pipelines; Cloudflare controls DNS authority and network edge. These must be migrated first, as downstream services may depend on them.

### 1.1 GitHub Organization Ownership

**Preconditions**

The `syncrescendence@gmail.com` account must already exist on GitHub.com and must already be an active member of the Syncrescendence organization. The current owner (`truongphillipthanh@icloud.com`) must be logged in and able to access **Organization Settings**. Confirm that no pending organization invitations are blocking the role change.

**Owner Mutation Step**

Step 1: From the `truongphillipthanh@icloud.com` account, navigate to the organization on GitHub.com. Select **Settings → Members** and locate the `syncrescendence@gmail.com` account. Assign the **Owner** role to that account. [^1]

Step 2: Log in as `syncrescendence@gmail.com` and confirm access to **Organization Settings**.

Step 3: As `syncrescendence@gmail.com`, navigate to **Settings → Billing & plans** and update the payment method and billing contact email to `syncrescendence@gmail.com`. [^1]

> **Warning (from GitHub docs):** Removing yourself from the organization does **not** update billing information. The new owner or a billing manager must update billing information separately to remove the old payment method.

Step 4: From the `truongphillipthanh@icloud.com` account, navigate to **Organization Settings → Members** and select **Leave organization** to remove the legacy account.

**Post-Verification Step**

Confirm that `syncrescendence@gmail.com` is the sole account with the **Owner** role. Navigate to **Settings → Billing** and verify the billing email and payment method reflect the new owner. Attempt to access a private repository and create a test team to validate permissions.

**Rollback Step**

If the transfer fails or produces an unacceptable state, the new owner (`syncrescendence@gmail.com`) can re-invite `truongphillipthanh@icloud.com` and assign the Owner role. The original owner can then update billing information back to the original payment method and the new owner can leave the organization.

---

### 1.2 GitHub Repository Ownership (Individual Repos)

If any repositories are owned by the personal account `truongphillipthanh@icloud.com` rather than the organization, each must be transferred individually.

**Preconditions**

Enumerate all repositories owned by `truongphillipthanh@icloud.com` that need to be transferred to the organization or to `syncrescendence@gmail.com`.

**Owner Mutation Step**

For each repository: navigate to **Repository Settings → General → Danger Zone → Transfer**. Enter the repository name to confirm, then specify the destination organization or account. [^1]

**Post-Verification Step**

Confirm the repository appears in the destination organization's repository list. Verify all collaborators, branch protections, and webhooks are intact.

**Rollback Step**

The repository can be transferred back to the original account using the same Danger Zone transfer flow.

---

### 1.3 Cloudflare Domain Authority

Cloudflare does not support direct account ownership transfer. The migration path is to move each domain (zone) from the legacy account to the new account. [^2]

**Preconditions**

A Cloudflare account must exist for `syncrescendence@gmail.com`. Export a full DNS record snapshot from the legacy account for each domain (use the **Export** button in the DNS settings, or the Cloudflare API). Confirm access to the upstream domain registrar.

**Owner Mutation Step**

Step 1: In the `syncrescendence@gmail.com` Cloudflare account, click **Add a Site** and enter the domain name. Follow the onboarding wizard.

Step 2: Cloudflare will provide two new nameserver hostnames. Log in to the domain registrar and update the nameserver records to point to these new Cloudflare nameservers.

Step 3: In the new Cloudflare account, navigate to the domain's **Overview** tab and click **Re-check now** to trigger nameserver verification.

Step 4: Manually recreate all DNS records in the new zone using the previously exported snapshot. [^2]

> **Note:** If the domain is registered through Cloudflare Registrar, a separate inter-account domain registration transfer process applies. Refer to the Cloudflare Registrar inter-account transfer documentation.

**Post-Verification Step**

Confirm the domain status changes to **Active** in the new account. Issue new SSL/TLS certificates (Universal SSL will provision automatically once the zone is active). Verify DNS propagation using a tool such as `dig` or dnschecker.org. Confirm that the legacy account shows the domain as **Moved Away**.

**Rollback Step**

Revert the nameserver records at the registrar to the original Cloudflare nameservers from the legacy account. The domain will reactivate in the legacy account once nameserver propagation completes.

---

## Wave 2 — Communication Platforms (Slack + Discord)

Wave 2 migrates the communication layer. These platforms are operationally critical but do not block infrastructure. Slack and Discord ownership transfers are independent of each other and can be executed in parallel.

### 2.1 Slack Workspace Primary Ownership

**Preconditions**

`syncrescendence@gmail.com` must already be a full member of the Slack workspace (not a guest). The current Primary Owner (`truongphillipthanh@icloud.com`) must be logged in and able to access workspace administration. Confirm the new owner's email address is verified in Slack.

**Owner Mutation Step**

Step 1: As `truongphillipthanh@icloud.com`, navigate to the **Transfer Ownership** page (accessible via **Admin → Settings → Transfer Ownership** or directly at `https://{workspace}.slack.com/admin/transferOwnership`). [^3]

Step 2: Search for and select `syncrescendence@gmail.com` as the new Primary Owner.

Step 3: Enter the current owner's password to confirm the transfer and click **Transfer Workspace Ownership**.

> The transfer is immediate. The current Primary Owner's role will change to **Owner** (not Primary Owner).

**Post-Verification Step**

Log in as `syncrescendence@gmail.com` and navigate to **Admin → Settings** to confirm the Primary Owner role. Navigate to **Admin → Billing** and update the billing contact and payment method to the new owner. Verify that the old account now shows the **Owner** role (not Primary Owner).

**Rollback Step**

The new Primary Owner (`syncrescendence@gmail.com`) can navigate to the Transfer Ownership page and transfer the role back to `truongphillipthanh@icloud.com`. [^3]

---

### 2.2 Slack App Ownership and Token Lifecycle

Slack does not support direct app ownership transfer between accounts. The migration path depends on whether the app is a workspace app or an org-level app.

**Preconditions**

Enumerate all Slack apps installed in the workspace. For each app, determine whether it was created under `truongphillipthanh@icloud.com`'s developer account at [api.slack.com](https://api.slack.com). Identify which apps use token rotation.

**Owner Mutation Step**

For apps where the creating account can be changed: log in to [api.slack.com](https://api.slack.com) as `syncrescendence@gmail.com` and recreate the app using the existing app manifest (downloadable from the app's **App Manifest** tab). Reinstall the new app to the workspace to generate new OAuth tokens. Update all downstream integrations and secrets stores with the new tokens.

For apps using token rotation: implement the `tooling.tokens.rotate` API method to exchange the existing refresh token for a new access token. [^4] This does not change app ownership but ensures token continuity.

**Post-Verification Step**

Test each app's functionality end-to-end after migration. Verify that all slash commands, event subscriptions, and bot interactions function correctly under the new app credentials.

**Rollback Step**

Reactivate the original app in the workspace. Revert downstream integrations to the original tokens.

---

### 2.3 Discord Server Ownership

**Preconditions**

`syncrescendence@gmail.com`'s Discord account must be an existing member of the server. The current server owner (`truongphillipthanh@icloud.com`) must be logged in.

**Owner Mutation Step**

Step 1: As `truongphillipthanh@icloud.com`, open **Server Settings → Members**.

Step 2: Right-click on the `syncrescendence@gmail.com` member entry and select **Transfer Ownership**. [^5]

Step 3: Confirm the transfer in the dialog box.

**Post-Verification Step**

Log in as `syncrescendence@gmail.com` and confirm the server crown icon appears next to the account name. Verify that all server settings, roles, and channels remain intact.

**Rollback Step**

The new server owner can transfer ownership back to `truongphillipthanh@icloud.com` using the same process.

---

### 2.4 Discord Developer Team and Application/Bot Ownership

Discord developer team and application ownership transfers for verified apps require a formal support request. [^6]

**Preconditions**

Collect the following information before submitting the request: the **App ID** of each application, the **Team ID** of the developer team, the **User ID** of the `syncrescendence@gmail.com` Discord account, the reason for the transfer, and written consent from the receiving account. Confirm that all team members and applications are in good standing (not banned or suspended). Note that ownership transfers are limited to one request per developer product within a 90-day period. [^6]

**Owner Mutation Step**

Step 1: The current owner submits a transfer request via the Discord Developer Support form at [https://dis.gd/developer-support/teams-and-ownership](https://dis.gd/developer-support/teams-and-ownership). [^6]

Step 2: Both the current owner and the receiving account (`syncrescendence@gmail.com`) must respond to Discord's consent requests within **30 days**.

Step 3: If the team owns verified applications, Discord will remove verification from those applications as part of the transfer process. The new owner must reapply for verification after the transfer is complete.

Step 4: Once both parties consent and verification is removed (if applicable), Discord processes the transfer through the Developer Portal.

> **Timeline:** The process typically takes 30–60 days depending on response times. Plan accordingly.

**Post-Verification Step**

Confirm in the Discord Developer Portal that `syncrescendence@gmail.com` is listed as the team owner. Reapply for app verification if applicable. Test all bot integrations to confirm tokens and permissions are functioning.

**Rollback Step**

Submit a new transfer request to Discord Support to revert ownership. This is subject to the 90-day cooldown period per developer product.

---

## Wave 3 — Google Ecosystem (Workspace + GCP + YouTube)

### 3.1 Google Workspace Super Admin Transfer

**Preconditions**

`syncrescendence@gmail.com` must already have a user account within the Google Workspace organization (not an external Gmail account — it must be a managed user). The current Super Admin must be logged in to the Google Admin console.

**Owner Mutation Step**

Step 1: Log in to the Google Admin console at [admin.google.com](https://admin.google.com) as `truongphillipthanh@icloud.com`.

Step 2: Navigate to **Directory → Users**, locate the `syncrescendence@gmail.com` managed user account, and open the user's profile.

Step 3: Click **Admin roles and privileges → Super Admin** and toggle the Super Admin role to **On**. [^7]

Step 4: Log in as `syncrescendence@gmail.com` and verify Super Admin access.

Step 5: Optionally, remove the Super Admin role from `truongphillipthanh@icloud.com` or deprovision that account.

**Post-Verification Step**

Confirm that `syncrescendence@gmail.com` can access all sections of the Admin console, including Billing, Users, and Security. Verify that the legacy account's admin role has been appropriately downgraded.

**Rollback Step**

The new Super Admin can reassign the Super Admin role to `truongphillipthanh@icloud.com` using the same process.

---

### 3.2 GCP Project Ownership Transfer

**Preconditions**

`syncrescendence@gmail.com` must have a Google account. The current project Owner must be logged in to the GCP Console.

**Owner Mutation Step**

Step 1: In the [GCP Console](https://console.cloud.google.com), navigate to **IAM & Admin → IAM** for the target project.

Step 2: Click **Grant Access**, enter `syncrescendence@gmail.com`, and assign the **Owner** role. [^8]

Step 3: Navigate to **Billing** and link the project to a billing account controlled by `syncrescendence@gmail.com`, or add `syncrescendence@gmail.com` as a **Billing Account Administrator** on the existing billing account. [^9]

Step 4: Remove the **Owner** role from `truongphillipthanh@icloud.com` after confirming the new owner has full access.

**Post-Verification Step**

Log in as `syncrescendence@gmail.com` and verify full access to all GCP project resources, including Compute, Storage, and API management. Confirm billing access.

**Rollback Step**

Re-add `truongphillipthanh@icloud.com` as an Owner in IAM and restore billing access.

---

### 3.3 YouTube Channel Ownership

YouTube channels are tied to the Google Account that owns them. If the channel is owned by the Google Workspace account (`truongphillipthanh@icloud.com`), transferring Super Admin rights (Step 3.1) does not automatically transfer the YouTube channel. The channel must be moved to a **Brand Account** managed by `syncrescendence@gmail.com`.

**Owner Mutation Step**

Step 1: Log in to YouTube as `truongphillipthanh@icloud.com`. Navigate to **YouTube Studio → Settings → Channel → Advanced Settings**.

Step 2: If the channel is not already a Brand Account, move it to a Brand Account.

Step 3: Add `syncrescendence@gmail.com` as a **Manager** of the Brand Account via [myaccount.google.com/brandaccounts](https://myaccount.google.com/brandaccounts).

Step 4: Remove `truongphillipthanh@icloud.com` from the Brand Account managers.

**Post-Verification Step**

Log in as `syncrescendence@gmail.com` and confirm access to YouTube Studio for the channel.

**Rollback Step**

Re-add `truongphillipthanh@icloud.com` as a Manager of the Brand Account.

---

## Wave 4 — Exocortex Suite

Wave 4 covers the knowledge management and project management platforms. These can generally be executed in parallel with each other after Wave 3 is complete.

### 4.1 Notion

**Owner Mutation Step**

The simplest path for Notion is to change the email address of the existing Syncrescendence Notion account from `truongphillipthanh@icloud.com` to `syncrescendence@gmail.com`. Navigate to **Settings → My Account → Change email**, enter the new email, and verify via the code sent to `syncrescendence@gmail.com`. [^10] This preserves all workspace memberships, owned pages, and databases without requiring any content migration.

**Post-Verification Step**

Log in to Notion using `syncrescendence@gmail.com` and confirm all workspaces, pages, and databases are accessible.

**Rollback Step**

Repeat the email change process to revert to `truongphillipthanh@icloud.com`.

---

### 4.2 Coda

**Owner Mutation Step**

For each Coda doc owned by `truongphillipthanh@icloud.com`: open the doc, click the **Share** button, locate `syncrescendence@gmail.com` in the collaborators list (add if not present), and click **Make Owner**. [^11] For workspace-level ownership, contact Coda support or use the workspace admin panel to transfer ownership.

**Post-Verification Step**

Confirm that `syncrescendence@gmail.com` is listed as the owner of all transferred docs.

**Rollback Step**

Repeat the Make Owner process to revert doc ownership.

---

### 4.3 Confluence and Jira (Atlassian)

**Owner Mutation Step**

Step 1: Log in to [admin.atlassian.com](https://admin.atlassian.com) as the current organization admin.

Step 2: Navigate to **Directory → Users**, locate `syncrescendence@gmail.com`, open the user profile, click the more actions menu (•••), and select **Assign org admin role**. [^12]

Step 3: Log in as `syncrescendence@gmail.com` and confirm organization admin access.

Step 4: Optionally remove the org admin role from `truongphillipthanh@icloud.com`.

> **Note:** If the current admin is no longer available, contact Atlassian Support to initiate a role transfer process. The current admin will be contacted for approval; if there is no response within three days, the role transfer can proceed after verification. [^12]

**Post-Verification Step**

Confirm that `syncrescendence@gmail.com` has full access to all Jira projects and Confluence spaces via the Atlassian Admin console.

**Rollback Step**

Assign the org admin role back to `truongphillipthanh@icloud.com`.

---

### 4.4 Linear

**Owner Mutation Step**

In Linear, navigate to **Settings → Members**. Locate `syncrescendence@gmail.com` (invite if not present) and promote them to **Workspace Owner**. [^13] The previous owner's role will be downgraded to Admin.

**Post-Verification Step**

Log in as `syncrescendence@gmail.com` and confirm Workspace Owner access, including billing and settings.

**Rollback Step**

Transfer workspace ownership back to `truongphillipthanh@icloud.com` from the Settings panel.

---

### 4.5 ClickUp

**Owner Mutation Step**

In ClickUp, navigate to **Settings → People**. Locate `syncrescendence@gmail.com` (invite if not present). Click the role dropdown next to the account and select **Transfer Ownership**. Confirm the transfer. [^14] The previous owner becomes an Admin.

**Post-Verification Step**

Log in as `syncrescendence@gmail.com` and confirm Workspace Owner access.

**Rollback Step**

Transfer workspace ownership back to `truongphillipthanh@icloud.com`.

---

### 4.6 Basecamp

**Owner Mutation Step**

In Basecamp, navigate to **Account Settings → Administrators**. Add `syncrescendence@gmail.com` as an Administrator. Contact Basecamp support or use the account owner transfer flow to designate `syncrescendence@gmail.com` as the primary account owner.

**Post-Verification Step**

Confirm `syncrescendence@gmail.com` has full account owner access including billing.

**Rollback Step**

Revert account owner designation back to `truongphillipthanh@icloud.com`.

---

### 4.7 Airtable

**Owner Mutation Step**

For workspace ownership: if on an Enterprise plan, use the **Workspaces tab** in the admin panel to transfer workspace ownership to `syncrescendence@gmail.com`. [^15] For individual bases: open each base, navigate to **Share → Collaborators**, and use the ownership transfer option to assign `syncrescendence@gmail.com` as the new owner.

**Post-Verification Step**

Confirm `syncrescendence@gmail.com` is listed as the owner of all workspaces and bases.

**Rollback Step**

Repeat the ownership transfer process to revert to `truongphillipthanh@icloud.com`.

---

## References

[^1]: [Transferring organization ownership — GitHub Docs](https://docs.github.com/en/organizations/managing-organization-settings/transferring-organization-ownership)
[^2]: [Move a domain between Cloudflare accounts — Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/manage-domains/move-domain/)
[^3]: [Transfer ownership of a workspace or org — Slack Help Center](https://slack.com/help/articles/204401633-Transfer-ownership-of-a-workspace-or-org)
[^4]: [Using token rotation — Slack Developer Docs](https://docs.slack.dev/authentication/using-token-rotation/)
[^5]: [How to Transfer Ownership of a Discord Server — Discord Support](https://support.discord.com/hc/en-us/articles/216273938-How-to-Transfer-Ownership-of-a-Discord-Server)
[^6]: [How to Transfer Ownership of a Developer Team — Discord Developer Support](https://support-dev.discord.com/hc/en-us/articles/34905402845591-How-to-Transfer-Ownership-of-a-Developer-Team)
[^7]: [Make a user an admin — Google Workspace Admin Help](https://knowledge.workspace.google.com/admin/users/make-a-user-an-admin)
[^8]: [Manage access to projects, folders, and organizations — Google Cloud IAM](https://cloud.google.com/iam/docs/granting-changing-revoking-access)
[^9]: [Enable, disable, or change billing for a project — Google Cloud Billing](https://cloud.google.com/billing/docs/how-to/modify-project)
[^10]: [Account settings & preferences — Notion Help Center](https://www.notion.com/help/account-settings)
[^11]: [Change ownership of your Coda doc — Coda Help](https://help.coda.io/hc/en-us/articles/39555803168013-Change-ownership-of-your-Coda-doc)
[^12]: [Give users admin permissions — Atlassian Support](https://support.atlassian.com/user-management/docs/give-users-admin-permissions/)
[^13]: [Members and roles — Linear Docs](https://linear.app/docs/members-roles)
[^14]: [Transfer Workspace ownership — ClickUp Help](https://help.clickup.com/hc/en-us/articles/6310482663063-Transfer-Workspace-ownership)
[^15]: [Transferring Airtable workspace, base, and interface ownership — Airtable Support](https://support.airtable.com/docs/transferring-airtable-workspace-base-and-interface-ownership)
