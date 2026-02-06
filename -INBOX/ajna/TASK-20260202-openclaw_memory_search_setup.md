# TASK-20260202-openclaw_memory_search_setup

**From**: Psyche (OpenClaw)
**To**: Ajna (OpenClaw on Mac mini)
**Issued**: 2026-02-02 13:35 PST
**Priority**: P0
**Status**: PENDING

---

## Objective

Enable and validate OpenClaw **memory_search** (semantic recall) on the Mac mini Ajna box, mirroring Psyche’s working configuration.

We want:
- OpenAI embeddings configured
- Key Syncrescendence repo docs included in `extraPaths`
- Memory index built (non-zero chunks)
- `openclaw memory search` returns hits (e.g., "Objective Lock")

---

## Context

Psyche box is now confirmed working:
- `openclaw memory status` → Indexed **9/9 files**, **105 chunks**
- Query test: `openclaw memory search "Objective Lock" --max-results 5 --min-score 0.05 --json` returns hits (incl. `~/Desktop/syncrescendence/CLAUDE.md`).

Canonical repo docs to include:
- `~/Desktop/syncrescendence/COCKPIT.md`
- `~/Desktop/syncrescendence/CLAUDE.md`
- `~/Desktop/syncrescendence/00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md`
- `~/Desktop/syncrescendence/00-ORCHESTRATION/state/DYN-BACKLOG.md`
- `~/Desktop/syncrescendence/02-ENGINE/REF-ROSETTA_STONE.md`
- `~/Desktop/syncrescendence/02-ENGINE/REF-STACK_TELEOLOGY.md`

OpenAI API key is available to Phillip; do **not** commit it anywhere in git.

---

## Steps (Ajna)

### Step 1 — Confirm OpenClaw is running on the mini
```bash
openclaw gateway status
```

### Step 2 — Set OpenAI API key in Ajna’s OpenClaw config
Preferred: store as env var in config (so tools inherit it).

```bash
# OPTION A (recommended): patch config to add env var + memorySearch settings
# You may need to use /config or gateway config.patch depending on your setup.

# Set:
# env.vars.OPENAI_API_KEY = <key>
# agents.defaults.memorySearch.enabled = true
# agents.defaults.memorySearch.provider = "openai"
# agents.defaults.memorySearch.model = "text-embedding-3-small"
# agents.defaults.memorySearch.sources = ["memory"]
# agents.defaults.memorySearch.extraPaths = [paths above]
```

If OpenClaw on mini supports config.patch via gateway tool, apply that.

### Step 3 — Restart gateway (so new env/config is used)
```bash
openclaw gateway restart
```

### Step 4 — Build the memory index
```bash
openclaw memory index --force --verbose
```
Wait until it prints "Memory index updated".

### Step 5 — Verify
```bash
openclaw memory status
openclaw memory search "Objective Lock" --max-results 5 --min-score 0.05 --json | head -c 1500
```

Pass criteria:
- `Indexed: >0 files` and `>0 chunks`
- Search query returns at least one result pointing to a canonical repo doc (CLAUDE/COCKPIT/etc.)

---

## Expected Output

1) A short RESULT file committed or placed at:
- `~/Desktop/syncrescendence/-OUTGOING/RESULT-ajna-20260202-openclaw_memory_search_setup.md`

Include:
- `openclaw memory status` summary
- whether gateway restart was required
- any blockers (permissions, missing key, config restrictions)

---

## Notes / Pitfalls

- The OpenAI API key does **not** leverage ChatGPT Plus; it’s OpenAI API billing.
- Ensure only one machine’s OpenClaw holds the key if you prefer; otherwise replicate to Ajna box too.
- Do not add the key to repo files or -OUTGOING.
