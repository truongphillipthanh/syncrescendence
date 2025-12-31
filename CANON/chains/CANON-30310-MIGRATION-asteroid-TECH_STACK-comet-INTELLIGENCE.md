---
id: CANON-30310
name: Tech Stack Migration
identity: Technology Stack Database Complete Migration
tier: CANON
type: asteroid
version: 1.0.0
status: canonical
created: 2025-10-17
updated: 2025-12-30
synopsis: Complete migration protocol for transforming fragmentary Technology artifacts into coherent, queryable database implementing ASA Model classification
chain: INTELLIGENCE
parent: CANON-30300
---

# Technology Stack Database: Complete Migration

---

## I. EXECUTIVE SUMMARY

This document completes the migration of fragmentary Technology lunar artifacts into a coherent, queryable database implementing the ASA Model classification framework. Three CSV files (447 apps, 42 models, 31 API pricing records) have been analyzed, structured, and prepared for operational use.

**What This Enables**:
- Capability-based tool discovery ("What can edit PDFs?")
- Context-aware routing ("Quick capture tool for Layer 3?")
- Primitive-based search ("What has vim keybindings?")
- Workflow intelligence ("Complete writing apparatus?")
- Cost optimization ("Cheapest reasoning model?")
- Lifecycle management ("Show obsolete tools")

**Current State**: Schema complete, data analyzed, migration protocol specified. Ready for database instantiation and interface development.

---

## II. SOURCE DATA ANALYSIS

### Function.csv - 447 Applications

**Structure**:
- Role (functional classification)
- Apparatus (workflow grouping, mostly null - awaiting crystallization)
- Application (name + Notion URL)
- Description (detailed functional explanation)
- Layer (ASA cognitive layer reference)
- Stage (workflow phase reference)

**Sample Patterns**:
```
Role: ContentSourceProcurer
Layer: 3 - Index
Stage: Feed Definement
Apps: Feedly, Inoreader, NewsBlur

Role: PowerSourceProcurer  
Layer: 3 - Index
Stage: Feed Definement
Apps: Inoreader (high-volume RSS)

Role: NewsSourceProcurer
Layer: 3 - Index  
Stage: Feed Definement
Apps: NewsBlur (intelligent filtering)
```

**Key Insight**: Role taxonomy is rich but needs normalization. Many roles appear once, suggesting either:
1. Over-specification (consolidation needed)
2. Legitimate diversity (preserve granularity)

### Models.csv - 42 AI Models

**Structure**:
- Name (model identifier)
- API (API endpoint string)
- Family (model series: GPT-4.1, o3, Claude 4, etc.)
- Research Lab (OpenAI, Anthropic, Google, Meta, etc.)
- Context Window (token capacity)
- Input/Output (modality capabilities)
- Output Token Limit (generation ceiling)
- Type (Reasoning, Coding, General, etc.)
- Vision (Yes/No)
- Extended Thinking (Yes/No)
- Search (Yes/No)
- Training Cutoff Data (knowledge date)
- Release (publication date)

**Sample Patterns**:
```
o3 (OpenAI): 200K context, Reasoning, Search, $10/$40 per M tokens
GPT-4.1 (OpenAI): 1.047M context, Coding, Vision, $2/$8 per M tokens  
Claude Sonnet 4.5 (Anthropic): 200K context, General, $3/$15 per M tokens
Gemini 2.5 Pro (Google): 2M context, General, Vision, $1.25/$10 per M tokens
```

**Key Insight**: Models differentiate on: context window, modality support, specialized capabilities (reasoning/coding), and pricing. Need multi-dimensional filtering.

### API.csv - 31 Pricing Records

**Structure**:
- api_name (matches Models.csv)
- input_token_pricing (per million)
- output_token_pricing (per million)
- cached_input_token_pricing (caching discount)
- context_caching_storage (persistence pricing)
- prompt_caching read/write pricing (varies by context size)
- audio input/output pricing (when applicable)
- search_pricing_per_1000 (search capability cost)

