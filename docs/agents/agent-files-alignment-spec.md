# Spec: Align Agent Files Across the TTS Workspace

> **Status:** Draft (session deliverable, doc-only — alignment is *not* executed in this session)
> **Canonical tracked spec:** https://github.com/NASA-JPL-Teamtools-Studio/teamtools_documentation/issues/63
>
> This file is the **living detail / phased work breakdown** (Phases 0–5); the issue
> above is the canonical, reviewable spec. Keep them in sync.
> **Owner:** Teamtools Studio developer tooling
> **Last decided:** See §3 Decisions.
> **Follows from:** `setup-matt-pocock-skills` skill (`~/.agents/skills/setup-matt-pocock-skills`), ADR `tts_core/tts_ci_cd/docs/adr/001-ai-skill-infrastructure.md`.

## 1. Goal

Each engineering skill (`to-tickets`, `triage`, `to-spec`, `wayfinder`, `git_hygiene`, …) needs a repo to answer three questions:
1. **Where do issues live?** (issue tracker + `gh` host/flags)
2. **What does this repo *mean*?** (domain context; what it adapts upstream)
3. **What are the conventions?** (triage labels, ADR reading rules, skill onboarding)

Today that config is **duplicated per repo** as `docs/agents/{issue-tracker,domain,triage-labels}.md` + a `## Agent skills` block in each repo's `AGENTS.md`/`CLAUDE.md`. That drift is unmanageable across **94 repos**.

**This spec** replaces 90 near-identical copies with: one set of **central convention docs** in `teamtools_documentation`, and a **thin pointer file** (`docs/agents/README.md`) in every repo that only carries *per-repo instance data*.

## 2. Current state (verified)

| | Count | Repos (examples) |
|---|---|---|
| Fully configured (full per-repo `docs/agents/` + `## Agent skills` block) | 4 | `oco2/oco2_tower`, `oxus/oxus_telemetry_store`, `tts_core/tts_data_utils`, `tts_core/tts_tower` |
| Empty placeholder `docs/agents/` | 1 | `tts_core/teamtools_documentation` |
| Has `AGENTS.md`/`CLAUSE.md` but **no** agent-skills block | 6 | `demosat/demosat_documentation`, `fss/fss_documentation`, `oco2/oco2_documentation`, `tts_core/tts_ci_cd`, `work_tracking/porkchop`, `work_tracking/resume` |
| Nothing yet | 83 | all the rest |
| Total git repos in workspace | **94** | |

Ownership is mixed but follows a naming invariant (see §5): canonical orgs on `github.com` (`NASA-JPL-Teamtools-Studio`, `NASA-JPL-TTS-Demosat`), mature-but-internal orgs on `github.jpl.nasa.gov`, personal sandbox forks under `muszynsk` on JPL GHE, and 6 repos with **no `origin` locally** (`demosat_dtat`, `oco3/{oco3_dict,oco3_dictionary_interface}`, `oxus/{oxus_dict,oxus_dtat,oxus_events}`) that nevertheless exist on `github.jpl.nasa.gov`.

## 3. Decisions

