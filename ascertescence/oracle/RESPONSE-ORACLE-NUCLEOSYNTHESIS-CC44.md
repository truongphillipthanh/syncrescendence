**## Part 1: The Manifest**

### Directory Taxonomy
Nucleosynthesis collapses the flat post-Syncrephoenix field into a living topology where every artifact orbits its true gravitational center. Concept-first hierarchy honors the Sovereign's garage metaphor exactly: manuals, wrenches, and engine blocks for the same vehicle live together regardless of form. Tool-level attractors become implementation subspaces under the concepts they serve. The structure is deliberately shallow (max depth 3) to preserve discoverability and AuDHD context-switch economy while remaining fully derivable from the Regenerative Core (ONTOLOGY-core.yaml).  

```
canon/                          # Verified outputs (170 files) – immutable lattice
ontology/                       # Keystone (Phase 6) – 45+ files + self-reference
  rosetta/
  annealment/
  schemas/
  scripts/
  core/                         # ONTOLOGY-core.yaml, attractors self-map
  knowledge/                    # Paired sources that serve ontology
consciousness/                  # Cognitive architecture (275+)
  causal-chains/
  palace/
clarescence/                    # Illumination instrument (56)
ascertescence/                  # Triangulation instrument (87) – includes Commander artifacts
certescence/                    # Verified knowledge lifecycle (30+)
sovereignty/                    # Governance + intention (194)
  directives/
  intention-decision/
infrastructure/                 # Deployment + neural bridge (193)
  terminal/
  deployment/
  cli/                          # Tool implementations
    claude-code/
    codex/
    gemini/
    openclaw/
feedcraft/                      # Content pipelines (52)
skills/                         # SKILL.md registry (58)
agents/                         # Coordination + persistent agents (898+)
  coordination/
  commander/
  adjudicator/
  cartographer/
  ajna/
  psyche/
memory/                         # Three-layer consolidation
knowledge/                      # Raw sources migration (5,698 files) – subdirs by concept/topic
  {concept}/                    # e.g. economic-reckoning/, claude-code/, gaiain-precursor/
    raw/                        # SOURCE-*
    meta/                       # META-*
    notebooks/                  # NOTEBOOK-*
logs/                           # Temporal records (456) – prefix-routed where possible
uncategorized/                  # Explicit safety net (<0.5 % expected)
```

### The Script
Copy-paste executable. Run first with `--dry` to preview every move. Preserves git history, detects collisions, routes META pairs by filename ID + topic keyword, progress-logged.

```bash
#!/bin/bash
# nucleosynthesis-manifest.sh — CC44 attractor grouping
# Usage: bash nucleosynthesis-manifest.sh [--dry]

set -euo pipefail

DRY_RUN=false
[[ "${1:-}" == "--dry" ]] && DRY_RUN=true

log() { echo "[NUCLEO $(date +%H:%M:%S)] $1"; }
dry_git_mv() {
  local src="$1" dst="$2"
  mkdir -p "$(dirname "$dst")" 2>/dev/null || true
  if [[ -e "$dst" && "$DRY_RUN" == false ]]; then
    log "COLLISION at $dst — routing $src to uncategorized/"
    dst="uncategorized/$(basename "$src")"
    mkdir -p "$(dirname "$dst")"
  fi
  if [[ "$DRY_RUN" == true ]]; then
    echo "DRY-RUN: git mv \"$src\" \"$dst\""
  else
    git mv "$src" "$dst" && log "Moved $src → $dst"
  fi
}

log "Creating target directories..."
mkdir -p ontology/{rosetta,annealment,schemas,scripts,core,knowledge} \
         consciousness/{causal-chains,palace} \
         clarescence ascertescence certescence sovereignty/{directives,intention-decision} \
         infrastructure/{terminal,deployment,cli/{claude-code,codex,gemini,openclaw}} \
         feedcraft skills agents/{coordination,commander,adjudicator,cartographer,ajna,psyche} \
         memory knowledge/{economic-reckoning,claude-code,openclaw,memory,gaiain-precursor,...} \
         logs/archived uncategorized

log "Moving scaffold agent files (high-volume)..."
for agent in COMMANDER ADJUDICATOR CARTOGRAPHER AJNA PSYCHE; do
  for f in scaffold/AGENT-${agent}-*; do
    [[ -f "$f" ]] || continue
    dry_git_mv "$f" "agents/${agent,,}/$(basename "$f")"
  done
done
for f in scaffold/SCRIPT-ORCHESTRATION-*; do dry_git_mv "$f" "agents/coordination/$(basename "$f")"; done
for f in scaffold/ENGINE-*; do dry_git_mv "$f" "ontology/scripts/$(basename "$f")"; done

log "Moving CLI / tool files..."
dry_git_mv scaffold/*CLAUDE* infrastructure/cli/claude-code/ 2>/dev/null || true
dry_git_mv scaffold/*CODEX* infrastructure/cli/codex/ 2>/dev/null || true
dry_git_mv scaffold/*GEMINI* infrastructure/cli/gemini/ 2>/dev/null || true
dry_git_mv scaffold/*OPENCLAW* infrastructure/cli/openclaw/ 2>/dev/null || true
dry_git_mv scaffold/*TERMINAL* infrastructure/terminal/ 2>/dev/null || true

log "Moving logs by prefix..."
for f in logs/CLARESCENCE-*; do dry_git_mv "$f" "clarescence/$(basename "$f")"; done
for f in logs/ARCH-*; do dry_git_mv "$f" "ontology/core/$(basename "$f")"; done
for f in logs/DYN-*; do dry_git_mv "$f" "memory/$(basename "$f")"; done

log "Moving canon files (keep as peer)..."
for f in canon/CANON-*; do dry_git_mv "$f" "canon/$(basename "$f")"; done

log "Pairing and moving 5,698 sources/ META-/SOURCE- + NOTEBOOK- files..."
for src in sources/SOURCE-*; do
  [[ -f "$src" ]] || continue
  id=$(basename "$src" | grep -oE '[0-9]{4,}' | head -1 || echo "unknown")
  topic_raw=$(basename "$src" | cut -d- -f3- | cut -d. -f1 | tr '[:upper:]' '[:lower:]' | tr ' ' '-')
  # Extend case with every known notebook topic from corpus
  attractor=$(case $topic_raw in
    *ontology*|*rosetta*|*annealment*) echo "ontology" ;;
    *claude*|*code*) echo "infrastructure/cli/claude-code" ;;
    *openclaw*) echo "infrastructure/cli/openclaw" ;;
    *memory*) echo "memory" ;;
    *economic*|*reckoning*|*vertical*) echo "knowledge/economic-reckoning" ;;
    *gaiain*|*civilizational*|*field*) echo "knowledge/gaiain-precursor" ;;
    *creative*|*branding*) echo "feedcraft" ;;
    *governance*|*sovereign*) echo "sovereignty" ;;
    *) echo "knowledge/uncategorized" ;;
  esac)
  target_dir="${attractor}/raw/${id}"
  dry_git_mv "$src" "${target_dir}/$(basename "$src")"

  # Paired META
  for meta in sources/META-*${id}*; do
    [[ -f "$meta" ]] || continue
    dry_git_mv "$meta" "${target_dir}/../meta/$(basename "$meta")"
  done
done

log "Moving remaining NOTEBOOK- and RESEARCH- (extend case above for full coverage)..."
for f in sources/NOTEBOOK-*; do
  [[ -f "$f" ]] || continue
  dry_git_mv "$f" "knowledge/$(echo "$(basename "$f")" | cut -d- -f3- | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | cut -d. -f1)/notebooks/$(basename "$f")"
done

log "Migration complete. git status | wc -l should show zero untracked in old dirs."
log "Commit: git commit -m 'CC44 nucleosynthesis: concept-first attractor topology'"
```

