# Offline Brief

## Local Facts

- Purpose: ordinary messages, reminders, and review for Bahasa Komering.
- Region: Sumatra Selatan. Peta Bahasa names Ogan Komering Ulu, Ogan Komering Ulu Timur, and Ogan Komering Ulu Selatan, plus the villages it uses as observation points.
- Dialects on Peta Bahasa: Pulau Negara and Aji. Difference between them is given as about 51–80 percent.
- Aji is named for Desa Negeri Batin, OKU Timur. Pulau Negara is named for Sriwangi, Campang Tiga, Sukaraja, Pulau Negara, and Batu Raja Bungin.
- Catalog: ISO 639-3 `kge`, glottocode `kome1238`. Glottolog and ABVD place it in the Lampungic group. It is not Bahasa Lampung.
- Peta Bahasa counts Komering as a separate language from Pedamaran, Ogan, Melayu, Lematang, and Kayu Agung, at about 81–100 percent difference.
- Phrase source: Kamus Komering Indonesia on the Balai Bahasa Sumatera Selatan site. Level 2.
- The public word list does not mark dialect on each example.
- This file is the offline substitute. It does not replace the dictionary.

## Guardrails

- Do not invent vocabulary, titles, or adat formulas.
- Do not copy Bahasa Lampung, including `tabik pun` and the Api/Nyo split.
- Do not treat Pulau Negara and Aji as one wording when the user named a village.
- Do not label a dictionary sentence as Aji or Pulau Negara. The word list does not.
- `tabik` means permisi while passing people who are seated, with the body lowered. It is not a general hello.
- Keep schedules, money, health advice, and official instructions in Indonesian.
- If a full sentence is not in the dictionary, write a short attested phrase and leave the rest in Indonesian. Label that text mixed.
- Do not recombine `nyak`, `niku`, and `sikam` into a sentence the dictionary does not print.

## Sample Prompts

- "Use $tutur-komering to adapt this short chat for a cousin in OKU Timur."
- "Review this text. Is it Bahasa Komering or Bahasa Lampung with a Komering label?"
- "Write a neighbor reminder. One dictionary line, rest in Indonesian."
- "Someone is walking past seated elders. Use the tabik example, not a Lampung greeting."

## Safe Output Patterns

- Open with one dictionary sentence when it matches the situation, then the practical point in Indonesian.
- For a cousin, a question already printed in the dictionary is enough. Do not add a fake greeting in front of it.
- For an unknown word, keep the Indonesian word.
- For adat, ask for the wording used by the family. Do not expand `adat kumoring` into a wedding speech.
