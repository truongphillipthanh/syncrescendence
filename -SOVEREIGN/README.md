# -SOVEREIGN

**Sovereign Decision Queue** — Asynchronous tasks and decisions requiring Phillip's direct judgment, approval, or action. Any CLI agent can triage items here.

Files here represent blocking decisions, external actions, or choices that need human authority.

---

## How This Works

1. **Any CLI agent** (Commander, Adjudicator, Cartographer, Psyche, Ajna) triages items here when they exceed autonomous scope
2. Each file is a self-contained **decision brief** with context, options, and recommendation
3. Once decided, the Sovereign marks status and the originating agent executes
4. Items are numbered sequentially: `SOVEREIGN-NNN-{TOPIC}.md`

## File Format

```markdown
# SOVEREIGN-NNN-{TOPIC}

**From**: {originating agent}
**Date**: {YYYY-MM-DD}
**Priority**: P0 | P1 | P2 | P3
**Status**: PENDING | DECIDED | EXECUTED | ARCHIVED

## Context
{Why this needs Sovereign judgment}

## Options
1. {Option A} — {tradeoffs}
2. {Option B} — {tradeoffs}

## Recommendation
{Agent's recommended option with rationale}

## Decision
{Sovereign fills this in}
```

## When To Use

- **API keys, credentials, account actions** — agents cannot self-provision
- **Architectural decisions** with irreversible consequences
- **External communications** (emails, interviews, registrations)
- **Budget/spending decisions** exceeding established patterns
- **Deletions in protected zones** (01-CANON/, 00-ORCHESTRATION/state/)

## Interim Role

Until Linear and Slack are onboarded, -SOVEREIGN serves as the primary async communication channel from CLI agents to the Sovereign. Post-onboarding, this folder transitions to high-stakes decisions only, with routine items flowing through Linear tasks and Slack messages.