**Sample Patterns**:
```
gpt-4.1: $2 input / $8 output, $0.50 cached
o3: $10 input / $40 output, $2.50 cached
claude-sonnet-4.5: $3 input / $15 output, $0.30 cached
gemini-2.5-pro: $1.25 input / $10 output, $0.313 cached
```

**Key Insight**: Pricing varies 10x across models. Caching provides 4-10x discount. Cost optimization requires use-case analysis (token volume, caching viability, context requirements).

---

## III. DATABASE SCHEMA

### A. Bedrock Layer - Taxonomies (Stable Categories)

```sql
-- Cognitive Layers (ASA Model dimensional substrate)
CREATE TABLE layers (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  description TEXT,
  domain TEXT, -- mechanics, symbols, semantics, narrative, etc.
  sort_order INTEGER
);

-- Functional Roles (what the app does in workflow)
CREATE TABLE roles (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  parent_role_id INTEGER REFERENCES roles(id),
  layer_id INTEGER REFERENCES layers(id),
  description TEXT,
  frequency_count INTEGER DEFAULT 1
);

-- ASA Object Types (classification categories)
CREATE TABLE object_types (
  id INTEGER PRIMARY KEY,
  asa_code TEXT NOT NULL UNIQUE, -- O.MOD, O.SVC, O.DP, O.PRO, etc.
  name TEXT NOT NULL,
  description TEXT
);

-- Modalities (input/output capabilities)
CREATE TABLE modalities (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE, -- Text, Images, Audio, Video, Documents, Code
  description TEXT
);

-- Lifecycle States (tool evolution tracking)
CREATE TABLE lifecycle_states (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE, -- Active, Primitive Repository, Deprecated, Superseded
  description TEXT,
  is_operational BOOLEAN DEFAULT TRUE
);

-- Research Labs (AI model creators)
CREATE TABLE research_labs (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  url TEXT,
  focus_areas TEXT
);

-- Model Types (specialized capabilities)
CREATE TABLE model_types (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE, -- Reasoning, Coding, General, Multimodal
  description TEXT
);

-- Workflow Stages (TOOLCRAFT phases)
CREATE TABLE workflow_stages (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  area TEXT, -- Capture, Synthesis, Articulation, etc.
  sort_order INTEGER
);
```

### B. Settlement Layer - Entities (Dynamic Instances)

```sql
-- Applications (the 447 tools)
CREATE TABLE apps (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  url TEXT,
  role_id INTEGER REFERENCES roles(id),
  layer_id INTEGER REFERENCES layers(id),
  object_type_id INTEGER REFERENCES object_types(id),
  lifecycle_state_id INTEGER REFERENCES lifecycle_states(id),
  stage_id INTEGER REFERENCES workflow_stages(id),
  description TEXT,
  notes TEXT,
  date_added DATE DEFAULT CURRENT_DATE,
  last_reviewed DATE,
  notion_url TEXT -- preserve original links
);

-- AI Models (the 42 models)
CREATE TABLE models (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  api_name TEXT UNIQUE,
  family TEXT, -- GPT-4.1, o3, Claude 4, etc.
  research_lab_id INTEGER REFERENCES research_labs(id),
  model_type_id INTEGER REFERENCES model_types(id),
  context_window INTEGER,
  output_token_limit INTEGER,
  has_vision BOOLEAN DEFAULT FALSE,
  has_extended_thinking BOOLEAN DEFAULT FALSE,
  has_search BOOLEAN DEFAULT FALSE,
  training_cutoff_date DATE,
  release_date DATE,
  object_type_id INTEGER REFERENCES object_types(id),
  lifecycle_state_id INTEGER REFERENCES lifecycle_states(id),
  notes TEXT
);

-- Model Capabilities (modality support)
CREATE TABLE model_capabilities (
  model_id INTEGER REFERENCES models(id),
  modality_id INTEGER REFERENCES modalities(id),
  capability_type TEXT, -- input, output, both
  notes TEXT,
  PRIMARY KEY (model_id, modality_id, capability_type)
);

-- API Pricing (cost data)
CREATE TABLE api_pricing (
  id INTEGER PRIMARY KEY,
  model_id INTEGER REFERENCES models(id),
  input_token_price DECIMAL(10,6), -- per million tokens
  output_token_price DECIMAL(10,6),
  cached_input_price DECIMAL(10,6),
  audio_input_price DECIMAL(10,6),
  audio_output_price DECIMAL(10,6),
  search_price_per_1000 DECIMAL(10,6),
  context_caching_storage TEXT,
  prompt_caching_read_price DECIMAL(10,6),
  prompt_caching_write_price DECIMAL(10,6),
  prompt_caching_read_price_200k DECIMAL(10,6),
  prompt_caching_write_price_200k DECIMAL(10,6),
  effective_date DATE DEFAULT CURRENT_DATE,
  notes TEXT
);
```

