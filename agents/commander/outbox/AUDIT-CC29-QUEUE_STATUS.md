# AUDIT-CC29-QUEUE_STATUS
**Date**: 2026-02-24 | **Session**: CC29 | **Auditor**: Commander (Claude Opus 4.6)

---

## 1. Commander Inbox

### Pending (1 item)
| File | Age | Recommendation |
|------|-----|----------------|
| `RESULT-CODEX-CONFIG-CENTRALIZATION.md` (11k) | Today | **PROCESS** — fresh Codex result, needs review and integration |

### Active (88 items) — CRITICALLY BACKLOGGED
| Category | Count | Date Range | Recommendation |
|----------|-------|------------|----------------|
| CONFIRM-adjudicator | 17 | Feb 19-22 | **ARCHIVE** — stale DC followups (dc_002/003/004/013), 4 days of repeated runs |
| CONFIRM-bridgeprobe | 1 | Feb 17 | **ARCHIVE** — bridge test completed |
| CONFIRM-cartographer | 2 | Feb 15-21 | **ARCHIVE** — corpus analysis done |
| EXECLOG-* | 20 | Feb 19-22 | **ARCHIVE** — execution logs for completed tasks |
| RESULT-adjudicator | 18 | Feb 19-22 | **ARCHIVE** — reviewed in Phase 2 |
| RESULT-ADJUDICATOR-DC203 | 1 | Feb 23 | **ARCHIVE** — consumed in DC204 synthesis |
| RESULT-cartographer | 2 | Feb 15-21 | **ARCHIVE** — consumed |
| RESULT-CODEX-CONFIG | 1 | Today | **DUPLICATE** of pending — delete one |
| RESULT-DIVINER-DC205 | 1 | Feb 23 | **ARCHIVE** — consumed in synthesis |
| RESULT-ORACLE-DC201/202/204E | 3 | Feb 23 | **ARCHIVE** — consumed |
| RESPONSE-ORACLE-DC204T | 1 | Feb 23 | **ARCHIVE** — consumed |
| BRIEFING-constellation-reconfig | 1 | Feb 9 | **ARCHIVE** — 15 days old, superseded |
| TASK-LINEAR-STATUS | 8 | Feb 18-22 | **ARCHIVE** — stale status snapshots |
| TASK-SESSION-REVIEW | 4 | Feb 17-20 | **ARCHIVE** — reviewed |
| TASK-* (other) | 6 | Feb 11-21 | **ARCHIVE** — completed or superseded |
| SOVEREIGN-TEST | 1 | Feb 22 | **DELETE** — test artifact |

**Oldest item**: BRIEFING-20260209 (15 days). **Triage**: Move all to `inbox/done/`, keep only RESULT-CODEX-CONFIG-CENTRALIZATION in pending.

---

## 2. -INBOX/commander/00-INBOX0/ (42 files)

| Category | Count | Recommendation |
|----------|-------|----------------|
| RESPONSE-* (triangulation) | 37 | **RETAIN** — canonical triangulation archive. Index exists. |
| RESULT-CODEX-CONFIG | 1 | **PROCESS** — same as pending item |
| INDEX-TRIANGULATION | 1 | **RETAIN** — index file |
| REPORT-SIEGE-MECHANICAL | 1 | **RETAIN** — CC28 siege report |
| HANDOFF-LATEST | 1 | **RETAIN** — rolling handoff pointer |
| TASK-LINEAR-STATUS | 1 | **ARCHIVE** — stale (Feb 22) |

**Status**: Healthy. This is the triangulation response archive. No action needed except archiving the stale TASK file.

---

## 3. -SOVEREIGN/ Queue (21 items + 3 dirs)

| Category | Count | Recommendation |
|----------|-------|----------------|
| SOVEREIGN-NNN decisions | 9 | **RETAIN** — sovereign decision records (002-016 + TRAJECTORY) |
| PROMPT-* (outbound) | 6 | **ARCHIVE** — dispatched prompts, responses landed |
| ALERT-* | 2 | **ARCHIVE** — Feb 21 alerts, resolved |
| DECISION-* | 2 | **RETAIN** — MCP onboarding + plist fixes decisions |
| ESCALATION-* | 1 | **ARCHIVE** — adjudicator rate-limit, resolved |
| REINIT-* | 1 | **ARCHIVE** — Feb 8 reinit, historical |
| CONFIG-SANDBOX-* (dir+zip) | 2 | **ARCHIVE** — INT-2210 recovery artifacts |
| antifragile-scaffold-archive/ | 1 | **RETAIN** — permanent archive |
| ARCHIVED/ | 1 | Already archive dir |

**Oldest item**: REINIT-COMMANDER-2026-02-08 (16 days).

---

## 4. Commander Outbox (145 files + handoffs/)

| Category | Count | Recommendation |
|----------|-------|----------------|
| RECEIPT-* | 62 | **ARCHIVE** — dispatch receipts, all completed |
| RESULT-* | 28 | **RETAIN** active session results; archive pre-CC26 |
| CONFIRM-* | 20 | **ARCHIVE** — completed confirmations |
| EXECLOG-* | 18 | **ARCHIVE** — execution logs |
| TASK-* | 11 | **ARCHIVE** — stale watchdog/corpus/linear tasks |
| DECISION_ATOMS-* | 2 | **RETAIN** — DC204 + Phase 2 synthesis atoms |
| HANDOFF-CC28-* | 1 | **RETAIN** — current session terminal |
| _DISPATCH_TEMPLATE | 1 | **RETAIN** — template |
| cli_logs/ | 1 | **ARCHIVE** — old CLI logs |

