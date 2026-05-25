# ClawHub Publishing

Tutur skills are published to ClawHub from a local terminal. Do not use GitHub Actions for this repository's ClawHub release path.

## Local Secret

Keep the ClawHub token in `.env.local`:

```bash
CLAWHUB_TOKEN=...
```

`.env.local` is ignored by git. Never paste the token into README, skill files, changelogs, issue comments, or command output.

## Validate First

```bash
python3 -m py_compile scripts/check-local-resources.py scripts/new-regional-skill.py
python3 -m json.tool skills/manifest.json >/dev/null
./scripts/validate-skills.sh
git diff --check
```

## Login

```bash
set -a
. ./.env.local
set +a
npx --yes clawhub@0.17.0 login --token "$CLAWHUB_TOKEN" --no-browser
npx --yes clawhub@0.17.0 whoami
```

## Dry Run

Always pin the workdir and root so ClawHub does not scan sibling repos:

```bash
npx --yes clawhub@0.17.0 \
  --workdir "$PWD" \
  --dir skills \
  sync \
  --root "$PWD/skills" \
  --dry-run \
  --all \
  --changelog "Tutur skill update" \
  --tags latest
```

The dry run should list only `tutur-*` skills.

## Publish

```bash
npx --yes clawhub@0.17.0 \
  --workdir "$PWD" \
  --dir skills \
  sync \
  --root "$PWD/skills" \
  --all \
  --changelog "Tutur skill update" \
  --tags latest
```

Use `clawhub inspect <skill>` after publishing to verify the public registry metadata.

## Per-Skill Publish

If sync is too broad, publish one skill:

```bash
npx --yes clawhub@0.17.0 skill publish "$PWD/skills/tutur-sasak" \
  --slug tutur-sasak \
  --version 0.1.0 \
  --changelog "Add source-aware Sasak skill" \
  --tags latest
```

