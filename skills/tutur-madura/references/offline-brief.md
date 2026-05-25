# Offline Brief

## Local Facts

- Purpose: support source-aware generation and review for Bahasa Madura.
- Region/context: Pulau Madura, Tapal Kuda Jawa Timur, Bawean, and Madurese diaspora.
- ISO 639-3: `mad`.
- Common Glottolog reference: `nucl1460`.
- Source confidence: Level 2 because public dictionary, grammar, and Peta Bahasa references exist.
- Bahasa Madura is not a dialect of Bahasa Jawa.

## Guardrails

- Do not import Javanese krama forms as if they were Madurese.
- Do not assume one Madurese dialect represents all speakers.
- Ask whether the target is everyday, polite, Sumenep-style, Tapal Kuda/Pendalungan, Bawean, or another local context.
- Do not use casual forms for elders, formal events, religious/cultural settings, or public notices unless requested.
- For public, ritual, legal, educational, or official use, recommend native-speaker review.

## Sample Prompts

- "Use $tutur-madura to review this Bahasa Madura output."
- "Check if this sounds like Madura or Indonesian/Javanese with replaced words."
- "Make this public notice more appropriate for a Madurese audience."

## Safe Output Patterns

- Ask target region when the text is public.
- For review, flag Javanese/Indonesian interference.
- For Tapal Kuda/Pendalungan, clarify whether the user wants Madurese, Indonesian with Madurese flavor, or mixed local speech.

## Local Example

Request:

> Tolong ubah ke bahasa Madura.

Safe response shape:

> Tanyakan konteks dulu: teman sebaya, orang tua, pengumuman, acara resmi, atau komunitas Tapal Kuda. Pilih tingkat kesopanan setelah target jelas.
