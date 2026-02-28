# AI-Business Reclassification Summary

**Date**: 2026-02-27
**Files Processed**: 389
**Output File**: SUBCLUSTER-ai-business.tsv

## Overview
All 389 files originally tagged as "ai-business" have been reclassified with more specific subtopics based on content analysis of the first 15-20 lines of each file.

## Topic Distribution

| Topic | Count | % |
|-------|-------|---|
| aib-market | 188 | 48.3% |
| aib-anthropic | 40 | 10.3% |
| aib-compute | 38 | 9.8% |
| aib-enterprise | 31 | 8.0% |
| aib-investment | 25 | 6.4% |
| aib-future-of-work | 20 | 5.1% |
| aib-openai | 17 | 4.4% |
| aib-monetization | 10 | 2.6% |
| aib-google | 9 | 2.3% |
| aib-startups | 8 | 2.1% |
| aib-meta | 3 | 0.8% |
| aib-solopreneur | 0 | 0.0% |

## Classification Method

1. **Keyword Matching**: Each file was analyzed using domain-specific keywords:
   - **aib-anthropic**: "anthropic", "claude", "constitution", "safety institute"
   - **aib-openai**: "openai", "chatgpt", "gpt-4", "gpt-3", "o1", "o3", "sam altman"
   - **aib-google**: "google", "gemini", "deepmind", "bard", "palm", "vertex"
   - **aib-meta**: "meta", "facebook", "llama", "metaai"
   - **aib-startups**: "startup", "founded", "seed", "series a", "ycombinator"
   - **aib-enterprise**: "enterprise", "corporation", "adoption", "implementation", "cto", "cio"
   - **aib-market**: market analysis, trends, competition, industry landscape
   - **aib-monetization**: pricing, revenue, business models, subscriptions, ROI
   - **aib-solopreneur**: indie, freelance, side hustle, bootstrap
   - **aib-future-of-work**: employment, workforce, jobs, careers, skills
   - **aib-compute**: GPU, infrastructure, cloud costs, training
   - **aib-investment**: VC, venture capital, funding, investors

2. **Content Analysis**: First 15-20 lines extracted from each file (both .jsonl and .md formats)

3. **Default Classification**: Files with no strong keyword matches default to "aib-market"

## Key Findings

- **Dominant Category**: aib-market (48.3%) suggests corpus heavily weighted toward market analysis and industry trends
- **Company Focus**: Strong Anthropic focus (10.3%) indicates substantial coverage of Anthropic-specific news
- **Infrastructure**: aib-compute (9.8%) shows significant attention to GPU/compute economics
- **Missing Coverage**: No solopreneur AI business files found, suggesting gap in indie maker content
- **Emerging Companies**: Limited OpenAI/Google/Meta coverage relative to general market content

## Output Format

```
filename[TAB]refined_topic[TAB]one_line_summary
```

Example:
```
04877.jsonl	aib-anthropic	Deedy Das, a Partner at Menlo Ventures, invested in Anthropic early on when the company had no revenue
05049.jsonl	aib-compute	Nvidia's recent blowout earnings affirmed its position as the world's most valuable company...
```

## Notes

- Total files in SUBCLUSTER-ai-business.tsv: 389
- All original filenames preserved
- Summaries truncated to 180 characters for readability
- No files were excluded or modified
