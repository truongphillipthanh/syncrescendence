# DIRECTIVE-027: COMPREHENSIVE FORGE
## UNIFIED EXECUTION — Claude Code
**Issued**: 2025-12-31
**Authority**: Oracle7 under Sovereign direction
**Classification**: CRITICAL — Complete Repository Transformation
**Mode**: COMPREHENSIVE — Survey everything, fix everything, ONE PASS

---

## SOVEREIGN'S MANDATE

> "It is absolutely not enough for Claudes 2 and 3 to just execute, they must survey the entire repository rigorously, comprehensively, and meticulously."

> "You have to WITH EVERY DIRECTIVE HAVE THEM ENCODE WHAT WE GO OVER. ALWAYS."

> "We are executing extremely inefficiently... make sure we are getting lots more done."

> "This is not some simple nominal or tactical fix. REVIEW EVERY CONVERSATION."

---

## WHY PREVIOUS DIRECTIVES FAILED

1. **Narrow scope** — Each directive addressed one slice; no comprehensive cleanup
2. **No deletion verification** — Files "marked for deletion" were never actually deleted
3. **Rename without delete** — GENESIS→CANON created new files, didn't delete originals
4. **Append-only accumulation** — Old and new versions coexist
5. **Mechanical execution** — Claudes didn't survey; they executed blindly
6. **No context encoding** — Decisions weren't embedded; context lost

**THIS DIRECTIVE FIXES ALL OF THIS IN ONE PASS.**

---

## MANDATORY FIRST STEP: COMPREHENSIVE SURVEY

Before ANY execution, you MUST:

```bash
# 1. List EVERYTHING at repository root
ls -la

# 2. Count files by pattern
echo "=== DUPLICATES AND LEGACY ==="
ls | grep -E "^GENESIS-" | wc -l
ls | grep -E "^CANON-0000[1-9]" | wc -l  # Old cosmos numbering
ls | grep -E "^Technological_Lunar" | wc -l
ls | grep -E "^Technology_Lunar" | wc -l
ls | grep -E "^Al_" | wc -l  # Typos
ls | grep -E "___" | wc -l  # Triple underscore
ls | grep -E "^ALPHA_|^BETA_" | wc -l
ls | grep -E "^EXECUTION_LOG-" | wc -l
ls | grep -E "^DIRECTIVE-" | wc -l

# 3. Verify CANON structure
ls CANON/ | wc -l
ls CANON/ | head -20

# 4. Verify orchestration structure
ls orchestration/
ls orchestration/state/
ls orchestration/execution_logs/
ls orchestration/directives/

# 5. Verify QUEUE structure  
ls QUEUE/
ls QUEUE/modal1/ 2>/dev/null
ls QUEUE/modal2/ 2>/dev/null

# 6. Verify OPERATIONAL structure
ls OPERATIONAL/
ls OPERATIONAL/functions/ 2>/dev/null
ls OPERATIONAL/prompts/ 2>/dev/null
```

**Document findings BEFORE proceeding.**

---

## THE ORACLE DECISIONS (ENCODE THIS)

These decisions govern ALL actions. Every file disposition derives from these principles:

### From Oracle0-3: Foundational Architecture
- **Civilizational sensing infrastructure** — Not personal productivity tooling
- **Five-chain IIC architecture** — Acumen, Coherence, Efficacy, Mastery, Transcendence
- **Flat + symlink architecture** — All CANON at same level, aliases for navigation
- **Reception Calibration** — Calibrate models to understand Sovereign, not engineer personas

### From Oracle4: Metabolism Model
- **"Canonize or delete"** — No archive tier, no guilt-driven hoarding
- **Orchestration is protected** — Infrastructure, not content; maintained, not metabolized
- **Near-term temporal horizon** — Fluid documents expire; eternal documents persist

### From Oracle5-6: Structural Standards
- **GENESIS is cosmos tier** — Canonized as [[CANON-00001-ORIGIN-cosmos]] through 00004
- **Cosmos renumbered** — Syncrescendence is 00005, sequence continues to 00014
- **18 evaluative lenses** — Every decision evaluated against full framework
- **Aliases for Finder, not Obsidian** — Symlinks provide multiple views

