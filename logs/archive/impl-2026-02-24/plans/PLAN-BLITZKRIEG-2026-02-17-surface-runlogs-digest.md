# BLITZKRIEG PLAN — -surface/running_logs Progressive Digest
## Issued: 2026-02-17 | Fingerprint: 3cc50bd

---

### Objective

Progressively summarize ALL files in `/Users/system/Desktop/-surface/running_logs/` (26 files,
8,431 lines) and `/Users/system/Desktop/-surface/_sovereign.md` (93 lines) into compressed
digests, then synthesize into a single master digest — capturing the **rescued knowledge** these
files contain as evacuation relay portals from dying agent sessions.

### Key Context: Evacuation Relay Portals

These files served a dual function:
1. **Standard logs**: Ongoing agent activity (requests, editor events, execution traces)
2. **Evacuation relays**: When sessions hit context limits or died mid-task, agents dumped
   substantive output, decisions, and work-in-progress into these files for rescue/retrieval.

The synthesis must recover the **rescued content** — not just summarize activity.

### Constraints

- Context: Opus orchestrator (<10K token content budget) — all reads delegated to Sonnet
- Per-agent budget: ≤3,000 lines across all reads
- Ceiling: Master digest ≤400 lines
- Dependencies: All batch digests must complete before master synthesis

### Success Criteria

- [x] Group A: mba-commander-log.md (3,042 lines) — RUNLOGS-DIGEST-A.md
- [x] Group B: mba-commander-log-2.md + mm-commander-log.md (2,502 lines) — RUNLOGS-DIGEST-B.md
- [x] Group C: request files — mba-commander-request.md + mm-commander-request.md + mm-psyche-request.md (1,763 lines) — RUNLOGS-DIGEST-C.md ✓ DONE (165 lines)
- [x] Group D: all remaining agents — adjudicator, cartographer, ajna, psyche, editor logs (1,124 lines) — RUNLOGS-DIGEST-D.md ✓ DONE (291 lines)
- [x] Group E: _sovereign.md (93 lines — credentials file, not log) — RUNLOGS-DIGEST-E.md ✓ DONE (110 lines)
- [ ] Master synthesis: all 5 digests → RUNLOGS-MASTER-DIGEST.md (≤400 lines)
- [ ] Commit all digests to repo

### Lanes

| Lane | File Group | Lines | Status |
|------|-----------|-------|--------|
| A | mba-commander-log.md | 3,042 | IN FLIGHT |
| B | mba-commander-log-2.md + mm-commander-log.md | 2,502 | IN FLIGHT |
| C | mba-commander-request.md + mm-commander-request.md + mm-psyche-request.md | 1,763 | DONE |
| D | adjudicator + cartographer + ajna + psyche + editor logs | 1,124 | DONE |
| E | _sovereign.md | 93 | DONE |
| MASTER | All 5 digests → RUNLOGS-MASTER-DIGEST.md | ~1K | PENDING |

### Risk Assessment

- **High**: Group A (3,042 lines) is at the per-agent context budget ceiling — agent may need to
  read in chunks; risk of losing content at the end of the file
- **Medium**: Evacuation relay content may be interleaved with routine logs — synthesis agent
  must distinguish rescued knowledge from activity traces
- **Low**: Some files (editor logs, ajna-request) are very sparse — digests may be thin
- **Mitigation**: If Group A produces incomplete digest, re-dispatch with explicit chunking
  instructions (read lines 1-1000, 1001-2000, 2001-3042 in three passes)

### Security Note

- `_sovereign.md` is a **plaintext credentials file** (API keys for 15+ services) — this is
  DC-003 (P0 OPEN). Digest was written with redacted awareness. Credential rotation is a
  Sovereign action item.

### Output Location

All digests: `orchestration/state/impl/.scratch/RUNLOGS-DIGEST-[A-E].md`
Master: `orchestration/state/impl/.scratch/RUNLOGS-MASTER-DIGEST.md`

---

*PLAN-BLITZKRIEG-2026-02-17-surface-runlogs-digest.md | Commander | 2026-02-17*
*Operation in progress — Groups A+B in flight, C+D+E complete*