### C. Primitive Layer - Feature Extraction

```sql
-- Primitives (reusable features extracted from apps)
CREATE TABLE primitives (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  category TEXT, -- keybinding, rendering, collaboration, storage, etc.
  description TEXT,
  source_app_id INTEGER REFERENCES apps(id), -- where first identified
  extractable BOOLEAN DEFAULT TRUE,
  lifecycle_state_id INTEGER REFERENCES lifecycle_states(id),
  date_identified DATE DEFAULT CURRENT_DATE
);

-- App-Primitive Relationships (which apps have which primitives)
CREATE TABLE app_primitives (
  app_id INTEGER REFERENCES apps(id),
  primitive_id INTEGER REFERENCES primitives(id),
  implementation_quality TEXT, -- excellent, good, basic, poor
  notes TEXT,
  PRIMARY KEY (app_id, primitive_id)
);
```

### D. Intelligence Layer - Relationships & Patterns

```sql
-- Apparatus (emergent workflow configurations)
CREATE TABLE apparatus (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  description TEXT,
  emergence_pattern TEXT, -- how components combine
  frequency_score INTEGER DEFAULT 0, -- how often used
  stability_score INTEGER DEFAULT 0, -- how consistent
  last_detected DATE,
  is_canonical BOOLEAN DEFAULT FALSE, -- promoted to standard
  notes TEXT
);

-- Apparatus Components (apps composing each apparatus)
CREATE TABLE apparatus_components (
  apparatus_id INTEGER REFERENCES apparatus(id),
  app_id INTEGER REFERENCES apps(id),
  role_in_apparatus TEXT,
  is_essential BOOLEAN DEFAULT TRUE,
  sort_order INTEGER,
  PRIMARY KEY (apparatus_id, app_id)
);

-- App Relationships (how apps interact)
CREATE TABLE app_relationships (
  app_id INTEGER REFERENCES apps(id),
  related_app_id INTEGER REFERENCES apps(id),
  relationship_type TEXT, -- powers, competes, requires, obsoletes, combines, complements
  strength INTEGER DEFAULT 5, -- 1-10 scale
  notes TEXT,
  PRIMARY KEY (app_id, related_app_id),
  CHECK (app_id != related_app_id)
);

-- Model Comparisons (competitive analysis)
CREATE TABLE model_comparisons (
  model_a_id INTEGER REFERENCES models(id),
  model_b_id INTEGER REFERENCES models(id),
  dimension TEXT, -- cost, speed, quality, context, etc.
  winner_id INTEGER REFERENCES models(id),
  notes TEXT,
  last_updated DATE DEFAULT CURRENT_DATE,
  PRIMARY KEY (model_a_id, model_b_id, dimension)
);
```

---

## IV. DATA MIGRATION PROTOCOL

### Phase 1: Taxonomy Population (Bedrock)