### From Oracle7: Documentation Protocol
- **Maximum resolution** — Every decision documented with Sovereign's words
- **Verify before declare** — Examine actual files, not reports about files
- **Repository is Foyer** — All context accessible to any agent
- **Directives encode decisions** — Claudes need full rationale

---

## COMPLETE FILE MANIFEST

### CATEGORY A: DELETE IMMEDIATELY (Legacy/Duplicate)

These files are VESTIGES of old state. They were supposed to be deleted but weren't.

```bash
# A1: GENESIS files (canonized to CANON-00001-4, originals not deleted)
rm GENESIS-000-ORIGIN.md
rm GENESIS-001-LINEAGE.md
rm GENESIS-002-PRINCIPLES.md
rm GENESIS-003-EVOLUTION.md

# A2: Old cosmos numbering (renumbered, originals not deleted)
rm CANON-00001-SYNCRESCENDENCE-cosmos.md  # Now [[CANON-00005-SYNCRESCENDENCE-cosmos]]
rm CANON-00002-CORPUS-cosmos.md           # Now [[CANON-00006-CORPUS-cosmos]]
rm CANON-00003-EVALUATION-cosmos.md       # Now [[CANON-00007-EVALUATION-cosmos]]
rm CANON-00004-RESOLUTIONS-cosmos.md      # Now [[CANON-00008-RESOLUTIONS-cosmos]]
rm CANON-00005-STRATEGY-cosmos.md         # Now [[CANON-00009-STRATEGY-cosmos]]
rm CANON-00006-OPERATIONS-cosmos.md       # Now [[CANON-00010-OPERATIONS-cosmos]]
rm CANON-00007-ARTIFACT_PROTOCOL-cosmos.md # Now [[CANON-00011-ARTIFACT_PROTOCOL-cosmos]]
rm CANON-00008-MODAL_SEQUENCE-cosmos.md   # Now [[CANON-00012-MODAL_SEQUENCE-cosmos]]
rm CANON-00009-QUICKSTART-cosmos.md       # Now [[CANON-00013-QUICKSTART-cosmos]]
rm CANON-00010-CONTENT_PROTOCOL-cosmos.md # Now [[CANON-00014-CONTENT_PROTOCOL-cosmos]]

# A3: Legacy system prompt exports (extraction verified Oracle7)
rm "Technological_Lunar_-_System_PromptsChatGPT__OpenAI_Apple__Memories.txt"
rm "Technological_Lunar_-_System_PromptsChatGPT__OpenAI_Apple__System_Prompt_1_-_What_traits_should_ChatGPT_have_.txt"
rm "Technological_Lunar_-_System_PromptsChatGPT__OpenAI_Apple__System_Prompt_2_-_Anything_else_ChatGPT_should_know_about_you_.txt"
rm "Technological_Lunar_-_System_PromptsChatGPT__OpenAI_Google__Memories.txt"
rm "Technological_Lunar_-_System_PromptsChatGPT__OpenAI_Google__System_Prompt_1_-_What_traits_should_ChatGPT_have_.txt"
rm "Technological_Lunar_-_System_PromptsChatGPT__OpenAI_Google__System_Prompt_2_-_Anything_else_ChatGPT_should_know_about_you_.txt"
rm "Technological_Lunar_-_System_PromptsClaude__Anthropic_Apple__System_Prompt_-_What_personal_preferences_should_Claude_consider_in_responses_.txt"
rm "Technological_Lunar_-_System_PromptsClaude__Anthropic_Google__System_Prompt_-_What_personal_preferences_should_Claude_consider_in_responses_.txt"
rm "Technological_Lunar_-_System_PromptsGemini_Saved_Info_-_What_do_you_want_Gemini_to_remember__1.txt"
rm "Technological_Lunar_-_System_PromptsGemini_Saved_Info_-_What_do_you_want_Gemini_to_remember__2.txt"
rm "Technological_Lunar_-_System_PromptsGemini_Saved_Info_-_What_do_you_want_Gemini_to_remember__3.txt"
rm "Technological_Lunar_-_System_PromptsGemini_Saved_Info_-_What_do_you_want_Gemini_to_remember__4.txt"
rm "Technological_Lunar_-_System_PromptsGrok__xAI_Apple__System_Prompt_-_Custom_Instructions.txt"
rm "Technological_Lunar_-_System_PromptsGrok__xAI_Google__System_Prompt_-_Custom_Instructions.txt"

# A4: Tech Lunar files (canonized or marked for deletion per Oracle7)
rm "Technology_Lunar_-_3_Research_Protocols.md"      # Canonized to [[CANON-30330-RESEARCH_PROTOCOLS-asteroid-TECH_STACK-comet-INTELLIGENCE]]
rm "Technology_Lunar_-_4_Implementation_Guide.md"    # Canonized to [[CANON-30340-IMPLEMENTATION_PATTERNS-asteroid-TECH_STACK-comet-INTELLIGENCE]]
rm "Technology_Lunar_-_FrontierModels.md"            # Fails 15/18 lenses, temporal
rm "Technology_Lunar_-_Agentic_ScreenplayFormatting.md"           # Queued to QUEUE-36200
rm "Technology_Lunar_-_Screenplay_Formatting_-_agentic_screenplay_format.md"
rm "Technology_Lunar_-_Screenplay_Formatting_-_culmination.md"
rm "Technology_Lunar_-_Screenplay_Formatting_-_screenplay_manual.md"
rm "Technology_Lunar_-_Screenplay_Formatting_-_validation.md"

# A5: Typo files (correct versions exist)
rm "Al_Academic_Research.md"              # Correct: AI_Academic_Research.md
rm "Al_Image_Generators.md"               # Correct: AI_Image_Generators.md
rm "AI_3D___VFX.md"                       # Correct: AI_3D_VFX.md
rm "The_Next_Wave_in_Al_Video_and_VFX.md" # Correct: The_Next_Wave_in_AI_Video_and_VFX.md

# A6: Consumed prep files (work completed)
rm CANONIZATION_PREP_Implementation_Guide.md
rm CANONIZATION_PREP_Research_Protocols.md
rm QUEUE_PREP_Screenplay_Formatting.md
rm DELETION_MANIFEST.md
rm SYSTEM_PROMPT_EXTRACTION_VERIFICATION.md
rm TECH_LUNAR_CANONIZATION_PLAN.md
```

