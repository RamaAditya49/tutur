# Offline Brief

## Local Facts

- Purpose: support cautious drafting and review for Bahasa Aceh.
- Region/context: Aceh and Acehnese communities outside Aceh.
- ISO 639-3: `ace`.
- Glottocode: `achi1257`.
- Source confidence: Level 2 because an official Balai Bahasa Aceh dictionary site and official language-map material exist.
- Bahasa Aceh is not Indonesian with local slang.

## Guardrails

- Do not invent vocabulary.
- Do not assume one Aceh variety represents all speakers.
- Do not force Acehnese spelling when the source gives only Indonesian.
- For public, ritual, legal, educational, or official use, recommend native-speaker or Balai Bahasa review.
- Keep Islamic greetings and religious phrases as the user writes them unless localization is requested and sourced.

## Sample Prompts

- "Use $tutur-aceh to review this Bahasa Aceh draft."
- "Make a cautious Bahasa Aceh version of this short greeting."
- "Check if this text is just Indonesian grammar with Acehnese words."

## Safe Output Patterns

- For translation: ask for dialect/audience if the text matters publicly.
- For review: flag suspicious word choices and Indonesian-grammar interference.
- For unknown terms: keep Indonesian and mark them for verification.
- For short public text: provide a draft plus a review caveat.

## Local Example

Request:

> Buat versi lokal untuk poster: "Mari jaga bahasa daerah kita."

Safe response shape:

> Saya bisa buat draf, tetapi untuk publikasi sebaiknya dicek penutur Aceh. Jika tidak ada rujukan kata yang pasti, pertahankan kalimat Indonesia atau minta padanan dari KBDA/penutur.
