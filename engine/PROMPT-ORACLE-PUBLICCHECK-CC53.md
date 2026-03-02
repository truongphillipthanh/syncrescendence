# PUBLIC CONTENT VERIFICATION — Oracle (Grok)

## Context
The Syncrescendence repo at **https://github.com/truongphillipthanh/syncrescendence** — `main` branch. The `corpus/` directory has ~6,719 files remaining after deleting 5,014 exact duplicates.

The Sovereign's directive: if content is freely available online, we may not need our copy. Your job is to verify which files are just copies of public content.

## Your Assignment
Browse the corpus on GitHub. For files in your previous range (08001-11712), many have been deleted as duplicates. For what remains:

1. Take YouTube transcript files (they have `**Channel**:` headers) — these are publicly available via the original videos. Flag ALL of them as `public`.

2. Take X/Twitter thread files (they reference `x-article` or `x-thread` in their content) — these are publicly available tweets. Flag ALL of them as `public`.

3. Take files that appear to be blog posts or articles — web search the title. If the original exists online, flag as `public`.

4. Files that are clearly internal Syncrescendence artifacts (TASK-, RESULT-, CONFIRM-, HANDOFF-, prompts, configs, session logs) — flag as `internal`.

5. Files that contain unique synthesis, analysis, or knowledge not available elsewhere — flag as `unique`.

## Output
Produce a TSV in your response:
```
filename[TAB]public_or_internal_or_unique[TAB]source_url_if_public
```

Focus on the files you can access. Coverage over perfection. The key question for each file: "If we deleted this, could we get the same information from the internet?"

## Important
- YouTube transcripts without actual transcript content (just title + URL + description) are STUBS — flag as `stub_public` (we know the content is public, the stub is just a placeholder waiting for transcript processing)
- YouTube transcripts WITH full transcript content are `public` (we have the content but it's recoverable from the video)
- Internal synthesis documents that COMBINE multiple public sources into novel analysis are `unique` even if individual sources are public
