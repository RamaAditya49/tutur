# Local Mirror

## Source Mirror

- Language: Bahasa Bima, also Nggahi Mbojo. Peta Bahasa heading: Bahasa Bima (Mbojo).
- ISO 639-3: `bhp`. Glottocode: `bima1247`. Glottolog status comment: not endangered, 5* (Developing).
- Classification on the Glottolog/ABVD side: Austronesian, Central-Eastern Malayo-Polynesian, Bima-Sumba. The Bima-Sumba group name does not make this Bahasa Sumbawa.
- Region: Kabupaten Bima, Kota Bima, Kabupaten Dompu, eastern Sumbawa. Further notes in Peta Bahasa: parts of Kabupaten Sumbawa, Lombok, and Reo and Pota in Manggarai, NTT.
- Dialects, Peta Bahasa: Serasuba, Wawo, Kolo, Kore. Differences about 51%–55%. Wawo is named for Sambori and Tarlawi. Kolo for Desa Kolo. Kore for Taloko. Serasuba is the wide one, including Rasanae and parts of Dompu.
- Against Samawa and Sasak: about 81%–100% difference. The Kota Bima curriculum book also treats aksara Sumbawa as a different script section.
- Dictionary of record: Kamus Mbojo-Indonesia, Kantor Bahasa NTB, reported at 5.214 lemmas. Not copied here.
- Usable tables: Bahan Ajar Mulok Kelas IV Kota Bima, Dinas Pendidikan dan Kebudayaan Kota Bima, 2021. Address study: Hasan, Jurnal Onoma 7(2), 2021.

## Local Usability

This file is the offline substitute for a dictionary lookup. It stores glossed pairs and two glossed sentences. It does not store pantun, kande, or jiki texts. Those genres are named in the curriculum book so the agent can recognize a request and refuse to compose them.

Ordinary chat may use a short opener plus Indonesian. The halus/kasa choice has to be made before any Bima pronoun is written.

## Vocabulary And Semantics

Kota Bima curriculum table, nggahi halus then nggahi kasa, then the book's Indonesian (`aona`):

- `mada` / `nahu`: saya.
- `ita` / `nggomi`: kamu.
- `mbora` / `made`: mati. Do not drop this pair into a casual joke. It is a register pair, not a greeting.
- `ngaha` / `lohi ra'a`: makan.
- `iha` / `dabae`: rusak.
- The book prints an unglossed sample that begins `Santabe ta la mada...`. Do not translate that whole line. The words `mada` and the later `nggomi` in it match the table. The full sentence stays untranslated here.

Hasan 2021, with his role notes:

- `nahu` or `ndaiku`: saya. `nahu` when the speaker is older than, or the same age as, the addressee.
- `mada`: saya, halus, when the speaker is younger.
- `nami`: kami. `mada doho`: kami, halus.
- `nggomi`: kamu, to someone younger or a peer. `nggomi doho`: kalian.
- `ndaimu`: anda, neutral. `ita`: anda/tuan, halus. `ita doho`: anda sekalian, halus.
- `sia`: dia. `sia doho`: mereka. His example `Sia ede nawancuku cakana karawi` is glossed "Dia itu sangat rajin bekerja". `Nggomi aina batu rawi sia doho aka` is glossed "Kamu jangan ikut-ikutan perbuatan mereka itu".
- `Sakola tabe nggomi Hama?`: "Sekolah di mana kamu Achmad". Peer or younger addressee. `Hama` is the calling form he gives for Achmad/Muhammad.
- Father address he lists from the field, not as one synonym set to mix freely: `ama`, `aba`, `baba`, `dae`, `uba`, `abu`, `aji`, `bapa`, `papa`. Ask which one the family uses.
- Respectful nickname (`lia kai`) changes a vowel and is not a constant rule. Published examples only: Hama to Hima, Hasa to Heso, Mina to Mene. Do not apply the change to a new name.
- He also says Bima address words end in a vowel. That is a check, not a generator.

Support phrase list (IDN Times, with `bune` and `santabe` also on a community vocabulary page):

- `Bune haba?`: apa kabar?
- `Haba tahopa`: kabar baik.
- `Santabe ta`: permisi/silakan.
- `Tarima kasi`: terima kasih. This looks like a Malay loan in the list. Prefer Indonesian "terima kasih" in the body unless the user wants this listed form, and mark it as support.
- `Mboto kangampu`: banyak maaf / mohon maaf. Support only. Do not expand it into a speech.

Food names in the same curriculum book, for recognition only, not for recipes: `mbohi dungga` sambal jeruk, `doco fo'o` sambal mangga muda. Ceremony names for the boundary, not for composition: `kande`, `jiki kapanca`, `tuha ro lanti`, `rawa Mbojo`, `patu`.

## Generation Rules

1. Decide the relationship first: younger speaker uses `mada` and `ita`. Older speaker or peer uses `nahu` and `nggomi`.
2. Write the facts in Indonesian.
3. Add `Santabe ta` or `Bune haba?` only as the short support phrase.
4. Do not mix halus and kasa in one address.
5. Do not produce Samawa or Sasak wording.
6. Do not generate a `lia kai` nickname.
7. Mark mixed text as mixed.
8. If the request is `patu`, `kande`, or `jiki`, stop at review.

## Starter Lexicon Policy

Add a Bima word only from the curriculum table, a glossed sentence in Hasan 2021, or a user sample. Phrase-list items stay labeled support. Do not copy Kamus Mbojo-Indonesia. Do not copy the rawa or kande verses printed in the school book.

## Register Handling

- Peer chat: `nggomi`, `nahu`, opener `Santabe ta` or `Bune haba?`.
- Younger person to an older neighbor: `mada`, `ita`, no `nggomi`.
- Public notice to mixed ages: Indonesian body, `Santabe ta` as the opener, no kasa pronoun aimed at the whole group.
- Professional: Indonesian for documents and deadlines.
- Adat and pantun: name the genre and ask for the local text.
