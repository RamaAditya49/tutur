# Offline Brief

## Local Facts

- Purpose: support ordinary-context generation, adaptation, and review for Bahasa Sasak.
- Region/context: Pulau Lombok, Nusa Tenggara Barat; sebaran diaspora di Bali, Sulawesi Tenggara, dan Lampung menurut Peta Bahasa
- Source confidence: Level 2 guardrail/register skill with official Peta Bahasa and Kamus Sasak-Indonesia references.
- This skill should work without browsing.
- Peta Bahasa describes Sasak as originating in Lombok with four phonological dialect variants: `[a-a]`, `[a-â]`, `[â-â]`, and `[a-o]`.
- Peta Bahasa also notes social variation, commonly simplified here as ordinary/biasa and polite/halus.
- Use `matur tampiasih`, `tabeq`, and `berembe kabar?` only as short source-supported phrase examples, not as proof that long generated text is verified.

## Guardrails

- Do not invent vocabulary.
- Do not assume one dialect represents all speakers.
- Do not use the language for sacred, ritual, legal, educational, or official text without review.
- Preserve Indonesian terms when the regional equivalent is unknown.
- Ask for a user-provided sample when voice, dialect, or register matters.
- Do not turn Sasak into Indonesian with a few Lombok words attached.
- For tourism and public materials, pair short reviewed Sasak phrases with clear Indonesian support text.

## Sample Prompts

- "Use $tutur-sasak to review this Bahasa Sasak text."
- "Make a source-aware Bahasa Sasak version of this short message."
- "Check whether this text sounds like real Bahasa Sasak or just Indonesian with local words."
- "Make a Lombok tourism greeting with safe Sasak phrases and Indonesian explanation."
- "Create casual and polite variants for a community WhatsApp reminder."

## Safe Output Patterns

- For translation: ask for audience and dialect if the text matters publicly.
- For review: flag uncertain vocabulary, grammar interference, and register risks.
- For unknown terms: keep Indonesian and mark them for verification.
- For public use: recommend review by a competent speaker or language institution.
- For adat/ceremony: avoid inventing formulas and ask for local source text.
