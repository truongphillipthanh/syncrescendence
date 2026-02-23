# Gemini Refinement Pass — Ready

## Script Location
`/Users/system/syncrescendence/00-ORCHESTRATION/scripts/gemini_refine.py`

## How to Run
```bash
source ~/.syncrescendence/venv/bin/activate && python3 /Users/system/syncrescendence/00-ORCHESTRATION/scripts/gemini_refine.py
```

### Flags
- `--dry-run` — show what would be sent without calling API or modifying files
- `--max N` — limit to first N files (useful for testing)
- `--verbose` — print each file as it is processed
- `--resume` — skip files already refined (tracked in `04-SOURCES/_meta/.gemini_refined.txt`)

### Example: test with 5 files
```bash
python3 gemini_refine.py --max 5 --verbose
```

### Example: resume after quota exhaustion
```bash
python3 gemini_refine.py --resume --verbose
```

## Cost Estimate
- Model: `gemini-2.0-flash-lite` (cheapest tier)
- ~$0.002/file x 743 files = **~$1.50 total**
- Free tier: 15 RPM, 1M tokens/day

## Quota
- Resets at **midnight Pacific Time** daily
- On 429 (quota exhausted), the script stops gracefully and reports progress
- Use `--resume` to continue the next day

## Estimated Time
- 15 RPM with 4-second delay between requests
- ~743 files / 15 per minute = **~50 minutes**

## What It Refines
- Files where `notebooklm_category: ai-engineering` (heuristic fallback default, ~743 files)
- Files where `synopsis` starts with the title (auto-generated thin synopsis)
- Fields updated: `signal_tier`, `teleology`, `notebooklm_category`, `topics`, `synopsis`
