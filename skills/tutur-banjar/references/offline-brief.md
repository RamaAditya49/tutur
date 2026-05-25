# Offline Brief

## Local Facts

- Purpose: support ordinary-context generation, adaptation, and review for Bahasa Banjar.
- Region/context: Kalimantan Selatan dan komunitas Banjar di Kalimantan serta diaspora; dialek utama Banjar Kuala dan Banjar Hulu
- Source confidence: Level 2 guardrail/register skill with Kemdikbud/Balai Bahasa dictionaries and Glottolog/ISO references.
- This skill should work without browsing.
- Common supported forms include `ulun` for "saya", `pian` for "kamu/Anda", `apa habar?` for "apa kabar?", and `bujur` for "benar".
- Treat Banjar Kuala and Banjar Hulu as meaningful dialect/register targets. Ask which one matters before public or formal use.

## Guardrails

- Do not invent vocabulary.
- Do not assume one dialect represents all speakers.
- Do not use the language for sacred, ritual, legal, educational, or official text without review.
- Preserve Indonesian terms when the regional equivalent is unknown.
- Ask for a user-provided sample when voice, dialect, or register matters.
- Avoid using romantic/slang phrase lists as authority for formal or public translation.
- Do not flatten Banjar into generic Indonesian Malay or Jakarta slang.

## Sample Prompts

- "Use $tutur-banjar to review this Bahasa Banjar text."
- "Make a source-aware Bahasa Banjar version of this short message."
- "Check whether this text sounds like real Bahasa Banjar or just Indonesian with local words."
- "Make a polite Banjar-flavored WhatsApp reminder using ulun/pian carefully."
- "Create casual and public variants for a Banjar community announcement."

## Safe Output Patterns

- For translation: ask for audience and dialect if the text matters publicly.
- For review: flag uncertain vocabulary, grammar interference, and register risks.
- For unknown terms: keep Indonesian and mark them for verification.
- For public use: recommend review by a competent speaker or language institution.
- For professional use: keep operational facts in Indonesian unless the Banjar form is source-backed or supplied by the user.
