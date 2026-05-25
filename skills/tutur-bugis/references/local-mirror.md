# Local Mirror

## Source Mirror

- Language/register: Bahasa Bugis.
- Region/context: Sulawesi Selatan dan komunitas Bugis diaspora; termasuk variasi lokal seperti Soppeng, Bone, Wajo, Sidenreng Rappang, Sinjai, dan daerah Bugis lainnya.
- Source confidence: Level 2 guardrail/register skill with Kemdikbud/Balai Bahasa dictionaries, Peta Bahasa, Glottolog/ISO, and politeness references.
- Source links copied from `sources.md`:
- Peta Bahasa Provinsi Sulawesi Selatan, Badan Bahasa: https://petabahasa.kemdikbud.go.id/provinsi.php?idp=Sulawesi+Selatan
- Kamus Bahasa Bugis-Indonesia, repositori Kemdikbud: https://repositori.kemdikbud.go.id/2856/
- Kamus Bugis-Indonesia edisi revisi, Balai Bahasa Provinsi Sulawesi Selatan: https://repositori.kemendikdasmen.go.id/29004/1/Kamus%20Bugis-Indonesia.pdf
- Kamus Bugis-Indonesia, Balai Bahasa Provinsi Sulawesi Selatan: https://repositori.kemendikdasmen.go.id/35378/1/Kamus%20Bugis-Indonesia.pdf
- Glottolog Bugis entry, glottocode bugi1244 / ISO 639-3 bug: https://glottolog.org/glottolog?iso=bug
- ABVD Buginese Soppeng wordlist, ISO 639-3 bug / glottocode bugi1244: https://abvd.eva.mpg.de/austronesian/language.php?id=48
- Kesantunan berbahasa Bugis references mention iye, tabe, and idi' as politeness markers: https://download.garuda.kemdikbud.go.id/article.php?article=1079193&title=KESANTUNAN+BERBAHASA+BUGIS+PADA+MASYARAKAT+BUGIS+DI+KABUPATEN+SINJAI+PROVINSI+SULAWESI+SELATAN&val=16277

Source mirror notes:

- Glottolog identifies Bugis with glottocode `bugi1244`; ISO 639-3 is `bug`.
- ABVD lists a Buginese Soppeng wordlist under the South Sulawesi group.
- Peta Bahasa Sulawesi Selatan lists Bugis as a language with South Sulawesi homeland.
- Public sources and politeness references show that `tabe'`, `iye`, and `idi'` carry etiquette/politeness value; do not use them as decoration without context.

## Local Usability

Use this file as the offline substitute for source orientation. It does not copy a full dictionary. It gives the agent enough local context to decide what it can say directly, what it should keep in Indonesian, and what needs a user sample.

Ordinary short text is allowed when the vocabulary and register are covered by this skill. Sensitive public, ritual, legal, official, or educational wording needs competent speaker review.

The skill may safely produce short Bugis-aware greetings, polite reminders, invitations, and review comments when it uses supported forms and keeps operational details clear.

## Vocabulary And Semantics

- Keep identity terms, names, titles, institutions, and places unchanged unless the user provides the local form.
- Preserve Indonesian words when the regional equivalent is unknown.
- Do not decorate Indonesian grammar with random local words and call it Bahasa Bugis.
- Track audience, dialect/community, speech level, and purpose before choosing local terms.
- `Tabe'`: permission/excuse/politeness cue. Use as a short opening or etiquette marker, not as a full ceremonial formula.
- `Iye`: affirmative/polite response marker. Context and spelling can vary.
- `Idi'`: respectful second-person address. Use when polite address fits.
- `Basa Ugi`: common identity phrase for Bahasa Bugis.
- Lontara script is culturally important but this skill is not a script transliteration authority unless a source sample is provided.

## Generation Rules

1. Build the meaning in plain Indonesian first.
2. Replace only the words and patterns supported by local references or user-provided samples.
3. Keep uncertain terms visibly marked or left in Indonesian.
4. Add a short review note only when the use case is public, ritual, legal, official, or dialect-sensitive.
5. For professional or public text, keep schedules, prices, policy, legal, safety, and administrative facts in Indonesian unless the user supplies Bugis wording.
6. Ask for target community or area when the output is for Bone, Wajo, Soppeng, Sidrap, Sinjai, or another local Bugis context.

## Starter Lexicon Policy

Add only verified terms here. Do not bulk-copy copyrighted dictionaries. Prefer short semantic notes, phrase patterns, and source-backed examples that help an agent write responsibly.

## Register Handling

- Everyday/casual: use short politeness markers and clear Indonesian support text.
- Polite/public: use `tabe'`, `iye`, or `idi'` only where the relationship and tone fit.
- Professional: keep operational details in Indonesian.
- Adat/ceremony/religious/wedding: do not generate formulas from scratch; ask for source text or competent speaker review.
