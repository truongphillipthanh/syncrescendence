# AGENTS.md
Type: file
First seen: Genesis
Status: active

## What it is
Constitutional law of the constellation (v6.0.0). Defines all agent roles, protocols, dispatch modes, anti-patterns, and operational rules. Source of truth that generates CLAUDE.md and GEMINI.md via `make configs`.

## Relationships
- generates: CLAUDE.md, GEMINI.md (via `make configs`)
- mentions: All 6 agents, OpenClaw, tmux, launchd, Constellation, memsync, AjnaPsyche Archon, Auto-Ingest
- outgoing_edges: 59 in knowledge graph
- references: watch_dispatch.sh, scaffold_validate.sh
- location: repo root `/Users/system/syncrescendence/AGENTS.md`

## Current state
Active. v6.0.0. The single source of constitutional law. 59 outgoing edges make it the most connected file in the graph. All agents inherit it. Must stay synced with Frontier Model Registry in MEMORY.md.
