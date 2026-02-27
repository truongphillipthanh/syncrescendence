# BOOT.md

On every session start:

1. cd "$(git rev-parse --show-toplevel)" || exit 1
2. git pull --ff-only
3. make configs
4. Load ACTIVE-TASKS.md
5. Load agents/<self>/inbox/pending/
6. Run inbox triage (per INIT.md)
7. Confirm Objective Lock with Sovereign if any P0 item present
8. Resume from last checkpoint in memory/ daily log
