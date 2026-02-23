# Ontology Registry Proposal (from legacy/Tech folder) — v0.1

**Source**: `/Users/system/Desktop/legacy/Tech - essentially the capability blockers in order for us to achieve our Palantir-like Ontology/`

## Purpose
Extract the legacy “Tech” folder into a **structured ontology registry** proposal: a concrete, implementable schema for a Palantir-like ontology layer that can:
- unify tool/agent/workflow concepts,
- power search + routing + automation,
- remain durable as platforms churn.

This doc is a *proposal* for how to metabolize legacy content into a registry (not the full extraction yet).

## Observed legacy folder ontology strata (initial)
The folder already implies a hierarchy that can become registry “domains”:
1. **Toolcraft Endeavor — Unification**
2. **Workstation Taxonomy — Interaction Dynamics**
3. **Context Engineering (live doc)**
4. **Intelligence Capabilities (live doc)**
5. **Prompting (process archaeology)**
6. **Systematizing Business (HR/ops principles)**
7. **Agents (orchestration best practices)**
8. **Tool Landscape (cartography)**
9. **Intelligence Apparatus (unfinished archaeology: constitution/timelines/roles/engine)**

## Registry philosophy (what we’re building)
An “ontology registry” here means:
- **Canonical entity types** (Agent, Capability, Tool, Workflow, Artifact, Source, Protocol, Role, Environment…)
- **Explicit relations** (uses, produces, depends_on, mitigates, replaces, conflicts_with, governed_by…)
- **Versioning + provenance** (where did this claim come from; when was it true)
- **Operational bindings** (how the ontology maps to repo structure + execution automation)

## Proposed minimal schema (v0)
Store as **YAML or JSON** per-entity; aggregate indexes generated later.

### Entity Types
1) **Capability**
- id
- name
- definition
- maturity: {idea|draft|operational|deprecated}
- evaluation: (optional rubric)
- related_terms: []

2) **Tool**
- id
- name
- vendor
- category: {llm|agent-framework|automation|notes|messaging|search|code|storage|other}
- capabilities: [capability_id]
- constraints: (pricing, rate limits, OS, privacy)
- integration_points: (APIs, MCP, CLI, plugins)

3) **Agent / Role**
- id
- name
- function
- boundaries (what it must not do)
- inputs/outputs

4) **Workflow / Protocol**
- id
- name
- intent
- steps
- artifacts_produced
- quality_gates

5) **Artifact Type**
- id
- name
- location_pattern
- required_fields

6) **Source / Evidence**
- id
- kind: {doc|thread|repo|paper|video}
- citation
- extracted_claims: []

### Relation primitives (start small)
- tool_provides_capability
- agent_uses_tool
- workflow_requires_capability
- workflow_produces_artifact
- claim_supported_by_source
- term_alias_of_term

## Where it should live (proposal)
Create a canonical location:
- `engine/ontology/` (implementation-facing)
- OR `orchestration/state/REF-ONTOLOGY_REGISTRY.md` (protocol + schema)
- With data in: `engine/ontology/registry/` (YAML/JSON)

Recommendation:
- **Schema + conventions** in `orchestration/state/REF-ONTOLOGY_REGISTRY.md`
- **Entities** in `engine/ontology/registry/` (data-first)

## Extraction plan (from legacy/Tech)
### Phase 1 — Inventory
For each legacy markdown file, record:
- filename/path
- inferred domain
- candidate entities
- candidate relations
- “claims” (atomic statements) with confidence

### Phase 2 — Normalize to registry
- Create entity stubs
- Deduplicate terms (Rosetta alignment helps)
- Add provenance back-links to legacy file paths

### Phase 3 — Operational binding
- Use registry to drive:
  - doc routing (triage)
  - tool selection
  - “capability gap” backlog

## Immediate next actions (to execute next)
1) Create a **file-by-file extraction table** for the Tech folder (first pass, shallow).
2) Pick 5–10 “spine” entities to seed the registry:
   - Capability: context_management, task_routing, retrieval, memory, messaging, automation
   - Tool: openclaw, claude_code, codex_cli, gemini_cli
   - Workflow: capture→dispatch→return, handoff-token
3) Draft `REF-ONTOLOGY_REGISTRY.md` (schema + naming + file layout).

---

## Notes / Constraints
- This is intentionally minimal: we want an ontology that can be **used operationally** before it becomes philosophically complete.
- Legacy content is treated as **source evidence**, not truth.
