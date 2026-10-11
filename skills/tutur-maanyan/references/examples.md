# Examples

## Target-Language Examples

- Target: `ulun yiti hengaw anniku`
  Indonesian gloss: Orang ini teman adikku.
  Note: Teaching page, item 1. http://bahasamaanyan.blogspot.com/
  Usage: Introducing someone in chat. Not a Warukin-only or Batapah-only line; the page names no village.

- Target: `aku naan hengaw lawah`
  Indonesian gloss: Saya ada teman lama.
  Note: Same page, item 14.
  Usage: Telling a cousin you ran into an old friend. The plan after that stays Indonesian.

- Target: `amahku tulak bagawi`
  Indonesian gloss: Ayahku pergi bekerja.
  Note: Same page, item 20.
  Usage: A short status. Do not expand it into a work schedule in Maanyan.

- Target: `lewu yeru haut matueh`
  Indonesian gloss: Rumah itu sudah tua.
  Note: Same page, item 37.
  Usage: Pointing at a house. Repairs, costs, and dates stay Indonesian.

- Target: `takam ganyah ngakali ngampi luput urusan yiti`
  Indonesian gloss: Kita sedang berusaha menyelesaikan masalah ini.
  Note: Same page, item 23.
  Usage: Saying the group is still on the problem. Not a promise that it is finished.

- Target: `kami batelu bagawi`
  Indonesian gloss: Kita bertiga bekerja.
  Note: Same page, item 17. The page glosses this `kami` line with kita.
  Usage: Three people are working. Do not change the number.

## Casual Chat

Input:

> Kabari saudara bahwa ayah sudah berangkat kerja dan kita ketemu jam 7 di rumah.

Output (mixed):

> Amahku tulak bagawi. Ketemu jam 7 di rumah.

Why:

Item 20 is the father-left-for-work line. The hour has no attested Maanyan sentence, so it stays Indonesian.

## Public Reminder

Input:

> Umumkan bahwa urusan air kampung masih dibereskan dan kumpul jam 4 di balai.

Output (mixed):

> Takam ganyah ngakali ngampi luput urusan yiti. Kumpul jam 16.00 di balai.

Why:

Item 23 matches "we are still sorting this". The meeting time is Indonesian. `ranu hungey yeru tanang` means the river water is calm, so it does not replace a water-supply notice.

## Professional Or Admin

Input:

> Minta warga mengisi formulir bantuan hari ini sebelum pukul 17.00.

Output (mixed):

> Kami penduduk tumpuk yiti. Formulir bantuan diisi hari ini sebelum pukul 17.00. Kalau sudah, kirim ke admin.

Why:

Item 4 is "we are residents of this village". The form and the deadline stay Indonesian. No attested Maanyan line carries a clock time.

## Adat Boundary

Input:

> Buat taliwakas untuk acara kawin adat di Barito Timur.

Safe response:

> Taliwakas paadu tidak dibuat di sini. Linarto mencatat bahasa itu jauh dari Maanyan sehari-hari dan disampaikan mantir atau pangulu. Contoh jaraknya: pintu sehari-hari `wanawang`, sedangkan pangunraunnya `tukat amai wanawang suluk talaga rampan`. Kalimat itu tidak dilanjutkan.

## Review Mode

Input:

> Cek: "Ulun yiti jaga basa Ngaju hang lewu yeru."

Response:

1. `ulun yiti` and `lewu yeru` match the teaching page (orang ini; rumah itu). The rest is not a glossed line.
2. Ngaju is a different language on Peta Bahasa (perbedaan 95,75%). Do not put Ngaju inside a Maanyan sentence.
3. Safer reply: `Lewu yeru haut matueh. Soal bahasa Ngaju, itu bahasa lain, jangan dicampur ke kalimat Maanyan.`
