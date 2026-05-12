#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

if command -v shasum >/dev/null 2>&1; then
  shasum -a 256 -c checksums/SHA256SUMS.txt
elif command -v sha256sum >/dev/null 2>&1; then
  sha256sum -c checksums/SHA256SUMS.txt
else
  echo "No SHA256 verification tool found." >&2
  exit 1
fi
