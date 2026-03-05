# PACKET-MANUS-cc82b-github-slack-discord-cutover-runbook

Produce an execution-ready cutover runbook for ownership migration from:

- legacy owner surface: `truongphillipthanh@icloud.com`
- target owner surface: `syncrescendence@gmail.com`

Focus only on:

1. GitHub ownership/billing/control
2. Slack workspace/app/token migration
3. Discord server/app/bot migration

## Constraints

1. Evidence-backed steps only (official docs and references where possible).
2. No credentials.
3. No destructive actions.
4. Must include rollback path for each mutation step.

## Output format

Return exactly these sections:

1. `GITHUB_CUTOVER_CHECKLIST`
   - preconditions
   - mutation steps
   - post-verification
   - rollback
2. `SLACK_CUTOVER_CHECKLIST`
   - workspace owner/admin transfer
   - Slack app ownership/governance transition
   - token rotation sequence and reauthorization checks
   - rollback
3. `DISCORD_CUTOVER_CHECKLIST`
   - server ownership/admin transfer
   - developer app/team ownership transfer
   - bot token rotation and runtime verification
   - rollback
4. `MACHINE_READABLE_LEDGER_ROWS`
   - markdown table with columns:
     - `platform`
     - `state`
     - `human_action_required`
     - `api_automatable`
     - `next_step`
     - `rollback_step`
5. `OPEN_QUESTIONS_BLOCKING_EXECUTION`
   - unresolved blocking items only.

## Success condition

The output can be used immediately by a small operator team in one controlled migration window.
