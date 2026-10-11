# Examples

## Target-Language Examples

- Indonesian: "Selamat pagi."
  Bahasa Tombulu: "Syambae."
  Meaning/note: Vocabulary table on the Tombulu Wikipedia page glosses Good morning as Syambae. Support phrase, not from the 1993 grammar.
  Usage: Morning hello only. Do not add a second sentence in Tombulu.
- Indonesian: "Apa kabar? Baik semua?"
  Bahasa Tombulu: "Kura-mo? leos 'man?"
  Meaning/note: Phrase table glosses this line as "How are you? all good?" The 1993 grammar glosses le?os as 'baik'. Spelling leos / le'os / le?os is not unified.
  Usage: Casual check-in. Keep the reply after it in Indonesian unless the user supplies Tombulu.
- Indonesian: "Engkau."
  Bahasa Tombulu: "Niko."
  Meaning/note: Wikipedia vocabulary lists You as Niko. Struktur Bahasa Tombulu glosses niko as 'engkau'.
  Usage: Single pronoun. Do not invent a polite variant.
- Indonesian: "Terima kasih."
  Bahasa Tombulu: "Makapulu Leos."
  Meaning/note: Phrase table glosses Thank you as Makapulu Leos. No grammar example was found for this full thanks line.
  Usage: Short thanks. Do not extend it into a speech.
- Indonesian: "Orang."
  Bahasa Tombulu: "tou."
  Meaning/note: Struktur Bahasa Tombulu glosses tou as 'orang'. The 2004 guide uses tou Sawangan for 'orang Sawangan'.
  Usage: Cite the word. Do not build a new title from it.

## Casual Chat

Input:

> Balas sepupu di Tomohon yang tanya kabar.

Output (mixed):

> Syambae. Kura-mo? Aku baik. Sore ini aku lewat Woloan, titip kunci di rumah oma ya.

Note:

Syambae and Kura-mo? are the attested Tombulu pieces. The rest is ordinary Indonesian. Mixed. This is not a full Tombulu translation.

## Public Reminder

Input:

> Ingatkan warga kerja bakti besok pagi.

Output (mixed):

> Syambae. Besok kerja bakti jam 07.00 di balai lingkungan. Bawa sapu masing-masing. Kabar lagi kalau tidak bisa datang.

Note:

One attested greeting, then Indonesian so the time and place stay clear. Mixed. For a printed notice, ask a Tombulu speaker in the village named on the notice.

## Professional Or Admin

Input:

> Pesan admin homestay: tamu belum kirim KTP.

Output (mixed):

> Syambae, Kak. Foto KTP belum masuk. Mohon kirim hari ini sebelum pukul 18.00. Data dipakai untuk check-in saja.

Note:

The deadline and the document stay in Indonesian. Makapulu Leos can close a thanks message, not this request. Mixed.

## Adat Boundary

Input:

> Buat doa pembuka adat Tombulu untuk acara keluarga.

Safe response:

> Untuk doa atau pembuka adat, pakai teks yang sudah dipakai keluarga atau gereja setempat. Skill ini hanya memegang sapaan pendek seperti Syambae dan Kura-mo? leos 'man? Tabel frasa publik memuat teks ibadah. Teks itu tidak disalin ulang di sini dan tidak dijadikan pola baru.

## Review Mode

Input:

> Cek apakah teks ini Tombulu asli: "Syambae jo, kong apa kabar ngana?"

Response shape:

1. Flag Melayu Manado particles and pronouns.
2. Flag Tombulu words that are not in the local mirror.
3. Ask for a Tombulu speaker if the text will be printed.

Example review:

> Syambae ada di tabel frasa sebagai selamat pagi. jo, kong, dan ngana adalah pola Melayu Manado, bukan Tombulu. Ganti menjadi Syambae. Kura-mo? lalu lanjut dalam bahasa Indonesia. Hasilnya mixed, bukan paragraf Tombulu.
