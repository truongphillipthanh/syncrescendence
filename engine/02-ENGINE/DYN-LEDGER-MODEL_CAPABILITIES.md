# DYN-LEDGER-MODEL_CAPABILITIES.md
## Model Capability & Benchmarks

**Version**: 1.0.0
**Last Updated**: 2026-02-22
**Cadence**: weekly
**Primary Sources**: Oracle (Grok), Cartographer, Commander

### Entry Format
```
### [DOMAIN-NNN] Title
**Observed**: YYYY-MM-DD | **Source**: [origin]
**Confidence**: HIGH/MEDIUM/LOW/SPECULATIVE
**Freshness**: FRESH/CURRENT/AGING/STALE
**Tags**: #tags

[Observation content]

**Implications for Syncrescendence**: [what this means for us]
**Cross-refs**: [links to related docs]
```

---

## Entries

### [DOMAIN-001] Frontier Model Capability Landscape — Feb 2026
**Observed**: 2026-02-22 | **Source**: SWE-bench.com, onyx.app/llm-leaderboard, lmcouncil.ai, siliconflow benchmarks
**Confidence**: HIGH
**Freshness**: FRESH
**Tags**: #frontier #agentic #SWE-bench

Claude Opus 4.6 leads agentic coding with 75.6–80.9% on SWE-bench Verified; GPT-5.2/5.3 edges GPQA Diamond (~92%) and ARC-AGI reasoning; Gemini 3 Pro/2.5 Pro dominates multimodal/long-context hybrids (1M window native) and human preference arenas; Chinese models (Kimi K2.5, DeepSeek V3.2, Qwen3-Max) sit 3–8% behind on raw intelligence but win on tool-use and speed at 1/5–1/10 the cost. Open models (Llama 4 variants) competitive only in BFCL tool-use.

**Implications for Syncrescendence**: Our current mapping (Claude execution, Gemini cartography) is near-optimal; Chinese models represent unexploited cost-leverage for bulk sensing passes.
**Cross-refs**: REF-STACK_TELEOLOGY.md, AGENTS.md (agent-platform mappings).
