# YouTube URL Recovery via API

**Date**: 2026-02-21
**Method**: YouTube Data API v3 search endpoint
**Files processed**: 23

## Results

| # | File | URL Recovered | Confidence | Notes |
|---|------|---------------|------------|-------|
| 1 | SOURCE-20250605-...-ethan_mollick_ai_jagged_frontier.md | https://www.youtube.com/watch?v=KEQjwE7hDjk | HIGH | Sana channel, Jun 5 2025, exact topic match |
| 2 | SOURCE-20250902-...-david_deutsch_agi_constructor_theory.md | https://www.youtube.com/watch?v=IVA2bK9qjzE | HIGH | Sana channel, Sep 3 2025, "David Deutsch: AGI, the origins of quantum computing" |
| 3 | SOURCE-20251021-...-don_t_die_bryan_johnson...md | https://www.youtube.com/watch?v=lsDBwvPOzdM | HIGH | TBPN channel, exact title "Don't Die CEO Bryan Johnson on Living Forever, AI & His $60M Blueprint" |
| 4 | SOURCE-20251027-...-macroscopic_quantum_tunneling...md | https://www.youtube.com/watch?v=GWOPRdN8INU | HIGH | All-In Podcast, Oct 27, "Nobel Prize in Physics Winner: The Quantum Leap" John Martinis |
| 5 | SOURCE-20251027-...-coming_productivity_boom...md | https://www.youtube.com/watch?v=1aXMXss4cA4 | MEDIUM | David Carbutt channel, Oct 28, "America Is About To GO OFF | Cathie Wood" - closest date match, title differs from file |
| 6 | SOURCE-20251030-...-solana_crypto_ai_convergence...md | https://www.youtube.com/watch?v=bOkTm1JEBow | HIGH | Peter Diamandis channel, Oct 30, Anatoly Yakovenko Solana |
| 7 | SOURCE-20251223-...-how_ai_starts_doing_the_work...md | https://www.youtube.com/watch?v=VSLEGpCemtE | HIGH | AI Daily Brief, Dec 24, exact title "How AI Starts Doing the Work in 2026 with Anthropic CPO Mike Krieger" |
| 8 | SOURCE-20251030-...-end_of_ai_complete_integration...md | NOT FOUND | - | AI Explained channel searched; no matching video found. URL field set to empty string. |
| 9 | SOURCE-20251031-...-john_gaeta_transmedia_vfx_ai.md | https://www.youtube.com/watch?v=WoQPYIgTbik | HIGH | Bilawal Sidhu channel, Oct 31, "Matrix VFX Legend" John Gaeta |
| 10 | SOURCE-20251031-...-the_post_labor_enterprise.md | https://www.youtube.com/watch?v=-OJVfJEMYBs | HIGH | David Shapiro channel, Oct 31, exact title "The Post-Labor Enterprise" |
| 11 | SOURCE-20251101-...-renaissance_2_0...md | https://www.youtube.com/watch?v=AwDFO2b3_l0 | HIGH | David Shapiro channel, Nov 1, exact title "Renaissance 2.0" |
| 12 | SOURCE-20251226-...-scaling_paradox...md | https://www.youtube.com/watch?v=jKM_5A8-oKg | LOW | David Shapiro channel, Dec 26 date match, but title is "The next step towards AGI" not "Scaling Paradox". May be wrong video. |
| 13 | SOURCE-20251223-...-what_are_we_scaling...md | https://www.youtube.com/watch?v=_zgnSbu5GqE | HIGH | Dwarkesh Patel channel, Dec 23, exact title "What are we scaling?" |
| 14 | SOURCE-20251222-...-categorical_deep_learning...md | https://www.youtube.com/watch?v=AWqvBdqCAAE | HIGH | MLST channel, Dec 22, "The Final Boss of Deep Learning" (categorical deep learning topic) |
| 15 | SOURCE-20251224-...-mike_israetel_asi_timelines...md | https://www.youtube.com/watch?v=4yYcN_mFi18 | HIGH | MLST channel, Dec 24, "PhD Bodybuilder Predicts The Future of AI" Dr Mike Israetel |
| 16 | SOURCE-20250528-...-informational_theory_of_life.md | https://www.youtube.com/watch?v=zhzxQraB2m0 | HIGH | Long Now Foundation, May 28, exact title "Sara Imari Walker | An Informational Theory of Life" (replaced placeholder) |
| 17 | SOURCE-20250623-...-five_new_paradigms_of_intelligence.md | https://www.youtube.com/watch?v=l508X6nGjX4 | HIGH | BrainMind Summit, Jun 23, exact title "Blaise Aguera y Arcas - Five New Paradigms of Intelligence" |
| 18 | SOURCE-20250807-...-intelligence_of_us...md | https://www.youtube.com/watch?v=OD5UzhaDWfg | HIGH | TEDx Talks, Aug 7, exact title "The Intelligence of Us: Rethinking Minds in the Age of AI | Blaise Aguera y Arcas" |
| 19 | SOURCE-20251014-...-interface_theory_of_perception...md | https://www.youtube.com/watch?v=xaeafKPfs1M | HIGH | Andre Duqum channel, Oct 14, Donald Hoffman perception/consciousness |
| 20 | SOURCE-20251020-...-godfather_of_agi...md | https://www.youtube.com/watch?v=sozyCpZX4O4 | HIGH | Info-Tech Research Group, Oct 20, exact title "Godfather of AGI on Why Big Tech Innovation is Over" |
| 21 | SOURCE-20251023-...-chain_of_thought_mcp_atlas...md | https://www.youtube.com/watch?v=c34W8hmTxHo | HIGH | Scale AI channel, Oct 23, "Chain of Thought | Leaderboard Deep Dive - Scale's MCP Atlas Benchmark" |
| 22 | SOURCE-20251024-...-future_of_engineering...md | https://www.youtube.com/watch?v=LOk48ld2lBc | HIGH | EIT channel, Oct 24, exact title match |
| 23 | SOURCE-20251028-...-next_phase_accelerated_computing...md | https://www.youtube.com/watch?v=lQHK61IDFH4 | HIGH | NVIDIA channel, Oct 28, full GTC DC keynote with Jensen Huang |

## Summary

- **Total files**: 23
- **HIGH confidence**: 19
- **MEDIUM confidence**: 1 (Cathie Wood / David Carbutt - title mismatch but channel/date match)
- **LOW confidence**: 1 (David Shapiro Scaling Paradox - date match only, title mismatch)
- **NOT FOUND**: 1 (AI Explained "The End of AI" - video not surfaced by API search)
- **Placeholder replaced**: 1 (Sara Walker Long Now - had dummy `longnow_walker` ID)

## Action Items

- [ ] Manually verify #5 (Cathie Wood) - may need to browse David Carbutt's channel directly
- [ ] Manually verify #12 (David Shapiro Scaling Paradox) - "The next step towards AGI" may not be the correct video
- [ ] Manually find #8 (AI Explained "The End of AI") - not found via API search
