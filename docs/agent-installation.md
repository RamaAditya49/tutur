# Agent Installation

Tutur skills are portable skill folders. A compatible agent only needs to discover a directory with `SKILL.md` and the bundled local resources.

## Standard Skill Folder

```text
tutur-sunda/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── offline-brief.md
    ├── local-mirror.md
    ├── usage-patterns.md
    ├── sources.md
    ├── style-guide.md
    └── examples.md
```

Agents should load only the metadata first. When the skill is needed, they should read `SKILL.md`, then `references/offline-brief.md`, `references/local-mirror.md`, `references/usage-patterns.md`, then any specific reference file named by the skill.

Tools that want a machine-readable registry can read:

```text
skills/manifest.json
```

## Installer

Use the repository installer when possible:

```bash
./scripts/install-skills.sh --agent codex --all
./scripts/install-skills.sh --agent openclaw-workspace --all
./scripts/install-skills.sh --target /path/to/project/.agents/skills --skill tutur-humanizer
```

The installer never deletes a skill silently:

- default: skip if the target skill already exists,
- `--replace`: move the existing skill to `.<name>.backup-<timestamp>` and copy the new skill,
- `--mode symlink`: create symlinks instead of copying.

## ClawHub Public Install

OpenClaw users should prefer ClawHub when they want published Tutur skills without cloning the repository.

Install one skill:

```bash
npx --yes clawhub install tutur-humanizer
npx --yes clawhub install tutur-sasak
```

Install into an explicit OpenClaw workspace:

```bash
npx --yes clawhub --workdir "$HOME/.openclaw/workspace" --dir skills install tutur-jawa
```

Install every published Tutur skill:

```bash
mkdir -p "$HOME/.openclaw/workspace/skills"
for skill in \
  tutur-humanizer \
  tutur-korporat-profesi \
  tutur-jabodetabek-urban \
  tutur-kedhaton-solo \
  tutur-bagongan-jogja \
  tutur-aceh \
  tutur-gayo \
  tutur-minangkabau \
  tutur-sunda \
  tutur-jawa \
  tutur-madura \
  tutur-bali \
  tutur-sasak \
  tutur-banjar \
  tutur-bugis \
  tutur-makassar \
  tutur-batak-toba
do
  npx --yes clawhub --workdir "$HOME/.openclaw/workspace" --dir skills install "$skill"
done
```

Update:

```bash
npx --yes clawhub --workdir "$HOME/.openclaw/workspace" --dir skills update
```

Inspect a skill before installing:

```bash
npx --yes clawhub inspect tutur-korporat-profesi
```

## Codex / OpenAI Skill-Compatible Agents

Install to:

```bash
${CODEX_HOME:-$HOME/.codex}/skills
```

Command:

```bash
./scripts/install-skills.sh --agent codex --all
```

Manual:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/tutur-humanizer "${CODEX_HOME:-$HOME/.codex}/skills/"
```

## OpenClaw / GClaw

OpenClaw loads skills from multiple places. Use the one that matches the desired scope.

Recommended workspace install:

```bash
./scripts/install-skills.sh --agent openclaw-workspace --all
```

Typical OpenClaw targets:

```text
~/.openclaw/workspace/skills
<workspace>/skills
<workspace>/.agents/skills
~/.agents/skills
~/.openclaw/skills
```

Use `~/.openclaw/workspace/skills` for the main personal workspace. Use `<workspace>/.agents/skills` when the skill should travel with a project and be visible to project agents.

## Claude Code-Style Skill Directories

Some Claude Code setups and project templates use `.claude/skills`.

Project-local install:

```bash
./scripts/install-skills.sh --target /path/to/project/.claude/skills --all
```

User-local install, if your local setup supports it:

```bash
./scripts/install-skills.sh --target "$HOME/.claude/skills" --all
```

If the runner does not automatically discover `.claude/skills`, pass the specific `SKILL.md`, `references/offline-brief.md`, `references/local-mirror.md`, and `references/usage-patterns.md` into context.

## Cursor, Cline, Roo, Windsurf, Kilo Code, Kiro, Trae, Continue, OpenHands

These tools do not all share one official skill path. Use the configured local skill directory for your wrapper.

Common project-local targets:

```text
<project>/.agents/skills
<project>/.cursor/skills
<project>/.cline/skills
<project>/.roo/skills
<project>/.windsurf/skills
<project>/.kilocode/skills
<project>/.kiro/skills
<project>/.trae/skills
<project>/.continue/skills
<project>/.openhands/skills
```

Example:

```bash
./scripts/install-skills.sh --target /path/to/project/.agents/skills --skill tutur-jawa --skill tutur-sunda
```

## Hermes / OpenHermes / Custom Agentic Runners

Hermes-style model runners often do not have a native skill loader. Use one of these patterns:

1. Copy the skill folder into the runner's local registry if it has one.
2. Add `SKILL.md` plus `references/offline-brief.md`, `references/local-mirror.md`, and `references/usage-patterns.md` to the system or developer context.
3. For a single task, pass this instruction:

```text
Use the local Tutur skill folder. Read SKILL.md first. Then read references/offline-brief.md, references/local-mirror.md, and references/usage-patterns.md. Do not browse the internet unless the user explicitly asks for fresh verification.
```

For small-context models, include only:

- `SKILL.md`
- `references/offline-brief.md`
- `references/local-mirror.md`
- `references/usage-patterns.md`
- `references/examples.md`

For culturally sensitive text, also include:

- `references/style-guide.md`
- `references/lexicon.md` when present

## Generic Agentic Tools

If a tool has no skill convention, copy the skill folder somewhere in the project and mention the path explicitly:

```text
Use ./skills/tutur-humanizer/SKILL.md. Load local references only from ./skills/tutur-humanizer/references/.
```

This works for most coding agents because the skill is just Markdown plus local resources.
