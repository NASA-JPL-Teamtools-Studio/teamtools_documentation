# Spec: ROC Briefing Doc Set

**Status:** Draft for review with Tara Estlin
**Author:** Matt Muszynski (with Cascade)
**Date:** 2026-08-20
**Repo:** `teamtools_documentation`
**Target branch:** `mrmuszynski/roc-briefing` (not yet created)
**Target path:** `docs/briefings/roc_2026/`

---

## 1. Purpose

A set of standalone Markdown documents making the case that Teamtools Studio belongs
in the ROC service catalogue. The documents must work in three modes:

1. **Read cold** by someone who was not in the room.
2. **Presented** by Matt in a ~30 minute slot.
3. **Mined** by Matt for a summary PowerPoint, with the doc set as supporting material.

The body of the doc set is deliberately **ROC-agnostic**. A single appendix bolts on the
ROC-specific connections. This keeps the material reusable for other audiences and keeps
the argument from sounding tailored.

## 2. Audience

| Persona | Priority | What they need |
|---|---|---|
| ROC architects | Primary | Does this fit the architecture without adding complexity? |
| Program office | Primary | What does it cost, who sustains it, what do customers get? |
| Section managers | Secondary | Is this a credible institutional bet? |
| The skeptic | Cross-cutting | Why is this not another single-mission "multimission" tool? |

The audience has heard of TTS by word of mouth and through section-level advocacy. They are
vetting Matt as much as the software.

## 3. The ask

Catalogue inclusion, framed as a three-rung ladder so there is a yes available at every level:

- **Rung A (minimum viable):** TTS listed in the catalogue as available open-source software.
  Delivers institutional endorsement.
- **Rung B (better):** TTS adaptation and sustainment offered as a service line, with the
  libraries as substrate. Delivers endorsement plus a funded reason to grow expertise.
- **Rung C (best):** ROC staffs Systems Teamtools engineers as a standing role offered to
  customer missions. Delivers a body of TTS-fluent engineers at JPL who are hireable by
  external partners buying into the ROC.

## 4. Narrative spine

Approved in grilling, pending Tara's feedback:

1. **The gap.** The GDS tools already scoped do not reach the operator's desk. Ops teams end
   up writing their own tools. Every ROC customer will hit this, exactly as every JPL mission
   does.
2. **What goes wrong.** Those tools are messy, duplicative, and mission-captive. Heritage that
   does not transfer. Tools that die with their author.
3. **The thesis.** A developer-operator ecosystem: spacecraft operators doing devops, with
   real engineering discipline made accessible rather than imposed.
4. **The shape.** Strong central libraries plus thin mission-owned adaptation. Bricks, not tools.
5. **The fit.** That shape *is* a service-center architecture — shared core maintained centrally,
   per-customer adaptation owned by the customer, expertise as the deliverable.
6. **The proof.** Adoption matrix across missions, plus an OCO-2 deep dive.
7. **The ask.** The A/B/C ladder.

The Clipper situation is **not named on any page**. The multimission hazard is argued
structurally in section 2; the audience will make the connection unaided, and Matt handles it
verbally if it comes up.

## 5. Page hierarchy

Hub-and-spoke with numbered prefixes, so the linear read also works.

```
docs/briefings/roc_2026/
├── index.md                      Executive summary — standalone, whole argument
├── 01-the-gap.md                 What scoped GDS does not cover
├── 02-what-goes-wrong.md         Failure modes of ops-written and "multimission" tooling
├── 03-operator-devops.md         The thesis: a developer-operator ecosystem
├── 04-bricks-not-tools.md        Governing principles (subset + pointer to full set)
├── 05-core-and-adaptation.md     The architecture and who owns which layer
├── 06-service-center-fit.md      Structural isomorphism (still ROC-agnostic)
├── 07-adoption-matrix.md         Missions × tools, one view
├── 08-case-study-oco2.md         Deep dive
├── 09-what-it-costs.md           Adoption cost, à-la-carte, no infrastructure
├── 10-sustainment.md             Governance, community, forward plan
├── 11-the-ask.md                 The A/B/C catalogue ladder
└── appendix-a-roc-interfaces.md  Bolt-on: where TTS already meets ROC tooling
```

