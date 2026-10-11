# Examples

Lines below are from Kamus Bahasa Simalungun–Indonesia, edisi kedua, Balai Bahasa Provinsi Sumatera Utara: https://repositori.kemendikdasmen.go.id/18777/1/KAMUS-SIMALUNGUN-INDONESIA.pdf

The Indonesian line is that dictionary's gloss. Label: mixed, whenever Indonesian carries the rest of the message.

## Target-Language Examples

- Indonesian: "Selamat. Ucapan selamat saat bertemu."
  Bahasa Simalungun: "Horas."
  Note: Headword `horas`. The kamus says it is the selamat people use when they meet. This entry is in the Simalungun dictionary. Mauliate is not in the file that was read.
  Usage: Opening or closing a meeting. Do not attach Toba kinship after it.
- Indonesian: "Kami semua mengucapkan selamat."
  Bahasa Simalungun: "Haganup hanami makkatahon horas."
  Note: Example under `hanami`, kami. `haganup` is semua in this line.
  Usage: A group. Not a slogan with extra clauses.
- Indonesian: "Jangan kamu marah di situ."
  Bahasa Simalungun: "Ulang ho hanam i jin."
  Note: Example under `hanam`, marah. `ho` is inside this sentence.
  Usage: A short scolding. Not a general "don't".
- Indonesian: "Mau ke mana kau?"
  Bahasa Simalungun: "Laho huja ho?"
  Note: Example under `ho`, kau; anda. A different you-word, `ham`, has its own line `laho hu ja do ham in?` Do not mix the two spellings.
  Usage: One question to one person. The destination in the answer stays Indonesian.
- Indonesian: "Saya membaca buku."
  Bahasa Simalungun: "Ahu mamasa buku."
  Note: Example under `ahu`, aku. The salam example uses `au` instead (`jabat lobei au`). Do not swap `ahu` and `au`.
  Usage: Only for this reading remark. Not a school notice.
- Indonesian: "Semuanya sudah selesai."
  Bahasa Simalungun: "Domma sahei haganupan."
  Note: Example under `sahei`, selesai.
  Usage: Closing a job. The list of what finished stays Indonesian.
- Indonesian: "Rumah itu bagus sekali."
  Bahasa Simalungun: "Rumah ai handalan tumang."
  Note: Example under `handalan`, bagus. Do not replace `rumah` with `jabu`. `jabu` is tagged Tb in this kamus.
  Usage: A house remark.
- Indonesian: "Ia berbicara kepada saya."
  Bahasa Simalungun: "Ia marsahap hubakku."
  Note: Example under `sahap`, kata. `marsahap` is berkata.
  Usage: When the message is about someone speaking. Not a language motto.

## Casual Chat

Input:

> Balas sepupu yang sedang di jalan. Tanyakan mau ke mana, lalu bilang kamu tunggu di rumah.

Output:

> Label: mixed. Horas. Laho huja ho? Aku tunggu di rumah.

Use:

`Horas` and `laho huja ho?` are dictionary lines. The waiting plan is Indonesian. No mauliate, no `ham` spelling mixed into the `ho` question.

## Public Reminder

Input:

> Ingatkan warga bahwa kerja bakti sudah selesai dan besok tidak ada kumpul.

Output:

> Label: mixed. Horas. Domma sahei haganupan. Besok tidak ada kumpul. Kabar lagi menyusul.

Use:

The two Simalungun sentences are printed examples. The schedule stays Indonesian.

## Professional Or Admin

Input:

> Pesan admin sekolah untuk siswa yang belum kembalikan buku.

Output:

> Label: mixed. Horas. Buku paket dikembalikan ke perpustakaan sebelum Jumat pukul 12.00. `Ahu mamasa buku` hanya contoh kamus "saya membaca buku", bukan pengumuman ini.

Use:

The deadline is Indonesian. The dictionary sentence about reading is not forced into the notice.

## Adat Boundary

Input:

> Tulis umpasa pembuka pesta dan alihkan ke aksara Simalungun.

Safe response:

> Umpasa dan aksara tidak disusun dari kamus. Minta teks yang dipakai keluarga. Kamus hanya menyebut surat sapuluh siah sebagai nama huruf. `Amang` di kamus artinya ayah, bukan sapaan untuk semua tamu. `Jabu` berlabel Tb, jangan dipakai sebagai kata rumah Simalungun biasa.

## Review Mode

Input:

> Cek teks ini: "Horas. Mauliate. Jabu ai handalan."

Response:

> `Horas` ada di Kamus Simalungun sebagai selamat. `Mauliate` tidak ditemukan di PDF yang dibaca. `Jabu` berlabel Tb pada lema rumah. Contoh rumah yang tidak berlabel itu adalah `rumah ai handalan tumang`. Label yang jujur: horas-nya Simalungun, sisanya dicampur Toba. Tulis ulang dengan `horas`, lalu maksudnya dalam bahasa Indonesia.
