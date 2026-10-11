# Offline Brief

## Local Facts

- Purpose: ordinary messages, adaptation, and review for Bahasa Gorontalo.
- Local name in the sources: Hulontalo, beside the Indonesian name Gorontalo.
- Region: Bone Bolango, Gorontalo Utara, Kota Gorontalo, and Bolango speech in Bolaang Mongondow, Sulawesi Utara.
- ISO 639-3 `gor`. Glottocode `goro1259`. Gorontalo-Mongondow, Gorontalic. Not Melayu Manado. Not Minahasa.
- Source confidence: Level 2. Pateda dictionary (1977 and 2001) and Baruadi's conversation book.
- Peta Bahasa dialects: Suwawa, Atinggola, Kota, Bolango. Differences about 51%–78%. Difference from neighboring languages in the province about 81%–100%.
- Glottolog dialects, kept separate from the Peta Bahasa list: East Gorontalo, Gorontalo Kota, Limboto, Tilamuta, West Gorontalo.
- Conversation-book greetings: `Wolo habali?` / `Wololo habali?` apa kabar / bagaimana kabar. `Woloolo habali olanto?` bagaimana kabar Anda. `Odu'olo` terima kasih. `Paladu u dumodupo` selamat pagi. `Piyohu, odu'olo` baik, terima kasih.
- Pateda 1977: `wau` aku, `yio` engkau.
- Support note: married address `Temei` (man) and `Tilei` (woman) plus a nephew's name, as reported from Pateda's dictionary.

## Guardrails

- Do not invent vocabulary or adat formulas.
- Do not write Melayu Manado (`sto`, `kong`, `dang`) and call it Gorontalo.
- The conversation book prints `Oo jo, odu'olo` for "o iya, terima kasih". That line is not a license to switch the rest of the message into Manado Malay.
- Do not normalize `Wolo` / `Wololo` / `Woloolo` or `Odu'olo` / `odu'ola` into a new spelling.
- Do not invent a `Temei` or `Tilei` name. Use the pattern only when the user supplies the nephew's name and the source note is kept.
- Keep prices, schedules, health, and permits in Indonesian.
- Label mixed Gorontalo-Indonesian text as mixed.
- Public and adat text needs a Gorontalo speaker.

## Sample Prompts

- "Use $tutur-gorontalo to review this Bahasa Gorontalo text."
- "Reply to a cousin in Kota Gorontalo. Ask kabar with Wolo habali and keep the rest in Indonesian."
- "Check that this is Hulontalo and not Melayu Manado."
- "Write a morning guest note that uses Paladu u dumodupo."
- "Review a wedding speech. Do not invent the adat lines."

## Safe Output Patterns

- Open with `Wolo habali?` or `Paladu u dumodupo`, then the point in Indonesian.
- Close a thanks with `Odu'olo`.
- Use `Woloolo habali olanto?` when the addressee is being treated politely.
- Leave unattested content words in Indonesian.
- For adat, ask for a speaker sample.
