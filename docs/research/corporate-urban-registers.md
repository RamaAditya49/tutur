# Corporate And Urban Register Research

Date: 2026-05-26

## Goal

Add profession/corporate and urban Jabodetabek register support without mixing it into regional-language skills. The first delivery is two umbrella skills:

- `tutur-korporat-profesi` for role-aware workplace communication.
- `tutur-jabodetabek-urban` for Jaksel, Jaktim/Jakarta casual, Bekasi, and neutral Jabodetabek styles.

These skills can be split later into narrower skills when there are enough local examples and expert-reviewed resources.

## Research Notes

### Standard And Register Base

- EYD V and KBBI remain the baseline for spelling, standard Indonesian, and formal diction.
- The KBBI concept of `ragam bahasa` supports treating style as context-dependent: topic, speaker relationship, channel, and situation change the language choices.
- Plain-language guidance supports business writing that is easy to understand and act on. This maps well to Indonesian corporate messages: context, action, owner, deadline, and next step.

### Corporate Profession Registers

- Sales language should separate soft selling, follow-up, objection handling, and closing. The local rule is: listen first, acknowledge the concern, clarify the need, then offer the next step without fake urgency.
- Customer service language needs concrete empathy, a specific action, and a time-bound update. Avoid repeated apology without resolution.
- Admin and operations language should be short, task-first, and precise about documents, owner, deadline, and confirmation path.
- HRD/recruitment language should be respectful, concise, and policy-aware. It must not invent salary, offer terms, rejection reasons, or legal commitments.
- Finance and billing language should include amount, invoice/date, confirmation path, and escalation only when policy supports it.
- Marketing and leadership messages should prefer specific benefits, decision points, risks, owners, and deadlines over empty corporate jargon.

### Urban Jabodetabek Registers

- Jaksel style is best treated as Indonesian-English code-mixing, not as an English sentence with Indonesian particles. Sources describe word, phrase, and clause insertions, often spread through social media and peer identity.
- Jaktim/Jakarta casual is a pragmatic urban style: direct, conversational, `gue/lo` friendly, with light Jakarta particles when the relationship supports it.
- Bekasi style should not become a location joke. The safe register is commuter-pragmatic, casual, and close to wider Jakarta-area youth speech while acknowledging local variation.
- Neutral Jabodetabek works as the fallback for captions, chats, and brand copy that need urban casual Indonesian without strong area marking.

## Decisions

- Keep `tutur-korporat-profesi` as the first corporate skill because sales, CS, admin, HRD, finance, marketing, and leadership share enough channel/register rules.
- Keep `tutur-jabodetabek-urban` as the first urban sociolect skill because Jaksel/Jaktim/Bekasi styles are social labels, not fixed dialect promises.
- Add guardrails in both skills: no invented policy/price/SLAs for corporate work; no class, ethnic, or area stereotypes for urban style work.
- Put examples in each skill's `references/examples.md` so offline agents can generate actual sample language without browsing.

## Sources

- EYD V: https://ejaan.kemdikbud.go.id/
- KBBI Daring: https://kbbi.kemdikbud.go.id/
- KBBI `ragam bahasa`: https://kbbi.web.id/ragam
- U.S. SBA plain language: https://www.sba.gov/about-sba/open-government/information-quality/plain-language
- Mekari Qontak on soft selling and hard selling: https://qontak.com/blog/soft-selling-dan-hard-selling/
- SellingPro on follow-up and soft closing: https://sellingpro.co.id/teknik-follow-up-yang-efektif-untuk-menutup-penjualan/
- Hadirr on objection handling: https://www.hadirr.com/kamus-sales/objection-handling
- BFI Finance on complaint handling: https://www.bfi.co.id/en/blog/10-cara-mengatasi-komplain-pelanggan-dengan-efektif
- PhinCon on customer complaint handling: https://phincon.com/articles/keluhan-pelanggan/
- Workable on candidate rejection communication: https://resources.workable.com/tutorial/rejecting-candidates
- Indeed on candidate rejection messages: https://www.indeed.com/hire/c/info/how-to-write-a-candidate-rejection-email
- Tamaddun article on Bahasa Gaul Jaksel: https://ejournal.ahs-edu.org/index.php/tamaddun/article/view/326
- Basadya article on Indonesian-English code-mixing in Gen Z social media speech: https://sihojurnal.com/index.php/basadya/article/view/1365
- UI Library entry on Campur Kode Bahasa Anak Jaksel di Twitter: https://lib.ui.ac.id/detail?id=9999920528097&lokasi=lokal
- Dialect contact and koineization in Jakarta, Indonesia: https://www.sciencedirect.com/science/article/abs/pii/S0388000198000138
- Variasi Fonologis pada Bahasa Melayu Dialek Betawi di Kota Bekasi: https://attractivejournal.com/index.php/aj/article/view/979
- Peran Budaya Populer terhadap Penggunaan Bahasa Gaul oleh Remaja Kota Bekasi: https://repository.ub.ac.id/id/eprint/218098/

