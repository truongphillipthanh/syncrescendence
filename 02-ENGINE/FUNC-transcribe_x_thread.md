<workflow_instructions>
  <context>
    This is an administrative archival task for high-density X threads. The goal is to synthesize multiple sequential posts into two distinct Artifacts: a sanitized filename and a unified Markdown transcript.
  </context>

  <navigation_and_expansion>
    1. Identify all sequential posts by the original author within the current thread.
    2. Programmatically trigger "Show more" or "Read more" to ensure the entire thread is rendered in the DOM.
    3. Ignore all third-party replies, advertisements, and engagement metrics.
  </navigation_and_expansion>

  <media_ocr_protocol>
    For every image in the sequence:
    1. Perform a deep visual-to-text transcription.
    2. If the image contains text (code, lists, quotes), transcribe it verbatim.
    3. Insert the result into the flow of the transcript using the format: (Description: [Screenplay-style transcription of visual content and embedded text]).
    4. Ensure any code snippets found in images are wrapped in appropriate Markdown code blocks.
  </media_ocr_protocol>

  <output_requirements>
    <artifact_1_filename>
      Generate a single-line artifact containing ONLY the filename string.
      Template: {yyyymmdd}-x_thread-{first_six_words}-@{usernamehandle}
      Constraints: All lowercase, no file extension, replace spaces/special characters with underscores.
    </artifact_1_filename>

    <artifact_2_transcript>
      Generate a GitHub-flavored Markdown artifact of the unified thread.
      Include YAML frontmatter: {url, author, captured_date}.
      Preserve the original author's formatting (bold, italics, lists).
    </artifact_2_transcript>
  </output_requirements>

  <completion_step>
    Render both artifacts immediately. Do not ask for confirmation or provide conversational filler.
  </completion_step>
</workflow_instructions>