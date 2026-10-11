# Examples

## Target-Language Examples

- Target: `He'e.`
  Indonesian gloss: Ya. / Sudah.
  Note: Uma Lor, Malaka Barat. Used by women and men in everyday talk and in the recorded adat exchange. Adnyana 2018, http://www.ojs.linguistik-indonesia.org/index.php/linguistik_indonesia/article/download/74/66
  Usage: Short answer before the practical point. Do not replace it with `Hi'i` for a man or for a formal setting.

- Target: `Hi'i.`
  Indonesian gloss: Ya.
  Note: Same study. Informal speech by women only.
  Usage: A woman agreeing in a family chat. Not a public yes.

- Target: `Bai hau ba kare tia batar lai`
  Indonesian gloss: Kakek, saya pergi lihat jagung dulu.
  Note: Wife to grandfather in the Uma Lor transcript. The article's free translation also mentions the kitchen; the interlinear gloss is the line above.
  Usage: Leaving the house on an errand. Keep the Uma Lor spelling `hau`.

- Target: `Yani nabe?`
  Indonesian gloss: Yani di mana?
  Note: Husband asking about their daughter, Uma Lor transcript.
  Usage: Looking for a named person. The name stays the person's real name; `nabe` is the attested where-word in this line.

- Target: `Mai Bapa ita lao.`
  Indonesian gloss: Ayo Bapak, kita berangkat.
  Note: Wife to husband, Uma Lor transcript, as the bus arrives.
  Usage: Invitation to leave together. The address `Bapa` is part of the attested line.

- Target: `Mai ita la'o liu dei.`
  Indonesian gloss: Mari kita jalan terus saja.
  Note: Fehan sketch, Williams-van Klinken, example (56). Spelling `la'o` belongs to that sketch, not to the Uma Lor lines. http://www.tetundit.tl/Publications/Williams-van%20Klinken%20-%20Fehan%20overview.pdf
  Usage: Keep going with the people already walking. Do not respell it as `lao` in the same paragraph as this citation.

## Casual Chat

Input:

> Kabari kakak di Malaka bahwa saya sudah lihat pesan dan jagungnya saya cek dulu.

Output (mixed):

> He'e. Bai hau ba kare tia batar lai. Nanti saya kabari lagi.

Why:

`He'e` and the jagung line are attested. The follow-up stays Indonesian because no sourced sentence covers "I will message again".

## Public Reminder

Input:

> Ingatkan bapak-bapak di kampung supaya berangkat ke balai jam 4 sore.

Output (mixed):

> Mai Bapa ita lao. Kumpulnya jam 16.00 di balai.

Why:

The Tetun sentence is the attested "let's go" to Bapa. The time and place stay Indonesian. This is a spoken reminder, not a banner.

## Professional Or Admin

Input:

> Buat pesan untuk guru tentang rapat jam 9 dan daftar hadir.

Output:

> Rapat guru pukul 09.00. Daftar hadir diisi di lembar yang sudah dibagi. Untuk sapaan keluarga di luar surat ini, jawaban singkat yang tersurat adalah He'e.

Why:

The meeting facts have no attested Tetun sentence in this skill. `He'e` is named as the sourced family answer, not dropped into the letter as decoration.

## Adat Boundary

Input:

> Tuliskan sambutan makoan untuk minum adat.

Safe response:

> Sambutan makoan tidak disusun dari skill ini. Adnyana 2018 merekam sapaan di dalam satu acara minum, termasuk jawaban He'e dari ibu-ibu dan bapak-bapak. Itu kutipan peristiwa, bukan naskah untuk dipakai ulang. Minta teks dari makoan atau panitia setempat.

## Review Mode

Input:

> Cek: "Diak ka lae? Hau mau ke kantor dulu, bondia."

Response:

1. `Diak ka lae?` and `bondia` come from the Timor-Leste teaching register, including the 2019 Badan Bahasa textbook. They are Tetun Dili material, not the Uma Lor sample.
2. `Hau mau ke kantor dulu` is Indonesian grammar with `hau` attached. The attested first-person errand line is `Bai hau ba kare tia batar lai`, which is about checking corn, so it cannot be reused as "going to the office".
3. Safer mixed reply for a Belu family chat about leaving: `He'e. Saya ke kantor dulu.`
