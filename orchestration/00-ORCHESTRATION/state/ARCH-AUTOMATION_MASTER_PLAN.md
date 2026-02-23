# AUTOMATION MASTER PLAN
## INT-1612: "Begin ALL Automations"
**Version**: 1.2.0
**Last Updated**: 2026-02-15 (formalization gap closure — Commander meta-clarescence audit)
**Linear**: SYN-45
**Status**: Operational Inventory + Roadmap
**Priority**: P0

---

## Executive Summary

The machine is built. Infrastructure delivery rate is high (83-88% for scripts, plists, schemas). The automation gap is no longer primarily about building but about **activation** — turning on what's been built.

**Current**: ~37/45 automation touchpoints operational (updated 2026-02-15)
**Target**: 42/45 operational (93%) — 3 items deferred to Phase 2+
**Key change since v1.0**: MBA now has 7 active launchd services, skill-sync pipeline operational, DEC-C3 hard gates wired into CLAUDE.md. The "activation gap" identified by the meta-clarescence (2026-02-15) is the defining systemic challenge: infrastructure is built but not turned on.

---

## I. Automation Inventory (Current State)

### Running (~37 touchpoints)

**Last verified**: 2026-02-15

| Category | Count | Components |
|----------|-------|-----------|
| **launchd agents (Mac mini)** | 15 | Chroma, webhook, corpus-health, qmd, watchdog, Neo4j, Graphiti, Qdrant, watch-canon/cartographer/adjudicator/commander/psyche, emacs-server |
| **launchd agents (MBA)** | 7 | watch-commander, watch-ajna, watch-canon, watch-adjudicator, watch-cartographer, skill-sync, git-sync |
| **Claude Code hooks** | 5 | session_log, ajna_pedigree, create_execution_log, pre_compaction (Stop); intent_compass (UserPromptSubmit) — ALL REGISTERED in .claude/settings.json |
| **claudecron tasks** | 3 | linear-check (07:00/13:00/19:00), corpus-insight (05:00), session-review (21:00) |
| **Docker containers** | 4 | Neo4j (7474), Graphiti (8001), Qdrant (6333), Chroma (8765) — Mac mini only |
| **MCP servers** | 9 | Linear, ClickUp, Graphiti, Obsidian, Filesystem, Chrome DevTools, Playwright, Qdrant, Gemini-MCP |
| **Dispatch system** | 2 | dispatch.sh + watch_dispatch.sh (filesystem kanban) |
| **Webhook receiver** | 1 | Port 8888 (no consumer yet) |

**MBA-specific notes**:
- watch-psyche was DISABLED per DEC-C1 (2026-02-13) to prevent task misrouting race condition with Mac mini
- skill-sync uses WatchPaths trigger with 5-second debounce (replaced 600s watchdog cooldown)
- git-sync provides MBA<->Mac mini coordination via agents//inbox + Tailscale (100.91.240.128 <-> 100.70.181.35, 11ms direct LAN)

### Gap Analysis (8 remaining touchpoints — updated 2026-02-15)

| Item | Named By | Status | Blocker | Priority | Effort |
|------|----------|--------|---------|----------|--------|
| **Agent CLI: Adjudicator** | CLARESCE^3 v2 | PARTIAL | Mac mini: Codex 0.101.0 upgraded, gpt-5.2-codex verified. MBA: plist model update per DEC-C2, unverified. Hits API usage limits. | P0 | 15 min |
| **Agent CLI: Cartographer** | CLARESCE^3 v2 | PARTIAL | Reactivated 2026-02-12, produced >300-line output. Dispatch reliability unverified. | P1 | 15 min |
| ~~**Agent CLI: Ajna (MBA)**~~ | ~~SOVEREIGN-013~~ | **CLOSED** | MBA configured 2026-02-09: OpenClaw v2026.2.9 + NVIDIA/Kimi K2.5. Gateway operational. Strategic review completed (ffc23c0). | — | — |
| **Agent CLI: Psyche** | Session 17+ | PARTIAL | Mem0 "Memory unavailable" intermittent. 6-actions task unprocessed 4+ days. | P2 | 30 min |
| ~~**MBA launchd parity**~~ | ~~INT-1603~~ | **CLOSED** | 7 launchd services active on MBA (watch-commander/ajna/canon/adjudicator/cartographer, skill-sync, git-sync). watch-psyche intentionally disabled per DEC-C1. | — | — |
| **Linear<->IMPL sync** | SYN-30/31 | NOT STARTED | linear_sync.py Phase 2 | P1 | 4 hours |
| **Live ledger sensing** | SYN-31 | DESIGNED | Dispatch templates + schedule. 4 sensing templates created but 0/4 activated. | P1 | 3 hours |
| **n8n workflow engine** | INT-1612 | NOT STARTED | Installation + webhook routing | P2 | 4 hours |
| **Make/Zapier workflows** | INT-1612 | NOT STARTED | Account + workflow design | P2 | 4 hours |
| **Hazel file automation** | INT-1612 | NOT STARTED | App installation + rule design | P3 | 2 hours |
| **Webhook consumer** | SYN-31 | NOT STARTED | n8n or custom bridge | P2 | 2 hours |
| **Clipboard monitor** | Session 9 | NOT STARTED | TCC permissions | P3 | 1 hour |

