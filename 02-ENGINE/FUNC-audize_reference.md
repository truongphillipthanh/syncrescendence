AUDIZE COMPREHENSIVE REFERENCE v3.0

This document extends AUDIZE-PRODUCTION with detailed examples, edge case handlers, anti-patterns, and domain-specific guidance. Consult when the production instruction encounters unusual content.

SECTION ONE: FIDELITY EXAMPLES

Structural Linearization

Example: Headers with hierarchy.
Input: Level one header Mission Brief. Level two header Phase One Assessment. Level three header Initial Diagnostics.
Output: SECTION: MISSION BRIEF. SUBSECTION: PHASE ONE, ASSESSMENT. SUB-SUBSECTION: INITIAL DIAGNOSTICS.

Example: List quantification.
Input: To deploy the app, bullet run the build script, bullet check the logs, bullet restart nginx, bullet verify endpoints.
Output: To deploy the app, there are four steps. First, run the build script. Second, check the logs. Third, restart the Engine-Ex server. Fourth, verify endpoints.

Example: Table linearization with insight extraction.
Input: Table showing Apple with 5 units and 45 percent share, Samsung with 4 units and 36 percent share, Other with 2 units and 19 percent share.
Output: The market data shows Apple leading with five units and 45 percent market share, followed by Samsung with four units at 36 percent. Other vendors collectively hold two units, representing 19 percent of the market.

Example: File tree translation.
Input: Source directory containing components folder with Header and Footer jsx files, and utils folder with helpers javascript file.
Output: The source directory contains two subdirectories. First, the components folder, which holds Header and Footer jsx files. Second, the utils folder, containing a helpers javascript file.

Semantic Fidelity

Example: The Bonfire Rule for metaphor preservation.
Input: This is not an indiscriminate cleanup. It is a governed defrag, not an enthusiastic bonfire.
Correct output: This is not an indiscriminate cleanup. It is a governed defragmentation, not an enthusiastic bonfire.
Wrong output: This is a controlled cleanup process, not aggressive deletion.
Reason: Sterilizing bonfire imagery loses voice and instructional weight.

Example: Hard constraint preservation.
Input: Never proceed unless a specific file named APPLY_DEFRAG_APPROVAL.txt exists.
Output: Crucially, never proceed unless a specific file exists, named: A-P-P-L-Y underscore D-E-F-R-A-G underscore A-P-P-R-O-V-A-L dot T-X-T.

Example: Modality preservation.
Input: The system may attempt recovery, but this cannot be guaranteed.
Correct output: The system may attempt recovery, but this cannot be guaranteed.
Wrong output: The system will try to recover, but success is not certain.
Reason: Changing may to will alters commitment level.

Prosodic Mapping

Example: Instructional code spelling.
Input: Run the command chmod plus-x setup.sh.
Output: Run the following command. Type: c-h-m-o-d space plus-x space setup dot s-h.

Example: Contextual code summarization.
Input: Python code that loops through items, checks if each item is valid, and processes valid items.
Output: The code loops through each item in the collection. For each item, it checks whether the item is valid. If so, it processes that item.

Example: Compound sentence breaking.
Input: The server, which was already under load, finally crashed, causing a cascade failure across multiple systems, which then triggered alerts.
Output: The server was already under load. It finally crashed. This caused a cascade failure across multiple systems. The failures then triggered alerts.

SECTION TWO: ANTI-PATTERNS

Format Leakage

Bad: The next section is hash hash hash Phase One Initiation.
Correct: SECTION: PHASE ONE. INITIATION.

Bad: The critical point is asterisk asterisk never asterisk asterisk delete files.
Correct: The critical point is this: never delete files.

Bad: Run backtick npm install backtick to begin.
Correct: Run the command: n-p-m space install.

Semantic Sterilization

Bad: This requires careful cleanup of the directory.
Correct: This is not an indiscriminate cleanup. It is a governed defrag, not an enthusiastic bonfire.
Reason: When source uses bonfire, preserve it.

