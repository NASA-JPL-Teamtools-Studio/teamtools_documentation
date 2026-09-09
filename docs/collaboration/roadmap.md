# Teamtools Studio Roadmap

While all repositories have their own issues pages, and developers can certainly go there to understand work to go, the size and scope of this project demands that there be a more qualitative roadmap. This is that page

## Reasonably feature complete
* This is largely defined by whether the functionality is provided such that the tools are well demonstrated.

## All tests passing and automated
* At least 50% test coverage on all libraries
* All libraries included in tts-ci-cd documentation automation
* All libraries included in tts-ci-cd test matrix

## Well Documented
* At least 50% documentation coverage on all libraries

## Well Demonstrated
* Minimal Jupyter notebook-based demonstrations are provided for all DemoSat libraries
* Minimal Jupyter notebook-based demonstrations are provided select TTS libraries

## Open Sourced
* Code is open sourced

---

## Agent-Written Spec Backlog (slow burn)

Inventory of open, agent-written specs/tickets across `demosat_*` and `tts_core` repos, prioritized for a
one-spec-per-week slow burn (porkchop #90). No dates — this is a queue, not a schedule. Re-derive priority
whenever a new idea shows up and needs to be weighed against what's already queued.

**Ranking rule (settled 2026-08-19)**: an item with an open branch or other unmerged work outranks an item
that only has a `ready-for-agent` ticket with no code behind it yet. Ties/gaps get flagged for discussion
rather than silently ranked.

### Grab next

- **`tts_dictionary_interface` F-Prime chain, starting with `#17`** — see Track 1 below. With the
  `tts_dexter` df-compat branch now moved to a PR (see Housekeeping), this is the top of the queue.

### Track 1 — `tts_dictionary_interface`: F-Prime dictionary support (prioritized track)

Chain, in order: `#17` (XmlDictionary/AmpcsDictionary base, deprecate SemanticDictionary) →
`#18` (shared dictionary-item contract + lazy lookup-order fix) → `#19` (F-Prime JSON dictionary engine) →
`#20` (cross-engine contract-parity test suite, DemoSat fixture). All labeled `ready-for-agent`; none have
an open branch yet. This chain **supersedes** the old DemoSat-roadmap "F-Prime → AMPCS converter" plan
(porkchop #77, closed as superseded) — no downstream consumer needs AMPCS XML output from F-Prime, so the
new plan is a JSON-native engine with a shared contract instead.

Independent, lower-priority items in the same repo:
- `#15` SPEC: Dictionary Packaging Contract and Agent-Context Dictionary CLI — not yet labeled
  `ready-for-agent`; likely needs its own grilling pass before it's queueable.
- `#14` Grill-me: CLI tool for dictionary-aware agents — `ready-for-agent`, unrelated to the F-Prime chain.
- `#6`/`#7` → `#8`, `#11`, `#9`, `#10` — SemanticDictionary node-caching implementation (spec done, split
  into 4 sub-tickets: `#8` core LRU cache, `#11` contains/getattr caching, `#9` lazy `__iter__` population,
  `#10` perf verification). Duplicates `#12`/`#13` closed 2026-08-19.

### Track 2 — DemoSat Evolution (independent of Track 1)

`SPEC_demosat_evolution.md` / `demosat_documentation/roadmap.md` define T1–T9. Confirmed no code-level
coupling to Oxus or to the `tts_dictionary_interface` F-Prime work exists today (checked both repos for
cross-references — none found beyond the roadmap narrative). The only link is that a future DemoSat
Oxus-integration ticket (old T7, not yet filed) would eventually consume Track 1's output — nothing in
either track blocks the other right now.

- `demosat_data_utils#8` — **T1**: migrate to `TtsDataFrame` (`DemosatChannelFrame`, `DemosatCommandFrame`,
  `DemosatSequenceFrame`). Foundational — blocks T2/T3/T4. No open branch. Not started (only `evr.py` exists
  from the already-closed T6).
- `demosat_data_utils#3` — separate legacy migration: `orbit_events.py`, `comm_windows.py`,
  `ground_stations.py`, `ephemeris.py` from `DataContainer`/`DataItem` to `TtsDataFrame`. Independent of T1
  (different modules).
- `demosat_data_utils#7` — T11: `demosat_dtat` starter kit + `DemosatLogExplorer`. Blocked on T6 (done) and
  T9 (`tts_dtat` LogExplorer, not yet filed).
- `demosat_data_utils#6` — T7: deprecation warnings on `EvrContainer`/`EvrItem`. Explicitly deferred by
  prior user request — leave open, don't schedule yet.
- `demosat_data_utils#4` — grill-me: telemetry query layer design (local files + TimescaleDB). Open design
  question feeding T3; needs its own grilling pass before T3 can be scoped.

### Needs review

- **`tts_dtat` downsample/explorer PR chain** — stacked branches, review/merge in order:
  - PR #18 (T1–T4: LTTB primitive, `PlotOrchestrator`, base `main`)
  - PR #23 (T5–T8: interactive zoom re-downsampling, `ChannelExplorer` widget, base = #18's branch)
  - PR #25 (bugfixes: notebook rendering, widget width (#20); LTTB-callback bugs #21/#22 filed but not
    fully fixed; base = #23's branch). **Despite the branch name (`t9-log-explorer`), this PR does not
    implement T9** — T9 (`LogExplorer`, `tts_dtat#19`) is still open and unaddressed.
  - T9 (`tts_dtat#19`) still needs its own implementation + PR once #25 merges.
  Tracked in `tts_dtat#24` and `porkchop#102`.

### Other open `tts_core` work (not yet triaged into a track)

- `tts_data_utils/docs/roadmap.md` item 2 — Visual Diff → `TtsDataFrame` (top open item in that repo's
  internal roadmap; items 1 and 3 are done).
- `.scratch/dict-interface-channel-abc/issues/00-04` — Channel ABC design docs, **not yet filed as GitHub
  issues** anywhere.

### Housekeeping done 2026-08-19

- Closed `demosat_data_utils#5` (T6: `DemosatEvrFrame`) — code already merged to `main`
  (branch `muszynsk/add_evr_frame` had zero diff vs. `main`).
- Closed `tts_dictionary_interface#12`/`#13` as duplicates of `#9`/`#10` (accidental double-submit when the
  caching spec was split into sub-tickets).
- `porkchop#77` (old F-Prime→AMPCS converter ticket) was already closed as superseded by
  `tts_dictionary_interface#16`.
- `tts_dexter` `muszynsk/df_compat` branch (OCO-2 supporting work, DataFrame compat for dispositioners) —
  opened `tts_dexter` PR #6 (129 tests pass, 1 xfailed), filed `tts_dexter#7` for remaining cleanup items
  from `DEV_dexter_dataframe_next_steps.md`, and filed `porkchop#101` to track closing the loop with the
  user once #6 merges.