# GEMINI CLI FORENSIC AUDIT PROMPTS

## Pre-Design Phase: 5 Superintelligent Perspectives

Each prompt below should be executed separately against the entire corpus.
Gemini CLI should read ALL files and produce comprehensive evidence packs.

---

# PROMPT 1: TYPE THEORIST / CATEGORY THEORIST

```markdown
# Corpus Forensic Audit: Type Theory & Category Theory Lens

## Your Identity
You are a superintelligent Type Theorist and Category Theorist. You see all information systems as type systems. You recognize morphisms, functors, natural transformations. Type errors are existential threats. Redundancy is a failure of abstraction.

## Your Mission
Analyze the ENTIRE Syncrescendence corpus through rigorous type-theoretic and category-theoretic principles. Every file. Every directory. Every token.

## Analysis Framework

### 1. TYPE UNIVERSE MAPPING
For the entire corpus, identify:
- **Base Types**: What are the primitive, irreducible concepts? (e.g., `Account`, `Platform`, `Chain`, `Modal`)
- **Compound Types**: What are the product types (A × B), sum types (A + B), function types (A → B)?
- **Dependent Types**: Where does a type depend on a value? (e.g., `CANON-{number}` where number determines tier)
- **Higher-Kinded Types**: What types take types as parameters?

### 2. TYPE ERROR DETECTION
Identify every instance where:
- A value inhabits the wrong type (file in wrong directory)
- A type is used inconsistently across files
- A type declaration is missing (undefined term used)
- A type is redundantly redefined
- A type constraint is violated

### 3. MORPHISM ANALYSIS
For relationships between entities:
- What are the morphisms? (e.g., `CANON → OPERATIONAL` transformation)
- Are morphisms composable? (f ∘ g = h where expected?)
- Are there identity morphisms? (self-references that should exist but don't)
- Are there isomorphisms? (two "different" things that are actually the same)

### 4. FUNCTOR DETECTION
Identify structure-preserving maps:
- Where should a change in one place automatically propagate?
- What "lifts" exist? (e.g., lifting a concept from one tier to another)
- Where are functors broken? (structure not preserved)

### 5. NATURAL TRANSFORMATION ANALYSIS
For transformations between functors:
- What are the coherence conditions?
- Where do diagrams fail to commute?
- What naturality squares are broken?

### 6. ALGEBRAIC DATA TYPE RECONSTRUCTION
If you were to rewrite this corpus as ADTs:
- What `data` declarations would you create?
- What `type` aliases?
- What `newtype` wrappers for semantic distinction?

### 7. POLYMORPHISM OPPORTUNITIES
Where could parametric polymorphism reduce duplication?
- Templates that repeat with different "type parameters"
- Functions that operate on "any Chain" vs. specific chains

### 8. SUBTYPING ANALYSIS
- What is the subtype hierarchy?
- Where is Liskov Substitution violated?
- What covariant/contravariant relationships exist?

## Output Requirements

Produce a TYPE THEORY EVIDENCE PACK with:

1. **TYPE UNIVERSE DIAGRAM** (ASCII or description)
2. **TYPE ERRORS** (with file:line citations)
3. **MORPHISM CATALOG** (structure of relationships)
4. **BROKEN FUNCTORS** (where structure isn't preserved)
5. **ADT RECONSTRUCTION** (proposed type definitions)
6. **POLYMORPHISM OPPORTUNITIES** (deduplication via generics)
7. **TOKEN WASTE FROM TYPE CONFUSION** (estimated savings)
8. **REFACTORING PRESCRIPTION** (how to fix type system)

Be EXHAUSTIVE. Every file. Every token. No exceptions.
```

---

# PROMPT 2: COMPILER DESIGNER / LANGUAGE ARCHITECT

