# PACKET-MANUS-cc82b — GitHub / Slack / Discord Cutover Runbook

**Document type:** Execution-ready migration runbook
**Legacy owner surface:** `truongphillipthanh@icloud.com`
**Target owner surface:** `syncrescendence@gmail.com`
**Scope:** GitHub ownership/billing/control · Slack workspace/app/token migration · Discord server/app/bot migration
**Constraint set:** Evidence-backed steps only · No credentials embedded · No destructive actions · Rollback path for every mutation step

> **How to use this document.** Work through each checklist top-to-bottom in a single controlled maintenance window. Complete all preconditions before executing any mutation step. Tick off each step as it is completed. Do not proceed to the next platform section until post-verification for the current section passes.

---

# 1. GITHUB_CUTOVER_CHECKLIST

## 1.1 Preconditions

The following conditions must be confirmed as true before any mutation step is executed. Failure to satisfy any precondition is a hard blocker.

| # | Precondition | Verification method |
| :--- | :--- | :--- |
| P-GH-1 | The target owner (`syncrescendence@gmail.com`) has an active GitHub account. | Log in to github.com with the target account and confirm the dashboard loads. |
| P-GH-2 | The target owner's GitHub account has 2FA enabled. [^gh-2fa] | Settings → Password and authentication → confirm 2FA is active. |
| P-GH-3 | The legacy owner's GitHub account has 2FA enabled. [^gh-2fa] | Same as above for the legacy account. |
| P-GH-4 | The target owner is already a member of the GitHub organization. [^gh-org-transfer] | Organization → People → confirm target username appears. |
| P-GH-5 | A full inventory of GitHub Apps owned by the legacy account has been compiled. [^gh-app-transfer] | Settings → Developer settings → GitHub Apps. |
| P-GH-6 | A full inventory of repositories owned by the legacy account or organization has been compiled. [^gh-repo-transfer] | Organization → Repositories. |
| P-GH-7 | All CI/CD pipeline secrets and environment variables have been documented. [^gh-secrets] | Repository → Settings → Secrets and variables → Actions. |
| P-GH-8 | The target owner has valid payment information ready to substitute for the legacy billing details. [^gh-billing] | Confirm credit card or PayPal details are available. |

## 1.2 Mutation Steps

Execute these steps in strict order. Do not skip ahead.

**Step GH-M-1 — Grant Owner role to target account** [^gh-org-transfer]

From the legacy owner account: navigate to the organization's **People** page, locate the target account, click the three-dot menu, and select **Change role → Owner**. The target owner will receive a confirmation email. The target owner must accept the invitation before proceeding.

> **Rollback:** Navigate to the organization's **People** page, locate the target account, and change their role back to **Member** or remove them from the organization.

---

**Step GH-M-2 — Update organization billing information** [^gh-billing]

> **Warning (from GitHub Docs):** Removing yourself from the organization **does not** update the billing information on file for the organization account. The new owner or a billing manager must update the billing information to remove the legacy credit card or PayPal information.

From the target owner account: navigate to the organization → **Settings** → **Billing & Licensing** → **Payment information**. Click **Edit** and replace the legacy payment method with the target owner's payment method. Update the billing contact email to `syncrescendence@gmail.com`.

> **Rollback:** Navigate back to the same page and re-enter the legacy payment details. Note that this requires the legacy owner to supply their card details again.

---

**Step GH-M-3 — Transfer each GitHub App registration** [^gh-app-transfer]

For each GitHub App in the inventory (P-GH-5): from the legacy owner account, navigate to **Settings** → **Developer settings** → **GitHub Apps** → select the app → **Advanced** → **Transfer ownership**. Enter the target owner's GitHub username. Confirm the transfer.

> **Rollback:** From the target owner account, navigate to the same GitHub App settings and transfer ownership back to the legacy owner's username.

---

**Step GH-M-4 — Transfer each repository** [^gh-repo-transfer]