### Handoffs subdir (8 files) — all RETAIN
Active handoff chain: DC204 -> DC208 -> CC26 -> CC27 -> CC28. Plus autocompact artifacts.

**Oldest item**: RECEIPT-commander-TASK-20260207 (17 days).
**Total outbox size is bloated** — 145 files. Recommend moving pre-CC26 receipts/execlogs to `outbox/archive/`.

---

## 5. Other Agent Inboxes

| Agent | Pending | Active | Items | Recommendation |
|-------|---------|--------|-------|----------------|
| Adjudicator | 0 | 0 | Empty (clean) | No action |
| Cartographer | 0 | 0 | Empty (clean) | No action |
| Psyche | 0 | 1 | TASK-20260221-infrastructure_audit (3 days) | **ESCALATE** — stale unprocessed task |
| Ajna | 0 | 7 | BRIEFING (Feb 9), CONFIRM/EXECLOG/RESULT (Feb 15-17), TASK (Feb 11) | **ARCHIVE** — Ajna anesthetized, these will never be processed |

---

## 6. Uncommitted Work (24 items)

### Modified (16 files)
| File | Category |
|------|----------|
| HANDOFF-LATEST.md | Session state |
| AGENTS.md, CLAUDE.md, CLAUDE-EXT.md, GEMINI.md | Config updates |
| commander/memory/MEMORY.md | Memory update |
| journal/2026-02-25.jsonl | Journal entries |
| PROTOCOL-ASCERTESCENCE.md | Protocol update |
| session_state_brief.py | CC27 build |
| DYN-SESSION_BASELINE.json, DYN-SESSION_STATE_BRIEF.md | Session state |
| DYN-EXECUTION_STAGING.md, DYN-INTENTIONS_QUEUE.md | Dynamic state |
| DYN-PEDIGREE_LOG.md, DYN-SESSION_LOG.md | Logs |
| memory/ingest-stdout.log | Log |

### Untracked (9 items)
| File | Recommendation |
|------|----------------|
| `..bfg-report/` | **DELETE** — BFG repo cleaner artifact, stale |
| `.env.graphiti` | **KEEP UNTRACKED** — environment config, do not commit |
| `compaction_state.json` | **ADD** — memory compaction state |
| `2026-02-24-ingest.log` | **KEEP UNTRACKED** — transient log |
| `DYN-INTEGRATION_GATE_LOG.jsonl` | **ADD** — new dynamic state file |
| `DYN-SESSION_STATE_BRIEF.err.log` | **DELETE** — error log, investigate then remove |
| `orchestration/orchestration/` | **DELETE** — duplicate nested dir (likely accidental mkdir) |
| `memsync.stderr.log`, `memsync.stdout.log` | **KEEP UNTRACKED** — daemon logs |

---

## 7. Working Tree Artifacts

| Artifact | Location | Recommendation |
|----------|----------|----------------|
| `.env.graphiti` | repo root | **DO NOT COMMIT** — contains infra config. Verify in .gitignore |
| `orchestration/orchestration/state/` | nested duplicate | **DELETE** — accidental directory |
| `..bfg-report/` | repo parent | **DELETE** — stale BFG cleaner output |
| `DYN-SESSION_STATE_BRIEF.err.log` | orchestration state | **INVESTIGATE** — may indicate hook error |
| `memory/*.log` (4 files) | memory/ | Transient ingest logs, keep untracked |

---

## Summary Scorecard

| Queue | Items | Oldest | Health | Action |
|-------|-------|--------|--------|--------|
| Commander inbox/pending | 1 | Today | GREEN | Process Codex result |
| Commander inbox/active | 88 | Feb 9 (15d) | RED | Archive 87 items immediately |
| -INBOX/00-INBOX0 | 42 | Feb 23 | GREEN | Archive 1 stale TASK |
| -SOVEREIGN | 21 | Feb 8 (16d) | YELLOW | Archive 10 resolved items |
| Commander outbox | 145 | Feb 7 (17d) | YELLOW | Archive pre-CC26 artifacts (~100 files) |
| Adjudicator inbox | 0 | -- | GREEN | -- |
| Cartographer inbox | 0 | -- | GREEN | -- |
| Psyche inbox | 1 | Feb 21 (3d) | YELLOW | Escalate or archive |
| Ajna inbox | 7 | Feb 9 (15d) | RED | Archive all (agent anesthetized) |
| Uncommitted changes | 24 | -- | YELLOW | Commit session work; delete stale artifacts |

### Top 3 Actions
1. **Flush Commander active inbox** — 87 of 88 items are processed/stale. Move to `inbox/done/`.
2. **Archive Ajna inbox** — agent is anesthetized. 7 items will never be processed.
3. **Delete stale artifacts** — `orchestration/orchestration/`, `..bfg-report/`, `DYN-SESSION_STATE_BRIEF.err.log`.
