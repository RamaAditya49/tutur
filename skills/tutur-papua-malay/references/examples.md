# Examples

## Target-Language Examples

- Target: `mama-ade ko masak daging sa biking papeda e?`
  Indonesian gloss: Tante, masak dagingnya, saya bikin papeda, ya?
  Note: Kluge, example (51), record 080921-001-CvNP.0073. Free translation in the grammar: you aunt cook the meat, I make the sagu porridge, eh? https://library.oapen.org/bitstream/handle/20.500.12657/31325/1/631266.pdf
  Usage: Splitting kitchen work with the aunt. `sa` is I, `ko` marks tante as the one addressed.

- Target: `Wili ko jangang gara~gara tanta dia itu!`
  Indonesian gloss: Wili, jangan mengganggu tanta itu.
  Note: Kluge, example (53), record 081023-001-Cv.0038, said to a young boy. The grammar's free translation is "you Wili don't irritate that aunt".
  Usage: Quote this warning as recorded. Do not swap Wili for another name and call the new sentence attested.

- Target: `Nofela bicara suda!`
  Indonesian gloss: Nofela, bicara.
  Note: Kluge, example (56), record 080922-001a-CvPh.0805. A father asks his daughter to speak to him. `suda` is the push.
  Usage: Family prompt to Nofela, or a labelled quotation of that prompt.

- Target: `sa dengang pace ini kitong dua jalang, ayo`
  Indonesian gloss: Saya dengan pace ini, kita berdua jalan, ayo.
  Note: Corpus line quoted in the Wacana review of Kluge, with gloss 1sg with man this, 1pl two walk, come on. https://scholarhub.ui.ac.id/cgi/viewcontent.cgi?article=1303&context=wacana
  Usage: Setting off with one man. `pace` here is man, `kitong` is we.

- Target: `pace dorang dua ini ke atas`
  Indonesian gloss: Dua pace ini ke atas.
  Note: Kluge noun-phrase example, glossed "both of the two men here (went) up". https://scholarlypublications.universiteitleiden.nl/access/item%3A2944789/download
  Usage: Pointing at two men and the direction. Not a greeting.

- Target: `mace ko rasa lucu`
  Indonesian gloss: Mace, rasanya lucu.
  Note: Kluge, example (52), record 081010-001-Cv.0206. The book glosses `mace` as woman and translates the reaction as Madam feeling funny. The visible words are these.
  Usage: Reacting to a story while addressing a woman. Not a compliment template for new situations.

## Casual Chat

Input:

> Ajak tante bagi tugas masak, daging dia yang urus, papeda saya yang bikin, nanti jam enam makan.

Output (mixed):

> Mama-ade ko masak daging sa biking papeda e? Makannya jam enam.

Why:

The first sentence is the corpus offer. The hour is new, so it stays Indonesian. This is not the Ambon bamboo line and not a poster.

## Public Reminder

Input:

> Ingatkan anak-anak di kompleks supaya tidak mengganggu tante, dan rapat RT jam 7 malam.

Output (mixed):

> Contoh yang tersurat, kepada anak bernama Wili: Wili ko jangang gara~gara tanta dia itu! Untuk rapat RT, jam 19.00. Nama anak lain tidak dimasukkan ke kalimat itu.

Why:

The warning is a recorded address to Wili. The meeting time is Indonesian. The pattern is shown without pretending a new name is already in the grammar.

## Professional Or Admin

Input:

> Ingatkan staf bahwa perjalanan dinas berangkat sekarang dan laporan dikumpulkan besok pukul 10.

Output (mixed):

> Sa dengang pace ini kitong dua jalang, ayo. Laporan dikumpulkan besok pukul 10.00.

Why:

The walking line is attested unofficial speech. The deadline is an office fact and stays Indonesian. A formal surat dinas would not be written in this Malay.

## Adat Boundary

Input:

> Tuliskan doa adat Dani dalam bahasa Papua.

Safe response:

> Doa adat Dani tidak ditulis di skill ini. Skill ini hanya Melayu Papua, dari contoh seperti pace, mace, dan papeda dalam tata bahasa Kluge. Bahasa Dani, Biak, Sentani, dan Asmat punya urusan sendiri dan tidak digabung ke sini.

## Review Mode

Input:

> Cek: "Beta mo pi, jang buang sampa, pace ko ikut."

Response:

1. `Beta`, `mo pi`, and `jang buang sampa` are Melayu Ambon dictionary material, not the Sarmi corpus.
2. `pace ko` resembles the Papuan pattern of person plus `ko`, but that exact string is not one of the printed clauses. The printed walk line is `sa dengang pace ini kitong dua jalang, ayo`.
3. Safer mixed reply when two people are setting off: `Sa dengang pace ini kitong dua jalang, ayo. Sampahnya jangan dibuang di selokan.`
