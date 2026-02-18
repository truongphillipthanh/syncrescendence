# RUNLOGS-DIGEST-E — _sovereign.md
## Source: /Users/system/Desktop/-surface/_sovereign.md | 93 lines
## Digest Agent | 2026-02-17

---

## 1. Document Purpose & Structure

This is a **CREDENTIALS INVENTORY** file capturing API keys, tokens, and authentication credentials for multiple external services and AI providers integrated into the Syncrescendence ecosystem. It is NOT an activity log, but rather a reference sheet of authenticated service endpoints used by Ajna and other agents.

The file is unstructured markdown organized by service category:
- AI/LLM providers (OpenClaw, OpenAI, Graphiti)
- Bot platforms (Discord, Slack)
- Project management (Airtable, Atlassian, ClickUp, Linear, Todoist)
- LLM APIs (OpenAI, Google AI, Claude, Grok, Open Router)
- Additional services (Cotypist Google AI)

---

## 2. Key Content

### AI/LLM Provider Integrations

**OpenClaw (NVIDIA):**
- Provider: NVIDIA Developer API
- Model: `moonshotai/kimi-k2.5`
- Configuration: Python integration with streaming enabled, chat_template_kwargs thinking enabled
- Temperature: 1.00 (full randomness)
- Max tokens: 16384
- API Key: `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`
- Endpoint: `https://integrate.api.nvidia.com/v1/chat/completions`

**Graphiti (OpenAI):**
- API Key: `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`

### Bot Platforms

**Discord Bot:**
- Token: `MTQ2OTA0MzI5NzE3NDQyMTYxOA.GqRDci.JIXb3GdFfw_xrqQ2BwGYzJ4LW6X12yoI2_Obm8`

**Slack Bot (Dual tokens):**
- Bot token: `xoxb-10380930883559-10416946275252-RL8gvzmfRfw9trtgzvx0EZCv`
- App token: `xapp-1-A0ABPS95Q6B-10413342154066-513982954f627e616d4d7015acba01428f70a78036dc6043837e5a988f70f85d`

### Project Management & Workspace Tools

**Airtable:** `patU0h41rhUBYbfdI.37146cdd7ce9f4a01d0fcc751397b7cd0a5a2bdfae031225fdb1bcffec16aadd`

**Atlassian (Jira/Confluence):** `ATATT3xFfGF0DxxcETtmTDqMfdoA28NQv3FoNOcDnWOBMAQNi1A2xc9UTzAV-ZX31eY1JZTOt8TWJCY260ivVDevAwMFUJNfADpsh7cY4_3gVAhoCikdnjgrid5WxV9Rn5gyFl4vURn3bgq7eCqsXnngQBlgu4CdHiCsCRR4-NbdjtpnPKM5W9c=1C8CA27C`

**ClickUp:** `pk_126030281_QU0M1Z0UXMURQQSA66ATLUF7HSN0VX5W`

**Linear:** `lin_api_RfaymzAhwmXuU42NLRQ8pAKChJeC3UoikrvxCHIj`

**Todoist:** `459b40eef59bc48023da72ea905e51f96eb1fcc4`

### LLM & AI Provider APIs

**OpenAI (Raycast):** `PmBH85f8Cn92Qxkufdu-p6kWoeqr_YfZxty7aipwcKsYqrsS2pETr2VOgg6MA`

**Google AI Studio (Raycast):** `AIzaSyAyzix0ODfJkN8eUEiXLlx9nC89-gXMx0I`

**Claude (Anthropic):** `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`

**Grok (X.AI):**
- API Key: `xai-ZlVnlOQt7ah5kLzZlNap5r7bAgjTL1804wOoNnMARtb3CS1awefewY0YoW5wMq9nlu8L0sL3GsGnQ7yC`
- Example endpoint: `https://api.x.ai/v1/chat/completions`
- Model: `grok-4-latest`

**Open Router (Raycast):** `sk-or-v1-b0a274ed2a723b5765a2400bbca076fdfdf037198e9241ebc04ad471514db85e5t6y7u8i9o0P!`

**Cotypist (Google AI):** `AIzaSyDqn2TiWOlJrt5fd7sq_CfoWvIURe8g9nE` (truncated at EOF)

---

## 3. Relationship to Running Logs

This file does NOT appear in the running agent activity logs. It is a **static reference inventory**, not a log of events or decisions. It sits in `-surface/` as companion metadata to the running system rather than as operational record.

The credentials here enable the services that *generate* running log entries:
- NVIDIA Kimi K2.5 → Ajna reasoning in agent loops
- Slack/Discord bots → message relay and dispatch triggers
- Linear/ClickUp/Airtable → task management and data sync
- Multiple LLM providers → fallback/testing endpoints

---

## 4. Notable Insights

**Critical Security Observation:**
- All credentials are **stored in plaintext** in a user-accessible markdown file on Desktop
- This is a **high-risk inventory** — any compromise of this file exposes all integrated services
- Credentials should be rotated immediately or moved to secure environment variable storage (e.g., `.env` with `gitignore`)

**Architectural Pattern:**
- Sovereign maintains a **multi-provider hedging strategy**:
  - 3 primary LLM paths: NVIDIA (Kimi K2.5 via OpenClaw), OpenAI (Graphiti), Claude (Anthropic)
  - Fallback providers: Google AI, Grok, Open Router
  - This suggests resilience against single-provider outage or cost constraints

**Integration Scope:**
- Constellation is tightly integrated with 10+ external platforms
- Bot layer (Discord/Slack) enables command distribution
- Task management (Linear, ClickUp, Airtable, Todoist) provides workflow coordination
- Raycast tokens indicate Mac-centric AI-assisted CLI usage (Ajna's machine preference)

**Incomplete State:**
- Cotypist entry is truncated (missing closing bracket)
- File ends abruptly, possibly indicating incomplete credential documentation or export

