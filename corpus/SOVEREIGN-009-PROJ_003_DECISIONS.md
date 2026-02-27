# SOVEREIGN-009: PROJ-003 Stack Disposition Decisions

**Filed**: 2026-02-02
**Filed By**: Commander (Claude Code, Opus 4.5)
**Status**: RESOLVED
**Resolved**: 2026-02-10
**Priority**: P0 — These 5 decisions unblock PROJ-006 (Ontology), which unblocks PROJ-007 (Curriculum), PROJ-005 (Branding), and the entire downstream pipeline.
**Source**: REF-STACK_TELEOLOGY.md analysis + repository state audit

---

## WHY THIS MATTERS

PROJ-003 (Tooling Stack) is at 40%. It cannot close until you ratify tool dispositions. PROJ-006 (Ontology — the "Final Boss") is blocked by PROJ-003. Everything downstream — curriculum, branding, feedcraft, research pipeline execution — is blocked by the ontology.

**These 5 decisions are the single highest-leverage action you can take right now.**

---

## DECISION 1: Task Management

**Question**: What is the primary task management surface?

| Option | Strengths | Weaknesses | Verdict |
|--------|-----------|------------|---------|
| **Linear** | API-first, queryable, engineering-grade, feeds into Palantir ontology, team-scalable | $8/mo, another subscription, learning curve | Best long-term — API-first means it integrates with everything |
| **Things 3** | Native macOS, fast capture, already active on Mac mini, OpenClaw `things` CLI skill | No API, no queryable database, personal-only, no web | Best for daily personal tasks but dead-end for ontology |
| **OpenClaw cron** | Free, already running, persistent, multi-channel | Not a PM tool — no Kanban, no sprint, no structured views | Supplement, not primary |

**Recommendation**: **Linear for projects + Things for personal daily tasks + OpenClaw for reminders/cron**. Linear's API feeds directly into the ontology database. Things handles quick personal capture. OpenClaw handles time-based triggers.

**Your call**: [ ] Linear + Things + OpenClaw (recommended) / [ ] Things only / [ ] Linear only / [ ] Other: ___

---

## DECISION 2: PKM (Primary Knowledge Management)

**Question**: What is the primary PKM surface beyond the git repository?

| Option | Strengths | Weaknesses | Verdict |
|--------|-----------|------------|---------|
| **Obsidian** | Already active, CANON lives here, graph mode = accretion test, local-first, git-tracked, OpenClaw skill | No relational database, no API, limited query | Winner for knowledge graph |
| **Notion** | Relational databases, API, views/filters, Cowork MCP App candidate | Cloud-dependent, not local-first, vendor lock-in | Winner for structured data / dashboards |
| **DEVONthink** | AI classification, document management, macOS-native | Learning curve, no collaboration, expensive | Overkill unless you need document AI |

**Recommendation**: **Obsidian primary (knowledge graph) + Notion for structured dashboards**. Obsidian owns the CANON graph. Notion provides the relational database layer that Obsidian can't — IIC dashboards, model comparison tables, project tracking views. DEVONthink deferred unless a specific use case emerges.

**Your call**: [ ] Obsidian + Notion (recommended) / [ ] Obsidian only / [ ] Notion primary / [ ] Other: ___

---

## DECISION 3: Cloud Storage Consolidation

**Question**: Sunset Dropbox and Box?

| Service | Current Usage | Recommendation |
|---------|--------------|----------------|
| **Google Drive** | Active — Gemini Gems live-sync, Account 3 primary | KEEP (essential for Gemini integration) |
| **iCloud** | Active — Apple device sync, Account 1 substrate | KEEP (system-level, not project-level) |
| **Dropbox** | Unknown / legacy | SUNSET — redundant with Drive |
| **Box** | Cowork MCP App only | SUNSET — no other use case |

**Recommendation**: **Consolidate to Google Drive + iCloud. Sunset Dropbox and Box.** If any files remain in Dropbox, migrate to Drive first.

**Your call**: [ ] Sunset both (recommended) / [ ] Keep Dropbox / [ ] Keep Box / [ ] Other: ___

---

## DECISION 4: Quick AI Queries

**Question**: Raycast AI or OpenClaw for ad-hoc AI queries?

| Option | Strengths | Weaknesses |
|--------|-----------|------------|
| **Raycast AI** | GUI launcher, fast hotkey, visual snippets | Another subscription ($8/mo), overlaps with OpenClaw |
| **OpenClaw** | Already running, persistent context, free, multi-channel | Slower for quick GUI queries, no visual snippet preview |