**TOTAL CATEGORY A: ~45 files to DELETE**

---

### CATEGORY B: MOVE TO PROPER LOCATION

These files exist at root but belong in subdirectories.

```bash
# B1: Execution logs → orchestration/execution_logs/
mv EXECUTION_LOG-2025-12-30-019.md orchestration/execution_logs/
mv EXECUTION_LOG-2025-12-30-020A.md orchestration/execution_logs/
mv EXECUTION_LOG-2025-12-30-020B.md orchestration/execution_logs/
mv EXECUTION_LOG-2025-12-30-021.md orchestration/execution_logs/
mv EXECUTION_LOG-2025-12-30-022A.md orchestration/execution_logs/
mv EXECUTION_LOG-2025-12-30-022C.md orchestration/execution_logs/
mv EXECUTION_LOG-2025-12-31-024A.md orchestration/execution_logs/
mv EXECUTION_LOG-2025-12-31-024B.md orchestration/execution_logs/
mv EXECUTION_LOG-2025-12-31-024C.md orchestration/execution_logs/
mv EXECUTION_LOG-2025-12-31-024D.md orchestration/execution_logs/
mv EXECUTION_LOG-2025-12-31-024E.md orchestration/execution_logs/
mv EXECUTION_LOG-2025-12-31-025A.md orchestration/execution_logs/
mv EXECUTION_LOG-2025-12-31-025B.md orchestration/execution_logs/
mv EXECUTION_LOG-2025-12-31-026A.md orchestration/execution_logs/
mv EXECUTION_LOG-2025-12-31-026B.md orchestration/execution_logs/
mv DEFRAG_EXECUTION_LOG.md orchestration/execution_logs/

# B2: Directives → orchestration/directives/
mv DIRECTIVE-017_HOLISTIC_RECONCEPTION.md orchestration/directives/
mv DIRECTIVE-018_EXECUTION_COMPLETION.md orchestration/directives/
mv DIRECTIVE-019_ORCHESTRATION_RESTORATION.md orchestration/directives/
mv DIRECTIVE-020A_PHASE2_ALPHA.md orchestration/directives/
mv DIRECTIVE-020B_PHASE2_BETA.md orchestration/directives/
mv DIRECTIVE-021_PHASE3_RECONNAISSANCE.md orchestration/directives/
mv DIRECTIVE-022A_NUMBERING_UPDATE.md orchestration/directives/
mv DIRECTIVE-022B-EXECUTION.md orchestration/directives/

# B3: Scaffolding → orchestration/scaffolding/
mv ALPHA_ARCHAEOLOGY_REPORT.md orchestration/scaffolding/
mv ALPHA_OPERATIONAL_COHERENCE.md orchestration/scaffolding/
mv ALPHA_REPOSITORY_AUDIT.md orchestration/scaffolding/
mv ALPHA_SYNTHESIS.md orchestration/scaffolding/
mv ALPHA_TENSION_MAP.md orchestration/scaffolding/
mv BETA_METADATA_SCHEMA.md orchestration/scaffolding/
mv BETA_NOMENCLATURE_SPEC.md orchestration/scaffolding/
mv BETA_VALIDATION_REPORT.md orchestration/scaffolding/
mv DUPLICATE_MANIFEST.md orchestration/scaffolding/
mv POST_FORGE_TREE.md orchestration/scaffolding/
mv RECONNAISSANCE_REPORT.md orchestration/scaffolding/
mv REVISION_PRIORITIES.md orchestration/scaffolding/
mv THREAD_TRAJECTORY.md orchestration/scaffolding/
mv CONTENT_ALIGNMENT_AUDIT.md orchestration/scaffolding/
mv COSMOS_ALIGNMENT_REPORT.md orchestration/scaffolding/

# B4: State files → orchestration/state/
mv ORACLE_DECISIONS.md orchestration/state/
mv THREAD_CONTEXT.md orchestration/state/
mv STANDARDS.md orchestration/state/
mv DESIGN_DECISIONS.md orchestration/state/
mv BACKLOG.md orchestration/state/
mv CURRENT_STATE.md orchestration/state/

# B5: Unified prompts → OPERATIONAL/prompts/unified/
mv ChatGPT-unified-prompt.md OPERATIONAL/prompts/unified/
mv ChatGPT-gemknowledge-base.md OPERATIONAL/prompts/unified/
mv Claude-unified-prompt.md OPERATIONAL/prompts/unified/
mv Claude-gemknowledge-base.md OPERATIONAL/prompts/unified/
mv Gemini-unified-prompt.md OPERATIONAL/prompts/unified/
mv Gemini-gemknowledge-base.md OPERATIONAL/prompts/unified/
mv Grok-unified-prompt.md OPERATIONAL/prompts/unified/
mv Grok-gemknowledge-base.md OPERATIONAL/prompts/unified/

# B6: Model profiles → OPERATIONAL/prompts/profiles/
mv MODEL_PROFILE-Claude-4-Sonnet.yaml OPERATIONAL/prompts/profiles/
mv MODEL_PROFILE-Claude-4_1-Opus.yaml OPERATIONAL/prompts/profiles/
mv MODEL_PROFILE-GPT-5.yaml OPERATIONAL/prompts/profiles/
mv MODEL_PROFILE-Gemini-2_5-Pro.yaml OPERATIONAL/prompts/profiles/
mv MODEL_PROFILE-Grok-4.yaml OPERATIONAL/prompts/profiles/

# B7: Function XMLs → OPERATIONAL/functions/
mv absorb.xml OPERATIONAL/functions/
mv amalgamate.xml OPERATIONAL/functions/
mv amplify.xml OPERATIONAL/functions/
mv anneal.xml OPERATIONAL/functions/
mv coalesce.xml OPERATIONAL/functions/
mv compile.xml OPERATIONAL/functions/
mv consolidate.xml OPERATIONAL/functions/
mv convert.xml OPERATIONAL/functions/
mv harmonize.xml OPERATIONAL/functions/
mv integrate.xml OPERATIONAL/functions/
mv listenize.xml OPERATIONAL/functions/
mv offload.xml OPERATIONAL/functions/
mv optimize.xml OPERATIONAL/functions/
mv primer.xml OPERATIONAL/functions/
mv readize.xml OPERATIONAL/functions/
mv reforge.xml OPERATIONAL/functions/
mv transcribe_interview.xml OPERATIONAL/functions/
mv transcribe_panel.xml OPERATIONAL/functions/
mv transcribe_youtube.xml OPERATIONAL/functions/
mv translate.xml OPERATIONAL/functions/

# B8: Function documentation → OPERATIONAL/functions/
mv integrate.md OPERATIONAL/functions/
mv listenize.md OPERATIONAL/functions/
mv readize.md OPERATIONAL/functions/
mv transcribe_interview.md OPERATIONAL/functions/
mv transcribe_youtube.md OPERATIONAL/functions/

# B9: Shell scripts → OPERATIONAL/
mv rename_canon.sh OPERATIONAL/
mv validate_frontmatter.sh OPERATIONAL/

# B10: Queue content → QUEUE/
mv CONTENT_PROCESSING_QUEUE.md QUEUE/modal1/
mv YOUTUBE_PROCESSING_BACKLOG.md QUEUE/modal1/
mv QUICK_WINS.md QUEUE/modal1/
mv AI_Academic_Research.md QUEUE/modal2/
mv AI_Image_Generators.md QUEUE/modal2/
mv AI_Workflows_in_Video_and_Visual_Effects.md QUEUE/modal2/
mv AI_3D_VFX.md QUEUE/modal2/
mv Physical_AI.md QUEUE/modal2/
mv The_Next_Wave_in_AI_Video_and_VFX.md QUEUE/modal2/
mv operational_engine.md QUEUE/pending/
mv operational_engine_md.NOTE QUEUE/pending/

# B11: Miscellaneous
mv FUNCTION_INDEX.md OPERATIONAL/
mv OPERATIONAL_DOCUMENTS_TODO.md orchestration/scaffolding/
mv CRYSTALLINE_CHARACTERISTICS.md orchestration/scaffolding/
mv AI_ECOSYSTEM_SURVEY.md QUEUE/modal1/
```