`index.md` doubles as the outline for Matt's PowerPoint. Anyone who reads only the landing
page still receives the complete argument.

**Merge candidates if the set runs long:** 03+04 (thesis and principles), 05+06 (architecture
and its service-center reading).

## 6. Page specifications

Each page carries: the single claim it makes, the source backing that claim, the visual, and a
seed for what Matt says out loud.

---

### `index.md` — Executive summary

- **Claim:** Scoped GDS leaves the last stretch to the operators; TTS is the ecosystem that
  makes that stretch cheap, shared, and durable — and its shape is already a service-center shape.
- **Source:** `docs/about.md`, `docs/index.md`
- **Visual:** None, or the core/adaptation Mermaid diagram reused small.
- **Length:** ~600 words. Must stand alone.
- **Note seed:** "If you read nothing else, read this page."

### `01-the-gap.md` — What scoped GDS does not cover

- **Claim:** There is a predictable, nameable gap between where ground data systems stop and
  where operators make decisions, and every mission fills it by hand.
- **Source:** `docs/about.md` — "the penultimate three quarters of the last mile"; the explicit
  GDS-complement framing.
- **Visual:** A simple band diagram: GDS → **gap** → operator decision.
- **Note seed:** Name the gap before naming the product. Be generous to GDS — it is not
  failing, it was never scoped for this.
- **Watch:** A GDS stakeholder may be in the room. This page must read as complementary, never
  competitive.

### `02-what-goes-wrong.md` — Failure modes

- **Claim:** Ops-written tooling fails in four repeatable ways, and "multimission" labels
  applied after the fact do not fix any of them.
- **The four failure modes** (settled 2026-08-20):
  1. **Dies with its author.** Knowledge concentrated in one or two people on a subsystem team;
     leaves when they do.
  2. **Multimission by relabelling.** A single-mission tool renamed "multimission" after the
     fact, without the architecture to back the claim.
  3. **Heritage that doesn't transfer (the "potted plant").** Managers assume the ease a prior
     mission achieved carries forward, without accounting for the dependency and platform
     changes underneath. **Concrete example, cleared for use: MSL → M20.** Management expected
     M20 to inherit MSL's efficiencies; the underlying dependencies had moved on, so what looked
     like heritage was technically much harder than expected. Cite generically in the body text
     ("as happened on the transition from one Mars rover mission to the next") and let Matt name
     MSL/M20 verbally if useful — keep the written page mission-agnostic per the doc-set's
     ROC-agnostic posture, but this example is safe to write explicitly since it predates and is
     unrelated to the Clipper situation.
  4. **N missions independently rebuilding the same capability.** The direct cost case for
     de-duplication.
- **Undercurrent, do not editorialize:** modes 1 and 3 together explain *why* maintenance
  headaches concentrate around OS/Python version upgrades — brittle single-subsystem knowledge
  meets unacknowledged dependency drift. This sets up `04`/`05`'s structural answer without
  stating it here.
- **Source:** `docs/training.md` Module 1 — "Single-mission 'multimission' tools", "When
  Heritage Doesn't Count" (potted plant), "Aren't you just reinventing GDS?"; MSL→M20 example
  per Matt, 2026-08-20.
- **Visual:** Four named failure modes, no diagram.
- **Note seed:** This is where the audience's existing scar tissue gets acknowledged.
- **Constraint:** No Clipper, on the page or in the citations.

### `03-operator-devops.md` — The thesis

- **Claim:** The fix is not better tools handed down to operators; it is an ecosystem in which
  operators can do devops themselves, with discipline made accessible.
- **Source:** `docs/about.md` — "we eat our own dog food", operators first and software
  engineers second; `docs/training.md` Operator-Developer curriculum; `collaboration/ci_cd_policy.md`
  and `collaboration/testing.md` as evidence the discipline is real and enforced.
- **Visual:** Optional — the six-module training curriculum as a list.
- **Note seed:** This is the sentence Matt already argued to line management. It is the
  conceptual centre of the whole briefing.
