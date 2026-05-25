# Indonesian Humanizer Research Notes

Date: 2026-05-25

## Goal

Build a humanizer skill for Indonesian text that does more than translate English humanizer rules. Indonesian needs register control: official, formal, professional, casual, slang, and sales copy use different word choices and sentence rhythms.

## Sources

- EYD V: https://ejaan.kemdikbud.go.id/
- KBBI Daring: https://kbbi.kemdikbud.go.id/
- KBBI Petunjuk Pemakaian: https://kbbi.kemendikdasmen.go.id/Content/Files/Petunjuk%20Pemakaian.PDF
- Pedoman Umum Pembentukan Istilah: https://badanbahasa.kemendikdasmen.go.id/resource/doc/files/Pedoman_Umum_Pembentukan_Istilah_PBN_0.pdf

## Findings

1. EYD V should be the default authority for official spelling, punctuation, capitalization, word writing, and loanword spelling.

2. KBBI is useful for meaning and labels, but it is not a blanket permission to use a word in every context. Labels such as `cak`, `kas`, `hor`, and regional labels matter. A word can be valid Indonesian and still be wrong for an official letter.

3. KBBI's usage guidance distinguishes language variation by use, medium, relationship between speakers, dialect, and idiolect. This supports Tutur's main editorial position: "natural" depends on audience and context.

4. PUPI is useful for technical and professional text because terminology should be precise, concise, have suitable connotation, sound natural, and follow Indonesian word-formation rules.

5. Indonesian AI text often fails because of tone and rhythm, not only grammar. The most common problems are:
   - generic openers,
   - inflated significance,
   - vague business claims,
   - English calques,
   - bureaucratic padding,
   - formulaic contrast,
   - weak summary endings,
   - overlong "yang" chains.

## Editorial Direction

Tutur should preserve register. Do not automatically make text formal. Do not automatically make text slangy. The default should be readable public Indonesian: clean, natural, and not stiff.

For official/formal output, enforce standard Indonesian. For casual or gaul output, preserve intentional nonstandard forms when they fit the audience and do not confuse meaning.

## Product Direction

The repository should start with one broad skill:

- `tutur-humanizer`

Later skills can be narrower and more opinionated:

- `tutur-resmi`
- `tutur-gaul`
- `tutur-profesional`
- `tutur-salesman`

This keeps the first release useful while leaving room for specialist skills.
