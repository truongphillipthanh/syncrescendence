#!/usr/bin/env python3
"""
source_extract.py — Atomic knowledge extraction from Syncrescendence source documents.

DC-208-2: Source Mining Pipeline — Component 2 (Extraction Engine)

Reads a SOURCE-*.md file, chunks it with overlap, calls an LLM to extract
atomic knowledge units (claims, frameworks, predictions, concepts, analogies,
praxis_hooks), attaches chaperone metadata, deduplicates, and writes JSONL + MD output.

Dependencies: jsonschema (required), tiktoken (optional, falls back to word-count)
"""

from __future__ import annotations
from config import *

import argparse
import json
import logging
import os
import re
import sys
import hashlib
import uuid as _uuid_mod
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Optional

# ---------------------------------------------------------------------------
# Tokenizer — tiktoken preferred, word-count fallback
# ---------------------------------------------------------------------------

try:
    import tiktoken

    _ENC = tiktoken.encoding_for_model("gpt-4")

    def count_tokens(text: str) -> int:
        return len(_ENC.encode(text))

except ImportError:
    tiktoken = None  # type: ignore[assignment]

    def count_tokens(text: str) -> int:  # type: ignore[misc]
        """Fallback: ~0.75 words per token heuristic."""
        return int(len(text.split()) / 0.75)


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

CATEGORIES = frozenset(
    ["claim", "framework", "prediction", "concept", "analogy", "praxis_hook"]
)
CONTEXT_TYPES = frozenset(
    ["hypothesis", "rebuttal", "consensus", "speculation", "anecdote", "method"]
)
ARGUMENT_ROLES = frozenset(
    ["claim", "evidence", "counterevidence", "limitation"]
)

TENSION_DIMS = (
    "novelty",
    "consensus_pressure",
    "contradiction_load",
    "speculation_risk",
    "actionability",
    "epistemic_stability",
)


@dataclass
class Chunk:
    """A contiguous slice of source text with line provenance."""

    index: int
    text: str
    line_start: int
    line_end: int
    token_count: int


@dataclass
class ChaperoneMetadata:
    context_type: str = "hypothesis"
    argument_role: str = "claim"
    tension_vector: list[float] = field(
        default_factory=lambda: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    )
    opposes_atom_ids: list[str] = field(default_factory=list)


@dataclass
class Atom:
    atom_id: str
    source_id: str
    category: str
    content: str
    line_start: int
    line_end: int
    chaperone: ChaperoneMetadata = field(default_factory=ChaperoneMetadata)
    extensions: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        d = asdict(self)
        return d


@dataclass
class ValidationResult:
    valid: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# LLM interface abstraction
# ---------------------------------------------------------------------------

# Type alias for the LLM call function.
# Signature: (system_prompt: str, user_text: str) -> str
LLMCallFn = Callable[[str, str], str]


def _default_llm_call(system_prompt: str, user_text: str) -> str:
    """Placeholder LLM call — returns empty JSON array.

    Replace this with a real backend by passing --llm-backend or by
    providing a custom function to extract_atoms_from_chunk().
    """
    logging.warning(
        "Using placeholder LLM backend. No atoms will be extracted. "
        "Set LLM_BACKEND env var or pass a custom llm_call function."
    )
    return "[]"


