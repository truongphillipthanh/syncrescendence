#!/usr/bin/env python3
"""Feed Registry contract for the Acumen pipeline."""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Any


GENRES = {"Bulletin", "Deep Dive", "Commentary", "Tutorial", "Explainer", "Institutional", "Frontier"}
CADENCES = {"daily", "weekly", "biweekly", "monthly", "irregular"}
DEPTHS = {"Headline", "Abstract", "Precis", "Synopsis", "Blueprint", "Treatment", "Transcript"}
POLISH_LEVELS = {"clean_verbatim", "charitable", "editorial"}
SIGNAL_DENSITIES = {"high", "medium", "low"}
VISUAL_DEPENDENCY = {"none", "low", "high"}
VOICE_NORMALIZATION = {"original", "normalize", "flag_per_episode"}
CHAIN_ALIGNMENTS = {"Intelligence", "Information", "Insight", "Expertise", "Knowledge", "Wisdom"}
PRIORITY_BANDS = {"Tier 1", "Tier 2", "Tier 3"}
PORTFOLIO_ROLES = {"core_monitored", "selective_monitored", "event_surge", "primary_only_witness"}
SOURCE_ACCOUNTS = {"acumen", "coherence", "efficacy", "mastery", "transcendence"}
DOWNSTREAM_CHAIN_CONSUMER_ROLES = {
    "coherence_synthesis",
    "efficacy_execution",
    "mastery_curriculum",
    "transcendence_governance",
}
CADENCE_ORDER = {
    "daily": 0,
    "weekly": 1,
    "biweekly": 2,
    "monthly": 3,
    "irregular": 4,
}
ROLE_CADENCE_CEILINGS = {
    "core_monitored": "daily",
    "selective_monitored": "weekly",
    "event_surge": "weekly",
    "primary_only_witness": "monthly",
}
ROLE_MAX_ITEMS_PER_POLL = {
    "core_monitored": 5,
    "selective_monitored": 3,
    "event_surge": 2,
    "primary_only_witness": 1,
}
ROLE_MONTHLY_NEW_ITEM_BUDGET = {
    "core_monitored": 40,
    "selective_monitored": 16,
    "event_surge": 8,
    "primary_only_witness": 4,
}


def utc_now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def coerce_signal_density(hit_rate: float) -> str:
    if hit_rate > 0.7:
        return "high"
    if hit_rate >= 0.3:
        return "medium"
    return "low"


def _coerce_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    text = str(value).strip()
    if not text:
        return []
    return [text]


def cadence_is_more_aggressive(actual: str, ceiling: str) -> bool:
    return CADENCE_ORDER.get(actual, CADENCE_ORDER["irregular"]) < CADENCE_ORDER.get(ceiling, CADENCE_ORDER["irregular"])


def policy_view(channel: dict[str, Any]) -> dict[str, Any]:
    admission = channel.get("admission")
    if not isinstance(admission, dict):
        admission = {}
    poll_budget = channel.get("poll_budget")
    if not isinstance(poll_budget, dict):
        poll_budget = {}

    portfolio_role = str(channel.get("portfolio_role", "")).strip()
    source_account = str(admission.get("source_account", channel.get("source_account", ""))).strip()
    intake_plane = str(admission.get("intake_plane", channel.get("intake_plane", ""))).strip()
    manifest_refs = _coerce_list(admission.get("curated_manifest_refs", channel.get("curated_manifest_refs")))
    consumer_roles = _coerce_list(
        channel.get("downstream_chain_consumer_roles", channel.get("downstream_consumer_roles"))
    )
    max_items_per_poll = poll_budget.get("max_items_per_poll", channel.get("max_items_per_poll"))
    monthly_new_item_budget = poll_budget.get("monthly_new_item_budget", channel.get("monthly_new_item_budget"))
    event_window_active = bool(poll_budget.get("event_window_active", channel.get("event_window_active", False)))

    policy_fields_present = any(
        [
            "portfolio_role" in channel,
            "downstream_chain_consumer_roles" in channel,
            "downstream_consumer_roles" in channel,
            "admission" in channel,
            "source_account" in channel,
            "curated_manifest_refs" in channel,
            "poll_budget" in channel,
            "max_items_per_poll" in channel,
            "monthly_new_item_budget" in channel,
            "event_window_active" in channel,
        ]
    )

    return {
        "policy_fields_present": policy_fields_present,
        "portfolio_role": portfolio_role,
        "source_account": source_account,
        "intake_plane": intake_plane,
        "curated_manifest_refs": manifest_refs,
        "downstream_chain_consumer_roles": consumer_roles,
        "max_items_per_poll": max_items_per_poll,
        "monthly_new_item_budget": monthly_new_item_budget,
        "event_window_active": event_window_active,
    }


