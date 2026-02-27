#!/usr/bin/env python3
"""
ingest_chatgpt_container.py

Ingests a single ChatGPT response containing Readable and Directive Pack sections
and files them into -OUTGOING.

Input Format (Container/Blitzkrieg mode):
    ===READABLE===
    ...human text...
    ===DIRECTIVE_PACK===
    ---FILE: context.md---
    ...content...
    ---FILE: pedigree.md---
    ...content...
    ---FILE: directive-A.md---
    ...content...
    ===END===

Note: Transcripts (follow-along audio scripts) are now delivered as the final
fenced code block in standard responses, not via container markers. They are
for in-thread use, not filed by this script.

Output Structure:
    -OUTGOING/<DATE>-blitzkrieg-<slug>/01_context/context.md      (Context)
    -OUTGOING/<DATE>-blitzkrieg-<slug>/02_pedigree/pedigree.md    (Pedigree)
    -OUTGOING/<DATE>-blitzkrieg-<slug>/04_directives/*.md         (Directives)
    -OUTGOING/<DATE>-blitzkrieg-<slug>/06_return_to_webapp/merged_return_packet.md (Readable)
"""

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Optional


def get_repo_root() -> Path:
    """Get repository root via git rev-parse --show-toplevel."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            check=True,
        )
        return Path(result.stdout.strip())
    except subprocess.CalledProcessError:
        # Fallback: assume script is in orchestration/scripts/
        script_dir = Path(__file__).resolve().parent
        return script_dir.parent.parent


def parse_container(content: str) -> dict:
    """
    Parse ChatGPT container format into sections.

    Returns dict with keys: readable, directive_pack (list of {filename, content})

    Note: AUDIZABLE marker is retired. Transcripts are now extracted as the final
    fenced code block in standard responses, not via container markers.
    """
    result = {
        "readable": None,
        "directive_pack": [],
    }

    # Extract sections using markers
    readable_match = re.search(
        r"===READABLE===\s*(.*?)\s*(?====DIRECTIVE_PACK===|===END===|$)",
        content,
        re.DOTALL,
    )
    if readable_match:
        result["readable"] = readable_match.group(1).strip()

    directive_match = re.search(
        r"===DIRECTIVE_PACK===\s*(.*?)\s*(?====READABLE===|===END===|$)",
        content,
        re.DOTALL,
    )
    if directive_match:
        directive_content = directive_match.group(1)
        # Parse individual files within directive pack
        # Pattern: ---FILE: filename.md--- (filename may contain dashes)
        # Use findall to extract (filename, content) pairs
        file_pattern = r"---FILE:\s*(.+?)---\s*(.*?)(?=---FILE:|$)"
        file_matches = re.findall(file_pattern, directive_content, re.DOTALL)
        for filename, file_content in file_matches:
            result["directive_pack"].append({
                "filename": filename.strip(),
                "content": file_content.strip(),
            })

    return result


def route_directive_file(filename: str) -> tuple[str, str]:
    """
    Determine output subdirectory and final filename for a directive pack file.

    Returns: (subdirectory, output_filename)
    """
    filename_lower = filename.lower()

    if "context" in filename_lower:
        return "01_context", filename
    elif "pedigree" in filename_lower:
        return "02_pedigree", filename
    elif "directive" in filename_lower:
        return "04_directives", filename
    else:
        # Default unknown files to directives
        return "04_directives", filename


def safe_write_path(target_path: Path, force: bool = False) -> Path:
    """
    Get a safe write path, adding suffix if file exists and force=False.

    Returns path that is safe to write to.
    """
    if force or not target_path.exists():
        return target_path

    # Find next available suffix
    base = target_path.stem
    ext = target_path.suffix
    parent = target_path.parent

    suffix = 1
    while True:
        new_name = f"{base}-{suffix:02d}{ext}"
        new_path = parent / new_name
        if not new_path.exists():
            return new_path
        suffix += 1


def ingest_container(
    content: str,
    date: str,
    slug: str,
    repo_root: Path,
    force: bool = False,
    dry_run: bool = False,
) -> dict:
    """
    Process container content and write files to appropriate locations.

    Returns dict with created file paths.
    """
    parsed = parse_container(content)
    created_files = []

    # Validate we have at least some content
    if not any([parsed["readable"], parsed["directive_pack"]]):
        raise ValueError("No valid sections found in input. Expected ===READABLE=== or ===DIRECTIVE_PACK=== markers.")

    # Build output directory paths
    outgoing_dir = repo_root / "-OUTGOING"

    # Ensure base directory exists (should already exist per constitution)
    # NEVER create OUTGOING/ or outgoing/ - only -OUTGOING/
    if not outgoing_dir.exists():
        if dry_run:
            print(f"[DRY-RUN] Would create: {outgoing_dir}")
        else:
            outgoing_dir.mkdir(parents=True, exist_ok=True)

    # Process Directive Pack and Readable → -OUTGOING/<DATE>-blitzkrieg-<slug>/
    blitzkrieg_dir = outgoing_dir / f"{date}-blitzkrieg-{slug}"

    # Process Directive Pack files
    if parsed["directive_pack"]:
        for file_info in parsed["directive_pack"]:
            subdir, out_filename = route_directive_file(file_info["filename"])
            target_dir = blitzkrieg_dir / subdir
            target_file = target_dir / out_filename

            if dry_run:
                print(f"[DRY-RUN] Would create: {target_dir}")
                print(f"[DRY-RUN] Would write: {target_file}")
            else:
                target_dir.mkdir(parents=True, exist_ok=True)
                safe_path = safe_write_path(target_file, force)
                safe_path.write_text(file_info["content"] + "\n")
                created_files.append(str(safe_path.relative_to(repo_root)))
                if safe_path != target_file:
                    print(f"[WARN] File existed, wrote to: {safe_path.name}")

    # Process Readable → 06_return_to_webapp/merged_return_packet.md
    if parsed["readable"]:
        return_dir = blitzkrieg_dir / "06_return_to_webapp"
        return_file = return_dir / "merged_return_packet.md"

        if dry_run:
            print(f"[DRY-RUN] Would create: {return_dir}")
            print(f"[DRY-RUN] Would write: {return_file}")
        else:
            return_dir.mkdir(parents=True, exist_ok=True)
            safe_path = safe_write_path(return_file, force)
            safe_path.write_text(parsed["readable"] + "\n")
            created_files.append(str(safe_path.relative_to(repo_root)))
            if safe_path != return_file:
                print(f"[WARN] File existed, wrote to: {safe_path.name}")

    return {
        "created_files": created_files,
        "sections_found": {
            "readable": parsed["readable"] is not None,
            "directive_pack_count": len(parsed["directive_pack"]),
        },
    }


def main():
    parser = argparse.ArgumentParser(
        description="Ingest ChatGPT container response and file into repo structure.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  cat response.txt | python ingest_chatgpt_container.py --date 20260118 --slug phoenix
  python ingest_chatgpt_container.py --date 20260118 --slug phoenix --input response.txt
  python ingest_chatgpt_container.py --date 20260118 --slug phoenix --dry-run < response.txt
        """,
    )
    parser.add_argument(
        "--date",
        required=True,
        help="Date in YYYYMMDD format",
    )
    parser.add_argument(
        "--slug",
        required=True,
        help="Slug identifier for this ingestion",
    )
    parser.add_argument(
        "--input",
        "-i",
        type=str,
        default=None,
        help="Input file (default: read from stdin)",
    )
    parser.add_argument(
        "--force",
        "-f",
        action="store_true",
        help="Overwrite existing files without adding suffix",
    )
    parser.add_argument(
        "--dry-run",
        "-n",
        action="store_true",
        help="Show what would be done without making changes",
    )

    args = parser.parse_args()

    # Validate date format
    if not re.match(r"^\d{8}$", args.date):
        print(f"ERROR: Date must be in YYYYMMDD format, got: {args.date}", file=sys.stderr)
        sys.exit(1)

    # Validate slug (no spaces, reasonable characters)
    if not re.match(r"^[a-zA-Z0-9_-]+$", args.slug):
        print(f"ERROR: Slug must contain only alphanumeric, underscore, or hyphen characters", file=sys.stderr)
        sys.exit(1)

    # Read input
    if args.input:
        input_path = Path(args.input)
        if not input_path.exists():
            print(f"ERROR: Input file not found: {args.input}", file=sys.stderr)
            sys.exit(1)
        content = input_path.read_text()
    else:
        content = sys.stdin.read()

    if not content.strip():
        print("ERROR: Empty input", file=sys.stderr)
        sys.exit(1)

    repo_root = get_repo_root()

    try:
        result = ingest_container(
            content=content,
            date=args.date,
            slug=args.slug,
            repo_root=repo_root,
            force=args.force,
            dry_run=args.dry_run,
        )

        # Output summary
        print(f"\n{'[DRY-RUN] ' if args.dry_run else ''}Ingestion complete:")
        print(f"  Readable: {'found' if result['sections_found']['readable'] else 'not found'}")
        print(f"  Directive Pack: {result['sections_found']['directive_pack_count']} file(s)")

        if result["created_files"]:
            print(f"\n{'Would create' if args.dry_run else 'Created'} files:")
            for f in result["created_files"]:
                print(f"  {f}")

    except ValueError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
