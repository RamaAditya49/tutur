#!/usr/bin/env python3
"""Create a starter Tutur regional-language skill.

The generated skill is offline-first. It gives future agents a usable local
workflow and reference mirrors while still marking uncertainty for dialect,
ritual, legal, and official contexts.
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
        f"Produce, adapt, or review text for Bahasa {language} with an offline-first "
        f"regional-language workflow. Use when the user asks for Bahasa {language}, "
        f"{language} regional diction, local-language adaptation, or culturally "
        f"aware Indonesian-to-{language} wording without claiming native-level "
        f"fluency or inventing undocumented vocabulary."
    )

    sources = [line.strip() for line in args.source if line.strip()]
    source_lines = "\n".join(f"- {source}" for source in sources) or "- Add source links before raising this skill above Level 1."
    examples = [line.strip() for line in args.example if line.strip()]
    if examples:
        example_lines = []
        for raw_example in examples:
            parts = [part.strip() for part in raw_example.split("|")]
            if len(parts) < 3:
                raise SystemExit("--example must use: Indonesian|Target language|Meaning or note")
            indonesia, target, meaning = parts[:3]
            note = parts[3] if len(parts) > 3 else "Use only for the context covered by the source."
            example_lines.append(
                f"- Indonesian: \"{indonesia}\"\n"
                f"  Bahasa {language}: \"{target}\"\n"
                f"  Meaning/note: {meaning}\n"
                f"  Usage: {note}"
            )
        target_examples = "\n".join(example_lines)
    else:
        target_examples = (
            f"- No target-language sentence was supplied to the generator. Before committing "
            f"`{slug}`, add at least one verified Bahasa {language} example from a dictionary, "
            "grammar, source text, or native-speaker sample."
        )

    write(
        skill_dir / "SKILL.md",
        f"""
---
name: {slug}
description: {description}
---

# {display}

## Overview

Use this skill to produce, adapt, or review text related to Bahasa {language}. Produce usable ordinary-context output from local resources. Mark uncertain wording instead of pretending it is verified.

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

3. Compose with source discipline.
   - Keep names, places, titles, dates, and facts unchanged.
   - Prefer verified local words only.
   - For unknown terms, use Indonesian or ask for a local sample.

4. Final pass.
   - State uncertainty briefly when relevant.
   - Do not claim native-speaker or official authority.
   - Do not flatten the language into generic Indonesian slang.

## Output Style

- For direct requests, return the adapted output first.
- For review requests, list risks and then provide a safer rewrite.
- For public, ritual, legal, educational, or official use, recommend native-speaker or Balai Bahasa review.

## Resources

- `references/offline-brief.md`: compact local brief for agents without internet access.
- `references/local-mirror.md`: local mirror of source facts, vocabulary policy, and semantic guidance.
- `references/usage-patterns.md`: task patterns and review checklist for offline use.
- `references/sources.md`: source links and confidence level.
- `references/style-guide.md`: practical register and safety rules.
- `references/examples.md`: safe usage examples.
""",
    )

    write(
        skill_dir / "agents" / "openai.yaml",
        f"""
interface:
  display_name: "{display}"
  short_description: "{short}"
  default_prompt: "Use ${slug} to adapt this text with a source-aware Bahasa {language} regional register."
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

This skill supports ordinary local-language generation and review when the needed wording is covered by local resources or a user sample. It should mark uncertain dialect, ceremonial, legal, and official wording for competent speaker review.
""",
    )

    write(
        skill_dir / "references" / "offline-brief.md",
        f"""
# Offline Brief

## Local Facts

- Purpose: support ordinary-context generation, adaptation, and review for Bahasa {language}.
- Region/context: {region}
- Source confidence: Level 1 until richer local references are added.
- This skill should work without browsing.

## Guardrails

- Do not invent vocabulary.
- Do not assume one dialect represents all speakers.
- Do not use the language for sacred, ritual, legal, educational, or official text without review.
- Preserve Indonesian terms when the regional equivalent is unknown.
- Ask for a user-provided sample when voice, dialect, or register matters.

## Sample Prompts

- "Use ${slug} to review this Bahasa {language} text."
- "Make a source-aware Bahasa {language} version of this short message."
- "Check whether this text sounds like real Bahasa {language} or just Indonesian with local words."

