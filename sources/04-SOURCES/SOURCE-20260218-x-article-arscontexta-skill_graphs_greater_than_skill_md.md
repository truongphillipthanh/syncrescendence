---
url: https://x.com/arscontexta/status/2023957499183829467
author: "Heinrich (@arscontexta)"
captured_date: 2026-02-20
id: SOURCE-20260218-002
original_filename: "20260218-x_article-skill_graphs_greater_than_skill_md-@arscontexta.md"
status: triaged
platform: x
format: article
creator: arscontexta
signal_tier: paradigm
topics: [knowledge-management, ai-engineering, claude-code, developer-tools]
teleology: synthesize
notebooklm_category: claude-code
aliases: ["arscontexta - skill graphs greater than SKILL.md"]
synopsis: "Argues that single SKILL.md files cannot capture domain depth — skill graphs (networks of markdown files connected with wikilinks) enable recursive skill discovery, progressive disclosure, and domain understanding. Each node has YAML frontmatter for scanning, wikilinks embedded in prose carry semantic context, and MOCs organize clusters. Arscontexta is a 249-file skill graph that teaches agents to build skill graphs."
key_insights:
  - "Skill graphs apply skill discovery recursively: index -> descriptions -> links -> sections -> full content — most decisions happen before reading a single full file"
  - "Wikilinks embedded in prose carry semantic meaning (when and why to follow), unlike reference-only links — this gives agents contextual traversal paths"
  - "The difference between an agent that follows instructions and an agent that understands a domain is whether it navigates a knowledge structure vs reads a single file"
---
# Skill Graphs > SKILL.md
(Description: A dark-themed network graph visualization showing interconnected nodes with links radiating outward from a central purple node, representing a complex knowledge graph structure with labeled connection points)
People underestimate the power of structured knowledge. It enables entirely new kinds of applications.
Right now people write skills that capture one aspect of something. A skill for summarizing, a skill for code review and so on. (Often) one file with one capability.
That's fine for simple tasks but real depth requires something else.
Imagine a therapy skill that provides relevant information about cognitive behavioral patterns, attachment theory, active listening techniques, emotional regulation frameworks and so on.
A single skill file can't hold that.
## Skill Graphs
A skill graph is a network of skill files connected with wikilinks.
Instead of one big file you have many small composable pieces that reference each other. Each file is one complete thought, technique or skill and [[wikilinks between them create a traversable graph]].
A skill graph applies the same skill discovery pattern recursively inside the graph itself.
Every node has a yaml description the agent can scan without reading the whole file.
Every wiki link carries meaning because it's woven into prose so the agent follows relevant paths and skips what doesn't matter.
**Progressive disclosure:**
> index → descriptions → links → sections → full content
Most decisions happen before reading a single full file.
## The Primitives
You already have everything you need.
- **wikilinks** that read as prose in sentences, so they carry meaning not just references
- **yaml frontmatter** with descriptions so the agent can scan without reading full files
- **MOCs (maps of content)** that organize clusters of related skills into navigable sub-topics
Skill links to other skills which link to other skills and the graph goes as deep as the domain requires.
## Arscontexta Plugin
Arscontexta is a skill graph that teaches your agent how to build skill graphs.
(Okay actually it's about building knowledge bases but that's the same thing...)
~250 connected markdown files that teach an agent how to build a massive knowledge base aka skill graph for you.
One skill file couldn't do that.
But things change if you build a graph of interconnected research claims (/skills) about cognitive science, zettelkasten, graph theory, agent architecture where each piece links to others, each one composable and the whole thing is traversable.
## What This Enables
Think about it:
- **a trading skill graph**: risk management, market psychology, position sizing, technical analysis, each piece linked to related concepts so context flows between them
- **a legal skill graph**: contract patterns, compliance requirements, jurisdiction specifics, precedent chains, all traversable from one entry point
- **a company skill graph**: org structure, product knowledge, processes, onboarding context, culture, competitive landscape
None of these fit in one file but all of them work as graphs.
## How To Build One
**The easy way:** install the arscontexta claude code plugin, pick the research preset and point it at any topic.
It sets up the markdown folder structure for you and then you fill it with /learn and /reduce.
**The manual way:** it's simpler than you think.
A skill graph doesn't need to live in your .claude/skills/ folder. The key is an index file that tells the agent what exists and how to traverse it.
Here's what an index looks like for a knowledge work skill graph:
```markdown
# knowledge-work
Agents need tools for thought too. Just as Zettelkasten, evergreen notes, and memory palaces gave humans external structures to think with, agent-operated knowledge systems give agents external structures to think with.
## Synthesis
Developed arguments about how the pieces fit together:
- [[the system is the argument]] — philosophy with proof of work; every note, link, and MOC demonstrates the methodology it describes
- [[coherent architecture emerges from wiki links spreading activation and small-world topology]] — the foundational triangle that answers what structure looks like, why it works, how agents navigate it, and when to reassess
...
## Topic MOCs
The domain breaks into seven interconnected areas:
- [[graph-structure]] — how wiki links, topology, and linking patterns create traversable knowledge graphs
- [[agent-cognition]] — how agents think through external structures: traversal, sessions, attention limits
- [[agent-cognition-hooks]] — hook enforcement, composition, and cognitive science of automated quality
- [[agent-cognition-platforms]] — platform capability tiers, abstraction layers, context file architecture
- [[discovery-retrieval]] — how descriptions, progressive disclosure, and search enable finding and loading content
- [[processing-workflow]] — how throughput, sessions, and handoffs move work through the system
...
## Cross-Domain Claims
- [[forced engagement produces weak connections]] — the social analog of accretion over productivity: forcing engagement for activity's sake produces shallow connections, just as accumulation without synthesis produces shallow knowledge graphs
## Explorations Needed
- Missing: comparison between human and agent traversal patterns. do agents need different architectures?
- Scaling limits: at what system size does human curation fail?
```
The index isn't a lookup table, it's an entry point that points attention. The agent reads it, understands the landscape and follows the links that matter for the current conversation.
Each linked file is a standalone methodology claim (= skill). Here's what one node looks like:
(Description: A markdown document screenshot showing technical documentation about MOC (Map of Content) maintenance strategies, discussing organizational overhead in attention investment, MOC management patterns, and architectural considerations for agent navigation. The document contains blue wikilinks embedded within prose paragraphs demonstrating contextual linking patterns.)
See how the wikilinks inside the prose tell the agent when and why to follow them.
An map of contents (MOCs) organize sub-topics when the graph gets larger.
## The Evolution
Skills are context engineering, basically curated knowledge injected where it matters.
Skill graphs are the next step.
Instead of one injection the agent navigates a knowledge structure, pulling in exactly what the current situation requires.
This is the difference between an agent that follows instructions and an agent that understands a domain.
Arscontexta is a claude code plugin that does this for building knowledge systems. 249 files of structured knowledge the agent traverses to derive a local knowledge system that really fits your workflow.
Go use it and build skill graphs for everything else.
—heinrich