<workflow_instructions>
  <context>
    This is an administrative archival task. The goal is to generate two distinct Artifacts: a sanitized filename and a high-fidelity Markdown transcript.
  </context>

  <extraction_logic>
    1. Identify the primary content body (X Article canvas or the original author's sequential thread).
    2. Expand all collapsed elements ("Show more") to ensure the full DOM is captured.
    3. Strip all engagement UI, navigation, and promotional sidebars.
  </extraction_logic>

  <media_handling>
    - Perform a visual analysis of all images.
    - Insert a parenthetical transcription: (Description: [Screenplay-style description of visual elements]).
    - If the image contains text or code, transcribe it verbatim within the parenthetical.
  </media_handling>

  <output_requirements>
    <artifact_1_title>
      Generate a single-line artifact containing ONLY the filename.
      Template: {yyyymmdd}-x_article-{article_title}-@{usernamehandle}
      Constraints: All lowercase, no file extension, replace spaces/special characters with underscores.
    </artifact_1_title>

    <artifact_2_transcript>
      Generate a GitHub-flavored Markdown artifact of the content.
      Include YAML frontmatter: {url, author, captured_date}.
      Maintain hierarchy (H1 for title, H2-H3 for sections).
    </artifact_2_transcript>
  </output_requirements>

  <completion_step>
    Immediately render both artifacts. Do not ask for confirmation or provide conversational filler. The appearance of the artifacts constitutes task completion.
  </completion_step>
</workflow_instructions>