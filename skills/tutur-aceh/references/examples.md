# Examples

## Cautious Adaptation

Input:

> Tolong buat ucapan pembuka acara untuk komunitas Aceh.

Safer response shape:

> Provide a short Bahasa Indonesia draft first, then add a Bahasa Aceh draft only for phrases that can be checked against KBDA Daring or a user-provided sample.

Why:

Bahasa Aceh output can vary by region and register. For public events, do not invent ceremonial phrasing.

## Review Mode

Input:

> Review teks AI ini, apakah terasa seperti bahasa Aceh asli?

Response shape:

1. Check whether the text mixes Indonesian grammar with Acehnese words.
2. Flag suspicious words that need KBDA/native-speaker verification.
3. Provide a safer rewrite or ask for dialect context.

## Short Public Text

Input:

> Buat versi lokal untuk poster: "Mari jaga bahasa daerah kita."

Response shape:

> If no verified Acehnese wording is available, keep the Indonesian sentence and suggest checking KBDA/native speaker before publication.

This is better than producing a confident but invented translation.
