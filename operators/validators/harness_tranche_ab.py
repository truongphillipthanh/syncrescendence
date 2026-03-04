#!/usr/bin/env python3
"""Ingest harness artifacts and build a graded command capability registry."""

from __future__ import annotations

import argparse
import json
import re
import shlex
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[2]
COMMUNICATIONS_DIR = REPO_ROOT / "communications"
PROMPTS_DIR = COMMUNICATIONS_DIR / "prompts"
RESPONSES_DIR = COMMUNICATIONS_DIR / "responses"
ASSESSMENTS_DIR = COMMUNICATIONS_DIR / "assessments"
STATE_DIR = REPO_ROOT / "orchestration" / "state"
IMPL_DIR = STATE_DIR / "impl"

SEGMENT_SPLIT_RE = re.compile(r"\n\*\*\*\n")
INLINE_CODE_RE = re.compile(r"`([^`\n]{2,240})`")
FENCE_RE = re.compile(r"```[a-zA-Z0-9_-]*\n(.*?)\n```", re.DOTALL)
SPACE_RE = re.compile(r"\s+")

RUNTIME_PREFIXES = ("/", "$start", "$setup", "$skill-creator")
KNOWN_BIN_PREFIXES = (
    "codex ",
    "aider ",
    "gemini ",
    "opencode ",
    "openclaw ",
    "openhands ",
    "helm ",
    "skills.sh ",
    "python ",
    "curl ",
    "git ",
    "npm ",
    "go ",
    "jq ",
)

FIRST_PARTY_MARKERS = (
    "developers.openai.com",
    "aider.chat/docs",
    "docs.openclaw.ai",
    "docs.openhands.dev",
    "opencode.ai/docs",
    "github.com/openai/codex",
    "github.com/aider-ai/aider",
    "github.com/openclaw/openclaw",
    "github.com/all-hands-ai/openhands",
    "github.com/anomalyco/opencode",
    "github.com/google-gemini/gemini-cli",
)
COMMUNITY_MARKERS = ("reddit", "hn", "discord", "x ", "x.com", "youtube", "github issue")

HARNESS_TERMS: dict[str, tuple[str, ...]] = {
    "aider": ("aider", ".aider", "repomap", "architect"),
    "claude_code": ("claude code", "claude.md", "anthropic", ".claude"),
    "codex": ("codex", "ag ents.md".replace(" ", ""), "config.toml", "developers.openai.com/codex"),
    "gemini_cli": ("gemini cli", "gemini.md", ".gemini", "geminicli"),
    "openclaw": ("openclaw", "ajna", "psyche", "gateway", ".openclaw"),
    "opencode": ("opencode", "opencode.json", ".opencode", "oh-my-opencode"),
    "openhands": ("openhands", "conversationstate", "eventlog", "condenser", "routerllm"),
}

PROMPT_RESIDUE_MARKERS = (
    "you are grok",
    "output structure only",
    "continue from the previous",
    "triangulate exclusively",
    "begin immediately",
    "no preambles",
)


@dataclass
class SegmentRecord:
    index: int
    text: str
    accepted: bool
    reason: str
    tier: str
    first_party_hits: int
    community_hits: int


@dataclass
class CommandProbe:
    harness: str
    source_file: str
    segment_index: int
    segment_accepted: bool
    segment_tier: str
    command: str
    binary: str | None
    status: str
    tier: str
    probe_cmd: str | None
    detail: str

    def as_dict(self) -> dict[str, object]:
        return {
            "harness": self.harness,
            "source_file": self.source_file,
            "segment_index": self.segment_index,
            "segment_accepted": self.segment_accepted,
            "segment_tier": self.segment_tier,
            "command": self.command,
            "binary": self.binary,
            "status": self.status,
            "tier": self.tier,
            "probe_cmd": self.probe_cmd,
            "detail": self.detail,
        }


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def normalize_spaces(value: str) -> str:
    return SPACE_RE.sub(" ", value.strip())


def is_prompt_residue(segment_text: str) -> bool:
    lowered = segment_text.lower()
    return any(marker in lowered for marker in PROMPT_RESIDUE_MARKERS)


