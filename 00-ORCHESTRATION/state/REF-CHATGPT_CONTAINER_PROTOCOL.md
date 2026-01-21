---
id: chatgpt-container-protocol
kind: protocol
scope: repo
target: chatgpt
owner: Deviser
version: 3.0.0
---

# REF-CHATGPT_CONTAINER_PROTOCOL

## Purpose

Protocol for ingesting structured ChatGPT responses containing Readable, Audizable, and Directive Pack sections into the Syncrescendence repository structure.

## Container Grammar

The ingestion system extracts content deterministically without requiring human-facing labels. ChatGPT produces natural output; automation extracts artifacts reliably.

### Standard Response Format

For everyday responses, ChatGPT produces:
1. **Inline readable content** — normal markdown prose
2. **Final fenced transcript block** — plain text for TTS, always last

The transcript is extracted as the final fenced code block (no language tag). Nothing appears after it.

### Blitzkrieg Container Format (for automation)

When producing full directive packs for ingestion scripts:

```
===READABLE===
Human-readable summary text for return to webapp.
This goes to merged_return_packet.md.

===DIRECTIVE_PACK===
---FILE: context.md---
Context document content here.

---FILE: pedigree.md---
Pedigree/lineage document content.

---FILE: directive-A.md---
First directive specification.

---FILE: directive-B.md---
Second directive specification.

===END===
```

Note: The `===AUDIZABLE===` marker is retired. Transcripts are now extracted as the final fenced code block in standard responses, or omitted from container format (transcript is for in-thread use, not filing).

### Parsing Rules

**Standard responses**:
1. Extract final fenced code block (triple backticks, no language tag) as transcript
2. Everything before the final fence is readable content

**Container format** (Blitzkrieg):
1. **Section markers**: `===SECTION_NAME===` on its own line
2. **File markers**: `---FILE: filename.md---` on its own line
3. **Order-independent**: Sections can appear in any order
4. **Optional sections**: Not all sections required

### Why Final-Fence Over Markers

The "final fenced block = transcript" convention:
- Requires no special markers in everyday responses
- Is structurally unambiguous (last fence wins)
- Enforces the "nothing after transcript" invariant naturally
- Works within ChatGPT's standard output patterns

## Section Requirements

| Section | Required | Output Location |
|---------|----------|-----------------|
| READABLE | No | `-OUTGOING/<DATE>-blitzkrieg-<slug>/06_return_to_webapp/merged_return_packet.md` |
| DIRECTIVE_PACK | No | `-OUTGOING/<DATE>-blitzkrieg-<slug>/{01_context,02_pedigree,04_directives}/` |
| Final fenced block | No | Transcript for in-thread use (not filed by container ingestion) |

At least one section must be present for container ingestion. Standard responses use final-fenced-block for transcript.

## File Routing

Within `===DIRECTIVE_PACK===`, files are routed by filename pattern:

| Filename Pattern | Output Subdirectory |
|------------------|---------------------|
| `*context*` | `01_context/` |
| `*pedigree*` | `02_pedigree/` |
| `*directive*` | `04_directives/` |
| (other) | `04_directives/` |

## Usage

### Basic Usage (stdin)

```bash
cat pasted_response.txt | ./00-ORCHESTRATION/scripts/ingest_chatgpt_container.sh --date YYYYMMDD --slug <slug>
```

### From Clipboard (macOS)

```bash
pbpaste | ./00-ORCHESTRATION/scripts/ingest_chatgpt_container.sh --date 20260118 --slug phoenix
```

### From File

```bash
./00-ORCHESTRATION/scripts/ingest_chatgpt_container.sh --date 20260118 --slug phoenix --input response.txt
```

### Dry Run (Preview)

```bash
cat response.txt | ./00-ORCHESTRATION/scripts/ingest_chatgpt_container.sh --date 20260118 --slug phoenix --dry-run
```

### Force Overwrite

```bash
cat response.txt | ./00-ORCHESTRATION/scripts/ingest_chatgpt_container.sh --date 20260118 --slug phoenix --force
```

## Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `--date YYYYMMDD` | Yes | Date for filing (e.g., 20260118) |
| `--slug <slug>` | Yes | Identifier for this ingestion |
| `--input, -i FILE` | No | Read from file instead of stdin |
| `--force, -f` | No | Overwrite existing files |
| `--dry-run, -n` | No | Preview changes without writing |

## Output Structure

Given `--date 20260118 --slug phoenix`:

```
-OUTGOING/
└── 20260118-blitzkrieg-phoenix/
    ├── 01_context/
    │   └── context.md                 # Context document
    ├── 02_pedigree/
    │   └── pedigree.md                # Pedigree document
    ├── 04_directives/
    │   ├── directive-A.md             # Directive files
    │   ├── directive-B.md
    │   └── directive-C.md
    └── 06_return_to_webapp/
        └── merged_return_packet.md    # READABLE content
```

Note: Transcripts (final fenced blocks) are for in-thread follow-along use, not filed by container ingestion.

## Idempotency Behavior

- **Default**: If a file exists, a numeric suffix is appended (e.g., `phoenix-01.txt`)
- **With `--force`**: Existing files are overwritten without suffix

## Validation

After ingestion, run structural verification:

```bash
./00-ORCHESTRATION/scripts/structural_verify.sh
```

Check for:
- No `OUTGOING/` or `outgoing/` directories created (only `-OUTGOING/`)
- Proper directory structure under `-OUTGOING/<DATE>-blitzkrieg-<slug>/`
- Files present in expected locations

## Integration with Trifurcation

ChatGPT Deviser produces trifurcated output naturally (readable inline, audizable as artifact block, directives when executing). For automation:

1. When asking for "container format" output, ChatGPT wraps content in markers
2. Copy full response to file or clipboard
3. Pipe through ingestion script
4. Script parses markers deterministically

The Deviser prompt (PROMPT-CHATGPT-PROJECT_INSTRUCTIONS-DEVISER.md) documents the container format for consistent output.

## Troubleshooting

### Empty Input Error

Ensure the input contains at least one valid section marker (`===READABLE===` or `===DIRECTIVE_PACK===`).

### Invalid Date Format

Date must be exactly 8 digits in YYYYMMDD format (e.g., `20260118`).

### Invalid Slug

Slug must contain only alphanumeric characters, underscores, or hyphens.

### File Exists Warning

When files exist and `--force` is not set, new files get suffixed. Check output for actual filenames written.

## See Also

- `PROMPT-CHATGPT-PROJECT_INSTRUCTIONS-DEVISER.md` - Trifurcation output format
- `REF-AUDIZER_PROTOCOL.md` - Audio transcoding rules
- `REF-BLITZKRIEG_PROTOCOL_VNEXT.md` - Multi-lane execution protocol
- `blitzkrieg_finalize.sh` - Directive execution script
- `structural_verify.sh` - Constitutional compliance checker
