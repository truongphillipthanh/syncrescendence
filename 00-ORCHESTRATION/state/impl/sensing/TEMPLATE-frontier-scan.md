---
agent: cartographer
priority: P2
category: sensing
frequency: weekly
schedule: "Sunday 06:00"
launchd_agent: com.syncrescendence.sensing-frontier-scan
description: >
  Scan frontier model landscape for updates to MODEL-INDEX.md.
  Detects new model releases, deprecations, pricing changes, and platform shifts.
---

# SENSING: Frontier Model & Platform Scan

**From**: Scheduler (launchd/claudecron)
**To**: Cartographer (Gemini CLI)
**Reply-To**: commander
**Kind**: SURVEY
**Priority**: P2
**Status**: PENDING
**Timeout**: 30
**CC**: commander

---

## Objective

Perform a comprehensive scan of the frontier model landscape and update reference documents with current data.

### Scan Targets

1. **Model Releases** — Check for new model versions from:
   - Anthropic (Claude family)
   - OpenAI (GPT family, Codex)
   - Google DeepMind (Gemini family)
   - Meta (Llama family)
   - Mistral, Cohere, NVIDIA NIM catalog
   - xAI (Grok), Amazon (Nova)

2. **Platform Changes** — Check for updates to:
   - API pricing changes (any provider)
   - Rate limit adjustments
   - New API capabilities (tool use, vision, audio, agents)
   - Deprecation notices

3. **Competitive Intelligence** — Note any:
   - New agent frameworks or platforms (Amp, Devin, OpenHands updates)
   - Claude Code feature releases
   - OpenClaw ecosystem changes
   - Significant benchmark results

### Data Sources

- Provider announcement blogs and changelogs
- Hugging Face model hub (trending/new)
- NVIDIA NIM catalog
- API documentation pages

## Expected Output

1. Update `00-ORCHESTRATION/state/REF-MODEL_INDEX.md`:
   - Set `last_verified` date to today
   - Add new models discovered
   - Flag deprecated or sunset models
   - Update pricing if changed

2. Update `00-ORCHESTRATION/state/DYN-PLATFORMS.csv` if platform-level changes found

3. Write a summary RESULT file with:
   - Models added/updated/deprecated count
   - Notable changes requiring Sovereign attention
   - Any strategic implications for constellation agent model assignments

## Completion Protocol

1. Write results to `-OUTBOX/cartographer/RESULTS/RESULT-cartographer-YYYYMMDD-frontier_scan.md`
2. Update **Status** above from PENDING to COMPLETE
3. Commit: `git add -A && git commit -m "sensing: frontier scan YYYY-MM-DD"`
