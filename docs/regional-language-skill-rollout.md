# Regional Language Skill Rollout

Date: 2026-05-25

## Goal

Create one Tutur skill per Indonesian regional language or court register, with one commit and push after each finished language.

## Source Policy

Primary source order:

1. Badan Bahasa / Balai Bahasa / Labbineka / Peta Bahasa pages.
2. Official regional dictionaries from Balai Bahasa or local institutions.
3. Glottolog for language identity, ISO code, Glottocode, and broad classification.
4. Peer-reviewed or university references.
5. Community dictionaries only as supporting references, not as authority.

Do not generate confident grammar, translation, or ceremonial usage when there is no good source. Low-resource language skills must be honest: they help structure requests, preserve names, request samples, and avoid hallucinated vocabulary.

## Scale Notes

Indonesia has hundreds of regional languages. Labbineka currently presents 718 regional languages, while 2025 reporting has cited 817. The number depends on whether dialects, cross-border varieties, sign languages, and newly inventoried varieties are counted.

Because of that, Tutur should use a registry-first workflow:

1. Build or refresh a language registry from source data.
2. Prioritize languages with stronger public documentation.
3. Create one skill per language.
4. Validate the skill.
5. Commit and push.
6. Continue to the next language.

## Skill Quality Levels

- **Level 1: Guardrail skill.** Good for low-resource languages. It prevents fake fluency, asks for source text, and keeps cultural cautions.
- **Level 2: Register skill.** Adds known tone, orthography, naming, and basic examples from public references.
- **Level 3: Working editor skill.** Has enough dictionary/grammar references to revise simple text with safer vocabulary decisions.
- **Level 4: Specialist skill.** Expert-reviewed or backed by strong grammar/dictionary material.

New regional skills should start at Level 1 or 2 unless strong sources are available.

## Commit Rule

After this rollout document and generator are in place, each language skill gets its own commit:

```text
Add <language> regional skill
```

Push immediately after each commit before starting the next language.

## Initial Batch Order

Start with languages that have stronger public references and wide usage:

1. Aceh
2. Gayo
3. Minangkabau
4. Sunda
5. Jawa
6. Madura
7. Bali
8. Sasak
9. Banjar
10. Bugis
11. Makassar
12. Batak Toba

Court-register skills already created:

- Keraton Solo / Surakarta Kedhaton
- Keraton Jogja / Yogyakarta Bagongan

Regional-language skills created:

- Aceh

Recommended court-register follow-up:

- Mangkunegaran
- Pakualaman
- Cirebon
