# Offline Brief

## Local Facts

- Purpose: ordinary messages, reminders, and review for Bahasa Pakpak.
- Catalog: ISO 639-3 `btd`, glottocode `bata1294`. Glottolog name: Batak Dairi. Book title of the 1977 dictionary: Dairi Pakpak.
- Peta Bahasa: dialek Pakpak (Dairi) of Bahasa Batak, Kabupaten Dairi and Kabupaten Tapanuli Utara, 75,25 percent from dialek Toba.
- USU Press 2023 calls the language Bahasa Pakpak and lists five suak: Sim-sim (Pakpak Bharat), Keppas (Sidikalang and nearby, Dairi), Pegagan (Dairi, including Sumbul), Kelasen (Humbang Hasundutan, and toward Barus), Boang (Aceh Singkil and Subulussalam).
- The same book says `suak` can also mean dialek.
- Phrase source for this skill: Aksara Pakpak, USU Press, 2023. Level 2 because the Manik dictionary exists, with sentences taken from the book that was actually read.
- The 1977 dictionary PDF was not line-checked. Do not invent entries from its title.
- This file is the offline substitute.

## Guardrails

- Do not invent vocabulary, clan formulas, or ritual lines.
- Do not open with Horas or with Karo `mejuah-juah`. The Pakpak form in the book is `njuah-njuah`.
- Do not read `tulanmu` in the phonology example as the Toba kinship title Tulang. The gloss is tulangmu, the bone.
- `mela` is malu. `mella` is kalau. The extra consonant changes the word.
- Written e may be pepet or taling. `mate` mati, `keke` bangkit, and `mbereng` hitam use the hard e in the book's examples. `merampek` renyah and `mbergoh` dingin use the weak e. Do not respell them.
- Keep the nasal on `njuah`, `ndabuh`, `mbages`, `nceda`, and `ncuak`.
- Keep schedules, money, health advice, and official instructions in Indonesian.
- If a full sentence is not in the 2023 book, write a short attested phrase and leave the rest in Indonesian. Label that text mixed.
- Name the suak when the user names a town. Do not pretend one sentence fits all five.

## Sample Prompts

- "Use $tutur-pakpak to adapt this short chat for a cousin in Sidikalang."
- "Review this text. It opens with mejuah-juah. Is that Pakpak?"
- "Greet a group with njuah-njuah mo kita karinana, then Indonesian."
- "Warn someone not to climb the durian tree, using the printed sentence."

## Safe Output Patterns

- Open with `njuah-njuah`. For everyone, the printed line is `njuah-njuah mo kita karinana`.
- A practical warning can be the durian sentence or the broken-bridge sentence, if that is really the situation.
- For an unknown word, keep the Indonesian word.
- For adat, ask the family. Do not compose a menutung tulan utterance.
