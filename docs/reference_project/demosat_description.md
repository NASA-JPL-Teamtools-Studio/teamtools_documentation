# Introducing DemoSat

![DemoSat logo](https://github.com/NASA-JPL-Teamtools-Studio/teamtools_documentation/raw/main/docs/images/tts_image_artifacts/demosat.png)

DemoSat is a minimal example of a cartoon spacecraft to more realistically demonstrate the capabilities of the Teamtools Studio. Because of our architectural decisions to maximize extensibility and portability, the core libraries for FRESH, Tower, Dexter, Dante and difficult to parse and understand how to use. Within JPL we have several missions that extend each, but in order to demonstrate to developers who are not at JPL (or even JPLers who just don't have access to all those adaptations due to project security postures), we have created adapations of several TTS libraries for DemoSat. See [DemoSat Adaptation Libraries](demosat_libraries.md) for more specifics on the work that has been done there.

# Overview

DemoSat is loosly inspired by the SMAD FireSat example. We even considered calling it FireSat until we had a look back at SMAD and realized that it never really gets all that deep into operating the fictional spacecraft.

DemoSat is a sun syncronous low Earth orbiter with a single instrument that mostly points nadir. It can also point to targets on the surface of the Earth, at the Sun, at the moon, or at a handful of bright stars.

It is not meant to be an impressive example of spacecraft systems engineering, but is rather the "just enough" solution to demonstrate how our products work without needing a real spacecraft in the loop as was required before the DemoSat project was defined.

---
<a href="https://github.com/NASA-JPL-Teamtools-Studio/teamtools_documentation/blob/main/docs/reference_project/demosat_description.md" target="_blank" rel="noopener noreferrer">Edit/Comment on GitHub</a>
