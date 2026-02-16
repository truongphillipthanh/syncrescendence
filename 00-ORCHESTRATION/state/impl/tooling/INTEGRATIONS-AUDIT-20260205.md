# INTEGRATIONS-AUDIT — 2026-02-05

Purpose: record the *actual* incumbent SaaS interconnections observed/configured via native integrations.

> Note: this is a snapshot, not a policy. Teleology + orchestration recommendations live in the Clarescence record referenced below.

## Verified (via UI)

### Linear (workspace: Syncrescendence)
- Integrations → Enabled:
  - GitHub (enabled)
  - Notion (enabled)
- Connected accounts (user-level):
  - Slack: Connected (personal account attribution) ✅
  - GitHub: Connected ✅
  - Google Calendar: Connected ✅
  - Notion: Connected ✅
- Slack integration (workspace-level):
  - Workspace connection shows as Connected ✅
  - Linear Agent: Enabled for Syncrescendence workspace ✅
  - Linkbacks / Unfurls available (left at defaults; needs later policy pass for channel membership + privacy posture).

### GitHub (user: truongphillipthanh)
- Settings → Installed GitHub Apps includes:
  - Linear ✅
  - Notion Workspace ✅
  - Claude ✅
  - ChatGPT Codex Connector ✅
  - Vercel ✅

## Partially verified / pending deeper configuration

### Slack (workspace: Syncrescendence)
- Linear app installation + authorization was completed as part of Linear Slack integration.
- Pending: decide channel routing rules (which channels receive which Linear events) and whether Slack should be the *operational bus* for meta-work or only notifications.

### ClickUp
- Able to access workspace and settings UI.
- Blocker encountered: ClickUp settings “App Center” / integrations surfaces are heavy and caused browser control timeouts; requires a dedicated pass (possibly fewer open tabs; or using Chrome relay extension).

### Discord
- Logged in (web). No integration changes made yet.

### Make
- Logged in (dashboard reachable). No scenarios audited/created in this pass.

### Dropbox / Box / Outlook (Microsoft)
- Logged in; no integration changes made in this pass.

### Airtable / Notion (direct)
- Logged in; no workspace-level integration tightening performed beyond Linear→Notion.

## Next concrete steps (execution)
1) ClickUp: open App Center → verify/install GitHub + Slack + (if needed) Linear/Notion connectors.
2) Slack: decide the canonical notification channel(s) and configure Linear team notifications accordingly.
3) Discord: decide whether Discord is only Ajna habitat, or also receives system notifications; then install GitHub/Linear bots accordingly.
4) Make: map automation lanes (Linear↔ClickUp cross-posting, GitHub→Slack, etc.) once Cowork finalizes policy.

## Related
- Clarescence record (teleology / orchestration):
  - `00-ORCHESTRATION/state/impl/clarescence/CLARESCENCE-2026-02-05-incumbent-saas-teleology.md`