def make_llm_call_from_env() -> LLMCallFn:
    """Build an LLM call function from environment configuration.

    Supported backends (via LLM_BACKEND env var):
      - "openai"  — Uses OPENAI_API_KEY, OPENAI_MODEL (default: gpt-4)
      - "anthropic" — Uses ANTHROPIC_API_KEY, ANTHROPIC_MODEL (default: claude-sonnet-4-20250514)
      - "openrouter" — Uses OPENROUTER_API_KEY, OPENROUTER_MODEL (default: google/gemini-2.5-flash)
      - unset / unknown — returns placeholder

    This keeps the extraction script dependency-free beyond jsonschema.
    The actual API libraries are imported lazily.
    """
    backend = os.environ.get("LLM_BACKEND", "").lower()

    if backend == "openai":
        api_key = os.environ.get("OPENAI_API_KEY")
        model = os.environ.get("OPENAI_MODEL", "gpt-4")
        if not api_key:
            logging.error("LLM_BACKEND=openai but OPENAI_API_KEY not set")
            return _default_llm_call

        def openai_call(system_prompt: str, user_text: str) -> str:
            try:
                from openai import OpenAI  # type: ignore[import-untyped]
            except ImportError:
                logging.error("openai package not installed")
                return "[]"
            client = OpenAI(api_key=api_key)
            resp = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_text},
                ],
                temperature=0.1,
            )
            return resp.choices[0].message.content or "[]"

        return openai_call

    elif backend == "openrouter":
        api_key = os.environ.get("OPENROUTER_API_KEY")
        model = os.environ.get("OPENROUTER_MODEL", "google/gemini-2.5-flash")
        if not api_key:
            logging.error("LLM_BACKEND=openrouter but OPENROUTER_API_KEY not set")
            return _default_llm_call

        def openrouter_call(system_prompt: str, user_text: str) -> str:
            try:
                from openai import OpenAI  # type: ignore[import-untyped]
            except ImportError:
                logging.error("openai package not installed (needed for OpenRouter)")
                return "[]"
            client = OpenAI(
                api_key=api_key,
                base_url="https://openrouter.ai/api/v1",
            )
            resp = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_text},
                ],
                temperature=0.1,
            )
            return resp.choices[0].message.content or "[]"

        return openrouter_call

    elif backend == "anthropic":
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        model = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-20250514")
        if not api_key:
            logging.error("LLM_BACKEND=anthropic but ANTHROPIC_API_KEY not set")
            return _default_llm_call

        def anthropic_call(system_prompt: str, user_text: str) -> str:
            try:
                import anthropic  # type: ignore[import-untyped]
            except ImportError:
                logging.error("anthropic package not installed")
                return "[]"
            client = anthropic.Anthropic(api_key=api_key)
            resp = client.messages.create(
                model=model,
                max_tokens=4096,
                system=system_prompt,
                messages=[{"role": "user", "content": user_text}],
            )
            return resp.content[0].text if resp.content else "[]"

        return anthropic_call

    else:
        return _default_llm_call


# ---------------------------------------------------------------------------
# Source parsing
# ---------------------------------------------------------------------------


def parse_source_file(path: Path) -> tuple[str, str, list[str]]:
    """Parse a SOURCE-*.md file, returning (source_id, frontmatter_yaml, body_lines).

    The source_id is extracted from the YAML frontmatter 'id' field.
    Falls back to deriving it from the filename.
    """
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    # Extract frontmatter — handles both fenced (---) and bare YAML blocks.
    # Bare frontmatter: first 4KB scanned for YAML-like key: value lines before
    # any markdown content (heading, blank line, or non-YAML line terminates).
    frontmatter = ""
    body_start = 0

    if lines and lines[0].strip() == "---":
        # Fenced frontmatter
        for i, line in enumerate(lines[1:], start=1):
            if line.strip() == "---":
                frontmatter = "\n".join(lines[1:i])
                body_start = i + 1
                break
    else:
        # Bare (unfenced) frontmatter detection — scan first 4KB
        _YAML_KEY_RE = re.compile(r"^[a-zA-Z_][a-zA-Z0-9_-]*\s*:")
        char_budget = 4096
        bare_end = 0
        chars_seen = 0
        for idx, line in enumerate(lines):
            chars_seen += len(line) + 1
            if chars_seen > char_budget:
                break
            stripped = line.strip()
            if not stripped:
                # blank line terminates bare frontmatter
                bare_end = idx
                break
            if stripped.startswith("#"):
                # heading = content, not frontmatter
                break
            if _YAML_KEY_RE.match(stripped):
                bare_end = idx + 1
                continue
            # Non-YAML line → stop
            break
        if bare_end > 0:
            # Check for a fenced YAML block immediately following bare lines
            # (handles hybrid: bare keys on top, then ---...--- fenced block)
            fence_start = bare_end
            # Skip optional blank line between bare keys and fence
            if fence_start < len(lines) and not lines[fence_start].strip():
                fence_start += 1
            if fence_start < len(lines) and lines[fence_start].strip() == "---":
                # Found opening fence — scan for closing fence
                for fi in range(fence_start + 1, len(lines)):
                    if lines[fi].strip() == "---":
                        # Include both bare and fenced YAML as frontmatter
                        frontmatter = "\n".join(lines[:fi])
                        body_start = fi + 1
                        break
                else:
                    # No closing fence found — treat bare section only
                    frontmatter = "\n".join(lines[:bare_end])
                    body_start = bare_end
            else:
                frontmatter = "\n".join(lines[:bare_end])
                body_start = bare_end
            # Skip a single blank line separator after frontmatter
            if body_start < len(lines) and not lines[body_start].strip():
                body_start += 1

    # Extract source_id from frontmatter
    source_id = ""
    for fm_line in frontmatter.splitlines():
        m = re.match(r"^id:\s*(.+)", fm_line)
        if m:
            source_id = m.group(1).strip()
            break

    if not source_id:
        # Fallback: derive from filename
        stem = path.stem  # e.g. SOURCE-20020201-001
        source_id = stem

    body_lines = lines[body_start:]
    return source_id, frontmatter, body_lines


