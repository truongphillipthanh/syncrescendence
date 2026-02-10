# SOVEREIGN-013: OpenClaw Personality/Model Mismatch

**Status**: PENDING
**Priority**: P1
**Date**: 2026-02-09
**From**: Commander (Deep Audit)

---

## Finding

`~/.openclaw/SOUL.md` says "You are Ajna" (CSO personality) but `~/.openclaw/openclaw.json` has `model: openai-codex/gpt-5.2` (Psyche's model, running on Mac mini).

Session 6 "transition" changed SOUL/AGENTS/HEARTBEAT/USER/MEMORY.md personality files to Ajna but did NOT change the model in openclaw.json. Result: Mac mini OpenClaw instance has Ajna's personality but Psyche's model.

## Options

### A. Revert personality to Psyche (Recommended)
- Change SOUL.md back to "You are Psyche, the Synaptarch..."
- Mac mini OpenClaw = Psyche/CTO with GPT-5.3-codex (correct pairing)
- Ajna exists on MBA only, once configured

### B. Switch model to NVIDIA NIM for Ajna
- Change openclaw.json model to Kimi K2.5 via NVIDIA NIM
- Mac mini OpenClaw = Ajna/CSO with Kimi K2.5
- Psyche has no home until MBA is configured

### C. Two OpenClaw instances on Mac mini
- Run Psyche on port 18789 (existing) with GPT-5.3-codex
- Run Ajna on port 18790 with NVIDIA NIM
- Both on Mac mini temporarily until MBA is ready

### Commander Recommendation
Option A — revert personality to Psyche. The Mac mini is Psyche's machine. Ajna belongs on MBA. Running Ajna on the wrong machine creates confusion. Once MBA is configured, Ajna gets its own OpenClaw instance there.

---

*Filed by Commander as part of Deep Audit 2026-02-09*
