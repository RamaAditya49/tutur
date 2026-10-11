# Examples

## Target-Language Examples

- Indonesian: sapaan saat berjumpa, dibalas dengan kata yang sama.
  Bahasa Nias: "Ya'ahowu"
  Meaning/note: Bacaan Kemendikbud Ya'ahowu. The chapter sets it beside salam sejahtera and similar greetings. It does not print a word-by-word morpheme gloss.
  Usage: Open and answer an ordinary meeting. Source: https://rumahpusbin.kemendikdasmen.go.id/sastrawan3t/427_Ya_Ahowu.pdf
- Indonesian: "Orang Nias."
  Bahasa Nias: "Ono Niha"
  Meaning/note: Same reader. Used for the people, not as a summons invented for one person.
  Usage: Name the group. Same PDF.
- Indonesian: "Tanah Nias."
  Bahasa Nias: "Tano Niha"
  Meaning/note: Same reader, in the greeting chapter.
  Usage: Place name. Same PDF.
- Indonesian: "Bahasa Nias."
  Bahasa Nias: "Li Niha"
  Meaning/note: Peta Bahasa and the same reader. Speakers' name for the language.
  Usage: Name the language. Peta Bahasa: https://petabahasa.kemdikbud.go.id/infobahasa.php?idb=12
- Indonesian: "Terima kasih Pak. Terima kasih kami ucapkan kepada Bapak semuanya."
  Bahasa Nias: "Saohagolo Ama…saohagolo ma andro khomi fefu"
  Meaning/note: News note from Pengadilan Tinggi Agama Medan, quoting speech after a hearing at PA Gunungsitoli, with that office gloss. Spelling follows the news note.
  Usage: Quote the whole sentence only. Do not slice it into a new thanks line. Source: https://www.pta-medan.go.id/index.php/2016-12-22-04-37-57/arsip-berita/arsip-berita-pa-se-sumut?start=16730

## Casual Chat

Input:

> Balas saudara di Gunungsitoli yang menanya sudah sampai atau belum.

Output (mixed):

> Ya'ahowu. Sudah sampai di terminal. Jemput jam 4 kalau sempat.

Note:

Ya'ahowu is the attested greeting. The arrival and the time are Indonesian. Mixed. Dialect is not pinned to Teluk Dalam or Lahewa. This is not a Batak horas opening.

## Public Reminder

Input:

> Ingatkan warga kerja bakti besok pagi.

Output (mixed):

> Ya'ahowu. Kerja bakti lingkungan besok pagi jam 07.00 di halaman balai desa. Bawa alat sendiri. Kabar lagi kalau tidak bisa datang.

Note:

Only Ya'ahowu is Li Niha. The schedule stays in Indonesian. Mixed. For a loudspeaker or a printed notice, ask a speaker from that village. Do not recast this as pesta adat.

## Professional Or Admin

Input:

> Pesan admin puskesmas: kartu belum dibawa.

Output (mixed):

> Ya'ahowu. Kartu berobat belum kami terima. Mohon bawa hari ini sebelum pukul 14.00. Nama pasien tetap di halaman pertama.

Note:

The clinical detail stays in Indonesian. Mixed. Do not attach the court thanks sentence. That sentence addresses Bapak and a group after a hearing. It does not fit this desk note.

## Adat Boundary

Input:

> Tulis rumus hoho untuk nikahan dan doa sembuh.

Safe response:

> Hoho, rumus nikahan, dan rumus penyembuhan tidak disusun di skill ini. Buku Ya'ahowu menyebut salam dan afo. Itu bukan naskah upacara. Minta teks yang sudah dipakai keluarga di kampung yang dimaksud.

## Review Mode

Input:

> Cek teks ini: "Horas. Ya'ahowu, saohagolo, omasido khömö."

Response shape:

1. Flag the Batak greeting and the unsourced affection line.
2. Keep Ya'ahowu.
3. Refuse to expand saohagolo beyond the quoted court sentence.

Example review:

> Ya'ahowu aman sebagai salam, dari bacaan Kemendikbud, dan dibalas Ya'ahowu. Horas bukan Li Niha. "Omasido khömö" tidak ada di sumber skill ini, jadi tidak dipakai. Kalimat saohagolo yang tercatat utuh berbunyi "Saohagolo Ama…saohagolo ma andro khomi fefu", dengan glos pengadilan untuk terima kasih kepada Bapak semuanya. Jangan dipotong. Untuk chat biasa: Ya'ahowu, lalu bahasa Indonesia. Hasilnya mixed.
