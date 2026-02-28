# Extraction: SOURCE-20260206-004

**Source**: `SOURCE-20260206-x-article-elevenlabsdevs-let_your_openclaw_call_you_on_the_phone_using_elevenagents.md`
**Atoms extracted**: 7
**Categories**: praxis_hook

---

## Praxis Hook (7)

### ATOM-SOURCE-20260206-004-0001
**Lines**: 23-26
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To enable an OpenClaw bot to initiate phone calls, install ElevenLabs skills globally using `npx skills add elevenlabs/skills`.

### ATOM-SOURCE-20260206-004-0002
**Lines**: 29-32
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> After installing ElevenLabs skills, navigate to the OpenClaw dashboard (`openclaw dashboard`), go to the skills tab, find "agents," and input your ElevenLabs API key.

### ATOM-SOURCE-20260206-004-0003
**Lines**: 34-35
**Context**: method / limitation
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> For enhanced security, create an ElevenLabs API key with a scope limited to "agents-write" and a reasonable spend limit.

### ATOM-SOURCE-20260206-004-0004
**Lines**: 40-42
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To make an OpenClaw bot initiate a call, instruct it with `Call <your phone number> using agents skill`.

### ATOM-SOURCE-20260206-004-0005
**Lines**: 54-57
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> After a successful call, instruct OpenClaw to remember the Agent ID and Outbound Phone ID by saying `Put these IDs in your memory` to enable autonomous future calls.

### ATOM-SOURCE-20260206-004-0006
**Lines**: 60-62
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> To ensure all calls share a single OpenClaw agent instance and its context, provide an `x-openclaw-session-key` header to your custom LLM.

### ATOM-SOURCE-20260206-004-0007
**Lines**: 67-69
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To enable autonomous calls from your OpenClaw agent based on specific triggers, add a cron job in the OpenClaw UI or instruct the bot to set it up.
