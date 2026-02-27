# Neural Bridge
Type: system
First seen: Genesis
Status: active

## What it is
The SSH bidirectional link between MacBook Air and Mac mini. The constellation's circulatory system. Every cross-machine dispatch, CONFIRM routing, and health check flows through it.

## Relationships
- connects: MBA (Ajna) <-> Mac mini (Psyche, Commander, Adjudicator, Cartographer)
- mba_to_mini: `ssh mini` (key: `~/.ssh/id_ed25519_ajna`)
- mini_to_mba: `ssh macbook-air` (key: `~/.ssh/id_ed25519_ajna_to_psyche`)
- critical_for: dispatch.sh cross-machine SCP sling

## Current state
Active. ICMP ping is BLOCKED by Stealth Mode on both machines — NEVER use ping, always SSH. Connectivity loss is a critical incident. Health check: `ssh -o ConnectTimeout=5 mini hostname`.
