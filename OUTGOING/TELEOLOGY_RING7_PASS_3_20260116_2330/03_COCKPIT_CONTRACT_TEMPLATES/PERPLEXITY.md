# COCKPIT CONTRACT: Perplexity
## Operational Template for Perplexity Surfaces

**Platform**: Perplexity
**Surfaces**: Web app, iOS/Android app, API
**Version**: 1.0

---

## TELEOLOGY (Why This Platform Exists)

Perplexity serves as **CITATION-CRITICAL RESEARCH** in the Syncrescendence architecture:
- Accuracy-first search (93.9% SimpleQA)
- Multi-source synthesis with 100+ citations
- Deep Research mode (2-4 min comprehensive reports)
- Real-time web grounding

**Not for**: Execution (use Claude Code), planning (use ChatGPT), corpus-scale sensing (use Gemini), long-term memory (stateless).

---

## ALLOWED ACTIONS

| Action | Context | Output |
|--------|---------|--------|
| Fact-checking | Verify claims | Answer with sources |
| Research synthesis | Topic exploration | Report with 100+ citations |
| Current events | Real-time info | Sourced summary |
| Competitor analysis | Platform comparison | Documented findings |
| API documentation | Finding current APIs | Linked documentation |

---

## FORBIDDEN ACTIONS

| Action | Why Forbidden | Alternative |
|--------|---------------|-------------|
| Hold state across sessions | Perplexity is stateless | Export to repo immediately |
| Execute anything | Perplexity only researches | Route to Claude Code |
| Trust without citing | Even Perplexity can err | Require source links |
| Use for known-corpus queries | Wastes external search | Use Gemini for internal |
| Deep dives without time | Deep Research takes 2-4 min | Plan for wait time |

---

## MEMORY POLICY

### Perplexity Has No Memory
- Each query is independent
- No cross-session continuity
- No user profile persistence

### What This Means
- Must re-state context each query
- Export findings immediately after receiving
- Cannot build on prior queries without re-pasting

### Workaround
For multi-step research:
1. Collect all findings from Perplexity
2. Paste into ChatGPT or Claude for synthesis
3. Perplexity = research retrieval only

---

## PACKET POLICY

### Incoming (To Perplexity)
| Packet Type | When | Content |
|-------------|------|---------|
| Research Query | Need external facts | Specific question |
| Fact Check Request | Verify claim | Claim + context |

### Outgoing (From Perplexity)
| Packet Type | When | Destination |
|-------------|------|-------------|
| Research Findings | After search | Repo SOURCES/ or direct to synthesis |
| Citation Set | After Deep Research | Repo for reference |

---

## INITIALIZATION BLOCK

Perplexity doesn't need initialization - it's stateless. But for complex research:

```
I need accurate, well-cited research on:
[TOPIC]

Requirements:
- Provide source links for all claims
- Focus on [TIMEFRAME] if relevant (e.g., "2025-2026")
- Prioritize [SOURCE TYPES] (e.g., "official documentation, peer-reviewed")
- Flag any conflicting information between sources

Output as structured findings I can export.
```

---

## WHEN CONFUSED: ESCALATION RULE

Not applicable - Perplexity is stateless and query-based. If a query fails:

1. Rephrase the question more specifically
2. Break into smaller sub-queries
3. Check if topic is too recent (may not be indexed)
4. Fall back to manual search if needed

---

## SESSION END CHECKLIST

- [ ] All findings exported (Perplexity is stateless!)
- [ ] Citations preserved with URLs
- [ ] Findings pasted into repo or synthesis surface
- [ ] Nothing left only in Perplexity (it will be lost)

---

## ACCOUNT CONFIGURATION

### Tier Recommendations
| Tier | Cost | Best For |
|------|------|----------|
| Free | $0 | 5 queries/day, testing |
| Pro | $20/mo | 300+ queries/day, Deep Research |
| Enterprise | $325/seat | Institutional research, API access |

### API Usage
```bash
# Perplexity API for programmatic access
curl -X POST https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "sonar", "messages": [{"role": "user", "content": "..."}]}'
```

---

## LEGAL CONSIDERATIONS

Perplexity faces active copyright litigation:
- NYT lawsuit
- WSJ lawsuit
- Other publisher claims

**Governance rule**: Do not rely exclusively on Perplexity for critical business decisions. Cross-verify with primary sources.

---

**Perplexity researches with citations. It does not remember. Export immediately.**