def classify_segment(harness: str, segment_text: str) -> tuple[bool, str, str, int, int]:
    lowered = segment_text.lower()
    first_party_hits = sum(lowered.count(marker) for marker in FIRST_PARTY_MARKERS)
    community_hits = sum(lowered.count(marker) for marker in COMMUNITY_MARKERS)
    own_score = sum(lowered.count(term) for term in HARNESS_TERMS.get(harness, ()))
    other_score = 0
    for other, terms in HARNESS_TERMS.items():
        if other == harness:
            continue
        other_score += sum(lowered.count(term) for term in terms)

    if is_prompt_residue(segment_text):
        return False, "prompt_residue", "T3", first_party_hits, community_hits
    if own_score == 0 and other_score > 0:
        return False, "cross_harness_contamination", "T3", first_party_hits, community_hits
    if own_score == 0 and first_party_hits == 0 and community_hits == 0:
        return False, "weak_signal", "T3", first_party_hits, community_hits
    if first_party_hits > 0:
        return True, "accepted_first_party_anchored", "T1", first_party_hits, community_hits
    if community_hits > 0:
        return True, "accepted_community_anchored", "T2", first_party_hits, community_hits
    return True, "accepted_structural_signal", "T2", first_party_hits, community_hits


def segment_report(harness: str, text: str) -> list[SegmentRecord]:
    raw_segments = [s.strip() for s in SEGMENT_SPLIT_RE.split(text) if s.strip()]
    records: list[SegmentRecord] = []
    for idx, segment in enumerate(raw_segments, start=1):
        accepted, reason, tier, fp_hits, cm_hits = classify_segment(harness, segment)
        records.append(
            SegmentRecord(
                index=idx,
                text=segment,
                accepted=accepted,
                reason=reason,
                tier=tier,
                first_party_hits=fp_hits,
                community_hits=cm_hits,
            )
        )
    if records and not any(r.accepted for r in records):
        records[0].accepted = True
        records[0].reason = "forced_accept_no_other_survivor"
        records[0].tier = "T2"
    return records


def render_sanitized_report(harness: str, source_name: str, records: list[SegmentRecord]) -> str:
    lines = [
        f"# RESPONSE-GROK-cc79-harness-{harness}-sanitized",
        "",
        f"**Source**: `{source_name}`",
        "**Method**: segment-level sanitation for cross-harness contamination and prompt residue",
        "",
        "## Segment Classification",
        "",
    ]
    for rec in records:
        state = "accepted" if rec.accepted else "quarantined"
        lines.append(
            f"- segment {rec.index}: `{state}` | reason=`{rec.reason}` | tier=`{rec.tier}` "
            f"| first_party_hits={rec.first_party_hits} | community_hits={rec.community_hits}"
        )
    lines.extend(["", "## Accepted Segments", ""])
    for rec in records:
        if not rec.accepted:
            continue
        lines.extend(
            [
                f"### Segment {rec.index} (`{rec.tier}`)",
                "",
                rec.text,
                "",
            ]
        )
    lines.extend(["## Quarantined Segments", ""])
    quarantined = [r for r in records if not r.accepted]
    if not quarantined:
        lines.append("- none")
    else:
        for rec in quarantined:
            lines.append(f"- segment {rec.index}: `{rec.reason}`")
    return "\n".join(lines).rstrip() + "\n"


def iter_command_candidates(text: str) -> Iterable[str]:
    seen: set[str] = set()

    def emit(value: str) -> None:
        candidate = normalize_spaces(value.strip().strip(".,;"))
        if not candidate:
            return
        if candidate in seen:
            return
        if candidate.startswith("/") and not re.match(r"^/[A-Za-z]", candidate):
            return
        if candidate.startswith(RUNTIME_PREFIXES):
            seen.add(candidate)
            yield_list.append(candidate)
            return
        if candidate.startswith(KNOWN_BIN_PREFIXES):
            seen.add(candidate)
            yield_list.append(candidate)

    yield_list: list[str] = []
    for inline in INLINE_CODE_RE.findall(text):
        emit(inline)
    for block in FENCE_RE.findall(text):
        for line in block.splitlines():
            line = line.strip()
            if not line or line.startswith("#") or line.startswith("//") or line.startswith("/*") or line.startswith("*"):
                continue
            if line.startswith("$ "):
                line = line[2:].strip()
            emit(line)
    return yield_list


