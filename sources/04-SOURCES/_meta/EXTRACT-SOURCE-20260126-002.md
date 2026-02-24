# Extraction: SOURCE-20260126-002

**Source**: `SOURCE-20260126-x-article-arscontexta-vibe_note_taking_101_editing_workflow.md`
**Atoms extracted**: 8
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (1)

### ATOM-SOURCE-20260126-002-0001
**Lines**: 6-19
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Editing long content with Claude Code is inefficient due to the back-and-forth process of copying and pasting sections for edits.

## Concept (2)

### ATOM-SOURCE-20260126-002-0002
**Lines**: 26-30
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.60

> Spatial Editing is a method where edit instructions are placed directly within the text they pertain to, using curly braces `{}` to mark comments, rather than copying text to an external AI.

### ATOM-SOURCE-20260126-002-0007
**Lines**: 83-85
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> The key principle of Spatial Editing is that 'position IS context,' meaning the location of an edit comment inherently explains what it refers to, eliminating the need for explicit explanations.

## Framework (1)

### ATOM-SOURCE-20260126-002-0006
**Lines**: 74-79
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> A workflow for Spatial Editing involves: 1. Writing a draft without interruption. 2. Dropping `{thoughts}` wherever issues are found during a quick read. 3. Running the `/edit` command. 4. Reviewing the changes made.

## Praxis Hook (4)

### ATOM-SOURCE-20260126-002-0003
**Lines**: 26-30
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> To implement Spatial Editing, use curly braces `{}` to embed edit instructions directly within the text. Each comment applies to its surrounding text, or can point to another location if specified.

### ATOM-SOURCE-20260126-002-0004
**Lines**: 56-64
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> The `/edit` command can be used to process edits in the currently open file, a specific file (e.g., `/edit draft.md`), or multiple files (e.g., `/edit draft.md notes.md`).

### ATOM-SOURCE-20260126-002-0005
**Lines**: 66-70
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> If `/edit` is run without a file specified, it searches the vault for `{thoughts}` using `rg "\{[^}]+\}" --type md -l` and allows the user to select files for editing.

### ATOM-SOURCE-20260126-002-0008
**Lines**: 89-91
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> To build a similar Spatial Editing system, use the skill-creator skill within Claude Code plugins and integrate the principles described in this article.
