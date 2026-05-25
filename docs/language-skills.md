# Language Skills

This document gives agentic tools a compact index of Tutur's current language and register coverage. The detailed working material remains inside each skill's `references/` folder.

## Register Skills

| Skill | Use for | Local context |
| --- | --- | --- |
| `tutur-humanizer` | Natural Indonesian rewriting across formal, professional, casual, gaul, and sales-adjacent contexts. | AI-phrase scanner, Indonesian writing patterns, KBBI/EYD/PUPI references. |
| `tutur-korporat-profesi` | Sales, CS, admin, HRD, finance, marketing, leadership, internal chat, and WhatsApp business. | Role map, channel guidance, corporate code-mix rules, contextual examples. |
| `tutur-jabodetabek-urban` | Jaksel, Jaktim/Jakarta casual, Bekasi, and neutral Jabodetabek urban styles. | Code-mix guardrails, anti-stereotype notes, local style examples. |

## Court Register Skills

| Skill | Use for | Local context |
| --- | --- | --- |
| `tutur-kedhaton-solo` | Source-aware Keraton Solo/Surakarta Kedhaton-style output and review. | Court-register guardrails, lexicon notes, ceremonial caution. |
| `tutur-bagongan-jogja` | Source-aware Keraton Jogja/Yogyakarta Bagongan-style output and review. | Bagongan register notes, lexicon notes, ceremonial caution. |

## Regional Language Skills

| Skill | Everyday | Formal/public | Adat/ceremony | Key caution |
| --- | --- | --- | --- | --- |
| `tutur-aceh` | Short ordinary Acehnese phrases when covered by KBDA/source notes. | Use restrained source-backed wording. | Review required for ritual, religious, legal, or adat formulas. | Do not apply address terms such as `abu` or `ado` generically. |
| `tutur-gayo` | Short Gayo vocabulary-backed messages. | Use Indonesian baseline plus verified Gayo phrases. | Review required for community/adat wording. | Ask target area when the Gayo community context matters. |
| `tutur-minangkabau` | Everyday Minang community copy. | Public copy can use simple reviewed patterns. | Review required for adat, title, kinship, and ceremonial text. | Do not improvise adat formulas. |
| `tutur-sunda` | Loma/everyday or polite variants when level is known. | Use polite/public wording for schools, institutions, and elder-facing texts. | Review required for ceremonial/local dialect use. | Speech-level consistency matters more than isolated word choice. |
| `tutur-jawa` | Ngoko/everyday or krama variants when level is known. | Use krama/public style for elder-facing or formal use. | Review required for court, ritual, inscription, or high-register text. | Do not mix ngoko and krama randomly. |
| `tutur-madura` | Short community/everyday Madurese copy. | Ask region and politeness target before public use. | Review required for ceremony or high-politeness contexts. | Account for Sumenep, Bawean, Bangkalan, Pamekasan, Sampang, and Tapal Kuda variation. |
| `tutur-bali` | Everyday greetings and community copy. | Use careful public wording with anggah-ungguh awareness. | Review required for temple, ritual, adat, and status-sensitive text. | Do not improvise sacred formulas. |
| `tutur-sasak` | Everyday Sasak phrases such as greetings, thanks, and etiquette cues when source-backed. | Use short reviewed phrases plus Indonesian support text for public output. | Review required for adat, ritual, and status-sensitive Sasak halus. | Sasak has dialect and social-level variation; ask target dialect when it matters. |
| `tutur-banjar` | Everyday Banjar phrases such as `ulun`, `pian`, `apa habar?`, and `bujur` when source-backed. | Use Banjar-aware Indonesian with clear public facts. | Review required for adat, religious, wedding, and formal community text. | Ask whether the target is Banjar Kuala, Banjar Hulu, or general Banjar. |
| `tutur-bugis` | Everyday Bugis politeness cues such as `tabe'`, `iye`, `idi'`, and `Basa Ugi` when source-backed. | Use Bugis-aware Indonesian with clear public facts. | Review required for adat, religious, wedding, Lontara/script, and formal community text. | Ask target Bugis area/community before public use. |
| `tutur-makassar` | Everyday Makassar cues such as `tabe'`, `iye'`, and `Basa Mangkasara` when source-backed. | Use Makassar-aware Indonesian with clear public facts. | Review required for adat, religious, wedding, Lontara/script, and formal community text. | Distinguish Bahasa Makassar from Makassar Malay or local Indonesian accent. |

## Agent Loading Rule

For any skill, load:

1. `SKILL.md`
2. `references/offline-brief.md`
3. `references/local-mirror.md`
4. `references/usage-patterns.md`
5. `references/examples.md`
6. `references/style-guide.md` or `references/lexicon.md` when present

If the target use is public, ritual, legal, educational, or official, keep uncertainty visible and recommend competent speaker review.