def safe_probe_command(command: str) -> tuple[str | None, str | None]:
    if command.startswith(RUNTIME_PREFIXES):
        return None, None
    if any(ch in command for ch in ("|", ">", "<", ";", "&&", "||")):
        return None, None
    try:
        tokens = shlex.split(command)
    except ValueError:
        return None, None
    if not tokens:
        return None, None
    binary = tokens[0]
    if len(tokens) == 1:
        return binary, f"{binary} --help"
    if tokens[1].startswith("-"):
        return binary, f"{binary} --help"
    return binary, f"{binary} {tokens[1]} --help"


def run_probe(probe_cmd: str) -> tuple[int, str]:
    try:
        proc = subprocess.run(
            probe_cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=1,
        )
    except subprocess.TimeoutExpired:
        return 124, "probe timeout"
    output = (proc.stdout + "\n" + proc.stderr).strip()
    first_line = output.splitlines()[0] if output else ""
    return proc.returncode, first_line[:280]


def probe_claim_command(
    harness: str,
    source_file: str,
    segment: SegmentRecord,
    command: str,
    probe_cache: dict[str, tuple[int, str]],
) -> CommandProbe:
    binary, probe_cmd = safe_probe_command(command)
    if binary is None:
        return CommandProbe(
            harness=harness,
            source_file=source_file,
            segment_index=segment.index,
            segment_accepted=segment.accepted,
            segment_tier=segment.tier,
            command=command,
            binary=None,
            status="runtime_or_complex_shell_command_unprobed",
            tier="T2" if segment.accepted else "T3",
            probe_cmd=None,
            detail="slash-command or complex shell syntax; kept as operational pattern only",
        )
    which = shutil.which(binary)
    if which is None:
        if binary == "python" and shutil.which("python3"):
            return CommandProbe(
                harness=harness,
                source_file=source_file,
                segment_index=segment.index,
                segment_accepted=segment.accepted,
                segment_tier=segment.tier,
                command=command,
                binary=binary,
                status="binary_alias_missing_use_python3",
                tier="T2" if segment.accepted else "T3",
                probe_cmd=probe_cmd,
                detail="python missing; python3 is present on this machine",
            )
        return CommandProbe(
            harness=harness,
            source_file=source_file,
            segment_index=segment.index,
            segment_accepted=segment.accepted,
            segment_tier=segment.tier,
            command=command,
            binary=binary,
            status="binary_missing",
            tier="T3",
            probe_cmd=probe_cmd,
            detail="binary not present on this machine",
        )
    if probe_cmd in probe_cache:
        rc, line = probe_cache[probe_cmd]
    else:
        rc, line = run_probe(probe_cmd)
        probe_cache[probe_cmd] = (rc, line)
    lowered_line = (line or "").lower()
    if any(marker in lowered_line for marker in ("unknown command", "not a command", "invalid choice", "no such command", "unrecognized")):
        return CommandProbe(
            harness=harness,
            source_file=source_file,
            segment_index=segment.index,
            segment_accepted=segment.accepted,
            segment_tier=segment.tier,
            command=command,
            binary=binary,
            status="binary_present_subcommand_unverified",
            tier="T2" if segment.accepted else "T3",
            probe_cmd=probe_cmd,
            detail=line or "unknown subcommand",
        )
    cleaned_line = re.sub(r"\x1b\[[0-9;]*m", "", line or "").strip()
    if rc == 0 and binary == "codex" and probe_cmd != "codex --help" and lowered_line in ("codex cli", "codex"):
        return CommandProbe(
            harness=harness,
            source_file=source_file,
            segment_index=segment.index,
            segment_accepted=segment.accepted,
            segment_tier=segment.tier,
            command=command,
            binary=binary,
            status="binary_present_subcommand_unverified",
            tier="T2" if segment.accepted else "T3",
            probe_cmd=probe_cmd,
            detail=line or "generic codex help text returned",
        )
    if rc == 0 and binary == "opencode" and probe_cmd != "opencode --help" and cleaned_line in ("", "▄"):
        return CommandProbe(
            harness=harness,
            source_file=source_file,
            segment_index=segment.index,
            segment_accepted=segment.accepted,
            segment_tier=segment.tier,
            command=command,
            binary=binary,
            status="binary_present_subcommand_unverified",
            tier="T2" if segment.accepted else "T3",
            probe_cmd=probe_cmd,
            detail=line or "non-diagnostic help output",
        )
    if rc == 0:
        return CommandProbe(
            harness=harness,
            source_file=source_file,
            segment_index=segment.index,
            segment_accepted=segment.accepted,
            segment_tier=segment.tier,
            command=command,
            binary=binary,
            status="probe_pass",
            tier="T0" if segment.accepted else "T2",
            probe_cmd=probe_cmd,
            detail=line or "help probe succeeded",
        )
    if rc == 124:
        return CommandProbe(
            harness=harness,
            source_file=source_file,
            segment_index=segment.index,
            segment_accepted=segment.accepted,
            segment_tier=segment.tier,
            command=command,
            binary=binary,
            status="probe_timeout",
            tier="T2" if segment.accepted else "T3",
            probe_cmd=probe_cmd,
            detail="probe timeout",
        )
    fallback_cmd = f"{binary} --help"
    if fallback_cmd in probe_cache:
        frc, fline = probe_cache[fallback_cmd]
    else:
        frc, fline = run_probe(fallback_cmd)
        probe_cache[fallback_cmd] = (frc, fline)
    if frc == 0:
        return CommandProbe(
            harness=harness,
            source_file=source_file,
            segment_index=segment.index,
            segment_accepted=segment.accepted,
            segment_tier=segment.tier,
            command=command,
            binary=binary,
            status="binary_present_subcommand_unverified",
            tier="T2" if segment.accepted else "T3",
            probe_cmd=probe_cmd,
            detail=line or "subcommand probe failed but binary exists",
        )
    if "usage:" in (line or "").lower() or "usage:" in (fline or "").lower():
        return CommandProbe(
            harness=harness,
            source_file=source_file,
            segment_index=segment.index,
            segment_accepted=segment.accepted,
            segment_tier=segment.tier,
            command=command,
            binary=binary,
            status="binary_present_subcommand_unverified",
            tier="T2" if segment.accepted else "T3",
            probe_cmd=probe_cmd,
            detail=line or fline or "usage output indicates binary present",
        )
    return CommandProbe(
        harness=harness,
        source_file=source_file,
        segment_index=segment.index,
        segment_accepted=segment.accepted,
        segment_tier=segment.tier,
        command=command,
        binary=binary,
        status="probe_failed",
        tier="T3",
        probe_cmd=probe_cmd,
        detail=line or fline or "probe failed",
    )


