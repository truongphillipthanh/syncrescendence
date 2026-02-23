#!/usr/bin/env python3
"""
build_ontology_db.py — PROJ-006b Ontology Substrate Pilot
Implements CANON-30300 Tech Stack Database schema + operational tables.
Populates bedrock seed data and migrates all CSV ledgers.

Usage:
    python3 build_ontology_db.py [--db-path PATH] [--repo-root PATH]

Output: SQLite database at ~/.syncrescendence/ontology.db (default)
"""

import csv
import os
import sqlite3
import sys
from datetime import datetime
from pathlib import Path

# --- Configuration ---

DEFAULT_DB_PATH = os.path.expanduser("~/.syncrescendence/ontology.db")
DEFAULT_REPO_ROOT = os.path.expanduser("~/Desktop/syncrescendence")

# CSV locations relative to repo root
CSV_PATHS = {
    "projects": "orchestration/state/DYN-PROJECTS.csv",
    "tasks": "orchestration/state/DYN-TASKS.csv",
    "accounts": "engine/DYN-ACCOUNTS.csv",
    "platforms": "engine/DYN-PLATFORMS.csv",
    "roles": "engine/DYN-ROLES.csv",
    "sources": "sources/DYN-SOURCES.csv",
    "filename_mapping": "sources/REF-FILENAME_MAPPING.csv",
    "rename_mapping": "sources/REF-RENAME_MAPPING.csv",
    "functions": "orchestration/state/DYN-FUNCTIONS.csv",
    "models": "orchestration/state/DYN-MODELS.csv",
    "api_pricing": "orchestration/state/DYN-API_PRICING.csv",
}


# --- Schema: CANON-30300 Tech Stack Database (4 geological layers) ---

SCHEMA_BEDROCK = """
-- ============================================================
-- BEDROCK TABLES — Stable Taxonomies (rarely change)
-- ============================================================

-- ASA Layer Classification (L0-L6)
CREATE TABLE IF NOT EXISTS layers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    description TEXT,
    domain TEXT,
    sequence_order INTEGER NOT NULL
);

-- Functional Roles within Layers
CREATE TABLE IF NOT EXISTS roles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    parent_role_id INTEGER REFERENCES roles(id),
    layer_id INTEGER REFERENCES layers(id),
    description TEXT
);

-- ASA Object Type Classification
CREATE TABLE IF NOT EXISTS object_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    asa_code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    description TEXT,
    typical_layers TEXT
);

-- Interaction Modalities
CREATE TABLE IF NOT EXISTS modalities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    description TEXT
);

-- Lifecycle States
CREATE TABLE IF NOT EXISTS lifecycle_states (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    description TEXT,
    sequence_order INTEGER NOT NULL
);

-- Commercial Seams (from derived-taxonomy)
CREATE TABLE IF NOT EXISTS commercial_seams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    description TEXT,
    lock_in_risk TEXT,
    typical_pricing_model TEXT
);

-- Deployment Contexts
CREATE TABLE IF NOT EXISTS deployment_contexts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    description TEXT
);
"""

SCHEMA_SETTLEMENTS = """
-- ============================================================
-- SETTLEMENT TABLES — Dynamic Instances (evolve frequently)
-- ============================================================

-- Applications (from Function.csv / DYN-PLATFORMS.csv)
CREATE TABLE IF NOT EXISTS apps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    slug TEXT UNIQUE,
    layer_id INTEGER REFERENCES layers(id),
    role_id INTEGER REFERENCES roles(id),
    object_type_id INTEGER REFERENCES object_types(id),
    lifecycle_state_id INTEGER REFERENCES lifecycle_states(id),
    description TEXT,
    stage TEXT,
    url TEXT,
    notes TEXT,
    last_reviewed DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- App Modalities (many-to-many)
CREATE TABLE IF NOT EXISTS app_modalities (
    app_id INTEGER REFERENCES apps(id) ON DELETE CASCADE,
    modality_id INTEGER REFERENCES modalities(id),
    is_primary BOOLEAN DEFAULT FALSE,
    notes TEXT,
    PRIMARY KEY (app_id, modality_id)
);

-- App Commercial Seams (many-to-many)
CREATE TABLE IF NOT EXISTS app_commercial_seams (
    app_id INTEGER REFERENCES apps(id) ON DELETE CASCADE,
    seam_id INTEGER REFERENCES commercial_seams(id),
    role_in_seam TEXT,
    PRIMARY KEY (app_id, seam_id)
);

-- App Deployment Contexts
CREATE TABLE IF NOT EXISTS app_deployment_contexts (
    app_id INTEGER REFERENCES apps(id) ON DELETE CASCADE,
    context_id INTEGER REFERENCES deployment_contexts(id),
    is_preferred BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (app_id, context_id)
);

-- AI Models
CREATE TABLE IF NOT EXISTS models (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    slug TEXT UNIQUE,
    api_name TEXT,
    family TEXT,
    research_lab TEXT,
    object_type_id INTEGER REFERENCES object_types(id),
    lifecycle_state_id INTEGER REFERENCES lifecycle_states(id),
    context_window INTEGER,
    output_token_limit INTEGER,
    training_cutoff_date DATE,
    release_date DATE,
    supports_vision BOOLEAN DEFAULT FALSE,
    supports_extended_thinking BOOLEAN DEFAULT FALSE,
    supports_search BOOLEAN DEFAULT FALSE,
    url TEXT,
    notes TEXT,
    last_reviewed DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Model Capabilities
CREATE TABLE IF NOT EXISTS model_capabilities (
    model_id INTEGER REFERENCES models(id) ON DELETE CASCADE,
    modality_id INTEGER REFERENCES modalities(id),
    capability_description TEXT,
    PRIMARY KEY (model_id, modality_id)
);

-- API Pricing
CREATE TABLE IF NOT EXISTS api_pricing (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model_id INTEGER REFERENCES models(id) ON DELETE CASCADE,
    api_name TEXT,
    input_token_price DECIMAL(12, 9),
    output_token_price DECIMAL(12, 9),
    input_token_price_200k DECIMAL(12, 9),
    output_token_price_200k DECIMAL(12, 9),
    cached_input_token_price DECIMAL(12, 9),
    prompt_caching_read_price DECIMAL(12, 9),
    prompt_caching_write_price DECIMAL(12, 9),
    prompt_caching_read_price_200k DECIMAL(12, 9),
    prompt_caching_write_price_200k DECIMAL(12, 9),
    audio_input_token_price DECIMAL(12, 9),
    audio_cached_input_token_price DECIMAL(12, 9),
    audio_output_token_price DECIMAL(12, 9),
    search_price_per_1000 DECIMAL(12, 6),
    context_caching_storage_price TEXT,
    effective_date DATE,
    source_url TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

SCHEMA_PRIMITIVES = """
-- ============================================================
-- PRIMITIVE TABLES — Feature Extraction (discovered through use)
-- ============================================================

