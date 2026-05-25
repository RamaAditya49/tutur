---
name: tutur-madura
description: Draft, adapt, or review text for Bahasa Madura with a cautious regional-language workflow. Use when the user asks for Bahasa Madura, Madura regional diction, local-language adaptation, or culturally aware Indonesian-to-Madura drafting without claiming native-level fluency or inventing undocumented vocabulary.
---

# Tutur Madura

## Overview

Use this skill to adapt, draft, or review text related to Bahasa Madura. Treat output as a careful draft unless a dictionary, grammar source, or native-speaker sample supports the wording and the requested speech level.

Region/context: Pulau Madura, Tapal Kuda Jawa Timur, Bawean, dan komunitas Madura diaspora

Source confidence: Level 2. Public dictionary, grammar, and Peta Bahasa references exist, but dialect and speech-level choices require extra caution.

## Workflow

1. Identify the task.
   - If the user asks for translation, check whether a source sample or dictionary reference is available.
   - If the user asks for style, preserve meaning and adapt register carefully.
   - If the user asks for cultural tone, avoid stereotypes and ask for audience/context when needed.

2. Check source confidence.
   - Use `references/sources.md` first.
   - Identify whether the user needs everyday Madura, polite speech, Sumenep-style prestige tone, Tapal Kuda/Pendalungan context, or Bawean context.
   - Use dictionary/grammar references for important word and structure choices.
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

- `references/offline-brief.md`: compact local brief for agents without internet access.
- `references/sources.md`: source links and confidence level.
- `references/style-guide.md`: practical register and safety rules.
- `references/examples.md`: safe usage examples.