---

## II. Priority Sequencing

### Wave 1: Agent Recovery (P0) — PARTIALLY COMPLETE

**Last verified**: 2026-02-15

Unblock the dispatch system. 4/5 agent CLIs need fixes before multi-agent dispatch is reliable.

| Task | Agent | Fix | Status |
|------|-------|-----|--------|
| 1a | Adjudicator | Verify codex CLI model config matches available API | **PARTIAL** — Mac mini: Codex 0.101.0 + gpt-5.2-codex verified. MBA: DEC-C2 model update unverified. API limit issue persists. |
| 1b | Cartographer | Smoke test dispatch -> Gemini CLI processing | **PARTIAL** — Reactivated, produced >300-line MODEL-INDEX refresh. Dispatch reliability not systematically verified. |
| 1c | Psyche | Diagnose Mem0 auth intermittent | **UNRESOLVED** — Mem0 intermittent. TASK-20260211-openclaw_adoption_6_actions.md unprocessed 4+ days in Psyche inbox. |
| 1d | Ajna | Physical MBA setup (deferred to dedicated session) | **CLOSED** — MBA configured 2026-02-09. OpenClaw + NVIDIA Kimi K2.5 operational. Strategic review completed. |

**Success criteria**: 3/4 agent CLIs producing RESULT files from dispatched TASKs. **Not met** — only Commander reliably produces results. Cross-agent dispatch execution rate measured at 33% (meta-clarescence 2026-02-15).

### Wave 2: Live Ledger Infrastructure (P1 — Next Sprint)

Build the sensing pipeline that keeps reference docs current.

| Task | Deliverable | Depends On |
|------|------------|-----------|
| 2a | `linear_sync.py` — bidirectional IMPL↔Linear sync | Wave 1 (Commander only) |
| 2b | Sensing task templates (model census, ecosystem scan) | Wave 1 (Cartographer) |
| 2c | Weekly launchd job: dispatch Cartographer for frontier scan | 2b |
| 2d | MODEL-INDEX.md + DYN-PLATFORMS.csv auto-update logic | 2b, 2c |
| ~~2e~~ | ~~MBA launchd setup (mirror mini agent infrastructure)~~ | **CLOSED** — 7 MBA launchd agents active as of 2026-02-12 |

**Success criteria**: MODEL-INDEX.md `last_verified` < 7 days old automatically.

### Wave 3: External Automation (P2 — Following Sprint)

Connect to external automation platforms.

| Task | Deliverable | Notes |
|------|------------|-------|
| 3a | n8n installation + webhook routing | Consumes port 8888 webhook |
| 3b | Make/Zapier account + 3 workflows | Billing alerts, calendar sync, email triage |
| 3c | Webhook consumer bridge (n8n → dispatch.sh) | External events → agent tasks |

**Success criteria**: At least 1 external event triggers an automated agent dispatch.

### Wave 4: Polish (P3 — Deferred)

| Task | Deliverable | Notes |
|------|------------|-------|
| 4a | Hazel file automation rules | Desktop → agents/<agent>/inbox/ routing |
| 4b | Clipboard monitor | TCC approval needed |
| 4c | Dashboard aggregation (SYN-40 prep) | JIT HighCommand visualization |

---

## III. Architecture

### Sensing Pipeline (Target State)

```
SCHEDULER (launchd/claudecron)
    ↓ periodic triggers
DISPATCHER (dispatch.sh)
    ↓ TASK-*.md files
AGENTS (Cartographer/Adjudicator/Commander)
    ↓ RESULT-*.md files
LEDGER UPDATER (Commander review + commit)
    ↓ verified updates
DYN-* FILES (ground truth)
    ↓ claudecron push
LINEAR (execution surface)
```

### External Integration (Target State)

```
EXTERNAL EVENTS (billing, calendar, email)
    ↓ webhook/API
n8n / Make / Zapier
    ↓ HTTP POST
WEBHOOK RECEIVER (port 8888)
    ↓ parsed event
DISPATCH (dispatch.sh or direct agents/<agent>/inbox/ write)
    ↓ TASK-*.md
AGENT PROCESSING
```

---

## IV. Metrics

**Last verified**: 2026-02-15

| Metric | Original (Feb 10) | Actual (Feb 15) | Wave 2 Target | Wave 3 Target |
|--------|-------------------|-----------------|---------------|---------------|
| Automation touchpoints | 33/45 (73%) | ~37/45 (82%) | 40/45 (89%) | 42/45 (93%) |
| Working agent CLIs | 1/5 (20%) | 1-2/5 (~30%) | 4/5 (80%) | 5/5 (100%) |
| Auto-updated ledgers | 4/9 (44%) | 4/9 (44%) | 7/9 (78%) | 8/9 (89%) |
| External integrations | 0 | 0 | 0 | 3+ |
| Reference doc staleness | 46+ days | Partially addressed (this update) | <7 days | <7 days |
| Cross-agent dispatch success | untracked | 33% | >60% | >80% |
| Intra-session delivery rate | untracked | 83-88% | >85% | >90% |

