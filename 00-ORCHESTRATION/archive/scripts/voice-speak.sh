#!/usr/bin/env bash
# voice-speak.sh — Text-to-speech with optional persona DSP
# Usage: echo "text" | voice-speak.sh [--persona commander|adjudicator|cartographer|psyche]

set -euo pipefail

VOICE="${PIPER_VOICE:-$HOME/.local/share/piper-voices/en_US-amy-medium.onnx}"
PERSONA=""
TEMP_RAW="/tmp/voice-raw-$(date +%s).wav"
TEMP_DSP="/tmp/voice-dsp-$(date +%s).wav"

while [[ $# -gt 0 ]]; do
    case $1 in
        --persona) PERSONA="$2"; shift 2 ;;
        --voice) VOICE="$2"; shift 2 ;;
        *) shift ;;
    esac
done

# Read text from stdin
TEXT=$(cat)

# Generate speech
echo "$TEXT" | piper --model "$VOICE" --output_file "$TEMP_RAW" 2>/dev/null

if [[ -n "$PERSONA" ]] && [[ -f "$HOME/.config/voice-personas/${PERSONA}.sh" ]]; then
    # Apply DSP persona filter
    bash "$HOME/.config/voice-personas/${PERSONA}.sh" "$TEMP_RAW" "$TEMP_DSP"
    afplay "$TEMP_DSP"
    rm -f "$TEMP_DSP"
else
    afplay "$TEMP_RAW"
fi

rm -f "$TEMP_RAW"
