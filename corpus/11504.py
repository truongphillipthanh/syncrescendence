#!/usr/bin/env python3
"""
Gemini API refinement pass for SOURCE-*.md files.
Improves heuristic-only classifications from batch_enrich.py by sending
title/creator/content to Gemini 2.0 Flash Lite for proper classification.

Usage:
    python3 gemini_refine.py [--dry-run] [--max N] [--verbose] [--resume]
"""
from config import *

import argparse
import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

SOURCES_DIR = Path("/Users/system/Desktop/syncrescendence/sources")
API_KEY_FILE = Path("/Users/system/.syncrescendence/gemini_api_key.txt")
MARKER_FILE = SOURCES_DIR / "_meta" / ".gemini_refined.txt"
ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-lite:generateContent"
DELAY_SECONDS = 4  # ~15 RPM

VALID_SIGNAL_TIERS = {"paradigm", "strategic", "tactical"}
VALID_TELEOLOGIES = {"extract", "implement", "strategize", "synthesize", "contextualize", "inspire", "reference"}
VALID_CATEGORIES = {
    "claude-code", "coding-tools", "ai-engineering", "agents-orchestration",
    "philosophy-paradigm", "career-growth", "vibe-coding", "prompt-engineering",
    "ai-creative-media", "syncrescendence"
}

PROMPT_TEMPLATE = """Classify this content for a knowledge management system.

Title: {title}
Creator: {creator}
Content preview: {content_preview}

Return ONLY a JSON object with these fields:
- signal_tier: one of "paradigm", "strategic", "tactical"
- teleology: one of "extract", "implement", "strategize", "synthesize", "contextualize", "inspire", "reference"
- notebooklm_category: one of "claude-code", "coding-tools", "ai-engineering", "agents-orchestration", "philosophy-paradigm", "career-growth", "vibe-coding", "prompt-engineering", "ai-creative-media", "syncrescendence"
- topics: array of 3-5 lowercase topic tags
- synopsis: 2-3 sentence summary of what this content says and why it matters"""


def load_api_key() -> str:
    if not API_KEY_FILE.exists():
        print(f"ERROR: API key file not found: {API_KEY_FILE}", file=sys.stderr)
        sys.exit(1)
    return API_KEY_FILE.read_text().strip()


def load_refined_set() -> set:
    if MARKER_FILE.exists():
        return set(MARKER_FILE.read_text().strip().splitlines())
    return set()


def save_refined(filename: str):
    MARKER_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(MARKER_FILE, "a") as f:
        f.write(filename + "\n")


def parse_frontmatter(text: str) -> tuple[dict, str, int, int]:
    """Return (frontmatter_dict, body, fm_start_line, fm_end_line).
    fm_start_line and fm_end_line are character offsets of the --- delimiters."""
    m = re.match(r'^---\n(.*?\n)---\n', text, re.DOTALL)
    if not m:
        return {}, text, 0, 0
    fm_text = m.group(1)
    fm_end = m.end()
    body = text[fm_end:]

    fm = {}
    current_key = None
    current_list = None
    for line in fm_text.splitlines():
        # List item
        list_m = re.match(r'^  - (.+)$', line)
        if list_m and current_key:
            val = list_m.group(1).strip().strip('"').strip("'")
            if current_list is not None:
                current_list.append(val)
            continue

        # Key-value
        kv_m = re.match(r'^([a-z_]+):\s*(.*)', line)
        if kv_m:
            key = kv_m.group(1)
            val = kv_m.group(2).strip()
            if val == '' or val == '[]':
                fm[key] = []
                current_key = key
                current_list = fm[key]
            else:
                val = val.strip('"').strip("'")
                if val == 'null':
                    val = None
                fm[key] = val
                current_key = key
                current_list = None
        else:
            current_key = None
            current_list = None

    return fm, body, 0, fm_end


def needs_refinement(fm: dict, body: str) -> bool:
    cat = fm.get("notebooklm_category", "")
    if cat == "ai-engineering":
        return True
    synopsis = fm.get("synopsis", "")
    title = fm.get("title", "")
    if synopsis and title and synopsis.startswith(title[:30]):
        return True
    return False


def update_frontmatter_field(text: str, key: str, value) -> str:
    """Update a single frontmatter field in the raw text."""
    if isinstance(value, list):
        # Replace array field
        # First, remove existing array entries
        pattern = rf'^({key}:).*$'
        lines = text.split('\n')
        new_lines = []
        skip_list = False
        found = False
        for line in lines:
            if re.match(rf'^{key}:', line):
                found = True
                if not value:
                    new_lines.append(f'{key}: []')
                else:
                    new_lines.append(f'{key}:')
                    for item in value:
                        new_lines.append(f'  - "{item}"')
                skip_list = True
                continue
            if skip_list:
                if re.match(r'^  - ', line):
                    continue
                else:
                    skip_list = False
            new_lines.append(line)
        return '\n'.join(new_lines)
    else:
        # Replace scalar field
        val_str = f'"{value}"' if isinstance(value, str) and (' ' in value or ':' in value or ',' in value) else str(value)
        pattern = rf'^({key}:)\s*.*$'
        result = re.sub(pattern, rf'\1 {val_str}', text, count=1, flags=re.MULTILINE)
        return result


