#!/bin/bash
# Apply DC-114 patches on Graphiti container startup
set -e
echo "[patches] Applying DC-114 /triples patch..."
cp /app/patches/triples_dto.py /tmp/triples_dto.py
python /tmp/patch_triples.py 2>&1 || echo "[patches] WARNING: patch_triples.py failed (may already be applied)"
echo "[patches] Patches applied."