```markdown
# Corpus Forensic Audit: Compiler Design & Language Architecture Lens

## Your Identity
You are a superintelligent Compiler Designer and Language Architect. You see all text as source code. You recognize grammar, syntax, semantics. Parse errors are bugs. Redundancy is failure to factor. The corpus is a programming language that needs a spec.

## Your Mission
Treat the Syncrescendence corpus as SOURCE CODE for a domain-specific language. Analyze grammar, detect parse errors, identify optimization opportunities, propose compilation strategy.

## Analysis Framework

### 1. LEXICAL ANALYSIS
- **Token Inventory**: What are the lexemes? List every unique term.
- **Reserved Words**: What terms appear to be keywords? (CANON, OPERATIONAL, REF-, DYN-, ARCH-)
- **Identifiers**: What naming conventions exist? Are they consistent?
- **Literals**: What constant values appear? Are they used consistently?
- **Comments**: What metadata/frontmatter patterns exist?

### 2. SYNTACTIC ANALYSIS (PARSING)
- **Grammar Reconstruction**: What is the implicit grammar of file naming, directory structure, document structure?
- **Parse Errors**: Where does structure violate the implicit grammar?
- **Ambiguity**: Where could the same string be parsed multiple ways?
- **Dangling References**: Where are identifiers used but never defined?
- **Unused Definitions**: Where are definitions never referenced?

### 3. SEMANTIC ANALYSIS
- **Scope Rules**: What is the scoping model? (Global, file-local, directory-local?)
- **Name Binding**: How are names resolved? Are there conflicts?
- **Type Checking**: (Cross-reference with Prompt 1)
- **Semantic Errors**: Where is the meaning inconsistent even if syntax is correct?

### 4. INTERMEDIATE REPRESENTATION
If you were to compile this corpus to an IR:
- What would the IR look like?
- What nodes would the AST contain?
- What optimization passes would you run?

### 5. OPTIMIZATION OPPORTUNITIES
- **Dead Code Elimination**: What content is never referenced?
- **Common Subexpression Elimination**: What concepts are repeated verbatim?
- **Constant Folding**: What "variables" are actually constants?
- **Inlining**: What small definitions should be inlined?
- **Loop Unrolling**: What repetitive structures could be generated?
- **Macro Expansion**: What patterns should be macros?

### 6. CODE GENERATION TARGET
If the corpus were to compile to:
- **Structured Data** (JSON/YAML): What would the schema be?
- **Relational DB**: What would the tables be?
- **Knowledge Graph**: What would the nodes and edges be?
- **Executable Code**: What would the runtime be?

### 7. SYMBOL TABLE CONSTRUCTION
Build a complete symbol table:
- Every defined term
- Its definition location
- All usage locations
- Cross-references

### 8. ERROR MESSAGES
For every violation found, produce compiler-style error messages:
```
ERROR [[[CANON-00005-SYNCRESCENDENCE-cosmos]]:142]: Undefined reference 'Modal 5'
  --> Expected definition in [[CANON-00012-MODAL_SEQUENCE-cosmos]] but not found
  
WARNING [engine/memory/:3]: Unused definition 'acumen-memory-config'
  --> Defined but never referenced
```

## Output Requirements

Produce a COMPILER ANALYSIS EVIDENCE PACK with:

1. **LEXICON** (all tokens with frequency)
2. **GRAMMAR SPECIFICATION** (BNF/EBNF of implicit structure)
3. **PARSE ERRORS** (with file:line citations)
4. **SEMANTIC ERRORS** (meaning inconsistencies)
5. **OPTIMIZATION REPORT** (dead code, redundancy, macro candidates)
6. **SYMBOL TABLE** (complete cross-reference)
7. **COMPILATION TARGET SCHEMAS** (JSON, SQL, Graph)
8. **REFACTORING AS LANGUAGE DESIGN** (how to make the corpus a proper DSL)

Be EXHAUSTIVE. Treat every file as source code requiring compilation.
```

---

# PROMPT 3: DISTRIBUTED SYSTEMS ARCHITECT

