---
id: CANON-30300
name: Technology Stack Database
identity: Technology Stack Database
tier: CANON
type: comet
version: 2.0.0
status: canonical
created: 2025-10-17
updated: 2025-12-30
synopsis: ASA Model implementation database for systematic tool classification, navigation, and workflow optimization across 447 applications, 42 AI models, and 31 APIs
chain: INTELLIGENCE
parent: CANON-30000
---

# P0-3: TECHNOLOGY STACK DATABASE
## ASA Implementation for Rational Tool Navigation

**Status**: Beta - Schema Complete, Awaiting Data Migration  
**Version**: 1.0  
**Date**: October 19, 2025  
**Dependencies**: ASA Model (Canonical), derived-taxonomy (Stable)  
**Integration Points**: Enables P0-2 (TONE LIBRARY), P1-3 (TOOLCRAFT Consolidation)

---

## PURPOSE

Transform 447 fragmentary application records, 42 AI model specifications, and 31 API pricing entries into a coherent, navigable technology intelligence system. This database implements the Anthromachina Symbiosis Architecture (ASA) Model's seven-layer Constitutional Stack and Object Ontology, enabling rational tool selection, workflow optimization, and apparatus crystallization.

**Core Problem Solved**: The current state—scattered CSV files and incomplete records—makes tool selection arbitrary and workflow design haphazard. This database creates systematic classification, relationship mapping, and navigation capabilities that transform tool chaos into architectural intelligence.

---

## SCOPE

### Included
- Complete database schema implementing ASA Model classification
- Migration protocol for Function.csv (447 apps), Models.csv (42 models), API.csv (31 pricing records)
- Navigation query specifications for capability-based search
- Primitive extraction framework for feature identification
- Apparatus detection system for workflow patterns
- Lifecycle state management (Active, Primitive Repository, Deprecated)
- Commercial seam integration from derived-taxonomy

### Excluded
- Frontend user interface (specification only, not implementation)
- Automated data collection/scraping systems
- Real-time pricing updates (manual refresh protocol)
- Community contribution system (future enhancement)

### Limitations
- Classification accuracy depends on description quality
- Apparatus detection requires usage data not yet collected
- Primitive extraction will be incomplete initially
- Commercial relationships may change faster than database updates

---

## THEORETICAL FOUNDATION

### ASA Model Integration

The database structure mirrors the ASA Model's core architecture:

**Seven-Layer Constitutional Stack** (L0-L6):
- **L0 Physical Substrate**: Hardware, silicon, energy (GPUs, TPUs, power requirements)
- **L1 Transduction Interface**: Sensors, actuators, signal conversion
- **L2 Perceptual Surface**: UI/UX, visual design, sensory presentation
- **L3 Interaction Grammar**: Input methods, gestures, commands
- **L4 Choreographic Flows**: Workflow orchestration, state management
- **L5 Cognitive Convergence**: AI models, RAG systems, reasoning
- **L6 Agentic Emergence**: Autonomous agents, multi-agent systems

**Object Ontology** (primary types):
- **O.FN**: Function objects (stateless transformations)
- **O.SVC**: Service objects (stateful, persistent)
- **O.WF**: Workflow objects (multi-step orchestration)
- **O.AGT**: Agent objects (autonomous, goal-directed)
- **O.MOD**: Model objects (trained intelligence)
- **O.DP**: Data product objects (governed datasets)
- **O.SRF**: Surface objects (presentation/display)
- **O.SNS**: Sensor objects (environmental perception)
- **O.ACT**: Actuator objects (physical manipulation)
- **O.GRD**: Guard objects (policy enforcement)

**Commercial Seams** (from derived-taxonomy):
- API Routers & Multi-Model Orchestrators
- Vector DBs & Retrieval Infrastructure (sticky)
- Inference Engines & Optimizers
- Observability / Eval / Alignment systems
- Model Marketplaces & Hubs
- Edge Runtimes & On-device Orchestration
- Security & Policy Gateways

### Geological Model Metaphor

Think of the technology stack as a **geological column**:
- **BEDROCK**: Stable taxonomies (Layers, Roles, Object Types, Modalities)
- **SETTLEMENTS**: Dynamic instances (Apps, Models, Pricing)
- **PRIMITIVES**: Extractable features (vim motions, markdown rendering, real-time sync)
- **INTELLIGENCE**: Emergent patterns (apparatus combinations, usage workflows)

This metaphor guides the schema design, separating what rarely changes (bedrock) from what evolves frequently (settlements) from what we discover through use (intelligence).

---

## DATABASE SCHEMA

### Design Principles

1. **Normalized for Integrity**: Separate stable taxonomies from volatile data
2. **Optimized for Navigation**: Indexes on all search-critical fields
3. **Extensible for Discovery**: Flexible tagging and relationship systems
4. **Queryable for Intelligence**: Support complex cross-table analytics

### Bedrock Tables (Stable Taxonomies)

