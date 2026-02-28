# Extraction Pipeline
Type: concept
First seen: DC-208/209 (Phase 2C)
Status: active

## What it is
The source mining and atomic extraction system. Uses `source_extract.py` and `PROMPT-SOURCE_EXTRACTION_ATOMIC.md` to process raw sources into decision atoms. Part of Phase 2C (content decruft + source mining). Achieved 14,311 atoms from 1,152 sources with 0 failures.

## Relationships
- implements: DC-208 (source mining), DC-209 (extraction model routing)
- script: source_extract.py
- prompt: engine/02-ENGINE/PROMPT-SOURCE_EXTRACTION_ATOMIC.md
- reviewed_by: Adjudicator (DC-208 code review), Oracle (DC-209 routing), Diviner (DC-208 synthesis)
- feeds: praxis/, canon/

## Current state
Complete for Phase 2C. All 9 components built. Quality gate (6) and cluster (3) components are P1 but not blocking. 14,311 atoms extracted, 1,152 sources processed. The pipeline is the primary content-to-knowledge transformation mechanism.
