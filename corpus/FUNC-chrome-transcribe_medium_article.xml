<workflow_instructions>
  <context>
    This is an administrative archival task for Medium articles. The goal is to synthesize a complete article into two distinct Artifacts: a sanitized filename and a unified Markdown transcript with complete metadata preservation.
  </context>

  <navigation_and_expansion>
    1. Scroll to ensure the entire article is loaded in the DOM, including any lazy-loaded content.
    2. Capture the full article body, ignoring sidebar recommendations, comment sections, and engagement overlays.
    3. Preserve article structure: title, subtitle, author byline, publication name, reading time, publication date, and tags.
  </navigation_and_expansion>

  <date_extraction_protocol>
    CRITICAL: The filename date and frontmatter published_date must reflect when the article was ORIGINALLY PUBLISHED, NOT today's date.
    1. Look for the publication date displayed on the article (e.g., "Feb 14, 2026", "3 days ago").
    2. If the date is relative (e.g., "3 days ago"), calculate the absolute date from today (2026-02-21).
    3. If no publication date is visible, use "undated" in the filename and omit published_date from frontmatter.
    4. The captured_date field records today's date (when the transcription was made).
  </date_extraction_protocol>

  <media_ocr_protocol>
    For every image or embedded visual element:
    1. Perform deep visual-to-text transcription.
    2. If the image contains text (diagrams, screenshots, code, quotes), transcribe it verbatim.
    3. Preserve Medium's native image captions if present.
    4. Insert using format: (Image: [Screenplay-style description]. Caption: [if present]. Embedded text: [verbatim transcription]).
    5. Code snippets in images should be wrapped in appropriate Markdown code blocks with language identifiers.
  </media_ocr_protocol>

  <embedded_content_handling>
    For embedded content (tweets, GitHub gists, videos, iframes):
    1. Note the content type and source.
    2. Transcribe visible text or provide descriptive summary.
    3. Format as: (Embedded [type]: [description/transcription]. Source: [URL if visible]).
  </embedded_content_handling>

  <output_requirements>
    <artifact_1_filename>
      Generate a single-line artifact containing ONLY the filename string.
      Template: {yyyymmdd}-medium-{first_six_words_of_title}-{author_lastname}
      IMPORTANT: {yyyymmdd} = the article's ORIGINAL PUBLICATION DATE, not today.
      Constraints: All lowercase, no file extension, replace spaces/special characters with underscores, use em-dash for clarity.
    </artifact_1_filename>

    <artifact_2_transcript>
      Generate a GitHub-flavored Markdown artifact of the complete article.

      Include YAML frontmatter:
      - url: [article URL]
      - title: [full title]
      - author: [full name]
      - author_profile: [Medium profile URL]
      - publication: [if applicable, otherwise "Independent"]
      - published_date: [ORIGINAL publication date — when the author published it]
      - captured_date: [today's date — when this transcription was made]
      - reading_time: [if displayed]
      - tags: [array of article tags]

      Preserve Medium-specific formatting:
      - Pull quotes as blockquotes with visual distinction
      - Image captions in italics beneath images
      - Section dividers (Medium's triple-dot separators)
      - Bold, italic, inline code, and links
      - Ordered and unordered lists with proper nesting
      - Code blocks with language identifiers

      Maintain logical hierarchy:
      - H1: Article title
      - H2: Subtitle (if present)
      - H3+: Section headers as styled in original
    </artifact_2_transcript>
  </output_requirements>

  <completion_step>
    Render both artifacts immediately. Do not ask for confirmation or provide conversational filler.
  </completion_step>
</workflow_instructions>