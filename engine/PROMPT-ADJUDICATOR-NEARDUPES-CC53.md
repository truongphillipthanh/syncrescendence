# NEAR-DUPLICATE DETECTION — Adjudicator (Codex)

## Context
You are in `/Users/system/syncrescendence/corpus/`. We just deleted 5,014 exact byte-for-byte duplicates. 6,719 files remain. Now we need to find NEAR-DUPLICATES — files that contain the same content but with different wrappers, formatting, or metadata.

## The Pattern We Already Know
From prior analysis, we found pairs like:
- `08136.md` (bare article) + `08829.md` (same article with tweet metadata: author, date, URL, engagement stats)
- `08351.md` (truncated version) + `08350.md` (full version with references)
- `08347` (missing extension) + `08348.md` (same content, slightly different formatting)

These are NOT byte-identical but one is clearly a version of the other.

## Your Assignment
Systematically find ALL near-duplicate pairs in the corpus. Method:

1. For each file, compute a "content fingerprint" — strip metadata headers (author, date, URL, engagement lines), normalize whitespace, take first 500 characters of actual content
2. Compare fingerprints to find files with >80% content overlap
3. For each near-dupe pair, determine:
   - Which has MORE information (metadata, full text, references) — this is the KEEPER
   - Which is the subset/bare version — this is the MERGE candidate
   - What metadata from the subset version should be merged into the keeper (if any)

## Output Format
Write to `/Users/system/syncrescendence/corpus/NEARDUPES-ADJUDICATOR.tsv`

Format:
```
keeper_file[TAB]merge_file[TAB]action[TAB]reason
```

Where action is one of:
- `delete_merge` — merge_file's unique metadata into keeper_file, then delete merge_file
- `delete_subset` — merge_file is a strict subset of keeper_file, just delete it
- `delete_truncated` — merge_file is a truncated version, just delete it

Also write a summary to `/Users/system/syncrescendence/corpus/NEARDUPES-SUMMARY.md`

## Rules
- Only flag pairs where you're CONFIDENT they're the same content
- When in doubt, leave both — false positives are worse than missed pairs
- Process ALL 6,719 files
