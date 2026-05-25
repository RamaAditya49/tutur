# Offline Brief

## Local Facts

- Purpose: support ordinary-context generation, adaptation, and review for Bahasa Batak Toba.
- Region/context: Sumatera Utara: kawasan Toba/Samosir/Tapanuli Utara dan komunitas Batak Toba diaspora; berbeda dari Karo, Simalungun, Mandailing, Angkola, dan Pakpak
- Source confidence: Level 2 guardrail/register skill with Glottolog/ISO, dictionary references, Kemdikbud semantic/grammar references, and script support references.
- This skill should work without browsing.
- Common supported forms include `Horas` for greeting/well-wishing, `Mauliate` for thanks, and `Hata Batak Toba` as a language identity phrase.
- Batak Toba is not the same as all Batak languages. Do not mix it with Karo, Simalungun, Mandailing, Angkola, or Pakpak.
- Kinship and respect terms such as `Amang`, `Inang`, `Lae`, `Ito`, `Tulang`, `Hula-hula`, `Boru`, and `Dongan tubu` are relationship-sensitive.

## Guardrails

- Do not invent vocabulary.
- Do not assume one dialect represents all speakers.
- Do not use the language for sacred, ritual, legal, educational, or official text without review.
- Preserve Indonesian terms when the regional equivalent is unknown.
- Ask for a user-provided sample when voice, dialect, or register matters.
- Do not create adat, wedding, ulos, marga, church, ritual, or kinship-sensitive formulas from scratch.
- Do not write aksara Batak Toba unless the user supplies source text or asks for script-aware work with review.

## Sample Prompts

- "Use $tutur-batak-toba to review this Bahasa Batak Toba text."
- "Make a source-aware Bahasa Batak Toba version of this short message."
- "Check whether this text sounds like real Bahasa Batak Toba or just Indonesian with local words."
- "Make a Horas/Mauliate greeting for a community message without inventing adat language."
- "Review whether this text confuses Batak Toba with other Batak languages."

## Safe Output Patterns

- For translation: ask for audience and dialect if the text matters publicly.
- For review: flag uncertain vocabulary, grammar interference, and register risks.
- For unknown terms: keep Indonesian and mark them for verification.
- For public use: recommend review by a competent speaker or language institution.
- For professional use: keep operational facts in Indonesian unless the Batak Toba wording is source-backed or supplied by the user.
