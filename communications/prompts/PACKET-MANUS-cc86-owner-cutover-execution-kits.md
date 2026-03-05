# PACKET-MANUS-cc86-owner-cutover-execution-kits

Produce a deterministic owner-cutover execution kit for this environment.

Context:

1. Canonical control-plane target owner is `syncrescendence@gmail.com`.
2. Account-role decision already established:
   - `syncrescendence@gmail.com` = control-plane owner
   - `icloud.truongphillipthanh@gmail.com` = billing/benefit anchor (retain non-transferable plans)
   - `truongphillipthanh@icloud.com` = break-glass during migration window
3. Current runbooks and trackers:
   - `orchestration/state/impl/CC81-IDENTITY-CUTOVER-RUNBOOK-v1.md`
   - `orchestration/state/IDENTITY-CUTOVER-TRACKER-CC81.json`
   - `orchestration/state/EXOCORTEX-CENTRALIZATION-LEDGER-CC82.json`
   - `orchestration/state/impl/ACCOUNT-TOPOLOGY-DECISION-CC83.md`

Required output:

1. `WAVE1_CONTROL_PLANE_KIT`
   - GitHub
   - Cloudflare
   - GCP / Google Cloud IAM
2. `WAVE2_OPERATOR_BUS_KIT`
   - Slack
   - Discord
3. For each platform include:
   - Prechecks (must-pass gates)
   - Exact owner/admin promotion steps
   - Verification probes (owner-only actions)
   - Rollback steps
   - Token/integration rotation scope after transfer
   - Evidence artifacts to capture in repo-safe form
   - Failure signatures and immediate recovery actions
4. Include a strict mutation order with hold points between platforms.
5. Include a `SOVEREIGN_OPERATOR_CHECKLIST` that is short and executable.

Constraints:

1. Do not assume local shell access.
2. Treat this as human-in-the-loop browser/admin-console execution.
3. Keep billing/benefit migration conservative; do not force subscription churn in this wave.
4. Prefer deterministic, auditable, reversible steps.

Output format:

1. Markdown.
2. Top-level sections exactly:
   - `WAVE1_CONTROL_PLANE_KIT`
   - `WAVE2_OPERATOR_BUS_KIT`
   - `MUTATION_ORDER_AND_HOLDS`
   - `SOVEREIGN_OPERATOR_CHECKLIST`
   - `RISKS_AND_FAILURE_SIGNATURES`
