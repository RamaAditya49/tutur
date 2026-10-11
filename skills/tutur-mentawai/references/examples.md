# Examples

## Target-Language Examples

- Indonesian: "Bagaimana? Apa kabar?"
  Bahasa Mentawai: "abekia"
  Meaning/note: Kamus Mentawai–Indonesia–Inggris, Panulis Saguntung. Gloss printed as bagaimana, apa kabar, how, how are you.
  Usage: Short kabar question. Do not extend it. Source: https://id.scribd.com/document/789584828/kamus-bahasa-mentawai
- Indonesian: "Terima kasih."
  Bahasa Mentawai: "surak" or "sura'"
  Meaning/note: Same dictionary preface. sura(k) and sura' are the two spellings it discusses for terima kasih. The final sound is k in some sources and a hamzah in others.
  Usage: Use one spelling and say which. Do not invent a longer thanks sentence. Same URL.
- Indonesian: "Ucapan selamat."
  Bahasa Mentawai: "anai leuk ita"
  Meaning/note: Same dictionary. Gloss is ucapan selamat, also congratulation language in the English column. It is not glossed there as "apa kabar".
  Usage: Quote the phrase for a short selamat. Do not retarget it as a kabar question. Same URL.
- Indonesian: sapaan "hai" sesama laki-laki.
  Bahasa Mentawai: "ale"
  Meaning/note: Same dictionary, second sense of ale. The first sense is sembuh, pulih. Keep the senses apart.
  Usage: Men addressing men, as a short hail. Not a healing line. Same URL.
- Indonesian: sapaan di kantor layanan, glos tidak dicetak.
  Bahasa Mentawai: "Anaileuita" or "Maronsita"
  Meaning/note: Dinas Kominfo Mentawai, laporan peluncuran kamus 17 November 2025. Staff Ahli Brandus Donatus Simanjuntak names both as sapaan for a public office wall. No gloss is printed.
  Usage: Name the greeting. Do not translate it beyond "sapaan". Source: https://diskominfo.mentawaikab.go.id/2025/11/pemkab-mentawai-luncurkan-kamus-bahasa.html

## Casual Chat

Input:

> Balas teman di Tuapejat yang menanya kabar.

Output (mixed):

> Abekia. Aku baik. Besok aku ke kantor camat, jam 9 kalau mau ikut.

Note:

Abekia is the dictionary kabar word. The plan is Indonesian. Mixed. Island is not pinned beyond the user's Tuapejat, which is on Sipora. Do not add a healing or uma line.

## Public Reminder

Input:

> Ingatkan warga kerja bakti besok pagi.

Output (mixed):

> Maronsita. Kerja bakti lingkungan besok pagi jam 07.00 di halaman balai desa. Bawa alat sendiri. Kabar lagi kalau tidak bisa datang.

Note:

Maronsita is the office greeting named by the district news note, without a tighter gloss. The schedule stays in Indonesian. Mixed. For a loudspeaker, ask a speaker from that island. Do not recast this as upacara uma.

## Professional Or Admin

Input:

> Pesan loket: berkas KTP belum lengkap.

Output (mixed):

> Anaileuita. Berkas KTP belum lengkap. Mohon kirim ulang hari ini sebelum pukul 15.00. Nama tetap di halaman pertama. Surak.

Note:

Anaileuita is the other office greeting from the same news note. Surak is the dictionary thanks word, k-spelling. The deadline stays in Indonesian. Mixed. Sipora office context only if the user said Tuapejat. Otherwise say the island is unspecified.

## Adat Boundary

Input:

> Tulis rumus sikerei untuk nikahan dan obat.

Safe response:

> Rumus sikerei, nikahan, dan penyembuhan tidak disusun di skill ini. Kamus menggloss ale sebagai sembuh pada satu arti, dan sebagai hai pada arti lain. Itu bukan naskah upacara. Minta teks yang sudah dipakai keluarga di pulau yang dimaksud.

## Review Mode

Input:

> Cek teks ini: "Tabeq. Anaileuita berarti apa kabar. Abekia, masura bagata, punen."

Response shape:

1. Flag Minangkabau or unsourced pieces.
2. Keep the Mentawai items that match a gloss.
3. Leave ritual words unexpanded.

Example review:

> Abekia memang glos kamusnya bagaimana / apa kabar. Anaileuita di berita pemda adalah nama sapaan kantor, tanpa glos, jadi jangan disamakan paksa dengan abekia. Anai leuk ita di kamus Saguntung adalah ucapan selamat, ejaannya juga tidak sama dengan tulisan pemda. Tabeq bukan dari sumber Mentawai skill ini. "Masura bagata" dan punen tidak dipakai untuk menyusun kalimat baru. Untuk chat: Abekia, lalu bahasa Indonesia. Hasilnya mixed.
