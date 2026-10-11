# Language Rollout Queue

Date started: 2026-05-26

## Operating Rule

Tutur uses a never-fake-fluency workflow:

1. Research the language/register from Badan Bahasa, Balai Bahasa, Labbineka/Peta Bahasa, Glottolog/ISO, dictionaries, grammars, and university references.
2. Create or update one skill with offline resources.
3. Add contextual examples that show ordinary, public/formal, casual, professional, and adat-sensitive handling when the sources support it.
4. Validate locally.
5. Commit and push before moving to the next language.

## Coverage Model

Indonesia has hundreds of mapped regional languages. Public references often cite 718 mapped regional languages; newer counts may differ depending on dialect/language boundaries, sign languages, cross-border varieties, and newly inventoried varieties.

Tutur will not pretend one pass can make every language a high-confidence translator. Low-resource languages start as guardrail skills. Higher-resource languages can become working editor skills after local mirrors, examples, dictionaries, and grammar notes are strong enough.

## Register Model

Each ready language skill should cover these contexts where the source base allows it:

- everyday/sehari-hari,
- casual/santai,
- public/formal,
- professional or office-adjacent use,
- adat/ceremonial caution,
- review mode for AI-generated text.

If a language has speech levels, dialects, or ritual restrictions, those must appear in `references/local-mirror.md`, `references/style-guide.md`, and contextual examples.

## Current Ready Skills

- `tutur-humanizer`
- `tutur-korporat-profesi`
- `tutur-jabodetabek-urban`
- `tutur-kedhaton-solo`
- `tutur-bagongan-jogja`
- `tutur-aceh`
- `tutur-gayo`
- `tutur-minangkabau`
- `tutur-sunda`
- `tutur-jawa`
- `tutur-madura`
- `tutur-bali`
- `tutur-sasak`
- `tutur-banjar`
- `tutur-bugis`
- `tutur-makassar`
- `tutur-batak-toba`
- `tutur-lampung`
- `tutur-betawi`
- `tutur-palembang`
- `tutur-rejang`
- `tutur-kerinci`
- `tutur-komering`
- `tutur-karo`
- `tutur-simalungun`
- `tutur-mandailing`
- `tutur-pakpak`
- `tutur-nias`
- `tutur-mentawai`
- `tutur-dayak-ngaju`
- `tutur-maanyan`
- `tutur-kutai`
- `tutur-paser`
- `tutur-tidung`
- `tutur-bajau`
- `tutur-toraja`
- `tutur-mandar`
- `tutur-tolaki`
- `tutur-muna`
- `tutur-wolio`
- `tutur-gorontalo`
- `tutur-minahasa-tombulu`
- `tutur-bima`
- `tutur-sumbawa`
- `tutur-manggarai`
- `tutur-dawan`
- `tutur-tetun`
- `tutur-ambon-malay`
- `tutur-ternate`
- `tutur-papua-malay`

## Active Queue

The Betawi-through-Papuan-Malay batch is now under Current Ready Skills. Hundreds of mapped languages remain. Do not generate them by swapping a language name into one template. Research one language from Badan Bahasa, Balai Bahasa, and Peta Bahasa, and stop when a local line cannot be quoted.

1. `tutur-melayu-manado`
2. `tutur-melayu-kupang`
3. `tutur-melayu-riau`
4. `tutur-jambi`
5. `tutur-besemah`
6. `tutur-osing`
7. `tutur-banyumasan`
8. `tutur-kaili-ledo`
9. `tutur-banggai`
10. `tutur-iban`
11. `tutur-kenyah`
12. `tutur-biak`
13. `tutur-dani`
14. `tutur-galela`
15. `tutur-tobelo`
16. `tutur-buru`
17. `tutur-kei`

This queue is intentionally not final. After each batch, add the next documented languages from Labbineka/Peta Bahasa and continue.

## Source Priority

1. Badan Bahasa / Balai Bahasa / Labbineka / Peta Bahasa / Dapobas.
2. Official dictionaries and grammars in Kemendikdasmen repositories.
3. Glottolog, ISO 639-3, WALS, PHOIBLE, ABVD, ASJP for identity and classification.
4. Peer-reviewed papers and university theses.
5. Community dictionaries or phrase lists only as supporting material, never as sole authority for formal or public output.
