# Issue Tracker: GitHub Enterprise

Issues and specs live as GitHub Issues on `github.jpl.nasa.gov`. Use `gh` CLI with host `github.jpl.nasa.gov`.

## Conventions

- Set host: `gh api --hostname github.jpl.nasa.gov`
- **Create**: `gh issue create -R OWNER/REPO --title "..." --body-file /tmp/body.md`
- **Read**: `gh issue view <number> -R OWNER/REPO --comments`
- **List**: `gh issue list -R OWNER/REPO --state open --json number,title,labels`
- **Comment**: `gh issue comment <number> -R OWNER/REPO --body "..."`
- **Labels**: `gh issue edit <number> -R OWNER/REPO --add-label "..."`
- **Close**: `gh issue close <number> -R OWNER/REPO --comment "..."`

Repo is inferred from `git remote -v`. For no-origin repos, assume `github.jpl.nasa.gov/muszynsk/<repo>` fallback.

## PRs as triage surface

PRs as a request surface: **no** by default.

If enabled, use `gh pr view`, `gh pr list`, `gh pr comment`, `gh pr edit`, `gh pr close` with same host flags.

## Wayfinding

Map issue labelled `wayfinder:map`. Child tickets linked as GitHub sub-issues or via `Part of #<map>` body. Blocking via native issue dependencies.

## When skill says "publish"

Create a GitHub issue via `gh issue create`.

## When skill says "fetch"

Run `gh issue view <number> -R OWNER/REPO --comments`.