def write_registry_markdown(probes: list[CommandProbe], out_path: Path) -> None:
    counts: dict[str, int] = {}
    for probe in probes:
        counts[probe.tier] = counts.get(probe.tier, 0) + 1
    lines = [
        "# CC79 Harness Capability Registry",
        "",
        "**Class**: command capability registry",
        "**Method**: extracted commands from sanitized harness segments + local safety probes",
        "",
        "## Tier Counts",
        "",
        f"- `T0`: {counts.get('T0', 0)}",
        f"- `T1`: {counts.get('T1', 0)}",
        f"- `T2`: {counts.get('T2', 0)}",
        f"- `T3`: {counts.get('T3', 0)}",
        "",
        "## Registry",
        "",
        "| Harness | Tier | Status | Command | Probe | Detail |",
        "|---|---|---|---|---|---|",
    ]
    for probe in sorted(
        probes,
        key=lambda p: (p.harness, p.tier, p.status, p.command),
    ):
        command = probe.command.replace("|", "\\|")
        detail = probe.detail.replace("|", "\\|")
        probe_cmd = (probe.probe_cmd or "").replace("|", "\\|")
        lines.append(
            f"| {probe.harness} | {probe.tier} | {probe.status} | `{command}` | `{probe_cmd}` | {detail} |"
        )
    write_text(out_path, "\n".join(lines).rstrip() + "\n")


