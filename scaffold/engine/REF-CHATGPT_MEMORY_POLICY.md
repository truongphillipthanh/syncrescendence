---
id: chatgpt-memory-policy
kind: protocol
scope: project
target: chatgpt
owner: Vanguard
---

# Memory Policy: what goes in Saved Memory vs Project vs Repo

## Principle

Saved Memory is for stable, high-level preferences and invariants. It is not a template store. Anything large, exact, or frequently changing belongs in the repo (and optionally in Project Files for retrieval).

## Saved Memory (global)

Store only durable invariants that reduce renegotiation across all threads, such as:

* Output trifurcation requirement (Readable + Audizable + Directive Pack when executing)
* Your core workflow trigger semantics ("Blitzkrieg" means Context + Pedigree + Directives A/B/C)
* Stable style constraints that matter everywhere

Do NOT store:

* long protocols
* full prompts
* deep research dumps
* lists of paid accounts or tool entitlements that change

## Project Instructions (Syncrescendence project)

Store the behavioral contract and workflow rules. This is the canonical "how we work" statement for the project.

## Project Files (RAG)

Store reference canon that should always be retrievable inside the project:

* Constitution / orchestration model
* Blitzkrieg Protocol vNext
* Audizer Protocol
* Memory Policy (this doc)

## Repo

Store ground truth and archaeology:

* directives, execution logs, evidence packs
* capability ledgers / env manifests
* continuity bundles and reinit capsules

## Capabilities / "env"

Maintain a human-readable capabilities ledger in the repo that answers:
"What tools and paid assets are available right now?"
This belongs in the repo, not in memory.
