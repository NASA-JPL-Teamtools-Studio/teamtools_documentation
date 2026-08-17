# Teamtools Studio Roadmap

While all repositories have their own issues pages, and developers can certainly go there to understand work to go, the size and scope of this project demands that there be a more qualitative roadmap. This is that page.

---

## Critical Path: Oxus Launch (6 Months)

**Goal**: Enable Oxus to use the same ingest/query/visualization infrastructure as DemoSat, despite using F-Prime (not AMPCS) ground system.

### T5: ADR — F-Prime Topology in TTS Dictionary Interface

**What**: Write an Architecture Decision Record documenting how F-Prime (component/port model) integrates with TTS dictionary interface alongside AMPCS (flat channel model).

**Decision**: Start with converter approach (F-Prime → AMPCS format). F-Prime ABC is future work.

**Outputs**: ADR in `tts_dictionary_interface/docs/adr/005-fprime-topology-in-tts.md`

**Timeline**: 2026-08-22

**Blocking**: T6 (converter script)

---

### T6: Implement F-Prime → AMPCS Converter

**What**: Create a utility in `tts_dictionary_interface` that converts F-Prime topology (component definitions, port definitions, parameter definitions) to AMPCS-compatible dictionary format.

**Why**: Enables Oxus to use the same ingest/query pipeline as DemoSat without duplicating code.

**Outputs**: 
- `src/tts_dictionary_interface/converters/fprime_to_ampcs.py`
- Tests with Oxus topology examples
- Documentation on F-Prime → AMPCS mapping

**Timeline**: 2026-08-29

**Blocking**: T7 (Oxus integration)

---

### T7: Oxus Integration — Unify Ingest/Query

**What**: Apply F-Prime converter to Oxus topology. Implement `oxus_ingest` and `oxus_query` using the same pattern as DemoSat (CSV + Postgres backends, validates against dictionary).

**Why**: Oxus launch is in 6 months. Reusing DemoSat infrastructure saves time and ensures consistency.

**Inputs**: 
- T6 (F-Prime converter)
- Oxus topology work (in parallel)
- DemoSat ingest/query pattern (T2–T3)

**Outputs**:
- `oxus_ingest` repository
- `oxus_query` repository
- Oxus-specific frame types in `oxus_data_utils`

**Timeline**: 2026-09-30 (must complete before launch)

**Blocking**: Oxus launch readiness

---

## DemoSat Evolution (Foundation for Oxus)

See `demosat_documentation/roadmap.md` for detailed DemoSat roadmap (T1–T9).

**Summary**:
- **T1**: Migrate `demosat_data_utils` to TtsDataFrame
- **T2**: Create `demosat_ingest` (CSV → Postgres)
- **T3**: Create `demosat_query` (dual-backend)
- **T4**: Expand `demosat_dtat` (explorers)
- **T8–T9**: Uplink data and advanced visualization (Phase 3)

---

## TTS Core Roadmap

### Reasonably feature complete
* This is largely defined by whether the functionality is provided such that the tools are well demonstrated.

### All tests passing and automated
* At least 50% test coverage on all libraries
* All libraries included in tts-ci-cd documentation automation
* All libraries included in tts-ci-cd test matrix

### Well Documented
* At least 50% documentation coverage on all libraries

### Well Demonstrated
* Minimal Jupyter notebook-based demonstrations are provided for all DemoSat libraries
* Minimal Jupyter notebook-based demonstrations are provided select TTS libraries

### Open Sourced
* Code is open sourced

---

## Supporting Roadmaps

For detailed roadmaps of specific TTS libraries and mission adaptations, see:

- **`tts_data_utils` roadmap** (`tts_core/tts_data_utils/docs/roadmap.md`) — Core data frame types and ecosystem patterns
  - Item #1: PowerTable → TtsDataFrame (✅ Done)
  - Item #2: Visual Diff → TtsDataFrame (✅ Done)
  - Item #3: AmpcsEha/AmpcsEvr Migration (✅ Done — AmpcsEhaFrame + AmpcsEvrFrame)
  - Item #3b: TtsLogFrame (✅ Done)
  - Item #4: Vectorized Interpolation (Medium priority)
  - Item #5: Lorem Ipsum → TtsDataFrame (Low priority)
  - Item #6: TtsDataNode (Long-term)
  - Item #7: IDM / tts_events Interoperability (Medium priority)
  - Item #8: jpl_time Integration (Low priority)
  - Item #9: Sort-Safe Subcontainers (Low priority)
  - Item #10: Python Version Deprecation (Low priority)

- **`demosat_documentation` roadmap** (`demosat/demosat_documentation/roadmap.md`) — DemoSat evolution and Oxus foundation
  - Phase 1 (T1–T4): DataFrame migration & dual-backend query
  - Phase 2 (T5–T7): F-Prime support & Oxus integration (critical path)
  - Phase 3 (T8–T9): Uplink data & advanced visualization

- **`tts_dictionary_interface` roadmap** (TBD) — Dictionary interface evolution and F-Prime support
  - T5: ADR — F-Prime Topology in TTS (blocks T6)
  - T6: F-Prime → AMPCS Converter (blocks Oxus T7)