# X/Twitter URL Recovery Report

**Date**: 2026-02-21
**Method**: xAI Grok API (grok-4-latest) with native X/Twitter data access
**Snowflake formula**: `(tweet_id >> 22) + 1288834974657` = epoch milliseconds

---

## Summary

| File | Status | URL | Date |
|------|--------|-----|------|
| danshipper - openai_has_some_catching_up_to_do | UNRESOLVED | Grok hallucinated 2023/2024 tweet IDs; article references Opus 4.5, GPT-5, Nov 2025 events | Est. late 2025 / early 2026 |
| exm777 - how_to_master_prompt_engineering | UNRESOLVED | NOTFOUND across all query variants | Unknown |
| kr0der - codex_has_a_hidden_spec_mode | UNRESOLVED | NOTFOUND across all query variants | Unknown |
| leocooout - post | UNRESOLVED | NOTFOUND across all query variants | Unknown |

**URLs recovered via Grok: 0**
**Dates computed from recovered URLs: 0**

---

## Detailed Findings

### 1. danshipper - "OpenAI Has Some Catching Up to Do"

- **File**: `SOURCE-undated-x-article-danshipper-openai_has_some_catching_up_to_do.md`
- **Known blog URL**: `https://every.to/chain-of-thought/openai-has-some-catching-up-to-do`
- **Grok results**: Returned two different tweet IDs across queries:
  - `1765779194739195961` -> Snowflake date: 2024-03-07 (impossible -- article references Opus 4.5, GPT-5 August launch, November 2025 testing)
  - `1641478058045545472` -> Snowflake date: 2023-03-30 (even more impossible)
- **Assessment**: Both IDs are hallucinated. The article content (Opus 4.5, GPT-5, Codex Web, events through November 2025) places it in **late November or December 2025**. Grok cannot find the actual tweet, likely because it is too recent or the tweet was deleted.
- **Content date estimate**: Late Nov 2025 - Jan 2026 (mentions "this week" re: Codex usage limit, "Tuesday night" dinner, Opus 4.5 tested "in November")

### 2. exm777 / EXM7777 - "How To Master Prompt Engineering"

- **File**: `SOURCE-undated-x-article-exm777-how_to_master_prompt_engineering.md`
- **Handle variations tried**: @exm777, @EXM7777
- **Key text searched**: "in 2026 each and every tool you use daily will eventually become a chatbox"
- **Grok result**: NOTFOUND on all attempts
- **Content date estimate**: 2026 (opening line says "in 2026")

### 3. kr0der - "Codex Has a Hidden Spec Mode"

- **File**: `SOURCE-undated-x-article-kr0der-codex_has_a_hidden_spec_mode_one_word_unlocks_it.md`
- **Handle variations tried**: @kr0der, @Krod3r
- **Key text searched**: "Codex planning felt underwhelming", "make a spec"
- **Grok result**: NOTFOUND on all attempts
- **Content date estimate**: 2025-2026 (references Codex with planning features)

### 4. leocooout - TikTok codebase file search optimization

- **File**: `SOURCE-undated-x-article-leocooout-post.md`
- **Handle tried**: @leocooout, @LeoCooOut
- **Key text searched**: "reduced the file search time in the TikTok codebase from nearly 8s to less than 200ms"
- **Grok result**: NOTFOUND on all attempts
- **Content date estimate**: 2025-2026 (references Claude Code fileSuggestion settings.json feature)

---

## Other Undated Files (Non-X, not addressable via Grok)

These 13 files are NOT X/Twitter posts and cannot be resolved via the Grok API:

### Website articles (have URLs, no dates)
| File | URL |
|------|-----|
| `SOURCE-undated-website-article-agents-agents_md_simple_open_format_guiding.md` | https://agents.md/ |
| `SOURCE-undated-website-article-huggingface-solverforge.md` | https://huggingface.co/SolverForge |
| `SOURCE-undated-website-article-soul-soul_md_what_makes_an_ai_itself.md` | https://soul.md/ |
| `SOURCE-undated-website-article-voicebox-voicebox_open_source_voice_cloning_powered.md` | https://voicebox.sh/ |

### Unknown-platform articles (no URLs, no dates)
1. `SOURCE-undated-unknown-article-chasing_next-how_to_set_up_lcaude_code_in_15_minutes_for_beginners.md` -- Note: a DATED version exists (`SOURCE-20260109-x-article-chasing_next-*`); this may be a duplicate
2. `SOURCE-undated-unknown-article-chrislaubai-13_best_claude_code_prompts.md`
3. `SOURCE-undated-unknown-article-unknown-boris_claude_code_setup.md` -- Note: a DATED version exists (`SOURCE-20260102-x-thread-bcherny-boris_created_claude_code_setup.md`); likely duplicate
4. `SOURCE-undated-unknown-article-unknown-claude_code_learning_path.md`
5. `SOURCE-undated-unknown-article-unknown-course.md`
6. `SOURCE-undated-unknown-article-unknown-how_to_set_up_claude_skills_in_15_minutes_for_nontechnical_people.md`
7. `SOURCE-undated-unknown-article-unknown-i_almost_quit_codex_after_1_day_heres_how_to_actually_use_it.md` -- Contains embedded tweet link from 2026-01-01 (`@thsottiaux` status/2006624682515247604)
8. `SOURCE-undated-unknown-article-unknown-meta_narrative_and_perspectival_schemas.md`
9. `SOURCE-undated-unknown-article-unknown-the_single_best_claude_code_prompt_steal_this.md`

---

## Snowflake Date Extractions from Existing Files

One useful extraction from body content:
- `SOURCE-undated-unknown-article-unknown-i_almost_quit_codex_after_1_day_heres_how_to_actually_use_it.md` references tweet `2006624682515247604` -> **2026-01-01** (gives a lower bound for the article date)

---

## Files Needing Rename (undated -> dated)

**None at this time.** All 4 X/Twitter URL recovery attempts failed. No dates were definitively confirmed.

### Candidates for rename if dates are confirmed manually:
| Current Name | Estimated Date | Confidence |
|-------------|---------------|------------|
| `SOURCE-undated-x-article-danshipper-openai_has_some_catching_up_to_do.md` | ~2025-11/12 | Medium (content analysis) |
| `SOURCE-undated-x-article-exm777-how_to_master_prompt_engineering.md` | 2026 | Low (only "in 2026" text) |
| `SOURCE-undated-unknown-article-unknown-i_almost_quit_codex_after_1_day_heres_how_to_actually_use_it.md` | >= 2026-01-01 | Medium (embedded tweet date) |

---

## Recommendations

1. **Manual browser verification**: Open X.com and search for these handles + keywords directly. Grok's search returned NOTFOUND for all 4, which may indicate the tweets are very recent (Feb 2026), deleted, or the handles are slightly different than recorded.
2. **Duplicate cleanup**: Files #1 and #3 in the unknown-platform list appear to be duplicates of existing dated files. Verify content overlap and remove if confirmed.
3. **Alternative date sources**: For the Dan Shipper article, check the Every.to blog page directly for a publication date -- that would at least date the content if not the tweet.
