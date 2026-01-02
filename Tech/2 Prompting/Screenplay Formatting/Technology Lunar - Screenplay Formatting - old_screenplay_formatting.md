Screenplay Formatting Requirements for Portal Prompts

A style guide for human-facing orchestration scripts

⸻

Purpose

This format is designed for full-portal prompts — cinematic, human-readable orchestration scripts where the operator (“YOU”) is the active human-in-the-loop delivering prompts to multiple LLMs or tools in a coordinated sequence.

Where XML or JSON structures are designed for the LLM’s machine parsing, this is designed for the human (YOU) to:
	•	See the workflow at a glance.
	•	Understand the narrative flow of multi-stage orchestration.
	•	Reduce cognitive load by chunking information into cinematic “beats.”
	•	Preserve readability and reusability across projects.
	
⸻

Core Structure

Each stage in the orchestration is expressed as a scene. A scene contains two identifying headers, followed by character and dialogue blocks, deliverables, action lines, and a transition.

1. SCENE TITLE
	•	Format:
	
SCENE <stage-number> — <descriptive stage name>


	•	Example:
SCENE 4 — ECOSYSTEMAL SYMBIOTICS
	•	Always ALL CAPS.
	•	Purpose: Signals the stage index and its role in the workflow.
	
⸻

2. SCENE HEADING
	•	Format:
	
<RunID>. <PLATFORM (+ MODE)> – <TOOL STATUS>


	•	RunID: Unique identifier for the production run.
	•	PLATFORM: Platform name in ALL CAPS (CHATGPT, CLAUDE, GEMINI, GROK).
	•	MODE: Optional model-tier descriptor in parentheses (STANDARD, EXTENDED THINKING, DEEP RESEARCH, etc.).
	•	TOOL STATUS: “NO TOOL” or “TOOL ENABLED.”
	•	Purpose: This is the screenplay equivalent of EXT/INT + location — it orients you instantly to where this scene “takes place.”
	
⸻

3. CHARACTER LINE
	•	Always:
	
YOU


	•	If this is an initialization scene that embeds the global context (Rolling Canon), append (INIT) immediately after YOU.
	•	Below the character line, on its own line, add a parenthetical:
	
(to PLATFORM)

	•	to is lowercase; PLATFORM is uppercase.
	
	•	Rationale: The character is always the operator, because you are delivering the prompt. The parenthetical makes explicit which LLM or platform is being addressed in this scene.
	
⸻

4. DIALOGUE BLOCKS
	•	Contain the exact text to be sent to the platform.
	•	Enclosed in triple backticks (```) and double-indented.
	•	No quotation marks.
	•	For (INIT) scenes, the first dialogue block is the Rolling Canon (or equivalent global context).
	•	For non-init scenes, the dialogue block is the stage’s tasking instructions.
	
Example:

YOU (INIT) 
(to CLAUDE) 
  ``` 
  [Embed Rolling Canon here] 
  ``` 

YOU 
(to CLAUDE) 
  ``` 
  Excavate a taxonomy of primitives relevant to the project… 
  ```

	•	Rationale: The triple-backtick fencing cleanly separates prompt text from scene scaffolding, so the human eye and the platform both know exactly what is being sent.
	
⸻

5. DELIVERABLE SECTION
	•	Label exactly as:
	
DELIVERABLE

in ALL CAPS.

	•	Follow with a bulleted list of expected output artifacts.
	•	Each bullet contains the exact artifact filename or placeholder name.
	•	Rationale: This is a visual contract — you can scan deliverables without parsing the task instructions.
	
Example:

DELIVERABLE
- <runID>_stage<stage#>_<artifact-name>_version<rev>.<ext>
- <runID>_stage<stage#>_<artifact-name>_version<rev>.<ext>


⸻

6. ACTION LINES
	•	These are meta-instructions to the operator.
	•	They are not enclosed in backticks.
	•	First two words are in ALL CAPS, the remainder in standard sentence case.
	•	Indent flush with the scene heading.
	•	Example:
	
PRODUCE IN first ten lines the run identifier, stage, and next consumer.


	•	Rationale: ALL CAPS for the first two words creates a scannable imperative cue for operator action.
	
⸻

7. TRANSITION LINE
	•	Triple-indented, ALL CAPS:
	
   SWITCH TO <PLATFORM>


	•	PLATFORM is uppercase and matches the platform name in the next scene heading.
	•	Rationale: Creates a clear connective tissue between scenes, just like film transitions.
	
⸻

Stylistic Rules
	•	ALL CAPS for:
	•	Scene titles
	•	Scene headings
	•	Deliverable labels
	•	Transition lines
	•	First two words of each action line
	•	Parentheticals:
	•	Always on their own line under the character name.
	•	Lowercase to + uppercase platform.
	•	YOU:
	•	Always the character, because the operator is the one delivering prompts.
	•	Dialogue:
	•	Always in triple backticks, double-indented.
	•	Action Lines:
	•	ALL CAPS for first two words; rest in sentence case.
	•	Minimal visual noise:
	•	Avoid extraneous punctuation in headings.
	•	Keep whitespace consistent.
	
⸻

Workflow Implications
	•	The (INIT) scenes mark thread start points for each platform. They must embed the Rolling Canon so the platform has full context from the outset.
	•	Stage Packets (local context, artifacts) are provided only when switching between platforms or model tiers mid-run.
	•	This screenplay is human-facing. The LLM should only see the contents of the triple-backtick dialogue blocks, unless the entire screenplay is intentionally fed for meta-instruction purposes.
	
⸻

Why This Works
	•	For Humans: It reads like a production script — fast to scan, visually chunked, narrative in flow.
	•	For LLMs: The prompts themselves are clean, isolated, and unambiguous.
	•	For Multi-Stage Orchestration: The SCENE/SCENE HEADING/TRANSITION triad makes it obvious where you are, what you’re doing, and where you go next.