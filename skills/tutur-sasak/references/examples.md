# Examples

## Target-Language Examples

- Indonesian: "Apa kabar?"
  Bahasa Sasak: "Berembe kabar?"
  Meaning/note: Common everyday greeting; verify local dialect before formal publication.
  Usage: Use for casual greeting examples only.
- Indonesian: "Terima kasih."
  Bahasa Sasak: "Matur tampiasih."
  Meaning/note: Common polite thanks phrase in Sasak support sources.
  Usage: Safe as a short phrase; verify spelling for formal print.
- Indonesian: "Permisi."
  Bahasa Sasak: "Tabeq."
  Meaning/note: Polite permission/excuse phrase associated with Sasak etiquette.
  Usage: Use as a short etiquette example, not as full ceremonial language.

## Source-Aware Generation

Input:

> Buat teks pendek untuk mengajak anak muda menjaga Bahasa Sasak.

Safer output:

> Tabeq, semeton muda Lombok. Yuk jaga Bahasa Sasak mulai dari hal kecil: pakai sapaan sehari-hari, tanya ke orang tua kalau ada kata yang belum yakin, dan jangan malu belajar lagi.

Note:

This keeps the main message in Indonesian with a short Sasak etiquette cue. For a full Sasak version, ask for target dialect and speaker review.

## Casual Chat

Input:

> Balas teman yang tanya kabar.

Output:

> Berembe kabar? Aku baik, matur tampiasih. Kamu gimana?

Use:

For informal chat only. Do not reuse as formal event wording.

## Tourism Greeting

Input:

> Buat sambutan pendek untuk tamu homestay di Lombok.

Output:

> Tabeq. Selamat datang di Lombok. Matur tampiasih sudah menginap di tempat kami. Kalau butuh bantuan soal kamar, sarapan, atau arah wisata, silakan hubungi admin.

Why:

The greeting uses short Sasak phrases while operational details remain clear in Indonesian.

## Community Reminder

Input:

> Ingatkan warga untuk hadir kerja bakti besok.

Output:

> Tabeq, Bapak/Ibu. Besok pagi ada kerja bakti lingkungan pukul 07.00. Mohon hadir tepat waktu dan membawa alat kebersihan masing-masing. Matur tampiasih.

Review note:

This is Sasak-aware Indonesian, not a full Sasak translation. For village-level public print, ask a local speaker to adjust dialect and politeness.

## Professional/Admin

Input:

> Buat pesan admin untuk tamu yang belum mengirim KTP.

Output:

> Tabeq, Kak. Untuk proses check-in, mohon kirim foto KTP sebelum pukul 18.00 hari ini. Data hanya digunakan untuk administrasi penginapan. Matur tampiasih.

Why:

Identity, deadline, and privacy details stay in standard Indonesian to avoid ambiguity.

## Review Mode

Input:

> Cek apakah teks ini terdengar seperti Bahasa Sasak asli.

Response shape:

1. Flag Indonesian grammar with local-word decoration.
2. Flag unsupported vocabulary.
3. Recommend native-speaker review for public use.

Example review:

> Bagian `Tabeq` dan `matur tampiasih` aman sebagai frasa pendek. Namun kalimat panjang setelahnya masih struktur Indonesia penuh. Jika ingin versi Sasak yang lebih utuh, tentukan dialek/daerah target dan minta contoh dari penutur lokal.
