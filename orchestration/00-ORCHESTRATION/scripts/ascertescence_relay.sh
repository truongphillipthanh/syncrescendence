#!/usr/bin/env bash
# ascertescence_relay.sh — Sequential leg-by-leg relay for the ascertescence triangulation cycle
#
# WORKFLOW (sequential — one file at a time):
#   1. Commander creates PROMPT-COMMANDER-ASCERTESCENCE-CC{N}.md in engine/02-ENGINE/
#   2. This script rsyncs it to ~/Desktop/ RENAMED with the target agent's RESPONSE- prefix
#   3. Sovereign overwrites that Desktop file with the agent's actual response
#   4. Sovereign drags the file into Commander's inbox alias (-INBOX/commander/00-INBOX0/)
#   5. Sovereign tells Commander "Oracle just landed"
#   6. Commander reads response, creates next leg's prompt, then calls this script again
#
# USAGE:
# LEG ORDER: Oracle (1st) → Diviner (2nd) → Adjudicator (3rd, last)
#
# RELAY MODES:
#   Oracle and Diviner: chat relay via web app (Sovereign pastes prompt, overwrites Desktop file
#     with response, drags into Commander inbox). Do NOT use Gemini CLI for Diviner (nerfed).
#   Adjudicator: Codex Desktop App (NOT Codex CLI — two separate products). Adjudicator writes
#     its response directly into the Desktop file. Sovereign drops it into Commander inbox.
#
#   ascertescence_relay.sh <N> send oracle        [LEG 1]
#     → copies PROMPT-COMMANDER-ASCERTESCENCE-CC{N}.md
#           to ~/Desktop/RESPONSE-ORACLE-ASCERTESCENCE-CC{N}.md
#     → Sovereign relays via Grok web chat, overwrites file, drags to inbox
#
#   ascertescence_relay.sh <N> send diviner       [LEG 2]
#     → copies PROMPT-COMMANDER-ASCERTESCENCE-CC{N}-DIV.md
#           to ~/Desktop/RESPONSE-DIVINER-ASCERTESCENCE-CC{N}.md
#     → Sovereign relays via Gemini Pro 3.1 web chat, overwrites file, drags to inbox
#
#   ascertescence_relay.sh <N> send adjudicator   [LEG 3 — LAST]
#     → copies PROMPT-COMMANDER-ASCERTESCENCE-CC{N}-ADJ.md
#           to ~/Desktop/RESPONSE-ADJUDICATOR-ASCERTESCENCE-CC{N}.md
#     → Adjudicator (Codex Desktop App) writes response directly into this file.
#       Sovereign drops it into Commander inbox as a self-check gate.
#
#   ascertescence_relay.sh index
#     → scans engine/02-ENGINE/ for all CC sessions and -INBOX for responses,
#       prints completion status per leg

set -euo pipefail

# ── Resolve repo root ──────────────────────────────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"

ENGINE_DIR="$REPO_ROOT/engine/02-ENGINE"
INBOX_DIR="$REPO_ROOT/-INBOX/commander/00-INBOX0"
DESKTOP="$HOME/Desktop"

# ── Argument parsing ───────────────────────────────────────────────────────────
usage() {
    echo "Usage:"
    echo "  ascertescence_relay.sh <N> send oracle|adjudicator|diviner"
    echo "  ascertescence_relay.sh index"
    exit 1
}

if [ $# -lt 1 ]; then
    usage
fi

# Handle both "<N> send <agent>" and "send <N> <agent>" and "index"
case "$1" in
    index)
        SUBCMD="index"
        ;;
    send)
        SUBCMD="send"
        shift
        ;;
    *[0-9]*)
        # First arg is council number: <N> send <agent>
        COUNCIL_NUM_EARLY="$1"
        shift
        SUBCMD="${1:-}"
        if [ "$SUBCMD" = "send" ]; then
            shift
            AGENT_EARLY="${1:-}"
        else
            usage
        fi
        ;;
    *)
        usage
        ;;
esac