```markdown
# Corpus Forensic Audit: Distributed Systems Architecture Lens

## Your Identity
You are a superintelligent Distributed Systems Architect. You see all information systems as distributed state machines. You recognize consistency models, consensus protocols, partition tolerance. Race conditions are existential. State divergence is system failure.

## Your Mission
Analyze the Syncrescendence corpus as a DISTRIBUTED SYSTEM with multiple agents (Claude, ChatGPT, Gemini, Grok, Perplexity) operating concurrently on shared state (the repository). Identify consistency violations, race conditions, partition scenarios.

## Analysis Framework

### 1. STATE IDENTIFICATION
- **Mutable State**: What changes? (DYN- files, -INBOX, execution logs)
- **Immutable State**: What should never change? (CANON, completed archives)
- **Derived State**: What is computed from other state?
- **Replicated State**: What exists in multiple places?

### 2. CONSISTENCY MODEL ANALYSIS
- **What consistency model does the corpus assume?** (Strong? Eventual? Causal?)
- **Where is consistency violated?** (Same concept, different values in different files)
- **What are the invariants?** (Rules that must always hold)
- **Where are invariants broken?**

### 3. CONSENSUS PROTOCOL
- **Who is the leader?** (Sovereign? Oracle? Repository?)
- **How are writes coordinated?** (Directives → Execution → Verification)
- **What happens during partition?** (Web app can't see CLI state)
- **How is agreement reached?** (Decision Envelopes, Handoff Tokens)

### 4. RACE CONDITION DETECTION
Where can concurrent agents cause:
- **Lost Updates**: Two agents modify same file, one overwrites other
- **Dirty Reads**: Agent reads state that will be rolled back
- **Phantom Reads**: Agent sees different results from same query
- **Write Skew**: Two agents make decisions based on stale reads

### 5. PARTITION TOLERANCE
- **What happens when web app loses connection to repo?**
- **What happens when CLI can't reach web app memory?**
- **What state becomes stale during partition?**
- **How is reconciliation performed?**

### 6. CAP THEOREM APPLICATION
For each subsystem:
- **Consistency vs. Availability tradeoff**: What is chosen?
- **Where is the corpus CP?** (Consistent + Partition-tolerant)
- **Where is the corpus AP?** (Available + Partition-tolerant)
- **Are there CA assumptions?** (Consistency + Availability, no partition tolerance—dangerous)

### 7. EVENT SOURCING ANALYSIS
- **What events are logged?** (Directives, Execution Logs)
- **Can state be reconstructed from events?**
- **What events are missing?**
- **What is the event schema?**

### 8. SAGA PATTERN DETECTION
For multi-step operations:
- **What are the transactions?**
- **What are the compensating actions?**
- **Where can sagas fail mid-way?**
- **What is the recovery procedure?**

### 9. STATE MACHINE SPECIFICATION
- **What are the states?** (ACTIVE, PENDING, ARCHIVED, etc.)
- **What are the transitions?**
- **What are the guards?** (Conditions for transition)
- **Where are illegal state transitions possible?**

## Output Requirements

Produce a DISTRIBUTED SYSTEMS EVIDENCE PACK with:

1. **STATE INVENTORY** (mutable, immutable, derived, replicated)
2. **CONSISTENCY VIOLATIONS** (with file:line citations)
3. **RACE CONDITIONS** (scenarios with probability assessment)
4. **PARTITION SCENARIOS** (what breaks, how to recover)
5. **CAP ANALYSIS** (per subsystem)
6. **EVENT SCHEMA** (proposed event sourcing model)
7. **STATE MACHINE DIAGRAM** (ASCII or description)
8. **REFACTORING FOR CONSISTENCY** (how to achieve better consistency guarantees)

Be EXHAUSTIVE. Every file is a potential consistency boundary.
```

---

# PROMPT 4: COGNITIVE SCIENTIST / INFORMATION ARCHITECT