def write_promotion_candidates(probes: list[CommandProbe], out_path: Path) -> None:
    primary_bin = {
        "aider": "aider ",
        "claude_code": "claude ",
        "codex": "codex ",
        "gemini_cli": "gemini ",
        "openclaw": "openclaw ",
        "opencode": "opencode ",
        "openhands": "openhands ",
    }
    by_harness: dict[str, list[CommandProbe]] = {}
    for probe in probes:
        if probe.tier not in ("T0", "T1"):
            continue
        if probe.status != "probe_pass":
            continue
        prefix = primary_bin.get(probe.harness)
        if prefix and not probe.command.startswith(prefix):
            continue
        by_harness.setdefault(probe.harness, []).append(probe)

    lines = [
        "# CC79 Harness Promotion Candidates",
        "",
        "**Class**: promotion queue",
        "**Rule**: only `T0/T1` and `probe_pass` claims appear here",
        "",
    ]
    for harness in sorted(HARNESS_TERMS.keys()):
        lines.extend([f"## {harness}", ""])
        claims = sorted(by_harness.get(harness, []), key=lambda p: p.command)
        if not claims:
            lines.append("- no command-level candidates yet")
            lines.append("")
            continue
        lines.append("### Candidate Claims")
        lines.append("")
        for claim in claims:
            lines.append(f"- `{claim.command}`")
        lines.extend(
            [
                "",
                "### Promotion Target",
                "",
                "- add/adjust harness playbook atom",
                "- add validator/operator only if command is deterministic and non-interactive",
                "",
            ]
        )
    write_text(out_path, "\n".join(lines).rstrip() + "\n")