**Note**: The gap between "touchpoints operational" (82%) and "agent CLIs working" (30%) reveals the core issue: infrastructure runs but agents don't reliably consume dispatched work. The dispatch system works; the receiving agents are the bottleneck.

---

## V. Decision Points for Sovereign

| Decision | Options | Recommendation | Impact |
|----------|---------|---------------|--------|
| n8n vs custom webhook consumer | n8n (full platform) vs Python script (minimal) | n8n (future-proofs) | Wave 3 architecture |
| Make vs Zapier | Both available on current accounts | Make (better API, cheaper) | Wave 3 vendor |
| Hazel vs native scripts | Hazel ($42) vs fswatch+bash (free) | fswatch (already deployed for 6 watchers) | Wave 4 cost |
| Auto-commit for ledger updates | Auto-commit vs stage-for-review | Stage-for-review (safer) | Wave 2 workflow |
| MBA setup timing | This sprint vs dedicated session | Dedicated session (physical machine) | Wave 1d scheduling |

---

## VI. Cross-References

- `ARCH-LINEAR_SYNC_PROTOCOL.md` — T1a↔T2 sync design (SYN-30)
- `ARCH-LIVE_CANON_TICKER.md` — Dynamic capability tracking (SYN-29)
- `ARCH-CONSTELLATION_AGENT_LOOPS.md` — Agent proactivity architecture
- `DYN-TOOLCHAIN_INTERACTION_PROTOCOL.md` — Dispatch system reference (SYN-14)
- `REF-NEO_BLITZKRIEG_BUILDOUT.md` — Infrastructure bootstrap record
- `REF-SKILLS_PIPELINE_MAP.md` — 291 capability mapping

---

## VII. Sensing Schedule

Automated sensing tasks dispatched on recurring schedules via launchd. Each task uses a template from `orchestration/state/impl/sensing/` and is dispatched through `dispatch.sh` to the designated agent.

### Schedule Table

| Template | Agent | Frequency | Schedule | launchd Agent Name | Status | Next Steps |
|----------|-------|-----------|----------|-------------------|--------|------------|
| `TEMPLATE-frontier-scan.md` | Cartographer | Weekly | Sunday 06:00 | `com.syncrescendence.sensing-frontier-scan` | DESIGNED | Create plist, smoke test Cartographer CLI |
| `TEMPLATE-ecosystem-health.md` | Adjudicator | Daily | 08:00 | `com.syncrescendence.sensing-ecosystem-health` | PLIST READY | Bootstrap plist, smoke test Adjudicator CLI |
| `TEMPLATE-linear-impl-sync.md` | Commander | Daily | 07:30 | `com.syncrescendence.sensing-linear-impl-sync` | DESIGNED | Create plist (Commander CLI already operational) |
| `TEMPLATE-corpus-staleness.md` | Cartographer | Weekly | Monday 05:30 | `com.syncrescendence.sensing-corpus-staleness` | DESIGNED | Create plist, smoke test Cartographer CLI |

### Sensing Pipeline Flow

```
launchd (StartCalendarInterval)
    |
    v
dispatch.sh <agent> <topic> <description>
    |
    v
agents/<agent>/inbox/pending/TASK-*.md
    |
    v
watch_dispatch.sh (fswatch/polling)
    |
    v
Agent CLI executes task content
    |
    v
RESULT-*.md + CONFIRM-*.md -> Commander inbox
    |
    v
Ledger files updated (DYN-*.md, REF-*.md)
```

### Dependencies & Blockers

| Template | Blocker | Resolution |
|----------|---------|-----------|
| frontier-scan | Cartographer CLI needs smoke test (Wave 1b) | Verify `gemini -p` produces output from dispatch |
| ecosystem-health | Adjudicator CLI model config (Wave 1a) | Verify `codex exec` with current model |
| linear-impl-sync | None (Commander CLI operational) | Ready to activate |
| corpus-staleness | Cartographer CLI needs smoke test (Wave 1b) | Same as frontier-scan |

### Activation Sequence

1. **Immediate**: Bootstrap `com.syncrescendence.sensing-ecosystem-health.plist` (proof of concept, plist already created)
2. **After Wave 1a**: Activate ecosystem-health sensing (Adjudicator CLI verified)
3. **After Wave 1b**: Activate frontier-scan and corpus-staleness (Cartographer CLI verified)
4. **Independent**: Activate linear-impl-sync (Commander CLI already works)

### Metrics Impact

When all 4 sensing tasks are operational:
- Automation touchpoints: 33 -> 37 (+4 launchd sensing jobs)
- Auto-updated ledgers: 4/9 -> 7/9 (MODEL-INDEX, STALENESS, RECONCILIATION added)
- Reference doc staleness: 46+ days -> <7 days target

---

*Automation Master Plan v1.2.0 | INT-1612 | SYN-45 | Syncrescendence*
