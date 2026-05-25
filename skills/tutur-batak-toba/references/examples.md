# Examples

## Target-Language Examples

- Indonesian: "Salam."
  Bahasa Batak Toba: "Horas."
  Meaning/note: Common Batak Toba greeting/well-wishing expression.
  Usage: Use as short greeting only; adat context needs review.
- Indonesian: "Terima kasih."
  Bahasa Batak Toba: "Mauliate."
  Meaning/note: Common thanks phrase in Batak Toba support sources.
  Usage: Use as short phrase; verify relationship/address term.
- Indonesian: "Bahasa Batak Toba."
  Bahasa Batak Toba: "Hata Batak Toba."
  Meaning/note: Common identity phrase for the language.
  Usage: Use for language identity, not full grammar modeling.
- Indonesian: "Bapak/Ibu."
  Bahasa Batak Toba: "Amang/Inang."
  Meaning/note: Kinship/respect address terms.
  Usage: Use only when relationship and cultural context fit.

## Source-Aware Generation

Input:

> Buat teks pendek untuk mengajak anak muda menjaga Bahasa Batak Toba.

Safer output:

> Horas. Mari belajar Hata Batak Toba mulai dari sapaan, ucapan terima kasih, dan cerita keluarga. Kalau ada kata yang belum yakin, cek kamus atau tanya penutur Batak Toba di keluarga/komunitas.

Why:

The output uses short source-supported cues and keeps the broader message in Indonesian.

## Casual Greeting

Input:

> Sapa teman di grup komunitas.

Output:

> Horas, kawan-kawan. Mauliate sudah aktif di grup. Kalau ada info kegiatan, silakan tulis di sini.

Use:

Good for simple community greeting. Do not treat it as adat language.

## Community Invitation

Input:

> Buat undangan pendek untuk kegiatan komunitas Batak Toba.

Output:

> Horas, Bapak/Ibu. Kami mengundang hadir pada kegiatan komunitas Batak Toba hari Sabtu pukul 19.30. Lokasi dan susunan acara ada di lampiran. Mauliate.

Why:

The greeting and thanks create Batak Toba warmth while operational details remain clear in Indonesian.

## Professional/Admin

Input:

> Buat pesan admin untuk peserta yang belum mengirim data.

Output:

> Horas, Kak. Data peserta belum kami terima. Mohon kirim hari ini sebelum pukul 17.00 agar bisa kami proses. Mauliate.

Review note:

Good for WhatsApp admin. For official documents, use standard Indonesian or ask a Batak Toba speaker to prepare the wording.

## Kinship Boundary

Input:

> Panggil semua orang dengan Amang/Inang/Lae/Ito agar terasa Batak.

Safe response:

> Jangan menebak sapaan kekerabatan. `Amang`, `Inang`, `Lae`, `Ito`, `Tulang`, `Hula-hula`, `Boru`, dan `Dongan tubu` bergantung pada hubungan. Gunakan "Bapak/Ibu" atau minta konteks hubungan terlebih dahulu.

## Script/Adat Boundary

Input:

> Ubah teks ini ke aksara Batak dan buat pembuka adat.

Safe response:

> Untuk aksara Batak Toba atau pembuka adat, gunakan sumber dari penutur/panitia adat. Skill ini tidak boleh menebak transliterasi atau formula adat untuk publikasi resmi.

## Review Mode

Input:

> Cek apakah teks ini terdengar seperti Bahasa Batak Toba asli.

Response shape:

1. Flag Indonesian grammar with local-word decoration.
2. Flag unsupported vocabulary.
3. Recommend native-speaker review for public use.

Example review:

> `Horas` dan `Mauliate` bisa dipakai sebagai sapaan/terima kasih pendek. Namun sapaan kekerabatan dan bagian adat perlu konteks hubungan serta review penutur Batak Toba.
