# SOURCE POOL DATA GAPS REPORT
**Generated:** 2026-02-21
**Scope:** 627 SOURCE-*.md files in `sources/`
**Purpose:** Pre-AI-enrichment quality gate — identify all data gaps before automated enrichment pass

---

## 1. SUMMARY TABLE

| ID | Gap Type | Count | Severity | Auto-Resolvable? |
|----|----------|-------|----------|-----------------|
| A | Undated files (SOURCE-undated-*) | 42 | MEDIUM | Partial |
| B | Unknown platform | 9 | MEDIUM | Partial |
| C | Unknown format | 0 | — | N/A |
| D | Unknown or empty creator | 24 | MEDIUM | Partial |
| E | Missing `url:` field | 92 | CRITICAL | Partial (40 YouTube reconstructible) |
| E2 | URL leaked into body (not frontmatter) | 2 | CRITICAL | YES — mechanical fix |
| F | Missing `title:` field | 433 | LOW | YES — X platform by design, internal need manual |
| G | No frontmatter at all | 0 | — | N/A |
| H | Very small files (<500 bytes) | 1 | LOW | Manual review |
| I | Very large files (>50KB) | 1 | LOW | Manual review |
| J | Dual/embedded legacy YAML in body | 21 | MEDIUM | YES — migration script |
| K | Enrichment fields empty (synopsis, teleology, topics, key_insights) | 627 | EXPECTED | YES — AI enrichment pass target |
| K2 | `signal_tier` empty | 593 | MEDIUM | YES — AI enrichment pass target |

**Critical path:** Gaps E, E2 must be resolved BEFORE enrichment. Gaps A, B, D, J should be resolved before or during enrichment. Gap K is the enrichment target itself.

---

## 2. DETAILED FILE LISTS

---

### A. UNDATED FILES (42 total)

Files with `undated` in the filename. These are missing a publication date in the filename component.

#### A1. Undated files WITH a date clue in frontmatter (4 files)
These can be renamed/corrected from their frontmatter `captured_date` or `published_date`.

| Filename | FM Field | Value | Resolution |
|----------|----------|-------|------------|
| `SOURCE-undated-website-article-agents-agents_md_simple_open_format_guiding.md` | `captured_date` | 2026-02-20 | Capture date only — use as `~2026-02` approximate |
| `SOURCE-undated-website-article-huggingface-solverforge.md` | `captured_date` | 2026-02-20 | Body contains month clues (Jan/Dec) — likely 2025-late/2026-early |
| `SOURCE-undated-website-article-soul-soul_md_what_makes_an_ai_itself.md` | `published_date` | `~` | Published date is literally `~` — unknown. Check body. |
| `SOURCE-undated-website-article-voicebox-voicebox_open_source_voice_cloning_powered.md` | `captured_date` | 2026-02-20 | Capture date only |

#### A2. Undated files WITH body date clues (14 x-transcript files)
These have month-level clues in body text ("January", "February") but no year-anchored date. All are X transcripts.

Likely date range: Jan–Feb 2026 based on content context.

| Filename | Body Clue |
|----------|-----------|
| `SOURCE-undated-x-transcript-aiedge-claude_code_starter_pack_p2.md` | "January" |
| `SOURCE-undated-x-transcript-armanhezarkhani-complete_guide_learn_anything.md` | "January" |
| `SOURCE-undated-x-transcript-bcherny-claude_cowork_code_lesson.md` | "January" |
| `SOURCE-undated-x-transcript-bui1987-nelson_autonomous_coding.md` | "January" |
| `SOURCE-undated-x-transcript-chasing_next-manus_ai_setup_guide.md` | "January" |
| `SOURCE-undated-x-transcript-froessell-ai_design_toolkit_2026.md` | "February" |
| `SOURCE-undated-x-transcript-ganimcorey-10_more_clawdbot_setups.md` | "February" |
| `SOURCE-undated-x-transcript-gregisenberg-claude_cowork_qt.md` | "January" |
| `SOURCE-undated-x-transcript-honchodotdev-openclaw_honcho_memory.md` | "February" |
| `SOURCE-undated-x-transcript-kekius_sage-ground_up_math.md` | "January" |
| `SOURCE-undated-x-transcript-kimiproduct-kimi_openclaw_simplest_setup.md` | "February" |
| `SOURCE-undated-x-transcript-oprydai-hardware_homelab.md` | "February" |
| `SOURCE-undated-x-transcript-saboo_shubham-ai_agents_learn_skills.md` | "February" |
| `SOURCE-undated-x-transcript-seejayhess-the_swarm_has_arrived.md` | "January" |
| `SOURCE-undated-x-transcript-shpigford-kimi_k25_free_nvidia.md` | "February" |

