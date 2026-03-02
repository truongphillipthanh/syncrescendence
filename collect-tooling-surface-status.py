#!/usr/bin/env python3
"""Collect repo-safe local tooling and domain readiness status."""

from __future__ import annotations

import argparse
import json
import socket
import subprocess
import urllib.error
import urllib.request
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parent
STATE_DIR = REPO_ROOT / "00-ORCHESTRATION" / "state"
JSON_PATH = STATE_DIR / "LOCAL-SURFACE-STATUS.json"
MD_PATH = STATE_DIR / "LOCAL-SURFACE-STATUS.md"

KEYCHAIN_CANDIDATES = {
    "gcloud_account": [("syncrescendence", "gcloud-account")],
    "cloudflare_account_id": [("syncrescendence", "cloudflare-account-id")],
    "wrangler_account": [("syncrescendence", "wrangler-account")],
    "manus_api_key": [
        ("manus-api-key", "syncrescendence"),
        ("syncrescendence", "manus-api-key"),
    ],
}


def utc_now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def run_command(command: list[str], timeout: float = 5.0) -> tuple[int | None, str, str, bool]:
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False,
            timeout=timeout,
        )
        return result.returncode, result.stdout, result.stderr, False
    except subprocess.TimeoutExpired as exc:
        return None, exc.stdout or "", exc.stderr or "", True


def keychain_item_status(service: str, account: str, timeout: float = 2.0) -> dict[str, Any]:
    code, stdout, stderr, timed_out = run_command(
        [
            "security",
            "find-generic-password",
            "-s",
            service,
            "-a",
            account,
        ],
        timeout=timeout,
    )
    if timed_out:
        return {"present": False, "timed_out": True}
    if code != 0:
        return {"present": False, "error": (stderr or stdout).strip() or None}

    created_at = None
    modified_at = None
    for line in stdout.splitlines():
        if '"cdat"' in line and "202" in line:
            created_at = line.split('"')[-2].replace("\\000", "")
        if '"mdat"' in line and "202" in line:
            modified_at = line.split('"')[-2].replace("\\000", "")
    return {
        "present": True,
        "service": service,
        "account": account,
        "created_at": created_at,
        "modified_at": modified_at,
    }


def resolve_candidate_group(name: str) -> dict[str, Any]:
    candidates = KEYCHAIN_CANDIDATES[name]
    attempts: list[dict[str, Any]] = []
    for service, account in candidates:
        status = keychain_item_status(service, account)
        attempts.append(status)
        if status.get("present"):
            return {"name": name, "present": True, "selected": status, "attempts": attempts}
    return {"name": name, "present": False, "attempts": attempts}


def gcloud_status() -> dict[str, Any]:
    code, stdout, stderr, timed_out = run_command(["gcloud", "auth", "list", "--format=json"])
    if timed_out:
        return {"available": True, "timed_out": True}
    if code != 0:
        return {"available": False, "error": (stderr or stdout).strip() or None}
    rows = json.loads(stdout or "[]")
    active = next((item for item in rows if item.get("status") == "ACTIVE"), None)
    return {
        "available": True,
        "authenticated": bool(active),
        "active_account": active.get("account") if active else None,
        "accounts": rows,
    }


def wrangler_status() -> dict[str, Any]:
    code, stdout, stderr, timed_out = run_command(["wrangler", "whoami", "--json"])
    if timed_out:
        return {"available": True, "timed_out": True}
    if code != 0:
        return {"available": False, "error": (stderr or stdout).strip() or None}
    payload = json.loads(stdout or "{}")
    primary_account = (payload.get("accounts") or [{}])[0]
    return {
        "available": True,
        "authenticated": bool(payload.get("loggedIn")),
        "email": payload.get("email"),
        "auth_type": payload.get("authType"),
        "account_id": primary_account.get("id"),
        "account_name": primary_account.get("name"),
        "token_permissions": payload.get("tokenPermissions", []),
    }


