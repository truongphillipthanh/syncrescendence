#!/usr/bin/env python3
"""Deterministic Track for Acumen transcript normalization and templating."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any


WORD_RE = re.compile(r"[A-Za-z0-9']+")
SPACE_RE = re.compile(r"\s+")
PUNCT_SPACE_RE = re.compile(r"\s+([,.;:!?])")
FILLER_PATTERNS = [
    (re.compile(r"\b(um|uh|hm+|mhm|ah|er)\b", re.IGNORECASE), " "),
    (re.compile(r"\blike\b(?=\s+(?:um|uh|you know))", re.IGNORECASE), " "),
    (re.compile(r"\byou know\b(?!\?)", re.IGNORECASE), " "),
    (re.compile(r"(?<=[.!?])\s*\bI mean\b", re.IGNORECASE), " "),
    (re.compile(r"\b(sort|kind) of\b(?=\s+\1)", re.IGNORECASE), " "),
    (re.compile(r"\b(basically|essentially|literally)\b(?=\s*[,.]|\s+(?:the|it|we|they|I))", re.IGNORECASE), " "),
]


@dataclass
class Segment:
    text: str
    start_ms: int
    end_ms: int


def normalize_space(text: str) -> str:
    text = SPACE_RE.sub(" ", text).strip()
    text = PUNCT_SPACE_RE.sub(r"\1", text)
    text = re.sub(r"\s*\n\s*", "\n", text)
    return text.strip()


def normalize_for_match(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def tokenize_words(text: str) -> list[str]:
    return [token for token in text.split(" ") if token]


def fuzzy_apply_resolution(text: str, terms: list[str], threshold: float) -> str:
    if not terms:
        return text
    words = tokenize_words(text)
    if not words:
        return text

    normalized_terms: list[tuple[str, list[str], str]] = []
    for term in terms:
        tokenized = tokenize_words(term)
        if not tokenized:
            continue
        normalized_terms.append((term, tokenized, normalize_for_match(term)))

    max_len = max((len(item[1]) for item in normalized_terms), default=1) + 1
    output: list[str] = []
    i = 0
    while i < len(words):
        best_term = None
        best_span = 0
        best_score = 0.0
        span_limit = min(max_len, len(words) - i)
        for span in range(1, span_limit + 1):
            candidate_tokens = words[i : i + span]
            candidate_text = " ".join(candidate_tokens)
            candidate_norm = normalize_for_match(candidate_text)
            if not candidate_norm:
                continue
            for original_term, term_tokens, term_norm in normalized_terms:
                if abs(span - len(term_tokens)) > 1:
                    continue
                score = SequenceMatcher(None, candidate_norm, term_norm).ratio()
                if score >= threshold and score > best_score:
                    best_term = original_term
                    best_span = span
                    best_score = score
        if best_term:
            trailing = re.search(r"([^\w']+)$", words[i + best_span - 1])
            suffix = trailing.group(1) if trailing else ""
            output.append(best_term + suffix)
            i += best_span
            continue
        output.append(words[i])
        i += 1
    return normalize_space(" ".join(output))


def remove_disfluencies(text: str) -> str:
    cleaned = text
    for pattern, replacement in FILLER_PATTERNS:
        cleaned = pattern.sub(replacement, cleaned)
    cleaned = re.sub(r"\s{2,}", " ", cleaned)
    cleaned = re.sub(r",\s*,", ", ", cleaned)
    return normalize_space(cleaned)


def parse_segments(payload: Any) -> list[Segment]:
    if not isinstance(payload, list):
        raise SystemExit("captions payload must be a JSON list")
    segments: list[Segment] = []
    for row in payload:
        if not isinstance(row, dict):
            continue
        text = str(row.get("text", "")).strip()
        if not text:
            continue
        start_ms = row.get("start_ms")
        end_ms = row.get("end_ms")
        if start_ms is None:
            start = row.get("start", 0)
            start_ms = int(float(start) * 1000)
        else:
            start_ms = int(start_ms)
        if end_ms is None:
            end = row.get("end")
            if end is None:
                end_ms = start_ms + 1000
            else:
                end_ms = int(float(end) * 1000)
        else:
            end_ms = int(end_ms)
        segments.append(Segment(text=text, start_ms=start_ms, end_ms=end_ms))
    return sorted(segments, key=lambda item: item.start_ms)


def stitch_segments(segments: list[Segment]) -> str:
    if not segments:
        return ""
    chunks: list[str] = [segments[0].text]
    previous = segments[0]
    for current in segments[1:]:
        delta = max(0, current.start_ms - previous.end_ms)
        if delta > 1500:
            chunks.append(".\n\n")
        elif delta > 800:
            chunks.append(". ")
        elif delta > 400:
            chunks.append(", ")
        else:
            chunks.append(" ")
        chunks.append(current.text)
        previous = current
    return normalize_space("".join(chunks))


def headline_template(text: str) -> str:
    words = tokenize_words(text)
    clipped = " ".join(words[:24]).strip()
    if clipped and clipped[-1] not in ".!?":
        clipped += "."
    return clipped


def sentence_split(text: str) -> list[str]:
    return [part.strip() for part in re.split(r"(?<=[.!?])\s+", text) if part.strip()]


def abstract_template(text: str) -> str:
    sentences = sentence_split(text)
    claim = sentences[0] if len(sentences) >= 1 else text
    evidence = sentences[1] if len(sentences) >= 2 else claim
    implication = sentences[2] if len(sentences) >= 3 else evidence
    return (
        "### Claim\n"
        f"{claim}\n\n"
        "### Evidence\n"
        f"{evidence}\n\n"
        "### Implication\n"
        f"{implication}\n"
    )


def precis_template(text: str) -> str:
    words = tokenize_words(text)
    return " ".join(words[:170]).strip()


def synopsis_template(text: str) -> str:
    sentences = sentence_split(text)
    if not sentences:
        return text
    quarter = max(1, len(sentences) // 4)
    chunks = [
        ("Core Concept", " ".join(sentences[:quarter])),
        ("Intuition", " ".join(sentences[quarter : quarter * 2]) or sentences[0]),
        ("Formal Treatment", " ".join(sentences[quarter * 2 : quarter * 3]) or sentences[-1]),
        ("Connections", " ".join(sentences[quarter * 3 :]) or sentences[-1]),
    ]
    return "\n\n".join([f"### {title}\n{body}" for title, body in chunks])


def blueprint_template(text: str) -> str:
    sentences = sentence_split(text)
    steps = sentences[:8] if sentences else [text]
    body = ["### Prerequisites", "- Review source context and dependencies.", "", "### Steps"]
    for idx, step in enumerate(steps, start=1):
        body.append(f"{idx}. {step}")
    body.extend(["", "### Gotchas", "- Validate assumptions against primary source artifacts.", "", "### Outcome", "- Actionable implementation path captured."])
    return "\n".join(body)


def render_by_depth(text: str, target_depth: str) -> str:
    if target_depth == "Headline":
        return headline_template(text)
    if target_depth == "Abstract":
        return abstract_template(text)
    if target_depth == "Precis":
        return precis_template(text)
    if target_depth == "Synopsis":
        return synopsis_template(text)
    if target_depth == "Blueprint":
        return blueprint_template(text)
    return text


def gather_terms(args: argparse.Namespace) -> list[str]:
    terms: list[str] = []
    terms.extend(args.resolution_term or [])
    if args.resolution_json:
        payload = json.loads(Path(args.resolution_json).read_text(encoding="utf-8"))
        if isinstance(payload, dict):
            payload = payload.get("terms", [])
        if isinstance(payload, list):
            terms.extend(str(item) for item in payload)
    deduped = []
    seen = set()
    for term in terms:
        key = normalize_for_match(term)
        if not key or key in seen:
            continue
        seen.add(key)
        deduped.append(term.strip())
    return deduped


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--input-text")
    group.add_argument("--input-captions", help="JSON list of segments with text/start_ms/end_ms.")
    parser.add_argument("--genre", default="Commentary")
    parser.add_argument("--target-depth", default="Precis")
    parser.add_argument("--target-polish", default="clean_verbatim")
    parser.add_argument("--resolution-term", action="append")
    parser.add_argument("--resolution-json")
    parser.add_argument("--similarity-threshold", type=float, default=0.85)
    parser.add_argument("--output", required=True)
    parser.add_argument("--debug-json")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    terms = gather_terms(args)

    if args.input_captions:
        segments_payload = json.loads(Path(args.input_captions).read_text(encoding="utf-8"))
        segments = parse_segments(segments_payload)
        transformed = []
        for item in segments:
            resolved = fuzzy_apply_resolution(item.text, terms, args.similarity_threshold)
            transformed.append(Segment(text=resolved, start_ms=item.start_ms, end_ms=item.end_ms))
        base_text = stitch_segments(transformed)
    else:
        raw = Path(args.input_text).read_text(encoding="utf-8", errors="replace")
        base_text = fuzzy_apply_resolution(normalize_space(raw), terms, args.similarity_threshold)

    cleaned = remove_disfluencies(base_text)
    rendered = render_by_depth(cleaned, args.target_depth)

    if args.target_polish in {"charitable", "editorial"}:
        rendered = (
            "### Deterministic Base\n"
            f"{rendered}\n\n"
            "### Intelligent Track Required\n"
            f"Target polish `{args.target_polish}` requires semantic processing beyond deterministic cleaning.\n"
        )

    output_body = (
        f"# Acumen Deterministic Artifact\n\n"
        f"- Genre: `{args.genre}`\n"
        f"- Target depth: `{args.target_depth}`\n"
        f"- Target polish: `{args.target_polish}`\n"
        f"- Resolution terms: `{len(terms)}`\n\n"
        f"{rendered}\n"
    )
    output_path = Path(args.output).expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(output_body, encoding="utf-8")

    if args.debug_json:
        debug = {
            "genre": args.genre,
            "target_depth": args.target_depth,
            "target_polish": args.target_polish,
            "resolution_terms": terms,
            "cleaned_preview": cleaned[:600],
        }
        debug_path = Path(args.debug_json).expanduser().resolve()
        debug_path.parent.mkdir(parents=True, exist_ok=True)
        debug_path.write_text(json.dumps(debug, indent=2) + "\n", encoding="utf-8")

    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
