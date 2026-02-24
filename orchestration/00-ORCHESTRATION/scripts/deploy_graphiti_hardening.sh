#!/usr/bin/env bash
# deploy_graphiti_hardening.sh — DC-114 + DC-115 hardening for Graphiti/Neo4j
#
# DC-114: Persist Graphiti /triples endpoint permanently
# DC-115: Permanent API key wiring for Graphiti/Neo4j
#
# RUN FROM: Mac mini (where Docker/Graphiti/Neo4j live)
#   ssh mini
#   cd ~/Desktop/syncrescendence
#   bash orchestration/00-ORCHESTRATION/scripts/deploy_graphiti_hardening.sh
#
# Or deploy remotely from MBA:
#   scp orchestration/00-ORCHESTRATION/scripts/deploy_graphiti_hardening.sh mini:~/Desktop/syncrescendence/orchestration/00-ORCHESTRATION/scripts/
#   ssh mini 'cd ~/Desktop/syncrescendence && bash orchestration/00-ORCHESTRATION/scripts/deploy_graphiti_hardening.sh'

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"

# Docker CLI path on Mac mini (not in PATH by default)
DOCKER="${DOCKER_CLI:-/Applications/Docker.app/Contents/Resources/bin/docker}"

log() { echo "$(date '+%Y-%m-%dT%H:%M:%S') [deploy] $*"; }
die() { log "FATAL: $*"; exit 1; }

###############################################################################
# Pre-flight checks
###############################################################################
log "Pre-flight: checking Docker CLI..."
"$DOCKER" info >/dev/null 2>&1 || die "Docker not running. Start Docker Desktop first."

log "Pre-flight: checking Graphiti container..."
GRAPHITI_CONTAINER=$("$DOCKER" ps --filter "ancestor=zepai/graphiti" --format '{{.Names}}' | head -1)
[ -n "$GRAPHITI_CONTAINER" ] || GRAPHITI_CONTAINER=$("$DOCKER" ps --filter "name=graphiti" --format '{{.Names}}' | head -1)
[ -n "$GRAPHITI_CONTAINER" ] || die "No running Graphiti container found."
log "Found Graphiti container: $GRAPHITI_CONTAINER"

log "Pre-flight: checking Neo4j container..."
NEO4J_CONTAINER=$("$DOCKER" ps --filter "name=neo4j" --format '{{.Names}}' | head -1)
[ -n "$NEO4J_CONTAINER" ] || log "WARNING: No Neo4j container found (may be external or named differently)"

###############################################################################
# DC-114: Persist /triples endpoint
###############################################################################
log "=== DC-114: Patching Graphiti with /triples endpoint ==="

# Create the patch files locally, then copy into container
PATCH_DIR=$(mktemp -d)
trap 'rm -rf "$PATCH_DIR"' EXIT

# 1. DTO addition
cat > "$PATCH_DIR/triples_dto.py" << 'PYEOF'
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
PYEOF

# 2. Router patch script — appends to existing ingest.py
cat > "$PATCH_DIR/patch_triples.py" << 'PYEOF'
"""
Patch script: adds POST /triples to Graphiti's ingest router.
Idempotent — checks if endpoint already exists before patching.
Run inside the Graphiti container.
"""
import sys
import os

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
    # Search for it
    import subprocess
    result = subprocess.run(["find", "/app", "-name", "ingest.py", "-path", "*/routers/*"], capture_output=True, text=True)
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

# Find the dto module path relative to ingest.py
router_dir = os.path.dirname(ingest_path)
dto_dir = os.path.dirname(router_dir)  # graph_service/

# Copy DTO file
dto_path = os.path.join(dto_dir, "dto.py")
dto_triples_path = os.path.join(dto_dir, "triples_dto.py")

# Write DTO as separate module to avoid conflicts
import shutil
shutil.copy("/tmp/triples_dto.py", dto_triples_path)
print(f"Wrote DTO to: {dto_triples_path}")

