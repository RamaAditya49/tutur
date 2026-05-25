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

## Active Queue

1. `tutur-makassar`
2. `tutur-batak-toba`
3. `tutur-lampung`
4. `tutur-betawi`
5. `tutur-palembang`
6. `tutur-rejang`
7. `tutur-kerinci`
8. `tutur-komering`
9. `tutur-karo`
10. `tutur-simalungun`
11. `tutur-mandailing`
12. `tutur-pakpak`
13. `tutur-nias`
14. `tutur-mentawai`
15. `tutur-dayak-ngaju`
16. `tutur-maanyan`
17. `tutur-kutai`
18. `tutur-paser`
19. `tutur-tidung`
20. `tutur-bajau`
21. `tutur-toraja`
22. `tutur-mandar`
23. `tutur-tolaki`
24. `tutur-muna`
25. `tutur-wolio`
26. `tutur-gorontalo`
27. `tutur-minahasa-tombulu`
28. `tutur-bima`
29. `tutur-sumbawa`
30. `tutur-manggarai`
31. `tutur-dawan`
32. `tutur-tetun`
33. `tutur-ambon-malay`
34. `tutur-ternate`
35. `tutur-papua-malay`

This queue is intentionally not final. After each batch, add the next documented languages from Labbineka/Peta Bahasa and continue.

## Source Priority

1. Badan Bahasa / Balai Bahasa / Labbineka / Peta Bahasa / Dapobas.
2. Official dictionaries and grammars in Kemendikdasmen repositories.
3. Glottolog, ISO 639-3, WALS, PHOIBLE, ABVD, ASJP for identity and classification.
4. Peer-reviewed papers and university theses.
5. Community dictionaries or phrase lists only as supporting material, never as sole authority for formal or public output.
