# YouTube URL Recovery Log

**Date**: 2026-02-21
**Agent**: Commander (Claude Opus 4.6)
**Method**: WebSearch + WebFetch to recover YouTube URLs from podcast pages, transcript sites, and embedded links

## Summary

- **Total YouTube SOURCE files**: 41
- **URLs recovered this session**: 9
- **URLs still missing**: 32
- **Pre-existing placeholder replaced**: 0 (Long Now placeholder `longnow_walker` left for manual verification)

## URLs Successfully Recovered

| File | YouTube URL |
|------|-------------|
| SOURCE-20250312-...-dwarkesh_patel_joseph_henrich_cultural_evolutio.md | https://www.youtube.com/watch?v=TcfhrThp1OU |
| SOURCE-20250903-...-max_tegmark_physics_ai_consciousness.md | https://www.youtube.com/watch?v=-gekVfUAS7c |
| SOURCE-20250912-...-foundation_models_for_physical_intelligence.md | https://www.youtube.com/watch?v=48pxVdmkMIE |
| SOURCE-20251013-...-faith_physics_and_the_quantum_race_matthew_kins.md | https://www.youtube.com/watch?v=Ir0Sl5awXig |
| SOURCE-20251025-...-life_emerges_from_code.md | https://www.youtube.com/watch?v=rMSEqJ_4EBk |
| SOURCE-20251031-...-trevor_mccourt_probabilistic_circuits.md | https://www.youtube.com/watch?v=OwDWOtFNsKQ |
| SOURCE-20251222-...-how_ai_agents_will_transform_in_2026.md | https://www.youtube.com/watch?v=ULszsXDyjMY |
| SOURCE-20260112-...-kennylia_why_i_stopped_using_mcps_in_claude_code.md | https://www.youtube.com/watch?v=Xs2CkHEpIrM |
| SOURCE-20260114-...-leonvanzyl-...stop_using_claude_code.md | https://www.youtube.com/watch?v=P60LqQg1RH8 |

### Recovery Sources
- Dwarkesh Patel episodes: fetched from dwarkesh.com episode pages (embedded YouTube links)
- MLST / Blaise Aguera y Arcas: fetched from startuphub.ai article (embedded YouTube player)
- Quantum Economy Podcast: fetched from thequantumeconomy.com (YouTube playlist links)
- Max Tegmark / Theories of Everything: fetched from blog.biocomm.ai (embedded YouTube link)
- Extropic / Trevor McCourt: fetched from digitalhabitats.global (embedded YouTube link)
- a16z AI Agents 2026: fetched from recapio.com (embedded YouTube player)
- kennylia + leonvanzyl: extracted from timestamp links already in file body

## URLs NOT Recovered (Manual Lookup Required)

These 32 files need manual YouTube URL lookup. Web searches returned podcast aggregator pages (Spotify, Apple Podcasts) but not direct YouTube URLs.

1. SOURCE-20250528-...-an_informational_theory_of_life.md (has placeholder `longnow_walker` -- needs real URL from Long Now YouTube)
2. SOURCE-20250605-...-ethan_mollick_ai_jagged_frontier.md (Strange Loop podcast)
3. SOURCE-20250623-...-five_new_paradigms_of_intelligence.md (BrainMind channel)
4. SOURCE-20250807-...-the_intelligence_of_us_rethinking_minds_in_the_ag.md (TEDx, Blaise Aguera y Arcas)
5. SOURCE-20250902-...-david_deutsch_agi_constructor_theory.md (Strange Loop podcast)
6. SOURCE-20251014-...-interface_theory_of_perception_and_consciousness.md (Duqun, Donald Hoffman)
7. SOURCE-20251020-...-reid_hoffman_on_ai_consciousness_and_the_future.md (a16z)
8. SOURCE-20251020-...-godfather_of_agi_on_why_big_tech_innovation_is_ove.md (Info Tech Research Group, Ben Goertzel)
9. SOURCE-20251021-...-the_universal_hierarchy_of_life.md (MLST, Chris Kempes)
10. SOURCE-20251021-...-don_t_die_bryan_johnson_on_living_forever_ai_an.md (TBPN)
11. SOURCE-20251023-...-chain_of_thought_mcp_atlas_benchmark_deep_dive.md (Scale AI)
12. SOURCE-20251024-...-arc_agi_v3_and_measuring_intelligence.md (ARC Prize, Chollet/Knoop)
13. SOURCE-20251024-...-the_future_of_engineering_a_discipline_evolving_t.md (EIT, Henrik von Scheel)
14. SOURCE-20251027-...-macroscopic_quantum_tunneling_to_quantum_computing.md (All-In, John Martinis)
15. SOURCE-20251027-...-the_coming_productivity_boom_tax_policy_and_econo.md (David Carbutt, Cathie Wood)
16. SOURCE-20251028-...-the_next_phase_of_accelerated_computing_and_ai.md (NVIDIA GTC, Jensen Huang)
17. SOURCE-20251029-...-openai_structure_change_and_ai_timelines.md (OpenAI, Sam Altman)
18. SOURCE-20251030-...-solana_crypto_ai_convergence_and_machine_to_mach.md (Moonshots, Anatoly Yakovenko)
19. SOURCE-20251030-...-the_end_of_ai_complete_integration_into_society.md (AI Explained)
20. SOURCE-20251031-...-marc_andreessen_and_ben_horowitz_on_the_state_of_a.md (a16z)
21. SOURCE-20251031-...-state_of_ai_runtime_keynote.md (a16z)
22. SOURCE-20251031-...-elon_musk_on_3_years_of_x_openai_lawsuit_and_the.md (All-In)
23. SOURCE-20251031-...-john_gaeta_transmedia_vfx_ai.md (Bilawal Sidhu)
24. SOURCE-20251031-...-jre_2404_elon_musk_civilization_technology_a.md (Joe Rogan)
25. SOURCE-20251031-...-the_post_labor_enterprise.md (David Shapiro)
26. SOURCE-20251031-...-no_priors_the_best_of_2025_so_far.md (No Priors)
27. SOURCE-20251101-...-renaissance_2_0_open_ai_models_signal_democratic.md (David Shapiro)
28. SOURCE-20251222-...-mlst_categorical_deep_learning_from_alchemy_to.md (MLST, Bruno Gavranovic et al.)
29. SOURCE-20251223-...-how_ai_starts_doing_the_work_in_2026.md (AI Daily Brief, Mike Krieger)
30. SOURCE-20251223-...-dwarkesh_patel_what_are_we_scaling_the_continu.md (Dwarkesh Patel solo)
31. SOURCE-20251224-...-mlst_dr_mike_israetel_asi_timelines_embodimen.md (MLST, Dr. Mike Israetel)
32. SOURCE-20251226-...-david_shapiro_the_scaling_paradox_why_capabilit.md (David Shapiro)

### Recommended Manual Recovery Strategy
- **High-value targets**: Search each creator's YouTube channel directly for the specific episode title
- **Podcast-first shows** (All-In, No Priors, TBPN, Moonshots, AI Daily Brief): These often publish to YouTube under a slightly different title than the podcast feed; search the channel directly
- **a16z**: Check youtube.com/@a16z for Runtime conference recordings
- **David Shapiro**: Check youtube.com/@DavidShapiro or @daveshap channel
- **MLST**: Check youtube.com/@MachineLearningStreetTalk
- **Strange Loop**: Check youtube.com/@strangelooppodcast or Sana Labs channel