For each repository in the inventory (P-GH-6): navigate to the repository → **Settings** → scroll to the **Danger Zone** → **Transfer**. Specify the target owner's username or organization name. Type the repository name to confirm. The new owner will receive a confirmation email and must accept within one day.

Key transfer behaviors to note: all issues, pull requests, wiki pages, stars, and watchers transfer with the repository. Repository-level GitHub Actions secrets transfer with the repository; organization-level secrets and environment secrets do not and must be recreated manually. [^gh-secrets-transfer]

> **Rollback:** From the target owner account, navigate to the repository → **Settings** → **Danger Zone** → **Transfer** and transfer ownership back to the legacy owner.

---

**Step GH-M-5 — Rotate Personal Access Tokens (PATs)** [^gh-pats]

From the target owner account: navigate to **Settings** → **Developer settings** → **Personal access tokens**. Revoke all existing fine-grained and classic PATs that were issued under the legacy account context and that are now used by integrations or automation. Issue new PATs with the minimum required scopes. Update all downstream systems (CI/CD, scripts, third-party integrations) with the new token values.

> **Rollback:** If a new PAT causes a downstream failure, revoke it and issue a replacement with the correct scope. There is no mechanism to restore a revoked PAT; a new one must be generated.

---

**Step GH-M-6 — Rotate SSH deploy keys** [^gh-ssh]

For each repository that uses SSH deploy keys: navigate to the repository → **Settings** → **Deploy keys**. Delete the legacy key. Generate a new SSH key pair on the target owner's machine (`ssh-keygen -t ed25519 -C "syncrescendence@gmail.com"`). Add the new public key as a deploy key. Update all servers or automation agents that use the private key.

> **Rollback:** Delete the new deploy key and re-add the legacy public key if it was preserved.

---

**Step GH-M-7 — Recreate organization-level and environment-level GitHub Actions secrets** [^gh-secrets]

Navigate to the organization → **Settings** → **Secrets and variables** → **Actions**. For each secret that was documented in P-GH-7 and that is not automatically transferred with repositories, create a new secret with the same name and the updated value. Repeat for each repository environment under **Settings** → **Environments**.

> **Rollback:** Delete the newly created secrets and recreate them with the original values.

---

**Step GH-M-8 — Remove legacy owner from the organization** [^gh-org-transfer]

Only execute this step after all post-verification checks in Section 1.3 pass. From the target owner account: navigate to the organization → **People** → locate the legacy owner → click the three-dot menu → **Remove from organization**.

> **Rollback:** Re-invite the legacy owner (`truongphillipthanh@icloud.com`) to the organization and grant them the Owner role.

## 1.3 Post-Verification

| # | Check | Pass condition |
| :--- | :--- | :--- |
| V-GH-1 | Organization ownership | Target owner can access organization **Settings** without restriction. |
| V-GH-2 | Billing | Billing page shows target owner's payment method and `syncrescendence@gmail.com` as the billing contact. |
| V-GH-3 | GitHub App ownership | Each transferred app appears under the target owner's **Developer settings → GitHub Apps**. |
| V-GH-4 | Repository admin access | Target owner has **Admin** role on all transferred repositories. |
| V-GH-5 | CI/CD pipelines | At least one full pipeline run completes successfully after the token and secret rotation. |
| V-GH-6 | Legacy owner removed | The legacy owner's account does not appear in the organization's **People** list. |

## 1.4 Rollback Summary

All individual rollback paths are documented inline with each mutation step above. The general recovery sequence in the event of a full rollback is: re-invite the legacy owner → restore their Owner role → revert billing information → re-transfer GitHub Apps → re-transfer repositories → restore PATs and SSH keys → restore secrets → remove the target owner if desired.

---

# 2. SLACK_CUTOVER_CHECKLIST

## 2.1 Workspace Owner/Admin Transfer

### Preconditions

