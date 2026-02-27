# YouTube URL Recovery - Final Report

**Date**: 2026-02-21
**Agent**: Commander (Claude Opus 4.6)
**Method**: WebSearch + WebFetch via startuphub.ai, podwise.ai, and other intermediary sites (YouTube Data API v3 was NOT enabled for the provided Google Cloud project)

## API Key Issue

The YouTube Data API v3 key `AIzaSyDSYHoMKhDvKE8ELtH0RIp3nQ9C6bNxOYY` returned HTTP 403:
> "YouTube Data API v3 has not been used in project 152977485256 before or it is disabled."

**Action required**: Enable YouTube Data API v3 at:
https://console.developers.google.com/apis/api/youtube.googleapis.com/overview?project=152977485256

All recoveries below were performed via web search and intermediary site scraping instead.

## Summary

| Metric | Count |
|--------|-------|
| Total YouTube SOURCE files | 41 |
| URLs recovered (prior session) | 9 |
| URLs recovered (this session) | 9 |
| **Total files with valid URLs** | **18** |
| Placeholder URL (Long Now) | 1 |
| **Still missing** | **22** |

## URLs Recovered This Session

| # | File | YouTube URL | Source |
|---|------|-------------|--------|
| 1 | SOURCE-20251021-...-the_universal_hierarchy_of_life.md | https://www.youtube.com/watch?v=iwClZ-7OweY | podwise.ai episode page |
| 2 | SOURCE-20251031-...-marc_andreessen_and_ben_horowitz_on_the_state_of_a.md | https://www.youtube.com/watch?v=Y7dwbJ0AtUA | startuphub.ai embedded player |
| 3 | SOURCE-20251031-...-state_of_ai_runtime_keynote.md | https://www.youtube.com/watch?v=Y7dwbJ0AtUA | Same video as #2 (duplicate capture) |
| 4 | SOURCE-20251031-...-elon_musk_on_3_years_of_x_openai_lawsuit_and_the.md | https://www.youtube.com/watch?v=j6_VfR-CyuM | drwilsonwang.substack.com cover image |
| 5 | SOURCE-20251031-...-jre_2404_elon_musk_civilization_technology_a.md | https://www.youtube.com/watch?v=O4wBUysNe2k | podwise.ai episode page |
| 6 | SOURCE-20251020-...-reid_hoffman_on_ai_consciousness_and_the_future.md | https://www.youtube.com/watch?v=brjL6iyoEhI | startuphub.ai embedded player |
| 7 | SOURCE-20251024-...-arc_agi_v3_and_measuring_intelligence.md | https://www.youtube.com/watch?v=pBlIgs6w7Ss | startuphub.ai embedded player |
| 8 | SOURCE-20251029-...-openai_structure_change_and_ai_timelines.md | https://www.youtube.com/watch?v=w4qcTwdJRFU | startuphub.ai embedded player |
| 9 | SOURCE-20251031-...-no_priors_the_best_of_2025_so_far.md | https://www.youtube.com/watch?v=OdEJjJq1I28 | startuphub.ai embedded player |

### Confidence Notes
- Items 1-3, 5-9: HIGH confidence (video IDs extracted from embedded YouTube players on article/podcast pages)
- Item 4 (All-In Elon Musk): MEDIUM confidence (extracted from Substack cover image metadata; may be a clip rather than full episode)

## URLs Still Missing (22 files)

### Podcast-first shows (audio primary, YouTube secondary)
These shows publish to YouTube but search engines index their podcast feeds first, making YouTube IDs hard to extract without direct YouTube search or API access.

| # | File | Creator | Guest/Topic | Difficulty |
|---|------|---------|-------------|------------|
| 1 | SOURCE-20250605-...-ethan_mollick_ai_jagged_frontier.md | Strange Loop (Sana) | Ethan Mollick | Medium - check Sana YouTube channel |
| 2 | SOURCE-20250902-...-david_deutsch_agi_constructor_theory.md | Strange Loop (Sana) | David Deutsch | Medium - check Sana YouTube channel |
| 3 | SOURCE-20251021-...-don_t_die_bryan_johnson.md | TBPN | Bryan Johnson | Medium |
| 4 | SOURCE-20251027-...-macroscopic_quantum_tunneling.md | All-In Podcast | John Martinis | Medium |
| 5 | SOURCE-20251027-...-coming_productivity_boom.md | David Carbutt | Cathie Wood | Hard - small channel |
| 6 | SOURCE-20251030-...-solana_crypto_ai_convergence.md | Moonshots (Diamandis) | Anatoly Yakovenko | Medium |
| 7 | SOURCE-20251223-...-how_ai_starts_doing_the_work.md | AI Daily Brief | Mike Krieger | Medium |

### Creator YouTube channels (direct upload)
These videos were uploaded directly to creator YouTube channels.

| # | File | Creator | Topic | Difficulty |
|---|------|---------|-------|------------|
| 8 | SOURCE-20251030-...-end_of_ai_complete_integration.md | AI Explained | End of AI | Medium - check AI Explained channel |
| 9 | SOURCE-20251031-...-john_gaeta_transmedia_vfx_ai.md | Bilawal Sidhu | John Gaeta | Medium - check Bilawal channel |
| 10 | SOURCE-20251031-...-the_post_labor_enterprise.md | David Shapiro | Post-Labor Enterprise | Easy - check daveshap channel |
| 11 | SOURCE-20251101-...-renaissance_2_0.md | David Shapiro | Renaissance 2.0 | Easy - check daveshap channel |
| 12 | SOURCE-20251226-...-scaling_paradox.md | David Shapiro | Scaling Paradox | Easy - check daveshap channel |
| 13 | SOURCE-20251223-...-what_are_we_scaling.md | Dwarkesh Patel | Continual Learning | Easy - check Dwarkesh channel |

