# Tutur

Tutur is a public, offline-first skill collection for Indonesian writing, professional registers, urban slang, court registers, and Indonesian regional-language work.

The repository is built for AI agents and coding tools that understand the common skill-folder pattern:

```text
skill-name/
├── SKILL.md
├── agents/openai.yaml
└── references/
```

Every skill keeps its main instructions in `SKILL.md` and its reusable local context under `references/`. Agents should not need internet access to understand the intent, risks, examples, source notes, and safe usage of a skill.

## What This Is

Tutur is not a "translate everything confidently" package. Indonesian regional languages, court registers, speech levels, and local dialects need care. Many skills in this repo are intentionally guarded: they help agents avoid fake fluency, ask for source samples when needed, and distinguish normal generation from public, ritual, legal, or official use.

## Skills

| Skill | Status | Offline resources | Purpose |
| --- | --- | --- | --- |
| `tutur-humanizer` | Ready | Yes | Rewrite or review Indonesian text so it sounds natural, human, and register-appropriate. |
| `tutur-korporat-profesi` | Ready | Yes | Produce role-aware Indonesian workplace messages for sales, CS, admin, HRD, ops, finance, marketing, and leadership. |
| `tutur-jabodetabek-urban` | Ready | Yes | Produce or review Jaksel, Jaktim, Bekasi, and neutral Jabodetabek urban styles without stereotyping. |
| `tutur-kedhaton-solo` | Ready | Yes | Produce or adapt text with a source-aware Keraton Solo/Surakarta Kedhaton register. |
| `tutur-bagongan-jogja` | Ready | Yes | Produce or adapt text with a source-aware Keraton Jogja/Yogyakarta Bagongan register. |
| `tutur-aceh` | Ready | Yes | Produce or review Bahasa Aceh with a source-backed workflow. |
| `tutur-gayo` | Ready | Yes | Produce or review Bahasa Gayo with a source-backed workflow. |
| `tutur-minangkabau` | Ready | Yes | Produce or review Bahasa Minangkabau with a source-backed workflow. |
| `tutur-sunda` | Ready | Yes | Produce or review Bahasa Sunda with careful speech-level handling. |
| `tutur-jawa` | Ready | Yes | Produce or review Bahasa Jawa with careful speech-level and dialect handling. |
| `tutur-madura` | Ready | Yes | Produce or review Bahasa Madura with careful speech-level and dialect handling. |
| `tutur-bali` | Ready | Yes | Produce or review Bahasa Bali with careful anggah-ungguh handling. |
| `tutur-sasak` | Ready | Yes | Produce or review Bahasa Sasak with dialect and speech-level caution. |
| `tutur-banjar` | Ready | Yes | Produce or review Bahasa Banjar with Banjar Kuala/Hulu and polite pronoun caution. |

Planned skills:

- `tutur-resmi`
- `tutur-gaul`
- `tutur-sales`
- `tutur-customer-service`
- `tutur-admin`
- `tutur-hrd`
- `tutur-finance-admin`
- `tutur-marketing`
- `tutur-jaksel`
- `tutur-jaktim`
- `tutur-bekasi`
- `tutur-betawi-jakarta`
- `tutur-bugis`
- `tutur-makassar`
- `tutur-batak-toba`
- `tutur-mangkunegaran`
- `tutur-pakualaman`
- `tutur-cirebon`

## Repository Structure

```text
tutur/
├── AGENTS.md
├── README.md
├── LICENSE
├── docs/
│   ├── agent-installation.md
│   ├── offline-resources.md
│   ├── regional-language-skill-rollout.md
│   ├── skill-authoring-standard.md
│   ├── roadmap.md
│   └── research/
├── scripts/
│   ├── check-local-resources.py
│   ├── install-skills.sh
│   ├── new-regional-skill.py
│   └── validate-skills.sh
└── skills/
    ├── manifest.json
    ├── tutur-humanizer/
    │   ├── SKILL.md
    │   ├── agents/openai.yaml
    │   ├── references/
    │   │   ├── offline-brief.md
    │   │   ├── local-mirror.md
    │   │   ├── usage-patterns.md
    │   │   ├── examples.md
    │   │   └── ...
    │   └── scripts/
    ├── tutur-korporat-profesi/
    ├── tutur-jabodetabek-urban/
    ├── tutur-kedhaton-solo/
    ├── tutur-bagongan-jogja/
    ├── tutur-aceh/
    ├── tutur-gayo/
    ├── tutur-minangkabau/
    ├── tutur-sunda/
    ├── tutur-jawa/
    ├── tutur-madura/
    ├── tutur-bali/
    ├── tutur-sasak/
    └── tutur-banjar/
```

## Quick Install

### ClawHub

ClawHub is the recommended public install path for OpenClaw users:

```bash
npx --yes clawhub install tutur-humanizer
npx --yes clawhub install tutur-jawa
npx --yes clawhub install tutur-korporat-profesi
```

Install every published Tutur skill into an OpenClaw-compatible skills directory:

```bash
mkdir -p ~/.openclaw/workspace/skills
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
  tutur-banjar
do
  npx --yes clawhub --workdir ~/.openclaw/workspace --dir skills install "$skill"
done
```

Update installed skills:

```bash
npx --yes clawhub update
```

Inspect before installing:

```bash
npx --yes clawhub inspect tutur-sasak
```

### Git Clone

Clone the repo:

```bash
git clone https://github.com/RamaAditya49/tutur.git
cd tutur
```

