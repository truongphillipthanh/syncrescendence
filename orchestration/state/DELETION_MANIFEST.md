# DELETION MANIFEST
## Files Pending Deletion — Awaiting Principal Approval
**Created**: 2025-12-31
**Created by**: Claude 2 (DIRECTIVE-025A)

---

## STATUS: AWAITING PRINCIPAL APPROVAL

These files have been verified as fully extracted. Their value has been captured in:
- Unified prompt files (*-unified-prompt.md)
- DESIGN_DECISIONS.md (learnings and patterns)
- ORACLE_DECISIONS.md (decision context)

**Do not delete until Principal approves.**

---

## Category 1: System Prompt Raw Exports (14 files)

### ChatGPT Exports (6 files)

| # | File Path | Size | Extraction Verified |
|---|-----------|------|---------------------|
| 1 | `OPERATIONAL/prompts/Technological Lunar - System PromptsChatGPT [OpenAI@Apple] Memories.txt` | ~7K | ✓ |
| 2 | `OPERATIONAL/prompts/Technological Lunar - System PromptsChatGPT [OpenAI@Apple] System Prompt 1 - What traits should ChatGPT have?.txt` | ~2K | ✓ |
| 3 | `OPERATIONAL/prompts/Technological Lunar - System PromptsChatGPT [OpenAI@Apple] System Prompt 2 - Anything else ChatGPT should know about you?.txt` | ~1K | ✓ |
| 4 | `OPERATIONAL/prompts/Technological Lunar - System PromptsChatGPT [OpenAI@Google] Memories.txt` | ~3K | ✓ |
| 5 | `OPERATIONAL/prompts/Technological Lunar - System PromptsChatGPT [OpenAI@Google] System Prompt 1 - What traits should ChatGPT have?.txt` | ~2K | ✓ |
| 6 | `OPERATIONAL/prompts/Technological Lunar - System PromptsChatGPT [OpenAI@Google] System Prompt 2 - Anything else ChatGPT should know about you?.txt` | ~1K | ✓ |

### Claude Exports (2 files)

| # | File Path | Size | Extraction Verified |
|---|-----------|------|---------------------|
| 7 | `OPERATIONAL/prompts/Technological Lunar - System PromptsClaude [Anthropic@Apple] System Prompt - What personal preferences should Claude consider in responses?.txt` | ~2K | ✓ |
| 8 | `OPERATIONAL/prompts/Technological Lunar - System PromptsClaude [Anthropic@Google] System Prompt - What personal preferences should Claude consider in responses?.txt` | ~2K | ✓ |

### Gemini Exports (4 files)

| # | File Path | Size | Extraction Verified |
|---|-----------|------|---------------------|
| 9 | `OPERATIONAL/prompts/Technological Lunar - System PromptsGemini Saved Info - What do you want Gemini to remember? 1.txt` | ~1K | ✓ |
| 10 | `OPERATIONAL/prompts/Technological Lunar - System PromptsGemini Saved Info - What do you want Gemini to remember? 2.txt` | ~1K | ✓ |
| 11 | `OPERATIONAL/prompts/Technological Lunar - System PromptsGemini Saved Info - What do you want Gemini to remember? 3.txt` | ~1K | ✓ |
| 12 | `OPERATIONAL/prompts/Technological Lunar - System PromptsGemini Saved Info - What do you want Gemini to remember? 4.txt` | ~1K | ✓ |

### Grok Exports (2 files)

| # | File Path | Size | Extraction Verified |
|---|-----------|------|---------------------|
| 13 | `OPERATIONAL/prompts/Technological Lunar - System PromptsGrok [xAI@Apple] System Prompt - Custom Instructions.txt` | ~2K | ✓ |
| 14 | `OPERATIONAL/prompts/Technological Lunar - System PromptsGrok [xAI@Google] System Prompt - Custom Instructions.txt` | ~2K | ✓ |

---

## Category 2: Tech Lunar Files Pending Deletion (1 file)

| # | File Path | Size | Reason |
|---|-----------|------|--------|
| 15 | `OPERATIONAL/prompts/Technology Lunar - FrontierModels.md` | ~25K | Temporal/obsolete (October 2025 landscape) |

**Note**: FrontierModels.md is a point-in-time snapshot of AI model landscape. Value is limited:
- Model capabilities change rapidly
- No unique methodology to extract
- Historical snapshot has minimal value
- Not canonical — belongs in no chain

---

## Category 3: Double Extension Files (if any remain)

| # | File Path | Authoritative Version |
|---|-----------|----------------------|
| - | (Cleared in DIRECTIVE-024) | - |

---

## Deletion Commands

When Principal approves, execute:

```bash
# System Prompt Exports
rm "OPERATIONAL/prompts/Technological Lunar - System PromptsChatGPT [OpenAI@Apple] Memories.txt"
rm "OPERATIONAL/prompts/Technological Lunar - System PromptsChatGPT [OpenAI@Apple] System Prompt 1 - What traits should ChatGPT have?.txt"
rm "OPERATIONAL/prompts/Technological Lunar - System PromptsChatGPT [OpenAI@Apple] System Prompt 2 - Anything else ChatGPT should know about you?.txt"
rm "OPERATIONAL/prompts/Technological Lunar - System PromptsChatGPT [OpenAI@Google] Memories.txt"
rm "OPERATIONAL/prompts/Technological Lunar - System PromptsChatGPT [OpenAI@Google] System Prompt 1 - What traits should ChatGPT have?.txt"
rm "OPERATIONAL/prompts/Technological Lunar - System PromptsChatGPT [OpenAI@Google] System Prompt 2 - Anything else ChatGPT should know about you?.txt"
rm "OPERATIONAL/prompts/Technological Lunar - System PromptsClaude [Anthropic@Apple] System Prompt - What personal preferences should Claude consider in responses?.txt"
rm "OPERATIONAL/prompts/Technological Lunar - System PromptsClaude [Anthropic@Google] System Prompt - What personal preferences should Claude consider in responses?.txt"
rm "OPERATIONAL/prompts/Technological Lunar - System PromptsGemini Saved Info - What do you want Gemini to remember? 1.txt"
rm "OPERATIONAL/prompts/Technological Lunar - System PromptsGemini Saved Info - What do you want Gemini to remember? 2.txt"
rm "OPERATIONAL/prompts/Technological Lunar - System PromptsGemini Saved Info - What do you want Gemini to remember? 3.txt"
rm "OPERATIONAL/prompts/Technological Lunar - System PromptsGemini Saved Info - What do you want Gemini to remember? 4.txt"
rm "OPERATIONAL/prompts/Technological Lunar - System PromptsGrok [xAI@Apple] System Prompt - Custom Instructions.txt"
rm "OPERATIONAL/prompts/Technological Lunar - System PromptsGrok [xAI@Google] System Prompt - Custom Instructions.txt"

# Tech Lunar Files
rm "OPERATIONAL/prompts/Technology Lunar - FrontierModels.md"
```

---

## Verification References

- **Extraction verification**: `orchestration/state/SYSTEM_PROMPT_EXTRACTION_VERIFICATION.md`
- **Learnings captured**: `orchestration/state/DESIGN_DECISIONS.md`
- **Decision context**: `orchestration/state/ORACLE_DECISIONS.md`

---

## Approval Required

**Principal must approve deletion before execution.**

| Approver | Date | Decision |
|----------|------|----------|
| Principal | ___ | [ ] APPROVED / [ ] REJECTED |

---

**END DELETION MANIFEST**
