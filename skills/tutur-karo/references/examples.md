# Examples

Glosses below were read from the public OCR of Kamus Bahasa Karo-Indonesia, Pusat Bahasa / Balai Pustaka, 2001: https://adoc.pub/pusat-bahasa-departemen-pendidikan-nasional-o-balai-pustaka.html

The catalog record for that book is https://elibrary.uinbanten.ac.id/index.php?id=8885&keywords=&p=show_detail

Label: mixed, whenever Indonesian carries the rest of the message. Broken OCR lines are not repaired into new Karo.

## Target-Language Examples

- Indonesian: "Sehat-sehat; selamat."
  Bahasa Karo: "Mejuah-juah."
  Note: Headword gloss in the 2001 dictionary: sehat-sehat; selamat. It is not Horas.
  Usage: One person to one person. The other person can answer with the same word.
- Indonesian: "Sehat kita semua."
  Bahasa Karo: "Mejuah-juah kita kerina."
  Note: The dictionary prints this as the dashed example under `mejuah-juah`.
  Usage: A group. Do not use it as a slogan with extra clauses attached.
- Indonesian: "Terima kasih."
  Bahasa Karo: "Bujur."
  Note: Headword gloss. The example sentence in the OCR runs into the next entry, so only the word is quoted.
  Usage: Thanks at the end of a chat. Not mauliate.
- Indonesian: "Ia berbicara Karo."
  Bahasa Karo: "Ia cakap Karo."
  Note: Visible example glossed ia berbicara Karo. This is the language name inside that dictionary, not hata Batak.
  Usage: When the message is about the language. Do not expand it into a grammar lesson.
- Indonesian: "Supaya jangan menangis."
  Bahasa Karo: "Ken anakmu e gelah ula ngandung."
  Note: Visible string under the menimang example, glossed timang anakmu itu supaya jangan menangis. The headword spelling is messy, so no extra verb is added in front. `ula` stays in this phrase. Do not replace it with `ulang`.
  Usage: Only when the talk is about a child crying. Not a general prohibition.

The fifth line keeps the dictionary's `ken anakmu`, not a cleaned spelling. If a later print of the kamus shows a different vowel, follow that print.

## Casual Chat

Input:

> Balas sepupu di Kabanjahe. Kamu akan kirim foto rumah nanti malam.

Output:

> Label: mixed. Mejuah-juah. Foto rumahnya kukirim nanti malam. Bujur.

Use:

Greeting and thanks are the dictionary words. The photo plan is Indonesian. No merga, no Horas.

## Public Reminder

Input:

> Ingatkan warga soal kerja bakti Sabtu pagi.

Output:

> Label: mixed. Mejuah-juah kita kerina. Kerja bakti tetap Sabtu pukul 07.00 di balai. Bawa alat sendiri. Bujur.

Use:

The group greeting matches the dictionary example. Time, place, and tools stay Indonesian.

## Professional Or Admin

Input:

> Pesan admin puskesmas untuk pasien yang batal periksa.

Output:

> Label: mixed. Mejuah-juah. Pemeriksaan hari ini dibatalkan. Datang lagi besok pukul 08.00 dengan kartu berobat. Bujur.

Use:

The clinic fact is Indonesian. Karo is only the opening and the thanks.

## Adat Boundary

Input:

> Buat pengenalan merga dan sambutan kalimbubu untuk pesta.

Safe response:

> Pengenalan merga dan sambutan adat tidak disusun dari kamus. Minta teks yang dipakai keluarga. Skill ini hanya memegang `mejuah-juah`, `mejuah-juah kita kerina`, `bujur`, `ia cakap Karo`, dan contoh `ula ngandung`. Horas, mauliate, dan sapaan kekerabatan Toba tidak dipakai.

## Review Mode

Input:

> Cek teks ini: "Horas. Mauliate sudah datang. Mejuah-juah."

Response:

> `Mejuah-juah` ada di Kamus Bahasa Karo-Indonesia sebagai sehat-sehat atau selamat. `Horas` dan `mauliate` tidak dipakai di skill ini. Label yang jujur: campur Toba dan Karo. Untuk chat Karo, tulis `Mejuah-juah`, lalu maksudnya dalam bahasa Indonesia, dan `bujur` kalau memang berterima kasih.