```sql
-- ASA Layer Classification
CREATE TABLE layers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  code TEXT NOT NULL UNIQUE, -- L0, L1, L2, L3, L4, L5, L6
  name TEXT NOT NULL,
  description TEXT,
  domain TEXT, -- mechanics, symbols, semantics, etc.
  sequence_order INTEGER NOT NULL
);

-- Functional Roles within Layers
CREATE TABLE roles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  code TEXT NOT NULL UNIQUE, -- e.g., "capture", "process", "present"
  name TEXT NOT NULL,
  parent_role_id INTEGER REFERENCES roles(id),
  layer_id INTEGER REFERENCES layers(id),
  description TEXT
);

-- ASA Object Type Classification
CREATE TABLE object_types (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  asa_code TEXT NOT NULL UNIQUE, -- O.MOD, O.SVC, O.DP, O.FN, etc.
  name TEXT NOT NULL,
  description TEXT,
  typical_layers TEXT -- comma-separated layer codes where this type typically appears
);

-- Interaction Modalities
CREATE TABLE modalities (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  code TEXT NOT NULL UNIQUE, -- text, voice, visual, gesture, haptic
  name TEXT NOT NULL,
  description TEXT
);

-- Lifecycle States
CREATE TABLE lifecycle_states (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  code TEXT NOT NULL UNIQUE, -- active, primitive_repository, deprecated, experimental
  name TEXT NOT NULL,
  description TEXT,
  sequence_order INTEGER NOT NULL
);

-- Commercial Seams (from derived-taxonomy)
CREATE TABLE commercial_seams (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  code TEXT NOT NULL UNIQUE, -- vector_db, api_router, inference_engine, etc.
  name TEXT NOT NULL,
  description TEXT,
  lock_in_risk TEXT, -- low, medium, high
  typical_pricing_model TEXT
);

-- Deployment Contexts
CREATE TABLE deployment_contexts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  code TEXT NOT NULL UNIQUE, -- cloud, on_premise, edge, hybrid
  name TEXT NOT NULL,
  description TEXT
);
```

### Settlement Tables (Dynamic Instances)

