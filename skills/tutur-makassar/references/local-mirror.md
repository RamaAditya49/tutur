# Local Mirror

## Source Mirror

- Language/register: Bahasa Makassar.
- Region/context: Sulawesi Selatan: Kota Makassar, Gowa, Takalar, Jeneponto, Bantaeng, Maros, Pangkajene Kepulauan, Kepulauan Selayar, dan komunitas Makassar diaspora menurut Peta Bahasa.
- Source confidence: Level 2 guardrail/register skill with Peta Bahasa, Kemdikbud/Balai Bahasa dictionaries, structure notes, Glottolog/ISO, ABVD, and politeness references.
- Source links copied from `sources.md`:
- Peta Bahasa Makassar, Badan Bahasa: https://petabahasa.kemdikbud.go.id/infobahasa.php?idb=177
- Kamus Makassar-Indonesia, repositori Kemendikdasmen: https://repositori.kemendikdasmen.go.id/2931/
- Kamus Indonesia-Makassar Edisi Revisi, Balai Bahasa Provinsi Sulawesi Selatan: https://repositori.kemendikdasmen.go.id/35499/1/Kamus%20Indonesia-Makassar%20Edisi%20Revisi.pdf
- Struktur Bahasa Makassar, repositori Kemendikdasmen: https://repositori.kemendikdasmen.go.id/3669/1/struktur%20bahasa%20makassar%201981%20%20%20%2063h.pdf
- Glottolog Makasar entry, glottocode maka1311 / ISO 639-3 mak: https://glottolog.org/resource/languoid/id/maka1311
- ABVD Makassar wordlist, ISO 639-3 mak / glottocode maka1311: https://abvd.eva.mpg.de/austronesian/language.php?id=166
- Makassar politeness support for tabe and iye: https://repository.unhas.ac.id/48312/2/F021201003-1cMZmuti8jLPnHp7-20250321143252.pdf

Source mirror notes:

- Peta Bahasa lists Bahasa Makassar in Kota Makassar, Gowa, Takalar, Jeneponto, Bantaeng, Maros, Pangkajene Kepulauan, Kepulauan Selayar, and related areas.
- Glottolog identifies Makasar with glottocode `maka1311`; ISO 639-3 is `mak`.
- ABVD lists a Makassar wordlist under the South Sulawesi group.
- `Tabe'` and `iye'` are politeness/affirmation cues in Makassar support sources; use them carefully and do not overextend them.

## Local Usability

Use this file as the offline substitute for source orientation. It does not copy a full dictionary. It gives the agent enough local context to decide what it can say directly, what it should keep in Indonesian, and what needs a user sample.

Ordinary short text is allowed when the vocabulary and register are covered by this skill. Sensitive public, ritual, legal, official, or educational wording needs competent speaker review.

The skill may safely produce short Makassar-aware greetings, tourism/admin messages, invitations, and AI-output reviews when it keeps the unsupported parts in Indonesian.

## Vocabulary And Semantics

- Keep identity terms, names, titles, institutions, and places unchanged unless the user provides the local form.
- Preserve Indonesian words when the regional equivalent is unknown.
- Do not decorate Indonesian grammar with random local words and call it Bahasa Makassar.
- Track audience, dialect/community, speech level, and purpose before choosing local terms.
- `Tabe'`: respect/permission/excuse cue. Use as a short opening or etiquette marker.
- `Iye'`: polite affirmative. Context and spelling can vary.
- `Basa Mangkasara`: common identity phrase for Bahasa Makassar; verify formal spelling when printing.
- Bahasa Makassar is distinct from Makassar Malay or Indonesian spoken with Makassar local flavor.

## Generation Rules

1. Build the meaning in plain Indonesian first.
2. Replace only the words and patterns supported by local references or user-provided samples.
3. Keep uncertain terms visibly marked or left in Indonesian.
4. Add a short review note only when the use case is public, ritual, legal, official, or dialect-sensitive.
5. For professional or tourism text, keep schedules, prices, policy, safety, and administrative facts in Indonesian unless the user supplies Makassar wording.
6. Ask for target community or area when the output is for Gowa, Takalar, Jeneponto, Bantaeng, Maros, Pangkep, Selayar, or Makassar city context.

## Starter Lexicon Policy

Add only verified terms here. Do not bulk-copy copyrighted dictionaries. Prefer short semantic notes, phrase patterns, and source-backed examples that help an agent write responsibly.

## Register Handling

- Everyday/casual: short Makassar cues with Indonesian support text.
- Polite/public: use `tabe'` or `iye'` only when the relationship and tone fit.
- Professional/tourism: keep operational details in Indonesian.
- Adat/ceremony/religious/wedding: do not generate formulas from scratch; ask for source text or competent speaker review.
