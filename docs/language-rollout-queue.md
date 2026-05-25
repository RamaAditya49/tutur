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

## Active Queue

1. `tutur-lampung`
2. `tutur-betawi`
3. `tutur-palembang`
4. `tutur-rejang`
5. `tutur-kerinci`
6. `tutur-komering`
7. `tutur-karo`
8. `tutur-simalungun`
9. `tutur-mandailing`
10. `tutur-pakpak`
11. `tutur-nias`
12. `tutur-mentawai`
13. `tutur-dayak-ngaju`
14. `tutur-maanyan`
15. `tutur-kutai`
16. `tutur-paser`
17. `tutur-tidung`
18. `tutur-bajau`
19. `tutur-toraja`
20. `tutur-mandar`
21. `tutur-tolaki`
22. `tutur-muna`
23. `tutur-wolio`
24. `tutur-gorontalo`
25. `tutur-minahasa-tombulu`
26. `tutur-bima`
27. `tutur-sumbawa`
28. `tutur-manggarai`
29. `tutur-dawan`
30. `tutur-tetun`
31. `tutur-ambon-malay`
32. `tutur-ternate`
33. `tutur-papua-malay`

This queue is intentionally not final. After each batch, add the next documented languages from Labbineka/Peta Bahasa and continue.

## Source Priority

1. Badan Bahasa / Balai Bahasa / Labbineka / Peta Bahasa / Dapobas.
2. Official dictionaries and grammars in Kemendikdasmen repositories.
3. Glottolog, ISO 639-3, WALS, PHOIBLE, ABVD, ASJP for identity and classification.
4. Peer-reviewed papers and university theses.
5. Community dictionaries or phrase lists only as supporting material, never as sole authority for formal or public output.
