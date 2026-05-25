# Keraton Language Skill Notes

Date: 2026-05-25

## Goal

Add court-register skills to Tutur without pretending that a general-purpose AI can produce fully authoritative palace speech. The skills should support source-aware outputs, stylistic adaptation, and cultural direction.

## Initial Scope

1. `tutur-kedhaton-solo`
   - Target: Keraton Kasunanan Surakarta / Keraton Solo.
   - Register: Basa Kedhaton.
   - Style: more hierarchical, krama-structured, role-sensitive.

2. `tutur-bagongan-jogja`
   - Target: Keraton Kasultanan Yogyakarta / Keraton Jogja.
   - Register: Basa Bagongan.
   - Style: respectful, plainer, more leveling, with the `manira` / `pakenira` pair.

## Source Summary

The main linguistic source is UGM's article on Basa Kedhaton and Basa Bagongan:

https://sastrajawa.fib.ugm.ac.id/seputar-jawa-basa-kedhaton-dan-basa-bagongan-ragam-tutur-khas-keraton-surakarta-dan-yogyakarta/

Key research points:

- Surakarta uses the term Basa Kedhaton.
- Yogyakarta uses the term Basa Bagongan.
- Both are specialized court registers, not just ordinary ngoko/krama.
- Surakarta Kedhaton has role-sensitive pronoun options.
- Yogyakarta Bagongan centers on `manira` / `pakenira` and may mix krama and ngoko morphology.
- Both have limited special vocabulary and need careful handling.

## Recommended Next Courts

1. `tutur-mangkunegaran`
   - Pura Mangkunegaran is a living Surakarta court and cultural institution.
   - Close to Solo context but historically distinct from Kasunanan Surakarta.
   - Source: https://mangkunegaran.id/about-us

2. `tutur-pakualaman`
   - Pura Pakualaman is a living Yogyakarta court/cultural site, distinct from Kasultanan Yogyakarta.
   - Source: https://jogjacagar.jogjaprov.go.id/detail/1084/puro-pakualaman

3. `tutur-cirebon`
   - Covers Cirebon court world: Kasepuhan, Kanoman, Kacirebonan, and Keprabon.
   - This should not be forced into Mataram Solo/Jogja patterns.
   - Source: https://www.indonesia.travel/gb/en/destination/java/west-java/cirebon---kasepuhan-palace/

4. `tutur-sumenep`
   - Useful later for Madurese court style, but it needs separate linguistic research.

## Guardrails

- Do not call generated text "authentic palace language" without verified source text.
- Add a short caveat for ceremony, ritual, royal address, inscription, or publication.
- Keep Solo and Jogja separate.
- Keep Cirebon separate from Mataram-derived court registers.
