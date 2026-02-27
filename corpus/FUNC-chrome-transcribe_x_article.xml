<workflow_instructions>
  <context>
    This is an administrative archival task for X (Twitter) long-form articles. The goal is to generate two distinct Artifacts: a sanitized filename and a high-fidelity Markdown transcript.
  </context>

  <extraction_logic>
    1. Identify the primary content body (X Article canvas or the original author's sequential thread).
    2. Expand all collapsed elements ("Show more") to ensure the full DOM is captured.
    3. Strip all engagement UI, navigation, and promotional sidebars.
  </extraction_logic>

  <date_extraction_protocol>
    CRITICAL: The filename date must reflect when the article was ORIGINALLY POSTED, NOT today's date.
    1. Look for the post timestamp (e.g., "Feb 14, 2026", "11:32 AM · Feb 14, 2026").
    2. If the date is relative (e.g., "3d"), calculate the absolute date from today (2026-02-21).
    3. If no date is visible, check the URL for date fragments or use "undated".
    4. The captured_date field records today's date (when the transcription was made).
  </date_extraction_protocol>

  <media_handling>
    - Perform a visual analysis of all images.
    - Insert a parenthetical transcription: (Description: [Screenplay-style description of visual elements]).
    - If the image contains text or code, transcribe it verbatim within the parenthetical.
  </media_handling>

  <output_requirements>
    <artifact_1_title>
      Generate a single-line artifact containing ONLY the filename.
      Template: {yyyymmdd}-x_article-{article_title}-@{usernamehandle}
      IMPORTANT: {yyyymmdd} = the article's ORIGINAL POST DATE, not today.
      Constraints: All lowercase, no file extension, replace spaces/special characters with underscores.
    </artifact_1_title>

    <artifact_2_transcript>
      Generate a GitHub-flavored Markdown artifact of the content.

      Include YAML frontmatter:
      - url: [post/article URL]
      - author: [display name]
      - handle: [@username]
      - published_date: [ORIGINAL post date — when the author published it]
      - captured_date: [today's date — when this transcription was made]

      Maintain hierarchy (H1 for title, H2-H3 for sections).
    </artifact_2_transcript>
  </output_requirements>

  <completion_step>
    Immediately render both artifacts. Do not ask for confirmation or provide conversational filler. The appearance of the artifacts constitutes task completion.
  </completion_step>
</workflow_instructions>