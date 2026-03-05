# Acumen Operators

Operator lane for the Acumen Intelligence Pipeline (Mode 2 extraction path).

This lane provides:

1. feed registry contract and validation
2. deterministic transcript processing primitives
3. triage packet rendering for Gemini Flash
4. Dawn Brief compilation
5. lightweight flow runner scaffold

## Commands

1. initialize registry:
   - `python3 operators/acumen/init_registry.py --seed operators/acumen/channel_seed.example.json --output runtime/acumen/registry.json`
2. validate registry:
   - `python3 operators/acumen/validate_registry.py --registry runtime/acumen/registry.json`
3. validate identity binding (`syncrescendence@gmail.com`):
   - `python3 operators/acumen/identity_binding_probe.py --binding orchestration/state/ACUMEN-IDENTITY-BINDING-CC87.json --strict`
4. deterministic processing:
   - `python3 operators/acumen/deterministic_track.py --input-text <path> --genre Commentary --target-depth Precis --target-polish charitable --output runtime/acumen/out/sample.md`
5. build triage packet:
   - `python3 operators/acumen/build_triage_packet.py --registry runtime/acumen/registry.json --channel-id <id> --video <video.json> --output runtime/acumen/out/triage-packet.md`
6. compile Dawn Brief:
   - `python3 operators/acumen/build_dawn_brief.py --input-jsonl <decisions.jsonl> --output runtime/acumen/out/DAWN-BRIEF.md`
7. run scaffold flow:
   - `python3 operators/acumen/pipeline_flow.py --registry runtime/acumen/registry.json --queue runtime/acumen/triage-decisions.jsonl --out runtime/acumen/out --strict-identity`
