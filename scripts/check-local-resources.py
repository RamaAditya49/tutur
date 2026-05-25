#!/usr/bin/env python3
"""Validate Tutur offline resource expectations."""

from __future__ import annotations

import sys
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"

REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/offline-brief.md",
    "references/sources.md",
    "references/examples.md",
]

REQUIRED_BRIEF_MARKERS = [
    "## Local Facts",
    "## Guardrails",
    "## Sample Prompts",
    "## Safe Output Patterns",
]


def check_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    for rel in REQUIRED_FILES:
        path = skill_dir / rel
        if not path.exists():
            errors.append(f"{skill_dir.name}: missing {rel}")

    brief = skill_dir / "references/offline-brief.md"
    if brief.exists():
        text = brief.read_text(encoding="utf-8")
        for marker in REQUIRED_BRIEF_MARKERS:
            if marker not in text:
                errors.append(f"{skill_dir.name}: offline-brief.md missing {marker}")
        if len(text.strip().splitlines()) < 24:
            errors.append(f"{skill_dir.name}: offline-brief.md is too thin")

    return errors


def main() -> int:
    errors: list[str] = []
    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    for skill_dir in skill_dirs:
        errors.extend(check_skill(skill_dir))

    manifest_path = SKILLS_DIR / "manifest.json"
    if not manifest_path.exists():
        errors.append("skills: missing manifest.json")
    else:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest_names = {item.get("name") for item in manifest.get("skills", [])}
        folder_names = {path.name for path in skill_dirs}
        missing_from_manifest = sorted(folder_names - manifest_names)
        missing_folders = sorted(manifest_names - folder_names)
        for name in missing_from_manifest:
            errors.append(f"{name}: missing from skills/manifest.json")
        for name in missing_folders:
            errors.append(f"{name}: listed in manifest but folder is missing")

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("Local resources are complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
