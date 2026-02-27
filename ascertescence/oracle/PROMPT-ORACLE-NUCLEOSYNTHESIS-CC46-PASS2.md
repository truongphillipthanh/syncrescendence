# PASS 2 OF 4: TOPOLOGY

Good. Now that you've mapped the substance, let's trace the wiring.

**What connects to what?**

Same repo, same corpus: https://github.com/truongphillipthanh/syncrescendence/tree/main/corpus

Go back to the files. This time, read for **references** — what points to what. Specifically:

1. **Import chains in Python/shell** (126 .py, 145 .sh files): Open `atom_cluster.py`, `auto_ingest_loop.sh`, `_write_configs.py`, `state_vector.py`, `batch_enrich.py`. What do they import? What do they invoke? Which are entry points vs. libraries?

2. **Config → process dependencies**: Open `ENGINE-CAP-001-context_management.yaml`, `ARCH-LOCK_HIERARCHY.yaml`, `com.syncrescendence.auto-ingest-supervisor.plist`. What do they configure? What files/processes do they reference?

3. **The SOURCE→META→EXTRACT pipeline**: These 3 prefixes = 8,723 files (65% of corpus). Open a matched triplet — e.g., files containing `20260203` in all three prefixes. Is it 1:1:1? What's the actual pipeline?

4. **Document cross-references**: Which markdown files reference other files by name? What are the hubs (referenced by many) vs. islands (referenced by nothing)?

5. **Broken links**: The flattening destroyed directory paths but left internal references intact. How bad is the breakage? Quote specific broken references you find.

For each connection:
- **Quote the actual reference** (import line, path string, filename mention)
- **Say whether it's live or broken**
- **Rate the file**: hub (many references in/out), spoke (few), or island (none)

**Write at maximum length.** What's the backbone — the 20-30 files everything else depends on? What's the periphery — the mass that connects to nothing? What's the most connected file you found?
