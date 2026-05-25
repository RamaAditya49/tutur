---
name: tutur-minangkabau
description: Produce, adapt, or review text for Bahasa Minangkabau with an offline-first regional-language workflow. Use when the user asks for Bahasa Minangkabau, Minangkabau regional diction, local-language adaptation, or culturally aware Indonesian-to-Minangkabau wording without claiming native-level fluency or inventing undocumented vocabulary.
---

# Tutur Minangkabau

## Overview

Use this skill to produce, adapt, or review text related to Bahasa Minangkabau. Produce usable ordinary-context output from local resources. Mark uncertain wording instead of pretending it is verified.

Region/context: Sumatra Barat, rantau Minangkabau, dan komunitas Minang

Source confidence: Level 2. Public dictionary and grammar references exist, but dialect and register choices still need care.

## Workflow

1. Identify the task.
   - If the user asks for translation, check whether a source sample or dictionary reference is available.
   - If the user asks for style, preserve meaning and adapt register carefully.
   - If the user asks for cultural tone, avoid stereotypes and ask for audience/context when needed.

2. Check source confidence.
   - Use `references/sources.md` first.
   - Use Minangkabau dictionaries or grammar references for important word and structure choices.
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
