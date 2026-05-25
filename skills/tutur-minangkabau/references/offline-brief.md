# Offline Brief

## Local Facts

- Purpose: support source-aware generation and review for Bahasa Minangkabau.
- Region/context: Sumatra Barat, rantau Minangkabau, and Minang communities.
- ISO 639-3: `min`.
- Glottocode: `mina1268`.
- Source confidence: Level 2 because public dictionary and grammar references exist.
- Bahasa Minangkabau has strong regional identity and dialect variation.

## Guardrails

- Do not reduce Minangkabau to "bahasa Padang" or generic Malay/Indonesian with Minang particles.
- Do not assume one local form represents all Minangkabau speakers.
- Be source-aware with adat, kinship, title, and religious language.
- Preserve Indonesian terms for modern technical vocabulary unless a verified Minangkabau term is available.
- For public, adat, ritual, legal, educational, or official use, recommend native-speaker review.

## Sample Prompts

- "Use $tutur-minangkabau to review this Minang caption."
- "Make this announcement more natural for a general Minang audience."
- "Check whether this text is only Indonesian with Minang particles."

## Safe Output Patterns

- Ask whether the target is general Minang, local dialect, rantau tone, or adat context.
- For review, flag superficial markers and dialect mismatches.
- For adat content, do not improvise. Ask for source phrases or expert review.

## Local Example

Request:

> Buat ajakan pendek untuk menjaga bahasa Minangkabau.

Safe response shape:

> Tanyakan target audiens dulu. Jika untuk publik umum, buat teks sederhana dan tandai istilah yang perlu dicek oleh penutur Minangkabau.
