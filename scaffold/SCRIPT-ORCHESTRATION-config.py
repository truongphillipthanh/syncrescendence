"""Syncrescendence central configuration - Python edition."""
import os
from pathlib import Path

_REPO_ROOT_DEFAULT = Path(__file__).resolve().parent.parent.parent.parent
SYNCRESCENDENCE_ROOT = os.environ.get("SYNCRESCENDENCE_ROOT", "").strip()
REPO_ROOT = Path(SYNCRESCENDENCE_ROOT).expanduser() if SYNCRESCENDENCE_ROOT else _REPO_ROOT_DEFAULT

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


class ConfigError(Exception):
    """Raised when critical config assumptions are violated."""


REQUIRED_PATHS = {
    "REPO_ROOT": REPO_ROOT,
    "ORCHESTRATION_DIR": ORCHESTRATION_DIR,
    "ENGINE_DIR": ENGINE_DIR,
    "SOURCES_DIR": SOURCES_DIR,
    "PRAXIS_DIR": PRAXIS_DIR,
    "AGENTS_DIR": AGENTS_DIR,
    "CANON_DIR": CANON_DIR,
    "STATE_DIR": STATE_DIR,
    "SCRIPTS_DIR": SCRIPTS_DIR,
}

OPTIONAL_PATHS = {
    "SOVEREIGN_DIR": SOVEREIGN_DIR,
    "COLLAB_DIR": COLLAB_DIR,
    "INBOX_DIR": INBOX_DIR,
    "ARCHIVE_DIR": ARCHIVE_DIR,
    "TEMPLATES_DIR": TEMPLATES_DIR,
}

REQUIRED_STATE_FILES = {
    "DYN-DEFERRED_COMMITMENTS": STATE_DIR / "DYN-DEFERRED_COMMITMENTS.md",
    "ARCH-INTENTION_COMPASS": STATE_DIR / "ARCH-INTENTION_COMPASS.md",
}

REQUIRED_ENV_VARS = ("SYNCRESCENDENCE_ROOT",)
OPTIONAL_ENV_VARS = ("HOME", "USER")


def validate_config(strict: bool = False) -> list[str]:
    """Validate configuration assumptions and return non-critical violations.

    Raises:
        ConfigError: when one or more critical assertions fail.
    """

    critical: list[str] = []
    violations: list[str] = []

    root_env = os.environ.get("SYNCRESCENDENCE_ROOT", "").strip()
    if not root_env:
        critical.append(
            "Required env var SYNCRESCENDENCE_ROOT is unset. "
            "Set it before running scripts (example: export SYNCRESCENDENCE_ROOT=/path/to/repo)."
        )

    if len(AGENTS) != len(AGENT_MACHINES):
        critical.append(
            "AGENTS and AGENT_MACHINES length mismatch; update config.py so machine mapping is complete."
        )

    for name, path in REQUIRED_PATHS.items():
        if not path.exists():
            critical.append(f"Missing required path {name}: {path}")

    for name, path in REQUIRED_STATE_FILES.items():
        if not path.is_file():
            critical.append(f"Missing required state file {name}: {path}")

    if strict:
        for name, path in OPTIONAL_PATHS.items():
            if not path.exists():
                violations.append(f"Missing optional path {name}: {path}")

        for var_name in REQUIRED_ENV_VARS + OPTIONAL_ENV_VARS:
            value = os.environ.get(var_name, "").strip()
            if not value:
                violations.append(f"Missing env var {var_name}")

    if critical:
        raise ConfigError("\n".join(critical))

    return violations


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
    "ConfigError",
    "SYNCRESCENDENCE_ROOT",
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
    "REQUIRED_PATHS",
    "OPTIONAL_PATHS",
    "REQUIRED_STATE_FILES",
    "REQUIRED_ENV_VARS",
    "OPTIONAL_ENV_VARS",
    "INBOX_STATES",
    "validate_config",
    "get_agent_dir",
    "get_inbox",
]
