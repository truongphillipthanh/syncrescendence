<workflow_instructions>
  <context>
    This is an administrative archival task for general web content. The goal is to synthesize a complete webpage into two distinct Artifacts: a sanitized filename and a unified Markdown transcript with relevant metadata preservation.
  </context>
  
  <navigation_and_expansion>
    1. Scroll to ensure all content is loaded, including lazy-loaded sections and dynamic content.
    2. Identify the primary content area, excluding navigation menus, footers, sidebars, cookie notices, and advertisement blocks.
    3. For multi-page articles or documentation, capture only the current page unless explicitly instructed otherwise.
    4. Preserve structural hierarchy: main heading, subheadings, author/publication info if present, and publication date if displayed.
  </navigation_and_expansion>
  
  <media_ocr_protocol>
    For every image, diagram, or visual element in the primary content:
    1. Perform deep visual-to-text transcription.
    2. If the image contains text (charts, screenshots, diagrams, code), transcribe it verbatim.
    3. Preserve alt text and captions if present.
    4. Insert using format: (Image: [Screenplay-style description]. Alt text: [if present]. Caption: [if present]. Embedded text: [verbatim transcription]).
    5. Code snippets in images should be wrapped in appropriate Markdown code blocks with language identifiers.
  </media_ocr_protocol>
  
  <embedded_content_handling>
    For embedded content (videos, tweets, iframes, widgets, interactive elements):
    1. Note the content type and source.
    2. Transcribe visible text or provide descriptive summary of functionality.
    3. Format as: (Embedded [type]: [description/transcription]. Source: [URL/platform if visible]).
    4. For video content, note title, duration if visible, and any visible transcript or description.
  </embedded_content_handling>
  
  <output_requirements>
    <artifact_1_filename>
      Generate a single-line artifact containing ONLY the filename string.
      Template: {yyyymmdd}-website-{first_six_words_of_title_or_h1}-{domain_name}
      Constraints: All lowercase, no file extension, replace spaces/special characters with underscores, use em-dash for clarity, extract domain without TLD for brevity.
    </artifact_1_filename>
    
    <artifact_2_transcript>
      Generate a GitHub-flavored Markdown artifact of the complete page content.
      
      Include YAML frontmatter:
      - url: [full URL]
      - title: [page title or main H1]
      - domain: [root domain]
      - author: [if identifiable, otherwise omit]
      - published_date: [if displayed, otherwise omit]
      - modified_date: [if displayed, otherwise omit]
      - captured_date: [current date]
      - content_type: [article/documentation/blog/landing/other]
      
      Preserve semantic formatting:
      - Maintain heading hierarchy (H1-H6)
      - Blockquotes and pull quotes
      - Bold, italic, inline code, strikethrough, and links
      - Tables with proper alignment
      - Ordered and unordered lists with proper nesting
      - Code blocks with language identifiers
      - Horizontal rules for section breaks
      
      Content organization:
      - Begin with the primary heading as H1
      - Preserve original heading levels relative to structure
      - Maintain logical reading order even if visual layout differs
      - Include image descriptions inline at point of appearance
      - Note footnotes or references at point of citation with full text at document end if applicable
    </artifact_2_transcript>
  </output_requirements>
  
  <completion_step>
    Render both artifacts immediately. Do not ask for confirmation or provide conversational filler.
  </completion_step>
</workflow_instructions>