# ---------------------------------------------------------------------------
# Chunking
# ---------------------------------------------------------------------------


def chunk_source_with_overlap(
    lines: list[str],
    max_tokens: int = 1800,
    overlap_tokens: int = 220,
) -> list[Chunk]:
    """Deterministic chunking with overlap for resumable extraction.

    Splits on line boundaries, ensuring each chunk is under max_tokens.
    Overlap is applied by including trailing lines from the previous chunk.
    """
    if not lines:
        return []

    chunks: list[Chunk] = []
    chunk_idx = 0
    current_lines: list[str] = []
    current_tokens = 0
    chunk_line_start = 0  # 0-indexed into `lines`

    i = 0
    while i < len(lines):
        line = lines[i]
        line_tokens = count_tokens(line)

        if current_tokens + line_tokens > max_tokens and current_lines:
            # Emit chunk
            chunks.append(
                Chunk(
                    index=chunk_idx,
                    text="\n".join(current_lines),
                    line_start=chunk_line_start + 1,  # 1-indexed for output
                    line_end=chunk_line_start + len(current_lines),
                    token_count=current_tokens,
                )
            )
            chunk_idx += 1

            # Calculate overlap: walk backwards from end of current_lines
            overlap_acc = 0
            overlap_line_count = 0
            for rev_line in reversed(current_lines):
                t = count_tokens(rev_line)
                if overlap_acc + t > overlap_tokens:
                    break
                overlap_acc += t
                overlap_line_count += 1

            # Rewind i to start of overlap
            overlap_start = chunk_line_start + len(current_lines) - overlap_line_count
            chunk_line_start = overlap_start
            current_lines = list(lines[overlap_start : chunk_line_start + overlap_line_count])
            current_tokens = overlap_acc
            i = chunk_line_start + overlap_line_count
            continue

        current_lines.append(line)
        current_tokens += line_tokens
        i += 1

    # Final chunk
    if current_lines:
        chunks.append(
            Chunk(
                index=chunk_idx,
                text="\n".join(current_lines),
                line_start=chunk_line_start + 1,
                line_end=chunk_line_start + len(current_lines),
                token_count=current_tokens,
            )
        )

    return chunks


# ---------------------------------------------------------------------------
# Prompt loading
# ---------------------------------------------------------------------------

_PROMPT_TEMPLATE_PATH = Path(__file__).resolve().parent.parent.parent.parent / (
    "engine/02-ENGINE/PROMPT-SOURCE_EXTRACTION_ATOMIC.md"
)


def load_extraction_prompt(template_path: Optional[Path] = None) -> str:
    """Load the extraction prompt template from the engine directory."""
    p = template_path or _PROMPT_TEMPLATE_PATH
    if not p.exists():
        logging.error("Extraction prompt template not found at %s", p)
        sys.exit(1)
    return p.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# Atom extraction
# ---------------------------------------------------------------------------


