# Refined Symbolic Compression Rules

## Purpose
Ensure no meaning loss when archiving or deleting obsolete or duplicate artifacts.

## Required Fields (Header)
Each ARCH- file must include:
- Archived From: absolute repo path
- Archived On: YYYY-MM-DD
- Superseded By: path or N/A
- Compression Source: defrag run id

## Required Sections
1. ESSENCE (2-4 sentences)
2. KEY DECISIONS RECORDED (bulleted, or "None")
3. INTEGRATION RECORD (where value moved)
4. RETRIEVAL (git log + git show guidance)
5. OBSOLESCENCE REASON (specific, not generic)

## Quality Gates (must pass before deleting original)
- All required fields present
- Essence stands alone without original
- At least one retrieval command works
- References updated for any moved targets

## Special Cases
- Version chains (ORACLE10_CONTEXT v1-v4):
  - Add "Superseded By: ORACLE10_CONTEXT_FINAL.md"
  - Note unique deltas vs FINAL if any
- Session continuity artifacts (previous_thread, deviser1_continuity, oracle_memories):
  - Record explicit handoff data captured
  - Note whether content was integrated into ORACLE contexts
- Directives losers (043A/043B if archived):
  - Include renumbered destination or archive rationale
  - Record any governance decisions that caused renumbering

## Detritus Exception
- Pure detritus (.DS_Store, .tmp.driveupload/) can be deleted without compression.

## Update Index
- compression_index.md must be updated with status, location, and completion date for each compressed file.
