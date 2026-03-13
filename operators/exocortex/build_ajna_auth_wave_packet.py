#!/usr/bin/env python3
"""Build a markdown packet for an Ajna exocortex auth/onboarding wave."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PROGRAM = REPO_ROOT / "orchestration" / "state" / "AJNA-EXOCORTEX-ACCESS-PROGRAM-CC93.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet(program: dict[str, Any], wave: str) -> str:
    surfaces = [row for row in program.get("surfaces", []) if row.get("wave") == wave]
    if not surfaces:
        raise SystemExit(f"No surfaces found for wave: {wave}")
    lines = [
        f"# PACKET-AJNA-{wave.upper()}-AUTH-CC93",
        "",
        f"- Office: `ajna`",
        f"- Designated browser: `{program['designated_browser']['browser_family']}` via profile `{program['designated_browser']['openclaw_profile']}`",
        f"- Wave: `{wave}`",
        "",
        "## Mission",
        "",
        "Expand Ajna's exocortex reach for this wave without letting browser state or external tools become constitutional truth.",
        "",
        "## Rules",
        "",
        "- Prefer native API/CLI credential capture after browser login, not permanent browser-only dependence.",
        "- Never persist raw secrets into repo artifacts.",
        "- After any successful auth, promote only pointer-safe state back into repo.",
        "- Parent-auth children must be activated through their parent roots, not treated as separate login universes.",
        "",
        "## Surfaces",
        "",
    ]
    for row in surfaces:
        parent = f" | parent=`{row['auth_parent_surface']}`" if row.get("auth_parent_surface") else ""
        lines.append(
            f"- `{row['slug']}`: `{row['service']}` | strategy=`{row['access_strategy']}` | role=`{row['ajna_role']}` | priority=`{row['integration_priority']}`{parent}"
        )
        lines.append(f"  Proper role: {row['proper_role']}")
        lines.append(f"  Anti-role: {row['anti_role']}")
    lines.extend(
        [
            "",
            "## Completion Condition",
            "",
            "- Surface is authenticated in the correct identity/workspace.",
            "- Any stable token/API key is placed in the correct local secret store rather than repo text.",
            "- Repo receives a pointer-safe status update describing what is live, what remains blocked, and what still needs human auth.",
            "",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--program", default=str(DEFAULT_PROGRAM))
    parser.add_argument("--wave", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    program = load_json(Path(args.program).expanduser().resolve())
    output = Path(args.output).expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build_packet(program, args.wave), encoding="utf-8")
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
