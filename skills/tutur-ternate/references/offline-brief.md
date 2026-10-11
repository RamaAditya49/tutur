# Offline Brief

## Local Facts

- Purpose: short messages in Bahasa Ternate, the North Halmahera language.
- Codes: glottocode `tern1247`, ISO 639-3 `tft`.
- Not Melayu Ternate / Melayu Maluku Utara, and not Tidore (`tido1248`, ISO `tvo`).
- Peta Bahasa records Ternate at Togafo (Kota Ternate), Ome (Tidore Utara), and Gamkonora (Halmahera Barat), and it uses dialect labels that include Tidore. This skill still does not write Tidore.
- Verbs take a subject prefix. Free pronouns can be dropped, but this skill does not drop them unless the source sentence already does.
- Peer I, in Duwila: `ngori`, prefix `to-`.
- Respectful I: `fangare` when the speaker is male, `fajaru` when the speaker is female. Prefix still `to-` in the cited sentences.
- Lower you: `ngana`, prefix `no-`. Polite you: `ngon`, prefix `ni-` in Watuseke's table.
- We exclusive: `ngom`, prefix `mi-`. We inclusive: `ngone`.
- Watuseke: `ngori` is not used in polite conversation. `ngana` addresses someone younger or lower.
- This skill should work without browsing.

## Guardrails

- Do not invent vocabulary, titles, or kesultanan formulas.
- Do not put `tara`, `pi`, or `torang` into a Bahasa Ternate line. Those mark Melayu Ternate.
- Do not attach `to-` or `no-` to a verb that is not in an attested sentence.
- Do not use `ngana` when the listener's rank is unknown.
- Do not treat Tidore words as Ternate words.
- One attested clause, then Indonesian. Label mixed text as mixed.
- Court, marriage, and installation language is out of scope.

## Sample Prompts

- "Use $tutur-ternate to review this Bahasa Ternate text."
- "Make a source-aware Bahasa Ternate note to a peer, then Indonesian for the time."
- "Check whether this sentence is Bahasa Ternate or Melayu Ternate."
- "Keep Tidore and sultanate formulas out of this reply."
- "Show `ngori` and `fangare` as two different address situations."

## Safe Output Patterns

- Not knowing: `fangare ware ua`.
- Sitting, peer subject: `Ngori to-tego toma degodego`.
- Going home, exclusive we: `Ngom mi-kudiho toma fala`.
- Leave the hour, the place name added by the user, and the request in Indonesian.
- If the user needs polite you and no attested `ngon` sentence fits, keep the request in Indonesian and name `ngon` as the polite pronoun without building a new clause.
