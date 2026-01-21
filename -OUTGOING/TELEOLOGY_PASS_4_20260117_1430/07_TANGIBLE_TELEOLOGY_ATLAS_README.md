# TANGIBLE TELEOLOGY ATLAS: README
## How to Read the CSV Matrix
**Generated**: 2026-01-17

---

## PURPOSE

The `07_TANGIBLE_TELEOLOGY_ATLAS.csv` provides a decision matrix for every platform feature in your constellation. When you're unsure how to use a feature, consult this atlas.

---

## COLUMN DEFINITIONS

| Column | Description | Example Values |
|--------|-------------|----------------|
| `platform_feature` | The specific platform and feature | `claude_web_app_oracle`, `gemini_corpus_sensing` |
| `account_scope` | Which account provides this feature | `personal_icloud`, `hybrid_gmail`, `google_gmail`, `openai_icloud`, `xai_icloud` |
| `teleology` | The "why" — what this feature is FOR | "Strategic synthesis and directive generation" |
| `risks` | Known failure modes and dangers | `context_loss_on_export;memory_opacity` |
| `prerequisites` | What must be true before using | "Claude Pro subscription;Project setup" |
| `when_to_use` | Specific scenarios where this is the right choice | "Oracle synthesis sessions;Long-form strategic analysis" |
| `low_hanging_now` | Is this ready to use immediately? | `YES` or `NO` |
| `deep_contrivance` | Does this require significant setup? | `YES` or `NO` |

---

## HOW TO USE

### Scenario 1: "I need to do X. Which feature should I use?"

1. Open the CSV in a spreadsheet or viewer
2. Search the `when_to_use` column for your task type
3. Check `low_hanging_now` — if YES, you can use it immediately
4. Review `risks` before proceeding
5. Verify `prerequisites` are met

### Scenario 2: "I want to try a new feature. What do I need?"

1. Find the feature row
2. Check `prerequisites` — do you have everything?
3. Check `deep_contrivance` — if YES, expect setup time
4. Read `risks` to understand failure modes
5. Read `teleology` to understand the intended use

### Scenario 3: "Something went wrong. Why?"

1. Find the feature row
2. Check `risks` column
3. Match your symptom to the listed risk
4. Determine if this is a known limitation

---

## ACCOUNT SCOPE REFERENCE

| Scope | Email | Primary Features |
|-------|-------|------------------|
| `personal_icloud` | @icloud.com | Claude Web (Concierge), Notion, Midjourney |
| `hybrid_gmail` | @gmail.com | Claude Code, GitHub, Supabase |
| `openai_icloud` | @icloud.com | ChatGPT (Deviser), Codex CLI |
| `google_gmail` | @gmail.com | Gemini (Oracle), NotebookLM, Drive |
| `xai_icloud` | @icloud.com | Grok (Sensor) |

---

## LOW-HANGING NOW vs DEEP CONTRIVANCE

**Low-Hanging Now (`YES`)**: Ready to use with existing setup. Just open and go.

Examples:
- Claude Web App for Oracle sessions
- Claude Code for execution
- Gemini for corpus sensing
- NotebookLM for grounded RAG
- Perplexity for research

**Deep Contrivance (`NO`)**: Requires setup, configuration, or additional work before usable.

Examples:
- Claude Code MCP Gateway (needs gateway CLI setup)
- ChatGPT Agent Mode (needs task identification, monthly limits)
- Gemini Personal Intelligence (US-only beta)
- Grok Voice API (needs billing setup)
- Supabase Backend (needs schema and project setup)
- Orbit-2 SSH (needs network and key configuration)

---

## FILTERING TIPS

### Show only immediately usable features
Filter: `low_hanging_now = YES`

### Show only features on a specific account
Filter: `account_scope = personal_icloud`

### Find all research-capable features
Search `teleology` for: "research"

### Find all execution-capable features
Search `teleology` for: "execution"

---

## GOVERNANCE QUICK REFERENCE

| Task Type | Primary Feature | Fallback |
|-----------|-----------------|----------|
| Strategic synthesis | `claude_web_app_oracle` | — |
| Plan creation | `chatgpt_planning` | `claude_web_app_oracle` |
| File execution | `claude_code_cli_execution` | — |
| Corpus analysis | `gemini_corpus_sensing` | — |
| Video processing | `gemini_corpus_sensing` | — |
| Grounded Q&A | `notebooklm_grounded_rag` | — |
| External research | `perplexity_research` | `chatgpt_deep_research` |
| Real-time news | `grok_realtime` | `perplexity_research` |
| Post-execution audit | `chatgpt_audit` | — |
| Image generation | `midjourney_images` | — |

---

## UPDATING THE ATLAS

When a new feature becomes available or entitlements change:

1. Add row with all columns filled
2. Update `low_hanging_now` based on current setup state
3. Document `risks` from experience
4. Commit change with `docs(teleology): add/update [feature]`

---

## CSV VIEWER RECOMMENDATIONS

- **macOS**: Numbers, Excel, or VS Code with Rainbow CSV extension
- **Terminal**: `column -s, -t < 07_TANGIBLE_TELEOLOGY_ATLAS.csv | less -S`
- **Claude Code**: `cat 07_TANGIBLE_TELEOLOGY_ATLAS.csv` or use Read tool

---

**The atlas is your decision reference. Consult it before using any platform feature.**
