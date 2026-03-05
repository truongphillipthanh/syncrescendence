# SLACK-DISCORD-FOCUSED-CUTOVER

**Project:** Syncrescendence Account Centralization — CC82
**Scope:** Slack workspace + app ownership; Discord server + developer team/app/bot ownership and token rotation
**Prepared:** 2026-03-05

---

## Overview

This document provides the detailed, step-by-step cutover procedure for the Slack and Discord surfaces. These platforms present the highest operational complexity in the migration due to the absence of direct API-based ownership transfer, the need for dual-party consent (Discord), and the requirement to rotate all app tokens after ownership changes. Each section follows the structure: **Preconditions → Owner Mutation → Post-Verification → Rollback**.

---

## Part 1: Slack

### 1.1 Workspace Primary Ownership Transfer

Slack's Primary Owner role is the highest-privilege role in a workspace. Only the current Primary Owner can initiate a transfer. [^1]

**Preconditions**

Confirm that `syncrescendence@gmail.com` is a full member (not a guest) of the Slack workspace. Confirm the current Primary Owner (`truongphillipthanh@icloud.com`) has access to their Slack account and knows their password. Notify the workspace of the upcoming ownership change if appropriate.

**Owner Mutation Step**

1. Log in to Slack as `truongphillipthanh@icloud.com` on the desktop client.
2. Navigate to the **Transfer Ownership** page. This is accessible via **Admin → Settings → Transfer Ownership**, or directly at `https://{workspace-name}.slack.com/admin/transferOwnership`.
3. In the search field, type and select `syncrescendence@gmail.com` as the new Primary Owner.
4. Enter the current Primary Owner's Slack password when prompted.
5. Click **Transfer Workspace Ownership** to confirm.

> The transfer is **immediate and irreversible via self-service** (though the new Primary Owner can transfer back). The current owner's role changes from **Primary Owner** to **Owner**.

**Post-Verification Step**

Log in as `syncrescendence@gmail.com`. Navigate to **Admin → Settings** and confirm the account is listed as **Primary Owner**. Navigate to **Admin → Billing** and update the billing contact email and payment method to reflect the new owner. Verify that `truongphillipthanh@icloud.com` is now listed as **Owner** (not Primary Owner).

**Rollback Step**

The new Primary Owner (`syncrescendence@gmail.com`) navigates to the Transfer Ownership page and transfers the role back to `truongphillipthanh@icloud.com`. [^1]

---

### 1.2 Slack App Inventory and Ownership Assessment

Before executing app ownership changes, the operator team must complete a full inventory of all Slack apps installed in the workspace and all apps created under the `truongphillipthanh@icloud.com` developer account.

**Inventory Steps**

