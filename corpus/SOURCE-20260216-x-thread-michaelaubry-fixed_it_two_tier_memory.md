# Fixed it. Two-tier memory:
1. **SOUL.md + MEMORY.md** load into context every message (always-on working memory)
2. Everything else goes into vector search — OpenClaw chunks your memory files, embeds them, and the agent pulls relevant fragments on demand via `memory_search`
The key most people miss: enable compaction `memoryFlush` so conversations auto-persist to daily logs. Then vector search indexes those logs. Your agent remembers last Tuesday's conversation without you doing anything.
For surviving reboots we sync memory/ to S3 every 5 min. On restart, files restore → vector index rebuilds automatically.
`qmd` is solid if you're self-hosting on beefy hardware — it adds reranking and runs fully local. We're on Fargate so the built-in SQLite + remote embeddings makes more sense. Less overhead, same result at our scale.
---
**Original Context (Quote)**
@levelsio asked: "How did you guys fix persistent memory with OpenClaw? My bot keeps forgetting stuff, I already have qmd installed"