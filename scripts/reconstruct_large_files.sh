#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PART_DIR="$REPO_ROOT/experiments/photoshop_2026/01_delete_object/delete_object_ps2026_layered.psd.parts"
OUT_FILE="$REPO_ROOT/experiments/photoshop_2026/01_delete_object/delete_object_ps2026_layered.psd"
CHECKSUM_FILE="$REPO_ROOT/checksums/LARGE_FILE_SHA256SUMS.txt"

if [ ! -d "$PART_DIR" ]; then
  echo "Missing part directory: $PART_DIR" >&2
  exit 1
fi

cat "$PART_DIR"/delete_object_ps2026_layered.psd.part-* > "$OUT_FILE"

cd "$REPO_ROOT"
if command -v shasum >/dev/null 2>&1; then
  shasum -a 256 -c "$CHECKSUM_FILE"
elif command -v sha256sum >/dev/null 2>&1; then
  sha256sum -c "$CHECKSUM_FILE"
else
  echo "Reconstructed $OUT_FILE, but no SHA256 tool was found for verification."
fi