def extract_atoms_from_chunk(
    chunk: Chunk,
    source_id: str,
    prompt_template: str,
    llm_call: LLMCallFn,
    atom_seq_offset: int = 0,
    target_compression: float = 0.1,
) -> list[Atom]:
    """Call LLM with the extraction prompt to get atoms from a single chunk.

    Returns a list of Atom dataclass instances with sequential IDs.
    """
    system_prompt = prompt_template
    user_text = (
        f"## Source: {source_id}\n"
        f"## Lines: {chunk.line_start}-{chunk.line_end}\n"
        f"## Target compression ratio: {target_compression}\n\n"
        f"{chunk.text}"
    )

    raw_response = llm_call(system_prompt, user_text)

    # Parse JSON array from response — handle markdown code fences
    json_str = raw_response.strip()
    if json_str.startswith("```"):
        # Strip code fence
        lines = json_str.splitlines()
        # Remove first and last fence lines
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip().startswith("```"):
            lines = lines[:-1]
        json_str = "\n".join(lines)

    try:
        raw_atoms = json.loads(json_str)
    except json.JSONDecodeError as e:
        logging.warning(
            "Failed to parse LLM response for chunk %d: %s", chunk.index, e
        )
        return []

    if not isinstance(raw_atoms, list):
        logging.warning("LLM response for chunk %d is not a list", chunk.index)
        return []

    atoms: list[Atom] = []
    for i, raw in enumerate(raw_atoms):
        if not isinstance(raw, dict):
            continue
        seq = atom_seq_offset + i + 1
        atom_id = f"ATOM-{source_id}-{seq:04d}"

        category = raw.get("category", "claim")
        if category not in CATEGORIES:
            logging.warning("Unknown category '%s' in chunk %d, defaulting to 'claim'", category, chunk.index)
            category = "claim"

        chap_raw = raw.get("chaperone", {})
        chaperone = ChaperoneMetadata(
            context_type=chap_raw.get("context_type", "hypothesis"),
            argument_role=chap_raw.get("argument_role", "claim"),
            tension_vector=chap_raw.get(
                "tension_vector", [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            ),
            opposes_atom_ids=chap_raw.get("opposes_atom_ids", []),
        )

        # Clamp tension vector
        tv = chaperone.tension_vector
        if len(tv) != 6:
            tv = (tv + [0.0] * 6)[:6]
        chaperone.tension_vector = [max(0.0, min(1.0, v)) for v in tv]

        # Clamp provenance lines to chunk bounds
        raw_line_start = raw.get("line_start", chunk.line_start)
        raw_line_end = raw.get("line_end", chunk.line_end)
        clamped_start = max(raw_line_start, chunk.line_start)
        clamped_end = min(raw_line_end, chunk.line_end)
        if clamped_start > clamped_end:
            logging.warning(
                "Atom %s in chunk %d: clamped range invalid (%d > %d), rejecting",
                atom_id, chunk.index, clamped_start, clamped_end,
            )
            continue

        atom = Atom(
            atom_id=atom_id,
            source_id=source_id,
            category=category,
            content=raw.get("content", ""),
            line_start=clamped_start,
            line_end=clamped_end,
            chaperone=chaperone,
            extensions=raw.get("extensions", {}),
        )
        atoms.append(atom)

    return atoms


# ---------------------------------------------------------------------------
# Chaperone attachment (enrichment pass)
# ---------------------------------------------------------------------------


def attach_chaperone_metadata(atom: Atom, local_context: str) -> Atom:
    """Enrich chaperone metadata using local context heuristics.

    This is a rule-based pass that augments LLM-provided chaperone data.
    It does NOT call an LLM — purely deterministic.
    """
    content_lower = atom.content.lower()

    # Heuristic: detect prediction-like language
    prediction_signals = ["will ", "by 20", "in the next", "forecast", "predict"]
    if any(s in content_lower for s in prediction_signals):
        if atom.chaperone.context_type == "hypothesis":
            atom.chaperone.context_type = "speculation"
        # Bump speculation_risk
        atom.chaperone.tension_vector[3] = max(
            atom.chaperone.tension_vector[3], 0.6
        )

    # Heuristic: detect method/practice language
    method_signals = ["step 1", "how to", "technique", "method", "practice", "protocol"]
    if any(s in content_lower for s in method_signals):
        atom.chaperone.tension_vector[4] = max(
            atom.chaperone.tension_vector[4], 0.7
        )  # actionability

    # Heuristic: detect rebuttal/counter language
    counter_signals = ["however", "contrary to", "critics argue", "on the other hand"]
    if any(s in content_lower for s in counter_signals):
        atom.chaperone.tension_vector[2] = max(
            atom.chaperone.tension_vector[2], 0.5
        )  # contradiction_load

    return atom


# ---------------------------------------------------------------------------
# Deduplication
# ---------------------------------------------------------------------------


def _content_fingerprint(text: str) -> str:
    """Normalize and hash content for dedup."""
    normalized = re.sub(r"\s+", " ", text.strip().lower())
    return hashlib.sha256(normalized.encode()).hexdigest()[:16]


def merge_and_dedup_atoms(atoms: list[Atom]) -> list[Atom]:
    """Deduplicate atoms by content similarity.

    Uses normalized content hashing. When duplicates found, keeps the one
    with the earliest line_start (preserves provenance priority).
    """
    seen: dict[str, Atom] = {}
    for atom in atoms:
        fp = _content_fingerprint(atom.content)
        if fp in seen:
            existing = seen[fp]
            if atom.line_start < existing.line_start:
                seen[fp] = atom
            logging.debug(
                "Dedup: %s duplicates %s", atom.atom_id, existing.atom_id
            )
        else:
            seen[fp] = atom

    # Re-sequence atom IDs after dedup
    deduped = sorted(seen.values(), key=lambda a: a.line_start)
    for i, atom in enumerate(deduped):
        atom.atom_id = f"ATOM-{atom.source_id}-{i + 1:04d}"

    return deduped


# ---------------------------------------------------------------------------
# Two-pass map-reduce for large sources
# ---------------------------------------------------------------------------


def is_large_source(lines: list[str], threshold: int = 5000) -> bool:
    return len(lines) > threshold


def consolidation_pass(
    atoms: list[Atom], llm_call: LLMCallFn, prompt_template: str
) -> list[Atom]:
    """Pass 2 for large sources: consolidation via LLM.

    Sends all atoms to the LLM for merge/conflict resolution.
    Falls back to rule-based dedup if LLM call fails.
    """
    if len(atoms) <= 10:
        return merge_and_dedup_atoms(atoms)

    # Prepare atom summaries for consolidation
    atom_summaries = []
    for a in atoms:
        atom_summaries.append(
            {
                "atom_id": a.atom_id,
                "category": a.category,
                "content": a.content[:200],
                "line_start": a.line_start,
                "line_end": a.line_end,
            }
        )

    system_prompt = (
        "You are a knowledge consolidation engine. Given a list of extracted "
        "knowledge atoms, identify duplicates and conflicts. Return a JSON array "
        "of objects with 'keep_id' (atom_id to keep) and 'merge_ids' (list of "
        "atom_ids that are duplicates of keep_id). Only include groups where "
        "duplicates exist."
    )
    user_text = json.dumps(atom_summaries, indent=2)

    raw = llm_call(system_prompt, user_text)
    try:
        merge_groups = json.loads(raw.strip())
    except json.JSONDecodeError:
        logging.warning("Consolidation LLM parse failed, falling back to hash dedup")
        return merge_and_dedup_atoms(atoms)

    # Apply merge directives
    atoms_by_id = {a.atom_id: a for a in atoms}
    to_remove: set[str] = set()
    if isinstance(merge_groups, list):
        for group in merge_groups:
            if not isinstance(group, dict):
                continue
            for mid in group.get("merge_ids", []):
                to_remove.add(mid)

    kept = [a for a in atoms if a.atom_id not in to_remove]
    return merge_and_dedup_atoms(kept)


# ---------------------------------------------------------------------------
# Output writers
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Bridge-compatible export (memsync_schema envelope)
# ---------------------------------------------------------------------------

CATEGORY_TO_ENTITY_TYPE = {
    "claim": "Claim",
    "framework": "Framework",
    "prediction": "Prediction",
    "concept": "Concept",
    "analogy": "Concept",
    "praxis_hook": "PraxisHook",
}


def _deterministic_uuid(atom_id: str) -> str:
    """Generate a deterministic UUID v5 from an atom_id (DNS namespace)."""
    return str(_uuid_mod.uuid5(_uuid_mod.NAMESPACE_DNS, atom_id))


def write_bridge_jsonl(atoms: list[Atom], source_id: str, out_path: Path) -> None:
    """Write bridge-compatible JSONL with memsync_schema envelopes.

    Emits source_atom records for each atom, and source_relation records
    for any opposes_atom_ids references (as CONTRADICTS edges).
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).isoformat()

    with open(out_path, "w", encoding="utf-8") as f:
        for atom in atoms:
            entity_type = CATEGORY_TO_ENTITY_TYPE.get(atom.category, "Concept")
            rec_uuid = _deterministic_uuid(atom.atom_id)

            # Build a short name from content (first 80 chars, no newlines)
            name = atom.content.replace("\n", " ")[:80].strip()

            envelope = {
                "record_type": "source_atom",
                "schema_version": "1.0.0",
                "uuid": rec_uuid,
                "timestamp": now,
                "payload": atom.to_dict(),
                # Top-level fields expected by memsync_schema.SourceAtomRecord
                "source_id": atom.source_id,
                "entity_type": entity_type,
                "name": name,
                "content": atom.content,
                "confidence": 1.0,
                "provenance": {
                    "source_id": atom.source_id,
                    "line_start": atom.line_start,
                    "line_end": atom.line_end,
                    "atom_id": atom.atom_id,
                },
                "metadata": {
                    "category": atom.category,
                    "chaperone": atom.chaperone.__dict__ if hasattr(atom.chaperone, '__dict__') else {},
                    "extensions": atom.extensions,
                },
            }
            f.write(json.dumps(envelope, ensure_ascii=False) + "\n")

            # Emit source_relation records for opposes_atom_ids
            for target_atom_id in atom.chaperone.opposes_atom_ids:
                rel_uuid = _deterministic_uuid(f"{atom.atom_id}:CONTRADICTS:{target_atom_id}")
                target_uuid = _deterministic_uuid(target_atom_id)
                relation_rec = {
                    "record_type": "source_relation",
                    "schema_version": "1.0.0",
                    "uuid": rel_uuid,
                    "timestamp": now,
                    "source_atom_id": rec_uuid,
                    "target_atom_id": target_uuid,
                    "relation_type": "CONTRADICTS",
                    "weight": 1.0,
                    "provenance": {
                        "source_id": atom.source_id,
                        "line_start": atom.line_start,
                        "line_end": atom.line_end,
                        "atom_id": atom.atom_id,
                    },
                    "metadata": {
                        "source_atom_id_raw": atom.atom_id,
                        "target_atom_id_raw": target_atom_id,
                    },
                }
                f.write(json.dumps(relation_rec, ensure_ascii=False) + "\n")

    total_relations = sum(len(a.chaperone.opposes_atom_ids) for a in atoms)
    logging.info(
        "Wrote %d atom + %d relation bridge records to %s",
        len(atoms), total_relations, out_path,
    )


def write_jsonl(atoms: list[Atom], out_path: Path) -> None:
    """Write atoms as JSONL — one atom per line."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        for atom in atoms:
            f.write(json.dumps(atom.to_dict(), ensure_ascii=False) + "\n")
    logging.info("Wrote %d atoms to %s", len(atoms), out_path)


def write_companion_md(
    atoms: list[Atom], source_id: str, source_path: Path, out_path: Path
) -> None:
    """Write human-readable companion markdown."""
    out_path.parent.mkdir(parents=True, exist_ok=True)

    category_groups: dict[str, list[Atom]] = {}
    for atom in atoms:
        category_groups.setdefault(atom.category, []).append(atom)

    lines = [
        f"# Extraction: {source_id}",
        f"",
        f"**Source**: `{source_path.name}`",
        f"**Atoms extracted**: {len(atoms)}",
        f"**Categories**: {', '.join(sorted(category_groups.keys()))}",
        f"",
        "---",
        "",
    ]

    for cat in sorted(category_groups.keys()):
        cat_atoms = category_groups[cat]
        lines.append(f"## {cat.replace('_', ' ').title()} ({len(cat_atoms)})")
        lines.append("")
        for atom in cat_atoms:
            lines.append(f"### {atom.atom_id}")
            lines.append(f"**Lines**: {atom.line_start}-{atom.line_end}")
            lines.append(f"**Context**: {atom.chaperone.context_type} / {atom.chaperone.argument_role}")
            tv = atom.chaperone.tension_vector
            tv_labels = [
                f"{TENSION_DIMS[i]}={tv[i]:.2f}" for i in range(len(TENSION_DIMS))
            ]
            lines.append(f"**Tension**: {', '.join(tv_labels)}")
            lines.append("")
            lines.append(f"> {atom.content}")
            lines.append("")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    logging.info("Wrote companion MD to %s", out_path)


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------


def run_extraction(
    source_path: Path,
    max_chunk_tokens: int = 1800,
    overlap_tokens: int = 220,
    target_compression: float = 0.1,
    out_dir: Optional[Path] = None,
    prompt_template_path: Optional[Path] = None,
    llm_call: Optional[LLMCallFn] = None,
) -> list[Atom]:
    """Full extraction pipeline for a single source document."""
    log = logging.getLogger("source_extract")

    if not source_path.exists():
        log.error("Source file not found: %s", source_path)
        sys.exit(1)

    # Parse source
    source_id, frontmatter, body_lines = parse_source_file(source_path)
    log.info(
        "Source: %s | %d lines | large=%s",
        source_id,
        len(body_lines),
        is_large_source(body_lines),
    )

    # Load prompt template
    prompt_template = load_extraction_prompt(prompt_template_path)

    # Resolve LLM backend
    if llm_call is None:
        llm_call = make_llm_call_from_env()

    # Chunk
    chunks = chunk_source_with_overlap(body_lines, max_chunk_tokens, overlap_tokens)
    log.info("Chunked into %d chunks (max_tokens=%d, overlap=%d)",
             len(chunks), max_chunk_tokens, overlap_tokens)

    # Pass 1: extract atoms from each chunk
    all_atoms: list[Atom] = []
    seq_offset = 0
    for chunk in chunks:
        log.info("Extracting chunk %d/%d (lines %d-%d, %d tokens)",
                 chunk.index + 1, len(chunks),
                 chunk.line_start, chunk.line_end, chunk.token_count)
        atoms = extract_atoms_from_chunk(
            chunk, source_id, prompt_template, llm_call,
            atom_seq_offset=seq_offset,
            target_compression=target_compression,
        )
        # Enrich with chaperone heuristics
        for atom in atoms:
            attach_chaperone_metadata(atom, chunk.text)
        all_atoms.extend(atoms)
        seq_offset += len(atoms)

    log.info("Pass 1 complete: %d raw atoms", len(all_atoms))

    # Pass 2: consolidation (large sources get LLM-assisted, small get hash dedup)
    if is_large_source(body_lines):
        log.info("Large source detected — running consolidation pass")
        final_atoms = consolidation_pass(all_atoms, llm_call, prompt_template)
    else:
        final_atoms = merge_and_dedup_atoms(all_atoms)

    log.info("Final: %d atoms after dedup/consolidation", len(final_atoms))

    # Compute output paths
    if out_dir is None:
        out_dir = source_path.parent / "_meta"

    jsonl_path = out_dir / f"EXTRACT-{source_id}.jsonl"
    bridge_path = out_dir / f"EXTRACT-{source_id}.bridge.jsonl"
    md_path = out_dir / f"EXTRACT-{source_id}.md"

    write_jsonl(final_atoms, jsonl_path)
    write_bridge_jsonl(final_atoms, source_id, bridge_path)
    write_companion_md(final_atoms, source_id, source_path, md_path)

    return final_atoms


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract atomic knowledge from Syncrescendence source documents.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python3 source_extract.py --source sources/04-SOURCES/SOURCE-20020201-001.md\n"
            "  python3 source_extract.py --source sources/04-SOURCES/SOURCE-*.md --max-chunk-tokens 2000\n"
        ),
    )
    parser.add_argument(
        "--source",
        type=Path,
        required=True,
        help="Path to SOURCE-*.md file",
    )
    parser.add_argument(
        "--max-chunk-tokens",
        type=int,
        default=1800,
        help="Maximum tokens per chunk (default: 1800)",
    )
    parser.add_argument(
        "--overlap",
        type=int,
        default=220,
        help="Overlap tokens between chunks (default: 220)",
    )
    parser.add_argument(
        "--target-compression",
        type=float,
        default=0.1,
        help="Target compression ratio, e.g. 0.1 = 1:10 (default: 0.1)",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=None,
        help="Output directory (default: <source_dir>/_meta)",
    )
    parser.add_argument(
        "--prompt-template",
        type=Path,
        default=None,
        help="Path to extraction prompt template (default: engine/02-ENGINE/PROMPT-SOURCE_EXTRACTION_ATOMIC.md)",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable debug logging",
    )

    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )

    run_extraction(
        source_path=args.source,
        max_chunk_tokens=args.max_chunk_tokens,
        overlap_tokens=args.overlap,
        target_compression=args.target_compression,
        out_dir=args.out_dir,
        prompt_template_path=args.prompt_template,
    )


if __name__ == "__main__":
    main()
