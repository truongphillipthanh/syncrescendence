# CLARESCENCE RECORD — Incumbent SaaS Stack Teleology (2026-02-05)

**Trigger**: Phillip directive to interconnect incumbent SaaS stack (Linear, ClickUp, Slack, Discord, GitHub, Airtable, Notion, Dropbox, Box, GSuite, Make, Microsoft/Outlook) and provide a holistic teleology + orchestration posture.

**Scope**: This record is a *systems* recommendation: role boundaries, truth surfaces, routing semantics, and orchestration patterns. It avoids vendor-specific minutiae unless they create hard constraints.

---

## 1) Intent (what this stack is for)

### Primary intent
A two-layer execution substrate:
- **Linear** = tasks “on the corpus/repo” (work that must land as repo-ground-truth artifacts)
- **ClickUp** = tasks “meta to the corpus/repo” (operations, business, coordination, externalities)

### Secondary intent
- **Slack / Discord** = living interaction surfaces (where agent/human collaboration actually happens)
- **GitHub** = authoritative code-change surface + CI signal plane
- **Make** = glue + event router (automation layer), not a source of truth
- **Airtable / Notion** = structured knowledge + planning dashboards (should not compete with repo truth)
- **Drive/Dropbox/Box/Outlook** = inbound/outbound peripheral surfaces; should be absorbed into the dispatch substrate without becoming competing task-truth.

---

## 2) Truth surfaces (avoid double-truth)

### Recommendation: explicit “one owner per truth axis”

- **Repo (syncrescendence)**
  - owns: Canon, Orchestration specs, DecisionAtoms, ledgers/logs, executable scripts, durable receipts.
  - style: append-only where possible (ledgers), deterministic artifacts.

- **Linear**
  - owns: *execution commitments* for repo-bound work (issue lifecycle, assignees, projects/milestones).
  - must not own: canonical technical specs (those must live in repo).

- **ClickUp**
  - owns: meta-work commitments (ops, outreach, finance, admin, partnerships) + “coordination obligations” that don’t map to repo artifacts.

- **Slack/Discord**
  - owns: conversational state, alerts, and lightweight operational coordination.
  - must not own: long-lived specs or canonical task state.

- **Make**
  - owns: automation DAGs *only*; treat as replaceable.

- **Notion/Airtable**
  - owns: dashboards, catalog views, curated knowledge that is useful to browse.
  - must not own: final canonical definitions that change frequently.

### Failure mode to avoid
If Linear/ClickUp/Notion/Airtable each separately track “the same task,” you get drift. So:
- choose a **single “execution state owner”** per task (Linear OR ClickUp),
- allow other tools to mirror as read-only views.

---

## 3) Teleology per platform (role assignments)

### GitHub
- “Code reality.”
- Should emit events to:
  - Linear (PR links, close-on-merge semantics, review status)
  - Slack/Discord (alerts)
- Do not attempt GitHub→ClickUp as a primary path unless ClickUp is truly owning that task.

### Linear
- “Repo work contract.”
- Use GitHub integration for:
  - linkbacks, PR/commit association, branch name format
  - optional GitHub Issues sync only if you decide to treat GitHub Issues as an *external intake* surface (not recommended as primary).
- Use Slack integration for:
  - creation-from-message, unfurls, thread sync
  - notifications configured per Linear Team → Slack channel.

### ClickUp
- “Meta execution plane.”
- Best practice: keep ClickUp tasks describing outcomes, not duplicating repo patch details.
- Integrate with Slack for:
  - notifications + lightweight create-from-Slack where appropriate.

### Slack
- “Psyche habitat / operational bus.”
- Recommendation: one canonical channel for system alerts (e.g. `#all-syncrescendence`) + per-lane channels only if noise becomes too high.

### Discord
- “Ajna habitat / swarm staging.”
- Recommendation: Discord is *not* the primary notification sink initially; use it for agent-facing operations and route only high-signal alerts there.

### Notion
- “Readable wiki + meeting/strategy.”
- Use for:
  - curated briefs, narrative synthesis, dashboards
- Avoid using it as the live task-state owner.

### Airtable
- “Structured inventory / catalog + lightweight CRM-ish substrate.”
- Use for:
  - catalogs (tools, vendors, contacts, assets)
  - maps that need flexible relational views

### Make
- “Automation router.”
- Use for:
  - event fan-out (GitHub→Slack, Linear→Slack)
  - optional mirroring (Linear→ClickUp create meta-tasks; ClickUp→Linear linkbacks)
- Avoid Make owning any canonical data.

### Dropbox / Box / Google Drive
- Recommendation: pick **one** as primary file substrate for operational documents; the rest become bridges.
  - If you keep all three, you must define which is canonical to avoid duplicated file truth.

### Microsoft Outlook
- Treat as an external comms surface; pull “actionable obligations” into ClickUp (meta) or Linear (repo) by explicit policy.

---

## 4) Orchestration pattern (how this becomes a system)

### Event vocabulary (align with ledger/event set)
Use the same high-level events across surfaces:
- DISPATCH, CLAIM, COMPLETE, FAILED, BLOCKED, RESULT, DECISION, REGEN, COMPACT

### Routing principles
- **Repo-bound work**:
  - Slack/Discord message → (optional) Linear issue created → dispatch packet in repo → watcher executes → RESULT/receipt → Linear updated/closed.

- **Meta work**:
  - Slack/Discord/Email → ClickUp task → (optional) repo note if it affects Canon/Orchestration → completion logged.

### Minimal viable automation (MV-A)
1) GitHub → Linear linking (already in place)
2) Linear → Slack (creation + notifications)
3) GitHub → Slack high-signal (PR opened/merged, CI red)
4) (Optional) Linear → ClickUp mirroring only for select meta tags/projects.

---

## 5) Recommendations / “two cents” (opinionated)

1) **Slack is the operational bus; Discord is a lane habitat.** Don’t try to make both equal sinks.
2) **Make is the router, not the brain.** All durable automation intent should be spec’d in repo, then implemented in Make.
3) **Pick a canonical file substrate.** If you keep Dropbox + Box + Drive simultaneously, you’ll get file-truth drift.
4) **Stop tool creep with explicit purpose tags.** Every tool needs a one-line role and a “what it must never own.”
5) **Mirror read-only; reconcile in one place.** Linear owns repo-work state; ClickUp owns meta state.

---

## 6) Concrete follow-on actions (repo-level)

- Add an “Integration hooks” section to `DYN-DISPATCH_KANBAN_PROTOCOL.md` enumerating:
  - which SaaS subscribes to which event types
  - which channel(s) are the notification sinks
  - what metadata is required for cross-linking

- Produce a `DYN-INCUMBENT_SAAS_STACK.md` with:
  - tool roles, truth axes, and routing rules
  - “canonical vs cache” statement for each

---

## References
- Integration audit snapshot:
  - `orchestration/state/impl/tooling/INTEGRATIONS-AUDIT-20260205.md`
