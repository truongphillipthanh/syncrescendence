# BOTTOM-UP CLUSTERING — Cartographer (Gemini Pro 3.1)

## Context
You are in `/Users/system/syncrescendence/corpus/`. After deleting 5,014 exact duplicates, 6,719 files remain. We need GRANULAR semantic clustering — bottom-up, not top-down.

## What Bottom-Up Means
Do NOT start with predefined categories. READ the files. Notice what groups NATURALLY form. Name the clusters AFTER you see the patterns. If 30 files all discuss "how to set up CLAUDE.md rules files" — that's a natural cluster. If 15 files all cover "the February 2026 Anthropic pricing change" — that's another. The clusters emerge from the content.

## Your Assignment
Take all .md files in the corpus (~4,249 files). Read the first 20 lines of each. As you read, track what topics keep appearing. Group files by their actual subject matter at the most specific level possible.

## What We Need From You
1. A list of every natural cluster you find, with:
   - A descriptive name based on what the files actually say
   - The exact filenames in that cluster
   - How many files are in it
   - Whether the files within the cluster are saying the SAME thing (crush candidates) or different things about the same topic

2. Specifically flag:
   - Files that are near-duplicates (same content, different formatting/wrapper)
   - Files where one has metadata (author, date, URL, engagement stats) and another is the bare content — these need MERGING
   - Files that are publicly available content (YouTube transcripts, blog posts, tweets) vs. unique internal knowledge

## Output
Write to `/Users/system/syncrescendence/corpus/BOTTOMUP-CARTOGRAPHER-FULL.md`

## Rules
- NO predefined topic lists. Let clusters emerge.
- Be as SPECIFIC as possible. Not "AI tools" — "OpenClaw setup guides that all explain the same SOUL.md configuration"
- List actual filenames, not counts alone
- The goal is finding crushable redundancy and mergeable near-dupes
