# Offline Resources

Tutur skills must be useful even when an agent cannot browse the internet.

## Required Files

Every ready skill must include:

```text
SKILL.md
agents/openai.yaml
references/offline-brief.md
references/local-mirror.md
references/usage-patterns.md
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

## local-mirror.md

`local-mirror.md` is the offline mirror of source facts and working language guidance. It should include:

- source identity and stable facts,
- language/register identity,
- what the agent can do without browsing,
- vocabulary and semantic rules,
- generation rules,
- starter lexicon policy or source-backed sample terms.

It must not bulk-copy copyrighted dictionaries, books, articles, or PDFs. Mirror the operational knowledge, not the entire source text.

## usage-patterns.md

`usage-patterns.md` tells agents how to use the skill in real tasks. It should include:

- ordinary output rules,
- sample tasks,
- register and semantic decisions,
- review checklist,
- output patterns for direct generation, review, and public-use text.

## sources.md

`sources.md` stores source links and short source notes. It should still be useful offline by summarizing what each source contributes.

## examples.md

`examples.md` should include realistic requests and safe answer patterns. For low-resource languages, examples may show how to ask for context or avoid false fluency instead of pretending the agent can translate anything.

Every `examples.md` must include `## Target-Language Examples` with actual output in the target language/register. For low-resource languages, this may be a short verified phrase, source-backed vocabulary phrase, or micro-example with a review note.

## Validation

Run:

```bash
./scripts/validate-skills.sh
```

The validation script checks required files and looks for sample sections in `offline-brief.md`, `local-mirror.md`, and `usage-patterns.md`.