-- Primitives (extractable features)
CREATE TABLE IF NOT EXISTS primitives (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    category TEXT,
    description TEXT,
    source_app_id INTEGER REFERENCES apps(id),
    extractable BOOLEAN DEFAULT TRUE,
    abstraction_level TEXT,
    lifecycle_state_id INTEGER REFERENCES lifecycle_states(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- App-Primitive Relationships
CREATE TABLE IF NOT EXISTS app_primitives (
    app_id INTEGER REFERENCES apps(id) ON DELETE CASCADE,
    primitive_id INTEGER REFERENCES primitives(id),
    implementation_quality TEXT,
    implementation_notes TEXT,
    discovered_date DATE,
    PRIMARY KEY (app_id, primitive_id)
);

-- Primitive Dependencies
CREATE TABLE IF NOT EXISTS primitive_dependencies (
    primitive_id INTEGER REFERENCES primitives(id),
    depends_on_primitive_id INTEGER REFERENCES primitives(id),
    dependency_type TEXT,
    PRIMARY KEY (primitive_id, depends_on_primitive_id)
);
"""

SCHEMA_INTELLIGENCE = """
-- ============================================================
-- INTELLIGENCE TABLES — Emergent Patterns (discovered over time)
-- ============================================================

-- Apparatus (workflow patterns)
CREATE TABLE IF NOT EXISTS apparatus (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    description TEXT,
    emergence_pattern TEXT,
    frequency_score INTEGER,
    last_detected DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Apparatus Components
CREATE TABLE IF NOT EXISTS apparatus_components (
    apparatus_id INTEGER REFERENCES apparatus(id) ON DELETE CASCADE,
    app_id INTEGER REFERENCES apps(id),
    role_in_apparatus TEXT,
    is_core BOOLEAN DEFAULT TRUE,
    usage_notes TEXT,
    PRIMARY KEY (apparatus_id, app_id)
);

-- App Relationships
CREATE TABLE IF NOT EXISTS app_relationships (
    app_id INTEGER REFERENCES apps(id),
    related_app_id INTEGER REFERENCES apps(id),
    relationship_type TEXT,
    strength INTEGER,
    notes TEXT,
    discovered_date DATE,
    PRIMARY KEY (app_id, related_app_id),
    CHECK (app_id != related_app_id)
);

-- Usage Contexts
CREATE TABLE IF NOT EXISTS usage_contexts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    description TEXT,
    spatial_context TEXT,
    attentional_state TEXT,
    temporal_dynamic TEXT,
    social_setting TEXT
);

-- App Usage Contexts
CREATE TABLE IF NOT EXISTS app_usage_contexts (
    app_id INTEGER REFERENCES apps(id),
    context_id INTEGER REFERENCES usage_contexts(id),
    effectiveness_score INTEGER,
    notes TEXT,
    PRIMARY KEY (app_id, context_id)
);

-- Workflow Templates
CREATE TABLE IF NOT EXISTS workflow_templates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    description TEXT,
    apparatus_id INTEGER REFERENCES apparatus(id),
    use_frequency TEXT,
    average_duration_minutes INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Workflow Steps
CREATE TABLE IF NOT EXISTS workflow_steps (
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
"""

SCHEMA_KINETIC = """
-- ============================================================
-- KINETIC TABLES — Action Vocabulary and Agent Bindings (Phase B)
-- ============================================================

-- Action Types: the verbs of the ontology
CREATE TABLE IF NOT EXISTS action_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    parent_role_id INTEGER REFERENCES roles(id),
    description TEXT,
    input_type TEXT,
    output_type TEXT,
    write_back_capable BOOLEAN DEFAULT FALSE,
    requires_approval BOOLEAN DEFAULT FALSE,
    automation_level TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- App Actions: which app supports which action type (with quality rating)
CREATE TABLE IF NOT EXISTS app_actions (
    app_id INTEGER REFERENCES apps(id) ON DELETE CASCADE,
    action_type_id INTEGER REFERENCES action_types(id),
    quality_rating TEXT,
    is_primary BOOLEAN DEFAULT FALSE,
    automation_support TEXT,
    notes TEXT,
    PRIMARY KEY (app_id, action_type_id)
);

-- Agent Bindings: which Constellation agent uses which app for which action
CREATE TABLE IF NOT EXISTS agent_bindings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    agent_code TEXT NOT NULL,
    app_id INTEGER REFERENCES apps(id) ON DELETE CASCADE,
    action_type_id INTEGER REFERENCES action_types(id),
    binding_strength TEXT,
    invocation_method TEXT,
    frequency TEXT,
    notes TEXT,
    UNIQUE (agent_code, app_id, action_type_id)
);
"""

SCHEMA_STRATEGIC = """
-- ============================================================
-- STRATEGIC TABLES — Entity Expansion (DA-07, 2026-02-11)
-- 6 new entity types + governed verbs (advisory mode)
-- ============================================================

-- Commitments: obligations, promises, deadlines
CREATE TABLE IF NOT EXISTS commitments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    stakeholder TEXT,
    deadline DATE,
    status TEXT DEFAULT 'active',
    intention_link TEXT,
    linear_id TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Goals: desired outcomes linked to intentions
CREATE TABLE IF NOT EXISTS goals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    intention_link TEXT,
    target_date DATE,
    status TEXT DEFAULT 'active',
    success_criteria TEXT,
    linear_id TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Risks: identified threats with probability and impact
CREATE TABLE IF NOT EXISTS risks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    category TEXT,
    probability TEXT,
    impact TEXT,
    mitigation TEXT,
    status TEXT DEFAULT 'active',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Strategic Relationships: connections between entities
CREATE TABLE IF NOT EXISTS strategic_relationships (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    entity_a TEXT NOT NULL,
    entity_a_type TEXT NOT NULL,
    entity_b TEXT NOT NULL,
    entity_b_type TEXT NOT NULL,
    relationship_type TEXT NOT NULL,
    strength INTEGER,
    context TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Resources: physical and digital assets
CREATE TABLE IF NOT EXISTS resources (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    category TEXT,
    monthly_cost REAL DEFAULT 0,
    status TEXT DEFAULT 'active',
    owner TEXT,
    machine TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Environments: operating contexts
CREATE TABLE IF NOT EXISTS environments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    machine TEXT,
    spatial_context TEXT,
    primary_agent TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Governed Verbs: advisory mode — tracks verb usage, does not enforce
CREATE TABLE IF NOT EXISTS governed_verbs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    verb TEXT NOT NULL UNIQUE,
    category TEXT,
    applies_to TEXT,
    requires_approval BOOLEAN DEFAULT FALSE,
    advisory_note TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Strategic indexes
CREATE INDEX IF NOT EXISTS idx_commitments_status ON commitments(status);
CREATE INDEX IF NOT EXISTS idx_goals_status ON goals(status);
CREATE INDEX IF NOT EXISTS idx_risks_category ON risks(category);
CREATE INDEX IF NOT EXISTS idx_resources_category ON resources(category);
CREATE INDEX IF NOT EXISTS idx_governed_verbs_category ON governed_verbs(category);
"""

SCHEMA_OPERATIONAL = """
-- ============================================================
-- OPERATIONAL TABLES — Syncrescendence Project Management
-- (Not part of CANON-30300 tech stack, but part of ontology substrate)
-- ============================================================

-- Projects (from DYN-PROJECTS.csv)
CREATE TABLE IF NOT EXISTS projects (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT,
    status TEXT,
    priority TEXT,
    owner TEXT,
    blocked_by TEXT,
    oracle_scope TEXT,
    modal TEXT,
    due_date TEXT,
    created TEXT,
    updated TEXT,
    notes TEXT
);

-- Tasks (from DYN-TASKS.csv)
CREATE TABLE IF NOT EXISTS tasks (
    id TEXT PRIMARY KEY,
    project_id TEXT REFERENCES projects(id),
    name TEXT NOT NULL,
    type TEXT,
    status TEXT,
    priority TEXT,
    owner TEXT,
    blocked_by TEXT,
    estimate_hrs REAL,
    actual_hrs REAL,
    created TEXT,
    updated TEXT,
    notes TEXT
);

-- Accounts (from DYN-ACCOUNTS.csv)
CREATE TABLE IF NOT EXISTS accounts (
    account_id INTEGER PRIMARY KEY,
    email TEXT NOT NULL,
    auth_method TEXT,
    teleology TEXT,
    owns_origin BOOLEAN,
    google_ecosystem BOOLEAN
);

-- Platforms (from DYN-PLATFORMS.csv — also feeds apps table)
CREATE TABLE IF NOT EXISTS platforms (
    platform_id INTEGER PRIMARY KEY,
    platform_name TEXT NOT NULL,
    platform_type TEXT,
    vendor TEXT,
    account TEXT,
    role TEXT,
    has_projects BOOLEAN,
    has_memory BOOLEAN,
    max_context_tokens TEXT,
    status TEXT,
    device TEXT,
    teleology TEXT
);

-- Platform Roles (from DYN-ROLES.csv)
CREATE TABLE IF NOT EXISTS platform_roles (
    role_id INTEGER PRIMARY KEY,
    role_name TEXT NOT NULL,
    role_function TEXT,
    specification_tier TEXT,
    invocation_mode TEXT
);

-- Sources (from DYN-SOURCES.csv)
CREATE TABLE IF NOT EXISTS sources (
    id TEXT PRIMARY KEY,
    filename TEXT,
    filepath TEXT,
    platform TEXT,
    format TEXT,
    cadence TEXT,
    value_modality TEXT,
    signal_tier TEXT,
    status TEXT,
    chain TEXT,
    topics TEXT,
    creator TEXT,
    guest TEXT,
    title TEXT,
    date_published TEXT,
    date_processed TEXT,
    date_integrated TEXT,
    integrated_into TEXT,
    notes TEXT
);

-- Filename Mappings (from REF-FILENAME_MAPPING.csv)
CREATE TABLE IF NOT EXISTS filename_mappings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    original_filename TEXT,
    mapped_filename TEXT
);

-- Rename Mappings (from REF-RENAME_MAPPING.csv)
CREATE TABLE IF NOT EXISTS rename_mappings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    old_name TEXT,
    new_name TEXT
);
"""

SCHEMA_INDEXES = """
-- ============================================================
-- INDEXES — Navigation Performance
-- ============================================================

-- App search
CREATE INDEX IF NOT EXISTS idx_apps_name ON apps(name);
CREATE INDEX IF NOT EXISTS idx_apps_slug ON apps(slug);
CREATE INDEX IF NOT EXISTS idx_apps_layer ON apps(layer_id);
CREATE INDEX IF NOT EXISTS idx_apps_role ON apps(role_id);
CREATE INDEX IF NOT EXISTS idx_apps_object_type ON apps(object_type_id);
CREATE INDEX IF NOT EXISTS idx_apps_lifecycle ON apps(lifecycle_state_id);
CREATE INDEX IF NOT EXISTS idx_apps_stage ON apps(stage);

-- Model search
CREATE INDEX IF NOT EXISTS idx_models_name ON models(name);
CREATE INDEX IF NOT EXISTS idx_models_api_name ON models(api_name);
CREATE INDEX IF NOT EXISTS idx_models_family ON models(family);
CREATE INDEX IF NOT EXISTS idx_models_lab ON models(research_lab);

-- Primitive search
CREATE INDEX IF NOT EXISTS idx_primitives_code ON primitives(code);
CREATE INDEX IF NOT EXISTS idx_primitives_category ON primitives(category);
CREATE INDEX IF NOT EXISTS idx_primitives_extractable ON primitives(extractable);

-- Apparatus search
CREATE INDEX IF NOT EXISTS idx_apparatus_code ON apparatus(code);
CREATE INDEX IF NOT EXISTS idx_apparatus_frequency ON apparatus(frequency_score);

-- Relationship search
CREATE INDEX IF NOT EXISTS idx_app_relationships_type ON app_relationships(relationship_type);
CREATE INDEX IF NOT EXISTS idx_app_primitives_quality ON app_primitives(implementation_quality);

-- Kinetic indexes
CREATE INDEX IF NOT EXISTS idx_action_types_code ON action_types(code);
CREATE INDEX IF NOT EXISTS idx_action_types_category ON action_types(category);
CREATE INDEX IF NOT EXISTS idx_app_actions_quality ON app_actions(quality_rating);
CREATE INDEX IF NOT EXISTS idx_agent_bindings_agent ON agent_bindings(agent_code);
CREATE INDEX IF NOT EXISTS idx_agent_bindings_app ON agent_bindings(app_id);

-- Operational indexes
CREATE INDEX IF NOT EXISTS idx_projects_status ON projects(status);
CREATE INDEX IF NOT EXISTS idx_tasks_status ON tasks(status);
CREATE INDEX IF NOT EXISTS idx_tasks_project ON tasks(project_id);
CREATE INDEX IF NOT EXISTS idx_sources_status ON sources(status);
CREATE INDEX IF NOT EXISTS idx_sources_chain ON sources(chain);
CREATE INDEX IF NOT EXISTS idx_platforms_vendor ON platforms(vendor);
"""

SCHEMA_META = """
-- ============================================================
-- META TABLE — Database metadata and migration tracking
-- ============================================================

CREATE TABLE IF NOT EXISTS _meta (
    key TEXT PRIMARY KEY,
    value TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""


# --- Bedrock Seed Data ---

def seed_bedrock(conn):
    """Populate bedrock tables with canonical taxonomy data from CANON-30300."""
    cur = conn.cursor()

    # Layers (ASA L0-L6)
    cur.executemany(
        "INSERT OR IGNORE INTO layers (code, name, description, domain, sequence_order) VALUES (?, ?, ?, ?, ?)",
        [
            ("L0", "Physical Substrate", "Material and energetic foundation: silicon, memory, cooling, power", "mechanics", 0),
            ("L1", "Transduction Interface", "Bidirectional conversion: sensors, actuators, signal processing", "mechanics", 1),
            ("L2", "Perceptual Surface", "Sensory presentation: visual, auditory, haptic design optimized for humans", "symbols", 2),
            ("L3", "Interaction Grammar", "Structured actions and communications: gestures, language, multimodal input", "symbols", 3),
            ("L4", "Choreographic Flows", "Temporal architecture: navigation, state, synchronization, error recovery", "semantics", 4),
            ("L5", "Cognitive Convergence", "Hybrid reasoning: augmentation, collaboration, personalization, knowledge synthesis", "semantics", 5),
            ("L6", "Agentic Emergence", "Autonomous operation: planning, coordination, value alignment, oversight", "agency", 6),
        ],
    )

    # Object Types (ASA ontology)
    cur.executemany(
        "INSERT OR IGNORE INTO object_types (asa_code, name, description, typical_layers) VALUES (?, ?, ?, ?)",
        [
            ("O.FN", "Function Objects", "Stateless computational units performing specific transformations", "L4,L5"),
            ("O.SVC", "Service Objects", "Stateful processes providing ongoing capabilities", "L4,L5,L6"),
            ("O.WF", "Workflow Objects", "Orchestrated multi-step processes", "L4"),
            ("O.AGT", "Agent Objects", "Goal-directed autonomous systems with adaptive behavior", "L6"),
            ("O.MOD", "Model Objects", "Trained intelligence: prediction, generation, reasoning", "L5"),
            ("O.DP", "Data Product Objects", "Governed, versioned datasets", "L4,L5"),
            ("O.STM", "Stream Objects", "Continuous data flows for real-time updates", "L4"),
            ("O.ARC", "Archive Objects", "Long-term information preservation", "L4"),
            ("O.SRF", "Surface Objects", "Presentation and display components", "L2,L3"),
            ("O.SNS", "Sensor Objects", "Environmental perception and data capture", "L1"),
            ("O.ACT", "Actuator Objects", "Physical manipulation and feedback", "L1"),
            ("O.INS", "Instrument Objects", "High-fidelity human control mechanisms", "L3"),
            ("O.GRD", "Guard Objects", "Policy enforcement and safety mechanisms", "L5,L6"),
            ("O.EVL", "Evaluator Objects", "Quality assessment and performance measurement", "L5,L6"),
            ("O.CPL", "Copilot Objects", "Human-AI collaborative interface components", "L5"),
            # Strategic Entity Types (DA-07 expansion, 2026-02-11)
            ("O.CMT", "Commitment Objects", "Obligations, promises, and deadlines with stakeholders", "L6"),
            ("O.GOL", "Goal Objects", "Desired outcomes linked to intentions and success criteria", "L6"),
            ("O.RSK", "Risk Objects", "Identified threats with probability, impact, and mitigation", "L6"),
            ("O.REL", "Relationship Objects", "Strategic connections between entities across domains", "L5,L6"),
            ("O.RES", "Resource Objects", "Physical and digital assets with cost and ownership", "L0,L4"),
            ("O.ENV", "Environment Objects", "Operating contexts binding machines, agents, and spatial states", "L0,L2"),
        ],
    )

    # Commercial Seams
    cur.executemany(
        "INSERT OR IGNORE INTO commercial_seams (code, name, description, lock_in_risk, typical_pricing_model) VALUES (?, ?, ?, ?, ?)",
        [
            ("vector_db", "Vector Database / Retrieval", "Embedding storage and similarity search (Pinecone, Weaviate, Chroma)", "high", "per-query + storage"),
            ("api_router", "API Router / Multi-Model Orchestrator", "Unified model access (OpenRouter, Perplexity)", "medium", "per-request markup"),
            ("inference_engine", "Inference Engine / Optimizer", "Model serving optimization (fal.ai, Triton, DeepSpeed)", "medium", "compute time"),
            ("observability", "Observability / Eval / Alignment", "Monitoring and quality assurance (Helicone, Langfuse)", "low", "SaaS subscription"),
            ("model_marketplace", "Model Marketplace / Hub", "Weight hosting and discovery (Hugging Face, Replicate)", "medium", "marketplace fee"),
            ("edge_runtime", "Edge Runtime / On-device", "Local model execution (CoreML, TFLite, Ollama)", "low", "SDK licensing"),
            ("security_gateway", "Security / Policy Gateway", "Data masking, PII scrubbing, safety filters", "medium", "SaaS or self-hosted"),
        ],
    )

    # Modalities
    cur.executemany(
        "INSERT OR IGNORE INTO modalities (code, name, description) VALUES (?, ?, ?)",
        [
            ("text", "Text", "Written language input and output"),
            ("voice", "Voice", "Speech input and synthesis"),
            ("visual", "Visual", "Image and video processing"),
            ("gesture", "Gesture", "Physical movement and spatial input"),
            ("haptic", "Haptic", "Touch and force feedback"),
        ],
    )

    # Lifecycle States
    cur.executemany(
        "INSERT OR IGNORE INTO lifecycle_states (code, name, description, sequence_order) VALUES (?, ?, ?, ?)",
        [
            ("experimental", "Experimental", "Testing phase, not production-ready", 1),
            ("active", "Active", "Currently in regular use", 2),
            ("primitive_repository", "Primitive Repository", "No longer primary tool, but features worth extracting", 3),
            ("deprecated", "Deprecated", "Discontinued, replaced by alternatives", 4),
            ("archived", "Archived", "Historical record only", 5),
        ],
    )

    # Deployment Contexts
    cur.executemany(
        "INSERT OR IGNORE INTO deployment_contexts (code, name, description) VALUES (?, ?, ?)",
        [
            ("cloud", "Cloud", "Hosted on remote servers, accessed via internet"),
            ("on_premise", "On-Premise", "Installed and run on local infrastructure"),
            ("edge", "Edge", "Runs on edge devices with limited connectivity"),
            ("hybrid", "Hybrid", "Combination of cloud and local deployment"),
            ("local", "Local", "Runs entirely on personal hardware"),
        ],
    )

    # Initial Primitives (seed set from CANON-30300)
    cur.executemany(
        "INSERT OR IGNORE INTO primitives (code, name, category, description, extractable, abstraction_level) VALUES (?, ?, ?, ?, ?, ?)",
        [
            ("vim_motions", "Vim-style Navigation", "keybinding", "Modal editing with hjkl navigation and text objects", True, "atomic"),
            ("markdown_render", "Markdown Rendering", "rendering", "Live preview of markdown with formatting", True, "atomic"),
            ("real_time_sync", "Real-time Synchronization", "collaboration", "Instant updates across devices/users", True, "compound"),
            ("offline_first", "Offline-first Architecture", "data_sync", "Full functionality without internet connection", True, "compound"),
            ("bi_directional_sync", "Bidirectional Sync", "data_sync", "Two-way synchronization preserving local changes", True, "compound"),
            ("full_text_search", "Full-text Search", "search", "Search across all content with relevance ranking", True, "atomic"),
            ("tag_system", "Flexible Tagging", "organization", "Arbitrary tags for classification", True, "atomic"),
            ("link_system", "Bidirectional Links", "organization", "Wikilink-style connections between notes", True, "atomic"),
            ("api_access", "API Access", "integration", "Programmatic access to data and functions", True, "atomic"),
            ("webhook_support", "Webhook Integration", "integration", "Event-driven automation triggers", True, "atomic"),
        ],
    )

    # Initial Apparatus patterns
    cur.executemany(
        "INSERT OR IGNORE INTO apparatus (code, name, description, emergence_pattern, frequency_score) VALUES (?, ?, ?, ?, ?)",
        [
            ("writing_apparatus", "Writing & Publishing Workflow", "Capture > Draft > Edit > Publish across multiple platforms", "emerges naturally from need for systematic content production", 5),
            ("research_apparatus", "Research & Synthesis Workflow", "Collect > Annotate > Connect > Synthesize > Document", "emerges from knowledge work and learning projects", 5),
            ("coding_apparatus", "Software Development Workflow", "Edit > Test > Debug > Deploy > Monitor", "standard in software development", 5),
            ("design_apparatus", "Design & Creation Workflow", "Ideate > Sketch > Prototype > Refine > Export", "emerges in creative work", 4),
            ("analysis_apparatus", "Data Analysis Workflow", "Import > Clean > Transform > Visualize > Report", "emerges in data-driven work", 4),
            ("communication_apparatus", "Communication & Collaboration", "Schedule > Meet > Document > Follow-up > Archive", "standard in team work", 5),
        ],
    )

    # Initial Usage Contexts
    cur.executemany(
        "INSERT OR IGNORE INTO usage_contexts (code, name, description, spatial_context, attentional_state, temporal_dynamic, social_setting) VALUES (?, ?, ?, ?, ?, ?, ?)",
        [
            ("mobile_capture", "Mobile Capture", "Quick information capture while mobile", "ambulatory", "divided", "reactive", "solitary"),
            ("deep_analysis", "Deep Analysis", "Sustained focused work on complex problems", "fixed", "immersive", "deliberative", "solitary"),
            ("rapid_synthesis", "Rapid Synthesis", "Quickly combining multiple information sources", "fixed", "focused", "reactive", "solitary"),
            ("collaborative_session", "Collaborative Session", "Real-time work with others", "situated", "focused", "reactive", "collaborative"),
            ("cockpit_ops", "Cockpit Operations", "Multi-agent coordination from command center", "fixed", "immersive", "persistent", "solitary"),
        ],
    )

    conn.commit()
    return cur.rowcount


def import_csv(conn, table, csv_path, column_map=None):
    """Import a CSV file into a table. column_map renames CSV headers to DB columns."""
    if not os.path.exists(csv_path):
        print(f"  SKIP: {csv_path} not found")
        return 0

    cur = conn.cursor()
    count = 0

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            print(f"  SKIP: {csv_path} has no headers")
            return 0

        for row in reader:
            # Apply column mapping if provided
            if column_map:
                mapped = {}
                for csv_col, db_col in column_map.items():
                    if csv_col in row:
                        mapped[db_col] = row[csv_col]
                row = mapped

            # Clean values
            cleaned = {}
            for k, v in row.items():
                if v in ("null", "NULL", "", None):
                    cleaned[k] = None
                elif v in ("TRUE", "true", "True"):
                    cleaned[k] = True
                elif v in ("FALSE", "false", "False"):
                    cleaned[k] = False
                else:
                    cleaned[k] = v.strip() if isinstance(v, str) else v

            cols = list(cleaned.keys())
            placeholders = ", ".join(["?"] * len(cols))
            col_names = ", ".join(cols)

            try:
                cur.execute(
                    f"INSERT OR REPLACE INTO {table} ({col_names}) VALUES ({placeholders})",
                    list(cleaned.values()),
                )
                count += 1
            except sqlite3.Error as e:
                print(f"  WARN: Row {count + 1} in {csv_path}: {e}")

    conn.commit()
    return count


def import_platforms_to_apps(conn, csv_path):
    """Cross-populate apps table from DYN-PLATFORMS.csv data."""
    if not os.path.exists(csv_path):
        return 0

    cur = conn.cursor()
    count = 0

    # Get lifecycle state ID for 'active'
    cur.execute("SELECT id FROM lifecycle_states WHERE code = 'active'")
    active_id = cur.fetchone()
    active_lifecycle_id = active_id[0] if active_id else None

    # Get object type IDs
    type_map = {}
    cur.execute("SELECT asa_code, id FROM object_types")
    for row in cur.fetchall():
        type_map[row[0]] = row[1]

    # Map platform_type to object type
    platform_type_to_asa = {
        "web_app": "O.SRF",
        "desktop_app": "O.SRF",
        "cli": "O.INS",
        "browser_ext": "O.SRF",
        "mobile_app": "O.SRF",
        "agent": "O.AGT",
    }

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row.get("platform_name", "").strip()
            vendor = row.get("vendor", "").strip()
            platform_type = row.get("platform_type", "").strip()
            status = row.get("status", "").strip()
            teleology = row.get("teleology", "").strip()

            slug = f"{vendor}-{name}".lower().replace(" ", "-").replace("(", "").replace(")", "")

            asa_code = platform_type_to_asa.get(platform_type, "O.SVC")
            obj_type_id = type_map.get(asa_code)

            lifecycle_id = active_lifecycle_id if status == "ACTIVE" else None

            try:
                cur.execute(
                    """INSERT OR IGNORE INTO apps (name, slug, object_type_id, lifecycle_state_id, description, stage, notes)
                       VALUES (?, ?, ?, ?, ?, ?, ?)""",
                    (
                        f"{name} ({vendor})",
                        slug,
                        obj_type_id,
                        lifecycle_id,
                        teleology,
                        status,
                        f"Source: DYN-PLATFORMS.csv, type={platform_type}",
                    ),
                )
                count += 1
            except sqlite3.Error as e:
                print(f"  WARN: Platform {name}: {e}")

    conn.commit()
    return count


def import_functions_to_apps(conn, csv_path):
    """Import DYN-FUNCTIONS.csv into the apps table."""
    if not os.path.exists(csv_path):
        print(f"  SKIP: {csv_path} not found")
        return 0

    cur = conn.cursor()
    count = 0

    # Get lifecycle state ID for 'active'
    cur.execute("SELECT id FROM lifecycle_states WHERE code = 'active'")
    active_id = cur.fetchone()
    active_lifecycle_id = active_id[0] if active_id else None

    # Get object type IDs
    type_map = {}
    cur.execute("SELECT asa_code, id FROM object_types")
    for row in cur.fetchall():
        type_map[row[0]] = row[1]

    # Map category to object type
    category_to_asa = {
        "ai_agent": "O.AGT",
        "ai_ide": "O.CPL",
        "ai_local": "O.MOD",
        "ai_search": "O.SVC",
        "terminal": "O.SRF",
        "editor": "O.INS",
        "multiplexer": "O.INS",
        "shell": "O.INS",
        "knowledge_management": "O.DP",
        "project_management": "O.SVC",
        "design": "O.SRF",
        "communication": "O.SVC",
        "productivity": "O.SRF",
        "containerization": "O.SVC",
        "browser": "O.SRF",
        "developer_tool": "O.INS",
        "media": "O.FN",
        "input": "O.INS",
        "automation": "O.WF",
        "networking": "O.SVC",
        "app_store": "O.SVC",
        "cloud": "O.SVC",
        "infrastructure": "O.SVC",
    }

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row.get("name", "").strip()
            category = row.get("category", "").strip()
            provider = row.get("provider", "").strip()
            tier = row.get("tier", "").strip()
            cost = row.get("monthly_cost", "0").strip()
            capabilities = row.get("capabilities", "").strip()
            platform = row.get("platform", "").strip()
            notes = row.get("notes", "").strip()

            slug = f"{name.lower().replace(' ', '-').replace('(', '').replace(')', '')}"

            asa_code = category_to_asa.get(category, "O.SVC")
            obj_type_id = type_map.get(asa_code)

            try:
                cur.execute(
                    """INSERT OR IGNORE INTO apps (name, slug, object_type_id, lifecycle_state_id, description, stage, notes)
                       VALUES (?, ?, ?, ?, ?, ?, ?)""",
                    (
                        name,
                        slug,
                        obj_type_id,
                        active_lifecycle_id,
                        capabilities,
                        "ACTIVE",
                        f"provider={provider}, tier={tier}, cost=${cost}/mo, platform={platform}. {notes}",
                    ),
                )
                count += 1
            except sqlite3.Error as e:
                print(f"  WARN: Function {name}: {e}")

    conn.commit()
    return count


def import_models_csv(conn, csv_path):
    """Import DYN-MODELS.csv into the models table."""
    if not os.path.exists(csv_path):
        print(f"  SKIP: {csv_path} not found")
        return 0

    cur = conn.cursor()
    count = 0

    # Get object type ID for models
    cur.execute("SELECT id FROM object_types WHERE asa_code = 'O.MOD'")
    mod_type = cur.fetchone()
    mod_type_id = mod_type[0] if mod_type else None

    # Get lifecycle state ID for 'active'
    cur.execute("SELECT id FROM lifecycle_states WHERE code = 'active'")
    active_id = cur.fetchone()
    active_lifecycle_id = active_id[0] if active_id else None

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row.get("name", "").strip()
            provider = row.get("provider", "").strip()
            api_name = row.get("api_name", "").strip()
            family = row.get("family", "").strip()
            context_window = int(row.get("context_window", "0").strip() or "0")
            output_limit = int(row.get("output_token_limit", "0").strip() or "0")
            supports_vision = row.get("supports_vision", "FALSE").strip().upper() == "TRUE"
            supports_thinking = row.get("supports_extended_thinking", "FALSE").strip().upper() == "TRUE"
            supports_search = row.get("supports_search", "FALSE").strip().upper() == "TRUE"
            release_date = row.get("release_date", "").strip() or None
            training_cutoff = row.get("training_cutoff", "").strip() or None
            notes = row.get("notes", "").strip()
            capabilities = row.get("capabilities", "").strip()

            slug = f"{provider.lower()}-{api_name}".replace(" ", "-")

            try:
                cur.execute(
                    """INSERT OR IGNORE INTO models
                       (name, slug, api_name, family, research_lab, object_type_id,
                        lifecycle_state_id, context_window, output_token_limit,
                        training_cutoff_date, release_date,
                        supports_vision, supports_extended_thinking, supports_search,
                        notes)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (
                        name, slug, api_name, family, provider,
                        mod_type_id, active_lifecycle_id,
                        context_window, output_limit,
                        training_cutoff, release_date,
                        supports_vision, supports_thinking, supports_search,
                        f"{capabilities}. {notes}",
                    ),
                )
                model_id = cur.lastrowid

                # Also insert pricing from the same CSV
                input_cost = row.get("input_cost_per_1k", "0").strip()
                output_cost = row.get("output_cost_per_1k", "0").strip()
                if model_id and (float(input_cost or 0) > 0 or float(output_cost or 0) > 0):
                    # Convert per-1k to per-token for the pricing table
                    input_per_token = float(input_cost) / 1000.0 if input_cost else 0
                    output_per_token = float(output_cost) / 1000.0 if output_cost else 0
                    cur.execute(
                        """INSERT OR IGNORE INTO api_pricing
                           (model_id, api_name, input_token_price, output_token_price,
                            effective_date, notes)
                           VALUES (?, ?, ?, ?, ?, ?)""",
                        (
                            model_id, api_name,
                            input_per_token, output_per_token,
                            release_date,
                            f"Source: DYN-MODELS.csv. Per-1k rates: ${input_cost}/${output_cost}",
                        ),
                    )

                count += 1
            except sqlite3.Error as e:
                print(f"  WARN: Model {name}: {e}")

    conn.commit()
    return count


def import_api_pricing_csv(conn, csv_path):
    """Import DYN-API_PRICING.csv as supplemental service pricing data.
    These are subscription/service-level entries (not per-token model pricing).
    Stored in a separate services table or as notes in apps."""
    if not os.path.exists(csv_path):
        print(f"  SKIP: {csv_path} not found")
        return 0

    cur = conn.cursor()
    count = 0

    # Get lifecycle state ID for 'active'
    cur.execute("SELECT id FROM lifecycle_states WHERE code = 'active'")
    active_id = cur.fetchone()
    active_lifecycle_id = active_id[0] if active_id else None

    # Get object type ID for services
    cur.execute("SELECT id FROM object_types WHERE asa_code = 'O.SVC'")
    svc_type = cur.fetchone()
    svc_type_id = svc_type[0] if svc_type else None

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            service = row.get("service", "").strip()
            plan = row.get("plan", "").strip()
            cost = row.get("monthly_cost", "0").strip()
            rate_limit = row.get("rate_limit", "").strip()
            features = row.get("features", "").strip()
            status = row.get("status", "").strip()
            notes = row.get("notes", "").strip()

            slug = f"api-{service.lower().replace(' ', '-').replace('(', '').replace(')', '')}"

            try:
                cur.execute(
                    """INSERT OR IGNORE INTO apps
                       (name, slug, object_type_id, lifecycle_state_id, description, stage, notes)
                       VALUES (?, ?, ?, ?, ?, ?, ?)""",
                    (
                        f"{service} [{plan}]",
                        slug,
                        svc_type_id,
                        active_lifecycle_id if status == "active" else None,
                        features,
                        status.upper(),
                        f"plan={plan}, cost=${cost}/mo, rate_limit={rate_limit}. {notes}",
                    ),
                )
                count += 1
            except sqlite3.Error as e:
                print(f"  WARN: API {service}: {e}")

    conn.commit()
    return count


# --- Ontology Enrichment Functions (Phase 5) ---


def seed_roles(conn):
    """Populate roles table with functional role taxonomy from CANON-30300."""
    cur = conn.cursor()
    cur.executemany(
        "INSERT OR IGNORE INTO roles (code, name, description) VALUES (?, ?, ?)",
        [
            ("capture", "Capture", "Acquire information from external sources into the system"),
            ("process", "Process", "Transform, analyze, or synthesize captured information"),
            ("present", "Present", "Display, publish, or output processed information"),
            ("orchestrate", "Orchestrate", "Coordinate multi-step workflows across tools"),
            ("store", "Store", "Persist and organize data for retrieval"),
            ("search", "Search", "Find and retrieve stored information"),
            ("communicate", "Communicate", "Enable human-to-human or human-to-AI interaction"),
            ("automate", "Automate", "Execute rule-based or triggered actions without human intervention"),
            ("verify", "Verify", "Validate, test, or confirm correctness"),
            ("secure", "Secure", "Protect access, credentials, and data integrity"),
            ("navigate", "Navigate", "File system, window, and context navigation"),
            ("edit", "Edit", "Modify text, code, media, or structured data"),
            ("model", "Model", "Provide AI inference, reasoning, or generation"),
            ("deploy", "Deploy", "Package and deliver applications or infrastructure"),
            ("monitor", "Monitor", "Observe system state and performance"),
        ],
    )
    conn.commit()


def seed_expanded_primitives(conn):
    """Expand primitives from 10 seeds to ~45 covering all major feature categories."""
    cur = conn.cursor()
    cur.executemany(
        "INSERT OR IGNORE INTO primitives (code, name, category, description, extractable, abstraction_level) VALUES (?, ?, ?, ?, ?, ?)",
        [
            # Keybinding
            ("keyboard_shortcuts", "Keyboard Shortcuts", "keybinding", "Configurable keyboard shortcuts for common actions", True, "atomic"),
            ("command_palette", "Command Palette", "keybinding", "Fuzzy-searchable command launcher (Cmd+K/Cmd+P pattern)", True, "atomic"),
            # Rendering
            ("syntax_highlighting", "Syntax Highlighting", "rendering", "Language-aware code coloring with theme support", True, "atomic"),
            ("latex_render", "LaTeX Rendering", "rendering", "Mathematical equation typesetting", True, "atomic"),
            ("mermaid_diagrams", "Mermaid Diagram Rendering", "rendering", "Code-to-diagram rendering for flowcharts, sequences, etc.", True, "atomic"),
            ("live_preview", "Live Preview", "rendering", "Real-time rendering of markup as you type", True, "compound"),
            # Collaboration
            ("presence_awareness", "Presence Awareness", "collaboration", "See who else is viewing/editing the same content", True, "compound"),
            ("commenting", "Inline Commenting", "collaboration", "Threaded comments anchored to specific content locations", True, "atomic"),
            ("version_history", "Version History", "collaboration", "Browse and restore previous versions of content", True, "compound"),
            # Data sync
            ("git_integration", "Git Integration", "data_sync", "Built-in version control with commit/push/pull", True, "compound"),
            ("cloud_sync", "Cloud Synchronization", "data_sync", "Automatic sync to cloud storage services", True, "compound"),
            ("conflict_resolution", "Conflict Resolution", "data_sync", "Automated or assisted merge conflict handling", True, "compound"),
            # Search
            ("fuzzy_search", "Fuzzy Search", "search", "Approximate string matching with ranking", True, "atomic"),
            ("regex_search", "Regex Search", "search", "Regular expression pattern matching in search", True, "atomic"),
            ("semantic_search", "Semantic Search", "search", "Meaning-based search using embeddings or AI", True, "compound"),
            # Organization
            ("folder_hierarchy", "Folder Hierarchy", "organization", "Nested directory/folder organization", True, "atomic"),
            ("database_views", "Database Views", "organization", "Structured data with multiple view types (table, board, calendar)", True, "compound"),
            ("graph_view", "Graph View", "organization", "Visual network graph of linked content", True, "compound"),
            ("templates", "Content Templates", "organization", "Reusable content templates and scaffolding", True, "atomic"),
            # Integration
            ("plugin_system", "Plugin/Extension System", "integration", "Third-party extensibility via plugins or extensions", True, "compound"),
            ("mcp_support", "MCP Protocol Support", "integration", "Model Context Protocol for AI tool integration", True, "compound"),
            ("cli_interface", "CLI Interface", "integration", "Command-line interface for scripted automation", True, "atomic"),
            ("deep_linking", "Deep Linking", "integration", "URL scheme for linking directly to specific content", True, "atomic"),
            # Export
            ("pdf_export", "PDF Export", "export", "Export content to PDF format", True, "atomic"),
            ("multi_format_export", "Multi-format Export", "export", "Export to multiple formats (HTML, PDF, DOCX, etc.)", True, "compound"),
            ("publish_api", "Publish API", "export", "Programmatic publishing to external platforms", True, "compound"),
            # AI capabilities
            ("ai_chat", "AI Chat Interface", "ai", "Conversational AI interaction within the application", True, "compound"),
            ("ai_code_completion", "AI Code Completion", "ai", "Inline code suggestions powered by AI models", True, "compound"),
            ("ai_search_grounding", "AI Search Grounding", "ai", "AI responses grounded in web or document search", True, "compound"),
            ("extended_thinking", "Extended Thinking", "ai", "Visible chain-of-thought reasoning before response", True, "compound"),
            ("memory_persistence", "Memory Persistence", "ai", "Cross-session memory of user preferences and context", True, "compound"),
            ("multi_model_routing", "Multi-model Routing", "ai", "Ability to route requests to different AI models", True, "compound"),
            # Automation
            ("rule_engine", "Rule-based Automation", "automation", "If-then rules for automated actions", True, "compound"),
            ("cron_scheduling", "Scheduled Automation", "automation", "Time-based triggering of automated tasks", True, "atomic"),
            ("file_watching", "File System Watching", "automation", "Monitor filesystem changes and trigger actions", True, "atomic"),
        ],
    )
    conn.commit()


def seed_app_primitives(conn):
    """Map apps to their implemented primitives with quality ratings."""
    cur = conn.cursor()

    # Build dynamic lookup maps (IDs may change across rebuilds)
    slug_to_id = {}
    cur.execute("SELECT id, slug FROM apps")
    for row in cur.fetchall():
        slug_to_id[row[1]] = row[0]

    prim_map = {}
    cur.execute("SELECT id, code FROM primitives")
    for row in cur.fetchall():
        prim_map[row[1]] = row[0]

    # (app_slug, primitive_code, quality, notes)
    mappings = [
        # Obsidian
        ("obsidian", "vim_motions", "good", "Via vim plugin"),
        ("obsidian", "markdown_render", "excellent", "Core feature"),
        ("obsidian", "link_system", "excellent", "Wikilinks + backlinks"),
        ("obsidian", "graph_view", "excellent", "Built-in graph"),
        ("obsidian", "tag_system", "excellent", "Nested tags"),
        ("obsidian", "full_text_search", "excellent", "Fast vault-wide search"),
        ("obsidian", "plugin_system", "excellent", "Community plugins ecosystem"),
        ("obsidian", "offline_first", "excellent", "Local-first markdown files"),
        ("obsidian", "templates", "good", "Template plugin"),
        ("obsidian", "cloud_sync", "good", "Via iCloud/Obsidian Sync"),
        ("obsidian", "mermaid_diagrams", "good", "Built-in mermaid support"),
        ("obsidian", "deep_linking", "good", "obsidian:// URL scheme"),
        ("obsidian", "command_palette", "excellent", "Cmd+P command palette"),
        ("obsidian", "keyboard_shortcuts", "excellent", "Fully customizable"),
        ("obsidian", "pdf_export", "good", "Via plugin"),
        # Neovim
        ("neovim", "vim_motions", "excellent", "Native modal editing"),
        ("neovim", "syntax_highlighting", "excellent", "Treesitter-based"),
        ("neovim", "keyboard_shortcuts", "excellent", "Fully programmable"),
        ("neovim", "command_palette", "good", "Telescope fuzzy finder"),
        ("neovim", "plugin_system", "excellent", "Lua plugin ecosystem (Lazy.nvim)"),
        ("neovim", "git_integration", "good", "Via fugitive/gitsigns"),
        ("neovim", "fuzzy_search", "excellent", "Telescope"),
        ("neovim", "regex_search", "excellent", "Native regex"),
        ("neovim", "cli_interface", "excellent", "Terminal-native"),
        ("neovim", "ai_code_completion", "good", "Via Copilot/Codeium plugins"),
        # Claude Code
        ("claude-code", "ai_chat", "excellent", "Core feature"),
        ("claude-code", "ai_code_completion", "excellent", "Inline code editing"),
        ("claude-code", "extended_thinking", "excellent", "Extended thinking mode"),
        ("claude-code", "mcp_support", "excellent", "Native MCP tool use"),
        ("claude-code", "cli_interface", "excellent", "Terminal-native"),
        ("claude-code", "git_integration", "excellent", "Direct git operations"),
        ("claude-code", "full_text_search", "excellent", "Grep/ripgrep integration"),
        ("claude-code", "memory_persistence", "good", "CLAUDE.md-based context"),
        ("claude-code", "multi_model_routing", "good", "Model switching"),
        # Cursor
        ("cursor", "ai_code_completion", "excellent", "Core AI coding feature"),
        ("cursor", "ai_chat", "excellent", "Inline AI chat"),
        ("cursor", "syntax_highlighting", "excellent", "VSCode-based"),
        ("cursor", "vim_motions", "good", "Via vim extension"),
        ("cursor", "git_integration", "excellent", "Built-in git"),
        ("cursor", "plugin_system", "excellent", "VSCode extension ecosystem"),
        ("cursor", "command_palette", "excellent", "Cmd+Shift+P"),
        ("cursor", "multi_model_routing", "excellent", "Multiple AI model support"),
        ("cursor", "keyboard_shortcuts", "excellent", "Fully customizable"),
        ("cursor", "fuzzy_search", "excellent", "Cmd+P file search"),
        # ChatGPT
        ("chatgpt", "ai_chat", "excellent", "Core feature"),
        ("chatgpt", "extended_thinking", "excellent", "o3/GPT-5 thinking"),
        ("chatgpt", "ai_search_grounding", "excellent", "Web browsing"),
        ("chatgpt", "memory_persistence", "excellent", "Cross-session memory"),
        ("chatgpt", "multi_format_export", "good", "Canvas + download"),
        ("chatgpt", "ai_code_completion", "good", "Via Canvas"),
        # Notion
        ("notion", "database_views", "excellent", "Core feature — table/board/calendar/gallery"),
        ("notion", "templates", "excellent", "Template system"),
        ("notion", "real_time_sync", "excellent", "Cloud-native collaboration"),
        ("notion", "commenting", "excellent", "Inline comments"),
        ("notion", "api_access", "excellent", "REST API"),
        ("notion", "full_text_search", "good", "Full page search"),
        ("notion", "markdown_render", "good", "Markdown-like blocks"),
        ("notion", "presence_awareness", "good", "See who is editing"),
        ("notion", "deep_linking", "good", "Page/block URLs"),
        ("notion", "keyboard_shortcuts", "good", "Cmd+K and shortcuts"),
        ("notion", "ai_chat", "good", "Notion AI feature"),
        # Linear
        ("linear", "keyboard_shortcuts", "excellent", "Keyboard-first design"),
        ("linear", "api_access", "excellent", "GraphQL API"),
        ("linear", "webhook_support", "excellent", "Webhook integrations"),
        ("linear", "full_text_search", "excellent", "Fast issue search"),
        ("linear", "templates", "good", "Issue templates"),
        ("linear", "database_views", "good", "Views: board/list/timeline"),
        ("linear", "command_palette", "excellent", "Cmd+K command menu"),
        # Gemini CLI
        ("gemini-cli", "ai_chat", "excellent", "Core feature"),
        ("gemini-cli", "ai_search_grounding", "excellent", "Google Search grounding"),
        ("gemini-cli", "cli_interface", "excellent", "Terminal-native"),
        ("gemini-cli", "extended_thinking", "good", "2.5 Pro thinking"),
        # Raycast
        ("raycast", "command_palette", "excellent", "Core launcher feature"),
        ("raycast", "keyboard_shortcuts", "excellent", "Global hotkeys"),
        ("raycast", "plugin_system", "excellent", "Extension store"),
        ("raycast", "fuzzy_search", "excellent", "Fuzzy app/file/command search"),
        ("raycast", "deep_linking", "good", "Raycast URL scheme"),
        ("raycast", "ai_chat", "good", "Raycast AI"),
        # git
        ("git", "git_integration", "excellent", "Git IS the integration"),
        ("git", "cli_interface", "excellent", "Terminal-native"),
        ("git", "version_history", "excellent", "Core feature"),
        ("git", "conflict_resolution", "good", "Merge conflict tools"),
        # gh
        ("gh", "cli_interface", "excellent", "GitHub CLI"),
        ("gh", "api_access", "excellent", "GitHub API access"),
        # ripgrep
        ("ripgrep", "regex_search", "excellent", "Core feature — fast regex"),
        ("ripgrep", "full_text_search", "excellent", "Fastest grep alternative"),
        ("ripgrep", "cli_interface", "excellent", "Terminal-native"),
        # fzf
        ("fzf", "fuzzy_search", "excellent", "Core feature"),
        ("fzf", "cli_interface", "excellent", "Terminal-native"),
        # lazygit
        ("lazygit", "git_integration", "excellent", "Git TUI"),
        ("lazygit", "keyboard_shortcuts", "excellent", "Vim-like navigation"),
        ("lazygit", "version_history", "good", "Visual commit history"),
        # Slack
        ("slack", "real_time_sync", "excellent", "Real-time messaging"),
        ("slack", "full_text_search", "good", "Message search"),
        ("slack", "api_access", "excellent", "Slack API"),
        ("slack", "webhook_support", "excellent", "Incoming/outgoing webhooks"),
        ("slack", "plugin_system", "good", "Slack apps"),
        ("slack", "keyboard_shortcuts", "good", "Cmd+K navigation"),
        # Discord
        ("discord", "real_time_sync", "excellent", "Real-time messaging"),
        ("discord", "api_access", "good", "Bot API"),
        ("discord", "webhook_support", "excellent", "Channel webhooks"),
        # Figma
        ("figma", "real_time_sync", "excellent", "Real-time collaboration"),
        ("figma", "presence_awareness", "excellent", "Cursor presence"),
        ("figma", "commenting", "excellent", "Design comments"),
        ("figma", "version_history", "excellent", "File version history"),
        ("figma", "plugin_system", "excellent", "Plugin ecosystem"),
        ("figma", "keyboard_shortcuts", "excellent", "Design shortcuts"),
        # Keyboard Maestro
        ("keyboard-maestro", "rule_engine", "excellent", "Core macro automation"),
        ("keyboard-maestro", "keyboard_shortcuts", "excellent", "Trigger via hotkeys"),
        ("keyboard-maestro", "file_watching", "good", "Folder trigger"),
        ("keyboard-maestro", "cron_scheduling", "excellent", "Time-based triggers"),
        # Hazel
        ("hazel", "rule_engine", "excellent", "File organization rules"),
        ("hazel", "file_watching", "excellent", "Core feature — folder monitoring"),
        # tmux
        ("tmux", "keyboard_shortcuts", "excellent", "Prefix-key bindings"),
        ("tmux", "cli_interface", "excellent", "Terminal multiplexer"),
        # Ollama
        ("ollama", "ai_chat", "good", "Local chat interface"),
        ("ollama", "cli_interface", "excellent", "Terminal-native"),
        ("ollama", "api_access", "excellent", "REST API"),
        ("ollama", "multi_model_routing", "excellent", "Multiple local models"),
        # 1Password
        ("1password", "cli_interface", "excellent", "op CLI"),
        ("1password", "deep_linking", "good", "1password:// URLs"),
        ("1password", "cloud_sync", "excellent", "Cross-device sync"),
        # DEVONthink
        ("devonthink", "full_text_search", "excellent", "AI-powered search"),
        ("devonthink", "tag_system", "excellent", "Hierarchical tags"),
        ("devonthink", "folder_hierarchy", "excellent", "Database/group hierarchy"),
        ("devonthink", "pdf_export", "good", "PDF handling"),
        ("devonthink", "semantic_search", "good", "AI classify/see-also"),
        ("devonthink", "cloud_sync", "good", "Sync via CloudKit/WebDAV"),
        ("devonthink", "deep_linking", "excellent", "x-devonthink-item:// links"),
        # Perplexity
        ("perplexity", "ai_chat", "excellent", "Citation-backed AI chat"),
        ("perplexity", "ai_search_grounding", "excellent", "Core feature"),
        ("perplexity", "full_text_search", "good", "Query history search"),
        # Zotero
        ("zotero", "tag_system", "excellent", "Reference tagging"),
        ("zotero", "full_text_search", "excellent", "PDF full-text search"),
        ("zotero", "cloud_sync", "excellent", "Zotero sync"),
        ("zotero", "plugin_system", "good", "Zotero plugins"),
        # OpenClaw
        ("openclaw", "ai_chat", "excellent", "Persistent agent chat"),
        ("openclaw", "memory_persistence", "excellent", "Cross-session memory"),
        ("openclaw", "multi_model_routing", "excellent", "Multi-model gateway"),
        ("openclaw", "plugin_system", "excellent", "Plugin architecture"),
        ("openclaw", "api_access", "excellent", "REST API gateway"),
        # Things3
        ("things3", "tag_system", "excellent", "GTD tags"),
        ("things3", "keyboard_shortcuts", "excellent", "Quick entry hotkey"),
        ("things3", "deep_linking", "excellent", "things:// URL scheme"),
        ("things3", "templates", "good", "Project templates"),
        # ClickUp
        ("clickup", "database_views", "excellent", "Multiple view types"),
        ("clickup", "api_access", "excellent", "REST API"),
        ("clickup", "templates", "good", "Task templates"),
        ("clickup", "commenting", "good", "Task comments"),
        # Airtable
        ("airtable", "database_views", "excellent", "Core feature"),
        ("airtable", "api_access", "excellent", "REST API"),
        ("airtable", "webhook_support", "good", "Automation webhooks"),
        ("airtable", "templates", "excellent", "Base templates"),
        # Docker Desktop
        ("docker-desktop", "cli_interface", "excellent", "docker/docker-compose CLI"),
        ("docker-desktop", "templates", "good", "Compose templates"),
        # Ghostty
        ("ghostty", "keyboard_shortcuts", "excellent", "Configurable keybindings"),
        ("ghostty", "cli_interface", "good", "Terminal emulator shell host"),
    ]

    count = 0
    for slug, prim_code, quality, notes in mappings:
        app_id = slug_to_id.get(slug)
        prim_id = prim_map.get(prim_code)
        if app_id and prim_id:
            try:
                cur.execute(
                    "INSERT OR IGNORE INTO app_primitives (app_id, primitive_id, implementation_quality, implementation_notes) VALUES (?, ?, ?, ?)",
                    (app_id, prim_id, quality, notes),
                )
                count += 1
            except sqlite3.Error as e:
                print(f"  WARN: app_primitives {slug}/{prim_code}: {e}")
        else:
            if not app_id:
                pass  # Slug not in DB — silently skip (may be renamed or missing from CSV)
            if not prim_id:
                print(f"  WARN: primitive '{prim_code}' not found — check seed data")
    conn.commit()
    return count


def seed_app_modalities(conn):
    """Map all apps to their interaction modalities."""
    cur = conn.cursor()

    app_ids = {}
    cur.execute("SELECT id, slug FROM apps")
    for row in cur.fetchall():
        app_ids[row[1]] = row[0]

    mod_ids = {}
    cur.execute("SELECT id, code FROM modalities")
    for row in cur.fetchall():
        mod_ids[row[1]] = row[0]

    text_id = mod_ids["text"]
    voice_id = mod_ids["voice"]
    visual_id = mod_ids["visual"]
    gesture_id = mod_ids["gesture"]
    haptic_id = mod_ids["haptic"]

    # Default: ALL apps get text modality (primary)
    for slug, app_id in app_ids.items():
        cur.execute(
            "INSERT OR IGNORE INTO app_modalities (app_id, modality_id, is_primary, notes) VALUES (?, ?, ?, ?)",
            (app_id, text_id, True, "Default text interaction"),
        )

    # Visual modality apps (GUI with significant visual interaction)
    visual_slugs = [
        "obsidian", "notion", "figma", "cursor", "brave-browser",
        "google-chrome", "safari", "vivaldi", "linear", "clickup",
        "chatgpt", "claude-desktop", "blender", "final-cut-pro",
        "logic-pro", "iina", "milanote", "raycast", "github-desktop",
        "shottr", "pixelsnap", "imageoptim", "airtable", "things3",
        "devonthink", "zotero", "forklift", "yazi", "lazygit",
        "docker-desktop", "iterm2", "ghostty", "elgato-stream-deck",
        "hookmark", "nitro-pdf-pro", "presentify", "soulver",
        "alttab", "dockdoor", "ice", "maccy", "keyclu",
    ]
    for slug in visual_slugs:
        app_id = app_ids.get(slug)
        if app_id:
            cur.execute(
                "INSERT OR IGNORE INTO app_modalities (app_id, modality_id, is_primary, notes) VALUES (?, ?, ?, ?)",
                (app_id, visual_id, False, "GUI-based visual interaction"),
            )

    # Voice modality apps
    for slug in ["chatgpt", "whisper-cpp", "discord", "slack"]:
        app_id = app_ids.get(slug)
        if app_id:
            cur.execute(
                "INSERT OR IGNORE INTO app_modalities (app_id, modality_id, is_primary, notes) VALUES (?, ?, ?, ?)",
                (app_id, voice_id, False, "Voice interaction support"),
            )

    # Gesture modality (trackpad/touch)
    for slug in ["bettertouchtool", "magnet", "karabiner-elements"]:
        app_id = app_ids.get(slug)
        if app_id:
            cur.execute(
                "INSERT OR IGNORE INTO app_modalities (app_id, modality_id, is_primary, notes) VALUES (?, ?, ?, ?)",
                (app_id, gesture_id, False, "Gesture/touch interaction"),
            )

    # Haptic modality
    app_id = app_ids.get("elgato-stream-deck")
    if app_id:
        cur.execute(
            "INSERT OR IGNORE INTO app_modalities (app_id, modality_id, is_primary, notes) VALUES (?, ?, ?, ?)",
            (app_id, haptic_id, False, "Physical tactile buttons"),
        )

    conn.commit()


def seed_app_deployment_contexts(conn):
    """Map all apps to their deployment contexts (cloud/local/hybrid/on-premise)."""
    cur = conn.cursor()

    app_ids = {}
    cur.execute("SELECT id, slug FROM apps")
    for row in cur.fetchall():
        app_ids[row[1]] = row[0]

    ctx_ids = {}
    cur.execute("SELECT id, code FROM deployment_contexts")
    for row in cur.fetchall():
        ctx_ids[row[1]] = row[0]

    cloud_id = ctx_ids["cloud"]
    local_id = ctx_ids["local"]
    hybrid_id = ctx_ids["hybrid"]
    on_prem_id = ctx_ids["on_premise"]

    # CLI tools → local (preferred)
    cli_slugs = [
        "claude-code", "neovim", "tmux", "gh", "git", "ripgrep", "fzf",
        "bat", "eza", "fd", "jq", "yazi", "lazygit", "starship", "atuin",
        "zoxide", "direnv", "sesh", "mise", "whisper-cpp", "ffmpeg",
        "yt-dlp", "gemini-cli", "codex-cli", "awscli", "gcloud", "terraform",
    ]
    for slug in cli_slugs:
        app_id = app_ids.get(slug)
        if app_id:
            cur.execute(
                "INSERT OR IGNORE INTO app_deployment_contexts (app_id, context_id, is_preferred) VALUES (?, ?, ?)",
                (app_id, local_id, True),
            )

    # Desktop apps → local (preferred)
    desktop_slugs = [
        "cursor", "ghostty", "emacs", "obsidian", "raycast",
        "brave-browser", "google-chrome", "safari", "vivaldi",
        "karabiner-elements", "keyboard-maestro", "hazel", "1password",
        "alttab", "appcleaner", "bettertouchtool", "blender", "default-folder-x",
        "dockdoor", "expressions", "final-cut-pro", "forklift", "github-desktop",
        "handbrake", "hookmark", "huggingchat", "ice", "iina", "imageoptim",
        "iterm2", "keyclu", "logic-pro", "maccy", "milanote", "netnewswire",
        "nitro-pdf-pro", "pixelsnap", "presentify", "shottr", "soulver",
        "things3", "vivaldi", "zotero", "magnet", "amphetamine",
        "elgato-stream-deck", "devonthink", "xcode",
    ]
    for slug in desktop_slugs:
        app_id = app_ids.get(slug)
        if app_id:
            cur.execute(
                "INSERT OR IGNORE INTO app_deployment_contexts (app_id, context_id, is_preferred) VALUES (?, ?, ?)",
                (app_id, local_id, True),
            )

    # Hybrid apps (both local client and cloud backend)
    hybrid_slugs = [
        "obsidian", "1password", "docker-desktop", "tailscale", "figma",
        "slack", "discord", "notion", "linear", "clickup", "zotero",
        "devonthink", "airtable", "setapp", "chatgpt", "claude-desktop",
        "perplexity",
    ]
    for slug in hybrid_slugs:
        app_id = app_ids.get(slug)
        if app_id:
            cur.execute(
                "INSERT OR IGNORE INTO app_deployment_contexts (app_id, context_id, is_preferred) VALUES (?, ?, ?)",
                (app_id, hybrid_id, False),
            )

    # Cloud-native (web apps, SaaS platforms — entries 1-18)
    for slug in [
        "anthropic-claude-web", "anthropic-claude-desktop", "anthropic-claude-code-cli",
        "anthropic-claude-chrome-ext", "anthropic-claude-cowork",
        "openai-chatgpt-web", "openai-chatgpt-desktop", "openai-codex-cli",
        "google-gemini-web", "google-gemini-cli", "google-gemini-mobile",
        "google-notebooklm", "xai-grok-web",
        "perplexity-perplexity-web", "perplexity-perplexity-desktop",
    ]:
        app_id = app_ids.get(slug)
        if app_id:
            cur.execute(
                "INSERT OR IGNORE INTO app_deployment_contexts (app_id, context_id, is_preferred) VALUES (?, ?, ?)",
                (app_id, cloud_id, True),
            )

    # Self-hosted / on-premise
    self_hosted_slugs = [
        "ollama", "openclaw", "openclaw-openclaw-mini", "openclaw-openclaw-mba",
        "api-graphiti", "api-qdrant", "api-neo4j", "api-chroma", "api-ollama", "api-openclaw",
    ]
    for slug in self_hosted_slugs:
        app_id = app_ids.get(slug)
        if app_id:
            cur.execute(
                "INSERT OR IGNORE INTO app_deployment_contexts (app_id, context_id, is_preferred) VALUES (?, ?, ?)",
                (app_id, on_prem_id, True),
            )

    # API service entries → cloud
    cloud_api_slugs = [
        "api-anthropic-claude-max", "api-anthropic-claude-pro",
        "api-openai-chatgpt-plus", "api-google-ai-pro", "api-nvidia-nim",
        "api-linear", "api-clickup", "api-notion", "api-github",
        "api-setapp", "api-perplexity", "api-xai-grok", "api-tailscale", "api-homebrew",
    ]
    for slug in cloud_api_slugs:
        app_id = app_ids.get(slug)
        if app_id:
            cur.execute(
                "INSERT OR IGNORE INTO app_deployment_contexts (app_id, context_id, is_preferred) VALUES (?, ?, ?)",
                (app_id, cloud_id, True),
            )

    conn.commit()


def seed_apparatus_components(conn):
    """Map apps to their roles in the 6 apparatus workflow patterns."""
    cur = conn.cursor()

    app_ids = {}
    cur.execute("SELECT id, slug FROM apps")
    for row in cur.fetchall():
        app_ids[row[1]] = row[0]

    apparatus_ids = {}
    cur.execute("SELECT id, code FROM apparatus")
    for row in cur.fetchall():
        apparatus_ids[row[1]] = row[0]

    # (apparatus_code, app_slug, role_in_apparatus, is_core, usage_notes)
    components = [
        # Writing Apparatus
        ("writing_apparatus", "obsidian", "capture", True, "Quick capture + long-form drafting"),
        ("writing_apparatus", "claude-code", "process", True, "AI-assisted editing and restructuring"),
        ("writing_apparatus", "chatgpt", "process", False, "Canvas for formatting and editing"),
        ("writing_apparatus", "neovim", "process", False, "Technical/markdown editing"),
        ("writing_apparatus", "notion", "present", False, "Publishing and sharing"),
        ("writing_apparatus", "keyboard-maestro", "orchestrate", False, "Text expansion and automation"),
        # Research Apparatus
        ("research_apparatus", "perplexity", "capture", True, "Citation-backed research queries"),
        ("research_apparatus", "obsidian", "capture", True, "Research note capture"),
        ("research_apparatus", "zotero", "capture", True, "Reference management and PDF annotation"),
        ("research_apparatus", "devonthink", "store", False, "Document archive and AI classification"),
        ("research_apparatus", "claude-code", "process", True, "Analysis and synthesis"),
        ("research_apparatus", "gemini-cli", "process", True, "Corpus sensing with 2M context"),
        # Coding Apparatus
        ("coding_apparatus", "neovim", "edit", True, "Primary code editor (LazyVim)"),
        ("coding_apparatus", "claude-code", "process", True, "AI code generation and editing"),
        ("coding_apparatus", "git", "orchestrate", True, "Version control backbone"),
        ("coding_apparatus", "gh", "orchestrate", True, "GitHub PR/issue management"),
        ("coding_apparatus", "lazygit", "orchestrate", False, "Visual git operations"),
        ("coding_apparatus", "docker-desktop", "deploy", False, "Container-based deployment"),
        ("coding_apparatus", "tmux", "orchestrate", True, "Session/pane management"),
        ("coding_apparatus", "ghostty", "present", True, "Terminal rendering"),
        ("coding_apparatus", "ripgrep", "search", True, "Fast codebase search"),
        # Design Apparatus
        ("design_apparatus", "figma", "process", True, "UI/UX design and prototyping"),
        ("design_apparatus", "blender", "process", False, "3D modeling and rendering"),
        ("design_apparatus", "shottr", "capture", True, "Screenshot capture and annotation"),
        ("design_apparatus", "imageoptim", "process", False, "Image optimization for export"),
        ("design_apparatus", "pixelsnap", "capture", False, "Pixel measurement tool"),
        # Analysis Apparatus
        ("analysis_apparatus", "claude-code", "process", True, "Data analysis and transformation"),
        ("analysis_apparatus", "gemini-cli", "process", True, "Large corpus analysis"),
        ("analysis_apparatus", "obsidian", "present", True, "Analysis documentation"),
        ("analysis_apparatus", "airtable", "store", False, "Structured data storage"),
        ("analysis_apparatus", "jq", "process", False, "JSON data transformation"),
        # Communication Apparatus
        ("communication_apparatus", "slack", "communicate", True, "Team messaging"),
        ("communication_apparatus", "discord", "communicate", True, "Community + agent integration"),
        ("communication_apparatus", "linear", "orchestrate", True, "Task tracking and assignment"),
        ("communication_apparatus", "notion", "present", False, "Documentation and wikis"),
        ("communication_apparatus", "obsidian", "capture", False, "Meeting notes capture"),
    ]

    count = 0
    for app_code, app_slug, role, is_core, notes in components:
        apparatus_id = apparatus_ids.get(app_code)
        app_id = app_ids.get(app_slug)
        if apparatus_id and app_id:
            try:
                cur.execute(
                    "INSERT OR IGNORE INTO apparatus_components (apparatus_id, app_id, role_in_apparatus, is_core, usage_notes) VALUES (?, ?, ?, ?, ?)",
                    (apparatus_id, app_id, role, is_core, notes),
                )
                count += 1
            except sqlite3.Error as e:
                print(f"  WARN: apparatus_components {app_code}/{app_slug}: {e}")
    conn.commit()
    return count


def seed_app_relationships(conn):
    """Map key relationships between apps (powers, competes, requires, combines_with, obsoletes)."""
    cur = conn.cursor()

    app_ids = {}
    cur.execute("SELECT id, slug FROM apps")
    for row in cur.fetchall():
        app_ids[row[1]] = row[0]

    # (app_slug, related_slug, relationship_type, strength 1-5, notes)
    relationships = [
        # Competition
        ("obsidian", "notion", "competes", 4, "PKM: local-first vs cloud-first"),
        ("obsidian", "devonthink", "competes", 3, "Document management overlap"),
        ("notion", "clickup", "competes", 3, "Project management + docs overlap"),
        ("notion", "airtable", "competes", 3, "Database views overlap"),
        ("linear", "clickup", "competes", 4, "Project management"),
        ("linear", "things3", "competes", 2, "Task management (different scales)"),
        ("neovim", "cursor", "competes", 4, "Code editing (vim vs AI-first)"),
        ("neovim", "emacs", "competes", 3, "Terminal editor choice"),
        ("brave-browser", "google-chrome", "competes", 4, "Primary browser"),
        ("brave-browser", "safari", "competes", 3, "Browser choice"),
        ("brave-browser", "vivaldi", "competes", 3, "Privacy browser"),
        ("slack", "discord", "competes", 3, "Team communication"),
        ("ghostty", "iterm2", "competes", 4, "Terminal emulator"),
        ("claude-code", "codex-cli", "competes", 4, "CLI AI coding agent"),
        ("claude-code", "cursor", "competes", 3, "AI coding tool"),
        ("chatgpt", "claude-desktop", "competes", 4, "AI chat desktop app"),
        ("perplexity", "chatgpt", "competes", 3, "AI search vs AI chat+search"),
        ("hazel", "keyboard-maestro", "competes", 2, "Automation overlap"),
        # Powers (provides capabilities to another)
        ("ollama", "openclaw", "powers", 5, "Local model inference for agent"),
        ("tmux", "neovim", "powers", 4, "Session management for editor"),
        ("tmux", "claude-code", "powers", 3, "Terminal session for agent"),
        ("ghostty", "tmux", "powers", 5, "GPU-rendered terminal for multiplexer"),
        ("starship", "ghostty", "powers", 3, "Prompt rendering in terminal"),
        ("git", "gh", "powers", 5, "VCS backbone for GitHub CLI"),
        ("git", "lazygit", "powers", 5, "VCS backbone for git TUI"),
        ("docker-desktop", "openclaw", "powers", 4, "Container runtime for agent services"),
        ("tailscale", "openclaw", "powers", 3, "Mesh VPN for inter-machine agent access"),
        # Requires (hard dependency)
        ("lazygit", "git", "requires", 5, "Cannot function without git"),
        ("gh", "git", "requires", 5, "GitHub CLI requires git"),
        ("sesh", "tmux", "requires", 5, "Session manager requires tmux"),
        ("cursor", "git", "requires", 3, "VCS integration dependency"),
        # Combines With (synergistic pairing)
        ("obsidian", "zotero", "combines_with", 4, "Research notes + reference management"),
        ("obsidian", "devonthink", "combines_with", 3, "Notes + document archive"),
        ("claude-code", "gemini-cli", "combines_with", 4, "Execution + corpus sensing"),
        ("claude-code", "openclaw", "combines_with", 4, "Execution + persistent memory"),
        ("neovim", "claude-code", "combines_with", 4, "Editor + AI agent"),
        ("fzf", "ripgrep", "combines_with", 4, "Fuzzy filter + fast search"),
        ("fzf", "fd", "combines_with", 4, "Fuzzy filter + fast find"),
        ("keyboard-maestro", "raycast", "combines_with", 3, "Deep automation + quick launch"),
        ("hazel", "keyboard-maestro", "combines_with", 3, "File automation + macro automation"),
        ("bat", "fzf", "combines_with", 3, "Preview in fuzzy finder"),
        ("linear", "slack", "combines_with", 3, "Task tracking + communication"),
        ("linear", "gh", "combines_with", 4, "Issue tracking + PR management"),
        ("figma", "notion", "combines_with", 3, "Design + documentation"),
        # Obsoletes
        ("ghostty", "iterm2", "obsoletes", 3, "GPU-accelerated replacement"),
    ]

    count = 0
    for app_slug, related_slug, rel_type, strength, notes in relationships:
        app_id = app_ids.get(app_slug)
        related_id = app_ids.get(related_slug)
        if app_id and related_id and app_id != related_id:
            try:
                cur.execute(
                    "INSERT OR IGNORE INTO app_relationships (app_id, related_app_id, relationship_type, strength, notes) VALUES (?, ?, ?, ?, ?)",
                    (app_id, related_id, rel_type, strength, notes),
                )
                count += 1
            except sqlite3.Error as e:
                print(f"  WARN: app_relationships {app_slug}/{related_slug}: {e}")
    conn.commit()
    return count


def seed_model_capabilities(conn):
    """Populate model_capabilities junction table — maps AI models to modality capabilities."""
    cur = conn.cursor()

    # Build lookup maps
    model_ids = {}
    cur.execute("SELECT id, slug FROM models")
    for row in cur.fetchall():
        model_ids[row[1]] = row[0]

    modality_ids = {}
    cur.execute("SELECT id, code FROM modalities")
    for row in cur.fetchall():
        modality_ids[row[1]] = row[0]

    # (model_slug, modality_code, capability_description)
    capabilities = [
        # Anthropic
        ("anthropic-claude-opus-4-6", "text", "State-of-the-art reasoning, coding, analysis, extended thinking"),
        ("anthropic-claude-opus-4-6", "visual", "Image understanding, chart analysis, screenshot interpretation"),
        ("anthropic-claude-sonnet-4-5-20250514", "text", "Fast balanced reasoning, coding, extended thinking"),
        ("anthropic-claude-sonnet-4-5-20250514", "visual", "Image understanding, diagram analysis"),
        ("anthropic-claude-sonnet-4-20250514", "text", "Balanced reasoning and coding"),
        ("anthropic-claude-sonnet-4-20250514", "visual", "Image understanding"),
        ("anthropic-claude-3-5-haiku-20241022", "text", "Fast lightweight text generation and classification"),
        # OpenAI
        ("openai-gpt-5", "text", "Frontier reasoning, coding, multimodal understanding"),
        ("openai-gpt-5", "visual", "Image understanding, generation, analysis"),
        ("openai-gpt-5", "voice", "Real-time voice conversation via ChatGPT"),
        ("openai-gpt-5.3-codex", "text", "Code-specialized reasoning with autonomous execution"),
        ("openai-gpt-5.3-codex", "visual", "Screenshot and diagram understanding for code context"),
        ("openai-o3", "text", "Deep deliberative reasoning, math, science, coding"),
        ("openai-o3", "visual", "Visual reasoning for complex diagrams"),
        ("openai-o4-mini", "text", "Fast cost-effective reasoning"),
        ("openai-text-embedding-3-large", "text", "High-dimensional text embeddings (3072d)"),
        ("openai-text-embedding-3-small", "text", "Compact text embeddings (1536d)"),
        # Google
        ("google-gemini-2.5-pro", "text", "Frontier reasoning, 1M+ context, code generation"),
        ("google-gemini-2.5-pro", "visual", "Image, video, and document understanding"),
        ("google-gemini-2.5-pro", "voice", "Audio understanding and generation"),
        ("google-gemini-2.5-flash", "text", "Fast balanced reasoning, large context"),
        ("google-gemini-2.5-flash", "visual", "Image and video understanding"),
        ("google-gemini-2.0-flash", "text", "Real-time fast generation"),
        ("google-gemini-2.0-flash", "visual", "Image understanding"),
        # Meta
        ("meta-llama-4-maverick", "text", "Open-weight frontier reasoning and coding"),
        ("meta-llama-4-maverick", "visual", "Multimodal image understanding"),
        ("meta-llama-4-scout", "text", "Efficient open-weight generation, long context"),
        ("meta-llama-4-scout", "visual", "Basic image understanding"),
        # Others
        ("xai-grok-3", "text", "Real-time web-grounded reasoning and analysis"),
        ("xai-grok-3", "visual", "Image understanding and generation"),
        ("deepseek-deepseek-r1", "text", "Open-weight reasoning with chain-of-thought"),
        ("moonshot-ai-kimi-k2.5", "text", "Long-context reasoning, coding, multi-turn"),
        ("moonshot-ai-kimi-k2.5", "visual", "Image and document understanding"),
        ("alibaba-qwen-3", "text", "Multilingual reasoning and coding"),
        ("mistral-codestral-latest", "text", "Code-specialized generation and completion"),
    ]

    count = 0
    for model_slug, modality_code, description in capabilities:
        model_id = model_ids.get(model_slug)
        modality_id = modality_ids.get(modality_code)
        if model_id and modality_id:
            try:
                cur.execute(
                    "INSERT OR IGNORE INTO model_capabilities (model_id, modality_id, capability_description) VALUES (?, ?, ?)",
                    (model_id, modality_id, description),
                )
                count += 1
            except sqlite3.Error as e:
                print(f"  WARN: model_capabilities {model_slug}/{modality_code}: {e}")
    conn.commit()
    return count


def seed_app_commercial_seams(conn):
    """Populate app_commercial_seams junction table — maps apps to commercial seam categories."""
    cur = conn.cursor()

    # Build lookup maps
    app_ids = {}
    cur.execute("SELECT id, slug FROM apps WHERE slug IS NOT NULL")
    for row in cur.fetchall():
        app_ids[row[1]] = row[0]

    seam_ids = {}
    cur.execute("SELECT id, code FROM commercial_seams")
    for row in cur.fetchall():
        seam_ids[row[1]] = row[0]

    # (app_slug, seam_code, role_in_seam)
    mappings = [
        # Vector DB seam
        ("api-qdrant", "vector_db", "primary storage"),
        ("api-chroma", "vector_db", "local development"),
        # API Router seam
        ("api-openclaw", "api_router", "agent gateway"),
        ("api-anthropic-claude-max", "api_router", "Claude API access"),
        ("api-anthropic-claude-pro", "api_router", "Claude API access (secondary)"),
        ("api-openai-chatgpt-plus", "api_router", "OpenAI API access"),
        ("api-google-ai-pro", "api_router", "Google AI API access"),
        ("api-nvidia-nim", "api_router", "NVIDIA model inference"),
        ("api-ollama", "api_router", "Local model routing"),
        ("api-perplexity", "api_router", "Search-augmented inference"),
        ("api-xai-grok", "api_router", "xAI API access"),
        # Inference Engine seam
        ("ollama", "inference_engine", "local inference runtime"),
        ("openclaw", "inference_engine", "agent inference orchestration"),
        ("api-ollama", "inference_engine", "local model serving"),
        # Observability seam
        ("api-graphiti", "observability", "knowledge graph memory"),
        ("api-neo4j", "observability", "graph database backend"),
        # Model Marketplace seam
        ("api-nvidia-nim", "model_marketplace", "hosted model catalog"),
        ("ollama", "model_marketplace", "local model registry"),
        ("api-setapp", "model_marketplace", "app subscription marketplace"),
        # Edge Runtime seam
        ("docker-desktop", "edge_runtime", "container orchestration"),
        ("tailscale", "edge_runtime", "mesh networking"),
        ("api-tailscale", "edge_runtime", "mesh network API"),
        # Security Gateway seam
        ("1password", "security_gateway", "credential management"),
        ("tailscale", "security_gateway", "zero-trust networking"),
    ]

    count = 0
    for app_slug, seam_code, role in mappings:
        app_id = app_ids.get(app_slug)
        seam_id = seam_ids.get(seam_code)
        if app_id and seam_id:
            try:
                cur.execute(
                    "INSERT OR IGNORE INTO app_commercial_seams (app_id, seam_id, role_in_seam) VALUES (?, ?, ?)",
                    (app_id, seam_id, role),
                )
                count += 1
            except sqlite3.Error as e:
                print(f"  WARN: app_commercial_seams {app_slug}/{seam_code}: {e}")
    conn.commit()
    return count


def seed_action_types(conn):
    """Populate action_types with kinetic vocabulary — Phase B.

    66 action types across 4 categories:
    - core (45): 3 per role, anchored to 15 existing roles
    - compound (7): multi-role spanning actions
    - governance (7): authorization and control actions
    - personal (7): sovereign cognitive/commitment actions
    """
    cur = conn.cursor()

    # Build role lookup
    cur.execute("SELECT id, code FROM roles")
    role_map = {row[1]: row[0] for row in cur.fetchall()}

    # (code, name, category, parent_role_code_or_None, description,
    #  input_type, output_type, write_back, requires_approval, automation_level)
    action_types = [
        # === CORE: capture (role_id=1) ===
        ("capture_text", "Capture Text", "core", "capture", "Ingest raw text content from any source into the system", "text", "text", True, False, "automated"),
        ("capture_screenshot", "Capture Screenshot", "core", "capture", "Take a visual snapshot of screen, app, or region", "signal", "file", True, False, "assisted"),
        ("capture_url", "Capture URL", "core", "capture", "Bookmark and archive a web resource with metadata", "text", "object", True, False, "automated"),
        ("capture_audio", "Capture Audio", "core", "capture", "Record or ingest audio for transcription or storage", "signal", "file", True, False, "assisted"),
        # === CORE: process (role_id=2) ===
        ("transform_text", "Transform Text", "core", "process", "Convert text between formats (markdown, HTML, JSON, etc.)", "text", "text", False, False, "automated"),
        ("extract_entities", "Extract Entities", "core", "process", "Identify and tag named entities, concepts, or primitives from text", "text", "data", False, False, "automated"),
        ("summarize", "Summarize", "core", "process", "Produce a concise distillation of longer content", "text", "text", False, False, "automated"),
        ("classify", "Classify", "core", "process", "Assign categorical labels, tags, or tiers to content", "mixed", "data", False, False, "automated"),
        # === CORE: present (role_id=3) ===
        ("render_markdown", "Render Markdown", "core", "present", "Format structured data or text as readable markdown output", "data", "text", False, False, "automated"),
        ("generate_report", "Generate Report", "core", "present", "Produce a structured analytical report from data inputs", "data", "text", True, False, "automated"),
        ("compose_message", "Compose Message", "core", "present", "Draft a communication for a specific audience and channel", "text", "text", False, False, "assisted"),
        # === CORE: orchestrate (role_id=4) ===
        ("dispatch_task", "Dispatch Task", "core", "orchestrate", "Create and route a TASK file to an agent inbox", "object", "file", True, False, "automated"),
        ("coordinate_agents", "Coordinate Agents", "core", "orchestrate", "Synchronize work across multiple Constellation agents", "signal", "signal", False, False, "assisted"),
        ("schedule_workflow", "Schedule Workflow", "core", "orchestrate", "Queue a multi-step workflow for deferred or periodic execution", "object", "object", True, False, "automated"),
        ("route_request", "Route Request", "core", "orchestrate", "Direct an inbound request to the appropriate handler agent", "signal", "signal", False, False, "automated"),
        # === CORE: store (role_id=5) ===
        ("persist_file", "Persist File", "core", "store", "Write a file to the filesystem with proper path and naming", "file", "file", True, False, "automated"),
        ("archive_content", "Archive Content", "core", "store", "Move completed or superseded content to archive with metadata", "file", "file", True, False, "automated"),
        ("index_document", "Index Document", "core", "store", "Add a document to a search index (Qdrant, Chroma, BM25)", "file", "data", True, False, "automated"),
        # === CORE: search (role_id=6) ===
        ("semantic_search", "Semantic Search", "core", "search", "Find content by meaning via vector similarity", "text", "data", False, False, "automated"),
        ("keyword_search", "Keyword Search", "core", "search", "Find content by exact or fuzzy text matching", "text", "data", False, False, "automated"),
        ("query_database", "Query Database", "core", "search", "Execute structured queries against SQLite, Neo4j, or APIs", "text", "data", False, False, "automated"),
        ("browse_web", "Browse Web", "core", "search", "Fetch and extract information from web URLs", "text", "text", False, False, "automated"),
        # === CORE: communicate (role_id=7) ===
        ("send_message", "Send Message", "core", "communicate", "Deliver a message to a specific agent or platform channel", "text", "signal", True, False, "automated"),
        ("post_update", "Post Update", "core", "communicate", "Publish a status update to a tracking platform (Linear, ClickUp)", "text", "object", True, False, "automated"),
        ("notify_agent", "Notify Agent", "core", "communicate", "Send a targeted notification or alert to a Constellation agent", "signal", "signal", False, False, "automated"),
        # === CORE: automate (role_id=8) ===
        ("trigger_webhook", "Trigger Webhook", "core", "automate", "Fire an HTTP webhook to an external service", "data", "signal", True, False, "autonomous"),
        ("run_script", "Run Script", "core", "automate", "Execute a shell script, Python script, or CLI command", "text", "mixed", True, False, "automated"),
        ("execute_macro", "Execute Macro", "core", "automate", "Run a pre-defined Keyboard Maestro or Raycast macro", "signal", "mixed", True, False, "autonomous"),
        ("schedule_cron", "Schedule Cron", "core", "automate", "Register or modify a claudecron or launchd scheduled task", "object", "object", True, True, "assisted"),
        # === CORE: verify (role_id=9) ===
        ("validate_schema", "Validate Schema", "core", "verify", "Check data structure against defined schema constraints", "data", "data", False, False, "automated"),
        ("run_tests", "Run Tests", "core", "verify", "Execute test suites and report pass/fail results", "signal", "data", False, False, "automated"),
        ("check_integrity", "Check Integrity", "core", "verify", "Verify FK consistency, orphan checks, and data completeness", "data", "data", False, False, "automated"),
        ("lint_code", "Lint Code", "core", "verify", "Run static analysis or style checks on source code", "file", "data", False, False, "automated"),
        # === CORE: secure (role_id=10) ===
        ("encrypt_data", "Encrypt Data", "core", "secure", "Apply encryption to sensitive data at rest or in transit", "data", "data", True, False, "automated"),
        ("manage_credentials", "Manage Credentials", "core", "secure", "Store, retrieve, or update authentication credentials", "object", "object", True, True, "assisted"),
        ("rotate_keys", "Rotate Keys", "core", "secure", "Generate new API keys and update all consuming services", "object", "object", True, True, "assisted"),
        # === CORE: navigate (role_id=11) ===
        ("browse_filesystem", "Browse Filesystem", "core", "navigate", "List and explore directory structures and file metadata", "text", "data", False, False, "automated"),
        ("traverse_graph", "Traverse Graph", "core", "navigate", "Walk knowledge graph relationships in Neo4j or Graphiti", "text", "data", False, False, "automated"),
        ("switch_context", "Switch Context", "core", "navigate", "Change active working directory, tmux pane, or agent focus", "signal", "signal", True, False, "assisted"),
        # === CORE: edit (role_id=12) ===
        ("modify_file", "Modify File", "core", "edit", "Make targeted changes to a specific file", "text", "file", True, False, "automated"),
        ("refactor_code", "Refactor Code", "core", "edit", "Restructure code while preserving behavior", "file", "file", True, False, "assisted"),
        ("merge_changes", "Merge Changes", "core", "edit", "Combine changes from branches, PRs, or agent outputs", "file", "file", True, False, "assisted"),
        # === CORE: model (role_id=13) ===
        ("run_inference", "Run Inference", "core", "model", "Send a prompt to an AI model and receive a response", "text", "text", False, False, "automated"),
        ("embed_text", "Embed Text", "core", "model", "Generate vector embeddings from text content", "text", "data", False, False, "automated"),
        ("fine_tune", "Fine-Tune Model", "core", "model", "Train or adapt a model on domain-specific data", "data", "object", True, True, "manual"),
        # === CORE: deploy (role_id=14) ===
        ("push_code", "Push Code", "core", "deploy", "Push committed changes to a remote git repository", "signal", "signal", True, False, "assisted"),
        ("build_artifact", "Build Artifact", "core", "deploy", "Compile, bundle, or package a deployable artifact", "file", "file", True, False, "automated"),
        ("release_version", "Release Version", "core", "deploy", "Tag and publish a versioned release", "signal", "signal", True, True, "assisted"),
        # === CORE: monitor (role_id=15) ===
        ("track_metrics", "Track Metrics", "core", "monitor", "Collect and record operational metrics over time", "data", "data", True, False, "autonomous"),
        ("detect_anomaly", "Detect Anomaly", "core", "monitor", "Identify deviations from expected patterns or thresholds", "data", "signal", False, False, "autonomous"),
        ("health_check", "Health Check", "core", "monitor", "Verify that services, agents, and pipelines are operational", "signal", "data", False, False, "autonomous"),
        # === COMPOUND (7) ===
        ("research_synthesize", "Research & Synthesize", "compound", None, "Search multiple sources, process findings, and produce a structured synthesis", "text", "text", True, False, "assisted"),
        ("code_review", "Code Review", "compound", None, "Analyze code changes for correctness, style, security, and design", "file", "text", False, False, "assisted"),
        ("clarescence", "Clarescence", "compound", None, "Multi-pass progressive refinement of a decision space to convergence", "text", "file", True, False, "assisted"),
        ("blitzkrieg_dispatch", "Blitzkrieg Dispatch", "compound", None, "Parallel multi-agent task dispatch with coordination", "object", "signal", True, False, "assisted"),
        ("metabolize_content", "Metabolize Content", "compound", None, "Capture, extract unique value, compress, and archive original", "file", "file", True, False, "assisted"),
        ("corpus_survey", "Corpus Survey", "compound", None, "Comprehensive scan of vault or codebase for patterns and gaps", "text", "text", False, False, "assisted"),
        ("pipeline_fusion", "Pipeline Fusion", "compound", None, "Wire together multiple automation stages into a continuous pipeline", "object", "object", True, True, "assisted"),
        # === GOVERNANCE (7) ===
        ("approve", "Approve", "governance", None, "Sovereign authorization gate for protected operations", "signal", "signal", True, True, "manual"),
        ("delegate", "Delegate", "governance", None, "Assign responsibility for a task or domain to another agent", "object", "signal", True, False, "assisted"),
        ("revoke", "Revoke", "governance", None, "Remove a permission, cancel a running task, or withdraw approval", "signal", "signal", True, True, "manual"),
        ("sandbox_operation", "Sandbox Operation", "governance", None, "Isolate an operation in a safe execution environment", "object", "object", True, False, "automated"),
        ("escalate", "Escalate", "governance", None, "Bump an issue to a higher authority or broader attention", "signal", "signal", True, False, "assisted"),
        ("gate", "Gate", "governance", None, "Block progression until a specified condition is met", "signal", "signal", False, False, "automated"),
        ("audit_trail", "Audit Trail", "governance", None, "Record a decision, action, or state change with full lineage", "data", "data", True, False, "automated"),
        # === PERSONAL (7) ===
        ("commit_to", "Commit To", "personal", None, "Accept an obligation or allocate resources to a commitment", "text", "object", True, True, "manual"),
        ("decline", "Decline", "personal", None, "Refuse an obligation or request with recorded rationale", "text", "object", True, False, "manual"),
        ("renegotiate", "Renegotiate", "personal", None, "Modify the terms, timeline, or scope of an existing commitment", "text", "object", True, True, "manual"),
        ("allocate_attention", "Allocate Attention", "personal", None, "Direct cognitive resources to a specific domain or task", "signal", "signal", True, False, "manual"),
        ("set_boundary", "Set Boundary", "personal", None, "Define operational limits on time, energy, or scope", "text", "object", True, False, "manual"),
        ("recover_energy", "Recover Energy", "personal", None, "Schedule recovery time and reduce operational load", "signal", "signal", True, False, "manual"),
        ("prioritize", "Prioritize", "personal", None, "Reorder the commitment stack based on current values and constraints", "data", "data", True, False, "assisted"),
    ]

    count = 0
    for (code, name, category, parent_role_code, description,
         input_type, output_type, write_back, requires_approval, automation_level) in action_types:
        parent_role_id = role_map.get(parent_role_code) if parent_role_code else None
        try:
            cur.execute(
                """INSERT INTO action_types
                   (code, name, category, parent_role_id, description,
                    input_type, output_type, write_back_capable, requires_approval, automation_level)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (code, name, category, parent_role_id, description,
                 input_type, output_type, write_back, requires_approval, automation_level),
            )
            count += 1
        except sqlite3.IntegrityError as e:
            print(f"  WARN: action_type {code}: {e}")
    conn.commit()
    return count


def seed_app_actions(conn):
    """Populate app_actions junction table — Phase B.

    Maps 40 priority apps to action types with quality ratings.
    ~230 rows covering primary app-action relationships.
    """
    cur = conn.cursor()

    # Build lookups
    cur.execute("SELECT id, slug FROM apps")
    app_map = {row[1]: row[0] for row in cur.fetchall()}

    cur.execute("SELECT id, code FROM action_types")
    action_map = {row[1]: row[0] for row in cur.fetchall()}

    # (app_slug, action_code, quality_rating, is_primary, automation_support, notes)
    mappings = [
        # Obsidian
        ("obsidian", "capture_text", "excellent", True, "mcp", "Primary knowledge capture via vault notes"),
        ("obsidian", "persist_file", "excellent", True, "mcp", "Native markdown file persistence"),
        ("obsidian", "index_document", "good", False, "mcp", "Frontmatter + Dataview indexing"),
        ("obsidian", "keyword_search", "excellent", True, "mcp", "Vault-wide search with Obsidian MCP"),
        ("obsidian", "modify_file", "excellent", True, "mcp", "Edit notes via MCP write operations"),
        ("obsidian", "render_markdown", "excellent", True, "native", "Native markdown rendering with plugins"),
        ("obsidian", "browse_filesystem", "good", False, "mcp", "Vault directory traversal via MCP"),
        # Neovim
        ("neovim", "modify_file", "excellent", True, "cli", "Primary code editor with LSP integration"),
        ("neovim", "refactor_code", "excellent", True, "cli", "LSP-powered refactoring"),
        ("neovim", "lint_code", "excellent", True, "cli", "Integrated linting via conform.nvim/nvim-lint"),
        ("neovim", "keyword_search", "good", False, "cli", "Telescope grep integration"),
        ("neovim", "merge_changes", "good", False, "cli", "Diffview and fugitive for merge resolution"),
        ("neovim", "browse_filesystem", "good", False, "cli", "Oil.nvim and neo-tree file navigation"),
        # Claude Code
        ("claude-code", "run_inference", "excellent", True, "cli", "Primary CLI agent for Opus 4.6 reasoning"),
        ("claude-code", "modify_file", "excellent", True, "cli", "Edit tool for targeted file modifications"),
        ("claude-code", "dispatch_task", "excellent", True, "cli", "Task tool for subagent dispatch"),
        ("claude-code", "run_script", "excellent", True, "cli", "Bash tool for command execution"),
        ("claude-code", "semantic_search", "good", False, "mcp", "Via Qdrant/Graphiti MCP servers"),
        ("claude-code", "coordinate_agents", "excellent", True, "cli", "Native team and Task tool coordination"),
        ("claude-code", "code_review", "excellent", True, "cli", "Inline code analysis and suggestions"),
        ("claude-code", "generate_report", "excellent", True, "cli", "Structured output generation"),
        # Cursor
        ("cursor", "modify_file", "excellent", False, "native", "AI-assisted code editing with Cmd+K"),
        ("cursor", "refactor_code", "excellent", False, "native", "AI-powered code refactoring"),
        ("cursor", "run_inference", "good", False, "native", "Integrated chat with multiple models"),
        ("cursor", "lint_code", "good", False, "native", "LSP integration for diagnostics"),
        ("cursor", "code_review", "good", False, "native", "Inline code suggestions and review"),
        # ChatGPT
        ("chatgpt", "run_inference", "excellent", False, "api", "GPT-5/5.3-codex via desktop or web"),
        ("chatgpt", "summarize", "excellent", False, "api", "Long document summarization"),
        ("chatgpt", "research_synthesize", "good", False, "api", "Web-browsing research mode"),
        ("chatgpt", "compose_message", "good", False, "api", "Draft messages and communications"),
        ("chatgpt", "classify", "good", False, "api", "Content classification and tagging"),
        # Notion
        ("notion", "persist_file", "good", False, "api", "Document storage in Notion pages"),
        ("notion", "generate_report", "good", False, "api", "Structured report pages with databases"),
        ("notion", "post_update", "good", False, "api", "Status updates in Notion databases"),
        ("notion", "capture_text", "good", False, "api", "Quick capture via web clipper or API"),
        # Linear
        ("linear", "post_update", "excellent", True, "mcp", "Primary issue tracker for T1a operations"),
        ("linear", "dispatch_task", "good", False, "mcp", "Issue creation as task dispatch"),
        ("linear", "track_metrics", "good", False, "mcp", "Cycle time and velocity tracking"),
        ("linear", "query_database", "good", False, "mcp", "Issue queries via MCP/GraphQL"),
        ("linear", "schedule_workflow", "basic", False, "mcp", "Workflow state automation"),
        # ClickUp
        ("clickup", "post_update", "good", False, "mcp", "T1b task tracking"),
        ("clickup", "dispatch_task", "good", False, "mcp", "Task creation in ClickUp spaces"),
        ("clickup", "track_metrics", "basic", False, "mcp", "Basic time and status tracking"),
        ("clickup", "query_database", "good", False, "mcp", "Task queries via MCP API"),
        # Git
        ("git", "push_code", "excellent", True, "cli", "Primary VCS for all code operations"),
        ("git", "merge_changes", "excellent", True, "cli", "Branch merging and conflict resolution"),
        ("git", "archive_content", "good", False, "cli", "Version history as content archive"),
        ("git", "check_integrity", "good", False, "cli", "Status, diff, and log verification"),
        ("git", "release_version", "excellent", True, "cli", "Tag-based versioning"),
        ("git", "audit_trail", "excellent", True, "cli", "Commit log as authoritative audit trail"),
        # gh (GitHub CLI)
        ("gh", "push_code", "good", False, "cli", "PR creation and management"),
        ("gh", "code_review", "good", False, "cli", "PR review via gh pr review"),
        ("gh", "post_update", "good", False, "cli", "Issue/PR comments and labels"),
        ("gh", "query_database", "good", False, "cli", "API queries for repo metadata"),
        ("gh", "release_version", "good", False, "cli", "GitHub Releases management"),
        # lazygit
        ("lazygit", "merge_changes", "excellent", False, "cli", "Visual git merge and rebase interface"),
        ("lazygit", "browse_filesystem", "good", False, "cli", "Visual file staging and navigation"),
        ("lazygit", "push_code", "good", False, "cli", "Interactive push with branch selection"),
        ("lazygit", "check_integrity", "good", False, "cli", "Visual diff and status overview"),
        # tmux
        ("tmux", "switch_context", "excellent", True, "cli", "Primary pane/window context switching"),
        ("tmux", "coordinate_agents", "good", False, "cli", "Multi-pane agent workspace management"),
        ("tmux", "run_script", "good", False, "cli", "Send-keys for script execution in panes"),
        # ghostty
        ("ghostty", "run_script", "excellent", True, "native", "Primary terminal emulator for all CLI ops"),
        ("ghostty", "switch_context", "good", False, "native", "Tab/split-based context switching"),
        ("ghostty", "capture_text", "basic", False, "native", "Terminal output capture"),
        # Raycast
        ("raycast", "execute_macro", "excellent", True, "native", "Primary launcher and macro execution"),
        ("raycast", "browse_web", "good", False, "native", "Quick web search and URL launching"),
        ("raycast", "switch_context", "good", False, "native", "App switching and window management"),
        ("raycast", "capture_text", "good", False, "native", "Clipboard history and snippets"),
        ("raycast", "run_script", "good", False, "scripted", "Script commands and extensions"),
        # Figma
        ("figma", "render_markdown", "basic", False, "native", "Design artifact presentation"),
        ("figma", "compose_message", "basic", False, "native", "Design annotation and commenting"),
        ("figma", "capture_screenshot", "good", False, "native", "Design frame export"),
        # Slack
        ("slack", "send_message", "excellent", True, "api", "Primary team communication channel"),
        ("slack", "notify_agent", "good", False, "api", "Webhook-based agent notifications"),
        ("slack", "post_update", "good", False, "api", "Channel updates and thread replies"),
        ("slack", "compose_message", "good", False, "native", "Message drafting with formatting"),
        # Discord
        ("discord", "send_message", "good", False, "api", "Community communication channel"),
        ("discord", "notify_agent", "good", False, "api", "Bot-based notifications"),
        ("discord", "post_update", "basic", False, "api", "Channel announcements"),
        # Perplexity
        ("perplexity", "browse_web", "excellent", True, "api", "Primary web research with citations"),
        ("perplexity", "research_synthesize", "excellent", True, "api", "Multi-source research synthesis"),
        ("perplexity", "summarize", "good", False, "api", "Source-backed summarization"),
        ("perplexity", "query_database", "good", False, "api", "Structured knowledge queries"),
        # Gemini CLI
        ("gemini-cli", "run_inference", "excellent", False, "cli", "Gemini 2.5 Pro reasoning via CLI"),
        ("gemini-cli", "corpus_survey", "excellent", True, "cli", "Long-context vault surveys (1M tokens)"),
        ("gemini-cli", "summarize", "good", False, "cli", "Document summarization"),
        ("gemini-cli", "research_synthesize", "good", False, "cli", "Multi-file synthesis"),
        ("gemini-cli", "extract_entities", "good", False, "cli", "Entity extraction from large corpora"),
        # Codex CLI
        ("codex-cli", "run_inference", "good", False, "cli", "GPT-5.3-codex via Codex CLI"),
        ("codex-cli", "modify_file", "good", False, "cli", "File editing with full-auto mode"),
        ("codex-cli", "run_script", "good", False, "cli", "Command execution in sandbox"),
        ("codex-cli", "validate_schema", "good", False, "cli", "Schema validation tasks"),
        ("codex-cli", "lint_code", "good", False, "cli", "Code quality checks"),
        # OpenClaw
        ("openclaw", "run_inference", "good", False, "api", "Multi-model gateway for agent orchestration"),
        ("openclaw", "coordinate_agents", "good", False, "api", "Agent management via OpenClaw framework"),
        ("openclaw", "dispatch_task", "good", False, "api", "Task routing through gateway"),
        ("openclaw", "send_message", "good", False, "api", "Inter-agent messaging via plugins"),
        # Ollama
        ("ollama", "run_inference", "good", False, "api", "Local model inference (Llama, etc.)"),
        ("ollama", "embed_text", "good", False, "api", "Local embedding generation"),
        ("ollama", "fine_tune", "basic", False, "api", "Model customization via Modelfile"),
        # Docker Desktop
        ("docker-desktop", "build_artifact", "excellent", True, "cli", "Container image building and management"),
        ("docker-desktop", "release_version", "good", False, "cli", "Image versioning and registry push"),
        ("docker-desktop", "health_check", "good", False, "cli", "Container health monitoring"),
        ("docker-desktop", "sandbox_operation", "excellent", True, "cli", "Isolated execution environments"),
        # ripgrep
        ("ripgrep", "keyword_search", "excellent", False, "cli", "Ultra-fast content search across codebase"),
        ("ripgrep", "check_integrity", "good", False, "cli", "Pattern verification in source files"),
        # fzf
        ("fzf", "browse_filesystem", "excellent", True, "cli", "Fuzzy file and content finder"),
        ("fzf", "keyword_search", "good", False, "cli", "Interactive fuzzy search"),
        ("fzf", "switch_context", "good", False, "cli", "Quick selection for context switching"),
        # 1password
        ("1password", "manage_credentials", "excellent", True, "cli", "Primary credential vault and manager"),
        ("1password", "rotate_keys", "good", False, "cli", "Password and key rotation"),
        ("1password", "encrypt_data", "good", False, "native", "Secure note and document encryption"),
        ("1password", "audit_trail", "good", False, "native", "Access log and credential audit"),
        # DEVONthink
        ("devonthink", "index_document", "excellent", False, "scripted", "Advanced document indexing and AI classification"),
        ("devonthink", "archive_content", "excellent", True, "scripted", "Long-term document archival with metadata"),
        ("devonthink", "semantic_search", "good", False, "scripted", "AI-powered document search"),
        ("devonthink", "capture_url", "good", False, "scripted", "Web archive and clipping"),
        ("devonthink", "classify", "good", False, "scripted", "Auto-classification of documents"),
        # Zotero
        ("zotero", "capture_url", "excellent", True, "scripted", "Academic reference capture and management"),
        ("zotero", "index_document", "good", False, "scripted", "Research paper indexing with metadata"),
        ("zotero", "archive_content", "good", False, "scripted", "Reference library archival"),
        # Airtable
        ("airtable", "query_database", "excellent", True, "mcp", "Structured data queries via MCP"),
        ("airtable", "persist_file", "good", False, "mcp", "Record creation and update"),
        ("airtable", "generate_report", "good", False, "mcp", "View-based reporting"),
        ("airtable", "track_metrics", "good", False, "mcp", "Dashboard and summary views"),
        ("airtable", "classify", "good", False, "mcp", "Multi-select and linked record classification"),
        # Keyboard Maestro
        ("keyboard-maestro", "execute_macro", "excellent", False, "native", "Complex multi-step macro automation"),
        ("keyboard-maestro", "trigger_webhook", "good", False, "native", "HTTP request actions in macros"),
        ("keyboard-maestro", "run_script", "good", False, "native", "Script execution within macros"),
        ("keyboard-maestro", "schedule_cron", "good", False, "native", "Time-based macro triggers"),
        ("keyboard-maestro", "switch_context", "good", False, "native", "App/window manipulation macros"),
        # Hazel
        ("hazel", "archive_content", "excellent", True, "native", "Automated file organization and archival"),
        ("hazel", "classify", "excellent", True, "native", "Rule-based file classification"),
        ("hazel", "run_script", "good", False, "native", "Shell script actions on file events"),
        # Things 3
        ("things3", "dispatch_task", "good", False, "native", "Personal task creation and management"),
        ("things3", "schedule_workflow", "good", False, "native", "Project and area organization"),
        ("things3", "prioritize", "good", False, "native", "Today/upcoming priority management"),
        ("things3", "commit_to", "good", False, "native", "Task acceptance and deadline setting"),
        # Brave Browser
        ("brave-browser", "browse_web", "excellent", False, "native", "Primary web browser with privacy"),
        ("brave-browser", "capture_url", "good", False, "native", "Bookmark and reading list capture"),
        ("brave-browser", "research_synthesize", "basic", False, "native", "Tab-based multi-source research"),
        ("brave-browser", "capture_screenshot", "good", False, "native", "Full-page and region screenshots"),
        # sesh
        ("sesh", "switch_context", "excellent", False, "cli", "tmux session management and switching"),
        # starship
        ("starship", "render_markdown", "basic", False, "native", "Shell prompt context rendering"),
        ("starship", "health_check", "basic", False, "native", "Git status and env indicators in prompt"),
        # whisper-cpp
        ("whisper-cpp", "capture_audio", "excellent", True, "cli", "Primary speech-to-text transcription"),
        ("whisper-cpp", "transform_text", "good", False, "cli", "Audio-to-text format conversion"),
        # bat
        ("bat", "render_markdown", "good", False, "cli", "Syntax-highlighted file viewing"),
        ("bat", "browse_filesystem", "good", False, "cli", "File content preview with line numbers"),
        # fd
        ("fd", "browse_filesystem", "excellent", False, "cli", "Fast file finding by name/pattern"),
        # yazi
        ("yazi", "browse_filesystem", "excellent", False, "cli", "Terminal file manager with preview"),
        ("yazi", "switch_context", "good", False, "cli", "Directory navigation and switching"),
        ("yazi", "persist_file", "basic", False, "cli", "File move/copy/rename operations"),
        # atuin
        ("atuin", "audit_trail", "excellent", True, "cli", "Shell command history with context"),
        ("atuin", "keyword_search", "good", False, "cli", "Fuzzy search across command history"),
        ("atuin", "query_database", "good", False, "cli", "SQLite-backed history queries"),
    ]

    count = 0
    for (app_slug, action_code, quality_rating, is_primary,
         automation_support, notes) in mappings:
        app_id = app_map.get(app_slug)
        action_id = action_map.get(action_code)
        if not app_id:
            print(f"  WARN: app_actions - unknown app slug: {app_slug}")
            continue
        if not action_id:
            print(f"  WARN: app_actions - unknown action code: {action_code}")
            continue
        try:
            cur.execute(
                """INSERT INTO app_actions
                   (app_id, action_type_id, quality_rating, is_primary, automation_support, notes)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (app_id, action_id, quality_rating, is_primary, automation_support, notes),
            )
            count += 1
        except sqlite3.IntegrityError as e:
            print(f"  WARN: app_actions {app_slug}/{action_code}: {e}")
    conn.commit()
    return count


def seed_agent_bindings(conn):
    """Populate agent_bindings — Phase B.

    Maps 6 Constellation agents to app-action bindings.
    ~120 rows covering primary, secondary, fallback, and experimental bindings.
    """
    cur = conn.cursor()

    # Build lookups
    cur.execute("SELECT id, slug FROM apps")
    app_map = {row[1]: row[0] for row in cur.fetchall()}

    cur.execute("SELECT id, code FROM action_types")
    action_map = {row[1]: row[0] for row in cur.fetchall()}

    # (agent_code, app_slug, action_code, binding_strength, invocation_method, frequency, notes)
    bindings = [
        # === SOVEREIGN (human, GUI interactions) ===
        ("sovereign", "obsidian", "capture_text", "primary", "gui", "constant", "Primary knowledge capture interface"),
        ("sovereign", "obsidian", "modify_file", "primary", "gui", "frequent", "Direct note editing in vault"),
        ("sovereign", "obsidian", "keyword_search", "primary", "gui", "frequent", "Vault search for decision context"),
        ("sovereign", "obsidian", "approve", "primary", "gui", "frequent", "Sovereign authorization gate via vault decisions"),
        ("sovereign", "obsidian", "allocate_attention", "primary", "gui", "constant", "Direct cognitive resources via vault planning"),
        ("sovereign", "obsidian", "set_boundary", "primary", "gui", "periodic", "Define operational limits in vault notes"),
        ("sovereign", "brave-browser", "browse_web", "primary", "gui", "frequent", "Web research and information gathering"),
        ("sovereign", "brave-browser", "capture_url", "primary", "gui", "frequent", "Bookmark strategic references"),
        ("sovereign", "slack", "send_message", "primary", "gui", "frequent", "Team and external communication"),
        ("sovereign", "slack", "compose_message", "primary", "gui", "frequent", "Draft communications"),
        ("sovereign", "discord", "send_message", "secondary", "gui", "periodic", "Community engagement"),
        ("sovereign", "things3", "dispatch_task", "primary", "gui", "frequent", "Personal task management"),
        ("sovereign", "things3", "prioritize", "primary", "gui", "frequent", "Daily priority decisions"),
        ("sovereign", "things3", "commit_to", "primary", "gui", "frequent", "Accept obligations with deadlines"),
        ("sovereign", "things3", "decline", "primary", "gui", "periodic", "Refuse obligations via task rejection"),
        ("sovereign", "things3", "renegotiate", "primary", "gui", "periodic", "Modify commitment terms via task updates"),
        ("sovereign", "notion", "capture_text", "secondary", "gui", "periodic", "Supplementary knowledge capture"),
        ("sovereign", "notion", "generate_report", "secondary", "gui", "periodic", "Report viewing and annotation"),
        ("sovereign", "linear", "post_update", "secondary", "gui", "periodic", "Review and update Linear issues"),
        ("sovereign", "clickup", "post_update", "secondary", "gui", "periodic", "Review T1b task status"),
        ("sovereign", "figma", "render_markdown", "secondary", "gui", "rare", "Design review and annotation"),
        # === COMMANDER (Claude Opus 4.6, multi-tool MCP) ===
        ("commander", "claude-code", "run_inference", "primary", "cli", "constant", "Primary reasoning engine"),
        ("commander", "claude-code", "modify_file", "primary", "cli", "constant", "File editing via Edit tool"),
        ("commander", "claude-code", "dispatch_task", "primary", "cli", "frequent", "Subagent and team dispatch"),
        ("commander", "claude-code", "run_script", "primary", "cli", "constant", "Bash command execution"),
        ("commander", "claude-code", "coordinate_agents", "primary", "cli", "frequent", "Multi-agent coordination"),
        ("commander", "claude-code", "code_review", "primary", "cli", "frequent", "Code analysis and review"),
        ("commander", "claude-code", "generate_report", "primary", "cli", "frequent", "Structured report generation"),
        ("commander", "claude-code", "research_synthesize", "primary", "cli", "frequent", "Multi-source research"),
        ("commander", "claude-code", "clarescence", "primary", "cli", "periodic", "Decision space refinement"),
        ("commander", "obsidian", "capture_text", "primary", "mcp", "frequent", "Vault writes via Obsidian MCP"),
        ("commander", "obsidian", "keyword_search", "primary", "mcp", "frequent", "Vault search via MCP"),
        ("commander", "obsidian", "modify_file", "primary", "mcp", "frequent", "Note editing via MCP"),
        ("commander", "linear", "post_update", "primary", "mcp", "frequent", "T1a issue management via MCP"),
        ("commander", "linear", "query_database", "primary", "mcp", "frequent", "Issue queries via GraphQL"),
        ("commander", "linear", "dispatch_task", "secondary", "mcp", "periodic", "Issue creation as task proxy"),
        ("commander", "clickup", "post_update", "primary", "mcp", "periodic", "T1b task updates via MCP"),
        ("commander", "clickup", "query_database", "primary", "mcp", "periodic", "Task queries via API"),
        ("commander", "git", "push_code", "primary", "cli", "frequent", "Code commits and pushes"),
        ("commander", "git", "merge_changes", "primary", "cli", "periodic", "Branch management"),
        ("commander", "git", "check_integrity", "primary", "cli", "constant", "Status verification"),
        ("commander", "git", "audit_trail", "primary", "cli", "constant", "Commit log management"),
        ("commander", "gh", "push_code", "secondary", "cli", "periodic", "PR creation and management"),
        ("commander", "gh", "code_review", "secondary", "cli", "periodic", "PR review operations"),
        ("commander", "ripgrep", "keyword_search", "primary", "cli", "constant", "Codebase text search"),
        ("commander", "fzf", "browse_filesystem", "secondary", "cli", "frequent", "Fuzzy file finding"),
        ("commander", "tmux", "switch_context", "primary", "cli", "frequent", "Pane and session management"),
        ("commander", "tmux", "coordinate_agents", "secondary", "cli", "periodic", "Multi-pane workspace ops"),
        ("commander", "airtable", "query_database", "secondary", "mcp", "periodic", "Structured data queries"),
        ("commander", "docker-desktop", "sandbox_operation", "secondary", "cli", "periodic", "Container-based isolation"),
        ("commander", "docker-desktop", "health_check", "secondary", "cli", "periodic", "Service health monitoring"),
        # === ADJUDICATOR (Codex CLI, GPT-5.3-codex) ===
        ("adjudicator", "codex-cli", "run_inference", "primary", "cli", "constant", "Primary reasoning via GPT-5.3-codex"),
        ("adjudicator", "codex-cli", "modify_file", "primary", "cli", "constant", "File editing in full-auto mode"),
        ("adjudicator", "codex-cli", "run_script", "primary", "cli", "frequent", "Command execution"),
        ("adjudicator", "codex-cli", "validate_schema", "primary", "cli", "frequent", "Schema and data validation"),
        ("adjudicator", "codex-cli", "lint_code", "primary", "cli", "frequent", "Code quality enforcement"),
        ("adjudicator", "codex-cli", "run_tests", "primary", "cli", "frequent", "Test suite execution via Codex CLI"),
        ("adjudicator", "codex-cli", "check_integrity", "primary", "cli", "frequent", "Data integrity verification via Codex CLI"),
        ("adjudicator", "git", "push_code", "primary", "cli", "frequent", "Commit and push completed work"),
        ("adjudicator", "git", "check_integrity", "primary", "cli", "constant", "Working tree verification"),
        ("adjudicator", "git", "audit_trail", "secondary", "cli", "frequent", "Commit log entries"),
        ("adjudicator", "neovim", "modify_file", "secondary", "cli", "periodic", "Direct file editing when needed"),
        ("adjudicator", "neovim", "refactor_code", "secondary", "cli", "periodic", "Code restructuring"),
        ("adjudicator", "neovim", "lint_code", "secondary", "cli", "periodic", "LSP diagnostics"),
        ("adjudicator", "ripgrep", "keyword_search", "primary", "cli", "constant", "Pattern search for validation"),
        ("adjudicator", "ripgrep", "check_integrity", "secondary", "cli", "frequent", "Reference verification"),
        ("adjudicator", "fd", "browse_filesystem", "primary", "cli", "frequent", "Fast file discovery"),
        ("adjudicator", "bat", "render_markdown", "secondary", "cli", "frequent", "Syntax-highlighted file review"),
        ("adjudicator", "bat", "browse_filesystem", "secondary", "cli", "frequent", "File content inspection"),
        # === CARTOGRAPHER (Gemini CLI, Gemini 2.5 Pro) ===
        ("cartographer", "gemini-cli", "run_inference", "primary", "cli", "constant", "Primary reasoning via Gemini 2.5 Pro"),
        ("cartographer", "gemini-cli", "corpus_survey", "primary", "cli", "frequent", "Long-context vault surveys"),
        ("cartographer", "gemini-cli", "summarize", "primary", "cli", "frequent", "Document distillation"),
        ("cartographer", "gemini-cli", "research_synthesize", "primary", "cli", "frequent", "Multi-source synthesis"),
        ("cartographer", "gemini-cli", "extract_entities", "primary", "cli", "periodic", "Entity extraction from corpora"),
        ("cartographer", "obsidian", "keyword_search", "secondary", "mcp", "frequent", "Vault search for survey context"),
        ("cartographer", "obsidian", "capture_text", "secondary", "mcp", "periodic", "Survey result persistence"),
        ("cartographer", "ripgrep", "keyword_search", "primary", "cli", "constant", "Codebase content search"),
        ("cartographer", "fd", "browse_filesystem", "primary", "cli", "frequent", "File discovery for surveys"),
        ("cartographer", "git", "check_integrity", "secondary", "cli", "periodic", "Repo state verification"),
        ("cartographer", "git", "audit_trail", "secondary", "cli", "periodic", "History analysis"),
        ("cartographer", "perplexity", "browse_web", "secondary", "api", "periodic", "Web research for intelligence"),
        ("cartographer", "perplexity", "research_synthesize", "secondary", "api", "periodic", "External source synthesis"),
        # === PSYCHE (OpenClaw, GPT-5.3-codex) ===
        ("psyche", "openclaw", "run_inference", "primary", "api", "constant", "GPT-5.3-codex via OpenClaw gateway"),
        ("psyche", "openclaw", "coordinate_agents", "primary", "api", "frequent", "Agent management via OpenClaw"),
        ("psyche", "openclaw", "dispatch_task", "primary", "api", "frequent", "Task routing through gateway"),
        ("psyche", "openclaw", "send_message", "primary", "api", "frequent", "Inter-agent messaging"),
        ("psyche", "openclaw", "trigger_webhook", "secondary", "api", "periodic", "Automation triggers via OpenClaw"),
        ("psyche", "openclaw", "schedule_cron", "secondary", "api", "rare", "Automation scheduling via OpenClaw"),
        ("psyche", "openclaw", "pipeline_fusion", "primary", "api", "periodic", "Pipeline wiring via OpenClaw"),
        ("psyche", "openclaw", "run_script", "secondary", "cli", "frequent", "System cohesion scripts via OpenClaw"),
        ("psyche", "openclaw", "health_check", "secondary", "cli", "periodic", "Service monitoring via OpenClaw"),
        ("psyche", "git", "push_code", "secondary", "cli", "periodic", "Commit system cohesion changes"),
        ("psyche", "git", "check_integrity", "secondary", "cli", "frequent", "Repo state verification"),
        ("psyche", "obsidian", "modify_file", "secondary", "mcp", "periodic", "Vault writes via MCP adapter"),
        ("psyche", "obsidian", "keyword_search", "secondary", "mcp", "periodic", "Vault search for policy context"),
        # === AJNA (OpenClaw on MBA, Kimi K2.5) ===
        ("ajna", "openclaw", "run_inference", "primary", "api", "constant", "Kimi K2.5 via NVIDIA NIM API"),
        ("ajna", "openclaw", "coordinate_agents", "primary", "api", "frequent", "Strategic dispatch optimization"),
        ("ajna", "openclaw", "dispatch_task", "secondary", "api", "periodic", "Strategic task routing"),
        ("ajna", "openclaw", "clarescence", "secondary", "api", "periodic", "Strategic decision refinement via OpenClaw"),
        ("ajna", "openclaw", "prioritize", "primary", "api", "frequent", "Strategic priority reordering via OpenClaw"),
        ("ajna", "openclaw", "allocate_attention", "secondary", "api", "periodic", "Macro attention allocation via OpenClaw"),
        ("ajna", "openclaw", "research_synthesize", "secondary", "api", "periodic", "Strategic research synthesis via OpenClaw"),
        ("ajna", "openclaw", "blitzkrieg_dispatch", "experimental", "api", "rare", "Parallel strategic dispatch via OpenClaw"),
        ("ajna", "git", "push_code", "secondary", "cli", "periodic", "MBA-side commits"),
        ("ajna", "git", "check_integrity", "secondary", "cli", "frequent", "MBA repo state verification"),
        ("ajna", "obsidian", "keyword_search", "experimental", "mcp", "rare", "Vault search (MBA MCP pending config)"),
    ]

    count = 0
    for (agent_code, app_slug, action_code, binding_strength,
         invocation_method, frequency, notes) in bindings:
        app_id = app_map.get(app_slug)
        action_id = action_map.get(action_code)
        if not app_id:
            print(f"  WARN: agent_bindings - unknown app slug: {app_slug}")
            continue
        if not action_id:
            print(f"  WARN: agent_bindings - unknown action code: {action_code}")
            continue
        try:
            cur.execute(
                """INSERT INTO agent_bindings
                   (agent_code, app_id, action_type_id, binding_strength,
                    invocation_method, frequency, notes)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (agent_code, app_id, action_id, binding_strength,
                 invocation_method, frequency, notes),
            )
            count += 1
        except sqlite3.IntegrityError as e:
            print(f"  WARN: agent_bindings {agent_code}/{app_slug}/{action_code}: {e}")
    conn.commit()
    return count


def seed_workflow_templates(conn):
    """Populate workflow_templates — Phase B.

    11 templates: 6 formalized from existing apparatus + 5 new.
    """
    cur = conn.cursor()

    # Build apparatus lookup
    cur.execute("SELECT id, code FROM apparatus")
    apparatus_map = {row[1]: row[0] for row in cur.fetchall()}

    # (code, name, description, apparatus_code_or_None, use_frequency, avg_duration_minutes)
    templates = [
        ("wf_research", "Research & Synthesis", "Multi-source research with structured synthesis output", "research_apparatus", "frequent", 45),
        ("wf_writing", "Writing & Publishing", "Draft, refine, review, and publish written content", "writing_apparatus", "frequent", 60),
        ("wf_coding", "Software Development", "Implement, test, review, and deploy code changes", "coding_apparatus", "constant", 90),
        ("wf_design", "Design & Creation", "Create, iterate, and finalize design artifacts", "design_apparatus", "periodic", 120),
        ("wf_analysis", "Data Analysis", "Collect, process, analyze, and present data insights", "analysis_apparatus", "frequent", 30),
        ("wf_communication", "Communication & Collaboration", "Draft, review, send, and follow up on communications", "communication_apparatus", "constant", 15),
        ("wf_orchestration", "Agent Orchestration", "Dispatch, coordinate, and collect results from multiple agents", None, "constant", 20),
        ("wf_sensing", "Sensing & Intelligence", "Detect changes, ingest signals, classify, and route to handlers", None, "frequent", 10),
        ("wf_deployment", "Build & Deployment", "Build artifacts, run checks, version, and deploy to targets", None, "periodic", 30),
        ("wf_maintenance", "System Maintenance", "Health check, diagnose, fix, and verify system components", None, "periodic", 25),
        ("wf_clarescence", "Clarescence Protocol", "Multi-pass progressive refinement of a decision space", None, "periodic", 40),
    ]

    count = 0
    for (code, name, description, apparatus_code, use_frequency, avg_duration) in templates:
        apparatus_id = apparatus_map.get(apparatus_code) if apparatus_code else None
        try:
            cur.execute(
                """INSERT INTO workflow_templates
                   (code, name, description, apparatus_id, use_frequency, average_duration_minutes)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (code, name, description, apparatus_id, use_frequency, avg_duration),
            )
            count += 1
        except sqlite3.IntegrityError as e:
            print(f"  WARN: workflow_templates {code}: {e}")
    conn.commit()
    return count


def seed_workflow_steps(conn):
    """Populate workflow_steps — Phase B.

    72 steps across 11 workflow templates.
    """
    cur = conn.cursor()

    # Build lookups
    cur.execute("SELECT id, code FROM workflow_templates")
    wf_map = {row[1]: row[0] for row in cur.fetchall()}

    cur.execute("SELECT id, slug FROM apps")
    app_map = {row[1]: row[0] for row in cur.fetchall()}

    # (workflow_code, step_number, app_slug, action_description,
    #  input_from_previous, output_to_next, avg_duration_minutes, notes)
    steps = [
        # wf_research (7 steps)
        ("wf_research", 1, "obsidian", "Define research question and scope in vault note", "none", "research brief", 5, "Capture objective and boundaries"),
        ("wf_research", 2, "perplexity", "Search web for primary sources with citations", "research brief", "source list", 10, "Use focused queries from brief"),
        ("wf_research", 3, "gemini-cli", "Deep-read and extract entities from long sources", "source list", "extracted data", 10, "Leverage 1M token context"),
        ("wf_research", 4, "claude-code", "Synthesize findings into structured analysis", "extracted data", "synthesis draft", 10, "Cross-reference multiple sources"),
        ("wf_research", 5, "obsidian", "Persist synthesis as canonical vault document", "synthesis draft", "vault document", 5, "Apply frontmatter and tags"),
        ("wf_research", 6, "git", "Commit research artifact with semantic prefix", "vault document", "committed file", 2, "docs: or feat: prefix"),
        ("wf_research", 7, "linear", "Update relevant SYN issue with research outcome", "committed file", "issue updated", 3, "Link commit to issue"),
        # wf_writing (7 steps)
        ("wf_writing", 1, "obsidian", "Create draft document with outline structure", "none", "outline", 5, "Use templates for structure"),
        ("wf_writing", 2, "claude-code", "Generate first draft from outline and context", "outline", "first draft", 15, "Provide relevant vault context"),
        ("wf_writing", 3, "neovim", "Edit and refine draft for voice and precision", "first draft", "refined draft", 15, "Human-in-the-loop editing"),
        ("wf_writing", 4, "claude-code", "Review for coherence, style, and completeness", "refined draft", "review notes", 10, "Check against standards"),
        ("wf_writing", 5, "neovim", "Apply final edits from review feedback", "review notes", "final draft", 10, "Sovereign review if needed"),
        ("wf_writing", 6, "git", "Commit final document to repository", "final draft", "committed file", 2, "docs: prefix"),
        ("wf_writing", 7, "obsidian", "Cross-link document to related vault notes", "committed file", "linked document", 3, "Update backlinks and tags"),
        # wf_coding (8 steps)
        ("wf_coding", 1, "claude-code", "Analyze requirements and design implementation plan", "none", "implementation plan", 10, "Read relevant code first"),
        ("wf_coding", 2, "claude-code", "Implement code changes across target files", "implementation plan", "code changes", 30, "Edit tool for precise modifications"),
        ("wf_coding", 3, "codex-cli", "Run test suite and validate changes", "code changes", "test results", 10, "Adjudicator validation"),
        ("wf_coding", 4, "ripgrep", "Verify no broken references or orphaned code", "test results", "integrity report", 5, "grep for removed identifiers"),
        ("wf_coding", 5, "neovim", "Manual review and refinement of edge cases", "integrity report", "reviewed code", 15, "Human review for complex changes"),
        ("wf_coding", 6, "git", "Stage and commit with semantic message", "reviewed code", "commit", 5, "feat:/fix:/refactor: prefix"),
        ("wf_coding", 7, "gh", "Create PR if branch-based workflow", "commit", "pull request", 5, "Include test evidence"),
        ("wf_coding", 8, "linear", "Update SYN issue status and link commit", "pull request", "issue updated", 5, "Close or advance issue"),
        # wf_design (7 steps)
        ("wf_design", 1, "obsidian", "Capture design brief and requirements", "none", "design brief", 10, "Reference existing patterns"),
        ("wf_design", 2, "figma", "Create initial design mockups and wireframes", "design brief", "mockups", 40, "Iterate on layout and hierarchy"),
        ("wf_design", 3, "claude-code", "Review design against system patterns and constraints", "mockups", "design feedback", 15, "Check consistency with Canon"),
        ("wf_design", 4, "figma", "Refine design based on feedback", "design feedback", "refined design", 30, "Apply systematic corrections"),
        ("wf_design", 5, "obsidian", "Document design decisions and rationale", "refined design", "design doc", 15, "Persist to vault"),
        ("wf_design", 6, "git", "Commit design documentation", "design doc", "committed file", 5, "docs: prefix"),
        ("wf_design", 7, "linear", "Update project issue with design artifacts", "committed file", "issue updated", 5, "Link to design files"),
        # wf_analysis (6 steps)
        ("wf_analysis", 1, "airtable", "Query structured data from relevant bases", "none", "raw data", 5, "Use MCP for queries"),
        ("wf_analysis", 2, "claude-code", "Process and transform data for analysis", "raw data", "processed data", 5, "Clean and normalize"),
        ("wf_analysis", 3, "claude-code", "Run analytical queries and compute metrics", "processed data", "analysis results", 10, "Statistical summaries"),
        ("wf_analysis", 4, "claude-code", "Generate structured report with findings", "analysis results", "analysis report", 5, "Markdown tables and charts"),
        ("wf_analysis", 5, "obsidian", "Persist analysis report to vault", "analysis report", "vault document", 3, "Apply appropriate tags"),
        ("wf_analysis", 6, "git", "Commit analysis artifact", "vault document", "committed file", 2, "docs: or feat: prefix"),
        # wf_communication (6 steps)
        ("wf_communication", 1, "obsidian", "Draft communication content and key points", "none", "draft content", 3, "Reference relevant context"),
        ("wf_communication", 2, "claude-code", "Refine message for audience and channel", "draft content", "refined message", 3, "Adjust tone and format"),
        ("wf_communication", 3, "slack", "Send message to appropriate channel or DM", "refined message", "sent message", 2, "Or discord/email as needed"),
        ("wf_communication", 4, "linear", "Log communication outcome if project-relevant", "sent message", "logged event", 2, "Update issue if applicable"),
        ("wf_communication", 5, "obsidian", "Archive significant communications in vault", "logged event", "archived record", 3, "For decisions and agreements"),
        ("wf_communication", 6, "atuin", "Command history preserves execution context", "archived record", "history entry", 2, "Automatic via shell integration"),
        # wf_orchestration (6 steps)
        ("wf_orchestration", 1, "claude-code", "Assess task scope and decompose into subtasks", "none", "task decomposition", 3, "Identify parallelizable work"),
        ("wf_orchestration", 2, "claude-code", "Dispatch tasks to appropriate agents via inbox", "task decomposition", "dispatched tasks", 3, "Use dispatch.sh or Task tool"),
        ("wf_orchestration", 3, "tmux", "Monitor agent panes for progress signals", "dispatched tasks", "progress signals", 5, "Visual monitoring across panes"),
        ("wf_orchestration", 4, "claude-code", "Collect and integrate results from agents", "progress signals", "integrated results", 5, "Read RESULT/CONFIRM files"),
        ("wf_orchestration", 5, "git", "Commit integrated results", "integrated results", "committed files", 2, "Merge agent contributions"),
        ("wf_orchestration", 6, "linear", "Update tracking with orchestration outcome", "committed files", "issues updated", 2, "Close or advance issues"),
        # wf_sensing (5 steps)
        ("wf_sensing", 1, "ripgrep", "Scan filesystem for new or changed signals", "none", "change list", 2, "Monitor inbox and state files"),
        ("wf_sensing", 2, "claude-code", "Classify signal type and urgency", "change list", "classified signals", 2, "Route P0 immediately"),
        ("wf_sensing", 3, "obsidian", "Log signal to appropriate dynamic ledger", "classified signals", "ledger entry", 2, "DYN-GLOBAL_LEDGER.md"),
        ("wf_sensing", 4, "claude-code", "Route actionable signals to handler agents", "ledger entry", "dispatched actions", 2, "Trigger workflows or tasks"),
        ("wf_sensing", 5, "linear", "Create issue if signal warrants T1a tracking", "dispatched actions", "issue created", 2, "P0/P1 signals only"),
        # wf_deployment (7 steps)
        ("wf_deployment", 1, "claude-code", "Verify all changes committed and tests passing", "none", "readiness check", 3, "Pre-deployment validation"),
        ("wf_deployment", 2, "docker-desktop", "Build container image or artifact package", "readiness check", "build artifact", 5, "Versioned build"),
        ("wf_deployment", 3, "codex-cli", "Run deployment validation suite", "build artifact", "validation results", 5, "Schema, lint, integrity checks"),
        ("wf_deployment", 4, "git", "Tag release version and push", "validation results", "tagged release", 3, "Semantic versioning"),
        ("wf_deployment", 5, "gh", "Create GitHub release with changelog", "tagged release", "published release", 5, "Include build artifacts"),
        ("wf_deployment", 6, "claude-code", "Verify deployment health post-release", "published release", "health report", 5, "Run health checks"),
        ("wf_deployment", 7, "linear", "Close deployment issue and update project", "health report", "issue closed", 4, "Link release to issue"),
        # wf_maintenance (6 steps)
        ("wf_maintenance", 1, "claude-code", "Run health checks across all services", "none", "health report", 3, "8 services + launchd agents"),
        ("wf_maintenance", 2, "docker-desktop", "Check container status and resource usage", "health report", "container status", 3, "Neo4j, Graphiti, Qdrant"),
        ("wf_maintenance", 3, "claude-code", "Diagnose any failing services or anomalies", "container status", "diagnosis", 5, "Root cause analysis"),
        ("wf_maintenance", 4, "claude-code", "Apply fixes for diagnosed issues", "diagnosis", "fixes applied", 8, "Restart, config change, patch"),
        ("wf_maintenance", 5, "codex-cli", "Verify fixes and run regression checks", "fixes applied", "verification report", 4, "Adjudicator validation"),
        ("wf_maintenance", 6, "git", "Commit maintenance changes", "verification report", "committed fixes", 2, "fix: prefix"),
        # wf_clarescence (7 steps)
        ("wf_clarescence", 1, "claude-code", "Orient and situate: read Triumvirate, git status, inbox", "none", "orientation context", 5, "Pass 0: mandatory grounding"),
        ("wf_clarescence", 2, "claude-code", "Calibrate against intentions and verify current state", "orientation context", "calibration data", 5, "Pass 1: Triumvirate Calibration"),
        ("wf_clarescence", 3, "claude-code", "Run 18-lens sweep scoring pass/fail per lens", "calibration data", "lens scores", 8, "Pass 2: require >= 12/18"),
        ("wf_clarescence", 4, "obsidian", "Check Canon coherence and flag stale documents", "lens scores", "coherence report", 5, "Pass 3: Canon alignment"),
        ("wf_clarescence", 5, "claude-code", "Run remaining passes based on fidelity level", "coherence report", "analysis results", 10, "Passes 4-10 as needed"),
        ("wf_clarescence", 6, "obsidian", "Write clarescence record to impl/clarescence/", "analysis results", "clarescence record", 5, "Structured markdown artifact"),
        ("wf_clarescence", 7, "git", "Commit clarescence record", "clarescence record", "committed file", 2, "docs: prefix"),
    ]

    count = 0
    for (wf_code, step_number, app_slug, action_description,
         input_from, output_to, avg_duration, notes) in steps:
        wf_id = wf_map.get(wf_code)
        app_id = app_map.get(app_slug)
        if not wf_id:
            print(f"  WARN: workflow_steps - unknown workflow: {wf_code}")
            continue
        if not app_id:
            print(f"  WARN: workflow_steps - unknown app slug: {app_slug}")
            continue
        try:
            cur.execute(
                """INSERT INTO workflow_steps
                   (workflow_id, step_number, app_id, action_description,
                    input_from_previous_step, output_to_next_step, average_duration_minutes, notes)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (wf_id, step_number, app_id, action_description,
                 input_from, output_to, avg_duration, notes),
            )
            count += 1
        except sqlite3.IntegrityError as e:
            print(f"  WARN: workflow_steps {wf_code}/{step_number}: {e}")
    conn.commit()
    return count


def validate_integrity(conn):
    """Run data integrity checks and return results."""
    cur = conn.cursor()
    results = {}

    # Table row counts
    tables = [
        "layers", "roles", "object_types", "modalities", "lifecycle_states",
        "commercial_seams", "deployment_contexts", "apps", "models", "api_pricing",
        "app_modalities", "app_commercial_seams", "app_deployment_contexts",
        "model_capabilities",
        "primitives", "app_primitives", "primitive_dependencies",
        "apparatus", "apparatus_components", "usage_contexts",
        "app_relationships", "app_usage_contexts",
        "workflow_templates", "workflow_steps",
        "action_types", "app_actions", "agent_bindings",
        "projects", "tasks", "accounts", "platforms", "platform_roles", "sources",
        "filename_mappings", "rename_mappings",
    ]

    results["row_counts"] = {}
    for table in tables:
        try:
            cur.execute(f"SELECT COUNT(*) FROM {table}")
            results["row_counts"][table] = cur.fetchone()[0]
        except sqlite3.Error:
            results["row_counts"][table] = -1

    # Foreign key violations
    cur.execute("PRAGMA foreign_key_check")
    fk_violations = cur.fetchall()
    results["fk_violations"] = len(fk_violations)

    # Integrity check
    cur.execute("PRAGMA integrity_check")
    integrity = cur.fetchone()[0]
    results["integrity"] = integrity

    return results


def print_report(results, db_path):
    """Print a formatted summary report."""
    print("\n" + "=" * 60)
    print("  ONTOLOGY SUBSTRATE PILOT — BUILD REPORT")
    print("=" * 60)
    print(f"\n  Database: {db_path}")
    print(f"  Built:    {datetime.now().isoformat()}")

    print("\n  --- BEDROCK (Stable Taxonomies) ---")
    bedrock_tables = ["layers", "object_types", "commercial_seams", "modalities", "lifecycle_states", "deployment_contexts", "roles"]
    bedrock_total = 0
    for t in bedrock_tables:
        count = results["row_counts"].get(t, 0)
        bedrock_total += max(count, 0)
        print(f"  {t:30s} {count:>6d} rows")
    print(f"  {'BEDROCK TOTAL':30s} {bedrock_total:>6d}")

    print("\n  --- SETTLEMENTS (Dynamic Instances) ---")
    settlement_tables = ["apps", "models", "api_pricing"]
    settlement_total = 0
    for t in settlement_tables:
        count = results["row_counts"].get(t, 0)
        settlement_total += max(count, 0)
        print(f"  {t:30s} {count:>6d} rows")
    print(f"  {'SETTLEMENTS TOTAL':30s} {settlement_total:>6d}")

    print("\n  --- PRIMITIVES & INTELLIGENCE ---")
    intel_tables = ["primitives", "apparatus", "usage_contexts"]
    intel_total = 0
    for t in intel_tables:
        count = results["row_counts"].get(t, 0)
        intel_total += max(count, 0)
        print(f"  {t:30s} {count:>6d} rows")
    print(f"  {'INTELLIGENCE TOTAL':30s} {intel_total:>6d}")

    print("\n  --- JUNCTION TABLES (Enrichment) ---")
    junction_tables = [
        "app_modalities", "app_commercial_seams", "app_deployment_contexts",
        "model_capabilities", "app_primitives", "primitive_dependencies",
        "apparatus_components", "app_relationships", "app_usage_contexts",
        "workflow_templates", "workflow_steps",
    ]
    junction_total = 0
    for t in junction_tables:
        count = results["row_counts"].get(t, 0)
        junction_total += max(count, 0)
        print(f"  {t:30s} {count:>6d} rows")
    print(f"  {'JUNCTION TOTAL':30s} {junction_total:>6d}")

    print("\n  --- KINETIC TABLES (Phase B) ---")
    kinetic_tables = ["action_types", "app_actions", "agent_bindings"]
    kinetic_total = 0
    for t in kinetic_tables:
        count = results["row_counts"].get(t, 0)
        kinetic_total += max(count, 0)
        print(f"  {t:30s} {count:>6d} rows")
    print(f"  {'KINETIC TOTAL':30s} {kinetic_total:>6d}")

    print("\n  --- OPERATIONAL (CSV Ledgers) ---")
    ops_tables = ["projects", "tasks", "accounts", "platforms", "platform_roles", "sources", "filename_mappings", "rename_mappings"]
    ops_total = 0
    for t in ops_tables:
        count = results["row_counts"].get(t, 0)
        ops_total += max(count, 0)
        print(f"  {t:30s} {count:>6d} rows")
    print(f"  {'OPERATIONAL TOTAL':30s} {ops_total:>6d}")

    grand_total = bedrock_total + settlement_total + intel_total + junction_total + kinetic_total + ops_total
    print(f"\n  {'GRAND TOTAL':30s} {grand_total:>6d} rows")

    print(f"\n  --- INTEGRITY ---")
    print(f"  Foreign key violations: {results['fk_violations']}")
    print(f"  SQLite integrity check: {results['integrity']}")

    total_tables = sum(1 for v in results["row_counts"].values() if v >= 0)
    populated = sum(1 for v in results["row_counts"].values() if v > 0)
    print(f"  Tables created: {total_tables}")
    print(f"  Tables populated: {populated}")

    print("\n" + "=" * 60)
    status = "PASS" if results["fk_violations"] == 0 and results["integrity"] == "ok" else "FAIL"
    print(f"  STATUS: {status}")
    print("=" * 60 + "\n")

    return status


# --- Phase 7b: Strategic Entity Seeding (DA-07) ---


def seed_strategic_entities(conn):
    """Seed strategic entity tables with initial data from operational state."""
    cur = conn.cursor()

    # Commitments: active obligations from Intention Compass (15 records)
    cur.executemany(
        "INSERT OR IGNORE INTO commitments (code, name, stakeholder, deadline, status, intention_link, linear_id, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        [
            ("CMT-001", "Revenue mechanism by month end", "Sovereign", "2026-02-28", "failed", "INT-1201", None, "INT-1201 FAILED — needs reset with concrete mechanism"),
            ("CMT-002", "Ontology substrate operational", "System", None, "active", "INT-MI19", None, "FINAL BOSS — Palantir-like ontology. Currently at 45%"),
            ("CMT-003", "Begin ALL automations", "System", None, "active", "INT-1612", None, "P0 master plan — automation pipeline expansion"),
            ("CMT-004", "MBA Ajna setup", "Sovereign", None, "active", "INT-P015", "SYN-35", "Dual-machine paradigm — MBA=kinetic micro. SYN-35"),
            ("CMT-005", "Tool onboarding pipeline", "System", None, "active", "INT-1202", None, "SYN-51/53 in progress, SYN-52/54 todo"),
            ("CMT-006", "Complete Jira onboarding", "System", None, "active", "INT-1202", "SYN-51", "5 epics, 5 stories, Sprint 0 active. Board conversion pending."),
            ("CMT-007", "Complete Todoist onboarding", "System", None, "active", "INT-1202", "SYN-53", "16 tasks, 13 labels, weekly review configured."),
            ("CMT-008", "Mastery IIC email setup", "Sovereign", None, "active", "INT-1206", "SYN-24", "P0-Critical. Sovereign-gated — requires manual email input."),
            ("CMT-009", "Terminal cascade machine sync", "System", None, "active", "INT-1610", "SYN-43", "AI CLI tools synchronized between Mac mini and MBA."),
            ("CMT-010", "JIT HighCommand variable dashboard", "System", None, "active", "INT-1603", "SYN-40", "Palantir-like observation dashboard replacing Emacs layer."),
            ("CMT-011", "LifeOS PKM architectural convergence", "Sovereign", None, "active", "INT-1616", "SYN-48", "Notion/Airtable/Zettelkasten/PARA/GTD convergence."),
            ("CMT-012", "Information stream extraction pipeline", "System", None, "active", "INT-1608", "SYN-46", "Apple Notes, YouTube Watch Later, X favorites — ingest/digest/excrete."),
            ("CMT-013", "OpenClaw Discord+Slack self-service", "System", None, "active", "INT-1606", "SYN-50", "Give OpenClaw all tools to self-service on communication platforms."),
            ("CMT-014", "Ontology Content phase completion", "Commander", None, "active", "INT-MI19", None, "PROJ-006a at 50%. Remaining: Dataview queries, theoretical→canonical promotion."),
            ("CMT-015", "Domain registration", "Sovereign", "2026-02-16", "active", "INT-1201", None, "Sovereign securing domain this week."),
        ],
    )

    # Goals: desired outcomes (12 records)
    cur.executemany(
        "INSERT OR IGNORE INTO goals (code, name, intention_link, target_date, status, success_criteria, linear_id, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        [
            ("GOL-001", "Self-sustaining economics", "INT-1201", None, "blocked", "$160-210/mo covered by revenue", None, "Consulting, skill licensing, or architecture advisory"),
            ("GOL-002", "Ontology kernel complete", "INT-MI19", None, "active", "All entity types + query surface operational", None, "4-layer kernel: Storage → Semantic → Integration → AI"),
            ("GOL-003", "Constellation fully operational", "INT-1202", None, "partial", "All 6 agents dispatching successfully", None, "Currently: Commander reliable, Adjudicator restored, Cartographer hibernated"),
            ("GOL-004", "HighCommand web dashboard", "INT-1603", None, "deferred", "Palantir-like observation dashboard", None, "Replaces Emacs observation layer"),
            ("GOL-005", "Token economics optimized", "INT-P014", None, "active", "Zero waste in API spend", None, "Google AI Pro ($20/mo) under evaluation for cancellation"),
            ("GOL-006", "Epic 3 Capability Cascade complete", "INT-1202", None, "partial", "MBA Ajna operational with full MCP + launchd stack", None, "SYN-34 Done, SYN-35 Todo. MBA 95% restored."),
            ("GOL-007", "Epic 8 Multi-Methodology Stack complete", "INT-1202", None, "partial", "All 5 onboarding tools operational (Jira, Todoist, Airtable, Trello, TeamGantt)", None, "Airtable DONE. Jira/Todoist in progress. Trello/TeamGantt todo."),
            ("GOL-008", "Modal 1 completion", "INT-MI19", None, "active", "Ontology substrate + debt clearance complete", None, "Dependency chain: Debt clearance → Ontology Phase 1 → Phase 2 → Modal 1."),
            ("GOL-009", "250+ skills operational", "INT-1202", None, "active", "Skills across Commander/Adjudicator/Cartographer/Psyche/Ajna exceed 250", None, "Currently 226+ Commander, 23 Codex, 9 OpenClaw = 258 total."),
            ("GOL-010", "Automation pipeline fully activated", "INT-1612", None, "active", "Hazel, launchd, Make/Zapier, webhook bridges, n8n, all wired", None, "P0 master plan. 19 launchd agents live. Webhook server live. n8n pending."),
            ("GOL-011", "Dual-machine operational parity", "INT-P015", None, "active", "MBA matches Mac mini capability for its role (kinetic micro)", None, "Mac mini=stable macro, MBA=kinetic micro. SYN-35 pending."),
            ("GOL-012", "Domain secured and online presence", "INT-1201", "2026-02-16", "active", "Domain registered, basic web presence established", None, "Sovereign commitment for this week."),
        ],
    )

    # Risks: identified threats (15 records)
    cur.executemany(
        "INSERT OR IGNORE INTO risks (code, name, category, probability, impact, mitigation, status, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        [
            ("RSK-001", "NVIDIA free tier exhaustion", "economic", "high", "high", "Monitor credit consumption; prepare paid tier evaluation", "active", "Opaque consumption, ~1000 credits, 40 RPM"),
            ("RSK-002", "ChatGPT Plus daily limit", "economic", "medium", "medium", "Prioritize Psyche tasks by value; batch operations", "active", "GPT-5.3-codex resets ~10:00"),
            ("RSK-003", "Single point of execution", "operational", "high", "critical", "Restore Adjudicator (done), pursue MBA Ajna setup", "mitigated", "Commander was sole executor — Adjudicator now restored"),
            ("RSK-004", "Stale state drift", "operational", "high", "medium", "Regular state corrections, automated sensing pipeline", "active", "MEMORY.md/BACKLOG.md drift discovered and fixed"),
            ("RSK-005", "OAuth model access revocation", "strategic", "low", "critical", "Multi-model strategy, local fallbacks (Ollama)", "monitoring", "Anthropic blocked OAuth for Claude Max plan"),
            ("RSK-006", "Google AI Pro zero ROI", "economic", "certain", "low", "Cancel subscription (SOVEREIGN-GATED)", "active", "Cartographer produced 0% signal-to-noise — $20/mo wasted"),
            ("RSK-007", "MBA MCP config drift", "operational", "medium", "medium", "Regular sync checks with Mac mini config. Differential deployment playbook.", "active", "MBA restored but MCP config may diverge from Mac mini over time."),
            ("RSK-008", "launchd agent failure cascade", "operational", "low", "high", "Watchdog service monitors every 5 minutes. Health checks on all 19 agents.", "monitoring", "19 agents — if one fails it could cascade to dependent services."),
            ("RSK-009", "Git concurrent write collision", "operational", "low", "medium", "Psyche/Ajna check git status before large operations.", "monitoring", "Multiple agents can write to filesystem concurrently via OpenClaw."),
            ("RSK-010", "NVIDIA paid tier cost escalation", "economic", "medium", "high", "Defer Ajna heavy usage until evaluation complete. Monitor credit consumption.", "active", "Free tier ~1000 credits, opaque consumption. Production would require paid tier."),
            ("RSK-011", "Claude Max usage cap", "economic", "low", "critical", "Multi-agent distribution across 6 agents reduces single-platform dependency.", "monitoring", "Currently $100/mo Claude Max — cap would halt Commander operations."),
            ("RSK-012", "Ontology substrate abandonment", "strategic", "very_low", "catastrophic", "Regular commits, incremental value delivery, Sovereign alignment checks.", "monitoring", "INT-MI19 is the FINAL BOSS. Abandonment would invalidate the project thesis."),
            ("RSK-013", "Tool onboarding fatigue", "strategic", "medium", "medium", "Prioritize high-value tools first. SYN-51/53 active, defer SYN-52/54.", "active", "5 onboarding tools is ambitious. Risk of spreading too thin."),
            ("RSK-014", "SYN-24 Mastery IIC blocked", "dependency", "certain", "medium", "Sovereign must provide email. Escalated repeatedly.", "active", "P0-Critical label, 5+ days stale. Blocks PROJ-002 completion."),
            ("RSK-015", "ClickUp zero execution", "operational", "high", "medium", "Triage ClickUp tasks, assign ownership, set realistic deadlines.", "active", "26/26 tasks in to-do status. Zero progress on T1b platform."),
        ],
    )

    # Resources: physical and digital assets (25 records)
    cur.executemany(
        "INSERT OR IGNORE INTO resources (code, name, category, monthly_cost, status, owner, machine, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        [
            ("RES-001", "Mac mini", "hardware", 0, "active", "Sovereign", "mac-mini", "Primary server — Commander, Adjudicator, Psyche, OpenClaw"),
            ("RES-002", "MacBook Air", "hardware", 0, "active", "Sovereign", "mba", "Mobile cockpit — Ajna (pending setup)"),
            ("RES-003", "5120x1440 Ultrawide", "hardware", 0, "active", "Sovereign", "mac-mini", "Display for 4-pane cockpit layout"),
            ("RES-004", "Claude Max subscription", "subscription", 100, "active", "Sovereign", None, "Account 1 — Opus 4.6 via Claude Code"),
            ("RES-005", "ChatGPT Plus subscription", "subscription", 20, "active", "Sovereign", None, "Account 1 — GPT-5.3-codex for Psyche"),
            ("RES-006", "Google AI Pro subscription", "subscription", 20, "active", "Sovereign", None, "Account 2 — Gemini 2.5 Pro for Cartographer. UNDER REVIEW (DA-01)"),
            ("RES-007", "Neo4j + Graphiti (Docker)", "infrastructure", 0, "active", "System", "mac-mini", "Knowledge graph — ports 7474/8001"),
            ("RES-008", "Qdrant (Docker)", "infrastructure", 0, "active", "System", "mac-mini", "Vector store — port 6333"),
            ("RES-009", "OpenClaw Gateway", "infrastructure", 0, "active", "System", "mac-mini", "Agent gateway — port 18789"),
            ("RES-010", "Setapp subscription", "subscription", 9.99, "active", "Sovereign", None, "240+ macOS apps. Audit pending (SYN-56 DONE)."),
            ("RES-011", "Linear workspace", "subscription", 0, "active", "System", None, "Free tier. 56 issues, T1a operational. MCP live."),
            ("RES-012", "ClickUp workspace", "subscription", 0, "active", "System", None, "Free tier. 26 tasks across 3 spaces, 9 lists."),
            ("RES-013", "Airtable workspace", "subscription", 0, "active", "System", None, "Free tier. 442 records seeded in Ontology base."),
            ("RES-014", "Jira workspace", "subscription", 0, "active", "System", None, "Free tier. 5 epics, 5 stories, Sprint 0 active."),
            ("RES-015", "Todoist workspace", "subscription", 0, "active", "System", None, "Free tier. 16 tasks, 13 labels, weekly review."),
            ("RES-016", "Chroma vector store", "infrastructure", 0, "active", "System", "mac-mini", "Port 8765. Python 3.13 venv-chroma. Semantic search."),
            ("RES-017", "Webhook receiver server", "infrastructure", 0, "active", "System", "mac-mini", "Port 8888. Event ingestion endpoint."),
            ("RES-018", "Corpus health daemon", "infrastructure", 0, "active", "System", "mac-mini", "6-hour interval. Git + structure validation."),
            ("RES-019", "QMD local search", "infrastructure", 0, "active", "System", "mac-mini", "BM25 over 693 vault .md files. Hourly refresh."),
            ("RES-020", "Watchdog service", "infrastructure", 0, "active", "System", "mac-mini", "5-minute interval. Service health monitoring for all agents."),
            ("RES-021", "Claude Code skills ecosystem", "software", 0, "active", "Commander", "mac-mini", "226+ skills in ~/.agents/skills/. Primary capability layer."),
            ("RES-022", "Codex CLI skills", "software", 0, "active", "Adjudicator", "mac-mini", "23 skills in ~/.codex/skills/."),
            ("RES-023", "OpenClaw skills", "software", 0, "active", "Psyche", "mac-mini", "9 skills. MCP adapter bridges filesystem+obsidian."),
            ("RES-024", "CLI tools collection", "software", 0, "active", "System", "mac-mini", "recall, ccusage, ccundo, splitrail, vsync, gemini-mcp-tool."),
            ("RES-025", "Ontology SQLite database", "data", 0, "active", "System", "mac-mini", "43 tables, 1080 tracked rows. Schema v1.3.0. Daemon DB."),
        ],
    )

    # Environments: operating contexts (10 records)
    cur.executemany(
        "INSERT OR IGNORE INTO environments (code, name, machine, spatial_context, primary_agent, notes) VALUES (?, ?, ?, ?, ?, ?)",
        [
            ("ENV-001", "Mac mini Cockpit", "mac-mini", "fixed", "Commander", "Primary HQ — 4-pane tmux, 8 services, 19 launchd agents"),
            ("ENV-002", "MBA Mobile Cockpit", "mba", "ambulatory", "Ajna", "Mobile operations — pending full setup (SYN-35)"),
            ("ENV-003", "Deep Analysis", "mac-mini", "fixed", "Commander", "Sustained focus context — /claresce, ontology work"),
            ("ENV-004", "Blitzkrieg Dispatch", "mac-mini", "fixed", "Commander", "Parallel multi-agent execution context"),
            ("ENV-005", "Adjudicator Execution Context", "mac-mini", "fixed", "Adjudicator", "Codex CLI full-auto mode. Test suites, validation, formatting, standards enforcement."),
            ("ENV-006", "Cartographer Survey Context", "mac-mini", "fixed", "Cartographer", "Gemini 2.5 Pro 1M context. Corpus surveys. HIBERNATED (DA-01) — 0% signal-to-noise."),
            ("ENV-007", "Psyche Cohesion Context", "mac-mini", "fixed", "Psyche", "OpenClaw GPT-5.3-codex. System automation, policy enforcement, pipeline fusion."),
            ("ENV-008", "Ajna Strategy Context", "mba", "ambulatory", "Ajna", "OpenClaw Kimi K2.5 via NVIDIA. Strategic direction, dispatch optimization. Pending full setup."),
            ("ENV-009", "Sovereign Decision Gate", "mac-mini", "fixed", "Sovereign", "-SOVEREIGN/ queue processing. Approval gates for irreversible decisions."),
            ("ENV-010", "Metabolization Context", "mac-mini", "fixed", "Commander", "Capture > Extract > Compress > Archive workflow. Desktop/corpus content processing."),
        ],
    )

    # Governed Verbs: advisory mode — track but don't enforce (35 records)
    cur.executemany(
        "INSERT OR IGNORE INTO governed_verbs (verb, category, applies_to, requires_approval, advisory_note) VALUES (?, ?, ?, ?, ?)",
        [
            # Commitment verbs
            ("commit_to", "commitment", "commitments", False, "Create a new obligation"),
            ("fulfill", "commitment", "commitments", False, "Complete an obligation"),
            ("renegotiate", "commitment", "commitments", True, "Modify terms of an obligation"),
            ("abandon", "commitment", "commitments", True, "Drop an obligation (requires Sovereign)"),
            # Goal verbs
            ("target", "goal", "goals", False, "Set a desired outcome"),
            ("achieve", "goal", "goals", False, "Reach a desired outcome"),
            ("defer", "goal", "goals", False, "Postpone a goal"),
            ("redefine", "goal", "goals", True, "Change success criteria"),
            # Risk verbs
            ("identify", "risk", "risks", False, "Discover a new threat"),
            ("mitigate", "risk", "risks", False, "Reduce probability or impact"),
            ("accept", "risk", "risks", True, "Consciously accept a risk"),
            ("escalate", "risk", "risks", False, "Raise risk visibility to Sovereign"),
            # Resource verbs
            ("allocate", "resource", "resources", True, "Assign a resource to a purpose"),
            ("retire", "resource", "resources", True, "Remove a resource from service"),
            ("audit", "resource", "resources", False, "Verify resource state and cost"),
            # General strategic verbs
            ("hibernate", "lifecycle", "any", False, "Suspend without deleting — reactivate later"),
            ("activate", "lifecycle", "any", False, "Bring from hibernation to active"),
            ("approve", "sovereign", "any", True, "Sovereign authorization gate"),
            ("decline", "sovereign", "any", True, "Sovereign refusal gate"),
            # Orchestration verbs
            ("dispatch", "orchestration", "task,agent", False, "Route TASK file to agent inbox via dispatch.sh"),
            ("coordinate", "orchestration", "agent,workflow", False, "Synchronize multi-agent work across constellation"),
            ("delegate", "orchestration", "task", False, "Assign task to another agent for execution"),
            ("handoff", "orchestration", "context,state", False, "Transfer working state between agents or sessions"),
            # Content verbs
            ("metabolize", "content", "document,corpus", False, "READ > EXTRACT unique value > COMPRESS > DELETE originals"),
            ("distill", "content", "document", False, "Extract essential meaning, discard noise"),
            ("compress", "content", "log,staging", False, "Reduce volume while preserving information density"),
            ("translate", "content", "notation,format", False, "Convert between representations (SN, markdown, SQL)"),
            # Analysis verbs
            ("survey", "analysis", "corpus,codebase", False, "Comprehensive scan of large content bodies (1M+ context)"),
            ("sense", "analysis", "platform,model", False, "Detect changes in external platform features or capabilities"),
            ("audit_system", "analysis", "infrastructure,config", False, "Verify system state matches declared configuration"),
            ("reconcile", "analysis", "state,ledger", False, "Align divergent records or resolve conflicts between sources"),
            # Compound verbs
            ("blitzkrieg_dispatch", "compound", "multi-agent", False, "Parallel directive dispatch across all active constellation agents"),
            ("clarescence", "compound", "decision,strategy", False, "Multi-pass value-guided progressive refinement meta-operation"),
            ("metabolize_content", "compound", "document,corpus", False, "Full pipeline: Capture > Interpret > Compile > Stage > Commit"),
            ("corpus_survey", "compound", "vault,repository", False, "Comprehensive vault/codebase scan with structured output"),
        ],
    )

    # Strategic Relationships: cross-entity mappings (30 records)
    cur.executemany(
        "INSERT OR IGNORE INTO strategic_relationships (code, entity_a, entity_a_type, entity_b, entity_b_type, relationship_type, strength, context, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
        [
            # Commitment → Goal
            ("REL-001", "CMT-002", "commitment", "GOL-002", "goal", "supports", 10, "Ontology substrate operational → Ontology kernel complete", None),
            ("REL-002", "CMT-003", "commitment", "GOL-010", "goal", "enables", 9, "Begin ALL automations → Automation pipeline activated", None),
            ("REL-003", "CMT-004", "commitment", "GOL-011", "goal", "contributes_to", 7, "MBA Ajna setup → Dual-machine parity", None),
            ("REL-004", "CMT-005", "commitment", "GOL-007", "goal", "enables", 8, "Tool onboarding pipeline → Multi-Methodology Stack", None),
            ("REL-005", "CMT-015", "commitment", "GOL-012", "goal", "enables", 9, "Domain registration → Online presence", None),
            # Risk → Resource
            ("REL-006", "RSK-001", "risk", "RES-006", "resource", "threatens", 8, "NVIDIA free tier exhaustion → Google AI Pro subscription", None),
            ("REL-007", "RSK-002", "risk", "RES-005", "resource", "constrains", 9, "ChatGPT Plus daily limit → ChatGPT Plus subscription", None),
            ("REL-008", "RSK-006", "risk", "RES-006", "resource", "invalidates", 10, "Google AI Pro zero ROI → Google AI Pro subscription", None),
            ("REL-009", "RSK-010", "risk", "RES-004", "resource", "threatens", 6, "NVIDIA paid tier escalation → Claude Max subscription", None),
            ("REL-010", "RSK-015", "risk", "CMT-005", "commitment", "threatens", 7, "ClickUp zero execution → Tool onboarding pipeline", None),
            # Resource → Environment
            ("REL-011", "RES-001", "resource", "ENV-001", "environment", "hosts", 10, "Mac mini → Mac mini Cockpit", None),
            ("REL-012", "RES-002", "resource", "ENV-002", "environment", "hosts", 10, "MacBook Air → MBA Mobile Cockpit", None),
            ("REL-013", "RES-003", "resource", "ENV-001", "environment", "enables", 8, "5120x1440 Ultrawide → Cockpit 4-pane layout", None),
            ("REL-014", "RES-007", "resource", "ENV-001", "environment", "supports", 7, "Neo4j + Graphiti → Cockpit knowledge graph infra", None),
            ("REL-015", "RES-008", "resource", "ENV-001", "environment", "supports", 7, "Qdrant → Cockpit vector store infra", None),
            # Goal → Risk (mitigations)
            ("REL-016", "GOL-005", "goal", "RSK-006", "risk", "mitigates", 7, "Token economics optimized → Google AI Pro zero ROI", None),
            ("REL-017", "GOL-003", "goal", "RSK-003", "risk", "resolves", 10, "Constellation fully operational → Single point of execution", None),
            ("REL-018", "GOL-011", "goal", "RSK-007", "risk", "mitigates", 8, "Dual-machine parity → MBA MCP config drift", None),
            ("REL-019", "GOL-010", "goal", "RSK-013", "risk", "mitigates", 6, "Automation pipeline → Tool onboarding fatigue", None),
            ("REL-020", "GOL-008", "goal", "RSK-012", "risk", "mitigates", 10, "Modal 1 completion → Ontology substrate abandonment", None),
            # Intention → Commitment (drivers)
            ("REL-021", "INT-MI19", "intention", "CMT-002", "commitment", "drives", 10, "Palantir-like ontology → Ontology substrate operational", None),
            ("REL-022", "INT-1612", "intention", "CMT-003", "commitment", "drives", 10, "Begin ALL automations → Begin ALL automations commitment", None),
            ("REL-023", "INT-1202", "intention", "CMT-005", "commitment", "drives", 9, "Capitalize on heavy machinery → Tool onboarding pipeline", None),
            ("REL-024", "INT-P015", "intention", "CMT-004", "commitment", "drives", 8, "Dual-machine paradigm → MBA Ajna setup", None),
            ("REL-025", "INT-1201", "intention", "GOL-001", "goal", "drives", 10, "Self-sustaining economics → Economics goal", None),
            # Project → Goal (implementations)
            ("REL-026", "PROJ-006b", "project", "GOL-002", "goal", "implements", 10, "Ontology Substrate → Ontology kernel complete", None),
            ("REL-027", "PROJ-002", "project", "GOL-012", "goal", "enables", 7, "IIC Configuration → Domain + online presence", None),
            ("REL-028", "PROJ-LINEAR", "project", "GOL-003", "goal", "supports", 8, "Linear Onboarding → Constellation fully operational", None),
            ("REL-029", "PROJ-DESKTOP", "project", "GOL-010", "goal", "unblocks", 6, "Desktop Metabolization → Automation pipeline", None),
            ("REL-030", "PROJ-006a", "project", "GOL-008", "goal", "contributes_to", 9, "Ontology Content → Modal 1 completion", None),
            # CMT-006 through CMT-014: fill relationship gaps (REL-031 to REL-045)
            # Commitment → Goal (new)
            ("REL-031", "CMT-006", "commitment", "GOL-007", "goal", "contributes_to", 8, "Jira onboarding → Multi-Methodology Stack", None),
            ("REL-032", "CMT-007", "commitment", "GOL-007", "goal", "contributes_to", 8, "Todoist onboarding → Multi-Methodology Stack", None),
            ("REL-033", "CMT-009", "commitment", "GOL-006", "goal", "contributes_to", 7, "Terminal cascade sync → Capability Cascade", None),
            ("REL-034", "CMT-010", "commitment", "GOL-004", "goal", "implements", 9, "JIT HighCommand dashboard → HighCommand web dashboard", None),
            ("REL-035", "CMT-011", "commitment", "GOL-008", "goal", "contributes_to", 7, "LifeOS PKM convergence → Modal 1 completion", None),
            ("REL-036", "CMT-012", "commitment", "GOL-010", "goal", "enables", 8, "Info stream extraction → Automation pipeline", None),
            ("REL-037", "CMT-013", "commitment", "GOL-003", "goal", "contributes_to", 6, "OpenClaw self-service → Constellation operational", None),
            ("REL-038", "CMT-014", "commitment", "GOL-002", "goal", "supports", 9, "Ontology Content completion → Ontology kernel", None),
            # Intention → Commitment (new drivers)
            ("REL-039", "INT-1202", "intention", "CMT-006", "commitment", "drives", 8, "Heavy machinery → Jira onboarding", None),
            ("REL-040", "INT-1202", "intention", "CMT-007", "commitment", "drives", 8, "Heavy machinery → Todoist onboarding", None),
            ("REL-041", "INT-1603", "intention", "CMT-010", "commitment", "drives", 9, "JIT HighCommand → Dashboard commitment", None),
            ("REL-042", "INT-1608", "intention", "CMT-012", "commitment", "drives", 8, "Info stream extraction → Pipeline commitment", None),
            ("REL-043", "INT-1606", "intention", "CMT-013", "commitment", "drives", 7, "OpenClaw community → Self-service commitment", None),
            # Risk → Commitment (threats)
            ("REL-044", "RSK-014", "risk", "CMT-008", "commitment", "blocks", 10, "Mastery IIC blocked → Mastery email setup", None),
            ("REL-045", "RSK-013", "risk", "CMT-006", "commitment", "threatens", 6, "Tool onboarding fatigue → Jira onboarding", None),
        ],
    )

    conn.commit()
    print(f"    Commitments: {cur.execute('SELECT COUNT(*) FROM commitments').fetchone()[0]}")
    print(f"    Goals: {cur.execute('SELECT COUNT(*) FROM goals').fetchone()[0]}")
    print(f"    Risks: {cur.execute('SELECT COUNT(*) FROM risks').fetchone()[0]}")
    print(f"    Resources: {cur.execute('SELECT COUNT(*) FROM resources').fetchone()[0]}")
    print(f"    Environments: {cur.execute('SELECT COUNT(*) FROM environments').fetchone()[0]}")
    print(f"    Governed Verbs: {cur.execute('SELECT COUNT(*) FROM governed_verbs').fetchone()[0]}")
    print(f"    Strategic Relationships: {cur.execute('SELECT COUNT(*) FROM strategic_relationships').fetchone()[0]}")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Build Syncrescendence Ontology Substrate (SQLite)")
    parser.add_argument("--db-path", default=DEFAULT_DB_PATH, help="Output database path")
    parser.add_argument("--repo-root", default=DEFAULT_REPO_ROOT, help="Syncrescendence repo root")
    args = parser.parse_args()

    db_path = args.db_path
    repo_root = args.repo_root

    # Ensure parent directory exists
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    # Remove existing DB for clean rebuild
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"Removed existing database: {db_path}")

    print(f"Building ontology database: {db_path}")
    print(f"Repo root: {repo_root}\n")

    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")

    # Phase 1: Create schema
    print("Phase 1: Creating schema...")
    for label, sql in [
        ("Bedrock", SCHEMA_BEDROCK),
        ("Settlements", SCHEMA_SETTLEMENTS),
        ("Primitives", SCHEMA_PRIMITIVES),
        ("Intelligence", SCHEMA_INTELLIGENCE),
        ("Kinetic", SCHEMA_KINETIC),
        ("Strategic", SCHEMA_STRATEGIC),
        ("Operational", SCHEMA_OPERATIONAL),
        ("Indexes", SCHEMA_INDEXES),
        ("Meta", SCHEMA_META),
    ]:
        conn.executescript(sql)
        print(f"  {label} tables created")

    # Phase 2: Seed bedrock
    print("\nPhase 2: Seeding bedrock taxonomies...")
    seed_bedrock(conn)
    print("  Bedrock seeded (layers, object_types, commercial_seams, modalities, lifecycle_states, deployment_contexts, primitives, apparatus, usage_contexts)")

    # Phase 3: Import CSV ledgers
    print("\nPhase 3: Importing CSV ledgers...")

    for label, table, csv_key, col_map in [
        ("Projects", "projects", "projects", None),
        ("Tasks", "tasks", "tasks", None),
        ("Accounts", "accounts", "accounts", None),
        ("Platforms", "platforms", "platforms", None),
        ("Roles", "platform_roles", "roles", None),
        ("Sources", "sources", "sources", None),
    ]:
        csv_path = os.path.join(repo_root, CSV_PATHS[csv_key])
        count = import_csv(conn, table, csv_path, col_map)
        print(f"  {label}: {count} rows imported from {CSV_PATHS[csv_key]}")

    # Import filename/rename mappings
    for label, table, csv_key in [
        ("Filename mappings", "filename_mappings", "filename_mapping"),
        ("Rename mappings", "rename_mappings", "rename_mapping"),
    ]:
        csv_path = os.path.join(repo_root, CSV_PATHS[csv_key])
        if os.path.exists(csv_path):
            with open(csv_path, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                headers = next(reader, None)
                if headers and len(headers) >= 2:
                    cur = conn.cursor()
                    count = 0
                    col_a = "original_filename" if "filename" in table else "old_name"
                    col_b = "mapped_filename" if "filename" in table else "new_name"
                    for row in reader:
                        if len(row) >= 2:
                            cur.execute(
                                f"INSERT INTO {table} ({col_a}, {col_b}) VALUES (?, ?)",
                                (row[0].strip(), row[1].strip()),
                            )
                            count += 1
                    conn.commit()
                    print(f"  {label}: {count} rows imported")
        else:
            print(f"  {label}: SKIP (file not found)")

    # Phase 4: Cross-populate apps from platforms
    print("\nPhase 4: Cross-populating apps table from platforms...")
    platforms_csv = os.path.join(repo_root, CSV_PATHS["platforms"])
    app_count = import_platforms_to_apps(conn, platforms_csv)
    print(f"  {app_count} apps created from platform data")

    # Phase 4a: Import DYN-FUNCTIONS.csv into apps
    print("\nPhase 4a: Importing tech stack functions into apps...")
    functions_csv = os.path.join(repo_root, CSV_PATHS["functions"])
    func_count = import_functions_to_apps(conn, functions_csv)
    print(f"  {func_count} apps created from DYN-FUNCTIONS.csv")

    # Phase 4b: Import DYN-MODELS.csv into models + api_pricing
    print("\nPhase 4b: Importing AI model catalog...")
    models_csv = os.path.join(repo_root, CSV_PATHS["models"])
    model_count = import_models_csv(conn, models_csv)
    print(f"  {model_count} models imported from DYN-MODELS.csv")

    # Phase 4c: Import DYN-API_PRICING.csv as service entries
    print("\nPhase 4c: Importing API/service pricing catalog...")
    api_csv = os.path.join(repo_root, CSV_PATHS["api_pricing"])
    api_count = import_api_pricing_csv(conn, api_csv)
    print(f"  {api_count} service entries imported from DYN-API_PRICING.csv")

    # Phase 5: Ontology Enrichment (junction tables + expanded seeds)
    print("\nPhase 5: Enriching ontology with junction table data...")

    print("  5a: Seeding functional roles...")
    seed_roles(conn)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM roles")
    print(f"      {cur.fetchone()[0]} roles seeded")

    print("  5b: Expanding primitive catalog...")
    seed_expanded_primitives(conn)
    cur.execute("SELECT COUNT(*) FROM primitives")
    print(f"      {cur.fetchone()[0]} total primitives")

    print("  5c: Mapping app-primitive relationships...")
    ap_count = seed_app_primitives(conn)
    print(f"      {ap_count} app-primitive mappings created")

    print("  5d: Mapping app modalities...")
    seed_app_modalities(conn)
    cur.execute("SELECT COUNT(*) FROM app_modalities")
    print(f"      {cur.fetchone()[0]} app-modality mappings")

    print("  5e: Mapping app deployment contexts...")
    seed_app_deployment_contexts(conn)
    cur.execute("SELECT COUNT(*) FROM app_deployment_contexts")
    print(f"      {cur.fetchone()[0]} app-deployment mappings")

    print("  5f: Mapping apparatus components...")
    ac_count = seed_apparatus_components(conn)
    print(f"      {ac_count} apparatus-component mappings")

    print("  5g: Mapping app relationships...")
    ar_count = seed_app_relationships(conn)
    print(f"      {ar_count} app relationships mapped")

    # Phase 6: Kinetic Layer Enrichment
    print("\nPhase 6: Kinetic Layer Enrichment (Phase B)...")

    print("  6a: Seeding model capabilities...")
    mc_count = seed_model_capabilities(conn)
    print(f"      {mc_count} model-capability mappings")

    print("  6b: Seeding app commercial seams...")
    cs_count = seed_app_commercial_seams(conn)
    print(f"      {cs_count} app-commercial-seam mappings")

    print("  6c: Seeding action types...")
    seed_action_types(conn)
    cur.execute("SELECT COUNT(*) FROM action_types")
    at_count = cur.fetchone()[0]
    print(f"      {at_count} action types seeded")

    print("  6d: Mapping app-action relationships...")
    seed_app_actions(conn)
    cur.execute("SELECT COUNT(*) FROM app_actions")
    aa_count = cur.fetchone()[0]
    print(f"      {aa_count} app-action mappings")

    print("  6e: Mapping agent bindings...")
    seed_agent_bindings(conn)
    cur.execute("SELECT COUNT(*) FROM agent_bindings")
    ab_count = cur.fetchone()[0]
    print(f"      {ab_count} agent bindings")

    print("  6f: Seeding workflow templates...")
    seed_workflow_templates(conn)
    cur.execute("SELECT COUNT(*) FROM workflow_templates")
    wt_count = cur.fetchone()[0]
    print(f"      {wt_count} workflow templates")

    print("  6g: Seeding workflow steps...")
    seed_workflow_steps(conn)
    cur.execute("SELECT COUNT(*) FROM workflow_steps")
    ws_count = cur.fetchone()[0]
    print(f"      {ws_count} workflow steps")

    # Phase 7: Strategic Entity Expansion (DA-07)
    print("\nPhase 7: Strategic Entity Expansion (DA-07)...")
    seed_strategic_entities(conn)

    # Phase 8: Write metadata
    print("\nPhase 8: Writing metadata...")
    conn.execute(
        "INSERT OR REPLACE INTO _meta (key, value, updated_at) VALUES (?, ?, ?)",
        ("schema_version", "1.3.0", datetime.now().isoformat()),
    )
    conn.execute(
        "INSERT OR REPLACE INTO _meta (key, value, updated_at) VALUES (?, ?, ?)",
        ("canon_source", "CANON-30300-TECH_STACK-comet-INTELLIGENCE", datetime.now().isoformat()),
    )
    conn.execute(
        "INSERT OR REPLACE INTO _meta (key, value, updated_at) VALUES (?, ?, ?)",
        ("build_timestamp", datetime.now().isoformat(), datetime.now().isoformat()),
    )
    conn.execute(
        "INSERT OR REPLACE INTO _meta (key, value, updated_at) VALUES (?, ?, ?)",
        ("repo_root", repo_root, datetime.now().isoformat()),
    )
    conn.commit()

    # Phase 9: Validate
    print("\nPhase 9: Validating integrity...")
    results = validate_integrity(conn)
    status = print_report(results, db_path)

    conn.close()

    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
