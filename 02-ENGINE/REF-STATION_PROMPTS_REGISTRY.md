# STATION_PROMPTS_REGISTRY.md
## Syncrescendence Prompt Registry

**Version**: 1.0.0
**Updated**: 2026-01-16

---

## 1. RECEPTION CALIBRATION PROMPTS

These prompts configure platform behavior for general interaction with the Sovereign.

| File | Platform | Purpose | Status |
|------|----------|---------|--------|
| PROMPT-CHATGPT-canonical.md | ChatGPT | Sovereign cognitive profile + response calibration | ACTIVE |
| PROMPT-CLAUDE-canonical.md | Claude | Sovereign preferences + extended thinking guidance | ACTIVE |
| PROMPT-GEMINI-canonical.md | Gemini | 4-slot deployment for Sovereign interaction | ACTIVE |
| PROMPT-GROK-canonical.md | Grok | Sovereign calibration (backup platform) | ACTIVE |

---

## 2. IMEP STATION PROMPTS

These prompts configure platforms for specific IMEP protocol roles.

| File | Platform | Role | Packet Type | Status |
|------|----------|------|-------------|--------|
| PROMPT-IMEP-CHATGPT-DEVISER.md | ChatGPT | Vanguard | PLN (Plan) | **RESOLVED** |
| PROMPT-IMEP-CHATGPT-AUDITOR.md | ChatGPT | Auditor | AUD (Audit) | **RESOLVED** |
| PROMPT-IMEP-GEMINI-ORACLE.md | Gemini | Oracle | EVD (Evidence) | **RESOLVED** |
| PROMPT-IMEP-CLAUDE-ENGINEER.md | Claude Code | Engineer/Executor | EXE (Execution) | **RESOLVED** |
| PROMPT-IMEP-CLAUDE-AUDITOR.md | Claude Code | Auditor | AUD (Audit) | **RESOLVED** |

---

## 3. ROLE-TO-PLATFORM MAPPING

| IMEP Role | Primary Platform | Prompt File |
|-----------|------------------|-------------|
| Oracle | Gemini | PROMPT-IMEP-GEMINI-ORACLE.md |
| Vanguard | ChatGPT | PROMPT-IMEP-CHATGPT-DEVISER.md |
| Engineer | Claude Code | PROMPT-IMEP-CLAUDE-ENGINEER.md |
| Auditor | ChatGPT or Claude Code | PROMPT-IMEP-CHATGPT-AUDITOR.md or PROMPT-IMEP-CLAUDE-AUDITOR.md |

---

## 4. PACKET TYPE SUMMARY

| Packet | ID Pattern | Emitter Role | Emitter Platform |
|--------|------------|--------------|------------------|
| Evidence | EVD-YYYYMMDD-NNN | Oracle | Gemini |
| Plan | PLN-YYYYMMDD-NNN | Vanguard | ChatGPT |
| Execution | EXE-YYYYMMDD-NNN | Engineer | Claude Code |
| Audit | AUD-YYYYMMDD-NNN | Auditor | ChatGPT or Claude Code |

---

## 5. DEPLOYMENT NOTES

### ChatGPT Vanguard Thread
1. Start new thread
2. Paste PROMPT-IMEP-CHATGPT-DEVISER.md as first message
3. Provide BOOT_CAPSULE.md contents
4. Submit Evidence packet to receive Plan packet

### Gemini Oracle Thread
1. Configure Gemini with PROMPT-IMEP-GEMINI-ORACLE.md
2. Query corpus for evidence gathering
3. Receive Evidence packet

### Claude Code Engineer
1. PROMPT-IMEP-CLAUDE-ENGINEER.md loaded via CLAUDE.md context
2. Provide Plan packet
3. Execute and receive Execution packet

### Auditor (either platform)
1. Load appropriate auditor prompt
2. Provide Execution packet + original Plan packet
3. Receive Audit packet with APPROVE/REJECT

---

## 6. PREVIOUSLY MISSING (NOW RESOLVED)

The following IMEP station prompts were identified as missing and have been created:

- [x] PROMPT-IMEP-CHATGPT-DEVISER.md — Created 2026-01-16
- [x] PROMPT-IMEP-CHATGPT-AUDITOR.md — Created 2026-01-16
- [x] PROMPT-IMEP-GEMINI-ORACLE.md — Created 2026-01-16
- [x] PROMPT-IMEP-CLAUDE-ENGINEER.md — Created 2026-01-16
- [x] PROMPT-IMEP-CLAUDE-AUDITOR.md — Created 2026-01-16

---

*Registry maintained by Oracle 13+*
