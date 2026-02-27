"""AddTripleRequest DTO for deterministic edge writes (DC-114)."""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class AddTripleRequest(BaseModel):
    group_id: str
    source_uuid: str
    source_name: str
    target_uuid: str
    target_name: str
    edge_name: str
    edge_fact: str
    edge_uuid: Optional[str] = None
    created_at: Optional[datetime] = None
