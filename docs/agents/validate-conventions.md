# Validate Agent Conventions

Keeps the agent-files alignment honest.

## Purpose

Rerun validation on one or more repos to ensure:
- `docs/agents/README.md` exists and contains the 5 required fields
- No legacy `docs/agents/{issue-tracker,domain,triage-labels}.md` files remain
- `AGENTS.md` does not contain a duplicate `## Agent skills` block
- Capture rule is respected

## Usage

Run the CLI tool added to `tts_ci_cd`:

```bash
tts-validate-agent-pointers
```

The tool walks the workspace, finds in-scope repos per capture rule, and prints `[OK]` or `[FAIL]` with reasons. Exit code is non-zero if any repo fails.

You can also validate a single repo by running the script with a custom workspace root.

## Integration

This is the skill referenced in issue #69 to prevent agents from drifting conventions. It can be invoked manually or in CI.

## Related

- Central conventions: `docs/agents/README.md`
- Pointer injector: `tts-write-agent-pointer`
- Spec: https://github.com/NASA-JPL-Teamtools-Studio/teamtools_documentation/issues/63
