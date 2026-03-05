# AUTOMATION-VS-HUMAN-MATRIX

**Project:** Syncrescendence Account Centralization — CC82
**Prepared:** 2026-03-05

---

## Overview

This matrix classifies each platform surface by its degree of automation support for ownership transfer operations. The three columns represent: whether the operation can be fully or partially automated via API (`api_automatable`), whether a human account owner must be physically present and authenticated to complete the transfer (`human_owner_required`), and any known unknowns that would block execution without resolution (`blocking_unknowns`).

The matrix is intended to guide the operator team in sequencing work and identifying where engineering effort on automation is warranted versus where manual ceremony is unavoidable.

| Platform | `api_automatable` | `human_owner_required` | `blocking_unknowns` |
|---|---|---|---|
| **GitHub** | **Partial.** Member role assignment and removal can be scripted via the GitHub REST API (`PUT /orgs/{org}/memberships/{username}`). Billing contact update requires UI. Repository transfers can be triggered via API (`POST /repos/{owner}/{repo}/transfer`). | **Yes.** The current owner must be authenticated. Billing update requires UI interaction by the new owner. | None identified. Process is well-documented. |
| **Slack (Workspace)** | **No.** The Primary Ownership transfer has no API endpoint. It is a UI-only operation. | **Yes.** Only the current Primary Owner can initiate the transfer. They must be authenticated and enter their password. | If the Primary Owner account is inaccessible, a Slack Support request is required and is not guaranteed to be approved. |
| **Slack (Apps/Tokens)** | **Partial.** Token rotation can be automated via the `tooling.tokens.rotate` API method. App reinstallation can be scripted. | **Yes.** App recreation (where ownership transfer is not supported) requires a human to configure and install the new app. | Full inventory of all Slack apps and their individual ownership/transferability status is required before execution. |
| **Discord (Server)** | **No.** Server ownership transfer is a UI-only operation in Server Settings. | **Yes.** The current server owner must be authenticated and perform the transfer manually. | None identified. |
| **Discord (Dev Team/Apps)** | **No.** Developer team ownership transfer requires a formal support ticket to Discord. No API path exists. | **Yes.** Both the current owner and the receiving account must respond to Discord's consent requests within 30 days. | (1) Verified apps will lose verification status during transfer; re-verification timeline is unknown. (2) The 90-day cooldown period between transfer requests per developer product must be respected. (3) All team members and apps must be in good standing. |
| **Cloudflare** | **Partial.** DNS record export and recreation can be automated via the Cloudflare API. Zone creation in the new account can be scripted. | **Yes.** Nameserver updates must be performed at the domain registrar, which typically requires UI interaction. If using Cloudflare Registrar, an inter-account domain registration transfer requires manual confirmation from both accounts. | SSL/TLS certificates do not transfer and must be reissued. Custom certificates must be manually migrated. |
| **Google Workspace** | **Partial.** The Super Admin role can be assigned via the Admin SDK Directory API (`POST /admin/directory/v1/users/{userKey}/makeAdmin`). | **Yes.** The current Super Admin must be authenticated to initiate the role assignment. | If the current Super Admin account is inaccessible, account recovery via Google's identity verification process is required. |
| **GCP** | **Yes.** IAM role bindings can be fully managed via the `gcloud` CLI or the Resource Manager API (`POST /v1/projects/{resource}:setIamPolicy`). Billing account linkage can be changed via the Billing API. | **Yes.** The current project Owner must authorize the initial IAM change. | None identified. |
| **YouTube** | **No.** Brand Account manager assignment is a UI-only operation via Google Account settings. | **Yes.** The current channel owner must be authenticated to add the new manager and remove the old one. | If the channel is not yet a Brand Account, a conversion step is required first. |
| **Notion** | **Partial.** The Notion API supports user provisioning and workspace management. However, the account email change (the recommended migration path) is a UI-only operation. | **Yes.** The account holder must be authenticated to change their email address. | Private pages not shared with the workspace may not be accessible after the email change if the account is deprovisioned. Inventory of private content is required. |
| **Coda** | **Partial.** The Coda API supports doc and workspace management. Doc ownership transfer is a UI operation per document. | **Yes.** The current doc owner must be authenticated to transfer each doc. | No known bulk-transfer API for doc ownership. Large numbers of docs may require significant manual effort. |
| **Confluence / Jira (Atlassian)** | **Partial.** The Atlassian Admin API supports user and role management. Org admin role assignment can be scripted. | **Yes.** The current org admin must be authenticated to assign the new admin role. | If the current admin is unavailable, a 3-day Atlassian Support escalation process is required. Content ownership (pages, projects) is separate from org admin and may require additional bulk-transfer steps. |
| **Linear** | **Partial.** Linear's GraphQL API supports member role management. Workspace ownership transfer itself is a UI operation. | **Yes.** The current workspace owner must be authenticated to transfer ownership. | None identified. |
| **ClickUp** | **Partial.** The ClickUp API supports user and workspace management. Workspace ownership transfer is a UI operation. | **Yes.** The current workspace owner must be authenticated to transfer ownership. | None identified. |
| **Basecamp** | **Partial.** The Basecamp API supports user and account management. Account owner transfer may require contacting Basecamp support. | **Yes.** The current account owner must be authenticated. | The exact self-service path for Basecamp account owner transfer is not clearly documented; support contact may be required. |
| **Airtable** | **Partial.** The Airtable API supports workspace and base management. Enterprise admins can transfer workspace ownership via the admin panel. Base ownership transfer is a UI operation per base. | **Yes.** The current workspace/base owner must be authenticated. | No known bulk-transfer API for base ownership. Enterprise plan required for admin panel workspace ownership transfer. |

---

## Summary Assessment

The majority of ownership transfers in this migration are **human-required, UI-driven operations**. The platforms with the most automation potential for supporting tasks (DNS, IAM, user provisioning) are Cloudflare, GCP, and Atlassian. The platforms with the highest manual burden and longest lead times are **Discord Developer Team** (30–60 day support process) and **Slack App ownership** (requires app recreation and token rotation across all integrations).

The operator team should prioritize resolving the blocking unknowns for Discord and Slack apps before scheduling those waves.
