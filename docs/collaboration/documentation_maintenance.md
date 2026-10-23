# Documentation Maintenance

This page defines the conventions that make TTS documentation useful to humans and AI agents. It is the central source for Markdown metadata, documentation maturity, progressive traversal, grooming, and context validation.

Repository-specific documentation may add domain rules, but it must preserve this baseline. Mission safety, operational-authority, and domain guardrails remain authoritative over generic documentation workflows.

## Why this exists

TTS documentation is a workspace, not a pile of independent pages. A human or agent should be able to discover the document hierarchy, choose the smallest useful context, follow local references, and identify which claims are stable enough to trust operationally.

The documentation-maintenance contract makes those behaviors explicit and gives tooling a deterministic surface to inspect. It does not replace human judgment about whether content is correct or operationally authoritative.

## Document metadata

Every Markdown document in an in-scope repository has one visible metadata section at the bottom of the file. The section has this shape:

````markdown
## TTS Metadata

```yaml
tts:
  kind: standard
  maturity: baseline
  summary: "The one-sentence purpose of this document."
  audience:
    - agent
    - human
  related:
    - docs/collaboration/testing.md
  policy_ids:
    - documentation.metadata
```
````

The metadata section:

- appears exactly once;
- is the final substantive section of the document;
- uses exactly one fenced `yaml` block;
- remains visible so a human can inspect it in the rendered documentation;
- is ordinary Markdown and does not require a MkDocs plugin;
- uses repository-relative paths for local references; and
- must not be confused with YAML examples elsewhere in the document.

The initial universal fields are:

| Field | Requirement | Meaning |
| --- | --- | --- |
| `kind` | Required | What role the document plays in the documentation corpus. |
| `maturity` | Required | How complete and operationally trusted the document is. |
| `summary` | Required | A concise description of the document's purpose. |
| `audience` | Optional initially | The readers or agents the document serves. |
| `related` | Optional initially | Repository-relative documents that provide useful neighboring context. |
| `policy_ids` | Optional initially | Stable standards or policy rules explained by the document. |

Fields may become required for particular document kinds as the schema evolves. A missing optional field is not equivalent to malformed metadata.

### Document kinds

The initial `kind` vocabulary is:

- `standard` — a normative convention or policy;
- `guide` — procedural or explanatory instruction;
- `reference` — factual material consulted while working;
- `repository` — documentation about a repository or library;
- `glossary` — definitions and terminology;
- `roadmap` — planned or proposed future work; and
- `incidental` — material in scope for inventory but not intended to define a standard.

Repositories may add a more specific kind only through an update to this central convention.

## Documentation maturity

`maturity` is a human-owned lifecycle value. Tooling validates the value and reports contradictions, but never changes it or automatically promotes or demotes a document.

| Maturity | Meaning |
| --- | --- |
| `draft` | Anything goes. The content may be vibe-coded, exploratory, incomplete, or merely scaffolding. It must not be treated as authoritative. |
| `preliminary` | The document is complete enough to be coherent, but remains under active work. |
| `baseline` | The document is close to complete, but active liens may still cause meaningful changes. |
| `released` | The document is operationally trusted and highly stable. Changes remain possible, but should be rare and receive additional review. |
| `retired` | The document is no longer in use and is retained for historical purposes. |

A document may be structurally complete without being operationally trusted. Conversely, a released document may still receive a deterministic finding if its current contents no longer satisfy the published contract.

A document declaring `released` should have:

- valid metadata;
- no blocking deterministic findings; and
- named human or SME review evidence.

Tooling can verify the first two conditions and report the third as declared evidence. It cannot establish operational authority by itself.

Existing warnings such as `Draft — SME review needed` remain part of the document until a human changes them. A tooling report should identify disagreement between a warning and declared maturity rather than deleting or rewriting either one.

## Traversal and context

Documentation tools should support the same progressive reading path a person would use:

1. inspect the document tree;
2. inspect a page outline;
3. choose a heading or section;
4. follow relevant local links; and
5. read the complete document when the question requires it.

The traversal vocabulary is:

- **tree** — the documents available in a selected scope and their hierarchy;
- **outline** — headings and nesting for one document;
- **section** — the content under a selected heading;
- **follow** — resolution of a local Markdown link; 
- **search** — matching text, headings, metadata, and links; and
- **read** — the complete document.

