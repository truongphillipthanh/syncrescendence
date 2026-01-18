# NEXT ACTIONS: SINGLE COMMAND
## Regenerate/Update This Bundle

**Purpose**: Minimal command set to regenerate this teleology bundle in the future
**Generated**: 2026-01-16

---

## I. THE SINGLE COMMAND

To regenerate this bundle with updated inputs:

```bash
claude --model opus "
Execute the following, reading from repo:

1. Create directory: outgoing/TELEOLOGY_RING7_PASS_4_\$(date +%Y%m%d_%H%M)/

2. Read and synthesize:
   - deviser1_continuity.md
   - oracle_memories.md
   - 00-ORCHESTRATION/state/REF-STANDARDS.md
   - 00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md
   - platform_features.md
   - INTERACTION_PARADIGM.md
   - Any outgoing/RING7_* from previous passes

3. Produce updated versions of:
   - 00_INDEX.md
   - 01_DEVISER1_DELETION_PACK.md (update checklist based on current state)
   - 02_RING_MAP_V4_RING7_FIRST.md (incorporate any ring model changes)
   - 03_COCKPIT_CONTRACT_TEMPLATES/ (one per platform)
   - 04_PACKETS_AND_PROTOCOLS_V2.md (update packet schemas if needed)
   - 05_PLATFORM_FEATURE_TELEOLOGY_TABLES.md (refresh with latest features)
   - 06_RING7_SUBSTRATE_BLUEPRINT.md (incorporate learnings)
   - 07_NEXT_ACTIONS_SINGLE_COMMAND.md (increment pass number)

4. Verify all files created.

Prioritize: lossless continuity, deletable threads, Ring 7 as enabling membrane.
"
```

---

## II. WHEN TO REGENERATE

Regenerate this bundle when:

| Trigger | Reason |
|---------|--------|
| Major platform update | Features changed, governance needs update |
| New platform added | Needs cockpit contract |
| Quarterly review | Ensure currency |
| Before deleting significant chat | Capture continuity |
| After major Oracle session | Incorporate decisions |
| Ring model refined | Architecture evolved |

---

## III. VERIFICATION STEPS

After regeneration, verify:

### Files Exist
```bash
ls -la outgoing/TELEOLOGY_RING7_PASS_*_*/
# Should see all 8 deliverables
```

### Content Current
```bash
# Check INDEX references current pass
head -20 outgoing/TELEOLOGY_RING7_PASS_*_*/00_INDEX.md

# Check platform tables have current features
grep -A5 "Extended Thinking" outgoing/TELEOLOGY_RING7_PASS_*_*/05_PLATFORM_FEATURE_TELEOLOGY_TABLES.md
```

### Deletion Pack Valid
```bash
# Check Deviser1 checklist matches current state
cat outgoing/TELEOLOGY_RING7_PASS_*_*/01_DEVISER1_DELETION_PACK.md | grep -A20 "SAFE TO DELETE"
```

### Ring 7 Blueprint Current
```bash
# Check sub-agent roles match actual capabilities
grep -A10 "Seven Roles" outgoing/TELEOLOGY_RING7_PASS_*_*/06_RING7_SUBSTRATE_BLUEPRINT.md
```

---

## IV. EXPECTED OUTPUTS

After successful regeneration:

| File | Size (approx) | Purpose |
|------|---------------|---------|
| 00_INDEX.md | 2-3 KB | Navigation |
| 01_DEVISER1_DELETION_PACK.md | 8-10 KB | Continuity capture |
| 02_RING_MAP_V4_RING7_FIRST.md | 12-15 KB | Architecture |
| 03_COCKPIT_CONTRACT_TEMPLATES/ | 5x 3-5 KB | Platform contracts |
| 04_PACKETS_AND_PROTOCOLS_V2.md | 15-20 KB | Packet specs |
| 05_PLATFORM_FEATURE_TELEOLOGY_TABLES.md | 12-15 KB | Feature governance |
| 06_RING7_SUBSTRATE_BLUEPRINT.md | 15-18 KB | Execution patterns |
| 07_NEXT_ACTIONS_SINGLE_COMMAND.md | 2-3 KB | This file |

**Total**: ~80-100 KB of structured visibility

---

## V. FALLBACK: MANUAL REGENERATION

If the single command fails, regenerate manually:

```bash
# 1. Create directory
mkdir -p "outgoing/TELEOLOGY_RING7_PASS_4_$(date +%Y%m%d_%H%M)"

# 2. Read each input file
cat deviser1_continuity.md
cat 00-ORCHESTRATION/state/REF-STANDARDS.md
# ... etc.

# 3. Write each output file
# Use templates from this bundle as starting points
# Update with current information

# 4. Verify
ls -la outgoing/TELEOLOGY_RING7_PASS_4_*/
```

---

## VI. VERSION HISTORY

| Pass | Date | Major Changes |
|------|------|---------------|
| 1 | (prior) | Initial Ring 7 definitions |
| 2 | 2026-01-16 22:19 | RING7_PHASESHIFT_PASS (6 technical docs) |
| 3 | 2026-01-16 23:30 | TELEOLOGY_RING7_PASS (this bundle, 8 deliverables) |
| 4 | (next) | TBD - regenerate when needed |

---

## VII. COMMIT MESSAGE TEMPLATE

After regenerating:

```bash
git add outgoing/TELEOLOGY_RING7_PASS_*_*/
git commit -m "$(cat <<'EOF'
docs: regenerate teleology Ring 7 bundle (Pass N)

- Updated platform features for [changes]
- Refined ring model for [changes]
- Added/updated cockpit contracts for [platforms]
- Refreshed packet protocols

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
EOF
)"
```

---

**One command regenerates the entire visibility bundle. Use it.**