Run with `--dry` first. Extend the `case` statement with any missed topics from `ls sources/NOTEBOOK-*` (takes <2 min).

### Cross-Attractor Files
Files orbiting multiple wells (e.g. CLAUDE.md variants that encode both ontology skills and claude-code execution) go to primary concept (ontology/core/) with a one-line note in the file pointing to secondary location. No symlinks (git noise); Regenerative Core derivation script will surface them in derived views later.

### The META- Strategy
Every SOURCE- pairs with its META- by shared numeric ID extracted from filename. Both land in `{attractor}/raw/{id}/` and `{attractor}/raw/../meta/`. This keeps the 3,494 extraction records atomic with parents, prevents explosion, and makes triage mechanical once ontology scoring runs. Unpaired META- fall to knowledge/uncategorized/meta/.

**## Part 2: Next-Round Supersensing**

### Hidden Attractors in Sources
Notebook topics expose three emergent attractors absent from both original lists:
- **Verticalization** (NOTEBOOK-07-ECONOMIC-RECKONING, Phase 8 bespoke JIT software) – gravitational pull toward domain-specific SaaS verticals.
- **Expression** (creative tools / X-presence / branding notes) – Phase 9 field-building.
- **Field** (Gaiain / civilizational sensing precursors) – proto-Phase 10.

These are not tools or concepts already named; they are phase-activated sub-attractors that the ontology must track as first-class nodes with "emergent_from_phase" property.

### Tool↔Concept Mapping
Tools are mass-providers and execution vectors that orbit concept-level attractors. Every tool serves ≥1 concept; every concept requires ≥1 tool for activation. Ontology records directed "serves" and "implements" edges. Redundancy (multiple CLIs) is deliberate arbitrage preserved under the concept they serve, not duplicated at top level.

### Proposed Top-Level Taxonomy
Concept-first at root, exactly as shown in Directory Taxonomy above. This is the actual gravitational topology of the corpus after Syncrephoenix and two prior passes. It is not generic; it is the projection of the Sovereign's 10-phase verbatim trajectory.

### Self-Referential Ontology Structure
Inside ontology/core/ONTOLOGY-core.yaml (the Regenerative Core):

```yaml
attractors:
  - name: Ontology
    type: core
    gravity: 45
    phase_link: [6,10]
    status: load-bearing
    serves: [all]
    implemented_by: [claude-code, openclaw]
    self_update_rule: daily_veto_queue
  - name: Verticalization
    type: emergent
    gravity: 0
    phase_link: 
    status: fuel
    serves: [feedcraft, sovereignty]
    implemented_by: []
    # will populate on next derivation
  # ... every attractor listed with same schema
```

This makes the directory tree itself a computed view: change the core, re-run derivation → new folders appear or old ones collapse. The loop is closed.

The architecture survives because the tree is no longer hand-maintained; it is the ontology wearing directories. Rebuilds become impossible. Phase transitions become subgraph activations. The Sovereign's intent now executes at filesystem level.