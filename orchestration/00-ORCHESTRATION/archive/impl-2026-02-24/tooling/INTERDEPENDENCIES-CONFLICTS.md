# Tooling Interdependencies & Conflicts (Holism Pass)

> Purpose: surface *cross-cutting interdependencies*, *duplications*, and *protocol conflicts* across `orchestration/scripts/*`, Makefile targets, and CANON-30300 Tech Stack DB ambitions.
> This is a synthesis artifact for Ajna/Commander to implement against.

Generated: 2026-02-04

---

## 1) Duplicate / Competing “intelligence DB” surfaces

### Observation
- `orchestration/scripts/model_db.py` implements a **SQLite DB** at:
  - `orchestration/state/model_intelligence.db`
  - It explicitly claims: “Pilot implementation of CANON-30300 TechStackDB schema (subset).”
- `CANON-30300-TECH_STACK-comet-INTELLIGENCE.md` specifies a broader **Tech Stack DB** schema (`apps`, `models`, `api_pricing`, etc.).

### Conflict
- Risk of **two parallel DBs** for overlapping domains (models + pricing + routing), with diverging truth semantics.

### Dependency / Decision needed
- Decide whether:
  1) `model_db.py` becomes the official Tech Stack DB implementation *for the models slice*, or
  2) Tech Stack DB supersedes model_db and model_db becomes a thin CLI layer over it, or
  3) They remain separate with explicit boundary + export/import contract.

### Recommended resolution
- Define a **Truth Surface Decision** (DecisionAtom):
  - Canonical source for models/pricing/routing (markdown? csv? sqlite?)
  - Refresh cadence + regeneration trigger
  - Artifact locations + ownership

---

## 2) Dispatch protocol vs watcher protocol (metadata + lifecycle)

### Observation
- `dispatch.sh` writes task files with fields:
  - From/To/Issued/Fingerprint/Priority/Status/Timeout
  - Status starts `PENDING`
  - Also appends ledger event if `append_ledger.sh` exists
- `watch_dispatch.sh` only processes `TASK-*.md` where `Status.*PENDING` matches.
- `watch_dispatch.sh` claim-locks by renaming:
  - `TASK-...md` → `TASK-...md.claimed-by-<agent>-<hostname>`
  - It does **NOT** modify the internal `Status:` line.
- `triage_inbox.sh` *also* looks for:
  - internal `Status.*(PENDING|IN_PROGRESS)` and also file suffixes `.claimed-by-*`, `.complete`, `.failed`.
- `triage_outgoing.sh` looks for internal `Status.*(PENDING|IN_PROGRESS)` via ripgrep/grep and does not summarize claim-lock suffixes.

### Conflict
- “Lifecycle truth” is split across **(a) file rename suffixes** and **(b) internal Status field**.
- A claimed task still reads as `Status: PENDING` in the file body, so text-based greps can be misleading.
- `triage_outgoing.sh` will miss claimed tasks that are not greppable as IN_PROGRESS.

### Recommended resolution
- Make watcher update internal status on claim:
  - On claim, set `Status: IN_PROGRESS` and add `Claimed-By:` + timestamp.
  - On complete/fail, set `Status: COMPLETE/FAILED` in-body *before* suffix rename.
- Standardize triage output as a single report artifact (see §6).

---

## 3) CLI handler assumptions inside watchers

### Observation
`watch_dispatch.sh` routes to:
- `claude -p` (commander)
- `codex` (adjudicator)
- `gemini` (cartographer)
- `openclaw agent --local -m` (psyche/ajna)

### Conflict
- `openclaw agent --local -m` may not be stable/portable across machines; OpenClaw’s actual CLI surface may differ by install version.
- Failure mode: watcher “processes” but does nothing useful; still renames tasks to `.failed` with limited diagnostics.

### Recommended resolution
- Add a `--dry-run` and `--check` mode for watchers.
- Add a preflight check:
  - verify required CLIs exist (`command -v ...`)
  - write explicit error to a `-OUTGOING/RESULT-*` file if missing
- Decide whether OpenClaw should be invoked via:
  - gateway session injection (preferred) vs one-shot local CLI.

---

## 4) Ledger protocol is opportunistic, not mandatory

### Observation
- `dispatch.sh` appends ledger DISPATCH iff `append_ledger.sh` exists + executable.
- `watch_dispatch.sh` appends CLAIM/COMPLETE/FAILED if `append_ledger.sh` exists.

### Conflict
- Ledger becomes non-deterministic across environments, undermining “ledger is mandatory.”

### Recommended resolution
- Treat ledger append as **hard requirement** for dispatch/watch paths:
  - If ledger append fails, either:
    - fail loudly (exit non-zero), or
    - write a local warning artifact and mark the task as `FAILED` with reason.

---

## 5) Worktree naming + branch policy drift

### Observation
- `setup-worktrees.sh`:
  - ensures `develop` branch
  - creates worktrees: `syncrescendence-alpha`, `-beta`, `-gamma`
  - creates branches: `alpha/work`, `beta/work`, `gamma/work`

### Conflict
- Tranche A requires: “worktree isolation as canonical parallel execution mechanism for Blitzkrieg,” but naming/branching constraints are not yet ratified.
- Potential conflict with any future sigma/tau terminology, or Neo-Blitzkrieg pipe naming.

### Recommended resolution
- Produce a single canonical spec for:
  - allowed base branches (main vs develop)
  - worktree directory naming
  - branch naming conventions
  - merge/rebase policy
  - whether agents share branches or always fork

---

## 6) Triage observability surfaces are split

### Observation
- `make triage` runs `triage_outgoing.sh` (pipe status + grep)
- `triage_inbox.sh` provides a better lifecycle view but is not wired into Make.

### Recommended resolution
- Create a unified triage report generator that:
  - prints a human summary
  - writes `orchestration/state/DYN-TRIAGE_REPORT.md` (append-only per run)
  - includes: claimed tasks, staleness, pending prompts, pending sovereign briefs.

---

## 7) CANON regeneration log hardcodes CANON IDs

### Observation
- `watch_canon.sh` uses a template registry to build watch paths.
- But `append_regen_log()` writes a table row with CANON IDs hardcoded to `31150`.

### Conflict
- If multiple CANON templates regenerate, the log becomes incorrect.

### Recommended resolution
- Modify regenerate script to return the list of CANON IDs regenerated, and log them.

---

## 8) Lint scope too narrow for drift prevention

### Observation
- `ops_lint.sh` only checks PROMPT/REF files in `engine/` maxdepth=1.

### Conflict
- Drift can occur in DYN + CANON artifacts and templates without detection.

### Recommended resolution
- Expand lint targets to include:
  - `orchestration/state/*.md` (DYN)
  - critical templates/registry files
  - `canon/*.md` frontmatter integrity (at least required keys)

---

## 9) Verify suite checks vs Makefile help text

### Observation
- `Makefile verify` and `verify_all.sh` overlap but differ (expected root md <=3 vs <=2; message mismatch).

### Recommended resolution
- Normalize expectations + messages:
  - decide allowed root md files count and list explicitly.
  - unify verify output format.

---

## Actionable interdependencies (graph-style)

- D-001..D-006 (Tech Stack DB) depends on resolving **(1) model_db boundary**.
- D-008/D-009/D-010 depend on standardizing **(2) lifecycle truth** and **(4) ledger mandatory**.
- A-004 (worktrees canonical) depends on resolving **(5) naming + branch policy**.
- B-012 (ledger mandatory) is blocked until watcher/dispatch scripts treat ledger as required.
- B-021 (registry/index) should incorporate **(6) triage report** + **(7) canon regen log** adjustments.
