# CANON-31121: TONE LIBRARY TAXONOMY
## SN: Complete Classification Framework for Systematic Content Production

```yaml
id: CANON-31121
tier: satellite
chain: INFORMATION
parent: CANON-31120
sn_version: 1.0.0
compression: ~93%
```

---

## SUTRA

Rhetorical taxonomy enabling Recipe-based content execution across 11 dimensions spanning function→form→execution.

---

## GLOSS

This taxonomy consolidates classification structures from TONE LIBRARY enabling systematic content production through Recipe-based execution. Provides 90 total entries across rhetorical functions, stylistic forms, cadence patterns, diction rules, guardrails, evidence types, CTAs, scaffold elements, families, audience archetypes, and domains. Functions as reference when creating Recipes or analyzing existing content for rhetorical structure.

---

## SPEC

### TERM::TaxonomyScope
```
sutra: 11 taxonomies | 90 entries | function→form→execution
spec:
  taxonomies:
    - rhetorical_function: 10
    - stylistic_form: 15
    - cadence_pattern: 4
    - diction_pattern: 4
    - guardrail: 5
    - evidence_type: 5
    - cta_pattern: 5
    - scaffold_element: 7
    - family: 10
    - recipient_archetype: 10
    - domain: 15
  total_entries: 90
```

---

### TERM::RhetoricalFunction
```
sutra: Core communicative purpose shaping structure + evidence deployment

spec:
  functions[10]:
    inform_describe:
      job: "deliver accurate facts and contours"
      structure: fact >> context >> significance
      anti: fact_piles | undefined_jargon | scope_creep

    explain_interpret:
      job: "make why/how legible"
      structure: claim >> mechanism >> example >> implication
      anti: theory_sans_instance | metaphor_fights_model

    instruct_enable:
      job: "enable correct action now"
      structure: prereqs >> steps >> checks >> pitfalls >> next
      anti: prose_walls | missing_guardrails | tool_agnostic

    evaluate_appraise:
      job: "judge quality against criteria"
      structure: criteria >> evidence >> score >> recommendation
      anti: vibe_judgments | hidden_criteria | apples_oranges

    argue_persuade:
      job: "change a mind"
      structure: thesis >> reasons >> evidence >> counter >> close
      anti: straw_men | moralizing | scope_inflation

    decide_recommend:
      job: "cause a choice"
      structure: goal_constraints >> options >> risks_returns >> pick >> rationale
      anti: it_depends | hidden_assumptions | option_bloat

    mobilize_organize:
      job: "move people to coordinated action"
      structure: shared_stake >> concrete_ask >> roles >> timeline >> proof
      anti: abstract_uplift | no_next_step | heroic_singularity

    console_repair:
      job: "restore trust and agency"
      structure: acknowledge >> own_impact >> remedy >> safeguards >> check_in
      anti: passive_voice | conditional_apology | remedy_sans_timeline

    sensemake_reframe:
      job: "change how problem seen"
      structure: current_frame >> limits >> new_frame >> payoff >> test
      anti: rename_sans_consequence | neologism_fog

    investigate_forensic:
      job: "establish what happened and why"
      structure: timeline >> evidence_chain >> causal_factors >> correctives
      anti: blame_hunt | single_cause | unverifiable
```

---

### TERM::StylisticForm
```
sutra: Structural templates by flavor family | skeleton architecture

spec:
  narrative_family[6]:
    profile_sketch: scenes >> quotes >> motif
    vignette_chain: beats >> echo_image >> capstone
    tick_tock: timeline >> turning_points >> aftermath
    quest_arc: call >> trials >> return_with_tool
    heist_build: team_roles >> plan_seams >> execution >> reveal
    failure_memoir: hypothesis >> failure_mode >> remedy

  explanatory_family[5]:
    mechanism_walkthrough: parts >> interactions >> failures >> implications
    comparative_anatomy: dimensions >> matrix >> verdict
    taxonomy_sheet: definition >> contrast >> example >> rule_of_thumb
    analogy_ladder: everyday_image >> controlled_stretch >> formalization
    faq_ledger: question >> shortest_true >> pointer

  instructional_family[4]:
    recipe_card: BOM >> timing >> technique >> variations
    decision_tree: if_else >> thresholds >> stop_conditions
    field_manual: signals >> actions >> kit >> warnings
    pattern_language: context >> problem >> forces >> solution >> known_uses
```

