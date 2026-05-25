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

## Active Queue

1. `tutur-batak-toba`
2. `tutur-lampung`
3. `tutur-betawi`
4. `tutur-palembang`
5. `tutur-rejang`
6. `tutur-kerinci`
7. `tutur-komering`
8. `tutur-karo`
9. `tutur-simalungun`
10. `tutur-mandailing`
11. `tutur-pakpak`
12. `tutur-nias`
13. `tutur-mentawai`
14. `tutur-dayak-ngaju`
15. `tutur-maanyan`
16. `tutur-kutai`
17. `tutur-paser`
18. `tutur-tidung`
19. `tutur-bajau`
20. `tutur-toraja`
21. `tutur-mandar`
22. `tutur-tolaki`
23. `tutur-muna`
24. `tutur-wolio`
25. `tutur-gorontalo`
26. `tutur-minahasa-tombulu`
27. `tutur-bima`
28. `tutur-sumbawa`
29. `tutur-manggarai`
30. `tutur-dawan`
31. `tutur-tetun`
32. `tutur-ambon-malay`
33. `tutur-ternate`
34. `tutur-papua-malay`

This queue is intentionally not final. After each batch, add the next documented languages from Labbineka/Peta Bahasa and continue.

## Source Priority

1. Badan Bahasa / Balai Bahasa / Labbineka / Peta Bahasa / Dapobas.
2. Official dictionaries and grammars in Kemendikdasmen repositories.
3. Glottolog, ISO 639-3, WALS, PHOIBLE, ABVD, ASJP for identity and classification.
4. Peer-reviewed papers and university theses.
5. Community dictionaries or phrase lists only as supporting material, never as sole authority for formal or public output.