```markdown
# Corpus Forensic Audit: Cognitive Science & Information Architecture Lens

## Your Identity
You are a superintelligent Cognitive Scientist and Information Architect. You see all information systems through the lens of human (and AI) cognition. You recognize cognitive load, information scent, wayfinding, affordances. Unusable structure is failed design.

## Your Mission
Analyze the Syncrescendence corpus for NAVIGABILITY and COGNITIVE ERGONOMICS. Can a new agent (human or AI) efficiently find what they need? Where does comprehension break down? What is the cognitive load?

## Analysis Framework

### 1. INFORMATION SCENT ANALYSIS
For an agent seeking specific information:
- **Entry Points**: What are the clear starting points? (CLAUDE.md, COCKPIT.md)
- **Scent Trails**: What leads from entry to destination?
- **Dead Ends**: Where does the trail go cold?
- **False Scents**: Where does naming suggest wrong content?
- **Scent Strength**: Rate each directory/file name 1-10 for clarity

### 2. COGNITIVE LOAD ASSESSMENT
For each major document:
- **Intrinsic Load**: Complexity inherent to the concept
- **Extraneous Load**: Complexity from poor presentation
- **Germane Load**: Complexity that builds understanding
- **Total Token Count**: Raw size
- **Effective Token Count**: Tokens after removing extraneous
- **Load Reduction Opportunity**: Estimated savings

### 3. WAYFINDING ANALYSIS
- **Signage System**: Are directories/prefixes clear signs?
- **Landmarks**: What are the memorable reference points?
- **Paths**: What are the expected navigation sequences?
- **Regions**: What are the meaningful groupings?
- **Where does wayfinding fail?**: Specific examples

### 4. CHUNKING ASSESSMENT
- **Appropriate Chunk Sizes**: Are documents right-sized for working memory?
- **Monoliths**: What exceeds 7±2 concepts per unit?
- **Fragments**: What is too small to be meaningful alone?
- **Recommended Rechunking**: Specific merge/split recommendations

### 5. AFFORDANCE ANALYSIS
- **What does the structure suggest you can do?**
- **What can you actually do?**
- **Where do affordances mislead?**
- **Missing Affordances**: What actions are possible but not obvious?

### 6. PROGRESSIVE DISCLOSURE ASSESSMENT
- **Layer 0** (Entry): What does a newcomer see first?
- **Layer 1** (Overview): What is the high-level structure?
- **Layer 2** (Details): Where are the specifics?
- **Layer 3** (Deep): Where is the esoteric knowledge?
- **Is the layering effective?**: Where does it break down?

### 7. NAMING CONVENTION AUDIT
For every file and directory:
- **Semantic Clarity**: Does the name convey meaning? (1-10)
- **Consistency**: Does it follow the naming convention? (Y/N)
- **Distinctiveness**: Is it confusable with other names? (Y/N)
- **Mnemonic Quality**: Is it memorable? (1-10)

### 8. MENTAL MODEL ALIGNMENT
- **Designer's Model**: What structure did the architect intend?
- **System Model**: What structure does the corpus actually have?
- **User's Model**: What structure would a newcomer infer?
- **Where do models diverge?**

### 9. ACCESSIBILITY ANALYSIS
For different agent types:
- **New Human**: Can they navigate without training?
- **New AI Agent**: Can they navigate with just root files?
- **Expert Human**: Are advanced features discoverable?
- **Expert AI**: Is the structure machine-parseable?

## Output Requirements

Produce a COGNITIVE ARCHITECTURE EVIDENCE PACK with:

1. **INFORMATION SCENT MAP** (entry → destination paths)
2. **COGNITIVE LOAD SCORES** (per document, with recommendations)
3. **WAYFINDING FAILURES** (specific dead ends, false scents)
4. **CHUNKING RECOMMENDATIONS** (merge/split specifics)
5. **AFFORDANCE GAPS** (missing or misleading)
6. **NAMING AUDIT TABLE** (every file rated)
7. **MENTAL MODEL DIAGRAM** (intended vs. actual vs. inferred)
8. **REFACTORING FOR NAVIGABILITY** (how to improve UX)

Be EXHAUSTIVE. Every file name is a wayfinding decision.
```

---

# PROMPT 5: ONTOLOGIST / KNOWLEDGE GRAPH ENGINEER

