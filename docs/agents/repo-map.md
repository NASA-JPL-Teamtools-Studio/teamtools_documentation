# Repo Map

## Overview

The TTS workspace contains 94 independent Git repositories. The authoritative dependency→consumer map is `WORKSPACE_MAP.md` at the workspace root.

This file provides a summary of ownership categories and the capture rule, not a duplicate list.

## Ownership categories

- **public** – `github.com/NASA-JPL-Teamtools-Studio/...`
- **jpl-internal** – `github.jpl.nasa.gov/...`
- **sandbox** – personal forks under `github.jpl.nasa.gov/muszynsk/...`
- **no-origin** – repo exists but has no local `origin` remote; assume `github.jpl.nasa.gov/muszynsk/<repo>` fallback

## Capture rule

In-scope iff:
- name is `tts_[lib]`, or
- name is `[mission]_[lib]` where `tts_[lib]` exists in workspace

Excluded entirely:
- Non-TTS pulls: `mro/mro_sci`, `m20/mech_data_tools`, `work_tracking/resume`
- Non-repo dirs: `venv/`, `tmp/`, `sandboxes/`, `SunRISE/`

## Adapts mapping

Use `WORKSPACE_MAP.md` as source of truth. Example entries:
- `demosat/demosat_seq` → Adapts `tts_core/tts_seq`
- `fss/fss_tower` → Adapts `tts_core/tts_tower`
- `oco2/oco2_tower` → Adapts `tts_core/tts_tower`

Do not duplicate here; reference the workspace map.

## Maintenance

When new missions or libs appear, update `WORKSPACE_MAP.md`. This file is regenerated from that map.