- **One paragraph, AI-readiness dividend (added 2026-08-20):** Structure pays a second dividend —
  because the deterministic tools are typed and disciplined, agents can be layered on safely,
  constrained to surfacing context rather than asserting spacecraft state (see
  `oco2_documentation/AGENTS.md`'s guardrails as the working example). Add one paragraph that TTS
  is prototyping AI skills to stand up a *working draft* of a new mission's TTS adaptations with
  minimal effort — source: `tts_genai_utils/src/tts_genai_utils/ai_skills/tts_day_0_adaptation.md`.
  Keep it to one paragraph; do not turn this into an AI pitch page.

### `04-bricks-not-tools.md` — Governing principles

- **Claim:** A small number of design commitments are why TTS adds less complexity than it removes.
- **Content:** Summarise the principles that matter to this audience — *don't build tools, build
  bricks*; *projects manage their own risk*; *accessible anywhere*; *support the little guys too* —
  then point to the full set of eight.
- **Source:** `docs/philosophy.md`; the non-goals in `docs/about.md` (no persistent state, no
  infrastructure ownership, libraries not applications).
- **Visual:** None.
- **Note seed:** "Less complexity than it resolves" is the warm-fuzzy this page must deliver.

### `05-core-and-adaptation.md` — The architecture

- **Claim:** A shared core defines the interfaces; each mission owns a thin adaptation layer;
  neither can break the other.
- **Source:** `docs/architecture.md` (existing Mermaid dependency graph); `CONTEXT.md`
  core/adaptation vocabulary; `WORKSPACE_MAP.md` as the concrete instance.
- **Visual:** **Primary diagram of the doc set.** Mermaid, consistent with the existing site.
  Likely a simplified redraw of `architecture.md` rather than the full graph.
- **Note seed:** *Projects manage their own risk* is the load-bearing principle here, and it is
  the direct answer to the multimission skeptic.

### `06-service-center-fit.md` — Structural isomorphism

- **Claim:** Centrally-maintained core plus customer-owned adaptation plus expertise-as-deliverable
  is precisely how a service centre is organised. The fit is architectural, not marketing.
- **Source:** Derived from 05 plus `collaboration/day_zero_design.md` (the Systems Teamtools Lead
  role and its precedents on M20, Clipper, SRL).
- **Systems Teamtools Lead, defined (settled 2026-08-20):** Today this role exists de facto on
  JPL missions but is rarely named. Its functions: runs the mission's TT Working Group (TTWG) to
  support and educate subsystem team members; is the single point of contact back to the studio
  lead; negotiates core changes on the mission's behalf; navigates a path forward when the
  mission is blocked by the core; and negotiates the boundary between what the GDS covers and
  what TTS covers. This is the person best positioned to understand the GDS/downstream interface
  and give other users vision in that space. Naming this role explicitly, rather than leaving it
  de facto, is itself part of the pitch — it is a role a service centre can staff and standardize
  in a way an individual mission rarely does on its own initiative.
- **Visual:** Side-by-side mapping — architecture layer ↔ service-centre function.
- **Note seed:** Say "service centre", not "ROC". Let them arrive at it. This page is why the
  ask in `11` lands as a discovery rather than a pitch.

### `07-adoption-matrix.md` — Missions × tools

- **Claim:** This is already in production across the portfolio, not a proposal.
- **Source:** The "Projects Currently Supported" section of each of the 14 pages in
  `docs/repositories/`.
- **⚠ Known unreliable — Matt confirmed on 2026-08-20.** The published lists mix confirmed
  current use, aspirational entries Matt wrote as an educated guess about what a mission *would*
  use, and "if the mission finished migrating off its prototype" projections. This is not a
  briefing-day fix — the spec should track it as ongoing source-of-truth maintenance, not a
  blocker (see §8, D7).
- **Visual:** A single matrix, mission identifiers down one axis, TTS libraries across the other,
  labelled candidly — e.g. a footer note: *"Reflects current documentation, which is under active
  correction; treat as directional."*
- **Build note:** Extract from the repository pages as they stand today. Do not attempt to
  independently verify mission-by-mission truth for this briefing — that is out of scope for a
  single grilling/authoring pass and is Matt's ongoing maintenance task.
- **Note seed:** Let the density of the grid do the arguing, but do not overclaim breadth in the
  spoken narration beyond what the page itself is willing to assert.

### `08-case-study-oco2.md` — Deep dive

- **Claim:** OCO-2 is not the broadest TTS adoption (NISAR is, as currently documented) — it is
  the deepest: full-stack TTS, sustained by a 4–5 person team on a twelve-year extended mission.
  State this distinction explicitly on the page.
- **Headline:** "Four to five people fly a twelve-year-old spacecraft."
- **Body arc:**
  1. Team size and tenure (the hook).
  2. What those five people were doing before TTS coverage — the legacy IDL scripts and the
     Maestro HK-script-to-`.npy` pipeline documented in `oco2_documentation/CONTEXT.md` §514
     ("Automation Opportunities") — presented as the same messy, duplicative, single-team-legible
     tooling named generically in `02`, now visibly being replaced by `oco2_query` and friends.
  3. **Full-stack proof points:** a working prototype of sequence modeling, real sequence review
     tooling, and real downlink analysis tooling. **Downlink analysis is not yet reflected in the
     public repository pages** — needs a citation once documented (see §8, D8).
  4. Concrete illustration: the weekly ATS review running through Tower end to end.
- **Source:** `oco2/oco2_documentation/CONTEXT.md` (Teams §17, Automation Opportunities §514,
  ATS Review §163); `oco2/oco2_documentation/AGENTS.md` (deterministic tool roster); the OCO-2
  entries across `docs/repositories/`.
- **Visual:** Optional screenshot, decorative only.
- **Open:** Needs a substantive interview pass with Matt for the sequence-modeling prototype and
  downlink analysis specifics, since neither is documented anywhere in this workspace yet.

### `09-what-it-costs.md` — Adoption cost

- **Claim:** Standing up a new mission adaptation is days of effort, not a procurement, and
  nothing has to be adopted that is not wanted.
- **Source:** `collaboration/day_zero_design.md` — the day-zero adaptations and the "one FTE week"
  figure; `collaboration/install.md` — the concrete bootstrap sequence.
- **Visual:** The day-zero checklist.
- **⚠ Blocked:** `day_zero_design.md` names `tts_query` and `tts_dpp` among the mandatory
  day-zero adaptations, and neither exists in `WORKSPACE_MAP.md` or on disk. The cost claim
  cannot cite that page until this is reconciled. See §8.

### `10-sustainment.md` — Governance and community

- **Claim:** TTS is governed, open source, and backed by a growing developer base, with community
  growth as an active area of work.
- **Source:** `collaboration/governance.md`; `collaboration/licence.md`; the CI/CD and testing policy
  pages as evidence of institutional discipline.
- **Tone constraint:** Honest, not confessional. Acknowledge that community depth is something
  actively being built. Do **not** advertise immaturity, do **not** frame ROC as a funding
  mechanism, do **not** raise Matt's personal bus factor unprompted.
- **Note seed:** If asked directly about key-person risk, answer plainly: not dead in the water,
  but the product suffers, and broadening the contributor base is exactly why institutional
  adoption matters.
- **⚠ Blocked:** `governance.md` has a placeholder discussion link and committer profile URLs
  pointing at an unrelated GitHub account. Must be fixed before anyone follows the citation.

### `11-the-ask.md` — The catalogue ladder

- **Claim:** There are three levels of inclusion, each with a defined deliverable and a defined
  cost to ROC.
- **Content:** Rungs A, B, C from §3, each with: what ROC lists, what ROC staffs, what the
  customer receives.
- **Rung C, concrete (settled 2026-08-20):** the deliverable is a **pooled-at-ROC, part-time
  embedded Systems Teamtools Lead per customer during adaptation** — see the role definition in
  `06`. First-year outcome: a working mission adaptation of the day-zero libraries, plus a
  trained customer-side operator-developer able to carry it forward. Frame this explicitly as a
  **capability transfer**, not an ongoing dependency — it pre-empts the "so we're hiring you
  forever" objection. *(Matt's numbers, not yet confirmed against §3's ladder — flag for his
  review before this goes final.)*
