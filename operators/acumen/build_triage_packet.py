#!/usr/bin/env python3
"""Render the Gemini Flash triage packet from registry + video metadata."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


TRIAGE_PROMPT_TEMPLATE = """System: You are an intelligence triage engine for a personal knowledge pipeline monitoring
YouTube channels. Your job: determine whether this upload justifies the practitioner's
attention, and if so, at what compression depth and polish level.

Context from registry:
- Channel: {name} | Genre: {genre} | Priority: {priority_band}
- Default compression: {default_compression} | Default polish: {default_polish}
- Signal density: {signal_density}
- Domain tags: {domain_tags}
- Resolution vocabulary: {resolution_vocabulary}

Video metadata:
- Title: {title}
- Duration: {duration}
- Description: {description}
- First 60s transcript: {initial_transcript}

Output strictly valid JSON:
{{
  "decision": "Skip|Headline|Compress|Promote|Flag-for-Primary",
  "target_depth": "None|Headline|Abstract|Precis|Synopsis|Blueprint|Treatment|Transcript",
  "target_polish": "clean_verbatim|charitable|editorial",
  "rationale": "One sentence: why this decision, what signal was detected or absent.",
  "primary_flag_reason": "null unless Flag-for-Primary. Why must this be consumed in original form?"
}}

Decision rules:
1. Skip: Bulletin content restating existing news with no novel signal.
2. Headline: Low-signal content from medium/high-density channels worth logging.
3. Compress: Standard content processed at channel defaults.
4. Promote: Override defaults upward when a lower-tier channel hosts a Tier 1 guest,
   covers a paradigm shift, or produces unusually deep analysis.
5. Flag-for-Primary: Content where compression destroys signal — live debates with
   performative dynamics, hardware teardowns, visually dependent demonstrations,
   or events where the practitioner's own judgment is required.
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", required=True)
    parser.add_argument("--channel-id", required=True)
    parser.add_argument("--video", required=True, help="JSON object with title/duration/description/initial_transcript.")
    parser.add_argument("--output", required=True)
    return parser.parse_args()


def load_json(path: str) -> Any:
    return json.loads(Path(path).expanduser().read_text(encoding="utf-8"))


def resolve_channel(registry: dict[str, Any], channel_id: str) -> dict[str, Any]:
    for channel in registry.get("channels", []):
        if str(channel.get("channel_id")) == channel_id:
            return channel
    raise SystemExit(f"channel not found in registry: {channel_id}")


def main() -> int:
    args = parse_args()
    registry = load_json(args.registry)
    video = load_json(args.video)
    channel = resolve_channel(registry, args.channel_id)

    required_video = {"title", "duration", "description", "initial_transcript"}
    missing = required_video - set(video.keys())
    if missing:
        raise SystemExit(f"video metadata missing required keys: {sorted(missing)}")

    packet = TRIAGE_PROMPT_TEMPLATE.format(
        name=channel.get("name"),
        genre=channel.get("genre"),
        priority_band=channel.get("priority_band"),
        default_compression=channel.get("default_compression"),
        default_polish=channel.get("default_polish"),
        signal_density=channel.get("signal_density"),
        domain_tags=", ".join(channel.get("domain_tags", [])),
        resolution_vocabulary=", ".join(channel.get("resolution_vocabulary", [])),
        title=video["title"],
        duration=video["duration"],
        description=video["description"],
        initial_transcript=video["initial_transcript"],
    )

    output_path = Path(args.output).expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(packet, encoding="utf-8")
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
