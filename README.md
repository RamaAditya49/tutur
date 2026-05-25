# Tutur

Tutur is a public skill collection for Indonesian writing.

The first skill is `tutur-humanizer`: a humanizer for Indonesian text that can handle official/formal Indonesian, KBBI-aligned word choice, professional copy, and casual/slang-heavy writing without flattening every voice into stiff textbook language.

## Skills

| Skill | Status | Purpose |
| --- | --- | --- |
| `tutur-humanizer` | Ready | Rewrite or review Indonesian text so it sounds natural, human, and register-appropriate. |
| `tutur-kedhaton-solo` | Ready | Draft or adapt text with a cautious Keraton Solo/Surakarta Kedhaton register. |
| `tutur-bagongan-jogja` | Ready | Draft or adapt text with a cautious Keraton Jogja/Yogyakarta Bagongan register. |
| `tutur-aceh` | Ready | Draft or review Bahasa Aceh with a cautious source-backed workflow. |
| `tutur-gayo` | Ready | Draft or review Bahasa Gayo with a cautious source-backed workflow. |
| `tutur-minangkabau` | Ready | Draft or review Bahasa Minangkabau with a cautious source-backed workflow. |

Planned skills:

- `tutur-resmi`
- `tutur-gaul`
- `tutur-profesional`
- `tutur-salesman`
- `tutur-mangkunegaran`
- `tutur-pakualaman`
- `tutur-cirebon`

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
    ├── tutur-kedhaton-solo/
    └── tutur-bagongan-jogja/
    └── tutur-aceh/
    └── tutur-gayo/
    └── tutur-minangkabau/
```

## Install

Copy the skill folder into your Codex skills directory:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/tutur-humanizer "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/tutur-kedhaton-solo "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/tutur-bagongan-jogja "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/tutur-aceh "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/tutur-gayo "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/tutur-minangkabau "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Then invoke it with:

```text
Use $tutur-humanizer to make this Indonesian text sound natural.
Use $tutur-kedhaton-solo to adapt this text into Keraton Solo style.
Use $tutur-bagongan-jogja to adapt this text into Keraton Jogja style.
Use $tutur-aceh to review this Bahasa Aceh draft.
Use $tutur-gayo to review this Bahasa Gayo draft.
Use $tutur-minangkabau to review this Bahasa Minangkabau draft.
```

## Research Base

The skill uses these references as its editorial base:

- EYD V: https://ejaan.kemdikbud.go.id/
- KBBI Daring: https://kbbi.kemdikbud.go.id/
- KBBI Petunjuk Pemakaian: https://kbbi.kemendikdasmen.go.id/Content/Files/Petunjuk%20Pemakaian.PDF
- Pedoman Umum Pembentukan Istilah: https://badanbahasa.kemendikdasmen.go.id/resource/doc/files/Pedoman_Umum_Pembentukan_Istilah_PBN_0.pdf
- UGM Basa Kedhaton and Basa Bagongan notes: https://sastrajawa.fib.ugm.ac.id/seputar-jawa-basa-kedhaton-dan-basa-bagongan-ragam-tutur-khas-keraton-surakarta-dan-yogyakarta/

## Validate

```bash
./scripts/validate-skills.sh
```

## License

MIT
