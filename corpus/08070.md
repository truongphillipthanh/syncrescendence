# Undated → Dated Rename Log

**Date**: 2026-02-21
**Agent**: Commander (Claude Sonnet 4.6)
**Method**: Snowflake ID date computation (documented in X_URL_RECOVERY.md)
**Total renamed**: 25
**Remaining undated (need manual lookup)**: 4

---

## Rename Mappings (Old → New)

| Old Filename | New Filename | Date |
|---|---|---|
| SOURCE-undated-x-article-0xsero-conversation_with_chat_history.md | SOURCE-20260110-x-article-0xsero-conversation_with_chat_history.md | 2026-01-10 |
| SOURCE-undated-x-article-ghumare64-agents_201_orchestrating_multiple_agents_that_actu.md | SOURCE-20260116-x-article-ghumare64-agents_201_orchestrating_multiple_agents_that_actu.md | 2026-01-16 |
| SOURCE-undated-x-article-gr00vyfairy-everyone_s_talking_about_claude_cowork_for_the_wro.md | SOURCE-20260114-x-article-gr00vyfairy-everyone_s_talking_about_claude_cowork_for_the_wro.md | 2026-01-14 |
| SOURCE-undated-x-article-mert-state_machine.md | SOURCE-20260110-x-article-mert-state_machine.md | 2026-01-10 |
| SOURCE-undated-x-article-minchoi-optimization.md | SOURCE-20260103-x-article-minchoi-optimization.md | 2026-01-03 |
| SOURCE-undated-x-article-nummanali-compaction.md | SOURCE-20260110-x-article-nummanali-compaction.md | 2026-01-10 |
| SOURCE-undated-x-article-paulsolt-if_youre_new_to_codex_here_are_7_beginner_tips.md | SOURCE-20260116-x-article-paulsolt-if_youre_new_to_codex_here_are_7_beginner_tips.md | 2026-01-16 |
| SOURCE-undated-x-article-steipete-shipping_at_inference_speed.md | SOURCE-20251229-x-article-steipete-shipping_at_inference_speed.md | 2025-12-29 |
| SOURCE-undated-x-article-thezvi-claude_codes.md | SOURCE-20260108-x-article-thezvi-claude_codes.md | 2026-01-08 |
| SOURCE-undated-x-article-vasuman-ai_agents_101.md | SOURCE-20260116-x-article-vasuman-ai_agents_101.md | 2026-01-16 |
| SOURCE-undated-x-transcript-aiedge-claude_code_starter_pack_p2.md | SOURCE-20260116-x-transcript-aiedge-claude_code_starter_pack_p2.md | 2026-01-16 |
| SOURCE-undated-x-transcript-armanhezarkhani-complete_guide_learn_anything.md | SOURCE-20260123-x-transcript-armanhezarkhani-complete_guide_learn_anything.md | 2026-01-23 |
| SOURCE-undated-x-transcript-bcherny-claude_cowork_code_lesson.md | SOURCE-20260123-x-transcript-bcherny-claude_cowork_code_lesson.md | 2026-01-23 |
| SOURCE-undated-x-transcript-bui1987-nelson_autonomous_coding.md | SOURCE-20260123-x-transcript-bui1987-nelson_autonomous_coding.md | 2026-01-23 |
| SOURCE-undated-x-transcript-chasing_next-manus_ai_setup_guide.md | SOURCE-20260115-x-transcript-chasing_next-manus_ai_setup_guide.md | 2026-01-15 |
| SOURCE-undated-x-transcript-froessell-ai_design_toolkit_2026.md | SOURCE-20260203-x-transcript-froessell-ai_design_toolkit_2026.md | 2026-02-03 |
| SOURCE-undated-x-transcript-ganimcorey-10_more_clawdbot_setups.md | SOURCE-20260204-x-transcript-ganimcorey-10_more_clawdbot_setups.md | 2026-02-04 |
| SOURCE-undated-x-transcript-gregisenberg-claude_cowork_qt.md | SOURCE-20260123-x-transcript-gregisenberg-claude_cowork_qt.md | 2026-01-23 |
| SOURCE-undated-x-transcript-honchodotdev-openclaw_honcho_memory.md | SOURCE-20260203-x-transcript-honchodotdev-openclaw_honcho_memory.md | 2026-02-03 |
| SOURCE-undated-x-transcript-kekius_sage-ground_up_math.md | SOURCE-20260123-x-transcript-kekius_sage-ground_up_math.md | 2026-01-23 |
| SOURCE-undated-x-transcript-kimiproduct-kimi_openclaw_simplest_setup.md | SOURCE-20260204-x-transcript-kimiproduct-kimi_openclaw_simplest_setup.md | 2026-02-04 |
| SOURCE-undated-x-transcript-oprydai-hardware_homelab.md | SOURCE-20260204-x-transcript-oprydai-hardware_homelab.md | 2026-02-04 |
| SOURCE-undated-x-transcript-saboo_shubham-ai_agents_learn_skills.md | SOURCE-20260204-x-transcript-saboo_shubham-ai_agents_learn_skills.md | 2026-02-04 |
| SOURCE-undated-x-transcript-seejayhess-the_swarm_has_arrived.md | SOURCE-20260124-x-transcript-seejayhess-the_swarm_has_arrived.md | 2026-01-24 |
| SOURCE-undated-x-transcript-shpigford-kimi_k25_free_nvidia.md | SOURCE-20260203-x-transcript-shpigford-kimi_k25_free_nvidia.md | 2026-02-03 |

---

## Frontmatter Changes

### id: field
- Files with `id: SOURCE-undated-x-{format}-{creator}-{title}` pattern (7 files): id updated to match new filename stem.
- Files with `id: SOURCE-undated-NNN` numeric pattern (18 files): id left as-is (numeric IDs are stable references; not tied to filename).

### date_published: field
- Files that already had `date_published:` set: left unchanged (already populated by URL recovery step).
- Files missing `date_published:` entirely (7 article files): field added after `id:` line with computed date.

---

## Still Undated (4 files — need manual lookup)

| Filename | Blocker |
|---|---|
| SOURCE-undated-x-article-danshipper-openai_has_some_catching_up_to_do.md | Every.to newsletter article; no X tweet URL found |
| SOURCE-undated-x-article-exm777-how_to_master_prompt_engineering.md | X handle @EXM7777 found but tweet not located |
| SOURCE-undated-x-article-kr0der-codex_has_a_hidden_spec_mode_one_word_unlocks_it.md | Multiple kr0der posts found, not this exact one |
| SOURCE-undated-x-article-leocooout-post.md | X handle not found |
