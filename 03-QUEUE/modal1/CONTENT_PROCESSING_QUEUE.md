# CONTENT PROCESSING QUEUE

**Document Type**: QUEUE (General Content Processing)
**Last Updated**: 2025-12-29
**Purpose**: Track non-YouTube content awaiting integration (literature, podcasts, research papers)

---

## LITERATURE BACKLOG

Books, papers, articles pending reading and synthesis.

### Priority Queue
_None currently. Add items as identified._

**Template**:
```markdown
- [ ] **Title** by Author (Source, Date Added)
  - Type: Book | Paper | Article
  - Topic: [Primary subject]
  - Strategic Value: [Why this matters]
  - Processing Function: digest | integrate | primer
  - Target Tier: OPERATIONAL | REFERENCE | CANON candidate
```

---

## TRANSCRIPT BACKLOG

Podcasts, interviews, recorded conversations pending transcription and synthesis.

### Priority Queue
_None currently. Add items as identified._

**Template**:
```markdown
- [ ] **Episode Title** - Show Name (Date Added)
  - Guest(s): [Names]
  - Topic: [Primary subject]
  - Processing Function: transcribe_interview | digest
  - Strategic Value: [Why this matters]
  - Target Tier: OPERATIONAL | REFERENCE
```

---

## INTEGRATION BACKLOG

Processed items awaiting synthesis into existing documents.

### Pending Integration
_None currently. Items move here after processing but before tier assignment._

**Template**:
```markdown
- [ ] **Content Title** (Processed: YYYY-MM-DD)
  - Source: [Original source]
  - Function Applied: [transcribe_youtube | digest | integrate]
  - Key Insights: [1-3 bullet points]
  - Target Document: [OPERATIONAL doc to update or REFERENCE location]
  - Integration Status: Awaiting human review
```

---

## PROCESSING PROTOCOL

Same 6-step protocol as YOUTUBE_PROCESSING_BACKLOG:
1. **Monitor**: Track incoming content (bookmarks, recommendations, research alerts)
2. **Qualify**: Signal vs noise assessment
3. **Process**: Apply appropriate function (digest, transcribe_interview, integrate)
4. **Synthesize**: Extract key insights, frameworks, methodologies
5. **Route**: OPERATIONAL (living knowledge) or REFERENCE (stable archive)
6. **Archive**: Mark as processed with integration notes

---

## AUTOMATION POTENTIAL

- **Literature**: Pocket/Instapaper integration via MCP → Auto-qualify → Route to appropriate function
- **Transcripts**: Upload audio → Apply `transcribe_interview` → Synthesize → Route
- **Integration**: Agent monitors backlog → Proposes OPERATIONAL document updates → Human approves

---

**END CONTENT PROCESSING QUEUE**