**Recommendation**: **OpenClaw for AI queries. Keep Raycast as launcher only (free tier).** OpenClaw's persistent context and memory make it superior for queries that benefit from history. Raycast stays as a macOS launcher (free), not an AI surface.

**Your call**: [ ] OpenClaw + Raycast free tier (recommended) / [ ] Raycast AI (paid) / [ ] OpenClaw only / [ ] Other: ___

---

## DECISION 5: Setapp Subscription

**Question**: Keep or cancel Setapp?

**Current state**: No inventory of which Setapp apps you actually use. Before deciding, you need to audit.

**Quick audit method**: Open Setapp → Settings → My Apps → screenshot the list. Or run:
```bash
ls /Applications/ | grep -i setapp
```

**Recommendation**: **Audit first, then cancel.** Most Setapp apps fall into categories now covered by OpenClaw + native macOS + existing tools:
- Text editors → Claude Code / VS Code / native
- Note taking → Obsidian / Apple Notes / OpenClaw memo
- Task management → Things / Linear (if selected)
- Automation → OpenClaw + Keyboard Maestro + Hazel
- Utilities → Most have free alternatives or macOS native equivalents

**Your call**: [ ] Run audit and report back / [ ] Cancel immediately / [ ] Keep for now / [ ] Other: ___

---

## BONUS DECISIONS (Lower Priority, Resolve When Convenient)

### 5a. Accounts 4-8 (IIC Chain Segregation)
Still needed? With OpenClaw + simplified routing, 3 accounts (iCloud, Gmail parallel, Gmail primary) may suffice. IIC-specific accounts are overhead if you never configure them.
**Recommendation**: Defer activation. Use 3 accounts until a concrete need arises.

### 5b. Atlas+Comet Browser Strategy
Still needed with OpenClaw routing?
**Recommendation**: Keep for now — Account 1 ChatGPT access still requires a dedicated browser. Revisit when OpenClaw can authenticate to ChatGPT directly.

### 5c. Make/IFTTT
**Recommendation**: Sunset both. OpenClaw's cron + skills replace all use cases.

### 5d. Cursor/Windsurf
**Recommendation**: Confirmed sunset. Claude Code + Codex CLI cover all IDE-adjacent needs.

### 5e. Tailscale
**Recommendation**: Enable. Remote access to Mac mini agent (Ajna) is high value for mobile workflows. Low effort to configure.

---

## HOW TO RESPOND

Mark your choices above, or reply with a numbered list:
```
1. Linear + Things + OpenClaw
2. Obsidian + Notion
3. Sunset Dropbox and Box
4. OpenClaw + Raycast free
5. Run Setapp audit first
```

Once decisions are made, Commander will:
1. Update REF-STACK_TELEOLOGY.md with ratified dispositions
2. Close PROJ-003
3. Unblock PROJ-006 (Ontology)
4. Begin database implementation (SQLite pilot already built)

---

*"Every tool either compounds meaning or drains attention. There is no neutral."*

---

## SOVEREIGN DECISIONS (2026-02-10)

### Decision 1: Task Management
**Ruling**: MASSIVELY EXPANDED beyond original options.
- Keep Linear (T1a engineering PM) + ClickUp (T1b operational hub)
- **Onboard**: Jira (Scrum, superstructures Linear, bridges ClickUp), Trello (Kanban), Todoist (GTD, substructures ClickUp), TeamGantt (Waterfall, superstructures ClickUp)
- **Additional methodologies**: Prince2, Critical Chain, Critical Path, OPM3, CMMI, XP
- **Additional SaaS to consider**: Basecamp, Asana, Airtable (confirmed), Smartsheet (clone target)
- **Goal**: Eventually replace all with internal tools

### Decision 2: PKM
**Ruling**: Notion = personal context manager / LifeOS. Obsidian = corpus / extended cognition. If exact PKM function needed, find copycat in interim. These tools may be too complex to clone correctly.

### Decision 3: Cloud Storage
**Ruling**: KEEP ALL with differentiated roles (opposite of sunset recommendation).
- Box = stage deliverables
- Dropbox = share with clients
- Google Drive = main storage
- iCloud = cross-format sync

### Decision 4: Raycast
**Ruling**: Raycast free tier. "Probably a good internal app to build" — clone candidate.

### Decision 5: Setapp
**Ruling**: Cancel subscription. Extract primitives and clone functionality.

### Applied To
- REF-STACK_TELEOLOGY.md updated to v1.0.0 (RATIFIED)
- PROJ-003 unblocked for closure
- Linear issues created for onboarding tasks
