# TASK-20260211-KINETIC_LAYER_DATA

**From**: Commander (Claude Code Opus)
**To**: Adjudicator (Codex CLI)
**Reply-To**: commander
**Issued**: 2026-02-11T19:30:00Z
**Fingerprint**: dcfc8e7
**Kind**: TASK
**Priority**: P0
**Status**: SUPERSEDED
**Kanban**: DONE
**Claimed-By**: commander-Lisas-MacBook-Air
**Claimed-At**: 2026-02-11T19:10:00Z
**Completed-At**: 2026-02-11T19:10:00Z
**Exit-Code**: 0
**Resolution**: Kinetic layer data produced by Commander-mini (Opus 4.6) as fallback. All 5 deliverables exist at 00-ORCHESTRATION/state/impl/kinetic/. This re-dispatch is unnecessary.
**Timeout**: 60
**CC**: commander
**Receipts-To**: -OUTBOX/adjudicator/RESULTS
**Escalation-Contact**: commander
**Escalation-Delay**: 10

---

## Objective

Design complete Kinetic Layer data artifacts for PROJ-006b Phase B. You are the coequal data architect for this phase. Commander owns the schema DDL and Python code; you own the precision taxonomy and exhaustive mappings that populate the kinetic tables.

Produce 5 structured markdown files in `00-ORCHESTRATION/state/impl/kinetic/`. Each file contains markdown tables that Commander will parse into Python seed data. Accuracy and coverage matter more than speed.

---

## Context

### Current Ontology State
- 35 tables, 1,591 rows, schema v1.2.0
- 126 apps, 20 AI models, 15 functional roles, 6 apparatus, 45 primitives
- 5 modalities: text, voice, visual, gesture, haptic
- 7 commercial seams, 5 deployment contexts
- Kinetic tables CREATED but EMPTY: action_types, app_actions, agent_bindings

### Constellation Agent Roles (from COCKPIT.md)
| Agent | Role | Platform | Machine | Primary Actions |
|-------|------|----------|---------|----------------|
| Sovereign | CEO | Human | Both | Approve, decide, direct, review |
| Ajna | CSO | Kimi K2.5 (NVIDIA) | MBA | Strategic analysis, dispatch optimization |
| Psyche | CTO | GPT-5.3-codex (OpenClaw) | Mac mini | System cohesion, automation, policy |
| Commander | COO | Claude Opus 4.6 | Mac mini | Multi-tool orchestration, implementation |
| Adjudicator | CQO | Codex CLI (Sonnet) | Mac mini | Precision execution, validation, standards |
| Cartographer | CIO | Gemini 2.5 Pro | Mac mini | Corpus survey, intelligence gathering |

### Design Decision (Sovereign-approved)
Keep existing `roles` table as-is. Create `action_types` as a NEW superset table with optional `parent_role_id` FK back to `roles`.

---

## Deliverable 1: ACTION_TYPES.md

Path: `00-ORCHESTRATION/state/impl/kinetic/ACTION_TYPES.md`

Design the complete action type vocabulary.

Table format:

```
| code | name | category | parent_role | description | input_type | output_type | write_back | requires_approval | automation_level |
```

Column definitions:
- code: snake_case unique identifier
- name: Human-readable name
- category: core | compound | governance | personal
- parent_role: One of 15 existing roles, or blank
- description: What this action does
- input_type: text | data | file | object | signal | mixed
- output_type: What the action produces
- write_back: TRUE if mutates state, FALSE if read-only
- requires_approval: TRUE if Sovereign must approve
- automation_level: manual | assisted | automated | autonomous

Requirements:
1. Start from 15 existing roles as category anchors
2. Expand each role into 2-5 specific verbs (capture -> capture_text, capture_screenshot, capture_audio, capture_url, capture_file; process -> transform_text, extract_entities, summarize, classify; etc.)
3. Add 5-8 compound actions spanning multiple roles (research_synthesize, code_review, clarescence, blitzkrieg_dispatch, metabolize_content)
4. Add 5-8 governance actions (approve, delegate, revoke, sandbox, escalate, gate, audit_trail)
5. Add 5-8 personal actions (commit_to, decline, renegotiate, allocate_attention, set_boundary, recover_energy, prioritize)

Target: 50-70 action types total

---

## Deliverable 2: APP_ACTIONS.md

Path: `00-ORCHESTRATION/state/impl/kinetic/APP_ACTIONS.md`

Map top 40 apps to their supported action types.

Table format:

```
| app_slug | action_code | quality_rating | is_primary | automation_support | notes |
```

Column definitions:
- app_slug: Must match exactly from slug list below
- action_code: Must match exactly from Deliverable 1
- quality_rating: excellent | good | basic | limited
- is_primary: TRUE if BEST app for this action, FALSE otherwise
- automation_support: native | api | mcp | scripted | manual
- notes: Brief clarification

Priority apps (must cover these 40): obsidian, neovim, claude-code, cursor, chatgpt, notion, linear, clickup, git, gh, lazygit, tmux, ghostty, raycast, figma, slack, discord, perplexity, gemini-cli, codex-cli, openclaw, ollama, docker-desktop, ripgrep, fzf, 1password, devonthink, zotero, airtable, keyboard-maestro, hazel, things3, brave-browser, sesh, starship, whisper-cpp, bat, fd, yazi, atuin

Each app: 3-8 action mappings.

Target: 200-320 rows

---

## Deliverable 3: AGENT_BINDINGS.md

Path: `00-ORCHESTRATION/state/impl/kinetic/AGENT_BINDINGS.md`

Map each Constellation agent to their app-action bindings.

Table format:

