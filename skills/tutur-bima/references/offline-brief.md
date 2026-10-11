# Offline Brief

## Local Facts

- Purpose: ordinary messages, adaptation, and review for Bahasa Bima / Nggahi Mbojo.
- Region: Kabupaten Bima, Kota Bima, Kabupaten Dompu, east Sumbawa. Peta Bahasa also notes speech in parts of Kabupaten Sumbawa, Lombok, and Reo and Pota in Manggarai.
- ISO 639-3 `bhp`. Glottocode `bima1247`. Bima-Sumba group. Not Bahasa Sumbawa (Samawa). Not Sasak.
- Dialects in Peta Bahasa: Serasuba, Wawo, Kolo, Kore. Differences about 51%–55%. Difference from Samawa and Sasak about 81%–100%.
- Source confidence: Level 2. Kamus Mbojo-Indonesia exists. Usable pairs here come from the 2021 Kota Bima curriculum book and Hasan 2021.
- Nggahi halus / nggahi kasa pairs from that book: `mada` / `nahu` saya, `ita` / `nggomi` kamu, `ngaha` / `lohi ra'a` makan, `iha` / `dabae` rusak.
- Hasan 2021: `mada` when the speaker is younger, `nahu` when the speaker is older or a peer, `ita` as polite you, `nggomi` as kamu to a younger person or a peer.
- Hasan's glossed line: `Sakola tabe nggomi Hama?` sekolah di mana kamu, Achmad. Peer or younger addressee, not an elder.
- Support phrases: `Santabe ta` permisi/silakan, `Bune haba?` apa kabar.
- Hasan says Bima personal names in address end in a vowel, and respectful nickname vowels are not a fixed rule. Do not generate new ones.

## Guardrails

- Do not invent vocabulary, patu, kande, jiki, or sultanate lines.
- Do not mix halus and kasa toward the same person in one message.
- Do not turn Hama/Hima, Hasa/Heso, or Mina/Mene into a machine for other names.
- Do not answer with Samawa or Sasak.
- Keep schedules, money, health, and documents in Indonesian.
- Label mixed Bima-Indonesian text as mixed.
- A phrase-list greeting is a short opener, not a paragraph.
- Public and adat text needs a Bima speaker.

## Sample Prompts

- "Use $tutur-bima to review this Nggahi Mbojo text."
- "Write a cousin chat in Bima. Peer register, nggomi, not ita."
- "Write the same note to an older neighbor. Use ita, not nggomi."
- "Check that this is not Bahasa Sumbawa."
- "Review a patu. Do not add lines."

## Safe Output Patterns

- Open with `Santabe ta`, then Indonesian.
- Ask kabar with `Bune haba?` and stop there.
- Choose `mada`/`ita` or `nahu`/`nggomi` from the age relation, and say which one you chose.
- Use `Sakola tabe nggomi Hama?` only as the published example, or as a pattern when the user has confirmed a peer named in that way.
- For adat and pantun, ask for the local text.
