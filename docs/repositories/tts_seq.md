# Teamtools Studio Seq

![Project logo](https://github.com/NASA-JPL-Teamtools-Studio/teamtools_documentation/raw/main/docs/images/tts_image_artifacts/tts_seq.png)

### Overview

TTS Seq is the central library for interacting with command sequences at JPL. It includes IO methods for common sequencing languages including 
SeqJSON, .seq, RML, and SCR. VML is not currently supported, but that contribution would be very much welcomed.

TTS Seq also includes classes for managing collections of sequences, usually most important for modeling the state of sequences currently
onboard a spacecraft or expected to be onboard at a given moment.

Finally, TTS Seq also includes a simulation engine for simulating the state of a spacecraft given a particular sequence load. It is 
currently fairly modest and only appropriate for relatively simple simulations, but it is currently being expanded.

### Projects Currently Supported

* DemoSat
* Orbiting Carbon Observatory 2 (OCO-2)
* NISAR

## Architecture

### TTS dependencies

* TTS Dicitonary Interface
* TTS Utilities
* Data Utilities
* HTML Utilities

---
**Repository Links:** <a href="nasa-jpl-teamtools-studio.github.io/NASA-JPL-Teamtools-Studio/tts_seq/" target="_blank" rel="noopener noreferrer">Docs</a> | <a href="github.com/NASA-JPL-Teamtools-Studio/tts_seq/issues" target="_blank" rel="noopener noreferrer">Issues</a> | <a href="github.com/NASA-JPL-Teamtools-Studio/tts_seq" target="_blank" rel="noopener noreferrer">Source</a>