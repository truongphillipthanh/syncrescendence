---
url: https://x.com/maithra_raghu/status/2024154498961420509
author: "Maithra Raghu (@maithra_raghu)"
captured_date: 2026-02-18
id: SOURCE-20260218-012
original_filename: "20260218-x_article-the_post_scaling_era_for_frontier_ai-@maithra_raghu.md"
status: triaged
platform: x
format: article
creator: maithra_raghu
signal_tier: paradigm
topics:
  - gpt
  - open-source
  - cost-optimization
teleology: synthesize
notebooklm_category: ai-engineering
aliases:
  - "The PostScaling Era for Frontier AI"
synopsis: "The Post-Scaling Era for Frontier AI Opening The most surprising point from @DarioAmodei's interview on the @dwarkesh_sp podcast was the candid discussion on **what happens when frontier model training costs stop exponentially increasing — and where that leaves the AI labs.** (First time I've heard."
key_insights:
  - "The individual models make returns, but the lab is at a deficit as it invests in the next model."
  - "But exponential increase in training costs can't continue forever — eventually scaling both hits real world capacity constraints and diminishing returns on improving capabilities."
  - "This has been my top question for the past few years."
---
# The Post-Scaling Era for Frontier AI
## Opening
The most surprising point from @DarioAmodei's interview on the @dwarkesh_sp podcast was the candid discussion on **what happens when frontier model training costs stop exponentially increasing — and where that leaves the AI labs.** (First time I've heard an AI lab CEO discuss this so explicitly.)
## The Current Economic Dynamic
The relentless push to scale comes from today's dynamic, where **each frontier model has roughly (only!) a two month lifespan at the frontier.** If that model costs $1B for research and training, $1B for inference, and makes $4B+ in revenues, that's a $2B+ net, **while it's at the frontier.** Revenues can drop off quickly as the models fall behind, so in the meantime the lab is training the next model, at the next level of scale, for maybe a $10B cost. The individual models make returns, but the lab is at a deficit as it invests in the next model.
But exponential increase in training costs can't continue forever — eventually scaling both hits real world capacity constraints and diminishing returns on improving capabilities. This has been my top question for the past few years. Dario outlines an eventual **"equilibrium" state where training costs diminish, improvements are more efficient and driven by algorithmic advances.**
## Market Concentration: Moats in the Post-Scaling Era
### Do frontier labs maintain their moat in this post scaling world?
In early 2023, shortly after the release of ChatGPT and during the open source LLM boom, I speculated about the future of large AI models in a post "Does one large model rule them all?" with @matei_zaharia and @ericschmidt. We saw two possible end states for large AI models: (i) commoditization or (ii) a few large dominant players.
(Description: A text box with light gray background containing a discussion of "The Future of General AI Models?" explaining how commoditization vs. dominant player scenarios depend on cost utility tradeoffs. Three highlighted scenarios are presented, with yellow highlighting emphasizing that if costs increase but utility shows proportional gains, there will be a small number of very high cost, general purpose models.)
We're now unambiguously in the second state, where there are a few dominant players in frontier AI, due to the order of magnitude cost increase in model training and commensurate improvement in capabilities. Our prediction then was that **AI labs would look like cloud providers from the business perspective,** which was echoed in the podcast.
Dario sees the post scaling era for AI labs maintaining a large barrier to entry due to massive upfront capital requirements. He pointed out that **cloud has 3-4 players which are largely undifferentiated, but we may see the top AI models be much more differentiated than cloud providers.** Seeing variations in Claude, ChatGPT, and Gemini strengths and personalities, which have **largely emerged over the past 6-8 months of advances,** this was an interesting takeaway for the future AI landscape! (Relatedly, the podcast also discusses the delicate process of forecasting exactly the right amount of compute to support exponential scaling and demand -- too little and you can't do enough scaling + inference, too much and there's the risk of bankruptcy.)
## Open Questions on Model Distillation
I have a remaining open question:
### What happens with model distillation in the post-scaling era?
Model distillation, which is the process of generating outputs from a frontier model to cost-effectively copy it, remains a heated topic. Right now there's a substantial gap between frontier models and distillation attempts (as well as open-source models), because the frontier moves so quickly (every two months). In the post-scaling era, will the frontier continue to move quickly but just more cost-effectively? Or will other capital intensive moats prevent distilled copy-cats?
## Training Methods: Present and Future
The podcast also highlighted a couple of interesting takeaways on the state of training methods today:
1. **AI doesn't need to learn like a human**
2. **RL is set to scale**
### On Learning Methods
On 1, we're seeing a resurgence of interest in "continual learning" and "recursive self-improvement" -- ways to make AI "learn on the fly", just like humans do. (In late 2023 when these topics were of peak interest, I'd written a post "On AGI and self-improvement" on my doubts of achieving AGI if recursive self-improvement was a necessary ingredient.)
Dario makes the argument that these learning methods might not matter, and what we have right now: **(i) pretraining (ii) in-context learning with long contexts (iii) RL** might be enough. Although this makes AI much less sample efficient and less adaptable than human learning, the current progress certainly points to super-human successes without limiting AI to human-like learning methods.
(Description: A diagram with light gray background showing imperfect analogies between AI training methods and human learning approaches. Three rows present: "Pretraining → Human Evolution (+ some human learning)", "In-Context Learning → Long-term & short-term human learning", and "RL (on pretrained base) → Human Learning". Caption reads "Imperfect analogies of the different AI training methods with human learning methods".)
### On Reinforcement Learning
On 2, and the training methods that do matter, RL is poised to scale substantially in the months ahead. Dario roughly sees **RL today like where pretraining was as we moved from GPT-1 (narrow pretraining, poor generalization) to GPT-2 (broader pretraining on the internet corpus, first signs of generalization.)** The scaling laws for RL are still to be discovered, but there's clear log-linear improvements across a variety of tasks — lots more to come here!
## Conclusion and Future Direction
In summary, the podcast highlighted an approaching transition from the current era of exponentially increasing training costs to a more stable equilibrium, where frontier labs start to resemble cloud providers — capital-intensive, differentiated, and structurally profitable. The training methods that get us there may not look like human learning at all, and RL scaling is the next big chapter. I have some thoughts on what this means for vertical AI and for @samaya_AI that I hope to share in a follow-up.
Curious to hear what else stood out to others from the full conversation!