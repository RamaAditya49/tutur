# Examples

Muna lines are from René van den Berg, A Grammar of the Muna Language, standard Muna of Kecamatan Katobu. Square brackets mark an infix, as in his own note on `na-k[um]ala` "he will go". They are not pronounced. Indonesian glosses translate his English glosses. Longer messages are labeled mixed.

## Target-Language Examples

- Indonesian: "Kamu mau ke mana?"
  Bahasa Muna: "O-k[um]ala ne hamai?"
  Note: Usual greeting on the street. `o-` is kamu on the verb, `ne hamai` is the "where" of this example. Brackets mark the infix `-um-`.
  Usage: Passing someone in Raha or another Katobu setting. Not a Wolio greeting.
- Indonesian: "Matahari sudah di puncak."
  Bahasa Muna: "Ka-ghindotu-no gholeo itu-a!"
  Note: Printed as a greeting at noon. The final `-a` is the clitic he discusses on exclamations, not an extra word to copy onto other sentences.
  Usage: A midday hello. Do not also invent selamat pagi.
- Indonesian: "Saya belajar bahasa Muna."
  Bahasa Muna: "A-po-guru-ghoo wamba Wuna."
  Note: `wamba Wuna` is the language's own name in the grammar. `a-` is saya.
  Usage: Saying you are learning it. The schedule stays Indonesian.
- Indonesian: "Besok saya pergi ke Raha."
  Bahasa Muna: "Naewine a-k[um]ala we Raha."
  Note: Locative in this line is `we`, not the `ne` of the street greeting. `naewine` is tomorrow in the gloss.
  Usage: A travel text to Raha. Add the hour in Indonesian.
- Indonesian: "Kamu di mana?"
  Bahasa Muna: "Hamai-ko-mo?"
  Note: Separate from the street greeting. Here kamu is `-ko` on `hamai`.
  Usage: When you need a location, not a direction of travel.
- Indonesian: "Apa ini?"
  Bahasa Muna: "O hae-no ini-a?"
  Note: `o` here is the article on the question word in this example. Related: `peda hae itu-a?` "how is it (going)?"
  Usage: Asking about a thing in front of you. Do not add `o` to Indonesian nouns.

## Casual Chat

Input:

> Balas sepupu di Raha yang ketemu di jalan dan tanya jadi ke mana.

Output:

> Label: mixed. O-k[um]ala ne hamai? Aku ke pasar dulu, balik sebelum zuhur.

Use:

Street greeting from the Katobu grammar, then the plan in Indonesian. The brackets in the greeting mark the infix. They are part of the grammar's spelling, not extra letters to pronounce.

## Public Reminder

Input:

> Ingatkan warga soal pertemuan siang di balai Raha.

Output:

> Label: mixed. Ka-ghindotu-no gholeo itu-a! Pertemuan siang ini pukul 13.00 di balai Raha. Yang berhalangan, kabari ketua RT sebelum pukul 11.00.

Use:

Noon greeting, standard Muna. The hour and the place stay Indonesian so nobody has to guess a Muna time expression.

## Professional Or Admin

Input:

> Pengumuman singkat les bahasa Muna untuk orang tua murid.

Output:

> Label: mixed. A-po-guru-ghoo wamba Wuna. Les dimulai Senin pukul 16.00 di ruang 2.

Use:

The learning sentence matches the class. The schedule stays Indonesian. This line is standard Muna from the Katobu grammar, not a Gumas or Tiworo transcript.

## Adat Boundary

Input:

> Buat rumus adat pernikahan Muna untuk dibacakan di Buton.

Safe response:

> Rumus adat tidak disusun dari tata bahasa van den Berg. Minta teks keluarga atau tokoh adat di kampung yang dimaksud. Contoh di skill ini adalah bahasa sehari-hari standard Muna, Katobu, dan tidak mencakup dialek Buton yang dipisah di Peta Bahasa. Wolio dan Tolaki juga bukan bahasa ini.

## Review Mode

Input:

> Cek: "Salam Wolio, o-k[um]ala ne hamai, mari lestarikan bahasa Tolaki di Muna."

Response:

> `O-k[um]ala ne hamai?` adalah sapaan jalan dalam bahasa Muna standard, Katobu, dan butuh tanda tanya. Wolio adalah bahasa lain. Tata bahasa ini bahkan memakai `wamba Wolio` untuk menyebut bahasa Wolio, terpisah dari `wamba Wuna`. Tolaki juga bukan Muna. Kalimat ajakan yang panjang itu tidak perlu. Label: mixed. "O-k[um]ala ne hamai? Aku ke balai. Ini wamba Wuna, bukan Wolio."