def policy_findings(channel: dict[str, Any], *, require_explicit: bool) -> list[str]:
    findings: list[str] = []
    channel_id = str(channel.get("channel_id", "<missing>"))
    policy = policy_view(channel)
    policy_fields_present = bool(policy["policy_fields_present"])

    if not policy_fields_present and not require_explicit:
        return findings

    portfolio_role = str(policy["portfolio_role"])
    source_account = str(policy["source_account"])
    intake_plane = str(policy["intake_plane"])
    manifest_refs = list(policy["curated_manifest_refs"])
    consumer_roles = list(policy["downstream_chain_consumer_roles"])
    cadence = str(channel.get("cadence", "irregular"))
    signal_density = str(channel.get("signal_density", ""))
    visual_dependency = str(channel.get("visual_dependency", ""))
    default_compression = str(channel.get("default_compression", ""))

    if not portfolio_role:
        findings.append(f"{channel_id}: missing explicit portfolio_role")
    elif portfolio_role not in PORTFOLIO_ROLES:
        findings.append(f"{channel_id}: portfolio_role={portfolio_role!r} not in {sorted(PORTFOLIO_ROLES)}")

    if not source_account:
        findings.append(f"{channel_id}: missing admission.source_account")
    elif source_account not in SOURCE_ACCOUNTS:
        findings.append(f"{channel_id}: source_account={source_account!r} not in {sorted(SOURCE_ACCOUNTS)}")

    if intake_plane != "acumen":
        findings.append(f"{channel_id}: intake_plane must remain 'acumen', got {intake_plane!r}")

    if not manifest_refs:
        findings.append(f"{channel_id}: missing curated inbound manifest refs")

    if not consumer_roles:
        findings.append(f"{channel_id}: missing downstream_chain_consumer_roles")
    else:
        invalid_consumer_roles = [item for item in consumer_roles if item not in DOWNSTREAM_CHAIN_CONSUMER_ROLES]
        if invalid_consumer_roles:
            findings.append(
                f"{channel_id}: downstream_chain_consumer_roles contain invalid values {invalid_consumer_roles!r}"
            )

    max_items_per_poll = policy.get("max_items_per_poll")
    monthly_new_item_budget = policy.get("monthly_new_item_budget")
    try:
        max_items = int(max_items_per_poll)
        if max_items <= 0:
            raise ValueError
    except Exception:
        findings.append(f"{channel_id}: poll_budget.max_items_per_poll must be a positive integer")
        max_items = None

    try:
        monthly_budget = int(monthly_new_item_budget)
        if monthly_budget <= 0:
            raise ValueError
    except Exception:
        findings.append(f"{channel_id}: poll_budget.monthly_new_item_budget must be a positive integer")
        monthly_budget = None

    if portfolio_role in ROLE_CADENCE_CEILINGS and cadence_is_more_aggressive(cadence, ROLE_CADENCE_CEILINGS[portfolio_role]):
        findings.append(
            f"{channel_id}: cadence={cadence!r} exceeds {portfolio_role} ceiling {ROLE_CADENCE_CEILINGS[portfolio_role]!r}"
        )

    if portfolio_role in ROLE_MAX_ITEMS_PER_POLL and max_items is not None and max_items > ROLE_MAX_ITEMS_PER_POLL[portfolio_role]:
        findings.append(
            f"{channel_id}: max_items_per_poll={max_items} exceeds {portfolio_role} cap {ROLE_MAX_ITEMS_PER_POLL[portfolio_role]}"
        )

    if (
        portfolio_role in ROLE_MONTHLY_NEW_ITEM_BUDGET
        and monthly_budget is not None
        and monthly_budget > ROLE_MONTHLY_NEW_ITEM_BUDGET[portfolio_role]
    ):
        findings.append(
            f"{channel_id}: monthly_new_item_budget={monthly_budget} exceeds {portfolio_role} cap {ROLE_MONTHLY_NEW_ITEM_BUDGET[portfolio_role]}"
        )

    try:
        triage_hit_rate = float(channel.get("triage_hit_rate", 0.0))
    except Exception:
        triage_hit_rate = 0.0

    if portfolio_role == "core_monitored":
        if signal_density == "low":
            findings.append(f"{channel_id}: core_monitored cannot run with low signal_density")
        if visual_dependency == "high":
            findings.append(f"{channel_id}: core_monitored cannot treat high-visual sources as routine intake")
        if triage_hit_rate < 0.35:
            findings.append(f"{channel_id}: core_monitored requires triage_hit_rate >= 0.35, got {triage_hit_rate:.2f}")

    if portfolio_role == "selective_monitored" and cadence == "daily":
        findings.append(f"{channel_id}: selective_monitored cannot run on daily cadence")

    if portfolio_role == "event_surge":
        event_window_active = bool(policy.get("event_window_active"))
        if not event_window_active and cadence_is_more_aggressive(cadence, "monthly"):
            findings.append(f"{channel_id}: inactive event_surge feeds must stay at monthly or irregular cadence")

    if portfolio_role == "primary_only_witness":
        if visual_dependency != "high":
            findings.append(f"{channel_id}: primary_only_witness requires visual_dependency='high'")
        if default_compression not in {"Treatment", "Transcript"}:
            findings.append(
                f"{channel_id}: primary_only_witness requires default_compression in ['Treatment', 'Transcript']"
            )

    if visual_dependency == "high" and portfolio_role not in {"event_surge", "primary_only_witness"}:
        findings.append(f"{channel_id}: high-visual sources must be event_surge or primary_only_witness")

    return findings


