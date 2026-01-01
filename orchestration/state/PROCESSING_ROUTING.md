# Processing Routing
## Function Selection Based on Source Characteristics

**Version**: 1.0.0
**Created**: 2026-01-01
**Authority**: Oracle9

---

## Routing Logic

Processing function selection depends on:
1. **platform** — Determines native processor (Gemini vs Claude)
2. **format** — Determines structural handling
3. **value_modality** — Determines compression approach

---

## Primary Routing Table

| Platform | Format | Function | Processor |
|----------|--------|----------|-----------|
| youtube | interview | transcribe_interview | Gemini |
| youtube | panel | transcribe_panel | Gemini |
| youtube | solo_presentation | transcribe_youtube | Gemini |
| youtube | tutorial | transcribe_youtube | Gemini |
| youtube | lecture | transcribe_youtube | Gemini |
| podcast | interview | transcribe_interview | Gemini |
| podcast | panel | transcribe_panel | Gemini |
| podcast | solo | transcribe_youtube | Gemini |
| substack | article | readize | Claude |
| substack | essay | readize | Claude |
| newsletter | article | readize | Claude |
| arxiv | paper | (academic_process) | Claude |
| paper | paper | (academic_process) | Claude |
| book | chapter | (chapter_process) | Claude |
| x | thread | (thread_process) | Claude |
| reddit | post | (thread_process) | Claude |
| film | — | (defer to Modal 2) | — |

**Note**: Functions in parentheses are planned but not yet implemented.

---

## value_modality Modifiers

| value_modality | Additional Processing |
|----------------|----------------------|
| dialogue_primary | Standard processing sufficient |
| audio_primary | Note: consider audio consumption |
| visual_primary | Require Gemini visual summary |
| comments_primary | Capture discourse separately |
| multimodal_essential | Defer to Modal 2 / partial only |
| text_native | Direct processing |

---

## Processor Allocation

### Gemini Handles:
- All YouTube processing (native platform)
- All podcast/audio processing (audio transcription)
- Visual summary generation for visual_primary sources
- Speaker diarization for panels

### Claude Handles:
- All text-native sources (articles, papers, threads)
- Synthesis and integration
- Routing decisions
- Infrastructure and orchestration

### Why This Split?

1. **Native capability**: Gemini can directly process YouTube URLs
2. **Multi-modal**: Gemini can see video frames, read slides
3. **Cost efficiency**: Gemini subscription is flat-rate for native content
4. **Quality**: Claude excels at text synthesis and integration

---

## Function Specifications

### transcribe_youtube
**Input**: YouTube video URL or transcript
**Output**: Clean essay with ads/previews removed
**Location**: `OPERATIONAL/functions/transcribe_youtube.xml`

### transcribe_interview
**Input**: Interview transcript
**Output**: Multi-voice narrative, commercials removed
**Location**: `OPERATIONAL/functions/transcribe_interview.xml`

### transcribe_panel
**Input**: Panel discussion transcript
**Output**: Thematic extraction with speaker attribution
**Location**: `OPERATIONAL/functions/transcribe_panel.xml`

### readize
**Input**: Any text
**Output**: Read-optimized crystalline prose
**Location**: `OPERATIONAL/functions/readize.xml`

### integrate
**Input**: Multiple sources
**Output**: Unified synthesis
**Location**: `OPERATIONAL/functions/integrate.xml`

---

## Processing Workflow

```
1. Source arrives in SOURCES/raw/
        ↓
2. Triage assigns dimensions (see TRIAGE_PROTOCOL.md)
        ↓
3. Routing selects function based on:
   - platform → processor
   - format → function
   - value_modality → modifiers
        ↓
4. Execute function
        ↓
5. Output to SOURCES/processed/
        ↓
6. Update status: processed
        ↓
7. Queue for integration (if paradigm/strategic)
```

---

## Edge Cases

### YouTube with essential visuals
- Platform: youtube
- value_modality: visual_primary
- **Action**: Standard transcription + Gemini visual summary

### Podcast that's actually a video
- Platform: podcast (original format)
- **Action**: Process as audio-primary, note video version exists

### X thread with embedded YouTube
- Platform: x (primary)
- **Action**: Process thread as primary, note video separately

### Academic paper with code
- Platform: arxiv
- **Action**: Process paper, code in separate artifact

### Interview vs Solo determination
- **Interview**: Two or more distinct voices in dialogue
- **Solo**: Single speaker, regardless of content type
- **Panel**: Three or more speakers

---

## Future Functions (Planned)

| Function | For | Status |
|----------|-----|--------|
| academic_process | ArXiv, papers | Planned |
| chapter_process | Books | Planned |
| thread_process | X, Reddit | Planned |
| visual_summary | Visual-primary | Planned (Gemini) |

---

## Cross-References

- **Sources Schema**: See `SOURCES_SCHEMA.md` for dimension definitions
- **Triage Protocol**: See `TRIAGE_PROTOCOL.md` for qualification procedures
- **Four Systems**: See `FOUR_SYSTEMS.md` for operational modes
- **Function Files**: See `OPERATIONAL/functions/` for implementations
- **ORACLE9 Context**: See `ORACLE9_CONTEXT_v2.md` for architectural decisions
