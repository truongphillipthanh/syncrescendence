# Extraction: SOURCE-20260108-website-article-dbreunig-a_software_library_with_no_code

**Source**: `SOURCE-20260108-website-article-dbreunig-a_software_library_with_no_code.md`
**Atoms extracted**: 18
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (12)

### ATOM-SOURCE-20260108-website-article-dbreunig-a_software_library_with_no_code-0001
**Lines**: 6-7
**Context**: anecdote / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.60

> The `whenwords` library is a relative time formatting library that contains no code.

### ATOM-SOURCE-20260108-website-article-dbreunig-a_software_library_with_no_code-0003
**Lines**: 14-16
**Context**: consensus / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> Unlike many similar libraries, `whenwords` is language agnostic, supporting Ruby, Python, Rust, Elixir, Swift, PHP, and Bash, and likely other languages.

### ATOM-SOURCE-20260108-website-article-dbreunig-a_software_library_with_no_code-0006
**Lines**: 44-46
**Context**: consensus / evidence
**Tension**: novelty=0.70, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.20, actionability=0.30, epistemic_stability=0.60

> Recent advancements in coding agents, such as Opus 4.5 coupled with Claude Code, have enabled them to implement tightly specified code with uncanny ability, crossing a threshold in Q4.

### ATOM-SOURCE-20260108-website-article-dbreunig-a_software_library_with_no_code-0008
**Lines**: 54-57
**Context**: hypothesis / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.20, speculation_risk=0.60, actionability=0.50, epistemic_stability=0.40

> For simple utility libraries, it might be preferable to have one tightly defined set of rules (specs) that are implemented on demand by coding agents, rather than many language-specific code libraries.

### ATOM-SOURCE-20260108-website-article-dbreunig-a_software_library_with_no_code-0009
**Lines**: 59-62
**Context**: anecdote / limitation
**Tension**: novelty=0.20, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> The `whenwords` utility is simple, with five functions, few dependencies, a well-defined standard (Unix time), and a ~500-line spec, making it suitable for a spec-only approach.

### ATOM-SOURCE-20260108-website-article-dbreunig-a_software_library_with_no_code-0011
**Lines**: 72-79
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.20, actionability=0.40, epistemic_stability=0.80

> Performance is a critical factor for traditional code libraries; for example, a spec-only browser would likely struggle with memory leaks and rendering speed compared to highly optimized, code-based implementations.

### ATOM-SOURCE-20260108-website-article-dbreunig-a_software_library_with_no_code-0012
**Lines**: 81-90
**Context**: hypothesis / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.20, speculation_risk=0.50, actionability=0.40, epistemic_stability=0.50

> Testing updates for spec-only libraries becomes complicated quickly, as changes to the spec must be verified across multiple languages and coding agents to ensure no regressions occur.

### ATOM-SOURCE-20260108-website-article-dbreunig-a_software_library_with_no_code-0013
**Lines**: 87-88
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> Foundational libraries such as nginx, Rails, and Postgres require ongoing maintenance, including essential security updates, making them dependencies worth maintaining.

### ATOM-SOURCE-20260108-website-article-dbreunig-a_software_library_with_no_code-0014
**Lines**: 88-90
**Context**: hypothesis / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.20, speculation_risk=0.30, actionability=0.40, epistemic_stability=0.60

> Spec-only libraries are best suited for implement-and-forget utilities and functions where continuous fixes, support, and security are not critical or valued.

### ATOM-SOURCE-20260108-website-article-dbreunig-a_software_library_with_no_code-0015
**Lines**: 92-95
**Context**: consensus / evidence
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.30, epistemic_stability=0.70

> The amount of surface area for testing grows rapidly for moderately complex spec-only libraries; for instance, `whenwords` has 125 tests, while SQLite has 51,445 tests.

### ATOM-SOURCE-20260108-website-article-dbreunig-a_software_library_with_no_code-0016
**Lines**: 93-96
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> A strong community around a software library leads to more bugs being spotted and fixed, faster acceptance of pull requests due to comprehensive testing, increased availability of help, and up-to-date code.

### ATOM-SOURCE-20260108-website-article-dbreunig-a_software_library_with_no_code-0018
**Lines**: 100-100
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.90

> For foundational software that serves as a building block, community is essential because it provides benefits like bug detection, fixes, and ongoing maintenance.

## Concept (2)

### ATOM-SOURCE-20260108-website-article-dbreunig-a_software_library_with_no_code-0007
**Lines**: 48-50
**Context**: hypothesis / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.70, actionability=0.40, epistemic_stability=0.50

> The "software library without code" is a tangible thought experiment to explore the implications of coding agents, particularly the question: "What does software engineering look like when coding is free?"

### ATOM-SOURCE-20260108-website-article-dbreunig-a_software_library_with_no_code-0017
**Lines**: 97-99
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.30, epistemic_stability=0.80

> The code we rely on is not merely an instantiation of a specification but also the product of the people and culture that form around a common goal, embodying the essence of open source.

## Framework (2)

### ATOM-SOURCE-20260108-website-article-dbreunig-a_software_library_with_no_code-0004
**Lines**: 20-24
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.60

> The `whenwords` library consists of specs and tests, specifically: `SPEC.md` (detailed behavior and implementation description), `tests.yaml` (language-agnostic input/output test cases), and `INSTALL.md` (instructions for building the library).

### ATOM-SOURCE-20260108-website-article-dbreunig-a_software_library_with_no_code-0010
**Lines**: 68-70
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.30, actionability=0.50, epistemic_stability=0.60

> There are five reasons why traditional code libraries are still preferred over spec-only libraries: when performance matters, when testing is complicated, when support and bug fixes are needed, when updates are crucial, and when community and interoperability are important.

## Praxis Hook (2)

### ATOM-SOURCE-20260108-website-article-dbreunig-a_software_library_with_no_code-0002
**Lines**: 9-10
**Context**: method / evidence
**Tension**: novelty=0.20, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> `whenwords` provides five functions (timeago, duration, parse_duration, human_date, date_range) that convert between timestamps and human-readable strings, such as turning a UNIX timestamp into "3 hours ago".

### ATOM-SOURCE-20260108-website-article-dbreunig-a_software_library_with_no_code-0005
**Lines**: 26-39
**Context**: method / evidence
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.60

> The installation instructions for `whenwords` involve pasting a prompt into a coding agent (e.g., Claude, Codex, Cursor) to implement the library in a specified language, read `SPEC.md`, parse `tests.yaml` to generate a test file, implement five functions, run tests until all pass, and place the implementation in a specified location.
