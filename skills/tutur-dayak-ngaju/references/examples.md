# Examples

## Target-Language Examples

- Indonesian: "Bantu kami."
  Bahasa Ngaju: "dohop ikei"
  Meaning/note: Kamus Dwibahasa Dayak Ngaju–Indonesia, Balai Bahasa Kalimantan Tengah, 2013. Lemma dohop, v bantu.
  Usage: Short help request. Source: https://commons.wikimedia.org/wiki/File:Kamus_Dwibahasa_Dayak_Ngaju-Indonesia.pdf
- Indonesian: "Terima kasih atas pertolongan kalian kepada kami."
  Bahasa Ngaju: "tarima kasih tagal ketun handiai"
  Meaning/note: Same dictionary, lemma pandohop, n pertolongan, bantuan. The example prints tarima kasih inside the Ngaju line. Quote the line as printed.
  Usage: Quote when the thanks is really for help. Same PDF.
- Indonesian: "Apa pertanyaannya padamu?"
  Bahasa Ngaju: "narai paiseke dengam?"
  Meaning/note: Same dictionary, lemma paisek, n pertanyaan. Headword restored from the dash.
  Usage: Quote this question. Do not change who is asked. Same PDF.
- Indonesian: "Kami lima bersaudara."
  Bahasa Ngaju: "ikei lime hapahari"
  Meaning/note: Same dictionary, lemma lime, angka lima. The ha- prefix list also glosses hapahari as bersaudara. Headword lime restored from the dash.
  Usage: Quote for that family count. Do not change the number. Same PDF.
- Indonesian: "Di bagian agak ke hulu (tentang sungai)."
  Bahasa Ngaju: "ngaju"
  Meaning/note: Same dictionary. Separate from the ethnic-name entry Ngaju. A related line glosses a search "ngaju ngawa" as hilir mudik, under a different verb. Do not build a new direction sentence from that fragment.
  Usage: Use the word for upstream. Same PDF.

## Casual Chat

Input:

> Balas saudara di Palangka Raya yang menawar bantuan angkut beras.

Output (mixed):

> Dohop ikei. Berasnya dua karung, dijemput jam 4 di rumah. Tarima kasih tagal ketun handiai.

Note:

Both Ngaju sentences are dictionary examples: help, then thanks for that help. The rice, the time, and the place are Indonesian. Mixed. Dialect village is unspecified. This is Ngaju, not a generic Dayak note.

## Public Reminder

Input:

> Ingatkan warga kerja bakti besok pagi.

Output (mixed):

> Dohop ikei. Kerja bakti lingkungan besok pagi jam 07.00 di halaman balai kelurahan. Bawa alat sendiri. Kabar lagi kalau tidak bisa datang.

Note:

Dohop ikei matches a request for help. The schedule stays in Indonesian. Mixed. For a loudspeaker, ask an Ngaju speaker from that village.

## Professional Or Admin

Input:

> Pesan admin sekolah: berkas bantuan belum lengkap.

Output (mixed):

> Berkas bantuan belum lengkap. Mohon kirim ulang hari ini sebelum pukul 15.00. Nama siswa tetap di halaman pertama.

Note:

No Ngaju sentence in the mirror is about a file deadline. The message stays in Indonesian. Do not decorate it with ngaju. If a one-word opening is required, say so and mark the result mixed only after an attested line is actually added.

## Adat Boundary

Input:

> Tulis doa adat dan rumus penyembuhan.

Safe response:

> Doa adat dan rumus penyembuhan tidak disusun dari kamus. Contoh mandoa yang tercetak hanya "aku mandoa ketun salamat sampai lewu", artinya saya mendoakan kalian selamat sampai kampung. Itu ucapan perjalanan, bukan naskah upacara. Minta teks yang sudah dipakai keluarga.

## Review Mode

Input:

> Cek teks ini: "Tabe, ulun. Narai kabar, bahasa Dayak kita sama."

Response shape:

1. Flag the pan-Dayak claim.
2. Keep only Ngaju pieces that match a printed example.
3. Leave unsourced greetings unused.

Example review:

> Kamus Balai Bahasa menggloss narai di dalam "narai paiseke dengam?", apa pertanyaannya padamu, bukan sebagai sapaan "apa kabar" yang berdiri sendiri. Tabe dan ulun tidak ada di contoh yang disimpan skill ini. "Bahasa Dayak" terlalu luas. Folder ini hanya Ngaju, ISO nij. Untuk minta bantuan: Dohop ikei, lalu bahasa Indonesia. Hasilnya mixed.
