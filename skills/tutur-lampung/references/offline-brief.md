# Offline Brief

## Local Facts

- Purpose: support ordinary-context generation, adaptation, and review for Bahasa Lampung.
- Region/context: Provinsi Lampung dan komunitas Lampung diaspora; perhatikan variasi dialek Api/A dan Nyo/O serta aksara Lampung
- Source confidence: Level 2 guardrail/register skill with official Kamus Daring Bahasa Lampung, Kemdikbud dictionary material, Glottolog/WALS identity references, and script references.
- This skill should work without browsing.
- Main operational caution: Lampung has dialect variation often simplified as Api/A and Nyo/O.
- Common supported forms include `Tabik pun`, `Kabar wawai`, `Api kabar?`, and `Nyow kabar?`.
- Aksara Lampung is a separate script-sensitive task and should not be generated for public use without review.

## Guardrails

- Do not invent vocabulary.
- Do not assume one dialect represents all speakers.
- Do not use the language for sacred, ritual, legal, educational, or official text without review.
- Preserve Indonesian terms when the regional equivalent is unknown.
- Ask for a user-provided sample when voice, dialect, or register matters.
- Do not mix Api/A and Nyo/O dialect cues randomly.
- Do not create adat, wedding, ritual, or script text from scratch.

## Sample Prompts

- "Use $tutur-lampung to review this Bahasa Lampung text."
- "Make a source-aware Bahasa Lampung version of this short message."
- "Check whether this text sounds like real Bahasa Lampung or just Indonesian with local words."
- "Make two variants: Lampung Api/A and Lampung Nyo/O."
- "Review whether this text mixes dialects or needs aksara Lampung review."

## Safe Output Patterns

- For translation: ask for audience and dialect if the text matters publicly.
- For review: flag uncertain vocabulary, grammar interference, and register risks.
- For unknown terms: keep Indonesian and mark them for verification.
- For public use: recommend review by a competent speaker or language institution.
- For professional use: keep operational facts in Indonesian unless the Lampung wording is source-backed or supplied by the user.
