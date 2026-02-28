# Extraction: SOURCE-20260213-014

**Source**: `SOURCE-20260213-x-article-sillydarket-solving_memory_for_openclaw_and_general_agents.md`
**Atoms extracted**: 21
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (10)

### ATOM-SOURCE-20260213-014-0001
**Lines**: 7-9
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> Every AI agent currently in use suffers from "context death," losing all session-specific information like decisions, preferences, and project context once a session ends.

### ATOM-SOURCE-20260213-014-0003
**Lines**: 23-26
**Context**: anecdote / evidence
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.50, epistemic_stability=0.60

> Plain markdown files, organized in folders and searchable with tools like grep, outperformed specialized memory infrastructure in the LoCoMo long-context memory benchmark, achieving 74.0% compared to 68.5% for specialized tools.

### ATOM-SOURCE-20260213-014-0004
**Lines**: 28-30
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> LLMs are inherently proficient at working with files, reading, searching, and organizing text due to their training on billions of examples, making specialized APIs for memory counterproductive.

### ATOM-SOURCE-20260213-014-0011
**Lines**: 114-117
**Context**: anecdote / limitation
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.00, speculation_risk=0.20, actionability=0.40, epistemic_stability=0.70

> LLMs tend to rewrite keywords during compression (e.g., "Decision: use Postgres" becomes "Postgres was selected for the database layer"), which can hinder downstream pattern-matching for classification.

### ATOM-SOURCE-20260213-014-0014
**Lines**: 139-146
**Context**: consensus / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> ClawVault makes zero network calls (excluding optional LLM for observation compression) and has no cloud dependency, storing agent memories directly on the filesystem to ensure data sovereignty and security for sensitive operational data.

### ATOM-SOURCE-20260213-014-0016
**Lines**: 150-153
**Context**: consensus / claim
**Tension**: novelty=0.50, consensus_pressure=0.50, contradiction_load=0.00, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.80

> The agent memory problem is fundamentally a design problem, not a technology problem, as existing tools like markdown files, YAML frontmatter, folder hierarchies, and wiki-links are sufficient.

### ATOM-SOURCE-20260213-014-0017
**Lines**: 155-162
**Context**: consensus / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> Human knowledge management and agent memory management are the same problem, both requiring typed/structured storage, associative linking, priority-based retrieval under budget constraints, signal-preserving compression, and zero platform lock-in.

### ATOM-SOURCE-20260213-014-0018
**Lines**: 156-159
**Context**: consensus / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> Using an Obsidian vault as an agent's memory vault makes the agent's knowledge inspectable, auditable, and editable by humans.

### ATOM-SOURCE-20260213-014-0020
**Lines**: 164-167
**Context**: consensus / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.00, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> When an agent's memory vault is an Obsidian vault, its memory becomes inspectable, auditable, and editable by humans through the graph view, folders, and frontmatter.

### ATOM-SOURCE-20260213-014-0021
**Lines**: 170-170
**Context**: consensus / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> ClawVault aims to solve the problem of 'context death' in AI agents.

## Concept (1)

### ATOM-SOURCE-20260213-014-0007
**Lines**: 60-68
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> Not all memories are equal; they can be categorized into types such as decisions, preferences, relationships, commitments, and lessons.

## Framework (2)

### ATOM-SOURCE-20260213-014-0005
**Lines**: 34-38
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.70

> Obsidian's approach to knowledge management, where notes are plain markdown files in folders with structured metadata (YAML frontmatter), wiki-links, and an emergent graph view, provides a powerful model for agent memory.

### ATOM-SOURCE-20260213-014-0015
**Lines**: 149-154
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.80

> An effective agent memory vault should possess five key characteristics: typed, structured storage; associative linking between concepts; priority-based retrieval under budget constraints; compression that preserves signal; and zero lock-in to any platform.

## Praxis Hook (8)

### ATOM-SOURCE-20260213-014-0002
**Lines**: 11-13
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.00, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> ClawVault™ is an open-source memory architecture designed to provide continuity for AI agents by preventing context death.

### ATOM-SOURCE-20260213-014-0006
**Lines**: 40-56
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.00, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> ClawVault stores every memory as a markdown file with YAML frontmatter, allowing it to function as a searchable ClawVault document, an Obsidian note with full Properties panel support, and a plain text file readable by any tool, ensuring zero lock-in and complete interoperability.

### ATOM-SOURCE-20260213-014-0008
**Lines**: 70-80
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.00, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> ClawVault enforces a taxonomy where every memory is typed, mapping these categories directly to Obsidian folders (e.g., `vault/decisions/`, `vault/people/`), enabling structured queries and visual organization for both agents and humans.

### ATOM-SOURCE-20260213-014-0009
**Lines**: 84-96
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.00, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> ClawVault utilizes wiki-links (`[[entity-name]]`) within notes, similar to Obsidian, to connect related memories (e.g., people, projects, decisions), which, when processed by `clawvault link --all`, generates a navigable knowledge graph for the agent's associative memory.

### ATOM-SOURCE-20260213-014-0010
**Lines**: 102-112
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.00, speculation_risk=0.30, actionability=0.90, epistemic_stability=0.60

> ClawVault's observational memory system compresses raw conversation transcripts into priority-tagged observations (🔴 Critical, 🟡 Notable, 🟢 Background) using an LLM, enabling budget-aware context injection where critical memories are loaded first.

### ATOM-SOURCE-20260213-014-0012
**Lines**: 119-121
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.00, speculation_risk=0.30, actionability=0.90, epistemic_stability=0.60

> To address LLM keyword rewriting during compression, ClawVault applies regex-based priority enforcement after LLM compression to ensure classification accuracy, trusting the LLM for compression quality but not for classification.

### ATOM-SOURCE-20260213-014-0013
**Lines**: 125-135
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.00, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> ClawVault uses a "vault index"—a single file listing every note with a one-line description—which agents scan first for queries, making it more efficient than embedding search for most queries by reducing vector similarity computations.

### ATOM-SOURCE-20260213-014-0019
**Lines**: 162-168
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> ClawVault™ is an open-source tool available for use today, installable via npm (`npm install clawvault`) for building agents with continuity.