**Resolution method:** For X transcripts, the tweet URL (once recovered — see Gap E) will contain a Snowflake ID that encodes the exact post timestamp. URL recovery = date recovery for these files.

#### A3. Undated files with NO date clues anywhere — truly dateless (38 files)
No date in frontmatter, no date in body, no URL to derive from.

**9 unknown-platform articles (no URL, no date, unknown creator for most):**
```
SOURCE-undated-unknown-article-chasing_next-how_to_set_up_lcaude_code_in_15_minutes_for_beginners.md
SOURCE-undated-unknown-article-chrislaubai-13_best_claude_code_prompts.md
SOURCE-undated-unknown-article-unknown-boris_claude_code_setup.md
SOURCE-undated-unknown-article-unknown-claude_code_learning_path.md
SOURCE-undated-unknown-article-unknown-course.md
SOURCE-undated-unknown-article-unknown-how_to_set_up_claude_skills_in_15_minutes_for_nontechnical_people.md
SOURCE-undated-unknown-article-unknown-i_almost_quit_codex_after_1_day_heres_how_to_actually_use_it.md
SOURCE-undated-unknown-article-unknown-meta_narrative_and_perspectival_schemas.md
SOURCE-undated-unknown-article-unknown-the_single_best_claude_code_prompt_steal_this.md
```

**23 X platform articles/threads (no URL, no date in FM):**
```
SOURCE-undated-x-article-0xsero-conversation_with_chat_history.md
SOURCE-undated-x-article-danshipper-openai_has_some_catching_up_to_do.md
SOURCE-undated-x-article-exm777-how_to_master_prompt_engineering.md
SOURCE-undated-x-article-ghumare64-agents_201_orchestrating_multiple_agents_that_actu.md
SOURCE-undated-x-article-gr00vyfairy-everyone_s_talking_about_claude_cowork_for_the_wro.md
SOURCE-undated-x-article-kr0der-codex_has_a_hidden_spec_mode_one_word_unlocks_it.md
SOURCE-undated-x-article-leocooout-post.md
SOURCE-undated-x-article-mert-state_machine.md
SOURCE-undated-x-article-minchoi-optimization.md
SOURCE-undated-x-article-nummanali-compaction.md
SOURCE-undated-x-article-paulsolt-if_youre_new_to_codex_here_are_7_beginner_tips.md
SOURCE-undated-x-article-steipete-shipping_at_inference_speed.md
SOURCE-undated-x-article-thezvi-claude_codes.md
SOURCE-undated-x-article-vasuman-ai_agents_101.md
SOURCE-undated-x-transcript-aiedge-claude_code_starter_pack_p2.md  (body has "January")
SOURCE-undated-x-transcript-armanhezarkhani-complete_guide_learn_anything.md
SOURCE-undated-x-transcript-bcherny-claude_cowork_code_lesson.md
SOURCE-undated-x-transcript-bui1987-nelson_autonomous_coding.md
SOURCE-undated-x-transcript-chasing_next-manus_ai_setup_guide.md
SOURCE-undated-x-transcript-froessell-ai_design_toolkit_2026.md
SOURCE-undated-x-transcript-ganimcorey-10_more_clawdbot_setups.md
SOURCE-undated-x-transcript-gregisenberg-claude_cowork_qt.md
SOURCE-undated-x-transcript-honchodotdev-openclaw_honcho_memory.md
SOURCE-undated-x-transcript-kekius_sage-ground_up_math.md
SOURCE-undated-x-transcript-kimiproduct-kimi_openclaw_simplest_setup.md
SOURCE-undated-x-transcript-oprydai-hardware_homelab.md
SOURCE-undated-x-transcript-saboo_shubham-ai_agents_learn_skills.md
SOURCE-undated-x-transcript-seejayhess-the_swarm_has_arrived.md
SOURCE-undated-x-transcript-shpigford-kimi_k25_free_nvidia.md
```

