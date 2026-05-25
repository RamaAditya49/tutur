# Examples

## Target-Language Examples

- Indonesian: "Salam hormat."
  Bahasa Lampung: "Tabik pun."
  Meaning/note: Common Lampung greeting/respect cue in Lampung cultural usage.
  Usage: Use as short greeting; formal/adat text needs review.
- Indonesian: "Kabar baik."
  Bahasa Lampung: "Kabar wawai."
  Meaning/note: Common answer pattern in Lampung support sources.
  Usage: Use only as short phrase; dialect matters.
- Indonesian: "Apa kabar?"
  Bahasa Lampung: "Api kabar?"
  Meaning/note: Lampung Api/A-oriented support phrase; verify dialect before use.
  Usage: Use for casual dialect-aware examples.
- Indonesian: "Apa kabar?"
  Bahasa Lampung: "Nyow kabar?"
  Meaning/note: Lampung Nyo/O-oriented support phrase; verify dialect before use.
  Usage: Use for casual dialect-aware examples.

## Source-Aware Generation

Input:

> Buat teks pendek untuk mengajak anak muda menjaga Bahasa Lampung.

Safer output:

> Tabik pun. Mari belajar Bahasa Lampung mulai dari sapaan harian. Kalau memakai dialek Api/A atau Nyo/O, tulis variannya dengan jelas dan cek lagi ke kamus resmi.

Why:

The output uses a short Lampung greeting and marks dialect choice as important.

## Dialect Variants

Input:

> Buat dua versi "apa kabar?".

Output:

> Api/A: Api kabar?
> Nyo/O: Nyow kabar?
> Jawaban pendek: Kabar wawai.

Review note:

Use these as short phrase examples only. Do not mix dialects in one public text.

## Tourism/Admin

Input:

> Buat sambutan singkat untuk tamu acara Lampung.

Output:

> Tabik pun. Selamat datang di acara komunitas Lampung. Informasi jadwal, lokasi, dan kontak panitia ada di bawah ini.

Why:

The greeting gives local warmth while operational details stay clear in Indonesian.

## Professional

Input:

> Buat pesan admin untuk peserta yang belum mengirim formulir.

Output:

> Tabik pun, Kak. Formulir peserta belum kami terima. Mohon kirim hari ini sebelum pukul 17.00 agar data bisa diproses.

Review note:

Good for WhatsApp admin. For official letters, use Indonesian or ask a Lampung speaker to review the dialect.

## Aksara/Adat Boundary

Input:

> Ubah teks ini ke aksara Lampung dan buat pembuka adat.

Safe response:

> Untuk aksara Lampung atau pembuka adat, gunakan sumber dari penutur/panitia setempat. Skill ini tidak boleh menebak transliterasi atau formula adat untuk publikasi resmi.

## Review Mode

Input:

> Cek apakah teks ini terdengar seperti Bahasa Lampung asli.

Response shape:

1. Flag Indonesian grammar with local-word decoration.
2. Flag unsupported vocabulary.
3. Recommend native-speaker review for public use.

Example review:

> `Tabik pun` aman sebagai pembuka pendek. Namun teks ini mencampur bentuk Api/A dan Nyo/O tanpa label, jadi perlu dipilih satu dialek atau dibuat dua varian terpisah.
