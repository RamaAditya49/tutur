# Offline Brief

## Local Facts

- Purpose: support ordinary-context generation, adaptation, and review for Bahasa Bugis.
- Region/context: Sulawesi Selatan dan komunitas Bugis diaspora; termasuk variasi lokal seperti Soppeng, Bone, Wajo, Sidenreng Rappang, Sinjai, dan daerah Bugis lainnya
- Source confidence: Level 2 guardrail/register skill with Kemdikbud/Balai Bahasa dictionaries, Peta Bahasa, Glottolog/ISO, and politeness references.
- This skill should work without browsing.
- Common supported forms include `tabe'` as a politeness/permission cue, `iye` as an affirmative/polite response, `idi'` as respectful second-person address, and `Basa Ugi` as a common language name.
- Bugis has local variation across South Sulawesi communities; ask target area when public wording matters.

## Guardrails

- Do not invent vocabulary.
- Do not assume one dialect represents all speakers.
- Do not use the language for sacred, ritual, legal, educational, or official text without review.
- Preserve Indonesian terms when the regional equivalent is unknown.
- Ask for a user-provided sample when voice, dialect, or register matters.
- Do not use Lontara script unless the user supplies text or specifically requests a script-aware task.
- Do not create adat, wedding, religious, or ceremonial formulas from scratch.

## Sample Prompts

- "Use $tutur-bugis to review this Bahasa Bugis text."
- "Make a source-aware Bahasa Bugis version of this short message."
- "Check whether this text sounds like real Bahasa Bugis or just Indonesian with local words."
- "Make a Bugis-aware invitation with `tabe'` and clear Indonesian details."
- "Review whether this output uses Bugis politeness markers naturally."

## Safe Output Patterns

- For translation: ask for audience and dialect if the text matters publicly.
- For review: flag uncertain vocabulary, grammar interference, and register risks.
- For unknown terms: keep Indonesian and mark them for verification.
- For public use: recommend review by a competent speaker or language institution.
- For professional use: keep operational facts in Indonesian unless the Bugis wording is source-backed or supplied by the user.
