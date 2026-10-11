# Local Mirror

## Source Mirror

- Language: Bahasa Melayu Ambon.
- Glottocode: `ambo1250`. ISO 639-3: `abs`.
- Glottolog classification: Austronesian, Malayo-Polynesian, Malayo-Chamic, Malayic, Nuclear Malayic, Vehicular Malay, Eastern Indonesia Trade Malay, Ambonic Malay.
- The 2025 Balai Bahasa dictionary is the preferred word check. It gives a headword, a class, an Indonesian gloss, and a short example.
- Van Minde 1997, as excerpted on APiCS, gives long and short pronouns. This mirror keeps the long forms that also appear in the dictionary.
- The IAIN Ambon thesis quotes the local contrast: many Muslim villages kept bahasa tanah, while Malay became the mother tongue in much of the Christian community and the city lingua franca. Both statements are historical description, not a rule for who may speak Malay today.
- Peta Bahasa does not treat Melayu Ambon as Hitu. Hitu is the indigenous language entry.

Source links live in `sources.md`. Dictionary pages are not copied here.

## Local Usability

Offline, use the phrases in the vocabulary list as whole lines. Code-mixing is already inside the dictionary examples, including Indonesian place names and everyday nouns. Leave new facts in Indonesian.

Do not produce Hitu, Asilulu, or other bahasa tanah from this file.

## Vocabulary And Semantics

Checked against the 2025 dictionary unless noted.

- `beta`: saya. Example fragment in the dictionary includes `beta masi bujang` (saya masih bujang) and `beta pung bapa`.
- `ose`: kamu. Example: `ingatang, baso tangang tu ee, supaya jang korona loko ose` (ingat cuci tangan supaya kamu tidak terjangkit virus korona).
- `ale`: kamu. Example: `ale mo pi mana` (kamu mau pergi ke mana). APiCS, citing van Minde, lists `ose` and `ale`, with `ale` intimate.
- `katong`: kita/kami. Example: `mari katong pigi cari bulu di utang` (ayo kita pergi mencari bambu di hutan).
- `dong`: mereka. Example: `dong pi ka Pante Ora` (mereka berkunjung ke Pantai Ora).
- `pung`: punya, in `beta pung bapa ada ka Surabaya` (ayah saya sedang ke Surabaya).
- `dangke`: terima kasih. Example: `dangke lae su tolong beta tola oto ni`.
- `da`: selamat jalan. Example: `da Rudi, sampe baku dapa lai`.
- `jang`: jangan. Example: `jang buang sampa di got`.
- `su`: sudah, inside several examples (`su tolong`, `su lulus`).
- `seng`: tidak, inside examples such as `Ema seng pi skola`.
- `par`: untuk, inside examples such as `par sono`.
- `baku dapa`: bertemu, inside the `da` example. APiCS and van Minde also note `baku-` as a reciprocal pattern in related descriptions. Do not coin new `baku-` verbs.
- Adat-context words, not scripts: `baileo` rumah adat, `berang` kain merah di kepala, in the dictionary example `dong pake berang, barang ada biking adat di baileo`.

APiCS short forms (`bet`, `os`, `tong`, `de`) are reductions listed there. Prefer the long dictionary forms unless the user sample uses the short one.

## Generation Rules

1. Write the meaning in Indonesian first.
2. Drop in a whole dictionary sentence when it matches the intent.
3. Do not change names inside an attested sentence except where the dictionary itself uses a placeholder name the user has replaced with a real one, and then mark that the frame is attested and the name is the user's.
4. Do not build a new sentence by swapping `beta` for `saya` across Indonesian grammar.
5. Keep schedules, money, and policy in Indonesian.
6. Label mixed text as mixed.

## Register Handling

- Everyday: `Ale mo pi mana`, `beta masi bujang`, `dangke` plus the attested thanks line.
- Public: `Jang buang sampa di got` and the handwashing `ose` line are already public-shaped dictionary examples.
- Professional: the dictionary's masker line is a spoken vehicle reminder. Letters and forms stay in Indonesian.
- Adat: cite `baileo` only to say a ritual is happening. Do not write the ritual.
