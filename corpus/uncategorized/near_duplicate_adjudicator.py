import itertools
import json
import os
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from difflib import SequenceMatcher
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple


ROOT = "/Users/system/syncrescendence/corpus"
TSV_PATH = os.path.join(ROOT, "NEARDUPES-ADJUDICATOR.tsv")
SUMMARY_PATH = os.path.join(ROOT, "NEARDUPES-SUMMARY.md")
REVIEW_PATH = os.path.join(ROOT, "NEARDUPES-REVIEW.json")

NUMERIC_FILE_RE = re.compile(r"^\d+(?:\.[A-Za-z0-9_]+)?$")
URL_RE = re.compile(r"https?://\S+")
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
FRONTMATTER_RE = re.compile(r"\A---\s*\n.*?\n---\s*\n", re.S)
WORD_RE = re.compile(r"[a-z0-9]+")
METADATA_KEY_RE = re.compile(
    r"^\s{0,3}(?:[-*]\s+|>\s*)?(?:\*\*)?"
    r"(author|handle|date|thread date|url|type|engagement|source|platform|retrieved|published|"
    r"from|to|issued|fingerprint|priority|status|claimed-by|claimed-at|completed-at|exit-code|"
    r"timeout|views|likes|reposts|bookmarks|reply count|video url|presentation url|watch url|"
    r"archive url|extraction date|summary url|canonical url)"
    r"(?:\*\*)?\s*[:|-]\s*",
    re.I,
)
WRAPPER_HEADING_RE = re.compile(
    r"^\s{0,3}#{1,6}\s+"
    r"(article content|content|main content|thread content|body|transcript|extraction|text|"
    r"post content|full text|primary text)\s*$",
    re.I,
)
REFERENCES_HEADING_RE = re.compile(
    r"^\s{0,3}#{1,6}\s+(references|resources(?:\s*&\s*references)?|cross-references.*?)\s*$",
    re.I,
)

TEXTUAL_EXTENSIONS = {
    "",
    ".complete",
    ".csv",
    ".heartbeat",
    ".json",
    ".jsonl",
    ".lock",
    ".log",
    ".md",
    ".orchestrator_last_run",
    ".plist",
    ".py",
    ".sh",
    ".txt",
    ".watchdog_state",
    ".xml",
    ".yaml",
}

SKIP_EXTENSIONS = {".jpeg", ".jpg", ".png", ".gif", ".pdf"}

MERGE_METADATA_KEYS = ["author", "handle", "date", "url", "engagement", "source", "platform", "published"]
TITLE_STOPWORDS = {
    "a",
    "an",
    "and",
    "as",
    "at",
    "by",
    "for",
    "from",
    "in",
    "of",
    "on",
    "or",
    "the",
    "to",
    "with",
}


@dataclass
class FileRecord:
    name: str
    ext: str
    raw_text: str
    raw_length: int
    metadata: Dict[str, List[str]]
    metadata_line_count: int
    normalized_body: str
    fingerprint: str
    tokens: List[str]
    shingles: Set[str]
    has_references: bool
    title: str


def numeric_sort_key(name: str) -> Tuple[int, str]:
    stem = name.split(".", 1)[0]
    return int(stem), name


def list_target_files() -> List[str]:
    files = []
    for name in os.listdir(ROOT):
        path = os.path.join(ROOT, name)
        if not os.path.isfile(path):
            continue
        if not NUMERIC_FILE_RE.fullmatch(name):
            continue
        files.append(name)
    files.sort(key=numeric_sort_key)
    return files


def is_probably_binary(data: bytes) -> bool:
    if not data:
        return False
    if b"\x00" in data:
        return True
    sample = data[:2048]
    control_count = sum(1 for b in sample if b < 9 or 13 < b < 32)
    return control_count / max(len(sample), 1) > 0.15


def read_text(path: str, ext: str) -> str:
    if ext in SKIP_EXTENSIONS:
        return ""
    with open(path, "rb") as fh:
        data = fh.read()
    if is_probably_binary(data):
        return ""
    return data.decode("utf-8", errors="replace")


