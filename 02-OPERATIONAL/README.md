# OPERATIONAL Index

## Purpose
Executable components: functions, prompts, protocols, and model configurations. This is the "engine room" of Syncrescendence.

## Directory Structure

### /functions/
Processing functions for content transformation and integration.

**Available functions** (partial list):
- `integrate.md` — Synthesize disparate materials into unified narrative
- `listenize.md` — Transform prompts for audio delivery optimization
- `transcribe_youtube.xml` — Clean YouTube transcripts
- `transcribe_interview.xml` — Polish multi-speaker transcripts
- `readize.xml` — Optimize for visual reading density
- Additional XML functions for various transformations

See `FUNCTION_INDEX.md` for complete catalog.

### /prompts/
LLM prompt templates (currently empty - to be migrated).

### /protocols/
Interaction protocols and handoff procedures.

- `BLITZKRIEG_PROTOCOL.md` — Multi-lane parallel execution framework
- `PROTOCOL-ChatGPT-Onboarding.md` — ChatGPT platform integration
- `PROTOCOL-Gemini-Onboarding.md` — Gemini platform integration

### /models/
Model-specific configurations (currently empty - to be created).

### /memory/
Persistent memory structures (currently empty - to be created).

### /avatars/
Visual identity assets.

## Root-Level Files

### Information Integration Constellation (IIC) Configs
- `IIC-Acumen-config.md` — Acumen node configuration
- `IIC-Coherence-config.md` — Coherence node configuration
- `IIC-Efficacy-config.md` — Efficacy node configuration
- `IIC-Mastery-config.md` — Mastery node configuration
- `IIC-Transcendence-config.md` — Transcendence node configuration
- `IIC-shared-protocols.md` — Cross-node protocols

### Platform Entry Points
- `GEMINI.md` — Gemini-specific instructions and entry point
- `MCP_SETUP.md` — Model Context Protocol setup guide

### Operational References
- `DYN-COORDINATION.yaml` — Multi-Claude zone ownership and routing
- `REF-OPERATIONAL_ENGINE.md` — Operational engine documentation
- `THREAD_HANDOFF_ORACLE13_SUNSET.md` — Thread transition documentation

## Quick Start

1. **Find a function**: Check `/functions/FUNCTION_INDEX.md`
2. **Check protocols**: See `BLITZKRIEG_PROTOCOL.md` for parallel execution
3. **Platform onboarding**: See `PROTOCOL-<Platform>-Onboarding.md`
4. **Multi-Claude coordination**: See `DYN-COORDINATION.yaml`

## TODO: Reorganization Pending

This directory needs structural cleanup:
1. Migrate standalone .md files to appropriate subdirectories
2. Create /models/ structure for model-specific prompts
3. Create /prompts/ templates for common interactions
4. Flatten IIC configs or move to constellation/ subdirectory
5. Consolidate protocol files

See DIRECTIVE-046 and future directives for planned reorganization.

## Development Status

- ✅ Functions library established
- ✅ IIC constellation configured
- ✅ Platform protocols defined
- 🚧 Prompts directory (to be populated)
- 🚧 Models directory (to be created)
- 🚧 Memory structures (to be implemented)