---

### TERM::CadencePattern
```
sutra: Sentence rhythm calibrated to reading context + cognitive load

spec:
  bands[4]:
    staccato:
      wps: 8-12
      def: "short crisp urgency"
      use: checklists | briefings | emergencies

    compact:
      wps: 12-16
      def: "balanced clarity flow, default"
      use: layered_explainers | FAQs | tutorials

    measured:
      wps: 16-20
      def: "connective tissue, suited to analysis"
      use: thesis_essays | features | analytics

    longline:
      wps: 20-28
      def: "expansive rolling elevated"
      use: prose_poems | manifestos | contemplative
```

---

### TERM::DictionPattern
```
sutra: Vocabulary calibration | accessibility <-> precision

spec:
  registers[4]:
    plain_english:
      register: plain
      rule: "everyday words, define jargon"

    technical_precise:
      register: mid
      rule: "terms of art, define once reuse"

    elevated_clean:
      register: elevated
      rule: "lean lyricism, imagery serves clarity"

    second_person_direct:
      pronoun: you
      rule: "imperative verbs, instruction focus"
```

---

### TERM::Guardrail
```
sutra: Quality controls ensuring honesty + reader safety

spec:
  constraints[5]:
    steelman_opposing:
      def: "present strongest countercase first"
      params: include=sources

    bounded_claims:
      def: "state limits scope uncertainty"
      params: section=limits

    source_attribution:
      def: "cite docs data authors plainly"
      params: style=minimal

    hazard_notice:
      def: "flag safety thresholds upfront"
      params: thresholds=values

    privacy_safe:
      def: "avoid revealing sensitive PII"
      params: pii=false
```

---

### TERM::EvidenceType
```
sutra: Proof structures supporting claims + enabling verification

spec:
  modes[5]:
    anecdote: "single illustrative incident"
    case: "structured named example with context outcome"
    data: "quantitative tabular measured facts"
    mechanism: "causal explanation parts interactions"
    demonstration: "direct showing reproduction of method"
```

---

### TERM::CTAPattern
```
sutra: Reader activation | comprehension >> practice

spec:
  actions[5]:
    checklist:
      def: "concrete items verify completion"
      params: count=5-9

    exercise:
      def: "short task practice transfer"
      params: time=10-20min

    question_set:
      def: "prompts test understanding"
      params: items=3-7

    decision:
      def: "choose among options with criteria"
      params: thresholds=list

    report_back:
      def: "ask evidence of completion"
      params: artifact=screenshot|log
```

---

### TERM::ScaffoldElement
```
sutra: Organizational structures enhancing navigation + comprehension

spec:
  structures[7]:
    headings: "chunk topics H2/H3 depth=2-3"
    numbered_steps: "ordered procedure checks pitfalls"
    bulleted_lists: "concise scan-readers max=12wps"
    callouts: "highlight rules hazards tips tone=warn|info|success"
    sidebar: "parallel track context definitions width=1/3"
    faq_block: "Q >> shortest_true >> pointer"
    timeline_table: "time-stamped sequence cols=time,event,notes"
```

---

### TERM::FamilyFlavor
```
sutra: High-level genre classifications | 10 flavors

spec:
  families[10]:
    - narrative_story: "character-driven temporal scene-based"
    - explanatory_mapmaking: "conceptual structural sense-making"
    - instructional_procedural: "action-oriented step-based enabling"
    - dialogic_deliberative: "multi-voice question-driven exploratory"
    - persuasive_polemical: "argument-driven position mind-changing"
    - scientific_technical: "evidence-based methodology falsifiable"
    - journalistic_documentary: "event-based source-verified timely"
    - commercial_product: "value-driven conversion benefit-oriented"
    - civic_legal_governance: "policy rights accountability"
    - devotional_reflective: "contemplative meaning-seeking form-only"
```

