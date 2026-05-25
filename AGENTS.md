# AGENTS.md

This repository contains portable AI-agent skills for Indonesian writing and regional-language work.

## Working Rules

- Keep every skill offline-first. Do not rely on a live website as the only source of guidance.
- Keep `SKILL.md` concise. Put reusable details in `references/`.
- Every ready skill must have:
  - `SKILL.md`
  - `agents/openai.yaml`
  - `references/offline-brief.md`
  - `references/local-mirror.md`
  - `references/usage-patterns.md`
  - `references/sources.md`
  - `references/examples.md`
- Regional and court-language skills must be source-aware and usable offline. Do not invent vocabulary, ritual language, titles, or cultural formulas.
- For each new regional language, commit and push after the skill validates before starting another language.
- Treat `SKILL.md` as the public/SEO landing document for each skill. Add a `Search And Discovery` section with honest search terms and safety boundaries instead of creating per-skill README files.

## Validation

Run:

```bash
./scripts/validate-skills.sh
```

Do not call a skill ready if validation fails.

## Install Docs

Agent installation docs live in `docs/agent-installation.md`.
