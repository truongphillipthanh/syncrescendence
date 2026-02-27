# TASK: IIC Configuration Consolidation

**Priority**: P2
**Reply-To**: commander
**CC**: commander
**Created**: 2026-02-09

## Objective
Consolidate the 5 separate IIC (Initial Instruction Configuration) files in engine/ into:
1. A single `TEMPLATE-IIC.md` with parameterized fields
2. A `DYN-IIC_REGISTRY.yaml` mapping agent → config values

## Current Files to Consolidate
Search engine/ for files matching `IIC-*` or `*IIC*` pattern.

## Acceptance Criteria
- [ ] Single template covers all agent configurations
- [ ] YAML registry maps agent names to their specific values
- [ ] Original files archived to `orchestration/archive/`
- [ ] No information lost in consolidation
- [ ] Verify with grep that no other files reference the old IIC paths

## Context
Part of Epic 1: Live Intelligence Substrate. The engine directory has 108 files with significant overlap. This consolidation reduces cognitive load and enables programmatic IIC generation.
DISPATCH_FAILED: Agent rejected or structurally blocked
