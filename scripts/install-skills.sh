#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE_DIR="$ROOT_DIR/skills"
TARGET_DIR=""
MODE="copy"
REPLACE=0
ALL=0
SKILLS=()

usage() {
  cat <<'USAGE'
Usage:
  scripts/install-skills.sh [--agent NAME | --target DIR] [--all | --skill NAME ...] [--mode copy|symlink] [--replace]

Agents:
  codex               ${CODEX_HOME:-$HOME/.codex}/skills
  openclaw-workspace  $HOME/.openclaw/workspace/skills
  openclaw-managed    $HOME/.openclaw/skills
  agents              $HOME/.agents/skills

Examples:
  ./scripts/install-skills.sh --agent codex --all
  ./scripts/install-skills.sh --agent openclaw-workspace --skill tutur-humanizer
  ./scripts/install-skills.sh --target /path/to/project/.agents/skills --all
  ./scripts/install-skills.sh --target /path/to/project/.claude/skills --skill tutur-sunda --replace
USAGE
}

resolve_agent_target() {
  case "$1" in
    codex)
      printf '%s\n' "${CODEX_HOME:-$HOME/.codex}/skills"
      ;;
    openclaw-workspace)
      printf '%s\n' "$HOME/.openclaw/workspace/skills"
      ;;
    openclaw-managed)
      printf '%s\n' "$HOME/.openclaw/skills"
      ;;
    agents)
      printf '%s\n' "$HOME/.agents/skills"
      ;;
    *)
      echo "Unknown agent target: $1" >&2
      exit 2
      ;;
  esac
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --agent)
      [[ $# -ge 2 ]] || { echo "--agent needs a value" >&2; exit 2; }
      TARGET_DIR="$(resolve_agent_target "$2")"
      shift 2
      ;;
    --target)
      [[ $# -ge 2 ]] || { echo "--target needs a value" >&2; exit 2; }
      TARGET_DIR="$2"
      shift 2
      ;;
    --all)
      ALL=1
      shift
      ;;
    --skill)
      [[ $# -ge 2 ]] || { echo "--skill needs a value" >&2; exit 2; }
      SKILLS+=("$2")
      shift 2
      ;;
    --mode)
      [[ $# -ge 2 ]] || { echo "--mode needs a value" >&2; exit 2; }
      MODE="$2"
      shift 2
      ;;
    --replace)
      REPLACE=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

[[ -n "$TARGET_DIR" ]] || { echo "Set --agent or --target" >&2; usage >&2; exit 2; }
[[ "$MODE" == "copy" || "$MODE" == "symlink" ]] || { echo "--mode must be copy or symlink" >&2; exit 2; }

if [[ "$ALL" -eq 1 ]]; then
  mapfile -t SKILLS < <(find "$SOURCE_DIR" -mindepth 1 -maxdepth 1 -type d -printf '%f\n' | sort)
fi

[[ "${#SKILLS[@]}" -gt 0 ]] || { echo "Set --all or at least one --skill" >&2; exit 2; }

mkdir -p "$TARGET_DIR"

timestamp="$(date +%Y%m%d-%H%M%S)"

for skill in "${SKILLS[@]}"; do
  src="$SOURCE_DIR/$skill"
  dest="$TARGET_DIR/$skill"

  if [[ ! -f "$src/SKILL.md" ]]; then
    echo "Missing skill source: $src" >&2
    exit 1
  fi

  if [[ -e "$dest" ]]; then
    if [[ "$REPLACE" -ne 1 ]]; then
      echo "skip existing: $dest"
      continue
    fi
    backup="$TARGET_DIR/.$skill.backup-$timestamp"
    echo "backup existing: $dest -> $backup"
    mv "$dest" "$backup"
  fi

  if [[ "$MODE" == "symlink" ]]; then
    ln -s "$src" "$dest"
    echo "linked: $dest -> $src"
  else
    cp -a "$src" "$dest"
    echo "installed: $dest"
  fi
done
