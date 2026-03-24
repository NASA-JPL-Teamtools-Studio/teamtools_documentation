# Design Philosophy

In order to have as coherent a product as possible, the Teamtools Studio has made several high-level design philosophies that give this suite the character that it has. If you want to know what we feel we take ownership of and what you would have ownership of should you choose to extend our work, this is a good place to start. More specific choices are noted elsewhere in the COLLABORATION section below. This section is meant to be more of a narrative of why we do things the way we do them, and less exactly what we do or how we do it.

## Don’t build tools. Build bricks
> **Rationale** The more specific the solution, the less likely it will be useful to other projects. We will never be as imaginative as the community as a whole. We are here to enable complete solutions, not to deliver them.
> 
> **Design Influence** Split out libraries to be as atomic as feasible. Missions get to take everything they want and don’t have to leave things behind because they’re attached to things they don’t want.

## Purely Python when Practical
> **Rationale** Limit technical diversity to maximize pool of studio developers and customer base. Python is the most popular language among operators and likely will be for some time.
> 
> **Design Influence** Some tools have other components under the hood (JavaScript in html_utils). But end users should see only Python wherever possible.

## Projects manage their own risk
> **Rationale** No one will want to use this stuff if they feel like we’re tying their hands. People closest to the risk should always make the assessment of it. That is not TTS even though individual TTS developers may be on a project where they assess risk.
> 
> **Design Influence** Drives architecture choices, drives use of Python for its very strong extensibility via Abstract Base Classes and similar. Drive ssupport of older Python versions.

## Accessible anywhere
> **Rationale** Tools that are available as CLI should be written such that their functionality is as easily accessed via library.
> 
> **Design Influence** Avoids users writing bad command line parsers, maintains pythonic data structures throughout and avoids loss of data. Allows tools ostensibly built for the command line to be leveraged in larger libraries or web apps.

## Support the little guys, too
> **Rationale** Small missions have long been a place where young and inexperienced engineers flounder without much help. At the same time, they usually have much more flexible risk postures than flagships, meaning that a talented mid-career or senior engineer could make progress with less red tape while also being present to mentor more junior colleagues.
> 
> **Design Influence** Support older Python versions, keep tools portable enough not to require cloud resources. Allow very simple deployment with just Python venvs

## Make them know who you are
> **Rationale** There’s a lot here, and it would be easy for people using TTS tools in disparate places to not know it
> 
> **Design Influence** Drives branding in reporting, logos, library naming (e.g. tts-library-name), dedicated GitHub Organization


---
<a href="https://github.com/NASA-JPL-Teamtools-Studio/teamtools_documentation/blob/main/docs/philosophy.md" target="_blank" rel="noopener noreferrer">Edit/Comment on GitHub</a>