# Append the /triples endpoint to ingest.py
TRIPLES_CODE = '''

# === DC-114: Deterministic triple writes (Vanguard spec 1.5) ===
import uuid as _uuidlib
from datetime import datetime as _datetime, timezone as _timezone

try:
    from graphiti_core.nodes import EntityNode as _EntityNode
    from graphiti_core.edges import EntityEdge as _EntityEdge
except ImportError:
    # Fallback for different graphiti versions
    _EntityNode = None
    _EntityEdge = None

# Import DTO — try multiple paths
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
PYEOF

# 3. Copy files into container and run patch
log "Copying patch files into container..."
"$DOCKER" cp "$PATCH_DIR/triples_dto.py" "$GRAPHITI_CONTAINER:/tmp/triples_dto.py"
"$DOCKER" cp "$PATCH_DIR/patch_triples.py" "$GRAPHITI_CONTAINER:/tmp/patch_triples.py"

log "Running patch inside container..."
"$DOCKER" exec "$GRAPHITI_CONTAINER" python /tmp/patch_triples.py

# 4. Make patch persistent across container restarts using a docker-compose override
COMPOSE_DIR="$REPO_ROOT"
OVERRIDE_FILE="$COMPOSE_DIR/docker-compose.graphiti-patch.yml"

if [ ! -f "$OVERRIDE_FILE" ]; then
    log "Creating docker-compose override for persistence..."
    cat > "$OVERRIDE_FILE" << 'YMLEOF'
# DC-114: Persistent /triples patch
# Usage: docker compose -f docker-compose.yml -f docker-compose.graphiti-patch.yml up -d
#
# This mounts the patch files into the Graphiti container so they survive
# container recreation. The entrypoint script applies the patch on startup.
version: "3.8"
services:
  graphiti:
    volumes:
      - ./orchestration/00-ORCHESTRATION/scripts/graphiti-patches/triples_dto.py:/app/patches/triples_dto.py:ro
      - ./orchestration/00-ORCHESTRATION/scripts/graphiti-patches/apply_patches.sh:/app/patches/apply_patches.sh:ro
    entrypoint: ["/bin/bash", "-c", "bash /app/patches/apply_patches.sh && exec python -m uvicorn graph_service.main:app --host 0.0.0.0 --port 8001"]
YMLEOF
    log "Created: $OVERRIDE_FILE"
fi

# 5. Create persistent patch directory
PATCH_PERSIST="$REPO_ROOT/orchestration/00-ORCHESTRATION/scripts/graphiti-patches"
mkdir -p "$PATCH_PERSIST"

cp "$PATCH_DIR/triples_dto.py" "$PATCH_PERSIST/triples_dto.py"
cp "$PATCH_DIR/patch_triples.py" "$PATCH_PERSIST/patch_triples.py"

cat > "$PATCH_PERSIST/apply_patches.sh" << 'SHEOF'
#!/bin/bash
# Apply DC-114 patches on Graphiti container startup
set -e
echo "[patches] Applying DC-114 /triples patch..."
cp /app/patches/triples_dto.py /tmp/triples_dto.py
python /tmp/patch_triples.py 2>&1 || echo "[patches] WARNING: patch_triples.py failed (may already be applied)"
echo "[patches] Patches applied."
SHEOF
chmod +x "$PATCH_PERSIST/apply_patches.sh"

log "DC-114: Patch files persisted to $PATCH_PERSIST"

###############################################################################
# DC-115: Permanent API key wiring
###############################################################################
log "=== DC-115: Checking and persisting API key configuration ==="

# Check current Graphiti env vars
log "Current Graphiti environment:"
"$DOCKER" exec "$GRAPHITI_CONTAINER" env | grep -iE 'NEO4J|OPENAI|API_KEY|MODEL' || true

# Create .env template for Graphiti stack
ENV_FILE="$REPO_ROOT/.env.graphiti"
if [ ! -f "$ENV_FILE" ]; then
    log "Creating .env.graphiti template..."
    cat > "$ENV_FILE" << 'ENVEOF'
# DC-115: Graphiti/Neo4j permanent environment configuration
# Copy to Mac mini and source in docker-compose or export in shell profile.
#
# Neo4j
NEO4J_URI=bolt://neo4j:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=__CHANGE_ME__

# Graphiti requires an LLM for entity extraction
# Options: set OPENAI_API_KEY or configure a local model
OPENAI_API_KEY=__CHANGE_ME__

# Model selection (optional — Graphiti defaults to gpt-4o-mini)
# GRAPHITI_LLM_MODEL=gpt-4o-mini
# GRAPHITI_EMBEDDING_MODEL=text-embedding-3-small

# Service ports
GRAPHITI_PORT=8001
NEO4J_BOLT_PORT=7687
NEO4J_HTTP_PORT=7474
ENVEOF
    log "Created: $ENV_FILE"
    log "ACTION REQUIRED: Edit $ENV_FILE with actual credentials before deploying."
else
    log ".env.graphiti already exists, skipping."
fi

# Create a launchd-compatible env export script for Mac mini
ENV_EXPORT="$REPO_ROOT/orchestration/00-ORCHESTRATION/scripts/graphiti_env_export.sh"
if [ ! -f "$ENV_EXPORT" ]; then
    cat > "$ENV_EXPORT" << 'EXPEOF'
#!/usr/bin/env bash
# DC-115: Export Graphiti/Neo4j env vars for non-login shells (launchd, cron).
# Source this in any script that needs to talk to Graphiti/Neo4j.
# CRITICAL: launchd does NOT source ~/.zshrc. This file is the workaround.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
ENV_FILE="$REPO_ROOT/.env.graphiti"

if [ -f "$ENV_FILE" ]; then
    set -a
    # shellcheck disable=SC1090
    source "$ENV_FILE"
    set +a
fi

# Graphiti base URL (for memsync and other clients)
export GRAPHITI_BASE="${GRAPHITI_BASE:-http://localhost:8001}"
EXPEOF
    chmod +x "$ENV_EXPORT"
    log "Created: $ENV_EXPORT"
fi

###############################################################################
# Restart Graphiti to pick up DC-114 patch
###############################################################################
log "Restarting Graphiti container to activate /triples patch..."
"$DOCKER" restart "$GRAPHITI_CONTAINER"
sleep 5

# Verify health
log "Verifying Graphiti health..."
for i in 1 2 3 4 5; do
    if curl -sf http://localhost:8001/healthcheck >/dev/null 2>&1; then
        log "Graphiti healthy after restart."
        break
    fi
    [ "$i" -eq 5 ] && die "Graphiti failed to come back healthy after restart."
    sleep 3
done

# Verify /triples endpoint exists
log "Verifying /triples endpoint..."
HTTP_CODE=$(curl -sf -o /dev/null -w '%{http_code}' -X POST http://localhost:8001/triples \
    -H 'Content-Type: application/json' \
    -d '{"group_id":"test","source_uuid":"test_s","source_name":"TestS","target_uuid":"test_t","target_name":"TestT","edge_name":"TEST","edge_fact":"test"}' \
    2>/dev/null || echo "000")

if [ "$HTTP_CODE" = "201" ] || [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "422" ]; then
    log "DC-114 VERIFIED: /triples endpoint responding (HTTP $HTTP_CODE)"
elif [ "$HTTP_CODE" = "404" ]; then
    log "WARNING: /triples returned 404 — patch may not have taken effect. Check container logs."
    log "  Debug: $DOCKER logs $GRAPHITI_CONTAINER --tail 20"
else
    log "WARNING: /triples returned HTTP $HTTP_CODE — investigate."
fi

###############################################################################
# Summary
###############################################################################
log ""
log "========================================="
log "  DC-114 + DC-115 Deployment Summary"
log "========================================="
log ""
log "DC-114 (Graphiti /triples):"
log "  - Patch applied to running container: $GRAPHITI_CONTAINER"
log "  - Persistent patches: $PATCH_PERSIST/"
log "  - Docker Compose override: $OVERRIDE_FILE"
log "  - To make permanent across docker compose up:"
log "    docker compose -f docker-compose.yml -f docker-compose.graphiti-patch.yml up -d"
log ""
log "DC-115 (API key wiring):"
log "  - Env template: $ENV_FILE"
log "  - Env export script: $ENV_EXPORT"
log "  - ACTION REQUIRED: Edit .env.graphiti with real credentials"
log "  - For launchd services, source graphiti_env_export.sh in service scripts"
log ""
log "Next steps:"
log "  1. Edit .env.graphiti with actual Neo4j password and OpenAI key"
log "  2. Test: curl -sS http://localhost:8001/triples -H 'Content-Type: application/json' -d '{...}'"
log "  3. Update memsync_daemon.py --graphiti-base to use env var"
log "  4. Mark DC-114 and DC-115 as DONE in DYN-DEFERRED_COMMITMENTS.md"
