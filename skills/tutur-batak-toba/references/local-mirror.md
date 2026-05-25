# Local Mirror

## Source Mirror

- Language/register: Bahasa Batak Toba.
- Region/context: Sumatera Utara: kawasan Toba/Samosir/Tapanuli Utara dan komunitas Batak Toba diaspora; berbeda dari Karo, Simalungun, Mandailing, Angkola, dan Pakpak.
- Source confidence: Level 2 guardrail/register skill with Glottolog/ISO, dictionary references, Kemdikbud semantic/grammar references, and script support references.
- Source links copied from `sources.md`:
- Glottolog Batak Toba entry, glottocode bata1289 / ISO 639-3 bbc: https://glottolog.org/glottolog?iso=bbc
- Kamus Bahasa Batak Toba, Op Faustin Panjaitan 2010, referenced by Glottolog: https://glottolog.org/resource/reference/id/588972
- Semantik Bahasa Batak Toba, Pusat Bahasa/Kemendikdasmen: https://repositori.kemendikdasmen.go.id/3550/
- Sistem Kata Benda dan Kata Sifat Bahasa Batak Toba, Pusat Pembinaan dan Pengembangan Bahasa: https://repositori.kemendikdasmen.go.id/3693/
- Kamus Bahasa Batak Toba file mirror from Kemdikbud source: https://commons.wikimedia.org/wiki/File:Kamus_Bahasa_Batak_Toba.pdf
- Batak Toba language and alphabet support reference: https://omniglot.com/writing/bataktoba.htm

Source mirror notes:

- Glottolog identifies Batak Toba with glottocode `bata1289`; ISO 639-3 is `bbc`.
- Batak Toba belongs to the Batak language group, but it must not be collapsed into Karo, Simalungun, Mandailing, Angkola, Pakpak, or other Batak languages.
- Kemdikbud semantic and grammar references support source-aware review, but this skill does not contain a full grammar.
- Batak script is culturally important; this skill should not perform public script conversion without source review.

## Local Usability

Use this file as the offline substitute for source orientation. It does not copy a full dictionary. It gives the agent enough local context to decide what it can say directly, what it should keep in Indonesian, and what needs a user sample.

Ordinary short text is allowed when the vocabulary and register are covered by this skill. Sensitive public, ritual, legal, official, or educational wording needs competent speaker review.

The skill may safely produce short greeting/thanks messages, community reminders, admin messages, and AI-output reviews when it avoids kinship/adat overreach.

## Vocabulary And Semantics

- Keep identity terms, names, titles, institutions, and places unchanged unless the user provides the local form.
- Preserve Indonesian words when the regional equivalent is unknown.
- Do not decorate Indonesian grammar with random local words and call it Bahasa Batak Toba.
- Track audience, dialect/community, speech level, and purpose before choosing local terms.
- `Horas`: greeting/well-wishing expression; do not use as a complete adat formula.
- `Mauliate`: thanks phrase; verify address terms around it.
- `Hata Batak Toba`: identity phrase for the language.
- `Amang` and `Inang`: respect/kinship terms; use only when relationship and cultural setting fit.
- `Lae`, `Ito`, `Tulang`, `Hula-hula`, `Boru`, `Dongan tubu`: kinship/adat relation terms; do not assign them without user-provided relationship context.

## Generation Rules

1. Build the meaning in plain Indonesian first.
2. Replace only the words and patterns supported by local references or user-provided samples.
3. Keep uncertain terms visibly marked or left in Indonesian.
4. Add a short review note only when the use case is public, ritual, legal, official, or dialect-sensitive.
5. For professional or public text, keep schedules, prices, policies, church/event details, and legal information in Indonesian unless the user supplies Batak Toba wording.
6. Ask for marga/kinship/adat context before using relationship terms.

## Starter Lexicon Policy

Add only verified terms here. Do not bulk-copy copyrighted dictionaries. Prefer short semantic notes, phrase patterns, and source-backed examples that help an agent write responsibly.

## Register Handling

- Everyday/casual: short `Horas`/`Mauliate` phrases with Indonesian support text.
- Polite/community: use address terms only when relationship is known.
- Professional/admin: keep operational details in Indonesian.
- Adat/wedding/church/ritual/script: do not generate from scratch; ask for source text or competent speaker review.
