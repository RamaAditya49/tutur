# Examples

## Target-Language Examples

- Indonesian: "Apa kabar? Bagaimana kabar?"
  Bahasa Gorontalo: "Wolo habali?" Also printed "Wololo habali?"
  Note: Mohamad Karmin Baruadi, Percakapan Bahasa Gorontalo. The polite line in the same list is `Woloolo habali olanto?` "Bagaimana kabar Anda?" Dialogues in the book also print `Wololo habaliinto?` and `wololo habali?`. https://repository.ung.ac.id/get/karyailmiah/2737/Mohamad-Karmin-Baruadi-BUKU-Percakapan-Bahasa-Gorontalo.pdf
  Usage: Ask kabar. Use the `olanto` line when addressing someone as Anda.
- Indonesian: "Terima kasih." "Baik, terima kasih."
  Bahasa Gorontalo: "Odu'olo." "Piyohu, odu'olo."
  Note: Same book. Also `Odu'olo po'odaata` "terima kasih banyak", and `Oo jo, odu'olo` "o iya, terima kasih". Spelling `odu'ola` also occurs.
  Usage: Thanks at the end of a note. `Oo jo, odu'olo` is not a switch into Melayu Manado.
- Indonesian: "Selamat pagi."
  Bahasa Gorontalo: "Paladu u dumodupo." Polite parallel: "Paladu olanto u dumodupo."
  Note: Same book. Siang `Paladu u mohuloonu`, sore `Paladu u lolaango`, malam `Paladu u hui`.
  Usage: Match the time of day. Do not invent a fifth Paladu line.
- Indonesian: "Aku." "Engkau."
  Bahasa Gorontalo: "wau." "yio."
  Note: Pateda, Kamus Bahasa Gorontalo-Indonesia, 1977. Example `yio potibuloa te: to` "engkau duduklah di situ". Example `wau mao mohama buku` "aku pergi mengambil buku". http://www.luk.staff.ugm.ac.id/bahasa/1977-DepdikbudKamusBahasaGorontalo-Indonesia.pdf
  Usage: Pronouns and those two examples only. Do not recombine them into a new errand.
- Indonesian: "Pak Dula dan Bu Dula akan datang dijemput Pak Asi dan Bu Asi di Gorontalo."
  Bahasa Gorontalo: "Temei Dula wolilei Dula mai hamaa lemei Asi wolilei Asi to Hulondalo."
  Note: Gorut News, reporting Pateda's dictionary. `Temei` married man, `Tilei` married woman, plus the nephew's name. Support-level. https://gorutnews.com/kata-sapaan-dalam-bahasa-gorontalo-menurut-kamus-bahasa-gorontalo/
  Usage: Explain the address habit. Do not change Dula or Asi.

## Casual Chat

Input:

> Balas sepupu di Kota Gorontalo yang tanya kabar.

Output (mixed):

> Wolo habali? Aku baik. Keluarga di rumah juga baik. Odu'olo sudah nanya.

Note:

`Wolo habali?` and `Odu'olo` are from the conversation book. "Aku baik" and the family sentence are Indonesian, so the message is mixed. For an older cousin, use `Woloolo habali olanto?` instead of the short form.

## Public Reminder

Input:

> Pengingat kerja bakti pagi untuk warga kelurahan.

Output (mixed):

> Paladu u dumodupo. Besok kerja bakti jam 07.00 di kelurahan. Bawa sapu sendiri. Odu'olo.

Note:

The morning greeting and the thanks are attested. The hour and the tool are Indonesian. If the notice speaks to residents as Anda, the book’s parallel is `Paladu olanto u dumodupo`.

## Professional Or Admin

Input:

> Admin sekolah mengingatkan berkas yang belum masuk.

Output (mixed):

> Paladu u dumodupo. Woloolo habali olanto? Berkas belum lengkap. Mohon kirim sebelum jam 15.00. Odu'olo.

Note:

`Paladu u dumodupo`, `Woloolo habali olanto?`, and `Odu'olo` are attested. The deadline stays Indonesian. Send the morning line only in the morning. Use `Paladu u mohuloonu` if the note goes out at midday.

## Adat Boundary

Input:

> Tuliskan sambutan adat pernikahan Gorontalo.

Output:

> Sambutan adat tidak disusun di sini. Yang tercatat untuk sapaan orang yang sudah menikah, dari laporan atas kamus Pateda, adalah `Temei` atau `Tilei` ditambah nama kemenakan. Itu sapaan, bukan teks nikah. Kalau keluarganya punya rumus sendiri, tempelkan rumus itu.

## Review Mode

Input:

> Cek: "Sto Wolo habali kong, bahasa kita harus lebih modern dan keren."

Response:

1. `Wolo habali` matches the conversation book’s kabar question only if it is `Wolo habali?`. The `sto` and `kong` around it are Melayu Manado, not the Hulontalo samples in this skill.
2. The rest is casual Indonesian. It is not a Gorontalo sentence.
3. No adat formula is present, and none should be added.

Safer rewrite (mixed):

> Wolo habali? Aku lagi catat kata yang pasti dulu. Odu'olo kalau mau bantu cek ejaan Suwawa atau Kota.