## Safe Output Patterns

- For translation: ask for audience and dialect if the text matters publicly.
- For review: flag uncertain vocabulary, grammar interference, and register risks.
- For unknown terms: keep Indonesian and mark them for verification.
- For public use: recommend review by a competent speaker or language institution.
""",
    )

    write(
        skill_dir / "references" / "local-mirror.md",
        f"""
# Local Mirror

## Source Mirror

- Language/register: Bahasa {language}.
- Region/context: {region}.
- Source confidence: Level 1 until richer local references are added.
- Source links copied from `sources.md`:
{source_lines}

## Local Usability

Use this file as the offline substitute for source orientation. It does not copy a full dictionary. It gives the agent enough local context to decide what it can say directly, what it should keep in Indonesian, and what needs a user sample.

Ordinary short text is allowed when the vocabulary and register are covered by this skill. Sensitive public, ritual, legal, official, or educational wording needs competent speaker review.

## Vocabulary And Semantics

- Keep identity terms, names, titles, institutions, and places unchanged unless the user provides the local form.
- Preserve Indonesian words when the regional equivalent is unknown.
- Do not decorate Indonesian grammar with random local words and call it Bahasa {language}.
- Track audience, dialect/community, speech level, and purpose before choosing local terms.

## Generation Rules

1. Build the meaning in plain Indonesian first.
2. Replace only the words and patterns supported by local references or user-provided samples.
3. Keep uncertain terms visibly marked or left in Indonesian.
4. Add a short review note only when the use case is public, ritual, legal, official, or dialect-sensitive.

## Starter Lexicon Policy

Add only verified terms here. Do not bulk-copy copyrighted dictionaries. Prefer short semantic notes, phrase patterns, and source-backed examples that help an agent write responsibly.
""",
    )

    write(
        skill_dir / "references" / "usage-patterns.md",
        f"""
# Usage Patterns

## Ordinary Output

For everyday messages, captions, short announcements, and tone adaptation, produce a usable output when local resources cover the wording. Keep the answer direct and avoid long disclaimers.

## Sample Tasks

- Rewrite a short Indonesian message with Bahasa {language} flavor.
- Review a Bahasa {language} text for Indonesian interference.
- Create two variants: everyday and more respectful.
- Localize greetings, invitations, and community announcements.

## Register And Semantics

- Confirm audience when the request involves elders, institutions, ceremonies, or public signage.
- Preserve semantic intent before changing vocabulary.
- Avoid stereotypes, jokes about ethnicity, or invented cultural formulas.
- Keep technical/legal/medical terms in Indonesian unless the user provides accepted local equivalents.

## Review Checklist

- Does the output mix Indonesian grammar with isolated local words?
- Are all local terms covered by references or user samples?
- Is the dialect/community target clear?
- Are titles, names, dates, and facts unchanged?
- Does the note clearly mark only the genuinely uncertain parts?

## Output Patterns

- Direct request: provide the adapted output first.
- Review request: list risks, then provide safer wording.
- Public text: include a short speaker-review note for uncertain terms.
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

- source-aware regional-language output,
- tone adaptation,
- localized greetings or short public text,
- review of AI-generated local-language output,
- identifying uncertainty before publication.
""",
    )

    write(
        skill_dir / "references" / "examples.md",
        f"""
# Examples

## Target-Language Examples

{target_examples}

## Source-Aware Generation

Input:

> Buat teks pendek untuk mengajak anak muda menjaga Bahasa {language}.

Safe response shape:

1. Ask for target audience and dialect if needed.
2. Write a clear Indonesian baseline.
3. Use Bahasa {language} only where wording can be verified from sources or a user-provided sample.
4. Mark uncertain terms for speaker review.

## Review Mode

Input:

> Cek apakah teks ini terdengar seperti Bahasa {language} asli.

Safe response shape:

1. Flag Indonesian grammar with local-word decoration.
2. Flag unsupported vocabulary.
3. Recommend native-speaker review for public use.
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
    parser.add_argument(
        "--example",
        action="append",
        default=[],
        help="Target example as Indonesian|Target language|Meaning or note|Usage note. Repeatable.",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite an existing skill directory.")
    args = parser.parse_args()
    build_skill(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
