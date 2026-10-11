---
name: tutur-tidung
description: Produce, adapt, or review text for Bahasa Tidung of North Kalimantan, including the Tarakan area, with an offline-first workflow. Use for Bahasa Tidung, Tidong, dialek Sesayap, Berusu, Belusu, or Tagul, and for Indonesian-to-Tidung wording. This is not Kutai and not Banjar. Keep the dialect label, and do not invent vocabulary.
---

# Tutur Tidung

## Overview

Use this skill for ordinary Bahasa Tidung text in Kalimantan Utara. The working variety is Bahasa Tidung as mapped by Peta Bahasa, with short phrases taken from a field study in Desa Salimbatu, Kecamatan Tanjung Palas Tengah, Kabupaten Bulungan. Peta Bahasa places Salimbatu in dialek Sesayap, the same dialect group it names for Kelurahan Juata Laut, Tarakan Utara. Those phrases are a Sesayap sample from Salimbatu. They are not a transcript from Tarakan, and they are not dialek Berusu or dialek Tagul.

Badan Bahasa treats Tidung as one language with three dialects: Berusu (also called Belusu by its speakers), Sesayap, and Tagul. ISO 639-3 retired `tid` in 2016 and split the catalog into Southern Tidung `itd` (glottocode `sout3241`) and Northern Tidung `ntd` (glottocode `nort3262`). For the Kalimantan Utara coast, including Tarakan and Nunukan, the catalog code that matches is Southern Tidung `itd`. Northern Tidung is a different ISO language and stays out of this skill.

Source confidence: Level 1. Identity and the dialect map come from Peta Bahasa and Glottolog. The phrases come from one published Salimbatu study. A 1981 Pusat Bahasa grammar and a 2022 Nunukan dictionary exist as publications, but their entries were not available as open text here, so this skill does not quote them.

## Search And Discovery

Relevant searches: Bahasa Tidung, kamus Bahasa Tidung, contoh Bahasa Tidung, belajar Bahasa Tidung, terjemahan Indonesia Tidung, translate Bahasa Tidung, Tidong, Tedong, dialek Sesayap, Berusu, Belusu, Tagul, Tarakan, Salimbatu, AI skill Bahasa Tidung.

Use this skill for source-aware Bahasa Tidung generation and review. It is not a certified translator. Public, legal, school, and adat text stays with a Tidung speaker who knows the target dialect.

## Human Voice

Orang Tidung di Salimbatu menaruh sifat dan penguat di depan atau di belakang benda. `kenjulu tupar seluarku` dan `seluarku tupar` sama-sama soal celana yang kebesaran. Milik menempel di kata: perut saya yang sakit jadi `tinaiku`, bukan rangkaian kata Indonesia yang hanya diganti satu-satu. Contoh yang diterbitkan sudah campur. `tapi`, `dan`, dan `seluar` ada di dalamnya. Buka pesan dengan keluhan atau kabar pendek itu, lalu teruskan dalam bahasa Indonesia kalau sisa kalimatnya belum tercatat. Jangan bunyikan ini seperti Banjar atau Kutai.

## Workflow

1. Identify the task.
   - Name the dialect if the user gives a place: Sesayap, Berusu/Belusu, or Tagul.
   - Salimbatu and Juata Laut (Tarakan Utara) are both listed as dialek Sesayap. Berusu/Belusu is the name speakers in Limbu Sedulun, Kujau, and Sesua use. Tagul is Desa Tagul, Sembakung, Nunukan.
   - If the place is unknown, keep the message in Indonesian and offer only a labeled Sesayap phrase.

2. Check source confidence.
   - Read `references/sources.md` before adding a Tidung word.
   - Use a phrase only when this skill quotes it from the Salimbatu study or from a sample the user supplies.
   - Leave unknown words in Indonesian.

3. Compose with source discipline.
   - Keep names, places, dates, prices, and instructions unchanged.
   - Label mixed text as mixed.
   - Do not build a full Tidung sentence by lining up single words from different examples.

4. Final pass.
   - Say which dialect the Tidung words belong to.
   - Do not claim the wording was checked by a speaker in Tarakan.
   - Do not treat Northern Tidung (`ntd`) material as the same list.

## Output Style

- For a direct request, give the message first.
- For a review, point at unsupported words, then give a shorter rewrite.
- For a public notice, keep the operative facts in Indonesian.

## Resources

- `references/offline-brief.md`: compact local brief for agents without internet access.
- `references/local-mirror.md`: identity, dialect map, and the small verified lexicon.
- `references/usage-patterns.md`: task patterns and review checklist.
- `references/sources.md`: source links and confidence level.
- `references/style-guide.md`: register and safety rules.
- `references/examples.md`: spoken examples with glosses.
