# Examples

Lines below are example sentences from Kamus Komering Indonesia, Balai Bahasa Sumatera Selatan: https://kbdsumsel.kemdikbud.go.id/kki/kamus/words

The Indonesian line is that dictionary's gloss. Label: mixed, whenever Indonesian carries the rest of the message. None of these lines is marked Pulau Negara or Aji on the word list.

## Target-Language Examples

- Indonesian: "Lelaki itu permisi kepada orang tua itu."
  Bahasa Komering: "Bakas sina tabik rik jolma tuha sina."
  Note: Headword `tabik`, permisi kepada orang yang sedang duduk sambil menundukkan badan. Not Lampung `tabik pun`.
  Usage: Passing seated elders. Do not put it at the top of every chat.
- Indonesian: "Wah kamu ini, jangan marah begitu."
  Bahasa Komering: "Ai niku ja dang ngamuk juk sina."
  Note: Headword `ai`, a seruan. `niku` and `dang` are inside this printed sentence.
  Usage: A short scolding to someone already in the conversation.
- Indonesian: "Kamu jangan ke sini sekarang nanti saja."
  Bahasa Komering: "Niku dang tidija ganta onti juga."
  Note: Headword `dang`, jangan. The follow-up time stays in Indonesian if you need a clock time.
  Usage: Tell one person to come later. Do not turn it into a public schedule.
- Indonesian: "Kalau hari hujan, saya tidak datang."
  Bahasa Komering: "Amon hujan, nyak mak ratong."
  Note: Headword `amon`, kalau. `nyak` is inside the printed sentence as saya.
  Usage: A rain excuse to family. The replacement day stays in Indonesian.
- Indonesian: "Mengapa engkau tidak datang semalam."
  Bahasa Komering: "Ngapi niku mak ratong bingi sina."
  Note: Headword `ngapi`, mengapa.
  Usage: One question in a chat. Do not add a second Komering sentence after it.
- Indonesian: "Apa kabar para hadirin?"
  Bahasa Komering: "Api kabar gusti pohngun?"
  Note: Headword `gusti pohngun`, saudara sekalian, para hadirin.
  Usage: A room of guests. Stiff for one cousin.
- Indonesian: "Rumahmu bagus sekali."
  Bahasa Komering: "Lambahanmu holau nihan."
  Note: Headword `holau`, bagus.
  Usage: A house remark. Do not expand it into an invitation.
- Indonesian: "Dari mana kamu, malam-malam baru pulang?"
  Bahasa Komering: "Jakpa niku, bingi-bingi ompai mulang?"
  Note: Headword `jakpa`, dari mana.
  Usage: A doorstep question. The answer can stay Indonesian.

## Casual Chat

Input:

> Balas sepupu yang batal datang semalam.

Output:

> Label: mixed. Ngapi niku mak ratong bingi sina. Kabarnya lewat chat saja, besok pagi aku tunggu di rumah.

Use:

The Komering question is the dictionary line. The plan for tomorrow is Indonesian. No `tabik`, because nobody is passing seated elders.

## Public Reminder

Input:

> Ingatkan warga soal kumpul di balai Sabtu pagi.

Output:

> Label: mixed. Api kabar gusti pohngun? Kumpul tetap Sabtu pukul 08.00 di balai. Bawa alat sendiri.

Use:

`gusti pohngun` matches a group of guests in the dictionary. The hour and the place stay Indonesian. Do not claim the line is dialek Aji or Pulau Negara.

## Professional Or Admin

Input:

> Pesan admin sekolah untuk orang tua yang belum kirim formulir.

Output:

> Label: mixed. Formulir tetap bahasa Indonesia. Niku dang tidija ganta onti juga hanya kalau maksudnya memang "jangan ke sini sekarang". Untuk pengumuman, tulis: formulir dikumpul di tata usaha sebelum Jumat pukul 14.00.

Use:

The school deadline is Indonesian. The Komering line is optional and only if the message is really "don't come now".

## Adat Boundary

Input:

> Buat sambutan adat pernikahan Komering di OKU Timur.

Safe response:

> Sambutan adat tidak disusun dari kamus. Minta teks yang dipakai keluarga di kampung itu. `Sikam kahwin adat kumoring` di kamus hanya contoh lema adat, artinya kami kawin adat komering, dan dialeknya tidak ditandai. Hiring-hiring dan pisaan juga tidak direka di sini.

## Review Mode

Input:

> Cek teks ini: "Tabik pun, kak. Sikam ke balai nihan."

Response:

> `Tabik pun` bukan contoh di Kamus Komering Indonesia. Di kamus itu `tabik` artinya permisi kepada orang yang sedang duduk. `Sikam ke balai nihan` tidak ada di contoh yang dibaca. Label yang jujur: ini bukan kalimat Komering. Pakai satu kalimat kamus, misalnya `tamuna kok ratong` kalau tamunya memang sudah datang, lalu sisanya bahasa Indonesia.