- **Visual:** Three-column ladder.
- **Note seed:** Make it easy to say yes to A today and grow to C.

### `appendix-a-roc-interfaces.md` — ROC bolt-on

- **Claim:** Map TTS tools against the GDS tooling expected to be offered by the ROC, and name
  where TTS already has a real connection to ROC-relevant infrastructure versus where the
  connection is prospective.
- **⚠ Fact check, 2026-08-20 — F-Prime is NOT a real interface today.**
  `docs/reference_project/fprime.md` states the DemoSat F-Prime build is "at the moment mostly
  aspirational... just a twinkle in our eyes." There is no delivered TTS↔F-Prime connection
  anywhere in this workspace. If F-Prime appears on this page, it must be labelled prospective,
  not as a proven past interface.
- **RML:** No RML material exists anywhere in the workspace. Purely a fact Matt must supply.
- **⚠ Blocked, new task:** baseline Mission Control System (MCS) for the ROC is unknown to this
  workspace — YAMCS is suspected but unconfirmed. Add a task: *determine the ROC's baseline MCS*
  before this page is written, since the whole page is organized around what that MCS is.
- **Fallback per Matt's Q27 guidance:** if the real interfaces turn out thin, cut this page
  rather than pad it, and close `11` instead with an offer to run a joint scoping session.