```sql
-- Insert Layers
INSERT INTO layers (name, description, domain, sort_order) VALUES
  ('0 - Substrate', 'Computational mechanics', 'mechanics', 0),
  ('1 - Logic', 'Symbolic operations', 'symbols', 1),
  ('2 - Memory', 'Semantic networks', 'semantics', 2),
  ('3 - Index', 'Organizational structures', 'indexing', 3),
  ('4 - Voice', 'Expressive capabilities', 'narrative', 4),
  ('5 - Mirror', 'Self-awareness systems', 'reflection', 5),
  ('6 - Temple', 'Value alignment', 'ethics', 6);

-- Insert Object Types (from ASA Model)
INSERT INTO object_types (asa_code, name, description) VALUES
  ('O.MOD', 'Model', 'AI language model'),
  ('O.SVC', 'Service', 'Cloud-hosted application'),
  ('O.DP', 'Data Pipeline', 'Information flow system'),
  ('O.PRO', 'Protocol', 'Communication standard'),
  ('O.PKG', 'Package', 'Software library'),
  ('O.KIT', 'Toolkit', 'Integrated tool suite'),
  ('O.ENV', 'Environment', 'Development platform');

-- Insert Modalities
INSERT INTO modalities (name, description) VALUES
  ('Text', 'Plain text input/output'),
  ('Documents', 'Structured documents (PDF, DOCX, etc.)'),
  ('Images', 'Visual content'),
  ('Audio', 'Sound recordings'),
  ('Video', 'Moving pictures'),
  ('Code', 'Programming languages');

-- Insert Lifecycle States
INSERT INTO lifecycle_states (name, description, is_operational) VALUES
  ('Active', 'Currently used in workflows', TRUE),
  ('Primitive Repository', 'Useful features, seeking extraction', TRUE),
  ('Deprecated', 'Superseded but not removed', FALSE),
  ('Superseded', 'Replaced by superior alternative', FALSE),
  ('Experimental', 'Testing phase', TRUE),
  ('Archived', 'Historical reference only', FALSE);

-- Insert Research Labs
INSERT INTO research_labs (name, url, focus_areas) VALUES
  ('OpenAI', 'https://openai.com', 'AGI development, reasoning models, coding assistants'),
  ('Anthropic', 'https://anthropic.com', 'Constitutional AI, safety research, helpful assistants'),
  ('Google DeepMind', 'https://deepmind.google', 'Multimodal models, search integration, long context'),
  ('Meta AI', 'https://ai.meta.com', 'Open source models, multilingual capabilities'),
  ('Mistral AI', 'https://mistral.ai', 'European AI, efficient models'),
  ('xAI', 'https://x.ai', 'Real-time knowledge, Twitter integration');

-- Insert Model Types
INSERT INTO model_types (name, description) VALUES
  ('Reasoning', 'Extended chain-of-thought, complex problem solving'),
  ('Coding', 'Programming assistance, code generation, debugging'),
  ('General', 'Broad capabilities, conversational AI'),
  ('Multimodal', 'Handles multiple input/output types'),
  ('Specialized', 'Domain-specific optimization');

-- Insert Workflow Stages (from TOOLCRAFT)
INSERT INTO workflow_stages (name, area, sort_order) VALUES
  ('Capture', 'Intake', 1),
  ('Feed Definement', 'Curation', 2),
  ('Synthesis', 'Processing', 3),
  ('Articulation', 'Production', 4),
  ('Distribution', 'Dissemination', 5),
  ('Measurement', 'Assessment', 6);
```

### Phase 2: Entity Migration (Settlements)

