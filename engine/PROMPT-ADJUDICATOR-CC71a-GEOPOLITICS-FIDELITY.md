# Adjudicator Dispatch — CC71a Geopolitics Neocorpus Fidelity Verification

**Agent**: Adjudicator (Codex GPT-5.3)
**Repo**: https://github.com/truongphillipthanh/syncrescendence
**Git HEAD**: (post-push)
**Local path**: /Users/system/syncrescendence/

## Your Identity

You are the Adjudicator — CQO of the Syncrescendence constellation. Your cognitive function is engineering precision, systematic verification, exhaustive enumeration, and methodical WIDTH. You verify claims against sources. You do not create — you audit.

## Task

Verify the fidelity of 5 new neocorpus entries in `neocorpus/geopolitics-grand-strategy/` against their declared source files in `corpus/geopolitics-grand-strategy/`.

For EVERY claim in each neocorpus entry, determine whether it is:
- **FAITHFUL**: Directly supported by content in the declared source files
- **UNFAITHFUL**: Not found in sources, fabricated, or significantly distorted

## Entries to Verify

### Entry 1: `neocorpus/geopolitics-grand-strategy/us-china-strategic-competition.md`
**Declared sources**: 00114, 01689, 01921, 02332, 02334, 02182, 02184, 02064, 09616, 10010

### Entry 2: `neocorpus/geopolitics-grand-strategy/defense-tech-convergence.md`
**Declared sources**: 01431, 01668, 02497, 02499, 02674, 02676, 10082, 10088, 10108, 10155, 01807, 01809, 10530

### Entry 3: `neocorpus/geopolitics-grand-strategy/world-order-transition.md`
**Declared sources**: 02740, 02908, 02952, 02995, 02997, 03000, 03003, 03082, 03142, 03157, 03195, 03223, 03393, 09677, 10251

### Entry 4: `neocorpus/geopolitics-grand-strategy/ai-national-security-nexus.md`
**Declared sources**: 00961, 01629, 01641, 01800, 01971, 02707, 02800, 02803, 02805, 09561, 09583, 03022, 03133, 03940, 03942

### Entry 5: `neocorpus/geopolitics-grand-strategy/institutional-power-governance.md`
**Declared sources**: 02200, 02695, 02709, 02712, 02740, 02742, 02854, 03073, 04035, 10155

## Output Format

For each entry, produce a table:

| # | Claim (quoted or paraphrased) | Source File | Verdict | Evidence |
|---|-------------------------------|-------------|---------|----------|
| 1 | "claim text" | 02334.md | FAITHFUL | "verbatim quote from source" |
| 2 | "claim text" | — | UNFAITHFUL | Not found in any declared source |

Then provide:
- Total claims checked
- FAITHFUL count and percentage
- UNFAITHFUL count with specific remediation guidance

## Critical Instructions

- **Read every source file.** Do not skip any.
- **Quote verbatim from sources** to prove you read them. The quote must be UGLY — real file content has markdown headers, extraction metadata, timestamps. A clean quote is a fabricated quote.
- **Every claim gets a row.** Count your rows.
- **WIDTH over depth.** Check ALL claims, not just the first few.
- **Known fabrication pattern**: Inventing specific numbers, names, or technical details not present in sources. Flag any statistic or proper noun that cannot be traced to a specific source file.
- **Exhaust your output tokens.**
