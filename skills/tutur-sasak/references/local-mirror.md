# Local Mirror

## Source Mirror

- Language/register: Bahasa Sasak.
- Region/context: Pulau Lombok, Nusa Tenggara Barat; sebaran diaspora di Bali, Sulawesi Tenggara, dan Lampung menurut Peta Bahasa.
- Source confidence: Level 2 guardrail/register skill with official Peta Bahasa and Kamus Sasak-Indonesia references.
- Source links copied from `sources.md`:
- Peta Bahasa Sasak, Badan Bahasa: https://petabahasa.kemdikbud.go.id/infobahasa.php?idb=217
- Kamus Sasak-Indonesia, Kantor Bahasa Provinsi NTB, 2018: https://repositori.kemendikdasmen.go.id/20342/
- Glottolog Sasak entry, glottocode sasa1249: https://glottolog.org/resource/languoid/id/sasa1249
- ABVD Sasak wordlist, ISO 639-3 sas / glottocode sasa1249: https://abvd.eva.mpg.de/austronesian/language.php?id=185
- Struktur Bahasa Sasak Umum, Pusat Bahasa/Kemendikdasmen repository: https://repositori.kemendikdasmen.go.id/2542/
- Sasak phrasebook support for everyday phrases: https://id.wikivoyage.org/wiki/Buku_percakapan_Sasak

Peta Bahasa mirror:

- Tanah asal Bahasa Sasak berada di Pulau Lombok.
- Peta Bahasa describes four phonological dialect variants: `[a-a]`, `[a-â]`, `[â-â]`, and `[a-o]`.
- Example variation in the source includes forms for "mata" and "apa" that differ by final or central vowel quality.
- The `[a-a]` variant is associated with areas such as Sembalun, Bayan, Tanjung, Pringgasela, Sokong, Tebango, and parts of Lombok Timur.
- The `[a-â]` variant spreads broadly from west to east Lombok and is described as widely used.
- The `[â-â]` and `[a-o]` variants occur in more specific areas of Lombok Barat, Lombok Tengah, and Lombok Timur.
- Peta Bahasa also notes social variation, here operationalized as ordinary/biasa and polite/halus.
- Sasak also has diaspora/sebaran notes outside Lombok, including Bali, Sulawesi Tenggara, and Lampung.

## Local Usability

Use this file as the offline substitute for source orientation. It does not copy a full dictionary. It gives the agent enough local context to decide what it can say directly, what it should keep in Indonesian, and what needs a user sample.

Ordinary short text is allowed when the vocabulary and register are covered by this skill. Sensitive public, ritual, legal, official, or educational wording needs competent speaker review.

The skill may safely produce short greetings, thanks, permission phrases, tourism welcome notes, community reminders, and review comments when the output is framed as source-aware and not a certified translation.

## Vocabulary And Semantics

- Keep identity terms, names, titles, institutions, and places unchanged unless the user provides the local form.
- Preserve Indonesian words when the regional equivalent is unknown.
- Do not decorate Indonesian grammar with random local words and call it Bahasa Sasak.
- Track audience, dialect/community, speech level, and purpose before choosing local terms.
- `Berembe kabar?`: everyday phrase for asking how someone is.
- `Matur tampiasih`: polite thanks phrase used in support sources.
- `Tabeq`: permission/excuse phrase tied to etiquette; use as a short phrase, not a full ritual marker.
- `Silaq` or `silak`: supporting phrase-list form for please/please go ahead; spelling may vary.
- `Aoq` and `Ndeq`: yes/no forms in supporting phrase lists; verify before formal publication.
- `Pade-pade`: supporting phrase-list form for "sama-sama"; use only in simple everyday context.

## Generation Rules

1. Build the meaning in plain Indonesian first.
2. Replace only the words and patterns supported by local references or user-provided samples.
3. Keep uncertain terms visibly marked or left in Indonesian.
4. Add a short review note only when the use case is public, ritual, legal, official, or dialect-sensitive.
5. For public/tourism copy, use short Sasak phrases plus clear Indonesian so the message stays accessible.
6. For professional use, keep operational details in Indonesian unless a Sasak speaker supplies the exact local wording.

## Starter Lexicon Policy

Add only verified terms here. Do not bulk-copy copyrighted dictionaries. Prefer short semantic notes, phrase patterns, and source-backed examples that help an agent write responsibly.

## Register Handling

- Everyday/casual: short phrases are acceptable when the relationship is peer-level or visitor-facing.
- Polite/halus: prefer short verified expressions and ask for a local sample when speaking to elders or community leaders.
- Public/formal: use Indonesian as the structural base and include Sasak phrases only where checked.
- Professional: keep schedules, prices, policy, health, safety, and legal details in Indonesian unless the user supplies verified Sasak wording.
- Adat/ceremony: do not generate formulas from scratch; request source text or speaker review.
