# Offline Brief

## Local Facts

- Purpose: support ordinary-context generation, adaptation, and review for Bahasa Makassar.
- Region/context: Sulawesi Selatan: Kota Makassar, Gowa, Takalar, Jeneponto, Bantaeng, Maros, Pangkajene Kepulauan, Kepulauan Selayar, dan komunitas Makassar diaspora menurut Peta Bahasa
- Source confidence: Level 2 guardrail/register skill with Peta Bahasa, Kemdikbud/Balai Bahasa dictionaries, structure notes, Glottolog/ISO, ABVD, and politeness references.
- This skill should work without browsing.
- Peta Bahasa places Bahasa Makassar in Makassar, Gowa, Takalar, Jeneponto, Bantaeng, Maros, Pangkep, Selayar, and related communities.
- Common supported forms include `tabe'` as a respect/permission cue, `iye'` as a polite affirmative, and `Basa Mangkasara` as a language identity phrase.
- Makassar language and Makassar Malay/Indonesian local accent are not the same thing.

## Guardrails

- Do not invent vocabulary.
- Do not assume one dialect represents all speakers.
- Do not use the language for sacred, ritual, legal, educational, or official text without review.
- Preserve Indonesian terms when the regional equivalent is unknown.
- Ask for a user-provided sample when voice, dialect, or register matters.
- Do not create adat, wedding, religious, or ceremonial formulas from scratch.
- Do not use Lontara/Makassar script unless the user supplies source text or asks for a script-aware task with sources.

## Sample Prompts

- "Use $tutur-makassar to review this Bahasa Makassar text."
- "Make a source-aware Bahasa Makassar version of this short message."
- "Check whether this text sounds like real Bahasa Makassar or just Indonesian with local words."
- "Make a Makassar-aware welcome message with `tabe'` and clear Indonesian details."
- "Review whether a text confuses Bahasa Makassar with Makassar-flavored Indonesian."

## Safe Output Patterns

- For translation: ask for audience and dialect if the text matters publicly.
- For review: flag uncertain vocabulary, grammar interference, and register risks.
- For unknown terms: keep Indonesian and mark them for verification.
- For public use: recommend review by a competent speaker or language institution.
- For professional use: keep operational facts in Indonesian unless the Makassar wording is source-backed or supplied by the user.
