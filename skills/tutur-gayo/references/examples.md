# Examples

## Target-Language Examples

KBDA-backed Gayo vocabulary examples:

- `belejer`: belajar.
- `becerite`: bercerita.
- `anak benen`: anak perempuan.
- `anak rawan`: anak laki-laki.

Working micro-example:

> Belejer bahasa Gayo.

Meaning:

> Belajar bahasa Gayo.

Note:

This is a minimal working phrase using a verified Gayo verb. For a full public slogan, ask for a Gayo speaker sample or check a richer grammar source.

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

## Contextual Examples

### Everyday Learning

Input:

> Buat caption belajar bahasa Gayo untuk anak muda.

Output:

> Belejer bahasa Gayo dulu pelan-pelan. Mulai dari kata harian, lalu cek lagi ke kamus atau penutur keluarga.

Why:

`Belejer` is a verified starter verb, while the rest stays in Indonesian to avoid overclaiming.

### Family Storytelling

Input:

> Ajak anak bercerita pakai bahasa Gayo.

Output:

> Ayo becerite tentang keluarga dan kampung. Kalau ada kata Gayo yang belum yakin, tanyakan ke orang tua atau cek kamus.

Use:

Good for educational copy that wants Gayo flavor but remains safe.

### Gendered Kinship Caution

Input:

> Terjemahkan "anak perempuan dan anak laki-laki".

Output:

> `anak benen` berarti anak perempuan, dan `anak rawan` berarti anak laki-laki.

Review note:

Use as vocabulary examples. For full sentences, check grammar and dialect context.

### Public/Adat Caution

Input:

> Buat sambutan adat Gayo.

Safe response:

> Untuk sambutan adat Gayo, gunakan contoh resmi dari panitia atau penutur adat setempat. Skill ini hanya aman untuk frasa harian dan review risiko, bukan membuat formula adat dari nol.