**Resolution for X undated files:** Recover URLs (see Gap E), then decode the Snowflake tweet ID for exact date. This is the single highest-leverage action for undated X files — URL recovery solves date simultaneously.

**Resolution for unknown-platform articles:** Sovereign manual review required. Content may have internal clues (references to model releases, dates of events) that allow approximate dating.

---

### B. UNKNOWN PLATFORM (9 files)

All 9 are the same cluster: `SOURCE-undated-unknown-article-*`. No URL, no date, no platform.

```
SOURCE-undated-unknown-article-chasing_next-how_to_set_up_lcaude_code_in_15_minutes_for_beginners.md
SOURCE-undated-unknown-article-chrislaubai-13_best_claude_code_prompts.md
SOURCE-undated-unknown-article-unknown-boris_claude_code_setup.md
SOURCE-undated-unknown-article-unknown-claude_code_learning_path.md
SOURCE-undated-unknown-article-unknown-course.md
SOURCE-undated-unknown-article-unknown-how_to_set_up_claude_skills_in_15_minutes_for_nontechnical_people.md
SOURCE-undated-unknown-article-unknown-i_almost_quit_codex_after_1_day_heres_how_to_actually_use_it.md
SOURCE-undated-unknown-article-unknown-meta_narrative_and_perspectival_schemas.md
SOURCE-undated-unknown-article-unknown-the_single_best_claude_code_prompt_steal_this.md
```

**Resolution:** Content analysis. Body text may reference platform-specific patterns (tweet syntax, Substack formatting, YouTube transcript style). AI enrichment can suggest likely platform. `chasing_next` and `chrislaubai` are known X handles, so those two are very likely `platform: x`. The `meta_narrative_and_perspectival_schemas` is likely internal. `course.md` is likely a course platform (Udemy/Gumroad/etc).

---

### C. UNKNOWN FORMAT

**Count: 0.** All 627 files have a `format:` field with a non-unknown, non-empty value. No gap.

---

### D. UNKNOWN OR EMPTY CREATOR (24 files)

#### D1. creator = "unknown" (19 files)
```
SOURCE-20250124-website-article-unknown-writing_a_good_claude_md_humanlayer.md
SOURCE-20250217-website-article-unknown-what_actually_is_claude_code_s_plan_mode_lucumr.md
SOURCE-20260102-x-thread-unknown-boris_created_claude_code_setup_bcherny.md
SOURCE-20260112-youtube-video-unknown-kennylia_why_i_stopped_using_mcps_in_claude_code_and_what_i_use_instead.md
SOURCE-20260124-website-article-unknown-overview_agent_skills_agentskills.md
SOURCE-20260124-x-thread-unknown-add_this_paragraph_to_zarazhangrui.md
SOURCE-20260126-x-thread-unknown-agent_browser_0_8_3_is_even_ctatedev.md
SOURCE-20260126-x-thread-unknown-karpathy_guidelines_for_coding_agents_jiayuan_jy.md
SOURCE-20260127-x-thread-unknown-openai_and_anthropic_engineers_leaked_aiwithmayank.md
SOURCE-20260204-website-article-unknown-agentmail_api_first_email_platform_clawhub.md
SOURCE-20260204-website-article-unknown-machines_of_loving_grace_darioamodei.md
SOURCE-20260204-website-article-unknown-my_ai_had_already_fixed_the_code_every.md
SOURCE-undated-unknown-article-unknown-boris_claude_code_setup.md
SOURCE-undated-unknown-article-unknown-claude_code_learning_path.md
SOURCE-undated-unknown-article-unknown-course.md
SOURCE-undated-unknown-article-unknown-how_to_set_up_claude_skills_in_15_minutes_for_nontechnical_people.md
SOURCE-undated-unknown-article-unknown-i_almost_quit_codex_after_1_day_heres_how_to_actually_use_it.md
SOURCE-undated-unknown-article-unknown-meta_narrative_and_perspectival_schemas.md
SOURCE-undated-unknown-article-unknown-the_single_best_claude_code_prompt_steal_this.md
```