def default_channel(seed: dict[str, Any]) -> dict[str, Any]:
    hit_rate = float(seed.get("triage_hit_rate", 0.5))
    return {
        "channel_id": str(seed["channel_id"]),
        "name": str(seed["name"]),
        "genre": seed.get("genre", "Commentary"),
        "cadence": seed.get("cadence", "irregular"),
        "default_compression": seed.get("default_compression", "Precis"),
        "default_polish": seed.get("default_polish", "charitable"),
        "signal_density": seed.get("signal_density", coerce_signal_density(hit_rate)),
        "visual_dependency": seed.get("visual_dependency", "low"),
        "voice_normalization": seed.get("voice_normalization", "normalize"),
        "domain_tags": list(seed.get("domain_tags", [])),
        "chain_alignment": seed.get("chain_alignment", "Insight"),
        "resolution_vocabulary": list(seed.get("resolution_vocabulary", [])),
        "priority_band": seed.get("priority_band", "Tier 2"),
        "triage_hit_rate": hit_rate,
        "last_processed": seed.get("last_processed", utc_now()),
        "notes": seed.get("notes", ""),
    }


def _expect_enum(errors: list[str], channel_id: str, field: str, value: Any, allowed: set[str]) -> None:
    if value not in allowed:
        errors.append(f"{channel_id}: field {field!r}={value!r} not in {sorted(allowed)}")


def validate_channel(channel: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    channel_id = str(channel.get("channel_id", "<missing>"))

    required = {
        "channel_id",
        "name",
        "genre",
        "cadence",
        "default_compression",
        "default_polish",
        "signal_density",
        "visual_dependency",
        "voice_normalization",
        "domain_tags",
        "chain_alignment",
        "resolution_vocabulary",
        "priority_band",
        "triage_hit_rate",
        "last_processed",
        "notes",
    }
    missing = sorted(required - set(channel.keys()))
    if missing:
        errors.append(f"{channel_id}: missing required fields {missing}")
        return errors

    _expect_enum(errors, channel_id, "genre", channel["genre"], GENRES)
    _expect_enum(errors, channel_id, "cadence", channel["cadence"], CADENCES)
    _expect_enum(errors, channel_id, "default_compression", channel["default_compression"], DEPTHS)
    _expect_enum(errors, channel_id, "default_polish", channel["default_polish"], POLISH_LEVELS)
    _expect_enum(errors, channel_id, "signal_density", channel["signal_density"], SIGNAL_DENSITIES)
    _expect_enum(errors, channel_id, "visual_dependency", channel["visual_dependency"], VISUAL_DEPENDENCY)
    _expect_enum(errors, channel_id, "voice_normalization", channel["voice_normalization"], VOICE_NORMALIZATION)
    _expect_enum(errors, channel_id, "chain_alignment", channel["chain_alignment"], CHAIN_ALIGNMENTS)
    _expect_enum(errors, channel_id, "priority_band", channel["priority_band"], PRIORITY_BANDS)

    if not isinstance(channel["domain_tags"], list):
        errors.append(f"{channel_id}: domain_tags must be a list")
    if not isinstance(channel["resolution_vocabulary"], list):
        errors.append(f"{channel_id}: resolution_vocabulary must be a list")

    try:
        hit_rate = float(channel["triage_hit_rate"])
        if hit_rate < 0.0 or hit_rate > 1.0:
            errors.append(f"{channel_id}: triage_hit_rate must be in [0.0,1.0], got {hit_rate}")
    except Exception:
        errors.append(f"{channel_id}: triage_hit_rate must be numeric")

    if not str(channel["channel_id"]).strip():
        errors.append("channel_id must be non-empty")
    if not str(channel["name"]).strip():
        errors.append(f"{channel_id}: name must be non-empty")
    return errors


def validate_registry(registry: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if "channels" not in registry or not isinstance(registry["channels"], list):
        return ["registry requires top-level list field 'channels'"]

    seen: set[str] = set()
    for item in registry["channels"]:
        if not isinstance(item, dict):
            errors.append("registry channels entries must be objects")
            continue
        cid = str(item.get("channel_id", ""))
        if cid in seen:
            errors.append(f"duplicate channel_id: {cid}")
        seen.add(cid)
        errors.extend(validate_channel(item))
    return errors