```sql
-- Applications (447 records from Function.csv)
CREATE TABLE apps (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  slug TEXT UNIQUE, -- URL-friendly identifier
  layer_id INTEGER REFERENCES layers(id),
  role_id INTEGER REFERENCES roles(id),
  object_type_id INTEGER REFERENCES object_types(id),
  lifecycle_state_id INTEGER REFERENCES lifecycle_states(id),
  description TEXT,
  stage TEXT, -- from original Function.csv "Stage" column
  url TEXT,
  notes TEXT,
  last_reviewed DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- App Modalities (many-to-many relationship)
CREATE TABLE app_modalities (
  app_id INTEGER REFERENCES apps(id) ON DELETE CASCADE,
  modality_id INTEGER REFERENCES modalities(id),
  is_primary BOOLEAN DEFAULT FALSE,
  notes TEXT,
  PRIMARY KEY (app_id, modality_id)
);

-- App Commercial Seams (many-to-many)
CREATE TABLE app_commercial_seams (
  app_id INTEGER REFERENCES apps(id) ON DELETE CASCADE,
  seam_id INTEGER REFERENCES commercial_seams(id),
  role_in_seam TEXT, -- e.g., "provider", "consumer", "integrator"
  PRIMARY KEY (app_id, seam_id)
);

-- App Deployment Contexts
CREATE TABLE app_deployment_contexts (
  app_id INTEGER REFERENCES apps(id) ON DELETE CASCADE,
  context_id INTEGER REFERENCES deployment_contexts(id),
  is_preferred BOOLEAN DEFAULT FALSE,
  PRIMARY KEY (app_id, context_id)
);

-- AI Models (42 records from Models.csv)
CREATE TABLE models (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  slug TEXT UNIQUE,
  api_name TEXT, -- e.g., "claude-sonnet-4-20250514"
  family TEXT, -- e.g., "Claude 4", "GPT-4", "Llama"
  research_lab TEXT, -- Anthropic, OpenAI, Google, Meta, etc.
  object_type_id INTEGER REFERENCES object_types(id),
  lifecycle_state_id INTEGER REFERENCES lifecycle_states(id),
  
  -- Capability specs
  context_window INTEGER, -- in tokens
  output_token_limit INTEGER,
  training_cutoff_date DATE,
  release_date DATE,
  
  -- Feature flags
  supports_vision BOOLEAN DEFAULT FALSE,
  supports_extended_thinking BOOLEAN DEFAULT FALSE,
  supports_search BOOLEAN DEFAULT FALSE,
  
  url TEXT,
  notes TEXT,
  last_reviewed DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Model Capabilities (detailed capability tracking)
CREATE TABLE model_capabilities (
  model_id INTEGER REFERENCES models(id) ON DELETE CASCADE,
  modality_id INTEGER REFERENCES modalities(id),
  capability_description TEXT,
  PRIMARY KEY (model_id, modality_id)
);

-- API Pricing (31 records from API.csv)
CREATE TABLE api_pricing (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  model_id INTEGER REFERENCES models(id) ON DELETE CASCADE,
  api_name TEXT, -- redundant with models.api_name but for validation
  
  -- Standard pricing
  input_token_price DECIMAL(12, 9), -- USD per token
  output_token_price DECIMAL(12, 9),
  
  -- Volume pricing (>200K tokens)
  input_token_price_200k DECIMAL(12, 9),
  output_token_price_200k DECIMAL(12, 9),
  
  -- Cached input pricing
  cached_input_token_price DECIMAL(12, 9),
  
  -- Prompt caching (per 5-minute TTL)
  prompt_caching_read_price DECIMAL(12, 9),
  prompt_caching_write_price DECIMAL(12, 9),
  prompt_caching_read_price_200k DECIMAL(12, 9),
  prompt_caching_write_price_200k DECIMAL(12, 9),
  
  -- Audio pricing
  audio_input_token_price DECIMAL(12, 9),
  audio_cached_input_token_price DECIMAL(12, 9),
  audio_output_token_price DECIMAL(12, 9),
  
  -- Search pricing
  search_price_per_1000 DECIMAL(12, 6),
  
  -- Context caching storage
  context_caching_storage_price TEXT, -- may be complex pricing structure
  
  effective_date DATE,
  source_url TEXT,
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Primitive Tables (Feature Extraction)

```sql
-- Primitives (extractable features)
CREATE TABLE primitives (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  code TEXT NOT NULL UNIQUE, -- vim_motions, markdown_render, real_time_sync
  name TEXT NOT NULL,
  category TEXT, -- keybinding, rendering, collaboration, data_sync, etc.
  description TEXT,
  source_app_id INTEGER REFERENCES apps(id), -- original discoverer
  extractable BOOLEAN DEFAULT TRUE,
  abstraction_level TEXT, -- atomic, compound, workflow
  lifecycle_state_id INTEGER REFERENCES lifecycle_states(id),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- App-Primitive Relationships (which apps have which primitives)
CREATE TABLE app_primitives (
  app_id INTEGER REFERENCES apps(id) ON DELETE CASCADE,
  primitive_id INTEGER REFERENCES primitives(id),
  implementation_quality TEXT, -- excellent, good, adequate, poor
  implementation_notes TEXT,
  discovered_date DATE,
  PRIMARY KEY (app_id, primitive_id)
);

-- Primitive Dependencies (some primitives require others)
CREATE TABLE primitive_dependencies (
  primitive_id INTEGER REFERENCES primitives(id),
  depends_on_primitive_id INTEGER REFERENCES primitives(id),
  dependency_type TEXT, -- required, optional, enhances
  PRIMARY KEY (primitive_id, depends_on_primitive_id)
);
```

### Intelligence Tables (Emergent Patterns)

```sql
-- Apparatus (workflow patterns that emerge from app combinations)
CREATE TABLE apparatus (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  code TEXT NOT NULL UNIQUE, -- writing_apparatus, research_apparatus
  name TEXT NOT NULL,
  description TEXT,
  emergence_pattern TEXT, -- how this pattern typically emerges
  frequency_score INTEGER, -- how often this pattern appears in practice
  last_detected DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Apparatus Components (which apps participate in which apparatus)
CREATE TABLE apparatus_components (
  apparatus_id INTEGER REFERENCES apparatus(id) ON DELETE CASCADE,
  app_id INTEGER REFERENCES apps(id),
  role_in_apparatus TEXT, -- capture, process, present, orchestrate
  is_core BOOLEAN DEFAULT TRUE, -- core vs optional component
  usage_notes TEXT,
  PRIMARY KEY (apparatus_id, app_id)
);

-- App Relationships (how apps relate to each other)
CREATE TABLE app_relationships (
  app_id INTEGER REFERENCES apps(id),
  related_app_id INTEGER REFERENCES apps(id),
  relationship_type TEXT, -- powers, competes, requires, obsoletes, combines_with
  strength INTEGER, -- 1-5 scale of relationship strength
  notes TEXT,
  discovered_date DATE,
  PRIMARY KEY (app_id, related_app_id),
  CHECK (app_id != related_app_id)
);

-- Usage Contexts (real-world usage patterns)
CREATE TABLE usage_contexts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  code TEXT NOT NULL UNIQUE, -- mobile_capture, deep_analysis, rapid_synthesis
  name TEXT NOT NULL,
  description TEXT,
  spatial_context TEXT, -- ambulatory, fixed, situated
  attentional_state TEXT, -- divided, focused, immersive
  temporal_dynamic TEXT, -- reactive, deliberative, persistent
  social_setting TEXT, -- solitary, intimate, collaborative, public
);

-- App Usage Contexts (which apps work well in which contexts)
CREATE TABLE app_usage_contexts (
  app_id INTEGER REFERENCES apps(id),
  context_id INTEGER REFERENCES usage_contexts(id),
  effectiveness_score INTEGER, -- 1-5 scale
  notes TEXT,
  PRIMARY KEY (app_id, context_id)
);

-- Workflow Templates (captured workflows using multiple apps)
CREATE TABLE workflow_templates (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  code TEXT NOT NULL UNIQUE,
  name TEXT NOT NULL,
  description TEXT,
  apparatus_id INTEGER REFERENCES apparatus(id), -- which apparatus this workflow belongs to
  use_frequency TEXT, -- daily, weekly, monthly, occasional
  average_duration_minutes INTEGER,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Workflow Steps (sequential steps in a workflow)
CREATE TABLE workflow_steps (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  workflow_id INTEGER REFERENCES workflow_templates(id) ON DELETE CASCADE,
  step_number INTEGER NOT NULL,
  app_id INTEGER REFERENCES apps(id),
  action_description TEXT,
  input_from_previous_step TEXT,
  output_to_next_step TEXT,
  average_duration_minutes INTEGER,
  notes TEXT,
  UNIQUE (workflow_id, step_number)
);
```

### Indexes for Navigation Performance

```sql
-- App search indexes
CREATE INDEX idx_apps_name ON apps(name);
CREATE INDEX idx_apps_slug ON apps(slug);
CREATE INDEX idx_apps_layer ON apps(layer_id);
CREATE INDEX idx_apps_role ON apps(role_id);
CREATE INDEX idx_apps_object_type ON apps(object_type_id);
CREATE INDEX idx_apps_lifecycle ON apps(lifecycle_state_id);
CREATE INDEX idx_apps_stage ON apps(stage);

-- Model search indexes
CREATE INDEX idx_models_name ON models(name);
CREATE INDEX idx_models_api_name ON models(api_name);
CREATE INDEX idx_models_family ON models(family);
CREATE INDEX idx_models_lab ON models(research_lab);

-- Primitive search indexes
CREATE INDEX idx_primitives_code ON primitives(code);
CREATE INDEX idx_primitives_category ON primitives(category);
CREATE INDEX idx_primitives_extractable ON primitives(extractable);

-- Apparatus search indexes
CREATE INDEX idx_apparatus_code ON apparatus(code);
CREATE INDEX idx_apparatus_frequency ON apparatus(frequency_score);

-- Relationship search indexes
CREATE INDEX idx_app_relationships_type ON app_relationships(relationship_type);
CREATE INDEX idx_app_primitives_quality ON app_primitives(implementation_quality);
```

---

## MIGRATION PROTOCOL

### Phase 1: Schema Creation (30 minutes)

1. **Execute schema SQL** in SQLite or PostgreSQL
2. **Verify table creation** with schema inspection queries
3. **Test foreign key constraints** with sample inserts
4. **Create backup protocol** for rollback capability

### Phase 2: Bedrock Population (1 hour)

#### 2.1 Layers Table
```sql
INSERT INTO layers (code, name, description, domain, sequence_order) VALUES
('L0', 'Physical Substrate', 'Material and energetic foundation: silicon, memory, cooling, power', 'mechanics', 0),
('L1', 'Transduction Interface', 'Bidirectional conversion: sensors, actuators, signal processing', 'mechanics', 1),
('L2', 'Perceptual Surface', 'Sensory presentation: visual, auditory, haptic design optimized for humans', 'symbols', 2),
('L3', 'Interaction Grammar', 'Structured actions and communications: gestures, language, multimodal input', 'symbols', 3),
('L4', 'Choreographic Flows', 'Temporal architecture: navigation, state, synchronization, error recovery', 'semantics', 4),
('L5', 'Cognitive Convergence', 'Hybrid reasoning: augmentation, collaboration, personalization, knowledge synthesis', 'semantics', 5),
('L6', 'Agentic Emergence', 'Autonomous operation: planning, coordination, value alignment, oversight', 'agency', 6);
```

#### 2.2 Object Types Table
```sql
INSERT INTO object_types (asa_code, name, description, typical_layers) VALUES
('O.FN', 'Function Objects', 'Stateless computational units performing specific transformations', 'L4,L5'),
('O.SVC', 'Service Objects', 'Stateful processes providing ongoing capabilities', 'L4,L5,L6'),
('O.WF', 'Workflow Objects', 'Orchestrated multi-step processes', 'L4'),
('O.AGT', 'Agent Objects', 'Goal-directed autonomous systems with adaptive behavior', 'L6'),
('O.MOD', 'Model Objects', 'Trained intelligence: prediction, generation, reasoning', 'L5'),
('O.DP', 'Data Product Objects', 'Governed, versioned datasets', 'L4,L5'),
('O.STM', 'Stream Objects', 'Continuous data flows for real-time updates', 'L4'),
('O.ARC', 'Archive Objects', 'Long-term information preservation', 'L4'),
('O.SRF', 'Surface Objects', 'Presentation and display components', 'L2,L3'),
('O.SNS', 'Sensor Objects', 'Environmental perception and data capture', 'L1'),
('O.ACT', 'Actuator Objects', 'Physical manipulation and feedback', 'L1'),
('O.INS', 'Instrument Objects', 'High-fidelity human control mechanisms', 'L3'),
('O.GRD', 'Guard Objects', 'Policy enforcement and safety mechanisms', 'L5,L6'),
('O.EVL', 'Evaluator Objects', 'Quality assessment and performance measurement', 'L5,L6'),
('O.CPL', 'Copilot Objects', 'Human-AI collaborative interface components', 'L5');
```

#### 2.3 Commercial Seams Table
```sql
INSERT INTO commercial_seams (code, name, description, lock_in_risk, typical_pricing_model) VALUES
('vector_db', 'Vector Database / Retrieval', 'Embedding storage and similarity search (Pinecone, Weaviate, Chroma)', 'high', 'per-query + storage'),
('api_router', 'API Router / Multi-Model Orchestrator', 'Unified model access (OpenRouter, Perplexity)', 'medium', 'per-request markup'),
('inference_engine', 'Inference Engine / Optimizer', 'Model serving optimization (fal.ai, Triton, DeepSpeed)', 'medium', 'compute time'),
('observability', 'Observability / Eval / Alignment', 'Monitoring and quality assurance (Helicone, Langfuse)', 'low', 'SaaS subscription'),
('model_marketplace', 'Model Marketplace / Hub', 'Weight hosting and discovery (Hugging Face, Replicate)', 'medium', 'marketplace fee'),
('edge_runtime', 'Edge Runtime / On-device', 'Local model execution (CoreML, TFLite, Ollama)', 'low', 'SDK licensing'),
('security_gateway', 'Security / Policy Gateway', 'Data masking, PII scrubbing, safety filters', 'medium', 'SaaS or self-hosted');
```

#### 2.4 Modalities Table
```sql
INSERT INTO modalities (code, name, description) VALUES
('text', 'Text', 'Written language input and output'),
('voice', 'Voice', 'Speech input and synthesis'),
('visual', 'Visual', 'Image and video processing'),
('gesture', 'Gesture', 'Physical movement and spatial input'),
('haptic', 'Haptic', 'Touch and force feedback');
```

#### 2.5 Lifecycle States Table
```sql
INSERT INTO lifecycle_states (code, name, description, sequence_order) VALUES
('experimental', 'Experimental', 'Testing phase, not production-ready', 1),
('active', 'Active', 'Currently in regular use', 2),
('primitive_repository', 'Primitive Repository', 'No longer primary tool, but features worth extracting', 3),
('deprecated', 'Deprecated', 'Discontinued, replaced by alternatives', 4),
('archived', 'Archived', 'Historical record only', 5);
```

### Phase 3: Settlement Migration (2-3 hours)

#### 3.1 Apps Migration from Function.csv
```python
import csv
import sqlite3

# Mapping functions (to be refined during actual migration)
def map_layer_from_description(layer_text):
    """Map Function.csv 'Layer' column to layer_id"""
    layer_map = {
        'Physical': 'L0',
        'Transduction': 'L1',
        'Perceptual': 'L2',
        'Interaction': 'L3',
        'Choreographic': 'L4',
        'Cognitive': 'L5',
        'Agentic': 'L6'
    }
    # Fuzzy match logic here
    pass

def map_object_type_from_description(description_text):
    """Infer object type from description keywords"""
    # Keywords: service, model, workflow, agent, etc.
    pass

def map_role_from_text(role_text):
    """Map Function.csv 'Role' to role_id"""
    # Create roles dynamically or match to predefined set
    pass

# Migration script
with open('Function.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        app_data = {
            'name': row['Application'],
            'description': row['Description'],
            'layer_id': map_layer_from_description(row['Layer']),
            'role_id': map_role_from_text(row['Role']),
            'object_type_id': map_object_type_from_description(row['Description']),
            'stage': row['Stage'],
            # Set lifecycle_state_id based on Stage or manual review
            'lifecycle_state_id': determine_lifecycle_state(row['Stage'])
        }
        # INSERT into apps table
```

**Manual Review Required**:
- Classify each app's object type (O.SVC, O.FN, O.WF, etc.)
- Determine lifecycle state (active, primitive_repository, etc.)
- Extract URL from notes or descriptions where available
- Identify commercial seam participation

#### 3.2 Models Migration from Models.csv
```python
with open('Models.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        model_data = {
            'name': row['Name'],
            'api_name': row['API'],
            'family': row['Family'],
            'research_lab': row['Research Lab'],
            'context_window': parse_context_window(row['Context Window']),
            'output_token_limit': parse_output_limit(row['Output Token Limit']),
            'training_cutoff_date': parse_date(row['Training Cutoff Data']),
            'release_date': parse_date(row['Release  ']),
            'supports_vision': parse_bool(row['Vision']),
            'supports_extended_thinking': parse_bool(row['Extended Thinking']),
            'supports_search': parse_bool(row['Search']),
            'object_type_id': get_object_type_id('O.MOD')
        }
        # INSERT into models table
```

#### 3.3 API Pricing Migration from API.csv
```python
with open('API.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        pricing_data = {
            'model_id': lookup_model_id(row['model']),
            'api_name': row['api_name'],
            'input_token_price': parse_price(row['input_token_pricing']),
            'output_token_price': parse_price(row['output_token_pricing']),
            # ... all other pricing fields
            'effective_date': datetime.now()
        }
        # INSERT into api_pricing table
```

### Phase 4: Primitive Extraction (3-4 hours)

**Systematic Extraction Process**:

1. **Read all app descriptions** and identify recurring feature mentions
2. **Create primitive categories**:
   - Keybindings: vim motions, emacs commands, custom shortcuts
   - Rendering: markdown, LaTeX, syntax highlighting, diagrams
   - Collaboration: real-time sync, conflict resolution, presence awareness
   - Data Sync: bidirectional sync, offline-first, version control
   - Search: full-text, semantic, fuzzy matching
   - Organization: tags, hierarchies, links, databases
   - Integration: API access, webhooks, automation
   - Export: formats, quality, metadata preservation

3. **Populate primitives table** with discovered features
4. **Link apps to primitives** via app_primitives table
5. **Identify primitive dependencies** (e.g., real-time sync requires conflict resolution)

**Initial Primitive Set** (to be expanded):
```sql
INSERT INTO primitives (code, name, category, description, extractable) VALUES
('vim_motions', 'Vim-style Navigation', 'keybinding', 'Modal editing with hjkl navigation and text objects', TRUE),
('markdown_render', 'Markdown Rendering', 'rendering', 'Live preview of markdown with formatting', TRUE),
('real_time_sync', 'Real-time Synchronization', 'collaboration', 'Instant updates across devices/users', TRUE),
('offline_first', 'Offline-first Architecture', 'data_sync', 'Full functionality without internet connection', TRUE),
('bi_directional_sync', 'Bidirectional Sync', 'data_sync', 'Two-way synchronization preserving local changes', TRUE),
('full_text_search', 'Full-text Search', 'search', 'Search across all content with relevance ranking', TRUE),
('tag_system', 'Flexible Tagging', 'organization', 'Arbitrary tags for classification', TRUE),
('link_system', 'Bidirectional Links', 'organization', 'Wikilink-style connections between notes', TRUE),
('api_access', 'API Access', 'integration', 'Programmatic access to data and functions', TRUE),
('webhook_support', 'Webhook Integration', 'integration', 'Event-driven automation triggers', TRUE);
```

### Phase 5: Apparatus Detection (2-3 hours)

**Initial Apparatus Patterns** (to be validated with usage data):

```sql
INSERT INTO apparatus (code, name, description, emergence_pattern, frequency_score) VALUES
('writing_apparatus', 'Writing & Publishing Workflow', 'Capture → Draft → Edit → Publish across multiple platforms', 'emerges naturally from need for systematic content production', 5),
('research_apparatus', 'Research & Synthesis Workflow', 'Collect → Annotate → Connect → Synthesize → Document', 'emerges from knowledge work and learning projects', 5),
('coding_apparatus', 'Software Development Workflow', 'Edit → Test → Debug → Deploy → Monitor', 'standard in software development', 5),
('design_apparatus', 'Design & Creation Workflow', 'Ideate → Sketch → Prototype → Refine → Export', 'emerges in creative work', 4),
('analysis_apparatus', 'Data Analysis Workflow', 'Import → Clean → Transform → Visualize → Report', 'emerges in data-driven work', 4),
('communication_apparatus', 'Communication & Collaboration', 'Schedule → Meet → Document → Follow-up → Archive', 'standard in team work', 5);
```

**Component Linking**:
- Identify which apps from the 447 participate in each apparatus
- Document their roles (capture, process, present, orchestrate)
- Note core vs optional components

### Phase 6: Validation & Quality Assurance (1-2 hours)

**Data Integrity Checks**:
```sql
-- Orphaned records (foreign key violations)
SELECT * FROM apps WHERE layer_id NOT IN (SELECT id FROM layers);
SELECT * FROM apps WHERE object_type_id NOT IN (SELECT id FROM object_types);

-- Missing critical data
SELECT * FROM apps WHERE name IS NULL OR name = '';
SELECT * FROM models WHERE api_name IS NULL;

-- Duplicate detection
SELECT name, COUNT(*) FROM apps GROUP BY name HAVING COUNT(*) > 1;
SELECT api_name, COUNT(*) FROM models GROUP BY api_name HAVING COUNT(*) > 1;

-- Classification coverage
SELECT 
  COUNT(*) as total_apps,
  SUM(CASE WHEN layer_id IS NULL THEN 1 ELSE 0 END) as missing_layer,
  SUM(CASE WHEN object_type_id IS NULL THEN 1 ELSE 0 END) as missing_object_type
FROM apps;
```

**Quality Metrics**:
- Apps classified: __/447 (100%)
- Models complete: __/42 (100%)
- Pricing records: __/31 (100%)
- Primitives extracted: __/50+ (initial target)
- Apparatus defined: 6+ (expandable)
- Relationships mapped: __/200+ (initial target)

---

## NAVIGATION SPECIFICATIONS

### Query Interface Requirements

The database must support these navigation patterns:

#### 1. Capability-Based Search
"What apps can [perform specific function]?"

```sql
-- Example: Find apps that can edit PDFs
SELECT a.name, a.description, l.name as layer, ot.name as object_type
FROM apps a
JOIN layers l ON a.layer_id = l.id
JOIN object_types ot ON a.object_type_id = ot.id
WHERE a.description LIKE '%PDF%'
  AND a.description LIKE '%edit%'
  AND a.lifecycle_state_id = (SELECT id FROM lifecycle_states WHERE code = 'active');
```

#### 2. Context-Aware Routing
"Quick capture tool for mobile?"

```sql
-- Find apps suitable for mobile capture context
SELECT a.name, a.description, r.name as role
FROM apps a
JOIN app_usage_contexts auc ON a.id = auc.app_id
JOIN usage_contexts uc ON auc.context_id = uc.id
JOIN roles r ON a.role_id = r.id
WHERE uc.spatial_context = 'ambulatory'
  AND r.code = 'capture'
  AND auc.effectiveness_score >= 4
ORDER BY auc.effectiveness_score DESC;
```

#### 3. Primitive-Based Filtering
"What apps have vim motions?"

```sql
-- Find apps implementing specific primitive
SELECT a.name, ap.implementation_quality, ap.implementation_notes
FROM apps a
JOIN app_primitives ap ON a.id = ap.app_id
JOIN primitives p ON ap.primitive_id = p.id
WHERE p.code = 'vim_motions'
  AND ap.implementation_quality IN ('excellent', 'good')
ORDER BY ap.implementation_quality DESC;
```

#### 4. Apparatus Discovery
"Show me the writing workflow"

```sql
-- Retrieve apparatus components and roles
SELECT 
  a.name as app_name,
  ac.role_in_apparatus,
  ac.is_core,
  l.name as layer,
  ac.usage_notes
FROM apparatus ap
JOIN apparatus_components ac ON ap.id = ac.apparatus_id
JOIN apps a ON ac.app_id = a.id
JOIN layers l ON a.layer_id = l.id
WHERE ap.code = 'writing_apparatus'
ORDER BY 
  CASE ac.role_in_apparatus
    WHEN 'capture' THEN 1
    WHEN 'process' THEN 2
    WHEN 'present' THEN 3
    WHEN 'orchestrate' THEN 4
  END;
```

#### 5. Cost Optimization
"Cheapest model for long-context reasoning?"

```sql
-- Find most cost-effective model for specific use case
SELECT 
  m.name,
  m.api_name,
  m.context_window,
  ap.input_token_price,
  ap.output_token_price,
  (ap.input_token_price * 100000 + ap.output_token_price * 1000) as cost_per_100k_in_1k_out
FROM models m
JOIN api_pricing ap ON m.id = ap.model_id
WHERE m.context_window >= 200000
  AND m.lifecycle_state_id = (SELECT id FROM lifecycle_states WHERE code = 'active')
ORDER BY cost_per_100k_in_1k_out ASC
LIMIT 5;
```

#### 6. Relationship Navigation
"What apps compete with Notion?"

```sql
-- Find competing or alternative apps
SELECT 
  related_app.name,
  ar.relationship_type,
  ar.strength,
  ar.notes
FROM apps a
JOIN app_relationships ar ON a.id = ar.app_id
JOIN apps related_app ON ar.related_app_id = related_app.id
WHERE a.name = 'Notion'
  AND ar.relationship_type IN ('competes', 'obsoletes')
ORDER BY ar.strength DESC;
```

#### 7. Workflow Suggestion
"How do people typically use Obsidian?"

```sql
-- Find workflow templates involving specific app
SELECT 
  wt.name as workflow_name,
  wt.description,
  ws.step_number,
  ws.action_description,
  a_step.name as tool_used
FROM apps a
JOIN workflow_steps ws ON a.id = ws.app_id
JOIN workflow_templates wt ON ws.workflow_id = wt.id
JOIN apps a_step ON ws.app_id = a_step.id
WHERE a.name = 'Obsidian'
ORDER BY wt.use_frequency DESC, ws.step_number ASC;
```

---

## INTERFACE MOCKUPS

### Command-Line Interface

```bash
# Basic search
$ techstack search "markdown editor"
Found 12 apps matching "markdown editor":

1. Obsidian (L3: Interaction Grammar, O.SRF)
   Lifecycle: Active | Primitives: markdown_render, vim_motions, link_system
   Layer: Perceptual Surface | Role: content_editing

2. Typora (L3: Interaction Grammar, O.SRF)
   Lifecycle: Active | Primitives: markdown_render, export_pdf
   Layer: Perceptual Surface | Role: content_editing

# Context-based navigation
$ techstack find --context ambulatory --role capture
Recommended for mobile capture:

1. Drafts (effectiveness: 5/5)
   Quick text capture with automation
   
2. Apple Notes (effectiveness: 4/5)
   Native iOS integration, reliable sync

# Primitive search
$ techstack primitives vim_motions
Apps with vim motions:

- Obsidian (excellent)
- Neovim (excellent)
- VSCode with Vim extension (good)
- Notion with Vim extension (adequate)

# Apparatus view
$ techstack apparatus writing
Writing & Publishing Apparatus:

[Capture] → [Process] → [Present] → [Orchestrate]

Capture:
  - Drafts (core)
  - Apple Notes (optional)
  
Process:
  - Obsidian (core)
  - VSCode (optional)
  
Present:
  - Ghost (core)
  - Medium (optional)
  
Orchestrate:
  - Zapier (core)

# Model comparison
$ techstack models compare --context-window 200000 --sort-by price
Long-context models (200K+ tokens), sorted by cost:

1. Claude Haiku 4 ($0.25 per 100K in + 1K out)
2. GPT-4o mini ($0.35 per 100K in + 1K out)
3. Claude Sonnet 4.5 ($0.80 per 100K in + 1K out)
```

### Web Interface (specification)

**Dashboard View**:
- Total apps: 447 (classify by layer, lifecycle state)
- Models tracked: 42 (by research lab, capability)
- Apparatus defined: 6 (with usage frequency)
- Primitives cataloged: 50+ (by category)

**Search View**:
- Multi-faceted search: by name, description, layer, role, primitive, context
- Filter sidebar: lifecycle state, object type, commercial seam
- Sort options: alphabetical, by layer, by usage frequency

**App Detail View**:
- Classification: Layer, Role, Object Type, Lifecycle State
- Description: Full text with links
- Primitives: List with quality ratings
- Relationships: Competing apps, requires apps, combines with
- Apparatus: Which workflows include this app
- Commercial: Pricing model, lock-in risk, vendor
- Links: Official URL, documentation

**Apparatus View**:
- Visual workflow diagram: Capture → Process → Present → Orchestrate
- Component list: Apps in each role with core/optional designation
- Alternative paths: Different tool combinations for same apparatus
- Estimated setup time and complexity

**Model Comparison View**:
- Side-by-side: Context window, capabilities, pricing
- Cost calculator: Input/output token estimate → total cost
- Capability matrix: Vision, extended thinking, search, modalities
- Recommendations: Best for specific use cases

---

## MAINTENANCE PROTOCOLS

### Regular Updates (Weekly/Monthly)

**Weekly Tasks**:
1. Check for new model releases from major labs
2. Update API pricing if changes announced
3. Review and add new apps discovered in use
4. Update lifecycle states for deprecated tools

**Monthly Tasks**:
1. Systematic primitive extraction from newly added apps
2. Apparatus pattern validation through usage review
3. Relationship mapping updates based on new integrations
4. Cost optimization analysis with updated pricing

**Quarterly Tasks**:
1. Comprehensive data quality audit
2. Classification review and refinement
3. Commercial seam landscape assessment
4. Strategic tool stack analysis and recommendations

### Data Collection Workflows

**New App Addition**:
1. Capture: Name, description, URL, discovery context
2. Classify: Layer, role, object type (may require research)
3. Extract: Identify primitives from features list
4. Relate: Map relationships to existing apps
5. Contextualize: Determine optimal usage contexts
6. Lifecycle: Set initial state (experimental, active)

**Model Tracking**:
1. Monitor: AI research lab announcements
2. Capture: Technical specs, capabilities, release date
3. Pricing: Extract from official API documentation
4. Classify: Family, modalities, context capabilities
5. Benchmark: Compare to existing models
6. Recommend: Update model selection guidance

### Quality Assurance

**Classification Accuracy**:
- Periodic review of layer assignments
- Object type validation through usage observation
- Role refinement based on actual functionality

**Completeness Checks**:
- Missing descriptions flagged for update
- Apps without primitives identified for extraction
- Apparatus without sufficient components reviewed

**Relationship Validation**:
- "Competes" relationships verified through feature comparison
- "Requires" dependencies tested in actual workflows
- "Combines" patterns validated through usage

---

## SUCCESS CRITERIA

### Quantitative Metrics

- **Migration Completeness**: 100% of CSV data successfully transferred
- **Classification Coverage**: 100% of apps have layer, role, object type assigned
- **Primitive Extraction**: 50+ primitives cataloged across 10+ categories
- **Apparatus Definition**: 6+ apparatus with comprehensive component mapping
- **Relationship Density**: 200+ app relationships documented
- **Navigation Speed**: Query response < 100ms for standard searches
- **Data Integrity**: Zero foreign key violations, zero duplicate records

### Qualitative Metrics

- **Rational Tool Selection**: Can answer "What should I use for X?" systematically
- **Context Awareness**: Recommendations appropriate for spatial/temporal/cognitive contexts
- **Workflow Intelligence**: Can suggest complete apparatus for common tasks
- **Cost Optimization**: Can identify most economical tools for specific requirements
- **Evolution Tracking**: Lifecycle states accurately reflect tool maturity and adoption

### Validation Tests

#### Test 1: Capability-Based Search
**Query**: "What can I use for quick text capture on mobile?"
**Expected**: List of 3-5 apps with capture role, ambulatory context, high effectiveness scores

#### Test 2: Primitive Discovery
**Query**: "Which writing apps have vim motions?"
**Expected**: Accurate list with quality ratings, ordered by implementation quality

#### Test 3: Cost Optimization
**Query**: "Cheapest model for 150K context reasoning tasks?"
**Expected**: Ranked list of models with pricing per 100K tokens, context window >= 150K

#### Test 4: Apparatus Navigation
**Query**: "Show me a complete research workflow"
**Expected**: Research apparatus with capture → annotate → connect → synthesize steps, apps for each

#### Test 5: Relationship Intelligence
**Query**: "What are alternatives to Roam Research?"
**Expected**: Apps with "competes" relationship, similar primitives (bidirectional links, graph view)

---

## INTEGRATION POINTS

### P0-2: TONE LIBRARY
- **Shared**: Tool selection for content production (editors, publishing platforms)
- **Flow**: TONE LIBRARY Recipes → content platform selection → query database for best tool
- **Example**: Recipe requires "long-form writing with rich media" → database suggests Medium, Substack, Ghost

### P1-3: TOOLCRAFT Consolidation
- **Shared**: Apparatus patterns, workflow typologies
- **Flow**: TOOLCRAFT concepts → database structure for capturing workflows
- **Integration**: Dissolve TOOLCRAFT into database as workflow_templates and usage_contexts tables

### Rhetorical Calibration (P0-1)
- **Shared**: Platform taxonomy (X, LinkedIn, Medium, etc.)
- **Flow**: Rhetorical platform priorities → database records for publishing apps
- **Example**: "X/Twitter" voice → identify Twitter clients and scheduling tools in database

### Business Operations (P0-5)
- **Shared**: Tool costs, infrastructure requirements
- **Flow**: Operations backbone → query database for pricing and deployment context
- **Example**: Budget constraints → cost optimization queries for AI models and services

---

## LIMITATIONS & HONEST ACKNOWLEDGMENTS

### Known Gaps

1. **Classification Subjectivity**: Layer and object type assignments require judgment; edge cases will exist
2. **Primitive Extraction Incompleteness**: Initial primitive catalog will miss nuances; continuous discovery needed
3. **Apparatus Patterns**: Initially theoretical; require real-world validation through usage tracking
4. **Commercial Data Volatility**: Pricing and vendor relationships change faster than manual updates can track
5. **Usage Context Data**: Effectiveness scores based on estimates; need empirical validation through user feedback

### Falsification Criteria

This system fails if:
- Tool recommendations don't match actual usage patterns after 3 months
- Classification changes > 20% in first 6 months (indicates unstable taxonomy)
- Users consistently bypass database search for tool selection (indicates poor utility)
- Maintenance burden exceeds 4 hours/week (indicates unsustainable complexity)
- Cost optimization recommendations prove inaccurate > 30% of the time

### Risks & Mitigation

**Risk**: Classification paralysis (too much time on perfect categorization)
**Mitigation**: Use "good enough" heuristics, iterate based on actual queries

**Risk**: Stale data (apps update faster than database)
**Mitigation**: Automated scraping where possible, community contribution system (future)

**Risk**: Apparatus patterns don't reflect actual workflows
**Mitigation**: Usage tracking integration (future), user-submitted workflows

**Risk**: Maintenance burden becomes unsustainable
**Mitigation**: Focus on high-value apps (top 100 by usage), automate updates where possible

---

## NEXT STEPS

### Immediate Actions (This Session)

1. ✅ **Schema Complete**: Database structure documented
2. ✅ **Migration Protocol Specified**: Steps for populating from CSVs
3. ⏭️ **Bedrock Population**: Execute taxonomy insert statements (30 min)
4. ⏭️ **CSV Access**: Obtain Function.csv, Models.csv, API.csv files
5. ⏭️ **Migration Execution**: Run import scripts with validation (2-3 hours)

### Week 1 Tasks

1. Complete all Settlement migrations (apps, models, pricing)
2. Begin primitive extraction (target: 30 primitives)
3. Define initial apparatus (6 patterns with components)
4. Build basic CLI for navigation testing
5. Validate with 10 real-world queries

### Week 2-4 Tasks

1. Expand primitive catalog to 50+
2. Add relationship mapping (200+ relationships)
3. Populate usage contexts with effectiveness scores
4. Create workflow templates (10+ documented workflows)
5. Build web interface dashboard

### Month 2-3 Tasks

1. Integrate with P0-2 (TONE LIBRARY tool selection)
2. Consolidate TOOLCRAFT insights into database
3. Add automated data collection where possible
4. Community contribution system design
5. Usage analytics integration

---

## MAINTENANCE LOG

### Version 1.0 (October 19, 2025)
- Initial schema design based on ASA Model and derived-taxonomy
- Complete database structure with all tables and relationships
- Migration protocol specified for Function.csv, Models.csv, API.csv
- Navigation specifications for 7 query patterns
- Interface mockups for CLI and web dashboard
- Integration points with P0-2, P1-3, P0-1, P0-5 documented

---

## FOUNDER ASSESSMENT

**Quality Evaluation**: [Pending - needs founder review]

**Production Readiness**: Schema is production-ready; migration requires CSV access and execution

**Embodiment Testing**: Cannot test until data populated; CLI queries designed for validation

**Integration Verification**: Conceptually integrated with P0-2 (TONE LIBRARY), P1-3 (TOOLCRAFT)

**Falsification Results**: [Pending - requires 3-month usage period]

**Evolution Needs**: [To be documented after initial deployment and testing]

---

*End P0-3 Artifact*

**Database Ready for Population**  
**Migration Protocol Specified**  
**Navigation Capabilities Defined**  
**Awaiting CSV Data Access and Execution Approval**
