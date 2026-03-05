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


def utc_now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def coerce_signal_density(hit_rate: float) -> str:
    if hit_rate > 0.7:
        return "high"
    if hit_rate >= 0.3:
        return "medium"
    return "low"


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
