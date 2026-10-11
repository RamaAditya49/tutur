# Examples

## Target-Language Examples

- Indonesian: "Salam hormat untuk kalian semua."
  Bahasa Mandailing: "santabi di hamu sude"
  Meaning/note: Kamus Angkola Mandailing–Indonesia, Balai Bahasa Sumatera Utara, 2021. Lemma santabi is tabik; salam (hormat). The line is not marked Akl.
  Usage: Group greeting. Quote it, then continue in Indonesian. Source: https://repositori.kemendikdasmen.go.id/34696/1/KAMUS%20ANGKOLA%20MANDAILING-FINAL.pdf
- Indonesian: "Terima kasih."
  Bahasa Mandailing: "mauliate"
  Meaning/note: Same dictionary. Noun, pronunciation note [mawliyate]. No full thanks sentence is copied from that entry.
  Usage: Use the word. Do not build a new sentence around it. Same PDF.
- Indonesian: "Ayo, kita pergi."
  Bahasa Mandailing: "ale, eta kehe"
  Meaning/note: Same dictionary, lemma ale, pronoun ayo. Shared entry, not an Akl label.
  Usage: Quote when the meaning is really "ayo, kita pergi". Do not swap the destination and keep the frame. Same PDF.
- Indonesian: "Adik menyapu halaman."
  Bahasa Mandailing: "anggi manyapu alaman"
  Meaning/note: Same dictionary, unlabeled example under alaman. anggi here is adik.
  Usage: Quote as a sample of anggi. Do not retarget it to a named person who is not the younger sibling. Same PDF.
- Indonesian: "Setelah makan, kita berangkat ke sawah."
  Bahasa Mandailing: "abis mangan, hita marangkat tu saba"
  Meaning/note: Same dictionary. abis is marked Mdl for this sense, sesudah.
  Usage: Quote the whole line. It is a Mandailing-marked example, still not a license to invent the next sentence. Same PDF.

## Casual Chat

Input:

> Balas adik di Panyabungan yang menanya kapan dijemput.

Output (mixed):

> Santabi. Anggi, aku sudah di terminal. Jemput jam 4 kalau sempat.

Note:

Santabi is the dictionary greeting word. Anggi is the adik address from "anggi manyapu alaman", used here because the listener is the younger sibling. The pickup sentence is Indonesian. Mixed. This is not a Toba horas opening.

## Public Reminder

Input:

> Ingatkan warga kerja bakti besok pagi.

Output (mixed):

> Santabi di hamu sude. Kerja bakti lingkungan besok pagi jam 07.00 di halaman balai desa. Bawa alat sendiri. Kabar lagi kalau tidak bisa datang.

Note:

The first sentence is the attested group line. The schedule stays in Indonesian. Mixed. For a loudspeaker or a printed notice, ask a Mandailing speaker. Do not recast this as horja.

## Professional Or Admin

Input:

> Pesan admin sekolah: berkas bantuan belum lengkap.

Output (mixed):

> Santabi di hamu sude. Berkas bantuan belum lengkap. Mohon kirim ulang hari ini sebelum pukul 15.00. Nama siswa tetap di halaman pertama. Mauliate.

Note:

Mauliate is only the glossed thanks noun. The deadline stays in Indonesian. Mixed. Shared dictionary greeting, not Toba.

## Adat Boundary

Input:

> Tulis markobar untuk horja keluarga.

Safe response:

> Markobar dan horja tidak disusun dari kamus. Kamus Balai Bahasa menggloss santabi dan adat sebagai kata, bukan sebagai naskah pesta. Minta teks yang sudah dipakai keluarga di Mandailing Natal. Jangan diganti dengan sambutan Batak Toba.

## Review Mode

Input:

> Cek teks ini: "Horas ma di hita. Santabi, mauliate godang."

Response shape:

1. Flag the Toba-style horas hello.
2. Keep the Mandailing piece that is actually attested.
3. Ask for a speaker if the text will be printed.

Example review:

> Santabi dan mauliate ada di kamus Angkola-Mandailing. "Santabi di hamu sude" adalah kalimat grup yang tercetak. Horas di kamus yang sama artinya selamat, contohnya "sai horas hita ibaen Tuhan", bukan sapaan pembuka. "Mauliate godang" tidak ada di cuplikan entri yang dipakai skill ini. Untuk chat keluarga, pakai santabi lalu lanjut bahasa Indonesia. Hasilnya mixed.
