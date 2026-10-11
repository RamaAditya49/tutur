# Offline Brief

## Local Facts

- Purpose: short messages in Bahasa Paser, also called Pasir on Peta Bahasa.
- Glottocode: `pasi1257`. No ISO 639-3 code.
- Not Kutai (`vkt` Tenggarong, `mqg` Kota Bangun) and not Banjar.
- Peta Bahasa: ten dialects, difference 51%–79%. Sepaku, Mentawir, Swan Slutung, Langon, Paser Belengkong, Sandeley, Sotek, Muara Toyu, Lomu, Long Kali.
- Places in that map include Sepaku, Mentawir, Sotek, Babulu Darat, Long Kali, Samuntai, Sandeley, Swan Slutung, Muara Langon, Busui, Lomu, Kerang, Pasir Belengkong, Bekoso, Muara Toyu, and Kepala Telake.
- Difference from neighboring Kaltim languages in the Peta Bahasa count: 81%–100%.
- Kamus Bahasa Paser—Indonesia is the phrase source. Entries are not labeled by those ten dialects.
- The kamus preface also cites Andi Hasan's seventeen dialects in Olo Ot Danum and Olo Ot Ngaju. Do not treat that list as identical to the ten Peta Bahasa names.
- Time greetings: `selamat ma` pagi, `selamat nayap` sore, `selamat malom` malam.
- You is `iko`. Question word `ise` covers apa, siapa, and bagaimana in the kamus.
- This skill should work without browsing.

## Guardrails

- Do not invent vocabulary, titles, or soyong.
- Do not import Kutai `nyawa`, `awak`, `etam`, or `mendi`.
- Do not treat a kamus line as Long Kali, Mentawir, or Sotek unless a speaker from there confirms it.
- One attested phrase, then Indonesian. Label mixed text as mixed.
- Noble titles in the kamus (`aji`, and the kamus's note that the Paser title is `andén`) are not assigned to people by this skill.
- Funeral and mulung procedure stays outside. The preface describes it; this skill does not repeat the steps.

## Sample Prompts

- "Use $tutur-paser to review this Bahasa Paser text."
- "Make a source-aware Paser morning note, then Indonesian for the hour."
- "Check whether this is Paser or Kutai."

## Safe Output Patterns

- Open with `selamat ma`, `selamat nayap`, or `selamat malom` when the time of day matches.
- Ask `ise kabar iko?` when the point is asking after someone.
- Put the schedule in Indonesian.
- Name the dialect gap: kamus example, dialect unlabeled.
