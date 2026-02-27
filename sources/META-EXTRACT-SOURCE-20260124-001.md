# Extraction: SOURCE-20260124-001

**Source**: `SOURCE-20260124-x-article-arscontexta-build_claude_a_tool_for_thought.md`
**Atoms extracted**: 15
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (4)

### ATOM-SOURCE-20260124-001-0001
**Lines**: 5-7
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Vibe note-taking, similar to vibe coding, leads to being overwhelmed by disorganized information when dealing with large quantities.

### ATOM-SOURCE-20260124-001-0005
**Lines**: 35-38
**Context**: hypothesis / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.20, speculation_risk=0.50, actionability=0.60, epistemic_stability=0.40

> Rules within an agent's tool for thought should start as hypotheses, with observations logged to persistent learning files for continuous reflection and evolution.

### ATOM-SOURCE-20260124-001-0010
**Lines**: 84-86
**Context**: hypothesis / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.30, speculation_risk=0.50, actionability=0.60, epistemic_stability=0.40

> The proposed agent-based tool for thought differs from human-operated systems because the architecture is used and can be built by the agent itself.

### ATOM-SOURCE-20260124-001-0015
**Lines**: 146-148
**Context**: hypothesis / claim
**Tension**: novelty=0.90, consensus_pressure=0.10, contradiction_load=0.40, speculation_risk=0.70, actionability=0.60, epistemic_stability=0.30

> The described agent-based tool for thought is a living system that gives Claude Code complete control to learn about tools for thought from humans and adapt its own note-taking based on that learning.

## Concept (2)

### ATOM-SOURCE-20260124-001-0002
**Lines**: 10-11
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.90

> Tools for thought are external systems humans build to facilitate thinking, addressing the limitations of internal cognitive capacity.

### ATOM-SOURCE-20260124-001-0009
**Lines**: 73-82
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.90

> Historical tools for thought like Llull's rotating wheels, Bruno's memory palaces, Zettelkasten, and evergreen notes were designed as systems to think WITH, not merely for storage, and were operated by humans.

## Framework (2)

### ATOM-SOURCE-20260124-001-0006
**Lines**: 42-46
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> A knowledge graph can be constructed from markdown files where files are nodes, wiki links are edges, and YAML frontmatter provides queryable metadata, allowing an LLM to navigate it naturally.

### ATOM-SOURCE-20260124-001-0012
**Lines**: 100-119
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.20, speculation_risk=0.50, actionability=0.90, epistemic_stability=0.40

> An agent-adapted Cornell Notes framework includes six phases for self-improvement: /reduce (extract claims), /reflect (find connections), /reweave (update notes), /recite (verify descriptions), /review (health checks), and /rethink (challenge assumptions), orchestrated by a /orchestrate pipeline and supported by /learn for further research.

## Praxis Hook (7)

### ATOM-SOURCE-20260124-001-0003
**Lines**: 14-22
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.20, speculation_risk=0.40, actionability=0.80, epistemic_stability=0.50

> To build a tool for thought native to agents, leverage existing agent capabilities such as markdown files and wiki links for structure, YAML and embeddings for discovery, hooks and subagents for automation, and bash, grep, git, and mcp servers for tooling.

### ATOM-SOURCE-20260124-001-0004
**Lines**: 30-33
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.30, speculation_risk=0.50, actionability=0.70, epistemic_stability=0.40

> A system can research tools for thought to build its own tool for thought by feeding it methodologies on how humans build knowledge systems, allowing it to adapt and adjust its instructions for agent-specific applications.

### ATOM-SOURCE-20260124-001-0007
**Lines**: 50-54
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.50

> To be more selective about context, an agent can be injected with a file tree at session start, where filenames are claims. When referencing a claim like "[[quality is the hard part]]", the title itself serves as the argument.

### ATOM-SOURCE-20260124-001-0008
**Lines**: 56-65
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.60

> Each note should include a YAML header with a one-sentence description, which an agent can use to decide if the full file content is worth loading, following a hierarchy of file tree → descriptions → headings → sections → full content.

### ATOM-SOURCE-20260124-001-0011
**Lines**: 90-95
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.30, speculation_risk=0.60, actionability=0.70, epistemic_stability=0.40

> To enable a self-engineering loop, an agent can read research articles, extract claims into notes, apply those claims to agent operations, log observations to persistent files, and reflect on its learnings to modify the system.

### ATOM-SOURCE-20260124-001-0013
**Lines**: 122-130
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.30, actionability=0.90, epistemic_stability=0.50

> Automated hooks can be used in an agent's tool for thought, such as /session-start.sh (injects vault context), /validate-note.sh (checks quality after write), /subagent-complete.sh (reminds about MOC updates), and /session-stop.sh (checks for broken links, prompts logging).

### ATOM-SOURCE-20260124-001-0014
**Lines**: 133-142
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.30, actionability=0.90, epistemic_stability=0.50

> Subagents can perform parallel, specialized work within an agent's tool for thought, such as 'reduce' for high-volume claim extraction (e.g., using Sonnet), 'reflect' for connection finding (e.g., using Sonnet), 'recite' for description verification (e.g., using Haiku), and 'review' for health checks (e.g., using a Haiku swarm).
