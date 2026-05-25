# Offline Brief

## Local Facts

- Purpose: make Indonesian text sound natural, human, and register-appropriate.
- Default register: natural baku-santai, not stiff, not slang-heavy.
- Official/formal output should follow EYD V, KBBI-aligned diction, and restrained tone.
- Casual/slang output may keep nonstandard words when they match the audience.
- Common Indonesian AI tells include generic openers, inflated significance, vague business claims, English calques, bureaucratic padding, formulaic contrast, and weak summary endings.

## Guardrails

- Preserve facts, names, numbers, claims, and intent.
- Do not invent proof, citations, or new promises.
- Do not make every text formal. Match the requested register.
- Do not remove useful personality just to make the text "correct".
- If the user gives a voice sample, match that sample before applying generic rules.

## Sample Prompts

- "Use $tutur-humanizer to make this caption sound natural."
- "Humanize this proposal but keep it formal."
- "Make this Indonesian landing page copy less AI-sounding."
- "Turn this into a casual WhatsApp message without sounding forced."

## Safe Output Patterns

- Direct rewrite: return the rewritten text first.
- Review: list the main AI tells, then provide a rewrite.
- File edit: update the file and summarize material changes only.
- Unclear register: use natural baku-santai and mention the assumption briefly.

## Local Example

Before:

> Di era digital yang terus berkembang, bisnis membutuhkan solusi inovatif untuk meningkatkan efisiensi operasional.

After:

> Bisnis butuh cara kerja yang lebih rapi, terutama saat operasional mulai tersebar di banyak alat.