**TOTAL CATEGORY B: ~85 files to MOVE**

---

### CATEGORY C: ALREADY CORRECT (VERIFY ONLY)

These should already be in correct locations. Verify they exist:

```bash
# C1: CANON files (71 files, flat structure)
ls CANON/CANON-00000-SCHEMA-cosmos.md
ls CANON/CANON-00001-ORIGIN-cosmos.md
ls CANON/CANON-00002-LINEAGE-cosmos.md
# ... (verify all 71)

# C2: README, TEMPLATE, ARCHIVE
ls README.md
ls TEMPLATE.md
ls ARCHIVE/
```

---

### CATEGORY D: CREATE IF MISSING

```bash
# D1: Ensure directory structure exists
mkdir -p orchestration/state
mkdir -p orchestration/execution_logs
mkdir -p orchestration/directives
mkdir -p orchestration/scaffolding
mkdir -p OPERATIONAL/functions
mkdir -p OPERATIONAL/prompts/unified
mkdir -p OPERATIONAL/prompts/profiles
mkdir -p QUEUE/modal1
mkdir -p QUEUE/modal2
mkdir -p QUEUE/pending
mkdir -p aliases/cosmos
mkdir -p aliases/core
mkdir -p aliases/lattice
mkdir -p aliases/chains/intelligence
mkdir -p aliases/chains/information
mkdir -p aliases/chains/insight
mkdir -p aliases/chains/expertise
mkdir -p aliases/chains/knowledge
mkdir -p aliases/chains/wisdom
```