### MLST episodes (YouTube + podcast dual publish)
| # | File | Guest | Topic | Difficulty |
|---|------|-------|-------|------------|
| 14 | SOURCE-20251222-...-categorical_deep_learning.md | Gavranovic et al. | Category Theory | Easy - check MLST channel |
| 15 | SOURCE-20251224-...-mike_israetel_asi_timelines.md | Dr. Mike Israetel | ASI Timelines | Easy - check MLST channel |

### Conference/organization uploads
| # | File | Creator | Topic | Difficulty |
|---|------|---------|-------|------------|
| 16 | SOURCE-20250528-...-informational_theory_of_life.md | Long Now | Sara Walker | Medium - has placeholder URL |
| 17 | SOURCE-20250623-...-five_new_paradigms.md | BrainMind | Intelligence paradigms | Hard - niche channel |
| 18 | SOURCE-20250807-...-intelligence_of_us.md | TEDx | Blaise Aguera y Arcas | Medium - check TEDx channels |
| 19 | SOURCE-20251014-...-interface_theory_perception.md | Duqun | Donald Hoffman | Hard - small channel |
| 20 | SOURCE-20251020-...-godfather_of_agi.md | Info Tech Research Group | Ben Goertzel | Medium |
| 21 | SOURCE-20251023-...-chain_of_thought_mcp.md | Scale AI | MCP Atlas benchmark | Medium |
| 22 | SOURCE-20251024-...-future_of_engineering.md | EIT | Henrik von Scheel | Hard - niche channel |
| 23 | SOURCE-20251028-...-next_phase_accelerated_computing.md | NVIDIA | Jensen Huang GTC DC | Easy - check NVIDIA channel |

## Recommended Next Steps

1. **Enable YouTube Data API v3** for the Google Cloud project (project 152977485256) at the console URL above. This will allow direct API queries for all 22 remaining videos.

2. **After API is enabled**, re-run this task. Most of the 22 remaining videos should be findable with API search queries like:
   - `David Shapiro post labor enterprise` -> direct channel search
   - `MLST categorical deep learning category theory` -> direct channel search
   - `Strange Loop podcast Ethan Mollick` -> Sana Labs channel
   - `NVIDIA GTC DC keynote Jensen Huang October 2025` -> NVIDIA channel

3. **Manual fallback for hard cases** (5 files): BrainMind, Duqun/Hoffman, David Carbutt, EIT/Henrik von Scheel, and the Long Now placeholder may require browsing the channels directly.

## Files With Valid URLs (18 total)

| # | File | URL |
|---|------|-----|
| 1 | SOURCE-20250312-...-dwarkesh_patel_joseph_henrich.md | https://www.youtube.com/watch?v=TcfhrThp1OU |
| 2 | SOURCE-20250903-...-max_tegmark_physics_ai.md | https://www.youtube.com/watch?v=-gekVfUAS7c |
| 3 | SOURCE-20250912-...-foundation_models.md | https://www.youtube.com/watch?v=48pxVdmkMIE |
| 4 | SOURCE-20251013-...-faith_physics_quantum_race.md | https://www.youtube.com/watch?v=Ir0Sl5awXig |
| 5 | SOURCE-20251020-...-reid_hoffman.md | https://www.youtube.com/watch?v=brjL6iyoEhI |
| 6 | SOURCE-20251021-...-universal_hierarchy_of_life.md | https://www.youtube.com/watch?v=iwClZ-7OweY |
| 7 | SOURCE-20251024-...-arc_agi_v3.md | https://www.youtube.com/watch?v=pBlIgs6w7Ss |
| 8 | SOURCE-20251025-...-life_emerges_from_code.md | https://www.youtube.com/watch?v=rMSEqJ_4EBk |
| 9 | SOURCE-20251029-...-openai_structure_change.md | https://www.youtube.com/watch?v=w4qcTwdJRFU |
| 10 | SOURCE-20251031-...-marc_andreessen_ben_horowitz.md | https://www.youtube.com/watch?v=Y7dwbJ0AtUA |
| 11 | SOURCE-20251031-...-state_of_ai_runtime_keynote.md | https://www.youtube.com/watch?v=Y7dwbJ0AtUA |
| 12 | SOURCE-20251031-...-elon_musk_3_years_of_x.md | https://www.youtube.com/watch?v=j6_VfR-CyuM |
| 13 | SOURCE-20251031-...-jre_2404_elon_musk.md | https://www.youtube.com/watch?v=O4wBUysNe2k |
| 14 | SOURCE-20251031-...-trevor_mccourt.md | https://www.youtube.com/watch?v=OwDWOtFNsKQ |
| 15 | SOURCE-20251031-...-no_priors_best_of_2025.md | https://www.youtube.com/watch?v=OdEJjJq1I28 |
| 16 | SOURCE-20251222-...-how_ai_agents_will_transform.md | https://www.youtube.com/watch?v=ULszsXDyjMY |
| 17 | SOURCE-20260112-...-kennylia_mcps.md | https://www.youtube.com/watch?v=Xs2CkHEpIrM |
| 18 | SOURCE-20260114-...-leonvanzyl_claude_code.md | https://www.youtube.com/watch?v=P60LqQg1RH8 |