def collect_text_fragments(value, key_hint: Optional[str] = None) -> List[str]:
    fragments: List[str] = []
    if isinstance(value, str):
        text = value.strip()
        if not text:
            return fragments
        if key_hint and key_hint.lower() in {"uuid", "id", "ts", "timestamp", "path", "agent", "scope", "kind"}:
            return fragments
        if len(text) >= 24 or any(ch.isspace() for ch in text):
            fragments.append(text)
        return fragments
    if isinstance(value, dict):
        preferred_keys = [
            "content",
            "text",
            "body",
            "message",
            "prompt",
            "summary",
            "title",
            "description",
            "objective",
            "response",
        ]
        used = set()
        for key in preferred_keys:
            if key in value:
                used.add(key)
                fragments.extend(collect_text_fragments(value[key], key))
        for key, nested in value.items():
            if key in used:
                continue
            fragments.extend(collect_text_fragments(nested, key))
        return fragments
    if isinstance(value, list):
        for item in value:
            fragments.extend(collect_text_fragments(item, key_hint))
    return fragments


def extract_structured_text(name: str, raw_text: str) -> str:
    ext = os.path.splitext(name)[1].lower()
    if ext == ".jsonl":
        fragments: List[str] = []
        for line in raw_text.splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                fragments.append(line)
                continue
            fragments.extend(collect_text_fragments(obj))
        return "\n".join(fragment for fragment in fragments if fragment)
    if ext == ".json":
        try:
            obj = json.loads(raw_text)
        except json.JSONDecodeError:
            return raw_text
        fragments = collect_text_fragments(obj)
        return "\n".join(fragment for fragment in fragments if fragment) or raw_text
    return raw_text


def normalize_line(line: str) -> str:
    line = MARKDOWN_LINK_RE.sub(r"\1", line)
    line = URL_RE.sub(" ", line)
    line = re.sub(r"`+", "", line)
    line = re.sub(r"[*_~]+", "", line)
    line = re.sub(r"\s+", " ", line)
    return line.strip()


def canonical_key(line: str) -> Optional[str]:
    match = METADATA_KEY_RE.match(line)
    if not match:
        return None
    return match.group(1).lower().replace(" ", "_")


def title_candidate(line: str) -> str:
    stripped = normalize_line(line.lstrip("#").strip())
    if len(stripped) < 12:
        return ""
    lower = stripped.lower()
    if lower.startswith(("## ", "# ")):
        stripped = normalize_line(stripped.lstrip("#").strip())
    if canonical_key(stripped):
        return ""
    return stripped


def strip_frontmatter(text: str) -> str:
    return FRONTMATTER_RE.sub("", text, count=1)


def extract_metadata_and_body(text: str) -> Tuple[Dict[str, List[str]], int, str, bool, str]:
    text = strip_frontmatter(text.replace("\r\n", "\n").replace("\r", "\n"))
    lines = text.split("\n")
    metadata: Dict[str, List[str]] = defaultdict(list)
    metadata_lines = 0
    title = ""
    body_lines: List[str] = []
    past_wrapper = False
    references_detected = False
    idx = 0

    while idx < len(lines) and not lines[idx].strip():
        idx += 1

    if idx < len(lines):
        first = lines[idx].strip()
        if first.startswith("#") and not WRAPPER_HEADING_RE.match(first):
            title = title_candidate(first)
            idx += 1

    while idx < len(lines):
        line = lines[idx]
        stripped = line.strip()

        if not stripped:
            if past_wrapper:
                body_lines.append("")
            idx += 1
            continue

        key = canonical_key(stripped)
        if key and not past_wrapper:
            metadata_lines += 1
            value = normalize_line(METADATA_KEY_RE.sub("", stripped, count=1))
            if value:
                metadata[key].append(value)
            idx += 1
            continue

        if stripped in {"---", "***"} and not past_wrapper:
            idx += 1
            continue

        if WRAPPER_HEADING_RE.match(stripped):
            past_wrapper = True
            idx += 1
            continue

        if REFERENCES_HEADING_RE.match(stripped):
            references_detected = True

        past_wrapper = True
        body_lines.append(line)
        idx += 1

    body = "\n".join(body_lines).strip()
    if title:
        body = f"{title}\n\n{body}" if body else title
    return dict(metadata), metadata_lines, body, references_detected, title


