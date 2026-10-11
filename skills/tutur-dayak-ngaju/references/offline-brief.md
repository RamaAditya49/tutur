# Offline Brief

## Local Facts

- Purpose: ordinary messages, short dictionary lines, and review for Bahasa Ngaju.
- Region: Kalimantan Tengah. Peta Bahasa lists village dialects, including Kasongan, Kuala Kurun, Tewah, Pulang Pisau, Tangkiling, and Kalampangan in Palangka Raya, among many others.
- ISO 639-3: `nij`. Glottocode: `ngaj1237`.
- Glottolog alternate names include Kapuas, Kahayan, Biadju, Ngadju, and Dayak. The last of those is too broad for this skill. A request that only says Dayak is not an Ngaju request.
- Source confidence: Level 2. Kamus Dwibahasa Dayak Ngaju–Indonesia, Balai Bahasa Kalimantan Tengah, 2013.
- Speech habit: direction is talked about from the river. The dictionary glosses ngaju as "di bagian agak ke hulu (tt sungai)". Thanks in one printed example is tarima kasih, then the help being thanked. A short help line is "dohop ikei".
- The dictionary already code-mixes. Do not invent a "purer" sentence to replace a printed example.
- Attested lines to reuse are copied in `local-mirror.md`. They are not a license to translate a paragraph.

## Guardrails

- Do not invent vocabulary, kinship titles, or ritual lines.
- Do not treat one village dialect as all Ngaju.
- Do not write ritual, funeral, or healing speeches from a dictionary gloss.
- Keep Indonesian when the Ngaju word is missing.
- Do not answer Maanyan, Bakumpai, Ot Danum, or any unnamed Dayak language with this folder. Those names are boundaries, not vocabularies stored here.
- Do not use ngaju the place-word as if it meant the whole province.
- Ask which river area the reader uses before a public line.

## Sample Prompts

- "Use $tutur-dayak-ngaju to review this Bahasa Ngaju text."
- "Open a note with dohop ikei, then the errand in Indonesian."
- "Check whether this is Ngaju or a generic Dayak mix."
- "Quote dohop ikei and keep the rest in Indonesian."
- "Refuse a ritual formula and say which dictionary line is actually available."

## Safe Output Patterns

- Quote a full dictionary example when the meaning matches. Do not swap the object.
- Use tarima kasih only inside the printed thanks example, or leave thanks in Indonesian.
- Use ngaju only as the upstream place gloss, or as the language name when that is the topic.
- For review, flag other Dayak languages and unlabeled village mixing.
- For unknown terms, keep Indonesian and name the gap.
- For admin facts, keep time, price, and document names in Indonesian.
- Mark mixed lines as mixed.
