# Local Mirror

## Source Mirror

- Language/register: Bahasa Lampung.
- Region/context: Provinsi Lampung dan komunitas Lampung diaspora; perhatikan variasi dialek Api/A dan Nyo/O serta aksara Lampung.
- Source confidence: Level 2 guardrail/register skill with official Kamus Daring Bahasa Lampung, Kemdikbud dictionary material, Glottolog/WALS identity references, and script references.
- Source links copied from `sources.md`:
- Kamus Daring Bahasa Lampung resmi: https://kamuslampung.kemendikdasmen.go.id/
- Balai Bahasa Provinsi Lampung, Kamus Daring Lampung-Indonesia: https://balaibahasalampung.kemendikdasmen.go.id/kamus-daring-lampung-indonesia/
- Kamus Lampung-Indonesia, Pusat Pembinaan dan Pengembangan Bahasa/Kemendikdasmen: https://repositori.kemendikdasmen.go.id/2930/
- Glottolog Lampung Api entry, glottocode lamp1243 / ISO 639-3 ljp: https://glottolog.org/glottolog?iso=ljp
- WALS Lampung entry, glottocode lamp1243 / ISO 639-3 ljp: https://wals.info/languoid/lect/wals_code_lmp
- ScriptSource Lampung Api, ljp-Latn support: https://scriptsource.org/cms/scripts/page.php?item_id=language_detail&key=ljp
- Unicode proposal for Lampung script notes Lampung Api and Lampung Nyo: https://www.unicode.org/L2/L2022/22044-lampung.pdf

Source mirror notes:

- Official Kamus Daring Bahasa Lampung is the preferred word-check source.
- Glottolog/WALS references identify Lampung Api with glottocode `lamp1243` and ISO 639-3 `ljp`.
- Lampung language work must account for Api/A and Nyo/O dialect labels.
- Lampung script/aksara is culturally important and requires source-aware handling.

## Local Usability

Use this file as the offline substitute for source orientation. It does not copy a full dictionary. It gives the agent enough local context to decide what it can say directly, what it should keep in Indonesian, and what needs a user sample.

Ordinary short text is allowed when the vocabulary and register are covered by this skill. Sensitive public, ritual, legal, official, or educational wording needs competent speaker review.

The skill may safely produce short Lampung-aware greetings, dialect-labelled examples, community reminders, tourism/admin messages, and AI-output reviews when it keeps unsupported parts in Indonesian.

## Vocabulary And Semantics

- Keep identity terms, names, titles, institutions, and places unchanged unless the user provides the local form.
- Preserve Indonesian words when the regional equivalent is unknown.
- Do not decorate Indonesian grammar with random local words and call it Bahasa Lampung.
- Track audience, dialect/community, speech level, and purpose before choosing local terms.
- `Tabik pun`: respect/greeting cue; use as a short opening, not as full adat formula.
- `Kabar wawai`: "kabar baik" phrase in support sources.
- `Api kabar?`: Lampung Api/A-oriented "apa kabar?" phrase; verify dialect.
- `Nyow kabar?`: Lampung Nyo/O-oriented "apa kabar?" phrase; verify dialect.
- Aksara Lampung: script work requires source sample or specialist review.

## Generation Rules

1. Build the meaning in plain Indonesian first.
2. Replace only the words and patterns supported by local references or user-provided samples.
3. Keep uncertain terms visibly marked or left in Indonesian.
4. Add a short review note only when the use case is public, ritual, legal, official, or dialect-sensitive.
5. Label dialect variants when offering both Api/A and Nyo/O forms.
6. For professional or public text, keep schedules, prices, policy, safety, and administrative facts in Indonesian unless the user supplies Lampung wording.

## Starter Lexicon Policy

Add only verified terms here. Do not bulk-copy copyrighted dictionaries. Prefer short semantic notes, phrase patterns, and source-backed examples that help an agent write responsibly.

## Register Handling

- Everyday/casual: use short dialect-labelled phrases.
- Polite/public: use `Tabik pun` with clear Indonesian support text.
- Professional/tourism/admin: keep operational details in Indonesian.
- Adat/ceremony/aksara: do not generate from scratch; ask for source text or competent speaker review.
