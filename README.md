# Tutur

Tutur is a public skill collection for Indonesian writing.

The first skill is `tutur-humanizer`: a humanizer for Indonesian text that can handle official/formal Indonesian, KBBI-aligned word choice, professional copy, and casual/slang-heavy writing without flattening every voice into stiff textbook language.

## Skills

| Skill | Status | Purpose |
| --- | --- | --- |
| `tutur-humanizer` | Ready | Rewrite or review Indonesian text so it sounds natural, human, and register-appropriate. |

Planned skills:

- `tutur-resmi`
- `tutur-gaul`
- `tutur-profesional`
- `tutur-salesman`

## Repository Structure

```text
tutur/
├── docs/
│   ├── research/
│   └── roadmap.md
├── scripts/
│   └── validate-skills.sh
└── skills/
    └── tutur-humanizer/
        ├── SKILL.md
        ├── agents/
        ├── references/
        └── scripts/
```

## Install

Copy the skill folder into your Codex skills directory:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/tutur-humanizer "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Then invoke it with:

```text
Use $tutur-humanizer to make this Indonesian text sound natural.
```

## Research Base

The skill uses these references as its editorial base:

- EYD V: https://ejaan.kemdikbud.go.id/
- KBBI Daring: https://kbbi.kemdikbud.go.id/
- KBBI Petunjuk Pemakaian: https://kbbi.kemendikdasmen.go.id/Content/Files/Petunjuk%20Pemakaian.PDF
- Pedoman Umum Pembentukan Istilah: https://badanbahasa.kemendikdasmen.go.id/resource/doc/files/Pedoman_Umum_Pembentukan_Istilah_PBN_0.pdf

## Validate

```bash
./scripts/validate-skills.sh
```

## License

MIT