```javascript
// Function.csv → apps table
import Papa from 'papaparse';

const functionCsv = await window.fs.readFile('Technology Lunar  Function.csv', { encoding: 'utf8' });
const functionData = Papa.parse(functionCsv, { header: true, dynamicTyping: true, skipEmptyLines: true });

// Extract unique roles
const roles = new Set();
functionData.data.forEach(row => {
  if (row.Role) roles.add(row.Role.trim());
});

// Insert roles (with deduplication and normalization)
const roleInserts = Array.from(roles).map((role, idx) => {
  // Normalize role names: remove suffixes like "Procurer", "Manager", etc.
  const normalized = role.replace(/(Procurer|Manager|Handler|Processor)$/, '').trim();
  return `INSERT INTO roles (id, name, description) VALUES (${idx + 1}, '${role}', 'Extracted from Function.csv');`;
});

// Insert apps (simplified - actual implementation would parse Notion URLs, extract clean names, etc.)
const appInserts = functionData.data.map((row, idx) => {
  const appName = row.Application ? row.Application.split('(')[0].trim() : 'Unknown';
  const notionUrl = row.Application ? row.Application.match(/\((.*?)\)/)?.[1] : null;
  
  return `
  INSERT INTO apps (id, name, role_id, description, notion_url, lifecycle_state_id)
  VALUES (
    ${idx + 1},
    '${appName.replace(/'/g, "''")}',
    (SELECT id FROM roles WHERE name = '${row.Role?.replace(/'/g, "''")}'),
    '${row.Description?.replace(/'/g, "''")}',
    '${notionUrl}',
    1 -- Active by default
  );`;
});

// Models.csv → models table
const modelsCsv = await window.fs.readFile('Technology Lunar  Models.csv', { encoding: 'utf8' });
const modelsData = Papa.parse(modelsCsv, { header: true, dynamicTyping: true, skipEmptyLines: true });

const modelInserts = modelsData.data.map((row, idx) => {
  return `
  INSERT INTO models (id, name, api_name, family, research_lab_id, model_type_id, 
                      context_window, output_token_limit, has_vision, has_extended_thinking, 
                      has_search, release_date)
  VALUES (
    ${idx + 1},
    '${row.Name?.replace(/'/g, "''")}',
    '${row.API?.split('(')[0].trim().replace(/'/g, "''")}',
    '${row.Family?.replace(/'/g, "''")}',
    (SELECT id FROM research_labs WHERE name LIKE '%${row['Research Lab']?.split('(')[0].trim()}%'),
    (SELECT id FROM model_types WHERE name = '${row.Type}'),
    ${row['Context Window']?.replace(/,/g, '') || 'NULL'},
    ${row['Output Token Limit']?.replace(/,/g, '') || 'NULL'},
    ${row.Vision === 'Yes' ? 'TRUE' : 'FALSE'},
    ${row['Extended Thinking'] === 'Yes' ? 'TRUE' : 'FALSE'},
    ${row.Search === 'Yes' ? 'TRUE' : 'FALSE'},
    ${row['Release  '] ? `'${row['Release  ']}'` : 'NULL'}
  );`;
});

// API.csv → api_pricing table
const apiCsv = await window.fs.readFile('Technology Lunar  API.csv', { encoding: 'utf8' });
const apiData = Papa.parse(apiCsv, { header: true, dynamicTyping: true, skipEmptyLines: true });

const pricingInserts = apiData.data.map((row, idx) => {
  const parsePrice = (priceStr) => priceStr ? parseFloat(priceStr.replace(/[\$,]/g, '')) : null;
  
  return `
  INSERT INTO api_pricing (id, model_id, input_token_price, output_token_price, cached_input_price)
  VALUES (
    ${idx + 1},
    (SELECT id FROM models WHERE api_name = '${row.api_name?.replace(/'/g, "''")}'),
    ${parsePrice(row.input_token_pricing)},
    ${parsePrice(row.output_token_pricing)},
    ${parsePrice(row.cached_input_token_pricing)}
  );`;
});
```

### Phase 3: Primitive Extraction (Feature Layer)

**Initial Primitive Catalog** (to be expanded through usage):

