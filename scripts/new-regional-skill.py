#!/usr/bin/env python3
"""Create a starter Tutur regional-language skill.

The generated skill is intentionally conservative. It gives future agents a
safe workflow and references without pretending to be fluent in a language that
may have limited public documentation.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def slugify(value: str) -> str:
    slug = value.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = re.sub(r"-+", "-", slug).strip("-")
    if not slug:
        raise ValueError("empty slug")
    return slug


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")


def build_skill(args: argparse.Namespace) -> None:
    language = args.language.strip()
    slug = args.slug or f"tutur-{slugify(language)}"
    skill_dir = ROOT / "skills" / slug
    if skill_dir.exists() and not args.force:
        raise SystemExit(f"Skill already exists: {skill_dir}")

    region = args.region.strip()
    display = args.display or f"Tutur {language}"
    short = args.short or f"Skill bahasa {language} daerah"
    if len(short) < 25:
        short = f"Skill bahasa {language} daerah Indonesia"
    if len(short) > 64:
        short = short[:61].rstrip() + "..."

    description = (
        f"Draft, adapt, or review text for Bahasa {language} with a cautious "
        f"regional-language workflow. Use when the user asks for Bahasa {language}, "
        f"{language} regional diction, local-language adaptation, or culturally "
        f"aware Indonesian-to-{language} drafting without claiming native-level "
        f"fluency or inventing undocumented vocabulary."
    )

    sources = [line.strip() for line in args.source if line.strip()]
    source_lines = "\n".join(f"- {source}" for source in sources) or "- Add source links before raising this skill above Level 1."

    write(
        skill_dir / "SKILL.md",
        f"""
---
name: {slug}
description: {description}
---

# {display}

## Overview

Use this skill to adapt, draft, or review text related to Bahasa {language}. Treat output as a careful draft unless strong dictionary, grammar, or native-speaker evidence is available.

Region/context: {region}

## Workflow

1. Identify the task.
   - If the user asks for translation, check whether a source sample or dictionary reference is available.
   - If the user asks for style, preserve meaning and adapt register carefully.
   - If the user asks for cultural tone, avoid stereotypes and ask for audience/context when needed.

2. Check source confidence.
   - Use `references/sources.md` first.
   - If the skill has only Level 1 sources, do not invent vocabulary.
   - If a local spelling or dialect choice is unclear, preserve the Indonesian term and add a short note.

3. Draft conservatively.
   - Keep names, places, titles, dates, and facts unchanged.
   - Prefer verified local words only.
   - For unknown terms, use Indonesian or ask for a local sample.

4. Final pass.
   - State uncertainty briefly when relevant.
   - Do not claim native-speaker or official authority.
   - Do not flatten the language into generic Indonesian slang.

## Output Style

- For direct requests, return the draft first.
- For review requests, list risks and then provide a safer rewrite.
- For public, ritual, legal, educational, or official use, recommend native-speaker or Balai Bahasa review.

## Resources

- `references/sources.md`: source links and confidence level.
- `references/style-guide.md`: practical register and safety rules.
""",
    )

    write(
        skill_dir / "agents" / "openai.yaml",
        f"""
interface:
  display_name: "{display}"
  short_description: "{short}"
  default_prompt: "Use ${slug} to adapt this text with a cautious Bahasa {language} regional register."
""",
    )

    write(
        skill_dir / "references" / "sources.md",
        f"""
# Sources

Language: {language}

Region/context: {region}

## Source Confidence

Level 1: guardrail skill. Raise this level only after adding reliable dictionary, grammar, corpus, or native-speaker-reviewed material.

## References

{source_lines}

## Editorial Position

This skill should support careful drafting and review. It should not claim full translation accuracy unless strong sources are added and the output has been reviewed by a competent speaker.
""",
    )

    write(
        skill_dir / "references" / "style-guide.md",
        f"""
# Style Guide

## Language Identity

- Name: Bahasa {language}
- Region/context: {region}

## Safety Rules

- Do not invent vocabulary.
- Do not assume one dialect represents all speakers.
- Do not use the language for sacred, ritual, legal, or official text without review.
- Preserve Indonesian terms when the regional equivalent is unknown.
- Ask for a user-provided sample when voice or dialect matters.

## Practical Use

Use this skill for:

- cautious regional-language drafts,
- tone adaptation,
- localized greetings or short public text,
- review of AI-generated local-language output,
- identifying uncertainty before publication.
""",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a Tutur regional-language skill.")
    parser.add_argument("language", help="Language display name, e.g. Aceh")
    parser.add_argument("--slug", help="Skill slug. Defaults to tutur-<language>.")
    parser.add_argument("--region", default="Indonesia", help="Region or community context.")
    parser.add_argument("--display", help="Display name.")
    parser.add_argument("--short", help="25-64 character UI description.")
    parser.add_argument("--source", action="append", default=[], help="Reference source line. Repeatable.")
    parser.add_argument("--force", action="store_true", help="Overwrite an existing skill directory.")
    args = parser.parse_args()
    build_skill(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
