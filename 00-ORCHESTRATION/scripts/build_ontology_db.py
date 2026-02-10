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
    "projects": "00-ORCHESTRATION/state/DYN-PROJECTS.csv",
    "tasks": "00-ORCHESTRATION/state/DYN-TASKS.csv",
    "accounts": "02-ENGINE/DYN-ACCOUNTS.csv",
    "platforms": "02-ENGINE/DYN-PLATFORMS.csv",
    "roles": "02-ENGINE/DYN-ROLES.csv",
    "sources": "04-SOURCES/DYN-SOURCES.csv",
    "filename_mapping": "04-SOURCES/REF-FILENAME_MAPPING.csv",
    "rename_mapping": "04-SOURCES/REF-RENAME_MAPPING.csv",
    "functions": "00-ORCHESTRATION/state/DYN-FUNCTIONS.csv",
    "models": "00-ORCHESTRATION/state/DYN-MODELS.csv",
    "api_pricing": "00-ORCHESTRATION/state/DYN-API_PRICING.csv",
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


def validate_integrity(conn):
    """Run data integrity checks and return results."""
    cur = conn.cursor()
    results = {}

    # Table row counts
    tables = [
        "layers", "roles", "object_types", "modalities", "lifecycle_states",
        "commercial_seams", "deployment_contexts", "apps", "models", "api_pricing",
        "primitives", "apparatus", "usage_contexts",
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

    print("\n  --- OPERATIONAL (CSV Ledgers) ---")
    ops_tables = ["projects", "tasks", "accounts", "platforms", "platform_roles", "sources", "filename_mappings", "rename_mappings"]
    ops_total = 0
    for t in ops_tables:
        count = results["row_counts"].get(t, 0)
        ops_total += max(count, 0)
        print(f"  {t:30s} {count:>6d} rows")
    print(f"  {'OPERATIONAL TOTAL':30s} {ops_total:>6d}")

    grand_total = bedrock_total + settlement_total + intel_total + ops_total
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

    # Phase 5: Write metadata
    print("\nPhase 5: Writing metadata...")
    conn.execute(
        "INSERT OR REPLACE INTO _meta (key, value, updated_at) VALUES (?, ?, ?)",
        ("schema_version", "1.0.0", datetime.now().isoformat()),
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

    # Phase 6: Validate
    print("\nPhase 6: Validating integrity...")
    results = validate_integrity(conn)
    status = print_report(results, db_path)

    conn.close()

    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
