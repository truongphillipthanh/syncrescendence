#!/usr/bin/env bash
# voice-capture.sh — Record audio, transcribe via Whisper, output text
# Usage: voice-capture.sh [--format] [--clipboard] [--pane PANE_TARGET]

set -euo pipefail

MODEL="${WHISPER_MODEL:-$HOME/.local/share/whisper-models/ggml-base.en.bin}"
RECORDING="/tmp/voice-capture-$(date +%s).wav"
TRANSCRIPT="/tmp/voice-transcript-$(date +%s).txt"

FORMAT=false
CLIPBOARD=false
PANE_TARGET=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --format) FORMAT=true; shift ;;
        --clipboard) CLIPBOARD=true; shift ;;
        --pane) PANE_TARGET="$2"; shift 2 ;;
        *) shift ;;
    esac
done

echo "Recording... Press Ctrl+C to stop."
# Record from default mic (sox)
sox -d -r 16000 -c 1 -b 16 "$RECORDING" silence 1 0.1 1% 1 2.0 3% 2>/dev/null || true

echo "Transcribing..."
whisper-cli -m "$MODEL" -f "$RECORDING" -otxt -of "$TRANSCRIPT" 2>/dev/null
TRANSCRIPT_FILE="${TRANSCRIPT}.txt"

if [[ ! -f "$TRANSCRIPT_FILE" ]]; then
    echo "Error: Transcription failed"
    exit 1
fi

TEXT=$(cat "$TRANSCRIPT_FILE" | sed 's/^\[.*\] //g' | tr -s ' ')

if $CLIPBOARD; then
    echo "$TEXT" | pbcopy
    echo "Copied to clipboard"
fi

if [[ -n "$PANE_TARGET" ]]; then
    tmux send-keys -t "$PANE_TARGET" "$TEXT" Enter
    echo "Sent to tmux pane: $PANE_TARGET"
fi

echo "$TEXT"

# Cleanup
rm -f "$RECORDING" "$TRANSCRIPT_FILE"