def write_assessment(
    *,
    source_dir: Path,
    imported_prompts: list[Path],
    imported_responses: list[Path],
    sanitized_responses: list[Path],
    segment_records: dict[str, list[SegmentRecord]],
    registry_json: Path,
    registry_md: Path,
    promotion_md: Path,
    out_path: Path,
) -> None:
    accepted = 0
    quarantined = 0
    tcounts: dict[str, int] = {}
    for records in segment_records.values():
        for rec in records:
            if rec.accepted:
                accepted += 1
            else:
                quarantined += 1
            tcounts[rec.tier] = tcounts.get(rec.tier, 0) + 1
    lines = [
        "# CC79 Harness Ingest And Grading",
        "",
        "**Status**: completed",
        "**Purpose**: Tranche A+B completion record for harness packet ingest, sanitation, and capability grading",
        "",
        "## Source",
        "",
        f"- `{source_dir}`",
        "",
        "## Imported Prompts",
        "",
    ]
    lines.extend(f"- `{path.name}`" for path in imported_prompts)
    lines.extend(["", "## Imported Raw Responses", ""])
    lines.extend(f"- `{path.name}`" for path in imported_responses)
    lines.extend(["", "## Sanitized Responses", ""])
    lines.extend(f"- `{path.name}`" for path in sanitized_responses)
    lines.extend(
        [
            "",
            "## Segment Sanitation Summary",
            "",
            f"- accepted segments: {accepted}",
            f"- quarantined segments: {quarantined}",
            f"- T1 segments: {tcounts.get('T1', 0)}",
            f"- T2 segments: {tcounts.get('T2', 0)}",
            f"- T3 segments: {tcounts.get('T3', 0)}",
            "",
            "## Capability Registry Outputs",
            "",
            f"- `{registry_json}`",
            f"- `{registry_md}`",
            f"- `{promotion_md}`",
            "",
            "## Law Notes",
            "",
            "- raw source payloads preserved under communications lineage",
            "- contaminated or prompt-residue segments are quarantined, not deleted",
            "- only T0/T1 claims are eligible for executable promotion in future tranches",
        ]
    )
    write_text(out_path, "\n".join(lines).rstrip() + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", default="/Users/system/Desktop/harnesses")
    parser.add_argument("--cc-tag", default="cc79")
    args = parser.parse_args()

    source_dir = Path(args.source_dir).expanduser().resolve()
    if not source_dir.exists():
        raise SystemExit(f"source directory not found: {source_dir}")

    PROMPTS_DIR.mkdir(parents=True, exist_ok=True)
    RESPONSES_DIR.mkdir(parents=True, exist_ok=True)
    ASSESSMENTS_DIR.mkdir(parents=True, exist_ok=True)
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    IMPL_DIR.mkdir(parents=True, exist_ok=True)

    directives = sorted(source_dir.glob("directive-grok-*.md"))
    reports = sorted(source_dir.glob("report-grok-*.md"))
    if not directives or not reports:
        raise SystemExit("no directive/report files found in source directory")

    imported_prompts: list[Path] = []
    imported_responses: list[Path] = []
    sanitized_responses: list[Path] = []
    segment_map: dict[str, list[SegmentRecord]] = {}
    probes: list[CommandProbe] = []
    probe_cache: dict[str, tuple[int, str]] = {}

    for directive in directives:
        harness = directive.stem.replace("directive-grok-", "")
        dest = PROMPTS_DIR / f"PACKET-GROK-{args.cc_tag}-harness-{harness}.md"
        write_text(dest, read_text(directive))
        imported_prompts.append(dest)

    for report in reports:
        harness = report.stem.replace("report-grok-", "")
        seen_commands: set[str] = set()
        raw_dest = RESPONSES_DIR / f"RESPONSE-GROK-{args.cc_tag}-harness-{harness}-raw.md"
        write_text(raw_dest, read_text(report))
        imported_responses.append(raw_dest)

        records = segment_report(harness, read_text(report))
        segment_map[harness] = records
        sanitized_dest = RESPONSES_DIR / f"RESPONSE-GROK-{args.cc_tag}-harness-{harness}-sanitized.md"
        write_text(sanitized_dest, render_sanitized_report(harness, report.name, records))
        sanitized_responses.append(sanitized_dest)

        for rec in records:
            for command in iter_command_candidates(rec.text):
                dedupe_key = f"{harness}:{command}"
                if dedupe_key in seen_commands:
                    continue
                seen_commands.add(dedupe_key)
                if not rec.accepted:
                    probes.append(
                        CommandProbe(
                            harness=harness,
                            source_file=report.name,
                            segment_index=rec.index,
                            segment_accepted=rec.accepted,
                            segment_tier=rec.tier,
                            command=command,
                            binary=None,
                            status="quarantined_segment_not_probed",
                            tier="T3",
                            probe_cmd=None,
                            detail="segment quarantined",
                        )
                    )
                    continue
                probes.append(probe_claim_command(harness, report.name, rec, command, probe_cache))

    registry_json_path = STATE_DIR / f"HARNESS-CAPABILITY-REGISTRY-{args.cc_tag.upper()}.json"
    registry_md_path = IMPL_DIR / f"HARNESS-CAPABILITY-REGISTRY-{args.cc_tag.upper()}.md"
    promotion_md_path = IMPL_DIR / f"HARNESS-PROMOTION-CANDIDATES-{args.cc_tag.upper()}.md"
    write_text(
        registry_json_path,
        json.dumps([probe.as_dict() for probe in probes], indent=2, ensure_ascii=True) + "\n",
    )
    write_registry_markdown(probes, registry_md_path)
    write_promotion_candidates(probes, promotion_md_path)

    assessment_path = ASSESSMENTS_DIR / f"{args.cc_tag.upper()}-HARNESS-INGEST-AND-GRADING.md"
    write_assessment(
        source_dir=source_dir,
        imported_prompts=imported_prompts,
        imported_responses=imported_responses,
        sanitized_responses=sanitized_responses,
        segment_records=segment_map,
        registry_json=registry_json_path,
        registry_md=registry_md_path,
        promotion_md=promotion_md_path,
        out_path=assessment_path,
    )

    print(assessment_path)
    print(registry_json_path)
    print(registry_md_path)
    print(promotion_md_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
