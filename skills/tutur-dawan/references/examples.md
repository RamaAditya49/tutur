# Examples

## Target-Language Examples

- Indonesian: "Halo."
  Bahasa Dawan: "Tabe."
  Meaning/note: Uab Meto Wikipedia phrase table lists Halo, Tabe as hello. The table does not name Amanuban, Mollo, Amfoang, or any other variety.
  Usage: Opening only. The next sentence stays in Indonesian.
- Indonesian: "Sehat."
  Bahasa Dawan: "leko."
  Meaning/note: Humanis 2025 glosses leko as healthy in both Oenames and Kaesmetan (Amfoang). The Wikipedia table also puts leko in a you're-welcome row. Do not use that reading.
  Usage: Single-word health answer for those two subdialects. Not a thanks line, and not a full sentence.
- Indonesian: "Saya."
  Bahasa Dawan: "au."
  Meaning/note: Same Amfoang paper, both subdialects, gloss I. ho on that table is you, in is he/she.
  Usage: Cite the pronoun with the Amfoang label. Do not invent au leko as "saya sehat".
- Indonesian: "Satu."
  Bahasa Dawan: "mese."
  Meaning/note: Same paper, both subdialects, gloss one. Wikipedia spells a similar number Mese'. Do not mix the spellings.
  Usage: Cite the number. For two, use nub in Oenames and nua in Kaesmetan, not one form for every Dawan.
- Indonesian: "Kami/kita" (gloss sumber hanya we).
  Bahasa Dawan: "hit" (Oenames); "hita" (Kaesmetan).
  Meaning/note: Same paper. Both are glossed we. hai is also glossed we in both subdialects. The paper does not mark inclusive or exclusive.
  Usage: Pick hit or hita only after the subdialect is named. Do not export either form to Amarasi or Amanuban.

## Casual Chat

Input:

> Balas sepupu Amfoang, subdialek Oenames, yang tanya kabar.

Output (mixed):

> Tabe. Aku baik. Sore ini aku di rumah, jam 4 boleh mampir.

Note:

Tabe is the phrase-list hello and is not labeled Oenames in the source. The rest is Indonesian, so the message is mixed. leko is available as the single word 'sehat' for Oenames, not as a sentence meaning aku baik. ho is the Amfoang word for you and is not dropped into this Indonesian reply.

## Public Reminder

Input:

> Ingatkan warga desa di Timor Tengah Selatan, rapat besok.

Output (mixed):

> Tabe. Rapat desa besok jam 08.00 di balai. Bawa usulan tertulis. Kabar lagi kalau tidak bisa datang.

Note:

Tabe plus Indonesian. Mixed. The Amfoang words are not used, because Timor Tengah Selatan is a different Peta Bahasa dialect. Ask a speaker of that dialect before a loudspeaker or a printed notice.

## Professional Or Admin

Input:

> Pesan admin sekolah: SPP belum masuk.

Output (mixed):

> Tabe. SPP bulan ini belum masuk. Mohon transfer hari ini sebelum pukul 14.00 dan kirim bukti ke admin. Nominalnya tetap yang ada di surat.

Note:

Money, time, and the document stay in Indonesian. Hao and Kaha' can be yes and no only as single words from the phrase list, variety unstated. They do not carry this payment line. Mixed.

## Adat Boundary

Input:

> Buat sambutan adat Atoni untuk nikahan di Amanuban.

Safe response:

> Sambutan adat tidak disusun dari daftar kata. Data kata di skill ini adalah subdialek Oenames dan Kaesmetan di Amfoang, bukan naskah Amanuban. Minta teks yang sudah dipakai keluarga di desa itu, lalu skill ini hanya bisa mengecek kata yang memang ada di sumber.

## Review Mode

Input:

> Cek teks ini: "Tabe. Leko, obrigadu. Hita nub."

Response shape:

1. Flag the thanks reading of leko and the Baikeno loan.
2. Flag a mix of subdialects and an unattested string.
3. Keep Tabe as a hello with the variety unmarked.

Example review:

> Tabe boleh sebagai halo dari tabel frasa, ragam tidak disebut. leko di data Amfoang artinya sehat, bukan balasan terima kasih. obrigadu adalah bentuk yang sumber kaitkan dengan Timor Leste, bukan dengan contoh NTT di skill ini. hita adalah we untuk Kaesmetan, nub adalah two untuk Oenames, dan "Hita nub" bukan kalimat yang tercetak. Pisahkan: Tabe, lalu bahasa Indonesia. Kalau perlu angkanya, tulis nub untuk Oenames atau nua untuk Kaesmetan, satu saja.