def http_status(url: str, timeout: float = 5.0) -> dict[str, Any]:
    request = urllib.request.Request(url, headers={"User-Agent": "syncrescendence-status/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read().decode("utf-8", errors="replace")
            try:
                payload = json.loads(body)
            except Exception:
                payload = None
            return {
                "reachable": True,
                "status_code": response.status,
                "payload": payload,
            }
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        try:
            payload = json.loads(body)
        except Exception:
            payload = None
        return {"reachable": True, "status_code": exc.code, "payload": payload}
    except Exception as exc:
        return {"reachable": False, "error": str(exc)}


def dns_status(hostname: str) -> dict[str, Any]:
    try:
        host, aliases, addrs = socket.gethostbyname_ex(hostname)
        return {"resolves": True, "host": host, "aliases": aliases, "addresses": addrs}
    except Exception as exc:
        return {"resolves": False, "error": str(exc)}


def manus_status(keychain_status: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {
        "keychain": keychain_status,
    }
    selected = keychain_status.get("selected")
    if not selected or not selected.get("present"):
        result["reachable"] = False
        result["reason"] = "manus_api_key_missing"
        return result

    service = selected["service"]
    account = selected["account"]
    code, stdout, stderr, timed_out = run_command(
        ["security", "find-generic-password", "-s", service, "-a", account, "-w"],
        timeout=2.0,
    )
    if timed_out:
        result["reachable"] = False
        result["reason"] = "manus_key_read_timed_out"
        return result
    if code != 0:
        result["reachable"] = False
        result["reason"] = "manus_key_read_failed"
        result["error"] = (stderr or stdout).strip() or None
        return result

    key = stdout.strip()
    request = urllib.request.Request(
        "https://api.manus.ai/v1/tasks",
        headers={"API_KEY": key, "User-Agent": "syncrescendence-status/1.0"},
    )
    try:
        with urllib.request.urlopen(request, timeout=5.0) as response:
            body = response.read().decode("utf-8", errors="replace")
            try:
                payload = json.loads(body)
            except Exception:
                payload = None
            result.update(
                {
                    "reachable": True,
                    "status_code": response.status,
                    "response_shape": type(payload).__name__ if payload is not None else "unknown",
                }
            )
            if isinstance(payload, list):
                result["task_count"] = len(payload)
    except urllib.error.HTTPError as exc:
        result.update({"reachable": True, "status_code": exc.code})
    except Exception as exc:
        result.update({"reachable": False, "reason": "http_error", "error": str(exc)})
    return result


def collect() -> dict[str, Any]:
    gcloud_keychain = resolve_candidate_group("gcloud_account")
    cloudflare_keychain = resolve_candidate_group("cloudflare_account_id")
    wrangler_keychain = resolve_candidate_group("wrangler_account")
    manus_keychain = resolve_candidate_group("manus_api_key")

    return {
        "captured_at": utc_now(),
        "gcloud": {
            "cli": gcloud_status(),
            "keychain": gcloud_keychain,
        },
        "wrangler": {
            "cli": wrangler_status(),
            "keychain": {
                "wrangler_account": wrangler_keychain,
                "cloudflare_account_id": cloudflare_keychain,
            },
        },
        "manus": manus_status(manus_keychain),
        "ontology": {
            "local_api": http_status("http://127.0.0.1:8787/health"),
            "local_proxy": http_status("http://localhost:8080/health"),
            "domain_dns": dns_status("syncrescendence.com"),
            "domain_health": http_status("https://syncrescendence.com/health"),
        },
    }


def write_report(report: dict[str, Any]) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    JSON_PATH.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    gcloud_cli = report["gcloud"]["cli"]
    wrangler_cli = report["wrangler"]["cli"]
    manus = report["manus"]
    ontology = report["ontology"]
    lines = [
        "# Local Surface Status",
        "",
        f"**Captured**: {report['captured_at']}",
        "",
        "## Auth Surfaces",
        "",
        f"- `gcloud` authenticated: `{gcloud_cli.get('authenticated')}`",
        f"- `gcloud` active account: `{gcloud_cli.get('active_account')}`",
        f"- `gcloud` keychain pointer present: `{report['gcloud']['keychain'].get('present')}`",
        f"- `wrangler` authenticated: `{wrangler_cli.get('authenticated')}`",
        f"- `wrangler` email: `{wrangler_cli.get('email')}`",
        f"- `wrangler` account id: `{wrangler_cli.get('account_id')}`",
        f"- Cloudflare account-id keychain pointer present: `{report['wrangler']['keychain']['cloudflare_account_id'].get('present')}`",
        f"- Manus keychain pointer present: `{manus.get('keychain', {}).get('present')}`",
        f"- Manus API reachable: `{manus.get('reachable')}`",
        "",
        "## Ontology Domain Readiness",
        "",
        f"- Local API reachable: `{ontology['local_api'].get('reachable')}`",
        f"- Local proxy reachable: `{ontology['local_proxy'].get('reachable')}`",
        f"- Public DNS resolves: `{ontology['domain_dns'].get('resolves')}`",
        f"- Public domain health reachable: `{ontology['domain_health'].get('reachable')}`",
        "",
        "## Reading",
        "",
        "- Local auth and serving surfaces can be checked without exposing secrets in repo artifacts.",
        "- Public cutover remains blocked until DNS and edge routing make `syncrescendence.com` resolve and serve `/health`.",
        "- CLI and Keychain status should remain pointer-only; credentials stay local.",
        "",
    ]
    MD_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.parse_args()
    report = collect()
    write_report(report)
    print(f"Wrote tooling surface status to {JSON_PATH} and {MD_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
