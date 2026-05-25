# Full Language Rollout Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Expand Tutur from an initial Indonesian/regional skill set into a broad offline-first skill library for Indonesian languages, urban registers, professional registers, adat-sensitive usage, and everyday/formal/informal variants.

**Architecture:** Each language or register remains a standalone skill under `skills/<skill-name>/` with `SKILL.md`, `agents/openai.yaml`, and local `references/`. The rollout uses one commit and push per completed language or documentation unit, with `docs/language-rollout-queue.md` as the active queue.

**Tech Stack:** Markdown skill folders, JSON manifest, Bash/Python validation scripts, Git/GitHub.

---

### Task 1: Create Rollout Queue

**Files:**
- Create: `docs/language-rollout-queue.md`
- Modify: `docs/regional-language-skill-rollout.md`

- [x] **Step 1: Add queue document**

Create a queue that records the operating rule, coverage model, active skill list, and next languages.

- [x] **Step 2: Link queue from rollout guide**

Add register coverage notes and tell future agents to use the queue as the active tracker.

- [x] **Step 3: Validate docs**

Run: `git diff --check`

- [ ] **Step 4: Commit**

Run:

```bash
git add docs/language-rollout-queue.md docs/regional-language-skill-rollout.md docs/superpowers/plans/2026-05-26-full-language-rollout.md
git commit -m "Add full language rollout queue"
git push origin main
```

### Task 2: Add Sasak Skill

**Files:**
- Create: `skills/tutur-sasak/`
- Modify: `skills/manifest.json`
- Modify: `README.md`
- Modify: `docs/roadmap.md`
- Modify: `docs/language-rollout-queue.md`

- [ ] **Step 1: Research**

Use Peta Bahasa, the Kemendikdasmen Sasak dictionary record, Glottolog/ABVD, and supporting grammar references.

- [ ] **Step 2: Create skill**

Add source-aware Sasak workflow, local mirror, style guide, sources, and contextual examples.

- [ ] **Step 3: Validate**

Run:

```bash
python3 -m py_compile scripts/check-local-resources.py scripts/new-regional-skill.py
python3 -m json.tool skills/manifest.json >/dev/null
./scripts/validate-skills.sh
git diff --check
TUTUR_STATUS_PATTERN="dr""aft|dr""af|cau""tious" rg -ni "$TUTUR_STATUS_PATTERN" .
```

- [ ] **Step 4: Commit**

Run:

```bash
git add README.md docs/roadmap.md docs/language-rollout-queue.md skills/manifest.json skills/tutur-sasak
git commit -m "Add Sasak regional skill"
git push origin main
```

### Task 3: Continue One Language At A Time

**Files:**
- Create: `skills/tutur-<language>/`
- Modify: `skills/manifest.json`
- Modify: `README.md`
- Modify: `docs/roadmap.md`
- Modify: `docs/language-rollout-queue.md`

- [ ] **Step 1: Take the next queue item**

Use the first unfinished item in `docs/language-rollout-queue.md`.

- [ ] **Step 2: Research from source priority**

Use Badan Bahasa/Balai Bahasa/Peta Bahasa/Dapobas first, then Glottolog/ISO and dictionaries/grammar references.

- [ ] **Step 3: Add offline-first skill**

Create `SKILL.md`, `agents/openai.yaml`, and required `references/` files with contextual target-language examples.

- [ ] **Step 4: Validate**

Run the full validation command block from Task 2.

- [ ] **Step 5: Commit and push**

Use `Add <Language> regional skill` as the commit message, then push before starting the next language.