---

## TARGET STATE

After execution, repository root should contain ONLY:

```
syncrescendence/
├── README.md
├── TEMPLATE.md
├── ARCHIVE/
├── CANON/                    # 71 files, FLAT
├── EXEMPLA/
├── OPERATIONAL/
│   ├── functions/            # All XMLs + function docs
│   ├── prompts/
│   │   ├── unified/          # Platform prompts
│   │   └── profiles/         # MODEL_PROFILE YAMLs
│   └── *.sh                   # Shell scripts
├── QUEUE/
│   ├── modal1/               # Current modal queue
│   ├── modal2/               # Visual modal queue
│   └── pending/              # Unclassified
├── aliases/                  # Symlinks for Finder navigation
└── orchestration/
    ├── state/                # Living state files
    ├── execution_logs/       # All execution logs
    ├── directives/           # All directives
    └── scaffolding/          # Working documents
```

**Root should have ~6-8 items, not 180+**

---

## VERIFICATION PROTOCOL

After ALL deletions and moves:

```bash
# V1: Count root items (should be ~6-8)
ls | wc -l

# V2: No legacy patterns at root
ls | grep -E "^GENESIS-|^CANON-|^Technological_|^Technology_|^Al_|^ALPHA_|^BETA_|^EXECUTION_LOG|^DIRECTIVE-" | wc -l
# Should be 0

# V3: CANON file count
ls CANON/*.md | wc -l
# Should be 71

# V4: No duplicates in CANON
ls CANON/ | grep -E "CANON-0000[1-9].*SYNCRESCENDENCE|CANON-0000[2-9].*CORPUS" | wc -l
# Should be 0

# V5: Orchestration structure
ls orchestration/state/ | wc -l      # Should be ~6-8
ls orchestration/execution_logs/ | wc -l  # Should be ~16
ls orchestration/directives/ | wc -l      # Should be ~8

# V6: OPERATIONAL structure
ls OPERATIONAL/functions/*.xml | wc -l    # Should be ~20
ls OPERATIONAL/prompts/unified/*.md | wc -l   # Should be 8
ls OPERATIONAL/prompts/profiles/*.yaml | wc -l  # Should be 5

# V7: QUEUE structure
ls QUEUE/modal1/ | wc -l
ls QUEUE/modal2/ | wc -l
ls QUEUE/pending/ | wc -l
```

