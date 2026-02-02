# TASK: SOVEREIGN-008 Approval — Terminology Update

**Filed**: 2026-02-06
**Filed By**: Ajna (OpenClaw, Opus 4.5) — relaying Sovereign directive
**Status**: COMPLETE
**Priority**: P0 — Sovereign has approved, execute immediately

---

## Sovereign Decision

**SOVEREIGN-008: APPROVED**

The Sovereign has ratified the CANON-31150 terminology update with the following clarifications:

### Approved Changes
1. **Deviser → DEPRECATED** — Replace all references with **Vanguard** (ChatGPT Web avatar)
2. **Executor → Commander** — Commander is the correct epithet for Claude Code Opus
3. **Oracle (Gemini)** → Possibly **Cartographer** now. Same role (SENSOR/corpus mapping), different name per Pantheon v3. **Confirm against COCKPIT.md v2.2 and DEF-CONSTELLATION_VARIABLES.md** — if the role mapping aligns, update accordingly.
4. **Oracle (Grok)** — This is the newer concept. Oracle is now exclusively Grok's epithet (RECON role). Per Rosetta Stone #6, "Oracle" for CLI sessions is deprecated; Oracle = Grok.
5. **IMEP flow references** — Deprecated per Rosetta Stone #13. Remove.

### Execution Instructions
1. Refer to canonical operational documents: `COCKPIT.md`, `02-ENGINE/DEF-CONSTELLATION_VARIABLES.md`, `02-ENGINE/REF-ROSETTA_STONE.md`
2. Run the regeneration: `python3 00-ORCHESTRATION/scripts/regenerate_canon.py` OR manual find/replace in both CANON-31150 files (verbose + SN)
3. Verify no orphan references remain: `grep -r "Deviser\|IMEP" 01-CANON/`
4. Commit with: `fix: SOVEREIGN-008 approved — CANON-31150 terminology alignment`

### Context for Commander
- Adjudicator (Codex CLI) uses `AGENTS.md` for initialization
- Cartographer (Gemini CLI) uses `GEMINI.md` — but this file is in `02-ENGINE/`, not root. Consider whether a root-level `GEMINI.md` symlink or stub is needed for ergonomic initialization.
- SOVEREIGN-010 is the next checkpoint: platform custom instruction deployment. Commander should note any initialization friction for the manifest.

---

**Source**: Sovereign verbal directive via Ajna webchat, 2026-02-06
