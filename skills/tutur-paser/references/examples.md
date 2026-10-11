# Examples

## Target-Language Examples

- Target: `selamat ma`
  Indonesian gloss: Selamat pagi.
  Note: Kamus Bahasa Paser—Indonesia, under `selamat`. Same entry: `selamat malom` selamat malam, `selamat nayap` selamat sore. https://balaibahasakaltim.kemendikdasmen.go.id/file/kamus/KamusPaser-Indonesia.pdf
  Usage: A morning greeting. Do not use `selamat ma` at night. Dialect unlabeled in the entry.

- Target: `ise kabar iko?`
  Indonesian gloss: Apa kabarmu?
  Note: Same kamus, under `ise`. Also `ise karanyo?` siapa namanya.
  Usage: Asking after the person you are talking to. `iko` is you.

- Target: `tabe depo ulun tuo`
  Indonesian gloss: Permisi terhadap orang tua.
  Note: Same kamus, under `depo`.
  Usage: Asking leave of an older person. Not a greeting for every neighbor.

- Target: `iko harus deo belajar basa Paser`
  Indonesian gloss: Harus banyak belajar bahasa Paser. `iko` is the you of `ise kabar iko?`.
  Note: Same kamus, under `deo`. The printed gloss starts at "harus banyak belajar bahasa Paser".
  Usage: Urging someone to study Paser. Not a full school announcement.

- Target: `alamat iko mo mone?`
  Indonesian gloss: Alamatmu di mana?
  Note: Same kamus, under `alamat`.
  Usage: Asking where someone lives. The address they answer with stays as they wrote it.

- Target: `man taka ngadap Bupati`
  Indonesian gloss: Ayo menghadap Bupati.
  Note: Same kamus, under `ngadap`.
  Usage: Spoken nudge to go see the bupati. Not a letterhead.

## Casual Chat

Input:

> Sapa saudara pagi ini, tanya kabar, dan bilang ketemu jam 4 di balai.

Output (mixed):

> Selamat ma. Ise kabar iko? Ketemu jam 4 di balai.

Why:

`selamat ma` and `ise kabar iko?` are the morning greeting and the how-are-you from the kamus. The hour and the hall stay Indonesian. The kamus does not mark which of the ten dialects this is.

## Public Reminder

Input:

> Umumkan kerja bakti besok pagi jam 7, kumpul di pinggir jalan desa.

Output (mixed):

> Selamat ma. Kerja bakti besok jam 7, kumpul di pinggir jalan. Bawa alat sendiri.

Why:

Only the morning greeting is Paser. The place and the hour are Indonesian. Do not recast this as Kutai `hambat-hambat`.

## Professional Or Admin

Input:

> Ajak rekan berangkat menghadap bupati, formulir dibawa, selesai sebelum pukul 10.

Output (mixed):

> Man taka ngadap Bupati. Formulir dibawa. Selesai sebelum pukul 10.00.

Why:

The spoken clause is the kamus line. The form and the clock stay Indonesian.

## Adat Boundary

Input:

> Tuliskan soyong untuk buka ladang.

Safe response:

> Soyong tidak ditulis di sini. Kata pengantar kamus menyebut soyong sebagai ucapan permohonan yang dipimpin mulung, tetapi tidak mencetak teksnya. Yang ada untuk orang tua adalah kalimat biasa `tabe depo ulun tuo` dan larangan `nang derhaka depo ulun tuo`, bukan soyong ladang.

## Review Mode

Input:

> Cek: "Selamat ma, nyawa endak mendi dulu, etam pegi ke umo."

Response:

1. `selamat ma` is Paser for selamat pagi.
2. `nyawa`, `mendi`, and `etam` are Kutai dictionary pieces (aku, mandi, kita), not Paser lines in this skill.
3. Safer reply: `Selamat ma. Ise kabar iko? Rencana mandi dan berangkat ke ladang ditulis bahasa Indonesia, karena kalimatnya belum ada di contoh kamus Paser.`
