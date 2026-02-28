# Extraction: SOURCE-20260126-001

**Source**: `SOURCE-20260126-x-article-arscontexta-obsidian_and_claude_code_101_context_engineering.md`
**Atoms extracted**: 9
**Categories**: analogy, claim, framework, praxis_hook

---

## Analogy (1)

### ATOM-SOURCE-20260126-001-0007
**Lines**: 71-82
**Context**: consensus / evidence
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.70

> The progressive disclosure pattern for note-taking is analogous to MCP tool discovery, where tool specs are deferred until needed, following a structure of 'tool list → tool search → tool references → full definitions'.

## Claim (1)

### ATOM-SOURCE-20260126-001-0006
**Lines**: 62-69
**Context**: consensus / claim
**Tension**: novelty=0.50, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.60, actionability=0.70, epistemic_stability=0.70

> Most notes will not reach the 'Full Content' stage in a progressive disclosure system, as Claude is forced to justify each read, leading to better curation.

## Framework (2)

### ATOM-SOURCE-20260126-001-0002
**Lines**: 13-13
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> The progressive disclosure pattern for Claude Code note-taking involves four layers: File Tree, YAML Descriptions, Outline, and Full Content.

### ATOM-SOURCE-20260126-001-0008
**Lines**: 84-86
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> The progressive disclosure structure for Claude Code is: file tree → descriptions → outline → full content.

## Praxis Hook (5)

### ATOM-SOURCE-20260126-001-0001
**Lines**: 8-11
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> To improve note-taking with Claude Code, force it to be selective about what it reads by implementing a four-layer progressive disclosure pattern.

### ATOM-SOURCE-20260126-001-0003
**Lines**: 15-29
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> Implement a SessionStart hook to inject the full file tree (`tree -L 3 -a -I '.git|.obsidian' --noreport`) before Claude begins processing, providing a map of the project structure.

### ATOM-SOURCE-20260126-001-0004
**Lines**: 35-47
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> Include a one-sentence `description` in the YAML frontmatter of every note to elaborate on its title, allowing Claude to query descriptions with `rg "^description:" 01_thinking/*.md`.

### ATOM-SOURCE-20260126-001-0005
**Lines**: 49-60
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> After passing the description filter, Claude should check the note's outline using `grep -n "^#" "01_thinking/knowledge-work.md"` to identify relevant sections and avoid loading the full file unnecessarily.

### ATOM-SOURCE-20260126-001-0009
**Lines**: 88-96
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> Implementing the progressive disclosure system for Claude Code involves: a SessionStart hook running `tree`, YAML frontmatter with a description field, and instructions in `claude.md` guiding Claude to check descriptions before reading.
