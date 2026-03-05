# PACKET-MANUS-cc86b-owner-cutover-kits-inline

Generate a deterministic, human-executable owner cutover kit.

Hard context:

1. Target control-plane identity: `syncrescendence@gmail.com`.
2. Keep non-transferable benefits on `icloud.truongphillipthanh@gmail.com` for now.
3. Keep `truongphillipthanh@icloud.com` as temporary break-glass during migration.
4. Do not force subscription churn in this wave.
5. Output must be browser/admin-console executable, with explicit verification and rollback.

Required sections (exact names):

1. `WAVE1_CONTROL_PLANE_KIT`
2. `WAVE2_OPERATOR_BUS_KIT`
3. `MUTATION_ORDER_AND_HOLDS`
4. `SOVEREIGN_OPERATOR_CHECKLIST`
5. `RISKS_AND_FAILURE_SIGNATURES`

Platforms to include:

1. Wave 1: GitHub, Cloudflare, GCP IAM
2. Wave 2: Slack, Discord

For each platform include:

1. prechecks (must-pass)
2. exact owner/admin promotion steps
3. owner-only verification probes
4. rollback procedure
5. token/integration rotation scope
6. evidence artifacts to capture (pointer-only, no secrets)
7. failure signatures + immediate recovery action

Constraints:

1. No local shell assumptions.
2. Deterministic and auditable.
3. Reversible wherever possible.
4. Keep answer concrete, operational, and concise.
