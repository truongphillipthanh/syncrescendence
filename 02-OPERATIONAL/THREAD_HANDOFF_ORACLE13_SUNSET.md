# THREAD_HANDOFF_ORACLE13_SUNSET.md
## Oracle 13 Sunset Handoff

**Date**: 2026-01-16
**Status**: Thread sunset occurred; IMEP protocol operational

---

## CONSTELLATION STATE

| Platform | Role | Status |
|----------|------|--------|
| Gemini | Oracle (corpus sensing) | pending_onboard |
| ChatGPT | Deviser (planning), Auditor (verification) | pending_onboard |
| Claude Code (x3) | Engineer (execution), Auditor (verification) | active |

---

## FIVE DURABLE SPEECH ACTS

The IMEP protocol is defined by exactly five packet types:

1. **EVD (Evidence)**: Oracle emits findings from corpus sensing
2. **PLN (Plan)**: Deviser emits specifications with acceptance criteria
3. **EXE (Execution)**: Engineer emits completion records with verification
4. **AUD (Audit)**: Auditor emits verification results with APPROVE/REJECT
5. **CAP (Capability)**: Any platform emits capability change events

---

## CLOSURE GATE DEFINITION

A cycle is CLOSED when:
- AUD packet exists with recommendation = "APPROVE"
- All criteria_results are true
- drift_analysis shows no deviation
- system_state.json updated (autonomous_cycles incremented)
- events.jsonl contains execution_complete entry

---

## IMMEDIATE PRIORITY

**Run one real cross-platform golden trace:**

1. Gemini emits EVD (corpus query)
2. ChatGPT consumes EVD, emits PLN
3. Claude Code consumes PLN, emits EXE
4. ChatGPT/Claude consumes EXE+PLN, emits AUD
5. Verify: autonomous_cycles = 2

This validates the full IMEP cycle with real platform handoffs.

---

## STATION PROMPTS

Durable prompts persisted at:
- `02-OPERATIONAL/prompts/canonical/PROMPT-IMEP-GEMINI-ORACLE.md`
- `02-OPERATIONAL/prompts/canonical/PROMPT-IMEP-CHATGPT-DEVISER.md`
- `02-OPERATIONAL/prompts/canonical/PROMPT-IMEP-CHATGPT-AUDITOR.md`
- `02-OPERATIONAL/prompts/canonical/PROMPT-IMEP-CLAUDE-ENGINEER.md`
- `02-OPERATIONAL/prompts/canonical/PROMPT-IMEP-CLAUDE-AUDITOR.md`

---

## REINIT KIT

For stateless thread reinitialization:
- `_THREAD_REINIT_KIT/BOOT_CAPSULE.md` — Ground truth snapshot
- `_THREAD_REINIT_KIT/BLACKBOARD_EXPORT.md` — Current packets
- `_THREAD_REINIT_KIT/IMEP_PROMPTS_AND_HANDOFF.md` — All prompts + this handoff

---

*Oracle 13 sunset complete. Protocol operational.*