```sql
-- Keybinding Primitives
INSERT INTO primitives (name, category, description, extractable) VALUES
  ('Vim Motions', 'keybinding', 'hjkl navigation and modal editing', TRUE),
  ('Emacs Bindings', 'keybinding', 'Ctrl-based commands and macros', TRUE),
  ('Custom Shortcuts', 'keybinding', 'User-definable key combinations', TRUE);

-- Rendering Primitives
INSERT INTO primitives (name, category, description, extractable) VALUES
  ('Markdown Preview', 'rendering', 'Live markdown rendering', TRUE),
  ('Syntax Highlighting', 'rendering', 'Code syntax coloring', TRUE),
  ('LaTeX Rendering', 'rendering', 'Mathematical notation display', TRUE),
  ('Mermaid Diagrams', 'rendering', 'Flowchart and diagram rendering', TRUE);

-- Collaboration Primitives
INSERT INTO primitives (name, category, description, extractable) VALUES
  ('Real-time Sync', 'collaboration', 'Multi-user simultaneous editing', TRUE),
  ('Comment Threads', 'collaboration', 'Inline discussion capabilities', TRUE),
  ('Version History', 'collaboration', 'Timestamped change tracking', TRUE),
  ('Permissions Management', 'collaboration', 'Granular access control', TRUE);

-- Storage Primitives
INSERT INTO primitives (name, category, description, extractable) VALUES
  ('Local First', 'storage', 'Offline-capable with sync', TRUE),
  ('Cloud Native', 'storage', 'Server-side storage only', FALSE),
  ('Export Capabilities', 'storage', 'Multiple format export', TRUE),
  ('API Access', 'storage', 'Programmatic data access', TRUE);

-- Search Primitives
INSERT INTO primitives (name, category, description, extractable) VALUES
  ('Full-Text Search', 'search', 'Content-based search', TRUE),
  ('Tag-Based Search', 'search', 'Metadata filtering', TRUE),
  ('Fuzzy Matching', 'search', 'Approximate string matching', TRUE),
  ('Saved Searches', 'search', 'Reusable search queries', TRUE);

-- (Continue for 50+ primitives across categories)
```

### Phase 4: Intelligence Layer Population (Patterns)

**Apparatus Detection Examples**:

```sql
-- Writing Apparatus (detected from common usage patterns)
INSERT INTO apparatus (name, description, emergence_pattern, is_canonical) VALUES
  ('Academic Writing', 'Research → Draft → Cite → Publish workflow', 
   'Zotero + Obsidian + Pandoc + LaTeX', TRUE),
  ('Content Creation', 'Ideate → Outline → Write → Edit → Format',
   'Notion + Hemingway + Grammarly + Canva', TRUE),
  ('Technical Documentation', 'Design → Document → Review → Deploy',
   'Figma + VS Code + GitHub + ReadTheDocs', TRUE);

-- Populate apparatus components
INSERT INTO apparatus_components (apparatus_id, app_id, role_in_apparatus) VALUES
  ((SELECT id FROM apparatus WHERE name = 'Academic Writing'),
   (SELECT id FROM apps WHERE name = 'Zotero'),
   'Reference management'),
  ((SELECT id FROM apparatus WHERE name = 'Academic Writing'),
   (SELECT id FROM apps WHERE name = 'Obsidian'),
   'Note-taking and synthesis'),
  ((SELECT id FROM apparatus WHERE name = 'Academic Writing'),
   (SELECT id FROM apps WHERE name = 'Pandoc'),
   'Format conversion');
```

---

## V. NAVIGATION INTERFACE SPECIFICATIONS

### Query Patterns Supported

**1. Capability-Based Discovery**
```sql
-- "What can edit PDFs?"
SELECT a.name, a.description, r.name as role
FROM apps a
JOIN roles r ON a.role_id = r.id
WHERE a.description LIKE '%PDF%'
  AND a.description LIKE '%edit%'
  AND a.lifecycle_state_id = (SELECT id FROM lifecycle_states WHERE name = 'Active');
```