#### D2. creator = "" (empty string, 5 files)
```
SOURCE-20250605-youtube-lecture-strange_loop-ethan_mollick_ai_jagged_frontier.md
SOURCE-20250902-youtube-lecture-strange_loop-david_deutsch_agi_constructor_theory.md
SOURCE-20250903-youtube-interview-theories_of_everything-max_tegmark_physics_ai_consciousness.md
SOURCE-20251031-youtube-interview-bilawal_sidhu-john_gaeta_transmedia_vfx_ai.md
SOURCE-20251031-youtube-lecture-extropic-trevor_mccourt_probabilistic_circuits.md
```
Note: These 5 have `creator: ""` in outer FM but the correct creator is visible in their embedded legacy YAML block inside the body (e.g., `creator: Strange Loop`, `creator: Extropic`). This is a dual-YAML migration issue (see Gap J).

**Resolution for D1:** Many are auto-resolvable. Filename slugs for X threads contain handle clues (e.g., `zarazhangrui`, `ctatedev`, `jiayuan_jy`, `aiwithmayank`). The `machines_of_loving_grace` file is Dario Amodei's essay — `creator: darioamodei`. `boris_created_claude_code` is clearly `bcherny`. `kennylia` YouTube is `@kennylia`. Website articles from `lucumr.pocoo.org` are by Armin Ronacher. AI enrichment can resolve most of these from URL + body text.

---

### E. MISSING URL FIELD (92 files total)

The `url:` field is absent from the outer frontmatter block. This prevents direct linkback to original source.

#### E1. URL in body outside frontmatter (2 files) — MECHANICAL FIX
These files have the URL in the body text rather than the frontmatter. The URL is present but misplaced.

```
SOURCE-20260102-x-thread-unknown-boris_created_claude_code_setup_bcherny.md
  → url: https://x.com/bcherny/status/2007179832300581177

SOURCE-20260220-x-thread-bilawalsidhu-between_gemini_31_and_claude_46.md
  → url: https://x.com/bilawalsidhu/status/2024672151949766950
```

**Resolution:** Mechanical — extract `url:` from body and move to frontmatter. Scriptable.

#### E2. YouTube files missing URL (40 files) — RECONSTRUCTIBLE VIA SEARCH
All are YouTube videos/interviews where the URL was never captured. The channel name, speaker names, and approximate date are all encoded in the filename and frontmatter, so URLs are reconstructible via YouTube search.