def normalize_body(text: str) -> str:
    text = text.replace("\u00a0", " ")
    text = re.sub(r"(?mi)^\(description:.*?\)\s*$", " ", text)
    text = re.sub(r"(?mi)^\[description:.*?\]\s*$", " ", text)
    text = re.sub(r"(?m)^\s{0,3}>\s*", "", text)
    text = re.sub(r"(?m)^\s*[-*]\s+", "", text)
    text = MARKDOWN_LINK_RE.sub(r"\1", text)
    text = URL_RE.sub(" ", text)
    text = re.sub(r"`{3,}.*?`{3,}", " ", text, flags=re.S)
    text = re.sub(r"[`*_~#>|]+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()


def make_shingles(tokens: Sequence[str], n: int = 4) -> Set[str]:
    if not tokens:
        return set()
    if len(tokens) < n:
        return {" ".join(tokens)}
    return {" ".join(tokens[idx : idx + n]) for idx in range(len(tokens) - n + 1)}


def normalize_title_text(title: str) -> str:
    title = title.lower()
    title = re.sub(r"[^\w\s]", " ", title)
    title = re.sub(r"\d+", " ", title)
    title = re.sub(r"\s+", " ", title)
    return title.strip()


def title_tokens(title: str) -> List[str]:
    return [token for token in WORD_RE.findall(normalize_title_text(title)) if token not in TITLE_STOPWORDS]


def title_token_overlap(title_a: str, title_b: str) -> float:
    tokens_a = set(title_tokens(title_a))
    tokens_b = set(title_tokens(title_b))
    if not tokens_a or not tokens_b:
        return 0.0
    return len(tokens_a & tokens_b) / len(tokens_a | tokens_b)


def title_stem(title: str) -> str:
    return " ".join(title_tokens(title))


def content_containment(shorter: str, longer: str) -> float:
    if not shorter or not longer:
        return 0.0
    if shorter in longer:
        return 1.0
    shorter_shingles = make_shingles(WORD_RE.findall(shorter), 4)
    longer_shingles = make_shingles(WORD_RE.findall(longer), 4)
    if not shorter_shingles or not longer_shingles:
        return SequenceMatcher(None, shorter[:500], longer[:500]).ratio()
    overlap = len(shorter_shingles & longer_shingles)
    return overlap / len(shorter_shingles)


def overlap_ratio(text_a: str, text_b: str) -> float:
    if not text_a or not text_b:
        return 0.0
    tokens_a = WORD_RE.findall(text_a)
    tokens_b = WORD_RE.findall(text_b)
    shingles_a = make_shingles(tokens_a, 4)
    shingles_b = make_shingles(tokens_b, 4)
    if not shingles_a or not shingles_b:
        return SequenceMatcher(None, text_a, text_b).ratio()
    shared = len(shingles_a & shingles_b)
    return shared / min(len(shingles_a), len(shingles_b))


def build_record(name: str) -> Optional[FileRecord]:
    ext = os.path.splitext(name)[1].lower()
    if ext not in TEXTUAL_EXTENSIONS:
        return None
    raw_text = read_text(os.path.join(ROOT, name), ext)
    if not raw_text.strip():
        return None
    structured = extract_structured_text(name, raw_text)
    metadata, metadata_lines, body, has_references, title = extract_metadata_and_body(structured)
    normalized_body = normalize_body(body)
    if len(normalized_body) < 180:
        return None
    fingerprint = normalized_body[:500]
    tokens = WORD_RE.findall(fingerprint)
    if len(tokens) < 25:
        return None
    shingles = make_shingles(tokens, 4)
    return FileRecord(
        name=name,
        ext=ext,
        raw_text=raw_text,
        raw_length=len(raw_text),
        metadata=metadata,
        metadata_line_count=metadata_lines,
        normalized_body=normalized_body,
        fingerprint=fingerprint,
        tokens=tokens,
        shingles=shingles,
        has_references=has_references,
        title=title,
    )


def generate_candidates(records: List[FileRecord]) -> Set[Tuple[int, int]]:
    inverted: Dict[str, List[int]] = defaultdict(list)
    for idx, record in enumerate(records):
        for shingle in record.shingles:
            inverted[shingle].append(idx)

    pair_counts: Counter[Tuple[int, int]] = Counter()
    for indices in inverted.values():
        if len(indices) < 2 or len(indices) > 24:
            continue
        for a, b in itertools.combinations(sorted(indices), 2):
            pair_counts[(a, b)] += 1

    candidates: Set[Tuple[int, int]] = set()
    for (a, b), shared_count in pair_counts.items():
        min_shingles = min(len(records[a].shingles), len(records[b].shingles))
        if shared_count >= max(3, int(min_shingles * 0.35)):
            candidates.add((a, b))
    return candidates


def assess_pair(a: FileRecord, b: FileRecord, title_stem_counts: Counter[str]) -> Optional[Dict[str, object]]:
    prefix_ratio = SequenceMatcher(None, a.fingerprint, b.fingerprint).ratio()
    shared_prefix_overlap = overlap_ratio(a.fingerprint, b.fingerprint)
    containment_ab = content_containment(a.fingerprint, b.fingerprint)
    containment_ba = content_containment(b.fingerprint, a.fingerprint)
    full_containment_ab = content_containment(a.normalized_body[:8000], b.normalized_body[:8000])
    full_containment_ba = content_containment(b.normalized_body[:8000], a.normalized_body[:8000])

    overlap = max(shared_prefix_overlap, containment_ab, containment_ba)
    if prefix_ratio < 0.82 and overlap < 0.82:
        return None

    if overlap < 0.88 and prefix_ratio < 0.9:
        return None

    length_a = len(a.normalized_body)
    length_b = len(b.normalized_body)
    shorter = min(length_a, length_b)
    longer = max(length_a, length_b)
    if shorter / longer < 0.55 and max(full_containment_ab, full_containment_ba) < 0.94:
        return None

    max_full_containment = max(full_containment_ab, full_containment_ba)
    both_md = a.ext == ".md" and b.ext == ".md"

    if both_md:
        title_ratio = SequenceMatcher(None, a.title.lower(), b.title.lower()).ratio() if a.title and b.title else 0.0
        token_overlap = title_token_overlap(a.title, b.title) if a.title and b.title else 0.0
        if title_ratio < 0.8:
            return None
        if title_ratio < 0.95:
            if max_full_containment < 0.94 or token_overlap < 0.6:
                return None
        else:
            stem_a = title_stem(a.title)
            stem_b = title_stem(b.title)
            common_template = stem_a and stem_a == stem_b and title_stem_counts[stem_a] > 3
            if common_template and max_full_containment < 0.98:
                return None
            if max_full_containment < 0.82 and prefix_ratio < 0.98:
                return None
    else:
        if max_full_containment < 0.98:
            return None

    return {
        "prefix_ratio": round(prefix_ratio, 4),
        "prefix_overlap": round(overlap, 4),
        "full_containment_ab": round(full_containment_ab, 4),
        "full_containment_ba": round(full_containment_ba, 4),
        "length_a": length_a,
        "length_b": length_b,
    }


def file_richness(record: FileRecord) -> int:
    score = min(len(record.normalized_body), 12000)
    score += min(record.raw_length, 12000) // 8
    score += record.metadata_line_count * 120
    if record.has_references:
        score += 500
    if record.ext == ".md":
        score += 80
    return score


def metadata_gap(keeper: FileRecord, merge: FileRecord) -> List[str]:
    missing = []
    for key in MERGE_METADATA_KEYS:
        keeper_values = {value.lower() for value in keeper.metadata.get(key, [])}
        merge_values = [value for value in merge.metadata.get(key, []) if value.lower() not in keeper_values]
        if merge_values:
            missing.append(key)
    return missing


def appears_truncated(shorter: FileRecord, longer: FileRecord) -> bool:
    if len(shorter.normalized_body) >= len(longer.normalized_body):
        return False
    if len(shorter.normalized_body) >= int(len(longer.normalized_body) * 0.9):
        return False
    ending = shorter.raw_text.rstrip()[-120:].strip()
    if not ending:
        return True
    if ending.endswith(("...", "…")):
        return True
    if ending and ending[-1].isalnum():
        return True
    return False


def pick_keeper(a: FileRecord, b: FileRecord) -> Tuple[FileRecord, FileRecord]:
    score_a = file_richness(a)
    score_b = file_richness(b)
    if score_a != score_b:
        return (a, b) if score_a > score_b else (b, a)
    return (a, b) if numeric_sort_key(a.name) < numeric_sort_key(b.name) else (b, a)


def classify_action(keeper: FileRecord, merge: FileRecord, metrics: Dict[str, object]) -> Tuple[str, str]:
    missing_metadata = metadata_gap(keeper, merge)
    length_keeper = len(keeper.normalized_body)
    length_merge = len(merge.normalized_body)

    if missing_metadata:
        reason = (
            f"Same core content after metadata stripping; keep richer version and merge unique "
            f"{', '.join(missing_metadata)} from {merge.name}."
        )
        return "delete_merge", reason

    if appears_truncated(merge, keeper):
        reason = "Merge file is a truncated cut of the keeper's content after wrapper normalization."
        return "delete_truncated", reason

    if length_merge < length_keeper:
        reason = "Merge file is a subset of the keeper after wrapper normalization and adds no unique metadata."
        return "delete_subset", reason

    reason = "Same content with formatting-only differences; merge file adds no unique metadata."
    return "delete_subset", reason


def connected_components(edges: Iterable[Tuple[str, str]]) -> List[Set[str]]:
    graph: Dict[str, Set[str]] = defaultdict(set)
    for left, right in edges:
        graph[left].add(right)
        graph[right].add(left)
    seen: Set[str] = set()
    components: List[Set[str]] = []
    for node in graph:
        if node in seen:
            continue
        stack = [node]
        component = set()
        seen.add(node)
        while stack:
            current = stack.pop()
            component.add(current)
            for nxt in graph[current]:
                if nxt in seen:
                    continue
                seen.add(nxt)
                stack.append(nxt)
        components.append(component)
    return components


def build_adjudications(
    records: List[FileRecord],
    match_rows: List[Dict[str, object]],
    title_stem_counts: Counter[str],
) -> List[Tuple[str, str, str, str]]:
    by_name = {record.name: record for record in records}
    edges = [(row["a"], row["b"]) for row in match_rows]
    metrics_lookup = {
        tuple(sorted((row["a"], row["b"]))): row["metrics"]
        for row in match_rows
    }
    components = connected_components(edges)
    adjudications: List[Tuple[str, str, str, str]] = []

    for component in components:
        component_records = sorted((by_name[name] for name in component), key=lambda item: numeric_sort_key(item.name))
        keeper = component_records[0]
        for record in component_records[1:]:
            keeper = pick_keeper(keeper, record)[0]

        for record in component_records:
            if record.name == keeper.name:
                continue
            pair_metrics = metrics_lookup.get(tuple(sorted((keeper.name, record.name))))
            if not pair_metrics:
                pair_metrics = assess_pair(keeper, record, title_stem_counts)
                if not pair_metrics:
                    continue
            action, reason = classify_action(keeper, record, pair_metrics)
            adjudications.append((keeper.name, record.name, action, reason))

    adjudications.sort(key=lambda row: (numeric_sort_key(row[0]), numeric_sort_key(row[1])))
    return adjudications


def write_outputs(total_files: int, analyzed_files: int, matches: List[Dict[str, object]], adjudications: List[Tuple[str, str, str, str]]) -> None:
    with open(TSV_PATH, "w", encoding="utf-8") as fh:
        for keeper, merge, action, reason in adjudications:
            fh.write(f"{keeper}\t{merge}\t{action}\t{reason}\n")

    action_counts = Counter(action for _, _, action, _ in adjudications)
    with open(SUMMARY_PATH, "w", encoding="utf-8") as fh:
        fh.write("# Near-Duplicate Adjudication Summary\n\n")
        fh.write(f"- Numeric corpus files scanned: {total_files}\n")
        fh.write(f"- Files with sufficient textual content to analyze: {analyzed_files}\n")
        fh.write(f"- High-confidence near-duplicate matches found: {len(matches)}\n")
        fh.write(f"- Adjudicated delete candidates: {len(adjudications)}\n")
        fh.write(f"- `delete_merge`: {action_counts['delete_merge']}\n")
        fh.write(f"- `delete_subset`: {action_counts['delete_subset']}\n")
        fh.write(f"- `delete_truncated`: {action_counts['delete_truncated']}\n\n")
        if adjudications:
            fh.write("## Keeper Clusters\n\n")
            grouped: Dict[str, List[Tuple[str, str, str]]] = defaultdict(list)
            for keeper, merge, action, reason in adjudications:
                grouped[keeper].append((merge, action, reason))
            for keeper in sorted(grouped, key=numeric_sort_key):
                fh.write(f"### {keeper}\n\n")
                for merge, action, reason in grouped[keeper]:
                    fh.write(f"- `{merge}` -> `{action}`: {reason}\n")
                fh.write("\n")

    with open(REVIEW_PATH, "w", encoding="utf-8") as fh:
        json.dump(
            {
                "total_files": total_files,
                "analyzed_files": analyzed_files,
                "matches": matches,
                "adjudications": [
                    {"keeper": keeper, "merge": merge, "action": action, "reason": reason}
                    for keeper, merge, action, reason in adjudications
                ],
            },
            fh,
            indent=2,
        )


def main() -> None:
    target_files = list_target_files()
    records = [record for record in (build_record(name) for name in target_files) if record]
    title_stem_counts = Counter(
        title_stem(record.title)
        for record in records
        if record.ext == ".md" and title_stem(record.title)
    )
    candidates = generate_candidates(records)

    matches: List[Dict[str, object]] = []
    for idx_a, idx_b in sorted(candidates):
        record_a = records[idx_a]
        record_b = records[idx_b]
        metrics = assess_pair(record_a, record_b, title_stem_counts)
        if not metrics:
            continue
        matches.append({"a": record_a.name, "b": record_b.name, "metrics": metrics})

    adjudications = build_adjudications(records, matches, title_stem_counts)
    write_outputs(len(target_files), len(records), matches, adjudications)


if __name__ == "__main__":
    main()
