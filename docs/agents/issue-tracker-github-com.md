# Issue Tracker: GitHub.com

Issues and specs live as GitHub Issues on `github.com`. Use standard `gh` CLI.

## Conventions

- **Create**: `gh issue create -R OWNER/REPO --title "..." --body-file /tmp/body.md`
- **Read**: `gh issue view <number> -R OWNER/REPO --comments`
- **List**: `gh issue list -R OWNER/REPO --state open --json number,title,labels`
- **Comment**: `gh issue comment <number> -R OWNER/REPO --body "..."`
- **Labels**: `gh issue edit <number> -R OWNER/REPO --add-label "..."`
- **Close**: `gh issue close <number> -R OWNER/REPO --comment "..."`

Repo is inferred from `git remote -v`.

## PRs as triage surface

PRs as a request surface: **no** by default.

If enabled, use `gh pr view/list/comment/edit/close` equivalents.

## Wayfinding

Map issue labelled `wayfinder:map`. Child tickets as sub-issues or via `Part of #<map>` body. Blocking via native issue dependencies.

## When skill says "publish"

Create a GitHub issue via `gh issue create`.

## When skill says "fetch"

Run `gh issue view <number> -R OWNER/REPO --comments`.