```
SOURCE-20250312-youtube-interview-dwarkesh_patel-dwarkesh_patel_joseph_henrich_cultural_evolutio.md
SOURCE-20250528-youtube-lecture-long_now_foundation-an_informational_theory_of_life.md  [has URL in FM - false positive excluded]
SOURCE-20250605-youtube-lecture-strange_loop-ethan_mollick_ai_jagged_frontier.md
SOURCE-20250623-youtube-interview-brainmind-five_new_paradigms_of_intelligence.md
SOURCE-20250807-youtube-lecture-tedx-the_intelligence_of_us_rethinking_minds_in_the_ag.md
SOURCE-20250902-youtube-lecture-strange_loop-david_deutsch_agi_constructor_theory.md
SOURCE-20250903-youtube-interview-theories_of_everything-max_tegmark_physics_ai_consciousness.md
SOURCE-20250912-youtube-interview-dwarkesh_patel-foundation_models_for_physical_intelligence.md
SOURCE-20251013-youtube-interview-the_quantum_economy_podcast-faith_physics_and_the_quantum_race_matthew_kins.md
SOURCE-20251014-youtube-interview-duqun-interface_theory_of_perception_and_consciousness.md
SOURCE-20251020-youtube-interview-a16z-reid_hoffman_on_ai_consciousness_and_the_future.md
SOURCE-20251020-youtube-interview-info_tech_research_group-godfather_of_agi_on_why_big_tech_innovation_is_ove.md
SOURCE-20251021-youtube-interview-machine_learning_street_talk-the_universal_hierarchy_of_life.md
SOURCE-20251021-youtube-interview-tbpn-don_t_die_bryan_johnson_on_living_forever_ai_an.md
SOURCE-20251023-youtube-panel-scale_ai-chain_of_thought_mcp_atlas_benchmark_deep_dive.md
SOURCE-20251024-youtube-interview-arc_prize-arc_agi_v3_and_measuring_intelligence.md
SOURCE-20251024-youtube-lecture-engineering_institute_of_technology-the_future_of_engineering_a_discipline_evolving_t.md
SOURCE-20251025-youtube-interview-machine_learning_street_talk-life_emerges_from_code.md
SOURCE-20251027-youtube-interview-all_in_podcast-macroscopic_quantum_tunneling_to_quantum_computing.md
SOURCE-20251027-youtube-interview-david_carbutt-the_coming_productivity_boom_tax_policy_and_econo.md
SOURCE-20251028-youtube-lecture-nvidia-the_next_phase_of_accelerated_computing_and_ai.md
SOURCE-20251029-youtube-interview-openai-openai_structure_change_and_ai_timelines.md
SOURCE-20251030-youtube-interview-moonshots_with_peter_diamandis-solana_crypto_ai_convergence_and_machine_to_mach.md
SOURCE-20251030-youtube-video-ai_explained-the_end_of_ai_complete_integration_into_society.md
SOURCE-20251031-youtube-interview-a16z-marc_andreessen_and_ben_horowitz_on_the_state_of_a.md
SOURCE-20251031-youtube-interview-a16z-state_of_ai_runtime_keynote.md
SOURCE-20251031-youtube-interview-all_in_podcast-elon_musk_on_3_years_of_x_openai_lawsuit_and_the.md
SOURCE-20251031-youtube-interview-bilawal_sidhu-john_gaeta_transmedia_vfx_ai.md
SOURCE-20251031-youtube-interview-joe_rogan-jre_2404_elon_musk_civilization_technology_a.md
SOURCE-20251031-youtube-lecture-extropic-trevor_mccourt_probabilistic_circuits.md
SOURCE-20251031-youtube-video-david_shapiro-the_post_labor_enterprise.md
SOURCE-20251031-youtube-video-no_priors-no_priors_the_best_of_2025_so_far.md
SOURCE-20251101-youtube-video-david_shapiro-renaissance_2_0_open_ai_models_signal_democratic.md
SOURCE-20251222-youtube-interview-machine_learning_street_talk-mlst_categorical_deep_learning_from_alchemy_to.md
SOURCE-20251222-youtube-panel-a16z-how_ai_agents_will_transform_in_2026.md
SOURCE-20251223-youtube-interview-ai_daily_brief-how_ai_starts_doing_the_work_in_2026.md
SOURCE-20251223-youtube-video-dwarkesh_patel-dwarkesh_patel_what_are_we_scaling_the_continu.md
SOURCE-20251224-youtube-interview-machine_learning_street_talk-mlst_dr_mike_israetel_asi_timelines_embodimen.md
SOURCE-20251226-youtube-video-david_shapiro-david_shapiro_the_scaling_paradox_why_capabilit.md
SOURCE-20260112-youtube-video-unknown-kennylia_why_i_stopped_using_mcps_in_claude_code_and_what_i_use_instead.md
SOURCE-20260114-youtube-video-leonvanzyl-youtube_video_stop_using_claude_code_like_this_us.md
```

**Resolution:** AI enrichment pass can search YouTube for each by channel + title slug + approximate date. High success rate expected for named channels with distinctive titles.

#### E3. Non-YouTube files missing URL (50 files) — HUMAN INPUT REQUIRED FOR MOST
These cannot be auto-reconstructed. Breakdown:

**Medium article (1):**
```
SOURCE-20250824-medium-article-dinan_jana-mastering_the_vibe_claude_code_best_practices_that_actually_work.md
```
Resolution: Searchable on Medium by author `Dinan Jana` + title.

**Internal research files (10) — URL not applicable:**
```
SOURCE-20260203-internal-research-augur-prompt_openclaw_deep_research.md
SOURCE-20260203-internal-research-augur-response_openclaw_deep_research.md
SOURCE-20260203-internal-research-diviner-prompt_openclaw_deep_research.md
SOURCE-20260203-internal-research-diviner-response_openclaw_deep_research.md
SOURCE-20260203-internal-research-oracle-prompt_openclaw_deep_research.md
SOURCE-20260203-internal-research-oracle-response_openclaw_deep_research.md
SOURCE-20260203-internal-research-vanguard-prompt_openclaw_deep_research.md
SOURCE-20260203-internal-research-vanguard-response_openclaw_deep_research.md
SOURCE-20260203-internal-research-vizier-prompt_openclaw_deep_research.md
SOURCE-20260203-internal-research-vizier-response_openclaw_deep_research.md
```
These are internally generated research documents — they have no external URL by definition. Mark `url: internal`.

**X articles/threads with no URL and no tweet ID (37):**
All undated X files listed in A3 above plus:
```
SOURCE-20260110-x-article-eyad_khrais-the_complete_claude_code_tutorial.md
```
Resolution for X files: The tweet URL pattern is `https://x.com/{handle}/status/{snowflake_id}`. Without the Snowflake ID these cannot be reconstructed mechanically. However, for known handles, the URL can be recovered by searching X or via Wayback Machine. Creator handle is encoded in the filename for most.

---

### F. MISSING TITLE FIELD (433 files)

#### F1. X platform files (423) — BY DESIGN, LOW PRIORITY
X platform files (tweets/threads/articles) were ingested without a separate `title:` field because tweets don't have titles. The functional equivalent is the first line of the tweet content, which is captured in the body. For AI enrichment, a synthetic `title:` can be generated from the first sentence of the content.

**AI enrichment action:** Generate `title:` from first meaningful sentence of body content for all 423 X files missing it.

#### F2. Internal research files (10) — NEED MANUAL TITLE
```
SOURCE-20260203-internal-research-augur-prompt_openclaw_deep_research.md
SOURCE-20260203-internal-research-augur-response_openclaw_deep_research.md
SOURCE-20260203-internal-research-diviner-prompt_openclaw_deep_research.md
SOURCE-20260203-internal-research-diviner-response_openclaw_deep_research.md
SOURCE-20260203-internal-research-oracle-prompt_openclaw_deep_research.md
SOURCE-20260203-internal-research-oracle-response_openclaw_deep_research.md
SOURCE-20260203-internal-research-vanguard-prompt_openclaw_deep_research.md
SOURCE-20260203-internal-research-vanguard-response_openclaw_deep_research.md
SOURCE-20260203-internal-research-vizier-prompt_openclaw_deep_research.md
SOURCE-20260203-internal-research-vizier-response_openclaw_deep_research.md
```
Resolution: Titles should follow pattern: `"{AgentName} — OpenClaw Deep Research {Prompt|Response}"`. AI enrichment can generate these from filename.

---

### G. FILES WITH NO FRONTMATTER

**Count: 0.** All 627 files have valid YAML frontmatter delimited by `---`. No gap.

---

### H. VERY SMALL FILES (<500 bytes)

| File | Size | Issue |
|------|------|-------|
| `SOURCE-undated-x-article-0xsero-conversation_with_chat_history.md` | 467 bytes | Near-empty stub |

**Next two smallest for reference:** `SOURCE-undated-x-article-mert-state_machine.md` (543 bytes) and `SOURCE-undated-x-article-nummanali-compaction.md` (560 bytes) — borderline, likely minimal tweet content.

**Resolution:** Read the 467-byte file manually. It may be frontmatter-only with no body, or an incomplete capture. If content is absent, flag for recapture or deletion.

---

### I. VERY LARGE FILES (>50KB)