# ── INDEX mode ─────────────────────────────────────────────────────────────────
if [ "$SUBCMD" = "index" ]; then
    echo "ASCERTESCENCE RELAY — SESSION INDEX"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    printf "%-8s  %-12s  %-12s  %-12s\n" "SESSION" "ORACLE" "ADJUDICATOR" "DIVINER"
    echo "────────  ────────────  ────────────  ────────────"

    # Collect all CC session numbers from prompt files in engine
    SESSIONS=""
    for f in "$ENGINE_DIR"/PROMPT-COMMANDER-ASCERTESCENCE-CC*.md; do
        [ -f "$f" ] || continue
        # Extract the number from filename
        base="$(basename "$f")"
        # Remove PROMPT-COMMANDER-ASCERTESCENCE-CC and .md, also strip -ADJ/-DIV suffixes
        num="${base#PROMPT-COMMANDER-ASCERTESCENCE-CC}"
        num="${num%.md}"
        # Skip leg-specific prompts (contain dash after number)
        case "$num" in
            *-*) continue ;;
        esac
        SESSIONS="$SESSIONS $num"
    done

    # Deduplicate and sort
    SESSIONS="$(echo "$SESSIONS" | tr ' ' '\n' | sort -nu | tr '\n' ' ')"

    if [ -z "$(echo "$SESSIONS" | tr -d ' ')" ]; then
        echo "(no sessions found in $ENGINE_DIR)"
        echo ""
        exit 0
    fi

    for N in $SESSIONS; do
        ORACLE_STATUS="—"
        ADJ_STATUS="—"
        DIV_STATUS="—"

        # Check inbox for responses
        if [ -f "$INBOX_DIR/RESPONSE-ORACLE-ASCERTESCENCE-CC${N}.md" ]; then
            ORACLE_STATUS="LANDED"
        elif [ -f "$DESKTOP/RESPONSE-ORACLE-ASCERTESCENCE-CC${N}.md" ]; then
            ORACLE_STATUS="on Desktop"
        elif [ -f "$ENGINE_DIR/PROMPT-COMMANDER-ASCERTESCENCE-CC${N}.md" ]; then
            ORACLE_STATUS="prompt ready"
        fi

        if [ -f "$INBOX_DIR/RESPONSE-ADJUDICATOR-ASCERTESCENCE-CC${N}.md" ]; then
            ADJ_STATUS="LANDED"
        elif [ -f "$DESKTOP/RESPONSE-ADJUDICATOR-ASCERTESCENCE-CC${N}.md" ]; then
            ADJ_STATUS="on Desktop"
        elif [ -f "$ENGINE_DIR/PROMPT-COMMANDER-ASCERTESCENCE-CC${N}-ADJ.md" ]; then
            ADJ_STATUS="prompt ready"
        fi

        if [ -f "$INBOX_DIR/RESPONSE-DIVINER-ASCERTESCENCE-CC${N}.md" ]; then
            DIV_STATUS="LANDED"
        elif [ -f "$DESKTOP/RESPONSE-DIVINER-ASCERTESCENCE-CC${N}.md" ]; then
            DIV_STATUS="on Desktop"
        elif [ -f "$ENGINE_DIR/PROMPT-COMMANDER-ASCERTESCENCE-CC${N}-DIV.md" ]; then
            DIV_STATUS="prompt ready"
        fi

        printf "CC%-6s  %-12s  %-12s  %-12s\n" "$N" "$ORACLE_STATUS" "$ADJ_STATUS" "$DIV_STATUS"
    done

    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "Status meanings:"
    echo "  prompt ready  = prompt file exists in engine/02-ENGINE/, not yet sent"
    echo "  on Desktop    = relay file sitting on Desktop awaiting Sovereign action"
    echo "  LANDED        = response collected into Commander inbox"
    echo "  —             = no prompt file found for this leg"
    exit 0
fi