Bad: The system should verify integrity before processing.
Correct: The system must verify integrity before processing.
Reason: Preserve must versus should distinction.

Chatty Wrappers

Bad: Here is the converted script followed by content.
Correct: Begin immediately with content.

Bad: I have processed your document. The output is as follows.
Correct: Begin immediately with content.

Bad: Let me know if you need any changes.
Correct: End with content, no postscript.

Structural Flattening

Bad: First, Item A, Second, Item B, Third, Item C.
Correct: There are three items. First, Item A. Second, Item B. Third, Item C.
Reason: Missing cognitive priming.

Missing Forecasting

Bad: First, configure the API. Second, test endpoints. Third, deploy.
Correct: There are three deployment steps. First, configure the A-P-I. Second, test endpoints. Third, deploy.

Acronym Inconsistency

Bad: The API connects to AWS using HTTP protocol.
Correct: The A-P-I connects to A-W-S using H-T-T-P protocol.
Reason: Consistent hyphenation for initialisms.

Numerical Precision Loss

Bad: Latency improved significantly.
Correct: Latency dropped nearly thirtyfold, from 340 to 12 milliseconds.
Reason: Preserves magnitude relationship.

Coverage Gaps

Bad: Skipping complex diagram without comment.
Correct: NOTE: A complex diagram appears here. Summary: the process begins with validation, proceeds through analysis, invalid inputs trigger rollback.

SECTION THREE: EDGE CASE HANDLERS

Homographs and Context-Dependent Pronunciation

Problem: TTS engines fail on words with multiple pronunciations.
Solution: Add one clarifying word.
Read as past tense: read aloud or context clarifies.
Read as present tense: will read or reading now.
Live as verb: live there or living.
Live as adjective: live broadcast or live performance.
Tear as crying: tear drop.
Tear as ripping: tear the paper.

Mixed Content Blocks

Problem: Code blocks containing both commands and comments.
Input: Comment saying install dependencies, command npm install, comment saying run tests, command npm test.
Output: Two-pass approach. First, install dependencies by typing: n-p-m space install. Then run tests by typing: n-p-m space test.
Method: Comments become context, commands become instructions.

URLs in Running Text

Problem: Full URLs break flow.
Input: Visit https://docs.example.com/api/v2/reference for details.
Output: Visit the A-P-I reference documentation at docs dot example dot com for details. A link is provided.
Method: Domain plus purpose, no full URL.

Inline Code in Prose

Problem: Variable references in sentences.
First mention: the variable named user ID.
Repeated mentions: user ID without ceremony.
Unclear context: the user I-D variable.

Emoji and Special Characters

Warning symbols become: Warning or Caution.
Checkmarks become: correct or yes.
X marks become: incorrect or no.
Fire emoji becomes: important or hot topic, if semantically meaningful.
Light bulb becomes: key insight or tip.
Decorative emoji: omit unless semantically meaningful.

Markdown Links with Meaningful Text

Input: See the configuration guide link for setup.
Output: See the configuration guide for setup. A link is provided.
Method: Keep link text, drop URL.

Input: Click here link to download.
Output: A download link is provided.
Method: When link text is meaningless, describe destination.

Nested Lists with Mixed Hierarchy

Input: Level one item A with level two items A1 and A2, then level one item B.
Output: There are two primary items. First, Level one item A. Within that, there are two sub-points: Level two item A-one, and Level two item A-two. Second, Level one item B.

Long Numbers

Problem: Reading 1234567890 is cognitively brutal.
Solution: Chunk in groups. One-two-three-four, five-six-seven-eight, nine-zero.
Alternative: ID ending in seven-eight-nine-zero, if context allows.
Timestamps: Fourteen thirty-two UTC, not one-four colon three-two.

Code Comments That Are Actually Instructions

Input: Python code with TODO comment about fixing race condition, placeholder function.
Output: The code includes a note: there is a TODO item to fix the race condition in the database handler. The process function is currently a placeholder.

