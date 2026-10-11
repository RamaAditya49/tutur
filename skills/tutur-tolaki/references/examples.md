# Examples

## Target-Language Examples

- Indonesian: "Permisi."
  Bahasa Tolaki: "Tabee." Also printed "tabea".
  Note: Dirjan and Ino 2019. `tabee` is the word that marks a polite request. Both spellings appear in that paper. https://journal.fib.uho.ac.id/index.php/cakrawalalistra/article/download/1371/1020
  Usage: Opener for a request or a pass-by. Not a full speech.
- Indonesian: "Permisi, kalau tidak berat..."
  Bahasa Tolaki: "Tabee, keno oki mobea..."
  Note: Same paper. This is the opening of their polite hoe-borrowing utterance. Do not reuse the rest of that sentence for a new object.
  Usage: Soften a real request, then say the object in Indonesian if it is not the published tool.
- Indonesian: "Tanpa mengurangi rasa hormat, bisa panggilkan bapaknya Dewi."
  Bahasa Tolaki: "tabea inggomiu perikeikona pani Dewi"
  Note: Same paper. They say `tabea inggomiu` includes speaker and hearer ("kita") and fits elder-to-elder talk. It does not stay polite when an elder aims it at a child.
  Usage: Quote between adults. Do not aim it downward.
- Indonesian: "Saya titip salam." Reply: "Saya akan sampaikan salammu."
  Bahasa Tolaki: "Salamunggu toka." Reply: "Ku onggoki moko dunggui salamumu."
  Note: Same paper, their data 18, between elders.
  Usage: Passing a greeting, not a new idiom for "forward this PDF".
- Indonesian: "Ibu." "Bapak." "Kakak." "Adik."
  Bahasa Tolaki: "ina." "ama." "ka'aka." "hai."
  Note: Haslan 2018 findings table. `pue` / `mbue` are kakek, nenek, and also cucu in that table. `hai langgai` adik laki-laki, `hai ndina` adik perempuan. https://ejournal.iainkendari.ac.id/index.php/shautut-tarbiyah/article/download/922/810/0
  Usage: Family address. Do not stack them into a title.
- Indonesian: "Tina, kamu pergi ke mana?" The paper's English is "Tina, where are you going?"
  Bahasa Tolaki: "Tina, embee ariamu?"
  Note: Haslan 2018. The reply in the paper is `Arilako mo'oli osampo`, English "I'm going to buy a shampoo".
  Usage: Quote this exchange. Do not change the errand.

## Casual Chat

Input:

> Balas sepupu di Konawe yang tanya sudah sampai belum.

Output (mixed):

> Tabee. Sudah sampai. Kabar ina di rumah baik. Aku singgah nanti sore.

Note:

`Tabee` and `ina` are attested. The rest is Indonesian. Do not expand this into the shampoo dialogue unless the user is actually asking Tina where she is going.

## Public Reminder

Input:

> Ingatkan warga kerja bakti besok pagi.

Output (mixed):

> Tabee. Besok kerja bakti jam 07.00 di balai. Bawa alat sendiri. Salamunggu toka kalau berhalangan, sampaikan ke ketua RT.

Note:

`Salamunggu toka` is only the "saya titip salam" piece. The time and the place stay Indonesian. For a printed notice, a Tolaki speaker should check it. This is not aimed as `tabea inggomiu`, because the crowd includes children and the paper limits that phrase.

## Professional Or Admin

Input:

> Pesan admin desa: KTP belum masuk.

Output (mixed):

> Tabea inggomiu. Foto KTP belum masuk. Mohon kirim sebelum jam 16.00. Data dipakai untuk administrasi saja.

Note:

Use `tabea inggomiu` here only if the clerk is writing to another adult as a peer. If the clerk is older and the reader is a young resident, open with `Tabee` instead. The deadline stays Indonesian.

## Adat Boundary

Input:

> Tuliskan sambutan adat Tolaki untuk penerimaan tamu.

Output:

> Bagian adatnya perlu kalimat dari penutur atau dari tetua yang biasa bicara di acara itu. Yang bisa dipakai dari sumber di skill ini hanya pembuka `tabea` / `tabee`, dan sapaan `ina`, `ama`, `pue`, `ka'aka`, `hai`. Sambutan lengkapnya jangan disusun dari situ.

## Review Mode

Input:

> Cek: "Tabea inggomiu adik, besok kita ke pesta adat pakai bahasa Tolaki penuh."

Response:

1. `Tabea inggomiu` di paper Dirjan dan Ino dipakai antarang dewasa. Diarahkan ke "adik", sumber yang sama mengatakan nuansanya berubah.
2. Tidak ada kalimat pesta adat yang tersimpan di skill ini. Jangan dianggap Tolaki penuh.
3. "Besok kita ke pesta adat" masih bahasa Indonesia.

Safer rewrite (mixed):

> Tabee. Besok ada acara adat. Waktu dan tempatnya menyusul dari panitia. Kalau ada rumus sambutannya, minta teks dari yang biasa bicara.
