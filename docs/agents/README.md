# Agent Skills – Central Conventions

This directory holds the canonical TTS-wide conventions for engineering skills (`to-tickets`, `triage`, `to-spec`, `wayfinder`, `git_hygiene`, `code-review`, `tdd`, etc.).

Per-repo instance data lives in each repo's `docs/agents/README.md`. This central set is the source of truth; repos only hold a thin pointer.

## Contents

- `skill-conventions.md` – Onboarding guidance and triage label vocabulary
- `repo-map.md` – Mission repos, ownership categories, and `Adapts:` mapping
- `domain-glossary.md` – Shared deterministic domain terms
- `issue-tracker-github-ghe.md` – GitHub Enterprise `github.jpl.nasa.gov` conventions
- `issue-tracker-github-com.md` – GitHub.com conventions
- `issue-tracker-local.md` – Local markdown `.scratch/` conventions

## Authoritative maps

Dependency → consumer mapping is maintained in the workspace root `WORKSPACE_MAP.md`:
`/Users/muszynsk/projects/tt_studio/dev/WORKSPACE_MAP.md`

Do not duplicate that map here; link to it.

## Capture rule

A repo is in-scope iff its name is `tts_[lib]` or `[mission]_[lib]` where a matching `tts_[lib]` exists in the workspace. Non-TTS pulls and ephemeral dirs are excluded.

See parent spec: https://github.com/NASA-JPL-Teamtools-Studio/teamtools_documentation/issues/63
