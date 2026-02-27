#!/usr/bin/env python3
"""
memsync_schema.py — Record type validators and entity/edge mapping for the
syncrescendence mining pipeline bridge (DC-208-5).

Defines typed dataclasses for every extraction record type, validation
functions, and mapping logic that converts source atoms/relations into
Graphiti-compatible entity and edge payloads.

Schema version is stamped on every record to prevent drift between the
extractor and the bridge.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List, Optional, Union


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

SCHEMA_VERSION = "1.0.0"

VALID_RECORD_TYPES = frozenset({
    "memory_event",
    "source_atom",
    "source_relation",
    "quality_gate",
    "failure_pheromone",
    "lineage_event",
})

VALID_ENTITY_TYPES = frozenset({
    "Source",
    "Claim",
    "Framework",
    "Prediction",
    "Concept",
    "PraxisHook",
})

VALID_EDGE_TYPES = frozenset({
    "ASSERTS",
    "SUPPORTS",
    "CONTRADICTS",
    "DERIVED_FROM",
    "MENTIONS",
    "TESTED_BY",
})


# ---------------------------------------------------------------------------
# Provenance (shared sub-structure)
# ---------------------------------------------------------------------------

@dataclass
class Provenance:
    """Tracks where a piece of knowledge came from."""
    source_id: str
    line_start: int
    line_end: int
    atom_id: str


# ---------------------------------------------------------------------------
# Record dataclasses
# ---------------------------------------------------------------------------

@dataclass
class SourceAtomRecord:
    """A single extractable knowledge atom from a source document."""
    record_type: str = "source_atom"
    schema_version: str = SCHEMA_VERSION
    uuid: str = ""
    timestamp: str = ""
    source_id: str = ""
    entity_type: str = ""          # one of VALID_ENTITY_TYPES
    name: str = ""
    content: str = ""
    confidence: float = 1.0
    provenance: Optional[Dict[str, Any]] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class SourceRelationRecord:
    """A directed relation between two atoms."""
    record_type: str = "source_relation"
    schema_version: str = SCHEMA_VERSION
    uuid: str = ""
    timestamp: str = ""
    source_atom_id: str = ""
    target_atom_id: str = ""
    relation_type: str = ""        # one of VALID_EDGE_TYPES
    weight: float = 1.0
    provenance: Optional[Dict[str, Any]] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class QualityGateRecord:
    """Result of a quality gate check during extraction."""
    record_type: str = "quality_gate"
    schema_version: str = SCHEMA_VERSION
    uuid: str = ""
    timestamp: str = ""
    gate_name: str = ""
    passed: bool = False
    source_id: str = ""
    details: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class FailurePheromoneRecord:
    """Signals a processing failure for stigmergic routing."""
    record_type: str = "failure_pheromone"
    schema_version: str = SCHEMA_VERSION
    uuid: str = ""
    timestamp: str = ""
    source_id: str = ""
    stage: str = ""
    error: str = ""
    severity: str = "warning"      # warning | error | fatal
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class LineageEventRecord:
    """Tracks provenance lineage: which source produced which atoms."""
    record_type: str = "lineage_event"
    schema_version: str = SCHEMA_VERSION
    uuid: str = ""
    timestamp: str = ""
    source_id: str = ""
    atom_ids: List[str] = field(default_factory=list)
    operation: str = ""            # extract | merge | split | delete
    metadata: Dict[str, Any] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Lookup: record_type string -> dataclass
# ---------------------------------------------------------------------------

RECORD_TYPE_MAP: Dict[str, type] = {
    "source_atom": SourceAtomRecord,
    "source_relation": SourceRelationRecord,
    "quality_gate": QualityGateRecord,
    "failure_pheromone": FailurePheromoneRecord,
    "lineage_event": LineageEventRecord,
}


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

class ValidationError(Exception):
    """Raised when a record fails schema validation."""


# Required fields per record type (beyond the universal uuid/schema_version/record_type)
REQUIRED_FIELDS: Dict[str, frozenset] = {
    "source_atom": frozenset({"source_id", "entity_type", "name", "content"}),
    "source_relation": frozenset({"source_atom_id", "target_atom_id", "relation_type"}),
    "quality_gate": frozenset({"gate_name", "source_id"}),
    "failure_pheromone": frozenset({"source_id", "stage", "error"}),
    "lineage_event": frozenset({"source_id", "operation"}),
}


def validate_record(raw: Dict[str, Any]) -> None:
    """Validate a raw dict against schema rules.  Raises ValidationError."""
    rt = raw.get("record_type")
    if rt not in VALID_RECORD_TYPES:
        raise ValidationError(f"Unknown record_type: {rt!r}")

    sv = raw.get("schema_version")
    if not sv:
        raise ValidationError("Missing schema_version")

    if not raw.get("uuid"):
        raise ValidationError("Missing uuid")

    # Per-type required field checks
    required = REQUIRED_FIELDS.get(rt, frozenset())
    for field_name in required:
        if not raw.get(field_name):
            raise ValidationError(f"{rt} requires non-empty '{field_name}'")

    # Type-specific value checks
    if rt == "source_atom":
        et = raw.get("entity_type", "")
        if et and et not in VALID_ENTITY_TYPES:
            raise ValidationError(f"Invalid entity_type: {et!r}")

    elif rt == "source_relation":
        rel = raw.get("relation_type", "")
        if rel and rel not in VALID_EDGE_TYPES:
            raise ValidationError(f"Invalid relation_type: {rel!r}")


def parse_record(raw: Dict[str, Any]) -> Union[
    SourceAtomRecord, SourceRelationRecord, QualityGateRecord,
    FailurePheromoneRecord, LineageEventRecord
]:
    """Validate and parse a raw dict into the appropriate dataclass."""
    validate_record(raw)
    rt = raw["record_type"]

    # memory_event passes validation but has no dedicated dataclass —
    # it is forwarded directly to the existing memsync daemon pipeline.
    if rt == "memory_event":
        raise ValidationError("memory_event records route through memsync_daemon, not the bridge")

    cls = RECORD_TYPE_MAP[rt]
    # Only pass keys the dataclass expects
    import dataclasses
    valid_keys = {f.name for f in dataclasses.fields(cls)}
    filtered = {k: v for k, v in raw.items() if k in valid_keys}
    return cls(**filtered)


# ---------------------------------------------------------------------------
# Graphiti entity / edge payloads
# ---------------------------------------------------------------------------

@dataclass
class GraphitiEntity:
    """Payload for creating/updating a Graphiti entity node."""
    group_id: str
    name: str
    entity_type: str
    summary: str
    uuid: str
    provenance: Optional[Dict[str, Any]] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class GraphitiEdge:
    """Payload for creating/updating a Graphiti relation edge."""
    group_id: str
    source_entity_uuid: str
    target_entity_uuid: str
    relation_type: str
    weight: float = 1.0
    provenance: Optional[Dict[str, Any]] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


def map_atom_to_entity(atom: SourceAtomRecord) -> GraphitiEntity:
    """Convert a SourceAtomRecord into a GraphitiEntity payload."""
    return GraphitiEntity(
        group_id=f"SOURCE:{atom.source_id}" if atom.source_id else "SOURCE:unknown",
        name=atom.name,
        entity_type=atom.entity_type,
        summary=atom.content[:500] if atom.content else "",
        uuid=atom.uuid,
        provenance=atom.provenance,
        metadata={
            **atom.metadata,
            "confidence": atom.confidence,
            "schema_version": atom.schema_version,
        },
    )


def map_relation_to_edge(rel: SourceRelationRecord) -> GraphitiEdge:
    """Convert a SourceRelationRecord into a GraphitiEdge payload."""
    return GraphitiEdge(
        group_id=f"RELATION:{rel.uuid}",
        source_entity_uuid=rel.source_atom_id,
        target_entity_uuid=rel.target_atom_id,
        relation_type=rel.relation_type,
        weight=rel.weight,
        provenance=rel.provenance,
        metadata={
            **rel.metadata,
            "schema_version": rel.schema_version,
        },
    )


# ---------------------------------------------------------------------------
# Idempotency key generation
# ---------------------------------------------------------------------------

def idempotency_key(record_uuid: str, relation_type: str, target_id: str) -> str:
    """Deterministic idempotency key = sha256(uuid + relation_type + target_id)."""
    raw = f"{record_uuid}{relation_type}{target_id}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Serialization helpers
# ---------------------------------------------------------------------------

def record_to_dict(rec: Any) -> Dict[str, Any]:
    """Serialize a dataclass record to a plain dict."""
    return asdict(rec)
