#!/usr/bin/env python3
"""Run Acumen triage with strict contracts and repo-local evidence outputs."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
from typing import Any

from build_triage_packet import build_triage_packet, resolve_channel
from gemini_triage_adapter import DEFAULT_API_BASE, DEFAULT_MODEL, GeminiTriageError, invoke_gemini_packet
try:
    from .evidence_family import (
        TRAINING_RUNTIME_PATH,
        TRIAGE_RUNTIME_PATH,
        ensure_surface_files,
        load_jsonl as load_evidence_jsonl,
        sha256_for_payload,
        write_jsonl as write_evidence_jsonl,
    )
    from .record_evidence import record_decision_payload, record_model_call_payload, rematerialize_runtime
except ImportError:
    from evidence_family import (
        TRAINING_RUNTIME_PATH,
        TRIAGE_RUNTIME_PATH,
        ensure_surface_files,
        load_jsonl as load_evidence_jsonl,
        sha256_for_payload,
        write_jsonl as write_evidence_jsonl,
    )
    from record_evidence import record_decision_payload, record_model_call_payload, rematerialize_runtime
from triage_contract import (
    TARGET_DEPTH_VALUES,
    TARGET_POLISH_VALUES,
    build_decision_record,
    render_prompt_preview,
    utc_now,
    validate_decision,
    write_json,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", required=True)
    parser.add_argument("--poll-jsonl", required=True)
    parser.add_argument("--queue-jsonl", required=True)
    parser.add_argument("--training-jsonl", required=True)
    parser.add_argument("--status-json", default="runtime/acumen/triage-status.json")
    parser.add_argument("--artifact-dir", default="runtime/acumen/out/triage")
    parser.add_argument("--mode", choices=("auto", "heuristic", "gemini"), default="auto")
    parser.add_argument("--model", default=os.environ.get("ACUMEN_GEMINI_MODEL", DEFAULT_MODEL))
    parser.add_argument("--api-base", default=os.environ.get("ACUMEN_GEMINI_API_BASE", DEFAULT_API_BASE))
    parser.add_argument("--api-key-env", default="GEMINI_API_KEY")
    parser.add_argument("--timeout-seconds", type=float, default=45.0)
    parser.add_argument("--max-live-calls", type=int, default=5)
    parser.add_argument("--max-retries", type=int, default=2)
    parser.add_argument("--retry-backoff-seconds", type=float, default=1.5)
    parser.add_argument("--max-prompt-chars", type=int, default=18000)
    parser.add_argument("--max-output-tokens", type=int, default=220)
    parser.add_argument("--max-total-tokens", type=int, default=4096)
    parser.add_argument("--estimated-cost-per-call-usd", type=float, default=0.0)
    parser.add_argument("--max-estimated-cost-usd", type=float, default=0.0)
    return parser.parse_args()


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not path.exists():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        payload = json.loads(line)
        if isinstance(payload, dict):
            rows.append(payload)
    return rows


def summarize_text(video: dict[str, Any], limit: int = 160) -> str:
    base = " ".join(
        str(video.get(key, "")).strip()
        for key in ("title", "description", "initial_transcript")
        if str(video.get(key, "")).strip()
    )
    if len(base) <= limit:
        return base
    return base[: limit - 1].rstrip() + "..."


def next_promoted_shape(default_depth: str, default_polish: str) -> tuple[str, str]:
    if default_depth in TARGET_DEPTH_VALUES:
        depth_index = TARGET_DEPTH_VALUES.index(default_depth)
        if depth_index < len(TARGET_DEPTH_VALUES) - 1:
            return TARGET_DEPTH_VALUES[depth_index + 1], default_polish
    if default_polish in TARGET_POLISH_VALUES:
        polish_index = TARGET_POLISH_VALUES.index(default_polish)
        if polish_index < len(TARGET_POLISH_VALUES) - 1:
            return default_depth, TARGET_POLISH_VALUES[polish_index + 1]
    return "Transcript", "editorial"


def heuristic_decision(channel: dict[str, Any], video: dict[str, Any]) -> dict[str, Any]:
    text = " ".join(str(video.get(key, "")).lower() for key in ("title", "description", "initial_transcript"))
    priority_band = str(channel.get("priority_band", "Tier 3"))
    default_depth = str(channel.get("default_compression", "Precis"))
    default_polish = str(channel.get("default_polish", "charitable"))

    if any(term in text for term in ("live debate", "live demo", "hearing", "cross-examination")):
        return {
            "decision": "Flag-for-Primary",
            "target_depth": "Transcript",
            "target_polish": "clean_verbatim",
            "rationale": "Live or adversarial dynamics create signal that compression will likely erase.",
            "primary_flag_reason": "Original viewing is required because interaction dynamics carry the signal.",
        }

    if any(term in text for term in ("architecture", "tpu", "alphafold", "gemini", "breakthrough", "roadmap", "release")):
        promoted_depth, promoted_polish = next_promoted_shape(default_depth, default_polish)
        if priority_band in {"Tier 1", "Tier 2"} and (
            promoted_depth != default_depth or promoted_polish != default_polish
        ):
            return {
                "decision": "Promote",
                "target_depth": promoted_depth,
                "target_polish": promoted_polish,
                "rationale": "Architecture or platform-shift language suggests non-routine signal worth escalation.",
                "primary_flag_reason": None,
            }
        return {
            "decision": "Compress",
            "target_depth": default_depth,
            "target_polish": default_polish,
            "rationale": "Architecture or platform-shift language is useful but remains compressible at the channel default.",
            "primary_flag_reason": None,
        }

    if any(term in text for term in ("walkthrough", "tutorial", "implementation", "tokenizer", "backpropagation")):
        return {
            "decision": "Compress",
            "target_depth": default_depth,
            "target_polish": default_polish,
            "rationale": "Implementation-oriented material is useful but remains compressible at the channel default.",
            "primary_flag_reason": None,
        }

    if priority_band == "Tier 1":
        return {
            "decision": "Headline",
            "target_depth": "Headline",
            "target_polish": "clean_verbatim",
            "rationale": "Tier 1 channel activity is worth logging even when novelty is not yet proven.",
            "primary_flag_reason": None,
        }

    return {
        "decision": "Skip",
        "target_depth": "None",
        "target_polish": "clean_verbatim",
        "rationale": "No strong novelty markers were detected in the available metadata.",
        "primary_flag_reason": None,
    }


def packet_sha256(packet: dict[str, Any]) -> str:
    digest = hashlib.sha256(
        json.dumps(packet, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    ).hexdigest()
    return f"sha256:{digest}"


def normalize_sha256(value: str | None) -> str | None:
    if value is None:
        return None
    if value.startswith("sha256:"):
        return value
    return f"sha256:{value}"


def queue_existing_ids(queue_rows: list[dict[str, Any]]) -> set[str]:
    existing: set[str] = set()
    for row in queue_rows:
        video_id = str(row.get("video_id", "")).strip()
        if video_id:
            existing.add(video_id)
    return existing


def scalarize_mapping(payload: dict[str, Any]) -> dict[str, int | float | str | bool | None]:
    sanitized: dict[str, int | float | str | bool | None] = {}
    for key, value in payload.items():
        if isinstance(value, (int, float, str, bool)) or value is None:
            sanitized[str(key)] = value
    return sanitized


def classify_gemini_failure(message: str) -> str:
    if "Missing Gemini API key" in message:
        return "missing_api_key"
    if "Prompt budget exceeded before invocation" in message:
        return "prompt_budget_exceeded"
    if "Token budget exceeded" in message:
        return "token_budget_exceeded"
    if "transport failure" in message:
        return "transport_failure"
    if "decision failed contract validation" in message:
        return "decision_contract_failure"
    if "malformed JSON decision" in message:
        return "malformed_model_output"
    if "HTTP " in message:
        return "provider_http_error"
    return "gemini_error"


def build_model_call_payload(
    *,
    provider: str,
    model: str,
    mode: str,
    channel_id: str,
    video_id: str,
    packet_id: str | None,
    packet_path: Path | None,
    packet_sha256: str | None,
    input_summary: str | None,
    outcome: dict[str, Any],
    response_sha256: str | None,
    structured_output: dict[str, Any] | None,
    usage: dict[str, Any] | None = None,
    cost: dict[str, Any] | None = None,
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "provider": provider,
        "model": model,
        "operation": "acumen_triage",
        "request_context": {
            "channel_id": channel_id,
            "video_id": video_id,
            "mode": mode,
        },
        "response_capture": {
            "policy": "metadata_only",
            "response_sha256": normalize_sha256(response_sha256),
            "structured_output_sha256": sha256_for_payload(structured_output) if structured_output is not None else None,
            "schema_valid": bool(structured_output) and outcome.get("status") == "success",
        },
        "usage": scalarize_mapping(usage or {}),
        "cost": scalarize_mapping(cost or {}),
        "outcome": outcome,
    }
    if packet_id:
        payload["request_context"]["packet_id"] = packet_id
    if packet_path is not None:
        payload["packet_path"] = str(packet_path)
    if packet_sha256 is not None:
        payload["packet_sha256"] = packet_sha256
    if input_summary is not None:
        payload["input_summary"] = input_summary
    return payload


def sync_runtime_surface(authoritative_path: Path, requested_path: Path) -> None:
    if authoritative_path == requested_path:
        return
    rows = load_evidence_jsonl(authoritative_path)
    write_evidence_jsonl(requested_path, rows)


def classify_failure(row: dict[str, Any]) -> tuple[str, str]:
    status = str(row.get("status", "")).strip() or "failed"
    mode = str(row.get("mode", "")).strip()
    reason = str(row.get("reason", "")).strip()

    if status == "invalid_input" or reason == "invalid_input":
        return "input_contract", "invalid_input"
    if reason == "budget_guardrail":
        return "guardrail", "budget_guardrail"
    if reason == "missing_api_key":
        return "credential", "missing_api_key"
    if reason in {"prompt_budget_exceeded", "token_budget_exceeded"}:
        return "guardrail", reason
    if mode != "gemini":
        return "input_contract", reason or status
    if reason in {"provider_http_error", "transport_failure"}:
        return "external_service", reason
    if reason in {"decision_contract_failure", "malformed_model_output", "gemini_error"}:
        return "external_service", reason
    return "external_service", reason or status or "failed"


def summarize_failures(rows: list[dict[str, Any]]) -> dict[str, Any] | None:
    failed_rows = [row for row in rows if str(row.get("status", "")).strip() not in {"", "ok"}]
    if not failed_rows:
        return None

    domains: dict[str, int] = {}
    codes: dict[str, int] = {}
    samples: list[dict[str, Any]] = []
    for row in failed_rows:
        domain, code = classify_failure(row)
        domains[domain] = domains.get(domain, 0) + 1
        codes[code] = codes.get(code, 0) + 1
        if len(samples) < 3:
            samples.append(
                {
                    "channel_id": row.get("channel_id"),
                    "message": row.get("reason") or row.get("status"),
                    "packet_id": row.get("packet_id"),
                    "code": code,
                    "domain": domain,
                    "video_id": row.get("video_id"),
                }
            )

    first = samples[0]
    return {
        "codes": codes,
        "domains": domains,
        "count": len(failed_rows),
        "failure_code": first["code"],
        "failure_domain": first["domain"],
        "failure_message": first["message"],
        "samples": samples,
    }


def main() -> int:
    args = parse_args()
    registry_path = Path(args.registry).expanduser().resolve()
    poll_path = Path(args.poll_jsonl).expanduser().resolve()
    queue_path = Path(args.queue_jsonl).expanduser().resolve()
    training_path = Path(args.training_jsonl).expanduser().resolve()
    status_path = Path(args.status_json).expanduser().resolve()
    artifact_dir = Path(args.artifact_dir).expanduser().resolve()
    authoritative_queue_path = TRIAGE_RUNTIME_PATH.resolve()
    authoritative_training_path = TRAINING_RUNTIME_PATH.resolve()
    actor = "acumen.triage"

    ensure_surface_files()
    registry = load_json(registry_path, {})
    poll_rows = load_jsonl(poll_path)
    existing_ids = queue_existing_ids(load_evidence_jsonl(authoritative_queue_path))

    artifact_dir.mkdir(parents=True, exist_ok=True)
    packet_dir = artifact_dir / "packets"
    prompt_dir = artifact_dir / "prompts"
    packet_dir.mkdir(parents=True, exist_ok=True)
    prompt_dir.mkdir(parents=True, exist_ok=True)

    training_rows: list[dict[str, Any]] = []
    queued = 0
    training_records = 0
    failures = 0
    skipped_existing = 0
    gemini_calls = 0
    estimated_cost = 0.0
    gemini_available = bool(os.environ.get(args.api_key_env, "").strip())

    for video in poll_rows:
        video_id = str(video.get("video_id", "")).strip()
        channel_id = str(video.get("channel_id", "")).strip()
        if video_id and video_id in existing_ids:
            skipped_existing += 1
            continue

        try:
            channel = resolve_channel(registry, channel_id)
            packet = build_triage_packet(registry, channel_id, video)
        except SystemExit as exc:
            failures += 1
            model_event = record_model_call_payload(
                build_model_call_payload(
                    provider="local",
                    model="input-contract",
                    mode=args.mode,
                    channel_id=channel_id,
                    video_id=video_id,
                    packet_id=None,
                    packet_path=None,
                    packet_sha256=None,
                    input_summary=summarize_text(video),
                    outcome={
                        "status": "failure",
                        "reason": "invalid_input",
                        "error_class": type(exc).__name__,
                    },
                    response_sha256=None,
                    structured_output=None,
                    usage={"attempts": 0},
                    cost={"estimated_usd": 0.0},
                ),
                actor,
                rematerialize=False,
            )
            training_records += 1
            training_rows.append(
                {
                    "captured_at": utc_now(),
                    "call_event_id": model_event["event_id"],
                    "video_id": video_id,
                    "channel_id": channel_id,
                    "mode": args.mode,
                    "model": "input-contract",
                    "status": "invalid_input",
                    "reason": "invalid_input",
                }
            )
            continue

        packet_name = video_id or packet["packet_id"]
        packet_path = write_json(packet_dir / f"{packet_name}.json", packet)
        prompt_preview = render_prompt_preview(packet)
        prompt_path = prompt_dir / f"{packet_name}.md"
        prompt_path.write_text(prompt_preview, encoding="utf-8")
        packet_digest = packet_sha256(packet)
        input_summary = summarize_text(video)

        active_mode = args.mode
        if active_mode == "auto":
            active_mode = "gemini" if gemini_available else "heuristic"

        live_allowed = (
            active_mode == "gemini"
            and gemini_calls < args.max_live_calls
            and (
                args.max_estimated_cost_usd <= 0
                or estimated_cost + args.estimated_cost_per_call_usd <= args.max_estimated_cost_usd
            )
        )

        if active_mode == "gemini" and not live_allowed:
            if args.mode == "gemini":
                failures += 1
                model_event = record_model_call_payload(
                    build_model_call_payload(
                        provider="google",
                        model=args.model,
                        mode="gemini",
                        channel_id=channel_id,
                        video_id=video_id,
                        packet_id=packet["packet_id"],
                        packet_path=packet_path,
                        packet_sha256=packet_digest,
                        input_summary=input_summary,
                        outcome={
                            "status": "failure",
                            "reason": "budget_guardrail",
                            "error_class": "GuardrailBlocked",
                        },
                        response_sha256=None,
                        structured_output=None,
                        usage={"attempts": 0},
                        cost={
                            "estimated_usd": round(estimated_cost, 6),
                            "estimated_cost_per_call_usd": args.estimated_cost_per_call_usd,
                        },
                    ),
                    actor,
                    rematerialize=False,
                )
                training_records += 1
                training_rows.append(
                    {
                        "captured_at": utc_now(),
                        "call_event_id": model_event["event_id"],
                        "packet_id": packet["packet_id"],
                        "video_id": video_id,
                        "channel_id": channel_id,
                        "model": args.model,
                        "mode": "gemini",
                        "status": "skipped_budget_guardrail",
                        "reason": "budget_guardrail",
                        "estimated_cost_usd": round(estimated_cost, 6),
                    }
                )
                continue
            active_mode = "heuristic"

        if active_mode == "gemini":
            try:
                result = invoke_gemini_packet(
                    packet,
                    model=args.model,
                    api_base=args.api_base,
                    api_key_env=args.api_key_env,
                    timeout_seconds=args.timeout_seconds,
                    max_attempts=args.max_retries + 1,
                    retry_backoff_seconds=args.retry_backoff_seconds,
                    max_prompt_chars=args.max_prompt_chars,
                    max_output_tokens=args.max_output_tokens,
                    max_total_tokens=args.max_total_tokens,
                )
                budget_guardrails = dict(result["budget_guardrails"])
                budget_guardrails["max_live_calls"] = args.max_live_calls
                budget_guardrails["estimated_cost_per_call_usd"] = args.estimated_cost_per_call_usd
                budget_guardrails["max_estimated_cost_usd"] = args.max_estimated_cost_usd
                record = build_decision_record(
                    packet,
                    result["decision"],
                    model=args.model,
                    attempts_used=result["attempts_used"],
                    prompt_chars=result["prompt_chars"],
                    usage_metadata=result["usage_metadata"],
                    budget_guardrails=budget_guardrails,
                    source_mode="gemini",
                    abstract=input_summary,
                )
                model_event = record_model_call_payload(
                    build_model_call_payload(
                        provider="google",
                        model=args.model,
                        mode="gemini",
                        channel_id=channel_id,
                        video_id=video_id,
                        packet_id=packet["packet_id"],
                        packet_path=packet_path,
                        packet_sha256=packet_digest,
                        input_summary=input_summary,
                        outcome={
                            "status": "success",
                            "decision": record["decision"],
                            "reason": None,
                        },
                        response_sha256=result["response_sha256"],
                        structured_output=result["decision"],
                        usage={
                            "attempts": result["attempts_used"],
                            **scalarize_mapping(result["usage_metadata"]),
                        },
                        cost={"estimated_usd": args.estimated_cost_per_call_usd},
                    ),
                    actor,
                    rematerialize=False,
                )
                training_records += 1
                decision_event = record_decision_payload(
                    {
                        **record,
                        "model_call_event_id": model_event["event_id"],
                        "packet_path": str(packet_path),
                        "packet_sha256": packet_digest,
                        "input_summary": input_summary,
                    },
                    actor,
                    rematerialize=False,
                )
                queued += 1
                if video_id:
                    existing_ids.add(video_id)
                gemini_calls += 1
                estimated_cost += args.estimated_cost_per_call_usd
                training_rows.append(
                    {
                        "captured_at": utc_now(),
                        "call_event_id": model_event["event_id"],
                        "decision_event_id": decision_event["event_id"],
                        "packet_id": packet["packet_id"],
                        "video_id": video_id,
                        "channel_id": channel_id,
                        "model": args.model,
                        "mode": "gemini",
                        "status": "ok",
                        "attempts": result["attempts_used"],
                        "reason": "",
                        "decision": record["decision"],
                        "target_depth": record["target_depth"],
                        "target_polish": record["target_polish"],
                        "estimated_cost_usd": args.estimated_cost_per_call_usd,
                    }
                )
                continue
            except GeminiTriageError as exc:
                failures += 1
                reason = classify_gemini_failure(str(exc))
                model_event = record_model_call_payload(
                    build_model_call_payload(
                        provider="google",
                        model=args.model,
                        mode="gemini",
                        channel_id=channel_id,
                        video_id=video_id,
                        packet_id=packet["packet_id"],
                        packet_path=packet_path,
                        packet_sha256=packet_digest,
                        input_summary=input_summary,
                        outcome={
                            "status": "failure",
                            "reason": reason,
                            "error_class": type(exc).__name__,
                        },
                        response_sha256=None,
                        structured_output=None,
                        usage={"attempts_requested": args.max_retries + 1},
                        cost={"estimated_usd": 0.0},
                    ),
                    actor,
                    rematerialize=False,
                )
                training_records += 1
                training_rows.append(
                    {
                        "captured_at": utc_now(),
                        "call_event_id": model_event["event_id"],
                        "packet_id": packet["packet_id"],
                        "video_id": video_id,
                        "channel_id": channel_id,
                        "model": args.model,
                        "mode": "gemini",
                        "status": "failed",
                        "reason": reason,
                        "attempts": args.max_retries + 1,
                    }
                )
                continue

        payload = heuristic_decision(channel, video)
        errors = validate_decision(packet, payload)
        if errors:
            failures += 1
            model_event = record_model_call_payload(
                build_model_call_payload(
                    provider="local",
                    model="deterministic-heuristic",
                    mode="heuristic",
                    channel_id=channel_id,
                    video_id=video_id,
                    packet_id=packet["packet_id"],
                    packet_path=packet_path,
                    packet_sha256=packet_digest,
                    input_summary=input_summary,
                    outcome={
                        "status": "failure",
                        "reason": "decision_contract_failure",
                        "error_class": "DecisionValidationError",
                    },
                    response_sha256=None,
                    structured_output=payload,
                    usage={"attempts": 0},
                    cost={"estimated_usd": 0.0},
                ),
                actor,
                rematerialize=False,
            )
            training_records += 1
            training_rows.append(
                {
                    "captured_at": utc_now(),
                    "call_event_id": model_event["event_id"],
                    "packet_id": packet["packet_id"],
                    "video_id": video_id,
                    "channel_id": channel_id,
                    "model": "deterministic-heuristic",
                    "mode": "heuristic",
                    "status": "failed",
                    "reason": "decision_contract_failure",
                }
            )
            continue

        record = build_decision_record(
            packet,
            payload,
            model="heuristic",
            attempts_used=0,
            prompt_chars=len(prompt_preview),
            usage_metadata={},
            budget_guardrails={
                "mode": "heuristic",
                "max_live_calls": args.max_live_calls,
                "estimated_cost_per_call_usd": args.estimated_cost_per_call_usd,
                "max_estimated_cost_usd": args.max_estimated_cost_usd,
            },
            source_mode="heuristic",
            abstract=input_summary,
        )
        model_event = record_model_call_payload(
            build_model_call_payload(
                provider="local",
                model="deterministic-heuristic",
                mode="heuristic",
                channel_id=channel_id,
                video_id=video_id,
                packet_id=packet["packet_id"],
                packet_path=packet_path,
                packet_sha256=packet_digest,
                input_summary=input_summary,
                outcome={
                    "status": "success",
                    "decision": record["decision"],
                    "reason": None,
                },
                response_sha256=None,
                structured_output=payload,
                usage={"attempts": 0},
                cost={"estimated_usd": 0.0},
            ),
            actor,
            rematerialize=False,
        )
        training_records += 1
        decision_event = record_decision_payload(
            {
                **record,
                "model_call_event_id": model_event["event_id"],
                "packet_path": str(packet_path),
                "packet_sha256": packet_digest,
                "input_summary": input_summary,
            },
            actor,
            rematerialize=False,
        )
        queued += 1
        if video_id:
            existing_ids.add(video_id)
        training_rows.append(
            {
                "captured_at": utc_now(),
                "call_event_id": model_event["event_id"],
                "decision_event_id": decision_event["event_id"],
                "packet_id": packet["packet_id"],
                "video_id": video_id,
                "channel_id": channel_id,
                "model": "deterministic-heuristic",
                "mode": "heuristic",
                "status": "ok",
                "reason": "",
                "attempts": 0,
                "decision": record["decision"],
                "target_depth": record["target_depth"],
                "target_polish": record["target_polish"],
            }
        )

    rematerialize_runtime()
    sync_runtime_surface(authoritative_queue_path, queue_path)
    sync_runtime_surface(authoritative_training_path, training_path)

    failure_summary = summarize_failures(training_rows)

    status = {
        "captured_at": utc_now(),
        "registry": str(registry_path),
        "poll_jsonl": str(poll_path),
        "queue_jsonl": str(authoritative_queue_path),
        "training_jsonl": str(authoritative_training_path),
        "requested_queue_jsonl": str(queue_path),
        "requested_training_jsonl": str(training_path),
        "artifact_dir": str(artifact_dir),
        "mode": args.mode,
        "processed": len(poll_rows),
        "queued": queued,
        "training_records": training_records,
        "failures": failures,
        "skipped_existing": skipped_existing,
        "ok": failures == 0,
        "runtime_surface_authority": {
            "triage_runtime": str(authoritative_queue_path),
            "training_runtime": str(authoritative_training_path),
            "triage_runtime_mirrored_to_requested_path": authoritative_queue_path != queue_path,
            "training_runtime_mirrored_to_requested_path": authoritative_training_path != training_path,
        },
        "external_dependencies": {
            "gemini_api": {
                "required": args.mode == "gemini" or (args.mode == "auto" and gemini_available),
                "available": gemini_available,
                "api_key_env": args.api_key_env,
                "api_base": args.api_base,
                "model": args.model,
                "calls_used": gemini_calls,
                "max_live_calls": args.max_live_calls,
                "estimated_cost_usd": round(estimated_cost, 6),
                "estimated_cost_per_call_usd": args.estimated_cost_per_call_usd,
                "max_estimated_cost_usd": args.max_estimated_cost_usd,
                "timeout_seconds": args.timeout_seconds,
                "max_attempts_per_call": args.max_retries + 1,
                "max_prompt_chars": args.max_prompt_chars,
                "max_output_tokens": args.max_output_tokens,
                "max_total_tokens": args.max_total_tokens,
            }
        },
    }
    if failure_summary is not None:
        status["failure_code"] = failure_summary["failure_code"]
        status["failure_domain"] = failure_summary["failure_domain"]
        status["failure_message"] = failure_summary["failure_message"]
        status["failure_summary"] = failure_summary
    status_path.parent.mkdir(parents=True, exist_ok=True)
    status_path.write_text(json.dumps(status, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(authoritative_queue_path)
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
