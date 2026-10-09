# Agent Orientation — Teamtools Studio

> **First step:** Run `tts-ctx start_here` to get the workspace overview,
> repo map, and navigation suggestions before doing anything else.

If the index doesn't exist yet:
```bash
tts-ctx index   # builds .ttsctx_index.sqlite3 + CSV dumps
tts-ctx start_here
```

## What this workspace is

The TTS workspace at `/Users/muszynsk/projects/tt_studio/dev/` contains ~90
independent Git repositories. The root is **not** a Git repo; each subdirectory
is its own repo with its own remote, branch, and CI.

- **`tts_core/`** — ~24 shared infrastructure libraries (`tts_utilities`,
  `tts_data_utils`, `tts_html_utils`, `tts_tower`, etc.)
- **Mission groups** — `demosat/`, `oco2/`, `fss/`, `nisar/`, etc. Each contains
  adaptation repos (e.g. `demosat_data_utils`, `oco2_tower`) that subclass TTS core
  classes for a specific mission.

## tts-ctx commands

| Command | Purpose |
|---|---|
| `tts-ctx index` | Rebuild the symbol index (run nightly or after major changes) |
| `tts-ctx start_here` | Bootstrap: workspace overview + navigation menu |
| `tts-ctx core` | List all `tts_core/*` libraries with key classes |
| `tts-ctx adaptations` | List all mission adaptation repos and their core targets |
| `tts-ctx concepts` | Key abstractions (TtsDataFrame, PowerTable, BaseSemanticDictionary, …) |
| `tts-ctx class <dotted.path> [--depth 1\|2\|3]` | Show a class's MRO, methods, and progressive source |
| `tts-ctx repo <repo-name>` | Key classes, modules, and dependencies for one repo |
| `tts-ctx search <query>` | Fuzzy search across all symbols |

Every command output ends with a **fixed suggestion block** — pick from those
options rather than inventing your own grep/read calls.

## Workspace conventions

- **Python floor**: 3.6.8+ — avoid 3.9+ syntax
- **Imports**: Fully-qualified (`from tts_data_utils.core.data_frame import TtsDataFrame`),
  no relative imports
- **Testing**: `src/` tree is mirrored in `tests/`; `inspection`-marked tests
  require human-certified `.sha256` sidecar files (run `certify.py`)
- **AGit remotes**: Public repos use `github.com/NASA-JPL-Teamtools-Studio`;
  internal use `github.jpl.nasa.gov`; personal forks use
  `github.jpl.nasa.gov/muszynsk`

## Repository-specific context

Each repo has:
- `AGENTS.md` — agent orientation (see this file's conventions)
- `CONTEXT.md` — repo-specific domain language (read this for domain context)
- `docs/agents/README.md` — thin pointer file (issue tracker, Adapts, ownership)