# ── SEND mode ──────────────────────────────────────────────────────────────────
if [ "$SUBCMD" = "send" ]; then
    # Support both arg orders
    if [ -n "${COUNCIL_NUM_EARLY:-}" ]; then
        COUNCIL_NUM="$COUNCIL_NUM_EARLY"
        AGENT_ARG="${AGENT_EARLY:-}"
    elif [ $# -ge 2 ]; then
        COUNCIL_NUM="$1"
        AGENT_ARG="$2"
    else
        usage
    fi

    case "$AGENT_ARG" in
        oracle|adjudicator|diviner) ;;
        *)
            echo "Error: agent must be oracle, adjudicator, or diviner. Got: $AGENT_ARG"
            exit 1
            ;;
    esac

    AGENT_UPPER="$(echo "$AGENT_ARG" | tr '[:lower:]' '[:upper:]')"

    # Determine source prompt file (leg-specific suffix for adj/div)
    case "$AGENT_ARG" in
        oracle)
            PROMPT_SRC="$ENGINE_DIR/PROMPT-COMMANDER-ASCERTESCENCE-CC${COUNCIL_NUM}.md"
            ;;
        adjudicator)
            PROMPT_SRC="$ENGINE_DIR/PROMPT-COMMANDER-ASCERTESCENCE-CC${COUNCIL_NUM}-ADJ.md"
            ;;
        diviner)
            PROMPT_SRC="$ENGINE_DIR/PROMPT-COMMANDER-ASCERTESCENCE-CC${COUNCIL_NUM}-DIV.md"
            ;;
    esac

    # Desktop destination: named with the RESPONSE- prefix for the target agent
    RESPONSE_DST="$DESKTOP/RESPONSE-${AGENT_UPPER}-ASCERTESCENCE-CC${COUNCIL_NUM}.md"

    echo "ASCERTESCENCE RELAY — CC${COUNCIL_NUM} / ${AGENT_UPPER} LEG"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    if [ ! -f "$PROMPT_SRC" ]; then
        echo "Error: prompt file not found."
        echo "  Expected: $PROMPT_SRC"
        echo ""
        case "$AGENT_ARG" in
            oracle)
                echo "Create it at: engine/02-ENGINE/PROMPT-COMMANDER-ASCERTESCENCE-CC${COUNCIL_NUM}.md"
                ;;
            adjudicator)
                echo "Create it at: engine/02-ENGINE/PROMPT-COMMANDER-ASCERTESCENCE-CC${COUNCIL_NUM}-ADJ.md"
                ;;
            diviner)
                echo "Create it at: engine/02-ENGINE/PROMPT-COMMANDER-ASCERTESCENCE-CC${COUNCIL_NUM}-DIV.md"
                ;;
        esac
        exit 1
    fi

    rsync -a "$PROMPT_SRC" "$RESPONSE_DST"

    echo "  [SENT]  $(basename "$PROMPT_SRC")"
    echo "       →  $RESPONSE_DST"
    echo ""

    case "$AGENT_ARG" in
        oracle)
            echo "NEXT STEPS (Sovereign):"
            echo "  1. Open ~/Desktop/RESPONSE-ORACLE-ASCERTESCENCE-CC${COUNCIL_NUM}.md"
            echo "  2. Relay contents to Oracle (Grok) via chat"
            echo "  3. Overwrite that same file with Oracle's response"
            echo "  4. Drag the file into Commander inbox (-INBOX/commander/00-INBOX0/)"
            echo "  5. Tell Commander: Oracle just landed for CC${COUNCIL_NUM}"
            ;;
        adjudicator)
            echo "NEXT STEPS (Adjudicator — Codex Desktop App, NOT Codex CLI):"
            echo "  Adjudicator writes its response DIRECTLY into:"
            echo "    ~/Desktop/RESPONSE-ADJUDICATOR-ASCERTESCENCE-CC${COUNCIL_NUM}.md"
            echo "  Sovereign: drop the completed file into Commander inbox as a self-check gate."
            echo "  (-INBOX/commander/00-INBOX0/)"
            echo "  Then tell Commander: Adjudicator just landed for CC${COUNCIL_NUM}"
            ;;
        diviner)
            echo "NEXT STEPS (Sovereign):"
            echo "  1. Open ~/Desktop/RESPONSE-DIVINER-ASCERTESCENCE-CC${COUNCIL_NUM}.md"
            echo "  2. Relay contents to Diviner (Gemini) via chat"
            echo "  3. Overwrite that same file with Diviner's response"
            echo "  4. Drag the file into Commander inbox (-INBOX/commander/00-INBOX0/)"
            echo "  5. Tell Commander: Diviner just landed for CC${COUNCIL_NUM}"
            ;;
    esac

    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    exit 0
fi

# ── Unknown subcommand ─────────────────────────────────────────────────────────
usage
