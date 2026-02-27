# ORACLE NUCLEOSYNTHESIS — CC46 PASS 3 OF 4: WIDTH

**Date**: 2026-02-27
**From**: Commander (Claude Opus 4.6)
**To**: Oracle (Grok 4.2)
**Repo**: https://github.com/truongphillipthanh/syncrescendence/tree/main/corpus
**Pass**: 3 of 4 — Width ("What did you miss?")

---

This is your first and only context window. You have no memory of prior sessions.

## YOUR TASK

You are looking at a single flat directory called `corpus/` containing 13,364 files. A previous analyst made two passes over this corpus — one asking "what's here?" and one asking "what connects to what?" Both passes had the same failure mode: they sampled the most visible, most recent, most recognizable files and glossed over the margins.

**Your one question: What's in the 20% that a first pass would skip?**

You must specifically seek out and read:

1. **Non-markdown files**: the `.py`, `.sh`, `.yaml`, `.json`, `.jsonl`, `.csv`, `.plist`, `.toml`, `.cfg` files. What do they do? Are they operational (actively used) or archaeological (remnants of dead systems)?

2. **Files with no standard prefix**: Most files start with prefixes like `SOURCE-`, `META-`, `ARCH-`, `DYN-`, `AGENT-`, `SCRIPT-`, `RESPONSE-`, `PROMPT-`, etc. Find the files that DON'T follow any prefix convention. What are they? Why are they different?

3. **The oldest files**: Files whose content references dates from 2020-2024, before the current project existed. What were they? Where did they come from? Are they still relevant?

4. **The smallest and largest files**: Tiny files (< 100 bytes) — are they placeholders or meaningful? Huge files (> 50KB) — what are they carrying?

5. **Duplicate or near-duplicate content**: Files that appear to be copies of each other with slightly different names (the flattening process may have created these by encoding different paths to the same original file).

Walk the repo via the GitHub link above. **Spend your time on the files that look boring, obscure, or broken.** The obvious files have been seen. Your job is to find what others missed.

**Do NOT propose a directory structure.** Report what you find in the margins. What's dead? What's surprisingly alive? What's duplicated? What's unique and uncategorizable?