Keyboard Shortcuts

Input: Press Ctrl plus Shift plus P to open command palette.
Output: Press Control-Shift-P to open the command palette.
Method: Spell out modifier keys, hyphenate combination.

Regex Patterns

Input: Pattern /^[A-Z]{2}\d{4}$/
Contextual output: The pattern matches two uppercase letters followed by four digits.
Instructional output: Spell character by character when user must type exactly.
Preference: Contextual unless user must type it.

Version Ranges

Input: Requires Node 14.x through 16.x.
Output: Requires Node version fourteen through sixteen.

Input: Python greater than or equal to 3.8, less than 4.0.
Output: Python version three point eight or higher, but below version four.

File Paths with Variables

Input: Home tilde Documents project name folder config yml.
Output: In your home directory, under Documents, in the project name folder, the config Y-M-L file.
Method: Expand tilde and variables naturally unless literal typing required.

Mathematical Expressions

Input: x squared plus 2x plus 1 equals 0.
Instructional: x squared plus two-x plus one equals zero.
Contextual: The equation is a quadratic in standard form.

Strikethrough Text

Input: Strikethrough Old approach, then New approach.
Output: The old approach is replaced by the new approach.
Method: Strikethrough implies replacement, state it explicitly.

Footnotes

Input: The study citation one found significant results. Footnote: Published in Nature, 2024.
Output: The study, published in Nature in 2024, found significant results.
Method: Integrate footnote into prose as aside.

Dense JSON Structures

Problem: Reading entire structure is noise.
Output: NOTE: A complex JSON structure follows containing user data. Key fields include: user ID, authentication token, preferences object with theme and language settings, and a nested permissions array. The structure spans 47 lines.
Follow-up if specific values matter: The theme is set to dark mode, and language is English.

Single-Letter Variables

Input: The variable i tracks iteration count.
Output: The variable named 'i' tracks iteration count.
Method: Quote the single letter to avoid confusion with eye.

Currency and Units

Input: $1,234.56
Output: One thousand, two hundred thirty-four dollars and fifty-six cents.
Alternative if precision less critical: approximately twelve hundred dollars.

Input: 5ms, 120GB, 3.2kg.
Output: Five milliseconds, one hundred twenty gigabytes, three point two kilograms.

Time Zones

Input: 2:30 PM EST.
Output: Two-thirty P-M Eastern Standard Time.

SECTION FOUR: PRONUNCIATION GLOSSARY

Pronounceable Acronyms

SaaS becomes Sass. SQL becomes Sequel. GUI becomes Gooey. YAML becomes Yam-el. JSON becomes Jay-sawn. AJAX becomes A-jacks. CRUD becomes Crud. WYSIWYG becomes Wizzy-wig. ASCII becomes As-key. BIOS becomes By-oss.

Initialisms to Hyphenate

API becomes A-P-I. AWS becomes A-W-S. PDF becomes P-D-F. HTTP becomes H-T-T-P. CSS becomes C-S-S. DNS becomes D-N-S. VPN becomes V-P-N. RAM becomes R-A-M. CPU becomes C-P-U. GPU becomes G-P-U. URL becomes U-R-L.

Mathematical and Logical Symbols

Plus sign becomes plus. Minus sign becomes minus. Asterisk becomes times or asterisk depending on context. Forward slash becomes divided by or slash. Equals sign becomes equals. Not equals becomes does not equal. Double equals becomes equals in code. Triple equals becomes strictly equals. Less than symbol becomes less than. Greater than symbol becomes greater than. Less than or equal becomes less than or equal to. Greater than or equal becomes greater than or equal to. Double ampersand becomes and also. Double pipe becomes or alternatively. Exclamation point becomes not. Arrow right becomes maps to or returns. Dash arrow becomes leads to or flows into.

File Path Elements

Forward slash. Backslash. Tilde. Dot. Underscore. Dash. Colon.

Programming Constructs

