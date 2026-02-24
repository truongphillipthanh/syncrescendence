"""Syncrescendence central configuration - Python edition."""
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent

# Directory structure
ORCHESTRATION_DIR = REPO_ROOT / "orchestration" / "00-ORCHESTRATION"
ENGINE_DIR = REPO_ROOT / "engine" / "02-ENGINE"
SOURCES_DIR = REPO_ROOT / "sources" / "04-SOURCES"
PRAXIS_DIR = REPO_ROOT / "praxis" / "05-SIGMA"
AGENTS_DIR = REPO_ROOT / "agents"
SOVEREIGN_DIR = REPO_ROOT / "-SOVEREIGN"
CANON_DIR = REPO_ROOT / "canon"
COLLAB_DIR = REPO_ROOT / "collab"
INBOX_DIR = REPO_ROOT / "-INBOX"

# Orchestration subdirectories
STATE_DIR = ORCHESTRATION_DIR / "state"
SCRIPTS_DIR = ORCHESTRATION_DIR / "scripts"
ARCHIVE_DIR = ORCHESTRATION_DIR / "archive"
TEMPLATES_DIR = ORCHESTRATION_DIR / "templates"

# Agent names and machine assignments
AGENTS = ("commander", "adjudicator", "cartographer", "psyche", "ajna")
AGENT_MACHINES = ("mini", "mini", "mini", "mini", "air")  # mac mini or macbook air
AGENT_MACHINE_MAP = dict(zip(AGENTS, AGENT_MACHINES))

# SSH aliases
SSH_MINI = "mini"
SSH_AIR = "macbook-air"

# Graphiti
GRAPHITI_ENDPOINT = "http://M1-Mac-mini.local:8001"

# Key paths
SSH_KEY_AJNA = Path.home() / ".ssh" / "id_ed25519_ajna"
SSH_KEY_PSYCHE = Path.home() / ".ssh" / "id_ed25519_ajna_to_psyche"

INBOX_STATES = {"pending", "active", "done", "failed", "blocked"}


def get_agent_dir(name: str) -> Path:
    """Return an agent directory path for a known agent name."""
    normalized = name.strip().lower()
    if normalized not in AGENTS:
        raise ValueError(f"Unknown agent '{name}'. Expected one of: {', '.join(AGENTS)}")
    return AGENTS_DIR / normalized


def get_inbox(name: str, state: str = "pending") -> Path:
    """Return an agent inbox path for the requested state."""
    normalized_state = state.strip().lower()
    if normalized_state not in INBOX_STATES:
        raise ValueError(
            f"Unknown inbox state '{state}'. Expected one of: {', '.join(sorted(INBOX_STATES))}"
        )
    return get_agent_dir(name) / "inbox" / normalized_state


__all__ = [
    "REPO_ROOT",
    "ORCHESTRATION_DIR",
    "ENGINE_DIR",
    "SOURCES_DIR",
    "PRAXIS_DIR",
    "AGENTS_DIR",
    "SOVEREIGN_DIR",
    "CANON_DIR",
    "COLLAB_DIR",
    "INBOX_DIR",
    "STATE_DIR",
    "SCRIPTS_DIR",
    "ARCHIVE_DIR",
    "TEMPLATES_DIR",
    "AGENTS",
    "AGENT_MACHINES",
    "AGENT_MACHINE_MAP",
    "SSH_MINI",
    "SSH_AIR",
    "GRAPHITI_ENDPOINT",
    "SSH_KEY_AJNA",
    "SSH_KEY_PSYCHE",
    "INBOX_STATES",
    "get_agent_dir",
    "get_inbox",
]
