# PACKET-MANUS-cc81-identity-cutover-capability-development

You are assisting Syncrescendence with a controlled account centralization.

## Objective

Determine how much of the migration from legacy identity surfaces to `syncrescendence@gmail.com` can be automated safely, and what must remain human-owner actions.

## Scope

- GitHub ownership and billing transfer
- Cloudflare/domain ownership transfer
- Google workspace/GCP ownership transfer
- Slack workspace/app ownership transfer
- Discord server/app/bot ownership transfer
- Exocortex platforms (Notion, Coda, Confluence, Linear, Jira, ClickUp, Basecamp, Airtable)

## Hard Constraints

1. No destructive actions.
2. No credential requests.
3. No login attempts into private tenant data.
4. Treat this as capability development + migration design only.
5. Output must be evidence-grounded and cite official docs URLs.

## Required Output

Produce a markdown report with these sections:

1. **Automation Envelope Matrix**
   Columns: `platform`, `can_automate_now`, `must_be_human_owner`, `risk_level`, `why`.
2. **Pre-Cutover Snapshot Checklist**
   Exact artifacts to capture before any owner mutation.
3. **Rollback Design**
   For each platform, list rollback prerequisites and time window considerations.
4. **Order of Operations**
   A lowest-risk sequence for platform cutover.
5. **Post-Cutover Verification Tests**
   Deterministic checks that prove ownership/control has moved correctly.
6. **Open Questions**
   Unknowns that still require manual confirmation.

## Success Condition

We receive a practical migration capability report that can be turned into executable runbooks without hidden assumptions.
