# PACKET-MANUS-cc88-full-migration-four-account-topology

You are executing exocortex/control-plane migration planning and constrained execution for Syncrescendence.

## Objective

Drive full migration progress using the 4-account topology below, with explicit split between:

1. what Manus can execute now
2. what requires human auth/owner-confirmation windows

## Account topology (authoritative)

1. `syncrescendence@gmail.com`  
   target control-plane owner
2. `truongphillipthanh@icloud.com`  
   legacy break-glass
3. `icloud.truongphillipthanh@gmail.com`  
   billing anchor / constrained paid-plan holder
4. `truongphillipthanh@gmail.com`  
   optional personal secondary

## Current posture

1. Acumen canonical identity gate is now green on local host.
2. Repo-side identity cutover framework exists (CC81/CC82/CC83/CC86 lines).
3. Manus API is reachable and can execute backend tasks.

## Guardrails (strict)

1. Do not request broad keychain export or plaintext secret dumps.
2. Assume owner mutations still require human interaction.
3. Preserve rollback path at every wave.
4. Use official docs and platform-native workflows only.

## Required outputs

1. `EXECUTION-READY-MIGRATION-MATRIX`
   - columns: `platform`, `can_manus_execute_now`, `human_action_required`, `credential_surface`, `rollback`, `evidence_required`
2. `WAVE-BY-WAVE-CEREMONY`
   - wave0..wave4 with exact gates, order, and anti-lockout checks
3. `HUMAN-AUTH-WINDOW-SCRIPT`
   - exact script for the operator during each owner transfer / OAuth / token rotation step
4. `MANUS-RUN-BATCH`
   - concrete task batch Manus should run immediately after each human window closes
5. `FAILURE-MODES-AND-RECOVERY`
   - top failure modes and deterministic recovery actions
6. `COMPLETION-DEFINITION`
   - clear done criteria for each platform + global migration done criteria

## Success condition

Return a migration package that can be executed immediately without additional architecture work, while remaining compliant with no-broad-secret-delegation boundary.