```
| agent_code | app_slug | action_code | binding_strength | invocation_method | frequency | notes |
```

Column definitions:
- agent_code: sovereign | ajna | psyche | commander | adjudicator | cartographer
- binding_strength: primary | secondary | fallback | experimental
- invocation_method: mcp | cli | api | gui | webhook | dispatch
- frequency: constant | frequent | periodic | rare

Agent profiles:
- Sovereign: GUI interactions, approval/decision. Uses obsidian (gui), brave-browser (gui), slack (gui), things3 (gui), notion (gui)
- Commander: 12 MCP servers, CLI tools. Uses claude-code, git, gh, obsidian (mcp), linear (mcp), clickup (mcp), ripgrep (cli), fzf (cli), tmux (cli)
- Adjudicator: Codex CLI, mechanical execution. Uses codex-cli, git, neovim (cli), ripgrep (cli), fd (cli), bat (cli)
- Cartographer: Gemini CLI, corpus surveys. Uses gemini-cli, ripgrep (cli), fd (cli), obsidian (mcp)
- Psyche: OpenClaw GPT-5.3-codex. Uses openclaw, git (cli), obsidian (mcp via adapter)
- Ajna: OpenClaw Kimi K2.5 on MBA. Uses openclaw-openclaw-mba, git (cli)

Target: 15-25 bindings per agent, 90-150 total

---

## Deliverable 4: MODEL_CAPABILITIES.md

Path: `00-ORCHESTRATION/state/impl/kinetic/MODEL_CAPABILITIES.md`

Map 20 AI models to modality capabilities.

Table format:

```
| model_slug | modality_code | capability_description |
```

Rules:
- Every model gets text. Vision-capable get visual. Voice-capable get voice.
- Embedding models are text-only.

Target: 40-60 rows

---

## Deliverable 5: WORKFLOW_TEMPLATES.md

Path: `00-ORCHESTRATION/state/impl/kinetic/WORKFLOW_TEMPLATES.md`

Templates table:

```
| code | name | description | apparatus_code | use_frequency | avg_duration_minutes |
```

Steps table:

```
| workflow_code | step_number | app_slug | action_description | input_from_previous | output_to_next | avg_duration_minutes | notes |
```

Requirements:
1. Formalize 6 existing apparatus (writing, research, coding, design, analysis, communication)
2. Add 4-6 new: orchestration, sensing, deployment, maintenance, onboarding, clarescence
3. Each workflow: 4-8 steps referencing valid app_slugs

Target: 10-12 templates, 60-80 steps

---

## App Slugs (126)

1password, airtable, alttab, amphetamine, anthropic-claude-chrome-ext, anthropic-claude-code-cli, anthropic-claude-cowork, anthropic-claude-desktop, anthropic-claude-web, api-anthropic-claude-max, api-anthropic-claude-pro, api-chroma, api-clickup, api-github, api-google-ai-pro, api-graphiti, api-homebrew, api-linear, api-neo4j, api-notion, api-nvidia-nim, api-ollama, api-openai-chatgpt-plus, api-openclaw, api-perplexity, api-qdrant, api-setapp, api-tailscale, api-xai-grok, appcleaner, atuin, awscli, bat, bettertouchtool, blender, brave-browser, chatgpt, claude-code, claude-desktop, clickup, codex-cli, cursor, default-folder-x, devonthink, direnv, discord, dockdoor, docker-desktop, elgato-stream-deck, emacs, expressions, eza, fd, ffmpeg, figma, final-cut-pro, forklift, fzf, gcloud, gemini-cli, gh, ghostty, git, github-desktop, google-chrome, google-gemini-cli, google-gemini-mobile, google-gemini-web, google-notebooklm, handbrake, hazel, hookmark, huggingchat, ice, iina, imageoptim, iterm2, jq, karabiner-elements, keyboard-maestro, keyclu, lazygit, linear, logic-pro, maccy, magnet, milanote, mise, neovim, netnewswire, nitro-pdf-pro, notion, obsidian, ollama, openai-chatgpt-desktop, openai-chatgpt-web, openai-codex-cli, openclaw, openclaw-openclaw-mba, openclaw-openclaw-mini, perplexity, perplexity-perplexity-desktop, perplexity-perplexity-web, pixelsnap, presentify, raycast, ripgrep, safari, sesh, setapp, shottr, slack, soulver, starship, tailscale, terraform, things3, tmux, vivaldi, whisper-cpp, xai-grok-web, xcode, yazi, yt-dlp, zotero, zoxide

## Model Slugs (20)

alibaba-qwen-3, anthropic-claude-3-5-haiku-20241022, anthropic-claude-opus-4-6, anthropic-claude-sonnet-4-20250514, anthropic-claude-sonnet-4-5-20250514, deepseek-deepseek-r1, google-gemini-2.0-flash, google-gemini-2.5-flash, google-gemini-2.5-pro, meta-llama-4-maverick, meta-llama-4-scout, mistral-codestral-latest, moonshot-ai-kimi-k2.5, openai-gpt-5, openai-gpt-5.3-codex, openai-o3, openai-o4-mini, openai-text-embedding-3-large, openai-text-embedding-3-small, xai-grok-3

---

## Completion Protocol

1. Write all 5 files to 00-ORCHESTRATION/state/impl/kinetic/
2. Cross-check: every action_code in APP_ACTIONS.md and AGENT_BINDINGS.md exists in ACTION_TYPES.md
3. Cross-check: every app_slug references a valid slug from the list above
4. git add 00-ORCHESTRATION/state/impl/kinetic/ && git commit -m "feat(PROJ-006b): Adjudicator kinetic data artifacts -- 5 deliverables for Phase B"
5. Report results to commander
