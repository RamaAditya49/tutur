# Skill Authoring Standard

## Principles

- Make each skill portable.
- Keep instructions local and offline-first.
- Keep `SKILL.md` concise enough for agents to load quickly.
- Put detailed reusable context in `references/`.
- Use guardrails when source quality is limited.
- Never let a skill imply native-speaker authority unless the material is expert-reviewed.

## Required Structure

```text
skills/<skill-name>/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── offline-brief.md
    ├── local-mirror.md
    ├── usage-patterns.md
    ├── sources.md
    └── examples.md
```

Optional:

```text
scripts/
assets/
references/style-guide.md
references/lexicon.md
```

## SKILL.md Rules

- Frontmatter must include only `name` and `description`.
- Description must explain what the skill does and when to use it.
- Body should cover workflow, output style, and resource map.
- Body should include a short `Search And Discovery` section for public ClawHub/agent discovery.
- Do not put long dictionaries or long source notes in `SKILL.md`.

## Regional Language Rules

- Add one language per commit.
- Validate and push before starting the next language.
- Prefer official Badan Bahasa, Balai Bahasa, Labbineka, Peta Bahasa, or Glottolog references.
- State source confidence clearly.
- Add dialect and register warnings.
- Include sample prompts, local mirror notes, usage patterns, safe output shapes, and actual target-language examples.

## Court Register Rules

- Keep court-register skills separate from everyday language skills.
- Add caveats for ceremony, ritual, royal address, inscriptions, and public use.
- Do not claim authentic palace language without verified source text.

## Validation Checklist

Before committing:

```bash
./scripts/validate-skills.sh
git diff --check
```

Then commit only the completed language or documentation unit.
