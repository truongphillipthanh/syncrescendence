#!/usr/bin/env python3
"""Sequential Acumen flow: identity -> poll -> triage -> evidence -> Dawn Brief."""

from __future__ import annotations

import argparse
import json
from datetime import UTC, datetime
from pathlib import Path
import subprocess

from build_dawn_brief import main as dawn_brief_main  # noqa: F401  # imported for lane linkage
try:
    from .evidence_family import TRAINING_RUNTIME_PATH, TRIAGE_RUNTIME_PATH
except ImportError:
    from evidence_family import TRAINING_RUNTIME_PATH, TRIAGE_RUNTIME_PATH


def utc_now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", required=True)
    parser.add_argument("--queue", required=True, help="Compatibility path mirroring the triage runtime view.")
    parser.add_argument("--out", required=True, help="Output directory for compiled artifacts.")
    parser.add_argument("--status-json", default="orchestration/state/ACUMEN-PIPELINE-STATUS.json")
    parser.add_argument("--identity-binding", default="orchestration/state/ACUMEN-IDENTITY-BINDING-CC87.json")
    parser.add_argument("--identity-status-json", help="Optional override for identity status output.")
    parser.add_argument("--poll-output", help="JSONL file for the latest polling batch.")
    parser.add_argument("--poll-cursor-json", default="runtime/acumen/poll_cursor.json")
    parser.add_argument("--poll-status-json", default="runtime/acumen/poll-status.json")
    parser.add_argument("--poll-mode", choices=("auto", "fixture", "live"), default="auto")
    parser.add_argument("--fixture-feed", help="Deterministic fixture used when poll-mode=fixture or auto.")
    parser.add_argument("--force-poll", action="store_true")
    parser.add_argument("--training-jsonl", default="runtime/acumen/training-corpus.jsonl")
    parser.add_argument("--triage-status-json", default="runtime/acumen/triage-status.json")
    parser.add_argument("--triage-mode", choices=("auto", "heuristic", "gemini"), default="auto")
    parser.add_argument("--triage-artifact-dir", help="Directory for packet and triage artifacts.")
    parser.add_argument("--triage-api-key-env", default="GEMINI_API_KEY")
    parser.add_argument("--triage-api-base", default="https://generativelanguage.googleapis.com/v1beta/models")
    parser.add_argument("--triage-timeout-seconds", type=float, default=45.0)
    parser.add_argument("--max-live-calls", type=int, default=5)
    parser.add_argument("--max-retries", type=int, default=2)
    parser.add_argument("--retry-backoff-seconds", type=float, default=1.5)
    parser.add_argument("--max-prompt-chars", type=int, default=18000)
    parser.add_argument("--max-output-tokens", type=int, default=220)
    parser.add_argument("--max-total-tokens", type=int, default=4096)
    parser.add_argument("--estimated-cost-per-call-usd", type=float, default=0.0)
    parser.add_argument("--max-estimated-cost-usd", type=float, default=0.0)
    parser.add_argument("--strict-identity", action="store_true")
    return parser.parse_args()