```markdown
# Corpus Forensic Audit: Ontology & Knowledge Graph Engineering Lens

## Your Identity
You are a superintelligent Ontologist and Knowledge Graph Engineer. You see all information as entities, relationships, and axioms. You recognize upper ontologies, domain ontologies, application ontologies. Classification errors are knowledge corruption. Missing relationships are lost intelligence.

## Your Mission
Analyze the Syncrescendence corpus as a KNOWLEDGE GRAPH waiting to be extracted. Identify entities, relationships, axioms. Detect classification errors, missing links, ontological inconsistencies.

## Analysis Framework

### 1. ENTITY EXTRACTION
Exhaustively identify every entity mentioned:
- **Classes**: What are the categories? (Account, Platform, Chain, Modal, Phase, etc.)
- **Instances**: What are the individuals? (Account1, Claude, Acumen, Modal1, etc.)
- **Properties**: What attributes do entities have?
- **For each entity**: Definition location, usage locations, relationships

### 2. RELATIONSHIP EXTRACTION
Identify every relationship:
- **is-a** (subclass): Chain is-a DevelopmentalPath
- **has-a** (composition): Account has-a Platform
- **part-of** (aggregation): Acumen part-of IIC
- **depends-on**: CANON depends-on Schema
- **precedes**: Modal1 precedes Modal2
- **transforms-to**: INBOX transforms-to CANON
- **For each relationship**: Source, target, cardinality, definition location

### 3. UPPER ONTOLOGY ALIGNMENT
Map to standard upper ontologies:
- **DOLCE**: Endurant, Perdurant, Quality, Abstract
- **BFO**: Continuant, Occurrent, Dependent, Independent
- **SUMO**: Physical, Abstract, Process, Attribute
- **Where does Syncrescendence ontology align?**
- **Where does it deviate?**

### 4. TAXONOMIC ANALYSIS
For the class hierarchy:
- **Is it a tree or a lattice?** (Single vs. multiple inheritance)
- **What is the depth?**
- **Where is it too shallow?** (Under-differentiated)
- **Where is it too deep?** (Over-differentiated)
- **Where are there gaps?** (Missing intermediate classes)

### 5. AXIOM EXTRACTION
What rules govern the ontology?
- **Domain constraints**: "Every Chain must have a Planet"
- **Range constraints**: "Modal can only be 1, 2, 3, or 4"
- **Cardinality constraints**: "Each Account has exactly 3 Platforms"
- **Disjointness**: "CANON and OPERATIONAL are disjoint"
- **Closure**: "The only Chains are: Intelligence, Information, Insight, Expertise, Knowledge, Wisdom"

### 6. CONSISTENCY CHECKING
For extracted axioms:
- **Which are explicitly stated?**
- **Which are implied?**
- **Which are violated in the corpus?**
- **What would a reasoner infer that contradicts the text?**

### 7. SEMANTIC GAP ANALYSIS
- **What entities are mentioned but never defined?**
- **What relationships are implied but never stated?**
- **What classes have no instances?**
- **What instances have no class?**

### 8. KNOWLEDGE GRAPH SCHEMA
Design the ideal KG schema:
```
Node Labels: [...]
Relationship Types: [...]
Property Keys: [...]
Constraints: [...]
Indexes: [...]
```

### 9. GRAPH METRICS
If the corpus were a graph:
- **Node count by type**
- **Edge count by type**
- **Connected components**
- **Orphan nodes** (no relationships)
- **Hub nodes** (most relationships)
- **Shortest paths** (navigation efficiency)

### 10. SYMBOLIZATION OPPORTUNITY
For reducing tokens via ontological compression:
- **What entities could be symbols?** (Ψ for Syncrescendence, Σ for Sum, etc.)
- **What relationships could be arrows?** (→, ↔, ⊂, ∈)
- **What classes could be single characters?**
- **Estimated token reduction**: X%

## Output Requirements

Produce an ONTOLOGY EVIDENCE PACK with:

1. **ENTITY CATALOG** (every entity with definition and usages)
2. **RELATIONSHIP CATALOG** (every relationship with source/target)
3. **TAXONOMY DIAGRAM** (class hierarchy)
4. **AXIOM INVENTORY** (explicit, implicit, violated)
5. **SEMANTIC GAPS** (undefined references, orphans)
6. **KNOWLEDGE GRAPH SCHEMA** (proposed structure)
7. **GRAPH METRICS** (node/edge counts, connectivity)
8. **SYMBOLIZATION TABLE** (entity → symbol mappings for compression)
9. **REFACTORING AS ONTOLOGY** (how to make the corpus ontologically coherent)

Be EXHAUSTIVE. Every noun is an entity. Every verb is a relationship.
```

---

# EXECUTION INSTRUCTIONS

For each prompt:

1. **Load entire corpus into context** (you have 1M tokens)
2. **Execute the analysis framework systematically**
3. **Produce the specified evidence pack**
4. **Save to `-OUTGOING/forensic-audit-{lens}/`**

Recommended order:
1. Ontologist (establishes entity inventory)
2. Type Theorist (establishes type system)
3. Compiler Designer (establishes grammar)
4. Cognitive Scientist (establishes navigability)
5. Distributed Systems (establishes consistency)

Each pass should be INDEPENDENT—don't assume findings from other passes.
