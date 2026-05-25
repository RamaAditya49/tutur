---
name: tutur-humanizer
description: Rewrite, edit, or review Indonesian text so it sounds natural, human, and context-appropriate. Use when the user asks to humanize Indonesian writing, remove AI-sounding phrasing, adapt text to official/formal/KBBI-aligned Indonesian, preserve casual/slang voice, smooth professional copy, or make generated Indonesian less stiff without changing meaning.
---

# Tutur Humanizer

## Overview

Use this skill to make Indonesian writing sound like it came from a real person. Preserve the user's meaning, facts, intent, and voice while removing AI-like filler, awkward translation, over-formality, and forced polish.

Default to clear Indonesian that is natural in writing: mostly baku, not bureaucratic, not slang-heavy. Shift register only when the user asks for a specific target such as resmi, formal, profesional, santai, gaul, or sales.

## Workflow

1. Identify the target register from the request.
   - If unspecified, use natural baku-santai: readable, correct enough for public writing, but not stiff.
   - For official/formal work, follow EYD V, KBBI labels, and standard Indonesian structure.
   - For casual/slang work, keep slang only when it fits the audience and does not blur meaning.

2. Diagnose the text.
   - Remove formulaic AI framing, inflated significance, vague claims, and copied English rhythm.
   - Cut filler before adding style. Human writing is usually more specific, not more decorated.
   - For longer files, optionally run `scripts/scan_ai_id.py` to find repeated phrases and tone risks.

3. Rewrite.
   - Keep the original facts, scope, and point of view.
   - Prefer concrete verbs over abstract nouns.
   - Use shorter sentences when the original stacks too many clauses.
   - Keep useful personality from the source instead of flattening everything into neutral formal Indonesian.

4. Final pass.
   - Check ejaan, punctuation, word choice, and register consistency.
   - Remove remaining stock phrases such as "di era digital", "solusi inovatif", "tidak hanya..., tetapi juga...", and "menjadi kunci".
   - Make sure the output still sounds Indonesian, not English translated word by word.

## Register Rules

- **Resmi/formal:** Use standard Indonesian, EYD V, KBBI-aligned diction, complete sentences, and restrained tone. Avoid slang, chat abbreviations, exaggerated claims, and regional/Jakarta-only vocabulary unless quoted.
- **Profesional:** Use clear business Indonesian without corporate padding. Prefer "kami membantu tim mengelola..." over "kami hadir sebagai solusi inovatif yang komprehensif...".
- **Santai/gaul:** Use conversational rhythm and light slang only when appropriate. Avoid forced slang, meme language, and overuse of "gue/lu" unless the user's voice already uses it.
- **Sales/copy:** Make benefits concrete. Replace hype with proof, context, or a sharper promise.
- **Academic/technical:** Keep terms precise. If terminology is uncertain, prefer established Indonesian terms or leave the source term with a short explanation.

Read `references/register-map.md` when the register decision matters.

## Indonesian AI Tells

Common Indonesian AI tells include:

- Overblown openers: "Di era digital yang terus berkembang...", "Dalam lanskap bisnis modern..."
- Vague importance: "memainkan peran penting", "menjadi kunci", "mendorong transformasi"
- Marketing mush: "solusi inovatif", "pengalaman yang mulus", "komprehensif", "terintegrasi"
- English calques: "menavigasi tantangan", "menghadirkan nilai", "lanskap", "beresonansi"
- Bureaucratic padding: "dalam rangka", "melakukan optimalisasi", "pelaksanaan kegiatan"
- Formulaic contrast: "bukan hanya..., melainkan juga...", "tidak hanya..., tetapi juga..."
- Empty conclusion: "Pada akhirnya", "Dengan demikian" when it adds nothing.

Read `references/pattern-bank.md` for a larger pattern list and replacement principles.

## Output Style

- If the user asks only for a rewrite, return the rewritten text directly.
- If the user asks for review, lead with the issues, then provide a rewrite.
- If editing a file, make the edit and summarize only the material changes.
- Do not invent citations, sources, numbers, names, or proof.
- Do not over-correct slang in casual content. Mark it as a register choice, not automatically an error.
- Do not make Indonesian sound "high" just to look correct. Correct Indonesian can still be simple.

## Resources

- `references/sources.md`: official references used by this skill.
- `references/register-map.md`: register decisions for resmi, formal, profesional, santai, gaul, sales, academic, and technical writing.
- `references/pattern-bank.md`: Indonesian AI-sounding patterns and rewrite principles.
- `references/examples.md`: before/after examples.
- `scripts/scan_ai_id.py`: optional scanner for repeated AI-like phrases and register risks.

## Quick Examples

Input:

> Di era digital yang terus berkembang, bisnis membutuhkan solusi inovatif untuk meningkatkan efisiensi operasional.

Natural professional:

> Bisnis butuh cara kerja yang lebih rapi dan cepat, terutama saat proses operasional mulai tersebar di banyak alat.

Formal:

> Perusahaan memerlukan sistem kerja yang lebih tertata agar proses operasional dapat berjalan lebih efisien.
