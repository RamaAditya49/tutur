# Examples

## Source-Aware Generation

Input:

> Buat teks pendek untuk mengajak anak muda menjaga bahasa Gayo.

Safer response shape:

1. Produce the message in Indonesian first.
2. Translate only verified short phrases into Gayo when sources support them.
3. Mark uncertain terms for KBDA/native-speaker review.

## Review Mode

Input:

> Cek apakah kalimat ini terdengar seperti bahasa Gayo atau cuma Indonesia yang diganti katanya.

Response shape:

1. Flag Indonesian grammar that is only decorated with Gayo vocabulary.
2. Check important words against KBDA/Kamus Gayo.
3. Recommend native-speaker review for public use.

## Dialect Caution

If the user asks for a slogan for a specific Gayo community, ask for the target area or a sample phrase before choosing local wording.