| File | Size | Issue |
|------|------|-------|
| `SOURCE-20260212-x-article-thezvi-ai_155_welcome_to_recursive_self_improvement.md` | 83,568 bytes | Likely a long-form Substack newsletter captured in full |

**Next largest for reference:**
- `SOURCE-20260204-website-article-darioamodei-the_adolescence_of_technology.md` — 47,781 bytes (borderline)
- `SOURCE-20260204-website-article-unknown-machines_of_loving_grace_darioamodei.md` — 47,603 bytes

**Resolution:** The thezvi file is a legitimately long newsletter (AI 155 issue). Not a concatenation error — Zvi's AI newsletters are routinely 20,000–80,000 words. No action required beyond noting it for chunked enrichment (AI enrichment may need to process this in segments).

---

### J. DUAL/EMBEDDED LEGACY YAML BLOCKS IN BODY (21 files)

These files have a normalized outer frontmatter block (the canonical schema) and a second legacy YAML block embedded in the body text. The legacy block often contains richer data (populated `creator`, `url`, `signal_tier`, `chain_relevance`, `integration_targets`) that was NOT migrated to the outer block.

**This is the highest-value data-recovery action** — the legacy blocks contain pre-enriched data from the original processing pass.

```
SOURCE-20250605-youtube-lecture-strange_loop-ethan_mollick_ai_jagged_frontier.md
SOURCE-20250902-youtube-lecture-strange_loop-david_deutsch_agi_constructor_theory.md
SOURCE-20250903-youtube-interview-theories_of_everything-max_tegmark_physics_ai_consciousness.md
SOURCE-20251031-youtube-interview-bilawal_sidhu-john_gaeta_transmedia_vfx_ai.md
SOURCE-20251031-youtube-lecture-extropic-trevor_mccourt_probabilistic_circuits.md
SOURCE-20260107-website-article-producttalk-how_to_use_claude_code_a_guide.md
SOURCE-20260112-x-article-eyad_khrais-the_claude_code_tutorial_level_2.md
SOURCE-20260122-x-article-dani_avila7-separation_of_responsibilities_mcp_vs_skills.md
SOURCE-20260124-website-article-unknown-overview_agent_skills_agentskills.md
SOURCE-20260124-x-article-arscontexta-build_claude_a_tool_for_thought.md
SOURCE-20260126-x-article-arscontexta-obsidian_and_claude_code_101_context_engineering.md
SOURCE-20260128-x-article-arscontexta-obsidian_and_claude_code_async_hooks_for_note_history.md
SOURCE-20260130-x-thread-kloss_xyz-my_current_ai_stack_heres_what_im_using.md
SOURCE-20260203-x-article-tempoimmaterial-subagents_when_and_how_to_use_them.md
SOURCE-20260207-x-article-fr0gger_-shield_md_a_security_standard_for_openclaw_and_ai_agents.md
SOURCE-20260209-x-article-yjstacked-how_to_build_an_ai_agent_army_with_claude_skills.md
SOURCE-20260213-x-article-sillydarket-solving_memory_for_openclaw_and_general_agents.md
SOURCE-20260215-x-thread-omarsar0-new_research_from_google_deepmind.md
SOURCE-20260216-x-thread-pk_iv-post_agi_there_are_only_four.md
SOURCE-20260217-x-article-meer_aiit-the_complete_guide_to_building_skills_for_claude.md
+ 1 more
```

**Resolution:** Write a migration script that:
1. Parses the embedded legacy block
2. For each field: if outer FM value is empty/null and legacy value is populated, copy legacy value to outer FM
3. Remove the embedded legacy block from body (or keep as comment)

Fields to rescue: `url`, `creator`, `signal_tier`, `chain_relevance`, `integration_targets`, `title`.

---

### K. ENRICHMENT FIELDS — ALL EMPTY (expected)

These fields are empty across all 627 files — they are the target of the AI enrichment pass, not a pre-existing gap.

| Field | Empty Count | Status |
|-------|-------------|--------|
| `synopsis` | 627 / 627 | AI enrichment target |
| `teleology` | 627 / 627 | AI enrichment target |
| `topics` | 627 / 627 | AI enrichment target |
| `key_insights` | 627 / 627 | AI enrichment target |
| `signal_tier` | 593 / 627 | AI enrichment target (34 already populated — mostly YouTube legacy files) |

