# ADR 001 — Prefer Open Source over SaaS for Developer Tooling

**Status**: Accepted  
**Date**: 2026-08-08  
**Deciders**: TTS Core Team

## Context

TTS is used across JPL missions with varied network and security environments. Developer tooling choices (CI, testing infrastructure, visual regression, reporting) carry long-term risk beyond just technical fit: a vendor can be acquired, discontinue a product, change pricing, or become inaccessible from a secure facility.

This ADR establishes the ecosystem-wide preference for open-source, self-hosted tooling over SaaS solutions for all developer infrastructure.

## Decision

**Prefer open-source, self-hosted, or locally-runnable tooling over SaaS products for all TTS developer infrastructure.**

This applies to:
- Visual regression testing (e.g., Percy vs. Playwright vs. custom hash-based review)
- CI/CD infrastructure (e.g., GitHub Actions vs. hosted CI products)
- Test reporting and dashboards
- Documentation hosting
- Any other tooling that developers depend on to build and validate TTS libraries

When a SaaS alternative exists alongside an open-source option, the open-source option is chosen unless there is a compelling technical reason the SaaS capabilities cannot be replicated locally.

## Rationale

1. **Vendor risk**: A SaaS company can be acquired, discontinue its product, or change pricing at any time. When that happens, every TTS workflow that depends on it breaks simultaneously across all missions.
2. **JPL network constraints**: JPL is a secure facility. Tools that upload data to external servers (screenshots, HTML, source code) require security review and may be prohibited outright. An assumption that any SaaS tool is accessible from all TTS environments is unsafe.
3. **Portability**: TTS libraries are used on small missions with minimal IT infrastructure and on large flagship missions with strict software controls. Self-hosted or local tools work in both environments without configuration differences.
4. **Auditability**: Open-source tools can be inspected, forked, and patched if they contain bugs or security issues. SaaS tools cannot.
5. **Cost predictability**: Open-source tooling has no per-seat or per-run pricing. This removes a variable from the long-term operational cost of the TTS ecosystem.

## Alternatives Considered

### Percy (BrowserStack)
- **What it does**: Captures screenshots of rendered HTML in CI, uploads to BrowserStack's cloud, provides visual pixel-level diffs against an approved baseline.
- **Why rejected**: Requires uploading rendered output to an external cloud service (security risk at JPL), subject to vendor pricing changes (BrowserStack has changed pricing multiple times), requires network access from CI runners, and SaaS continuity is not guaranteed.
- **Note**: JPL may have an enterprise Percy account. This is irrelevant to TTS because individual missions using TTS libraries may not have the same account access, and the vendor risk remains regardless of current availability.

### Playwright screenshot tests
- **What it does**: Open-source browser automation. Can take screenshots locally and compare pixel-by-pixel against stored PNG baselines.
- **Why not chosen**: Requires a Chromium/Firefox browser binary (~300MB) as a CI dependency. Pixel comparison is fragile across OS/CI environments (font hinting, subpixel antialiasing differ). More importantly, `--update-snapshots` can be run by an automated agent without human review — the "human must have looked" guarantee is documentation-only, not structural.

### pytest-snapshot
- **What it does**: Stores output (HTML, text, etc.) as snapshot files. Fails if output differs from stored snapshot. Updated via `--snapshot-update`.
- **Why not chosen**: The `--snapshot-update` flag can be run by an AI agent or a developer without actually reviewing the output. There is no structural forcing function that requires human inspection. Documentation-only constraints get violated in practice.

### Chosen approach: hash-based human certification
- SHA-256 sidecar files (`.sha256`) committed alongside inspection HTML artifacts.
- `certify.py --certify` is the only way to update the hash. It is a separate, explicitly-human-facing script, outside the test runner.
- `certify.py` (no args) generates a status dashboard (`inspection_status.html`) as the human entry point — no magic procedure steps required.
- `check_inspection_hash()` enforces the contract in the test: uncertified or stale artifacts fail the `@pytest.mark.inspection` test.
- Works for HTML, CSV, Excel, and any other byte-stream artifact type.
- No external dependencies, no network access, no browser binary.

## Consequences

- TTS developer tooling will occasionally be less polished than a best-in-class SaaS product.
- The tradeoff is accepted: reliability, security compatibility, and vendor independence matter more than UI polish on internal tooling.
- When an open-source tool does not yet exist for a need, TTS builds a minimal one (as with the inspection certification machinery) rather than adopting a SaaS dependency.
- Future agents and contributors should apply this preference actively. If adding a new CI tool or testing dependency, check: can this be done open-source/locally? If yes, do that.
