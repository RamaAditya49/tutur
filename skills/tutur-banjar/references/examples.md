# Examples

## Target-Language Examples

- Indonesian: "Saya."
  Bahasa Banjar: "Ulun."
  Meaning/note: Common first-person form in Banjar support sources.
  Usage: Use for polite/self-reference examples; verify context.
- Indonesian: "Kamu."
  Bahasa Banjar: "Pian."
  Meaning/note: Common second-person form in Banjar support sources.
  Usage: Use carefully; relationship and politeness matter.
- Indonesian: "Apa kabar?"
  Bahasa Banjar: "Apa habar?"
  Meaning/note: Common everyday greeting pattern.
  Usage: Use for casual greeting examples only.
- Indonesian: "Benar."
  Bahasa Banjar: "Bujur."
  Meaning/note: Common Banjar word meaning true/right.
  Usage: Use in short everyday examples.

## Source-Aware Generation

Input:

> Buat teks pendek untuk mengajak anak muda menjaga Bahasa Banjar.

Safer output:

> Apa habar, kawan-kawan. Ayo rawat Bahasa Banjar mulai dari obrolan harian. Kalau ada kata yang belum yakin, cek kamus atau tanya urang Banjar yang paham dialeknya.

Why:

The output uses a short Banjar greeting and keeps the rest understandable without pretending to be a certified full translation.

## Casual Chat

Input:

> Balas teman yang tanya kabar.

Output:

> Apa habar? Ulun baik haja. Pian kayapa?

Use:

For familiar/casual chat. Verify dialect and relationship before using in formal or elder-facing contexts.

## Community Reminder

Input:

> Ingatkan warga untuk datang kerja bakti besok.

Output:

> Apa habar, Bapak/Ibu. Ulun ingatkan besok ada kerja bakti pukul 07.00. Mohon hadir tepat waktu dan membawa alat kebersihan masing-masing.

Why:

The message uses Banjar flavor through greeting/self-reference while operational details stay clear in Indonesian.

## Professional/Admin

Input:

> Buat pesan admin untuk peserta yang belum mengirim bukti pembayaran.

Output:

> Apa habar, Kak. Ulun bantu ingatkan, bukti pembayaran belum kami terima. Mohon kirim bukti transfer hari ini sebelum pukul 17.00 agar pendaftaran bisa diproses.

Review note:

Good for WhatsApp admin. For official billing, use standard Indonesian or confirm Banjar wording with local staff.

## Polite Public Variant

Input:

> Buat undangan pendek untuk acara komunitas Banjar.

Output:

> Bapak/Ibu, kami mengundang pian hadir pada acara komunitas Banjar hari Sabtu pukul 19.30. Informasi lokasi dan susunan acara ada di lampiran.

Why:

`Pian` gives Banjar-facing tone, while public details remain unambiguous.

## Adat/Religious Boundary

Input:

> Buat pembukaan acara adat Banjar.

Safe response:

> Untuk acara adat atau keagamaan Banjar, jangan buat formula dari nol. Kirim contoh dari panitia atau penutur Banjar setempat, lalu skill ini bisa membantu merapikan dan menandai bagian yang perlu dicek.

## Review Mode

Input:

> Cek apakah teks ini terdengar seperti Bahasa Banjar asli.

Response shape:

1. Flag Indonesian grammar with local-word decoration.
2. Flag unsupported vocabulary.
3. Recommend native-speaker review for public use.

Example review:

> `Ulun`, `pian`, dan `apa habar` bisa dipakai sebagai sinyal Banjar pendek. Namun kalimat panjang setelahnya masih struktur Indonesia penuh. Kalau targetnya publik, tentukan Banjar Kuala atau Banjar Hulu dan minta penutur lokal mengecek pilihan katanya.
