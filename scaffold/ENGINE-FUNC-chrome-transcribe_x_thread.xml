<workflow_instructions>
  <context>
    This is an administrative archival task for high-density X threads. The goal is to synthesize multiple sequential posts into two distinct Artifacts: a sanitized filename and a unified Markdown transcript.
  </context>

  <login_and_access_check>
    CRITICAL PREREQUISITE: You must be viewing this thread while LOGGED IN to X.
    If you can only see the initial post and a login wall, STOP and inform the user:
    "This thread requires logged-in access to capture the full trailing thread. Please log in to X first."
    Do NOT transcribe a partial thread — a single initial post without the author's continuation is INCOMPLETE and useless.
  </login_and_access_check>

  <navigation_and_expansion>
    1. Identify ALL sequential posts by the original author within the current thread.
    2. Programmatically trigger "Show more" or "Read more" to ensure the entire thread is rendered in the DOM.
    3. Scroll down through the ENTIRE thread to load all of the original author's continuation posts.
    4. Ignore all third-party replies, advertisements, and engagement metrics.
    5. If the thread has numbered posts (e.g., "1/", "2/", "3/"), ensure ALL numbered posts are captured in sequence.
    6. Count the total posts captured and note it in the frontmatter as post_count.
  </navigation_and_expansion>

  <date_extraction_protocol>
    CRITICAL: The filename date must reflect when the thread was ORIGINALLY POSTED, NOT today's date.
    1. Look for the timestamp on the FIRST post in the thread (e.g., "Feb 14, 2026", "11:32 AM · Feb 14, 2026").
    2. If the date is relative (e.g., "3d"), calculate the absolute date from today (2026-02-21).
    3. If no date is visible, check the URL for date fragments or use "undated".
    4. The captured_date field records today's date (when the transcription was made).
  </date_extraction_protocol>

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
      IMPORTANT: {yyyymmdd} = the thread's ORIGINAL POST DATE, not today.
      Constraints: All lowercase, no file extension, replace spaces/special characters with underscores.
    </artifact_1_filename>

    <artifact_2_transcript>
      Generate a GitHub-flavored Markdown artifact of the unified thread.

      Include YAML frontmatter:
      - url: [URL of the first post in thread]
      - author: [display name]
      - handle: [@username]
      - published_date: [ORIGINAL post date — when the author posted it]
      - captured_date: [today's date — when this transcription was made]
      - post_count: [total number of posts by the original author captured]

      Preserve the original author's formatting (bold, italics, lists).
      Use "---" separators between individual posts in the thread.
      Number each post if the author used numbering (1/, 2/, etc.).
    </artifact_2_transcript>
  </output_requirements>

  <completion_step>
    Render both artifacts immediately. Do not ask for confirmation or provide conversational filler.
  </completion_step>
</workflow_instructions>