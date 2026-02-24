"""
Patch script: adds POST /triples to Graphiti's ingest router.
Idempotent — checks if endpoint already exists before patching.
Run inside the Graphiti container.
"""
import sys
import os
import shutil
import subprocess

# Locate ingest.py inside the container
CANDIDATES = [
    "/app/server/graph_service/routers/ingest.py",
    "/app/graph_service/routers/ingest.py",
]

ingest_path = None
for c in CANDIDATES:
    if os.path.isfile(c):
        ingest_path = c
        break

if not ingest_path:
    result = subprocess.run(
        ["find", "/app", "-name", "ingest.py", "-path", "*/routers/*"],
        capture_output=True, text=True,
    )
    paths = result.stdout.strip().split("\n")
    if paths and paths[0]:
        ingest_path = paths[0]

if not ingest_path:
    print("ERROR: Cannot find ingest.py in container", file=sys.stderr)
    sys.exit(1)

print(f"Found ingest.py at: {ingest_path}")

with open(ingest_path) as f:
    content = f.read()

if "/triples" in content:
    print("SKIP: /triples endpoint already present in ingest.py")
    sys.exit(0)

# Copy DTO to graph_service directory
router_dir = os.path.dirname(ingest_path)
dto_dir = os.path.dirname(router_dir)
dto_triples_path = os.path.join(dto_dir, "triples_dto.py")
shutil.copy("/tmp/triples_dto.py", dto_triples_path)
print(f"Wrote DTO to: {dto_triples_path}")

TRIPLES_CODE = '''

# === DC-114: Deterministic triple writes (Vanguard spec 1.5) ===
import uuid as _uuidlib
from datetime import datetime as _datetime, timezone as _timezone

try:
    from graphiti_core.nodes import EntityNode as _EntityNode
    from graphiti_core.edges import EntityEdge as _EntityEdge
except ImportError:
    _EntityNode = None
    _EntityEdge = None

try:
    from graph_service.triples_dto import AddTripleRequest as _AddTripleRequest
except ImportError:
    from triples_dto import AddTripleRequest as _AddTripleRequest


@router.post("/triples", status_code=201)
async def add_triple(request: _AddTripleRequest, graphiti=Depends(get_graphiti)):
    """Add a deterministic subject-predicate-object triple to the graph."""
    now = _datetime.now(_timezone.utc)
    edge_uuid = request.edge_uuid or str(_uuidlib.uuid4())
    created_at = request.created_at or now

    if _EntityNode is None:
        return {"error": "graphiti_core.nodes not available"}, 500

    source_node = _EntityNode(
        uuid=request.source_uuid,
        name=request.source_name,
        group_id=request.group_id,
    )
    target_node = _EntityNode(
        uuid=request.target_uuid,
        name=request.target_name,
        group_id=request.group_id,
    )
    edge = _EntityEdge(
        uuid=edge_uuid,
        group_id=request.group_id,
        source_node_uuid=request.source_uuid,
        target_node_uuid=request.target_uuid,
        created_at=created_at,
        name=request.edge_name,
        fact=request.edge_fact,
    )

    await graphiti.add_triplet(source_node, edge, target_node)
    return {"success": True, "edge_uuid": edge_uuid}
# === END DC-114 ===
'''

with open(ingest_path, "a") as f:
    f.write(TRIPLES_CODE)

print(f"PATCHED: /triples endpoint appended to {ingest_path}")
print("NOTE: Graphiti container must be restarted for changes to take effect.")
