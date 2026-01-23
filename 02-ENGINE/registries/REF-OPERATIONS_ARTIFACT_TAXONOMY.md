---
id: operations-artifact-taxonomy
kind: protocol
scope: repo
target: repo
owner: Deviser
triggers:
  - new prompt/spec/script created
  - Blitzkrieg
  - /deviser_reint
outputs:
  - consistent naming
  - frontmatter presence
  - discoverable registries
---

# Operations Artifact Taxonomy, Naming, and Frontmatter

## Purpose

We produce many artifact types across web apps and CLI. This protocol prevents drift by making each artifact (prompt, spec, command, schema, script, evidence pack) self-describing and routable by humans and automation.

## Naming (two layers)

1. Prefix indicates lifecycle/stability:

* REF- : stable reference spec (protocols, standards, taxonomies)
* ARCH- : historical narrative / archaeology
* DYN- : regenerated reports / dashboards
* SCAFF- : scaffolds intended to be replaced
* PROMPT- : executable prompt text for a model/system
* CMD- : command definition (slash command, CLI command recipe)
* SCHEMA- : structured schema (json/yaml)

2. Directory indicates function:

* 02-ENGINE/prompts/ : PROMPT-* files grouped by system (chatgpt/claude/gemini)
* 02-ENGINE/specs/ : REF-* protocols
* 02-ENGINE/schemas/ : SCHEMA-*
* 02-ENGINE/commands/ : CMD-* plus pointers to tool-native command locations
* 02-ENGINE/scripts/ : automation scripts (shell/python/applescript)
* 02-ENGINE/registries/ : indexes and lookup tables

## Minimal YAML frontmatter (required)

Every PROMPT-* and REF-* document must begin with YAML frontmatter containing:

* id
* kind (system_prompt | project_instructions | memory_registration | rag_reference | protocol | schema | command | script)
* scope (global | project | repo)
* target (chatgpt | claude_code | gemini | cli | repo)

Optional but encouraged:
* triggers
* inputs
* outputs
* owner

## Canonical renames (current)

* deviser_prompt_chatgpt.md -> PROMPT-CHATGPT-PROJECT_INSTRUCTIONS-DEVISER.md
* audizer.md -> REF-AUDIZER_PROTOCOL.md

## Filing semantics

* -INBOX is intake only.
* Stable canon lives in 02-ENGINE or 00-ORCHESTRATION/state depending on scope.
* -OUTGOING is for exports/handoffs and session bundles.
