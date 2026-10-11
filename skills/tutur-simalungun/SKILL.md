---
name: tutur-simalungun
description: Produce, adapt, or review ordinary Bahasa Simalungun text for the Simalungun area of North Sumatra. Use for Bahasa Simalungun, sahap, or horas as printed in the Simalungun dictionary. Glottolog lists ISO 639-3 bts. Peta Bahasa files it as a Batak dialect, and this skill still does not copy Toba. Mauliate is not in the dictionary that was read. Do not invent vocabulary.
---

# Tutur Simalungun

## Overview

Use this skill for ordinary Bahasa Simalungun. Glottolog lists Batak Simalungun as ISO 639-3 `bts`, glottocode `bata1288`. Peta Bahasa still files it as a dialect of Bahasa Batak, spoken in Kabupaten Simalungun and Kabupaten Tanjung Balai on that page, and gives a 69,25 percent difference from dialek Toba. The Balai Bahasa Sumatera Utara dictionary is a Simalungun dictionary, not a Toba appendix. Some of its lemmas are explicitly tagged Tb. Those stay out of ordinary Simalungun lines.

Source confidence: Level 2. The lines below were read from Kamus Bahasa Simalungun–Indonesia, edisi kedua, on the ministry repository.

## Search And Discovery

Relevant searches: Bahasa Simalungun, kamus Bahasa Simalungun, contoh Bahasa Simalungun, belajar Bahasa Simalungun, terjemahan Indonesia Simalungun, translate Bahasa Simalungun, sahap, horas, Pematangsiantar, Raya, Sipispis, AI skill Bahasa Simalungun.

Use this skill for source-aware Simalungun generation and review. It is not a certified translator. Public, school, legal, and adat text stays with a Simalungun speaker.

## Human Voice

Kamus Simalungun mencatat `horas` sebagai ucapan selamat saat bertemu, dengan contoh `haganup hanami makkatahon horas`. Mauliate tidak ada di berkas yang dibaca. Teguran yang tercetak pendek, `ulang ho hanam i jin`. Kata untuk bicara adalah `sahap`, seperti `ia marsahap hubakku`. Di petunjuk lafal, e yang ditulis biasa umumnya dibaca taling, o umumnya /O/, ayo adalah `eta`, dan ya adalah `olo`. Lema berlabel Tb jangan diselipkan biar terdengar Batak.

## Workflow

1. Identify the task.
   - If the user wants Toba, Karo, or Pakpak, stop. Karo opens with `mejuah-juah`. Pakpak opens with `njuah-njuah`. This dictionary's meeting word is `horas`.
   - The dictionary marks some entries Ry (Raya) or Sp (Sipispis). If a line in this skill has no such tag, do not invent one.

2. Check source confidence.
   - Read `references/sources.md` before adding a Simalungun word.
   - Quote a printed example. Do not build a new sentence from single glosses.
   - `ahu` and `au` both appear. Keep each inside the sentence where it was printed.

3. Compose with source discipline.
   - Keep names, places, dates, prices, and instructions unchanged.
   - Label mixed text as mixed.
   - `jabu` is tagged Tb for rumah. Do not swap it in to sound more Batak. The untagged house remark in this skill is `rumah ai handalan tumang`.

4. Final pass.
   - Say the line comes from the Simalungun dictionary.
   - Do not claim a speaker in Pematangsiantar checked the wording.

## Output Style

- For a direct request, give the message first.
- For a review, point at Toba-only words and Tb-tagged lemmas, then give a shorter rewrite.
- For a public notice, keep the date, place, and instruction in Indonesian.

## Resources

- `references/offline-brief.md`: compact local brief for agents without internet access.
- `references/local-mirror.md`: identity and the small verified lexicon.
- `references/usage-patterns.md`: task patterns and review checklist.
- `references/sources.md`: source links and confidence level.
- `references/style-guide.md`: register and safety rules.
- `references/examples.md`: spoken examples with glosses.