1. Navigate to [api.slack.com/apps](https://api.slack.com/apps) and log in as `truongphillipthanh@icloud.com`. Export the list of all apps created under this account.
2. In the Slack Admin console, navigate to **Installed Apps** to identify all apps installed in the workspace, including third-party apps.
3. For each app created by `truongphillipthanh@icloud.com`, determine the migration path:

| App Type | Migration Path |
|---|---|
| Custom workspace app (no verification) | Recreate under `syncrescendence@gmail.com` account |
| Custom workspace app (verified) | Recreate under new account; reapply for verification |
| Third-party OAuth app | Re-authorize under `syncrescendence@gmail.com` |
| App using token rotation | Rotate tokens; no ownership change required for functionality |

---

### 1.3 Slack App Recreation and Token Rotation

**Preconditions**

The full app inventory from Section 1.2 must be complete. For each app to be recreated, export the **App Manifest** (available in the app's configuration at [api.slack.com/apps](https://api.slack.com/apps) under **App Manifest**). Identify all downstream systems (CI/CD pipelines, integrations, secrets stores) that hold the current app's OAuth tokens.

**Owner Mutation Step — App Recreation**

For each custom app owned by `truongphillipthanh@icloud.com`:

1. Log in to [api.slack.com/apps](https://api.slack.com/apps) as `syncrescendence@gmail.com`.
2. Click **Create New App → From an app manifest**.
3. Paste the exported manifest from the original app.
4. Install the new app to the workspace by navigating to **OAuth & Permissions → Install to Workspace** and authorizing the required scopes.
5. Copy the new **Bot User OAuth Token** and **User OAuth Token** generated after installation.
6. Update all downstream integrations, environment variables, and secrets stores with the new tokens.
7. Deactivate (do not delete) the original app in the `truongphillipthanh@icloud.com` account after confirming the new app is functional.

**Owner Mutation Step — Token Rotation**

For apps that use Slack's token rotation feature, the existing tokens can be refreshed without recreating the app. This is appropriate for apps where the underlying app ownership is not being changed but the tokens need to be cycled. [^2]

To rotate a token, make a POST request to the `tooling.tokens.rotate` method with the current refresh token:

```
POST https://slack.com/api/tooling.tokens.rotate
Content-Type: application/x-www-form-urlencoded

refresh_token={current_refresh_token}
```

The response will contain a new `token` (access token) and a new `refresh_token`. Store these securely and update all downstream consumers.

**Post-Verification Step**

For each migrated app: trigger a test event or slash command to confirm the app responds correctly under the new credentials. Verify that all event subscriptions and interactive components are receiving and processing payloads. Check the app's **Event Subscriptions** and **Interactivity** pages in the app configuration to confirm the request URLs are still valid.

**Rollback Step**

Reactivate the original app in the `truongphillipthanh@icloud.com` account. Revert all downstream integrations to the original tokens. Deactivate the new app.

---

## Part 2: Discord

### 2.1 Discord Server Ownership Transfer

**Preconditions**

`syncrescendence@gmail.com`'s Discord account must be an existing member of the server. The current server owner (`truongphillipthanh@icloud.com`) must be logged in to Discord.

**Owner Mutation Step**

1. Log in to Discord as `truongphillipthanh@icloud.com`.
2. Right-click on the server icon in the left sidebar and select **Server Settings**.
3. Navigate to **Members** in the left panel.
4. Locate the `syncrescendence@gmail.com` Discord account in the member list.
5. Click the three-dot menu (⋮) next to the member's name and select **Transfer Ownership**. [^3]
6. Confirm the transfer in the dialog box.

**Post-Verification Step**

Log in as `syncrescendence@gmail.com`. Confirm the server crown icon (👑) appears next to the account name in the member list. Verify that all server settings, roles, channels, and integrations remain intact. Confirm that the previous owner (`truongphillipthanh@icloud.com`) now holds only their previously assigned role (e.g., Admin).

**Rollback Step**

Log in as `syncrescendence@gmail.com` (the new server owner) and repeat the transfer process to return ownership to `truongphillipthanh@icloud.com`.

---

### 2.2 Discord Developer Team Ownership Transfer

Discord developer team ownership transfers for teams that own verified applications require a formal support request to Discord. [^4]

**Preconditions**

Gather the following information before submitting the request:

| Required Item | Where to Find It |
|---|---|
| App ID | Discord Developer Portal → Application → General Information |
| Team ID | Discord Developer Portal → Teams → select team |
| New Owner's Discord User ID | Discord → User Settings → Advanced → Developer Mode → right-click username → Copy User ID |
| Reason for transfer | Prepare a brief written statement |
| Recipient consent | Written confirmation from `syncrescendence@gmail.com` Discord account |

Confirm that all team members and all applications owned by the team are in good standing (not banned or suspended). Note the 90-day cooldown period between transfer requests per developer product. [^4]

**Owner Mutation Step**

1. The current team owner (`truongphillipthanh@icloud.com`) submits a transfer request via the Discord Developer Support form at [https://dis.gd/developer-support/teams-and-ownership](https://dis.gd/developer-support/teams-and-ownership). [^4]
2. Select the appropriate category for developer product ownership transfers.
3. Provide all required information listed above.
4. Both the current owner and the receiving account (`syncrescendence@gmail.com`) must respond to Discord's consent requests within **30 days** of the request.
5. If the team owns verified applications, Discord will remove verification from those applications as part of the transfer. The new owner must reapply for verification after the transfer is complete.
6. Once both parties consent and verification is removed (if applicable), Discord processes the transfer through the Developer Portal.

> **Timeline:** The process typically takes **30–60 days** depending on response times from both parties. This wave must be initiated well in advance of any hard deadline.

**Post-Verification Step**

Confirm in the [Discord Developer Portal](https://discord.com/developers/applications) that `syncrescendence@gmail.com` is listed as the team owner. If applicable, initiate the re-verification process for any apps that lost verification status. Test all bot integrations to confirm tokens and permissions are functioning correctly.

**Rollback Step**

Submit a new transfer request to Discord Developer Support to revert ownership to `truongphillipthanh@icloud.com`. This is subject to the 90-day cooldown period per developer product.

---

### 2.3 Discord Bot Token Management

Discord bot tokens are tied to the application, not to the team owner. Transferring team ownership does not automatically invalidate or rotate bot tokens. However, it is best practice to regenerate the bot token after an ownership transfer to ensure the new owner has sole control.

**Token Rotation Step**

1. Log in to the [Discord Developer Portal](https://discord.com/developers/applications) as the new team owner (`syncrescendence@gmail.com`).
2. Navigate to the application and select **Bot** in the left panel.
3. Click **Reset Token** and confirm. A new bot token will be generated.
4. Update all downstream services, environment variables, and secrets stores with the new bot token.
5. Restart all bot processes to pick up the new token.

> **Warning:** Resetting the bot token immediately invalidates the old token. All bot instances using the old token will stop functioning until updated. Schedule this step during a low-traffic maintenance window.

**Post-Verification Step**

Confirm that the bot comes online and responds correctly in the Discord server after the token rotation. Verify all slash commands, event handlers, and integrations are functioning.

**Rollback Step**

There is no rollback for a token reset. If the new token is lost or compromised, reset the token again and update all consumers.

---

## References

[^1]: [Transfer ownership of a workspace or org — Slack Help Center](https://slack.com/help/articles/204401633-Transfer-ownership-of-a-workspace-or-org)
[^2]: [Using token rotation — Slack Developer Docs](https://docs.slack.dev/authentication/using-token-rotation/)
[^3]: [How to Transfer Ownership of a Discord Server — Discord Support](https://support.discord.com/hc/en-us/articles/216273938-How-to-Transfer-Ownership-of-a-Discord-Server)
[^4]: [How to Transfer Ownership of a Developer Team — Discord Developer Support](https://support-dev.discord.com/hc/en-us/articles/34905402845591-How-to-Transfer-Ownership-of-a-Developer-Team)
