#!/usr/bin/env python3
"""
Nucleosynthesis — CC45 comprehensive concept-first file routing.

Compiled from Oracle Passes 1-3 (CC44-CC45), validated against actual repo state.
Moves ~7,500 files from flat directories (scaffold/, sources/, logs/) into
concept-first attractor directories.

Usage:
    python3 nucleosynthesis.py --dry     # Preview all moves, no changes
    python3 nucleosynthesis.py           # Execute all moves
    python3 nucleosynthesis.py --phase scaffold  # Only process scaffold/
    python3 nucleosynthesis.py --phase sources   # Only process sources/
    python3 nucleosynthesis.py --phase logs      # Only process logs/
    python3 nucleosynthesis.py --phase cleanup   # Only process engine/orchestration/memory/
"""

import sys
import os
import subprocess
from pathlib import Path
from datetime import datetime

DRY_RUN = "--dry" in sys.argv
PHASE = None
for i, arg in enumerate(sys.argv):
    if arg == "--phase" and i + 1 < len(sys.argv):
        PHASE = sys.argv[i + 1]

STATS = {"moved": 0, "skipped": 0, "collision": 0, "error": 0}

def log(msg: str) -> None:
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[NUCLEO {ts}] {msg}")

def git_mv(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        # Collision — append suffix
        stem = dst.stem
        suffix = dst.suffix
        counter = 2
        while dst.exists():
            dst = dst.parent / f"{stem}_{counter}{suffix}"
            counter += 1
        log(f"COLLISION resolved: {src.name} → {dst.name}")
        STATS["collision"] += 1

    if DRY_RUN:
        print(f"  DRY: {src} → {dst}")
        STATS["moved"] += 1
        return

    try:
        result = subprocess.run(
            ["git", "mv", str(src), str(dst)],
            capture_output=True, text=True, check=True
        )
        STATS["moved"] += 1
    except subprocess.CalledProcessError as e:
        log(f"ERROR git mv {src} → {dst}: {e.stderr.strip()}")
        STATS["error"] += 1


# ═══════════════════════════════════════════════════════════
# TARGET DIRECTORY STRUCTURE
# ═══════════════════════════════════════════════════════════

TARGET_DIRS = [
    # Agents
    "agents/commander", "agents/adjudicator", "agents/cartographer",
    "agents/ajna", "agents/psyche", "agents/coordination",
    "agents/coordination/workflows",
    # Ontology
    "ontology/scripts", "ontology/rosetta", "ontology/annealment",
    "ontology/schemas", "ontology/core", "ontology/knowledge",
    "ontology/knowledge/references",
    # Consciousness
    "consciousness/capabilities",
    # Certescence
    "certescence",
    # Clarescence
    "clarescence",
    # Sovereignty
    "sovereignty/directives", "sovereignty/intention-decision",
    # Infrastructure
    "infrastructure/deployment", "infrastructure/terminal",
    "infrastructure/cli", "infrastructure/cli/claude-code",
    "infrastructure/cli/openclaw", "infrastructure/cli/codex",
    "infrastructure/cli/gemini",
    # Feedcraft
    "feedcraft/scripts",
    # Skills
    "skills",
    # Memory
    "memory-new",  # Temporary name to avoid collision with existing memory/
    # Knowledge
    "knowledge/processed", "knowledge/assets", "knowledge/uncategorized",
    "knowledge/uncategorized/notebooks",
    # Logs
    "logs/archived",
    # Uncategorized
    "uncategorized",
]

# Notebook topic → knowledge subdirectory
NOTEBOOK_TOPICS = {
    "AGENT-MEMORY-SYSTEMS": "memory-new",
    "AGENT-SECURITY-HARDENING": "infrastructure",
    "AGENTIC-NOTETAKING-KNOWLEDGE-VAULTS": "memory-new",
    "AI-ENGINEERING-ROADMAPS-ARCHITECTURE": "ontology",
    "CLAUDE-CODE-COWORK-POWER-PATTERNS": "infrastructure/cli/claude-code",
    "DESIGN-IN-AI-ERA": "consciousness",
    "ECONOMIC-RECKONING-SAAS-LABOR-SOCIETY": "knowledge/economic-reckoning",
    "HOMELAB-INFRASTRUCTURE": "infrastructure",
    "MULTI-AGENT-ORCHESTRATION-SWARMS": "agents/coordination",
    "OPENCLAW-ARCHITECTURE-SETUP": "infrastructure/cli/openclaw",
    "OPENCLAW-DEEP-RESEARCH-CONSTELLATION": "agents",
    "PHILOSOPHICAL-WILDCARDS-CULTURAL-COMMENTARY": "consciousness",
    "PROMPT-ENGINEERING-SKILLS-CRAFT": "skills",
    "VIBE-CODING-SOFTWARE-ABUNDANCE": "skills",
}


def route_scaffold(name: str) -> str:
    """Route a scaffold/ file to its target directory."""
    n = name

    # --- AGENT- prefix (878 files) ---
    if n.startswith("AGENT-COMMANDER-"):
        return "agents/commander"
    if n.startswith("AGENT-ADJUDICATOR-"):
        return "agents/adjudicator"
    if n.startswith("AGENT-CARTOGRAPHER-"):
        return "agents/cartographer"
    if n.startswith("AGENT-AJNA-"):
        return "agents/ajna"
    if n.startswith("AGENT-PSYCHE-"):
        return "agents/psyche"
    if n.startswith("AGENT-"):
        return "agents/coordination"  # Any remaining AGENT- files

    # --- SCRIPT-LEGACY- prefix ---
    if n.startswith("SCRIPT-LEGACY-"):
        return "infrastructure"

    # --- SCRIPT-ROOT- prefix ---
    if n.startswith("SCRIPT-ROOT-"):
        return "infrastructure/terminal"

    # --- SCRIPT-ORCHESTRATION- prefix (182 files) ---
    if n.startswith("SCRIPT-ORCHESTRATION-"):
        rest = n[len("SCRIPT-ORCHESTRATION-"):]
        # Feedcraft scripts
        if rest.startswith(("protease_", "atom_cluster", "pipeline_",
                            "batch_enrich", "batch_transcribe",
                            "bead_tracker", "cluster_engine",
                            "source_intake", "triage")):
            return "feedcraft/scripts"
        # Ontology scripts
        if rest.startswith(("ontology_", "build_ontology", "build_url_index")):
            return "ontology/scripts"
        # Memory / session
        if rest.startswith(("session_", "brief_", "state_vector",
                            "circadian_sync", "compact_wisdom",
                            "memsync", "journal")):
            return "memory-new"
        # Infrastructure / terminal / launchd
        if rest.startswith(("launchd_", "boot_", "com.syncrescendence",
                            "cockpit", "auto_ingest", "run_",
                            "LAUNCHD", "sn_", "mba_", "deploy")):
            return "infrastructure/terminal"
        # Config / build
        if rest.startswith(("_write_configs", "CLAUDE-", "config",
                            "build_", "scaffold_", "verify_",
                            "Makefile")):
            return "infrastructure"
        # Agent coordination
        if rest.startswith(("dispatch", "watch_dispatch", "sync_",
                            "commander_special", "ajna_pedigree",
                            "create_execution", "intent_compass",
                            "append_ledger", "autonomy_ledger",
                            "cc_handoff")):
            return "agents/coordination"
        # Certescence
        if rest.startswith(("ascertescence_relay",)):
            return "certescence"
        # Skills
        if rest.startswith(("youtube_", "chroma_", "graphiti_",
                            "GRAPHITI", "audit_")):
            return "skills"
        # Candidate / adapter
        if rest.startswith(("candidate_adapter",)):
            return "ontology/scripts"
        # Fallback: agents/coordination
        return "agents/coordination"

    # --- ENGINE- prefix (173 files) ---
    if n.startswith("ENGINE-"):
        rest = n[len("ENGINE-"):]

        # ENGINE-REF- (35 files) — complex routing
        if rest.startswith("REF-"):
            ref_rest = rest[len("REF-"):]
            if "ROSETTA" in ref_rest.upper():
                return "ontology/rosetta"
            if "ANNEALMENT" in ref_rest.upper() or "PALANTIR" in ref_rest.upper():
                return "ontology/annealment"
            if "STACK" in ref_rest.upper() and "TELEOLOGY" in ref_rest.upper():
                return "ontology/schemas"
            if "AUDIZER" in ref_rest.upper():
                return "infrastructure/cli"  # Pass 3 correction
            if "FLEET" in ref_rest.upper():
                return "agents/coordination"  # Pass 3 correction
            return "ontology/knowledge/references"

        # ENGINE-PROMPT- (35 files)
        if rest.startswith("PROMPT-"):
            if "ORACLE" in rest.upper():
                return "ascertescence/oracle"
            if "DIVINER" in rest.upper():
                return "ascertescence/diviner"
            if "ADJUDICATOR" in rest.upper():
                return "ascertescence/adjudicator"
            return "ascertescence"

        # ENGINE-FUNC- (28 files)
        if rest.startswith("FUNC-"):
            return "ontology/scripts"

        # ENGINE-DYN- (20 files)
        if rest.startswith("DYN-"):
            return "memory-new"

        # ENGINE-CERTESCENCE- (15 files)
        if rest.startswith("CERTESCENCE-"):
            return "certescence"

        # ENGINE-AVATAR- (8 files)
        if rest.startswith("AVATAR-"):
            return "agents"

        # ENGINE-QUEUE- (7 files)
        if rest.startswith("QUEUE-"):
            return "agents/coordination"

        # ENGINE-IIC- (6 files) — Pass 3: confirmed ontology
        if rest.startswith("IIC-"):
            return "ontology"

        # ENGINE-CAP- (5 files) — Pass 3: consciousness/capabilities
        if rest.startswith("CAP-"):
            return "consciousness/capabilities"

        # ENGINE-TOOL- (4 files)
        if rest.startswith("TOOL-"):
            return "skills"

        # ENGINE-TEMPLATE- (3 files)
        if rest.startswith("TEMPLATE-"):
            return "certescence"

        # ENGINE-PROTO- (2 files)
        if rest.startswith("PROTO-"):
            return "ontology"

        # ENGINE-SURVEY- (2 files) — Pass 3: confirmed sovereignty
        if rest.startswith("SURVEY-"):
            return "sovereignty"

        # ENGINE-WF- (1 file) — Pass 3: agents/coordination/workflows
        if rest.startswith("WF-"):
            return "agents/coordination/workflows"

        # ENGINE-MODEL- (1 file)
        if rest.startswith("MODEL-"):
            return "infrastructure/cli"

        # ENGINE-DEF- (1 file — constellation variables)
        if rest.startswith("DEF-"):
            return "agents/coordination"

        return "uncategorized"

    # --- PRAXIS- (34 files) ---
    if n.startswith("PRAXIS-"):
        return "skills"

    # --- CONFIG- (5 files) ---
    if n.startswith("CONFIG-"):
        return "infrastructure"

    # --- CONSTELLATION- (7 files) ---
    if n.startswith("CONSTELLATION-"):
        return "agents/coordination"

    # --- COLLAB- (11 files) ---
    if n.startswith("COLLAB-"):
        return "agents/coordination"

    # --- TEMPLATE- (2 files) ---
    if n.startswith("TEMPLATE-"):
        return "certescence"

    # --- OPENCLAW- (1 file) ---
    if n.startswith("OPENCLAW-"):
        return "infrastructure/cli/openclaw"

    # --- Singletons (Pass 3 edge case 1) ---
    if n == "PORTAL-CHAT-AGENTS.md":
        return "agents/coordination"
    if n == "FLEET-COMMANDERS-HANDBOOK.md":
        return "agents/coordination"
    if n == "DEPLOYMENT-PLAYBOOK.md":
        return "infrastructure/deployment"
    if n == "CONTINUOUS-IMPROVEMENT.md":
        return "agents/coordination"
    if n == "WORK-LOOP.md":
        return "agents/coordination"
    if n == "INTER-AGENT.md":
        return "agents/coordination"
    if n == "BOOT.md":
        return "infrastructure/deployment"
    if n == "README.md":
        return "infrastructure/deployment"

    # 'agents' directory inside scaffold (artifact)
    if n == "agents":
        return None  # Skip — it's a directory, not a file

    return "uncategorized"


def route_sources(name: str) -> str:
    """Route a sources/ file to its target directory."""
    n = name

    # --- NOTEBOOK- (265 files) ---
    if n.startswith("NOTEBOOK-"):
        for topic_key, target in NOTEBOOK_TOPICS.items():
            if topic_key in n.upper():
                return f"knowledge/{target.rstrip('/')}/notebooks"
        return "knowledge/uncategorized/notebooks"

    # --- SOURCE- (1,772 files) ---
    if n.startswith("SOURCE-"):
        # Route by embedded topic
        for topic_key, target in NOTEBOOK_TOPICS.items():
            if topic_key.lower().replace("-", "_") in n.lower().replace("-", "_"):
                return f"knowledge/{target.rstrip('/')}/raw"
        return "knowledge/uncategorized/raw"

    # --- META- (3,494 files) ---
    if n.startswith("META-"):
        for topic_key, target in NOTEBOOK_TOPICS.items():
            if topic_key.lower().replace("-", "_") in n.lower().replace("-", "_"):
                return f"knowledge/{target.rstrip('/')}/meta"
        return "knowledge/uncategorized/meta"

    # --- RESEARCH- (97 files) ---
    if n.startswith("RESEARCH-"):
        return "ontology/knowledge"

    # --- PROCESSED- (42 files) ---
    if n.startswith("PROCESSED-"):
        return "knowledge/processed"

    # --- INDEX- (8 files) ---
    if n.startswith("INDEX-"):
        return "ontology/knowledge"

    # --- ASSET- (6 files) ---
    if n.startswith("ASSET-"):
        return "knowledge/assets"

    # --- REF- (3 files) ---
    if n.startswith("REF-"):
        return "ontology/knowledge/references"

    # --- Singletons (Pass 3 edge case 2) ---
    if n == "FRONTMATTER_TEMPLATE.md":
        return "ontology/knowledge"
    if n == "DYN-SOURCES.csv":
        return "ontology/knowledge"
    if n == "TRANSCRIPT_RECONCILIATION.md":
        return "knowledge/uncategorized"
    if n in ("README.md", "index.md"):
        return "ontology/knowledge"

    return "knowledge/uncategorized"


def route_logs(name: str) -> str:
    """Route a logs/ file to its target directory."""
    n = name

    # --- RESPONSE-* / PROMPT-* (ascertescence) ---
    if n.startswith("RESPONSE-ORACLE-") or n.startswith("PROMPT-ORACLE-"):
        return "ascertescence/oracle"
    if n.startswith("RESPONSE-DIVINER-") or n.startswith("PROMPT-DIVINER-"):
        return "ascertescence/diviner"
    if n.startswith("RESPONSE-ADJUDICATOR-") or n.startswith("PROMPT-ADJUDICATOR-"):
        return "ascertescence/adjudicator"
    if n.startswith(("RESPONSE-", "PROMPT-")):
        return "ascertescence"

    # --- CLARESCENCE- / CLARESCE- ---
    if n.startswith(("CLARESCENCE-", "CLARESCE-")):
        return "clarescence"

    # --- ARCH-* (39 files) ---
    if n.startswith("ARCH-"):
        if "ONTOLOGY" in n.upper():
            return "ontology/annealment"
        if "MEMORY" in n.upper():
            return "memory-new"
        if "SKILL" in n.upper():
            return "skills"
        if "LOCK" in n.upper():
            return "infrastructure"
        return "ontology/core"

    # --- DYN-* (43 files) ---
    if n.startswith("DYN-"):
        return "memory-new"

    # --- ANNEAL-* (9 files) ---
    if n.startswith("ANNEAL-"):
        return "ontology/annealment"

    # --- REF-* (23 files) ---
    if n.startswith("REF-"):
        return "ontology/knowledge/references"

    # --- RESULT-* (21 files) ---
    if n.startswith("RESULT-"):
        return "certescence"

    # --- RENDEZVOUS-* (11 files) ---
    if n.startswith("RENDEZVOUS-"):
        return "agents/coordination"

    # --- QUEUE-* (7 files) ---
    if n.startswith("QUEUE-"):
        return "agents/coordination"

    # --- GATE-* (7 files) ---
    if n.startswith("GATE-"):
        return "sovereignty"

    # --- DISPATCH-* (7 files) ---
    if n.startswith("DISPATCH-"):
        return "agents/coordination"

    # --- VERIFY-* (6 files) ---
    if n.startswith("VERIFY-"):
        return "certescence"

    # --- RESEARCH-* (6 files) ---
    if n.startswith("RESEARCH-"):
        return "ontology/knowledge"

    # --- MODEL-* (6 files) ---
    if n.startswith("MODEL-"):
        return "infrastructure/cli"

    # --- SOVEREIGN-* (5 files) ---
    if n.startswith("SOVEREIGN-"):
        return "sovereignty/directives"

    # --- PRAC-* (5 files) ---
    if n.startswith("PRAC-"):
        return "skills"

    # --- DEC-* (8 files) ---
    if n.startswith("DEC-"):
        return "sovereignty/intention-decision"

    # --- RUNLOGS-* (6 files) ---
    if n.startswith("RUNLOGS-"):
        return "infrastructure"

    # --- Heartbeat files ---
    if n.endswith(".heartbeat"):
        return "infrastructure"

    # --- Remaining small-count prefixes ---
    for prefix, target in [
        ("GUIDE", "skills"),
        ("ENDEAVOR", "ontology/core"),
        ("CONVERGENCE", "ontology/core"),
        ("CONTRACT", "ontology/core"),
        ("CAPABILITY", "consciousness/capabilities"),
        ("AUDIT", "certescence"),
        ("ACTION_TYPES", "agents/coordination"),
        ("AGENT_BINDINGS", "agents/coordination"),
        ("APP_ACTIONS", "agents/coordination"),
        ("ACTIVE", "agents/coordination"),
        ("DECISION", "sovereignty/intention-decision"),
        ("CLAUDECRON", "infrastructure"),
    ]:
        if n.startswith(prefix):
            return target

    # Scripts/code that ended up in logs
    if n.endswith((".py", ".sh", ".yaml", ".yml", ".json", ".csv")):
        return "infrastructure"

    return "logs/archived"


def process_directory(source_dir: str, router_fn):
    """Process all files in a directory using the given router function."""
    source = Path(source_dir)
    if not source.exists():
        log(f"SKIP: {source_dir} does not exist")
        return

    files = sorted(source.iterdir())
    log(f"Processing {source_dir}/ — {len(files)} items")

    for p in files:
        if not p.is_file():
            STATS["skipped"] += 1
            continue
        if p.name == ".DS_Store":
            STATS["skipped"] += 1
            continue

        target = router_fn(p.name)
        if target is None:
            STATS["skipped"] += 1
            continue

        git_mv(p, Path(target) / p.name)


def cleanup_structural_voids():
    """Handle engine/, orchestration/, memory/ (Pass 3 edge case 3)."""
    log("Cleaning up structural voids...")

    # engine/ — move remaining files to ontology, then remove
    engine = Path("engine")
    if engine.exists():
        for p in engine.rglob("*"):
            if p.is_file():
                if p.name == ".DS_Store":
                    continue
                if p.suffix in (".log",):
                    git_mv(p, Path("infrastructure") / p.name)
                else:
                    git_mv(p, Path("ontology/core") / p.name)
        if not DRY_RUN:
            # Remove empty dirs
            subprocess.run(["git", "rm", "-rf", "--ignore-unmatch", "engine/"],
                           capture_output=True, text=True)
            log("Removed engine/ shell")

    # orchestration/ — archive logs, then remove
    orch = Path("orchestration")
    if orch.exists():
        for p in orch.rglob("*"):
            if p.is_file():
                if p.name == ".DS_Store":
                    continue
                git_mv(p, Path("infrastructure") / p.name)
        if not DRY_RUN:
            subprocess.run(["git", "rm", "-rf", "--ignore-unmatch", "orchestration/"],
                           capture_output=True, text=True)
            log("Removed orchestration/ shell")

    # memory/ → merge into memory-new/, then rename
    mem = Path("memory")
    if mem.exists():
        for p in mem.rglob("*"):
            if p.is_file():
                if p.name == ".DS_Store":
                    continue
                git_mv(p, Path("memory-new") / p.name)
        if not DRY_RUN:
            subprocess.run(["git", "rm", "-rf", "--ignore-unmatch", "memory/"],
                           capture_output=True, text=True)
            log("Removed old memory/ shell")


def rename_memory_new():
    """After old memory/ is gone, rename memory-new/ → memory/."""
    if Path("memory-new").exists() and not Path("memory").exists():
        if DRY_RUN:
            print("  DRY: git mv memory-new/ memory/")
        else:
            subprocess.run(["git", "mv", "memory-new", "memory"],
                           capture_output=True, text=True, check=True)
            log("Renamed memory-new/ → memory/")
    elif Path("memory-new").exists():
        log("WARNING: memory/ still exists, cannot rename memory-new/")


def remove_empty_source_dirs():
    """Remove scaffold/, sources/, logs/ after all files moved."""
    for d in ["scaffold", "sources", "logs"]:
        p = Path(d)
        if p.exists():
            remaining = list(p.rglob("*"))
            remaining = [f for f in remaining if f.is_file() and f.name != ".DS_Store"]
            if remaining:
                log(f"WARNING: {d}/ still has {len(remaining)} files!")
            elif not DRY_RUN:
                subprocess.run(["git", "rm", "-rf", "--ignore-unmatch", f"{d}/"],
                               capture_output=True, text=True)
                log(f"Removed empty {d}/ directory")


# ═══════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════

def main():
    os.chdir(Path(__file__).parent)

    log(f"Nucleosynthesis CC45 — {'DRY RUN' if DRY_RUN else 'LIVE'}")
    log(f"Phase filter: {PHASE or 'ALL'}")

    # Create target directories
    for d in TARGET_DIRS:
        Path(d).mkdir(parents=True, exist_ok=True)

    # Additional knowledge subdirs from notebook topics
    for topic_key, target in NOTEBOOK_TOPICS.items():
        for sub in ["raw", "meta", "notebooks"]:
            Path(f"knowledge/{target.rstrip('/')}/{sub}").mkdir(parents=True, exist_ok=True)

    if PHASE is None or PHASE == "scaffold":
        process_directory("scaffold", route_scaffold)

    if PHASE is None or PHASE == "sources":
        process_directory("sources", route_sources)

    if PHASE is None or PHASE == "logs":
        process_directory("logs", route_logs)

    if PHASE is None or PHASE == "cleanup":
        cleanup_structural_voids()
        rename_memory_new()
        remove_empty_source_dirs()

    log("─" * 50)
    log(f"RESULTS: {STATS['moved']} moved, {STATS['skipped']} skipped, "
        f"{STATS['collision']} collisions, {STATS['error']} errors")

    if STATS["error"] > 0:
        log("⚠ ERRORS DETECTED — review output above before committing")
        sys.exit(1)


if __name__ == "__main__":
    main()
