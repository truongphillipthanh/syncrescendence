#!/usr/bin/env python3
"""Integration-first session-close gate (DC-310)."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import subprocess
import sys
from pathlib import Path

BASELINE_REL = "orchestration/00-ORCHESTRATION/state/DYN-SESSION_BASELINE.json"
ATOM_REL = "sources/04-SOURCES/_meta/DYN-ATOM_INDEX.jsonl"
LOG_REL = "orchestration/00-ORCHESTRATION/state/DYN-INTEGRATION_GATE_LOG.jsonl"

ARTIFACT_PREFIXES = ("praxis/05-SIGMA/", "canon/01-CANON/sn/")
OUTBOX_PREFIX = "agents/commander/outbox/"
BYPASS_PREFIX = "-SOVEREIGN/BYPASS-INTEGRATION_GATE-"


class GateError(RuntimeError):
    pass


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def git(repo_root: Path, *args: str, check: bool = True) -> str:
    proc = subprocess.run(["git", "-C", str(repo_root), *args], capture_output=True, text=True)
    if check and proc.returncode != 0:
        raise GateError(proc.stderr.strip() or f"git failed: {' '.join(args)}")
    return proc.stdout


def read_baseline_commit(repo_root: Path) -> str:
    path = repo_root / BASELINE_REL
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise GateError(f"missing baseline file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise GateError(f"invalid baseline JSON: {path} ({exc})") from exc

    commit = str(data.get("commit", "")).strip()
    if not commit:
        raise GateError(f"missing 'commit' field in {path}")

    exists = subprocess.run(
        ["git", "-C", str(repo_root), "cat-file", "-e", f"{commit}^{{commit}}"],
        capture_output=True,
        text=True,
    )
    if exists.returncode != 0:
        raise GateError(f"baseline commit does not exist: {commit}")
    return commit


def collect_path_status(repo_root: Path, baseline_commit: str) -> dict[str, set[str]]:
    status_by_path: dict[str, set[str]] = {}

    diff_out = git(repo_root, "diff", "--name-status", "--find-renames", baseline_commit, "--")
    for line in diff_out.splitlines():
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        raw = parts[0]
        code = raw[0] if raw else ""
        if code in {"R", "C"} and len(parts) >= 3:
            path = parts[2]
        else:
            path = parts[1]
        if code and path:
            status_by_path.setdefault(path, set()).add(code)

    untracked = git(repo_root, "ls-files", "--others", "--exclude-standard")
    for path in (x.strip() for x in untracked.splitlines()):
        if path:
            status_by_path.setdefault(path, set()).add("A")

    return status_by_path


def non_delete(statuses: set[str]) -> bool:
    return any(code != "D" for code in statuses)


def collect_atom_transitions(repo_root: Path, baseline_commit: str) -> list[str]:
    diff_text = git(repo_root, "diff", "--unified=0", baseline_commit, "--", ATOM_REL, check=False)
    found: list[str] = []
    seen = set()
    for line in diff_text.splitlines():
        if not line.startswith("+") or line.startswith("+++"):
            continue
        raw = line[1:].strip()
        if not raw.startswith("{"):
            continue
        try:
            row = json.loads(raw)
        except json.JSONDecodeError:
            continue
        status = row.get("integration_status")
        if status == "consumed" or (isinstance(status, str) and status.startswith("promoted_")):
            token = f"{row.get('atom_id', 'unknown_atom')}:{status}"
            if token not in seen:
                seen.add(token)
                found.append(token)
    return found


def collect_artifact_paths(status_by_path: dict[str, set[str]]) -> list[str]:
    return sorted(
        p
        for p, statuses in status_by_path.items()
        if non_delete(statuses) and p.startswith(ARTIFACT_PREFIXES)
    )


def collect_outbox_paths(status_by_path: dict[str, set[str]]) -> list[str]:
    out = []
    for path, statuses in status_by_path.items():
        if not non_delete(statuses) or not path.startswith(OUTBOX_PREFIX):
            continue
        name = Path(path).name
        if name.startswith("RESULT-") or name.startswith("HANDOFF-"):
            out.append(path)
    return sorted(set(out))


def collect_bypass_reasons(repo_root: Path, status_by_path: dict[str, set[str]]) -> list[str]:
    reasons = []
    for path, statuses in status_by_path.items():
        if not non_delete(statuses):
            continue
        if not path.startswith(BYPASS_PREFIX) or not path.endswith(".md"):
            continue
        abs_path = repo_root / path
        if not abs_path.is_file():
            continue
        if len(abs_path.read_text(encoding="utf-8", errors="replace").strip()) >= 20:
            reasons.append(path)
    return sorted(set(reasons))


def append_log(
    repo_root: Path,
    session_id: str,
    result: str,
    evidence: list[str],
    baseline_commit: str,
    head_commit: str,
) -> None:
    log_path = repo_root / LOG_REL
    log_path.parent.mkdir(parents=True, exist_ok=True)
    row = {
        "timestamp": now_iso(),
        "session_id": session_id,
        "result": result,
        "evidence": evidence,
        "baseline_commit": baseline_commit,
        "head_commit": head_commit,
    }
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, ensure_ascii=True) + "\n")


def print_report(
    repo_root: Path,
    session_id: str,
    baseline_commit: str,
    head_commit: str,
    result: str,
    evidence: list[str],
    note: str,
) -> None:
    print("=== INTEGRATION-FIRST GATE (DC-310) ===")
    print(f"repo_root: {repo_root}")
    print(f"session_id: {session_id}")
    print(f"baseline_commit: {baseline_commit}")
    print(f"head_commit: {head_commit}")
    print(f"result: {result}")
    if evidence:
        print("evidence:")
        for item in evidence:
            print(f"- {item}")
    else:
        print("evidence: []")
    if note:
        print(f"note: {note}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Session-close integration-first gate")
    parser.add_argument("--repo-root", required=True)
    parser.add_argument("--session-id", default="")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    if not (repo_root / ".git").exists():
        print(f"ERROR: not a git repository: {repo_root}", file=sys.stderr)
        return 1

    session_id = args.session_id.strip() or os.environ.get("SESSION_ID", "").strip()
    if not session_id:
        session_id = f"session-{dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ')}"

    head_commit = git(repo_root, "rev-parse", "HEAD").strip() or "unknown"
    baseline_commit = "unknown"
    evidence: list[str] = []
    result = "fail"
    note = ""
    exit_code = 1

    try:
        baseline_commit = read_baseline_commit(repo_root)
        status_by_path = collect_path_status(repo_root, baseline_commit)
        if os.environ.get("INTEGRATION_GATE_BYPASS") == "1":
            reasons = collect_bypass_reasons(repo_root, status_by_path)
            if reasons:
                result, exit_code = "bypass", 0
                evidence = [f"bypass_reason:{p}" for p in reasons]
                note = "WARNING: INTEGRATION_GATE_BYPASS=1 active; gate bypassed."
            else:
                note = (
                    "INTEGRATION_GATE_BYPASS=1 requires a changed reason file at "
                    "-SOVEREIGN/BYPASS-INTEGRATION_GATE-<timestamp>.md with explanation text."
                )
        else:
            artifacts = collect_artifact_paths(status_by_path)
            atoms = collect_atom_transitions(repo_root, baseline_commit)
            outbox = collect_outbox_paths(status_by_path)
            evidence = [f"artifact:{p}" for p in artifacts]
            evidence += [f"atom_transition:{x}" for x in atoms]
            evidence += [f"outbox:{p}" for p in outbox]
            if evidence:
                result, exit_code = "pass", 0
            else:
                note = (
                    "No qualifying value artifact detected since baseline "
                    "(SIGMA/CANON, atom consumed/promoted, or RESULT/HANDOFF outbox)."
                )
    except GateError as exc:
        note = str(exc)

    append_log(repo_root, session_id, result, evidence, baseline_commit, head_commit)
    print_report(repo_root, session_id, baseline_commit, head_commit, result, evidence, note)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
