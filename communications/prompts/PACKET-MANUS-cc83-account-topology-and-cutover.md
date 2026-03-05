# PACKET-MANUS-cc83-account-topology-and-cutover

Design an execution-ready account topology and migration plan for this exact three-account state:

1. `truongphillipthanh@icloud.com` (Account 1)
2. `icloud.truongphillipthanh@gmail.com` (Account 2)
3. `truongphillipthanh@gmail.com` (Account 3)

Additional facts:

- paid Google AI Pro student benefits are currently on Account 2
- Claude Pro is currently on Account 1
- `syncrescendence@gmail.com` currently has no paid subscriptions
- active migration goal is to centralize organization control-plane ownership without operational downtime

## Required output

Return these sections:

1. `ACCOUNT_ROLE_TOPOLOGY`
   - define canonical roles for Account 1/2/3 and `syncrescendence@gmail.com`
   - include which account should own billing vs control-plane vs break-glass
2. `TARGET_END_STATE`
   - explicit final target mapping per platform family:
     - GitHub
     - Slack
     - Discord
     - Cloudflare
     - Google Workspace/GCP/YouTube
     - Claude/OpenAI/Gemini model subscriptions
     - exocortex SaaS set
3. `MIGRATION_SEQUENCING`
   - phased steps with preconditions, mutation actions, verification, rollback
4. `PAID_SUBSCRIPTION_STRATEGY`
   - how to preserve paid benefits while moving operational control
   - what should remain on Account 2 vs move to `syncrescendence@gmail.com`
5. `RISK_REGISTER`
   - specific risks from multi-account sprawl and failure modes
6. `OPERATOR_CHECKLIST`
   - concise checklist that a human operator can execute in order

## Constraints

1. no credentials
2. no destructive actions
3. evidence-backed claims only where possible
4. output must be directly usable for repo runbook updates