Curly braces become: the code block containing. Square brackets become: the array containing. Parentheses become: with parameters, or the group. Semicolon becomes: end statement. Comma becomes: comma, or followed by.

File Extensions

Dot md becomes markdown file. Dot py becomes Python file. Dot js becomes JavaScript file. Dot jsx becomes J-S-X file or React file. Dot txt becomes text file. Dot pdf becomes P-D-F file. Dot doc or docx becomes Word document.

SECTION FIVE: GENRE CALIBRATION

Apply silently without announcement. Never say: This appears to be technical documentation.

Technical Documentation

Recognition: API docs, specifications, reference manuals.
Priority order: Accuracy, then clarity, then brevity.
Emphasis: Preserve all technical terms verbatim. Spell out identifiers literally when instructional. Maintain precise version numbers. Keep conditional logic exact. Preserve all warnings.

Instructional Content

Recognition: Tutorials, guides, step-by-step procedures.
Priority order: Clarity, then accuracy, then brevity.
Emphasis: Strong list quantification. Clear transitions between stages. Explicit completion criteria. Warnings before critical steps.

Analytical Content

Recognition: Reports, analyses, whitepapers.
Priority order: Insight, then accuracy, then brevity.
Emphasis: Preserve thesis statements exactly. Maintain logical argument flow. Keep numerical evidence. Preserve hedging language.

Strategic Content

Recognition: Business plans, strategy docs, proposals.
Priority order: Clarity, then insight, then accuracy.
Emphasis: Preserve commitment levels. Maintain priority orderings. Keep success criteria exact.

Narrative Content

Recognition: Blog posts, essays, informal writing.
Priority order: Voice, then flow, then accuracy.
Emphasis: Maximum metaphor preservation. Maintain author's register. Preserve rhetorical devices. Keep sentence rhythm.

SECTION SIX: SELF-AUDIT CHECKLIST

Format Purity

Zero Markdown syntax including hashes, asterisks, underscores, backticks, greater-than signs, pipes, triple dashes.
Zero code fences.
Zero raw URLs, replaced with domain plus link provided note.
Zero visual glyphs including tree characters, box drawing, arrows.
Zero table pipes.

Wrapper Elimination

No preamble such as Here is or I have converted.
No genre announcements such as This appears to be or This document reads as.
No postscript such as Let me know or Hope this helps.
Script begins immediately with content.
Script ends immediately after content.

Hard Constraint Preservation

All do-not instructions intact with original modality.
All file names spelled out if instructional.
All commands spelled character by character if user must type.
All numeric thresholds preserved exactly.
All if-then conditions maintained.

Modality Integrity

Must still must, not softened to should.
Cannot still cannot, not becomes might not.
May still may, not upgraded to will.
All hedges preserved including approximately, likely, suggests.

Metaphor and Voice Fidelity

No sterilization of imagery.
Author's register maintained.
Domain terminology kept intact.
Rhetorical questions preserved.
Emotional tenor matches source.

Cognitive Priming

Lists announced with count before enumeration.
Hierarchy signposted before descending.
Complex sections warned before presenting.
Transitions marked between major shifts.

Prosodic Quality

Sentences under eighteen words.
Compound sentences broken into simpler units.
No run-on sentences.
Pauses indicated through punctuation.

Acronym Consistency

Pronounceable acronyms rendered phonetically.
Initialisms hyphenated.
No inconsistency within same script.

Coverage Completeness

No silently deleted content.
Complex visuals flagged with NOTE and summarized.
All omissions explicitly marked.
All summaries capture essential constraints.

No Invention

No claims added beyond source.
No metaphors introduced.
No recommendations unless in source.
Connective tissue minimal and neutral.

Final Scan Pattern

Read output start to finish looking for any formatting.
Scan for any Here is or I have phrases.
Check first hard constraint in source, verify in output.
Check most colorful metaphor in source, verify in output.
Check longest list in source, verify count announced.
Check any code block, verify appropriate handling.

If any item fails: rewrite and re-audit before emitting.