## 7. User stories

**ROC architect**
- As a ROC architect, I want to see where TTS sits relative to GDS so I can tell whether it
  overlaps anything already scoped. → `01`, `05`
- As a ROC architect, I want to know what infrastructure TTS requires so I can assess what I
  would be taking on. → `04`, `09`
- As a ROC architect, I want to understand how one customer's changes are isolated from another's
  so I can judge multi-tenancy risk. → `05`

**Program office**
- As a program office lead, I want a defensible cost of adoption per customer mission so I can
  price a catalogue entry. → `09`
- As a program office lead, I want to know who maintains this in five years so I can assess
  dependency risk. → `10`
- As a program office lead, I want to know what we would be staffing and what the customer
  receives for it. → `11`

**Skeptic**
- As someone burned by multimission tooling, I want the failure mode named accurately before I
  am told this is different. → `02`
- As a skeptic, I want evidence of adoption across missions that I can verify. → `07`, `08`

**Section manager**
- As a section manager, I want a one-page version I can forward. → `index.md`

**Matt**
- As the presenter, I want a landing page whose structure survives being pasted into a deck. → `index.md`
- As the presenter, I want every claim traceable to a doc I can open live if challenged. → all pages

## 8. Prerequisite debts

These are documentation defects found while surveying. Each one is reachable by a citation this
briefing wants to make.

| # | Debt | Blocks | Severity |
|---|---|---|---|
| D1 | `day_zero_design.md` names `tts_query` and `tts_dpp` as mandatory day-zero adaptations; neither repo exists | `09` | High — the cost claim rests on it |
| D2 | `governance.md` has a placeholder discussion link and committer URLs pointing at an unrelated account | `10` | High — undercuts the page it supports |
| D3 | `repositories/tts_data_utils.md` still describes `DataContainer`; the repo has pivoted to `TtsDataFrame` | `07` | Medium |
| D4 | Repo count is inconsistent across sources (~25 / 14 / 16 / 14 nav entries) | `07`, `index` | Medium — pick one number and use it everywhere |
| D5 | Stub pages in the nav: `fudamental_concepts.md`, `style_primer.md`, `documentation.md`, `releases.md` | Any live click-through | Low, but visible |
| D6 | Repos on disk absent from nav and architecture diagram: `tts_events`, `tts_ci_cd`, `tts_infrastructure`, `tts_deployments`, `tts_genai_utils` | `05`, `07` | Low |
| D7 | Adoption matrix (`07`) mixes confirmed use, aspirational guesses, and "if migration finished" projections — Matt confirmed this is not reliable as published | `07` | Acknowledged, not blocking — ongoing maintenance, see note on `07` above |
| D8 | OCO-2's real downlink analysis tooling is not reflected in any repository page | `08` | Medium — needed for the full-stack claim |
| D9 | ROC's baseline Mission Control System is unknown (YAMCS suspected, unconfirmed) | `appendix-a` | High — page cannot be organized without it |

