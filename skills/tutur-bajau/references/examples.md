# Examples

## Target-Language Examples

- Target: `ma'i`
  Indonesian gloss: Mari. Come here.
  Note: Nuraini 2010, Flores Sea Indonesian Bajo. She links it to Malay mari. https://scholarhub.ui.ac.id/wacana/vol12/iss2/5/
  Usage: Calling someone over. Not a Sabah sentence, and not Bajau Pondong.

- Target: `nggai`
  Indonesian gloss: Tidak.
  Note: Same article. The negator. Slower speech may be two syllables.
  Usage: A bare no. The reason stays Indonesian. Do not attach it to a new Bajo verb.

- Target: `malasso`
  Indonesian gloss: Baik.
  Note: Same article, "good, well".
  Usage: A short approval. Do not expand it into "semoga malasso" or any blessing.

- Target: `kampoh`
  Indonesian gloss: Kampung.
  Note: Same article, "village, hamlet". JIPA East Lombok also glosses kampoh as village, in q-spelling surroundings that this line does not use.
  Usage: Naming a village. The village name itself stays as given.

- Target: `nginta`
  Indonesian gloss: Makan.
  Note: Same article, "to eat". Actor-voice shape she lists from the root inta.
  Usage: The word for eat. "Makan dulu jam 6" stays Indonesian rather than a new Bajo clause.

- Target: `ba'u`
  Indonesian gloss: Baru.
  Note: Same article. Apostrophe is her glottal stop, not the East Lombok q.
  Usage: Marking that something is new. The new schedule is Indonesian.

## Casual Chat

Input:

> Panggil saudara supaya ke dermaga, ketemuan jam 5.

Output (mixed):

> Ma'i. Ketemu di dermaga jam 5.

Why:

`ma'i` is the attested "come here". The pier and the hour have no Bajo sentence in this skill, so they stay Indonesian. Spelling is Flores Sea / Sapeken, inside Peta Bahasa's Bahasa Bajo, not one village dialect.

## Public Reminder

Input:

> Umumkan bahwa kumpul besok dibatalkan dan diganti lusa jam 7 di balai.

Output (mixed):

> Nggai. Kumpul besok batal. Diganti lusa jam 7 di balai.

Why:

`nggai` is "no". The new time and the hall are Indonesian. `ellau` means "day" and is not a full date.

## Professional Or Admin

Input:

> Beritahu peserta bahwa jadwal loket yang baru mulai pukul 08.00.

Output (mixed):

> Ba'u. Jadwal loket mulai pukul 08.00.

Why:

`ba'u` is "new". The clock stays Indonesian. There is no Bajo form-letter line here.

## Adat Boundary

Input:

> Buat doa pelepasan perahu yang berlaku untuk semua Bajau.

Safe response:

> Doa pelepasan perahu tidak dibuat di sini. Sumber yang dipegang hanya kata lepas seperti `ma'i`, `nggai`, `kampoh`, dan `nganjame` untuk ragam Laut Flores. Peta Bahasa memisahkan Bahasa Bajo dari Bajau Pondong, Bajau Semayap, Bajau Tungkal Satu, dan Bajo Delang. Satu rumus untuk semuanya tidak ada di sumber itu.

## Review Mode

Input:

> Cek: "Muan kuih yo tak jomo, ma'i ke kampoh pasaq."

Response:

1. `ma'i` and `kampoh` are Flores Sea glosses (mari; kampung).
2. `Muan kuih yo tak jomo` is a Sabah Bajau sentence in a Sabah thesis, not Indonesian Bajo. West Coast Bajau is ISO `bdr`, not `bdl`.
3. `pasaq` is the East Lombok JIPA gloss "come, enter", another orthography. Do not weld it to `ma'i`.
4. Safer reply: `Ma'i. Soal kue untuk tetangga, tulis bahasa Indonesia. Jangan campur kalimat Sabah ke Bahasa Bajo.`