---

## EXECUTION LOG REQUIREMENTS

Your execution log MUST include:

```markdown
# EXECUTION LOG: DIRECTIVE-027
## Comprehensive Forge

---

## PRE-EXECUTION SURVEY

### Root File Count Before
[Output of ls | wc -l]

### Legacy Patterns Found
[Output of pattern searches]

### Current Structure Assessment
[Summary of what exists where]

---

## CATEGORY A: DELETIONS

### Files Deleted
[List each file deleted with confirmation]

### Deletion Verification
[Confirm files no longer exist]

---

## CATEGORY B: MOVES

### Files Moved
[List each file with source → destination]

### Move Verification
[Confirm files in new locations]

---

## CATEGORY C: VERIFICATION

### Correct Files Confirmed
[List files verified in correct locations]

---

## CATEGORY D: STRUCTURE CREATION

### Directories Created
[List any directories that were missing]

---

## POST-EXECUTION VERIFICATION

### Root File Count After
[Should be ~6-8]

### Final Structure
[tree output or ls -R summary]

### All Verification Checks
[V1 through V7 outputs]

---

## ORACLE DECISIONS ENCODED

This execution implements:
1. Oracle4 metabolism model (canonize or delete)
2. Oracle5-6 GENESIS canonization
3. Oracle5-6 cosmos renumbering
4. Oracle6 flat hierarchy with aliases
5. Oracle7 documentation protocol
6. Oracle7 comprehensive verification

---

## STATUS: [COMPLETE/INCOMPLETE]

Files deleted: X
Files moved: Y
Errors encountered: Z
Root items remaining: N
```

---

## FAILURE MODES TO AVOID

1. **Don't claim completion without verification** — Run ALL verification commands
2. **Don't skip files** — Execute EVERY deletion and move listed
3. **Don't create new problems** — If a file doesn't exist, skip it (don't error)
4. **Don't leave partial state** — Complete ALL categories before declaring done
5. **Don't lose context** — The Oracle Decisions section explains WHY

---

## SUCCESS CRITERIA (18-Lens)

| Lens | Criterion |
|------|-----------|
| Syncrescendent Route | Repository structure matches Oracle decisions |
| Bitter Lesson | Clean structure scales to 1000+ files |
| Antifragile | Robust to future changes |
| Meet the Moment | Current state reflects current understanding |
| Elegance + Dev Happiness | Root is clean, navigation is clear |
| Agentify + Human-Navigable | Any agent can traverse; human understands in 5 min |
| Industrial Engineering | Zero rework from structural confusion |
| Lean | No waste (duplicates, legacy, orphans) |
| Six Sigma | Zero defects in structure |

---

**EXECUTE COMPREHENSIVELY. VERIFY RIGOROUSLY. COMPLETE IN ONE PASS.**