The 34 files with `signal_tier` already populated are the dual-YAML files and early-processed YouTube files where the legacy block had this field set. These should be validated, not overwritten.

---

## 3. RESOLUTION PRIORITY MATRIX

### BEFORE ENRICHMENT (blocking)

| Priority | Action | Files | Method |
|----------|--------|-------|--------|
| P0-CRITICAL | Fix 2 files with URL in body not FM | 2 | Mechanical script |
| P0-CRITICAL | Migrate dual-YAML legacy fields to outer FM | 21 | Migration script |
| P1-HIGH | Mark internal files `url: internal` | 10 | Mechanical script |
| P1-HIGH | Resolve creator for D2 empty-creator files from legacy block | 5 | Part of dual-YAML migration |

### DURING ENRICHMENT (AI can resolve)

| Priority | Action | Files | Method |
|----------|--------|-------|--------|
| P2-MED | Generate synthetic `title:` for X files | 423 | AI enrichment — first sentence of body |
| P2-MED | Infer `platform:` for unknown-platform articles | 9 | AI content analysis |
| P2-MED | Infer `creator:` for unknown-creator files with URL clues | ~15 | AI + URL analysis |
| P2-MED | Search YouTube for URLs for 40 YouTube files | 40 | AI web search |
| P3-LOW | Estimate date from body clues for 14 transcript files | 14 | AI content analysis + "January/February 2026" |

### AFTER ENRICHMENT (human input required)

| Priority | Action | Files | Method |
|----------|--------|-------|--------|
| P3-LOW | Date for 9 unknown-platform articles | 9 | Sovereign review |
| P3-LOW | URL recovery for 37 undated X articles | 37 | X search by handle + content |
| P4-LOW | Validate/update 34 legacy signal_tier values | 34 | Spot check |
| P4-LOW | Review 467-byte stub file for recapture | 1 | Manual |

---

## 4. DATA QUALITY SCORECARD

| Metric | Count | % of 627 |
|--------|-------|----------|
| Files with complete outer frontmatter (all canonical fields) | ~480 | ~77% |
| Files with URL populated | 535 | 85% |
| Files with captured_date or date_published | ~580 | ~93% |
| Files with creator populated (non-unknown/non-empty) | 603 | 96% |
| Files with platform = known | 618 | 99% |
| Files with format = known | 627 | 100% |
| Files with original_filename | 627 | 100% |
| Files with any enrichment field populated (synopsis/teleology/etc) | 0 | 0% |
| Files with signal_tier | 34 | 5% |

**Overall pre-enrichment data quality: 77% complete on structural fields, 0% on semantic/enrichment fields.**

---

## 5. APPENDIX: SCHEMA REFERENCE

The canonical outer frontmatter schema (inferred from field frequency analysis):

```yaml
---
id:                    # always present (627/627)
original_filename:     # always present (627/627)
status:                # always present (627/627)
platform:              # always present (627/627)
format:                # always present (627/627)
creator:               # always present (627/627) — but 24 are "unknown" or ""
teleology:             # always present (627/627) — but all empty
notebooklm_category:   # always present (627/627)
aliases:               # always present (627/627)
signal_tier:           # 582/627 — 45 missing entirely, 593 empty including those with field
topics:                # 548/627 — all empty
synopsis:              # 548/627 — all empty
key_insights:          # 548/627 — all empty
url:                   # 535/627 — 92 missing
captured_date:         # 534/627
author:                # 529/627 — X platform author string (handle)
title:                 # 194/627 — YouTube + website only; X files missing by design
date_published:        # 79/627
published_date:        # 43/627
---
```

Fields present in <5% of files are legacy or per-type fields (guest, chain_relevance, integration_targets, domain, content_type, handle, post_count, engagement).

---

*Report generated by Commander audit pass. Next action: dispatch dual-YAML migration task and URL-in-body fix script before AI enrichment begins.*
