# CLUSTERING TASK — Oracle (Grok)

## Context
The Syncrescendence repo is at **https://github.com/truongphillipthanh/syncrescendence** — `main` branch, just pushed.

The `corpus/` directory has ~11,712 numbered files. We're classifying every file by semantic topic — what it's ABOUT.

Cartographer has files 00001-04000. Adjudicator has 04001-08000. **You have 08001 through 11712** plus all subdirectories (`corpus/sn_compressed/`, `corpus/sn_skeletons/`, `corpus/demoted/`, `corpus/views/`).

## How to Traverse
Browse the repo on GitHub. The files are in `corpus/`. Navigate to files in your range (08001-11712), read the first 10-20 lines of each, and classify by subject matter.

For JSONL files, read the `content` field values to determine topic.
For `.md` files, the title and first few lines tell you the topic.

## Your Assignment
For each file in your range:
1. Read the first 10-20 lines
2. Determine what SUBJECT MATTER it covers
3. Assign a granular topic tag

## Topic Tags (use these, add new ones if needed)
### AI Platforms
- `claude-code`, `openclaw`, `codex`, `gemini`, `chatgpt`, `cursor`, `other-ai-tool`

### AI Concepts
- `ai-agents`, `ai-coding`, `prompt-engineering`, `ai-memory`, `ai-safety`, `ai-models`, `ai-business`, `mcp`, `ai-video`, `ai-image`, `ai-general`

### Knowledge Domains
- `geopolitics-us-china`, `geopolitics-iran`, `geopolitics-russia`, `geopolitics-grand-strategy`, `geopolitics-other`
- `economics-macro`, `economics-investing`, `economics-startups`
- `physics-cosmology`, `biology-evolution`, `biology-neuroscience`
- `philosophy-consciousness`, `philosophy-epistemology`
- `history`, `self-improvement`, `content-creation`, `design`, `infrastructure`, `software-engineering`

### Syncrescendence Internal
- `sn-handoff`, `sn-task`, `sn-confirm`, `sn-result`, `sn-prompt`, `sn-certescence`
- `sn-config`, `sn-script`, `sn-watchdog`, `sn-canon`, `sn-rosetta`
- `sn-system-prompt`, `sn-architecture`, `sn-pipeline`, `sn-atom`, `sn-other`

## Additional Task — Strange Attractor Detection
Because you're web-connected: for any file that appears to be a copy of publicly available content (a YouTube transcript, a blog post, a tweet thread), note it in a 5th column as `public`. This helps the CRUSH phase — if the content is freely available online, we may not need our copy.

## Output Format
TSV file, one line per file:
```
filename[TAB]topic[TAB]secondary_topic[TAB]one_line_summary[TAB]public_or_unique
```

## Delivery
Output the full TSV directly in your response. The Sovereign will relay it to Commander who will save it to the repo.

## Rules
- Every file gets exactly ONE primary topic
- Tag by what the content is ABOUT, not what file type it is
- Atom extractions → tag by source topic, not as "extraction"
- JSONL → read `content` field for topic
- Speed over perfection — coverage on ~3,700 files + subdirs