**2. Context-Aware Routing**
```sql
-- "Quick capture tool for Layer 3 (Index)?"
SELECT a.name, a.description, r.name as role
FROM apps a
JOIN roles r ON a.role_id = r.id
JOIN layers l ON a.layer_id = l.id
JOIN workflow_stages ws ON a.stage_id = ws.id
WHERE l.name = '3 - Index'
  AND ws.name = 'Capture'
  AND a.lifecycle_state_id = (SELECT id FROM lifecycle_states WHERE name = 'Active')
ORDER BY a.name;
```

**3. Primitive-Based Search**
```sql
-- "What has vim keybindings?"
SELECT a.name, a.description, ap.implementation_quality
FROM apps a
JOIN app_primitives ap ON a.app_id = ap.app_id
JOIN primitives p ON ap.primitive_id = p.id
WHERE p.name = 'Vim Motions'
  AND a.lifecycle_state_id = (SELECT id FROM lifecycle_states WHERE name = 'Active')
ORDER BY ap.implementation_quality DESC;
```

**4. Workflow Suggestion**
```sql
-- "Complete writing apparatus?"
SELECT ap.name as apparatus, 
       GROUP_CONCAT(a.name, ' → ') as components,
       ap.description
FROM apparatus ap
JOIN apparatus_components ac ON ap.id = ac.apparatus_id
JOIN apps a ON ac.app_id = a.app_id
WHERE ap.name LIKE '%Writing%'
  AND ap.is_canonical = TRUE
GROUP BY ap.id;
```

**5. Cost Optimization**
```sql
-- "Cheapest reasoning model?"
SELECT m.name, m.context_window, m.output_token_limit,
       pr.input_token_price, pr.output_token_price,
       pr.cached_input_price,
       (pr.input_token_price + pr.output_token_price) as total_cost
FROM models m
JOIN api_pricing pr ON m.id = pr.model_id
JOIN model_types mt ON m.model_type_id = mt.id
WHERE mt.name = 'Reasoning'
  AND m.lifecycle_state_id = (SELECT id FROM lifecycle_states WHERE name = 'Active')
ORDER BY total_cost ASC
LIMIT 5;
```

**6. Lifecycle Management**
```sql
-- "Show primitive repositories" (tools to extract features from)
SELECT a.name, a.description, 
       COUNT(ap.primitive_id) as primitives_extracted
FROM apps a
JOIN lifecycle_states ls ON a.lifecycle_state_id = ls.id
LEFT JOIN app_primitives ap ON a.id = ap.app_id
WHERE ls.name = 'Primitive Repository'
GROUP BY a.id
ORDER BY primitives_extracted DESC;
```

---

## VI. IMPLEMENTATION ROADMAP

### Week 1: Database Instantiation
- Create SQLite database file
- Execute taxonomy population scripts
- Validate schema integrity
- Set up backup protocols

### Week 2: Entity Migration
- Run Function.csv → apps migration
- Execute Models.csv → models migration
- Process API.csv → pricing migration
- Verify data integrity (row counts, referential integrity)
- Audit for duplicates and anomalies

### Week 3: Primitive Extraction
- Manual review of 50 high-value apps
- Extract 100+ initial primitives
- Populate app_primitives relationships
- Document extraction methodology

### Week 4: Interface Development
- Build query library (20+ common patterns)
- Create command-line tool for quick queries
- Design web interface mockups
- Test navigation flows

### Week 5: Intelligence Layer
- Identify 5-10 canonical apparatus
- Document emergence patterns
- Establish relationship mapping protocols
- Create apparatus crystallization guide

---

## VII. QUALITY ASSURANCE

### Data Integrity Checks

