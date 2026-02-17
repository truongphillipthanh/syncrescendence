#!/bin/bash
# Backward-compatible shim.
# Canonical supervisor is now auto_ingest_supervisor.sh

exec /bin/bash "$(cd "$(dirname "$0")" && pwd)/auto_ingest_supervisor.sh" "$@"
