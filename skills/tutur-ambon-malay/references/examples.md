# Examples

## Target-Language Examples

- Target: `Ale mo pi mana`
  Indonesian gloss: Kamu mau pergi ke mana?
  Note: Kamus Dwibahasa Melayu Ambon-Indonesia, lema `ale`. https://balaibahasaprovinsimaluku.kemendikdasmen.go.id/wp-content/uploads/2025/08/Kamus-Melayu-Ambon-Indonesia.pdf
  Usage: Opening question to one person. `ale` is the you-word in this line.

- Target: `Jang buang sampa di got`
  Indonesian gloss: Jangan membuang sampah di selokan.
  Note: Same dictionary, lema `jang`.
  Usage: Spoken warning to neighbours. Do not extend it with unattested Malay.

- Target: `Mari katong pigi cari bulu di utang`
  Indonesian gloss: Ayo kita pergi mencari bambu di hutan.
  Note: Same dictionary, lema `bulu` (bambu).
  Usage: Inviting people to fetch bamboo. `katong` is the we-word here. Not a general slogan.

- Target: `Dangke lae su tolong beta tola oto ni`
  Indonesian gloss: Terima kasih sudah menolong saya mendorong mobil ini.
  Note: Same dictionary, lema `dangke`.
  Usage: Thanks after someone helps push a car. `beta` is I, `su` is already.

- Target: `Da Rudi, sampe baku dapa lai`
  Indonesian gloss: Selamat jalan Rudi, sampai bertemu lagi.
  Note: Same dictionary, lema `da`.
  Usage: Seeing someone off. Keep `baku dapa` as in the example. The name can stay Rudi when quoting, or the user may be told the frame is this line.

- Target: `Ingatang, baso tangang tu ee, supaya jang korona loko ose`
  Indonesian gloss: Ingat cuci tangan supaya kamu tidak terjangkit virus korona.
  Note: Same dictionary, lema `ose`.
  Usage: Handwashing reminder. `ose` is you in this sentence.

## Casual Chat

Input:

> Tanya saudara mau ke mana, dan bilang saya masih di rumah sampai jam lima.

Output (mixed):

> Ale mo pi mana? Saya masih di rumah sampai jam lima.

Why:

The question is the dictionary line. The whereabouts and the hour are Indonesian because the dictionary does not give that second sentence.

## Public Reminder

Input:

> Ingatkan warga jangan buang sampah di selokan. Tong sampah ada di ujung gang.

Output (mixed):

> Jang buang sampa di got. Tong sampah ada di ujung gang.

Why:

The warning is attested. The bin location is a new fact, so it stays Indonesian.

## Professional Or Admin

Input:

> Ingatkan penumpang mobil dinas supaya tetap pakai masker. Berangkat pukul 07.30 dari kantor.

Output (mixed):

> Basudara samua, mar biar kata dalam oto lai musti pasang masker e! Berangkat pukul 07.30 dari kantor.

Why:

The mask sentence is the dictionary example under `oto`. The departure time is Indonesian.

## Adat Boundary

Input:

> Buat doa atau urutan acara di baileo.

Safe response:

> Urutan acara baileo tidak disusun di sini. Kamus Balai Bahasa memakai kalimat `dong pake berang, barang ada biking adat di baileo` hanya untuk menjelaskan kain merah dan rumah adat. Minta teks dari negeri atau orang yang memimpin acara.

## Review Mode

Input:

> Cek: "Beta dan dong mari kita bersama menjaga got."

Response:

1. `Beta` and `dong` are real pronouns, but this sentence is Indonesian with two pronouns swapped in. The dictionary warning is `Jang buang sampa di got`.
2. `Mari katong pigi cari bulu di utang` is a different errand, fetching bamboo, so it cannot replace a drain notice.
3. Safer mixed line: `Jang buang sampa di got. Sampahnya dibuang di tong.`
