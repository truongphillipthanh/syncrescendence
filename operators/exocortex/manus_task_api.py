#!/usr/bin/env python3
"""Lightweight Manus task API helper for create/get/wait workflows."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


BASE_URL = "https://api.manus.ai/v1"
KEYCHAIN_CANDIDATES = [
    ("manus-api-key", "syncrescendence"),
    ("syncrescendence", "manus-api-key"),
]
TERMINAL_STATES = {"completed", "failed", "cancelled", "canceled"}


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


def resolve_api_key() -> str:
    for service, account in KEYCHAIN_CANDIDATES:
        code, stdout, stderr, timed_out = run_command(
            [
                "security",
                "find-generic-password",
                "-s",
                service,
                "-a",
                account,
                "-w",
            ],
            timeout=2.0,
        )
        if timed_out or code != 0:
            continue
        key = stdout.strip()
        if key:
            return key
    raise SystemExit(
        "Could not resolve Manus API key from Keychain candidates: "
        + ", ".join(f"{s}:{a}" for s, a in KEYCHAIN_CANDIDATES)
    )


def api_request(
    method: str,
    path: str,
    key: str,
    payload: dict[str, Any] | None = None,
    timeout: float = 30.0,
) -> dict[str, Any]:
    data = None
    headers = {
        "API_KEY": key,
        "User-Agent": "syncrescendence-manus-task-api/1.0",
    }
    if payload is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(payload).encode("utf-8")

    request = urllib.request.Request(
        f"{BASE_URL}{path}",
        data=data,
        headers=headers,
        method=method,
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read().decode("utf-8", errors="replace")
            return json.loads(body or "{}")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        try:
            error_obj = json.loads(body)
        except Exception:
            error_obj = {"raw": body}
        raise SystemExit(json.dumps({"status": exc.code, "error": error_obj}, indent=2))


def load_prompt(args: argparse.Namespace) -> str:
    if args.prompt_file:
        prompt_text = Path(args.prompt_file).read_text(encoding="utf-8")
    elif args.prompt:
        prompt_text = args.prompt
    else:
        raise SystemExit("Use --prompt or --prompt-file for create.")
    prompt_text = prompt_text.strip()
    if not prompt_text:
        raise SystemExit("Prompt is empty.")
    return prompt_text


def task_to_text(task: dict[str, Any]) -> str:
    lines: list[str] = []
    output = task.get("output")
    if not isinstance(output, list):
        return ""
    for item in output:
        if not isinstance(item, dict):
            continue
        role = item.get("role")
        content = item.get("content")
        if role != "assistant" or not isinstance(content, list):
            continue
        for chunk in content:
            if not isinstance(chunk, dict):
                continue
            if chunk.get("type") != "output_text":
                continue
            text = chunk.get("text")
            if isinstance(text, str) and text.strip():
                lines.append(text.strip())
    return "\n\n".join(lines).strip()


def command_create(args: argparse.Namespace) -> int:
    key = resolve_api_key()
    prompt = load_prompt(args)
    payload = {"prompt": prompt}
    response = api_request("POST", "/tasks", key, payload=payload)
    print(json.dumps(response, indent=2, sort_keys=True))
    return 0


def command_get(args: argparse.Namespace) -> int:
    key = resolve_api_key()
    task = api_request("GET", f"/tasks/{args.task_id}", key)
    if args.extract_text:
        print(task_to_text(task))
        return 0
    print(json.dumps(task, indent=2, sort_keys=True))
    return 0


def command_wait(args: argparse.Namespace) -> int:
    key = resolve_api_key()
    deadline = time.time() + args.timeout_seconds
    last_status = None
    while True:
        task = api_request("GET", f"/tasks/{args.task_id}", key)
        status = str(task.get("status"))
        if status != last_status:
            print(f"status={status}")
            last_status = status
        if status in TERMINAL_STATES:
            if args.extract_text:
                print(task_to_text(task))
            else:
                print(json.dumps(task, indent=2, sort_keys=True))
            return 0
        if time.time() >= deadline:
            raise SystemExit(f"Timed out waiting for task {args.task_id}; last status={status}")
        time.sleep(args.interval_seconds)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    create_parser = subparsers.add_parser("create", help="Create a Manus task.")
    create_group = create_parser.add_mutually_exclusive_group(required=True)
    create_group.add_argument("--prompt", help="Prompt text.")
    create_group.add_argument("--prompt-file", help="Path to prompt file.")
    create_parser.set_defaults(func=command_create)

    get_parser = subparsers.add_parser("get", help="Fetch a Manus task by ID.")
    get_parser.add_argument("--task-id", required=True)
    get_parser.add_argument("--extract-text", action="store_true")
    get_parser.set_defaults(func=command_get)

    wait_parser = subparsers.add_parser("wait", help="Wait for task completion.")
    wait_parser.add_argument("--task-id", required=True)
    wait_parser.add_argument("--timeout-seconds", type=int, default=900)
    wait_parser.add_argument("--interval-seconds", type=int, default=15)
    wait_parser.add_argument("--extract-text", action="store_true")
    wait_parser.set_defaults(func=command_wait)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
