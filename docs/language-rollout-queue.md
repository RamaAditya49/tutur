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

## Active Queue

1. `tutur-banjar`
2. `tutur-bugis`
3. `tutur-makassar`
4. `tutur-batak-toba`
5. `tutur-lampung`
6. `tutur-betawi`
7. `tutur-palembang`
8. `tutur-rejang`
9. `tutur-kerinci`
10. `tutur-komering`
11. `tutur-karo`
12. `tutur-simalungun`
13. `tutur-mandailing`
14. `tutur-pakpak`
15. `tutur-nias`
16. `tutur-mentawai`
17. `tutur-dayak-ngaju`
18. `tutur-maanyan`
19. `tutur-kutai`
20. `tutur-paser`
21. `tutur-tidung`
22. `tutur-bajau`
23. `tutur-toraja`
24. `tutur-mandar`
25. `tutur-tolaki`
26. `tutur-muna`
27. `tutur-wolio`
28. `tutur-gorontalo`
29. `tutur-minahasa-tombulu`
30. `tutur-bima`
31. `tutur-sumbawa`
32. `tutur-manggarai`
33. `tutur-dawan`
34. `tutur-tetun`
35. `tutur-ambon-malay`
36. `tutur-ternate`
37. `tutur-papua-malay`

This queue is intentionally not final. After each batch, add the next documented languages from Labbineka/Peta Bahasa and continue.

## Source Priority

1. Badan Bahasa / Balai Bahasa / Labbineka / Peta Bahasa / Dapobas.
2. Official dictionaries and grammars in Kemendikdasmen repositories.
3. Glottolog, ISO 639-3, WALS, PHOIBLE, ABVD, ASJP for identity and classification.
4. Peer-reviewed papers and university theses.
5. Community dictionaries or phrase lists only as supporting material, never as sole authority for formal or public output.
