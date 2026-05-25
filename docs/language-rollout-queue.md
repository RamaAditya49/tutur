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

## Active Queue

1. `tutur-bugis`
2. `tutur-makassar`
3. `tutur-batak-toba`
4. `tutur-lampung`
5. `tutur-betawi`
6. `tutur-palembang`
7. `tutur-rejang`
8. `tutur-kerinci`
9. `tutur-komering`
10. `tutur-karo`
11. `tutur-simalungun`
12. `tutur-mandailing`
13. `tutur-pakpak`
14. `tutur-nias`
15. `tutur-mentawai`
16. `tutur-dayak-ngaju`
17. `tutur-maanyan`
18. `tutur-kutai`
19. `tutur-paser`
20. `tutur-tidung`
21. `tutur-bajau`
22. `tutur-toraja`
23. `tutur-mandar`
24. `tutur-tolaki`
25. `tutur-muna`
26. `tutur-wolio`
27. `tutur-gorontalo`
28. `tutur-minahasa-tombulu`
29. `tutur-bima`
30. `tutur-sumbawa`
31. `tutur-manggarai`
32. `tutur-dawan`
33. `tutur-tetun`
34. `tutur-ambon-malay`
35. `tutur-ternate`
36. `tutur-papua-malay`

This queue is intentionally not final. After each batch, add the next documented languages from Labbineka/Peta Bahasa and continue.

## Source Priority

1. Badan Bahasa / Balai Bahasa / Labbineka / Peta Bahasa / Dapobas.
2. Official dictionaries and grammars in Kemendikdasmen repositories.
3. Glottolog, ISO 639-3, WALS, PHOIBLE, ABVD, ASJP for identity and classification.
4. Peer-reviewed papers and university theses.
5. Community dictionaries or phrase lists only as supporting material, never as sole authority for formal or public output.