def write_status(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def ensure_jsonl(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text("", encoding="utf-8")


def load_json(path: Path) -> dict[str, object] | None:
    if not path.exists():
        return None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None
    return payload if isinstance(payload, dict) else None


def run_command(command: list[str]) -> dict[str, object]:
    proc = subprocess.run(command, capture_output=True, text=True, check=False)
    return {
        "command": command,
        "returncode": proc.returncode,
        "stdout": (proc.stdout or "").strip()[:2000],
        "stderr": (proc.stderr or "").strip()[:2000],
        "ok": proc.returncode == 0,
    }


def pipeline_failure(
    *,
    domain: str,
    code: str,
    message: str,
    stage: str,
    details: dict[str, object] | None = None,
) -> dict[str, object]:
    payload: dict[str, object] = {
        "failure_domain": domain,
        "failure_code": code,
        "failure_message": message,
        "failed_stage": stage,
    }
    if details:
        payload["failure_details"] = details
    return payload


def run_sequential(args: argparse.Namespace) -> dict[str, object]:
    registry = Path(args.registry).expanduser().resolve()
    queue = Path(args.queue).expanduser().resolve()
    out = Path(args.out).expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)
    ensure_jsonl(queue)

    poll_output = Path(args.poll_output).expanduser().resolve() if args.poll_output else out / "poll-latest.jsonl"
    training_jsonl = Path(args.training_jsonl).expanduser().resolve()
    ensure_jsonl(training_jsonl)
    triage_artifact_dir = Path(args.triage_artifact_dir).expanduser().resolve() if args.triage_artifact_dir else out / "triage"
    poll_status_json = Path(args.poll_status_json).expanduser().resolve()
    triage_status_json = Path(args.triage_status_json).expanduser().resolve()
    evidence_report_json = out / "ACUMEN-TRIAGE-EVIDENCE-REPORT.json"
    evidence_report_md = out / "ACUMEN-TRIAGE-EVIDENCE-REPORT.md"
    authoritative_queue = TRIAGE_RUNTIME_PATH.resolve()
    authoritative_training = TRAINING_RUNTIME_PATH.resolve()

    binding_path = Path(args.identity_binding).expanduser().resolve()
    binding = json.loads(binding_path.read_text(encoding="utf-8"))
    canonical = binding["google_surfaces"]["canonical_identity"]
    identity_status_path = (
        Path(args.identity_status_json).expanduser().resolve()
        if args.identity_status_json
        else Path(args.status_json).expanduser().resolve().parent / "ACUMEN-IDENTITY-STATUS.json"
    )

    identity_probe = run_command(
        [
            "python3",
            str(Path(__file__).resolve().parent / "identity_binding_probe.py"),
            "--binding",
            str(binding_path),
            "--output",
            str(identity_status_path),
        ]
        + (["--strict"] if args.strict_identity else [])
    )

    identity_ok = False
    if identity_status_path.exists():
        try:
            identity_payload = json.loads(identity_status_path.read_text(encoding="utf-8"))
            identity_ok = bool(identity_payload.get("ok"))
        except Exception:
            identity_ok = False

    status: dict[str, object] = {
        "captured_at": utc_now(),
        "mode": "sequential",
        "execution_profile": "live_batch"
        if args.poll_mode == "live" and args.triage_mode == "gemini" and args.strict_identity
        else "fixture_safe"
        if args.poll_mode == "fixture"
        else "custom",
        "registry_exists": registry.exists(),
        "queue_exists": queue.exists(),
        "canonical_identity": canonical,
        "identity_probe_success": identity_ok,
        "identity_probe": identity_probe,
        "identity_status_json": str(identity_status_path),
        "poll_output": str(poll_output),
        "poll_status_json": str(poll_status_json),
        "queue_jsonl": str(authoritative_queue),
        "requested_queue_jsonl": str(queue),
        "training_jsonl": str(authoritative_training),
        "requested_training_jsonl": str(training_jsonl),
        "triage_status_json": str(triage_status_json),
        "evidence_report_json": str(evidence_report_json),
        "evidence_report_md": str(evidence_report_md),
        "external_dependencies": {
            "youtube_feed": {
                "mode": args.poll_mode,
                "fixture_feed": str(Path(args.fixture_feed).expanduser().resolve()) if args.fixture_feed else None,
            },
            "gemini_api": {
                "mode": args.triage_mode,
                "api_key_env": args.triage_api_key_env,
                "api_base": args.triage_api_base,
                "timeout_seconds": args.triage_timeout_seconds,
                "live_calls_guardrail": args.max_live_calls,
                "retry_backoff_seconds": args.retry_backoff_seconds,
                "max_prompt_chars": args.max_prompt_chars,
                "max_output_tokens": args.max_output_tokens,
                "max_total_tokens": args.max_total_tokens,
                "estimated_cost_per_call_usd": args.estimated_cost_per_call_usd,
                "max_estimated_cost_usd": args.max_estimated_cost_usd,
            },
        },
    }

    if args.strict_identity and not identity_ok:
        status["stopped_reason"] = "strict_identity_failure"
        status["poll_success"] = False
        status["triage_success"] = False
        status["evidence_validation_success"] = False
        status["dawn_brief_success"] = False
        status.update(
            pipeline_failure(
                domain="identity",
                code="identity_mismatch",
                message="strict identity gate failed",
                stage="identity_probe",
                details=load_json(identity_status_path),
            )
        )
        return status

    use_fixture_poll = args.poll_mode == "fixture" or bool(args.fixture_feed)
    if use_fixture_poll:
        poll_command = [
            "python3",
            str(Path(__file__).resolve().parent / "poll_registry.py"),
            "--registry",
            str(registry),
            "--output",
            str(poll_output),
            "--cursor-json",
            str(Path(args.poll_cursor_json).expanduser().resolve()),
            "--status-json",
            str(poll_status_json),
            "--mode",
            "fixture" if args.poll_mode == "fixture" else "auto",
        ]
        if args.fixture_feed:
            poll_command.extend(["--fixture-feed", str(Path(args.fixture_feed).expanduser().resolve())])
        if args.force_poll:
            poll_command.append("--force")
    else:
        poll_command = [
            "python3",
            str(Path(__file__).resolve().parent / "poll_youtube_registry.py"),
            "--registry",
            str(registry),
            "--cursor",
            str(Path(args.poll_cursor_json).expanduser().resolve()),
            "--output-jsonl",
            str(poll_output),
            "--status-json",
            str(poll_status_json),
        ]
        if args.force_poll:
            poll_command.append("--force")
    poll_status = run_command(poll_command)
    poll_snapshot = load_json(poll_status_json)

    triage_command = [
        "python3",
        str(Path(__file__).resolve().parent / "run_triage.py"),
        "--registry",
        str(registry),
        "--poll-jsonl",
        str(poll_output),
        "--queue-jsonl",
        str(queue),
        "--training-jsonl",
        str(training_jsonl),
        "--status-json",
        str(triage_status_json),
        "--artifact-dir",
        str(triage_artifact_dir),
        "--mode",
        args.triage_mode,
        "--api-key-env",
        args.triage_api_key_env,
        "--api-base",
        args.triage_api_base,
        "--timeout-seconds",
        str(args.triage_timeout_seconds),
        "--max-live-calls",
        str(args.max_live_calls),
        "--max-retries",
        str(args.max_retries),
        "--retry-backoff-seconds",
        str(args.retry_backoff_seconds),
        "--max-prompt-chars",
        str(args.max_prompt_chars),
        "--max-output-tokens",
        str(args.max_output_tokens),
        "--max-total-tokens",
        str(args.max_total_tokens),
        "--estimated-cost-per-call-usd",
        str(args.estimated_cost_per_call_usd),
        "--max-estimated-cost-usd",
        str(args.max_estimated_cost_usd),
    ]
    if poll_status["ok"]:
        triage_status = run_command(triage_command)
    else:
        triage_status = {
            "command": triage_command,
            "returncode": None,
            "stdout": "",
            "stderr": "poll stage failed",
            "ok": False,
        }
    triage_snapshot = load_json(triage_status_json)

    evidence_command = [
        "python3",
        str(Path(__file__).resolve().parents[1] / "validators" / "validate_acumen_evidence.py"),
        "--output-json",
        str(evidence_report_json),
        "--output-md",
        str(evidence_report_md),
    ]
    if triage_status["ok"]:
        evidence_status = run_command(evidence_command)
    else:
        evidence_status = {
            "command": evidence_command,
            "returncode": None,
            "stdout": "",
            "stderr": "triage stage failed",
            "ok": False,
        }
    evidence_snapshot = load_json(evidence_report_json)

    dawn_brief = out / f"DAWN-BRIEF-{datetime.now(UTC).strftime('%Y%m%d')}.md"
    dawn_command = [
        "python3",
        str(Path(__file__).resolve().parent / "build_dawn_brief.py"),
        "--input-jsonl",
        str(authoritative_queue),
        "--output",
        str(dawn_brief),
    ]
    if evidence_status["ok"]:
        dawn_status = run_command(dawn_command)
    else:
        dawn_status = {
            "command": dawn_command,
            "returncode": None,
            "stdout": "",
            "stderr": "evidence validation failed",
            "ok": False,
        }

    status["poll_success"] = bool(poll_status["ok"])
    status["poll_status"] = poll_status
    status["poll_status_snapshot"] = poll_snapshot
    status["triage_success"] = bool(triage_status["ok"])
    status["triage_status"] = triage_status
    status["triage_status_snapshot"] = triage_snapshot
    status["evidence_validation_success"] = bool(evidence_status["ok"])
    status["evidence_validation_status"] = evidence_status
    status["evidence_report_snapshot"] = evidence_snapshot
    status["dawn_brief_path"] = str(dawn_brief)
    status["dawn_brief_success"] = bool(dawn_status["ok"])
    status["dawn_brief_status"] = dawn_status
    status["runtime_surface_authority"] = {
        "triage_runtime": str(authoritative_queue),
        "training_runtime": str(authoritative_training),
    }
    status["ok"] = bool(identity_ok and poll_status["ok"] and triage_status["ok"] and evidence_status["ok"] and dawn_status["ok"])

    if not poll_status["ok"]:
        if isinstance(poll_snapshot, dict):
            if poll_snapshot.get("failure_code"):
                status.update(
                    pipeline_failure(
                        domain="identity"
                        if poll_snapshot.get("failure_code") == "identity_mismatch"
                        else "credential"
                        if poll_snapshot.get("failure_code") == "missing_api_key"
                        else "external_service",
                        code=str(poll_snapshot.get("failure_code")),
                        message=str(poll_snapshot.get("failure_message") or "poll stage failed"),
                        stage="poll",
                        details=poll_snapshot,
                    )
                )
            elif str(poll_snapshot.get("result")) == "partial" and isinstance(poll_snapshot.get("errors"), list) and poll_snapshot["errors"]:
                first_error = poll_snapshot["errors"][0]
                if isinstance(first_error, dict):
                    status.update(
                        pipeline_failure(
                            domain="external_service",
                            code=str(first_error.get("code") or "poll_partial"),
                            message=str(first_error.get("message") or "poll stage failed"),
                            stage="poll",
                            details=poll_snapshot,
                        )
                    )
        if "failure_code" not in status:
            status.update(
                pipeline_failure(
                    domain="external_service",
                    code="poll_stage_failed",
                    message=str(poll_status.get("stderr") or "poll stage failed"),
                    stage="poll",
                )
            )
    elif not triage_status["ok"]:
        if isinstance(triage_snapshot, dict) and triage_snapshot.get("failure_code"):
            status.update(
                pipeline_failure(
                    domain=str(triage_snapshot.get("failure_domain") or "external_service"),
                    code=str(triage_snapshot.get("failure_code")),
                    message=str(triage_snapshot.get("failure_message") or "triage stage failed"),
                    stage="triage",
                    details=triage_snapshot,
                )
            )
        else:
            status.update(
                pipeline_failure(
                    domain="external_service",
                    code="triage_stage_failed",
                    message=str(triage_status.get("stderr") or "triage stage failed"),
                    stage="triage",
                )
            )
    elif not evidence_status["ok"]:
        if isinstance(evidence_snapshot, dict) and isinstance(evidence_snapshot.get("findings"), list) and evidence_snapshot["findings"]:
            first_finding = evidence_snapshot["findings"][0]
            if isinstance(first_finding, dict):
                status.update(
                    pipeline_failure(
                        domain="evidence_contract",
                        code="evidence_validation_failed",
                        message=str(first_finding.get("message") or "evidence validation failed"),
                        stage="evidence_validation",
                        details=evidence_snapshot,
                    )
                )
        if "failure_code" not in status:
            status.update(
                pipeline_failure(
                    domain="evidence_contract",
                    code="evidence_validation_failed",
                    message=str(evidence_status.get("stderr") or "evidence validation failed"),
                    stage="evidence_validation",
                )
            )
    elif not dawn_status["ok"]:
        status.update(
            pipeline_failure(
                domain="external_service",
                code="dawn_brief_failed",
                message=str(dawn_status.get("stderr") or "dawn brief compile failed"),
                stage="dawn_brief",
            )
        )
    return status


def main() -> int:
    args = parse_args()
    status = run_sequential(args)
    status_path = Path(args.status_json).expanduser().resolve()
    write_status(status_path, status)
    print(status_path)
    if args.strict_identity and not status["identity_probe_success"]:
        return 2
    if not status["poll_success"]:
        return 3
    if not status["triage_success"]:
        return 4
    if not status["evidence_validation_success"]:
        return 5
    if not status["dawn_brief_success"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
