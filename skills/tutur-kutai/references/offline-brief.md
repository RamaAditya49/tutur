# Offline Brief

## Local Facts

- Purpose: short messages in Bahasa Kutai, defaulting to the Tenggarong-centered dictionary.
- Tenggarong: glottocode `teng1267`, ISO 639-3 `vkt`.
- Kota Bangun: glottocode `kota1275`, ISO 639-3 `mqg`. Do not mix the codes.
- 1974 split cited in the 2013 kamus: Kutai Tenggarong, Kutai Kota Bangun, Kutai Muara Ancalong.
- Peta Bahasa, under Melayu Kalimantan Timur, also names Kutai Muara Lesan, Kutai Muyup Ulu, Kahala, Banua, Badeng, and Banjar Samarinda. Banjar Samarinda is not Kutai.
- Everyday internal use, 2013 preface: concentrated in Kota Tenggarong.
- Speech is mostly oral. Old written products from the sultanate period are Malay in Jawi, according to that preface.
- Documented a-to-e pairs, preface only: mandi/mendi, jalan/jelan, darah/derah, balian/belian. Do not apply the pair to new words.
- Pronouns inside dictionary examples: nyawa aku, awak kamu, etam kita, nya dia, sida mereka.
- This skill should work without browsing.

## Guardrails

- Do not invent vocabulary, pantun, or court formulas.
- Do not answer a Kota Bangun, Muara Ancalong, Muara Lesan, or Muyub Ulu request with an unlabeled Tenggarong sentence presented as theirs.
- Do not import Banjar or Paser words.
- Do not build jelan or derah into a new sentence. They are preface pairs, not example sentences in this skill.
- One attested Kutai sentence, then Indonesian. Label mixed text as mixed.
- Megang and sujud lines stay tied to the gloss in the dictionary. Do not reuse them as a generic invitation.

## Sample Prompts

- "Use $tutur-kutai to review this Bahasa Kutai text."
- "Make a source-aware Kutai Tenggarong note, then Indonesian for the hour."
- "Check whether this is Kutai or Banjar with a few local words."

## Safe Output Patterns

- Say Tenggarong-centered kamus when a dictionary line is used.
- Ask the variety when the user names Kota Bangun or another point.
- Put hours, money, and places in Indonesian.
- If the user wants a pantun or a sultanate address, stop.
