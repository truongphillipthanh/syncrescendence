# EXOCORTEX-CENTRALIZATION-LEDGER

**Project:** Syncrescendence Account Centralization — CC82
**Prepared:** 2026-03-05
**Format:** Machine-readable Markdown table (CSV-compatible columns)

---

## Ledger

This ledger is the single source of truth for ownership centralization state across all Syncrescendence platform surfaces. Update the `state` column as each migration step is completed. Valid state values are: `NOT_STARTED`, `IN_PROGRESS`, `BLOCKED`, `COMPLETE`, `ROLLED_BACK`.

| platform | current_owner_surface | target_owner_surface | state | risk | next_action |
|---|---|---|---|---|---|
| GitHub (Org) | truongphillipthanh@icloud.com | syncrescendence@gmail.com | NOT_STARTED | LOW | Add syncrescendence@gmail.com as org Owner; update billing; remove legacy account. Ref: GITHUB-CUTOVER-TRACK §2. |
| GitHub (Repos) | truongphillipthanh@icloud.com | syncrescendence@gmail.com (org) | NOT_STARTED | LOW | Enumerate personal repos; transfer each to org via Danger Zone. Ref: GITHUB-CUTOVER-TRACK §3. |
| GitHub (Actions/CI) | truongphillipthanh@icloud.com | syncrescendence@gmail.com | NOT_STARTED | MEDIUM | Audit all org and repo secrets; rotate PATs; update workflow secrets. Ref: GITHUB-CUTOVER-TRACK §4. |
| Slack (Workspace) | truongphillipthanh@icloud.com | syncrescendence@gmail.com | NOT_STARTED | LOW | Current Primary Owner transfers ownership via Admin UI. Ref: SLACK-DISCORD-FOCUSED-CUTOVER §1.1. |
| Slack (Apps) | truongphillipthanh@icloud.com | syncrescendence@gmail.com | NOT_STARTED | HIGH | Complete app inventory; recreate apps under new account; rotate tokens. Ref: SLACK-DISCORD-FOCUSED-CUTOVER §1.3. BLOCKED pending inventory. |
| Discord (Server) | truongphillipthanh@icloud.com | syncrescendence@gmail.com | NOT_STARTED | LOW | Current server owner transfers via Server Settings → Members. Ref: SLACK-DISCORD-FOCUSED-CUTOVER §2.1. |
| Discord (Dev Team/Apps) | truongphillipthanh@icloud.com | syncrescendence@gmail.com | NOT_STARTED | HIGH | Submit support ticket to Discord; 30–60 day process; dual-party consent required. Ref: SLACK-DISCORD-FOCUSED-CUTOVER §2.2. INITIATE IMMEDIATELY. |
| Discord (Bot Tokens) | truongphillipthanh@icloud.com | syncrescendence@gmail.com | NOT_STARTED | MEDIUM | Reset bot token in Developer Portal after team transfer; update all consumers. Ref: SLACK-DISCORD-FOCUSED-CUTOVER §2.3. |
| Cloudflare (DNS/Zones) | truongphillipthanh@icloud.com | syncrescendence@gmail.com | NOT_STARTED | MEDIUM | Export DNS records; add domain to new account; update nameservers at registrar; reissue SSL. Ref: MIGRATION-CEREMONY-RUNBOOK Wave 1. |
| Cloudflare (Registrar) | truongphillipthanh@icloud.com | syncrescendence@gmail.com | NOT_STARTED | MEDIUM | If domain registered via Cloudflare Registrar, follow inter-account domain registration transfer process. Ref: Cloudflare Registrar docs. |
| Google Workspace (Super Admin) | truongphillipthanh@icloud.com | syncrescendence@gmail.com | NOT_STARTED | LOW | Assign Super Admin role to syncrescendence@gmail.com via Admin console. Ref: MIGRATION-CEREMONY-RUNBOOK Wave 3. |
| GCP (Project Owner) | truongphillipthanh@icloud.com | syncrescendence@gmail.com | NOT_STARTED | LOW | Add Owner IAM binding for new account; transfer billing account link. Ref: MIGRATION-CEREMONY-RUNBOOK Wave 3. |
| YouTube (Channel) | truongphillipthanh@icloud.com | syncrescendence@gmail.com | NOT_STARTED | MEDIUM | Convert channel to Brand Account if needed; add new account as Manager; remove legacy account. Ref: MIGRATION-CEREMONY-RUNBOOK Wave 3. |
| Notion (Workspace) | truongphillipthanh@icloud.com | syncrescendence@gmail.com | NOT_STARTED | LOW | Change email on existing Notion account from legacy to target. Settings → My Account → Change email. Ref: MIGRATION-CEREMONY-RUNBOOK Wave 4. |
| Coda (Workspace/Docs) | truongphillipthanh@icloud.com | syncrescendence@gmail.com | NOT_STARTED | LOW | Transfer doc ownership per doc via Share → Make Owner; transfer workspace ownership via admin panel. Ref: MIGRATION-CEREMONY-RUNBOOK Wave 4. |
| Confluence (Org Admin) | truongphillipthanh@icloud.com | syncrescendence@gmail.com | NOT_STARTED | MEDIUM | Assign org admin role via admin.atlassian.com → Directory → Users. Ref: MIGRATION-CEREMONY-RUNBOOK Wave 4. |
| Jira (Org Admin) | truongphillipthanh@icloud.com | syncrescendence@gmail.com | NOT_STARTED | MEDIUM | Shared with Confluence under Atlassian org admin. Same action covers both. Ref: MIGRATION-CEREMONY-RUNBOOK Wave 4. |
| Linear (Workspace) | truongphillipthanh@icloud.com | syncrescendence@gmail.com | NOT_STARTED | LOW | Transfer workspace ownership via Settings → Members. Ref: MIGRATION-CEREMONY-RUNBOOK Wave 4. |
| ClickUp (Workspace) | truongphillipthanh@icloud.com | syncrescendence@gmail.com | NOT_STARTED | LOW | Transfer workspace ownership via Settings → People → Transfer Ownership. Ref: MIGRATION-CEREMONY-RUNBOOK Wave 4. |
| Basecamp (Account) | truongphillipthanh@icloud.com | syncrescendence@gmail.com | NOT_STARTED | MEDIUM | Add new account as Administrator; contact Basecamp support for primary owner transfer if self-service is unavailable. Ref: MIGRATION-CEREMONY-RUNBOOK Wave 4. |
| Airtable (Workspace/Bases) | truongphillipthanh@icloud.com | syncrescendence@gmail.com | NOT_STARTED | MEDIUM | Transfer workspace ownership via Enterprise admin panel; transfer base ownership per base. Ref: MIGRATION-CEREMONY-RUNBOOK Wave 4. |

---

## Risk Legend

| Risk Level | Meaning |
|---|---|
| LOW | Well-documented, self-service, immediately reversible. No external dependencies. |
| MEDIUM | Requires careful sequencing, external dependencies (registrar, support tickets), or has non-trivial rollback complexity. |
| HIGH | Long lead time, dual-party consent, or loss of service state (e.g., app verification) during transition. Requires advance planning. |

---

## State Update Instructions

Update the `state` column in this ledger as each migration step progresses. When a step is `IN_PROGRESS`, add the operator's name and start date in the `next_action` column. When a step is `COMPLETE`, record the completion date. When a step is `BLOCKED`, record the blocking reason and the resolution path.
