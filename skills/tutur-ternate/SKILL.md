---
name: tutur-ternate
description: Produce, adapt, or review short text in Bahasa Ternate of North Maluku, the North Halmahera language. Use when the user asks for Bahasa Ternate or bahasa Ternate asli. Keep Ternate Malay and Tidore separate. Do not invent sultanate court formulas. Use only attested words with their person prefixes, and leave the rest in Indonesian.
---

# Tutur Ternate

## Overview

Use this skill for Bahasa Ternate, the North Halmahera language of Ternate and Ternate communities in North Maluku. Glottolog: glottocode `tern1247`, ISO 639-3 `tft`. It is not an Austronesian Malay. Verbs take a person prefix that agrees with the subject.

Melayu Ternate, also called Melayu Maluku Utara or bahasa pasar, is a different language. Its clauses use Malay grammar (`tara`, `pi`, `torang`) even when a word such as `ngana` was borrowed from Bahasa Ternate. Tidore is a separate Glottolog language, glottocode `tido1248`, ISO 639-3 `tvo`. Peta Bahasa prints "dialek Tidore" inside its Ternate survey page. This skill follows the Glottolog split and does not write Tidore.

Source confidence: Level 2 for the short sentences in Watuseke's sketch and in the 2019 Gramatika article from Kantor Bahasa Maluku Utara. Atjo's dictionary is cited by that article. This skill does not invent sentences beyond those lines.

## Search And Discovery

Relevant searches: Bahasa Ternate, kamus Bahasa Ternate, contoh Bahasa Ternate, belajar Bahasa Ternate, terjemahan Indonesia Ternate, translate Bahasa Ternate, ngori fangare fajaru, bahasa Ternate asli, Melayu Ternate, Tidore, AI skill Bahasa Ternate.

Use this skill for source-aware Bahasa Ternate. It is not a certified translator, not a Melayu Ternate writer, and not a source of sultanate speech.

## Human Voice

A peer-level line starts with `ngori` and a verb that already carries `to-`, as in `Ngori to-tego toma degodego`. Talking to someone who should be respected, the sources switch the subject to `fangare` for a man speaking or `fajaru` for a woman speaking, still with `to-` on the verb. `ngana` is the lower you, for someone younger or of lower rank in Watuseke's sketch, and the verb then takes `no-`. The polite you is `ngon`. People do not sound like Indonesian with `ngori` glued on, and they do not sound like Melayu Ternate (`kita tara`, `torang`). After one attested clause, the rest of a chat belongs in ordinary Indonesian.

## Workflow

1. Identify the language.
   - Bahasa Ternate, bahasa Ternate asli, North Halmahera Ternate: use this skill.
   - Melayu Ternate, Melayu Maluku Utara, bahasa pasar Ternate: label it as Malay and do not use this skill's prefixes on Malay verbs.
   - Tidore: stop. Name the separate code and ask for Tidore sources.

2. Check source confidence.
   - Use `references/sources.md` first.
   - Copy pronoun-plus-prefix pairs only from the listed sentences.
   - If the listener's rank is unknown, do not guess between `ngana` and `ngon`.

3. Compose with source discipline.
   - Keep names, places, dates, and facts unchanged.
   - Do not build a new prefixed verb.
   - One attested clause, then Indonesian. Label mixed text as mixed.

4. Final pass.
   - Do not add court titles or ceremony language.
   - Do not claim native-speaker or kesultanan authority.

## Output Style

- For direct requests, return the adapted output first.
- For review requests, separate Bahasa Ternate from Melayu Ternate before rewriting.
- For public, legal, or adat use, keep the operative text in Indonesian.
- Mark mixed text as mixed.

## Resources

- `references/offline-brief.md`: compact local brief for agents without internet access.
- `references/local-mirror.md`: local mirror of source facts, vocabulary policy, and semantic guidance.
- `references/usage-patterns.md`: task patterns and review checklist for offline use.
- `references/sources.md`: source links and confidence level.
- `references/style-guide.md`: practical register and safety rules.
- `references/examples.md`: sourced usage examples.