`outline` depth maps directly to Markdown heading levels:

- depth 1 includes `#` headings;
- depth 2 includes `#` and `##` headings; and
- depth 3 includes `#`, `##`, and `###` headings.

Traversal follows relative local Markdown links and reports external links without fetching them. Network access must not be required for deterministic documentation analysis. Results should preserve the source path, heading, section, and anchor information needed to cite the context that was read.

## Standards and policy identifiers

A document may use `policy_ids` to identify the stable standards or policy rules it explains. Document metadata identifies the relationship; it does not replace the explanatory prose.

Markdown remains the human- and agent-facing explanation of a rule. Deterministic tooling may use a separate machine-readable policy projection for thresholds, rule identifiers, and parameters. If the explanation and projection disagree, tooling reports the drift with evidence for human resolution rather than silently rewriting either source.

Policy identifiers should be stable, specific, and reusable across reports. They should identify a rule, not merely repeat a page title.

## Grooming responsibilities

The centralized documentation-grooming skills in `tts_ci_cd` own generic metadata, traversal, link, policy-synchronization, and validation mechanics. They may:

- repair deterministic formatting and schema errors;
- normalize known enum values and repository-relative paths;
- report missing metadata, broken links, and policy drift; and
- propose classifications or relationships for human review.

They must not:

- change a document's maturity;
- certify operational authority;
- erase mission-specific warnings;
- override safety or operational-authority guardrails; or
- fetch external links as part of deterministic analysis.

Central generic conventions override conflicting generic local conventions. Repository and mission documentation may add constraints and domain meaning. Agents must preserve those local safety and authority rules while applying the central documentation contract.

When a repository has pre-existing changes, grooming requires explicit confirmation before modifying the checkout and must make the pre-existing change set distinguishable from generated changes.

## Progressive and exhaustive validation

A documentation corpus should be useful when read progressively, not only when every page is loaded at once. Validation therefore compares two context modes:

- **progressive context** — the tree, outline, selected sections, and links an agent would normally follow; and
- **exhaustive context** — the complete available Markdown corpus for the same scope.

Validation compares:

1. structural facts, which require exact equality;
2. cited evidence, which should overlap when the conclusion is the same; and
3. answers to a versioned question set.

Results are classified as:

- `equivalent` — the contexts support the same conclusion and sufficient evidence;
- `divergent` — the contexts support different conclusions or materially different evidence; or
- `indeterminate` — the comparison cannot establish equivalence reliably.

Generic questions are maintained centrally. Repository-specific question sets may add mission or domain questions. AI-assisted comparison can provide useful evidence, but it is advisory until its behavior is shown to be stable; deterministic structural checks remain the foundation.

## Tooling and CI expectations

The documentation-maintenance contract is designed for both library and CLI use. A future `tts-ctx` implementation should expose the same behavior through a shared analysis interface and produce human-readable Markdown plus versioned machine-readable results.

Report mode should explain findings and next steps without treating every below-target metric as a failure. An explicit strict mode may apply documented thresholds for CI. GitHub Action enforcement should be added only after this contract and its migration workflow have been exercised against central, core, and mission documentation.

The existing MkDocs setup remains the publication path. Metadata is visible fenced Markdown, not front matter, so this convention does not require a front-matter plugin or a change to the existing navigation and theme.

## Related standards

- [Documentation practices](documentation.md)
- [Testing practices](testing.md)
- [CI/CD policies](ci_cd_policy.md)
- [Agent skills and central conventions](../agents/README.md)
- [Design philosophy](../philosophy.md)

---
<a href="https://github.com/NASA-JPL-Teamtools-Studio/teamtools_documentation/blob/main/docs/collaboration/documentation_maintenance.md" target="_blank" rel="noopener noreferrer">Edit/Comment on GitHub</a>

## TTS Metadata

```yaml
tts:
  kind: standard
  maturity: baseline
  summary: "Standards for maintaining TTS Markdown documentation for humans and AI agents."
  audience:
    - agent
    - human
    - reviewer
  related:
    - docs/collaboration/documentation.md
    - docs/collaboration/testing.md
    - docs/collaboration/ci_cd_policy.md
  policy_ids:
    - documentation.metadata
    - documentation.maturity
    - documentation.traversal
    - documentation.context_validation
```
