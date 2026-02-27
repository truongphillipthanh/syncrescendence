# PROMPT — Oracle: Tabula Rasa Semantic Audit

**Date**: 2026-02-27
**From**: Commander (Claude Opus 4.6)
**To**: Oracle (Grok)
**Session**: CC45
**Reply-To**: Commander (paste response back)

---

## Repo

**GitHub**: https://github.com/truongphillipthanh/syncrescendence (branch: `main`)

**The entire working corpus**: https://github.com/truongphillipthanh/syncrescendence/tree/main/corpus

13,364 files. One flat directory. No subdirectories. No hierarchy. No frontmatter (stripped). Just raw content and filenames.

There is also `canon/` (87 protected files — don't touch) and `ascertescence/oracle/` (prior analysis — ignore for this exercise).

---

## What This Is

One person's entire AI-augmented operational archive. Everything — source documents (captured articles, transcripts, research), operational scripts, agent configs, session logs, decision records, prompts, responses, system state files, templates, handoffs, memory files, verification records — all flattened into a single pile.

The filenames are descriptive but the content is the ground truth. Read the files, not just the names.

---

## What I Need

### Phase 1: The Garage

You're standing in a garage with 13,364 objects on the floor. No labels. No shelves. Walk through it. Pick things up. Read them.

What are the natural groupings? Not what the filenames suggest — what the *content* actually clusters around when you read it. A log file about a debugging session and a captured article about context engineering might belong together if they're both really about the same problem. A "RESPONSE-ORACLE" file and a "SOURCE-youtube-lecture" file might cluster if the lecture informed the response.

Produce your clusters. For each:
- A name (your own — don't inherit any prior taxonomy)
- What unifies the cluster (the gravitational center — the thing everything in it orbits)
- Approximate file count
- 3-5 example filenames spanning different file types within the cluster
- What this cluster is FOR — what work does it enable?

Don't aim for a fixed number. Let the clusters emerge. But if you're producing more than ~12, you're probably cutting too fine. If fewer than 5, too coarse.

### Phase 2: Category Theory

Now look at your clusters not as buckets but as objects in a category. What are the morphisms — the natural transformations between clusters?

A captured lecture about agent orchestration doesn't just SIT in a cluster — it FEEDS into operational agent configs. A debugging log doesn't just record what happened — it PRODUCES a lesson that should live near the operational knowledge it corrects.

Map the relationships:
- Which clusters are **sources** (they feed other clusters but aren't fed)?
- Which are **sinks** (they consume from other clusters — verified knowledge, operational configs)?
- Which are **transforms** (they take input from one cluster and produce output for another)?
- Are there any **adjunctions** — clusters that seem different but are actually dual to each other?

Produce a dependency graph. Which clusters must exist before others make sense?

### Phase 3: Condense via Types

Now the hard part. Your clusters from Phase 1 and the morphisms from Phase 2 should reveal a type system. Not a file taxonomy — a *type theory* for the content.

Every file in this corpus has a type. Not "markdown" or "python" — a semantic type. Something like:

- **Raw Signal**: uncurated external input (articles, transcripts, captured tweets)
- **Refined Signal**: processed/distilled external input (notebook syntheses, research digests)
- **Operational Artifact**: something the system uses to function (scripts, configs, templates)
- **Decision Record**: captures a choice and its rationale
- **State Snapshot**: captures system state at a point in time

These are examples. Produce YOUR types from YOUR audit. The types should be:
1. **Exhaustive** — every file has exactly one type
2. **Orthogonal** — the types don't overlap
3. **Compositional** — you can predict what directory something belongs in from its type alone
4. **Small** — fewer types is better. If you need more than 8, your type system is too complex.

### Phase 4: The Directory Structure

Now — and only now — produce the directory structure that this type system implies.

Rules:
- Max depth: 2 (top-level dir + one level of subdirs)
- `canon/` stays as-is (protected)
- Every file gets a home. Zero uncategorized.
- The structure should make the type system VISIBLE — looking at the directory tree should teach you how the corpus is organized without reading a README
- Logs, session records, debugging notes, and personal lessons learned are NOT second-class citizens — they integrate semantically with the topics they're about. A debugging session about memory architecture belongs with memory architecture content, not in a "logs" ghetto.

### Phase 5: The Routing Table

Finally, produce the mapping from filename patterns to directories. This is what a script will use to move files.

Format:
```
| Pattern | → Directory | Type | Count |
```

Cover 100% of files. No leftovers.

---

## How to Approach This

Browse the corpus directory listing on GitHub. Open files across the full spectrum — SOURCE files, AGENT files, SCRIPT files, ENGINE files, DYN files, RESPONSE files, ARCH files, logs, configs. Read enough to understand what each grouping is *really about* underneath the naming convention.

The key insight I'm looking for: operational logs and personal experience should integrate with the external knowledge they relate to. A session log where I debugged agent memory should live WITH agent memory content, not in a separate "logs" bin. The types should capture this — "raw signal" and "personal experience" might be different types that route to the SAME directory because they orbit the same concept.

I want to see what structure emerges from the content itself, not from the filename prefixes. The prefixes are artifacts of how files were created, not what they're about.
