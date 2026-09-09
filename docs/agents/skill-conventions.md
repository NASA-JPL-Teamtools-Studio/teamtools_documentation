# Skill Conventions

## Onboarding

Every in-scope repo must contain `docs/agents/README.md` with the 5-field pointer:
1. Issue tracker – URL + `gh` host/`-R` flags
2. `Adapts:` target – core `tts_[lib]` this mission lib extends
3. Triage-label overrides – defaults to central vocabulary unless diverges
4. Domain context link – pointer to repo's own `CONTEXT.md`
5. Ownership category – `public` / `jpl-internal` / `sandbox` / `no-origin`

The pointer file supersedes any `## Agent skills` block in `AGENTS.md`/`CLAUDE.md`.

## Triage label vocabulary

Canonical roles:
- `needs-triage` – Maintainer needs to evaluate
- `needs-info` – Waiting on reporter
- `ready-for-agent` – Fully specified, AFK agent ready
- `ready-for-human` – Requires human implementation
- `wontfix` – Will not be actioned

See `repo-map.md` for per-repo overrides.

## Issue tracker selection

- GitHub Enterprise: `github.jpl.nasa.gov` → `issue-tracker-github-ghe.md`
- GitHub.com: `github.com` → `issue-tracker-github-com.md`
- Local markdown: `.scratch/` → `issue-tracker-local.md`

## ADR reading rules

Read `CONTEXT.md` / `CONTEXT-MAP.md` and `docs/adr/` before exploring. Proceed silently if missing; `/domain-modeling` creates them lazily.

## Skill pointers

- `/to-tickets` reads `docs/agents/README.md` for host + `-R`
- `/triage` reads triage vocabulary, defaults unless overridden
- `/wayfinder` follows `Adapts:` mapping from `WORKSPACE_MAP.md`
- `/domain-modeling` follows Domain context link to `CONTEXT.md`

## Maintenance

Update this file when conventions change. Do not edit per-repo pointers for convention changes; update central docs only.
