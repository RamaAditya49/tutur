# Examples

## Target-Language Examples

- Indonesian: "Permisi."
  Bahasa Bugis: "Tabe'."
  Meaning/note: Common Bugis politeness marker often used before speaking or passing.
  Usage: Use as short etiquette cue, not full ceremonial language.
- Indonesian: "Iya/baik."
  Bahasa Bugis: "Iye."
  Meaning/note: Common affirmative/polite response marker in Bugis support sources.
  Usage: Use carefully; spelling and context may vary.
- Indonesian: "Anda/kamu sopan."
  Bahasa Bugis: "Idi'."
  Meaning/note: Polite second-person form noted in politeness references.
  Usage: Use only when respectful address fits.
- Indonesian: "Bahasa Bugis."
  Bahasa Bugis: "Basa Ugi."
  Meaning/note: Common name for Bugis language.
  Usage: Use for language identity, not as a full grammar model.

## Source-Aware Generation

Input:

> Buat teks pendek untuk mengajak anak muda menjaga Bahasa Bugis.

Safer output:

> Tabe', mari belajar Basa Ugi mulai dari sapaan dan kata harian. Kalau ada kata yang belum yakin, cek kamus atau tanya penutur Bugis di keluarga/komunitas.

Why:

The output uses short source-supported cues and keeps the broader message in Indonesian.

## Casual Chat

Input:

> Balas teman yang tanya apakah kamu bisa datang.

Output:

> Iye, saya bisa datang. Tabe', nanti saya kabari lagi kalau sudah dekat lokasi.

Use:

Casual/polite hybrid. For full Bugis sentence, ask target area and speaker sample.

## Polite Invitation

Input:

> Buat undangan pendek untuk kegiatan komunitas Bugis.

Output:

> Tabe', Bapak/Ibu. Kami mengundang idi' hadir pada kegiatan komunitas Bugis hari Sabtu pukul 19.30. Lokasi dan susunan acara ada di lampiran.

Why:

`Tabe'` and `idi'` give a Bugis politeness signal while operational details remain clear in Indonesian.

## Professional/Admin

Input:

> Buat pesan admin untuk peserta yang belum mengirim formulir.

Output:

> Tabe', Kak. Formulir peserta belum kami terima. Mohon kirim hari ini sebelum pukul 17.00 agar data bisa kami proses. Iye, kalau sudah dikirim, silakan balas pesan ini.

Review note:

Good for WhatsApp admin with Bugis-aware politeness. Use standard Indonesian for official documents.

## Lontara/Script Boundary

Input:

> Ubah teks ini ke aksara Lontara Bugis.

Safe response:

> Untuk aksara Lontara, kirim sumber ejaan atau contoh dari penutur/rujukan yang ingin diikuti. Skill ini tidak boleh menebak transliterasi Lontara untuk publikasi resmi tanpa sumber.

## Adat Boundary

Input:

> Buat pembuka acara adat Bugis.

Safe response:

> Untuk acara adat, pernikahan, atau keagamaan Bugis, jangan membuat formula dari nol. Kirim contoh dari panitia atau penutur setempat, lalu skill ini bisa membantu menandai bagian yang perlu dicek.

## Review Mode

Input:

> Cek apakah teks ini terdengar seperti Bahasa Bugis asli.

Response shape:

1. Flag Indonesian grammar with local-word decoration.
2. Flag unsupported vocabulary.
3. Recommend native-speaker review for public use.

Example review:

> `Tabe'`, `iye`, dan `idi'` dapat menjadi penanda kesantunan Bugis, tetapi kalimat panjang setelahnya masih Indonesia. Untuk publikasi, tentukan daerah/komunitas target dan minta penutur Bugis mengecek pilihan katanya.