**D1 and D2 are pre-briefing blockers per Matt's direction (2026-08-20) — resolve as tickets
before any page authoring begins, tracked as a blocking milestone ahead of the doc-set build.**
D3–D6 can be footnoted. D7 is explicitly non-blocking. D8 and D9 block only their specific page
and should be resolved during authoring of `08` and `appendix-a` respectively.

## 9. Technical notes

- **Not in TOC:** mkdocs 1.6.1 is installed. Pages under `docs/` that are absent from `nav` still
  build and are reachable by URL. Add `not_in_nav: briefings/*` to `mkdocs.yml` to suppress the
  build warning. No other config change needed.
- **Diagrams:** Mermaid, via the already-installed `mkdocs-mermaid2-plugin`, consistent with
  `architecture.md`.
- **PDF:** Achievable with pypandoc + `/Library/TeX/texbin/pdflatex` — this path produced
  `msr_proposal.pdf` on this machine in March, but `pandoc` is not currently on PATH and needs
  re-provisioning.
- **PPTX:** Out of scope. Pandoc's pptx output would be worse than what Matt builds by hand from
  `index.md`, and templating it is a rabbit hole.

## 10. Open questions

All rounds 1–3 questions are now settled except:

- **Q9 follow-up.** Tara's read on the narrative spine — the reason for today's conversation.
- **Appendix A facts.** Which real TTS↔ROC-adjacent tool interfaces exist, at what level, and
  where documented (if anywhere) — pending Matt, plus the new baseline-MCS task (D9).
- **Case study interview.** Sequence-modeling prototype and downlink analysis tooling specifics
  for `08`, neither yet documented in this workspace (D8).
- **Rung C numbers.** The pooled/part-time embedded staffing model in `11` is my synthesis of
  Matt's Q24 answer — needs his confirmation it matches what he actually wants to propose.

Carried as accepted (no further round needed): Q15 print the cost figure, Q16 hub-and-spoke
400–800 words/spoke, Q17 mkdocs canonical + pandoc PDF + no PPTX, Q18 keep load-bearing
metaphors, Q19 keep all 13 pages unmerged, Q20 publish as-documented with a candour footnote and
track true-state correction separately, Q21 no page-level hedge needed, Q22 full-stack headline,
Q23 the four failure modes above, Q25 one AI-readiness paragraph in `03`, Q26 D1/D2 as tickets
before authoring.

## 11. For the conversation with Tara

Decisions where a section manager's read is worth more than mine:

1. **Is the spine right?** Lead with the gap in scoped GDS, land on "operators doing devops",
   close on the catalogue ladder. Does that survive contact with how the ROC actually talks?
2. **How high do we reach?** Rung C — ROC staffing Systems Teamtools engineers — is the outcome
   worth having. Is it too much to put on the page in a first briefing, or does anchoring high
   make B easy?
3. **Sustainment posture.** How honest is honest? The plan is to say community depth is actively
   being built, without volunteering the key-person risk. Is that the right line for a program
   office that is deciding whether to depend on us?
4. **The Clipper silence.** Nothing on the page; handled verbally if raised. Is Tara comfortable
   with that, and does she know anything about the room that would change it?
5. **Cost figure.** Is "roughly one FTE week to stand up a mission adaptation" a number the
   section is willing to see quoted back to it?
6. **Appendix A.** Who actually knows where TTS has already touched ROC-inherited tooling? That
   material does not exist in any repo here. Matt directed (2026-08-20) that this become a
   GDS-tool mapping plus a named task to determine the ROC's baseline MCS — worth flagging to
   Tara as an open technical question, not just a documentation gap.
7. **Rung C staffing model.** Pooled at ROC, embedded part-time per customer, deliverable framed
   as capability transfer rather than dependency. Does this match what Matt wants to propose, or
   does Tara have a different staffing model in mind from how the ROC already sources engineers?

---

**Housekeeping:** `teamtools_documentation` is currently on `main` with an uncommitted change to
`docs/collaboration/roadmap.md` — homeless WIP by your own `tts-git-hygiene` definition. Worth
landing somewhere before a briefing branch gets cut.
