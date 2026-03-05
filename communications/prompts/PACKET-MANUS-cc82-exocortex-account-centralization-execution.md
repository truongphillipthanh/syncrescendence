# PACKET-MANUS-cc82-exocortex-account-centralization-execution

You are helping execute account centralization for Syncrescendence.

## Core objective

Migrate operational ownership from legacy account surfaces (primarily `truongphillipthanh@icloud.com`) to:

`syncrescendence@gmail.com`

for the exocortex and control plane.

## Priority surfaces

1. GitHub (repo/org/billing)
2. Slack (workspace ownership, app ownership, token lifecycle)
3. Discord (server ownership, developer team/app ownership, bot control)
4. Cloudflare/domain authority
5. Google Workspace/GCP/YouTube
6. Exocortex suite: Notion, Coda, Confluence, Jira, Linear, ClickUp, Basecamp, Airtable

## Constraints

1. No destructive actions.
2. No credentials.
3. No tenant logins.
4. Evidence-backed references only (official docs where possible).
5. Output should be directly executable by a small operator team.

## Required output

1. `MIGRATION-CEREMONY-RUNBOOK`
   - explicit wave-by-wave checklist including:
     - preconditions
     - owner mutation step
     - post-verification step
     - rollback step
2. `AUTOMATION-VS-HUMAN-MATRIX`
   - for each platform: `api_automatable`, `human_owner_required`, `blocking_unknowns`
3. `SLACK-DISCORD-FOCUSED-CUTOVER`
   - detailed steps for workspace/server + app/bot ownership and token rotation
4. `GITHUB-CUTOVER-TRACK`
   - org role transfer + billing/control validations
5. `EXOCORTEX-CENTRALIZATION-LEDGER`
   - machine-readable table (markdown or csv-friendly) with columns:
     - `platform`
     - `current_owner_surface`
     - `target_owner_surface`
     - `state`
     - `risk`
     - `next_action`
6. `OPEN-QUESTIONS`
   - unresolved items that block cutover execution.

## Success condition

Produce a concrete execution package that can be dropped into the CC81 tracker/runbook and immediately run.
