---
url: https://x.com/michaelaubry/status/2023291148580872429
author: "Michael Aubry (@michaelaubry)"
captured_date: 2026-02-15
id: SOURCE-20260216-024
original_filename: "20260216-x_thread-fixed_it_two_tier_memory-@michaelaubry.md"
status: triaged
platform: x
format: thread
creator: michaelaubry
signal_tier: tactical
topics: [ai-agents, developer-tools, best-practices]
teleology: implement
notebooklm_category: ai-agents
aliases: ["michaelaubry - two-tier OpenClaw memory architecture"]
synopsis: "Describes a two-tier memory system for OpenClaw: SOUL.md + MEMORY.md load every message (working memory), while everything else goes into vector search via chunked embeddings. Conversations auto-persist to daily logs via memoryFlush compaction, with S3 sync every 5 minutes for reboot survival."
key_insights:
  - "Two-tier memory: always-on context (SOUL+MEMORY) plus on-demand vector search over chunked daily logs"
  - "Enable memoryFlush compaction so conversations auto-persist - vector search indexes those logs automatically"
  - "S3 sync every 5 min for reboot survival, vector index rebuilds automatically on restore"
---
# Fixed it. Two-tier memory:
1. **SOUL.md + MEMORY.md** load into context every message (always-on working memory)
2. Everything else goes into vector search — OpenClaw chunks your memory files, embeds them, and the agent pulls relevant fragments on demand via `memory_search`
The key most people miss: enable compaction `memoryFlush` so conversations auto-persist to daily logs. Then vector search indexes those logs. Your agent remembers last Tuesday's conversation without you doing anything.
For surviving reboots we sync memory/ to S3 every 5 min. On restart, files restore → vector index rebuilds automatically.
`qmd` is solid if you're self-hosting on beefy hardware — it adds reranking and runs fully local. We're on Fargate so the built-in SQLite + remote embeddings makes more sense. Less overhead, same result at our scale.
---
**Original Context (Quote)**
@levelsio asked: "How did you guys fix persistent memory with OpenClaw? My bot keeps forgetting stuff, I already have qmd installed"