Install all skills into Codex-style local skills:

```bash
./scripts/install-skills.sh --agent codex --all
```

Install all skills into an OpenClaw workspace:

```bash
./scripts/install-skills.sh --agent openclaw-workspace --all
```

Install a single skill into any agent-compatible project:

```bash
./scripts/install-skills.sh --target /path/to/project/.agents/skills --skill tutur-humanizer
```

The installer is conservative. It skips existing skills by default. Use `--replace` only when you intentionally want the existing skill moved to a timestamped backup before copying the new one.

## Agent Compatibility

Tutur skills are plain folders. They work best in agents that load `SKILL.md` plus bundled resources.

Agents that need a machine-readable list can read `skills/manifest.json`.

| Agent/tool family | Recommended target |
| --- | --- |
| Codex / OpenAI skill-compatible local agents | `${CODEX_HOME:-$HOME/.codex}/skills` |
| OpenClaw workspace skills | `~/.openclaw/workspace/skills` or `<workspace>/skills` |
| OpenClaw project agent skills | `<workspace>/.agents/skills` |
| Personal AgentSkills | `~/.agents/skills` |
| Claude Code-style project skills | `<project>/.claude/skills` when your setup supports that directory |
| Cursor, Cline, Roo, Windsurf, Kilo Code, Kiro, Trae, Continue, OpenHands-style wrappers | Use the tool's configured skill directory, commonly `<project>/.agents/skills` or a tool-specific `<project>/.<tool>/skills` directory |
| Hermes/OpenHermes/custom agentic runners | Copy `SKILL.md` and `references/` into the runner's local context or skill registry |
| Any generic coding agent | Copy the needed skill folder and instruct the agent to read `SKILL.md` first, then local files under `references/` |

Detailed install notes: [docs/agent-installation.md](docs/agent-installation.md)

Language/register coverage guide: [docs/language-skills.md](docs/language-skills.md)

SEO/discovery standard for published skill pages: [docs/seo-guidelines.md](docs/seo-guidelines.md)

## How Agents Should Use A Skill

1. Match the user request to a skill by name or description.
2. Read `SKILL.md`.
3. Read `references/offline-brief.md`, `references/local-mirror.md`, and `references/usage-patterns.md`.
4. Read any specific referenced file such as `examples.md`, `style-guide.md`, `pattern-bank.md`, or `lexicon.md`.
5. Do the task with source discipline.
6. Do not invent vocabulary, claims, citations, cultural formulas, or ritual language.

Example prompts:

```text
Use $tutur-humanizer to make this Indonesian text sound natural.
Use $tutur-sunda to review this Bahasa Sunda output for politeness level.
Use $tutur-jawa to rewrite this announcement in polite public Bahasa Jawa.
Use $tutur-bali to check whether this temple announcement needs expert review.
Use $tutur-kedhaton-solo to make a source-aware Keraton Solo-style output.
Use $tutur-korporat-profesi to rewrite this HRD rejection email.
Use $tutur-jabodetabek-urban to make this caption sound Jaksel but not forced.
Use $tutur-sasak to review whether this Lombok tourism copy uses safe Sasak phrases.
Use $tutur-banjar to make this WhatsApp reminder sound Banjar-aware but still clear.
```

## Offline Resources

Every ready skill must include:

- `SKILL.md`
- `agents/openai.yaml`
- `references/offline-brief.md`
- `references/local-mirror.md`
- `references/usage-patterns.md`
- `references/sources.md`
- `references/examples.md`

Language/register skills should also include `references/style-guide.md`. Court-register skills should include `references/lexicon.md` when a source-aware starter lexicon is useful.

Offline resource policy: [docs/offline-resources.md](docs/offline-resources.md)

## Validate

Run the full local validation:

```bash
./scripts/validate-skills.sh
```

This checks:

- skill metadata with the skill validator,
- required local resource files,
- basic sample sections in the offline mirror files,
- target-language examples in every `examples.md`,
- the Indonesian AI-phrase scanner smoke test.

## Research Base

Core Indonesian references:

- EYD V: https://ejaan.kemdikbud.go.id/
- KBBI Daring: https://kbbi.kemdikbud.go.id/
- KBBI Petunjuk Pemakaian: https://kbbi.kemendikdasmen.go.id/Content/Files/Petunjuk%20Pemakaian.PDF
- Pedoman Umum Pembentukan Istilah: https://badanbahasa.kemendikdasmen.go.id/resource/doc/files/Pedoman_Umum_Pembentukan_Istilah_PBN_0.pdf

Regional/court references are summarized locally inside each skill under `references/`. Links are still kept in `sources.md`, but agents should not depend on live internet to understand the skill.

## ClawHub Publishing

Maintainers publish from the terminal after local validation and git push. GitHub Actions is not required.

```bash
set -a
. ./.env.local
set +a
npx --yes clawhub login --token "$CLAWHUB_TOKEN" --no-browser
npx --yes clawhub --workdir "$PWD" --dir skills sync --root "$PWD/skills" --dry-run --all --changelog "Tutur skill update" --tags latest
npx --yes clawhub --workdir "$PWD" --dir skills sync --root "$PWD/skills" --all --changelog "Tutur skill update" --tags latest
```

The `.env.local` file is ignored by git. Never commit ClawHub tokens.

## Contributing

Follow [docs/skill-authoring-standard.md](docs/skill-authoring-standard.md). For regional languages, add one language per commit and push after validation.

## License

MIT
