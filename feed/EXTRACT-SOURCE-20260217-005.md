# Extraction: SOURCE-20260217-005

**Source**: `SOURCE-20260217-x-article-dhravyashah-why_everyone_is_complaining_about_openclaw_memory_it_sucks_and_why_supermemory_fixes_it.md`
**Atoms extracted**: 7
**Categories**: claim, framework

---

## Claim (5)

### ATOM-SOURCE-20260217-005-0001
**Lines**: 12-13
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.10, epistemic_stability=0.80

> OpenClaw's primary problem is its memory system.

### ATOM-SOURCE-20260217-005-0002
**Lines**: 19-20
**Context**: anecdote / counterevidence
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.30, speculation_risk=0.20, actionability=0.10, epistemic_stability=0.60

> The QMD memory plugin, added by OpenClaw, does not adequately fix its memory problems.

### ATOM-SOURCE-20260217-005-0005
**Lines**: 44-48
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.20, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.70

> OpenClaw's memory system is problematic because it relies on tools rather than hooks, requiring the main agent to explicitly utilize tools for memory operations, which is slow and can use more tokens due to tool call overhead.

### ATOM-SOURCE-20260217-005-0006
**Lines**: 50-53
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.20, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.70

> OpenClaw's memory system does not effectively handle knowledge updates, temporal reasoning, or multi-session context, leading to redundancy and a failure to update existing knowledge.

### ATOM-SOURCE-20260217-005-0007
**Lines**: 55-57
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.20, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.70

> OpenClaw's memory system does not forget irrelevant information, which is crucial for keeping context fresh and useful over time.

## Framework (2)

### ATOM-SOURCE-20260217-005-0003
**Lines**: 32-36
**Context**: method / evidence
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> OpenClaw's memory system uses two layers of storage: daily append-only logs (`memory/YYYY-MM-DD.md`) for scratchpad context (today + yesterday at session start), and `MEMORY.md` for curated long-term facts, preferences, and decisions (loaded only in private/DM sessions).

### ATOM-SOURCE-20260217-005-0004
**Lines**: 38-41
**Context**: method / evidence
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> OpenClaw's memory system uses two read-side tools: `memory_search` for semantic search across all memory files to return snippets, and `memory_get` to read specific lines from a file after they are found by search.