def call_gemini(api_key: str, prompt: str) -> dict | None:
    url = f"{ENDPOINT}?key={api_key}"
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseMimeType": "application/json"}
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        if e.code == 429:
            return {"__quota_exhausted": True}
        print(f"  HTTP error {e.code}: {e.reason}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"  Request error: {e}", file=sys.stderr)
        return None

    try:
        text = result["candidates"][0]["content"]["parts"][0]["text"]
        return json.loads(text)
    except (KeyError, IndexError, json.JSONDecodeError) as e:
        print(f"  Failed to parse Gemini response: {e}", file=sys.stderr)
        return None


def main():
    parser = argparse.ArgumentParser(description="Gemini API refinement for SOURCE-*.md files")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without modifying files")
    parser.add_argument("--max", type=int, default=0, help="Max files to process (0=all)")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")
    parser.add_argument("--resume", action="store_true", help="Skip already-refined files")
    args = parser.parse_args()

    api_key = load_api_key()
    refined_set = load_refined_set() if args.resume else set()

    # Collect candidates
    candidates = []
    for f in sorted(SOURCES_DIR.glob("SOURCE-*.md")):
        if args.resume and f.name in refined_set:
            continue
        text = f.read_text(errors="replace")
        fm, body, _, _ = parse_frontmatter(text)
        if needs_refinement(fm, body):
            candidates.append((f, fm, body, text))

    total = len(candidates)
    if args.max > 0:
        candidates = candidates[:args.max]

    print(f"Found {total} files needing refinement, processing {len(candidates)}")

    processed = 0
    updated = 0
    errors = 0

    for i, (filepath, fm, body, original_text) in enumerate(candidates):
        title = fm.get("title", filepath.stem)
        creator = fm.get("creator", "Unknown")
        content_preview = body[:1000]

        prompt = PROMPT_TEMPLATE.format(title=title, creator=creator, content_preview=content_preview)

        if args.verbose:
            print(f"[{i+1}/{len(candidates)}] {filepath.name}")

        if args.dry_run:
            print(f"  DRY RUN: would send to Gemini: {title[:60]}...")
            processed += 1
            if (i + 1) % 10 == 0:
                print(f"  Progress: {i+1}/{len(candidates)}")
            continue

        result = call_gemini(api_key, prompt)

        if result and result.get("__quota_exhausted"):
            print(f"\nQuota exhausted (429). Processed {processed} files, updated {updated}.")
            sys.exit(0)

        if result is None:
            errors += 1
            if (i + 1) % 10 == 0:
                print(f"  Progress: {i+1}/{len(candidates)} (errors: {errors})")
            time.sleep(DELAY_SECONDS)
            continue

        # Validate and apply
        text = original_text
        changed = False

        if result.get("signal_tier") in VALID_SIGNAL_TIERS and result["signal_tier"] != fm.get("signal_tier"):
            text = update_frontmatter_field(text, "signal_tier", result["signal_tier"])
            changed = True

        if result.get("teleology") in VALID_TELEOLOGIES and result["teleology"] != fm.get("teleology"):
            text = update_frontmatter_field(text, "teleology", result["teleology"])
            changed = True

        if result.get("notebooklm_category") in VALID_CATEGORIES and result["notebooklm_category"] != fm.get("notebooklm_category"):
            text = update_frontmatter_field(text, "notebooklm_category", result["notebooklm_category"])
            changed = True

        if isinstance(result.get("topics"), list) and len(result["topics"]) >= 3:
            topics = [str(t).lower() for t in result["topics"][:5]]
            text = update_frontmatter_field(text, "topics", topics)
            changed = True

        if isinstance(result.get("synopsis"), str) and len(result["synopsis"]) > 20:
            title_str = fm.get("title", "")
            # Only overwrite if current synopsis is thin (starts with title)
            current_synopsis = fm.get("synopsis", "")
            if current_synopsis.startswith(title_str[:30]) or fm.get("notebooklm_category") == "ai-engineering":
                text = update_frontmatter_field(text, "synopsis", result["synopsis"])
                changed = True

        if changed:
            filepath.write_text(text)
            updated += 1
            if args.verbose:
                print(f"  UPDATED: {result.get('notebooklm_category', '?')}")

        save_refined(filepath.name)
        processed += 1

        if (i + 1) % 10 == 0:
            print(f"  Progress: {i+1}/{len(candidates)} | updated: {updated} | errors: {errors}")

        time.sleep(DELAY_SECONDS)

    print(f"\nDone. Processed: {processed}, Updated: {updated}, Errors: {errors}")


if __name__ == "__main__":
    main()