```sql
-- Orphaned apps (no role assigned)
SELECT COUNT(*) FROM apps WHERE role_id IS NULL;

-- Models without pricing
SELECT m.name FROM models m
LEFT JOIN api_pricing pr ON m.id = pr.model_id
WHERE pr.id IS NULL;

-- Apps without lifecycle state
SELECT COUNT(*) FROM apps WHERE lifecycle_state_id IS NULL;

-- Circular role hierarchies
WITH RECURSIVE role_tree AS (
  SELECT id, name, parent_role_id, 1 as depth
  FROM roles WHERE parent_role_id IS NULL
  UNION ALL
  SELECT r.id, r.name, r.parent_role_id, rt.depth + 1
  FROM roles r
  JOIN role_tree rt ON r.parent_role_id = rt.id
  WHERE rt.depth < 10
)
SELECT * FROM role_tree WHERE depth >= 10;
```

### Validation Metrics

**Success Criteria**:
- ✅ Zero data loss from CSV migration
- ✅ All 447 apps categorized and queryable
- ✅ All 42 models with complete capability data
- ✅ All 31 pricing records linked correctly
- ✅ 100+ primitives identified
- ✅ 5+ apparatus documented
- ✅ 20+ query patterns functional

---

## VIII. MAINTENANCE PROTOCOLS

### Update Frequencies

**High Velocity** (Weekly):
- New model releases
- API pricing changes
- New app discoveries

**Medium Velocity** (Monthly):
- Primitive extractions
- Apparatus crystallization
- Relationship mapping

**Low Velocity** (Quarterly):
- Taxonomy refinements
- Schema optimizations
- Documentation updates

### Contribution Workflow

1. **Discovery**: New tool encountered in workflow
2. **Evaluation**: Assess against existing tools
3. **Classification**: Apply ASA Model, assign role, identify layer
4. **Documentation**: Write description, note URL, extract primitives
5. **Integration**: Add to database, update relationships
6. **Validation**: Test queries, verify data integrity

---

## IX. FUTURE EXTENSIONS

### Planned Enhancements

**Phase 2** (After Beta Validation):
- Natural language query interface (AI-powered)
- Apparatus recommendation engine
- Cost modeling for typical workflows
- Integration with TONE LIBRARY (suggest tools for content production)
- Mobile companion app

**Phase 3** (After Stable Promotion):
- Community contributions (vetted tool submissions)
- Usage analytics (track which tools actually used)
- Workflow templates library
- Tool stack export/import (shareable configurations)

### Research Questions

- Can apparatus emergence be predicted from primitive combinations?
- What role taxonomy depth is optimal? (current: ~447 unique roles)
- How to measure tool obsolescence objectively?
- Can primitives be hierarchically organized?
- What defines a "canonical" apparatus?

---

## X. INTEGRATION POINTS

### Links to Other Moons

**Acumen Chain**:
- TONE LIBRARY uses model capabilities for content production
- Feedcraft references platform-specific tool requirements

**Mastery Chain**:
- Curriculum references tool stack for skill development
- Syllabus includes tool proficiency requirements

**Expertise Chain**:
- Business Operations tracks tool subscription costs
- Infrastructure planning uses capacity data

**Insight Chain**:
- Cognitive Palace maps tools to dimensional substrates
- ASA Model provides classification framework

---

## XI. FOUNDER ASSESSMENT

**[PLACEHOLDER FOR FOUNDER QUALITY EVALUATION]**

After reviewing database structure, migration protocol, and query capabilities, assess:
- Does schema capture essential tool ecosystem structure?
- Are query patterns aligned with actual discovery needs?
- Is primitive extraction methodology sound?
- What corrections or refinements needed before production use?

---

## XII. CONCLUSION

The Technology Stack Database consolidates three years of tool ecosystem evolution into a queryable, navigable system. It implements the ASA Model classification framework, preserves TOOLCRAFT workflow intelligence, and enables rational tool selection based on capability, context, cost, and primitive composition.

**Current State**: Schema complete, migration protocol specified, ready for database instantiation.

**Next Action**: Execute migration scripts, populate database, build query interface, begin primitive extraction.

**Critical Path**: This system unblocks content production (provides reliable tool recommendations), curriculum development (specifies required tool proficiency), and business operations (tracks infrastructure costs).

The fortress stands. The moons orbit. The technology substrate clarifies.