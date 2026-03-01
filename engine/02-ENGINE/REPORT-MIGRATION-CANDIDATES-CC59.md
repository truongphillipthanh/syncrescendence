# Migration Candidates Report — CC59

**Date**: 2026-02-28
**Git HEAD**: `0fc7a791`
**Source**: Oracle CC58 subcategory report (~97 estimated candidates)
**Actual**: 40 files moved (verified by content sampling)

## Summary

Oracle estimated ~97 migration candidates. After content verification, 40 were confirmed misplaced and moved. The remaining ~57 were false positives — files that mention keywords (e.g., "OpenClaw") but are semantically about the correct topic (e.g., AI capability futures that reference OpenClaw as an example).

## Migrations Executed

### From claude-code/ (24 files moved)

| File | Destination | Reason |
|------|-------------|--------|
| 00199.md | ai-capability-futures | Corporate War for Compute — not about Claude Code |
| 08472.md | ai-capability-futures | Post-Labor Enterprise — not about Claude Code |
| 09527.md | ai-capability-futures | TEDx AI wave talk — general AI futures |
| 09545.md | ai-capability-futures | AlphaFold Nobel Prize — not about Claude Code |
| 09642.md | ai-capability-futures | DeepMind robotics lab tour |
| 10153.md | ai-capability-futures | Craziest Experiment Humans Built |
| 10308.md | ai-capability-futures | Japan's Debt Bomb — economics |
| 08439.md | meaning-civilization | Joseph Henrich Cultural Evolution |
| 10886.md | meaning-civilization | Reality is Your Moat |
| 00409.md | multi-agent-systems | ARCH-NEO_SCAFFOLD — syncrescendence ops |
| 00913.md | multi-agent-systems | Screenplay orchestration format |
| 02037.md | multi-agent-systems | Extraction about non-Claude topic |
| 08488.md | multi-agent-systems | Adjudicator dispatch prompt |
| 08489.md | multi-agent-systems | Adjudicator dispatch prompt |
| 08495.md | multi-agent-systems | Adjudicator integration review |
| 08851.md | multi-agent-systems | Adjudicator response |
| 08861.md | multi-agent-systems | Adjudicator reviewtrospective |
| 10307.md | multi-agent-systems | Google agents research |
| 11399.md | multi-agent-systems | Adjudicator operational artifact |
| 09416.md | vibe-coding | Google VS Code + Gemini (not Claude) |
| 09450.md | vibe-coding | Google Cursor killer (not Claude) |
| 10075.md | vibe-coding | General AI productivity |
| 10166.md | vibe-coding | Disposable Software trend |
| 10302.md | vibe-coding | Codex product manager (not Claude) |

### From ai-capability-futures/ (12 files moved)

| File | Destination | Reason |
|------|-------------|--------|
| 02538.md | meaning-civilization | Jordan Peterson Sermon on the Mount |
| 02536.jsonl | meaning-civilization | Jordan Peterson atoms |
| 00398.md | multi-agent-systems | ARCH-GRAND_ANNEALMENT syncrescendence architecture |
| 03912.md | multi-agent-systems | Autonomous AI agent team — MAS topic |
| 00062.md | openclaw | Moltbot product discussion |
| 00254.md | openclaw | camofox-browser OpenClaw tool |
| 00926.md | openclaw | Jira Cloud Integration design |
| 03069.md | openclaw | Securing ClawdBot on VPS |
| 10273.md | openclaw | ClawdBot product praise |
| 10341.md | openclaw | ClawdBot out of control — product |
| 10350.md | openclaw | ClawdBot AGI freakout — product focus |
| 10422.md | openclaw | Rise of OpenClaw — product narrative |

### From multi-agent-systems/ (4 files moved)

| File | Destination | Reason |
|------|-------------|--------|
| 04134.md | openclaw | OpenClaw self-improvement article |
| 04295.jsonl | openclaw | Sam Altman hiring OpenClaw creator |
| 10434.md | openclaw | ClawdBot analysis — product focus |
| 10742.md | vibe-coding | General AI productivity — not MAS |

## Not Moved (False Positives)

- **ai-capability-futures OpenClaw mentions** (~15 files): Content is about AI futures/AGI timelines that merely references OpenClaw as an example. Semantically correct.
- **openclaw MiniMax mentions** (~18 files): Content is about OpenClaw setups using MiniMax. Semantically about OpenClaw usage, not MiniMax as a model.
- **openclaw philosophy files** (~18 files): "Your Company is a Filesystem" and second-brain content is OpenClaw philosophy — part of the product ecosystem, not general meaning-civilization.
- **multi-agent-systems Clarescence/ops files** (~10 files): Syncrescendence operational artifacts are legitimately about multi-agent coordination.
- **claude-code archived file** (1 file: 08403.md): Orphaned but historically about Claude Code scripts.

## Updated Folder Counts (post-migration)

| Folder | Count |
|--------|-------|
| ai-models | 881 |
| multi-agent-systems | 766 |
| openclaw | 584 |
| claude-code | 552 |
| ai-capability-futures | 419 |
| ai-memory-retrieval | 392 |
| product-business | 252 |
| philosophy-esoterica | 234 |
| writing-creation | 221 |
| vibe-coding | 213 |
| meaning-civilization | 208 |
| design-taste | 194 |
| productivity-pkm | 188 |
| health-psychology | 174 |
| geopolitics-grand-strategy | 152 |
| ai-video-vfx | 123 |
| ai-safety | 96 |
| infrastructure | 94 |
| startup-vc | 79 |
| leadership-management | 50 |
| prompt-engineering | 42 |
| ai-biotech | 10 |
| uncategorized | 3 |
| **TOTAL** | **5,926** |
