---
name: tutur-aceh
description: Produce, adapt, or review text for Bahasa Aceh with an offline-first regional-language workflow. Use when the user asks for Bahasa Aceh, Aceh regional diction, local-language adaptation, or culturally aware Indonesian-to-Aceh wording without claiming native-level fluency or inventing undocumented vocabulary.
---

# Tutur Aceh

## Overview

Use this skill to produce, adapt, or review text related to Bahasa Aceh. Produce usable ordinary-context output from local resources. Mark uncertain wording instead of pretending it is verified.

Region/context: Aceh; also used by Acehnese communities outside Aceh

Source confidence: Level 2. There is an official Balai Bahasa Aceh dictionary site and an official peta bahasa reference, but this skill still should not invent vocabulary or decide dialect questions alone.

## Search And Discovery

Relevant searches: Bahasa Aceh, kamus Bahasa Aceh, KBDA Aceh, contoh Bahasa Aceh, belajar Bahasa Aceh, terjemahan Indonesia Aceh, translate Bahasa Aceh, Acehnese language, bahasa daerah Aceh, AI skill Bahasa Aceh.

Use this skill for source-aware Acehnese generation and review. It is not a certified translator and must defer dialect-sensitive, public, ritual, religious, legal, or official text to competent speaker review.

## Workflow

1. Identify the task.
   - If the user asks for translation, check whether a source sample or dictionary reference is available.
   - If the user asks for style, preserve meaning and adapt register carefully.
   - If the user asks for cultural tone, avoid stereotypes and ask for audience/context when needed.

2. Check source confidence.
   - Use `references/sources.md` first.
   - Use KBDA Daring for word checks when possible.
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
