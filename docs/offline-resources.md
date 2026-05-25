# Offline Resources

Tutur skills must be useful even when an agent cannot browse the internet.

## Required Files

Every ready skill must include:

```text
SKILL.md
agents/openai.yaml
references/offline-brief.md
references/sources.md
references/examples.md
```

The repository also keeps a machine-readable skill registry:

```text
skills/manifest.json
```

Regional and court-language skills should also include:

```text
references/style-guide.md
```

Court-register skills may include:

```text
references/lexicon.md
```

## offline-brief.md

`offline-brief.md` is the fallback context for models without internet access. It should include:

- what the skill is for,
- the identity of the language/register,
- source-confidence level,
- local facts that do not require browsing,
- main risks,
- required behavior,
- sample prompts,
- safe output shapes.

It should not copy full copyrighted dictionaries, books, or articles. Use short notes and summaries.

## sources.md

`sources.md` stores source links and short source notes. It should still be useful offline by summarizing what each source contributes.

## examples.md

`examples.md` should include realistic requests and safe answer patterns. For low-resource languages, examples may show how to ask for context or avoid false fluency instead of pretending the agent can translate anything.

## Validation

Run:

```bash
./scripts/validate-skills.sh
```

The validation script checks required files and looks for sample sections in `offline-brief.md`.
