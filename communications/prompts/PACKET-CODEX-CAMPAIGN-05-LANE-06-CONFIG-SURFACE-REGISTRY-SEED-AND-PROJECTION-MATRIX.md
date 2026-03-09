# Dispatch Packet

**Packet ID**: `PKT-20260309-codex-campaign-05-lane-06-config-surface-registry-seed-and-projection-matrix`
**Surface**: `codex_parallel_session`
**Role**: `direct_write`
**Date**: `2026-03-09`
**Objective**: make the new config kernel machine-addressable through a seed registry and projection matrix
**Priority**: `high`
**Target**: `the first operational config-surface registry layer`
**Origin lane**: `communications/prompts`
**Expected response**: `communications/responses/RESPONSE-CODEX-CAMPAIGN-05-LANE-06-CONFIG-SURFACE-REGISTRY-SEED-AND-PROJECTION-MATRIX.md`

## Required Output

1. create `orchestration/state/registry/CONFIG-SURFACE-REGISTRY-v1.json`
2. create a projection matrix artifact that binds atom families and surface classes to concrete shell surfaces
3. keep the registry seed small and lawful rather than exhaustive
4. run `git diff --check`
5. report `complete / partial / blocked`
