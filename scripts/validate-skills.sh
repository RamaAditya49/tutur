#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VALIDATOR="${TUTUR_SKILL_VALIDATOR:-$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py}"

if [[ ! -f "$VALIDATOR" ]]; then
  echo "Validator not found: $VALIDATOR" >&2
  exit 1
fi

for skill_dir in "$ROOT_DIR"/skills/*; do
  [[ -d "$skill_dir" ]] || continue
  python3 "$VALIDATOR" "$skill_dir"
done

python3 "$ROOT_DIR/scripts/check-local-resources.py"

python3 "$ROOT_DIR/skills/tutur-humanizer/scripts/scan_ai_id.py" --pretty <<'TEXT'
Di era digital yang terus berkembang, bisnis membutuhkan solusi inovatif untuk meningkatkan efisiensi secara optimal.
TEXT
