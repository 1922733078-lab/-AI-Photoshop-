#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

CHECKSUM_FILE="checksums/SHA256SUMS.txt"
TMP_CHECKSUM_FILE="$(mktemp)"
trap 'rm -f "$TMP_CHECKSUM_FILE"' EXIT

grep -v "  ${CHECKSUM_FILE}$" "$CHECKSUM_FILE" > "$TMP_CHECKSUM_FILE"

if command -v shasum >/dev/null 2>&1; then
  shasum -a 256 -c "$TMP_CHECKSUM_FILE"
elif command -v sha256sum >/dev/null 2>&1; then
  sha256sum -c "$TMP_CHECKSUM_FILE"
else
  echo "No SHA256 verification tool found." >&2
  exit 1
fi
