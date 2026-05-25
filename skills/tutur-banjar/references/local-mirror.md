# Local Mirror

## Source Mirror

- Language/register: Bahasa Banjar.
- Region/context: Kalimantan Selatan dan komunitas Banjar di Kalimantan serta diaspora; dialek utama Banjar Kuala dan Banjar Hulu.
- Source confidence: Level 2 guardrail/register skill with Kemdikbud/Balai Bahasa dictionaries and Glottolog/ISO references.
- Source links copied from `sources.md`:
- Kamus Banjar-Indonesia, Pusat Pembinaan dan Pengembangan Bahasa/Kemdikbud: https://repositori.kemdikbud.go.id/2888/
- Kamus Bahasa Banjar-Indonesia untuk Pelajar, Balai Bahasa Provinsi Kalimantan Selatan: https://repositori.kemendikdasmen.go.id/35353/1/Kamus%20Bahasa%20Banjar-Indonesia%20untuk%20Pelajar.pdf
- Kamus Bahasa Banjar Dialek Hulu-Indonesia: https://repositori.kemendikdasmen.go.id/2855/1/kamus%20bahasa%20banjar%20dialek%20hulu.pdf
- Glottolog Banjar entry, glottocode banj1239 / ISO 639-3 bjn: https://glottolog.org/glottolog?iso=bjn
- ABVD Banjarese Malay wordlist, ISO 639-3 bjn / glottocode banj1239: https://lpan.eva.mpg.de/austronesian/language.php?id=150

Source mirror notes:

- Glottolog identifies Banjar with glottocode `banj1239`; ISO 639-3 is `bjn`.
- Banjar is commonly associated with Kalimantan Selatan and Banjar communities in wider Kalimantan and diaspora.
- Practical dialect labels used by source materials include Banjar Kuala and Banjar Hulu.
- Kemdikbud/Balai Bahasa dictionary material gives a stronger base than community phrase lists; use community phrase lists only as support.

## Local Usability

Use this file as the offline substitute for source orientation. It does not copy a full dictionary. It gives the agent enough local context to decide what it can say directly, what it should keep in Indonesian, and what needs a user sample.

Ordinary short text is allowed when the vocabulary and register are covered by this skill. Sensitive public, ritual, legal, official, or educational wording needs competent speaker review.

The skill may safely produce short Banjar-aware greetings, polite reminders, simple community copy, and AI-output reviews when the examples stay within verified vocabulary and ordinary context.

## Vocabulary And Semantics

- Keep identity terms, names, titles, institutions, and places unchanged unless the user provides the local form.
- Preserve Indonesian words when the regional equivalent is unknown.
- Do not decorate Indonesian grammar with random local words and call it Bahasa Banjar.
- Track audience, dialect/community, speech level, and purpose before choosing local terms.
- `Ulun`: first-person form, often useful for polite self-reference.
- `Pian`: second-person form, often used for "you/Anda"; relationship and politeness matter.
- `Apa habar?`: everyday "apa kabar?" pattern.
- `Bujur`: "benar/right"; also useful as an affirmation marker in short examples.
- `Lawan`: common relation/preposition form in phrase examples; do not overgeneralize grammar from one phrase.
- `Hanyar`: common word meaning "baru" in many Banjar examples; verify use before formal output.
- `Kada`: common negation form; use only in simple contexts unless grammar is clear.

## Generation Rules

1. Build the meaning in plain Indonesian first.
2. Replace only the words and patterns supported by local references or user-provided samples.
3. Keep uncertain terms visibly marked or left in Indonesian.
4. Add a short review note only when the use case is public, ritual, legal, official, or dialect-sensitive.
5. For professional or government-adjacent text, keep dates, prices, policy, legal, and procedural details in Indonesian.
6. Ask for Banjar Kuala or Banjar Hulu target when dialect flavor matters.

## Starter Lexicon Policy

Add only verified terms here. Do not bulk-copy copyrighted dictionaries. Prefer short semantic notes, phrase patterns, and source-backed examples that help an agent write responsibly.

## Register Handling

- Everyday/casual: short chat phrases and familiar community wording.
- Polite: use `ulun` and `pian` carefully; avoid over-intimacy.
- Public/formal: use Indonesian structure with limited Banjar phrases unless the user supplies local source text.
- Professional: keep operational details clear in Indonesian.
- Adat/ceremony/religious: do not generate formulas from scratch; request a source sample or local speaker review.