- **D1 — Centralize, don't replicate.** Conventions live once in `teamtools_documentation`; each repo holds only a pointer + its instance data. *(Replaces the idea of running `setup-matt-pocock-skills` in all 94 repos.)*
- **D2 — Convert the 4 done repos.** Fold their per-repo `docs/agents/*` into the central doc set and replace with the thin pointer, for uniformity.
- **D3 — Pointer file = `docs/agents/README.md`** in each repo. (Matches the `docs/agents/` location `setup-matt-pocock-skills` already looks for, and doesn't clobber existing `AGENTS.md`/`CLAUDE.md`.)
- **D4 — Central doc set** holds: skill onboarding + triage vocabulary, the repo+mission map, the dependency→consumer (`Adapts …`) map **(reused from `WORKSPACE_MAP.md`, not duplicated)**, shared *deterministic* domain glossary, issue-tracker templates (GitHub Enterprise / `github.com` / local-markdown), and a root-`AGENTS.md` replacement for this workspace.
- **D5 — Per-repo pointer carries exactly 5 instance fields** (see §4): issue tracker, upstream `Adapts:` target, triage-label overrides, link to the repo's own `CONTEXT.md` (repo-specific domain language), and an ownership-category tag.
- **D6 — Capture rule (hard constraint).** A repo is in-scope iff its name matches `tts_[lib]` *or* `[mission]_[lib]` where `[lib]` is a libname that **also exists as `tts_[lib]`**. Non-TTS pulls (`mro_sci`, `mech_data_tools`, `work_tracking/resume`, `venvs`, `sandboxes`, `tmp`, …) are **ephemeral and never referenced** by the pointer program or the central map.
- **D7 — No origin? Assume `muszynsk` on JPL GHE; create the remote if it does not exist.** (Future automation / human step — see §7.)
- **D8 — Doc-only this session.** This spec is the deliverable; the alignment itself ships as future tickets (§6).

## 4. The per-repo pointer file: `docs/agents/README.md`

Tiny, structured, machine-ish. Fields:

```markdown
# Agent skills

Canonical engineering-skill conventions and the cross-repo dependency map live in
`tts_core/teamtools_documentation/docs/agents/`. This repo holds only the
per-repo instance data a skill needs locally.

- **Issue tracker:** GitHub Issues at `github.jpl.nasa.gov/Oxus-teamtools/oxus_telemetry_store`
  (host `github.jpl.nasa.gov`, `-R Oxus-teamtools/oxus_telemetry_store`).
  *If a skill needs more, see `teamtools_documentation/docs/agents/issue-tracker-github-ghe.md`.*
- **Adapts:** `tts_core/tts_telemetry_store`  ← into the central repo map / WORKSPACE_MAP.md
- **Triage labels:** default vocabulary (see `teamtools_documentation/docs/agents/triage-labels.md`)
- **Domain context:** repo-specific domain language is in this repo's `CONTEXT.md`.
- **Ownership:** sandbox  ← one of: public | jpl-internal | sandbox | no-origin
```

> Concrete example above is from `oxus/oxus_telemetry_store` (its `CONTEXT.md`-level domain language stays local; host/org/labels are instance data). `teamtools_documentation` itself is **source of truth** and carries no self-pointer (or a one-liner saying so).

The 4 legacy repos are converted by (a) folding their specific issue-tracker URL / `Adapts` / label overrides into this template, (b) deleting the now-redundant `docs/agents/{issue-tracker,domain,triage-labels}.md`, (c) dropping the `## Agent skills` block from `AGENTS.md` (the pointer file supersedes it).

## 5. Capture rule (applied)

In-scope pattern: `tts_[lib]` or `[mission]_[lib]` where `tts_[lib]` also exists in this workspace.

- Core `tts_[lib]` libs anchor the set (e.g. `tts_seq` ⇒ `fss_seq`, `nisar_seq`, … are in-scope; `tts_data_utils` ⇒ every `*_data_utils` mission adaptation is in-scope).
- A `[mission]_[lib]` with **no** matching `tts_[lib]` is **out of scope** (e.g. `mro_sci` — "sci" is not a TTS lib).
- **Excluded entirely** (ephemeral, non-TTS, never referenced): `mro/mro_sci`, `m20/mech_data_tools`, `work_tracking/resume`, and anything under `venv/`, `tmp/`, `sandboxes/`, `SunRISE/`.

The exact in-scope list is the **output of a script** run at implementation time (the remote-org + `git remote` + WORKSPACE_MAP cross-check). This spec does not hard-code 90 names — that list drifts; the rule doesn't.

## 6. Implementation steps (ticketable, phased)

Each bullet under a phase = one ticket (or one PR). None executed in this session.

**Phase 0 — Meta (this spec)**
- [ ] `tts_core/teamtools_documentation`: add this spec at `docs/agents/agent-files-alignment-spec.md`.

**Phase 1 — Central doc set**
- [ ] Create `tts_core/teamtools_documentation/docs/agents/` seed set: `README.md` (index), `skill-conventions.md` (onboarding + triage vocab), `repo-map.md` (missions + ownership categories), `domain-glossary.md` (shared deterministic terms), `issue-tracker-github-ghe.md`, `issue-tracker-github-com.md`, `issue-tracker-local.md` (reuse the `setup-matt-pocock-skills` seed templates as starting points).
- [ ] Assert `WORKSPACE_MAP.md` as the authoritative dependency→consumer map (link, don't copy).

**Phase 2 — Pointer injector (the script)**
- [ ] `tts_core/tts_ci_cd` (or `tts_genai_utils`): add `tts-write-agent-pointer` command. Behavior:
  - enumerate in-scope repos per §5 (name pattern + `tts_[lib]` existence);
  - for each: resolve issue tracker from `git remote -v` (fallback `github.jpl.nasa.gov/muszynsk/<repo>` + `gh` lookup when no `origin`), `Adapts:` target from `WORKSPACE_MAP.md`, ownership category from remote org;
  - write `docs/agents/README.md` (template §4); convert the 4 legacy repos (fold + delete + drop `## Agent skills` block);
  - idempotent: re-running updates, doesn't duplicate.
- [ ] Wire it so `setup-matt-pocock-skills` (or this command) is the documented path to onboard a new/existing repo.

**Phase 3 — Workspace root `AGENTS.md` upgrade**
- [ ] Append an "Agent skills" section to the workspace-root `AGENTS.md` pointing to `teamtools_documentation/docs/agents/` + the capture rule, **correcting** the stale top-level directory list (missing `eurc`, `fss`, `m20`, `oco3`, `oxus`, `srl`, `SunRISE`, `work_tracking`; `tts_ci_cd` is under `tts_core/`).

**Phase 4 — 6 no-origin repos** *(depends: gh API access / human)*
- [ ] For `demosat_dtat`, `oco3_dict`, `oco3_dictionary_interface`, `oxus_dict`, `oxus_dtat`, `oxus_events`: set `origin` to `git@github.jpl.nasa.gov:muszynsk/<repo>.git`; create the remote on JPL GHE if it does not exist. The pointer file notes the `gh` lookup fallback in the meantime.

**Phase 5 — Verify**
- [ ] Spot-check agent skill runs (`to-tickets`, `wayfinder`) in 2 core + 2 mission repos using only the pointer file.
- [ ] Confirm the 4 legacy conversions didn't lose their specific tracker/upstream config.

## 7. Future / open

- **`make the remote` step (§6-Phase 4):** creating a GitHub remote on JPL GHE is not a local-filesystem op — needs `gh` API or a human. Tracked as a ticket; do not block the pointer rollout (the `gh`-lookup fallback covers it).
- **Domain glossary:** lazy. Don't backfill shared terms now; `/domain-modeling` (`/grill-with-docs`) creates them as conflicts/gaps surface (per the `setup-matt-pocock-skills` `domain.md` seed: "proceed silently" if `CONTEXT.md` is absent).
- **Symlink alternative:** rejected — fragile across `gh`/CI workflows; a real file is more robust.
- **`setup-matt-pocock-skills` itself:** becomes the *human-in-the-loop* onboarding skill; the pointer injector is the *bulk* path. Keep both.

## 8. Non-goals (this session)

- No `git remote` changes to the 6 no-origin repos.
- No `docs/agents/README.md` written into any repo.
- No `AGENTS.md`/`CLAUDE.md` edits beyond this spec doc.
- No execution of `setup-matt-pocock-skills` or the pointer injector.
