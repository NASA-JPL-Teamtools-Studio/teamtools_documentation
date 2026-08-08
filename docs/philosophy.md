# Design Philosophy

In order to have as coherent a product as possible, the Teamtools Studio has made several high-level design philosophies that give this suite the character that it has. If you want to know what we feel we take ownership of and what you would have ownership of should you choose to extend our work, this is a good place to start. More specific choices are noted elsewhere in the COLLABORATION section below. This section is meant to be more of a narrative of why we do things the way we do them, and less exactly what we do or how we do it.

## Don’t build tools. Build bricks
> **Rationale** The more specific the solution, the less likely it will be useful to other projects. We will never be as imaginative as the community as a whole. We are here to enable complete solutions, not to deliver them.
> 
> **Design Influence** Split out libraries to be as atomic as feasible. Missions get to take everything they want and don’t have to leave things behind because they’re attached to things they don’t want.

## Purely Python when Practical
> **Rationale** Limit technical diversity to maximize pool of studio developers and customer base. Python is the most popular language among operators and likely will be for some time.
> 
> **Design Influence** All TTS work must be pip-installable. Development internals should use Python unless: (a) a non-Python technology is self-contained and clearly more powerful than a Python alternative, or (b) building a Python equivalent would be prohibitively complex. Non-Python compiled libraries (e.g., C/C++ under the hood via packages like NumPy) are acceptable and sometimes even desirable for performance. JavaScript for web interactivity is the canonical acceptable exception — it cannot be done practically in Python. The developer-facing API must always be Python.

## Be mindful of the resources that your code touches
> Testing and maintenance will go much better if you can run your software from anywhere. Of course for space missions this will never fully be the case as you will need to access mission resources like telemetry data stores, which can very rarely be containerized in meaningful ways. However, avoid the trap of writing mission-specific resources too deeply in your tech stack. To the maximum extent possible, try to architect so the logic that truly needs to touch mission resources (with their access controls and limited access from non-mission machines) such that they can be replaced by a mock in a unit test or develpment areas. This can be as simple as leveraging the patters in `tts_data_utils` to build tests around CSVs instead of database calls that create tabular Pandas data. It will feel like extra work when you need to do it, but it will repay on 10x in risk reduction via reduction of technical debt and the portability of your tools.

## Projects manage their own risk
> **Rationale** No one will want to use this stuff if they feel like we’re tying their hands. People closest to the risk should always make the assessment of it. That is not TTS even though individual TTS developers may be on a project where they assess risk.
> 
> **Design Influence** Drives architecture choices, drives use of Python for its very strong extensibility via Abstract Base Classes and similar. Drives support of older Python versions. Missions may diverge from TTS core — we do not preclude this, but we do not recommend it. Semantic versioning is the primary mechanism for communicating breaking changes across the ecosystem. A planned `tts_ci_cd` tool will allow missions to interrogate their adaptation layers for divergence from TTS core, both to surface upgrade paths and to identify mission-developed improvements that deserve to be contributed back.

## Accessible anywhere
> **Rationale** Tools that are available as CLI should be written such that their functionality is as easily accessed via library.
> 
> **Design Influence** Avoids users writing bad command line parsers, maintains pythonic data structures throughout and avoids loss of data. Allows tools ostensibly built for the command line to be leveraged in larger libraries or web apps.

## Support the little guys, too
> **Rationale** Small missions have long been a place where young and inexperienced engineers flounder without much help. At the same time, they usually have much more flexible risk postures than flagships, meaning that a talented mid-career or senior engineer could make progress with less red tape while also being present to mentor more junior colleagues.
> 
> **Design Influence** Support older Python versions, keep tools portable enough not to require cloud resources. Allow very simple deployment with just Python venvs. The current floor is Python 3.6.8, chosen because some missions cannot easily upgrade due to operating system constraints (e.g., RHEL7, Solaris). Where a modern Python feature provides significant value and a 3.6.8-compatible alternative exists, prefer the alternative. Where no viable alternative exists, the newer feature may be used and 3.6.8 users must rely on a modern venv. An ADR is planned to formalize when and how the version floor will be raised.

## Make them know who you are
> **Rationale** There’s a lot here, and it would be easy for people using TTS tools in disparate places to not know it. This page is as much a manifesto as it is a technical guide — new projects should trust that we’ve encountered many common pitfalls in this space and have deliberate solutions for them. Visibility into where TTS is being used and the value it provides is essential to the studio’s continued investment and growth.
> 
> **Design Influence** Drives branding in reporting, logos, library naming (e.g. tts-library-name), dedicated GitHub Organization


## Prefer open source over SaaS
> **Rationale** A SaaS vendor can be acquired, change pricing, or go offline. Institutional security environments may block external data uploads entirely. TTS must work on small missions with minimal IT infrastructure and on flagship missions with strict software controls — a tool that requires cloud access fails in both. Interaction with SaaS products by projects extending TTS should not be excluded per the **Projects manage their own risk** philosophy above, but none should be required.
>
> **Design Influence** When open-source tooling exists for a need, use it. When it doesn't, build a minimal version rather than adopting a SaaS dependency. See `docs/adr/001-open-source-over-saas.md` for the specific decision on visual regression tooling. This principle is active — future contributors and agents should apply it to any new CI tool, testing library, or reporting dependency.

## Discoverability
> **Rationale** Magic procedure steps — things humans "just have to know" — create barriers to contribution, cause errors when steps are forgotten, and are invisible to AI agents. The right behavior should be easy to find. The wrong behavior should be hard to do accidentally. This is as true in sofware development as it is in spacecraft operations. Complex systems will necessarily have more human minds devoted to them in implementation phases than ops, sustainment, and maintenance. Posturing ourselves explicitly towards discoverability helps overcome the common pitfalls in later phases of JPL missions.
>
> **Design Influence** Error messages must tell you what to do next, not just what went wrong. Status dashboards and reports surface what needs attention without requiring the user to know where to look. Code structures that enforce constraints are preferred over documentation-only rules. APIs and CLI tools are self-describing wherever possible. Currently, structural enforcement of this principle lives primarily in agent instruction files (e.g., `CONTEXT.md`, `AGENTS.md`). An ADR is planned to evaluate whether automated auditing tools in `tts_ci_cd` are needed to enforce discoverability requirements structurally rather than documentarily.

---
<a href="https://github.com/NASA-JPL-Teamtools-Studio/teamtools_documentation/blob/main/docs/philosophy.md" target="_blank" rel="noopener noreferrer">Edit/Comment on GitHub</a>
