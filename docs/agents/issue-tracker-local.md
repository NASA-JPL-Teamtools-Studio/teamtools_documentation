# Issue Tracker: Local Markdown

Issues and specs live as markdown files under `.scratch/`.

## Conventions

- One feature per directory: `.scratch/<feature-slug>/`
- Spec: `.scratch/<feature-slug>/spec.md`
- Issues: `.scratch/<feature-slug>/issues/<NN>-<slug>.md`, numbered from `01`
- Triage state: `Status:` line at top of each issue file
- Comments append under `## Comments`

## When skill says "publish"

Create file under `.scratch/<feature-slug>/` (create directory if needed).

## When skill says "fetch"

Read the referenced file path.

## Wayfinding

- Map: `.scratch/<effort>/map.md`
- Child: `.scratch/<effort>/issues/NN-<slug>.md` with `Type:` and `Status:` lines
- Blocking: `Blocked by: NN, NN` line
- Frontier: scan for open, unblocked, unclaimed files
- Claim: set `Status: claimed`
- Resolve: append `## Answer`, set `Status: resolved`, update map Decisions-so-far