---

### TERM::RecipientArchetype
```
sutra: Audience models | distinct entry states + success criteria

spec:
  personas[10]:
    first_step_novice:
      brief: "orientation without shame"
      success: "retell gist attempt one practice"

    credential_seeker:
      brief: "scoped mastery pass thresholds"
      success: "checklist + practice completed"

    self_directed_generalist:
      brief: "mental map first details later"
      success: "schema with links acquired"

    meaning_seeker:
      brief: "why matters existentially"
      success: "felt coherence + daily practice"

    workflow_optimizer:
      brief: "faster safer execution"
      success: "time saved errors reduced"

    frontline_operator:
      brief: "do it right under pressure"
      success: "fewer mistakes today"

    builder_maker:
      brief: "how to prototype today"
      success: "first demo built"

    reliability_steward:
      brief: "eliminate failure modes"
      success: "fewer regressions"

    executive_decider:
      brief: "clear options risks upside"
      success: "decision + rationale documented"

    portfolio_evaluator:
      brief: "asymmetric bets"
      success: "calibrated priors go/no-go"
```

---

### TERM::DomainContext
```
sutra: Subject-matter contexts | terminology + expectations

spec:
  domains[15]:
    - research: "academic inquiry hypothesis-driven"
    - science: "empirical methods falsifiable"
    - engineering: "systems design implementation"
    - product: "user-centered market-oriented"
    - design: "aesthetic decisions UX"
    - ux: "interaction patterns usability"
    - data: "quantitative statistical"
    - ai_ml: "algorithm model training"
    - devops: "infrastructure deployment"
    - security: "threat modeling vulnerability"
    - policy: "governance regulatory"
    - civic: "public participation democratic"
    - law: "legal reasoning precedent"
    - finance: "capital allocation risk"
    - education: "learning design pedagogical"
```

---

## PROC::RecipeConstruction
```
sutra: Creating Recipe for systematic content production

steps:
  1: select_function >> 10 rhetorical based on goal
  2: choose_style >> 15 forms matching structure
  3: set_cadence >> 4 bands per reading context
  4: specify_diction >> 4 patterns accessibility|precision
  5: apply_guardrails >> 1-3 quality safety
  6: define_evidence >> 2-4 modes supporting claims
  7: design_cta >> 1-2 patterns activation
  8: select_scaffold >> 2-5 elements navigation
  9: identify_family >> 10 flavor classification
  10: target_archetype >> 1-2 recipient personas
  11: specify_domain >> subject-matter context
```

---

## PROC::ContentAnalysis
```
sutra: Assessing content for rhetorical structure

steps:
  1: identify_function >> what job doing?
  2: recognize_style >> what skeleton organizes?
  3: measure_cadence >> avg wps?
  4: assess_diction >> plain|technical|elevated?
  5: check_guardrails >> bounded? attributed?
  6: catalog_evidence >> which modes deployed?
  7: evaluate_cta >> activates readers?
  8: note_scaffold >> which elements present?
  9: classify_family >> which flavor?
  10: determine_archetype >> who is this for?
  11: identify_domain >> what context?
```

---

## XREF

```yaml
parent: [[CANON-31120-TONE_LIBRARY-lunar-ACUMEN-planetary-INFORMATION]]
siblings:
  - [[CANON-31122-RHETORICAL-satellite-TONE_LIBRARY-lunar-ACUMEN-planetary-INFORMATION]]
integration_points:
  - Rhetorical Calibration >> Recipe parameters
  - Feedcraft >> Family Style Cadence selection
  - Technology Stack >> Domain >> tool selection
  - Operations >> Archetype >> content calendar
  - Curriculum >> Instructional Family >> lesson structure
```

---

**Status**: Taxonomy complete | Ready for Recipe population P0-2
**Source**: Acumen Lunar TONE LIBRARY CSVs (October 2025)
