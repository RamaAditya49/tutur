# Examples

Sentences below are from Melisa Padang, Jekmen Sinulingga, and Flansius Tampubolon, Aksara Pakpak, USU Press, 2023: https://usupress.usu.ac.id/images/buku/Aksara%20Pakpak_layout_crop.pdf

The Indonesian line is that book's gloss. Label: mixed, whenever Indonesian carries the rest of the message. The 1977 Dairi Pakpak dictionary was not opened, so nothing here is quoted from it.

## Target-Language Examples

- Indonesian: "Sehat-sehat."
  Bahasa Pakpak: "Njuah-njuah."
  Note: Nasal form of `juah`, glossed kabar baik/sehat. The preface also closes with `Njuah Njuah`. Not Karo `mejuah-juah`. Not horas.
  Usage: Opening or closing a conversation.
- Indonesian: "Sehat-sehat lah kita semuanya."
  Bahasa Pakpak: "Njuah-njuah mo kita karinana."
  Note: The book prints `njuah-njuah mo kita karinana. i mo tuhu` and glosses the second piece Amen. Leave `i mo tuhu` off unless the user asked for that closing.
  Usage: A group. Do not add a second Pakpak sentence after it.
- Indonesian: "Jangan kau panjati pokok durian itu, nanti kamu jatuh."
  Bahasa Pakpak: "Ulang ko menangkih-nagkih i benna terutung, i ndabuh ko nahan."
  Note: Example of `ndabuh`, jatuh. `ko` is kamu in this line.
  Usage: A real warning about climbing. Not a general "don't".
- Indonesian: "Sudah rusak jembatan, tidak bisa lagi dilewati."
  Bahasa Pakpak: "Enggo nceda jembaten, oda boi ke karap i."
  Note: Example under `nceda`. `enggo` is sudah and `oda` is tidak inside this gloss.
  Usage: Only when the bridge is actually out. The detour stays Indonesian.
- Indonesian: "Rumahku dekat ke tempatmu, suatu saat kita akan bertemu."
  Bahasa Pakpak: "Njolmit ngo kutangku mi bekkasmu, kaduan pejumpa kita."
  Note: Second example under `njuah` / `nj` in the nasalisasi section.
  Usage: A short remark about distance. Do not turn it into directions.
- Indonesian: "Malu. Kalau."
  Bahasa Pakpak: "Mela. Mella."
  Note: The book says `mela` is malu and `mella` is kalau/jika. The consonant is the difference.
  Usage: As a check, not as a sentence by themselves. Do not swap them.

## Casual Chat

Input:

> Balas sepupu di Sidikalang. Kamu sudah terima berasnya.

Output:

> Label: mixed. Njuah-njuah. Berasnya sudah sampai. Suak di Sidikalang pada buku Aksara Pakpak adalah Keppas. Kalau ejaannya beda di rumah, ikuti keluarga.

Use:

The greeting is the book's word. The rice news is Indonesian. Keppas is the book's label for that area, not a claim that this sentence was recorded in Sidikalang.

## Public Reminder

Input:

> Kabari warga bahwa jembatan tidak bisa dilewati hari ini.

Output:

> Label: mixed. Njuah-njuah mo kita karinana. Enggo nceda jembaten, oda boi ke karap i. Lewat jalan atas. Kumpul info di balai pukul 16.00.

Use:

Both Pakpak sentences are printed in the book. The detour and the hour are Indonesian. Use this only if the bridge is really broken. Otherwise keep the whole notice in Indonesian and leave the bridge sentence out.

## Professional Or Admin

Input:

> Pesan admin puskesmas untuk pasien yang pindah jadwal.

Output:

> Label: mixed. Njuah-njuah. Pemeriksaan dipindah ke besok pukul 09.00. Bawa kartu berobat.

Use:

The clinic fact is Indonesian. Pakpak is the greeting only.

## Adat Boundary

Input:

> Buat ucapan saat bakar tulang leluhur dan tulis di aksara Pakpak.

Safe response:

> Ucapan menutung tulan dan aksara Pakpak tidak disusun dari buku fonologi. Buku Aksara Pakpak menyebut ritus itu dan mengatakan aksara di kulit kayu hanya bisa ditulis orang yang tahu bahasanya. Minta teks dari keluarga. `Tulanmu` pada contoh `mpihir pe tulanmu` artinya tulangmu, bukan sapaan paman.

## Review Mode

Input:

> Cek teks ini: "Mejuah-juah. Horas. Njuah-njuah, Tulang."

Response:

> `Njuah-njuah` ada di Aksara Pakpak sebagai sehat-sehat. `Mejuah-juah` adalah bentuk Karo. `Horas` bukan salam di sumber Pakpak ini. `Tulang` sebagai sapaan paman tidak ada di contoh yang dibaca. Di buku itu `tulanmu` pada satu kalimat fonologi artinya tulang. Label yang jujur: sapaan Pakpak-nya `njuah-njuah`, sisanya bahasa lain. Tulis `Njuah-njuah`, lalu maksudnya dalam bahasa Indonesia.