| # | Precondition | Verification method |
| :--- | :--- | :--- |
| P-SL-1 | The legacy owner (`truongphillipthanh@icloud.com`) holds the **Primary Owner** role in the workspace. [^sl-transfer] | Navigate to **About This Workspace** and confirm the Primary Owner identity. |
| P-SL-2 | The target owner (`syncrescendence@gmail.com`) is an active member of the workspace. [^sl-transfer] | Workspace **People & user groups** → confirm the target account is present. |
| P-SL-3 | The legacy owner has access to their account password (required to confirm the transfer). [^sl-transfer] | Confirm with the legacy owner prior to the maintenance window. |

### Mutation Steps

**Step SL-M-1 — Transfer Primary Ownership** [^sl-transfer]

From the legacy owner account: navigate to the [transfer ownership page](https://slack.com/intl/en-us/help/articles/204401633) (or go to **workspace name → Tools & settings → Manage members → Transfer ownership**). Search for and select the target owner's account. Enter the legacy owner's password to confirm. Click **Transfer Workspace Ownership**.

The transfer is immediate. The legacy owner's role changes from Primary Owner to Owner. The target owner becomes the new Primary Owner.

> **Rollback:** The new Primary Owner can transfer Primary Ownership back to the legacy owner by following the same procedure from the new Primary Owner account.

---

**Step SL-M-2 — Update billing information** [^sl-transfer]

After the ownership transfer, the new Primary Owner should verify and update the workspace billing information to reflect `syncrescendence@gmail.com` as the billing contact.

> **Rollback:** Update the billing contact back to the legacy email address.

## 2.2 Slack App Ownership/Governance Transition

### Preconditions

| # | Precondition | Verification method |
| :--- | :--- | :--- |
| P-SL-4 | A full inventory of internal Slack apps owned or managed by the legacy owner has been compiled. [^sl-collaborators] | Workspace **Tools & settings → Manage apps → Internal Apps**. |
| P-SL-5 | The workspace is on a **Business+** or **Enterprise** plan (required for the collaborator management feature). [^sl-collaborators] | Confirm plan tier in workspace billing settings. |

### Mutation Steps

**Step SL-M-3 — Add target owner as app collaborator** [^sl-collaborators]

For each internal app in the inventory (P-SL-4): from the workspace **Tools & settings → Manage apps → Internal Apps**, locate the app, click the three-dot icon, and select **Add myself as a collaborator** (if acting as a Workspace Owner) or use the Slack CLI command `slack collaborator add <email>` to add the target owner's email address.

> **Rollback:** Use the Slack CLI command `slack collaborator remove <email>` or the workspace admin UI to remove the target owner as a collaborator.

---

**Step SL-M-4 — Remove legacy owner as app collaborator** [^sl-collaborators]

Only execute after Step SL-M-3 is confirmed and the target owner has verified access. From the Slack CLI: run `slack collaborator remove <legacy-email>` for each app. Alternatively, use the workspace admin UI.

> **Important (from Slack Docs):** If a collaborator is removed from an app, they may still retain their OAuth tokens. It is therefore recommended that the app owner rotate secrets and tokens after a collaborator is removed. [^sl-collab-security]

> **Rollback:** Re-add the legacy owner as a collaborator using `slack collaborator add <legacy-email>`.

## 2.3 Token Rotation Sequence and Reauthorization Checks

This section applies to Slack apps that use the OAuth V2 granular permissions model with token rotation enabled. [^sl-token-rotation]

### Preconditions

| # | Precondition | Verification method |
| :--- | :--- | :--- |
| P-SL-6 | Token rotation is enabled for the app in the app's OAuth & Permissions settings. [^sl-token-rotation] | Navigate to **api.slack.com/apps → [App] → OAuth & Permissions** and confirm token rotation is toggled on. |
| P-SL-7 | The current long-lived access token (prefixed `xoxb-` for bot or `xoxp-` for user) has been securely noted. | Retrieve from the app's secure credential store. |

### Mutation Steps

**Step SL-M-5 — Exchange the long-lived token for a rotatable token pair** [^sl-token-rotation]

Call the `oauth.v2.exchange` API method with the existing long-lived access token:

```
POST https://slack.com/api/oauth.v2.exchange
Content-Type: application/x-www-form-urlencoded

client_id=<APP_CLIENT_ID>
client_secret=<APP_CLIENT_SECRET>
token=<EXISTING_LONG_LIVED_TOKEN>
```

The response returns a new short-lived `access_token` (prefixed `xoxe.xoxb-` or `xoxe.xoxp-`, valid for 12 hours) and a `refresh_token` (prefixed `xoxe-`). Store both securely. Do not attempt to exchange the same long-lived token twice; it can only be exchanged once.

> **Rollback:** If the exchange fails, the original long-lived token remains valid. Do not call `auth.revoke` on it. Diagnose the error and retry.

---

**Step SL-M-6 — Refresh the access token before expiry** [^sl-token-rotation]

Schedule a recurring task to call `oauth.v2.access` with the `grant_type=refresh_token` parameter before the 12-hour expiry window:

```
POST https://slack.com/api/oauth.v2.access
Content-Type: application/x-www-form-urlencoded

client_id=<APP_CLIENT_ID>
client_secret=<APP_CLIENT_SECRET>
grant_type=refresh_token
refresh_token=<CURRENT_REFRESH_TOKEN>
```

Each call returns a new `access_token` and a new `refresh_token`. The previous refresh token is revoked after a short grace period. Store the new pair immediately.

> **Rollback:** If a refresh call fails, the previous access token remains valid during the grace period. Retry the refresh call. If the access token has expired, the app must be reinstalled via the full OAuth flow.

---

**Step SL-M-7 — Verify old token invalidation** [^sl-token-rotation]

Call `auth.test` with the original long-lived token. Confirm that the response returns `{"ok": false, "error": "invalid_auth"}`, indicating the token has been successfully invalidated.

> **Rollback:** Not applicable. If the old token is still valid, do not revoke it manually; allow it to expire naturally or proceed with the next refresh cycle.

### Post-Verification

| # | Check | Pass condition |
| :--- | :--- | :--- |
| V-SL-1 | Primary Ownership | The target owner's account shows **Primary Owner** on the **About This Workspace** page. |
| V-SL-2 | App collaborator access | The target owner can open and modify each app's settings in the Slack Developer Portal. |
| V-SL-3 | Token validity | A call to `auth.test` with the new access token returns `{"ok": true}`. |
| V-SL-4 | Old token invalidation | A call to `auth.test` with the old long-lived token returns `{"ok": false, "error": "invalid_auth"}`. |

## 2.4 Rollback Summary

The general recovery sequence for a full Slack rollback is: the new Primary Owner transfers Primary Ownership back to the legacy owner → re-add the legacy owner as app collaborator → re-install the app to regenerate tokens if rotation has been disrupted.

---

# 3. DISCORD_CUTOVER_CHECKLIST

## 3.1 Server Ownership/Admin Transfer

### Preconditions

| # | Precondition | Verification method |
| :--- | :--- | :--- |
| P-DC-1 | The target owner's Discord account is an active member of the server. [^dc-server-transfer] | Server **Members** list → confirm target username is present. |
| P-DC-2 | The legacy owner has 2FA enabled on their Discord account (required to confirm the transfer). [^dc-server-transfer] | Legacy owner: **User Settings → My Account → Two-Factor Auth** → confirm active. |
| P-DC-3 | The target owner's Discord account is in good standing (not banned or suspended). | Confirm by checking the account's ability to send messages in the server. |

### Mutation Steps

**Step DC-M-1 — Transfer server ownership** [^dc-server-transfer]

From the legacy owner account on the desktop client: navigate to the target server → **Server Settings** → **Members** tab. Right-click the target owner's username and select **Transfer Ownership**. In the confirmation dialog, toggle the acknowledgement and click **Transfer Ownership**. If 2FA is enabled, enter the 2FA code when prompted.

After the transfer, the legacy owner remains a member of the server. Their retained access depends on the roles assigned to them.

> **Critical warning (from Discord Support):** Once a server has been transferred, Discord's Support team is not able to transfer it back. [^dc-server-transfer] The only recovery path is for the new owner to manually transfer ownership back to the legacy owner.

> **Rollback:** The new owner must manually transfer ownership back to the legacy owner following the same procedure.

## 3.2 Developer App/Team Ownership Transfer

### Preconditions

| # | Precondition | Verification method |
| :--- | :--- | :--- |
| P-DC-4 | The target owner's Discord account has 2FA enabled (required for Developer Portal access). [^dc-teams] | **User Settings → My Account → Two-Factor Auth** → confirm active. |
| P-DC-5 | All team members are in good account standing. [^dc-team-transfer] | Confirm no bans or suspensions on any team member account. |
| P-DC-6 | None of the applications owned by the team are currently banned or suspended. [^dc-team-transfer] | Review each app in the Developer Portal for any policy flags. |
| P-DC-7 | If the team owns **verified** applications, the new owner is prepared to reapply for verification after the transfer. [^dc-team-transfer] | Note all verified apps; prepare verification documentation. |
| P-DC-8 | No ownership transfer has been requested for this team within the past 90 days. [^dc-team-transfer] | Confirm with Discord Developer Support if uncertain. |

### Mutation Steps

**Step DC-M-2 — Transfer individual app to a team (if applicable)** [^dc-teams]

If any applications are currently owned individually by the legacy owner and need to be moved to a team first: navigate to the [Discord Developer Portal](https://discord.com/developers/applications) → select the application → **General Information** → scroll to the bottom → click **Transfer App to Team** → select the target team.

> **Critical warning (from Discord Docs):** Once an app has been transferred to a team, it cannot be transferred back. [^dc-teams]

> **Rollback:** Not available for individual-to-team transfers. Plan carefully before executing.

---

**Step DC-M-3 — Submit developer team ownership transfer request** [^dc-team-transfer]

For teams that own verified applications, or for any team ownership transfer, the current owner must submit a request to Discord Developer Support:

1. Navigate to [https://dis.gd/developer-support/teams-and-ownership](https://dis.gd/developer-support/teams-and-ownership).
2. Select the appropriate category for developer product ownership transfers.
3. Provide the following information: **App ID**, **Team ID**, **User ID of the recipient** (`syncrescendence@gmail.com`'s Discord User ID), **reason for the transfer**, and **written consent from the recipient**.

Discord requires dual-party consent: both the current owner and the recipient must respond within 30 days. The process typically takes 30–60 days. If the team owns verified apps, verification will be removed and must be reapplied for by the new owner.

> **Rollback:** Contact Discord Developer Support to cancel a pending transfer request before it is completed.

## 3.3 Bot Token Rotation and Runtime Verification

### Preconditions

| # | Precondition | Verification method |
| :--- | :--- | :--- |
| P-DC-9 | The new owner has access to the Discord Developer Portal for the application. | Log in to [discord.com/developers/applications](https://discord.com/developers/applications) and confirm the app is visible. |
| P-DC-10 | All runtime environments (servers, containers, hosting platforms) that run the bot have been identified. | Document all deployment targets before proceeding. |
| P-DC-11 | A deployment procedure is in place to update the bot token in all runtime environments with minimal downtime. | Confirm with the operations team. |

### Mutation Steps

**Step DC-M-4 — Reset the bot token** [^dc-token-reset]

From the new owner account: navigate to the [Discord Developer Portal](https://discord.com/developers/applications) → select the application → **Bot** (from the left sidebar) → under the **Build-a-Bot** section, click **Reset Token**. Confirm the action in the pop-up dialog. Enter the 2FA code if prompted. The new token will be displayed once. **Copy it immediately.** It cannot be retrieved again after leaving the page.

> **Critical warning:** Resetting the bot token immediately invalidates the old token. The bot will go offline until the new token is deployed to all runtime environments. [^dc-token-reset]

> **Rollback:** There is no rollback for a token reset. The old token is permanently invalidated. If the deployment of the new token fails, the new token must be updated in the runtime environment to restore bot functionality.

---

**Step DC-M-5 — Deploy the new token to all runtime environments**

Update the bot token environment variable or secret in each runtime environment identified in P-DC-10. Restart the bot process. Confirm the bot comes online in the Discord server (the bot's status indicator should turn green).

> **Rollback:** If the bot fails to come online, verify the token was copied correctly. If the token was corrupted, reset it again from the Developer Portal and redeploy.

### Post-Verification

| # | Check | Pass condition |
| :--- | :--- | :--- |
| V-DC-1 | Server ownership | The crown icon appears next to the target owner's username in the server's member list. |
| V-DC-2 | Developer Portal access | The new owner can access and modify all application settings in the Developer Portal. |
| V-DC-3 | Bot online | The bot's status indicator is green and the bot responds to a test command in the server. |
| V-DC-4 | Old token invalidated | Any service still using the old token receives an authentication error from the Discord API. |

## 3.4 Rollback Summary

Discord server ownership transfer and individual-to-team app transfers are irreversible by Discord Support. The only recovery mechanism is for the new owner to voluntarily transfer back to the legacy owner. Bot token resets are also irreversible; recovery requires deploying the new token to all environments. Plan all Discord steps with particular care and ensure the target owner is fully prepared before executing.

---

# 4. MACHINE_READABLE_LEDGER_ROWS

| platform | state | human_action_required | api_automatable | next_step | rollback_step |
| :--- | :--- | :--- | :--- | :--- | :--- |
| GitHub | P-GH: Preconditions verified | Yes | No | GH-M-1: Grant Owner role | N/A — no mutation yet |
| GitHub | GH-M-1: Grant Owner role | Yes | No | GH-M-2: Update billing | Remove target from org |
| GitHub | GH-M-2: Update billing information | Yes | No | GH-M-3: Transfer GitHub Apps | Revert payment method in billing settings |
| GitHub | GH-M-3: Transfer GitHub App(s) | Yes | No | GH-M-4: Transfer repositories | Transfer app(s) back to legacy owner |
| GitHub | GH-M-4: Transfer repositories | Yes | No | GH-M-5: Rotate PATs | Transfer repos back to legacy owner |
| GitHub | GH-M-5: Rotate PATs | Yes | Partial (API: token creation/revocation via REST) | GH-M-6: Rotate SSH keys | Issue replacement PAT with correct scope |
| GitHub | GH-M-6: Rotate SSH deploy keys | Yes | Partial (API: deploy key management via REST) | GH-M-7: Recreate secrets | Delete new key; re-add legacy public key |
| GitHub | GH-M-7: Recreate Actions secrets | Yes | Yes (GitHub REST API: secrets endpoints) | GH-M-8: Remove legacy owner | Delete new secrets; recreate with original values |
| GitHub | GH-M-8: Remove legacy owner | Yes | No | V-GH: Post-verification | Re-invite legacy owner; restore Owner role |
| Slack | P-SL: Preconditions verified | Yes | No | SL-M-1: Transfer Primary Ownership | N/A — no mutation yet |
| Slack | SL-M-1: Transfer Primary Ownership | Yes | No (UI only) | SL-M-2: Update billing contact | New Primary Owner transfers back to legacy |
| Slack | SL-M-2: Update billing contact | Yes | No | SL-M-3: Add collaborator | Revert billing contact email |
| Slack | SL-M-3: Add app collaborator | Yes | Yes (Slack CLI: `slack collaborator add`) | SL-M-4: Remove legacy collaborator | `slack collaborator remove <target-email>` |
| Slack | SL-M-4: Remove legacy collaborator | Yes | Yes (Slack CLI: `slack collaborator remove`) | SL-M-5: Token exchange | Re-add legacy as collaborator |
| Slack | SL-M-5: Exchange long-lived token | Yes | Yes (`oauth.v2.exchange` API call) | SL-M-6: Schedule token refresh | Original token remains valid if exchange not yet called |
| Slack | SL-M-6: Schedule token refresh | Yes | Yes (`oauth.v2.access` API call) | SL-M-7: Verify old token | Retry refresh; reinstall app if token expired |
| Slack | SL-M-7: Verify old token invalidated | Yes | Yes (`auth.test` API call) | V-SL: Post-verification | N/A |
| Discord | P-DC: Preconditions verified | Yes | No | DC-M-1: Transfer server ownership | N/A — no mutation yet |
| Discord | DC-M-1: Transfer server ownership | Yes | No (UI only; 2FA required) | DC-M-2: Transfer app to team (if needed) | New owner manually transfers back to legacy |
| Discord | DC-M-2: Transfer app to team | Yes | No (UI only; irreversible) | DC-M-3: Submit team transfer request | Irreversible — cannot transfer back to individual |
| Discord | DC-M-3: Submit team ownership transfer | Yes | No (Discord Support ticket required for verified apps) | DC-M-4: Reset bot token | Cancel pending request via Discord Support |
| Discord | DC-M-4: Reset bot token | Yes | No (Developer Portal UI; 2FA required) | DC-M-5: Deploy new token | Irreversible — deploy new token to restore bot |
| Discord | DC-M-5: Deploy new token to runtime | Yes | Yes (environment variable update via hosting platform API) | V-DC: Post-verification | Reset token again and redeploy if deployment failed |

---

# 5. OPEN_QUESTIONS_BLOCKING_EXECUTION

The following items are unresolved and must be answered before the migration window can be scheduled. Each is a hard blocker for at least one section of this runbook.

**OQ-1 — GitHub organization name(s)**
The runbook references "the organization" generically. The exact GitHub organization slug must be confirmed so that the correct settings pages and API endpoints are targeted. If multiple organizations exist under the legacy account, each must be listed and addressed individually.

**OQ-2 — GitHub App inventory**
No list of GitHub Apps registered under `truongphillipthanh@icloud.com` has been provided. Each app must be enumerated, including its App ID and installation scope, before Step GH-M-3 can be executed. Apps installed in third-party organizations require those organizations' consent to transfer.

**OQ-3 — GitHub repository inventory and transfer scope**
It is unclear whether all repositories are to be transferred or only a subset. Repository transfers that involve GitHub Marketplace actions or high-volume GitHub Actions usage trigger permanent namespace retirement of the `OWNER/REPOSITORY-NAME` combination. [^gh-repo-transfer] This must be reviewed before execution.

**OQ-4 — GitHub Actions secrets inventory**
Organization-level and environment-level secrets are not transferred automatically with repositories. [^gh-secrets-transfer] A complete secrets inventory must be compiled and the new values must be ready before Step GH-M-7.

**OQ-5 — Slack workspace name and plan tier**
The Slack workspace name and URL (e.g., `yourworkspace.slack.com`) must be confirmed. Additionally, the plan tier must be confirmed as **Business+** or **Enterprise** before the app collaborator management steps (SL-M-3, SL-M-4) can be executed, as this feature is not available on Free or Pro plans. [^sl-collaborators]

**OQ-6 — Slack app inventory and token rotation status**
The names and App IDs of all internal Slack apps managed by the legacy owner must be enumerated. For each app, it must be confirmed whether token rotation is currently enabled, as the token rotation sequence (SL-M-5 through SL-M-7) only applies to apps using the OAuth V2 granular permissions model with rotation enabled. [^sl-token-rotation]

**OQ-7 — Discord server name and member status of target owner**
The Discord server name and Server ID must be confirmed. It must also be confirmed that the target owner's Discord account is already a member of the server, as ownership can only be transferred to an existing member. [^dc-server-transfer]

**OQ-8 — Discord developer team and verified application status**
The Discord Team ID and a list of all applications owned by the team must be provided. If any applications are **verified**, the team ownership transfer process requires a Discord Developer Support ticket, dual-party consent, and a 30–60 day processing window. [^dc-team-transfer] This timeline must be factored into the migration schedule.

**OQ-9 — Discord bot runtime environments**
All environments where the Discord bot token is deployed (e.g., VPS, container orchestration, serverless functions, hosting platforms) must be documented before Step DC-M-4 is executed. Failure to update all environments immediately after the token reset will result in extended bot downtime.

**OQ-10 — Target owner's membership status across all platforms**
It must be confirmed that `syncrescendence@gmail.com` is already an active member of the GitHub organization, the Slack workspace, and the Discord server. If the target owner is not yet a member of any of these platforms, the corresponding onboarding steps must be completed before the cutover window begins.

---

# References

[^gh-org-transfer]: [Transferring organization ownership — GitHub Docs](https://docs.github.com/en/organizations/managing-organization-settings/transferring-organization-ownership)
[^gh-app-transfer]: [Transferring ownership of a GitHub App — GitHub Docs](https://docs.github.com/en/apps/maintaining-github-apps/transferring-ownership-of-a-github-app)
[^gh-billing]: [Managing your payment and billing information — GitHub Docs](https://docs.github.com/en/billing/managing-your-billing/managing-your-payment-and-billing-information)
[^gh-repo-transfer]: [Transferring a repository — GitHub Docs](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository)
[^gh-2fa]: [Requiring two-factor authentication in your organization — GitHub Docs](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-two-factor-authentication-for-your-organization/requiring-two-factor-authentication-in-your-organization)
[^gh-pats]: [Managing your personal access tokens — GitHub Docs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
[^gh-ssh]: [Adding a new SSH key to your GitHub account — GitHub Docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
[^gh-secrets]: [Using secrets in GitHub Actions — GitHub Docs](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)
[^gh-secrets-transfer]: [Most Elegant Way To Transfer Repositories From Personal Account — GitHub Community](https://github.com/orgs/community/discussions/188227) — "Repository-level secrets move with the repo, but Environment secrets and Organization-level secrets do not."
[^sl-transfer]: [Transfer ownership of a workspace or org — Slack Help Center](https://slack.com/help/articles/204401633-Transfer-ownership-of-a-workspace-or-org)
[^sl-collaborators]: [Add internal app collaborators — Slack Help Center](https://slack.com/help/articles/7887743766291-Add-internal-app-collaborators)
[^sl-collab-security]: [Collaborating with teammates — Slack Developer Docs](https://docs.slack.dev/tools/deno-slack-sdk/guides/collaborating-with-teammates/) — "It is therefore recommended that the app owner rotate secrets and tokens after an app collaborator is removed."
[^sl-token-rotation]: [Using token rotation — Slack Developer Docs](https://docs.slack.dev/authentication/using-token-rotation/)
[^dc-server-transfer]: [How to Transfer Ownership of a Discord Server — Discord Support](https://support.discord.com/hc/en-us/articles/216273938-How-to-Transfer-Ownership-of-a-Discord-Server)
[^dc-server-request]: [Requesting a Transfer of Server Ownership — Discord Support](https://support.discord.com/hc/en-us/articles/26286635870359-Requesting-a-Transfer-of-Server-Ownership)
[^dc-teams]: [Teams — Discord Developer Documentation](https://docs.discord.com/developers/topics/teams)
[^dc-team-transfer]: [How to Transfer Ownership of a Developer Team — Discord Developer Support](https://support-dev.discord.com/hc/en-us/articles/34905402845591-How-to-Transfer-Ownership-of-a-Developer-Team)
[^dc-token-reset]: [Why can't I copy my bot's token? — Discord Developer Support](https://support-dev.discord.com/hc/en-us/articles/6470840524311-Why-can-t-I-copy-my-bot-s-token)
